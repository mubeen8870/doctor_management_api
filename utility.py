import json

FILE = "doctors.json"

def load_doctors():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_doctors(doctors):
    with open(FILE, "w") as f:
        json.dump(doctors, f, indent=4)
