from numpy import add
from .Database import dbparty
import time, datetime
import bcrypt
import logging, string, random, json
from .Mail import Mail
from .Returns import messages as return_messages

logger= logging.getLogger()

"""
DATABASE PARTS
"""

def check_data(table, column=None, value=None, additional=None):
    try:
        mycursor = dbparty.cursor()
        query = "SELECT * FROM %s" % (table)
        if column is not None and value is not None:
            query += " where %s = '%s'" % (column, value)
        if additional is not None:
            query += additional
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        return myresult
    except Exception as e:
        logger.critical(e)
        return return_messages[8]

"""
REGISTER PARTS
"""

def register_user(name, surname, mail, passwd, timestamp):
    try:
        code = str(create_code(12))
        code_res = send_verify_mail(mail, code)
        if 'success' in code_res.keys():
            mycursor = dbparty.cursor()
            sql = "INSERT INTO registration (name, surname, type, mail, mail_confirm, paswd, paswd_confirm, mail_confirmed, mail_confirm_code, created_at, last_modified_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (name, surname, 0, mail, mail, passwd, passwd, 0, code, timestamp, timestamp)
            mycursor.execute(sql, val)
            dbparty.commit()
            return {"success": "user_created"}
        else:
            return code_res
    except Exception as e:
        logger.critical(e)
        return return_messages[7]

def register_validate(mail, conf_mail, passwd, conf_passwd, timestamp):
    if mail == conf_mail and passwd == conf_passwd:
        passwd = bcrypt.hashpw(str.encode(passwd), bcrypt.gensalt())
        datas = check_data("registration", "mail", mail)
        if len(datas) > 0:
            return return_messages[15]
        else:
            return register_user(mail, passwd, timestamp)
            
    elif mail != conf_mail:
        return return_messages[3]
    elif passwd != conf_passwd:
        return return_messages[401]


"""
VALIDATE FUNCTIONS
"""

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
        return return_messages[9]

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
                    return return_messages[7]
        return return_messages[4]
    except Exception as e:
        logger.critical(e)
        return return_messages[8]

"""
LOGIN PARTS
"""

def login_user(mail, passwd):
    try:
        datas = check_data("registration", "mail", mail)
        if len(datas) > 0:
            for result in datas:
                if bcrypt.hashpw(str.encode(passwd), str.encode(result[3])) == str.encode(result[3]):
                   return {'success': 'user_can_logged_in'}
                else:
                    return return_messages[10]
        else:
            return {"error": "mail_not_registered"}
    except Exception as e:
        logger.critical(e)
        return return_messages[8]

"""
PROFILE PARTS
"""

def create_profile_individual(id, mail, name, surname, description, image_list, interest_list, experience_list, educational_list, profile_package, timestamp):
    datas = check_data("individual_profile", "mail", mail)
    if len(datas) > 0:    
        return return_messages[15]
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO individual_profile (id, mail, name, surname, description, image_list, interest_list, experience_list, educational_list, profile_package, created_at, last_modified_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (id, mail, name, surname, description, image_list, interest_list, experience_list, educational_list, profile_package, timestamp, timestamp)
        mycursor.execute(sql, val)
        mycursor.execute("UPDATE registration SET type = 1, last_modified_at = '%s' WHERE mail = '%s'" % (timestamp, mail))
        dbparty.commit()
        return {"success": "individual_profile_created"}
    except Exception as e:
        logger.critical(e)
        return return_messages[7]

"""
TYPE ADDING PARTS
"""

def add_education_type(name, continent, timestamp):
    datas = check_data("education_types", "continent_name", continent)
    if len(datas) > 0:
        return return_messages[11]
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO education_types (name, continent_name, created_at, last_modified_at) VALUES (%s, %s, %s, %s)"
        val = (name, continent, timestamp, timestamp)
        mycursor.execute(sql, val)
        dbparty.commit()
        return {"success": "education_type_added"}
    except Exception as e:
        logger.critical(e)
        return return_messages[7]

def add_interest_type(name, continent, timestamp):
    datas = check_data("interest_types", "continent_name", continent)
    if len(datas) > 0:
        return return_messages[12]
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO interest_types (name, continent_name, created_at, last_modified_at) VALUES (%s, %s, %s, %s)"
        val = (name, continent, timestamp, timestamp)
        mycursor.execute(sql, val)
        dbparty.commit()
        return {"success": "interest_type_added"}
    except Exception as e:
        logger.critical(e)
        return return_messages[7]

def add_package(name, continent, description, price, timestamp):
    datas = check_data("profile_packages", "continent_name", continent)
    if len(datas) > 0:
        return return_messages[13]
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO profile_packages (name, continent_name, description, price, created_at, last_modified_at) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name, continent, description, price, timestamp, timestamp)
        mycursor.execute(sql, val)
        dbparty.commit()
        return {"success": "package_added"}
    except Exception as e:
        logger.critical(e)
        return return_messages[7]

