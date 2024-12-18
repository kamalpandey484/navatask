from pymongo import MongoClient
import os

# Load MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

# Access the database (master DB)
db = client["master_db"]
