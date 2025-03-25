from flask import Flask, request, render_template, redirect, url_for, session
import mysql.connector
import base64
import xml.etree.ElementTree as ET
import logging

app = Flask(__name__, static_folder='templates/static')
app.secret_key = 'supernovakey_n0t_supposed_to_be_cracked'

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# MySQL database connection details
MYSQL_CONFIG = {
    'user': 'cosmos_user',
    'password': 'C00sM0s1900.!',
    'host': 'localhost',
    'database': 'secret'
}

# Database query function with parameterized queries
def query_db(query, params=None):
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        app.logger.error(f"Database error: {e}")
        return []

# WAF:
def waf_check(encoded_query):
    try:
        # Check if the query is base64 encoded
        decoded_query = base64.b64decode(encoded_query).decode('utf-8')
        
        # Log the decoded query
        app.logger.debug(f"Decoded query: {decoded_query}")
        return decoded_query
        
    except Exception as e:
        app.logger.error(f"Error during WAF check: {e}")
        return None


# Home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check credentials from the database
        user = query_db("SELECT username, password FROM users WHERE username=%s AND password=%s", (username, password))
        
        if user:
            session['username'] = username
            if username == "administrator":
                return redirect(url_for('admin'))
            return redirect(url_for('index'))
        else:
            return "Invalid credentials", 403
    return render_template('login.html')


@app.route('/cosmos', methods=['GET', 'POST'])
def cosmos():
    if 'username' in session and session['username'] == 'cosmos':
        if request.method == 'POST':
            query = request.form.get('query')
            bypass_success = False

            if query:
                # Pass query to WAF check
                decoded_query = waf_check(query)

                if decoded_query:
                    # Set bypass success to True for valid Base64
                    bypass_success = True
                    
                    # Execute the SQL query (caution: adjust for SQL safety)
                    results = query_db(decoded_query) 
                    app.logger.debug(f"Query results: {results}")
                    return render_template('cosmos.html', results=results, bypass_success=bypass_success)
                else:
                    # Block unauthorized queries
                    return "Blocked by WAF!", 403

        return render_template('cosmos.html', results=None, bypass_success=False)
    return redirect(url_for('login'))



# Admin page (flag is here after successful login)
@app.route('/admin')
def admin():
    if 'username' in session and session['username'] == 'administrator':
        flag = "CSP{My_WAF_Isnt_Secure_I_Should_Do_More_Work}"
        return render_template('admin.html', flag=flag)
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5601, debug=True)