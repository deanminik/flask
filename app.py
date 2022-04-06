from flask import Flask

app = Flask(__name__)


# http://localhost:5000/
# flask run
@app.route('/')
def start():
    return 'hello from flask->'

# working on linux or mac if we need to work in development area
# export FLASK_APP=app.py

# then use the variable to indicate that we are in development zone
# export FLASK_ENV=development
# flask run
"""
 * Serving Flask app 'app.py' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 117-709-038

"""

