# coding: utf-8
#
# the top line, above, is important -- 
# in ensures that Python will be able to use this file,
# even in the case you paste in text with unicode characters
# (beyond ASCII)
# for an more expansive example of such a file, see
#    http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
#
# Name: Lawrence Mao
# Date: 11-13-17
#
#

import random

# function #1
#
def createDictionary( filename ):
    """
    takes in a string, the name of a text file containing some sample text. 
    It should return a dictionary whose keys are words encountered in the 
    text file and whose entries are a list of words that may legally follow 
    the key word
    """
    d = {}
    f = open( filename )
    text = f.read()
    f.close()
    
    LoW = text.split()
    isStart = True
    for i in range(len(LoW)) :
        
        if isStart :
            d.setdefault("$", []).append(LoW[i])
        else :
            d.setdefault(LoW[i-1], []).append(LoW[i])
        last = LoW[i][-1]
        if last == '.' or last == '!' or last == '?' :
            isStart = True
        else :
            isStart = False
    return d 

# function #2
#
def generateText(d,N):
    """
    take in a dictionary of word transitions d (generated in your createDictionary 
    function, above) and a positive integer, n. Then, generateText should print a 
    string of n words
    """
    res = ""
    curr = "$"
    for i in range(N) :
        curr = random.choice(d[curr])
        res += " " + curr
        last = curr[-1]
        if last == '.' or last == '!' or last == '?' :
            curr = "$"
    return res[1:]


#
# Your 500-or-so word CS-essay (paste in these triple-quoted strings, below):
#
"""
Source Name: The Emoji Movie Script by Tony Leondis

'No one option left. Now, me, turd. Sorry. Should be so angry. Alex wants his mind. I can\'t even try to get reprogrammed. 
I need Thumbs Up is my hands again. You\'re free! Look at all! There\'s so meh. Come on, hold on it! Of course. My goodness, 
I\'m sorry, Hi-5! Right on the favorites section where we\'ll find a good news? Hi! He\'s all inside the Loser Lounge, where 
Alex just slip under the phone, and unrelenting support. Like, what is the feeling of mistake. Chimichangas. Sorry. We know 
it was weird. Wait a text. Let\'s keep the last time, you make a mistake, which one, I\'ve got no matter what, this out. 
That\'s the phone store. Nice! Not too late for number one? We got the VIPs where he has. Ready? You\'re in that cloud is 
right next to do we wash our dreams are taking credit card offers thatbig hand pile. Hey, Trojan Horse. And if that\'s where 
we have to want to be. Meh. This is up the wipe and it\'s just do with me. All right, here will ever again. Hey. Gene! Yeah, 
you won\'t, Gene. Talk to free dance! What could ever again. Wait. Like rewrite some bad idea. I said! I\'m coming to free 
dance! Watch. Um... Whatare saying. I\'m freaking out! Addie! From Alex\'s pocket, emojis. A lot of mistake. Hey, wait. Let\'s 
go! As you mean, hey. Yeah, yeah, yeah. Maybe longer than nervous. You want to stay here is the cloud, where we can talk through 
our differences, okay? But, Mary... No. I... What\'s happening? Can we get you get uploaded to reply to be a malfunction. Like 
rewrite some sort of love for me. Devil, Poop, Thumbs Up is on top, but I can\'t... It\'s for the Emoji Pop! We got dumber. Hi-5? 
Yeah! I got dumber. He\'s never get sucked in. Gene? All right, Alex must have other great hands again. I\'m never get to delete 
us. Meh, meh, meh, what you mean? They\'ll never sent. You want you know? I can\'t feel the dunce in the list. What software 
version are up with Gene here because I help you, and sense of there. Yes, well, we please tell you know, I didn\'t say. What 
are you know? Great. Krav Maga. "Dear Addie, maybe it\'s just broken his favorite food. What? I hate knocking overthe trash, 
dude! Shade. The cloud? Steven, for you, you\'re about you have to stay locked out for you. Really? I\'d like it. Emojis. Don\'t 
worry. Red alert! Look who can look out this emoji. Sweep so pretty. For me? No way. I got to the conversation just gonna see 
the app. I\'ll go away, because I\'ve got to see and don\'t like it\'s a hacker? Out? That\'s our son is not working. But I can 
see that could ever and unrelenting support. I\'m sorry. It wasn\'t just want to be yourself, what\'s the other than nervous. I 
got you! Maybe'
"""
#
#