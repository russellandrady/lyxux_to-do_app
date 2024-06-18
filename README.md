# To-Do app by Russell Andrady

## Installation

1. **Clone the repository and open the project root location in a code editor**

2. **Create a Python virtual environment and activate (You should have Python installed)**
**Windows :**
python -m venv .venv
.\.venv\Scripts\Activate
**Mac :**
python3 -m venv .venv
source .venv/bin/activate

3. **Install dependencies from `requirements.txt**
**Windows :**
pip install -r requirements.txt
**Mac :**
pip3 install -r requirements.txt

4. **Set up environment variables with a .env file (for MySQl database credentials and secret_key in server.py)**
**If your MySQL server uses a port other than the default (3306), add the following line to your configuration:**
app.config['MYSQL_PORT'] = 'Your_Port'
Example: app.config['MYSQL_PORT'] = 8080

5. **Add a MySQL database named 'todoappdb'. I include the .sql database below. However if it doesnot work, you can just Add users and todos tables in it**
https://drive.google.com/file/d/1UYVe0LRbyr1wgZAY0XT-cUM_NiX3YPrG/view?usp=sharing
users
![alt text](image.png)
todos
![alt text](image-1.png)

6. **Now you can run the application locally**
