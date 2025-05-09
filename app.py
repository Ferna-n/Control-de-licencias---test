from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder='static', template_folder='templates')

# Configuración de la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'gestion_licencias'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username and not password:
            error = "Los campos de nombre de usuario y contraseña están vacíos."
        elif not username:
            error = "El campo de nombre de usuario está vacío."
        elif not password:
            error = "El campo de contraseña está vacío."
        else:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
            user = cursor.fetchone()
            conn.close()

            if not user:
                error = "El nombre de usuario es incorrecto."
            elif not check_password_hash(user['password'], password):
                error = "La contraseña es incorrecta."
            else:
                return redirect(url_for('dashboard'))

    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role_key = request.form.get('role_key', None)

        if not username and not password:
            error = "Los campos de nombre de usuario y contraseña están vacíos."
        elif not username:
            error = "El campo de nombre de usuario está vacío."
        elif not password:
            error = "El campo de contraseña está vacío."
        elif len(password) < 8 or not any(char.isdigit() for char in password) or not any(not char.isalnum() for char in password):
            error = "La contraseña debe tener al menos 8 caracteres, incluir un número y un carácter especial."
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user:
                error = "El nombre de usuario ya existe."
            elif role_key and role_key != 'practicantesdaem':
                error = "La clave de rol para administrador es incorrecta."
            else:
                hashed_password = generate_password_hash(password)
                rol_id = 1 if role_key == 'practicantesdaem' else 2  # 1 para admin, 2 para usuario normal
                cursor.execute("INSERT INTO usuarios (username, password, rol_id) VALUES (%s, %s, %s)", (username, hashed_password, rol_id))
                conn.commit()
                conn.close()
                return redirect(url_for('login'))

            conn.close()

    return render_template('register.html', error=error)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/view-licenses')
def view_licenses():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM licencias_medicas")
    licencias = cursor.fetchall()
    conn.close()
    return render_template('view_licenses.html', licencias=licencias)

@app.route('/add-license', methods=['GET', 'POST'])
def add_license():
    if request.method == 'POST':
        numero_licencia = request.form['numero_licencia']
        rut_paciente = request.form['rut_paciente']
        nombre_paciente = request.form['nombre_paciente']
        diagnostico = request.form['diagnostico']
        fecha_emision = request.form['fecha_emision']
        fecha_inicio_reposo = request.form['fecha_inicio_reposo']
        fecha_fin_reposo = request.form['fecha_fin_reposo']
        medico_tratante = request.form['medico_tratante']
        institucion_emisora = request.form['institucion_emisora']
        estado = request.form['estado']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO licencias_medicas (numero_licencia, rut_paciente, nombre_paciente, diagnostico, fecha_emision, fecha_inicio_reposo, fecha_fin_reposo, medico_tratante, institucion_emisora, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (numero_licencia, rut_paciente, nombre_paciente, diagnostico, fecha_emision, fecha_inicio_reposo, fecha_fin_reposo, medico_tratante, institucion_emisora, estado))
        conn.commit()
        conn.close()

        return redirect(url_for('dashboard'))

    return render_template('add_license.html')

@app.route('/edit-license/<int:license_id>', methods=['GET', 'POST'])
def edit_license(license_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        numero_licencia = request.form['numero_licencia']
        rut_paciente = request.form['rut_paciente']
        nombre_paciente = request.form['nombre_paciente']
        diagnostico = request.form['diagnostico']
        fecha_emision = request.form['fecha_emision']
        fecha_inicio_reposo = request.form['fecha_inicio_reposo']
        fecha_fin_reposo = request.form['fecha_fin_reposo']
        medico_tratante = request.form['medico_tratante']
        institucion_emisora = request.form['institucion_emisora']
        estado = request.form['estado']

        cursor.execute("""
            UPDATE licencias_medicas
            SET numero_licencia = %s, rut_paciente = %s, nombre_paciente = %s, diagnostico = %s,
                fecha_emision = %s, fecha_inicio_reposo = %s, fecha_fin_reposo = %s,
                medico_tratante = %s, institucion_emisora = %s, estado = %s
            WHERE id = %s
        """, (numero_licencia, rut_paciente, nombre_paciente, diagnostico, fecha_emision,
              fecha_inicio_reposo, fecha_fin_reposo, medico_tratante, institucion_emisora, estado, license_id))
        conn.commit()
        conn.close()
        return redirect(url_for('view_licenses'))

    cursor.execute("SELECT * FROM licencias_medicas WHERE id = %s", (license_id,))
    licencia = cursor.fetchone()
    conn.close()
    return render_template('edit_license.html', licencia=licencia)

@app.route('/delete-license/<int:license_id>', methods=['POST'])
def delete_license(license_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM licencias_medicas WHERE id = %s", (license_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('view_licenses'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)