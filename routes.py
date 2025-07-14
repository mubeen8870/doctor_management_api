from fastapi import APIRouter, HTTPException
from typing import List
from models import Doctor
from utility import load_doctors, save_doctors

router = APIRouter()

# 1. Get total doctor count
@router.get("/doctors/count")
def get_doctor_count():
    doctors = load_doctors()
    return {"total_doctors": len(doctors)}

# 2. Get all doctors
@router.get("/doctors", response_model=List[Doctor])
def get_all_doctors():
    return load_doctors()

# 3. Get doctor by ID
@router.get("/doctors/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int):
    doctors = load_doctors()
    for doc in doctors:
        if doc["id"] == doctor_id:
            return doc
    raise HTTPException(status_code=404, detail="Doctor not found")

# 4. Add new doctor
@router.post("/doctors", response_model=Doctor)
def add_doctor(doctor: Doctor):
    doctors = load_doctors()
    for d in doctors:
        if d["id"] == doctor.id:
            raise HTTPException(status_code=400, detail="Doctor ID already exists")
    doctors.append(doctor.dict())
    save_doctors(doctors)
    return doctor

# 5. Update doctor by ID
@router.put("/doctors/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, updated: Doctor):
    doctors = load_doctors()
    for i, doc in enumerate(doctors):
        if doc["id"] == doctor_id:
            doctors[i] = updated.dict()
            save_doctors(doctors)
            return updated
    raise HTTPException(status_code=404, detail="Doctor not found")

# 6. Delete doctor
@router.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int):
    doctors = load_doctors()
    new_doctors = [d for d in doctors if d["id"] != doctor_id]
    if len(doctors) == len(new_doctors):
        raise HTTPException(status_code=404, detail="Doctor not found")
    save_doctors(new_doctors)
    return {"message": "Doctor deleted"}

# 7. Get doctors by specialization
@router.get("/doctors/specialization/{specialty}", response_model=List[Doctor])
def get_by_specialization(specialty: str):
    doctors = load_doctors()
    return [d for d in doctors if d["specialization"].lower() == specialty.lower()]

# 8. Get doctors with minimum experience
@router.get("/doctors/experience/{years}", response_model=List[Doctor])
def get_by_experience(years: int):
    doctors = load_doctors()
    return [d for d in doctors if d["experience"] >= years]  


