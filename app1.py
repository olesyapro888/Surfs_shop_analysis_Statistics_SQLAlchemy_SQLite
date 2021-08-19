from flask import Flask

# create a new Flask instance
app = Flask(__name__)

# create a first route and define the starting point (a root)
@app.route('/')
# create a function
def hello_world():
    return 'Hello hello world'