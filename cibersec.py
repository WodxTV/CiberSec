#Developed by wodx @ 26-06-2019
import discord, subprocess, json, os, textwrap

#These commands are blacklisted, as they're pretty useless in this project.
BLACKLISTED_COMMANDS = [
    'nano', 
    'leafpad',
    'wireshark',
    'zenmap'
]

#Operators which are used to run multiple bash commands at once.
OPERATORS = [
    ';',
    '&&',
    '||'
]

CONFIG = json.loads(open('config/config.json').read())

def error(message):
    return discord.Embed(title='**ERROR**', description=message, colour=discord.Colour.red())

def warning(message):
    return discord.Embed(title='**WARNING**', description=message, colour=0xe7e33c)

def success(message):
    return discord.Embed(title='**SUCCESS**', description=message, colour=discord.Colour.green())

def main():
    #Bot token check
    token = CONFIG['config']['token']
    if not token or len(token) != 59 or not '.' in token:
        print('[-] Invalid token.')
        exit()

    #OS check
    if not os.name == 'posix':
        print('[-] CiberSec has to be run on a Linux machine.')
        exit()

    print('[*] Starting CiberSec bot...')

    client = discord.Client()

    #Ready event
    @client.event
    async def on_ready():
        print('[+] CiberSec is ready to use.')
        print('CiberSec - Cyber security bot')
        print('By: wodx')
        print('Version: 1.1')
        print('Made for Discord Hack Week.')
        await client.user.edit(username='CiberSec')

    @client.event
    async def on_member_join(member):
        if member.user == client.user:
            print('test')

    #Message event
    @client.event
    async def on_message(event_message):
        if event_message.author == client.user:
            return
        
        event_channel = event_message.channel
        try:
            try:
                if event_channel.id == int(CONFIG['config']['terminal']):
                    command = str(event_message.content)

                    #Command analyzing
                    for operator in OPERATORS:
                        if ' %s ' % (operator) in command:
                            command_split = command.split(' %s ' % (operator))
                            for cmd in command_split:
                                for cmd_blacklisted in BLACKLISTED_COMMANDS:
                                    if cmd.startswith(cmd_blacklisted):
                                        await event_channel.send(embed=error('The executed command contains a blacklisted command.'))
                                        return
                    for cmd_blacklisted in BLACKLISTED_COMMANDS:
                        if command.lower().startswith(cmd_blacklisted):
                            await event_channel.send(embed=error('The executed command is blacklisted.'))
                            return

                    #Clear command
                    if 'clear' in command.lower():
                        if command.lower() == 'clear history':
                            await client.get_channel(int(CONFIG['config']['history'])).purge(limit=1000)
                            await event_channel.send(embed=success('Command history has been cleared.'))
                        else:
                            await event_channel.purge(limit=1000)
                            await event_channel.send(embed=success('Terminal has been cleared.'))
                        return

                    #Change directory command
                    if 'cd ' in command:
                        command_split = command.split(' ')
                        for i, cmd in enumerate(command_split):
                            if cmd == ' ':
                                continue
                            if cmd.lower() == 'cd':
                                os.chdir(command_split[i + 1])
                                output = 'Changed directory to %s' % (os.getcwd())
                                await event_channel.send('```\n' + output + '\n```')
                                return
                        
                    #Executing the shell command
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

                    #Command output
                    output = process.stdout.read() + process.stderr.read()
                    output = output.decode()

                    #Adding command to history
                    try:
                        await client.get_channel(int(CONFIG['config']['history'])).send('``\n' + command + '\n``')
                    except:
                        await event_channel.send(embed=error('Command history channel not found.'))
                        return

                    #Handling +2000 chars output
                    if len(output) >= 2000:
                        await event_channel.send(embed=warning('Output is more than 2000 characters long. Please wait while all data is getting transferred.'))
                        for output_piece in [output[i * 1000 : i * 1000 + 1000] for i, _ in enumerate(output[::1000])]:
                            await event_channel.send('```\n' + output_piece + '\n```')
                        await event_channel.send(embed=success('All data has been transferred.'))

                    else:
                        if output.strip():
                            await event_channel.send('```\n' + output + '\n```')
                        else:
                            await event_channel.send(embed=error('No output recieved.'))

            except discord.DiscordException:
                await event_channel.send(embed=error('Terminal channel not found.'))

        except Exception as e:
            await event_channel.send(embed=error('An error occurred: %s' % (e)))
            exit()

    #Making the bot run
    client.run(CONFIG['config']['token'])

if __name__ == '__main__':
    main()
