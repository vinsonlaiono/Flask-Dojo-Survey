from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', phrase = 'Ninja ')  

@app.route('/results', methods=['GET', 'POST'])
def process():
    print('Welcome Ninja')
    name = request.form['name']
    language = request.form['language']
    location = request.form['location']
    print(location)
    return render_template('results.html', name = name, language = language, location = location)
if __name__=="__main__":
    app.run(debug = True)   