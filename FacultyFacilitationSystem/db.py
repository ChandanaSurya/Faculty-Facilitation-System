from flask import Flask
#from flask.ext.mysqldb import MYSQL
#from flask.ext.mysqldb import MySQL
#from flaskext.mysql import MySQL
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='ffs'

mysql = MySQL(app)

@app.route("/users")
def users():
    cur = mysql.connection.cursor()
    cur.execute('''select user from mysql.user''')
    r = cur.fetchall()
    return str(r)
@app.route("/db")
def db():
    cur = mysql.connection.cursor()
    cur.execute('''select * from users''')
    res = cur.fetchall()
    return str(res)
@app.route("/insert")
def insert():
    cur = mysql.connection.cursor()
    cur.execute('''insert into users(id,name,username,password) values(456,'bunty','bunty123','kumar')''')
    cur.connection.commit()
    cur.close()
@app.route("/one")
def one():
    c = mysql.connection.cursor()
    c.execute('''select * from users''')
    d = c.fetchone()
    print (str(d),end='\n')
    return 'completed'


if __name__ == "__main__":
    app.run(debug=True)
