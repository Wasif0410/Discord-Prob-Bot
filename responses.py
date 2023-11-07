import discord
import random

def handle_response(message):

    #turn passed messgae into lowercase
    p_message = message.lower()

    
    if p_message =="!flip":

        #set random integer 1 or 2 in variable x
        #set list of gif names
        x = int(random.randint(1,2))
        Gif = ["heads.gif", "tails.gif"]

        #random number is either 1 or 2
        #return string with corresponding gif
        if x == 1:
            return ["⚪ You got: ", Gif[0]]

        else:
            return ["⚪ You got: ", Gif[1]]



    if p_message =="!roll":
        #return keyword dice and random int 1-6
        return ["dice", str(random.randint(1,6))]
    


    if "!choose " in p_message:

        #collect message after thhe !choose and turn into string, split by spaces
        new_message = p_message[8:]
        p_list = new_message.split(" ")

        rand_list =[]
        
        #use a for loop to create another rand_list which has elements in random order
        for i in range(5):
            y = int(random.randint(0, len(p_list)-1))
            rand_list.append(p_list[y])

        #return the keyword spin, the list of random order elements
        return ["spin", rand_list]
    
    
    
    if p_message == "!cards":
        
        #create array of options
        face = ['A','K','Q','J','2','3','4','5','6','7','8','9','10']
        suit = ['Hearts (♥)','Club (♣)','Diamond (♦)','Spade (♠)']
        Gif = ["hearts.gif", "clubs.gif", "diamond.gif", "spades.gif"]

        #get a random face card and random suit
        ranFace = int(random.randint(0,len(face)-1))
        ranSuit = int(random.randint(0,len(suit)-1))

        #return the face or card + suit + image corresponding to the suit
        return [f"⚪ {face[ranFace]} of {suit[ranSuit]}", Gif[ranSuit]]

    
   