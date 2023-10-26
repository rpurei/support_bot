LOG_FOLDER = './logs'
LOG_FORMAT = '%(asctime)s [%(levelname)s] %(name)s : (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
LOG_FILE = 'app.log'
LOG_MAX_BYTES = 1048576
LOG_COUNT = 10

APP_PORT = 3000
APP_HOST = 'localhost'

APP_LOG_ERROR = 0
APP_LOG_WARN = 1
APP_LOG_INFO = 2

DEBUG_MODE = True

DP_ROOT_PATH = '/var/www/chatbot/api/.deeppavlov'
DP_DATA_PATH = '/var/www/chatbot/api/dataset/faq_qa.csv'
CLASS_BORDER = 0.1
