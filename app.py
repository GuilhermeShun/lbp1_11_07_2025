from flask import Flask, render_template, session, request, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'abc'
USUARIO_CADASTRADO = "admin"
SENHA_CADASTRADA = "123"
@app.route('/login', methods=['GET', 'POST'])
def login():
    mensagem = ""

    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']

        if usuario == USUARIO_CADASTRADO and senha == SENHA_CADASTRADA:
            
            # make_response permite que se tenha um maior controle sobre o que será enviado para o navegador
            # o make_response também permite que sejam enviados arquivos separados para o navegador
            resposta = make_response(redirect(url_for('bemvindo')))
            resposta.set_cookie('username', usuario, max_age=60*10)
            session['contador'] = 0
            return resposta
        else:
            mensagem = 'Usuário ou senha inválidos. Tente novamente'
        
    return render_template('login.html', error=mensagem)

@app.route('/bemvindo', methods=['GET', 'POST'])
def bemvindo():          
    #retoma o valor definido em resposta.set_cookie('username', usuario, max_age=60*10)
    username = request.cookies.get('username') 
    if not username:
        return redirect(url_for('login'))
    cores = {'escuro': {'Fundo': '#000000', 'Texto': '#ffffff'}, 
             'claro': {'Fundo': '#ffffff', 'Texto': '#000000'}}
    if request.method == 'POST':
        resposta = make_response(redirect(url_for('bemvindo')))
        tema = request.form['tema']
        resposta.set_cookie('tema', tema, max_age=60*30)
        return resposta
    else:
        session['contador'] += 1

    return render_template('bemvindo.html', contador=session['contador'], user=username, tema=request.cookies.get('tema', 'claro'), cores=cores)
        
@app.route('/tema', methods=['GET', 'POST'])
def tema():
    if request.method == 'POST':
        cor = request.form['cor']
        resposta = make_response(redirect(url_for('bemvindo')))
        resposta.set_cookie('cor', cor, max_age=60*10)
        return resposta
    return render_template('tema.html')

@app.route('/logout')
def logout():
    resposta = make_response(redirect(url_for('login')))
    resposta.set_cookie('username', '', expires=0)
    # expires=0 faz com que o cookie deixe de existir
    return resposta

@app.route('/bemvindo/noticia1')
def exibir_noticia1():
    return render_template("/noticias/noticia1.html")

@app.route('/bemvindo/noticia2')
def exibir_noticia2():
    return render_template("/noticias/noticia2.html")

@app.route('/bemvindo/noticia3')
def exibir_noticia3():
    return render_template("/noticias/noticia3.html")

@app.route('/bemvindo/noticia4')
def exibir_noticia4():
    return render_template("/noticias/noticia4.html")

@app.route('/bemvindo/noticia5')
def exibir_noticia5():
    return render_template("/noticias/noticia5.html")

@app.route('/bemvindo/noticia6')
def exibir_noticia6():
    return render_template("/noticias/noticia6.html")

@app.route('/bemvindo/noticia7')
def exibir_noticia7():
    return render_template("/noticias/noticia7.html")

@app.route('/bemvindo/noticia8')
def exibir_noticia8():
    return render_template("/noticias/noticia8.html")

@app.route('/bemvindo/noticia9')
def exibir_noticia9():
    return render_template("/noticias/noticia9.html")

if __name__ == '__main__':
    app.run(debug=True)