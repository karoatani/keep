# Intoduction
This is the backend api for keep, it includes various features like:
- [x] Robust authentication system; including social login 
- [x] Managing users
- [x] Creating, Updatingand managing notes
- [x] Testing
- [x] Advanced search Feature, etc

# How to run locally
To run locally, first of all clone this repo
 ```
git clone https://github.com/karoatani/keep.git
 ```

Navigate into project directory
 ```
cd keep
 ```

Install required dependencies
 ```
pipenv install
 ```

Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

Start development server
```
python manage.py runserver
```


# Endpoints and various response code

Here are the various endpoint provided by the keep api

| Endpoint | description | Methods | Response | 
| -------- | -------- | -------- | -------- |
| /admin   | Access the admin panel   | Cell 3   | Cell2 |
| /user   | Managing users   | Cell 6   | Cell |
| /auth   | Authenticating user   | Cell 6   | Cell |
| /note   | Managing notes   | Cell 6   | Cell |



