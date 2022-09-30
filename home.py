from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    lista = ['diego','jose','luna','laila']
    data = {
        'titulo':'Index',
        'bienvenida':'Saludos!!',
        'gente' : lista,
        'cantidad' : len(lista),
    }
    
    if request.method == "POST":
        valor = request.form["name"]
        data['nombre'] = valor
    
    return render_template('main.html', data=data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)