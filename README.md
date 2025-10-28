# SBO-Tasks: 
## Task Management System

### 🚀 Setup
    ```bash
    git clone https://github.com/AhmedHashim04/SBO-Tasks.git
    cd SBO-Tasks/src
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

    celery -A project worker -l info
    celery -A project beat -l info

    # List projects
    curl -X GET http://127.0.0.1:8000/projects/

    # Bulk create tasks
    curl -X POST http://127.0.0.1:8000/tasks/bulk-create/ \
    -H "Content-Type: application/json" \
    -d '[{"project":1,"title":"Task 1"},{"project":1,"title":"Task 2"}]'
