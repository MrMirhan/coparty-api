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
- Endpoint: /login

#### Request
- Format: FORM DATA

| Name                 | Type    | Example value          | Description     |
| -------------------- | ------- | ---------------------- | --------------- |
| mail         | String  | hamzaalmendi@gmail.com | Mail of user. | 
| passwd         | String  | 159951 | Password of user. | 

### 4. Send Code

- Methods: POST
- Endpoint: /sendcode

#### Request
- Format: FORM DATA

| Name                 | Type    | Example value          | Description     |
| -------------------- | ------- | ---------------------- | --------------- |
| code | String | #S7+C=VmN_&n!OtP7IUQ | Verification that willing to send users email. |
| mail         | String  | hamzaalmendi@gmail.com | Mail of user. | 

### 5. Validate

- Methods: POST
- Endpoint: /validate

#### Request
- Format: FORM DATA

| Name                 | Type    | Example value          | Description     |
| -------------------- | ------- | ---------------------- | --------------- |
| code | String | #S7+C=VmN_&n!OtP7IUQ | Verification that sent to user's email. |

### 6. Creating Profile

- Methods: PUT, PATCH
- Endpoint: /profile/create

#### Request
- Format: FORM DATA
- Method: PUT

| Name                 | Type    | Example value          | Description     |
| -------------------- | ------- | ---------------------- | --------------- |
| profile_type | String | individual | Profile type will decides users profile type. Types are individual, specialist and business. |
| id | Integer | 1 | User id. |
| mail | String | hamzaalmendi @gmail.com | Mail of user. |
| name | String | Hamza Mirhan | Name of user. |
| surname | String | Almendi | Surname of user. |
| description | Long Text | Hello, I'm Mirhan... | Long text that user gives informations about himself/herself. |
| profile_package | Integer | 0 | Package of profile that user select. |
| educational_list | Array | | Education list inside only id of educations. |
| educational_list[n] | Integer | 0 | Wanted education id to add profile. |
| experience_list | Array | | Experience list inside only id of educations. |
| experience_list [n] | Integer | 0 | Wanted experience id to add profile. |
| interest_list | Array | | Interest list inside only id of educations. |
| interest_list[n] | Integer | 0 | Wanted interest id to add profile. |
| image_list| Array | | Image list inside only id of educations. |
| image_list[n] | Integer | 0 | Wanted image id to add profile. |

### 7. Validate

- Methods: POST
- Endpoint: /validate

#### Request
- Format: FORM DATA

| Name                 | Type    | Example value          | Description     |
| -------------------- | ------- | ---------------------- | --------------- |
| code | String | #S7+C=VmN_&n!OtP7IUQ | Verification that sent to user's email. |