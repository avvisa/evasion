import os
import random
from os import system
import urllib
import json
from json import dumps, load
import argparse
from urllib.request import urlopen
system("pip install amino.fix")
system("pip install gtts")
system("pip install requests")
import aminofix
import time
from gtts import gTTS
import requests
from uuid import uuid4
import hmac
from hashlib import sha1
identifier = os.urandom(20)
x= ("42" + identifier.hex() + hmac.new(bytes.fromhex("02B258C63559D8804321C5D5065AF320358D366F"), b"\x42" + identifier, sha1).hexdigest()).upper()
devi = x
client=aminofix.Client(devi)
os.system("clear")
print("\t\033[1;32m EVASION \033[1;36m COMMUNITY BOT \n\n")
email=""
password=""

client.login(email=email,password=password)
cid="238471772"
cidy=238471772

adm=[]
self=client.socket
def generate_transaction_id(self):
        return str(uuid4())
transaction=generate_transaction_id(self)

admx=["http://aminoapps.com/p/gdswiwt","http://aminoapps.com/p/vaaj0f","http://aminoapps.com/p/n118js","http://aminoapps.com/p/t7gkoy","http://aminoapps.com/p/ru03uf","http://aminoapps.com/p/16ifz0"]

client.join_community(cid)
for i in admx:
	try:
		w=client.get_from_code(i).objectId
		adm.append(w)
	except:
		print("Invalid link")
subclient=aminofix.SubClient(comId=cid,profile=client.profile)
msg="""Welcome to the chat, make sure to follow the [Guidelines] and chat rules!

Type "/help" in the chat to view my commands!"""
print("BOT JOINED THE COMMUNITY")
subclient=aminofix.SubClient(comId=cid,profile=client.profile)
print("JOINING ALL CHATROOMS")
subclient=aminofix.SubClient(comId=cid,profile=client.profile)
chts=subclient.get_public_chat_threads(type="recommended", start=0, size=100).chatId
for chats in chts:
	try:
		subclient.join_chat(chatId=chats)
	except Exception:
		pass   				
print("JOINED ALL CHATROOMS")
print("EVASION READY")
l=[]
lis = ["It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Can't predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful","Yes","No" ,"Probably","100%", "Not sure"]

@client.event("on_group_member_join")
def on_group_member_join(data):
	if data.comId==cidy:
		try:
			x=data.message.author.icon
			response=requests.get(f"{x}")
			file=open("sample.png","wb")
			file.write(response.content)
			file.close()
			img=open("sample.png","rb")
			subclient.send_message(chatId=data.message.chatId,message=f"""[BC]👋 Welcome <${data.message.author.nickname}$>!
{msg}""",embedId=data.message.author.userId,embedTitle=data.message.author.nickname,embedLink=f"ndc://x{cid}/user-profile/{data.message.author.userId}",embedImage=img,mentionUserIds=[data.message.author.userId])
			print(f"\nwelcomed {data.message.author.nickname} to gc ")
		except Exception as e:
			print(e)
				
@client.event("on_group_member_leave")
def on_group_member_leave(data):
	if data.comId==cidy:
		try:
			subclient.send_message(chatId=data.message.chatId,message="""A member has left the chat.""")
			print(f"A member has left the chat.")
		except Exception as e:
			print(e)

