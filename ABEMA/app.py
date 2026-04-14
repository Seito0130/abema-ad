from flask import Flask, render_template, redirect

app = Flask(__name__)

# トップページの設定
@app.route('/')
def index():
    # templates/index.html を表示する
    return render_template('index.html')

# 広告をクリックした時の転送設定
@app.route('/goto/ad01')
def ad_click():
    # A8.netのリンク先URL（" " で囲むのがポイントです）
    target_url = "https://px.a8.net/svt/ejp?a8mat=4B1KXP+AZBUGI+4EKC+5ZEMP"
    return redirect(target_url)

if __name__ == '__main__':
    # ssl_context を消して、普通の HTTP で起動
    app.run(debug=True, port=8080)