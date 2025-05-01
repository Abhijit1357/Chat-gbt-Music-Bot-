# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API details
API_ID = os.getenv('API_ID', '22834593')  # Replace with your API_ID
API_HASH = os.getenv('API_HASH', 'f400bc1d1baeb9ae93014ce3ee5ea835')  # Replace with your API_HASH
BOT_TOKEN = os.getenv('BOT_TOKEN', '6666555316:AAHT6ObREaHwIsowFiH2UFd6kkSaRfFFiQs')  # Replace with your BOT_TOKEN

# Logger ID (for logging messages in channels/groups)
LOGGER_ID = os.getenv('LOGGER_ID', '-1002134425165')  # Replace with your Logger Channel ID

# MongoDB URI for database connection
MONGO_DB_URI = os.getenv('MONGO_DB_URI', 'mongodb+srv://AOMusic:AOMusic@cluster0.sibxiqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # Replace with your Mongo URI

# Owner's User ID (for admin privileges)
OWNER_ID = os.getenv('OWNER_ID', '6148346742')  # Replace with your Owner's User ID

# String session for user login to Telegram Client
STRING_SESSION = os.getenv('STRING_SESSION', 'BQFcbaEAj5NxCIU8FfUh9yTyJRus2cfcOENDLt3S5cBzU3GRdgEqu0aJsF830bwGDESnbk_9PHKwEDs8YQRvhbmvdxC71xZhJ34915RUl40FZkR3jhneWNkUEw_JAg0j_IMQb0tL3AtQme9Cn5jSFS5ixsJf_AMaGGkG8akwX69OJYO3-sgfxvKPT31aidz2OlS7IPTq842EdoioQTka8mxsLVgr8e7IrbZVMN-TJ5oPrEGrK8qfoLxlOjjO96IOoxDQOkUQ3zVUkArr02jB3CYPeZeB8zQqaS0xg3n-E2rq6VgeSEdlGOXIm29hhM_xk3wASEd69HIk9YU2TLofnzRR7hBxXwAAAAF5c5ovAA')  # Replace with your String Session
