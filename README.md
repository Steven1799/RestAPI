

# Flask API with SQLAlchemy for Action Journaling  

This repository contains a simple Flask application that demonstrates CRUD operations using Flask and SQLAlchemy. The app serves as an API for managing a journal of actions, allowing users to create, read, and delete entries in a SQLite database.  

## Features  
- **CRUD Operations**:  
  - Retrieve all journal actions.  
  - Retrieve a specific action by its ID.  
  - Add a new action with a name and description.  
  - Delete an action by its ID.  
- **Database**: Utilizes SQLAlchemy ORM with SQLite as the backend.  
- **Endpoints**:  
  - `GET /` - Simple "Hello World" message.  
  - `GET /journal` - Retrieve all actions in the journal.  
  - `GET /journal/<id>` - Retrieve a specific action by ID.  
  - `POST /journal` - Add a new action (expects JSON payload).  
  - `DELETE /journal/<id>` - Delete an action by ID.  

## Requirements  
- Python 3.x  
- Flask  
- Flask-SQLAlchemy  

## Setup  
1. Clone the repository:  
   ```bash  
   git clone <repository_url>  
   cd <repository_folder>  
   ```  

2. Create a virtual environment and activate it:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate   # On Windows: venv\Scripts\activate  
   ```  

3. Install dependencies:  
   ```bash  
   pip install flask flask-sqlalchemy  
   ```  

4. Initialize the database:  
   ```python  
   from application import app, db  
   with app.app_context():  
       db.create_all()  
   ```  

5. Run the application:  
   ```bash  
   flask run  
   ```  

## Usage  
- Use tools like Postman or `curl` to test the API endpoints.  

## Example Payload for Adding an Action  
```json  
{  
  "name": "Example Action",  
  "description": "This is an example action description."  
}  
```  

## Future Enhancements  
- Add input validation and error handling.  
- Implement user authentication.  
- Extend database models with more fields.  

---  

