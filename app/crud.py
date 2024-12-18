from datetime import datetime
from app.database import db
from app.models import OrganizationCreate

# Create organization in MongoDB
def create_organization(org_data: OrganizationCreate):
    org_collection = db.get_collection(f"{org_data.organization_name}_data")
    
    # Insert admin user
    org_collection.insert_one({
        "admin_email": org_data.email,
        "admin_password": org_data.password
    })

    # Insert organization metadata into master collection
    db.organizations.insert_one({
        "name": org_data.organization_name,
        "admin_email": org_data.email,
        "created_at": datetime.now()
    })

# Get organization by name
def get_organization_by_name(name: str):
    return db.organizations.find_one({"name": name})
