# readme

# Task Manager API

This is a Django-based Task Manager API built using Django REST Framework (DRF). The API allows users to manage tasks and their associated subtasks. Tasks can belong to different categories such as "School", "Work", or "Personal" and support CRUD operations for both tasks and subtasks.

## Features

- **Create, Read, Update, and Delete (CRUD)** operations for tasks and subtasks.
- **Nested Subtask Management**: Subtasks can be created, updated, or deleted alongside their parent task.
- **List and Filter Tasks**: Retrieve tasks along with their subtasks.
- **Validation**: Ensures data integrity for tasks and subtasks.

## Installation

### Prerequisites

- Python 3.8+
- Django 4.0+
- Django REST Framework (DRF) 3.14+

### Steps

1. Clone the repository:
    
    ```bash
    git clone <repository_url>
    cd task-manager-api
    
    ```
    
2. Create a virtual environment and activate it:
    
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    
    ```
    
3. Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
4. Run migrations:
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    
    ```
    
5. Start the development server:
    
    ```bash
    python manage.py runserver
    
    ```
    

## Endpoints

### Task Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/tasks/` | List all tasks. |
| POST | `/tasks/` | Create a new task. |
| GET | `/tasks/<id>/` | Retrieve a specific task. |
| PUT | `/tasks/<id>/` | Update a specific task. |
| DELETE | `/tasks/<id>/` | Delete a specific task. |

### SubTask Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/tasks/<task_id>/subtasks/` | List subtasks for a specific task. |
| POST | `/tasks/<task_id>/subtasks/` | Create a subtask under a specific task. |
| GET | `/subtasks/<id>/` | Retrieve a specific subtask. |
| PUT | `/subtasks/<id>/` | Update a specific subtask. |
| DELETE | `/subtasks/<id>/` | Delete a specific subtask. |

## Example Requests

### Create a Task with Subtasks

**Request**:
POST /tasks/
```json
{
    "title": "Complete Project Report",
    "list_type": "Work",
    "description": "Prepare the annual project report for submission.",
    "due_date": "2024-12-31",
    "display": true,
    "subtasks": [
        {"title": "Gather data", "completed": false},
        {"title": "Analyze findings", "completed": false}
    ]
}

```

**Response**:

```json
{
    "id": 1,
    "title": "Complete Project Report",
    "list_type": "Work",
    "description": "Prepare the annual project report for submission.",
    "due_date": "2024-12-31",
    "display": true,
    "subtasks": [
        {"id": 1, "title": "Gather data", "completed": false},
        {"id": 2, "title": "Analyze findings", "completed": false}
    ]
}

```

### Update a Task with Subtasks

**Request**:
PUT /tasks/1/
```json
{
    "title": "Complete Project Report (Updated)",
    "list_type": "Work",
    "description": "Updated description.",
    "due_date": "2025-01-15",
    "display": false,
    "subtasks": [
        {"id": 1, "title": "Gather updated data", "completed": true},
        {"title": "Create graphs", "completed": false}
    ]
}

```

**Response**:

```json
{
    "id": 1,
    "title": "Complete Project Report (Updated)",
    "list_type": "Work",
    "description": "Updated description.",
    "due_date": "2025-01-15",
    "display": false,
    "subtasks": [
        {"id": 1, "title": "Gather updated data", "completed": true},
        {"id": 3, "title": "Create graphs", "completed": false}
    ]
}

```

## Project Structure

```
project_root/
|├── manage.py
|├── task_manager/
|   |├── migrations/
|   |├── __init__.py
|   |├── models.py
|   |├── serializers.py
|   |├── views.py
|   |├── urls.py
|   └── admin.py
|├── requirements.txt
└── README.md

```

## Running Tests

1. Create test cases in the `tests.py` file.
2. Run tests using:
    
    ```bash
    python manage.py test
    
    ```
    

## Future Enhancements

- Add user authentication and permissions.
- Implement pagination for task lists.
- Add filtering options for tasks by `list_type` or `due_date`.

---

Developed with ❤️ using Django and DRF.