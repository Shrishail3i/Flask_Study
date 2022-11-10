
from flask import Flask
# Create a flask object with __name__ as parameter.
app = Flask(__name__)

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

@app.get("/store")
def get_stores():
    return {"stores":stores}

