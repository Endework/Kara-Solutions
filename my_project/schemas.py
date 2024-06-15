from pydantic import BaseModel
from typing import List

class DetectionResultBase(BaseModel):
    label: str
    confidence: float
    x_min: int
    y_min: int
    x_max: int
    y_max: int

class DetectionResultCreate(DetectionResultBase):
    image_id: int

class DetectionResult(DetectionResultBase):
    id: int
    image_id: int
    class Config:
        orm_mode = True

class ImageBase(BaseModel):
    url: str
    filename: str

class ImageCreate(ImageBase):
    pass

class Image(ImageBase):
    id: int
    detection_results: List[DetectionResult] = []
    class Config:
        orm_mode = True

class MedicalBusinessBase(BaseModel):
    name: str
    category: str
    description: str
    telegram_channel: str

class MedicalBusinessCreate(MedicalBusinessBase):
    pass

class MedicalBusiness(MedicalBusinessBase):
    id: int
    class Config:
        orm_mode = True
