import discord
import os
import json
from larousse import word_in_webhook
from better_log import log
from pystyle import Center, Anime, Colors, Colorate, Write, System


# Police des commentaires : https://patorjk.com/software/taag/#p=display&f=Big%20Money-se&t=je%20suis%20gay%20%3A)
text = r'''
_____                 _                                         _     
|  __ \               | |                                       | |    
| |__) |__ _ _ __   __| | ___  _ __ ___   __      _____  _ __ __| |___ 
|  _  // _` | '_ \ / _` |/ _ \| '_ ` _ \  \ \ /\ / / _ \| '__/ _` / __|
| | \ \ (_| | | | | (_| | (_) | | | | | |  \ V  V / (_) | | | (_| \__ \
|_|  \_\__,_|_| |_|\__,_|\___/|_| |_| |_|   \_/\_/ \___/|_|  \__,_|___/
                                                                                    
                                                                        
'''[1:]

run = r'''
   _____ ___  _   _  ____ _   _ _____     _____ _   _ _____ ____  _____ ____      
  |_   _/ _ \| | | |/ ___| | | | ____|   | ____| \ | |_   _|  _ \| ____|  _ \     
    | || | | | | | | |   | |_| |  _|     |  _| |  \| | | | | |_) |  _| | |_) |    
    | || |_| | |_| | |___|  _  | |___    | |___| |\  | | | |  _ <| |___|  _ <     
  __|_| \___/ \___/ \____|_| |_|_____|___|_____|_| \_| |_|_|_| \_\_____|_|_\_\__  
 |  _ \ / _ \| | | |  _ \     |  _ \| ____|  \/  |  / \  |  _ \|  _ \| ____|  _ \ 
 | |_) | | | | | | | |_) |    | | | |  _| | |\/| | / _ \ | |_) | |_) |  _| | |_) |
 |  __/| |_| | |_| |  _ <     | |_| | |___| |  | |/ ___ \|  _ <|  _ <| |___|  _ < 
 |_|    \___/ \___/|_|_\_\  __|____/|_____|_|_ |_/_/   \_\_| \_\_| \_\_____|_| \_\
                     | |   | ____| | __ ) / _ \_   _|                             
                     | |   |  _|   |  _ \| | | || |                               
                     | |___| |___  | |_) | |_| || |                               
                     |_____|_____| |____/ \___/ |_|                               
                                                                                  
'''[1:]


# Initialisation du token

if os.path.isfile('settings.json'):
    with open('settings.json') as json_data:
        data_dict = json.load(json_data)

    if data_dict['TOKEN']:
        TOKEN = data_dict['TOKEN']

    else:
        System.Clear()
        print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(text)))
        TOKEN = Write.Input("Token du bot -> ", Colors.red_to_yellow, interval=0.005)

else:
    System.Clear()
    print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(text)))
    TOKEN = Write.Input("Token du bot hehe -> ", Colors.red_to_yellow, interval=0.005)
class MyClient(discord.Client):
    async def on_ready(self):

        print(Center.XCenter(log(['Connecté sur', str(self.user), 'Préfix : !'])))
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

            #          __       __   ______  ________ 
            # |  \     /  \ /      \|        \
            # | $$\   /  $$|  $$$$$$\\$$$$$$$$
            # | $$$\ /  $$$| $$  | $$  | $$   
            # | $$$$\  $$$$| $$  | $$  | $$   
            # | $$\$$ $$ $$| $$  | $$  | $$   
            # | $$ \$$$| $$| $$__/ $$  | $$   
            # | $$  \$ | $$ \$$    $$  | $$   
            #  \$$      \$$  \$$$$$$    \$$            
                                
        if message.content.startswith('!mot'):
            args = message.content[5:]
            try:
                if  1<=int(args)<=5:
                    nombre = int(args)
                    txt = word_in_webhook(nombre, True)
                    resultat = f'__Nombre de mots : `{nombre}`__\n{txt}'
                    print(f'{message.author} a demandé {nombre} mots (définition)\n', txt)
                    return await message.reply(resultat)
                else:
                    return await message.reply('Saisie incorrecte de la commande, `!mot [nombre entre 1 et 5]` \n__ex :__```!mot 2```')
            except:
                return await message.reply('Saisie incorrecte de la commande, `!mot [nombre entre 1 et 5]` \n__ex :__```!mot 2```')

            #          _______   ________  ________ 
            # |       \ |        \|        \
            # | $$$$$$$\| $$$$$$$$| $$$$$$$$
            # | $$  | $$| $$__    | $$__    
            # | $$  | $$| $$  \   | $$  \   
            # | $$  | $$| $$$$$   | $$$$$   
            # | $$__/ $$| $$_____ | $$      
            # | $$    $$| $$     \| $$      
            #  \$$$$$$$  \$$$$$$$$ \$$                                   
                              
        elif message.content.startswith('!link'):
            args = message.content[5:]
            try:
                
                if  1<=int(args)<=10:
                    nombre = int(args)
                    txt = word_in_webhook(nombre, False)
                    resultat = f'__Nombre de mots : `{nombre}`__\n{txt}'
                    print(f'{message.author} a demandé {nombre} mots (juste lien)\n', txt)
                    return await message.reply(resultat)
                else:
                    return await message.reply('Saisie incorrecte de la commande, `!link [nombre entre 1 et 10]` \n__ex :__```!mot 2```')
            except:
                return await message.reply('Saisie incorrecte de la commande, `!link [nombre entre 1 et 10]` \n__ex :__```!mot 2```')


        elif message.content == '!help':
            return await message.reply('- Fais `!mot x` avec x qui est un nombre entier `entre 1 et 5` *(commande relativement lente)*\n- Fais `link x` avec x qui est un nombre entier `entre 1 et 10`')

Anime.Fade(Center.Center(run), Colors.red_to_yellow, Colorate.Vertical, enter=True)
client = MyClient()
client.run(TOKEN)
