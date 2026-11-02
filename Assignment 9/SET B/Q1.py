from flask import Flask,request,render_template,redirect
import psycopg2
app=Flask(__name__)
def dbconnect():
    return psycopg2.connect(
        dbname='stddetails',
        user='postgres',
        password='Dorit',
        host='localhost',
        port=5432
    )
@app.route('/createtable')
def createtable():
    conn=dbconnect()
    cur=conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS student1(id serial primary key,
        name varchar(100),
        course varchar(100));
        ''')
    conn.commit()
    cur.close()
    conn.close()
@app.route('/',methods=['GET','POST'])
def addstudent():
    conn=dbconnect()
    cur=conn.cursor()
    if request.method=="POST":
        n=request.form.get('name')
        c=request.form.get('course')
        cur.execute("INSERT INTO student1(name,course) VALUES(%s,%s)",(n,c))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/')
    return render_template('insert.html')
@app.route('/update',methods=['GET','POST'])
def update():
    conn=dbconnect()
    cur=conn.cursor()
    if request.method=='POST':
        i=request.form.get('id')
        c=request.form.get('course')
        cur.execute("UPDATE student1 SET course=%s WHERE id=%s;",(c,i))
        conn.commit()
    cur.execute("SELECT * FROM student1 ORDER BY id;")
    students=cur.fetchall()
    return render_template('update.html',students=students)
app.run(debug=True)
