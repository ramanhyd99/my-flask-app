from flask import Flask

app = Flask('My flask app')


@app.route('/')
def hello():
    return "Hello World!"


'''
__name__ is a built-in variable which evaluates to the name of the current module. 
Thus it can be used to check whether the current script is being run on its own 
or being imported somewhere else.
'''
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

'''

Steps to run the Flask App locally:

1. cd src/
2. export FLASK_APP=main, export FLASK_ENV=development
3. flask run 

Server should start by default on port 5000

Alternative for running:
python main.py

'''
