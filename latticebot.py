import discord
import asyncio

client = discord.Client()
roledict = {'i am 18+': '18+', 'dyn': 'dynastic', 'pxl': 'pxls', 'pla': 'plastuer'}
emojidict = {'grapu': 'grapu', 'graypu': 'graypu', 'greypu': 'graypu', 'gaypu': 'gaypu', 'cherru': 'cherru', 'owo': 'owo'}

def find_role_by_name(rolename, message):
    rolelist = []
    roleobj = None
    if message.server != None:
        rolelist = message.server.roles
        for item in rolelist:
            if roledict[rolename] == item.name.lower():
                roleobj = item
    return roleobj

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    for item in emojidict:
        if item in message.content.lower():
            emojilist = []
            emojiobj = None
            if message.server != None:
                emojilist = message.server.emojis
                for emoji in emojilist:
                    if emoji.name == emojidict[item]:
                        emojiobj = emoji
            if emojiobj != None:
                await client.add_reaction(message, emojiobj)

    if message.content.lower().startswith('!role '):
        addlist = []
        rolelist = []
        if 'admin' in message.content.lower():
            await client.send_message(message.channel, 'LOL DID YOU THINK YOU\'D GET ADMIN FROM THIS? C\'MON DUDE, THINK NEXT TIME.')
            return
        for item in roledict:
            if item in message.content.lower():
                roleobj = find_role_by_name(item, message)
                if roleobj != None:
                    rolelist.append(roleobj)
                    addlist.append(roledict[item])
        if addlist and rolelist:
            await client.add_roles(message.author, *rolelist)
            await client.send_message(message.channel, 'Assigning ' + ', '.join(addlist) +' role(s)')
        else:
            await client.send_message(message.channel, 'You did not request any valid roles, please run !roles for more info')

    if message.content.lower().startswith('!roles'):
        await client.send_message(message.channel, 'To request a role, just say "!role " and any number of the following options:\n' +
                                  'i am 18+ - gains you access to our NSFW room\n' +
                                  'dyn - sets you as a dynastic user\n' +
                                  'pxl - sets you as a pxls.space user\n' +
                                  'pla - sets you as a plastuer user\n' +
                                  'All of the site specific roles will provide you access to their respective diplomacy channel')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

while True:
    try:
        client.run('NO CREDS HERE BOSS')
    except:
        pass
