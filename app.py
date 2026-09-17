from bson.errors import InvalidId
from bson.objectid import ObjectId
from flask import Flask, redirect, render_template, request, url_for
import pymongo

app = Flask(__name__)

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["quotes_db"]
collection = db["quotes"]


# 1. READ (Home Page displaying all quotes)
@app.route("/")
def home():
  quotes = list(collection.find())  # Fetch all quotes from MongoDB
  return render_template("index.html", quotes=quotes)


# 2. CREATE (GET form page & POST form data)
@app.route("/add", methods=["GET", "POST"])
def add_quote():
  if request.method == "POST":
    quote_text = request.form.get("quote")
    author_text = request.form.get("author")

    # Input validation guard
    if not quote_text or not author_text:
      return render_template(
          "add_quote.html",
          error="Both quote and author fields are required.",
      )

    # Insert document into MongoDB
    collection.insert_one({"quote": quote_text, "author": author_text})

    # Post-Redirect-Get (PRG) pattern
    return redirect(url_for("home"))

  # GET request: render empty form
  return render_template("add_quote.html")


# 3. DELETE (Form submission per quote item)
@app.route("/delete/<quote_id>", methods=["POST"])
def delete_quote_ui(quote_id):
  try:
    object_id = ObjectId(quote_id)
    collection.delete_one({"_id": object_id})
  except InvalidId:
    pass  # Gracefully ignore or redirect if ID is malformed

  return redirect(url_for("home"))


if __name__ == "__main__":
  app.run(debug=True, port=5000)