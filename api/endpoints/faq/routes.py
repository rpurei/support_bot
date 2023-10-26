from config import DEBUG_MODE, APP_LOG_ERROR, APP_LOG_INFO, DP_DATA_PATH, DP_ROOT_PATH, CLASS_BORDER
from endpoints.utils import http_exception
from app_logger import logger_output
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status
from datetime import datetime
from deeppavlov import configs, train_model
from deeppavlov.core.common.file import read_json


router = APIRouter(
    prefix='/faq',
    tags=['FAQ'],
    responses={404: {'detail': 'Not found'}},
)

model_config = read_json(configs.faq.tfidf_autofaq)
model_config['dataset_reader']['x_col_name'] = 'Q'
model_config['dataset_reader']['y_col_name'] = 'A'
model_config['dataset_reader']['data_path'] = DP_DATA_PATH
model_config['dataset_reader']['data_url'] = None
model_config['metadata']['variables']['ROOT_PATH'] = DP_ROOT_PATH
faq = train_model(model_config)


async def data_processing(data: dict):
    generated_text = faq([data.get('message', '')])
    logger_output(f'Q: {str(data)} A: {str(generated_text)}', DEBUG_MODE, APP_LOG_INFO)
    return generated_text[0] if float(generated_text[1][0]) > CLASS_BORDER else f'Пока не знаю ответа на Ваш вопрос, попробуйте задать его по-другому'


@router.websocket("/ws")
async def faq_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_json()
            message_processed = await data_processing(data)
            await websocket.send_json({'message': message_processed,
                                       'time': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
                                       'side': 'bot'})
        except WebSocketDisconnect:
            break
        except Exception as exc:
            http_exception(str(exc), APP_LOG_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR)
