# Intoduction
This is the backend api for keep, it includes various features like:
- [x] Robust authentication system; including social login 
- [x] Endpoints for managing users
- [x] Endpoints for creating, updatingand managing notes
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


/admin
/note
/auth



