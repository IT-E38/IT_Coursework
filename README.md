# IT_Coursework
##  How To Run Project
1. PIP Requirement 
2. Configure Database(We use SQLITE3)
   1. Open a terminal in the root directory
   2. Use command: python manage.py makemigrations vlog_app
   3. Use command: python manage.py migrate
3. Generate Admin User
   1. Use command: python manage.py createsuperuser
4. Populate Test Data
   1. Run vlog_app/populate_vlog_app.py
5. TestUnit
   1. Run vlog_app/test.py 