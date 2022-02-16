from routes import index_route
from routes import reg_route

routes = [
    {
        "route": "/",
        "name": "index",
        "function": index_route.main,
        "methods": ["GET"]
    },
    {
        "route": "/register",
        "name": "register",
        "function": reg_route.main,
        "methods": ["POST"]
    }
]