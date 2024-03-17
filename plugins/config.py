import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6504389382:AAGiqASARUii1dxNQx0kH26mg8t3j6m2uwI")
    
    API_ID = int(os.environ.get("API_ID", "16732227"))
    
    API_HASH = os.environ.get("API_HASH", "8b5594ad7ad37f3a0a7ddbfb3963bb51")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ash:Movie123@cluster0.vfchgu0.mongodb.net/cluster0?retryWrites=true&w=majority")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002017073784"))
    
    LOGGER = logging
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5868426717"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "gbvddssggtbot")
                                  