@client.event("on_text_message")
def on_text_message(data):
	if data.comId==cidy:
		ex=data.message.content
		cd=ex.split(' ')
		x=cd[0]
		c=cd[1:]
		adx=[]
		for w in cd:
			adx.append(w)
		print(adx)
		if ex:
			for i in adx:
				if len(i)<=50:
					if i[:23]=="http://aminoapps.com/p/" or i[:23]=="http://aminoapps.com/c/":
						fok=client.get_from_code(i)
						cidx=fok.path[1:fok.path.index("/")]
						if cidx!=cid:
							try:
								subclient.delete_message(chatId=data.message.chatId,messageId=data.message.messageId,asStaff=True)
								s=subclient.get_chat_thread(data.message.chatId).title
								subclient.start_chat(userId=adm,message=f"ndc://x{cid}/user/profile/{data.message.author.userId} was advertisng in {s}")
								
								subclient.send_message(chatId=data.message.chatId,message=f"Please don't advertise here, <${data.message.author.nickname}")
								print("spotted advertiser")
							except Exception as e:
								print(e)
			if x.lower()=="/info" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="Hi, I'm a community bot ran by the staff, feel free to private message a staff if you have any questions!"'')
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/global":
				try:
					for i in c:
						mention = subclient.get_message_info(chatId=data.message.chatId, messageId=data.message.messageId).mentionUserIds
						for user in mention:
							h=subclient.get_user_info(userId=str(user)).nickname
							AID=client.get_user_info(userId=str(user)).aminoId
							d=client.get_from_code(i).objectId
							subclient.send_message(chatId=data.message.chatId,message="https://aminoapps.com/u/"+str(AID),embedTitle="Global Id",embedContent=f"{h}")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/clear":
				if x.lower() not in l:
					try:
						for i in c:
							d=int(i)
							a=subclient.get_chat_messages(chatId=data.message.chatId,size=d)
							for i in a.messageId:
								subclient.delete_message(chatId=data.message.chatId,messageId=i,asStaff=True,reason="clear")
							subclient.send_message(chatId=data.message.chatId,message=f"Cleared {d} messages!")
					except:
						subclient.send_message(chatId=data.message.chatId,message="You must give curator to the bot to be able to use this command!")
				else:
					subclient.send_message(chatId=data.message.chatId,message="This command is locked.")
			if x.lower()=="/llock" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"Locked commands {l}")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/lock":
				if data.message.author.userId in adm:
					try:
						for i in c:
							l.append(i)
							subclient.send_message(chatId=data.message.chatId,message=f"locked {i} command")
							print(l)
							print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="This command is only accessible to bot admins!")
					except Exception as e:
						print(e)
			if x.lower()=="/unlock":
				if data.message.author.userId in adm:
					try:
						for i in c:
							l.remove(i)
							subclient.send_message(chatId=data.message.chatId,message=f"Unlocked {i} command!")
							print(l)
							print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="This command is only accessible to bot admins!")
					except Exception as e:
						print(e)
			if x.lower()=="/say":
				if x.lower() not in l:
					if c==[]:
						try:
							subclient.send_message(chatId=data.message.chatId,message=f"You must put something after /say for me to talk, {data.message.author.nickname}")
						except:
							pass
					else:
						try:
							t=''
							lx='en'
							for i in c:
								t=t+i
							out=gTTS(text=t,lang=lx,tld='co.uk',slow=False)
							out.save("soundfx.mp3")
							with open("soundfx.mp3","rb") as f:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="audio")
							f.close()
							print(f"Info requested by {data.message.author.nickname}")
						except Exception as e:
							print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="This command is locked.")
					except:
						pass
			if x.lower()=="/join":
				if c==[]:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"You must paste the link after /join for the command to work, {data.message.author.nickname}")
					except:
						pass
				else:
					try:
						for i in c:
							try:
								d=client.get_from_code(i).objectId
								subclient.join_chat(chatId=d)
								subclient.send_message(chatId=data.message.chatId,message="I joined the chatroom!")
							except Exception as e:
								print(e)
						print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
			if x.lower()=="/vc" and c==[]:
				try:
					subclient.invite_to_vc(userId=data.message.author.userId,chatId=data.message.chatId)
					print(f"Invited {data.message.author.nickname} to the voice call.")
				except Exception as e:
					print(e)
					subclient.send_message(chatId=data.message.chatId,message=f"I can't invite you to the voice call if I don't have co-host, <$@{data.message.author.nickname}$>")
			if x.lower()=="/inviteall" and c==[]:
				if x.lower() not in l:
					try:
						h=subclient.get_all_users(start=0,size=1000).profile.userId
						m=len(h)
						for u in h:
							try:
								subclient.invite_to_chat(userId=u,chatId=data.message.chatId)
							except Exception as e:
								print(e)
								pass
						subclient.send_message(chatId=data.message.chatId,message=f"Invited {m} members to the chat!")
						print(f"Invited {data.message.author.nickname} to voice call.")
					except Exception as e:
						print(e)
						subclient.send_message(chatId=data.message.chatId,message=f"I can't invite you to the voice call if I don't have co-host, <$@{data.message.author.nickname}$>")
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="This command is locked.")
					except:
						pass
			if x.lower()=="/pm" and c==[]:
				if x.lower() not in l:
					try:
						subclient.start_chat(userId=data.message.author.userId,message="Hey, there!")
						subclient.send_message(chatId=data.message.chatId,message=f"Check your messages <${data.message.author.nickname}$>!",mentionUserIds=[data.message.author.userId])
						print(f"Invite {data.message.author.nickname} to private messages")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"This command is locked, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
					except:
						pass
			if x.lower()=="/startvc" and c==[]:
				if x.lower() not in l:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Starting the voice call in 5 seconds...")
						time.sleep(5)
						client.start_vc(comId=cid,chatId=data.message.chatId,joinType=1)
						#subclient.send_message(chatId=data.message.chatId,message=f"Vc started")
						print(f"VC started")
					except Exception as e:
						print(e)
						try:
							subclient.send_message(chatId=data.message.chatId,message=f"I can't run that command without co-host, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"Start command is locked, <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					except:
						pass
			if x.lower()=="/endlive" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="Ending the voice call in 5 seconds...")
					time.sleep(5)
					client.end_vc(comId=cid,chatId=data.message.chatId,joinType=2)
				except Exception as e:
					print(e)
					subclient.send_message(chatId=data.message.chatId,message=f"I can't run that command without co-host, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
			if x.lower()=="/onlinemem" and c==[]:
				if x.lower() not in l:
					try:
						o=""
						q=subclient.get_online_users(start=0,size=1000)
						for uid in q.profile.nickname:
							o=o+uid+"\n"
						subclient.send_message(chatId=data.message.chatId,message=f"""[BC]ONLINE MEMBERS;
{o}""")
						print("done")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Members command is locked")
					except:
						pass

			if x.lower()=="/goodmorning" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"Good morning, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/follow" and c==[]:
				try:
					subclient.follow(userId=data.message.author.userId)
					subclient.send_message(chatId=data.message.chatId,message=f"I followed you, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/goodevening" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"Good evening, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/love":
				try:
					for i in c:
						msg = i + " null null "
						msg = msg.split(" ")
						msg[2] = msg[1]
						msg[1] = msg[0]
						subclient.send_message(chatId=data.message.chatId, message=f"""Match ❤️ {random.randint(0,100)}%""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/dance" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""
(_＼ヽ
　 ＼＼ .Λ＿Λ.
　　 ＼(　ˇωˇ)　
　　　 >　⌒ヽ
　　　/ 　 へ＼
　　 /　　/　＼＼
　　 ﾚ　ノ　　 ヽ_つ
　　/　/
　 /　/|
　(　(ヽ
　|　|、＼
　| 丿 ＼ ⌒)
　| |　　) /
`ノ ) 　 Lﾉ
(_／""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/help" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[BC]EVASION BOT COMMANDS;
Evasion is a community bot ran by the staff on here, some commands might be broken, feel free to message a staff if you have any questions!

/join
/global
/say
/pm
/goodmorning
/unlock
/startvc
/dance
/goodnight
/leader
/playlist
/inviteall
/llock
/clear
/play
/goodnight
/endlive
/meme
/aboutevasion
/info
/chocolate
/nickname
/profilepic
/dance
/joke
/8ball
/follow
/coin
/onlinemem
/lock
/love
/gf""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/coin":
				try:
					for i in c:
						d=int(i)
						print(transaction)
						subclient.send_coins(coins=d, chatId=data.message.chatId, transactionId=transaction)
						subclient.send_message(chatId=data.message.chatId,message=f"Sent {d} coins to host!")
				except Exception as e:
					print(e)
			if x.lower()=="/goodnight" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"Goodnight, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/music" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""PARTY ALL NIGHT!""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/nickname":
				try:
					t=''
					for i in c:
						t=t+i
						subclient.edit_profile(nickname=t)
						subclient.send_message(chatId=data.message.chatId,message=f"My name changed to {i}!")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/profilepic" and c==[]:
				try:
					info = subclient.get_message_info(chatId = data.message.chatId, messageId = data.message.messageId)
					reply_message = info.json['extensions']
					if reply_message:
						image = info.json['extensions']['replyMessage']['mediaValue']
						filename = image.split("/")[-1]
						filetype = image.split(".")[-1]
						urllib.request.urlretrieve(image, filename)
						with open(filename, 'rb') as fp:
							for i in range(1,8):
								try:
									subclient.edit_profile(icon=fp)
								except Exception as e:
									subclient.send_message(data.message.chatId, message="My profile picture has changed!",replyTo=data.message.messageId)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/playlist" and c==[]:
				try:
					files=os.listdir("music")
					o=""
					for f in files:
						o=o+f+"\n"
					subclient.send_message(chatId=data.message.chatId,message=f"""[BC]MUSIC PLAYLIST
{o}""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/gf" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""You're single (づ｡◕‿‿◕｡)づ
I'm here for you...""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/joke" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""DEEZ NUTS""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/8ball":
				try:
					subclient.send_message(chatId=data.message.chatId,message=str(random.choice(lis)),replyTo=data.message.messageId)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/play":
				if subclient.get_chat_thread(data.message.chatId).title!=None:
					mx=random.choice(os.listdir("music"))
					if x.lower() not in l:
						sounds=f"music/{mx}"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="audio")
								print(f"Info requested by {data.message.author.nickname}")
							except Exception as e:
								print(e)
					else:
						try:
							subclient.send_message(chatId=data.message.chatId,message="command is locked")
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="This commands only works only in private messages, use the /pm command to make the bot message you.")
					except:
						pass
			if x.lower()=="/meme":
				if subclient.get_chat_thread(data.message.chatId).title!=None:
					hx=random.choice(os.listdir("memes"))
					if x.lower() not in l:
						sounds=f"memes/{hx}"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="image")
								print(f"Info requested by {data.message.author.nickname}")
							except Exception as e:
								print(e)
					else:
						try:
							subclient.send_message(chatId=data.message.chatId,message=" command is locked")
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="This commands only works only in private messages, use the /pm command to make the bot message you.")
					except:
						pass
			if x.lower()=="/leader" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="Go get one yourself, lol")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/aboutme" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""You're gay""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/chocolate" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""
╔╦╦
╠╬╬╬╣
╠╬╬╬╣ I ♥
╠╬╬╬╣ Chocolate
╚╩╩╩╝""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)