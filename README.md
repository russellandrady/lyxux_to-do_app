# To-Do app by Russell Andrady

## Installation

1. **Clone the repository**

2. **Create a Python virtual environment and activate**
**Windows :**
python -m venv .venv
.\.venv\Scripts\Activate
**Mac :**

3. **Install dependencies from `requirements.txt**
**Windows :**
pip install -r requirements.txt
**Mac :**

4. **Set up environment variables with a .env file (for MySQl database credentials and secret_key in server.py)**
**If the port is not 3306 for MySQL, add this line in the configuration:**
app.config['MYSQL_PORT'] = 'Your_Port'
Example: app.config['MYSQL_PORT'] = 8080

5. **Add a database named 'todoappdb'. Add these two tables in it**
![alt text](image.png)
