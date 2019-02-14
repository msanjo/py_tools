# メールを自動送信またはフォーマット送信するためのスクリプト
# 利用実績として、Gmail、OCNメールはこのスクリプトで利用可能
from email import message
import smtplib

# メール送信ようの情報を格納する。
# 必要となるのは、SMTPサーバ情報、自分のメールアドレス、SMTP認証ID/PW
smtp_host = 'Target_SMTP_server'
smtp_port = 587
from_email = 'USER@DOMAIN'
username = 'USERNAME'
password = 'PASSWORD'

# 宛先のメールアドレスを入力させる。引数化してもよい
to_email = input("宛先のメールアドレスを入力してください：")

# メールの内容を作成
# メール件名と本文を入力してもらう。引数としてもよい。
msg = message.EmailMessage()
msg['Subject'] = input("メール件名を入力してください：") # 件名
msg['From'] = from_email # メール送信元
msg['To'] = to_email #メール送信先
msg.set_content(input("メール本文を入力してください：")) # メールの本文

# メールサーバーへアクセス
server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
print("メールを送信しました。")
server.quit()
