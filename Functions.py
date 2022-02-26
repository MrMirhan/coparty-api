from Database import dbparty
import time, datetime
import bcrypt
import logging, string, random
from Mail import Mail

logger= logging.getLogger()

def check_data(table, column, value):
    try:
        mycursor = dbparty.cursor()
        mycursor.execute("SELECT * FROM %s where %s = '%s'" % (table, column, value))
        myresult = mycursor.fetchall()
        return myresult
    except Exception as e:
        logger.critical(e)
        return {"error": "selecting_database_error"}

def register_user(name, surname, mail, passwd, timestamp):
    try:
        code = str(create_code(12))
        code_res = send_verify_mail(mail, code)
        if 'success' in code_res.keys():
            mycursor = dbparty.cursor()
            sql = "INSERT INTO registration (name, surname, mail, mail_confirm, paswd, paswd_confirm, mail_confirmed, mail_confirm_code, created_at, last_modified_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (name, surname, mail, mail, passwd, passwd, 0, code, timestamp, timestamp)
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
        datas = check_data("registration", "mail", mail)
        if len(datas) > 0:
            for result in datas:
                if bcrypt.hashpw(str.encode(passwd), str.encode(result[3])) == str.encode(result[3]):
                   return {'success': 'user_can_logged_in'}
                else:
                    return {'error': 'wrong_password'}
        else:
            return {"error": "mail_not_registered"}
    except Exception as e:
        logger.critical(e)
        return {"error": "selecting_database_error"}

def register_validate(mail, conf_mail, passwd, conf_passwd, timestamp):
    if mail == conf_mail and passwd == conf_passwd:
        passwd = bcrypt.hashpw(str.encode(passwd), bcrypt.gensalt())
        datas = check_data("registration", "mail", mail)
        if len(datas) > 0:
            return {"error": "already_registered"}
        else:
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
        datas = check_data("registration", "mail_confirm_code", code)
        if len(datas) > 0:
            for result in datas:
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

def check_profile(mail, profile_type):
    if profile_type == "individual":
        try:
            mycursor = dbparty.cursor()
            mycursor.execute("SELECT * FROM individual_profile where mail = '%s'" % (mail))
            myresult = mycursor.fetchall()
            if len(myresult) > 0:
                return myresult[0]
            return {"success": "unique_mail"}
        except Exception as e:
            logger.critical(e)
            return {"error": "selecting_database_error"}

def create_profile_individual(id, mail, name, surname, description, image_list, interest_list, experience_list, educational_list, profile_package, timestamp):
    datas = check_data("individual_profile", "mail", mail)
    if len(datas) > 0:    
        return {"error": "already_registered_profile"}
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO individual_profile (id, mail, name, surname, description, image_list, interest_list, experience_list, educational_list, profile_package, created_at, last_modified_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (id, mail, name, surname, description, image_list, interest_list, experience_list, educational_list, profile_package, timestamp, timestamp)
        mycursor.execute(sql, val)
        dbparty.commit()
        return {"success": "individual_profile_created"}
    except Exception as e:
        logger.critical(e)
        return {"error": "writing_database_error"}

def add_package(name, continent, description, price, timestamp):
    datas = check_data("profile_packages", "continent_name", continent)
    if len(datas) > 0:
        return {'error': 'package_not_unique'}
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO profile_packages (name, continent_name, description, price, created_at, last_modified_at) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name, continent, description, price, timestamp, timestamp)
        mycursor.execute(sql, val)
        dbparty.commit()
        return {"success": "package_added"}
    except Exception as e:
        logger.critical(e)
        return {"error": "writing_database_error"}

def add_experience(name, continent, description, timestamp):
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO experiences (name, continent_name, description, created_at, last_modified_at) VALUES (%s, %s, %s, %s, %s)"
        val = (name, continent, description, timestamp, timestamp)
        mycursor.execute(sql, val)
        dbparty.commit()
        return {"success": "experience_added"}
    except Exception as e:
        logger.critical(e)
        return {"error": "writing_database_error"}

def add_education(name, continent, etype, description, timestamp):
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO educations (name, continent_name, type, description, created_at, last_modified_at) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name, continent, etype, description, timestamp, timestamp)
        mycursor.execute(sql, val)
        dbparty.commit()
        return {"success": "education_added"}
    except Exception as e:
        logger.critical(e)
        return {"error": "writing_database_error"}

def add_interest(name, continent, etype, description, timestamp):
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO interests (name, continent_name, type, description, created_at, last_modified_at) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name, continent, etype, description, timestamp, timestamp)
        mycursor.execute(sql, val)
        dbparty.commit()
        return {"success": "interest_added"}
    except Exception as e:
        logger.critical(e)
        return {"error": "writing_database_error"}

def add_education_type(name, continent, timestamp):
    datas = check_data("education_type", "continent_name", continent)
    if len(datas) > 0:
        return {'error': 'education_type_not_unique'}
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO education_type (name, continent_name, created_at, last_modified_at) VALUES (%s, %s, %s, %s)"
        val = (name, continent, timestamp, timestamp)
        mycursor.execute(sql, val)
        dbparty.commit()
        return {"success": "education_type_added"}
    except Exception as e:
        logger.critical(e)
        return {"error": "writing_database_error"}

def add_interest_type(name, continent, timestamp):
    datas = check_data("interest_type", "continent_name", continent)
    if len(datas) > 0:
        return {'error': 'interest_type_not_unique'}
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO interest_type (name, continent_name, created_at, last_modified_at) VALUES (%s, %s, %s, %s)"
        val = (name, continent, timestamp, timestamp)
        mycursor.execute(sql, val)
        dbparty.commit()
        return {"success": "interest_type_added"}
    except Exception as e:
        logger.critical(e)
        return {"error": "writing_database_error"}