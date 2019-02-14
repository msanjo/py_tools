# 特定のWebページのjpegファイルをスクレイピングで取得する
import requests
from bs4 import BeautifulSoup

# 取得対象の画像一覧があるurlからhtml情報を取得する
html = requests.get("https://xxxxxxxx"")
soup = BeautifulSoup(html.content,"html.parser")

# webページから画像ファイルが埋め込まれているurlを取得していく
urls = []
for a in soup.find_all(class_="lazy"):
    # この場合は仮にclass=lazyから、文字列jpgを含むものをaタグから読み取っている
    if "jpg" in str(a):
        urls.append(a.get("data-original"))

# 埋め込まれているurlの画像を取得してファイルにしていく
for url in urls:
    # ファイル名をurlの後ろ10文字を使って、カレントディレクトリに作成する
    fname = url[-10:]
    data = requests.get(url)
    with open(fname,"wb") as f:
        f.write(data.content)
