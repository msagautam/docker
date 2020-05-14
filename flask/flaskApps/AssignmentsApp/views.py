from AssignmentsApp import app

@app.route('/')
def home():
   return "hello world!"

