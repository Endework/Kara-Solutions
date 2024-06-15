from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class MedicalBusiness(Base):
    __tablename__ = "medical_businesses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    description = Column(String, index=True)
    telegram_channel = Column(String, index=True)

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    filename = Column(String, index=True)
    detection_results = relationship("DetectionResult", back_populates="image")

class DetectionResult(Base):
    __tablename__ = "detection_results"
    id = Column(Integer, primary_key=True, index=True)
    image_id = Column(Integer, ForeignKey('images.id'))
    label = Column(String, index=True)
    confidence = Column(Float)
    x_min = Column(Integer)
    y_min = Column(Integer)
    x_max = Column(Integer)
    y_max = Column(Integer)
    image = relationship("Image", back_populates="detection_results")
