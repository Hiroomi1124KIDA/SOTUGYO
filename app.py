
import sqlite3
from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/top2', methods= ['GET'])
def top2():
    #データベースに接続
        conn = sqlite3.connect('herbicide.db')
    #データベースの中身を確認できるようにする
        c = conn.cursor()
    #SQL文の実行 テーブルに格納されたデータの取得,SELECT カラム名1, カラム名2, ... FROM テーブル名;
        c.execute("select id,yakuzai from med")
    #取ってきた薬剤名を回収
        yakuzai_list=[]
        for row in c.fetchall():
            yakuzai_list.append({"id":row[0],"yakuzai":row[1]})
        c.close()
        return render_template("top2.html", yakuzai_list= yakuzai_list)

@app.route('/top2', methods= ['POST'])
def top2_post():
        #入力フォームに入れられた、データを取得
        Agricultural_chemicals_used= request.form.get('yakuzai["yakuzai"]')
        conn = sqlite3.connect('herbicide.db')
        c = conn.cursor()
        c.execute("select Spray_amount from med where yakuzai= ?", (Drug_name))
        #散布量取得
        Spray_amount= c.fetchone()
        conn.close()
        return render_template("edit<int:id>", kusuri_list= kusuri_list,Spray_amount= Spray_amount)

@app.route('/edit/<int:id>',methods =['GET'])
def edit(id):
    return render_template("edit.html")

@app.route('/edit<int:id>', methods =['POST'])
def edit_post(id):
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
    return render_template('gopage.html',magnification= magnification)

@app.route("/area.html", methods=['GET'])
def area():
    return render_template("area.html")

@app.route("/area.html", methods=['POST'])
def area_poat():
    Spray_area= request.form.get('Spray_area')
    Spray_amount= request.form.get('Spray_amount')
    return render_template("gopage.html")

@app.route('/page-4<int:id>') # http://○○○/item-detail/msg1/msg2を実行した場合にこの関数が実行される
def func(id):
    #倍率
    magnification= request.form.get('magnification')
    #散布量
    Spray_amount= request.form.get('Spray_amount')
    #面積
    result= request.form.get('result')
    

    return 'msg1 = {}, msg2 = {}'.format(msg1, msg2)
        


    
    
if __name__ == "__main__":
    app.run()