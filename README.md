# Discord Hack Week bot
**CiberSec** is mainly focused on cyber security. The bot works like a command shell - You simply type in a Linux shell command, and the bot will return the output from the executed command.


# Installation
Clone the repository via:
```bash
$ git clone https://github.com/WodxTV/CiberSec.git
```

Python 3 has to be installed on the Linux machine in order to make the bot work.

You can check the version of Python you've installed via:
```bash
$ python --version
```
If the command is not recognized, install Python 3.7 via:
```bash
$ sudo apt update
$ sudo apt install python3.7
```
PIP (a package-management system) for Python 3.7 also has to be installed.

Install PIP via:
```bash
$ sudo apt update
$ sudo apt install python3-pip
```
Install discord.py module via:
```bash
$ pip3 install discord
```

When you have Python 3, discord.py and PIP installed, create a new client bot via:
```
https://discordapp.com/developers/applications/
```

Copy the client ID of the bot you have created, and paste this URL into your browser to invite the bot to your Discord server:
```
https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID_HERE&scope=bot&permissions=8
```


# Running the bot
I recommend you running the bot on a penetration testing Linux distribution like **Kali Linux** or **Parrot OS**, as they have a lot of pre-installed penetration testing/hacking tools installed.

Start the bot via:
```bash
$ python3 cibersec.py
```


# Work in progress
* Auto create category named 'CiberSec'
* Auto create text channel named 'Terminal' under category 'CiberSec'
* Auto create text channel named 'Command History' under category 'CiberSec'
* Handling changing/'animated' outputs
* Design a logo for the bot


# Developer
**WodX**
* Github: [WodXTV](https://github.com/wodxtv)
* Discord: [wodx#0666](http://discordapp.com)
* Twitter: [@wodxofficial](https://twitter.com/wodxofficial)
