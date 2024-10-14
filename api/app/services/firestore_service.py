import google.cloud.firestore
from config import Config

config = Config()

if config.FIRESTORE_EMULATOR_HOST:
    # エミュレータに接続
    db = google.cloud.firestore.Client(project=config.GCLOUD_PROJECT)
else:
    # 本番FireStoreに接続
    db = google.cloud.firestore.Client(database=config.FIRESTORE_DB_NAME)