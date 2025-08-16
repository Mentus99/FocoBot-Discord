import discord
from discord.ext import commands
import asyncio

import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# --- CONFIGURAÇÃO ---
# Pega o token do arquivo .env de forma segura
TOKEN = os.getenv('TOKEN') 

# Configura as permissões básicas que o bot precisa
intents = discord.Intents.default()
intents.message_content = True

# Cria a instância do bot
bot = commands.Bot(command_prefix='/', intents=intents)

# Dicionário pra guardar os timers de cada um
user_timers = {}

# --- FUNÇÃO PRA AJUDAR A GERENCIAR OS TIMERS ---
async def start_timer(interaction: discord.Interaction, duration: int, timer_type: str, end_message: str):
    user_id = interaction.user.id
    
    # Checa se a pessoa já não tem um timer rolando
    if user_id in user_timers:
        await interaction.response.send_message("Opa, você já tem um timer rolando. Use `/parar` primeiro.", ephemeral=True)
        return

    # Manda a mensagem confirmando que começou
    await interaction.response.send_message(f"Ok, começando {duration} minutos de **{timer_type}**. Bora focar! 🚀")

    # A tarefa que vai ficar esperando o tempo passar
    async def timer_task():
        await asyncio.sleep(duration * 60)
        # Quando o tempo acabar, avisa a pessoa
        if user_id in user_timers:
            del user_timers[user_id]
            await interaction.followup.send(f"🔔 {interaction.user.mention}, seu tempo de **{timer_type}** acabou! {end_message}")

    # Guarda e inicia o timer pra esse usuário
    task = asyncio.create_task(timer_task())
    user_timers[user_id] = task

# --- AVISO DE QUANDO O BOT LIGA ---
@bot.event
async def on_ready():
    print(f'Bot {bot.user} tá on!')
    try:
        # Sincroniza os comandos pra eles aparecerem no Discord
        synced = await bot.tree.sync()
        print(f"Sincronizados {len(synced)} comandos.")
    except Exception as e:
        print(f"Deu erro pra sincronizar: {e}")

# --- COMANDOS DE BARRA (SLASH COMMANDS) ---
@bot.tree.command(name="iniciar_foco", description="Começa 1 hora de foco total no trabalho.")
async def iniciar_foco(interaction: discord.Interaction):
    # O tempo de foco agora é 60 minutos
    await start_timer(interaction, 60, "foco", "Deu o tempo! Que tal uma pausa? Use `/pausa_curta`.")

@bot.tree.command(name="pausa_curta", description="Faz uma pausa rápida de 5 minutos.")
async def pausa_curta(interaction: discord.Interaction):
    await start_timer(interaction, 5, "pausa curta", "Pausa finalizada. Bora voltar pro foco? `/iniciar_foco`.")

@bot.tree.command(name="pausa_longa", description="Faz uma pausa mais longa de 15 minutos.")
async def pausa_longa(interaction: discord.Interaction):
    await start_timer(interaction, 15, "pausa longa", "Pausa longa terminada! Deu pra recarregar? `/iniciar_foco` pra voltar.")

@bot.tree.command(name="parar", description="Cancela o timer que estiver rolando.")
async def parar(interaction: discord.Interaction):
    user_id = interaction.user.id
    if user_id in user_timers:
        # Cancela o timer da pessoa
        user_timers[user_id].cancel()
        del user_timers[user_id]
        await interaction.response.send_message("Timer cancelado. Quando quiser, é só começar outro.", ephemeral=True)
    else:
        await interaction.response.send_message("Não tem nenhum timer ativo pra parar.", ephemeral=True)

# --- RODA O BOT ---
bot.run(TOKEN)