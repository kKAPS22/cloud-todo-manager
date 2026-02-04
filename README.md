# Cloud Todo Manager ☁️📝

A cloud-based To-Do application built using Django and deployed on AWS EC2.

## Features
- User authentication
- Create, update, delete todos
- Cloud deployment on AWS
- Secure host using DuckDNS
- 
## Tech Stack
- Django REST backend
- AWS EC2 for hosting
- AWS RDS (PostgreSQL) for production database
- AWS S3 for file storage (images, media, backups)
- Nginx + Gunicorn for production server
- DuckDNS for domain mapping
  

## How to Run
```bash
git clone https://github.com/kKAPS22/cloud-todo-manager.git
cd cloud-todo-manager
pip install -r requirements.txt
python manage.py runserver
