import os
from decouple import config

DEBUG = config('DEBUG', cast=bool, default=True)
DATABASE_URL = config('DATABASE_URL', default='sqlite://')
OPERATION_TIME_RANGE = config('OPERATION_TIME_RANGE', default='06:00|00:00')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIGRATIONS_FOLDER = os.path.join(BASE_DIR, "migrations")
BUCKET_NAME = config('AWS_BUCKET')
S3_KEY = config('AWS_S3_KEY')
S3_SECRET = config('AWS_S3_SECRET')
S3_REGION = config('AWS_REGION')
RECORDING_FOLDER = config('RECORDING_FOLDER', default='$HOME/recordings')
