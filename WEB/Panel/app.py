from flask import Flask, render_template, request, redirect, url_for, session, abort
import os, re

app = Flask(__name__)
app.secret_key = os.urandom(24)

_flg_val = "CSP{R3g3x_Byp4ss_Vuln_1n_M4tch3r}"

_usr_data = {
    "admin": {
        "password": "Admin_1s_Th3_b3st",
        "role": "admin"
    }
}

for i in range(5):
    _name = f"user{i}"
    _usr_data[_name] = {
        "password": f"password{i}",
        "role": "user"
    }

@app.route('/')
def index():
    return render_template('index.html', username=session.get('username'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        if username in _usr_data and _usr_data[username]["password"] == password:
            session['username'] = username
            session['role'] = _usr_data[username]["role"]
            return redirect(url_for('index'))
        else:
            error = "Invalid credentials"
    
    return render_template('login.html', error=error)

@app.route('/admin')
def admin_redirect():
    if session.get('role') != 'admin':
        abort(403)
    return redirect('/admin/index')

@app.route('/admin/index')
def admin():
    if session.get('role') != 'admin':
        return render_template('admin.html', flag=_flg_val)
    return render_template('admin.html', flag=_flg_val)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
