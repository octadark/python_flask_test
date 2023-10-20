from flask import Flask   

app = Flask(__name__)    


@app.route('/')         
def hola_mundo():
    return 'Hola Mundo!'  

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say_name(name):
    return f"Hola {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output

if __name__=="__main__":
    app.run(debug=True)
