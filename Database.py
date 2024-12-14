from User import User
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# data = {"user_id": 331661322, "user_password" : 'zigger123', "level 1 start time": "0", "level 1 stars": "0"}
class Database:

    def __init__(self, db_key: str):
        self.cred = credentials.Certificate(db_key)
        self.app = firebase_admin.initialize_app(self.cred)
        self.client = firestore.client()

    def get_user(self, user_id: int) -> User:
        user_ref = self.client.collection("users").document(str(user_id))
        user_info = user_ref.get().to_dict()
        return User(user_info)

    def add_user(self, user: User):
        user_id = user.id
        user_info = user.get_dict()
        self.client.collection('users').document(str(user_id)).set(user_info)

    # def update_user(self):

#     user_info = user_ref.get().to_dict()
# # Add a new doc in collection 'cities' with ID 'LA'
# db.collection("users").document('331661322').set(data)

# doc_ref = db.collection("users").document("331661322")
# doc = doc_ref.get()
# print(doc.to_dict())

# def get_user(user_id : int):
#     user_ref = db.collection("users").document(str(user_id))
#     user_info = user_ref.get().to_dict()

#     return
