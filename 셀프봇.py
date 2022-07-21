import discord
from config import *
from discord.ext import commands
import asyncio, datetime
import requests, random, string
import os, urllib
from cultureland import *
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime

intents = discord.Intents.all()
command_prefix = 접두사
bot = commands.Bot(self_bot=True, command_prefix=command_prefix,intents=intents)
token = 사람토큰

def pick(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for _ in range(0, lenn):
        text += alpha

def headers(token):
    return {
        "authority": "discord.com",
        "method": "POST",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "Authorization": token,
        "content-length": "0",
        "cookie": f"__cfuid={pick(43)}; __dcfduid={pick(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }
def serverinfo(server):
    g = bot.get_guild(int(server))
    gname = g.name
    gm = g.member_count
    a = f'> **{gname} : {gm}명**'
    return a

def getinfo(id):
    url = f"https://discordapp.com/api/users/{id}"
    he = {
        "Authorization": "Bot ODU4NjA5NDQwNTEyOTMzOTI5.YNgoWg.HgtV8-gZU-ZXDpY85QDZMJrCoLs" #건들지말것
    }
    res = requests.get(url, headers=he)
    r = res.json()
    return r

@bot.event
async def on_ready():
    print(f"Login Success {bot.user}")
    if 상메무한반복 == True:
        while True:
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=상메1))
            await asyncio.sleep(10)
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=상메2))
            await asyncio.sleep(10)
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=상메3))
            await asyncio.sleep(10)
    else:
        await bot.change_presence(activity=discord.Streaming(name="Connecting...", url="https://www.twitch.tv/faker"))

@bot.command()
async def ping(ctx):
    await ctx.send(f'> **__pong__** {round(bot.latency*1000)} ms')

@bot.command()
async def 계좌(ctx):
    await ctx.message.delete()
    await ctx.send(f'> **{계좌정보}**') #수정

@bot.command()
async def 봇(ctx, *, rec):
    await ctx.message.delete()
    await ctx.send(f'> https://discord.com/oauth2/authorize?client_id={rec}&permissions=8&scope=bot')

@bot.command()
async def 정보(ctx, *, id):
    try:
        try:
            m = id
            m1 = m.split('@')[1]
            m2 = m1.split('>')[0]
            id = m2.split('!')[1]
        except:
            id = id
        res = getinfo(id)
        name = res['username']
        de = res['discriminator']
        icon = res['avatar']
        ba = res['banner_color']
        if icon != None:
            if "a_" in icon:
                iconurl = f"https://cdn.discordapp.com/avatars/{id}/{icon}.gif?size=1024"
            else:
                iconurl = f"https://cdn.discordapp.com/avatars/{id}/{icon}.png?size=1024"
        else:
            iconurl = "https://cdn.discordapp.com/embed/avatars/0.png"
        member = await bot.fetch_user(int(id))
        date_format = "%Y년 %m월 %d일 %H시 %M분 %S초"
        aa = member.created_at.strftime(date_format)
        banner = res['banner']
        if banner != None:
            if "a_" in banner:
                bannerurl = f"https://cdn.discordapp.com/banners/{id}/{banner}.gif?size=1024"
                await ctx.reply(f'> `유저이름` : {name}#{de}\n'
                                f'> `유저아이디` : {id}\n'
                                f'> `프로필` : ||{iconurl}||\n'
                                f'> `가입한날` : {aa}\n'
                                f'> `배너색` : {ba}\n'
                                f'> `배너사진` : ||{bannerurl}||')
            else:
                bannerurl = f"https://cdn.discordapp.com/banners/{id}/{banner}.png?size=1024"
                await ctx.reply(f'> `유저이름` : {name}#{de}\n'
                                f'> `유저아이디` : {id}\n'
                                f'> `프로필` : ||{iconurl}||\n'
                                f'> `가입한날` : {aa}\n'
                                f'> `배너색` : {ba}\n'
                                f'> `배너사진` : {bannerurl}')
        else:
            await ctx.reply(f'> `유저이름` : {name}#{de}\n'
                            f'> `유저아이디` : {id}\n'
                            f'> `프로필` : ||{iconurl}||\n'
                            f'> `가입한날` : {aa}\n'
                            f'> `배너색` : {ba}\n'
                            f'> `배너사진` : None')
    except:
        await ctx.reply("> 존재하지않는 사용자입니다.")

@bot.command()
async def 벤(ctx, member : discord.User, *, reason = None):
    if not reason:
        res = requests.put(f"https://discord.com/api/guilds/{ctx.guild.id}/bans/{member.id}", headers=headers(token), json={'delete_message_days': '1'})
        if res.status_code == 200 or res.status_code == 201 or res.status_code == 204:
            await ctx.send(f"> {member} 님을 `성공적으로` __영구차단하였습니다. 사유 : 없음__")
    else:
        res = requests.put(f"https://discord.com/api/guilds/{ctx.guild.id}/bans/{member.id}", headers=headers(token), json={'delete_message_days': '1','reason': reason})
        if res.status_code == 200 or res.status_code == 201 or res.status_code == 204:
            await ctx.send(f"> {member} 님을 `성공적으로` __영구차단하였습니다. 사유 : {reason}__")

@bot.command()
async def 벤해제(ctx, member : discord.User):
    res = requests.delete(f"https://discord.com/api/guilds/{ctx.guild.id}/bans/{member.id}", headers=headers(token))
    if res.status_code == 200 or res.status_code == 201 or res.status_code == 204:
        await ctx.send(f"> {member} 님을 `성공적으로` __차단해제하였습니다.__")

@bot.command()
async def 숨기기(ctx, link):
    await ctx.message.delete()
    await ctx.send(f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
                                   f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
                                   f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
                                   f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
                                   f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
                                   f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
                                   f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
                                   f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
                                   f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||"
                                   f"|​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||"
                                   f"​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||"
                                   f"​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||"
                                   f"​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ "
                                   f"{link}")

