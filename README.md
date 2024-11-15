# EasyFirebase

An easy implementation of Firebase in django application.
If you do not want to upload your static files (ex: Image, pdf etc.) to the server then you can use easyfirebase to upload all of your static files to Firebase and easyfirebase will do the rest. Updating your file on updating models, deletions of file while you delete your model object or changes the file etc.

## Usage

```python
  from easyfirebase.fields import FirebaseImageField
  from easyfirebase.storage import FirebaseStorage

  class MyModel(models.Model):
    name = models.CharField(max_length=100)
    #...
    photo = models.FirebaseImageField(storage=FirebaseStorage, ... )
```

If you do not provide any parameter for storage, then easyfirebase will use Default Django storage, which will store your image/pdf files in the local/server root dir or upload dir provided by STATIC_ROOT.

## Installation

```python
  pip install easyfirebase
```

Or,

Download the tar file and run the following command in django environment.

```python
  pip install ./easyfirebase.tar.gz
```

add the app name in the `settings.py` of project.

```python
  INSTALLED_APPS = [
    ...
    'easyfirebase',
    ...
    ]
```

## Configure Settings.py

Get your firebase json config file and info from firebase console. Write the following code in your projects `settings.py` file:

```python

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
      BASE_DIR / "name-of-your-firebase-json-file-in-project-root.json"
  )
```

### Steps to Get Firebase Config Data:

    Go to the Firebase Console:
        Visit [Firebase Console](https://console.firebase.google.com/).

    Create or Select a Project:
        If you don’t have a Firebase project yet, click on "Add project" and follow the steps to create one.
        Select an existing project if you already have one.

    Add a Web App:
        Click the gear icon in the top-left corner and select Project settings.
        Navigate to the General tab.
        Under "Your apps," click Add app and select the Web icon (</>).

    Register the App:
        Enter the name of your app (e.g., MyWebApp) and click Register app.

    Get the Config Object:
        After registration, Firebase will show you a code snippet that includes your Firebase Config Data:

      const firebaseConfig = {
        apiKey: "YOUR_API_KEY",
        authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
        projectId: "YOUR_PROJECT_ID",
        storageBucket: "YOUR_PROJECT_ID.appspot.com",
        messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
        appId: "YOUR_APP_ID"
      };
    
    

Copy this object and paste it in the `settings.py` in the project directory.

### Steps to Get the Service Account Key:

    Go to the Firebase Console:
        Visit [Firebase Console](https://console.firebase.google.com/).

    Select a Project:
        Click on the project you want to integrate with your Python app or create one.

    Navigate to Project Settings:
        Click the gear icon in the top-left corner and select Project settings.

    Go to the Service Accounts Tab:
        In the Project settings, click on the Service accounts tab.

    Generate the Key:
        Click Generate new private key.
        Confirm to download the JSON file. This file contains your Service Account Key.

    Store the File Securely:
        Save the file in a secure location within your project directory, e.g., firebase-key.json.

[optional]

```python
# settings.py

FIREBASE_DEFAULT_UPLOAD_DIR = "test_dir"
```

This will set the default upload directory for all FirebaseImageField instances in the Firebase Storage. If not provided, easyfirebase will first try to set the `Project_name` as the default upload dir in the Firebase Storage.
or if the above also fails, `FreeDjangoFirebase/` will be the default upload dir.

Note: You must put your FIREBASE_CONFIG in `settings.py` and put your firebase sdk json file in the `BASE_DIR` of the project. ie, in the directory where `settings.py` resides and FIREBASE_CREDENTIALS_FILE = ... as described above in `settings.py`.
