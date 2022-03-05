import random, string

def cc(length):
    code = ""
    banned = ["\\", '"', "'", "`", "|", "^", "#"]
    for x in range(length):
        while True:
            char = random.choice((string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits).replace(" ", ""))[0]
            if char in banned: continue
            code += char
            break
    return code

TELEGRAM_TOKEN = "5209834142:AAGH8AgjNSVOcXrJoM9v6cGGD--EjTUHoXY"

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 80
SERVER_DEBUG = True

MAIL_HOST = "mail.wevisionary.com"
MAIL_PORT = 465
MAIL_SENDER = "info@wevisionary.com"
MAIL_PASSWORD ="wevision_info"

MYSQL_HOST = "68.183.215.154"
MYSQL_USER = "coparty"
MYSQL_PASSWORD = "x159951A!"
MYSQL_DATABASE ="coparty_api"

API_AUTH_CODE = "%s" % (cc(random.choice(range(6, 12)))) + "_" + "%s" % (cc(random.choice(range(6, 12))))