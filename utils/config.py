import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
EMAILS_PATH = 'data/emails.csv'
WAREHOUSE_PATH = 'data/warehouse.csv'
PRODUCTION_DEADLINE = '15/4/2025'
