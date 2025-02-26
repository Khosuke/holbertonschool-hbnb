# HBnB Project

## Project Setup and Package Initialization

### Context
This project aims to create a well-organized structure for a scalable application. It includes the implementation of an in-memory repository, which will later be replaced by a database-backed solution.

### Directory Structure
The project is organized as follows:

```
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```

### Setup Instructions
1. **Initialize Python Packages**: Ensure each directory intended to be a Python package contains an empty `__init__.py` file.
2. **Set Up Flask Application**: Create the Flask application instance in `app/__init__.py`.
3. **Implement In-Memory Repository**: Implement the repository in `app/persistence/repository.py`.
4. **Plan for the Facade Pattern**: Define the `HBnBFacade` class in `app/services/facade.py` to handle communication between layers.

### Running the Application
To run the application, execute the following command:
```bash
python run.py
```

### Configuration
Create a `config.py` file in the root directory for environment-specific settings:
```python
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
```

### Install Required Packages
List the Python packages needed for the project in `requirements.txt`:
```
flask
flask-restx
```
Install the dependencies using:
```bash
pip install -r requirements.txt
```

### Future Enhancements
- Implement the Persistence layer using SQL Alchemy.
- Add more API endpoints for additional functionalities.

## Requirements
List all the Python packages needed for the project in `requirements.txt`.

## License
This project is licensed under the MIT License.