@bot.command(name="역할생성", help="뒤에 있는 역할 이름으로 역할을 생성합니다.")
@commands.has_permissions(manage_roles=True)
async def create_role(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'역할 `{name}` 이 만들어졌습니다.')

@bot.command()
async def 수정(ctx):
    msg = await ctx.send("곧 사라질 메시지")
    await asyncio.sleep(1)
    await msg.edit(content=f"**{ctx.prefix}{ctx.command}**")

@bot.command(pass_context=True)
async def 역할(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"> `{user}`님에게 `{role.name}`역할이 성공적으로 지급되었습니다.")

@bot.command()
async def 서버(ctx, *, server):
    await ctx.message.delete()
    a = serverinfo(server)
    await ctx.send(f'{a}')

@bot.command()
async def 채널(ctx):
    if ctx.guild != None:
        await ctx.send(f"> `{ctx.guild}` -> `{ctx.channel}` -> `{ctx.channel.id}`")
    else:
        await ctx.send(f"> `{ctx.channel}` -> `{ctx.channel.id}`")

@bot.command()
async def 시간(ctx):
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    msg = await ctx.reply(f'> 시간정보 : __{y}년 {m}월 {d}일 {h}시 {min}분__')
@bot.command()
async def 비코(ctx):
    await ctx.message.delete()
    msg = await ctx.send(f'> **BTC주소**\n> n3DtmorExe1dnZmn2q7U14x1aQgM3xwEtRR')
    await asyncio.sleep(10)
    await msg.delete()

@bot.command(name="청소", pass_context=True)
async def _clear(ctx, *, amount):
    if int(amount) <= 10:
        await ctx.channel.purge(limit=int(amount))
        await ctx.send(f"> `{amount}`개 청소가 __완료되었습니다__")
    else:
        await ctx.send(f"> `{amount}`개는 셀프봇으로 청소하기에 너무 __큰숫자입니다.__\n\n> `10`개 __이하로__ 입력해주세요.")

@bot.event
async def on_command_error(ctx, error):
    await ctx.message.delete()
    msg = await ctx.send(f"> **`오류`가 발생하였습니다.**\n\n> __{error}__")
    await msg.add_reaction('❌')

@bot.command()
async def 상메(ctx, *, text):
  await bot.change_presence(activity=discord.Game(name=f'{text}'))
  await ctx.send(f"> 상태메시지가 `{text}`로 성공적으로 __변경되었습니다.__")

@bot.command()
async def 주사위(ctx):
    com = random.choice(["1", "2", "3", "4", "5", "6"])
    await ctx.send(f"{ctx.author.mention}님 랜덤주사위 결과는 {com}입니다 🎲")

@bot.command()
async def 루트(ctx, *, dd):
    a = ("{:g}".format(int(dd) ** (1 / 2)))
    await ctx.reply(f"> `{a}`")

@bot.command()
async def 약수(ctx, *, n):
    i = 1
    list_a = []
    if len(str(n)) <= 5:
        while i <= int(n):
            if int(n) % i == 0:
                list_a.append(i)
            i += 1
    await ctx.reply(f"> `{list_a}`")

@bot.command()
async def 명령어(ctx):
    await ctx.send("> `ping` = 컴의 `핑`을 확인할수있습니다."
             "\n> `계좌` = 설정해논 `계좌`를 명령어로 불러옵니다."
             "\n> `봇` `봇아이디` = 봇아이디로 `봇초대링크`를 만들어서 불러옵니다."
             "\n> `벤` `유저멘션` = 멘션당한유저를 서버에서 `영구차단`합니다."
             "\n> `벤해제` `유저아이디` = 유저아이디에 해당하는 유저를 서버에서 `영구차단해제`를 합니다."
             "\n> `역할생성` `역할이름` = 역할이름으로 된 역할을 `생성`합니다."
             "\n> `역할` `유저멘션` `역할이름` = 역할이름으로 된 역할을 멘션당한 유저에게 `지급`합니다."
             "\n> `상메` `바꿀상메` = `상태메시지`를 적은 메시지로 바꿉니다."
             "\n> `서버` `서버아이디` = 서버아이디에 해당한 서버의 `인원수`를 불러옵니다."
             "\n> `채널` = 명령어를 쓴 `채널`의 정보를 불러옵니다."
             "\n> `시간` = 명령어를 쓴 `시간`의 정보를 불러옵니다."
             "\n> `청소` `숫자` = 숫자만큼 해당채널의 메시지를 `청소`합니다."
             "\n> `루트` `숫자` = 숫자의 `제곱근`을 불러옵니다."
             "\n> `약수` `숫자` = 숫자의 `약수`를 불러옵니다."
             "\n> `토큰만` `이멜:비번:토큰` = 받은토큰을 `토큰만` 출력합니다."
             "\n> `토큰체킹` `토큰` = 받은토큰을 `체킹`하여 사용가능한지 나타냅니다."
             "\n> `문상` `핀번호` = 핀번호로 문상을 `충전`합니다."
             "\n> `돈` = 설정한 컬쳐랜드아이디의 `잔액`을 불러옵니다."
             "\n> `웹훅생성` = 메시지를 친 채널의 `웹훅`을 `생성`합니다."
             "\n> `출금` `액수` = 액수만큼 문상을 `출금`합니다."
             "\n> `정보` `멘션혹은 아이디` = 대상의 `정보`를 불러옵니다."
             "\n> `검색` `검색할것` = 검색할것을 봇이 네이버에 `검색`하고 스샷해서 보여줍니다"
             "\n> `웹` `웹주소` = 웹주소의 `웹 소스를 파싱`해서 html파일형태로 출력합니다."
            f"\n> \n> __접두사__ = {command_prefix}")

