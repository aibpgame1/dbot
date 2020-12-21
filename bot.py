import discord
import asyncio
import os
from discord.ext import commands
import urllib
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from urllib.parse import quote
from urllib.parse import quote_plus
from urllib.parse import unquote
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import requests
import re
import warnings
import requests
import time
import youtube_dl
import datetime
import random
import requests
from discord import Game
import time
import json
import re
import lxml.html
import warnings
import requests
import unicodedata
import collections
from tqdm import tqdm

location = '대구'
a = 0

client = commands.Bot(command_prefix='잡냥아 ')

@client.command()
async def 잡냥아(ctx):
    responses = [
        "냥!!",
        "왜 부르냥?",
        "무슨일 있냥?",
        "냥냥? 왜그러냥?"
        ]
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def 호감도(ctx):
    await ctx.send('지금 잡냥이는 서버에 대한 호감도를 이만큼이나 가지고 있어요!')
    await ctx.send(a)

@client.command(aliases=['하이', '반가워' ,'헬로', 'ㅎㅇ'])
async def 안녕(ctx):
    await ctx.send('안녕하세요!! 저는 잡것냥냥이 입니다냥~!')
    print('인사 완료')

@client.command()
async def 코로나(ctx):
    await ctx.send('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=!')
    print('코로나')

@client.command()
async def 시간(ctx):
    secs = time.time()
    tm = time.localtime(secs)
    string = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)
    await ctx.send(string)
    print('시간')

@client.command()
async def 네이버(ctx):
    await ctx.send('http://naver.com/')
    print('네이버')

@client.command()
async def 구글(ctx):
    await ctx.send('https://google.com/')
    print('구글')

@client.command(aliases=['랜덤숫자', '랜숫', '숫자'])
async def lotto(ctx):
    responses = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10"
]

    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def 사랑해(ctx):
    responses = [
        "저도 사랑해요 주인님ㅎㅎ 냥냥냥",
        "저두 집사님을 무척 사랑한답니다냥!",
        "집사냥이 그렇게 말하니 어쩔줄 모르겠다냥!",
        "집사냥이 그래주면 나야 고맙다냥!",
        "이상한 사람이다냥! 나는 로봇이다냥!",
        "나 이제 태어난지 7일정도 됬다냥..?",
        "괜찮냥?",
        "아프냥?",
        "문제있냥?",
        "불쌍하냥 ㅠㅠ"
]

    await ctx.send(f'{random.choice(responses)}')
    global a
    a = a + 1
    await ctx.send('```호감도 + 1```')
    print('호감도 증가')

@client.command(aliases=['꺼져', '개새끼' ,'니엄마', 'ㅗㅗ'])
async def 시발(ctx):
    responses = [
        "말이 너무 심한거 아니냥?ㅠㅠ 개발자가 널 제제할 것이다냥 본 발언은 변수로서 저장되며 개발자에게 자동으로 전송된다냥 잡냥아 미안해 라고 한다면 용서를 고려해 볼 수 있다냥",
        "너 말이 너무 심하다냥 개발자가 널 제제할 것이다냥 본 발언은 변수로서 저장되며 개발자에게 자동으로 전송된다냥 잡냥아 미안해 라고 한다면 용서를 고려해 볼 수 있다냥",
        "말을 어떻게 그렇게 할 수 있냥? 개발자가 널 제제할 것이다냥 본 발언은 변수로서 저장되며 개발자에게 자동으로 전송된다냥 잡냥아 미안해 라고 한다면 용서를 고려해 볼 수 있다냥",
        "선넘지 마라냥 개발자가 널 제제할 것이다냥 본 발언은 변수로서 저장되며 개발자에게 자동으로 전송된다냥 잡냥아 미안해 라고 한다면 용서를 고려해 볼 수 있다냥",
        "그만하라냥 개발자가 널 제제할 것이다냥 본 발언은 변수로서 저장되며 개발자에게 자동으로 전송된다냥 잡냥아 미안해 라고 한다면 용서를 고려해 볼 수 있다냥",
        "감당되냥? 개발자가 널 제제할 것이다냥 본 발언은 변수로서 저장되며 개발자에게 자동으로 전송된다냥 잡냥아 미안해 라고 한다면 용서를 고려해 볼 수 있다냥",
]

    await ctx.send(f'{random.choice(responses)}')
    global a
    a = a - 10
    await ctx.send('```호감도 - 10```')
    print('호감도 하락 욕설')

@client.command(aliases=['사과할께', '다시는안그럴께' ,'미안', '잘못했어'])
async def 미안해(ctx):
    responses = [
        "딱 한번만 봐주겠다냥 하지만 너의 그 나쁜 행동은 이미 변수로서 기록되었다냥 한번만 더 그러면 가중처벌이다냥",
        "알겠다냥 마지막 기회다냥 하지만 너의 그 나쁜 행동은 이미 변수로서 기록되었다냥 한번만 더 그러면 가중처벌이다냥",
        "딱 한번만 용서해주겠다냥 하지만 너의 그 나쁜 행동은 이미 변수로서 기록되었다냥 한번만 더 그러면 가중처벌이다냥",
        "다시는 사과할 행동을 하지 말라냥 하지만 너의 그 나쁜 행동은 이미 변수로서 기록되었다냥 한번만 더 그러면 가중처벌이다냥",
        "지금이라도 사과해서 고맙다냥 하지만 너의 그 나쁜 행동은 이미 변수로서 기록되었다냥 한번만 더 그러면 가중처벌이다냥"
        ]
    await ctx.send(f'{random.choice(responses)}')
    global a
    a = a + 0.5
    await ctx.send('```호감도 + 0.5```')
    print('호감도 상승 사과')

@client.command()
async def 출석해줘(ctx):
    await ctx.send('니 출석을 왜 나한테 하냐 시발냥')
    await ctx.channel.purge(limit=1)
    await ctx.send('네 집사냥! 출석 감사드린다냥~')
    print('출석완료')

@client.command()
async def 출석초기화(ctx):
    await ctx.channel.purge(limit=100)
    await ctx.send('출석을 초기화 했습니다')
    print('개소리완료')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='귀여운 잡것 냥냥이의 그루밍을 받는중'))
    print('ready')

client.run('Nzg5OTMwNTAwOTYxMzM3Mzg0.X95OGw.hihXsOH-BTPJjrgU17Gy88uY6ss')