from flask import Flask, request,redirect, session
from flask.templating import render_template
app = Flask(__name__)
app.secret_key = 'root'

@app.route('/')
def count():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1 
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/plus_two', methods = ['POST'])
def two():
    session['count'] += 1
    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True)
