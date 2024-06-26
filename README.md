# To-Do app by Russell Andrady

## Installation

1. **Clone the repository and open the project root location in a code editor**<br>

2. **Create a Python virtual environment and activate (You should have Python installed)**<br>
**Windows :**<br>
`python -m venv .venv`<br>
`.\.venv\Scripts\Activate`<br>
**Mac :**<br>
python3 -m venv .venv<br>
`source .venv/bin/activate`<br>

3. **Install dependencies from requirements.txt**<br>
**Windows :**<br>
`pip install -r requirements.txt`<br>
**Mac :**<br>
`pip3 install -r requirements.txt`<br>

4. **Set up environment variables with a .env file (for MySQl database credentials and secret_key in server.py)**<br>
**If your MySQL server uses a port other than the default (3306), add the following line to your configuration:**<br>
`app.config['MYSQL_PORT'] = 'Your_Port'`<br>
Example: `app.config['MYSQL_PORT'] = 8080`<br>

5. **Add a MySQL database named 'todoappdb'. Below is the .sql file for the database schema extracted from phpMyAdmin in XAMPP. If importing the .sql file doesn't work, just manually create the 'users' and 'todos' tables in the 'todoappdb' database**<br>
https://drive.google.com/file/d/1UYVe0LRbyr1wgZAY0XT-cUM_NiX3YPrG/view?usp=sharing
users<br>
![alt text](image.png)<br>
todos<br>
![alt text](image-1.png)<br>

6. **Now you can run the application locally**<br>
