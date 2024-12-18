from pydantic import BaseModel
from typing import Optional

class OrganizationCreate(BaseModel):
    email: str
    password: str
    organization_name: str

class AdminLogin(BaseModel):
    email: str
    password: str
