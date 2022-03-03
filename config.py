import random, string

def cc(length):
    code = ""
    for x in range(length):
        while True:
            char = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits)[0]
            if char == "\\" or char == "`" or char == "'" or char == '"':
                continue
            else:
                code += char
                break
    return code

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