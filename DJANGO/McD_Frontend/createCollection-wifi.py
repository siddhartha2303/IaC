import pymongo
from django.conf import settings

# Specify the host and port for the MongoDB connection
host = '192.168.1.141'
port = 27017

# Create a MongoClient instance
my_client = pymongo.MongoClient(host, port)

# Define the database name
dbname = my_client['mcdmerakidb']

# Get/create collection name for VLAN model
wifi_collection = dbname["mcdmerakiapp_wifi"]

# Define VLAN documents with all fields from the model
ssids = [
    {
        "number": 0,
        "ssid": "McD_HHOT",
        "authMode": "psk",
        "password": "HCLtech@2024",
        "ipAssignmentMode": "Layer 3 roaming",
        "vlanId": 420,
        "visible": "false",
        "encryptionMode": "wpa",
        # Add other fields as per your VLAN model
    },
    {
        "number": 1,
        "ssid": "McD_HHOT2",
        "authMode": "psk",
        "password": "HCLtech@2024",
        "ipAssignmentMode": "Layer 3 roaming",
        "vlanId": 410,
        "visible": "false",
        "encryptionMode": "wpa",
        # Add other fields as per your VLAN model
    }
]

# Insert VLAN documents
result = wifi_collection.insert_many(ssids)

# Print the inserted document IDs
print("Inserted Wifi document IDs:", result.inserted_ids)