@bot.command()
async def 토큰만(ctx, *, tk):
    open('tokens.txt', 'w')
    with open('tokens.txt','w') as f:
        f.write(tk)
    with open('tokens.txt','r') as f:
        tokens=f.read().split('\n')
    go=[]
    for token in tokens:
        try:
            if not token=='':
                tokenone=token.split(':')[2]
        except:
            print('이메일:비밀번호:토큰 순으로 입력해주세요')
            print('========================================================')
            exit()
        go.append(tokenone)
    with open('tokens.txt','w') as f:
        f.write('\n'.join(go))
    await ctx.send(file=discord.File(f"tokens.txt"))
    os.remove(f"tokens.txt")

@bot.command()
async def 토큰체킹(ctx, *, token):
    try:
        token = token.split(":")[2]
    except:
        token = token
    headers = {'Content-Type': 'application/json', 'authorization': token}
    url = "https://discordapp.com/api/v6/users/@me/library"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        await ctx.reply(f"> 이 토큰은 사용가능합니다. :key: ")
    else:
        await ctx.reply("> 이 토큰은 사용불가능합니다. :lock:")

@bot.command()
async def 문상(ctx, *, msg):
    try:
        jsondata = {"token": "토큰", "id": 컬쳐아디, "pw": 컬쳐비번, "pin": msg}
        res = requests.post("API적으세요", json=jsondata)
    except:
        try:
            await ctx.reply("> 문화상품권 충전 실패\n> \n> 일시적인 서버 오류입니다.\n> 잠시 후 다시 시도해주세요.")
        except:
            pass
        return None
    res = res.json()
    if res["result"] == True:
        try:
            culture_fee = int(0)
            culture_amount = int(res["amount"])
            culture_amount_after_fee = culture_amount - int(culture_amount * (culture_fee / 100))
            await ctx.reply(f"> 문화상품권 충전 성공\n> \n> 핀코드: `{msg}`\n> 금액: `{culture_amount}`원\n> 충전한 금액: `{culture_amount_after_fee}`")
        except:
            pass

    else:
        await ctx.reply("> 문화상품권 충전 실패\n> \n> 실패 사유 : " + res["reason"])

@bot.command()
async def 충전(ctx, *, msg):
    try:
        jsondata = {"token": '토큰', "id": 컬쳐아디, "pw": 컬쳐비번, "pin": msg}
        res = requests.post('API적으세요', json=jsondata)
    except:
        try:
            await ctx.reply("> 문화상품권 충전 실패\n> \n> 일시적인 서버 오류입니다.\n> 잠시 후 다시 시도해주세요.")
        except:
            pass
        return None
    res = res.json()
    if res["result"] == True:
        try:
            culture_fee = int(0)
            culture_amount = int(res["amount"])
            culture_amount_after_fee = culture_amount - int(culture_amount * (culture_fee / 100))
            await ctx.reply(
                f"> 문화상품권 충전 성공\n> \n> 핀코드: `{msg}`\n> 금액: `{culture_amount}`원\n> 충전한 금액: `{culture_amount_after_fee}`")
        except:
            pass

    else:
        await ctx.reply("> 문화상품권 충전 실패\n> \n> 실패 사유 : " + res["reason"])

@bot.command()
async def 이모지(ctx, *, mes):
    msg = await ctx.send(f"{mes}")
    await msg.edit("ㅋㅋ")

@bot.command()
async def 링크(ctx, *, url):
    options = Options()
    options.add_argument('headless')
    browser = webdriver.Chrome("./chromedriver.exe", options=options)
    browser.get(url)
    screenshot = browser.save_screenshot("망치천재" + '.png')
    browser.quit()
    await ctx.reply(file=discord.File("망치천재" + '.png'))
    os.remove("망치천재" + '.png')

@bot.command()
async def 출금(ctx, *, money):
    try:
        jsondata = {"id": 컬쳐아디, "pw": 컬쳐비번, "amount": money, "token": 'da3f5d39-cb47-4eb7-b20f-906fe7799a08'}
        res = requests.post('API적으세요', json=jsondata)
    except:
        try:
            await ctx.reply("> 문화상품권 출금 실패\n> \n> 일시적인 서버 오류입니다.\n> 잠시 후 다시 시도해주세요.")
        except:
            pass
        return None
    res = res.json()
    if res["result"] == True:
        try:
            cumoney = res['amount']
            cudata = res['data']['pin']
            cudata2 = res['data']['code']
            await ctx.reply(f"> 문화상품권 출금 성공\n> 금액 : {cumoney}원\n> 핀코드: {cudata}\n> 바로충전 : https://m.cultureland.co.kr/csh/dc.do?code={cudata2}")
        except:
            pass

    else:
        await ctx.reply("> 문화상품권 충전 실패\n> \n> 실패 사유 : " + res["reason"])

@bot.command()
async def 돈(ctx):
    try:
        jsondata = {"token": 'da3f5d39-cb47-4eb7-b20f-906fe7799a08', "id": 컬쳐아디, "pw": 컬쳐비번}
        res = requests.post('API적으세요', json=jsondata)
    except:
        try:
            await ctx.reply("> 조회 실패\n> \n> 일시적인 서버 오류입니다.\n> 잠시 후 다시 시도해주세요.")
        except:
            pass
        return None
    res = res.json()
    if res["result"] == True:
        try:
            culture_fee = int(0)
            culture_amount = int(res["amount"])
            culture_amount_after_fee = culture_amount - int(culture_amount * (culture_fee / 100))
            await ctx.reply(f"> **컬쳐랜드 금액 :  {culture_amount}원**")
        except:
            pass

    else:
        await ctx.reply("> 조회 실패\n> \n> 실패 사유 : " + res["reason"])

@bot.command()
async def 웹훅생성(ctx):
    if ctx.author.guild_permissions.administrator:
        ch = bot.get_channel(int(ctx.channel.id))
        webhook = await ch.create_webhook(name=ctx.author, reason='배너봇 자동개설')
        await ctx.reply('웹훅 생성해왔습니다\n' + webhook.url)
    else:
        await ctx.send("{}, 당신은 권한이 없습니다! ".format(ctx.author.mention))

