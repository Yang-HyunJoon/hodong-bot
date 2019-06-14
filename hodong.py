import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import aiohttp
import string
import random
import openpyxl
import datetime
import command
import os



client = discord.Client()


@client.event
async def on_ready():
    print("[호동 BOT]의 동작 준비 중..")
    print("[호동 BOT]의 동작을 시작합니다.")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='#도움말', type=1))

@client.event
async def on_message(message):
    if message.content.startswith("호동"):
        await client.send_message(message.channel, "[호동 BOT] 호동이 불러쪄?")
        Filehodong = '호동.png'
        await client.send_file(message.channel, Filehodong)

    if message.content.startswith("!호스팅"):
        await client.send_message(message.channel, "[호동 BOT] Source Hub.Hosting on 192.168.0.16")

    if message.content.startswith("원유하"):
        await client.send_message(message.channel, "[호동 BOT] 검색결과 1건을 찾았습니다.")
        Filewyh = '원유하.jpg'
        await client.send_file(message.channel, Filewyh)

    if message.content.startswith("강재현"):
        await client.send_message(message.channel, "[호동 BOT] 검색결과 1건을 찾았습니다.")
        Filekjh = '강재현.png'
        await client.send_file(message.channel, Filekjh)

    if message.content.startswith("푸라면"):
        await client.send_message(message.channel, "[호동 BOT] 검색결과 92,384,672건을 찾았습니다.")
        Filesinramen = '신라면.jpg'
        await client.send_file(message.channel, Filesinramen)

    if message.content.startswith("!reload"):
        await client.send_message(message.channel, "[호동 BOT] 관리자 권한 확인 중..")
        await client.send_message(message.channel, "[호동 BOT] RELOADING...")

    if message.content.startswith("!ID"):
        await client.send_message(message.channel, "[호동 BOT] 관리자 권한 확인 중..")
        await client.send_message(message.channel, "[호동 BOT] SEARCHING...")
        file = open("X아이디.txt")
        await client.send_message(message.channel, file.read())
        file.close()
        
    if message.content.startswith("채팅청소"):
        await client.send_message(message.channel, "#채팅청소")

    if message.content.startswith("시발"):
        await client.send_message(message.channel, "#채팅청소")
        await client.send_message(message.channel, "[호동 BOT] 비속어 감지: 욕은 나쁜거야")

    if message.content.startswith("씨발"):
        await client.send_message(message.channel, "#채팅청소")
        await client.send_message(message.channel, "[호동 BOT] 비속어 감지: 욕은 나쁜거야")

    if message.content.startswith("ㅅㅂ"):
        await client.send_message(message.channel, "#채팅청소")
        await client.send_message(message.channel, "[호동 BOT] 비속어 감지: 욕은 나쁜거야")

    if message.content.startswith("존나"):
        await client.send_message(message.channel, "#채팅청소")
        await client.send_message(message.channel, "[호동 BOT] 비속어 감지: 욕은 나쁜거야")

    if message.content.startswith("닥쳐"):
        await client.send_message(message.channel, "#채팅청소")
        await client.send_message(message.channel, "[호동 BOT] 비속어 감지: 욕은 나쁜거야")

    if message.content.startswith("병신"):
        await client.send_message(message.channel, "#채팅청소")
        await client.send_message(message.channel, "[호동 BOT] 비속어 감지: 욕은 나쁜거야")

    if message.content.startswith("ㄴㄱㅁ"):
        await client.send_message(message.channel, "#채팅청소")
        await client.send_message(message.channel, "[호동 BOT] 비속어 감지: 패드립은 나쁜거야")

    if message.content.startswith("ㄴㅇㅁ"):
        await client.send_message(message.channel, "#채팅청소")
        await client.send_message(message.channel, "[호동 BOT] 비속어 감지: 패드립은 나쁜거야")

    if message.content.startswith("느금마"):
        await client.send_message(message.channel, "#채팅청소")
        await client.send_message(message.channel, "[호동 BOT] 비속어 감지: 패드립은 나쁜거야")

    if message.content.startswith("니애미"):
        await client.send_message(message.channel, "#채팅청소")
        await client.send_message(message.channel, "[호동 BOT] 비속어 감지: 패드립은 나쁜거야")

    if message.content.startswith("개새끼"):
        await client.send_message(message.channel, "#채팅청소")
        await client.send_message(message.channel, "[호동 BOT] 비속어 감지: 패드립은 나쁜거야")

    if message.content.startswith("사랑해"):
        await client.send_message(message.channel, "[호동 BOT] :heart_exclamation: 저도 사랑해요 :heart_exclamation: ")

    if message.content.startswith("안녕"):
        await client.send_message(message.channel, "[호동 BOT] 안녕하세요 :D (#도움말 입력)")

    if message.content.startswith("!import"):
        await client.send_message(message.channel, "[호동 BOT] 검색: 12 개의 구문 검색: import List: discord, discord.ext, asyncio, aiohttp, string, random, commands, discord.ext.commands, bot creative AND datetime")

    if message.content.startswith("!token"):
        await client.send_message(message.channel, "[호동 BOT] 다음 코드를 사용하세요: 호동, NTUxNDAwMjMzOTk3Njk3MDI2.D1zN6g.99cc_pP4WMB-dG32_DWyq5HTGSQ")

    if message.content.startswith("!초대링크"):
        await client.send_message(message.channel, "[호동 BOT] 호동봇의 초대링크: https://discordapp.com/oauth2/authorize?client_id=551400233997697026&scope=bot")

    if message.content.startswith('!현준상태설정'):
        a = datetime.datetime.today().month
        b = datetime.datetime.today().day
        c = datetime.datetime.today().hour
        d = datetime.datetime.today().minute
        learn = message.content.replace('!현준상태설정', str(a) + "월 " + str(b) + "일 " + str(c) + "시 " + str(d) + "분 기준)                                                               현준 님의 현재 상태 ▷▶ ")
        file = open("양현준_hodong_memo.txt", "w")
        file.write(learn)
        file.close()
        await client.send_message(message.channel, "[호동 BOT] (현준) 님의 상태가 갱신되었어요!")

    if message.content.startswith('!준호상태설정'):
        a = datetime.datetime.today().month
        b = datetime.datetime.today().day
        c = datetime.datetime.today().hour
        d = datetime.datetime.today().minute
        learn = message.content.replace('!준호상태설정', str(a) + "월 " + str(b) + "일 " + str(c) + "시 " + str(d) + "분 기준)                                                               준호 님의 현재 상태 ▷▶ ")
        file = open("정준호_hodong_memo.txt", "w")
        file.write(learn)
        file.close()
        await client.send_message(message.channel, "[호동 BOT] (준호) 님의 상태가 갱신되었어요!")

    if message.content.startswith('!재연상태설정'):
        a = datetime.datetime.today().month
        b = datetime.datetime.today().day
        c = datetime.datetime.today().hour
        d = datetime.datetime.today().minute
        learn = message.content.replace('!재연상태설정', str(a) + "월 " + str(b) + "일 " + str(c) + "시 " + str(d) + "분 기준)                                                               재연 님의 현재 상태 ▷▶ ")
        file = open("이재연_hodong_memo.txt", "w")
        file.write(learn)
        file.close()
        await client.send_message(message.channel, "[호동 BOT] (재연) 님의 상태가 갱신되었어요!")

    if message.content.startswith('!기철상태설정'):
        a = datetime.datetime.today().month
        b = datetime.datetime.today().day
        c = datetime.datetime.today().hour
        d = datetime.datetime.today().minute
        learn = message.content.replace('!기철상태설정', str(a) + "월 " + str(b) + "일 " + str(c) + "시 " + str(d) + "분 기준)                                                               기철 님의 현재 상태 ▷▶ ")
        file = open("손기철_hodong_memo.txt", "w")
        file.write(learn)
        file.close()
        await client.send_message(message.channel, "[호동 BOT] (기철) 님의 상태가 갱신되었어요!")
 
    if message.content.startswith('!재현상태설정'):
        a = datetime.datetime.today().month
        b = datetime.datetime.today().day
        c = datetime.datetime.today().hour
        d = datetime.datetime.today().minute
        learn = message.content.replace('!재현상태설정', str(a) + "월 " + str(b) + "일 " + str(c) + "시 " + str(d) + "분 기준)                                                               재현 님의 현재 상태 ▷▶ ")
        file = open("강재현_hodong_memo.txt", "w")
        file.write(learn)
        file.close()
        await client.send_message(message.channel, "[호동 BOT] (재현) 님의 상태가 갱신되었어요!")

    if message.content.startswith('!병우상태설정'):
        a = datetime.datetime.today().month
        b = datetime.datetime.today().day
        c = datetime.datetime.today().hour
        d = datetime.datetime.today().minute
        learn = message.content.replace('!병우상태설정', str(a) + "월 " + str(b) + "일 " + str(c) + "시 " + str(d) + "분 기준)                                                               병우 님의 현재 상태 ▷▶ ")
        file = open("윤병우_hodong_memo.txt", "w")
        file.write(learn)
        file.close()
        await client.send_message(message.channel, "[호동 BOT] (병우) 님의 상태가 갱신되었어요!")

        
    if message.content.startswith('!유하상태설정'):
        await client.send_message(message.channel, "[호동 BOT] [ERROR] This command is not registered ; Please Contact the admin or discord bot.")

    if message.content.startswith('!재민상태설정'):
        await client.send_message(message.channel, "[호동 BOT] [ERROR] This command is not registered ; Please Contact the admin or discord bot.")

    if message.content.startswith('!준일상태설정'):
        await client.send_message(message.channel, "[호동 BOT] [ERROR] This command is not registered ; Please Contact the admin or discord bot.")
                    
    if message.content.startswith('현준'):
        file = open("양현준_hodong_memo.txt")
        await client.send_message(message.channel, file.read())
        file.close()
    
    if message.content.startswith('재연'):
        file = open("이재연_hodong_memo.txt")
        await client.send_message(message.channel, file.read())
        file.close()

    if message.content.startswith('준호'):
        file = open("정준호_hodong_memo.txt")
        await client.send_message(message.channel, file.read())
        file.close()

    if message.content.startswith('재현'):
        file = open("강재현_hodong_memo.txt")
        await client.send_message(message.channel, file.read())
        file.close()

    if message.content.startswith('기철'):
        file = open("손기철_hodong_memo.txt")
        await client.send_message(message.channel, file.read())
        file.close()

    if message.content.startswith('병우'):
        file = open("윤병우_hodong_memo.txt")
        await client.send_message(message.channel, file.read())

    if message.content.startswith("!상태초기화"):
        await client.send_message(message.channel, "[호동 BOT] 유저의 상태 초기화 중.. (대상: ALL)")
        learn = message.content.replace('!상태초기화', "")
        file = open("양현준_hodong_memo.txt", "w")
        file.write(learn)
        file.close()
        file = open("정준호_hodong_memo.txt", "w")
        file.write(learn)
        file.close()
        file = open("이재연_hodong_memo.txt", "w")
        file.write(learn)
        file.close()
        file = open("강재현_hodong_memo.txt", "w")
        file.write(learn)
        file.close()
        file = open("손기철_hodong_memo.txt", "w")
        file.write(learn)
        file.close()
        file = open("윤병우_hodong_memo.txt", "w")
        file.write(learn)
        file.close()
        await client.send_message(message.channel, "[호동 BOT] 유저의 상태가 초기화되었습니다. (대상: ALL)")
        
    if message.content.startswith('!호동상태설정'):
        learn = message.content.replace('!호동상태설정', "")
        await client.change_presence(game=discord.Game(name=learn))
        await client.send_message(message.channel, "[호동 BOT] 봇의 상태가 변경되었습니다..")

    if message.content.startswith("!이용약관"):
        file = open("X이용약관.txt")
        await client.send_message(message.channel, file.read())
        file.close()

    if message.content.startswith("현충일"):
        await client.send_message(message.channel, "[호동 BOT] 현충일 검색결과:")
        file = open("X현충일.txt")
        await client.send_message(message.channel, file.read())
        file.close()


    if message.content.startswith("!시간"):
        a = datetime.datetime.today().month
        b = datetime.datetime.today().day
        c = datetime.datetime.today().hour
        d = datetime.datetime.today().minute
        e = datetime.datetime.today().second
        await client.send_message(message.channel, str(a) + "월 " + str(b) + "일의 현재시간은 " + str(c) + "시 " + str(d) + "분 " + str(e) + "초 입니다. (Seoul, GMT +9) ")

    if message.content.startswith("!패치노트"):
        await client.send_message(message.channel, "[호동 BOT] show ('hodong_patchnote')")
        file = open("hodong_patchnote.txt")
        await client.send_message(message.channel, file.read())
        file.close()

    if message.content.startswith("뭐먹지"):
        food = "집밥 짜장면 라면 떡볶이 치킨 냉면 굶어 피자"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith("라면"):
        ramen = "신라면 안성탕면 스낵면 너구리 짜빠게티 팔도비빔면 불닭볶음면 열라면 오징어짬뽕 진라면 진짬뽕 삼양라면 참깨라면 왕뚜껑 육개장"
        ramenchoice = ramen.split(" ")
        ramennumber = random.randint(1, len(ramenchoice))
        ramenresult = ramenchoice[ramennumber-1]
        await client.send_message(message.channel, ramenresult)

access_token = os.environ["BOT_TOKEN"]
client.run('NTUxNDAwMjMzOTk3Njk3MDI2.D1zN6g.99cc_pP4WMB-dG32_DWyq5HTGSQ')
