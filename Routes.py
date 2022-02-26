from routes import Index

from routes import Register
from routes import Login
from routes import Validate

from routes import ProfileCreate

from routes import AddEducation
from routes import AddEducationType
from routes import AddInterest
from routes import AddInterestType
from routes import AddImage
from routes import AddImageType
from routes import AddExperience
from routes import AddPackage


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
        "route": "/profile/create",
        "name": "profile/create",
        "function": ProfileCreate.main,
        "methods": ["POST"]
    },
    {
        "route": "/admin/add/type/education",
        "name": "admin/add/type/education",
        "function": AddEducationType.main,
        "methods": ["POST"]
    },
    {
        "route": "/admin/add/type/interest",
        "name": "admin/add/type/interest",
        "function": AddInterestType.main,
        "methods": ["POST"]
    },
    {
        "route": "/admin/add/type/image",
        "name": "admin/add/type/image",
        "function": AddImageType.main,
        "methods": ["POST"]
    },
    {
        "route": "/admin/add/education",
        "name": "admin/add/education",
        "function": AddEducation.main,
        "methods": ["POST"]
    },
    {
        "route": "/admin/add/interest",
        "name": "admin/add/interest",
        "function": AddInterest.main,
        "methods": ["POST"]
    },
    {
        "route": "/admin/add/image",
        "name": "admin/add/image",
        "function": AddImage.main,
        "methods": ["POST"]
    },
    {
        "route": "/admin/add/experience",
        "name": "admin/add/experience",
        "function": AddExperience.main,
        "methods": ["POST"]
    },
    {
        "route": "/admin/add/package",
        "name": "admin/add/package",
        "function": AddPackage.main,
        "methods": ["POST"]
    }
]