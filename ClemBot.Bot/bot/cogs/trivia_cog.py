import json
import logging
from urllib import response
import uuid
import random
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
       async with await self.session.get(url=DEFAULT_URL) as resp:  
            response = json.loads(await resp.text())
            correct_answers = self.JsonParser(response)
            await self.Dict_Publisher(ctx, response)

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

     if questionnumber and triviacategory and difficulty and questionnumber != None:   
        url = R"https://opentdb.com/api.php?amount="+questionnumber+"&category="+triviacategory+"&difficulty="+difficulty+"&type="+questiontype
        async with await self.session.get(url=url) as resp:  
            response = json.loads(await resp.text())
            correct_answers = await self.JsonParser(response)

     else:
         raise UserInputError("Incorrect entry! Try typing it again or use !help")

    



     return

    async def Json_Parser(dictionary):
        Correct_Answers= []
        for x in dictionary['results']:
            Correct_Answers.append(x['correct_answer'])
        return Correct_Answers

    async def Dict_Publisher(self, ctx, dictionary, Correct_answers):
        x=0
        cog_embeds = []
        for bob in dictionary['result']:
         Answers_List= []   
         Answers_List = bob['incorrect_answers']
         Answers_List.append(bob['correct_answer'])
         random.shuffle(Answers_List)  
         x+=1   
         embed = discord.Embed(title= "Your Trivia Question:",
         descripton="Question #"+x,
         color=Colors.ClemsonOrange)
         embed.addfield(name="Question:", value=bob['question'])
         embed.addfield(name="Category:", value=bob['category'])
         embed.addfield(name="Pick your Answer choice:", inline=False)
         a = 65
         for iterative in Answers_List:
            embed.addfield(name=chr(a)+":", value = iterative, inline=False)
            a=a+1
         cog_embeds.append(embed)
        
        msgembed = await self.bot.messenger.publish(Events.on_set_pageable_embed,
                                         pages=cog_embeds,
                                         author=ctx.author,
                                         channel=ctx.channel,
                                         timeout=360
                                         ) 
        await msgembed.add_reaction('🇦')
        await msgembed.add_reaction('🇧')
        await msgembed.add_reaction('🇨')
        await msgembed.add_reaction('🇩')
        reaction = await self.client.wait_for("reaction_add", timeout=None, check=check)
        return msgembed



























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