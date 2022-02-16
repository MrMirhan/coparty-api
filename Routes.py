from routes import Index
from routes import Register

routes = [
    {
        "route": "/",
        "name": "index",
        "function": Index.main,
        "methods": ["GET"]
    },
    {
        "route": "/register",
        "name": "register",
        "function": Register.main,
        "methods": ["POST", "GET"]
    }
]