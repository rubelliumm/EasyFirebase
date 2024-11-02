# EasyFirebase
a easy implementation of Firebase in django application.

#installation
Download the tar file and run the following command in django environment.
```python
  pip install ./EasyFirebase.tar.gz
```
#Settings.py
Get your firebase json config file and info from firebase console.Put the following code in your projects settings.py

```python
  import firebase_admin
  from firebase_admin import credentials

  FIREBASE_CONFIG = {
      "apiKey": "your api key",
      "authDomain": "your domain name",
      "databaseURL": "your databaseURL",
      "projectId": "your projectID",
      "storageBucket": "your storageBucket",
      "messagingSenderId": "your messagingSenderId",
      "appId": "your app id",
      "measurementId": "your measurementId",
  }
  
  FIREBASE_CREDENTIALS_FILE = (
      BASE_DIR / "path/to/your/firebase/config/file.json"
  )
  
  
  # Initialize the Firebase Admin SDk
  cred = credentials.Certificate(
      BASE_DIR / "path/to/your/firebase/config/file.json"
  )
  
  firebase_admin.initialize_app(
      cred,
      {
          "databaseURL": FIREBASE_CONFIG["databaseURL"],
          "storageBucket": FIREBASE_CONFIG["storageBucket"],
      },
      name="name of your app",
  )
```

#Usage
```python
  from EasyFirebase.models import FirebaseModel
  from EasyFirebase.fields import FirebaseImageField

  class MyModel(FirebaseModel):
    name = models.CharField(max_length=100)
    #...
    photo = models.FirebaseImageField()
```
