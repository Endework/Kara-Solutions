from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/medical_businesses/", response_model=schemas.MedicalBusiness)
def create_medical_business(medical_business: schemas.MedicalBusinessCreate, db: Session = Depends(get_db)):
    return crud.create_medical_business(db=db, medical_business=medical_business)

@app.get("/medical_businesses/", response_model=List[schemas.MedicalBusiness])
def read_medical_businesses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    medical_businesses = crud.get_medical_businesses(db, skip=skip, limit=limit)
    return medical_businesses

@app.post("/images/", response_model=schemas.Image)
def create_image(image: schemas.ImageCreate, db: Session = Depends(get_db)):
    return crud.create_image(db=db, image=image)

@app.get("/images/", response_model=List[schemas.Image])
def read_images(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    images = crud.get_images(db, skip=skip, limit=limit)
    return images

@app.post("/detection_results/", response_model=schemas.DetectionResult)
def create_detection_result(detection_result: schemas.DetectionResultCreate, db: Session = Depends(get_db)):
    return crud.create_detection_result(db=db, detection_result=detection_result)

@app.get("/detection_results/", response_model=List[schemas.DetectionResult])
def read_detection_results(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    detection_results = crud.get_detection_results(db, skip=skip, limit=limit)
    return detection_results
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application this is to show the server is working fine"}
