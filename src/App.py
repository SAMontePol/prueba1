from flask import Flask, render_template
from flaskwebgui import FlaskUI
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                        'Server=MX1STN9GNDXK2\\DATAWARSERVER;'
                        'Database=POLARIS_MTY;'
                        'Trusted_Connection=yes;')


def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from Sheet1")
    for row in cursor:
        print(f'row = {row}')
    print()

def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute('insert into Sheet1(a, b values(?,?))',
    (3232,'catzzz')
    )
    conn.commit()
    read(conn)

def update(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute('update Sheet1 set b = ? where a = ?;',
    ('catzzz', 3232)
    )
    conn.commit()
    read(conn)

def delete(conn):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute('delete from Sheet1 where a = 3232'
    )
    conn.commit()
    read(conn)

app = Flask(__name__)

ui = FlaskUI(app)

num = 47598

@app.route('/')
def Home():
    cursor = conn.cursor()
    cursor.execute('Select * from POLARIS_MTY.dbo.employee where numero = ?' , num)
    data = cursor.fetchall()
    return render_template('Home.html', value=data)

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

@app.route('/Planning-CPR')
def PCPR():
    return render_template('Planning-CPR.html')

@app.route('/Planning-KPI')
def PKPI():
    return render_template('Planning-KPI.html')

#ui.run()

if __name__ == '__main__':
    app.run(port=3000, debug=True)