import discord
import asyncio
import os
from threading import Thread
from flask import Flask

# Servidor web falso para o Render não dar erro
app = Flask('')

@app.route('/')
def home():
    return "Bot online!"

def run_web():
    # O Render usa a porta 10000 por padrão para Web Services
    app.run(host='0.0.0.0', port=10000)

# Código do seu Bot do Discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # IMPORTANTE: Coloque o ID do seu canal do Discord aqui dentro dos parênteses
    CANAL_ID = 1522683009503989813  

    if message.channel.id == CANAL_ID:
        await asyncio.sleep(1)
        try:
            await message.delete()
        except discord.errors.Forbidden:
            print("O bot precisa de permissão de 'Gerenciar Mensagens' no canal.")

# Ativa o servidor web falso
Thread(target=run_web).start()

# Liga o bot usando o Token seguro do Render
client.run(os.environ.get('DISCORD_TOKEN'))
