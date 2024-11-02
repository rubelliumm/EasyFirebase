from datetime import timedelta
from uuid import uuid4
from firebase_admin import db, get_app, storage, credentials, initialize_app
from django.conf import settings

BASE_DIR = settings.BASE_DIR
FIREBASE_CREDENTIALS_FILE = settings.FIREBASE_CREDENTIALS_FILE
FIREBASE_CONFIG = settings.FIREBASE_CONFIG


############################################
def init_app():
    cred = credentials.Certificate(BASE_DIR / FIREBASE_CREDENTIALS_FILE)
    initialize_app(
        cred,
        {
            "databaseURL": FIREBASE_CONFIG["databaseURL"],
            "storageBucket": FIREBASE_CONFIG["storageBucket"],
        },
    )


init_app()


# root_ref = db.reference(app=app)
RTDB_REF = db.reference(url=settings.FIREBASE_CONFIG["databaseURL"])
bucket = storage.bucket(name=settings.FIREBASE_CONFIG["storageBucket"])


def joinFirebaseNodeUrl(*args):
    return "/".join([str(url).strip("/") for url in list(args)])


def uploadFromFile(file, dest_folder="Images"):
    uid = uuid4()
    blob_uri = joinFirebaseNodeUrl(dest_folder, str(uid))
    blob = bucket.blob(blob_uri)
    blob.upload_from_file(file, content_type="image/jpeg")
    return str(uid)


# @apply session/cache func.
def getUrl(uid, dest_folder="Images"):
    blob = bucket.blob(joinFirebaseNodeUrl(dest_folder, str(uid)))
    download_url = blob.generate_signed_url(expiration=timedelta(minutes=2))
    return download_url


def deleteUid(uid, dest_folder="Images"):
    blob = bucket.blob(joinFirebaseNodeUrl(dest_folder, uid))
    if blob.exists():
        blob.delete()
    else:
        print(f"No file found with id {uid}")
