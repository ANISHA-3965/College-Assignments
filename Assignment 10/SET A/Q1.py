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

@app.route('/createtable')
def createtable():
    conn=dbconnect()
    cur=conn.cursor()
    cur.execute('''
                CREATE TABLE reg(id int primary key,
                name varchar(100),
                course varchar(100));
                ''')
    conn.commit()
    cur.close()
    conn.close()
    return "table created successfully"
@app.route('/',methods=['GET','POST'])
def home():
    msg=""
    if request.method=='POST':
        i=request.form['id'].strip()
        n=request.form['name'].strip()
        c=request.form['course'].strip()
        if n=="" or c=="" or i=="":
            msg="Please Fill all the Blanks"
        else:
            conn=dbconnect()
            cur=conn.cursor()
            cur.execute("INSERT INTO reg(id,name,course) VALUES(%s,%s,%s);",(i,n,c))
            conn.commit()
            cur.close()
            conn.close()
            msg="Student Added Successfully"
    return render_template('Q1.html',msg=msg)
app.run(debug=True)
