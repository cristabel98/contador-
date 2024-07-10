from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "llave super secreta"

@app.route("/")
def index():
    #guardar en session["contador"]la cantidad de veces que se ha ingresado 
    if 'contador' in session:
        session['contador'] +=1
    else:
        session['contador'] = 1
    return render_template("index.html")

@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")
    
@app.route("/mas-dos")
def masdos():
    session['contador'] += 1
    return redirect("/")









if __name__=="__main__":
    app.run(debug=True)