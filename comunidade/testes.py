from comunidade import app
from comunidade import database
from comunidade.models import Usuario


'''Para executar comandos no banco de dados é necessário a inclusão do with app_context() '''
with app.app_context():
    database.drop_all()
    database.create_all()

    '''Criação dos primeiros usuários no banco de dados'''
    # usuario = Usuario(username="kayo", email="kayo@gmail.com", senha="123456")
    # usuario2 = Usuario(username="joao", email="joao@gmail.com", senha="134679")
    # database.session.add(usuario)
    # database.session.add(usuario2)
    # database.session.commit()

    ''' Comando para pegar todos os usuários do BD '''
    # meus_usuarios = Usuario.query.all()
    # print(meus_usuarios)
    ''' podemos pegar o primeiro usuário e fazer consultas dos seus dados (id, email, senha, posts feitos etc)'''
    # primeiro_usuario = Usuario.query.first()
    # print(primeiro_usuario)
    # print(primeiro_usuario.id)
    # print(primeiro_usuario.email)
    # print(primeiro_usuario.post)

    ''' Outras formas de fazer uma busca no banco de dados'''
    # usuario_teste = Usuario.query.filter_by(id=1).first()
    # print(usuario_teste.email)

    '''teste de criação do primeiro post'''
    # primeiro_post = Post(id_usuario=1, titulo="Teste primeiro post", corpo="primeiro post")
    # database.session.add(primeiro_post)
    # database.session.commit()

    # post = Post.query.first()
    # print(post.autor.email)

    # usuario2 = Usuario.query.filter_by(username='kayo').first()
    # print(usuario2.email)
    # print(usuario2.senha)

