from bson.errors import InvalidId
from bson.objectid import ObjectId
from flask import Flask, jsonify, request
import pymongo

app = Flask(__name__)

# Database Setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["quotes_db"]
collection = db["quotes"]


# 1. READ ALL (GET)
@app.route("/api/v1/quotes", methods=["GET"])
def get_quotes():
  quotes = list(collection.find())
  for quote in quotes:
    quote["_id"] = str(quote["_id"])
  return jsonify({"quotes": quotes}), 200


# 2. READ BY AUTHOR (GET)
@app.route("/api/v1/quotes/<author>", methods=["GET"])
def get_quotes_by_author(author):
  quotes = list(collection.find({"author": author}))
  if not quotes:
    return jsonify({"message": "No quotes found for this author."}), 404

  for quote in quotes:
    quote["_id"] = str(quote["_id"])
  return jsonify({"quotes": quotes}), 200


# 3. CREATE (POST)
@app.route("/api/v1/quotes", methods=["POST"])
def add_quote():
  new_quote = request.get_json()
  if not new_quote:
    return jsonify({"message": "No data provided!"}), 400

  if "quote" not in new_quote or "author" not in new_quote:
    return jsonify({"message": "Missing required fields: 'quote' and 'author'"}), 400

  collection.insert_one(new_quote)
  new_quote["_id"] = str(new_quote["_id"])
  return jsonify({"_id": new_quote["_id"], "message": "Quote added successfully!"}), 201


# 4. UPDATE (PUT)
@app.route("/api/v1/quotes/<quote_id>", methods=["PUT"])
def update_quote(quote_id):
  try:
    object_id = ObjectId(quote_id)
  except InvalidId:
    return jsonify({"message": "Invalid quote ID!"}), 400

  updated_data = request.get_json()
  if not updated_data:
    return jsonify({"message": "No data provided!"}), 400

  result = collection.update_one({"_id": object_id}, {"$set": updated_data})
  if result.matched_count == 0:
    return jsonify({"message": "Quote not found!"}), 404
  else:
    return jsonify({"message": "Quote updated successfully!"}), 200


# 5. DELETE (DELETE)
@app.route("/api/v1/quotes/<quote_id>", methods=["DELETE"])
def delete_quote(quote_id):
  try:
    object_id = ObjectId(quote_id)
  except InvalidId:
    return jsonify({"message": "Invalid quote ID!"}), 400

  result = collection.delete_one({"_id": object_id})
  if result.deleted_count == 0:
    return jsonify({"message": "Quote not found!"}), 404
  else:
    return jsonify({"message": "Quote deleted successfully!"}), 200


if __name__ == "__main__":
  app.run(debug=True, port=5000)