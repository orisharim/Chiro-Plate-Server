import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\Users\ori\Documents\Programming\FirebaseKeys\chiro-plate-key")
firebase_admin.initialize_app(cred)
