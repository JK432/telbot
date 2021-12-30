
import telebot
import random
import requests
from github import Github





#github generated access token
access_token ="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"

#login with access token
login  = Github(access_token)

#get the user
user  = login.get_user()

#get all repositories
my_repos = user.get_repos()
list1 = [1, 2, 3, 4, 5, 6]
fount =0

    



API_KEY = "5099142440:AAGEVP7sxDYUGBZF7Pzq7tQ0KQJarIbClAE"
bot = telebot.TeleBot(API_KEY)





@bot.message_handler(commands=['start'])
def greet(message):
  bot.reply_to(message,"type \"anthasman<space>c/p<space>repilname\" "   )
  bot.send_message(message.chat.id,"Example:sandy p practise-2")
  bot.send_message(message.chat.id,"Copying is an ART so do it often")
  bot.send_animation(chat_id = message.chat.id,animation = "https://tenor.com/2lsS.gif")
  bot.send_message(message.chat.id,"പിന്നെ \" വിളച്ചിൽ എടുക്കരുത് കേട്ടോ\" എന്ന് സന്ദീപ് പറയാൻ പറഞ്ഞു  ")



def stock_request(message):
  
  request = message.text.split()
  # print(request)
  if len(request) < 3 or request[0].lower() not in "sandy":

    return False
  else:
    return True





  

@bot.message_handler(func=stock_request)
def send_price(message):
  ran=random.choice(list1)
  print(ran)
  lang = message.text.split()[1]
  rname = message.text.split()[2]
  if (lang=="p"):
    repolst=[]
    list(repolst)
    for r in my_repos:
      repolst.append(r.name.lower())
      
      
      
      
      if(r.name.lower()== rname.lower() and r.language=="Python"):
          
          url = r.get_contents("main.py").download_url
          m = requests.get(url) 
          bot.reply_to(message,r.name+" code bellow 👇")
          bot.send_message(message.chat.id,m.content)
          
          if(ran==3 or ran==6):
            
            bot.send_animation(chat_id = message.chat.id,animation = "https://tenor.com/bK36K.gif")
    repolst=list(set(repolst))
    if(rname.lower() not in repolst):
      bot.reply_to(message," can't find "+rname+" please try ")
      bot.send_animation(chat_id = message.chat.id,animation = "https://tenor.com/HjtT.gif")

  elif (lang=="c"):
    repolst=[]
    list(repolst)
    for r in my_repos:
      repolst.append(r.name.lower())
     
      
      
      
      
      if(r.name.lower()== rname.lower() and r.language=="C"):
          
          url = r.get_contents("main.c").download_url
          m = requests.get(url) 
          bot.reply_to(message,r.name+" code bellow 👇")
          bot.send_message(message.chat.id,m.content)
          
          
          if(ran==3 or ran==5):
            
            bot.send_animation(chat_id = message.chat.id,animation = "https://tenor.com/bMKyQ.gif")
    
       
    repolst=list(set(repolst))
    if(rname.lower() not in repolst):
      bot.reply_to(message," can't find "+rname+" please try ")
      bot.send_animation(chat_id = message.chat.id,animation = "https://tenor.com/HjtT.gif")


  else:
        bot.send_animation(chat_id = message.chat.id,animation = "https://tenor.com/2wi4.gif")
        
  

  
bot.polling()





