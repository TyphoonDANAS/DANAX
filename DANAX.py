# Work with Python 3.6
import asyncio
import discord
import random
import youtube_dl
import datetime
from os import system

system("title "+"DANAX")

TOKEN = os.environ["BOT_TOKEN"]

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    # 본인의 메시지에 답변을 하지 않음.
    fr = "~"
    if message.author == client.user:
        return

    if message.content.startswith(fr + '다낙스'):
        msg = ' {0.author.mention}, ㅎㅇ!'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith(fr + '버전'):
        msg = '버전: 당신의 버전'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(fr + '상태'):
        text = message.content
        rpl = text.replace(fr + "상태", "")
        await client.change_presence(game=discord.Game(name=rpl))
        msg = '상태 메시지가 바뀌었습니다.'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(fr + '열대저기압'):
        msg = '북서 태평양(태풍):`열대폭풍 풍웡`-45kts(TS)\n북 대서양(허리케인):`열대폭풍 세바스천`-50kts(TS)'.format(message)
        await client.send_message(message.channel, msg)

    if message.content==(fr + '가위'):
        str1 = ['가위','바위','보']
        r = random.choice(str1)
        if r == '가위':
            await client.send_message(message.channel, "님은 가위, DANAX는 " + r + "를 선택했다..." + "\n비겼다...")
        elif r == '바위':
            await client.send_message(message.channel, "님은 가위, DANAX는 " + r + "를 선택했다..." + "\n졌다 ㅋ")
        elif r == '보':
            await client.send_message(message.channel, "님은 가위, DANAX는 " + r + "를 선택했다..." + "\n이겼다 ㅠ")

    elif message.content==(fr + '바위'):
        str1 = ['가위','바위','보']
        r = random.choice(str1)
        if r == '바위':
            await client.send_message(message.channel, "님은 바위, DANAX는 " + r + "를 선택했다..." + "\n비겼다...")
        elif r == '보':
            await client.send_message(message.channel, "님은 바위, DANAX는 " + r + "를 선택했다..." + "\n졌다 ㅋ")
        elif r == '가위':
            await client.send_message(message.channel, "님은 바위, DANAX는 " + r + "를 선택했다..." + "\n이겼다 ㅠ")

    if message.content==(fr + '보'):
        str1 = ['가위','바위','보']
        r = random.choice(str1)
        if r == '보':
            await client.send_message(message.channel, "님은 보, DANAX는 " + r + "를 선택했다..." + "\n비겼다...")
        elif r == '가위':
            await client.send_message(message.channel, "님은 보, DANAX는 " + r + "를 선택했다..." + "\n졌다 ㅋ")
        elif r == '바위':
            await client.send_message(message.channel, "님은 보, DANAX는 " + r + "를 선택했다..." + "\n이겼다 ㅠ")

    if message.content==(fr + '도움'):
       embed = discord.Embed(title="DANAX 도움말", description="**~다낙스**:가벼운 인사를 건넵니다.\n**~가위/바위/보**:DANAX와 가위바위보를 합니다.\n**~열대저기압**:현재 활동 중인 열대저기압 정보를 알려줍니다.", color=0x00faf4)
       await client.send_message(message.channel, embed=embed)
     
    if message.content.startswith(fr + '주사위'):

        randomNum = random.randrange(1, 7) 
        print(randomNum)
        if randomNum == 1:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:', color=0x00faf4))
        if randomNum == 2:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:', color=0x00faf4))
        if randomNum ==3:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:', color=0x00faf4))
        if randomNum ==4:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:', color=0x00faf4))
        if randomNum ==5:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:', color=0x00faf4))
        if randomNum ==6:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: ', color=0x00faf4))

    
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="명령어는 `~도움`을 통해서 알아보세요!"))
    print('다음 계정으로 로그인됨:')
    print(client.user.name)
    print(client.user.id)
    print('--- 동작 중 ---')

client.run(TOKEN)
