import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')


DOWNLOADING_DIR = 'downloadings'
VIDEOS_DIR = os.path.join(DOWNLOADING_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADING_DIR, 'captions')
