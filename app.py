
import sqlite3
from flask import Flask , render_template, request, url_for

app = Flask(__name__)

@app.route('/top2', methods= ['GET', 'POST'])
def top2():
    # 共通の処理
    #GET時の処理
    if request.method == 'get':
        #データベースに接続
        conn = sqlite3.connect('herbicide.db')
        #データベースの中身を確認できるようにする
        c = conn.cursor()
        #SQL文の実行 テーブルに格納されたデータの取得,SELECT カラム名1, カラム名2, ... FROM テーブル名;
        c.execute("select med from 薬剤名")
        #取ってきたtaskを回収
        item = c.fetchall()
        #配列を受け取る
        task_list.append({"item":row,})
        c.close()
        return redirect("/top2.html", task_list= task_list)

    else:
        #POST時の処理
        #入力フォームに入れられた、データを取得
        Agricultural_chemicals_used= request.form.get("Agricultural_chemicals_used")
        print(Agricultural_chemicals_used)
        #共通の処理
        # ブラウザから送られてきた 使用農薬 を medテーブルに一致するレコードが
        # 存在するかを判定する。レコードが存在するとuser_idに整数が代入、存在しなければ nullが入る
        conn = sqlite3.connect('herbicide.db')
        c = conn.cursor()
        c.execute("select id from med where 薬剤名 = ?", (Drug_name,) )
        id = c.fetchone()
        conn.close()
        return render_template(url_for("edit.html", Agricultural_chemicals_used= Agricultural_chemicals_used))

@app.route("/edit<int:id>", methods =['GET', "POST"])
def edit(id):
    # 共通の処理
    #GET時の処理
    if request.method == 'get':
        #データベースに接続
        conn = sqlite3.connect('herbicide.db')
        #データベースの中身を確認できるようにする
        c = conn.cursor()
        #SQL文の実行 テーブルに格納されたデータの取得,SELECT カラム名1, カラム名2, ... FROM テーブル名;
        c.execute("select med from 希釈倍率 where id=?",(id,))
        #取ってきたidを回収
        倍率= c.fetchone()
        c.close()

    else:
        # POST時の処理
        result =request.form.get("result")
        print(result)
    # 共通の処理
        return render_template(url_for("edit.html", result=result, magnification=magnification))

@app.route("/area.html", methods=['GET', 'POST'])
def area():
    if request.method == 'get':
        return render_template("area.html")
    else:
        result = request.form.get("result")
        Spray_amount = request.form.get("Spray_amount")
        return render_template("gopage.html", result= result)

@app.route('/gopage', methods =['GET', 'POST'])
def gopage_post():
    if request.method == 'get':
        return render_template("gopage.html")
    else:
        


        return render_template('edit.html')
    
    
if __name__ == "__main__":
    app.run()
