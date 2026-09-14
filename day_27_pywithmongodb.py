# ==============================================================================
# 30 DAYS OF PYTHON - DAY 27: PYTHON WITH MONGODB (NOSQL DATABASE CRUD)
# CODE COMPILATION
# ==============================================================================

import pymongo

# ------------------------------------------------------------------------------
# 1. ESTABLISH CONNECTION & SELECT DATABASE / COLLECTION
# ------------------------------------------------------------------------------
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["thirty_days_of_python"]
collection = db["quotes"]

# ------------------------------------------------------------------------------
# 2. CREATE (INSERTING DOCUMENTS)
# ------------------------------------------------------------------------------
# Single insertion
single_quote = {
    "quote": "The mind is everything. What you think you become.",
    "author": "Buddha",
    "tags": ["mind", "philosophy"],
}
insert_res = collection.insert_one(single_quote)
print(f"Inserted single doc ID: {insert_res.inserted_id}")

# Multiple insertions
more_quotes = [
    {
        "quote": "Be the change that you wish to see in the world.",
        "author": "Mahatma Gandhi",
        "tags": ["change", "inspirational"],
    },
    {
        "quote": "Live as if you were to die tomorrow.",
        "author": "Mahatma Gandhi",
        "tags": ["life", "wisdom"],
    },
    {
        "quote": "Stay hungry, stay foolish.",
        "author": "Steve Jobs",
        "tags": ["inspiration", "tech"],
    },
]
many_res = collection.insert_many(more_quotes)
print(f"Inserted {len(many_res.inserted_ids)} documents.")

# ------------------------------------------------------------------------------
# 3. READ (QUERYING DATA)
# ------------------------------------------------------------------------------
# Find one document
one_doc = collection.find_one({"author": "Buddha"})
print("Find One Result:", one_doc["quote"])

# Find multiple documents (Returns a Cursor)
gandhi_quotes = collection.find({"author": "Mahatma Gandhi"})
print("\n--- Gandhi Quotes ---")
for doc in gandhi_quotes:
    print(f"Quote: {doc['quote']}")
    print(f"Author: {doc['author']}")

# ------------------------------------------------------------------------------
# 4. UPDATE (MODIFYING DOCUMENTS WITH $set)
# ------------------------------------------------------------------------------
collection.update_one(
    {"author": "Steve Jobs"}, {"$set": {"category": "Inspirational"}}
)
updated_doc = collection.find_one({"author": "Steve Jobs"})
print("\nUpdated Jobs Document:", updated_doc)

# ------------------------------------------------------------------------------
# 5. DELETE (REMOVING DOCUMENTS)
# ------------------------------------------------------------------------------
del_res = collection.delete_one({"author": "Steve Jobs"})
print(f"\nDeleted count: {del_res.deleted_count}")

# Verification (Should return None)
missing_doc = collection.find_one({"author": "Steve Jobs"})
print("Search after delete:", missing_doc)