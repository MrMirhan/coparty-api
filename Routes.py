from routes import Index

from routes import Auth

from routes import Register
from routes import Login

from routes import Validate
from routes import SendCode

from routes import ProfileCreate

from routes import Education
from routes import EducationType
from routes import Interest
from routes import InterestType
from routes import Image
from routes import ImageType
from routes import Experience
from routes import Packages


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
    },
    {
        "route": "/auth",
        "name": "Authenticate",
        "function": Auth.main,
        "methods": ["POST"]
    },
    {
        "route": "/sendcode",
        "name": "send_code",
        "function": SendCode.main,
        "methods": ["POST"]
    },
    {
        "route": "/profile/create",
        "name": "profile/create",
        "function": ProfileCreate.main,
        "methods": ["PUT", "PATCH"]
    },
    {
        "route": "/admin/type/education",
        "name": "admin/type/education",
        "function": EducationType.main,
        "methods": ["GET", "PUT", "DELETE", "PATCH"]
    },
    {
        "route": "/admin/type/interest",
        "name": "admin/type/interest",
        "function": InterestType.main,
        "methods": ["GET", "PUT", "DELETE", "PATCH"]
    },
    {
        "route": "/admin/type/image",
        "name": "admin/type/image",
        "function": ImageType.main,
        "methods": ["GET", "PUT", "DELETE", "PATCH"]
    },
    {
        "route": "/profile/education",
        "name": "admin/education",
        "function": Education.main,
        "methods": ["GET", "PUT", "DELETE", "PATCH"]
    },
    {
        "route": "/profile/interest",
        "name": "admin/interest",
        "function": Interest.main,
        "methods": ["GET", "PUT", "DELETE", "PATCH"]
    },
    {
        "route": "/profile/image",
        "name": "admin/image",
        "function": Image.main,
        "methods": ["GET", "PUT", "DELETE", "PATCH"]
    },
    {
        "route": "/profile/experience",
        "name": "admin/experience",
        "function": Experience.main,
        "methods": ["GET", "PUT", "DELETE", "PATCH"]
    },
    {
        "route": "/admin/packages",
        "name": "admin/packages",
        "function": Packages.main,
        "methods": ["GET", "PUT", "DELETE", "PATCH"]
    }
]