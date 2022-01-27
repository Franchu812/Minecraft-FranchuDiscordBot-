import os
from discord_easy_commands import EasyBot
#pip install discord_easy_commands
#from discord_easy_... usar librería EasyBot
bot = EasyBot()
#definimos la librería de el bot
bot.setCommand("!ip","elpolacosape2.mcnetwork.me")
bot.setCommand("hola", "hola!")
bot.setCommand("!version", "1.18.1")
bot.setCommand("!host", "Canada, server.pro")
#comandos de el bot
bot.run(os.environ['TOKEN'])
#ejecutamos el bot con el TOKEN secreto
