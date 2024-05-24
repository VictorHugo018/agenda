from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#lista
contatos =[]

@app.route('/')
def index():
    return render_template('index.html', contatos=contatos)

@app.route('/adicionar_contato', methods=['GET', 'POST'])
def adicionar_contato():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        codigo = len(contatos)
        contatos.append([codigo, nome, email, telefone])
        return redirect('/')
    else:
        return render_template('adicionar_contato.html')

    app.route('/editar_contato/<int:codigo>', methods=['GET', 'POST'])
    def editar_contato():
        if request.method == 'POST':
            nome = request.form['nome']
            telefone = request.form['telefone']
            email = request.form['email']
            codigo = len(contatos)
            contatos.append([codigo, nome, telefone, email])
            return redirect('/')  # Redireciona de volta para a página i
        else:
            contato = contatos[codigo]
            return render_template('editar_contato.html', contato=contato)

if __name__== '__main__':
    app.run(debug=True) #executa o aplicativo flask
