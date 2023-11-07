import discord
import responses
import asyncio
import random


#method for sending messages
async def send_message(message, user_message):

    #get responses from responses and use the handle_response function which take parameter user message
    response = responses.handle_response(user_message)
    
    #speical condition for !choose command
    #using this for a animation type command in text
    if(response[0]=="spin"):

        #change spin option to resonse[1] which contains all randomized options
        spin_options = response[1]

        #run a for loop thru the randomized list and output every random element from randomized list
        for i in range(len(spin_options)):
             await message.channel.send(f"➡  {spin_options[i]}  ⬅" )
             await asyncio.sleep(.2)

        #output final message of what it landed on
        await message.channel.send(f"\n\u200b It Landed on:    ❌ {spin_options[-1]} ❌")

    #speical condition for !roll command
    #implemented this so that the text displays after the gif
    #different than the others as the text displays before image for !cards and !flip
    elif(response[0]=="dice"):
        await message.channel.send(file=discord.File("visuals/dice.gif", 'gif.gif'))
        await asyncio.sleep(1)
        await message.channel.send(f"\n\u200b You Rolled:     ❌   {response[-1]}   ❌")

    #handles general cases
    else:
        gif_path = f"visuals/{response[1]}"

        #open as read binary
        with open(gif_path, 'rb') as img:
            await message.channel.send(f"{response[0]}\n\u200b",file=discord.File(img, 'gif.gif'))




#method for the dicord bot itself
def run_discord_bot():

    #set token value 
    TOKEN = "YOUR TOKEN HERE"

    #intents
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    #create a new event
    @client.event
    #default display message on ready
    async def on_ready():
        print(f"{client.user} is now running")  

    #new event6
    @client.event
    #when a message is sent
    async def on_message(message):
        #if the message by the user is the same as the bot return nothing
        if message.author == client.user:
            return
        
        #set values
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel) 

        #display message in python terminal
        print(f"{username} said: {user_message} {channel}")

        #send message with parameters
        await send_message(message,user_message)
        


    #run bot with token  
    client.run(TOKEN)
