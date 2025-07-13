from flask import Flask, render_template, session, request, redirect, url_for, make_response
cores = {'escuro': {'Fundo': '#000000', 'Texto': '#ffffff'}, 
         'claro': {'Fundo': '#ffffff', 'Texto': '#000000'}}
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
            resposta.set_cookie('username', usuario)
            session['contador'] = 0
            return resposta
        else:
            mensagem = 'Usuário ou senha inválidos. Tente novamente'
        
    return render_template('login.html', error=mensagem, tema=request.cookies.get('tema', 'claro'), cores=cores)

@app.route('/bemvindo', methods=['GET', 'POST'])
def bemvindo():
    #retoma o valor definido em resposta.set_cookie('username', usuario)
    username = request.cookies.get('username') 
    if not username:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        resposta = make_response(redirect(url_for('bemvindo')))
        if 'tema' in request.form:
            tema = request.form['tema']
            resposta.set_cookie('tema', tema, max_age=60*30)
        elif 'preferencia' in request.form:
            preferencia = request.form['preferencia']
            resposta.set_cookie('preferencia', preferencia)
        return resposta
                        
    else:
        session['contador'] += 1

    return render_template('bemvindo.html', contador=session['contador'], user=username, tema=request.cookies.get('tema', 'claro'), preferencia=request.cookies.get('preferencia', 'nenhum'), cores=cores)
        
@app.route('/logout')
def logout():
    resposta = make_response(redirect(url_for('login')))
    resposta.set_cookie('username', '', expires=0)
    # expires=0 faz com que o cookie deixe de existir
    
    return resposta

@app.route('/bemvindo/noticia1')
def exibir_noticia1():
    return render_template("/noticias/noticia1.html", cores=cores, tema=request.cookies.get('tema', 'claro'))

@app.route('/bemvindo/noticia2')
def exibir_noticia2():
    return render_template("/noticias/noticia2.html", cores=cores, tema=request.cookies.get('tema', 'claro'))

@app.route('/bemvindo/noticia3')
def exibir_noticia3():
    return render_template("/noticias/noticia3.html", cores=cores, tema=request.cookies.get('tema', 'claro'))

@app.route('/bemvindo/noticia4')
def exibir_noticia4():
    return render_template("/noticias/noticia4.html", cores=cores, tema=request.cookies.get('tema', 'claro'))

@app.route('/bemvindo/noticia5')
def exibir_noticia5():
    return render_template("/noticias/noticia5.html", cores=cores, tema=request.cookies.get('tema', 'claro'))

@app.route('/bemvindo/noticia6')
def exibir_noticia6():
    return render_template("/noticias/noticia6.html", cores=cores, tema=request.cookies.get('tema', 'claro'))

@app.route('/bemvindo/noticia7')
def exibir_noticia7():
    return render_template("/noticias/noticia7.html", cores=cores, tema=request.cookies.get('tema', 'claro'))

@app.route('/bemvindo/noticia8')
def exibir_noticia8():
    return render_template("/noticias/noticia8.html", cores=cores, tema=request.cookies.get('tema', 'claro'))

@app.route('/bemvindo/noticia9')
def exibir_noticia9():
    return render_template("/noticias/noticia9.html", cores=cores, tema=request.cookies.get('tema', 'claro'))

if __name__ == '__main__':
    app.run(debug=True)