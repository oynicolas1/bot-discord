import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    # Evita que o bot responda a si mesmo
    if message.author == client.user:
        return

    # Substitua pelo ID do canal onde o bot deve funcionar
    CANAL_ID = 1522683009503989813 

    if message.channel.id == CANAL_ID:
        # Aguarda 1 segundo
        await asyncio.sleep(1)
        try:
            await message.delete()
        except discord.errors.Forbidden:
            print("O bot não tem permissão para apagar mensagens neste canal.")

# Substitua pelo Token do seu Bot
client.run(os.environ.get('DISCORD_TOKEN'))
