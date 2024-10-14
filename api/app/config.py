import os

class Config:
    API_V1_PATH = "/api/v1"
    FIRESTORE_EMULATOR_HOST = os.getenv('FIRESTORE_EMULATOR_HOST')
    GCLOUD_PROJECT = os.getenv('GCLOUD_PROJECT')
    FIRESTORE_DB_NAME = os.getenv('FIRESTORE_DB_NAME')
