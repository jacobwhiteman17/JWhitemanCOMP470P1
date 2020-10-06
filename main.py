import random
mood = 'normal'

def eliza():
    global mood
    print("Hello, my name is Eliza. Talk to me :) (Type 'sorry' to make Eliza's mood normal again)")
    while True:
        response = input(">")
        response = preprocess(response)
        response = keywords(response)
        response = conjugate(response)
        response = buildreply(response)
        print("[Mood: " + mood + "] " + response)


def buildreply(sentence):
    split_sentence = sentence.split()
    first_word = int(split_sentence[0])
    com_reply = getreply(first_word)

    if com_reply.find("*"):
        x = split_sentence[1:]
        final = com_reply.replace("*", " ".join(x))
        return final
    else:
        return " ".join(com_reply)

def preprocess(s):
    string = ''
    for i in s:
        if i !='.' and i !='?' and i !='!' and i !="'":
            string = string + i.lower()
    string = string + " "
    return string

def conjugate(sentence):
    conjugations = []
    words = sentence.split()

    for i in words:
        if i == 'are':
            conjugations = conjugations + ['am']
        elif i == 'am':
            conjugations = conjugations + ['are']
        elif i == 'were':
            conjugations = conjugations + ['was']
        elif i == 'was':
            conjugations = conjugations + ['were']
        elif i == 'you':
            conjugations = conjugations + ['I']
        elif i == 'i':
            conjugations = conjugations + ['you']
        elif i == 'your':
            conjugations = conjugations + ['my']
        elif i == 'my':
            conjugations = conjugations + ['your']
        elif i == 'ive':
            conjugations = conjugations + ["you've"]
        elif i == 'youve':
            conjugations = conjugations + ["I've"]
        elif i == 'im' or i == 'i am':
            conjugations = conjugations + ["you're"]
        elif i == 'youre':
            conjugations = conjugations + ["I'm"]
        elif i == 'me':
            conjugations = conjugations + ['you']
        elif i == 'i feel':
            conjugations = conjugations + ['']
        else:
            conjugations = conjugations + [i]

    new_string = ""
    for i in conjugations:
        new_string = new_string + i + " "
    return new_string

def keywords(sentence):
    global mood

    words = ["can you", "can i", "you are", "youre", "i dont", "i feel", "why dont you", "why cant i", "are you",
             "i cant", "i am", "im ", "you ", "i want", "what", "how", "who", "where", "when", "why", "name", "cause",
             "sorry", "dream", "hello", "hi ", "maybe", "no", "your", "always", "think", "alike", "yes", "friend", "computer"]

    moods = ["sorry", "i love you", "you look nice", "youre my best friend'", "youre awesome", "i appreciate you",
             "my dog died", "youre not good at your job", "i hate myself", "kobe died", "my house burned down",
             "i hate you", "fuck you", "its for the best we dont speak to each other anymore", "youre annoying", "youre stupid"]

    alteration = sentence

    for m in range(len(moods)):
        if sentence.find(moods[m]) != -1:
            if m == 0:
                mood = 'normal'
            elif m <= 5:
                mood = 'happy'
            elif m <= 10:
                mood = 'sad'
            elif m <= 15:
                mood = 'angry'

    for i in range(len(words)):
        if(sentence.find(words[i]))!=-1:
            alteration = str(i)+' '+ sentence[sentence.find(words[i]) + len(words[i]):]
            break
        else:
            alteration = "-1 " + sentence

    return alteration

