from Database import dbparty
import time, datetime
import bcrypt
import logging, string, random
from Mail import Mail

logger= logging.getLogger()

def register_user(mail, passwd, timestamp):
    try:
        code = str(create_code(12))
        code_res = send_verify_mail(mail, code)
        if 'success' in code_res.keys():
            mycursor = dbparty.cursor()
            sql = "INSERT INTO registration (mail, mail_confirm, paswd, paswd_confirm, mail_confirmed, mail_confirm_code, created_at, last_modified_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (mail, mail, passwd, passwd, 0, code, timestamp, timestamp)
            mycursor.execute(sql, val)
            dbparty.commit()
            return {"success": "user_created"}
        else:
            return code_res
    except Exception as e:
        logger.critical(e)
        return {"error": "writing_database_error"}

def login_user(mail, passwd):
    try:
        mycursor = dbparty.cursor()
        mycursor.execute("SELECT * FROM registration where mail = '%s'" % (mail))
        myresult = mycursor.fetchall()
        if len(myresult) > 0:
            for result in myresult:
                if bcrypt.hashpw(str.encode(passwd), str.encode(result[3])) == str.encode(result[3]):
                   return {'success': 'user_can_logged_in'}
                else:
                    return {'error': 'wrong_password'}
        return {"error": "mail_not_registered"}
    except Exception as e:
        logger.critical(e)
        return {"error": "selecting_database_error"}

def check_user_register(mail):
    try:
        mycursor = dbparty.cursor()
        mycursor.execute("SELECT * FROM registration where mail = '%s'" % (mail))
        myresult = mycursor.fetchall()
        if len(myresult) > 0:
            return {"error": "already_registered"}
        return {"success": "unique_mail"}
    except Exception as e:
        logger.critical(e)
        return {"error": "selecting_database_error"}

def register_validate(mail, conf_mail, passwd, conf_passwd, timestamp):
    if mail == conf_mail and passwd == conf_passwd:
        passwd = bcrypt.hashpw(str.encode(passwd), bcrypt.gensalt())
        user_check = check_user_register(mail)
        try:
            user_check['error']
            return user_check
        except:
            return register_user(mail, passwd, timestamp)
    elif mail != conf_mail:
        return {"error": "mail_miss_match"}
    elif passwd != conf_passwd:
        return {"error": "pass_miss_match"}

def create_code(length):
    """
    " ` ", ' " ', " ' " ve " \\ " kod oluşturmada kullanılmamalı. Onaylanırken hata çıkartıyor.
    """
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

def send_verify_mail(mail, code):
    server = Mail()
    subject = "CoParty.io - Verify your email for login"
    message = """
Your verification code is: %s
""" % (str(code))
    sent = server.send_mail(mail, subject, message)
    if sent == True:
        return {"success": "verification_code_sent"}
    else:
        return {"error": "error_while_sending_mail"}

def verify_code(code, ts):
    try:
        mycursor = dbparty.cursor()
        mycursor.execute("SELECT * FROM registration where mail_confirm_code = '%s'" % (code))
        myresult = mycursor.fetchall()
        if len(myresult) > 0:
            for result in myresult:
                try:
                    mycursor.execute("UPDATE registration SET mail_confirmed = 1, last_modified_at = '%s' WHERE mail_confirm_code = '%s'" % (ts, code))
                    dbparty.commit()
                    return {'success': 'user_verified'}
                except Exception as e:
                    logger.critical(e)
                    return {"error": "writing_database_error"}
        return {"error": "code_not_found"}
    except Exception as e:
        logger.critical(e)
        return {"error": "selecting_database_error"}

if __name__ == "__main__":
    login_user("hamzaalmendi@gmail.com", "x159951A!")