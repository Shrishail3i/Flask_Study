# Import the Flask class from flask module
from flask import Flask, request

# Create a flask object with __name__ as parameter.
app = Flask(__name__)

# In this app, we want to manipulate the information regarding stores, so let us create a 
# python variable for storing this information. It is a list of dictionary having name (string) and
# items (list of dictionary) as keys.
stores = [
    {
        "name": "MyStore",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]
# Implementing the endpoint for getting the stores information using API
@app.get("/store")
def get_stores():
    return {"stores":stores}

# Implementing the simple endpoint for adding the stores information using API
@app.post("/store")
def add_stores():
    request_data = request.get_json()
    new_store = {"name":request_data["name"], "items":[]}
    # FIXME: What happens if the 'name' object is missing from the request JSON.
    stores.append(new_store)
    return new_store, 201

# Implementing the endpoint for adding the item to an existing store using API
@app.post("/store/<string:name>/item")
def add_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"]==name:
            new_item = {"name":request_data["name"], "price": request_data["price"]}
            store['items'].append(new_item)
            return new_item, 201
    return {"message": "store not found"}, 404

