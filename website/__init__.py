from flask import Flask

def create_app():
  app = Flask(__name__)

  app.config['SECRET_KEY'] ='hffefyerege3e3442332sd'

  return app


  

