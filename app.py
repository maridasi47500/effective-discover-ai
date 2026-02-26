from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method == 'POST':
        return "chercher sur google "+(request.form['search']+request.form['query'])
    return "<form><p>selectionne ce que tu cherches<select><option>first muusical phrase</option><option>first line of code</option></select></p><p>my recherche peut etre ajouter une phrase musical de quelque chose ou preciser ici <input name="query"/></p><input type="submit"/></form>"
