import pymongo

# MongoDB connection settings
host = '192.168.1.141'  # Replace with your MongoDB host
port = 27017            # Replace with your MongoDB port
database_name = 'your_database_name'  # Replace with your MongoDB database name
collection_name = 'mcdmerakiapp_vlan'  # Replace with your MongoDB collection name

def validate_vlan_duplicates():
    try:
        # Connect to MongoDB
        client = pymongo.MongoClient(host, port)
        db = client[database_name]
        collection = db[collection_name]

        # Aggregate to find duplicates
        pipeline = [
            {"$group": {"_id": "$_id", "count": {"$sum": 1}}},
            {"$match": {"count": {"$gt": 1}}}
        ]

        duplicates = list(collection.aggregate(pipeline))

        if duplicates:
            print("VLANs with multiple occurrences of the same _id:")
            for duplicate in duplicates:
                print(f"_id: {duplicate['_id']}, Count: {duplicate['count']}")
        else:
            print("No duplicates found in VLAN collection.")

    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        # Close MongoDB connection
        client.close()

# Run the validation function
if __name__ == '__main__':
    validate_vlan_duplicates()
