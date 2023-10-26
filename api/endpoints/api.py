from .faq.routes import router as faq_router
from fastapi import APIRouter

router = APIRouter(prefix='/api')
router.include_router(faq_router)


@router.get('/')
async def root():
    return {'message': 'ChatBot API online!'}
