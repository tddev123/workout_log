from flask import Flask,render_template, request
from views import views
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')
app.register_blueprint(views, url_prefix="/views")


    

    
    

    

@app.route('/tutcalc', methods=['POST'])
def calculate():
    if request.method == 'POST':
        progression = request.form['tut']
        
        if progression == ("stronger"):
            result = "same sets"
        if progression == ("weaker"):
            result = "less sets"
        
        return render_template('tutcalc.html', result = result)
    
    
    
    

    
    



if __name__ == '__main__':
    app.run(debug=True)
    