"""
EXPERIENCE, EDUCATION, INTEREST `PUT` REQUESTS
"""

def check_reg_prof(user):
    regdata = check_data("registration", "id", user)
    if not type(regdata) == list and 'error' in regdata.keys(): return regdata
    if len(regdata) < 1:
        return return_messages[0]
    if regdata[0][3] == 1:
        profiledata = check_data("individual_profile", "id", user)
        if len(profiledata) < 1:
            return return_messages[1]
        else:
            return {"success": "profile_found", "profile": profiledata[0], "profile_type": 1}
    elif regdata[0][3] == 2:
        profiledata = check_data("business_profile", "id", user)
        if len(profiledata) < 1:
            return return_messages[1]
        else:
            return {"success": "profile_found", "profile": profiledata[0], "profile_type": 2}
    else:
        return return_messages[1]

def add_experience(user, name, continent, company, description, timestamp):
    check = check_reg_prof(user)
    if "error" in check.keys(): return check
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO experiences (user, name, continent_name, company, description, created_at, last_modified_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (user, name, continent, company, description, timestamp, timestamp)
        mycursor.execute(sql, val)
        dbparty.commit()
        if check['profile_type'] == 1:
            newlist = json.loads(check['profile'][7])
            newlist.append(check_data('experiences')[-1][0])
            mycursor = dbparty.cursor()
            mycursor.execute("UPDATE individual_profile SET experience_list = '%s', last_modified_at = '%s' WHERE id = '%s'" % (json.dumps(newlist), timestamp, user))
            dbparty.commit()
        return {"success": "experience_added"}
    except Exception as e:
        logger.critical(e)
        return return_messages[7]

def add_education(user, name, continent, etype, description, timestamp):
    if len(check_data("education_types", "id", etype)) < 1:
        return return_messages[11]
    check = check_reg_prof(user)
    if "error" in check.keys(): return check
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO educations (user, name, continent_name, type, description, created_at, last_modified_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (user, name, continent, etype, description, timestamp, timestamp)
        mycursor.execute(sql, val)
        dbparty.commit()
        if check['profile_type'] == 1:
            newlist = json.loads(check['profile'][8])
            newlist.append(check_data('educations')[-1][0])
            mycursor = dbparty.cursor()
            mycursor.execute("UPDATE individual_profile SET educational_list = '%s', last_modified_at = '%s' WHERE id = '%s'" % (json.dumps(newlist), timestamp, user))
            dbparty.commit()
        return {"success": "education_added"}
    except Exception as e:
        logger.critical(e)
        return return_messages[7]

def add_interest(user, name, continent, etype, description, timestamp):
    if len(check_data("interest_types", "id", etype)) < 1:
        return {"error": "interest_type_not_found"}
    interestCheck = check_data("interests", "continent_name", continent, "AND type = %s" % (etype))
    check = check_reg_prof(user)
    if len(interestCheck) > 0:
        if check['profile_type'] == 1:
            newlist = json.loads(check['profile'][6])
            if interestCheck[0][0] in newlist:
                return return_messages[16]
            newlist.append(interestCheck[0][0])
            mycursor = dbparty.cursor()
            mycursor.execute("UPDATE individual_profile SET interest_list = '%s', last_modified_at = '%s' WHERE id = '%s'" % (json.dumps(newlist), timestamp, user))
            dbparty.commit()
        return {"success": "interest_added"}
    if "error" in check.keys(): return check
    try:
        mycursor = dbparty.cursor()
        sql = "INSERT INTO interests (name, continent_name, type, description, created_at, last_modified_at) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name, continent, etype, description, timestamp, timestamp)
        mycursor.execute(sql, val)
        dbparty.commit()
        if check['profile_type'] == 1:
            newlist = json.loads(check['profile'][6])
            newlist.append(check_data('interests')[-1][0])
            mycursor = dbparty.cursor()
            mycursor.execute("UPDATE individual_profile SET interest_list = '%s', last_modified_at = '%s' WHERE id = '%s'" % (json.dumps(newlist), timestamp, user))
            dbparty.commit()
        return {"success": "interest_added"}
    except Exception as e:
        logger.critical(e)
        return return_messages[7]

"""

"""

def get_interest(user):
    profileCheck = check_reg_prof(user)
    if "error" in profileCheck:
        return profileCheck
    if profileCheck['profile_type'] == 1:
        profileInterests = profileCheck['profile'][6]
        return {'status': True, 'interests': json.loads(profileInterests)}