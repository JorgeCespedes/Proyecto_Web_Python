from flask import Flask, render_template, request, url_for
import mysql.connector

app = Flask(__name__)

config = {
  'user': 'root',
  'password': 'root',
  'database': 'db_prueba',
}

@app.route("/")
def index():
  conn = mysql.connector.connect(**config)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM users LIMIT 0,10")
  users = cursor.fetchall()
  conn.commit()
  return render_template('index.html', users=users)


@app.route("/page/<number_page>")
def page(number_page):
  conn = mysql.connector.connect(**config)
  cursor = conn.cursor()

  if number_page == '1':
    cursor.execute("SELECT * FROM users LIMIT 0,10")
  if number_page == '2':
    cursor.execute("SELECT * FROM users LIMIT 10,10")
  if number_page == '3':
    cursor.execute("SELECT * FROM users LIMIT 20,10")
  if number_page == '4':
    cursor.execute("SELECT * FROM users LIMIT 30,10")
  if number_page == '5':
    cursor.execute("SELECT * FROM users LIMIT 40,10")
  if number_page == '6':
    cursor.execute("SELECT * FROM users LIMIT 50,10")
  if number_page == '7':
    cursor.execute("SELECT * FROM users LIMIT 60,10")
  if number_page == '8':
    cursor.execute("SELECT * FROM users LIMIT 70,10")
  if number_page == '9':
    cursor.execute("SELECT * FROM users LIMIT 80,10")
  if number_page == '10':
    cursor.execute("SELECT * FROM users LIMIT 90,10")

  users = cursor.fetchall()
  list_users = len(users)
  conn.commit()
  return render_template('index.html', users=users)


if __name__ == '__main__':
  app.run(debug=True)
