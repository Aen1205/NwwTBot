import discord


client = discord.Client()


@client.event
async def on_ready():
    print("로그인")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='24시간용 봇', type=1))


@client.event
async def on_message(message):
    if message.content.startswith("앤 안녕"):
        await client.send_message(message.channel, "안녕하세요")

@client.event
async def on_message(message):
   if message.content.startswith("앤 들어와"):
        channel = message.author.voice.voice_channel
        server = message.server
        voice_client = client.voice_client_in(server)
        print("들어와")
        print(voice_client)
        print("들어와")
        if voice_client== None:
            await client.send_message(message.channel, '') 
            await client.join_voice_channel(channel)
        else:
            await client.send_message(message.channel, '') 


client.run('NTQ5MTM4NTE3NjA4MTAzOTM2.D1Pgqg.nAzM16OAc-5CuxKzOPmpFvMdYUc')
