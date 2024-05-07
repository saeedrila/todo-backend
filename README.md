# To Do List API

**Instructions to run**
1. Create an environment
2. Install packages from requirements.txt
3. run the app using python manage.py runserver

**User credentials**
Username: saeed
Password: asdf

**Other information**
- Django's default password validators are disabled to create shorter password.

## API Endpoints:
base_url: http://localhost:8000/

### Login
1. Login Page
URL: {{base_url}}/api-auth/login/?next=/
Description: Endpoint for user authentication and login.
HTTP Method: POST
Authentication Required: No
Request Parameters:
username (string, required): User's username.
password (string, required): User's password.
Response Format: JSON

Example Request:
{
  "username": "example_user",
  "password": "example_password"
}

Example Response (Successful Login):
Status Code: 200 OK
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImV4YW1wbGVfdXNlciJ9.Vr1g1g9Rv5TX_wDv5n07djT3ZLpNdg5pLZXc0SE7MPM"
}

Example Response (Failed Login):
Status Code: 401 Unauthorized
{
  "detail": "Invalid username or password."
}


### To Do Lists
2. ToDoLists
URL: {{base_url}}/api/todolists/
Description: Endpoint for managing to-do lists.
HTTP Methods: GET, POST
Authentication Required: Yes
Request Parameters:
title (string, required): Title of the to-do list.
Response Format: JSON

Example Request (POST):
{
  "title": "Grocery List"
}

Example Response (POST):
{
  "id": 1,
  "title": "Grocery List"
}

3. ToDoLists
URL: {{base_url}}/todolists/<id>/
Description: Endpoint for managing a specific to-do list.
HTTP Methods: GET, PUT, DELETE
Authentication Required: Yes
Request Parameters:
title (string, required): New title of the to-do list (for PUT method only).
Response Format: JSON

Example Request (PUT):
{
  "title": "Updated Grocery List"
}

Example Response (PUT):
{
  "id": 1,
  "title": "Updated Grocery List"
}

Example Response (DELETE):
{
  "message": "ToDoList deleted successfully"
}

### To Do List Items
4. ToDoItems
URL: {{base_url}}/todoitems/
Description: Endpoint for managing to-do items.
HTTP Methods: GET, POST
Authentication Required: Yes
Request Parameters:
title (string, required): Title of the to-do item.
description (string, optional): Description of the to-do item.
todo_list (integer, required): ID of the associated to-do list.
Response Format: JSON


5. ToDoItems
URL: {{base_url}}/todoitems/<id>/
Description: Endpoint for managing a specific to-do item.
HTTP Methods: GET, PUT, DELETE
Authentication Required: Yes
Request Parameters:
title (string, required): New title of the to-do item (for PUT method only).
description (string, optional): New description of the to-do item (for PUT method only).
todo_list (integer, required): New ID of the associated to-do list (for PUT method only).
Response Format: JSON