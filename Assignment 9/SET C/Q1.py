from flask import Flask,request,render_template,redirect
import psycopg2
app=Flask(__name__)
def dbconnect():
    return psycopg2.connect(
        dbname='crudop',
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
        CREATE TABLE IF NOT EXISTS student2(id serial primary key,
        name varchar(100),
        department varchar(100));
        ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Table created successfully"
@app.route('/',methods=['GET','POST'])
def home():
    conn=dbconnect()
    cur=conn.cursor()
    if request.method=='POST':
        n=request.form.get('name')
        d=request.form.get('department')
        cur.execute("INSERT INTO student2(name,department) VALUES(%s,%s);",(n,d))
        conn.commit()
    cur.close()
    conn.close()
    return render_template('home.html')
@app.route('/update',methods=['GET','POST','PUT'])
def update():
    conn=dbconnect()
    cur=conn.cursor()
    if request.method=='POST':
        n=request.form.get('name')
        d=request.form.get('department')
        i=request.form.get('id')
        cur.execute("UPDATE student2 SET name=%s,department=%s WHERE id=%s;",(n,d,i))
        conn.commit()
        return redirect('/')
    cur.close()
    conn.close()
    return render_template('update.html')
@app.route('/delete',methods=['GET','POST','DELETE'])
def delete():
    conn=dbconnect()
    cur=conn.cursor()
    if request.method=='POST':
        i=request.form.get('id')
        cur.execute("DELETE FROM student2 where id=%s;",(i))
        conn.commit()
        return redirect('/')
    cur.close()
    conn.close()
    return render_template('delete.html')
@app.route('/display')
def display():
    conn=dbconnect()
    cur=conn.cursor()
    cur.execute("SELECT * FROM student2;")
    students=cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return render_template('display.html',students=students)
if __name__ == '__main__':
    app.run(debug=True)
