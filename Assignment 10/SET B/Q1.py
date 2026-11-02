from flask import Flask,request,render_template
import psycopg2
app=Flask(__name__)
def dbconnet():
    return psycopg2.connect(
        dbname='registration',
        user='postgres',
        password='Dorit',
        host='localhost',
        port=5432
    )
def createtable():
    conn=dbconnet()
    cur=conn.cursor()
    cur.execute('''
                create table if not exists feedback(name varchar(100) primary key,
                subject varchar(100),
                feedback varchar(200));
                ''')
    conn.commit()
    cur.close()
    conn.close()
@app.route('/',methods=['GET','POST'])
def home():
    msg=""
    if request.method=='POST':
        n=request.form['name'].strip()
        s=request.form['subject'].strip()
        f=request.form['feedback'].strip()
        if f=="":
            msg="fill the feedback"
        else:
            conn=dbconnet()
            cur=conn.cursor()
            cur.execute("insert into feedback(name,subject,feedback) values(%s,%s,%s);",(n,s,f))
            conn.commit()
            cur.close()
            conn.close()
            msg="FEEDBACK SUBMITTED SUCCESSFULLY"
    conn=dbconnet()
    cur=conn.cursor()
    cur.execute("select * from feedback;")
    feedbacks=cur.fetchall()
    cur.close()
    conn.close()
    return render_template('Q1.html',msg=msg,feedbacks=feedbacks)
if __name__ == '__main__':
    createtable()
    app.run(debug=True)
