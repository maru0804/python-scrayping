from flask import Flask, render_template, request
import get_news
# import requests
# from bs4 import BeautifulSoup
# import urllib3
# import certifi

app = Flask(__name__)

# getのときの処理
@app.route('/', methods=['GET'])
def get():
	return render_template('index.html', \
		title = 'Form Sample(get)', \
		message = '名前を入力して下さい。')

# postのときの処理
@app.route('/', methods=['POST'])
def post():
    news, url = get_news.get_news()
    # news = map(str, news)  #mapで要素すべてを文字列に
    # news = ','.join(news)
    name = request.form['name']
    return render_template('index.html', title = 'こんにちは、{}さん'.format(name), data=zip(news,url))

if __name__ == '__main__':
	app.run(debug=True)
