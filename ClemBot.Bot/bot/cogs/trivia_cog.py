import json
import logging
import uuid
import aiohttp
import discord
import discord.ext.commands as commands
from discord.ext.commands.errors import UserInputError
import bot.bot_secrets as bot_secrets
import bot.extensions as ext
from bot.consts import Colors
from bot.messaging.events import Events








class TriviaCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()



    async def Triviacog(self, ctx, *input:str):
       async with await self.session.post(url=DEFAULT_URL) as resp:  
            response = json.loads(await resp.text())

       return


    async def TriviaManual(self, ctx, *input:str):
     if len(input) < 4:
        raise UserInputError("You need more arguments to use this command")
     questionnumber = input[0]
     trivianumber = None
     if input[1].isnumeric():
        trivianumber = input[1]+9
     else:
        triviacategory = input[1].lower()
  
        for x in CATEGORYLIST_LOWER:
             searching = CATEGORYLIST_LOWER[x]
             if(searching.find(triviacategory) != -1):
                  trivianumber=x+9
                  break
            

     difficulty = input[2]
     foundstring = None
     if difficulty.isnumeric():
         difficulty = difficulty+9
        
     else: 
         difficulty = difficulty.lower()
         for x in DIFFICULTY_LOWER:
           searchthis = DIFFICULTY_LOWER[x]
           if(searchthis.find(difficulty) != -1):
               difficulty=x+9

 
     questiontype = input[3]
     foundquestion = None

     if questiontype.isnumeric():
         questiontype = questiontype+9
     else:
         questiontype = questiontype.lower()
         for x in QUESTIONTYPE_LOWER:
            searchingthis = QUESTIONTYPE_LOWER[x]
            if(searchingthis.find(QUESTIONTYPE) != -1):
                questiontype = x+9

                url = R"https://opentdb.com/api.php?amount="+questionnumber+"&category="+triviacategory+"&difficulty="+difficulty+"&type="+questiontype
     async with await self.session.post(url=url) as resp:  
            response = json.loads(await resp.text())    




     return

 async def JsonParser(dictionary):

     return
            


























DEFAULT_URL = "https://opentdb.com/api.php?amount=10"
   


DIFFICULTY = ["Easy", 
              "Medium", 
              "Hard"]

DIFFICULTY_LOWER = [k.lower() for k in DIFFICULTY]

QUESTIONTYPE = [
    "multiple", 
    "bool"
]
QUESTIONTYPE_LOWER = [k.lower for k in QUESTIONTYPE]
CATEGORYLIST = ["General Knowledge", #Including this out of consistency to avoid making the offset 10 for no reason. This will be the default value.
                 "Books", 
                 "Film", 
                 "Music", 
                 "Musicals & Theatres", 
                 "Television",
                 "Video Games",
                 "Board Games",
                 "Science & Nature", 
                 "Computers", 
                 "Mathematics", 
                 "Mythology", 
                 "Sports", 
                 "Geography", 
                 "History", 
                 "Politics", 
                 "Art",
                "Celebrities",
               "Animals", 
               "Vehicles",
              "Comics",
             "Gadgets",
            "Japanese Anime & Manga",
           "Cartoon & Animations"]
CATEGORYLIST_LOWER = [k.lower for k in CATEGORYLIST]