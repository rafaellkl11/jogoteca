from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('lista.html', titulo='Jogos', jogos=lista, t='Nome Categoria Console')

class Jogo:
  def __init__(self, nome, categoria, console):
    self.nome = nome
    self.categoria = categoria
    self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack in Slash', 'Ps2')
lista = [jogo1, jogo2]

@app.route('/novo')
def novo():
  return render_template('novo.html', titulo_='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  jogo = Jogo(nome, categoria, console)

  lista.append(jogo)
  return redirect('/')

app.run(host='0.0.0.0', debug=True)