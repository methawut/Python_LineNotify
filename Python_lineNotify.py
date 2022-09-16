from songline import Sendline

#ออก token ด้วย
token = '1zatRkrtYMNpcVpdAOg98ekXQriTgkuUyJ4c9TvO4WJ'
msg = Sendline(token)

#ส่งข้อความ
msg.sendtext('สวัสดี เรามาจาก Python_lineNotify')

#ส่งสติ๊กเกอร์
msg.sticker(620,4)
# https://uncle-engineer.com/api/sticker.pdf

#ส่งภาพ
msg.sendimage('https://os.mreport.co.th/medias/module-news/photo/fibo-kmutt-online-gather-application.jpg')
