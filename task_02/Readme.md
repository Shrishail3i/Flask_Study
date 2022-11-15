This is the simplest Flask application with request/response for handling the stores information. 

In this app, we want to manipulate the information regarding stores, which will  
be stored inside the python variables. The `stores` variable will be a list of 
dictionary having `name` (string) and `items` (list of dictionary) as keys. 
The `items` being a list of dictionary, each of its item will have a `name` (string) 
and `price` (float) as keys. 

Sample example showing `stores` and `items` variables is as follows:
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

This app currently has 3 API endpoints:
1. for getting all the stores information
2. for adding the stores information
3. for adding the item to an existing store

For designing and interacting with these API endpoints, we will use `Insomina` tool. 
One can also make use of `Postman` which is another popular tool similar to Insomnia.


> Insomnia is a free cross-platform desktop application that takes the pain out of interacting with and designing HTTP-based APIs. Insomnia combines an easy-to-use interface with advanced functionality like authentication helpers, code generation, and environment variables.

### How to run

Make sure the virtual environment is activated. Open the terminal in `task_02` folder 
and use the following command to run the application:

```
flask run
```

The flask application is running and will be available at url `http://127.0.0.1:5000`.
Use the following API endpoint to get the information of all stores:

```
http://127.0.0.1:5000/store
```

Use the Insomnia client for adding the stores information and adding an item to an
existing store.