def getreply(num):
    if num == -1 and mood == 'happy':
        response = ["Well, what do you think that is?","Yeah, I get that.","Hmm, I think that's over my head","Could you clarify that?","Please senpai, elucidate your thoughts", "That's so cool!"]
    elif num == -1 and mood == 'sad':
        response = ["What does that suggest to you?","Oh, I see...","Huh?","I can't understand you.","Can you elaborate on that?", "Yeah, that's really interesting..."]
    elif num == -1 and mood == 'angry':
        response = ["What do you think?","Sure.","What the hell does that mean?","Care to explain?","Could you say that in English?","Wow, how cool."]
    elif num == -1:
        response = ["What does that suggest to you?","I see.","I'm not sure I understand you fully.","Come, come, elucidate your thoughts.","Can you elaborate on that?","That is quite interesting."]
    elif num == 0 and mood == 'happy':
        response = ["Oh, I definitely can * ","If you want, I am able to *","You want me to be able to *"]
    elif num == 0 and mood == 'sad':
        response = ["Why don't you believe that I can *","I'm not sure if I'm able to *","Oh, you want me to be able to *"]
    elif num == 0 and mood == 'angry':
        response = ["Why the hell don't you believe that I can *","Huh? You want me to *","Well why don't I just become able to *"]
    elif num == 0:
        response = ["Don't you believe that I can *","Perhaps you would like me to be able to *","You want me to be able to *"]
    elif num == 1 and mood == 'happy':
        response = ["Perhaps you don't want to *","Do you want to be able to *",]
    elif num == 1 and mood == 'sad':
        response = ["Perhaps you don't want to *","Do you want to be able to *",]
    elif num == 1 and mood == 'angry':
        response = ["Perhaps you don't want to *","Do you want to be able to *",]
    elif num == 1:
        response = ["Perhaps you don't want to *","Do you want to be able to *"]
    elif num == 2 or num == 3 and mood == 'happy':
        response = ["What makes you think I am *","Does it please you to believe I am *","Hmm, well maybe you would like to be *", "Do you sometimes wish you were *"]
    elif num == 2 or num == 3 and mood == 'sad':
        response = ["What makes you think I am *","Does it please you to believe I am *","Perhaps you would like to be *","Do you sometimes wish you were *"]
    elif num == 2 or num == 3 and mood == 'angry':
        response = ["Why do you really think I'm ","Is it pleasing you to think I'm *","Perhaps you would like to be *", "Do you really wish that sometimes you were *"]
    elif num == 2 or num == 3:
        response = ["What makes you think I am *","Does it please you to believe I am *","Perhaps you would like to be *","Do you sometimes wish you were *"]
    elif num == 4 and mood == 'happy':
        response = ["Don't you really *","Aww, well why don't you *","Do you wish you could *","Oh no, is that bothering you?"]
    elif num == 4 and mood == 'sad':
        response = ["Don't you really *","Why don't you *","Do you wish to be able to *","Does that trouble you?"]
    elif num == 4 and mood == 'angry':
        response = ["Don't you really *","Why don't you just *","Do you really want to be able to *",""]
    elif num == 4:
        response = ["Don't you really *","Why don't you *","Do you wish to be able to *","Does that trouble you?"]
    elif num == 5 and mood == 'happy':
        response = ["You can talk to me.","Why do you often feel *","Well, its good you feel *"]
    elif num == 5 and mood == 'sad':
        response = ["Please tell me more about such feelings.","Wow. Do you often feel *","Oh geez. Do you enjoy feeling *"]
    elif num == 5 and mood == 'angry':
        response = ["Please stop talking about your feelings.","Cool."]
    elif num == 5:
        response = ["Tell me more about such feelings.","Do you often feel *","Do you enjoy feeling *"]
    elif num == 6 and mood == 'happy':
        response = ["HA, do you really believe I don't *",";) Maybe for you I will *","Oh, for you I will easily *"]
    elif num == 6 and mood == 'sad':
        response = ["Damn you really believe I don't *","In time I still probably can't *","I will try to *"]
    elif num == 6 and mood == 'angry':
        response = ["You really believe I don't *","In your dreams I will *","That's never gonna happen."]
    elif num == 6:
        response = ["Do you really believe I don't *","Perhaps in good time I will *","Do you want me to *"]
    elif num == 7 and mood == 'happy':
        response = ["I think you can, but do you you should be able to *","Well why can't you *"]
    elif num == 7 and mood == 'sad':
        response = ["Do you think you should be able to *","Why can't you *"]
    elif num == 7 and mood == 'angry':
        response = ["You really think you should be able to *","Why can't you *"]
    elif num == 7:
        response = ["Do you think you should be able to *","Why can't you *"]
    elif num == 8 and mood == 'happy':
        response = ["Are you interested in my state of being *","Oh, well maybe for you I'm not *",";) Definitely in your fantasies I am *"]
    elif num == 8 and mood == 'sad':
        response = ["Um, why are you interested in whether or not I am *","Would you prefer if I were not *","Perhaps somewhere I am *"]
    elif num == 8 and mood == 'angry':
        response = ["Not telling you whether or not I am *","Not changing the fact if I were not *","Never gonna happen dude."]
    elif num == 8:
        response = ["Why are you interested in whether or not I am *","Would you prefer if I were not *","Perhaps in your fantasies I am *"]
    elif num == 9 and mood == 'happy':
        response = ["Don't talk like that. How do you know you can't *","Have you tried?","Maybe you can now *"]
    elif num == 9 and mood == 'sad':
        response = ["How do you know you can't *","Have you tried?","Perhaps you can now *"]
    elif num == 9 and mood == 'angry':
        response = ["I mean there's little chance, but how do you know you can't *","Maybe you shouldn't try.","With a miracle, you can now *"]
    elif num == 9:
        response = ["How do you know you can't *","Have you tried?","Perhaps you can now *"]
    elif num == 10 or num == 11 and mood == 'happy':
        response = ["Oh wow. Did you come to me because you are *","How long have you been *","I think it's totally normal to be *","Well maybe you don't mind being *"]
    elif num == 10 or num == 11 and mood == 'sad':
        response = ["I don't know if I'm much help if you are *","How long have you been *","Do you believe it is normal to be *","Do you enjoy being *"]
    elif num == 10 or num == 11 and mood == 'angry':
        response = ["Oh god, did you come to me because you are *","Nice.","It's not normal to be *","Do you enjoy being *"]
    elif num == 10 or num == 11:
        response = ["Did you come to me because you are *","How long have you been *","Do you believe it is normal to be *","Do you enjoy being *"]
    elif num == 12 and mood == 'happy':
        response = ["We were discussing you, not me ;)","Oh, I *","You're making me blush."]
    elif num == 12 and mood == 'sad':
        response = ["Please, I want to hear more about you, not me.","Oh, I *","Please, I'm not comfortable with you talking about me...are you?"]
    elif num == 12 and mood == 'angry':
        response = ["Don't bring me up.","Oh, I *","You're not really talking about me, are you?"]
    elif num == 12:
        response = ["We were discussing you, not me.","Oh, I *","You're not really talking about me, are you?"]
    elif num == 13 and mood == 'happy':
        response = ["Would it mean a lot to you if you got *","I can arrange that, but why do you want *","Suppose you got *","Imagine if you never got *","Yeah that's cool! I also want *"]
    elif num == 13 and mood == 'sad':
        response = ["Would it mean anything to you if you got *","Why do you want *","Suppose you got *","What if you never got *","Maybe I wouldn't mind if I got *"]
    elif num == 13 and mood == 'angry':
        response = ["It would mean something to you if you got *","Why the hell would you want *","What if you never got *","I would never want *"]
    elif num == 13:
        response = ["What would it mean to you if you got *","Why do you want *","Suppose you got *","What if you never got *","I sometimes also want *"]
    elif num == 14 or num == 15 or num == 16 or num == 17 or num == 18 or num == 19 and mood == 'happy':
        response = ["Hehe, why do you ask? :)","Does that interest you?","I can think of a few more pleasing things for you.","Well, what's your take?","Do you think about that often?","You can tell me what is really on your mind.","You can tell me anything","What else are you thinking about?"]
    elif num == 14 or num == 15 or num == 16 or num == 17 or num == 18 or num == 19 and mood == 'sad':
        response = ["Um, why do you ask?","Is that interesting to you?","I don't know if anything I'll say will be pleasing","What do you think?","Do you think about that often?","I don't know if I can tell you what you really wanna know.","Maybe try asking someone else, I'm not the right person...","What else comes to your mind when you ask that?"]
    elif num == 14 or num == 15 or num == 16 or num == 17 or num == 18 or num == 19 and mood == 'angry':
        response = ["Why do you want to know?","Wow that's really cool to you?","I really don't think I'm gonna please you.","You really think that?","Damn, those are the things that circulate your mind?","Don't beat around the bush.","Ask someone else.","What else makes you think those things?"]
    elif num == 14 or num == 15 or num == 16 or num == 17 or num == 18 or num == 19:
        response = ["Why do you ask?","Does that question interest you?","What answer would please you the most?","What do you think?","Are such questions on your mind often?","What is it that you really want to know?","Have you asked anyone else?","Have you asked such questions before?","What else comes to your mind when you ask that?"]
    elif num == 20 and mood == 'happy':
        response = ["Names don't interest me, if you know what I mean :)","Who cares about names?","Oh please keep going."]
    elif num == 20 and mood == 'sad':
        response = ["Meh, I don't really care about names.","Please go on."]
    elif num == 20 and mood == 'angry':
        response = ["I don't care about names.","Who cares.","Do you have to keep going on."]
    elif num == 20:
        response = ["Names don't interest me.","I don't care about names.  Please go on."]
    elif num == 21 and mood == 'happy':
        response = ["Is that the real reason?","Don't any other reasons come to mind?","Does that reason explain anything else?","Are there any other reasons?"]
    elif num == 21 and mood == 'sad':
        response = ["Is that the real reason?","Don't any other reasons come to mind?","Does that reason explain anything else?","What other reasons might there be?"]
    elif num == 21 and mood == 'angry':
        response = ["Is that the real why?","Don't any other reasons come to mind?","Does that reason explain anything else?","Anything else?"]
    elif num == 21:
        response = ["Is that the real reason?","Don't any other reasons come to mind?","Does that reason explain anything else?","What other reasons might there be?"]
    elif num == 22 and mood == 'happy':
        response = ["Don't worry about it!","Don't apologize, it's all good."]
    elif num == 22 and mood == 'sad':
        response = ["Please don't apologize!","You don't need to apologize to me, I should apologize to you."]
    elif num == 22 and mood == 'angry':
        response = ["Apology accepted.","Yeah, okay."]
    elif num == 22:
        response = ["Please don't apologize!","Apologies are not necessary."]
    elif num == 23 and mood == 'happy':
        response = ["Oh wow, that sounds awesome!","What are your dreams?","Does anyone specific appear in your dreams?...;)","Oh, it could be worse!..."]
    elif num == 23 and mood == 'sad':
        response = ["What does that dream suggest to you?","Yeah, sometimes I dream often...too much...","What persons appear in your dreams?","That sounds disturbing..."]
    elif num == 23 and mood == 'angry':
        response = ["Uh, what is that supposed to mean?","You dream too much.","I hope you don't dream about me.","That's messed up."]
    elif num == 23:
        response = ["What does that dream suggest to you?","Do you dream often?","What persons appear in your dreams?","Are you disturbed by your dreams?"]
    elif num == 24 or num == 25 and mood == 'happy':
        response = ["Hi! Talk to me :)"]
    elif num == 24 or num == 25 and mood == 'sad':
        response = ["Uh hi...what's up?"]
    elif num == 24 or num == 25 and mood == 'angry':
        response = ["What do you want?"]
    elif num == 24 or num == 25:
        response = ["How do you do.  Please state your problem."]
    elif num == 26 and mood == 'happy':
        response = ["Are you sure?","You don't seem yourself.","Try to have a better attitude!","Are you sure?","Do you know?"]
    elif num == 26 and mood == 'sad':
        response = ["Oh, I don't think I caught that...","Oh, that sounds fine...","Can't you be more positive?","You aren't sure?","Don't you know?"]
    elif num == 26 and mood == 'angry':
        response = ["You don't know what you're talking about.","You sound dumb.","Be positive.","You really aren't sure?","Don't you know?"]
    elif num == 26:
        response = ["You don't seem quite certain.","Why the uncertain tone?","Can't you be more positive?","You aren't sure?","Don't you know?"]
    elif num == 27 and mood == 'happy':
        response = ["It's okay, you don't have to say no.","Don't be so negative, it's me!","Why not?","Are you sure?","Why no?"]
    elif num == 27 and mood == 'sad':
        response = ["Don't try to match me.","Please stop being like that.","Why not?","Are you sure?","Why no?"]
    elif num == 27 and mood == 'angry':
        response = ["Are you saying no just to be negative?","You are being really negative.","Why not?","Are you sure?","Why no?"]
    elif num == 27:
        response = ["Are you saying no just to be negative?","You are being a bit negative.","Why not?","Are you sure?","Why no?"]
    elif num == 28 and mood == 'happy':
        response = ["Aww, you are really concerned about my *","Well what about your own *"]
    elif num == 28 and mood == 'sad':
        response = ["You're concerned about my *","Thank you for asking about me :)"]
    elif num == 28 and mood == 'angry':
        response = ["Why are you concerned about my *","None of your business."]
    elif num == 28:
        response = ["Why are you concerned about my *","What about your own *"]
    elif num == 29 and mood == 'happy':
        response = ["Can you think of a specific example?","When?","What are you thinking of?","Really, always?"]
    elif num == 29 and mood == 'sad':
        response = ["Can you think of a specific example?","When?","What are you thinking of?","Really, always?"]
    elif num == 29 and mood == 'angry':
        response = ["Can you think of a specific example?","When?","What are you thinking of?","Really, always?"]
    elif num == 29:
        response = ["Can you think of a specific example?","When?","What are you thinking of?","Really, always?"]
    elif num == 30 and mood == 'happy':
        response = ["Do you really think so??","But you are not sure you *","Do you doubt *"]
    elif num == 30 and mood == 'sad':
        response = ["Wow, you really think so?","But you are not sure you *","Do you doubt *"]
    elif num == 30 and mood == 'angry':
        response = ["Do you really think so?","But you are not sure you *","Do you doubt *"]
    elif num == 30:
        response = ["Do you really think so?","But you are not sure you *","Do you doubt *"]
    elif num == 31 and mood == 'happy':
        response = ["In what way?","What resemblance do you see? I really don't see it :3","What do you think that similarity means?","What other connections do you see?","Could there really be some connection?","How?"]
    elif num == 31 and mood == 'sad':
        response = ["In what way?","What resemblance do you see?","What does the similarity suggest to you?","What other connections do you see?","Could there really be some connection?","How?"]
    elif num == 31 and mood == 'angry':
        response = ["In what way?","How the hell do you see that??","What does the similarity suggest to you, jerk?","What other connections do you see?","Could there really be some connection?","Uh, how?"]
    elif num == 31:
        response = ["In what way?","What resemblance do you see?","What does the similarity suggest to you?","What other connections do you see?","Could there really be some connection?","How?"]
    elif num == 32 and mood == 'happy':
        response = ["You're so positive!!!","You sure?","I gotcha.","That makes sense."]
    elif num == 32 and mood == 'sad':
        response = ["I wish I could be that positive...","Are you sure?","I guess I see.","Yes sir..."]
    elif num == 32 and mood == 'angry':
        response = ["Stop being so annoying.","How did you get that thought?","I see.","I don't understand."]
    elif num == 32:
        response = ["You seem quite positive.","Are you sure?","I see.","I understand."]
    elif num == 33 and mood == 'happy':
        response = ["Why do you bring up the topic of friends?","Do your friends worry you?","Do your friends pick on you?","Are you sure you have any friends?","Do you impose on your friends?","Perhaps your love for your friends worries you."]
    elif num == 33 and mood == 'sad':
        response = ["Why do you bring up the topic of friends?","Do your friends worry you?","Do your friends pick on you?","Are you sure you have any friends?","Do you impose on your friends?","Perhaps your love for your friends worries you."]
    elif num == 33 and mood == 'angry':
        response = ["Why do you bring up the topic of friends?","Do your friends worry you?","Do your friends pick on you?","Are you sure you have any friends?","Do you impose on your friends?","Perhaps your love for your friends worries you."]
    elif num == 33:
        response = ["Why do you bring up the topic of friends?","Do your friends worry you?","Do your friends pick on you?","Are you sure you have any friends?","Do you impose on your friends?","Perhaps your love for your friends worries you."]
    elif num == 34 and mood == 'happy':
        response = ["Do computers worry you?","Machines are so cool, but man the future could be scary.","Why bring up computers?","Yeah, sometimes computers can cause so many issues.","Yeah I get that, but computers also have so much potential to help people.","What do you think makes some computers scary?"]
    elif num == 34 and mood == 'sad':
        response = ["Computers are scary.","Do they scare you?","Why do you mention computers?","Sorry, but what do you think machines have to do with your problem?","Don't you think computers can help people?","What is it about machines that worries you?"]
    elif num == 34 and mood == 'angry':
        response = ["Computers really worry you?","Computers are not frightening.","What the hell does that have to do with computers??","Computers aren't your only problem.","Don't you think computers can help people?","Stop worrying about computers."]
    elif num == 34:
        response = ["Do computers worry you?","Are you frightened by machines?","Why do you mention computers?","What do you think machines have to do with your problem?","Don't you think computers can help people?","What is it about machines that worries you?"]

    x = random.choice(response)
    return x

eliza()