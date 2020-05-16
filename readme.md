# Flask API tutorial with authentication

### https://dev.to/paurakhsharma/flask-rest-api-part-5-password-reset-2f2e

## Note: Part 5 password reset is not working

1. Install pyenv to install python version
2. Install pipenv and set necessary environment variables
3. Start virtual env with `pipenv shell`
4. Set up .env, .env.test files:

JWT_SECRET_KEY = 

MAIL_SERVER: "localhost"

MAIL_PORT = "1025"

MAIL_USERNAME = 

MAIL_PASSWORD = 

MONGODB_SETTINGS = {
    'host': 'mongodb://localhost/movie-bag'
}


1. Spin up API with `python run.py`
2. Test using postman 