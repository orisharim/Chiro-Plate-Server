
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate(r'C:\Users\ori\Documents\Programming\FirebaseKeys\chiro-plate-key.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# data = {"user_id": 331661322, "user_password" : 'zigger123', "level 1 start time": "0", "level 1 stars": "0"}


# # Add a new doc in collection 'cities' with ID 'LA'
# db.collection("users").document('331661322').set(data)

doc_ref = db.collection("users").document("331661322")
doc = doc_ref.get()
print(doc.to_dict())

