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
vlan_collection = dbname["mcdmerakiapp_vlan"]

# Define VLAN documents with all fields from the model
vlans = [
    {
        "networkName": "vlan1",
        "vlan_id": 1,
        "vlan_name": "VLAN 1",
        "subnet": "192.168.1.0/24",
        "gateway": "192.168.1.1",
        "enable_dhcp": True,
        "lease_time": 86400,
        "reserved_ip_start": "192.168.1.100",
        "reserved_ip_end": "192.168.1.200",
        "dns_nameservers": "8.8.8.8, 8.8.4.4",
        "dhcp_option": "option1",
        "dhcp_type": "type1",
        "ntp_ip": "ntp.example.com",
        # Add other fields as per your VLAN model
    },
    {
        "networkName": "vlan2",
        "vlan_id": 2,
        "vlan_name": "VLAN 2",
        "subnet": "192.168.2.0/24",
        "gateway": "192.168.2.1",
        "enable_dhcp": True,
        "lease_time": 86400,
        "reserved_ip_start": "192.168.2.100",
        "reserved_ip_end": "192.168.2.200",
        "dns_nameservers": "8.8.8.8, 8.8.4.4",
        "dhcp_option": "option2",
        "dhcp_type": "type2",
        "ntp_ip": "ntp.example.com",
        # Add other fields as per your VLAN model
    }
]

# Insert VLAN documents
result = vlan_collection.insert_many(vlans)

# Print the inserted document IDs
print("Inserted VLAN document IDs:", result.inserted_ids)
