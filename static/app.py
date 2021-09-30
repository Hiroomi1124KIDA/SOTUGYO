
import sqlite3
from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def top():
    #データベースに接続
    conn = sqlite3.connect('herbicide.db')
    #データベースの中身を確認できるようにする
    c = conn.cursor()
    #SQL文の実行 テーブルに格納されたデータの取得,SELECT カラム名1, カラム名2, ... FROM テーブル名;
    c.execute("select id,yakuzai from med")
    #取ってきた薬剤名を回収
    yakuzai_list=[]
    # yakuzai = c.fetchall()
    for row in c.fetchall():
        yakuzai_list.append({"id":row[0],"yakuzai":row[1]})
    c.close()
    # print(yakuzai)
    return render_template("top.html",yakuzai_list= yakuzai_list)
    # return 0

@app.route('/top/<int:id>',methods=['GET'])
def top_post(id):
    conn = sqlite3.connect('herbicide.db')
    c = conn.cursor()
    c.execute("select Spray_amount from med where id= ?", (id,))
    #散布量取得
    Spray_amount= c.fetchone()[0]
    conn.close()
    print(Spray_amount)
    return render_template("page-2.html",Spray_amount= Spray_amount)


@app.route('/page-2/<int:id>',methods=['GET','POST'])
def page2_post(id):
    #データベースに接続
    conn = sqlite3.connect('herbicide.db')
    #データベースの中身を確認できるようにする
    c = conn.cursor()
    #SQL文の実行 テーブルに格納されたデータの取得,SELECT カラム名1, カラム名2, ... FROM テーブル名;
    c.execute("select magnification from med where id=?",(id,))
    #取ってきたidを回収
    #倍率
    magnification= c.fetchone()
    c.close()
    return render_template('page-4.html',magnification= magnification)

@app.route('/page-3/<int:id>',methods=['GET','POST'])
def area3_poat(id):
    #散布面積
    Spray_area= request.form.get('Spray_area')
    #１０a当たりの散布量
    Spray_amount= request.form.get('Spray_amount')
    return render_template("page-4.html",Spray_area=Spray_area,Spray_amount=Spray_amount)

@app.route('/page-4')
def total4():
    return render_template("page-4.html")

@app.route('/page-4/<int:id>)')
def total4_post(id):
    #希釈倍率
    magnification= request.form.get('magnification')
    #１０a当たり散布量
    Spray_amount= request.form.get('Spray_amount')
    #散布面積
    result= request.form.get('result')
    #↓それぞれの計算式↓
    #農薬量1=0a当り*面積/倍率
    Amount_of_pesticide=Spray_amount*result/magnification
    #水=面積*0.001*10a当り
    water=(result*0.001)*Spray_amounta
    return render_template("page-4.htm",magnification=magnification,Spray_amount=Spray_amount,result=result)


    
if __name__ == "__main__":
    app.run(debug=True)