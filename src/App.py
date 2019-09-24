from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/RH')
def RH():
    return render_template('RH.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)