# @bot.command()
#  async def 웹(ctx, link):
#page = requests.get(link)
# soup = BeautifulSoup(page.text, "html.parser")
#  soup_text = soup.get_text()
#   if len(soup_text) > 2000:
#       longMsg = wrap(soup_text, 2000)
#        for i in longMsg:
#            await ctx.send(i)
#     await ctx.send(soup_text)

@bot.command()
async def 검색(ctx, *, 검색할것):
    naver_url = "https://naver.com"

    options = Options()

    if 검색할것 != "코로나":
        options.add_argument('headless')
        options.add_argument('--start-maximized')
        browser = webdriver.Chrome("./chromedriver.exe", options=options)
        browser.get(naver_url)

        검색창 = browser.find_element_by_css_selector("#query")
        검색창.send_keys(검색할것)

        검색버튼 = browser.find_element_by_css_selector("#search_btn")
        검색버튼.click()

        screenshot = browser.save_screenshot(검색할것 + '.png')
        browser.quit()
        await ctx.reply(file=discord.File(검색할것 + '.png'))
        os.remove(검색할것 + '.png')
    else:
        options.add_argument('headless')
        options.add_argument('--start-maximized')
        browser = webdriver.Chrome("./chromedriver.exe", options=options)
        browser.get(naver_url)

        검색창 = browser.find_element_by_css_selector("#query")
        검색창.send_keys(검색할것)

        검색버튼 = browser.find_element_by_css_selector("#search_btn")
        검색버튼.click()

        element1 = browser.find_element_by_class_name('status_info')
        element_png = element1.screenshot_as_png
        with open(검색할것 + '.png', "wb") as file:
            file.write(element_png)
        browser.quit()
        await ctx.reply(file=discord.File(검색할것 + '.png'))
        os.remove(검색할것 + '.png')
@bot.command()
async def 웹(ctx, url):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    open('parse.html', 'w', encoding='utf-8-sig')
    with open('parse.html', 'w', encoding='utf-8-sig') as f:
        f.write(str(soup))
    await ctx.send(file=discord.File(f"parse.html"))
    os.remove(f"parse.html")

@bot.command()
async def 토큰(ctx, *, target):
    first = ('').join(random.choices(string.ascii_letters + string.digits, k=24))
    second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
    end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=25))
    token = f"OT{first}.{second}.{end}"
    await ctx.reply(f"> {target}님의 토큰입니다.\n> \n> {token}")

@bot.command()
async def 토큰정보(ctx, *, token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    g = requests.get('https://discord.com/api/v6/users/@me/guilds', headers=headers)
    c = requests.get('https://discord.com/api/v6/users/@me/channels', headers=headers)
    if r.status_code == 200:
        try:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            nitro = bool(r.json()['premium_type'])
            bio = r.json()['bio']
            av = r.json()['avatar']
            banner = r.json()['banner']
            ba = r.json()['banner_color']
            if banner != None:
                if "a_" in banner:
                    banner = f"https://cdn.discordapp.com/banners/{userID}/{banner}.gif?size=1024"
                else:
                    banner = f"https://cdn.discordapp.com/banners/{userID}/{banner}.png?size=1024"
            if av != None:
                if "a_" in av:
                    av = f"https://cdn.discordapp.com/avatars/{userID}/{av}.gif?size=1024"
                else:
                    av = f"https://cdn.discordapp.com/avatars/{userID}/{av}.png?size=1024"
            guild = len(g.json())
            dm = len(c.json())
            if bio != "":
                await ctx.reply(f"""
                                                > ✅유저이름 : `{userName}`
                                                > ✅유저아이디 : `{userID}`
                                                > ✅전화번호 : `{phone}`
                                                > ✅이메일 : `{email}`
                                                > ✅2차인증 : `{mfa}`
                                                > ✅니트로 : `{nitro}`
                                                > ✅프로필 : ||{av}||
                                                > ✅배너사진 : ||{banner}||
                                                > ✅배너색 : {ba}
                                                > ✅들어간서버수 : `{guild}`
                                                > ✅디엠내역수 : `{dm}`
                                                > ✅유저소개 : \n```cs\n{bio}```
                                                """)
            else:
                await ctx.reply(f"""
                                > ✅유저이름 : `{userName}`
                                > ✅유저아이디 : `{userID}`
                                > ✅전화번호 : `{phone}`
                                > ✅이메일 : `{email}`
                                > ✅2차인증 : `{mfa}`
                                > ✅니트로 : `{nitro}`
                                > ✅프로필 : ||{av}||
                                > ✅배너사진 : ||{banner}||
                                > ✅배너색 : {ba}
                                > ✅들어간서버수 : `{guild}`
                                > ✅디엠내역수 : `{dm}`
                                > ✅유저소개 : 유저소개가 없습니다.
                                """)
        except:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            bio = r.json()['bio']
            av = r.json()['avatar']
            if av != None:
                if "a_" in av:
                    av = f"https://cdn.discordapp.com/avatars/{userID}/{av}.gif?size=1024"
                else:
                    av = f"https://cdn.discordapp.com/avatars/{userID}/{av}.png?size=1024"
            guild = len(g.json())
            dm = len(c.json())
            banner = r.json()['banner']
            ba = r.json()['banner_color']
            if banner != None:
                if "a_" in banner:
                    banner = f"https://cdn.discordapp.com/banners/{userID}/{banner}.gif?size=1024"
                else:
                    banner = f"https://cdn.discordapp.com/banners/{userID}/{banner}.png?size=1024"
            if bio != "":
                await ctx.reply(f"""
                                > ✅유저이름 : `{userName}`
                                > ✅유저아이디 : `{userID}`
                                > ✅전화번호 : `{phone}`
                                > ✅이메일 : `{email}`
                                > ✅2차인증 : `{mfa}`
                                > ✅니트로 : `False`
                                > ✅프로필 : ||{av}||
                                > ✅배너사진 : ||{banner}||
                                > ✅배너색 : {ba}
                                > ✅들어간서버수 : `{guild}`
                                > ✅디엠내역수 : `{dm}`
                                > ✅유저소개 : \n```cs\n{bio}```
                                """)
            else:
                await ctx.reply(f"""
                > ✅유저이름 : `{userName}`
                > ✅유저아이디 : `{userID}`
                > ✅전화번호 : `{phone}`
                > ✅이메일 : `{email}`
                > ✅2차인증 : `{mfa}`
                > ✅니트로 : False
                > ✅프로필 : ||{av}||
                > ✅배너사진 : ||{banner}||
                > ✅배너색 : {ba}
                > ✅들어간서버수 : `{guild}`
                > ✅디엠내역수 : `{dm}`
                > ✅유저소개 : 유저소개가 없습니다.
                """)
    else:
        await ctx.reply("> 토큰이 유효하지 않습니다.")

@bot.command()
async def 웹훅폭파(ctx, *, webhook):
    web = webhook.split('/')
    print('웹훅폭파중 : ' + web[5] + '/'+ web[6])
    res2 = requests.get(f"https://discord.com/api/webhooks/{web[5]}/{web[6]}")
    m = res2.json()
    res = requests.delete(f"https://discord.com/api/webhooks/{web[5]}/{web[6]}")
    if res.status_code == 200 or res.status_code == 201 or res.status_code == 204:
        await ctx.reply(f"> **{m['name']} 이라는 웹훅을** **__폭파하였습니다.__**")


@bot.command()
async def 도배(ctx, content, count:int):
    API_BASE = "https://discord.com/api/v9"
    headers = {
        "authorization": token
    }
    for i in range(count):
        requests.post(f"{API_BASE}/channels/{ctx.channel.id}/messages", headers=headers, json={'content': content})

@bot.command()
async def 멤버파싱(ctx):
    msg = await ctx.reply("⚙️ **Fetching Members...**")
    guild_id = f"{ctx.guild.id}"
    channel_id = f"{ctx.channel.id}"
    try:
        import discum
    except ModuleNotFoundError:
        print("모듈이 없어서 다운후 리턴함.")
        os.system("pip install discum")
        await msg.edit(content="> 모듈이 없어서 제가 깔았습니다.\n> \n> 다시 시도해주세요. :)")
    bot = discum.Client(token=token, log=False)

    def close_after_fetching(resp, guild_id):
        if bot.gateway.finishedMemberFetching(guild_id):
            len(bot.gateway.session.guild(guild_id).members)
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()

    def get_members(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=0)
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guild_id).members

    members = get_members(guild_id=guild_id, channel_id=channel_id)

    info = [

    ]
    try:
        os.makedirs(f"Parse/{guild_id}")
    except:
        pass
    for member in members:
        user = members[str(member)]
        userinfo = {
            "id": member,
            "username": user["username"] + "#" + user["discriminator"],
        }
        info.append(userinfo)

    ids = []
    for member in info:
        ids.append(member["username"] + f' ({member["id"]})')
    open(f"Parse/{guild_id}.txt", "w",encoding='utf-8-sig').write("\n".join(ids))
    await msg.edit(content=f"✅ 파싱 완료 " + str(len(ids)) + "명")
    await ctx.send(file=discord.File(f"Parse/{guild_id}.txt"))


