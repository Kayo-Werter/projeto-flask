from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidade.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome do Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    '''O validate_on_submit tem uma função interna que faz rodar qualquer validators dentro da class e qualquer função
    que tenha o nome iniciando com "validate_". Assim, possibilitando a criação das nossa próprias validações e faremos
    a validação do Email. '''


    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Email já cadastrado! Cadastre-se com outro email ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome do Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar foto do perfil', validators=[FileAllowed(['jpg', 'png'])])
    linguagem_python = BooleanField('Linguagem Python')
    linguagem_js = BooleanField('Linguagem JavaScript')
    linguagem_ruby = BooleanField('Linguagem Ruby')
    linguagem_c = BooleanField('Linguagem C')
    linguagem_cmais = BooleanField('Linguagem C++')
    linguagem_csharp = BooleanField('Linguagem C#')
    linguagem_java = BooleanField('Linguagem Java')
    linguagem_assembly = BooleanField('Linguagem Assembly')

    botao_submit_editarperfil = SubmitField('Confirmar Edição')


    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse email!')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu post', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')
