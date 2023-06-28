from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

''' O arquivo init é responsável pela importação e criação do nosso app e do banco de dados'''

app = Flask(__name__)

app.config['SECRET_KEY'] = '17350bba99e89383d1ea7fe6c4cb5134'

if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

'''A importação dos routes deve ser feita após a criação do app pelo fato de as routes precisarem do app pra funcionar
'''
from comunidade import routes