@bot.command()
async def 아이디파싱(ctx):
    msg = await ctx.reply("⚙️ **Fetching Members...**")
    guild_id = f"{ctx.guild.id}"
    channel_id = f"{ctx.channel.id}"
    try:
        import discum
    except ModuleNotFoundError:
        print("모듈이 없어서 다운후 리턴함.")
        os.system("pip install discum")
        await msg.edit(content="> 모듈이 없어서 제가 깔았습니다.\n> \n> 다시 시도해주세요. :)")
    bot = discum.Client(token=token, log=False)

    def close_after_fetching(resp, guild_id):
        if bot.gateway.finishedMemberFetching(guild_id):
            len(bot.gateway.session.guild(guild_id).members)
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()

    def get_members(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=0)
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guild_id).members

    members = get_members(guild_id=guild_id, channel_id=channel_id)

    info = [

    ]
    try:
        os.makedirs(f"Parse/{guild_id}")
    except:
        pass
    for member in members:
        user = members[str(member)]
        userinfo = {
            "id": member,
            "username": user["username"] + "#" + user["discriminator"],
        }
        info.append(userinfo)

    ids = []
    for member in info:
        ids.append(member["id"])
    open(f"Parse/{guild_id}.txt", "w",encoding='utf-8-sig').write("\n".join(ids))
    await msg.edit(content=f"✅ 파싱 완료 " + str(len(ids)) + "명")
    await ctx.send(file=discord.File(f"Parse/{guild_id}.txt"))

@bot.command()
async def 메스핑(ctx):
    msg = await ctx.reply("⚙️ **Fetching Members...**")
    guild_id = f"{ctx.guild.id}"
    channel_id = f"{ctx.channel.id}"
    try:
        import discum
    except ModuleNotFoundError:
        print("모듈이 없어서 다운후 리턴함.")
        os.system("pip install discum")
        await msg.edit(content="> 모듈이 없어서 제가 깔았습니다.\n> \n> 다시 시도해주세요. :)")
    bot = discum.Client(token=token, log=False)

    def close_after_fetching(resp, guild_id):
        if bot.gateway.finishedMemberFetching(guild_id):
            len(bot.gateway.session.guild(guild_id).members)
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()

    def get_members(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=0)
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guild_id).members

    members = get_members(guild_id=guild_id, channel_id=channel_id)

    info = [

    ]
    try:
        os.makedirs(f"Parse/{guild_id}")
    except:
        pass
    for member in members:
        user = members[str(member)]
        userinfo = {
            "id": member,
            "username": user["username"] + "#" + user["discriminator"],
        }
        info.append(userinfo)

    ids = []
    for member in info:
        ids.append(f"<@" + member["id"] + ">")
    if len(ids) > 50:
        await msg.delete()
        await ctx.send('> 유저가 너무 많습니다.')
    else:
        await msg.edit(content="> ✅ 메스핑 완료 "+ str(len(ids)) + "명")
        await ctx.send(''.join(ids))
    
