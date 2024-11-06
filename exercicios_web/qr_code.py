import qrcode
meu_qrcode = qrcode.make('https://www.youtube.com/')
meu_qrcode.save('qrcode_youtube.png')
