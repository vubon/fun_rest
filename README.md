## Instructions
Should have docker install on your machine. 

Pre-step:
You need to set database information in .env file and docker-compose file same. 
example:
In .env
```text
# DB information
DB_NAME=hello_db
DB_USERNAME=postgres
DB_PASSWORD=postgres
```
 In docker-compose file 
 ```text
  db:
    image: postgres
    environment:
      - POSTGRES_DB=hello_db
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
```

Step 1:
```shell script
docker-compose build 
```
Step 2:
```shell script
docker-compose up 
```
or you can run both command at a time. 
```shell script
 docker-compose up --build -d
```
Step 3: Database schema migration 
```shell script
docker-compose run web python manage.py migrate
```

Now you can create data via REST API. 

## Create User

URL: http://0.0.0.0:8000/users <br>
Method: POST <br>
Request paylod:
```json
{
    "firstName": "<firstname>",
    "lastName": "<lastname>",
    "password": "<password>"
}
```
### Response
```json
{
"id": "<DB ID>"
}
```

### Get User Details
URL: http://0.0.0.0:8000/users/{user_id} <br>
Method: GET
### Response
```json
{
    "id": "<ID>",
    "name": "<full name>" 
}
```
### Create user tags
URL: http://0.0.0.0:8000/users/{id}/tags <br>
Method: POST <br>
Request Payload
```json
{
    "tags": ["tag1", "tag2", "....."],
    "expiry": "<miliseconds>" 
}
```

### Get user tags
URL: http://0.0.0.0:8000/users?tags=tag1,tag2,tag3 <br>
Method: GET
#### Response
```json
{
    "users": [
        {
            "id": "<id 1>",
            "name": "<full name 1>",
            "tags": ["tag1", "tag2", "....."]
        },
    ]
}
```

[N.B. does not have any programmantically data validation. So you need to send validate data set]