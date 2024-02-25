import firestore_admin
from firestore_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {
    "task": "Hello WOrld",
    "number": "dsadsa"
}

doc_ref = db.collection('expenses').document()
doc_ref.set(data)