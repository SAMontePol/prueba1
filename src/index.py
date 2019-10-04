from flask import Flask
from flask.ext.ldap import ldap

app = Flask(__name__)

app.config['LDAP_DOMAIN']='polarisind.com'
app.config['LDAP_AUTH_TEMPLATE']='layout.html'

ldap = ldap(app)

ldap = LDAP(app)
app.secret_key = "welfhwdlhwdlfhwelfhwlehfwlehfelwehflwefwlehflwefhlwefhlewjfhwelfjhweflhweflhwel"
app.add_url_rule('/login', 'login', ldap.login, methods=['GET', 'POST'])

@app.route('/')
@ldap.login_required
def index():
        pass




if __name__ == '__main__':
    app.run(debug=True, port=5000)