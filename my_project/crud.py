from sqlalchemy.orm import Session
import models
import schemas

def get_medical_businesses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.MedicalBusiness).offset(skip).limit(limit).all()

def create_medical_business(db: Session, medical_business: schemas.MedicalBusinessCreate):
    db_medical_business = models.MedicalBusiness(**medical_business.dict())
    db.add(db_medical_business)
    db.commit()
    db.refresh(db_medical_business)
    return db_medical_business

def get_images(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Image).offset(skip).limit(limit).all()

def create_image(db: Session, image: schemas.ImageCreate):
    db_image = models.Image(**image.dict())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

def get_detection_results(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.DetectionResult).offset(skip).limit(limit).all()

def create_detection_result(db: Session, detection_result: schemas.DetectionResultCreate):
    db_detection_result = models.DetectionResult(**detection_result.dict())
    db.add(db_detection_result)
    db.commit()
    db.refresh(db_detection_result)
    return db_detection_result
