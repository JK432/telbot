
import telebot
import random
import requests
from github import Github

# github generated access token
access_token = "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"

# login with access token
login = Github(access_token)

# get the user
user = login.get_user()

# get all repositories
my_repos = user.get_repos()
list1 = [1, 2, 3, 4, 5, 6]
giflist = ["https://tenor.com/bgzfD.gif", "https://tenor.com/bDrSi.gif", "https://tenor.com/SeP8.gif",
           "https://tenor.com/lnHKiYWYHmJ.gif", "https://tenor.com/5ThD.gif", "https://tenor.com/bfic7.gif",
           "https://tenor.com/biuD1.gif", "https://tenor.com/brcxd.gif",
           "https://tenor.com/cfB22fCDQYh.gif"]
giflstsad = ["https://tenor.com/btEYG.gif", "https://tenor.com/pH3B5ifYqn.gif", "https://tenor.com/hmoStO0Chvw.gif",
             "https://tenor.com/jsZFqz0UyvM.gif", "https://tenor.com/bDiJv.gif", "https://tenor.com/bGZwS.gif"]
fount = 0

API_KEY = "5099142440:AAGEVP7sxDYUGBZF7Pzq7tQ0KQJarIbClAE"
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_photo(message.chat.id, "https://ibb.co/ftvdnx9",
                   caption="\n Hai👋 \n\nI can help you with your lab questions😇 \"You can just copy my code\".\n\n\n📙For geting C lab codes just type\n\nbuck<space>c<space>repilName\nExample:buck c multiplication-table\n\n\n📙For geting Python lab codes just type\n\nbuck<space>p<space>repilName\nExample:buck p practise-2\n\n\n\n☠️☠️Remember while typeing repilname replace whitespace by \"-\" symbol☠️☠️\n\n🥳 Its version -v20.00.01 check WHATSNEW \n\n✅ provide full code for all files\n✅ Updated Gif")

    bot.send_animation(chat_id=message.chat.id, animation="https://tenor.com/2lsS.gif",
                       caption="അപ്പൊ എങ്ങന! തുടങ്ങാല്ല\n\nHappy Codeing ❤️")


@bot.message_handler(commands=['kill'])
def greet(message):
    bot.send_photo(message.chat.id, "https://ibb.co/ftvdnx9",
                   caption="Going off SOON..")

    bot.send_animation(chat_id=message.chat.id, animation="https://tenor.com/view/thanos-finger-snap-disappear-gif-13174976",
                       caption="Will come back with more POWER")




def stock_request(message):
    request = message.text.split()
    # print(request)
    if len(request) < 3 or request[0].lower() not in "buck":
        gifsad = random.choice(giflstsad)
        bot.send_animation(chat_id=message.chat.id, animation=gifsad,
                           caption="What do you mean👀 \n check input\n Or contact your provider")
        return False
    else:
        return True


@bot.message_handler(func=stock_request)
def send_price(message):
    my_repos = user.get_repos()
    gifhappy = random.choice(giflist)
    gifsad = random.choice(giflstsad)
    ran = random.choice(list1)
    lang = message.text.split()[1]
    rname = message.text.split()[2]
    if (lang == "p"):
        repolst = []
        list(repolst)
        for r in my_repos:
            repolst.append(r.name.lower())

            if (r.name.lower() == rname.lower() and r.language == "Python"):
                filelist = {}
                filelist = r.get_contents("")
                for t in filelist:
                    if (t.path != "__pycache__"):
                        url = t.download_url
                        m = requests.get(url)
                        bot.reply_to(message, t.path + " from " + r.name + " code bellow 👇")
                        bot.send_message(message.chat.id, m.content)

                if (ran == 3):
                    bot.send_animation(chat_id=message.chat.id, animation=gifhappy)
                if (ran == 6):
                    bot.send_animation(chat_id=message.chat.id, animation=gifhappy)

        repolst = list(set(repolst))
        if (rname.lower() not in repolst):
            bot.reply_to(message, " can't find " + rname + " please check your repil name👀 \nOr contact your provider")
            bot.send_animation(chat_id=message.chat.id, animation=gifsad)

    elif (lang == "c"):
        repolst = []
        list(repolst)
        for r in my_repos:
            repolst.append(r.name.lower())

            if (r.name.lower() == rname.lower() and r.language == "C"):

                url = r.get_contents("main.c").download_url
                m = requests.get(url)
                bot.reply_to(message, r.name + " code bellow 👇")
                bot.send_message(message.chat.id, m.content)

                if (ran == 3 or ran == 5):
                    bot.send_animation(chat_id=message.chat.id, animation=gifhappy)

        repolst = list(set(repolst))
        if (rname.lower() not in repolst):
            bot.reply_to(message, " can't find " + rname + " please check your repil name👀 \nOr contact your provider")
            bot.send_animation(chat_id=message.chat.id, animation=gifsad)


    else:
        bot.send_animation(chat_id=message.chat.id, animation=gifsad,
                           caption="What do you mean👀 \n check language selected\n Or contact your provider")


bot.polling()







