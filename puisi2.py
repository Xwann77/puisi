import os
import time
import sys

def slowprint (s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(100. / 1000)

slowprint ('''
Ketika aku bertanya kepadamu tentang cinta
Kau melihat langit membentang lapang
Menyerahkan diri untuk dinikmati,
tapi menolak untuk dimiliki
''')
time.sleep(100. / 1000)
slowprint ('''
Ketika kau bertanya kepadaku tentang cinta,
Aku melihat nasib manusia
Terkutuk hidup di bumi
Bersama jangkauan lengan mereka yang pendek
Dan kemauan mereka yang panjang
''')
time.sleep(100. / 1000)
slowprint ('''
Ketika aku bertanya kepadamu tentang cinta,
Kau bayangkan aku seekor burung kecil yang murung
Bersusah payah terbang mencari tempat sembunyi
Dari mata peluru para pemburu
''')

time.sleep(100. / 1000)
slowprint ('''
Ketika kau bertanya kepadaku tentang cinta
Aku bayangkan kau satu-satunya pohon yang tersisa
Kau kesepian dan mematahkan cabang-cabang sendiri
''')
time.sleep(100. /1000)
slowprint ('''
Ketika ada yang bertanya tentang cinta,
Apakah sungguh yang dibutuhkan adalah kemewahan kata-kata
Atau cukup ketidaksempurnaan kita?

''')

os.system('xdg-open https://mydear25.blogspot.com/2022/10/dearyme.html?m=1')
