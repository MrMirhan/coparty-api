# coparty-api
 Backend for API to connect frontend with backed written with Python Flask.

## 1. Install Requirements

```shell

$ python -m pip install -r requirements.txt
```

## 2. Run
```shell
$ python main.py
```

## 3. Description

> * Routes can editable and find in `Routes.py`
> * Route functions can edite in `/routes/(route).py`

## 4. API Usage

### Base URL(s)

- http:///139.59.133.94

### 1. Get authenticated

- Method: POST
- Endpoint: /auth

#### Request
- Format: FORM DATA

| Name                 | Type    | Example value          | Description     |
| -------------------- | ------- | ---------------------- | --------------- |
| authcode             | String  |  #S7+C=VmN_&n!OtP7IUQ  | The authentication code that server started at first.  |

### 2. Register

- Methods: POST
- Endpoint: /register

#### Request
- Format: FORM DATA

| Name                 | Type    | Example value          | Description     |
| -------------------- | ------- | ---------------------- | --------------- |
| name         | String  | Hamza Mirhan | Name of registered user. | 
| surname         | String  | Almendi | Surname of registered user. | 
| mail         | String  | hamzaalmendi@gmail.com | Mail of registered user. | 
| passwd         | String  | 159951 | Password of registered user. | 
| conf_passwd         | String  | 159951 | Password confirm of registered user. | 

### 3. Login

- Methods: POST
- Endpoint: /register

#### Request
- Format: FORM DATA

| Name                 | Type    | Example value          | Description     |
| -------------------- | ------- | ---------------------- | --------------- |
| mail         | String  | hamzaalmendi@gmail.com | Mail of user. | 
| passwd         | String  | 159951 | Password of user. | 

### 4. Send Code

- Methods: POST
- Endpoint: /register

#### Request
- Format: FORM DATA

| Name                 | Type    | Example value          | Description     |
| -------------------- | ------- | ---------------------- | --------------- |
| code | String | #S7+C=VmN_&n!OtP7IUQ | Verification that willing to send users email. |
| mail         | String  | hamzaalmendi@gmail.com | Mail of user. | 
