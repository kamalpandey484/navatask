from fastapi import FastAPI, HTTPException, Depends, status
from app.models import OrganizationCreate, AdminLogin
from app.crud import create_organization, get_organization_by_name
from app.auth import create_access_token, verify_token
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# OAuth2 password bearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="admin/login")

@app.post("/org/create")
async def create_organization_endpoint(org_data: OrganizationCreate):
    # Create the organization with admin user
    create_organization(org_data)
    return {"message": f"Organization {org_data.organization_name} created successfully."}

@app.get("/org/get")
async def get_organization_endpoint(organization_name: str):
    org = get_organization_by_name(organization_name)
    if org:
        return org
    raise HTTPException(status_code=404, detail="Organization not found")

@app.post("/admin/login")
async def admin_login(admin: AdminLogin):
    org = get_organization_by_name(admin.email)
    if org and org["admin_password"] == admin.password:
        access_token = create_access_token(data={"sub": admin.email})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