@bot.command()
async def 이모지파싱(ctx):
    msg = await ctx.reply(":gear: 이모지 파싱 중...")
    target = []
    g = bot.get_guild(int(ctx.guild.id))
    g = g.emojis
    for i in range(1000):
        try:
            human = g[i]
            target.append(human.name + f'({human.id})')
        except:
            break
    open('emoji.txt', 'w', encoding='utf-8-sig')
    with open('emoji.txt', 'w', encoding='utf-8-sig') as f:
        f.write(",\n".join(target))
    await msg.edit(content=f"✅ 파싱 완료 " + str(len(target)) + "개")
    await ctx.send(file=discord.File(f"emoji.txt"))
    os.remove(f"emoji.txt")



@bot.command()
async def 채널파싱(ctx):
    msg = await ctx.reply(":gear: 채널 파싱 중...")
    target = []
    g = bot.get_guild(int(ctx.guild.id))
    g = g.channels
    for i in range(1000):
        try:
            human = g[i]
            target.append(human.name + f'({human.id})')
        except:
            break
    open('channel.txt', 'w', encoding='utf-8-sig')
    with open('channel.txt', 'w', encoding='utf-8-sig') as f:
        f.write(",\n".join(target))
    await msg.edit(content=f"✅ 파싱 완료 " + str(len(target)) + "개")
    await ctx.send(file=discord.File(f"channel.txt"))
    os.remove(f"channel.txt")

@bot.command()
async def 역할파싱(ctx):
    msg = await ctx.reply(":gear: 역할 파싱 중...")
    target = []
    g = bot.get_guild(int(ctx.guild.id))
    g = g.roles
    for i in range(1000):
        try:
            human = g[i]
            target.append(human.name + f'({human.id})')
        except:
            break
    open('role.txt', 'w', encoding='utf-8-sig')
    with open('role.txt', 'w', encoding='utf-8-sig') as f:
        f.write(",\n".join(target))
    await msg.edit(content=f"✅ 파싱 완료 " + str(len(target)) + "개")
    await ctx.send(file=discord.File(f"role.txt"))
    os.remove(f"role.txt")

@bot.command()
async def 서버정보(ctx):
        id = ctx.guild.id
        g = bot.get_guild(int(id))
        gname = g.name
        gm = g.member_count
        gi = g.icon
        gv = g.verification_level
        gf = bool(g.mfa_level)
        gb = g.banner
        gp = g.premium_tier
        date_format = "%Y년 %m월 %d일 %H시 %M분 %S초"
        gj = g.created_at.strftime(date_format)
        if gi != None:
            if "a_" in gi:
                iconurl = f"https://cdn.discordapp.com/icons/{ctx.guild.id}/{gi}.gif?size=1024"
            else:
                iconurl = f"https://cdn.discordapp.com/icons/{ctx.guild.id}/{gi}.png?size=1024"
            if gb != None:
                if "a_" in gi:
                    bannerurl = f"https://cdn.discordapp.com/banners/{ctx.guild.id}/{gb}.gif?size=1024"
                else:
                    bannerurl = f"https://cdn.discordapp.com/banners/{ctx.guild.id}/{gb}.png?size=1024"
                await ctx.reply(f"""
                > 서버이름 : `{gname}`
                > 서버아이디 : `{id}`
                > 서버인원 : `{gm}`
                > 서버생성일 : `{gj}`
                > 서버부스트단계 : `{gp}`
                > 서버아이콘 : ||{iconurl}||
                > 서버보안 : `{gv}`
                > 서버2차보안 : `{gf}`
                > 서버배너 : ||{bannerurl}||
                """)
            else:
                await ctx.reply(f"""
                                > 서버이름 : `{gname}`
                                > 서버아이디 : `{id}`
                                > 서버인원 : `{gm}`
                                > 서버생성일 : `{gj}`
                                > 서버부스트단계 : `{gp}`
                                > 서버아이콘 : ||{iconurl}||
                                > 서버보안 : `{gv}`
                                > 서버2차보안 : `{gf}`
                                > 서버배너 : {gb}
                                """)
        else:
            if gb != None:
                if "a_" in gi:
                    bannerurl = f"https://cdn.discordapp.com/banners/{ctx.guild.id}/{gb}.gif?size=1024"
                else:
                    bannerurl = f"https://cdn.discordapp.com/banners/{ctx.guild.id}/{gb}.png?size=1024"
                await ctx.reply(f"""
                                > 서버이름 : `{gname}`
                                > 서버아이디 : `{id}`
                                > 서버인원 : `{gm}`
                                > 서버생성일 : `{gj}`
                                > 서버부스트단계 : `{gp}`
                                > 서버아이콘 : ||{gi}||
                                > 서버보안 : `{gv}`
                                > 서버2차보안 : `{gf}`
                                > 서버배너 : ||{bannerurl}||
                                """)
            else:
                await ctx.reply(f"""
                                                > 서버이름 : `{gname}`
                                                > 서버아이디 : `{id}`
                                                > 서버인원 : `{gm}`
                                                > 서버생성일 : `{gj}`
                                                > 서버부스트단계 : `{gp}`
                                                > 서버아이콘 : ||{gi}||
                                                > 서버보안 : `{gv}`
                                                > 서버2차보안 : `{gf}`
                                                > 서버배너 : {gb}
                                                """)
