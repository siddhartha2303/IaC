import pymongo
from django.conf import settings
#connect_string = 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority' 

# Specify the host and port for the MongoDB connection
host = '192.168.1.141'
port = 27017

# Create a MongoClient instance
my_client = pymongo.MongoClient(host, port)


#my_client = pymongo.MongoClient(connect_string)

# First define the database name
dbname = my_client['mcdmerakidb']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["mcdmerakiapp_device"]

#let's create two documents
devices = [
    {
        "serial_no": "Q3FA-CRVS-GF8L",
        "hostname": "C2_SDWAN_1",
        "warmspare": "no",
        "stp_root": "no",
    },
    {
        "serial_no": "Q3FA-4DMA-LQM5",
        "hostname": "C2_SDWAN_2",
        "warmspare": "yes",
        "stp_root": "no",
    }
]

# Insert the documents using insert_many
result = collection_name.insert_many(devices)

# Print the inserted document IDs
print("Inserted document IDs:", result.inserted_ids)

## Insert the documents
#collection_name.insert_many([devices])
## Check the count
#count = collection_name.count()
#print(count)
#
## Read the documents
#med_details = collection_name.find({})
## Print on the terminal
#for r in med_details:
#    print(r["common_name"])
## Update one document
#update_data = collection_name.update_one({'medicine_id':'RR000123456'}, {'$set':{'common_name':'Paracetamol 500'}})
#
## Delete one document
#delete_data = collection_name.delete_one({'medicine_id':'RR000123456'})