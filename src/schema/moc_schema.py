from pydantic import BaseModel
from uuid import UUID
from enum import Enum
from fastapi import Form

class DocumentType(str,Enum):
    PortalPayment="Portal Payment"
    ExamPayment="Exam Payment"
    CertificatePayment="Certification Payment"
    LicenseAndDegree="License & Degree"
    MocOrCertification="Moc/Certificate"
    Marksheet="Marksheet"
    CourseEnrollmentProof="Course Enrollment Proof"
    EnrollmentCertification="Enrollment Certification"

class Cycle(int,Enum):
    CYCLE1=1
    CYCLE2=2
    CYCLE3=3

class CreateMoc(BaseModel):
    document:DocumentType=Form(...)
    cycle_no:Cycle=Form(...)