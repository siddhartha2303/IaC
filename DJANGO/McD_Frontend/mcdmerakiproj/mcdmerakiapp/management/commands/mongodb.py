from pymongo import MongoClient
from django.shortcuts import render
from mcdmerakiproj.mcdmerakiapp.models import Device

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "/mnt/codes/McD_Frontend/mcdmerakiproj/settings.py")


import django
django.setup()

# MongoDB connection settings
host = '52.170.44.247'  # Replace with your MongoDB host
port = 27017            # Replace with your MongoDB port

# Connect to MongoDB
try:
    client = MongoClient(host, port)
    print("Connected successfully!")
except Exception as e:
    print("Error:", e)
    exit()

# List all databases
try:
    database_names = client.list_database_names()
    print("Databases:")
    for db_name in database_names:
        print("- ", db_name)
        
        # Get the database
        database = client[db_name]
        
        # List all collections in the database
        collection_names = database.list_collection_names()
        print("  Collections:")
        for col_name in collection_names:
            print("  -", col_name)
            
            # Print all documents in the collection
            collection = database[col_name]
            documents = collection.find()
            print("    Documents:")
            for doc in documents:
                print("    -", doc)
except Exception as e:
    print("Error:", e)

# Close the connection (should ideally be done in a finally block)
client.close()
