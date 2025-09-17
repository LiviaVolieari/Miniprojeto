
from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'chavesecreta'
db = SQLAlchemy(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
	mensagem = None
	if request.method == 'POST':
		email = request.form.get('email')
		senha = request.form.get('senha')
		usuario = User.query.filter_by(email=email, senha=senha).first()
		if usuario:
			session['usuario_id'] = usuario.id
			session['usuario_nome'] = usuario.nome
			return redirect(url_for('index'))
		else:
			mensagem = 'E-mail ou senha inválidos!'
	return render_template('login.html', mensagem=mensagem)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	senha = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
	mensagem = None
	if request.method == 'POST':
		nome = request.form.get('nome')
		email = request.form.get('email')
		senha = request.form.get('senha')
		if User.query.filter_by(email=email).first():
			mensagem = 'E-mail já cadastrado!'
		else:
			novo_usuario = User(nome=nome, email=email, senha=senha)
			db.session.add(novo_usuario)
			db.session.commit()
			mensagem = f'Usuário {nome} cadastrado com sucesso!'
	return render_template('cadastro.html', mensagem=mensagem)


if __name__ == '__main__':
	with app.app_context():
		db.create_all()
	app.run(debug=True)
