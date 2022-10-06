from datetime import timedelta
import babel
from flask import Flask,render_template,request,redirect,url_for,jsonify
from afd import dfa,buscar
import jyserver.Flask as jsf
from flask_babel import Babel,format_date,gettext

app = Flask(__name__)
app.send_file_max_age_default = timedelta(seconds=1)
lang = 'es'
# app.config['BABEL_DEFAULT_LOCALE'] = lang   
babel = Babel(app)

@babel.localeselector
def get_locale():
    return lang
    # return request.accept_languages.best_match({'en','es'})


@app.route('/',methods = ['GET','POST'])
def home(): 
    return render_template('index.html')


@app.route('/obtPalabra',methods = ['GET','POST'])
def obtPalabra():    
    if request.method == 'POST':
        palabraAbuscar = request.form["palabra"]
        estado = buscar(dfa,palabraAbuscar)
        
    return render_template('index.html',estado = estado)
    
    
@app.route('/indexEn',methods = ['GET','POST'])
def homeEn(): 
    return render_template('en/indexEn.html')


@app.route('/obtPalabraEn',methods = ['GET','POST'])
def obtPalabraEn():    
    if request.method == 'POST':
        palabraAbuscar = request.form["palabra"]
        estadoEn = buscar(dfa,palabraAbuscar)
        
    return render_template('en/indexEn.html',estadoEn = estadoEn)
        
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)