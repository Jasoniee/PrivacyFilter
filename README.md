# PrivacyFilter
This product aims to help filter private information before feeding something into a large language model
If you want to run this website on your local. Please follow the these steps:
1.Installing all the required package for this project:
pipenv install requirements.txt
2.Starting the Django Backend
Activate the Python Environment: If you're using a virtual environment (which is highly recommended), activate it. If you're using Pipenv, this would be pipenv shell.
Install Dependencies: Install any required packages using pip or pipenv. For Pipenv, it's typically pipenv install.
Migrate Database: Run python manage.py migrate to apply database migrations.
Start the Server: Run python manage.py runserver to start the Django development server. By default, it runs on http://localhost:8000.
3.Starting the React Frontend
Navigate to the Frontend Directory: Change your directory to where your React app is located (e.g., cd frontend).
Install Node Modules: If you haven't already, install the node modules with npm install.
Start the React App: Run npm start. This will start the React development server, typically on http://localhost:3000.
