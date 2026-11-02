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
                create table if not exists emp(id int primary key,
                name varchar(100),
                department varchar(100));
                ''')
    conn.commit()
    cur.close()
    conn.close()
    return "table created successfully"
@app.route('/',methods=['GET','POST'])
def home():
    msg=""
    emp=None
    if request.method=='POST':
        i=request.form['id'].strip()
        n=request.form['name'].strip()
        d=request.form['department'].strip()
        if i=="" or n=="" or d=="":
            msg="PLEASE FILL ALL THE BLANKS"
        else:
            conn=dbconnect()
            cur=conn.cursor()
            cur.execute("insert into emp(id,name,department) values(%s,%s,%s);",(i,n,d))
            conn.commit()
            msg="EMPLOYEE ADDED SUCCESSFULLY"
            emp=(i,n,d)
            cur.close()
            conn.close()
    return render_template('Q2.html',msg=msg,emp=emp)
app.run(debug=True)
