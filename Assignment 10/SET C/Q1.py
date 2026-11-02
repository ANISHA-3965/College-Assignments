from flask import Flask,request,render_template
import psycopg2
app=Flask(__name__)
def dbconnect():
    return psycopg2.connect(
        dbname='registration',
        user='postgres',
        password='Dorit',
        host='localhost',
        port=5432
    )
def createtable():
    conn=dbconnect()
    cur=conn.cursor()
    cur.execute('''
                create table if not exists register(id serial primary key,
                name varchar(100),
                email varchar(100),
                course varchar(100));
                ''')
    conn.commit()
    cur.close()
    conn.close()
@app.route('/',methods=['GET','POST'])
def home():
    msg=""
    if request.method=='POST':
        name=request.form['name'].strip()
        email=request.form['email'].strip()
        course=request.form['course'].strip()
        if name=="" or email=="" or course=="":
            msg="Please fill all the Fields"
        elif "@" not in email:
            msg="Invalid format @ not found"
        else:
            conn=dbconnect()
            cur=conn.cursor()
            cur.execute("insert into register(name,email,course) values(%s,%s,%s);",(name,email,course))
            conn.commit()
            cur.close()
            conn.close()
            msg="Student Registered Successfully"
    conn=dbconnect()
    cur=conn.cursor()
    cur.execute("select * from register order by id;")
    students=cur.fetchall()
    cur.close()
    conn.close()
    return render_template('Q1.html',msg=msg,students=students)
if __name__ == '__main__':
    createtable()
    app.run(debug=True)