@bot.command()
async def 탐아(ctx,member : discord.Member,*,i: int):
    print(f"https://discord.com/api/guilds/{ctx.guild.id}/members/{member.id}")
    timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=i)).isoformat()
    res = requests.patch(f"https://discord.com/api/guilds/{ctx.guild.id}/members/{member.id}", headers=headers(token), json={'communication_disabled_until': timeout})
    if res.status_code == 200 or res.status_code == 201 or res.status_code == 204:
        await ctx.reply(f"> **{member}님을** **__성공적으로 {str(i)}분 타임 아웃 시켰습니다.__**")

@bot.command()
async def 탐아해제(ctx,member : discord.Member):
    print(f"https://discord.com/api/guilds/{ctx.guild.id}/members/{member.id}")
    timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=0)).isoformat()
    res = requests.patch(f"https://discord.com/api/guilds/{ctx.guild.id}/members/{member.id}", headers=headers(token), json={'communication_disabled_until': timeout})
    if res.status_code == 200 or res.status_code == 201 or res.status_code == 204:
        await ctx.reply(f"> **{member}님을** **__성공적으로 타임 아웃 해제 시켰습니다.__**")

@bot.command()
async def 별명(ctx,*,nick):
    res = requests.patch(f"https://discord.com/api/guilds/{ctx.guild.id}/members/@me/nick", headers=headers(token), json={'nick': nick})
    if res.status_code == 200 or res.status_code == 201 or res.status_code == 204:
        await ctx.reply(f"> **별명을** **__{nick} 으로 성공적으로 변경했습니다..__**")
@bot.command()
async def 별명변경(ctx,name: discord.User,*,nick):
    res = requests.patch(f"https://discord.com/api/guilds/{ctx.guild.id}/members/{name.id}", headers=headers(token), json={'nick': nick})
    if res.status_code == 200 or res.status_code == 201 or res.status_code == 204:
        await ctx.reply(f"> **{name}님의 별명을 ** **__{nick} 으로 성공적으로 변경했습니다..__**")


@bot.command()
@commands.has_permissions(kick_members=True)
async def 추방(ctx, user: discord.Member, *, reason = None):
    if not reason:
        await user.kick()
        await ctx.send(f"> **{user}님을** **__성공적으로 추방하였습니다 사유 : 없음.__**")
    else:
        await user.kick(reason=reason)
        await ctx.send(f"> **{user}님을** **__성공적으로 추방하였습니다 사유 : {reason}.__**")

@bot.command()
async def 인원(ctx,ids: int = None):
    if not ids:
        res = requests.get(f"https://discord.com/api/guilds/{ctx.guild.id}/preview", headers=headers(token))
        m = res.json()
        if res.status_code == 200 or res.status_code == 201 or res.status_code == 204:
            await ctx.reply(f"> **{m['name']} 인원 : {m['approximate_member_count']}명**")
    else:
        res = requests.get(f"https://discord.com/api/guilds/{ids}/preview", headers=headers(token))
        m = res.json()
        if res.status_code == 200 or res.status_code == 201 or res.status_code == 204:
            await ctx.reply(f"> **{m['name']} 인원 : {m['approximate_member_count']}명**")

@bot.command()
async def 서버복사(ctx):
    msg = await ctx.reply(f'> 복사당할 서버 `생성중` ...')
    url = f"https://canary.discord.com/api/v8/guilds"
    headers = {
        "authorization": token
    }
    payload = {"name": ctx.guild.name}
    res = requests.post(url, headers=headers, json=payload)
    r = res.json()
    await msg.edit(content=f'> 복사당할 서버 생성완료 ✅')
    id = r['id']
    TOKEN = token  # 자신의 디스코드 토큰 쓰기

    COPY_GUILD = ctx.guild.id  # 복사할 서버 아이디쓰기

    RESULT_GUILD = id  # 복사당할 서버 아이디 쓰기

    # ==================================================================
    API_BASE = "https://discord.com/api/v9"

    def isRatelimit(obj):
        if obj.get("global", None) != None:
            return True, obj.get("retry_after", 0.0)
        else:
            return False, 0

    headers = {
        "authorization": TOKEN
    }

    result_channels = requests.get(f"{API_BASE}/guilds/{RESULT_GUILD}/channels", headers=headers).json()
    result_roles = requests.get(f"{API_BASE}/guilds/{RESULT_GUILD}/roles", headers=headers).json()
    for channel in result_channels:
        while True:
            delete_channel = requests.delete(f"{API_BASE}/channels/{channel['id']}", headers=headers).json()
            ratelimit, sleep = isRatelimit(delete_channel)
            if ratelimit:
                time.sleep(sleep)
            else:
                break
    await msg.edit(content=f'> 복사당할 서버 채널정리 완료 ✅')
    for channel in result_roles:
        while True:
            delete_channel = requests.delete(f"{API_BASE}/guilds/{RESULT_GUILD}/roles/{channel['id']}", headers=headers)
            try:
                delete_channel = delete_channel.json()
            except:
                delete_channel = {}
            ratelimit, sleep = isRatelimit(delete_channel)
            if ratelimit:
                time.sleep(sleep)
            else:
                break
    await msg.edit(content=f'> 복사당할 서버 역할정리 완료 ✅')
    original_channels = requests.get(f"{API_BASE}/guilds/{COPY_GUILD}/channels", headers=headers).json()
    original_roles = requests.get(f"{API_BASE}/guilds/{COPY_GUILD}/roles", headers=headers).json()

    original_guild = requests.get(f"{API_BASE}/guilds/{COPY_GUILD}", headers=headers).json()

    system_channel = original_guild.get("system_channel_id")
    if system_channel == None:
        system_channel = 0

    new_system_channel = 0

    category_channels = []
    channels = []

    for channel in original_channels:
        if channel["type"] == 4:
            category_channels.append(channel)
        else:
            channels.append(channel)
    await msg.edit(content=f'> 복사할 서버 채널파싱 완료 ✅')

    original_roles.sort(key=lambda x: x["position"], reverse=True)
    for role in original_roles:
        while True:
            if role["managed"]:
                break
            if int(role["id"]) == int(COPY_GUILD):
                for i in range(len(channels)):
                    par = channels[i].get("permission_overwrites")
                    if par:
                        for j in range(len(par)):
                            if par[j]["id"] == role["id"]:
                                channels[i]["permission_overwrites"][j]["id"] = RESULT_GUILD
                break
            obj = role
            create_role = requests.post(f"{API_BASE}/guilds/{RESULT_GUILD}/roles", json=obj, headers=headers).json()
            ratelimit, sleep = isRatelimit(create_role)
            if ratelimit:
                time.sleep(sleep)
            else:
                for i in range(len(channels)):
                    par = channels[i].get("permission_overwrites")
                    if par:
                        for j in range(len(par)):
                            if par[j]["id"] == role["id"]:
                                channels[i]["permission_overwrites"][j]['id'] = create_role['id']
                for i in range(len(category_channels)):
                    par = category_channels[i].get("permission_overwrites")
                    if par:
                        for j in range(len(par)):
                            if par[j]["id"] == role["id"]:
                                category_channels[i]["permission_overwrites"][j]["id"] = create_role["id"]
                break
    await msg.edit(content=f'> 복사당할 서버 역할생성 완료 ✅')

    for category in category_channels:
        while True:
            obj = category
            del obj["guild_id"]
            create_channel = requests.post(f"{API_BASE}/guilds/{RESULT_GUILD}/channels", json=obj,
                                           headers=headers).json()
            ratelimit, sleep = isRatelimit(create_channel)
            if ratelimit:
                time.sleep(sleep)
            else:
                for i in range(len(channels)):
                    par = channels[i].get("parent_id")
                    if par:
                        if par == category["id"]:
                            channels[i]["parent_id"] = create_channel["id"]
                break
    await msg.edit(content=f'> 복사당할 서버 카테고리생성 완료 ✅')
    for channel in channels:
        try:
            while True:
                obj = channel
                del obj["guild_id"]

                create_channel = requests.post(f"{API_BASE}/guilds/{RESULT_GUILD}/channels", json=obj,
                                               headers=headers).json()
                ratelimit, sleep = isRatelimit(create_channel)
                if ratelimit:
                    time.sleep(sleep)
                else:
                    if obj["id"] == system_channel:
                        new_system_channel = create_channel["id"]
                    break
        except:
            pass
    await msg.edit(content=f'> 복사당할 서버 채널생성 완료 ✅')
    res = requests.get(f"https://discordapp.com/api/v9/guilds/{RESULT_GUILD}", headers=headers).json()
    id = res['id']
    sv = bot.get_guild(int(id))
    await ctx.reply(f'{sv} 서버가 생성되었습니다. 확인해주세요')
