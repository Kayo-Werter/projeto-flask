from comunidade import database, login_manager
from datetime import datetime
from flask_login import UserMixin

'''A função load_usuario serve apenas para fazer a busca do usuário na tabela Usuário. o método Get é utilizado com a 
primary key. Ela é criada pois o login_manager precisa de uma função que retorne o id_usuario'''


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False, unique=True)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True)
    linguagem = database.Column(database.String, nullable=False, default='Não Informado')


    def contar_posts(self):
        return len(self.posts
                   )

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
