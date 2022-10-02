from flask import Flask,render_template,request,redirect,url_for
from grafo import buscar,g
import pyttsx3
from gtts import gTTS
from playsound import playsound

#español
ac = gTTS("aceptado")
ac.save('./app/static/audio/aceptado.mp3')
noAc = gTTS("denegado")
noAc.save('./app/static/audio/denegado.mp3')

#ingles
ac = gTTS("accepted")
ac.save('./app/static/audio/accepted.mp3')
noAc = gTTS("denied")
noAc.save('./app/static/audio/denied.mp3')

app = Flask(__name__)

#diccionario

@app.route('/')
def home():
    dic = {'ingles':['AUTOMATON','accepted','denied'],'español':['AUTOMATA','aceptado','denegado']}
    
    return render_template('index.html',dic=dic)

@app.route('/obtPalabra',methods = ['GET','POST'])
def getPalabra():
    
    if request.method == 'POST':
        p = request.form["palabra"]
        estado = buscar(g,p)
        
    return render_template('index.html',estado = estado)
    
@app.route('/obtWord',methods = ['GET','POST'])
def obtWord():
    
    if request.method == 'POST':
        p = request.form["palabra"]
        estado = buscar(g,p)
        
    return render_template('indexEn.html',estado = estado)    
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)