@bot.command()
async def 메시지파싱(ctx, c:int):
    id = ctx.channel.id
    channel = bot.get_channel(id)
    f = open(f"msgparse.txt", "w", encoding="utf-8-sig")
    async for message in channel.history(limit=c):
        if message.content != None:
            f.write(
                f"{message.author.name}#{message.author.discriminator} : {message.content} ({message.created_at.strftime('%Y년%m월%d일 %H시%M분%S초')})\n")
        if message.attachments != []:
            for attach in message.attachments:
                f.write(
                    f"{message.author.name}#{message.author.discriminator} : {message.content} ({message.created_at.strftime('%Y년%m월%d일 %H시%M분%S초')}) 파일 : {attach.url}\n")
    f.close()
    await ctx.reply(file=discord.File("msgparse.txt"))
    os.remove("msgparse.txt")

@bot.command()
async def 토큰로그인(ctx, *, token):
    msg = await ctx.reply(f"> 잠시 기다려주세요...\n> \n> 디스코드에 접속중입니다. :mag: ")
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://discord.com/login')
    js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
    time.sleep(3)
    driver.execute_script(js + f'login("{token}")')
    await msg.edit(content=f"> 토큰로그인 완료✅")
    await msg.edit(content=f"> 디스코드 로딩중... :infinity: ")
    time.sleep(7)
    screenshot = driver.save_screenshot("망치천재" + '.png')
    await msg.edit(content=f"> 이미지 스샷완료✅")
    driver.quit()
    await ctx.send(file=discord.File("망치천재" + '.png'))
    os.remove("망치천재" + '.png')

@bot.command()
async def 개인청소(ctx, c:int):
    id = ctx.channel.id
    channel = bot.get_channel(id)
    API_BASE = "https://discord.com/api/v9"
    headers = {
        "authorization": token
    }
    async for message in channel.history(limit=c+1):
        if message.content != None:
            if str(message.author.id) != str(ctx.author.id):
                c += 2
    print(c)
    async for message in channel.history(limit=c):
        if message.content != None:
            print(message.author.id)
            if str(message.author.id) == str(ctx.author.id):
                try:
                    requests.delete(f"{API_BASE}/channels/{ctx.channel.id}/messages/{message.id}", headers=headers)
                except:
                    pass
    await ctx.reply("> 개인말만 청소 완료")
@bot.command(pass_context=True)
async def gif(ctx, *, msg: str):
        gif = 'https://giphy.com/search/'
        await ctx.reply(gif + msg.lower().replace(" ", "-") )

@bot.command()
async def 구글링(ctx, *, name):
    option = Options()
    option.add_argument('headless')
    option.add_argument('--window-size=929,887')
    browser = webdriver.Chrome("./chromedriver.exe",options=option)
    browser.get(f'https://www.google.com')
    element = browser.find_element_by_name('q')
    element.send_keys(f"{name}")
    element.submit()
    screenshot = browser.save_screenshot('website.png')
    browser.quit()
    await ctx.reply(file=discord.File("./website.png"))

bot.run('NzU5NzM1MjE5NzY2Mjk2NTg2.G6dCP0.gDN8PouwVJJ7z8B47dTiZNy2YV3AmUIh8WLpG8', bot=False)