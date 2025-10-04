from django.shortcuts import render
import firebase_admin
from firebase_admin import firestore

def index(request):
    if not firebase_admin._apps:
        return render(request, "index.html", {"error": "Firebase no está inicializado"})
    
    db = firestore.client()
    stores_ref = db.collection("stores").stream()
    wip_ref = db.collection("wip").stream()
    dist_ref = db.collection("dist").stream()
    damage_ref = db.collection("damage").stream()

    stores = [doc.to_dict() for doc in stores_ref]
    wip = [doc.to_dict() for doc in wip_ref]
    dist = [doc.to_dict() for doc in dist_ref]
    damage = [doc.to_dict() for doc in damage_ref]

    context = {
        "stores": stores,
        "wip": wip,
        "dist": dist,
        "damage": damage,
    }

    return render(request, "index.html", context)