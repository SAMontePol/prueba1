from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/RH')
def RH():
    return render_template('RH.html')

@app.route('/Lean')
def Lean():
    return render_template('Lean.html')

@app.route('/Materials')
def Materials():
    return render_template('Materials.html')

@app.route('/Planning')
def Planning():
    return render_template('Planning.html')

@app.route('/Operations')
def Operations():
    return render_template('Operations.html')

@app.route('/Quality')
def Quality():
    return render_template('Quality.html')

@app.route('/Safety')
def Safety():
    return render_template('Safety.html')

def static():
    return '/static'

@app.route('/HR-BBEmployeeView')
def HRBBEV():
    return render_template('HR-BBEmployeeView.html')

@app.route('/HR-BBManagerView')
def HRBBMV():
    return render_template('HR-BBManagerView.html')

@app.route('/Safety-CS')
def SCS():
    return render_template('Safety-CS.html')

@app.route('/Safety-II')
def SII():
    return render_template('Safety-II.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)