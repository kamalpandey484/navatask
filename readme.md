RUN: docker-compose up --build #it will automatically create the DB

APIs:
POST: /org/create
Payload:
{
"organization_name: "",
"email": "",
"password": ""
}

GET: /org/get
Payload:
{
"organization_name": ""
}

Admin Login:
POST: /admin/login
Payload:
{
email: "",
"password: ""
}
