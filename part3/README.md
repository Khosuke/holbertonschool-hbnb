README.md:
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
<b>Explanation:</b>
<b>The app/</b> directory contains the core application code.<br>
<b>The api/</b> subdirectory houses the API endpoints, organized by version (v1/).<br>
<b>The models/</b> subdirectory contains the business logic classes (e.g., user.py, place.py).<br>
<b>The services/</b> subdirectory is where the Facade pattern is implemented, managing the interaction between layers.<br>
<b>The persistence/</b> subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQL Alchemy.<br>
<b>run.py</b> is the entry point for running the Flask application.<br>
<b>config.py</b> will be used for configuring environment variables and application settings.<br>
<b>requirements.txt</b> will list all the Python packages needed for the project.<br>
<b>README.md</b> will contain a brief overview of the project.<br>
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
### Entity-Relationship (ER) diagram:

## Requirements
List all the Python packages needed for the project in `requirements.txt`.
## Contributors
Frédéric Iglesias Montero, email: <9814@holbertonstudents.com><br>
Saïd Laamri, email: <9848@holbertonstudents.com><br>
Vithushan Satkunanathan, email: <9880@holbertonstudents.com>
## License
This project is licensed under the MIT License.
