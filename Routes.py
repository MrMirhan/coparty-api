from routes import Index
from routes import Register
from routes import Login
from routes import Validate

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
        "methods": ["POST"]
    },
    {
        "route": "/login",
        "name": "login",
        "function": Login.main,
        "methods": ["POST"]
    },
    {
        "route": "/validate",
        "name": "validate",
        "function": Validate.main,
        "methods": ["POST"]
    }
]