from flask import  Flask, render_template, request, redirect, url_for
import os
import database as db
from validator import Validator

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder=template_dir)

#Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

#Ruta para guardar usuarios en la bd
@app.route('/user', methods=['POST'])
def add_user():
    id = request.form['id']
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    phone = request.form['phone']
    role = "usuario"
    status = "activo"

    if Validator.validate_id(id) and Validator.validate_name(name) and Validator.validate_name(lastname) and Validator.validate_email(email) and Validator.validate_phone(phone):
        cursor = db.database.cursor()
        sql = "INSERT INTO users (ID, Nombre, Apellidos, Correo, Telefono, Rol, Estado) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (id, name, lastname, email, phone, role, status)
        cursor.execute(sql, data)
        db.database.commit()
    else:
        print("Hay un error en los datos")
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM users WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    id = request.form['id']
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    phone = request.form['phone']
    role = "usuario"
    status = "activo"

    if Validator.validate_id(id) and Validator.validate_name(name) and Validator.validate_name(lastname) and Validator.validate_email(email) and Validator.validate_phone(phone):
        cursor = db.database.cursor()
        sql = "UPDATE users SET ID=%s, Nombre=%s, Apellidos=%s, Correo=%s, Telefono=%s, Rol=%s, Estado=%s WHERE ID=%s"
        data = (id, name, lastname, email, phone, role, status, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)