label ocwednesday:
    show text " DAY 3 - WEDNESDAY "
    pause 1.5
    play music "audio/home.mp3"
    scene mcroom with dissolve
    " Morning, sleepyhead. "
    " Hopefully you did, because you're going to school again, woohoo. "
    " Another long day you're going to have to deal with... "
    " ...So you better get a whole lot of energy ready. "
    " You make yourself breakfast, do a little gaming... "
    " What, expected to study? Studying's for losers. "
    " Atleast in my opinion. "
    " You waited until it was the right time to go to school... "
    " ...And skedaddled your way over there!! "
    scene black with dissolve
    stop music fadeout 1.5
    pause 2.0
    play music "audio/paperhigh.mp3" fadein 1.5
    scene paperschoolfront with dissolve
    " You walked to the front of the school and found some guy covering his face while trying to find something. "
    " You recognized him as one of your classmates...let's see if you can help him. "
    show jacobneutral at center with easeinleft
    if jacobknow == True:
        jac " God damn it, where are they...?! "
        " You took a closer look and turns out he was missing his goggles and bandana. "
        " You've heard that he didn't like showing off his facial features, so you could understand the pain he's going through right now. "
        " Thing is, who would do this to him? Someone just did this to make fun of him most likely. "
        " It didn't take long for him to realize that you were there, and he just covered himself even more. "
        hide jacobneutral at bottom
        show jacobangry at center
        jac " Don't look at me! go away! " with vpunch
        " You told him that you weren't going to look at his ace, and that you only wanted to help him out. "
        " You promised. No making fun of him or anything. "
        hide jacobangry at bottom
        show jacobneutral at center
        jac " ...W...well, I appreciate you trying to help, but I can do this on my own! "
        jac " Some baffoon just decided to pull down my goggles and bandana and threw it away somewhere! "
        jac " And most people would know that I don't like showing off my face... "
        jac " It's just completely sick! I've been struggling to find my goggles and bandana for MINUTES now... "
        jac " I'm sure history class has already started by now! "
        jac " ...Well, I haven't heard the bell ring, but still! I can do this on my own! "
        jac " Thank you for offering your help, but I don't want it! "
        " Seems like he's being a little stubborn. "
        " What should you do? "
        menu:
            " Help him ":
                $ jacoblv += 10
                hide jacobneutral at bottom
                show jacobsurprised at center
                jac " ...H...huh??? "
                jac " You still want to help me, even though I told you to go away? "
                hide jacobsurprised at bottom
                show jacobneutral at center
                jac " ...Well, if it gets you to go away from me, then fine. "
                jac " And remember, DON'T LOOK AT MY FACE! "
                jac " I'll hate you if you do. Even when you think I'm not looking, I'd KNOW that you're looking. "
                jac " GOT THAT?! "
                " You nodded. You did wonder though... "
                " Why does he want to cover up his face so much? "
                " You decided not to actually ask him that though. "
                " It's probably a more personal matter. "
                scene black with dissolve
                " Before class started, you helped him find his goggles and bandana. "
                " You eventually found them behind a trash bin near you two. "
                " You gave him his belongings before he went inside of the school, thanking you. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, time for your first class. "
                " You walked into your school and went to your classroom for history class. "
                pause 2.0
                jump wedhistoryclass1
            " Leave him be ":
                " You decided to just leave him be. "
                " He DID tell you to leave him alone, so...you're going to do just that. "
                " You then went to your classroom for your first class of the day. "
                scene black with dissolve
                pause 2.0
                jump wedhistoryclass1
    else:
        x " God damn it, where are they...?! "
        " You took a closer look and turns out he was missing his goggles and bandana. "
        " You've heard that he didn't like showing off his facial features, so you could understand the pain he's going through right now. "
        " Thing is, who would do this to him? Someone just did this to make fun of him most likely. "
        $ jacobknow = True
        " You've also heard that this guy's name was Jacob. "
        " It didn't take long for him to realize that you were there, and he just covered himself even more. "
        hide jacobneutral at bottom
        show jacobangry at center
        jac " Don't look at me! go away! " with vpunch
        " You told him that you weren't going to look at his ace, and that you only wanted to help him out. "
        " You promised. No making fun of him or anything. "
        hide jacobangry at bottom
        show jacobneutral at center
        jac " ...W...well, I appreciate you trying to help, but I can do this on my own! "
        jac " Some baffoon just decided to pull down my goggles and bandana and threw it away somewhere! "
        jac " And most people would know that I don't like showing off my face... "
        jac " It's just completely sick! I've been struggling to find my goggles and bandana for MINUTES now... "
        jac " I'm sure history class has already started by now! "
        jac " ...Well, I haven't heard the bell ring, but still! I can do this on my own! "
        jac " Thank you for offering your help, but I don't want it! "
        " Seems like he's being a little stubborn. "
        " What should you do? "
        menu:
            " Help him ":
                $ jacoblv += 10
                hide jacobneutral at bottom
                show jacobsurprised at center
                jac " ...H...huh??? "
                jac " You still want to help me, even though I told you to go away? "
                hide jacobsurprised at bottom
                show jacobneutral at center
                jac " ...Well, if it gets you to go away from me, then fine. "
                jac " And remember, DON'T LOOK AT MY FACE! "
                jac " I'll hate you if you do. Even when you think I'm not looking, I'd KNOW that you're looking. "
                jac " GOT THAT?! "
                " You nodded. You did wonder though... "
                " Why does he want to cover up his face so much? "
                " You decided not to actually ask him that though. "
                " It's probably a more personal matter. "
                scene black with dissolve
                " Before class started, you helped him find his goggles and bandana. "
                " You eventually found them behind a trash bin near you two. "
                " You gave him his belongings before he went inside of the school, thanking you. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, time for your first class. "
                " You walked into your school and went to your classroom for history class. "
                pause 2.0
                jump wedhistoryclass1
            " Leave him be ":
                " You decided to just leave him be. "
                " He DID tell you to leave him alone, so...you're going to do just that. "
                " You then went to your classroom for your first class of the day. "
                scene black with dissolve
                pause 2.0
                jump wedhistoryclass1

label wedhistoryclass1:
    scene classroom with dissolve
    " You sat down in your seat and patiently waited for the teacher to arrive. "
    show mrclioneutral at center with easeinright
    " A few minutes later, the teacher walks in and stands infront of the class. "
    " Everyone greets him a good morning. "
    mscl " Good morning everyone. "
    mscl " Let's start our lesson for today. "
    mscl " And remember, no using your phones unless if I say so. "
    mscl " Get your notebooks and pens out. "
    mscl " Nothing else, otherwise I'm sending you to detention. "
    " Awww, but you wanted to take photos of the things that he's teaching about... "
    " Oh well. Whatever the teacher says is what's gonna happen. "
    " Can't really change anything about that. "
    " If you did try to change something about that, then you'd probably get sent to detention. "
    " Or even worse, suspension or you're gonna get expelled. "
    " Thankfully, you're not doing that anytime soon. "
    " Otherwise this route wouldn't even happen in the first place. "
    scene black with dissolve
    " You spent the rest of class hours taking down notes and trying to understand the topic more. "
    " You do sound like a nerd here, but you're trying to get your grades up. "
    " After all, you're in a prestigious school. You can't really let people's expectations down. "
    " ...Actually, that sounds pretty bad. You've still gotta chillax here and there. "
    " But yeah, you just take down notes here and there. "
    " And also ask some questions to understand the lesson more. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, time for the first break of the day. "
    " You put your things back into where they belong, and you went into the hallway to take a break. "
    " Let's see what the day has in store for you today... "
    pause 2.0
    jump wedocbreak1

label wedocbreak1:
    scene hallway with dissolve
    " Where do you want to hangout for today? "
    if pythonchallenge == True:
        " A card gets slapped onto your face before you could decide where to go. "
        " Time to read this... "
        " 'First to greet, last to see...' "
        " 'A gate to learning's mystery.' "
        " 'Where names are carved and flags may fly,' "
        " 'The number rests where strangers pass by.' "
        " You've got a good idea on where this might be... "
        " Where do you go? "
        pass
    else:
        pass
    menu:
        " {image=carmenicon} The front of the school {image=yinyangicon} ":
            jump wedocfrontschool1
        " {image=koaicon} The back of the school {image=orchidicon} ":
            jump wedocbackschool1
        " {image=jamicon} The gym {image=miaicon} ":
            jump wedocgym1
        " {image=diskicon} The cafeteria {image=sparkicon} ":
            jump wedoccafeteria1
        " {image=jacobicon} The rooftop {image=matteicon} ":
            jump wedocrooftop1
        " {image=noxicon} The library {image=temeroicon} ":
            jump wedoclibrary1

label wedocfrontschool1:
    # carmen, yinhui and yangyi
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school and spotted three of your classmates hanging out. "
    if pythonchallenge == True:
        $ pythoncode0 = True
        " Before the narrator could add anything more to that dialgue... "
        " You spot a card near a bush. "
        " You pick it up and it was the number zero... "
        " You put it into your pocket, and before you could do anything else, a piece of paper gets slapped onto your face. "
        " It's another thing. Let's see... "
        " 'You've searched the halls low and high...' "
        " 'With clever steps and a watchful eye.' "
        " 'Now one last task, you're nearly through - ' "
        " 'A hidden door awaits for you.' "
        " 'Behind it's frame, the path is clear - ' "
        " 'You've earned the right to enter here.' "
        " There's another note at the back of it... "
        " 'PS: Meet me at the third break of the day. <3' "
        " Well...okay. Back to normal shenanigans."
        pass
    else:
        pass
    " You're thinking of talking to one of them, but who do you talk to? "
    if carmenknow,yinhuiknow,yangyiknow == True:
        menu:
            " {image=carmenicon} Carmen {image=carmenicon} ":
                jump lovelycavity
            " {image=yinyangicon} Yinhui and Yangyi {image=yinyangicon} ":
                jump thinkingaboutchu
    elif carmenknow,yinhuiknow == True and yangyiknow == False:
        menu:
            " {image=carmenicon} Carmen {image=carmenicon} ":
                jump lovelycavity
            " {image=yinyangicon} Yinhui and smoeone who looks like his twin {image=yinyangicon} ":
                jump thinkingaboutchu
    elif carmenknow,yangyiknow == True and yinhuiknow == False:
        menu:
            " {image=carmenicon} Carmen {image=carmenicon} ":
                jump lovelycavity
            " {image=yinyangicon} Yangyi and someone who looks like his twin {image=yinyangicon} ":
                jump thinkingaboutchu
    elif yinhuiknow,yangyiknow == True and carmenknow == False:
        menu:
            " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                jump lovelycavity
            " {image=yinyangicon} Yinhui and Yangyi {image=yinyangicon} ":
                jump thinkingaboutchu
    elif carmenknow == True and yinhuiknow,yangyiknow == False:
        menu:
            " {image=carmenicon} Carmen {image=carmenicon} ":
                jump lovelycavity
            " {image=yinyangicon} People who look like twins {image=yinyangicon} ":
                jump thinkingaboutchu
    elif yinhuiknow == True and carmenknow,yangyiknow == False:
        menu:
            " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                jump lovelycavity
            " {image=yinyangicon} Yinhui and someone who looks like his twin {image=yinyangicon} ":
                jump thinkingaboutchu
    elif yangyiknow == True and carmenknow,yinhuiknow == False:
        menu:
            " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                jump lovelycavity
            " {image=yinyangicon} Yangyi and someone who looks like his twin {image=yinyangicon} ":
                jump thinkingaboutchu
    else:
        menu:
            " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                jump lovelycavity
            " {image=yinyangicon} People who look like twins {image=yinyangicon} ":
                jump thinkingaboutchu

    label lovelycavity:
        show carmenneutral at center with easeinleft
        if carmenknow == True:
            " You walked over to him and noticed that he was just plucking the strings on his guitar... "
            " ...He looked really bored and didn't know what to do. "
            " It didn't really take him long for him to notice that you were there and looking at him. "
            ca " ...! "
            " He waves at you, and then gestures to his guitar, and then his head. "
            " From what you can undertand...he needed some song ideas. "
            " Then he shrugs, probably meaning that he doesn't have any song ideas right now. "
            hide carmenneutral at bottom
            show carmenhappy at center
            " Maybe you could help in giving him a song idea...wait, what's he doing? "
            " He looks like he has an idea in his eyes. "
            " If he was in a cartoon, he would've had a comically large lightbulb above his head. "
            " Too bad we're on a budget, so we can't really give him that. "
            " Anyway, he starts looking around you - looking at you in different angles, I mean. "
            " He seems to be thinking about something...maybe he's gonna use you as inspiration? "
            " You don't really know what to think about being used as inspiration. "
            hide carmenhappy at bottom
            show carmenneutral at center
            " Before he let himself do anything else, he asks you in sign language if it's okay to make a song based off of you. "
            " And yes, I'm going to make you understand sign language because I say so. "
            " He's being nice and respectful...he's gonna understand if you want to give him another idea. "
            " What do you say? "
            menu:
                " Let him use you as inspiration ":
                    $ carmenlv += 10
                    hide carmenneutral at bottom
                    show carmenhappy at center
                    ca " ...!! "
                    " Carmen seems pleased with your decision. "
                    hide carmenhappy at bottom
                    show carmenneutralb2 at center
                    " He takes one more good look at you before he starts to play a song... "
                    if kind == True:
                        " The song he plays has a nice happy tune to it. "
                        " Feels pretty warm, like you're back at home. "
                        " It honestly makes you feel safe and sound, like everything's going to be okay. "
                        " Like someone's going to help you no matter what... "
                        " ...Even if it hurts them, they're going to help you. "
                        " Someone who will always be there for you, even in your darkest of hours. "
                        " A sweet song, really. "
                    elif calm == True:
                        " The song he plays has a really nice tune to it. "
                        " It makes you feel as if you're at a beach and just relaxing... "
                        " Even through the worst of times, you know that everything's going to be okay in the end. "
                        " Just there relaxing and being calm - even if someone is yelling at you... "
                        " ...You just wont lose your cool and fight with them. "
                        " You know that they're just trying to ragebait you, so you just chillax. "
                        " A real nice tune. You could really use some coconut water to relax with now... "
                        " If you had this in your playlist, you'd be chillaxing everyday. "
                    elif mean == True:
                        " The song he plays has kind of a empty feeling at the start. "
                        " A cold and empty feeling, as if you're not letting yourself open up to anyone at first. "
                        " Pushing others away and telling them that you're basically not worth it... "
                        " That feeling is familiar to you. "
                        " As the song progresses, it gets more lively. "
                        " Like a flower getting ready to bloom, like the sun rising. "
                        " You get more comfortable with those around you. "
                        " And you learn to be comfortable with yourself, too. "
                        " You started having fun with others like you never had before. "
                        " You learnt to be yourself. Not closing yourself off anymore. "
                        " Finally letting yourself be free from the chains you put on yourself. "
                        " It's a beautiful song...you didn't think Carmen would be this good. "
                        " Maybe you should listen to his songs more. "
                    else:
                        pass
                    hide carmenneutralb2 at bottom
                    show carmenneutral at center
                    " Carmen eventually stops playing his song, looking at you. "
                    " Looks like he wanted your opinion on it. "
                    " What do you think? "
                    menu:
                        " I love it! ":
                            $ carmenlv += 5
                            hide carmenneutral at bottom
                            show carmenhappy at center
                            ca " ...!!! "
                            " Camren looks happy that you liked it. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Carmen. "
                            " ...You have a feeling he's going to be a popular music artist in the future. "
                            " And you're going to listen to his music if he does. "
                            " You've actually told him about the idea of being a music artist in the future at some point in your conversation... "
                            " Though he just said that he's not really sure about being popular, but he could try. "
                            " Hell yeah. You get free banger songs in the future. "
                            " And also you get perks for being friends with a music artist before his popularity. Epic win. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a moment, stopping your conversation with Carmen. "
                            " The both of you enter the school again and went to the next class...health. "
                            pause 2.0
                            jump wedochealthclass1
                        " I like it ":
                            ca " ...!!! "
                            " Camren looks happy that you liked it. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Carmen. "
                            " ...You have a feeling he's going to be a popular music artist in the future. "
                            " And you're going to listen to his music if he does. "
                            " You've actually told him about the idea of being a music artist in the future at some point in your conversation... "
                            " Though he just said that he's not really sure about being popular, but he could try. "
                            " Hell yeah. You get free banger songs in the future. "
                            " And also you get perks for being friends with a music artist before his popularity. Epic win. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a moment, stopping your conversation with Carmen. "
                            " The both of you enter the school again and went to the next class...health. "
                            pause 2.0
                            jump wedochealthclass1
                " Give him another idea ":
                    $ carmenlv += 5
                    ca " ... "
                    " Carmen looks like he's ready to hear your ideas. "
                    " You think deeply for a moment... "
                    " ...Before giving him one of your ideas. "
                    scene black with dissolve
                    " You spent the rest of the break giving Carmen song ideas. "
                    " There were some that Carmen liked, and there were some that Carmen didn't. "
                    " He did find it funny that you tried to request a silly song at one point. "
                    " Eventually, you ended up with Carmen playing a song based off of friendship. "
                    " It sounded really nice, in your opinion. "
                    " You really needed to listen to his music more... "
                    " ...You have a feeling he's going to be a popular music artist in the future. "
                    " And you're going to listen to his music if he does. "
                    " You've actually told him about the idea of being a music artist in the future at some point in your conversation... "
                    " Though he just said that he's not really sure about being popular, but he could try. "
                    " Hell yeah. You get free banger songs in the future. "
                    " And also you get perks for being friends with a music artist before his popularity. Epic win. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a moment, stopping your conversation with Carmen. "
                    " The both of you enter the school again and went to the next class...health. "
                    pause 2.0
                    jump wedochealthclass1
        else:
            " You walked over to him and noticed that he was just plucking the strings on his guitar... "
            " ...He looked really bored and didn't know what to do. "
            $ carmenknow = True
            " You've heard that this guy's name was Carmen. He doesn't really speak, since he's mute. "
            " It didn't really take him long for him to notice that you were there and looking at him. "
            ca " ...! "
            " He waves at you, and then gestures to his guitar, and then his head. "
            " From what you can undertand...he needed some song ideas. "
            " Then he shrugs, probably meaning that he doesn't have any song ideas right now. "
            hide carmenneutral at bottom
            show carmenhappy at center
            " Maybe you could help in giving him a song idea...wait, what's he doing? "
            " He looks like he has an idea in his eyes. "
            " If he was in a cartoon, he would've had a comically large lightbulb above his head. "
            " Too bad we're on a budget, so we can't really give him that. "
            " Anyway, he starts looking around you - looking at you in different angles, I mean. "
            " He seems to be thinking about something...maybe he's gonna use you as inspiration? "
            " You don't really know what to think about being used as inspiration. "
            hide carmenhappy at bottom
            show carmenneutral at center
            " Before he let himself do anything else, he asks you in sign language if it's okay to make a song based off of you. "
            " And yes, I'm going to make you understand sign language because I say so. "
            " He's being nice and respectful...he's gonna understand if you want to give him another idea. "
            " What do you say? "
            menu:
                " Let him use you as inspiration ":
                    $ carmenlv += 10
                    hide carmenneutral at bottom
                    show carmenhappy at center
                    ca " ...!! "
                    " Carmen seems pleased with your decision. "
                    hide carmenhappy at bottom
                    show carmenneutralb2 at center
                    " He takes one more good look at you before he starts to play a song... "
                    if kind == True:
                        " The song he plays has a nice happy tune to it. "
                        " Feels pretty warm, like you're back at home. "
                        " It honestly makes you feel safe and sound, like everything's going to be okay. "
                        " Like someone's going to help you no matter what... "
                        " ...Even if it hurts them, they're going to help you. "
                        " Someone who will always be there for you, even in your darkest of hours. "
                        " A sweet song, really. "
                    elif calm == True:
                        " The song he plays has a really nice tune to it. "
                        " It makes you feel as if you're at a beach and just relaxing... "
                        " Even through the worst of times, you know that everything's going to be okay in the end. "
                        " Just there relaxing and being calm - even if someone is yelling at you... "
                        " ...You just wont lose your cool and fight with them. "
                        " You know that they're just trying to ragebait you, so you just chillax. "
                        " A real nice tune. You could really use some coconut water to relax with now... "
                        " If you had this in your playlist, you'd be chillaxing everyday. "
                    elif mean == True:
                        " The song he plays has kind of a empty feeling at the start. "
                        " A cold and empty feeling, as if you're not letting yourself open up to anyone at first. "
                        " Pushing others away and telling them that you're basically not worth it... "
                        " That feeling is familiar to you. "
                        " As the song progresses, it gets more lively. "
                        " Like a flower getting ready to bloom, like the sun rising. "
                        " You get more comfortable with those around you. "
                        " And you learn to be comfortable with yourself, too. "
                        " You started having fun with others like you never had before. "
                        " You learnt to be yourself. Not closing yourself off anymore. "
                        " Finally letting yourself be free from the chains you put on yourself. "
                        " It's a beautiful song...you didn't think Carmen would be this good. "
                        " Maybe you should listen to his songs more. "
                    else:
                        pass
                    hide carmenneutralb2 at bottom
                    show carmenneutral at center
                    " Carmen eventually stops playing his song, looking at you. "
                    " Looks like he wanted your opinion on it. "
                    " What do you think? "
                    menu:
                        " I love it! ":
                            $ carmenlv += 5
                            hide carmenneutral at bottom
                            show carmenhappy at center
                            ca " ...!!! "
                            " Camren looks happy that you liked it. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Carmen. "
                            " ...You have a feeling he's going to be a popular music artist in the future. "
                            " And you're going to listen to his music if he does. "
                            " You've actually told him about the idea of being a music artist in the future at some point in your conversation... "
                            " Though he just said that he's not really sure about being popular, but he could try. "
                            " Hell yeah. You get free banger songs in the future. "
                            " And also you get perks for being friends with a music artist before his popularity. Epic win. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a moment, stopping your conversation with Carmen. "
                            " The both of you enter the school again and went to the next class...health. "
                            pause 2.0
                            jump wedochealthclass1
                        " I like it ":
                            ca " ...!!! "
                            " Camren looks happy that you liked it. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Carmen. "
                            " ...You have a feeling he's going to be a popular music artist in the future. "
                            " And you're going to listen to his music if he does. "
                            " You've actually told him about the idea of being a music artist in the future at some point in your conversation... "
                            " Though he just said that he's not really sure about being popular, but he could try. "
                            " Hell yeah. You get free banger songs in the future. "
                            " And also you get perks for being friends with a music artist before his popularity. Epic win. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a moment, stopping your conversation with Carmen. "
                            " The both of you enter the school again and went to the next class...health. "
                            pause 2.0
                            jump wedochealthclass1
                " Give him another idea ":
                    $ carmenlv += 5
                    ca " ... "
                    " Carmen looks like he's ready to hear your ideas. "
                    " You think deeply for a moment... "
                    " ...Before giving him one of your ideas. "
                    scene black with dissolve
                    " You spent the rest of the break giving Carmen song ideas. "
                    " There were some that Carmen liked, and there were some that Carmen didn't. "
                    " He did find it funny that you tried to request a silly song at one point. "
                    " Eventually, you ended up with Carmen playing a song based off of friendship. "
                    " It sounded really nice, in your opinion. "
                    " You really needed to listen to his music more... "
                    " ...You have a feeling he's going to be a popular music artist in the future. "
                    " And you're going to listen to his music if he does. "
                    " You've actually told him about the idea of being a music artist in the future at some point in your conversation... "
                    " Though he just said that he's not really sure about being popular, but he could try. "
                    " Hell yeah. You get free banger songs in the future. "
                    " And also you get perks for being friends with a music artist before his popularity. Epic win. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a moment, stopping your conversation with Carmen. "
                    " The both of you enter the school again and went to the next class...health. "
                    pause 2.0
                    jump wedochealthclass1
    label thinkingaboutchu:
        show yinhuineutral at left with easeinright
        show yangyineutral at right with easeinright
        if yinhuiknow == True and yangyiknow == True:
            yi " ...Oh, it's you. "
            ya " Hiya, [name]! "
            " You greeted the both of them. "
            " You then asked them what they were doing. "
            ya " Just studying for the next class... "
            yi " It's health, by the way. "
            hide yinhuineutral at bottom
            show yinhuisurprised at left
            yi " Wait, hold on. Don't we have an activity in health today? "
            hide yangyineutral at bottom
            show yangyisurprised at right
            ya " Wait, really?? we do?? "
            ya " I don't remember anyone telling me about that... "
            ya " Are you absolutely sure that we have an activity today. "
            hide yinhuisurprised at bottom
            show yinhuiheh at left
            yi " The teacher literally told us that there'd be a test today. "
            yi " Actually, that was yesterday, I think... "
            yi " Even reminded us in the GC. I don't think you checked it. "
            yi " I mean, you WERE fast asleep that night... "
            yi " ...And you were also sleep talking about how much you wanted a bottle of coke. "
            ya " I DIDN'T DO THAT??? "
            ya " [name], don't believe him! "
            yi " What's funnier is that your pronounciation was so horrible... "
            ya " H-heyyyy...let's stop now...!! "
            menu:
                " I would like to listen more ":
                    $ yinhuilv += 10
                    hide yangyisurprised at bottom
                    show yangyisad at right
                    yi " See? [name] wants to hear more. "
                    ya " [name] how could you betray me like this... "
                    yi " Basically, Yangyi over here had a dream about coke, right? "
                    yi " For some weird ass reason, his pronounciation of coke was so horribly wrong. "
                    yi " He pronounced it as COCK!! That's real funny, isn't it? "
                    ya " HEY!! You used to pronounce it like that too! "
                    yi " Alteast I learnt how to ACTUALLY pronounce it. "
                    ya " Come oooooonnn... Why'd you have to tell [them] this... "
                    yi " Because [they] said that [they] wanted to know more, duh. "
                    ya " You're the worst.... "
                    yi " Love you too. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Yinhui and Yangyi. "
                    " You didn't know that someone could mispronounce coke so bad... "
                    " It's so bad that it's funny. "
                    " Their grammar is great, but their pronounciation is absolutely horrendous. "
                    " In a funny way, of course. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and you walked to your classroom. "
                    pause 2.0
                    jump wedochealthclass1
                " Let's spare Yangyi for now ":
                    $ yangyilv += 10
                    hide yangyisurprised at bottom
                    show yangyineutral at right
                    hide yinhuiheh at bottom
                    show yinhuineutral at left
                    yi " Awww, darn. "
                    ya " See? [name] doesn't want to learn about that! "
                    yi " Guess I'll tell [them] another time. "
                    ya " Whaaat? no. "
                    hide yinhuineutral at bottom
                    show yinhuihappy at left
                    yi " I'm gonna tell them a future. "
                    yi " You probably wouldn't know if I told them or not. "
                    hide yangyineutral at bottom
                    show yangyiangry at right
                    ya " Yinhui, if you dareeven tell them about THAT then... "
                    ya " Let's say you're going to end up just like dad. "
                    hide yinhuineutral at bottom
                    show yinhuisurprised at left
                    yi " Oh damn, alright. "
                    hide yangyiangry at bottom
                    show yangyihappy at right
                    ya " Yay! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Yinhui and Yangyi. "
                    " This is honestly the first time you've seen Yangyi mad... "
                    " Pretty insane. Hopefully you don't get on his bad side anytime soon. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and you walked to your classroom. "
                    pause 2.0
                    jump wedochealthclass1
        elif yinhuiknow == True and yangyiknow == False:
            yi " ...Oh, it's you. "
            x " Hiya, [name]! "
            yi " I don't think you've met my brother yet... "
            $ yangyiknow = True
            ya " I'm Yangyi! It's nice to meet you! "
            " You greeted the both of them. "
            " You then asked them what they were doing. "
            ya " Just studying for the next class... "
            yi " It's health, by the way. "
            hide yinhuineutral at bottom
            show yinhuisurprised at left
            yi " Wait, hold on. Don't we have an activity in health today? "
            hide yangyineutral at bottom
            show yangyisurprised at right
            ya " Wait, really?? we do?? "
            ya " I don't remember anyone telling me about that... "
            ya " Are you absolutely sure that we have an activity today. "
            hide yinhuisurprised at bottom
            show yinhuiheh at left
            yi " The teacher literally told us that there'd be a test today. "
            yi " Actually, that was yesterday, I think... "
            yi " Even reminded us in the GC. I don't think you checked it. "
            yi " I mean, you WERE fast asleep that night... "
            yi " ...And you were also sleep talking about how much you wanted a bottle of coke. "
            ya " I DIDN'T DO THAT??? "
            ya " [name], don't believe him! "
            yi " What's funnier is that your pronounciation was so horrible... "
            ya " H-heyyyy...let's stop now...!! "
            menu:
                " I would like to listen more ":
                    $ yinhuilv += 10
                    hide yangyisurprised at bottom
                    show yangyisad at right
                    yi " See? [name] wants to hear more. "
                    ya " [name] how could you betray me like this... "
                    yi " Basically, Yangyi over here had a dream about coke, right? "
                    yi " For some weird ass reason, his pronounciation of coke was so horribly wrong. "
                    yi " He pronounced it as COCK!! That's real funny, isn't it? "
                    ya " HEY!! You used to pronounce it like that too! "
                    yi " Alteast I learnt how to ACTUALLY pronounce it. "
                    ya " Come oooooonnn... Why'd you have to tell [them] this... "
                    yi " Because [they] said that [they] wanted to know more, duh. "
                    ya " You're the worst.... "
                    yi " Love you too. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Yinhui and Yangyi. "
                    " You didn't know that someone could mispronounce coke so bad... "
                    " It's so bad that it's funny. "
                    " Their grammar is great, but their pronounciation is absolutely horrendous. "
                    " In a funny way, of course. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and you walked to your classroom. "
                    pause 2.0
                    jump wedochealthclass1
                " Let's spare Yangyi for now ":
                    $ yangyilv += 10
                    hide yangyisurprised at bottom
                    show yangyineutral at right
                    hide yinhuiheh at bottom
                    show yinhuineutral at left
                    yi " Awww, darn. "
                    ya " See? [name] doesn't want to learn about that! "
                    yi " Guess I'll tell [them] another time. "
                    ya " Whaaat? no. "
                    hide yinhuineutral at bottom
                    show yinhuihappy at left
                    yi " I'm gonna tell them a future. "
                    yi " You probably wouldn't know if I told them or not. "
                    hide yangyineutral at bottom
                    show yangyiangry at right
                    ya " Yinhui, if you dareeven tell them about THAT then... "
                    ya " Let's say you're going to end up just like dad. "
                    hide yinhuineutral at bottom
                    show yinhuisurprised at left
                    yi " Oh damn, alright. "
                    hide yangyiangry at bottom
                    show yangyihappy at right
                    ya " Yay! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Yinhui and Yangyi. "
                    " This is honestly the first time you've seen Yangyi mad... "
                    " Pretty insane. Hopefully you don't get on his bad side anytime soon. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and you walked to your classroom. "
                    pause 2.0
                    jump wedochealthclass1
        elif yinhuiknow == False and yangyiknow == True:
            x " ...Oh, it's you. "
            ya " Hiya, [name]! "
            ya " I don't think you've met my brother yet... "
            $ yinhuiknow = True
            yi " I'm Yinhui. It's nice to meet you, I guess. "
            " You greeted the both of them. "
            " You then asked them what they were doing. "
            ya " Just studying for the next class... "
            yi " It's health, by the way. "
            hide yinhuineutral at bottom
            show yinhuisurprised at left
            yi " Wait, hold on. Don't we have an activity in health today? "
            hide yangyineutral at bottom
            show yangyisurprised at right
            ya " Wait, really?? we do?? "
            ya " I don't remember anyone telling me about that... "
            ya " Are you absolutely sure that we have an activity today. "
            hide yinhuisurprised at bottom
            show yinhuiheh at left
            yi " The teacher literally told us that there'd be a test today. "
            yi " Actually, that was yesterday, I think... "
            yi " Even reminded us in the GC. I don't think you checked it. "
            yi " I mean, you WERE fast asleep that night... "
            yi " ...And you were also sleep talking about how much you wanted a bottle of coke. "
            ya " I DIDN'T DO THAT??? "
            ya " [name], don't believe him! "
            yi " What's funnier is that your pronounciation was so horrible... "
            ya " H-heyyyy...let's stop now...!! "
            menu:
                " I would like to listen more ":
                    $ yinhuilv += 10
                    hide yangyisurprised at bottom
                    show yangyisad at right
                    yi " See? [name] wants to hear more. "
                    ya " [name] how could you betray me like this... "
                    yi " Basically, Yangyi over here had a dream about coke, right? "
                    yi " For some weird ass reason, his pronounciation of coke was so horribly wrong. "
                    yi " He pronounced it as COCK!! That's real funny, isn't it? "
                    ya " HEY!! You used to pronounce it like that too! "
                    yi " Alteast I learnt how to ACTUALLY pronounce it. "
                    ya " Come oooooonnn... Why'd you have to tell [them] this... "
                    yi " Because [they] said that [they] wanted to know more, duh. "
                    ya " You're the worst.... "
                    yi " Love you too. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Yinhui and Yangyi. "
                    " You didn't know that someone could mispronounce coke so bad... "
                    " It's so bad that it's funny. "
                    " Their grammar is great, but their pronounciation is absolutely horrendous. "
                    " In a funny way, of course. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and you walked to your classroom. "
                    pause 2.0
                    jump wedochealthclass1
                " Let's spare Yangyi for now ":
                    $ yangyilv += 10
                    hide yangyisurprised at bottom
                    show yangyineutral at right
                    hide yinhuiheh at bottom
                    show yinhuineutral at left
                    yi " Awww, darn. "
                    ya " See? [name] doesn't want to learn about that! "
                    yi " Guess I'll tell [them] another time. "
                    ya " Whaaat? no. "
                    hide yinhuineutral at bottom
                    show yinhuihappy at left
                    yi " I'm gonna tell them a future. "
                    yi " You probably wouldn't know if I told them or not. "
                    hide yangyineutral at bottom
                    show yangyiangry at right
                    ya " Yinhui, if you dareeven tell them about THAT then... "
                    ya " Let's say you're going to end up just like dad. "
                    hide yinhuineutral at bottom
                    show yinhuisurprised at left
                    yi " Oh damn, alright. "
                    hide yangyiangry at bottom
                    show yangyihappy at right
                    ya " Yay! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Yinhui and Yangyi. "
                    " This is honestly the first time you've seen Yangyi mad... "
                    " Pretty insane. Hopefully you don't get on his bad side anytime soon. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and you walked to your classroom. "
                    pause 2.0
                    jump wedochealthclass1
        else:
            x " ...Oh, it's you. "
            x " Hiya, [name]! "
            $ yangyiknow = True
            $ yinhuiknow = True
            ya " I'm Yangyi! It's nice to meet you! "
            yi " And I'm Yinhui. It's nice to meet you too, I guess. "
            ya " As you can tell, me and Yinhui are twins! "
            yi " We're also the sons of Miss Jiayu. "
            " You greeted the both of them. "
            " You then asked them what they were doing. "
            ya " Just studying for the next class... "
            yi " It's health, by the way. "
            hide yinhuineutral at bottom
            show yinhuisurprised at left
            yi " Wait, hold on. Don't we have an activity in health today? "
            hide yangyineutral at bottom
            show yangyisurprised at right
            ya " Wait, really?? we do?? "
            ya " I don't remember anyone telling me about that... "
            ya " Are you absolutely sure that we have an activity today. "
            hide yinhuisurprised at bottom
            show yinhuiheh at left
            yi " The teacher literally told us that there'd be a test today. "
            yi " Actually, that was yesterday, I think... "
            yi " Even reminded us in the GC. I don't think you checked it. "
            yi " I mean, you WERE fast asleep that night... "
            yi " ...And you were also sleep talking about how much you wanted a bottle of coke. "
            ya " I DIDN'T DO THAT??? "
            ya " [name], don't believe him! "
            yi " What's funnier is that your pronounciation was so horrible... "
            ya " H-heyyyy...let's stop now...!! "
            menu:
                " I would like to listen more ":
                    $ yinhuilv += 10
                    hide yangyisurprised at bottom
                    show yangyisad at right
                    yi " See? [name] wants to hear more. "
                    ya " [name] how could you betray me like this... "
                    yi " Basically, Yangyi over here had a dream about coke, right? "
                    yi " For some weird ass reason, his pronounciation of coke was so horribly wrong. "
                    yi " He pronounced it as COCK!! That's real funny, isn't it? "
                    ya " HEY!! You used to pronounce it like that too! "
                    yi " Alteast I learnt how to ACTUALLY pronounce it. "
                    ya " Come oooooonnn... Why'd you have to tell [them] this... "
                    yi " Because [they] said that [they] wanted to know more, duh. "
                    ya " You're the worst.... "
                    yi " Love you too. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Yinhui and Yangyi. "
                    " You didn't know that someone could mispronounce coke so bad... "
                    " It's so bad that it's funny. "
                    " Their grammar is great, but their pronounciation is absolutely horrendous. "
                    " In a funny way, of course. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and you walked to your classroom. "
                    pause 2.0
                    jump wedochealthclass1
                " Let's spare Yangyi for now ":
                    $ yangyilv += 10
                    hide yangyisurprised at bottom
                    show yangyineutral at right
                    hide yinhuiheh at bottom
                    show yinhuineutral at left
                    yi " Awww, darn. "
                    ya " See? [name] doesn't want to learn about that! "
                    yi " Guess I'll tell [them] another time. "
                    ya " Whaaat? no. "
                    hide yinhuineutral at bottom
                    show yinhuihappy at left
                    yi " I'm gonna tell them a future. "
                    yi " You probably wouldn't know if I told them or not. "
                    hide yangyineutral at bottom
                    show yangyiangry at right
                    ya " Yinhui, if you dareeven tell them about THAT then... "
                    ya " Let's say you're going to end up just like dad. "
                    hide yinhuineutral at bottom
                    show yinhuisurprised at left
                    yi " Oh damn, alright. "
                    hide yangyiangry at bottom
                    show yangyihappy at right
                    ya " Yay! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Yinhui and Yangyi. "
                    " This is honestly the first time you've seen Yangyi mad... "
                    " Pretty insane. Hopefully you don't get on his bad side anytime soon. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and you walked to your classroom. "
                    pause 2.0
                    jump wedochealthclass1

label wedocbackschool1:
    # koa and orchid
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked around the back of the school and spotted two of your classmates hanging out with eachother. "
    " You kinda wanted to know what they were talking about, so you walked over to them and sat down on the ground with them. "
    " Let's see what they're talking about... "
    show koaneutral at left with easeinbottom
    show orchidneutral at right with easeinbottom
    if koaknow == True and orchidknow == True:
        k " I think you need to interact with other people more, Orchid. "
        $ orchidknow = True
        oc " Really, Koa...? But I interact with other people a lot! "
        k " Yes, but not really that much. I've kinda noticed that you're alone most of the time. "
        oc " What? No I'm not...I always have a friend hanging out with me! "
        oc " It's just that they're always coming in late. Trust meee!! "
        k " ...I don't think I can believe that, Orchid. "
        k " Look, I know you mean well, but you've really got to socialize more. "
        hide orchidneutral at bottom
        show orchidsad at right
        oc " I do though... "
        k " I know that you try to interact with others who aren't me, but you've gotta do more. "
        k " Be friends with them and talk with them a lot. "
        k " I'm not saying this because I don't like you hanging out with me, I'm saying this because I want to help you with socializing. "
        k " How about I let you talk with [name] here? "
        oc " Uh, yeah, sure...! "
        k " Great. I'll get going, I have to go on a call with one of my siblings. "
        k " Just need to figure out if they're doing alright while I'm away. "
        k " I'll be near if you need anything, okay? "
        oc " ...Okay... "
        hide koaneutral at left with easeoutleft
        show orchidsad at center with move
        " Orchid doesn't say anything the moment Koa leaves. "
        " All they could do was just look everywhere but at you. "
        " You could practically feel the awkwardness coming out of him. "
        " Maybe you could do something to make them feel better? "
        menu:
            " Start up a conversation ":
                $ orchidlv += 10
                $ koalv += 10
                " You tried to talk, but nothing really came out of your mouth. "
                " You didn't know what to talk about with Orchid. "
                " After all, you didn't really know anything about their interests. "
                " Sure you might've talked with them before, but you wouldn't consider eachother as close. "
                " And if you haven't talked with them yet, then this is the problem. "
                " You can't just go with something basic like... "
                " ...Hey,how's the weather today? Or like complimenting them. "
                " This is awkward. Really awkward. "
                oc " ...So, uh... "
                oc " Hope you're doing alright and all that. "
                oc " ... "
                " God, what was that attempt at conversation? "
                " You could relate though, you didn't really like interacting with others too. "
                " Eventually, after a long period of silence, Orchid speaks up. "
                stop music fadeout 1.5
                play music "audio/emotionalmoment.mp3" fadein 1.5
                oc " ...I'm gonna get real here, [name]. Sorry if it makes you uncomfortable or anything... "
                oc " But I don't really like talking to others because...I don't even know. "
                oc " I try to talk to other people but it just ends up with me not even sharing the same interest with them. "
                oc " Some of their interests are things that I don't like, and it makes me really uncomfortable. "
                oc " That's why I kind of just cling to the people I trust the most... "
                oc " I know that they share the same interests as me, so I feel comfortable with talking with them, of course... "
                oc " And some of the other people in this school kinda scares me because they look like they'd be the type to bully me, in all honesty. "
                oc " I know that if they do, I should just tell the principal, but I'm still too afraid. "
                oc " Don't know why, either. "
                oc " And about clinging to the people I trust the most... "
                oc " I kinda wonder if I'm annoying Koa considering I talk to him a lot. "
                oc " I know he has a lot of other stuff to do, so I'm wondering if I'm annoying him to the point he might not want to talk to me anymore... "
                oc " ...You know what, this is stupid, this is all stupid. "
                oc " I probably just wasted a whole chunk of your time now, didn't I? "
                oc " You should get going instead of paying attention to a distraction like me. "
                menu:
                    " No, it's okay. You can talk to me. ":
                        $ orchidlv += 5
                        $ koalv += 10
                        stop music fadeout 1.5
                        play music "audio/paperhigh.mp3" fadein 1.5
                        hide orchidsad at bottom
                        show orchidsurprised at center
                        oc " ...You want me to talk to you? really? "
                        oc " I don't even think you'd enjoy the things I'd talk about. "
                        oc " But uh, if you insist then... "
                        scene black with dissolve
                        " You spent the rest of the break listening to Orchid rant. "
                        " At the corner of your eye, you could see Koa peeking by... "
                        " Looks like he was monitoring the conversation. "
                        " You could probably tell that he wanted to tell Orchid something about the whole annoying him thing. "
                        " But, he didn't want to interrupt your conversation with them right now. "
                        " For now, you're just going to have to listen to Orchid rant. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit. "
                        " Looks like it's time for your health class... "
                        " You get back into the school and walked back to your classroom. "
                        pause 2.0
                        jump wedochealthclass1
                    " I have to go somewhere ":
                        oc " Yeah, I know you do. "
                        oc " Go have fun, or something. "
                        scene black with dissolve
                        stop music fadeout 1.5
                        play music "audio/paperhigh.mp3" fadein 1.5
                        " You walked away from the back of the school and walked over to the library instead. "
                        " You couldn't really handle the fact that someone you didn't really know too well was venting to you. "
                        " As much as you felt bad for them, you couldn't handle it. "
                        " You weren't really that good of a comforter anyway. "
                        " You could understand why they were scared of interacting with other people though... "
                        " The fear of looking weird towards others just for having different interests with them. "
                        " The fear of being made fun of...all of that. "
                        " You've felt that at some point in your life too. "
                        " But you don't know how to comfort someone with that situation too. "
                        " You spent the rest of the break time reading books in the library. "
                        " Just random books that you think that's interesting. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your health class. "
                        " You return the book you took and you walked to your classroom for your next class. "
                        pause 2.0
                        jump wedochealthclass1
            " Make an excuse to go somewhere else ":
                oc " Uhhh...you gotta go? "
                oc " Sure, sure! Go have fun or something... "
                oc " If you need anything, I'm right here! "
                scene black with dissolve
                " You walked back into the school. You couldn't really find anything to talk about to him. "
                " It was way too awkward, and you didn't just want to stare at them for so long. "
                " You ended up at the library so that youcould relax for a bit. "
                " You spent the rest of the break time reading books in the library. "
                " Just random books that you think that's interesting. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your health class. "
                " You return the book you took and you walked to your classroom for your next class. "
                pause 2.0
                jump wedochealthclass1
    elif koaknow == True and orchidknow == False:
        k " I think you need to interact with other people more, Orchid. "
        oc " Really, Koa...? But I interact with other people a lot! "
        k " Yes, but not really that much. I've kinda noticed that you're alone most of the time. "
        oc " What? No I'm not...I always have a friend hanging out with me! "
        oc " It's just that they're always coming in late. Trust meee!! "
        k " ...I don't think I can believe that, Orchid. "
        k " Look, I know you mean well, but you've really got to socialize more. "
        hide orchidneutral at bottom
        show orchidsad at right
        oc " I do though... "
        k " I know that you try to interact with others who aren't me, but you've gotta do more. "
        k " Be friends with them and talk with them a lot. "
        k " I'm not saying this because I don't like you hanging out with me, I'm saying this because I want to help you with socializing. "
        k " How about I let you talk with [name] here? "
        oc " Uh, yeah, sure...! "
        k " Great. I'll get going, I have to go on a call with one of my siblings. "
        k " Just need to figure out if they're doing alright while I'm away. "
        k " I'll be near if you need anything, okay? "
        oc " ...Okay... "
        hide koaneutral at left with easeoutleft
        show orchidsad at center with move
        " Orchid doesn't say anything the moment Koa leaves. "
        " All they could do was just look everywhere but at you. "
        " You could practically feel the awkwardness coming out of him. "
        " Maybe you could do something to make them feel better? "
        menu:
            " Start up a conversation ":
                $ orchidlv += 10
                $ koalv += 10
                " You tried to talk, but nothing really came out of your mouth. "
                " You didn't know what to talk about with Orchid. "
                " After all, you didn't really know anything about their interests. "
                " Sure you might've talked with them before, but you wouldn't consider eachother as close. "
                " And if you haven't talked with them yet, then this is the problem. "
                " You can't just go with something basic like... "
                " ...Hey,how's the weather today? Or like complimenting them. "
                " This is awkward. Really awkward. "
                oc " ...So, uh... "
                oc " Hope you're doing alright and all that. "
                oc " ... "
                " God, what was that attempt at conversation? "
                " You could relate though, you didn't really like interacting with others too. "
                " Eventually, after a long period of silence, Orchid speaks up. "
                oc " Hey, uh. I gotta go. "
                oc " See you. "
                hide orchidneutral at right with easeoutright
                " Before you could say anything, they already left. "
                " You looked around for any sight of Koa, but Koa was away too. "
                " Wonder where they went... "
                scene black with dissolve
                " You went back into the school after what happened. "
                " You didn't really know what else to do, so you just went to the library to hang out there for a bit. "
                " You spent the rest of the break time reading books in the library. "
                " Just random books that you think that's interesting. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your health class. "
                " You return the book you took and you walked to your classroom for your next class. "
                pause 2.0
                jump wedochealthclass1
            " Make an excuse to go somewhere else ":
                oc " Uhhh...you gotta go? "
                oc " Sure, sure! Go have fun or something... "
                oc " If you need anything, I'm right here! "
                scene black with dissolve
                " You walked back into the school. You couldn't really find anything to talk about to him. "
                " It was way too awkward, and you didn't just want to stare at them for so long. "
                " You ended up at the library so that you could relax for a bit. "
                " You spent the rest of the break time reading books in the library. "
                " Just random books that you think that's interesting. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your health class. "
                " You return the book you took and you walked to your classroom for your next class. "
                pause 2.0
                jump wedochealthclass1
    elif koaknow == False and orchidknow == True:
        x " I think you need to interact with other people more, Orchid. "
        oc " Really, Koa...? But I interact with other people a lot! "
        $ koaknow = True
        k " Yes, but not really that much. I've kinda noticed that you're alone most of the time. "
        oc " What? No I'm not...I always have a friend hanging out with me! "
        oc " It's just that they're always coming in late. Trust meee!! "
        k " ...I don't think I can believe that, Orchid. "
        k " Look, I know you mean well, but you've really got to socialize more. "
        hide orchidneutral at bottom
        show orchidsad at right
        oc " I do though... "
        k " I know that you try to interact with others who aren't me, but you've gotta do more. "
        k " Be friends with them and talk with them a lot. "
        k " I'm not saying this because I don't like you hanging out with me, I'm saying this because I want to help you with socializing. "
        k " How about I let you talk with [name] here? "
        oc " Uh, yeah, sure...! "
        k " Great. I'll get going, I have to go on a call with one of my siblings. "
        k " Just need to figure out if they're doing alright while I'm away. "
        k " I'll be near if you need anything, okay? "
        oc " ...Okay... "
        hide koaneutral at left with easeoutleft
        show orchidsad at center with move
        " Orchid doesn't say anything the moment Koa leaves. "
        " All they could do was just look everywhere but at you. "
        " You could practically feel the awkwardness coming out of him. "
        " Maybe you could do something to make them feel better? "
        menu:
            " Start up a conversation ":
                $ orchidlv += 10
                $ koalv += 10
                " You tried to talk, but nothing really came out of your mouth. "
                " You didn't know what to talk about with Orchid. "
                " After all, you didn't really know anything about their interests. "
                " Sure you might've talked with them before, but you wouldn't consider eachother as close. "
                " And if you haven't talked with them yet, then this is the problem. "
                " You can't just go with something basic like... "
                " ...Hey,how's the weather today? Or like complimenting them. "
                " This is awkward. Really awkward. "
                oc " ...So, uh... "
                oc " Hope you're doing alright and all that. "
                oc " ... "
                " God, what was that attempt at conversation? "
                " You could relate though, you didn't really like interacting with others too. "
                " Eventually, after a long period of silence, Orchid speaks up. "
                stop music fadeout 1.5
                play music "audio/emotionalmoment.mp3" fadein 1.5
                oc " ...I'm gonna get real here, [name]. Sorry if it makes you uncomfortable or anything... "
                oc " But I don't really like talking to others because...I don't even know. "
                oc " I try to talk to other people but it just ends up with me not even sharing the same interest with them. "
                oc " Some of their interests are things that I don't like, and it makes me really uncomfortable. "
                oc " That's why I kind of just cling to the people I trust the most... "
                oc " I know that they share the same interests as me, so I feel comfortable with talking with them, of course... "
                oc " And some of the other people in this school kinda scares me because they look like they'd be the type to bully me, in all honesty. "
                oc " I know that if they do, I should just tell the principal, but I'm still too afraid. "
                oc " Don't know why, either. "
                oc " And about clinging to the people I trust the most... "
                oc " I kinda wonder if I'm annoying Koa considering I talk to him a lot. "
                oc " I know he has a lot of other stuff to do, so I'm wondering if I'm annoying him to the point he might not want to talk to me anymore... "
                oc " ...You know what, this is stupid, this is all stupid. "
                oc " I probably just wasted a whole chunk of your time now, didn't I? "
                oc " You should get going instead of paying attention to a distraction like me. "
                menu:
                    " No, it's okay. You can talk to me. ":
                        $ orchidlv += 5
                        $ koalv += 10
                        stop music fadeout 1.5
                        play music "audio/paperhigh.mp3" fadein 1.5
                        hide orchidsad at bottom
                        show orchidsurprised at center
                        oc " ...You want me to talk to you? really? "
                        oc " I don't even think you'd enjoy the things I'd talk about. "
                        oc " But uh, if you insist then... "
                        scene black with dissolve
                        " You spent the rest of the break listening to Orchid rant. "
                        " At the corner of your eye, you could see Koa peeking by... "
                        " Looks like he was monitoring the conversation. "
                        " You could probably tell that he wanted to tell Orchid something about the whole annoying him thing. "
                        " But, he didn't want to interrupt your conversation with them right now. "
                        " For now, you're just going to have to listen to Orchid rant. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit. "
                        " Looks like it's time for your health class... "
                        " You get back into the school and walked back to your classroom. "
                        pause 2.0
                        jump wedochealthclass1
                    " I have to go somewhere ":
                        oc " Yeah, I know you do. "
                        oc " Go have fun, or something. "
                        scene black with dissolve
                        stop music fadeout 1.5
                        play music "audio/paperhigh.mp3" fadein 1.5
                        " You walked away from the back of the school and walked over to the library instead. "
                        " You couldn't really handle the fact that someone you didn't really know too well was venting to you. "
                        " As much as you felt bad for them, you couldn't handle it. "
                        " You weren't really that good of a comforter anyway. "
                        " You could understand why they were scared of interacting with other people though... "
                        " The fear of looking weird towards others just for having different interests with them. "
                        " The fear of being made fun of...all of that. "
                        " You've felt that at some point in your life too. "
                        " But you don't know how to comfort someone with that situation too. "
                        " You spent the rest of the break time reading books in the library. "
                        " Just random books that you think that's interesting. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your health class. "
                        " You return the book you took and you walked to your classroom for your next class. "
                        pause 2.0
                        jump wedochealthclass1
            " Make an excuse to go somewhere else ":
                oc " Uhhh...you gotta go? "
                oc " Sure, sure! Go have fun or something... "
                oc " If you need anything, I'm right here! "
                scene black with dissolve
                " You walked back into the school. You couldn't really find anything to talk about to him. "
                " It was way too awkward, and you didn't just want to stare at them for so long. "
                " You ended up at the library so that youcould relax for a bit. "
                " You spent the rest of the break time reading books in the library. "
                " Just random books that you think that's interesting. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your health class. "
                " You return the book you took and you walked to your classroom for your next class. "
                pause 2.0
                jump wedochealthclass1
    else:
        x " I think you need to interact with other people more, Orchid. "
        $ orchidknow = True
        oc " Really, Koa...? But I interact with other people a lot! "
        $ koaknow = True
        k " Yes, but not really that much. I've kinda noticed that you're alone most of the time. "
        oc " What? No I'm not...I always have a friend hanging out with me! "
        oc " It's just that they're always coming in late. Trust meee!! "
        k " ...I don't think I can believe that, Orchid. "
        k " Look, I know you mean well, but you've really got to socialize more. "
        hide orchidneutral at bottom
        show orchidsad at right
        oc " I do though... "
        k " I know that you try to interact with others who aren't me, but you've gotta do more. "
        k " Be friends with them and talk with them a lot. "
        k " I'm not saying this because I don't like you hanging out with me, I'm saying this because I want to help you with socializing. "
        k " How about I let you talk with [name] here? "
        oc " Uh, yeah, sure...! "
        k " Great. I'll get going, I have to go on a call with one of my siblings. "
        k " Just need to figure out if they're doing alright while I'm away. "
        k " I'll be near if you need anything, okay? "
        oc " ...Okay... "
        hide koaneutral at left with easeoutleft
        show orchidsad at center with move
        " Orchid doesn't say anything the moment Koa leaves. "
        " All they could do was just look everywhere but at you. "
        " You could practically feel the awkwardness coming out of him. "
        " Maybe you could do something to make them feel better? "
        menu:
            " Start up a conversation ":
                $ orchidlv += 10
                $ koalv += 10
                " You tried to talk, but nothing really came out of your mouth. "
                " You didn't know what to talk about with Orchid. "
                " After all, you didn't really know anything about their interests. "
                " Sure you might've talked with them before, but you wouldn't consider eachother as close. "
                " And if you haven't talked with them yet, then this is the problem. "
                " You can't just go with something basic like... "
                " ...Hey,how's the weather today? Or like complimenting them. "
                " This is awkward. Really awkward. "
                oc " ...So, uh... "
                oc " Hope you're doing alright and all that. "
                oc " ... "
                " God, what was that attempt at conversation? "
                " You could relate though, you didn't really like interacting with others too. "
                " Eventually, after a long period of silence, Orchid speaks up. "
                oc " Hey, uh. I gotta go. "
                oc " See you. "
                hide orchidneutral at right with easeoutright
                " Before you could say anything, they already left. "
                " You looked around for any sight of Koa, but Koa was away too. "
                " Wonder where they went... "
                scene black with dissolve
                " You went back into the school after what happened. "
                " You didn't really know what else to do, so you just went to the library to hang out there for a bit. "
                " You spent the rest of the break time reading books in the library. "
                " Just random books that you think that's interesting. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your health class. "
                " You return the book you took and you walked to your classroom for your next class. "
                pause 2.0
                jump wedochealthclass1
            " Make an excuse to go somewhere else ":
                oc " Uhhh...you gotta go? "
                oc " Sure, sure! Go have fun or something... "
                oc " If you need anything, I'm right here! "
                scene black with dissolve
                " You walked back into the school. You couldn't really find anything to talk about to him. "
                " It was way too awkward, and you didn't just want to stare at them for so long. "
                " You ended up at the library so that you could relax for a bit. "
                " You spent the rest of the break time reading books in the library. "
                " Just random books that you think that's interesting. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your health class. "
                " You return the book you took and you walked to your classroom for your next class. "
                pause 2.0
                jump wedochealthclass1

label wedocgym1:
    # jam and mia
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym and spotted two of your classmates talking with eachother. "
    " Wondering what they were talking about, you walked up to them to join their conversation. "
    show jamneutral at right with easeinleft
    show mianeutral at left with easeinleft
    if jamknow == True and miaknow == True:
        ja " Uh, you're saying that I should give her flowers or something? "
        m " Yes! If you like her that much, then you should just give her flowers! "
        hide jamneutral at bottom
        show jamsad at right
        ja " Woah, hey...don't say that so loud, someone might hear... "
        m " Oh, come on! We're talking about someone you like, there's no problem with that! "
        m " The only thing that's gonna be concerning is if that certain person you like is listening on us right now. "
        hide jamsad at bottom
        show jamneutral at right
        ja " Well...there's [name], but that's not the person I like. Hi [name]. "
        m " Hiya, [name]! We're just deciding on what to do for Jam! "
        m " Jam's deciding on what gift she should get for Matte - I mean her crush! "
        ja " ...You just said who my crush was, idiot. "
        m " I promise I didn't mean to say that! "
        m " But, yeah...we're thinking of flowers so far! "
        m " Giving someone flowers is a classic way to show someone that you care and love for them... "
        m " ...The most common flower being given to people are roses! "
        m " Due to them being seen as romantic and all. But Jam over here wants to be a little bit more subtle... "
        ja " I want to give her flowers that AREN'T roses. "
        ja " If I do, I think that's just going to give myself away to her. "
        ja " Considering the fact that she knows that roses have a romantic meaning to them in gift giving... "
        m " Then we can go for something more unknown! "
        m " I have plenty of flowers back at my home that you could get for Matte! "
        m " Like...plently plenty! My family likes to garden a whole lot! "
        m " And that means we have a lot of flowers that also have a romantic meaning to them, like for example... "
        m " You could get her red tulips! We have a lot of those there.... "
        m " Red tulips symbolize passion and perfect love, you know! That's a perfect pick! "
        m " Or if you're not into that, then you could get some peonies, which represent prosperity and good fortune... "
        m " OR, you could get her some lavenders because they represent love, devotion, and serenity! "
        m " OOOOR..!! "
        scene black with dissolve
        " You spent the rest of the break talking with Mia and Jam. "
        " More like listening to Mia talk about the options Mia has for Jam. "
        " And damn, Mia had a lot of suggestions for Jam. "
        " I mean...you did hear that Mia liked flowers a lot. But not this much. "
        " Maybe you should go ahead and eat some of her flowers... "
        " Wonder how they would taste like. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your health class. "
        " You walked back to your classroom for your next class. "
        pause 2.0
        jump wedochealthclass1
    elif jamknow == True and miaknow == False:
        ja " Uh, you're saying that I should give her flowers or something? "
        x " Yes! If you like her that much, then you should just give her flowers! "
        hide jamneutral at bottom
        show jamsad at right
        ja " Woah, hey...don't say that so loud, someone might hear... "
        x " Oh, come on! We're talking about someone you like, there's no problem with that! "
        x " The only thing that's gonna be concerning is if that certain person you like is listening on us right now. "
        hide jamsad at bottom
        show jamneutral at right
        ja " Well...there's [name], but that's not the person I like. Hi [name]. "
        x " Hiya, [name]! We're just deciding on what to do for Jam! "
        $ miaknow = True
        m " I'm Mia by the way, ehhe. Nice to meet you. "
        m " Jam's deciding on what gift she should get for Matte - I mean her crush! "
        ja " ...You just said who my crush was, idiot. "
        m " I promise I didn't mean to say that! "
        m " But, yeah...we're thinking of flowers so far! "
        m " Giving someone flowers is a classic way to show someone that you care and love for them... "
        m " ...The most common flower being given to people are roses! "
        m " Due to them being seen as romantic and all. But Jam over here wants to be a little bit more subtle... "
        ja " I want to give her flowers that AREN'T roses. "
        ja " If I do, I think that's just going to give myself away to her. "
        ja " Considering the fact that she knows that roses have a romantic meaning to them in gift giving... "
        m " Then we can go for something more unknown! "
        m " I have plenty of flowers back at my home that you could get for Matte! "
        m " Like...plently plenty! My family likes to garden a whole lot! "
        m " And that means we have a lot of flowers that also have a romantic meaning to them, like for example... "
        m " You could get her red tulips! We have a lot of those there.... "
        m " Red tulips symbolize passion and perfect love, you know! That's a perfect pick! "
        m " Or if you're not into that, then you could get some peonies, which represent prosperity and good fortune... "
        m " OR, you could get her some lavenders because they represent love, devotion, and serenity! "
        m " OOOOR..!! "
        scene black with dissolve
        " You spent the rest of the break talking with Mia and Jam. "
        " More like listening to Mia talk about the options Mia has for Jam. "
        " And damn, Mia had a lot of suggestions for Jam. "
        " I mean...you did hear that Mia liked flowers a lot. But not this much. "
        " Maybe you should go ahead and eat some of her flowers... "
        " Wonder how they would taste like. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your health class. "
        " You walked back to your classroom for your next class. "
        pause 2.0
        jump wedochealthclass1
    elif jamknow == False and miaknow == True:
        x " Uh, you're saying that I should give her flowers or something? "
        m " Yes! If you like her that much, then you should just give her flowers! "
        hide jamneutral at bottom
        show jamsad at right
        x " Woah, hey...don't say that so loud, someone might hear... "
        m " Oh, come on! We're talking about someone you like, there's no problem with that! "
        m " The only thing that's gonna be concerning is if that certain person you like is listening on us right now. "
        hide jamsad at bottom
        show jamneutral at right
        x " Well...there's [name], but that's not the person I like. Hi [name]. "
        $ jamknow = True
        m " Hiya, [name]! We're just deciding on what to do for Jam! "
        m " Jam's deciding on what gift she should get for Matte - I mean her crush! "
        ja " ...You just said who my crush was, idiot. "
        m " I promise I didn't mean to say that! "
        m " But, yeah...we're thinking of flowers so far! "
        m " Giving someone flowers is a classic way to show someone that you care and love for them... "
        m " ...The most common flower being given to people are roses! "
        m " Due to them being seen as romantic and all. But Jam over here wants to be a little bit more subtle... "
        ja " I want to give her flowers that AREN'T roses. "
        ja " If I do, I think that's just going to give myself away to her. "
        ja " Considering the fact that she knows that roses have a romantic meaning to them in gift giving... "
        m " Then we can go for something more unknown! "
        m " I have plenty of flowers back at my home that you could get for Matte! "
        m " Like...plently plenty! My family likes to garden a whole lot! "
        m " And that means we have a lot of flowers that also have a romantic meaning to them, like for example... "
        m " You could get her red tulips! We have a lot of those there.... "
        m " Red tulips symbolize passion and perfect love, you know! That's a perfect pick! "
        m " Or if you're not into that, then you could get some peonies, which represent prosperity and good fortune... "
        m " OR, you could get her some lavenders because they represent love, devotion, and serenity! "
        m " OOOOR..!! "
        scene black with dissolve
        " You spent the rest of the break talking with Mia and Jam. "
        " More like listening to Mia talk about the options Mia has for Jam. "
        " And damn, Mia had a lot of suggestions for Jam. "
        " I mean...you did hear that Mia liked flowers a lot. But not this much. "
        " Maybe you should go ahead and eat some of her flowers... "
        " Wonder how they would taste like. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your health class. "
        " You walked back to your classroom for your next class. "
        pause 2.0
        jump wedochealthclass1
    else:
        x " Uh, you're saying that I should give her flowers or something? "
        x " Yes! If you like her that much, then you should just give her flowers! "
        hide jamneutral at bottom
        show jamsad at right
        x " Woah, hey...don't say that so loud, someone might hear... "
        x " Oh, come on! We're talking about someone you like, there's no problem with that! "
        x " The only thing that's gonna be concerning is if that certain person you like is listening on us right now. "
        hide jamsad at bottom
        show jamneutral at right
        x " Well...there's [name], but that's not the person I like. Hi [name]. "
        x " Hiya, [name]! We're just deciding on what to do for Jam! "
        $ jamknow = True
        $ miaknow = True
        m " I'm Mia by the way, ehhe. Nice to meet you. "
        m " Jam's deciding on what gift she should get for Matte - I mean her crush! "
        ja " ...You just said who my crush was, idiot. "
        m " I promise I didn't mean to say that! "
        m " But, yeah...we're thinking of flowers so far! "
        m " Giving someone flowers is a classic way to show someone that you care and love for them... "
        m " ...The most common flower being given to people are roses! "
        m " Due to them being seen as romantic and all. But Jam over here wants to be a little bit more subtle... "
        ja " I want to give her flowers that AREN'T roses. "
        ja " If I do, I think that's just going to give myself away to her. "
        ja " Considering the fact that she knows that roses have a romantic meaning to them in gift giving... "
        m " Then we can go for something more unknown! "
        m " I have plenty of flowers back at my home that you could get for Matte! "
        m " Like...plently plenty! My family likes to garden a whole lot! "
        m " And that means we have a lot of flowers that also have a romantic meaning to them, like for example... "
        m " You could get her red tulips! We have a lot of those there.... "
        m " Red tulips symbolize passion and perfect love, you know! That's a perfect pick! "
        m " Or if you're not into that, then you could get some peonies, which represent prosperity and good fortune... "
        m " OR, you could get her some lavenders because they represent love, devotion, and serenity! "
        m " OOOOR..!! "
        scene black with dissolve
        " You spent the rest of the break talking with Mia and Jam. "
        " More like listening to Mia talk about the options Mia has for Jam. "
        " And damn, Mia had a lot of suggestions for Jam. "
        " I mean...you did hear that Mia liked flowers a lot. But not this much. "
        " Maybe you should go ahead and eat some of her flowers... "
        " Wonder how they would taste like. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your health class. "
        " You walked back to your classroom for your next class. "
        pause 2.0
        jump wedochealthclass1

label wedoccafeteria1:
    # disk and spark
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted two of your classmates talking with eachother about something. "
    " You wanted to know what exactly that something was, so of course you sat down next to them on one of the tables. "
    " Let's see if they've got some juicy drama for you or not. "
    show diskneutral at left with easeinright
    show sparkneutral at right with easeinright
    if diskknow == True and sparkknow == True:
        d " Hiya there, [name]! "
        sp " Hey. Nice to see you here. "
        d " Me and Spark were just talking about the people we've met at the other schools we've been to! "
        sp " ...Like that one guy I've met... "
        d " Ooooh, and Abbie! Abbieeee!...he was just so adorable... "
        d " Waiit, you talking about Edward from that school? "
        d " Dude, he was so mean to me! How come he wasn't mean to you? "
        sp " I don't know. "
        sp " I mean, he DID pick on me at first, but... "
        sp " The more I talked to him, the less he made fun of me. "
        sp " Still called me a nerd here and there but.. "
        sp " ...I don't know, he picked on me less compared to others? "
        sp " I don't know why he thought I was so special. "
        sp " I'm literally just a random nobody that decided to show up one day. "
        d " Mmm..I think it's because of your good looks! "
        hide sparkneutral at bottom
        show sparkshit at right
        sp " ...Okay, now you're just saying nonsense. "
        hide diskneutral at bottom
        show diskhappy at left
        d " I mean it! You look pretty handsome, in my opinion... "
        d " Who would say no to such a pretty face like you? "
        sp " Wh...okay, you're clearly not seeing yourself right now. "
        sp " Look at a mirror. You're way better than me. "
        d " Nuh uh! "
        sp " Yuh huh. "
        d " Nuh uh! "
        sp " YUH HUH. "
        d " NUH UH!! " with vpunch
        scene black with dissolve
        " You spent the rest of the break watching Spark and Disk say nuh uh and yuh uh to eachother. "
        " Disk eventually fooled Spark and made him say that he himself is beautiful. "
        " Spark cringed very hard when he realized what he had just said about himself. "
        " Disk looked very proud...you also couldn't lie, but Disk is right about Spark. "
        " Very pretty boy in your opinion. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Looks like it's time for your health class. "
        " You got up from where you were seated, and you walked back to your classroom for your next class. "
        pause 2.0
        jump wedochealthclass1
    elif diskknow == True and sparkknow == False:
        d " Hiya there, [name]! "
        x " Hey. Nice to see you here. "
        $ sparkknow = True
        d " Me and Spark were just talking about the people we've met at the other schools we've been to! "
        sp " ...Like that one guy I've met... "
        d " Ooooh, and Abbie! Abbieeee!...he was just so adorable... "
        d " Waiit, you talking about Edward from that school? "
        d " Dude, he was so mean to me! How come he wasn't mean to you? "
        sp " I don't know. "
        sp " I mean, he DID pick on me at first, but... "
        sp " The more I talked to him, the less he made fun of me. "
        sp " Still called me a nerd here and there but.. "
        sp " ...I don't know, he picked on me less compared to others? "
        sp " I don't know why he thought I was so special. "
        sp " I'm literally just a random nobody that decided to show up one day. "
        d " Mmm..I think it's because of your good looks! "
        hide sparkneutral at bottom
        show sparkshit at right
        sp " ...Okay, now you're just saying nonsense. "
        hide diskneutral at bottom
        show diskhappy at left
        d " I mean it! You look pretty handsome, in my opinion... "
        d " Who would say no to such a pretty face like you? "
        sp " Wh...okay, you're clearly not seeing yourself right now. "
        sp " Look at a mirror. You're way better than me. "
        d " Nuh uh! "
        sp " Yuh huh. "
        d " Nuh uh! "
        sp " YUH HUH. "
        d " NUH UH!! " with vpunch
        scene black with dissolve
        " You spent the rest of the break watching Spark and Disk say nuh uh and yuh uh to eachother. "
        " Disk eventually fooled Spark and made him say that he himself is beautiful. "
        " Spark cringed very hard when he realized what he had just said about himself. "
        " Disk looked very proud...you also couldn't lie, but Disk is right about Spark. "
        " Very pretty boy in your opinion. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Looks like it's time for your health class. "
        " You got up from where you were seated, and you walked back to your classroom for your next class. "
        pause 2.0
        jump wedochealthclass1
    elif diskknow == False and sparkknow == True:
        x " Hiya there, [name]! "
        sp " Hey. Nice to see you here. "
        $ diskknow = True
        d " Oh, uh...I'm Disk by the way! Almost forgot to introduce myself, hehe... "
        d " Me and Spark were just talking about the people we've met at the other schools we've been to! "
        sp " ...Like that one guy I've met... "
        d " Ooooh, and Abbie! Abbieeee!...he was just so adorable... "
        d " Waiit, you talking about Edward from that school? "
        d " Dude, he was so mean to me! How come he wasn't mean to you? "
        sp " I don't know. "
        sp " I mean, he DID pick on me at first, but... "
        sp " The more I talked to him, the less he made fun of me. "
        sp " Still called me a nerd here and there but.. "
        sp " ...I don't know, he picked on me less compared to others? "
        sp " I don't know why he thought I was so special. "
        sp " I'm literally just a random nobody that decided to show up one day. "
        d " Mmm..I think it's because of your good looks! "
        hide sparkneutral at bottom
        show sparkshit at right
        sp " ...Okay, now you're just saying nonsense. "
        hide diskneutral at bottom
        show diskhappy at left
        d " I mean it! You look pretty handsome, in my opinion... "
        d " Who would say no to such a pretty face like you? "
        sp " Wh...okay, you're clearly not seeing yourself right now. "
        sp " Look at a mirror. You're way better than me. "
        d " Nuh uh! "
        sp " Yuh huh. "
        d " Nuh uh! "
        sp " YUH HUH. "
        d " NUH UH!! " with vpunch
        scene black with dissolve
        " You spent the rest of the break watching Spark and Disk say nuh uh and yuh uh to eachother. "
        " Disk eventually fooled Spark and made him say that he himself is beautiful. "
        " Spark cringed very hard when he realized what he had just said about himself. "
        " Disk looked very proud...you also couldn't lie, but Disk is right about Spark. "
        " Very pretty boy in your opinion. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Looks like it's time for your health class. "
        " You got up from where you were seated, and you walked back to your classroom for your next class. "
        pause 2.0
        jump wedochealthclass1
    else:
        x " Hiya there, [name]! "
        x " Hey. Nice to see you here. "
        $ diskknow = True
        d " Oh, uh...I'm Disk by the way! Almost forgot to introduce myself, hehe... "
        $ sparkknow = True
        d " Me and Spark were just talking about the people we've met at the other schools we've been to! "
        sp " ...Like that one guy I've met... "
        d " Ooooh, and Abbie! Abbieeee!...he was just so adorable... "
        d " Waiit, you talking about Edward from that school? "
        d " Dude, he was so mean to me! How come he wasn't mean to you? "
        sp " I don't know. "
        sp " I mean, he DID pick on me at first, but... "
        sp " The more I talked to him, the less he made fun of me. "
        sp " Still called me a nerd here and there but.. "
        sp " ...I don't know, he picked on me less compared to others? "
        sp " I don't know why he thought I was so special. "
        sp " I'm literally just a random nobody that decided to show up one day. "
        d " Mmm..I think it's because of your good looks! "
        hide sparkneutral at bottom
        show sparkshit at right
        sp " ...Okay, now you're just saying nonsense. "
        hide diskneutral at bottom
        show diskhappy at left
        d " I mean it! You look pretty handsome, in my opinion... "
        d " Who would say no to such a pretty face like you? "
        sp " Wh...okay, you're clearly not seeing yourself right now. "
        sp " Look at a mirror. You're way better than me. "
        d " Nuh uh! "
        sp " Yuh huh. "
        d " Nuh uh! "
        sp " YUH HUH. "
        d " NUH UH!! " with vpunch
        scene black with dissolve
        " You spent the rest of the break watching Spark and Disk say nuh uh and yuh uh to eachother. "
        " Disk eventually fooled Spark and made him say that he himself is beautiful. "
        " Spark cringed very hard when he realized what he had just said about himself. "
        " Disk looked very proud...you also couldn't lie, but Disk is right about Spark. "
        " Very pretty boy in your opinion. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Looks like it's time for your health class. "
        " You got up from where you were seated, and you walked back to your classroom for your next class. "
        pause 2.0
        jump wedochealthclass1

label wedocrooftop1:
    # jacob and matte
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked up onto the rooftop and spotted two of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if jacobknow == True and matteknow == True:
        menu:
            " {image=jacobicon} Jacob {image=jacobicon} ":
                jump hostagetx2
            " {image=matteicon} Matte {image=matteicon} ":
                jump glitterlexycat
    elif jacobknow == True and matteknow == False:
        menu:
            " {image=jacobicon} Jacob {image=jacobicon} ":
                jump hostagetx2
            " {image=matteicon} A girl struggling to paint {image=matteicon} ":
                jump glitterlexycat
    elif jacobknow == False and matteknow == True:
        menu:
            " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                jump hostagetx2
            " {image=matteicon} Matte {image=matteicon} ":
                jump glitterlexycat
    else:
        menu:
            " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                jump hostagetx2
            " {image=matteicon} A girl struggling to paint {image=matteicon} ":
                jump glitterlexycat
    label hostagetx2:
        show jacobneutral at center with easeinright
        if jacobknow == True:
            jac " God damn it... "
            " He seems to be pretty frustrated over something. "
            " You asked him if he was alright or not. "
            jac " Does it look like I'm doing alright right now? "
            jac " Of course I'm not. "
            jac " I'm not sure if you were there or not, but someone decided to throw away my goggles and my bandana. "
            jac " At the very start of the day, too... "
            jac " Luckily, no one was looking while my face was showing... "
            jac " ...It still pisses me off that someone decided to do that to me though! "
            jac " I couldn't get to see who took it off, probably some ugly bastard... "
            jac " ...I can't be the one to talk though, I'm definitely uglier than them without my goggles and bandana. "
            jac " God damn it... "
            menu:
                " I think you look pretty cool, with or without the bandana ":
                    $ jacoblv += 10
                    jac " Really? you think so? "
                    jac " I find that really hard to believe. "
                    jac " You haven't even seen me without the bandana and everything. "
                    jac " You don't really know what you're saying, aren't you? "
                    jac " ...Thanks for the compliment, though. "
                    jac " I know that you're just trying to make me feel better. "
                    jac " Can't really be mad at you or anything... "
                    if jacoblv >= 20 or jacoblv == 20:
                        jac " Why do you hang out with me so much? "
                        jac " Normally people would start running away from me if I talked to them too much. "
                        jac " ...You're an odd one. You're hard to understand. "
                        jac " ...But I guess...your company is nice. "
                        jac " You can hang out with me more if you want. "
                        jac " No one has really decided to hang out with me for this long... "
                        scene black with dissolve
                        " Jacob says nothing afterwards. "
                        " You enjoy the silence as you felt the fresh air around you... "
                        " ...You and Jacob enjoy the view for a bit. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your health class. "
                        " You walked down from the rooftop and went to your classroom for your next class. "
                        pause 2.0
                        jump wedochealthclass1
                    else:
                        scene black with dissolve
                        " Jacob says nothing afterwards. "
                        " You enjoy the silence as you felt the fresh air around you... "
                        " ...You and Jacob enjoy the view for a bit. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your health class. "
                        " You walked down from the rooftop and went to your classroom for your next class. "
                        pause 2.0
                        jump wedochealthclass1
                " *Say nothing* ":
                    jac " ... "
                    scene black with dissolve
                    " Jacob says nothing afterwards. "
                    " You enjoy the silence as you felt the fresh air around you... "
                    " ...You and Jacob enjoy the view for a bit. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your health class. "
                    " You walked down from the rooftop and went to your classroom for your next class. "
                    pause 2.0
                    jump wedochealthclass1
        else:
            x " God damn it... "
            $ jacobknow = True
            " Huh. You've heard about this guy before. His name is Jacob. "
            " He seems to be pretty frustrated over something. "
            " You asked him if he was alright or not. "
            jac " Does it look like I'm doing alright right now? "
            jac " Of course I'm not. "
            jac " I'm not sure if you were there or not, but someone decided to throw away my goggles and my bandana. "
            jac " At the very start of the day, too... "
            jac " Luckily, no one was looking while my face was showing... "
            jac " ...It still pisses me off that someone decided to do that to me though! "
            jac " I couldn't get to see who took it off, probably some ugly bastard... "
            jac " ...I can't be the one to talk though, I'm definitely uglier than them without my goggles and bandana. "
            jac " God damn it... "
            menu:
                " I think you look pretty cool, with or without the bandana ":
                    $ jacoblv += 10
                    jac " Really? you think so? "
                    jac " I find that really hard to believe. "
                    jac " You haven't even seen me without the bandana and everything. "
                    jac " You don't really know what you're saying, aren't you? "
                    jac " ...Thanks for the compliment, though. "
                    jac " I know that you're just trying to make me feel better. "
                    jac " Can't really be mad at you or anything... "
                    if jacoblv >= 20 or jacoblv == 20:
                        jac " Why do you hang out with me so much? "
                        jac " Normally people would start running away from me if I talked to them too much. "
                        jac " ...You're an odd one. You're hard to understand. "
                        jac " ...But I guess...your company is nice. "
                        jac " You can hang out with me more if you want. "
                        jac " No one has really decided to hang out with me for this long... "
                        scene black with dissolve
                        " Jacob says nothing afterwards. "
                        " You enjoy the silence as you felt the fresh air around you... "
                        " ...You and Jacob enjoy the view for a bit. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your health class. "
                        " You walked down from the rooftop and went to your classroom for your next class. "
                        pause 2.0
                        jump wedochealthclass1
                    else:
                        scene black with dissolve
                        " Jacob says nothing afterwards. "
                        " You enjoy the silence as you felt the fresh air around you... "
                        " ...You and Jacob enjoy the view for a bit. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your health class. "
                        " You walked down from the rooftop and went to your classroom for your next class. "
                        pause 2.0
                        jump wedochealthclass1
                " *Say nothing* ":
                    jac " ... "
                    scene black with dissolve
                    " Jacob says nothing afterwards. "
                    " You enjoy the silence as you felt the fresh air around you... "
                    " ...You and Jacob enjoy the view for a bit. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your health class. "
                    " You walked down from the rooftop and went to your classroom for your next class. "
                    pause 2.0
                    jump wedochealthclass1
    label glitterlexycat:
        show mattesad at center with easeinleft
        if matteknow == True:
            " You walked over to the troubled girl, staring into a blank canvas. "
            " You asked her what was wrong. "
            hide mattesad at bottom
            show matteneutral at center
            ma " Oh, hey there [name]! "
            ma " I'm doing fine, it's just that I've been getting some...artists block recently. "
            ma " You know that feeling where you want to do something, but then when you try to do it... "
            ma " It just suddenly feels like you can't? "
            ma " It's a horrible feeling since I {i}really{/i} want to start painting! "
            hide matteneutral at bottom
            show mattesad at center
            ma " But, alas...I have no ideas... "
            ma " I could draw the sky, but I've done that countless of times before! "
            ma " I could draw this rooftop, but I've already done that a few times... "
            ma " I could go around the school...but there's really nothing new. "
            ma " Geez, what can I do with all of this? "
            ma " I'm gonna need to have some sort of inspiration to paint... "
            ma " ...Or else I'm going to die of boredom for the rest of the break. "
            ma " And I really don't want that to happen! "
            ma " Boredom is my family's worst enemy!! "
            ma " Gah...I hate this so muchhhh... "
            menu:
                " Strike a pose for Matte ":
                    $ mattelv += 10
                    hide mattesad at bottom
                    show mattesurprised at center
                    " You decided to strike a rather inspirational pose for Matte to paint you. "
                    " Matte looked pretty dumbfounded at what you were doing. "
                    ma " ...? "
                    ma " [name], what are you doing...? "
                    ma " That pose you're doing is so silly, I... "
                    ma " ...Wait a moment. "
                    hide mattesurprised at bottom
                    show mattehappy at center
                    ma " You just want me to use you as inspiration, don't you? "
                    ma " Haha, [name]...you didn't have to pose just for me... "
                    ma " But, if you insist, then I suppose I can paint you for this break. "
                    hide mattehappy at bottom
                    show mattesilly at center
                    ma " Just make sure that you don't move too much while you're posing. "
                    ma " Otherwise, you're going to make me a little distracted. "
                    scene black with dissolve
                    " You spent the rest of the break standing still in a funny pose for Matte on the rooftop. "
                    " It was a little painful having to stay still for so long, but she eventually let you rest. "
                    " The painting got done pretty quickly, which was surprising considering the amount of time you need for a good painting... "
                    " You suppose that Matte is just that good. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked down from the rooftop and went back to your classroom for your health class. "
                    pause 2.0
                    jump wedochealthclass1
                " Give her a pat on the head ":
                    $ mattelv += 5
                    hide mattesad at bottom
                    show matteneutral at center
                    ma " Hehe...thanks, [name]. "
                    ma " While you're here, maybe you could give me some painting ideas? "
                    ma " I don't want you to just come up to me for nothing. "
                    ma " I know you've got some good ideas in that mind of yours, so... "
                    ma " ...Give those good ideas to me! "
                    scene black with dissolve
                    " You spent the rest of the break giving Matte ideas. "
                    " Most of the ideas you gave her, she's done, but... "
                    " When you mentioned painting some gems, she actually did it. "
                    " You thought it would be difficult for her, but actually, it was pretty easy. "
                    " She ended up painting a pearl and a rose quartz with pink flowers around them. "
                    " Is this a reference? go ahead and guess. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked down from the rooftop and went back to your classroom for your health class. "
                    pause 2.0
                    jump wedochealthclass1
        else:
            " You walked over to the troubled girl, staring into a blank canvas. "
            " You asked her what was wrong. "
            hide mattesad at bottom
            show matteneutral at center
            x " Oh, hey there [name]! "
            $ matteknow = True
            ma " I'm Matte, by the way. Pleasure to meet you! "
            ma " I'm doing fine, it's just that I've been getting some...artists block recently. "
            ma " You know that feeling where you want to do something, but then when you try to do it... "
            ma " It just suddenly feels like you can't? "
            ma " It's a horrible feeling since I {i}really{/i} want to start painting! "
            hide matteneutral at bottom
            show mattesad at center
            ma " But, alas...I have no ideas... "
            ma " I could draw the sky, but I've done that countless of times before! "
            ma " I could draw this rooftop, but I've already done that a few times... "
            ma " I could go around the school...but there's really nothing new. "
            ma " Geez, what can I do with all of this? "
            ma " I'm gonna need to have some sort of inspiration to paint... "
            ma " ...Or else I'm going to die of boredom for the rest of the break. "
            ma " And I really don't want that to happen! "
            ma " Boredom is my family's worst enemy!! "
            ma " Gah...I hate this so muchhhh... "
            menu:
                " Strike a pose for Matte ":
                    $ mattelv += 10
                    hide mattesad at bottom
                    show mattesurprised at center
                    " You decided to strike a rather inspirational pose for Matte to paint you. "
                    " Matte looked pretty dumbfounded at what you were doing. "
                    ma " ...? "
                    ma " [name], what are you doing...? "
                    ma " That pose you're doing is so silly, I... "
                    ma " ...Wait a moment. "
                    hide mattesurprised at bottom
                    show mattehappy at center
                    ma " You just want me to use you as inspiration, don't you? "
                    ma " Haha, [name]...you didn't have to pose just for me... "
                    ma " But, if you insist, then I suppose I can paint you for this break. "
                    hide mattehappy at bottom
                    show mattesilly at center
                    ma " Just make sure that you don't move too much while you're posing. "
                    ma " Otherwise, you're going to make me a little distracted. "
                    scene black with dissolve
                    " You spent the rest of the break standing still in a funny pose for Matte on the rooftop. "
                    " It was a little painful having to stay still for so long, but she eventually let you rest. "
                    " The painting got done pretty quickly, which was surprising considering the amount of time you need for a good painting... "
                    " You suppose that Matte is just that good. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked down from the rooftop and went back to your classroom for your health class. "
                    pause 2.0
                    jump wedochealthclass1
                " Give her a pat on the head ":
                    $ mattelv += 5
                    hide mattesad at bottom
                    show matteneutral at center
                    ma " Hehe...thanks, [name]. "
                    ma " While you're here, maybe you could give me some painting ideas? "
                    ma " I don't want you to just come up to me for nothing. "
                    ma " I know you've got some good ideas in that mind of yours, so... "
                    ma " ...Give those good ideas to me! "
                    scene black with dissolve
                    " You spent the rest of the break giving Matte ideas. "
                    " Most of the ideas you gave her, she's done, but... "
                    " When you mentioned painting some gems, she actually did it. "
                    " You thought it would be difficult for her, but actually, it was pretty easy. "
                    " She ended up painting a pearl and a rose quartz with pink flowers around them. "
                    " Is this a reference? go ahead and guess. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked down from the rooftop and went back to your classroom for your health class. "
                    pause 2.0
                    jump wedochealthclass1

label wedoclibrary1:
    # nox and temero
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and spotted two of your classmates talking to eachother "
    " You wanted to know what they were talking about, so you walked over to them to join into their conversation. "
    show noxneutral at left with easeinright
    show temeroneutral at right with easeinright
    if noxknow == True and temeroknow == True:
        n " I've already told you... "
        n " I'm not taking up your offer... "
        tm " Aww, come on, Noxxy! "
        tm " You know you want this good stuff. "
        " She says before pointing at a pill bottle labeled 'stay up pills, by Temero'. "
        tm " This stuff can help you stay up for longer! "
        tm " Make you less sleepy... Make you rest easy at night... "
        tm " It's all you've ever wanted, really! "
        n " While I do...*yawn*...want to stop sleeping so much... "
        n " I don't think I can trust you with the things you've done... "
        n " I don't know what kind of stuff you put in this, anyway... "
        tm " Oh, I put in all the good stuff, don't worry! "
        tm " You can have all of this, you just have to trust me on this one. "
        tm " I'm trustable! Right [name]? "
        " Oh. Well you weren't expecting to be dragged into this. "
        " Gues you have to make a choice here now. "
        menu:
            " I think you're trustable ":
                $ temerolv += 10
                hide temeroneutral at bottom
                show temerohappy at right
                tm " See? I {i}am{/i} trustable! "
                tm " Even [name] agrees! "
                n " ...It's just...*yawn*... "
                n " One person...syaing you're trustable... "
                n " I'm not taking up your product, sorry... "
                hide temerohappy at bottom
                show temeroangry at right
                tm " ...Seriously? "
                tm " You still don't trust me? "
                " For a split moment, you swear you just saw butterfly wings popping out from the sides of her head. "
                hide temeroangry at bottom
                show temerosad at right
                " But, she manages to calm herself down before she could do anything serious. "
                " Well...that was weird. "
                tm " ..Sorry. I get why you'd not trust me. "
                n " It's fine...could we talk about something else though...? "
                hide temerosad at bottom
                show temeroneutral at right
                tm " ...Sure! What would you like to talk about? "
                n " Well, let's see.. "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Nox. "
                " You guys just decided to talk about completely random things... "
                " Like butterfly fun facts. "
                " And the dreams Nox has been having. "
                " Pretty interesting in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for your next class. "
                " You got out of the library and you walked back to your classroom for health class. "
                pause 2.0
                jump wedochealthclass1
            " Don't listen to her ":
                $ noxlv += 10
                n " ...See...? "
                n " Even [they] can agree...that you're not trust worthy... "
                hide temeroneutral at bottom
                show temeroangry at right
                tm " ...Seriously? "
                tm " You still don't trust me? "
                " For a split moment, you swear you just saw butterfly wings popping out from the sides of her head. "
                hide temeroangry at bottom
                show temerosad at right
                " But, she manages to calm herself down before she could do anything serious. "
                " Well...that was weird. "
                tm " ..Sorry. I get why you'd not trust me. "
                n " It's fine...could we talk about something else though...? "
                hide temerosad at bottom
                show temeroneutral at right
                tm " ...Sure! What would you like to talk about? "
                n " Well, let's see.. "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Nox. "
                " You guys just decided to talk about completely random things... "
                " Like butterfly fun facts. "
                " And the dreams Nox has been having. "
                " Pretty interesting in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for your next class. "
                " You got out of the library and you walked back to your classroom for health class. "
                pause 2.0
                jump wedochealthclass1
    elif noxknow == True and temeroknow == False:
        n " I've already told you... "
        n " I'm not taking up your offer... "
        x " Aww, come on, Noxxy! "
        x " You know you want this good stuff. "
        " She says before pointing at a pill bottle labeled 'stay up pills, by Temero'. "
        x " This stuff can help you stay up for longer! "
        x " Make you less sleepy... Make you rest easy at night... "
        x " It's all you've ever wanted, really! "
        n " While I do...*yawn*...want to stop sleeping so much... "
        n " I don't think I can trust you with the things you've done... "
        n " I don't know what kind of stuff you put in this, anyway... "
        x " Oh, I put in all the good stuff, don't worry! "
        x " You can have all of this, you just have to trust me on this one. "
        x " I'm trustable! Right [name]? "
        $ temeroknow = True
        tm " You can ALWAYS trust your good friend Temero NEO! "
        " Oh. Well you weren't expecting to be dragged into this. "
        " Gues you have to make a choice here now. "
        menu:
            " I think you're trustable ":
                $ temerolv += 10
                hide temeroneutral at bottom
                show temerohappy at right
                tm " See? I {i}am{/i} trustable! "
                tm " Even [name] agrees! "
                n " ...It's just...*yawn*... "
                n " One person...syaing you're trustable... "
                n " I'm not taking up your product, sorry... "
                hide temerohappy at bottom
                show temeroangry at right
                tm " ...Seriously? "
                tm " You still don't trust me? "
                " For a split moment, you swear you just saw butterfly wings popping out from the sides of her head. "
                hide temeroangry at bottom
                show temerosad at right
                " But, she manages to calm herself down before she could do anything serious. "
                " Well...that was weird. "
                tm " ..Sorry. I get why you'd not trust me. "
                n " It's fine...could we talk about something else though...? "
                hide temerosad at bottom
                show temeroneutral at right
                tm " ...Sure! What would you like to talk about? "
                n " Well, let's see.. "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Nox. "
                " You guys just decided to talk about completely random things... "
                " Like butterfly fun facts. "
                " And the dreams Nox has been having. "
                " Pretty interesting in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for your next class. "
                " You got out of the library and you walked back to your classroom for health class. "
                pause 2.0
                jump wedochealthclass1
            " Don't listen to her ":
                $ noxlv += 10
                n " ...See...? "
                n " Even [they] can agree...that you're not trust worthy... "
                hide temeroneutral at bottom
                show temeroangry at right
                tm " ...Seriously? "
                tm " You still don't trust me? "
                " For a split moment, you swear you just saw butterfly wings popping out from the sides of her head. "
                hide temeroangry at bottom
                show temerosad at right
                " But, she manages to calm herself down before she could do anything serious. "
                " Well...that was weird. "
                tm " ..Sorry. I get why you'd not trust me. "
                n " It's fine...could we talk about something else though...? "
                hide temerosad at bottom
                show temeroneutral at right
                tm " ...Sure! What would you like to talk about? "
                n " Well, let's see.. "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Nox. "
                " You guys just decided to talk about completely random things... "
                " Like butterfly fun facts. "
                " And the dreams Nox has been having. "
                " Pretty interesting in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for your next class. "
                " You got out of the library and you walked back to your classroom for health class. "
                pause 2.0
                jump wedochealthclass1
    elif noxknow == False and temeroknow == True:
        x " I've already told you... "
        x " I'm not taking up your offer... "
        $ noxknow = True
        tm " Aww, come on, Noxxy! "
        tm " You know you want this good stuff. "
        " She says before pointing at a pill bottle labeled 'stay up pills, by Temero'. "
        tm " This stuff can help you stay up for longer! "
        tm " Make you less sleepy... Make you rest easy at night... "
        tm " It's all you've ever wanted, really! "
        n " While I do...*yawn*...want to stop sleeping so much... "
        n " I don't think I can trust you with the things you've done... "
        n " I don't know what kind of stuff you put in this, anyway... "
        tm " Oh, I put in all the good stuff, don't worry! "
        tm " You can have all of this, you just have to trust me on this one. "
        tm " I'm trustable! Right [name]? "
        " Oh. Well you weren't expecting to be dragged into this. "
        " Gues you have to make a choice here now. "
        menu:
            " I think you're trustable ":
                $ temerolv += 10
                hide temeroneutral at bottom
                show temerohappy at right
                tm " See? I {i}am{/i} trustable! "
                tm " Even [name] agrees! "
                n " ...It's just...*yawn*... "
                n " One person...syaing you're trustable... "
                n " I'm not taking up your product, sorry... "
                hide temerohappy at bottom
                show temeroangry at right
                tm " ...Seriously? "
                tm " You still don't trust me? "
                " For a split moment, you swear you just saw butterfly wings popping out from the sides of her head. "
                hide temeroangry at bottom
                show temerosad at right
                " But, she manages to calm herself down before she could do anything serious. "
                " Well...that was weird. "
                tm " ..Sorry. I get why you'd not trust me. "
                n " It's fine...could we talk about something else though...? "
                hide temerosad at bottom
                show temeroneutral at right
                tm " ...Sure! What would you like to talk about? "
                n " Well, let's see.. "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Nox. "
                " You guys just decided to talk about completely random things... "
                " Like butterfly fun facts. "
                " And the dreams Nox has been having. "
                " Pretty interesting in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for your next class. "
                " You got out of the library and you walked back to your classroom for health class. "
                pause 2.0
                jump wedochealthclass1
            " Don't listen to her ":
                $ noxlv += 10
                n " ...See...? "
                n " Even [they] can agree...that you're not trust worthy... "
                hide temeroneutral at bottom
                show temeroangry at right
                tm " ...Seriously? "
                tm " You still don't trust me? "
                " For a split moment, you swear you just saw butterfly wings popping out from the sides of her head. "
                hide temeroangry at bottom
                show temerosad at right
                " But, she manages to calm herself down before she could do anything serious. "
                " Well...that was weird. "
                tm " ..Sorry. I get why you'd not trust me. "
                n " It's fine...could we talk about something else though...? "
                hide temerosad at bottom
                show temeroneutral at right
                tm " ...Sure! What would you like to talk about? "
                n " Well, let's see.. "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Nox. "
                " You guys just decided to talk about completely random things... "
                " Like butterfly fun facts. "
                " And the dreams Nox has been having. "
                " Pretty interesting in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for your next class. "
                " You got out of the library and you walked back to your classroom for health class. "
                pause 2.0
                jump wedochealthclass1
    else:
        x " I've already told you... "
        x " I'm not taking up your offer... "
        $ noxknow = True
        x " Aww, come on, Noxxy! "
        x " You know you want this good stuff. "
        " She says before pointing at a pill bottle labeled 'stay up pills, by Temero'. "
        x " This stuff can help you stay up for longer! "
        x " Make you less sleepy... Make you rest easy at night... "
        x " It's all you've ever wanted, really! "
        n " While I do...*yawn*...want to stop sleeping so much... "
        n " I don't think I can trust you with the things you've done... "
        n " I don't know what kind of stuff you put in this, anyway... "
        x " Oh, I put in all the good stuff, don't worry! "
        x " You can have all of this, you just have to trust me on this one. "
        x " I'm trustable! Right [name]? "
        $ temeroknow = True
        tm " You can ALWAYS trust your good friend Temero NEO! "
        " Oh. Well you weren't expecting to be dragged into this. "
        " Gues you have to make a choice here now. "
        menu:
            " I think you're trustable ":
                $ temerolv += 10
                hide temeroneutral at bottom
                show temerohappy at right
                tm " See? I {i}am{/i} trustable! "
                tm " Even [name] agrees! "
                n " ...It's just...*yawn*... "
                n " One person...syaing you're trustable... "
                n " I'm not taking up your product, sorry... "
                hide temerohappy at bottom
                show temeroangry at right
                tm " ...Seriously? "
                tm " You still don't trust me? "
                " For a split moment, you swear you just saw butterfly wings popping out from the sides of her head. "
                hide temeroangry at bottom
                show temerosad at right
                " But, she manages to calm herself down before she could do anything serious. "
                " Well...that was weird. "
                tm " ..Sorry. I get why you'd not trust me. "
                n " It's fine...could we talk about something else though...? "
                hide temerosad at bottom
                show temeroneutral at right
                tm " ...Sure! What would you like to talk about? "
                n " Well, let's see.. "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Nox. "
                " You guys just decided to talk about completely random things... "
                " Like butterfly fun facts. "
                " And the dreams Nox has been having. "
                " Pretty interesting in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for your next class. "
                " You got out of the library and you walked back to your classroom for health class. "
                pause 2.0
                jump wedochealthclass1
            " Don't listen to her ":
                $ noxlv += 10
                n " ...See...? "
                n " Even [they] can agree...that you're not trust worthy... "
                hide temeroneutral at bottom
                show temeroangry at right
                tm " ...Seriously? "
                tm " You still don't trust me? "
                " For a split moment, you swear you just saw butterfly wings popping out from the sides of her head. "
                hide temeroangry at bottom
                show temerosad at right
                " But, she manages to calm herself down before she could do anything serious. "
                " Well...that was weird. "
                tm " ..Sorry. I get why you'd not trust me. "
                n " It's fine...could we talk about something else though...? "
                hide temerosad at bottom
                show temeroneutral at right
                tm " ...Sure! What would you like to talk about? "
                n " Well, let's see.. "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Nox. "
                " You guys just decided to talk about completely random things... "
                " Like butterfly fun facts. "
                " And the dreams Nox has been having. "
                " Pretty interesting in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for your next class. "
                " You got out of the library and you walked back to your classroom for health class. "
                pause 2.0
                jump wedochealthclass1

label wedochealthclass1:
    scene classroom with dissolve
    " You walked into the classroom and waited for the health teacher to get here. "
    " ...And he comes in after a few seconds right after you got on your seat. "
    show altrixsad at center with easeinright
    msa " ...Whew...hopefully I'm not late.. "
    " The class greets Mister Altrix and reassures him that he's not late. "
    " One of your clasmates then asks what the activity is going to be for today. "
    hide altrixsad at bottom
    show altrixneutral at center
    msa " Oh, right...! The activity... "
    msa " Almost forgot about that, silly me. "
    msa " Thank you for reminding me, class! "
    msa " Today's activity its going to be drawing. "
    msa " Pair yourself with someone else in this class, and make a poster about health! "
    msa " Eating healthy...having a healthy lifestyle... "
    msa " This is going to be worth 60 points in total! "
    msa " Oh right... I've already got you all each drawing/coloring materials and paper for you guys to draw on! "
    msa " Just take some drawing and coloring materials..and paper...from my desk! "
    msa " If you need anymore, you're going to have to ask one of the cafeteria ladies if they have some. "
    msa " Good luck! "
    hide altrixneutral at left with easeoutleft
    " Alright, time to pair up with someone. "
    " You looked around to see who you could pair up with... "
    if disklv >= 5 or disklv == 5:
        " You decided to pair up with Disk. "
        " You walked over to him and asked if he had a partner. "
        show diskneutral at center with easeinleft
        d " Oh? You want to pair up with me? "
        d " Why, of course you can! "
        d " Me and Quinn usually pair up with eachother, but I'm sure he doesn't mind... "
        d " So, do you want to be the one to get the papers and everything, or - "
        d " You know what, I'll just get them for you! "
        d " I insist! "
        hide diskneutral at right with easeoutright
        pause 1.0
        show diskneutral at center with easeinright
        d " Here we go! "
        " Disk comes back with all of the needed materials and put them down onto the desk. "
        " He came back pretty fast... "
        d " I already have some ideas for our poster! "
        d " Ohhh, maybe we could do this idea! "
        " Disk points at an image on his phone, then scrolls to another one. "
        d " Or maybe even this one! "
        d " This one is really cute and informational, I like it! "
        menu:
            " Not as cute as you though ":
                $ disklv += 10
                hide diskneutral at bottom
                show diskhappy at center
                " WOAH there buddy. What're you saying there? "
                " You're very lucky that this isn't a dating sim. "
                " Let me just change how Disk is gonna react to this for a bit... "
                d " Awwhh, [name]!! You're gonna make me blush!! "
                d " I think that you're cute, too! "
                d " I better not hear you saying otherwise! "
                hide diskhappy at bottom
                show diskneutral at center
                d " Anyways, back to choosing which poster idea we should do... "
                scene black with dissolve
                " Disk showed you a couple of ideas for the poster... "
                " ..You two eventually ended up on the one that was a mix of cute and informational. "
                " You two did your fair share of work on the poster before finishing it. "
                " You then passed the work to Mister Altrix, finally letting yourself relax for a bit. "
                " As you were relaxing, you talked with Disk about how his day was going. "
                " He seemed pretty content hanging out with you. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
            " *Say nothing* ":
                d " I've got a whole lot more ideas to show you though! "
                d " Let's look at all of them before we settle on one, yeah? "
                d " Who knows, there might be something that you really like! "
                scene black with dissolve
                " Disk showed you a couple of ideas for the poster... "
                " ..You two eventually ended up on the one that was a mix of cute and informational. "
                " You two did your fair share of work on the poster before finishing it. "
                " You then passed the work to Mister Altrix, finally letting yourself relax for a bit. "
                " As you were relaxing, you talked with Disk about how his day was going. "
                " He seemed pretty content hanging out with you. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
    elif quinnlv >= 5 or quinnlv == 5:
        " You decided to pair up with Quinn. "
        " You walked over to him and asked him if he had a partner already. "
        show quinnneutral at center with easeinleft
        q " Oh? you want to pair up with me? "
        q " Well...that's quite surprising. But, if you really want to be partners with me, then sure. "
        q " Usually I partner up with my brother, but I'm sure he doesn't mind. "
        q " Now, we should get the materials needed for the poster. "
        q " I'll go ahead and get the materials for you. "
        hide quinnneutral at right with easeoutright
        pause 1.0
        show quinnneutral at center with easeinright
        q " Here we are. "
        " He came back with the materials needed, and placed them down onto the desk. "
        " He came back pretty fast... "
        q " Now... we should get to work on our poster. "
        q " But of course, we need to get inspiration. "
        q " Luckily I have enough data to get some ideas from the internet... "
        q " Hhmhmm...oh, how about this one? "
        q " This one's quite eye catching. And not only that... "
        q " It's informational and interesting. "
        q " The perfect mix just for our poster. "
        menu:
            " Not as interesting as you though ":
                $ quinnlv += 10
                hide quinnneutral at bottom
                show quinnhappy at center
                " WOAH there buddy. What're you saying there? "
                " You're very lucky that this isn't a dating sim. "
                " Let me just change how Quinn is gonna react to this for a bit... "
                q " Oh. "
                q " Hah...I appreciate your compliment. "
                q " Not many would say things like that to me. "
                q " You're an odd one, [name]...in a good way. "
                q " I think you're quite interesting as well. "
                q " Don't tell yourself that you're garbage or anything like that. "
                hide quinnhappy at bottom
                show quinnneutral at center
                q " Now, now...let's get back to focusing. "
                q " We'll be doing this design. It's gonna be the best for us. "
                q " I'll do this part, and you can do that part. "
                q " Sound good to you? "
                scene black with dissolve
                " You two did your fair share of work for the poster. "
                " Your side looked slightly worse than Quinn's side, but it looked alright. "
                " Eventually, you two were done with the poster. "
                " You then went over to Mister Altrix to pass your work to him. "
                " Finally, some time for you to relax... "
                " As you were relaxing, you decided to talk to Quinn a little bit more. "
                " He seemed pretty happy that someone wanted to talk to him. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
            " *Say nothing* ":
                q " Well, let's do this one then. "
                q " I'll do this part, and you can do that part. "
                q " Sound good to you? "
                scene black with dissolve
                " You two did your fair share of work for the poster. "
                " Your side looked slightly worse than Quinn's side, but it looked alright. "
                " Eventually, you two were done with the poster. "
                " You then went over to Mister Altrix to pass your work to him. "
                " Finally, some time for you to relax... "
                " As you were relaxing, you decided to talk to Quinn a little bit more. "
                " He seemed pretty happy that someone wanted to talk to him. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
    elif mattelv >= 10 or mattelv == 10:
        " You decided to pair up with Matte. "
        " You walked over to her and asked her if she had a pertner already. "
        show matteneutral at right with easeinright
        ma " Oho, pairing up with the artist now, are we? "
        ma " I know what you're thinking, you're not slick. "
        ma " Buuut, if that's what you want to do, then I don't mind. "
        ma " Jam would actually want to partner up with me, but I'm sure she doesn't mind a change of pace! "
        ma " Besides, this could be an oppurtunity for her to make new friends! "
        ma " Anyway, enough with my talking... "
        ma " Let's get started! I'll go ahead and get all of the materials that we need! "
        ma " Stay right here, okay? "
        hide matteneutral at left with easeoutleft
        pause 1.0
        show matteneutral at center with easeinleft
        ma " I got all of them! "
        " Matte came back with all of the materials needed for the poster. "
        " She came back pretty fast... "
        ma " Now, I don't want you to suffer on coloring, sooo... "
        ma " How about you just do the sketching and I'll do everything else? "
        ma " It's going to be easier for you that way! "
        ma " I don't want you to go through the hells of color theory. "
        menu:
            " I'll go through the hells of color theory for you ":
                $ mattelv += 10
                hide matteneutral at bottom
                show mattehappy at center
                ma " Aw...really? "
                ma " Are you sure about that? "
                ma " Well, if you really want to, then we can! "
                ma " I'll teach you which colors are good to use or not. "
                scene black with dissolve
                " You went through the hells of color theory with Matte. "
                " It wasn't too bad, since the final poster looked great in the end. "
                " You then passed you and Matte's work to Mister Altrix, finally getting some time to relax. "
                " As you were relaxing, you decided to talk with Matte for a bit. "
                " She seemed pretty content talking to you. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
            " *Say nothing* ":
                ma " Here, I'll show you our reference picture! "
                ma " Here it is... "
                " Matte shows you a picture of what you're going to be doing for the poster. "
                " You then started sketching it all out... "
                scene black with dissolve
                " You sketched the work for your poster and let Matte do all of the work. "
                " It wasn't too bad, since the final poster looked great in the end. "
                " You then passed you and Matte's work to Mister Altrix, finally getting some time to relax. "
                " As you were relaxing, you decided to talk with Matte for a bit. "
                " She seemed pretty content talking to you. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
    elif jamlv >= 15 or jamlv == 15:
        " You decided to pair up with Jam. "
        " You walked over to her and asked her if she had a partner already. "
        show jamneutral at right with easeinright
        ja " ...You want to pair up with me...? "
        ja " Well, I don't mind, but... "
        ja " I was planning to pair up with Matte. "
        ja " I don't mind that you want to pair up with me though... "
        ja " Uh...let's get started. "
        ja " I should probably get the materials for you. "
        ja " Stay here. "
        hide jamneutral at left with easeoutleft
        pause 1.0
        show jamneutral at center with easeinleft
        ja " I'm back. Here's everything we need. "
        " Jam puts all of the things needed for the poster down onto the desk. "
        " She came back pretty fast... "
        ja " Now, uh...we probably need a reference photo. "
        ja " But hear me out, how about we just add the earth and some healthy stuff? "
        ja " Like sleeping well...eating vegetables...all that. "
        ja " I did that once and good a perfect grade in my old school. "
        ja " You can never go wrong with the earth and some healthy stuff. "
        ja " But, just so you know...my drawing skills are pretty shit. "
        ja " Don't expect anything good out of me. "
        menu:
            " I think you're gonna do fine ":
                $ jamlv += 10
                hide jamneutral at bottom
                show jamsurprised at center
                ja " ??? "
                ja " Uh ??? thanks ???? "
                hide jamsurprised at bottom
                show jamneutral at center
                ja " I don't know how to exactly respond to that... "
                ja " ...But I think you're going to do okay too. "
                scene black with dissolve
                " You then got to work with yours and Jam's poster. "
                " It ended up turning okay in the end. Not too bad, not too good. "
                " You then passed the work to Mister Altrix, finally getting some time to relax. "
                " You spent the rest of class hours talking with Jam. "
                " She seemed a little bit surprised that you wanted to know more about her at first. "
                " But she slowly started being comfortable with you the more you two talked. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
            " *Say nothing* ":
                ja " Alright, let's start. "
                ja " I'll do the line art and stuff, then you do the colors. "
                ja " Maybe I'll help you in coloring here and there... "
                scene black with dissolve
                " You then got to work with yours and Jam's poster. "
                " It ended up turning okay in the end. Not too bad, not too good. "
                " You then passed the work to Mister Altrix, finally getting some time to relax. "
                " You spent the rest of class hours talking with Jam. "
                " She seemed a little bit surprised that you wanted to know more about her at first. "
                " But she slowly started being comfortable with you the more you two talked. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
    elif sparklv >= 10 or sparklv == 10:
        " You decided to pair up with Spark. "
        " You walked up to him and asked him if he had a partner already. "
        show sparkneutral at center with easeinleft
        sp " Oh, you wanted to partner up with me? "
        sp " I mean, hell, why not. "
        sp " I usually partner up with Temero whenever it's a duo, but I guess you'll do. "
        " Spark's antenna twitches a bit and lets out a little...'spark'. "
        hide sparkneutral at bottom
        show sparkangry at center
        sp " Shit...uh, ignore that. "
        sp " Just my antennas being annoying again. "
        sp " It usually does that whenever I'm being moody. "
        sp " Not that I don't like you being my partner - "
        sp " Ah, whatever...I'm just rambling again. "
        hide sparkangry at bottom
        show sparkneutral at center
        sp " (Shit...my antennas are acting up again...) "
        sp " (I don't want to do this right here, right now...) "
        sp " (Mister Clio hasn't even given me orders yet...) "
        sp " (..I need to fix myself up after this class.) "
        sp " Erh, I'll go ahead and get the materials we need. "
        sp " Stay here, would you? "
        hide sparkneutral at right with easeoutright
        pause 1.0
        show sparkneutral at center with easeinright
        sp " I'm back. Here's everything we need... "
        " Spark places down the things you two need down onto the desk. "
        " He got back pretty fast... "
        sp " Since this a duo project, of course we're going to do this together. "
        sp " You do that side, and I'll do this side. "
        sp " I already have a reference photo for our poster, so you don't have to worry. "
        sp " Let me just prays that it loads in... "
        hide sparkneutral at bottom
        show sparkangry at center
        sp " Damn it, it's taking so long to load... "
        sp " Come on, I have a project to do...don't fail me now... "
        menu:
            " You look cute when you're angry ":
                $ sparklv += 10
                hide sparkangry at bottom
                show sparkshit at center
                " WOAH there buddy. What're you saying there? "
                " You're very lucky that this isn't a dating sim. "
                " Let me just change how Spark is gonna react to this for a bit... "
                sp " ...Do you even know what you're saying there??? "
                sp " God, you little... "
                sp " ...Whatever, thanks for the compliment anyway. "
                sp " You look a little decent yourself. "
                hide sparkshit at bottom
                show sparkneutral at center
                sp " Finally, it loaded in. "
                sp " Alright. Remember, you do this side and I do this side. "
                sp " Got that? Then let's start. "
                scene black with dissolve
                " You then got to work with Spark on the poster. "
                " In the end, the poster looked pretty good, in your opinion. "
                " You then passed the work to Mister Altrix, finally getting some time to relax. "
                " You spent the rest of class hours talking with Spark. "
                " He didn't seem to mind your company... "
                " You tried asking him about what happened with his antennas... "
                " ...But he ignored your question. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
            " *Say nothing* ":
                hide sparkangry at bottom
                show sparkneutral at center
                sp " Finally, it loaded in. "
                sp " Alright. Remember, you do this side and I do this side. "
                sp " Got that? Then let's start. "
                scene black with dissolve
                " You then got to work with Spark on the poster. "
                " In the end, the poster looked pretty good, in your opinion. "
                " You then passed the work to Mister Altrix, finally getting some time to relax. "
                " You spent the rest of class hours talking with Spark. "
                " He didn't seem to mind your company... "
                " You tried asking him about what happened with his antennas... "
                " ...But he ignored your question. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
    elif temerolv >= 20 or temerolv == 20:
        " You decided to pair up with Temero. "
        " You walked up to her and asked her if she had a partner already. "
        show temeroneutral at center with easeinleft
        tm " Oh, what's that? "
        tm " You want to work with the GREEAAATT Temero Neo? "
        hide temeroneutral at bottom
        show temerohappy at center
        tm " Well, I'd be happy to work with you! "
        tm " Though I usually pair up with Spark in duos, but I don't mind changing up for now. "
        tm " Let's begin! - "
        hide temerohappy at bottom
        show temeroangry at center
        " Before she could finish her sentence, she starts coughing a lot. "
        " You swear you could see pink butterfly wings grow out of her head, but they go back in after she's done coughing. "
        hide temeroangry at bottom
        show temeroneutral at center
        tm " ...Ahem. "
        tm " Sorry about that! Just feeling bad today, is all. "
        tm " I'll go ahead and get the materials needed then! "
        tm " You stay here, alright? "
        hide temeroneutral at right with easeoutright
        pause 1.0
        show temeroneutral at center with easeinright
        tm " Here we are! "
        " Temero puts the materials needed for the poster down on the desk. "
        tm " Now, our theme is 'healthy lifestyle'...or encouraging a healthy lifestyle. "
        tm " I've already got a reference for us! This one right here... "
        " She shows you a picture of her reference on the phone. "
        " Looks pretty good. Also pretty informational. "
        tm " Hmm...maybe I could make a product to make others instantly have a healthy lifestyle? "
        tm " Just a drink and you'll already feel healthy! Yes, that sounds perfect... "
        menu:
            " I'd buy all of that stuff for you ":
                $ temerolv += 10
                hide temeroneutral at bottom
                show temerohappy at center
                tm " Of course you would! "
                tm " My ideas are just that good, after all! "
                tm " Thank you for supporting my business, heheh. "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " Though, we've got to lock in now."
                tm " Don't want to get distracted and get a low grade! "
                tm " You do this part, and I do this part. "
                tm " Ready? let's begin! "
                scene black with dissolve
                " You then got to work on your poster. "
                " After you and Temero were done, the poster didn't look too bad. "
                " When you were done, you passed the work to Mister Altrix. "
                " You finally got some time to relax with Temero... "
                " You talked with Temero for your free time. "
                " You tried asking her about that whole butterfly thing earlier... "
                " But she just ignored your question and acted clueless. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
            " *Say nothing* ":
                tm " Though, I've got to lock in now."
                tm " Don't want to get distracted and get a low grade! "
                tm " You do this part, and I do this part. "
                tm " Ready? let's begin! "
                scene black with dissolve
                " You then got to work on your poster. "
                " After you and Temero were done, the poster didn't look too bad. "
                " When you were done, you passed the work to Mister Altrix. "
                " You finally got some time to relax with Temero... "
                " You talked with Temero for your free time. "
                " You tried asking her about that whole butterfly thing earlier... "
                " But she just ignored your question and acted clueless. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
    elif yinhuilv >= 10 or yangyilv >= 10:
        " Well, this was a hard choice. "
        " You wanted to pair up with one of the twins, but they already seemed paired with eachother. "
        " Huh...the more you thought about it, the more you didn't want to disturb them. "
        " You decided to pair with no one, you're just going to do this yourself. "
        " You get some paper and coloring materials, and started drawing... "
        scene black with dissolve
        " You did the activity Altrix gave you all by yourself. "
        " Your poster was pretty decent, not too bad but not too good. "
        " Just decent. "
        " You then passed your work to Mister Altrix and waited for class hours to be over. "
        " Mister Altrix allowed you to use your phone since you were done. "
        " Annnnd you spend the rest of class hours scrolling on your phone. Amazing use of time. "
        play sound "audio/bellring.mp3"
        " The bell rings after a few minutes of scrolling. "
        " You get up from your seat and you walked back into the hallways. "
        " Time to go and get a break. "
        pause 2.0
        jump wedocbreak2
    elif noxlv >= 10 or noxlv == 10:
        " You decided to pair up with Nox. "
        " You walked up to him and asked him if he had a partner or not. "
        show noxneutral at center with easeinright
        n " ...H...huh...? "
        n " You want to...*yawn*...partner up with me...? "
        n " I'm not really sure about that... "
        n " You know...I keep on sleeping every now and then... "
        n " I worry that I might...make you do all of the work... "
        n " Is that really okay with you...? "
        menu:
            " Anything for you ":
                $ noxlv += 10
                hide noxneutral at bottom
                show noxhappy at center
                n " ...You're...too kind... "
                n " *yawn*...I'm feeling too sleepy right now... "
                n " Are you sure that you're okay with...doing all the work...? "
                n " I don't want to feel like I'm being lazy or anything... "
                n " But I can't really...control my sleepiness... "
                hide noxhappy at bottom
                show noxsleepy at center
                n " I'm sorry if this bothers you or anything... "
                n " Real sorry, again... "
                n " ...*Yawn...* "
                " And with that, Nox falls asleep on the desk. "
                " You're going to have to be the one doing the work for this project. "
                " Not like you minded, anyway. "
                " Time to get to work... "
                scene black with dissolve
                " You were the one who did the work for the project. "
                " Every single thing. Nox DID wake up every now and then, but he immediately fell asleep right after. "
                " Before he could fall asleep, he would try to do something, but then...you know what happens. "
                " After you were done passing your work, you made sure that Nox had a nice time taking his nap. "
                " Everytime someone would come up and ask him a question, you would just tell them that Nox needs rest. "
                " What a good friend you were! "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for a break. "
                " The bell ringing also woke Nox up due to how loud it was. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
            " *Say nothing* ":
                hide noxneutral at bottom
                show noxsleepy at center
                " Before you could say anything, Nox immediately falls asleep. "
                " You're going to have to be the one doing the work for this project. "
                " Not like you minded, anyway. "
                " Time to get to work... "
                scene black with dissolve
                " You were the one who did the work for the project. "
                " Every single thing. Nox DID wake up every now and then, but he immediately fell asleep right after. "
                " Before he could fall asleep, he would try to do something, but then...you know what happens. "
                " After you were done passing your work, you made sure that Nox had a nice time taking his nap. "
                " Everytime someone would come up and ask him a question, you would just tell them that Nox needs rest. "
                " What a good friend you were! "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for a break. "
                " The bell ringing also woke Nox up due to how loud it was. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
    elif koalv >= 10 or koalv == 10:
        " You decided to pair up with Koa. "
        " You walked up to him and asked him if he had a partner or not. "
        show koaneutral at center with easeinleft
        k " ...? You want to partner up with me? "
        k " Well, if you really want to, then I suppose I don't mind... "
        k " How about you look for an idea for our poster online... "
        k " ...And I'll get our materials? That sound good? "
        " You gave him a thumbs up and started looking on your phone for ideas. "
        " Luckily you had enough data so that you could browse the internet. "
        k " Alright. I'll go and get our materials then. "
        hide koaneutral at right with easeoutright
        pause 1.0
        show koaneutral at center with easeinright
        k " I've got everything we needed. "
        " He places everything you guys needed down onto the desk. "
        " You showed him the inspiration you two were going to use on your phone. "
        " It was well designed, and also informational on why you should have a healthy lifestyle. "
        " Very eye catching, and also informational. A good mix of both. "
        " The problem is if someone has also gotten this idea and they've already started drawing. "
        k " Hmmm...this one's good... "
        k " We'll be using this, then. "
        k " How about we go from top to bottom on drawing and coloring the thing? "
        k " Ah, er...or, I do the top part and you do the bottom part. "
        k " I think it would be a little bit easier that way. "
        k " If you do get finished first with your part, you can just lend me the colors you used. "
        k " So that I can finish my part, of course. "
        k " Does that sound good to you? "
        " You nodded, before you started to work on your part of the drawing. "
        " Koa looks pretty concentrated...you wanna say something to mess with him? "
        menu:
            " You're pretty cute when you're concentrated ":
                $ koalv += 10
                hide koaneutral at bottom
                show koasurprised at center
                " WOAH WOAH WOAH!! "
                " You realize what you're saying here, right? "
                " Not that this is the bad option, but still WOAH. "
                " Too bad this isn't a dating sim or anything. "
                " Let me just change how Koa reacts to this... "
                k " ...??? "
                k " Oh, uh... "
                hide koasurprised at bottom
                show koahappy at center
                k " ...Thank you, [name]. "
                k " I appreciate that... "
                k " ...I think that you're pretty cute too. "
                " Aww. Of course this is just going to be something platonic. "
                " School first, kids! "
                scene black with dissolve
                " You and Koa got finished on the poster pretty quickly. "
                " You passed the work to Mister Altrix, finally getting some time to relax... "
                " While you were relaxing, you decided to talk with Koa. "
                " Koa seemed comfortable with your prescence. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
            " *Say nothing* ":
                k " ... "
                scene black with dissolve
                " You and Koa got finished on the poster pretty quickly. "
                " You passed the work to Mister Altrix, finally getting some time to relax... "
                " While you were relaxing, you decided to talk with Koa. "
                " Koa seemed comfortable with your prescence. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
    elif carmenlv >= 20 or carmenlv == 20:
        " You decided to pair up with Carmen. "
        " You walked up to him and asked him if he had a partner or not. "
        show carmenneutral at center with easeinright
        ca " ...? "
        " Carmen shakes his head no, meaning that he doesn't have a partner yet. "
        " Though, he would love to have you as his partner! "
        ca " ... "
        " Carmen scratches his head a bit, he doesn't exactly know how to communicate with you. "
        " I mean, he's seen you understand him through his guitar skills, and you've understod him through sign language... "
        " ...Guess he's not really sure of what to do right now. "
        " He decided to speak to you through sign language, don't worry, I'll translate. "
        ca " ...? "
        " Carmen told you that he's going to get some materials for the both of you. "
        " He also told you that you should look for some inspirations online. "
        " You nodded and gave him a thumbs up. He then went away to get the materials... "
        hide carmenneutral at left with easeoutleft
        pause 1.0
        show carmenneutral at center with easeinleft
        ca " ...!! "
        " He came back with the materials that you two needed. "
        " You then showed him a picture of the inspiration you liked. "
        " It was pretty information, and eye catching. "
        " Very nice combo. "
        " Carmen gives a thumbs up of approval! "
        " He then told you to do the left side of the poster, and that he'll do the right side of the poster. "
        hide carmenneutral at bottom
        show carmensad at center
        " He asked you if it's okay with you. Though he's starting to think that he's bothering you with all of this sign language he's throwing at you... "
        menu:
            " You're not bothering me at all, and it's okay with me ":
                $ carmenlv += 10
                hide carmensad at bottom
                show carmenhappy at center
                ca " ..!! "
                " Carmen seems really happy with what you just said. "
                " He looked like he didn't know how to describe what he feels right now, so... "
                " He decided to pat you on the head. It felt nice. "
                hide carmenhappy at bottom
                show carmenneutral at center
                ca " ... "
                " Carmen thinks that it's time to focus on the project now though. "
                " And that's what you two did, focus on the project. "
                scene black with dissolve
                " You and Carmen got finished with the poster pretty quickly. "
                " You then passed the work to Mister Altrix. "
                " You've now got some time to spend with Carmen. "
                " And you spend that time listening to Carmen's sick beats. "
                " Sick beats as in him playing the guitar. "
                " Very sick beats. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
            " Just tell him that it's fine ":
                hide carmensad at bottom
                show carmenneutral at center
                " Carmen seems relieved. "
                " He decided to pat you on the head. It felt nice. "
                ca " ... "
                " Carmen thinks that it's time to focus on the project now though. "
                " And that's what you two did, focus on the project. "
                scene black with dissolve
                " You and Carmen got finished with the poster pretty quickly. "
                " You then passed the work to Mister Altrix. "
                " You've now got some time to spend with Carmen. "
                " And you spend that time listening to Carmen's sick beats. "
                " Sick beats as in him playing the guitar. "
                " Very sick beats. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
    elif jacoblv >= 10 or jacoblv == 10:
        " You decided to pair up with Jacob. "
        " You walked up to him and asked him if he had a partner or not. "
        show jacobneutral at center with easeinright
        jac " ...You want to pair up with ME?! "
        jac " Look, are you really sure? "
        jac " I was actually planning to do nothing for this project, but I guess.. "
        jac " ...Fineee, let's do it. Since you really want to. "
        jac " I'll go and get the materials we need. "
        jac " Stay RIGHT here. And also search up some inspirations on google. "
        hide jacobneutral at left with easeoutleft
        pause 2.0
        show jacobneutral at center with easeinleft
        jac " There. I've got everything we need. "
        " Jacob puts everything you guys needed down on the desk. "
        " He got back here pretty fast... "
        " You then showed him the idea that you liked on google. "
        " He takes a long and good look at it, to make sure if it was really worth it... "
        " Eventually, he nodded and he gave a thumbs up of approval. "
        jac " This will do. "
        jac " Not the best, but it'll do. "
        jac " Let's do the lineart first before anything. "
        " You nodded and started getting to work. "
        " You wanted to say something to catch him offguard... "
        menu:
            " I like your hair style dude ":
                $ jacoblv += 10
                hide jacobneutral at bottom
                show jacobhappy at center
                jac " Uh...thanks? "
                jac " I'm glad that you like my hair, I guess. "
                jac " No one really compliments me. "
                jac " Not for my hair, not for anything. "
                jac " I guess your hair looks pretty okay, too. "
                jac " ...Thanks for the compliment, again. "
                hide jacobhappy at bottom
                show jacobneutral at center
                jac " But we should REALLY get back to focusing on the project. "
                jac " Don't want to get too distracted now. "
                scene black with dissolve
                " You eventually finish the poster with Jacob. "
                " You passed the work to Mister Altrix, finally getting some time to relax. "
                " You then spent the rest of class hours hanging out with Jacob. "
                " Jacob didn't seem to mind your prescence. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
            " *Say nothing, keep working* ":
                jac " ... "
                " Jacob stays silent. "
                scene black with dissolve
                " You eventually finish the poster with Jacob. "
                " You passed the work to Mister Altrix, finally getting some time to relax. "
                " You then spent the rest of class hours hanging out with Jacob. "
                " Jacob didn't seem to mind your prescence. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
    elif orchidlv >= 10 or orchidlv == 10:
        " You decided to pair up with Orchid. "
        " You walked up to them and asked them if they had a partner or not. "
        show orchidneutral at center with easeinleft
        oc " Uh? you want to partner up with me? "
        oc " Um...sure, I guess! I usually pair up with Koa, but... "
        oc " I think he'll be happy to know that I've been making new friends. "
        oc " Anyway...I should get our materials for us! "
        oc " Maybe you could go and look for some ideas for us? "
        oc " Online, of course! I don't want you to go around and steal ideas... "
        oc " Stay right here, okay? "
        hide orchidneutral at right with easeoutright
        pause 1.0
        show orchidneutral at center with easeinright
        oc " I'm baaaack!! "
        oc " Here's the stuff that we need... "
        " Orchid puts down the items you guys needed for the project down on the desk. "
        " They think for a bit before looking at your phone, which had all of the ideas. "
        oc " Oooh, maybe we could do this one! "
        oc " Or maybe we could do this one? It's informational, and... "
        oc " Oohoooo...but this one's good too! "
        oc " God, I can't decide... "
        hide orchidneutral at bottom
        show orchidsad at center
        oc " Guh...I'm so sorry, I'm probably bothering you, aren't I... "
        oc " I should really learn to talk less... "
        menu:
            " No, it's okay - we can go through the ideas and see which ones we like the most ":
                $ orchidlv += 10
                hide orchidsad at bottom
                show orchidhappy at center
                oc " ...Really? You're not annoyed? "
                oc " Thank god... "
                oc " And also, that's a good idea! "
                oc " Hm...I just had another idea, actually! "
                oc " What if we combine all of the ideas and just...make it look good? "
                oc " It shouldn't be that hard, right? "
                hide orchidhappy at bottom
                show orchidneutral at center
                oc " You can take this side, and I can take that side! "
                oc " Sounds pretty good, doesn't it? "
                " You nodded. You then started to get to work on the poster... "
                scene black with dissolve
                " Eventually you got finished working on the poster with Orchid. "
                " You two passed the work to Mister Altrix, and had some time to relax. "
                " You spent the rest of class hours talking to Orchid. "
                " He was surprised that you would talk to someone like him, but he didn't mind. "
                " Infact, they loved your company. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
            " Nah, you're good ":
                hide orchidsad at bottom
                show orchidneutral at center
                oc " Thank god... "
                oc " And also, that's a good idea! "
                oc " Hm...I just had another idea, actually! "
                oc " What if we combine all of the ideas and just...make it look good? "
                oc " It shouldn't be that hard, right? "
                oc " You can take this side, and I can take that side! "
                oc " Sounds pretty good, doesn't it? "
                " You nodded. You then started to get to work on the poster... "
                scene black with dissolve
                " Eventually you got finished working on the poster with Orchid. "
                " You two passed the work to Mister Altrix, and had some time to relax. "
                " You spent the rest of class hours talking to Orchid. "
                " He was surprised that you would talk to someone like him, but he didn't mind. "
                " Infact, they loved your company. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You walked out of your classroom and went back into the hallways. "
                pause 2.0
                jump wedocbreak2
    else:
        " You decided to pair with no one, you're just going to do this yourself. "
        " You get some paper and coloring materials, and started drawing... "
        scene black with dissolve
        " You did the activity Altrix gave you all by yourself. "
        " Your poster was pretty decent, not too bad but not too good. "
        " Just decent. "
        " You then passed your work to Mister Altrix and waited for class hours to be over. "
        " Mister Altrix allowed you to use your phone since you were done. "
        " Annnnd you spend the rest of class hours scrolling on your phone. Amazing use of time. "
        play sound "audio/bellring.mp3"
        " The bell rings after a few minutes of scrolling. "
        " You get up from your seat and you walked back into the hallways. "
        " Time to go and get a break. "
        pause 2.0
        jump wedocbreak2

label wedocbreak2:
    scene hallway with dissolve
    " You walked into the hallway, wondering where you should go... "
    " Where do you go for this break? "
    menu:
        " {image=orchidicon} The front of the school {image=temeroicon} ":
            jump frontschoolwed2
        " {image=quinnicon} The back of the school {image=diskicon} ":
            jump backschoolwed2
        " {image=matteicon} The gym {image=noxicon} ":
            jump gymwed2
        " {image=jacobicon} The cafeteria {image=carmenicon} ":
            jump cafeteriawed2
        " {image=sparkicon} The rooftop {image=jamicon} ":
            jump rooftopwed2
        " {image=koaicon} The library {image=yinyangicon} ":
            jump librarywed2

label frontschoolwed2:
    # orchid and temero
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school and spotted two of your classmates hanging out. "
    " You wanted to know what they were talking about, so you walked over to them to join in on the conversation. "
    show orchidsad at left with easeinright
    show temeroneutral at right with easeinright
    if orchidknow == True and temeroknow == True:
        tm " This could be the one product that could save your life! "
        tm " All you have to do... "
        tm " ...Is buy it, of course! "
        tm " Actually, I haven't tested it out yet. "
        tm " Would you do the honors of testing it, oh great customer - Orchid? "
        oc " ...I'm sorry, but uh... "
        oc " I gotta go, Temero. "
        oc " As much as I would love to test your product... "
        oc " I don't think you can fix the things I'm going through so easily, you know? "
        oc " Maybe you could try making some other products...like perfume? "
        oc " Uh, yeah. I definitely have to go. "
        oc " Koa must be wondering where I am... "
        oc " I'll see you in a bit!! Sorry again!! "
        hide orchidsad at right with easeoutright
        hide temeroneutral at bottom
        show temeroangry at right
        show temeroangry at center with move
        tm " ...Well great. This is just going SOOOO fantastic right now. "
        menu:
            " Stay with this girl ":
                $ temerolv += 10
                tm " Oh, you're gonna stay with me now, huh? "
                tm " Not that I don't mind, but... "
                tm " I think I just need some space for now. "
                tm " I appreciate that you'd want to stay with me though. "
                " You hope that she gets better soon. "
                tm " Yeah. Soon. "
                tm " (Mister Clio isn't going to be happy about this...) "
                " You were about to question what she meant by that, but she ran away. "
                " ...Maybe you could ask her another time. "
                scene black with dissolve
                " You spent the rest of the break hanging out at the front of the school. "
                " You just kind of...stared into the void for a bit. "
                " You really didn't have anything better to do. Especially after what happened. "
                " Maybe you could figure this out... "
                play sound "audio/bellring.mp3"
                " The bell rings at some point of your staring into the void. "
                " You snap out of it, and walked to the gym so that you could go to the next class."
                jump peclassoc1
            " Go to the other person ":
                $ orchidlv += 10
                " You decided to go to the other person to see what they're up to. "
                scene black with dissolve
                pause 1.0
                scene hallway with dissolve
                show orchidsad at center with easeinright
                oc " ...Oh, uh. It's you. "
                oc " It's nice to see you, really...it's just that... "
                oc " That conversation with that girl earlier really threw me off. "
                oc " I know that she went well and all, but... "
                oc " She mentioned something that she shouldn't have known. "
                oc " I don't know if I've told you about what I'm going through, but... "
                oc " She mentioned fixing one of my most uncomfortable issues. "
                oc " Just by buying her product... "
                oc " First she mentions my issues, then she tries to sell her product? "
                oc " That's shady to a whole 'nother level! "
                oc " You think I would just fall for that? Besides... "
                oc " ...I don't think my issues can be resolved that easily anyway. "
                oc " And also, she kinda scares me a little. "
                oc " I've heard some rumors of her being a {b}demon{/b}, but I doubt that it's true. "
                oc " Probably just the other people trying to scare me and others... "
                oc " ...Not a nice thing to do, man. "
                hide orchidsad at bottom
                show orchidneutral at center
                oc " ...Uhm, hey. "
                oc " I'd just like to thank you for listening to me talk for a bit. "
                oc " Even if we don't know eachother that much. "
                oc " If you want to...maybe we could continue talking? "
                oc " We still have some time to just yap to eachother. "
                oc " You can talk to me as much as you want, I don't mind at all! "
                scene black with dissolve
                " You spent the rest of the break talking with Orchid. "
                " They seemed much more happier talking with you than being with Temero. "
                " You can't help but wonder what was going on in Temero's head when she was doing that though... "
                " Maybe you could figure out her plans like a detective. "
                play sound "audio/bellring.mp3"
                " The bell rings at some point into your conversation with Orchid. "
                " You and Orchid then walked to the gym so that you could go to the next class."
                jump peclassoc1
    elif orchidknow == True and temeroknow == False:
        x " This could be the one product that could save your life! "
        x " All you have to do... "
        x " ...Is buy it, of course! "
        x " Actually, I haven't tested it out yet. "
        x " Would you do the honors of testing it, oh great customer - Orchid? "
        oc " ...I'm sorry, but uh... "
        $ temeroknow = True
        oc " I gotta go, Temero. "
        oc " As much as I would love to test your product... "
        oc " I don't think you can fix the things I'm going through so easily, you know? "
        oc " Maybe you could try making some other products...like perfume? "
        oc " Uh, yeah. I definitely have to go. "
        oc " Koa must be wondering where I am... "
        oc " I'll see you in a bit!! Sorry again!! "
        hide orchidsad at right with easeoutright
        hide temeroneutral at bottom
        show temeroangry at right
        show temeroangry at center with move
        tm " ...Well great. This is just going SOOOO fantastic right now. "
        menu:
            " Stay with this girl ":
                $ temerolv += 10
                tm " Oh, you're gonna stay with me now, huh? "
                tm " Not that I don't mind, but... "
                tm " I think I just need some space for now. "
                tm " I appreciate that you'd want to stay with me though. "
                " You hope that she gets better soon. "
                tm " Yeah. Soon. "
                tm " (Mister Clio isn't going to be happy about this...) "
                " You were about to question what she meant by that, but she ran away. "
                " ...Maybe you could ask her another time. "
                scene black with dissolve
                " You spent the rest of the break hanging out at the front of the school. "
                " You just kind of...stared into the void for a bit. "
                " You really didn't have anything better to do. Especially after what happened. "
                " Maybe you could figure this out... "
                play sound "audio/bellring.mp3"
                " The bell rings at some point of your staring into the void. "
                " You snap out of it, and walked to the gym so that you could go to the next class."
                jump peclassoc1
            " Go to the other person ":
                $ orchidlv += 10
                " You decided to go to the other person to see what they're up to. "
                scene black with dissolve
                pause 1.0
                scene hallway with dissolve
                show orchidsad at center with easeinright
                oc " ...Oh, uh. It's you. "
                oc " It's nice to see you, really...it's just that... "
                oc " That conversation with that girl earlier really threw me off. "
                oc " I know that she went well and all, but... "
                oc " She mentioned something that she shouldn't have known. "
                oc " I don't know if I've told you about what I'm going through, but... "
                oc " She mentioned fixing one of my most uncomfortable issues. "
                oc " Just by buying her product... "
                oc " First she mentions my issues, then she tries to sell her product? "
                oc " That's shady to a whole 'nother level! "
                oc " You think I would just fall for that? Besides... "
                oc " ...I don't think my issues can be resolved that easily anyway. "
                oc " And also, she kinda scares me a little. "
                oc " I've heard some rumors of her being a {b}demon{/b}, but I doubt that it's true. "
                oc " Probably just the other people trying to scare me and others... "
                oc " ...Not a nice thing to do, man. "
                hide orchidsad at bottom
                show orchidneutral at center
                oc " ...Uhm, hey. "
                oc " I'd just like to thank you for listening to me talk for a bit. "
                oc " Even if we don't know eachother that much. "
                oc " If you want to...maybe we could continue talking? "
                oc " We still have some time to just yap to eachother. "
                oc " You can talk to me as much as you want, I don't mind at all! "
                scene black with dissolve
                " You spent the rest of the break talking with Orchid. "
                " They seemed much more happier talking with you than being with Temero. "
                " You can't help but wonder what was going on in Temero's head when she was doing that though... "
                " Maybe you could figure out her plans like a detective. "
                play sound "audio/bellring.mp3"
                " The bell rings at some point into your conversation with Orchid. "
                " You and Orchid then walked to the gym so that you could go to the next class."
                jump peclassoc1
    elif orchidknow == False and temeroknow == True:
        tm " This could be the one product that could save your life! "
        tm " All you have to do... "
        tm " ...Is buy it, of course! "
        tm " Actually, I haven't tested it out yet. "
        $ orchidknow = True
        tm " Would you do the honors of testing it, oh great customer - Orchid? "
        oc " ...I'm sorry, but uh... "
        oc " I gotta go, Temero. "
        oc " As much as I would love to test your product... "
        oc " I don't think you can fix the things I'm going through so easily, you know? "
        oc " Maybe you could try making some other products...like perfume? "
        oc " Uh, yeah. I definitely have to go. "
        oc " Koa must be wondering where I am... "
        oc " I'll see you in a bit!! Sorry again!! "
        hide orchidsad at right with easeoutright
        hide temeroneutral at bottom
        show temeroangry at right
        show temeroangry at center with move
        tm " ...Well great. This is just going SOOOO fantastic right now. "
        menu:
            " Stay with this girl ":
                $ temerolv += 10
                tm " Oh, you're gonna stay with me now, huh? "
                tm " Not that I don't mind, but... "
                tm " I think I just need some space for now. "
                tm " I appreciate that you'd want to stay with me though. "
                " You hope that she gets better soon. "
                tm " Yeah. Soon. "
                tm " (Mister Clio isn't going to be happy about this...) "
                " You were about to question what she meant by that, but she ran away. "
                " ...Maybe you could ask her another time. "
                scene black with dissolve
                " You spent the rest of the break hanging out at the front of the school. "
                " You just kind of...stared into the void for a bit. "
                " You really didn't have anything better to do. Especially after what happened. "
                " Maybe you could figure this out... "
                play sound "audio/bellring.mp3"
                " The bell rings at some point of your staring into the void. "
                " You snap out of it, and walked to the gym so that you could go to the next class."
                jump peclassoc1
            " Go to the other person ":
                $ orchidlv += 10
                " You decided to go to the other person to see what they're up to. "
                scene black with dissolve
                pause 1.0
                scene hallway with dissolve
                show orchidsad at center with easeinright
                oc " ...Oh, uh. It's you. "
                oc " It's nice to see you, really...it's just that... "
                oc " That conversation with that girl earlier really threw me off. "
                oc " I know that she went well and all, but... "
                oc " She mentioned something that she shouldn't have known. "
                oc " I don't know if I've told you about what I'm going through, but... "
                oc " She mentioned fixing one of my most uncomfortable issues. "
                oc " Just by buying her product... "
                oc " First she mentions my issues, then she tries to sell her product? "
                oc " That's shady to a whole 'nother level! "
                oc " You think I would just fall for that? Besides... "
                oc " ...I don't think my issues can be resolved that easily anyway. "
                oc " And also, she kinda scares me a little. "
                oc " I've heard some rumors of her being a {b}demon{/b}, but I doubt that it's true. "
                oc " Probably just the other people trying to scare me and others... "
                oc " ...Not a nice thing to do, man. "
                hide orchidsad at bottom
                show orchidneutral at center
                oc " ...Uhm, hey. "
                oc " I'd just like to thank you for listening to me talk for a bit. "
                oc " Even if we don't know eachother that much. "
                oc " If you want to...maybe we could continue talking? "
                oc " We still have some time to just yap to eachother. "
                oc " You can talk to me as much as you want, I don't mind at all! "
                scene black with dissolve
                " You spent the rest of the break talking with Orchid. "
                " They seemed much more happier talking with you than being with Temero. "
                " You can't help but wonder what was going on in Temero's head when she was doing that though... "
                " Maybe you could figure out her plans like a detective. "
                play sound "audio/bellring.mp3"
                " The bell rings at some point into your conversation with Orchid. "
                " You and Orchid then walked to the gym so that you could go to the next class."
                jump peclassoc1
    else:
        x " This could be the one product that could save your life! "
        x " All you have to do... "
        x " ...Is buy it, of course! "
        x " Actually, I haven't tested it out yet. "
        x " Would you do the honors of testing it, oh great customer - Orchid? "
        $ orchidknow = True
        oc " ...I'm sorry, but uh... "
        $ temeroknow = True
        oc " I gotta go, Temero. "
        oc " As much as I would love to test your product... "
        oc " I don't think you can fix the things I'm going through so easily, you know? "
        oc " Maybe you could try making some other products...like perfume? "
        oc " Uh, yeah. I definitely have to go. "
        oc " Koa must be wondering where I am... "
        oc " I'll see you in a bit!! Sorry again!! "
        hide orchidsad at right with easeoutright
        hide temeroneutral at bottom
        show temeroangry at right
        show temeroangry at center with move
        tm " ...Well great. This is just going SOOOO fantastic right now. "
        menu:
            " Stay with this girl ":
                $ temerolv += 10
                tm " Oh, you're gonna stay with me now, huh? "
                tm " Not that I don't mind, but... "
                tm " I think I just need some space for now. "
                tm " I appreciate that you'd want to stay with me though. "
                " You hope that she gets better soon. "
                tm " Yeah. Soon. "
                tm " (Mister Clio isn't going to be happy about this...) "
                " You were about to question what she meant by that, but she ran away. "
                " ...Maybe you could ask her another time. "
                scene black with dissolve
                " You spent the rest of the break hanging out at the front of the school. "
                " You just kind of...stared into the void for a bit. "
                " You really didn't have anything better to do. Especially after what happened. "
                " Maybe you could figure this out... "
                play sound "audio/bellring.mp3"
                " The bell rings at some point of your staring into the void. "
                " You snap out of it, and walked to the gym so that you could go to the next class."
                jump peclassoc1
            " Go to the other person ":
                $ orchidlv += 10
                " You decided to go to the other person to see what they're up to. "
                scene black with dissolve
                pause 1.0
                scene hallway with dissolve
                show orchidsad at center with easeinright
                oc " ...Oh, uh. It's you. "
                oc " It's nice to see you, really...it's just that... "
                oc " That conversation with that girl earlier really threw me off. "
                oc " I know that she went well and all, but... "
                oc " She mentioned something that she shouldn't have known. "
                oc " I don't know if I've told you about what I'm going through, but... "
                oc " She mentioned fixing one of my most uncomfortable issues. "
                oc " Just by buying her product... "
                oc " First she mentions my issues, then she tries to sell her product? "
                oc " That's shady to a whole 'nother level! "
                oc " You think I would just fall for that? Besides... "
                oc " ...I don't think my issues can be resolved that easily anyway. "
                oc " And also, she kinda scares me a little. "
                oc " I've heard some rumors of her being a {b}demon{/b}, but I doubt that it's true. "
                oc " Probably just the other people trying to scare me and others... "
                oc " ...Not a nice thing to do, man. "
                hide orchidsad at bottom
                show orchidneutral at center
                oc " ...Uhm, hey. "
                oc " I'd just like to thank you for listening to me talk for a bit. "
                oc " Even if we don't know eachother that much. "
                oc " If you want to...maybe we could continue talking? "
                oc " We still have some time to just yap to eachother. "
                oc " You can talk to me as much as you want, I don't mind at all! "
                scene black with dissolve
                " You spent the rest of the break talking with Orchid. "
                " They seemed much more happier talking with you than being with Temero. "
                " You can't help but wonder what was going on in Temero's head when she was doing that though... "
                " Maybe you could figure out her plans like a detective. "
                play sound "audio/bellring.mp3"
                " The bell rings at some point into your conversation with Orchid. "
                " You and Orchid then walked to the gym so that you could go to the next class."
                jump peclassoc1
label backschoolwed2:
    # quinn and disk
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and spotted one of your classmates taking a photo of another one of your classmates. "
    " What they're doing seems interesting...let's see if you could join or not. "
    show quinnneutral at right with easeinleft
    show diskneutral at left with easeinleft
    if quinnknow == True and diskknow == True:
        q " How about there, Disk? "
        q " I've got to make sure my big brother looks good in the lighting. "
        q " Well, you always look good...but you'd look even better if we got the right angle. "
        d " Dude, come ooonnn... "
        d " I'm not even as pretty as mom! "
        q " Hey, don't you already know that we don't take shittalk about ourselves in OUR family? "
        d " I know, I know! "
        d " But in my opinion, she's the pretty one. "
        d " And me? I'm...handsome! "
        q " Mhm, that's right. "
        q " Just a few more photos, aaaaand... "
        " It took a bit for the one taking the photos to notice you. "
        " But, he eventually does after taking one more photo of the other guy. "
        " The other guy seems to notice you too. "
        hide diskneutral at bottom
        show diskhappy at left
        d " [name]!!! It's so nice to see you!! "
        hide quinnneutral at bottom
        show quinnhappy at right
        q " Hey there. "
        q " I just needed to take some pictures for big bro because mom asked for some. "
        hide quinnhappy at bottom
        hide diskhappy at bottom
        show diskneutral at left
        show quinnneutral at right
        q " You see, our mom's this really popular and successful model... "
        q " ...And she made this decision to mention us and show her our pictures. "
        q " Obviously I didn't want to show off my brother's more...goofier pictures... "
        d " So we decided to take new and impressive ones instead! "
        d " Though I do worry that her fans will ask some weird questions about us, she insisted! "
        d " ...And also told me that our dad and our bodyguards will just kick out creeps. "
        d " We've actually got some pretty S tier body guards to protect us, and plus, our dad's very strong... "
        q " So we wouldn't have to worry about someone coming in uninvited. "
        menu:
            " Could I be in a picture? ":
                $ disklv += 10
                $ quinnlv += 10
                hide quinnneutral at bottom
                show quinnhappy at right
                q " While we would love for you to be in there, our mom asked for specifically us. "
                d " Don't worry though! We can still hang out and take selfies together! "
                q " Mhm. If we do ask our mom about you being a picture, the least you're going to get is a special mention. "
                q " She's just going to have to say that she's made some great friends. And you really are a great one, that's for sure. "
                d " Uh huh! Actually, hold on... "
                d " How about we let [name] take a picture of us? "
                d " We've only been doing solo photos so far! "
                q " Ah, sure. "
                q " Here [name], the camera. "
                " You took a few photos for the brothers. "
                " Damn, you didn't know Disk and Quinn were THAAAAT rich. "
                " You feel extra poor being in their prescence. "
                scene black with dissolve
                " After you got done taking photos for Disk and Quinn, you got to hang out with them for a bit. "
                " Hell, they somehow managed to get the cafeteria ladies to give you three icecream. "
                " You kept on insisting that you're going to be fine, but they were more persistent than you. "
                " ...And they bought you a whole lot of snacks at the cafeteria. "
                " You're starting to feel just a bit guilty for making them waste their money on you. "
                " They told you not to worry because their weekly allowance was 1k$...WHAT. "
                " AND THEY SAID IT AS IF IT WAS NORMAL. "
                " I mean, they DO live the rich kid life, so that's the norm for them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, time for your next class. "
                " You three made it all the way to the gym and got prepared for a fun class. "
                pause 2.0
                jump peclassoc1
            " wow I feel poor now ":
                $ disklv += 5
                $ quinnlv +=5
                q " Hey, don't feel like that... "
                q " Otherwise Disk is gonna start giving you money every day. "
                d " ...I totally wasn't thinking about that... "
                d " But, yeah! "
                d " I don't want to end up like how my old school ended up... "
                d " People asking me for money daily...eeyikes! "
                d " Anyway, Quinn... how about we let [name] take a picture of us? "
                d " We've only been doing solo photos so far! "
                q " Ah, sure. "
                q " Here [name], the camera. "
                " You took a few photos for the brothers. "
                " Damn, you didn't know Disk and Quinn were THAAAAT rich. "
                " You feel extra poor being in their prescence. "
                scene black with dissolve
                " After you got done taking photos for Disk and Quinn, you got to hang out with them for a bit. "
                " Hell, they somehow managed to get the cafeteria ladies to give you three icecream. "
                " You kept on insisting that you're going to be fine, but they were more persistent than you. "
                " ...And they bought you a whole lot of snacks at the cafeteria. "
                " You're starting to feel just a bit guilty for making them waste their money on you. "
                " They told you not to worry because their weekly allowance was 1k$...WHAT. "
                " AND THEY SAID IT AS IF IT WAS NORMAL. "
                " I mean, they DO live the rich kid life, so that's the norm for them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, time for your next class. "
                " You three made it all the way to the gym and got prepared for a fun class. "
                pause 2.0
                jump peclassoc1
    elif quinnknow == True and diskknow == False:
        q " How about there, Disk? "
        q " I've got to make sure my big brother looks good in the lighting. "
        q " Well, you always look good...but you'd look even better if we got the right angle. "
        x " Dude, come ooonnn... "
        x " I'm not even as pretty as mom! "
        q " Hey, don't you already know that we don't take shittalk about ourselves in OUR family? "
        x " I know, I know! "
        x " But in my opinion, she's the pretty one. "
        x " And me? I'm...handsome! "
        x " Mhm, that's right. "
        q " Just a few more photos, aaaaand... "
        " It took a bit for the one taking the photos to notice you. "
        " But, he eventually does after taking one more photo of the other guy. "
        " The other guy seems to notice you too. "
        hide diskneutral at bottom
        show diskhappy at left
        x " [name]!!! It's so nice to see you!! "
        $ diskknow = True
        d " I'm Disk, by the way! Quinn's brother! "
        hide quinnneutral at bottom
        show quinnhappy at right
        q " Hey there. "
        q " I just needed to take some pictures for big bro because mom asked for some. "
        hide quinnhappy at bottom
        hide diskhappy at bottom
        show diskneutral at left
        show quinnneutral at right
        q " You see, our mom's this really popular and successful model... "
        q " ...And she made this decision to mention us and show her our pictures. "
        q " Obviously I didn't want to show off my brother's more...goofier pictures... "
        d " So we decided to take new and impressive ones instead! "
        d " Though I do worry that her fans will ask some weird questions about us, she insisted! "
        d " ...And also told me that our dad and our bodyguards will just kick out creeps. "
        d " We've actually got some pretty S tier body guards to protect us, and plus, our dad's very strong... "
        q " So we wouldn't have to worry about someone coming in uninvited. "
        menu:
            " Could I be in a picture? ":
                $ disklv += 10
                $ quinnlv += 10
                hide quinnneutral at bottom
                show quinnhappy at right
                q " While we would love for you to be in there, our mom asked for specifically us. "
                d " Don't worry though! We can still hang out and take selfies together! "
                q " Mhm. If we do ask our mom about you being a picture, the least you're going to get is a special mention. "
                q " She's just going to have to say that she's made some great friends. And you really are a great one, that's for sure. "
                d " Uh huh! Actually, hold on... "
                d " How about we let [name] take a picture of us? "
                d " We've only been doing solo photos so far! "
                q " Ah, sure. "
                q " Here [name], the camera. "
                " You took a few photos for the brothers. "
                " Damn, you didn't know Disk and Quinn were THAAAAT rich. "
                " You feel extra poor being in their prescence. "
                scene black with dissolve
                " After you got done taking photos for Disk and Quinn, you got to hang out with them for a bit. "
                " Hell, they somehow managed to get the cafeteria ladies to give you three icecream. "
                " You kept on insisting that you're going to be fine, but they were more persistent than you. "
                " ...And they bought you a whole lot of snacks at the cafeteria. "
                " You're starting to feel just a bit guilty for making them waste their money on you. "
                " They told you not to worry because their weekly allowance was 1k$...WHAT. "
                " AND THEY SAID IT AS IF IT WAS NORMAL. "
                " I mean, they DO live the rich kid life, so that's the norm for them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, time for your next class. "
                " You three made it all the way to the gym and got prepared for a fun class. "
                pause 2.0
                jump peclassoc1
            " wow I feel poor now ":
                $ disklv += 5
                $ quinnlv +=5
                q " Hey, don't feel like that... "
                q " Otherwise Disk is gonna start giving you money every day. "
                d " ...I totally wasn't thinking about that... "
                d " But, yeah! "
                d " I don't want to end up like how my old school ended up... "
                d " People asking me for money daily...eeyikes! "
                d " Anyway, Quinn... how about we let [name] take a picture of us? "
                d " We've only been doing solo photos so far! "
                q " Ah, sure. "
                q " Here [name], the camera. "
                " You took a few photos for the brothers. "
                " Damn, you didn't know Disk and Quinn were THAAAAT rich. "
                " You feel extra poor being in their prescence. "
                scene black with dissolve
                " After you got done taking photos for Disk and Quinn, you got to hang out with them for a bit. "
                " Hell, they somehow managed to get the cafeteria ladies to give you three icecream. "
                " You kept on insisting that you're going to be fine, but they were more persistent than you. "
                " ...And they bought you a whole lot of snacks at the cafeteria. "
                " You're starting to feel just a bit guilty for making them waste their money on you. "
                " They told you not to worry because their weekly allowance was 1k$...WHAT. "
                " AND THEY SAID IT AS IF IT WAS NORMAL. "
                " I mean, they DO live the rich kid life, so that's the norm for them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, time for your next class. "
                " You three made it all the way to the gym and got prepared for a fun class. "
                pause 2.0
                jump peclassoc1
    elif quinnknow == False and diskknow == True:
        x " How about there, Disk? "
        x " I've got to make sure my big brother looks good in the lighting. "
        x " Well, you always look good...but you'd look even better if we got the right angle. "
        d " Dude, come ooonnn... "
        d " I'm not even as pretty as mom! "
        x " Hey, don't you already know that we don't take shittalk about ourselves in OUR family? "
        d " I know, I know! "
        d " But in my opinion, she's the pretty one. "
        d " And me? I'm...handsome! "
        x " Mhm, that's right. "
        x " Just a few more photos, aaaaand... "
        " It took a bit for the one taking the photos to notice you. "
        " But, he eventually does after taking one more photo of the other guy. "
        " The other guy seems to notice you too. "
        hide diskneutral at bottom
        show diskhappy at left
        d " [name]!!! It's so nice to see you!! "
        hide quinnneutral at bottom
        show quinnhappy at right
        x " Hey there. "
        $ quinnknow = True
        q " I'm Quinn, Disk's younger brother. "
        q " I just needed to take some pictures for big bro because mom asked for some. "
        hide quinnhappy at bottom
        hide diskhappy at bottom
        show diskneutral at left
        show quinnneutral at right
        q " You see, our mom's this really popular and successful model... "
        q " ...And she made this decision to mention us and show her our pictures. "
        q " Obviously I didn't want to show off my brother's more...goofier pictures... "
        d " So we decided to take new and impressive ones instead! "
        d " Though I do worry that her fans will ask some weird questions about us, she insisted! "
        d " ...And also told me that our dad and our bodyguards will just kick out creeps. "
        d " We've actually got some pretty S tier body guards to protect us, and plus, our dad's very strong... "
        q " So we wouldn't have to worry about someone coming in uninvited. "
        menu:
            " Could I be in a picture? ":
                $ disklv += 10
                $ quinnlv += 10
                hide quinnneutral at bottom
                show quinnhappy at right
                q " While we would love for you to be in there, our mom asked for specifically us. "
                d " Don't worry though! We can still hang out and take selfies together! "
                q " Mhm. If we do ask our mom about you being a picture, the least you're going to get is a special mention. "
                q " She's just going to have to say that she's made some great friends. And you really are a great one, that's for sure. "
                d " Uh huh! Actually, hold on... "
                d " How about we let [name] take a picture of us? "
                d " We've only been doing solo photos so far! "
                q " Ah, sure. "
                q " Here [name], the camera. "
                " You took a few photos for the brothers. "
                " Damn, you didn't know Disk and Quinn were THAAAAT rich. "
                " You feel extra poor being in their prescence. "
                scene black with dissolve
                " After you got done taking photos for Disk and Quinn, you got to hang out with them for a bit. "
                " Hell, they somehow managed to get the cafeteria ladies to give you three icecream. "
                " You kept on insisting that you're going to be fine, but they were more persistent than you. "
                " ...And they bought you a whole lot of snacks at the cafeteria. "
                " You're starting to feel just a bit guilty for making them waste their money on you. "
                " They told you not to worry because their weekly allowance was 1k$...WHAT. "
                " AND THEY SAID IT AS IF IT WAS NORMAL. "
                " I mean, they DO live the rich kid life, so that's the norm for them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, time for your next class. "
                " You three made it all the way to the gym and got prepared for a fun class. "
                pause 2.0
                jump peclassoc1
            " wow I feel poor now ":
                $ disklv += 5
                $ quinnlv +=5
                q " Hey, don't feel like that... "
                q " Otherwise Disk is gonna start giving you money every day. "
                d " ...I totally wasn't thinking about that... "
                d " But, yeah! "
                d " I don't want to end up like how my old school ended up... "
                d " People asking me for money daily...eeyikes! "
                d " Anyway, Quinn... how about we let [name] take a picture of us? "
                d " We've only been doing solo photos so far! "
                q " Ah, sure. "
                q " Here [name], the camera. "
                " You took a few photos for the brothers. "
                " Damn, you didn't know Disk and Quinn were THAAAAT rich. "
                " You feel extra poor being in their prescence. "
                scene black with dissolve
                " After you got done taking photos for Disk and Quinn, you got to hang out with them for a bit. "
                " Hell, they somehow managed to get the cafeteria ladies to give you three icecream. "
                " You kept on insisting that you're going to be fine, but they were more persistent than you. "
                " ...And they bought you a whole lot of snacks at the cafeteria. "
                " You're starting to feel just a bit guilty for making them waste their money on you. "
                " They told you not to worry because their weekly allowance was 1k$...WHAT. "
                " AND THEY SAID IT AS IF IT WAS NORMAL. "
                " I mean, they DO live the rich kid life, so that's the norm for them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, time for your next class. "
                " You three made it all the way to the gym and got prepared for a fun class. "
                pause 2.0
                jump peclassoc1
    else:
        x " How about there, Disk? "
        x " I've got to make sure my big brother looks good in the lighting. "
        x " Well, you always look good...but you'd look even better if we got the right angle. "
        x " Dude, come ooonnn... "
        x " I'm not even as pretty as mom! "
        x " Hey, don't you already know that we don't take shittalk about ourselves in OUR family? "
        x " I know, I know! "
        x " But in my opinion, she's the pretty one. "
        x " And me? I'm...handsome! "
        x " Mhm, that's right. "
        x " Just a few more photos, aaaaand... "
        " It took a bit for the one taking the photos to notice you. "
        " But, he eventually does after taking one more photo of the other guy. "
        " The other guy seems to notice you too. "
        hide diskneutral at bottom
        show diskhappy at left
        x " [name]!!! It's so nice to see you!! "
        $ diskknow = True
        d " I'm Disk, by the way! This little fella's older brother! "
        x " Don't call me a little fella... "
        x " ...Ahem. "
        hide quinnneutral at bottom
        show quinnhappy at right
        x " Hey there. "
        $ quinnknow = True
        q " I'm Quinn, Disk's younger brother. "
        q " I just needed to take some pictures for big bro because mom asked for some. "
        hide quinnhappy at bottom
        hide diskhappy at bottom
        show diskneutral at left
        show quinnneutral at right
        q " You see, our mom's this really popular and successful model... "
        q " ...And she made this decision to mention us and show her our pictures. "
        q " Obviously I didn't want to show off my brother's more...goofier pictures... "
        d " So we decided to take new and impressive ones instead! "
        d " Though I do worry that her fans will ask some weird questions about us, she insisted! "
        d " ...And also told me that our dad and our bodyguards will just kick out creeps. "
        d " We've actually got some pretty S tier body guards to protect us, and plus, our dad's very strong... "
        q " So we wouldn't have to worry about someone coming in uninvited. "
        menu:
            " Could I be in a picture? ":
                $ disklv += 10
                $ quinnlv += 10
                hide quinnneutral at bottom
                show quinnhappy at right
                q " While we would love for you to be in there, our mom asked for specifically us. "
                d " Don't worry though! We can still hang out and take selfies together! "
                q " Mhm. If we do ask our mom about you being a picture, the least you're going to get is a special mention. "
                q " She's just going to have to say that she's made some great friends. And you really are a great one, that's for sure. "
                d " Uh huh! Actually, hold on... "
                d " How about we let [name] take a picture of us? "
                d " We've only been doing solo photos so far! "
                q " Ah, sure. "
                q " Here [name], the camera. "
                " You took a few photos for the brothers. "
                " Damn, you didn't know Disk and Quinn were THAAAAT rich. "
                " You feel extra poor being in their prescence. "
                scene black with dissolve
                " After you got done taking photos for Disk and Quinn, you got to hang out with them for a bit. "
                " Hell, they somehow managed to get the cafeteria ladies to give you three icecream. "
                " You kept on insisting that you're going to be fine, but they were more persistent than you. "
                " ...And they bought you a whole lot of snacks at the cafeteria. "
                " You're starting to feel just a bit guilty for making them waste their money on you. "
                " They told you not to worry because their weekly allowance was 1k$...WHAT. "
                " AND THEY SAID IT AS IF IT WAS NORMAL. "
                " I mean, they DO live the rich kid life, so that's the norm for them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, time for your next class. "
                " You three made it all the way to the gym and got prepared for a fun class. "
                pause 2.0
                jump peclassoc1
            " wow I feel poor now ":
                $ disklv += 5
                $ quinnlv +=5
                q " Hey, don't feel like that... "
                q " Otherwise Disk is gonna start giving you money every day. "
                d " ...I totally wasn't thinking about that... "
                d " But, yeah! "
                d " I don't want to end up like how my old school ended up... "
                d " People asking me for money daily...eeyikes! "
                d " Anyway, Quinn... how about we let [name] take a picture of us? "
                d " We've only been doing solo photos so far! "
                q " Ah, sure. "
                q " Here [name], the camera. "
                " You took a few photos for the brothers. "
                " Damn, you didn't know Disk and Quinn were THAAAAT rich. "
                " You feel extra poor being in their prescence. "
                scene black with dissolve
                " After you got done taking photos for Disk and Quinn, you got to hang out with them for a bit. "
                " Hell, they somehow managed to get the cafeteria ladies to give you three icecream. "
                " You kept on insisting that you're going to be fine, but they were more persistent than you. "
                " ...And they bought you a whole lot of snacks at the cafeteria. "
                " You're starting to feel just a bit guilty for making them waste their money on you. "
                " They told you not to worry because their weekly allowance was 1k$...WHAT. "
                " AND THEY SAID IT AS IF IT WAS NORMAL. "
                " I mean, they DO live the rich kid life, so that's the norm for them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, time for your next class. "
                " You three made it all the way to the gym and got prepared for a fun class. "
                pause 2.0
                jump peclassoc1
label gymwed2:
    # matte and nox
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked to the gym and spotted two of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you want to talk to? "
    if matteknow == True and noxknow == True:
        menu:
            " {image=matteicon} Matte {image=matteicon} ":
                jump macde
            " {image=noxicon} Nox {image=noxicon} ":
                jump willide
    elif matteknow == True and noxknow == False:
        menu:
            " {image=matteicon} Matte {image=matteicon} ":
                jump macde
            " {image=noxicon} A sleepy boy {image=noxicon} ":
                jump willide
    elif matteknow == False and noxknow == True:
        menu:
            " {image=matteicon} An artsy girl {image=matteicon} ":
                jump macde
            " {image=noxicon} Nox {image=noxicon} ":
                jump willide
    else:
        menu:
            " {image=matteicon} An artsy girl {image=matteicon} ":
                jump macde
            " {image=noxicon} A sleepy boy {image=noxicon} ":
                jump willide
    label macde:
        show matteneutral at center with easeinright
        if matteknow == True:
            ma " Hhmhm...what should I do for this break? "
            ma " Surely I can't just spend my time drawing again... "
            ma " Maybe study? but studying's honestly boring... "
            ma " Don't know how my cousins keep up in class while I'm just... "
            ma " ...Drawing on my desk about girls kissing. "
            hide matteneutral at bottom
            show mattesurprised at center
            ma " ...Oh wait, [name]?? You're here?? "
            ma " Hopefully you didn't hear what I just said, haha... "
            hide mattesurprised at bottom
            show mattesad at center
            ma " Girls kissing? Just for a commission, really! "
            ma " Not like I draw it every single day... "
            hide mattesad at bottom
            show matteneutral at center
            ma " ...Ahen. Anyway, did you have something to tell me? "
            ma " Oh, while you're here... "
            ma " Could you give me some things I should do whenever I'm bored? "
            ma " I know very well that most of the time, you'd see me drawing, buuut... "
            ma " There ARE times where I don't want to, you know? "
            ma " Especially whenever art block hits too hard. Like right now! "
            ma " I also can't really talk to my friends - don't want to bother them too much... "
            ma " Sooo, could you give me some ideas on what to do? "
            ma " If you don't mind, of course. "
            ma " It's TOTALLY okay if you don't want to give me any ideas! "
            ma " Though I most likely will end up doomscrolling for the rest of the break. "
            ma " I mean, at least that keeps me distracted??? "
            ma " But I wanna do something else instead of that. "
            " You think for a moment before giving her some ideas. "
            ma " ...Look at nature? Done that countless of times before for art... "
            ma " And yes, I do stop and admire mother nature every now and then. "
            ma " ...Read a book? I've tried reading before, but it isn't really my thing... "
            ma " (Would rather read on OA2, but no one needs to know that...) "
            ma " ...You know what? How about we just scroll on tiktok together... "
            ma " We could also show eachother some interesting videos we can find! "
            " You thought about the idea for a bit... "
            " You didn't really mind the idea since you do that a lot whenever you're not locking into school. "
            " Time to waste your time and scroll on social media! "
            scene black with dissolve
            " You spent the rest of the break scrolling with Matte on tiktok. "
            " You both would keep seeing stuff about some guy driving in his car right after a beer. "
            " ...Must be a new trend. It's real funny, too. "
            " With how somewhat badly animated it is, that's how it got you and Matte to laugh. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " Though you're already in the class area...so you waited on the bleachers until the teacher arrived. "
            pause 2.0
            jump peclassoc1
        else:
            x " Hhmhm...what should I do for this break? "
            x " Surely I can't just spend my time drawing again... "
            x " Maybe study? but studying's honestly boring... "
            x " Don't know how my cousins keep up in class while I'm just... "
            x " ...Drawing on my desk about girls kissing. "
            hide matteneutral at bottom
            show mattesurprised at center
            x " ...Oh wait, [name]?? You're here?? "
            x " Hopefully you didn't hear what I just said, haha... "
            hide mattesurprised at bottom
            show mattesad at center
            x " Girls kissing? Just for a commission, really! "
            x " Not like I draw it every single day... "
            hide mattesad at bottom
            show matteneutral at center
            $ matteknow = True
            ma " I'm Matte, by the way! Almost forgot to introduce myself, heheh... "
            ma " ...Ahen. Anyway, did you have something to tell me? "
            ma " Oh, while you're here... "
            ma " Could you give me some things I should do whenever I'm bored? "
            ma " I know very well that most of the time, you'd see me drawing, buuut... "
            ma " There ARE times where I don't want to, you know? "
            ma " Especially whenever art block hits too hard. Like right now! "
            ma " I also can't really talk to my friends - don't want to bother them too much... "
            ma " Sooo, could you give me some ideas on what to do? "
            ma " If you don't mind, of course. "
            ma " It's TOTALLY okay if you don't want to give me any ideas! "
            ma " Though I most likely will end up doomscrolling for the rest of the break. "
            ma " I mean, at least that keeps me distracted??? "
            ma " But I wanna do something else instead of that. "
            " You think for a moment before giving her some ideas. "
            ma " ...Look at nature? Done that countless of times before for art... "
            ma " And yes, I do stop and admire mother nature every now and then. "
            ma " ...Read a book? I've tried reading before, but it isn't really my thing... "
            ma " (Would rather read on OA2, but no one needs to know that...) "
            ma " ...You know what? How about we just scroll on tiktok together... "
            ma " We could also show eachother some interesting videos we can find! "
            " You thought about the idea for a bit... "
            " You didn't really mind the idea since you do that a lot whenever you're not locking into school. "
            " Time to waste your time and scroll on social media! "
            scene black with dissolve
            " You spent the rest of the break scrolling with Matte on tiktok. "
            " You both would keep seeing stuff about some guy driving in his car right after a beer. "
            " ...Must be a new trend. It's real funny, too. "
            " With how somewhat badly animated it is, that's how it got you and Matte to laugh. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " Though you're already in the class area...so you waited on the bleachers until the teacher arrived. "
            pause 2.0
            jump peclassoc1
    label willide:
        show noxsleepy at center with easeinleft
        if noxknow == True:
            n " Mmmmh...not again... "
            n " I fall asleep way too easily... "
            n " ...Not taking my medicine was a bad idea... "
            " You shook him a tad bit to wake him up a little. "
            hide noxsleepy at bottom
            show noxneutral at center
            " Luckily that worked. "
            " After he woke up a little, you asked him if he was doing alright. "
            n " ...If I'm being honest...*yawn*...no... "
            n " I don't want to bother Mister Altrix again though... "
            n " I'm pretty sleepy, but I'm sure... I can stay up for a bit longer... "
            n " It's not that I stayed up late or anything... "
            n " ...Just a condition that I have... "
            hide noxneutral at bottom
            show noxsleepy at center
            n " Hmhmmm... though I can't really handle this amount of sleepiness for long... "
            n " ...Could you...ask Mister Altrix if he has... some medicine for me...? "
            n " It's okay if you don't want to get it for me though... "
            n " I can just get it myself, I'll be fine... "
            n " As long as I don't get too sleepy and sleepwalk..*yawn*... "
            menu:
                " Help him ":
                    $ noxlv += 10
                    n " ...Thanks, [name]... "
                    n " ...You're the best... "
                    " Nox then shortly falls asleep on the bleachers. "
                    " Time to get his medicine then. "
                    scene black with dissolve
                    pause 1.0
                    scene classroom with dissolve
                    show altrixneutral at center with easeinleft
                    msa " Hmhm...Oh, [name]! "
                    msa " Did you have something to ask me? "
                    msa " You're kind of lucky that I was just in the middle of cleaning... "
                    msa " ...And not starting class, heh...that would be awkward. "
                    " You told him about what happened to Nox in the gym. "
                    hide altrixneutral at bottom
                    show altrixsad at center
                    msa " Oh dear...he forgot to take his medicine again? "
                    msa " Someone really needs to remind him to take his medicine... "
                    hide altrixsad at bottom
                    show altrixneutral at center
                    msa " Making sure that he's okay, alright? "
                    msa " I don't want him to fall asleep in the middle of Sol's class... "
                    hide altrixneutral at bottom
                    show altrixhappy at center
                    msa " Take care!! "
                    " You then went back to the gym. "
                    scene black with dissolve
                    pause 1.0
                    scene gym with dissolve
                    show noxsleepy at center with easeinleft
                    n " Zzzz...huh...? "
                    n " Oh...you got the medicine...thank you. "
                    n " Hold on, let me just... "
                    " Nox takes a tiny water bottle from his bag and uses it to swallow down his medicine. "
                    hide noxsleepy at bottom
                    show noxneutral at center
                    " He looks like he's feeling a bit better now, judging by his expression. "
                    " Well, not really, but slightly. "
                    n " Thanks for getting the medicine for me... "
                    n " I hope I didn't bother you too much for getting it... "
                    n " ...Well, uh... "
                    n " ...What do you want to talk about? "
                    scene black with dissolve
                    " You spent the rest of the break time talking with Nox. "
                    " You guys mostly talked about random things, like Nox's dream he had while you were gone. "
                    " Said that he was in a world where you had glasses so that you could date objects... "
                    " Sounds like you're just {a=https://store.steampowered.com/app/2201320/Date_Everything/}dating everything{/a} in there. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " Though you're already in the class area...so you waited on the bleachers until the teacher arrived. "
                    pause 2.0
                    jump peclassoc1
                " I'm kinda busy right now ":
                    n " That's okay.. "
                    n " I can go and get it on my own... "
                    " Before he could even take a step, he fell asleep. "
                    " Before he could land face flat into the ground, you caught him. "
                    " You then put him down on one of the bleachers. "
                    " Looks like you're going to have to get his medicine either way... "
                    " Let's go. "
                    scene black with dissolve
                    pause 1.0
                    scene classroom with dissolve
                    show altrixneutral at center with easeinleft
                    msa " Hmhm...Oh, [name]! "
                    msa " Did you have something to ask me? "
                    msa " You're kind of lucky that I was just in the middle of cleaning... "
                    msa " ...And not starting class, heh...that would be awkward. "
                    " You told him about what happened to Nox in the gym. "
                    hide altrixneutral at bottom
                    show altrixsad at center
                    msa " Oh dear...he forgot to take his medicine again? "
                    msa " Someone really needs to remind him to take his medicine... "
                    hide altrixsad at bottom
                    show altrixneutral at center
                    msa " Making sure that he's okay, alright? "
                    msa " I don't want him to fall asleep in the middle of Sol's class... "
                    hide altrixneutral at bottom
                    show altrixhappy at center
                    msa " Take care!! "
                    " You then went back to the gym. "
                    scene black with dissolve
                    pause 1.0
                    scene gym with dissolve
                    show noxsleepy at center with easeinleft
                    n " Zzzz...huh...? "
                    n " Oh...you got the medicine...thank you. "
                    n " Hold on, let me just... "
                    " Nox takes a tiny water bottle from his bag and uses it to swallow down his medicine. "
                    hide noxsleepy at bottom
                    show noxneutral at center
                    " He looks like he's feeling a bit better now, judging by his expression. "
                    " Well, not really, but slightly. "
                    n " Thanks for getting the medicine for me... "
                    n " I hope I didn't bother you too much for getting it... "
                    n " ...Well, uh... "
                    n " ...What do you want to talk about? "
                    scene black with dissolve
                    " You spent the rest of the break time talking with Nox. "
                    " You guys mostly talked about random things, like Nox's dream he had while you were gone. "
                    " Said that he was in a world where you had glasses so that you could date objects... "
                    " Sounds like you're just {a=https://store.steampowered.com/app/2201320/Date_Everything/}dating everything{/a} in there. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " Though you're already in the class area...so you waited on the bleachers until the teacher arrived. "
                    pause 2.0
                    jump peclassoc1
        else:
            x " Mmmmh...not again... "
            x " I fall asleep way too easily... "
            x " ...Not taking my medicine was a bad idea... "
            " You shook him a tad bit to wake him up a little. "
            hide noxsleepy at bottom
            show noxneutral at center
            " Luckily that worked. "
            " After he woke up a little, you asked him if he was doing alright. "
            x " ...If I'm being honest...*yawn*...no... "
            x " I don't want to bother Mister Altrix again though... "
            x " I'm pretty sleepy, but I'm sure... I can stay up for a bit longer... "
            x " It's not that I stayed up late or anything... "
            x " ...Just a condition that I have... "
            hide noxneutral at bottom
            show noxsleepy at center
            $ noxknow = True
            n " I'm Nox, by the way...Nox Cesso... "
            n " Hmhmmm... I can't really handle this amount of sleepiness for long... "
            n " ...Could you...ask Mister Altrix if he has... some medicine for me...? "
            n " It's okay if you don't want to get it for me though... "
            n " I can just get it myself, I'll be fine... "
            n " As long as I don't get too sleepy and sleepwalk..*yawn*... "
            menu:
                " Help him ":
                    $ noxlv += 10
                    n " ...Thanks, [name]... "
                    n " ...You're the best... "
                    " Nox then shortly falls asleep on the bleachers. "
                    " Time to get his medicine then. "
                    scene black with dissolve
                    pause 1.0
                    scene classroom with dissolve
                    show altrixneutral at center with easeinleft
                    msa " Hmhm...Oh, [name]! "
                    msa " Did you have something to ask me? "
                    msa " You're kind of lucky that I was just in the middle of cleaning... "
                    msa " ...And not starting class, heh...that would be awkward. "
                    " You told him about what happened to Nox in the gym. "
                    hide altrixneutral at bottom
                    show altrixsad at center
                    msa " Oh dear...he forgot to take his medicine again? "
                    msa " Someone really needs to remind him to take his medicine... "
                    hide altrixsad at bottom
                    show altrixneutral at center
                    msa " Making sure that he's okay, alright? "
                    msa " I don't want him to fall asleep in the middle of Sol's class... "
                    hide altrixneutral at bottom
                    show altrixhappy at center
                    msa " Take care!! "
                    " You then went back to the gym. "
                    scene black with dissolve
                    pause 1.0
                    scene gym with dissolve
                    show noxsleepy at center with easeinleft
                    n " Zzzz...huh...? "
                    n " Oh...you got the medicine...thank you. "
                    n " Hold on, let me just... "
                    " Nox takes a tiny water bottle from his bag and uses it to swallow down his medicine. "
                    hide noxsleepy at bottom
                    show noxneutral at center
                    " He looks like he's feeling a bit better now, judging by his expression. "
                    " Well, not really, but slightly. "
                    n " Thanks for getting the medicine for me... "
                    n " I hope I didn't bother you too much for getting it... "
                    n " ...Well, uh... "
                    n " ...What do you want to talk about? "
                    scene black with dissolve
                    " You spent the rest of the break time talking with Nox. "
                    " You guys mostly talked about random things, like Nox's dream he had while you were gone. "
                    " Said that he was in a world where you had glasses so that you could date objects... "
                    " Sounds like you're just {a=https://store.steampowered.com/app/2201320/Date_Everything/}dating everything{/a} in there. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " Though you're already in the class area...so you waited on the bleachers until the teacher arrived. "
                    pause 2.0
                    jump peclassoc1
                " I'm kinda busy right now ":
                    n " That's okay.. "
                    n " I can go and get it on my own... "
                    " Before he could even take a step, he fell asleep. "
                    " Before he could land face flat into the ground, you caught him. "
                    " You then put him down on one of the bleachers. "
                    " Looks like you're going to have to get his medicine either way... "
                    " Let's go. "
                    scene black with dissolve
                    pause 1.0
                    scene classroom with dissolve
                    show altrixneutral at center with easeinleft
                    msa " Hmhm...Oh, [name]! "
                    msa " Did you have something to ask me? "
                    msa " You're kind of lucky that I was just in the middle of cleaning... "
                    msa " ...And not starting class, heh...that would be awkward. "
                    " You told him about what happened to Nox in the gym. "
                    hide altrixneutral at bottom
                    show altrixsad at center
                    msa " Oh dear...he forgot to take his medicine again? "
                    msa " Someone really needs to remind him to take his medicine... "
                    hide altrixsad at bottom
                    show altrixneutral at center
                    msa " Making sure that he's okay, alright? "
                    msa " I don't want him to fall asleep in the middle of Sol's class... "
                    hide altrixneutral at bottom
                    show altrixhappy at center
                    msa " Take care!! "
                    " You then went back to the gym. "
                    scene black with dissolve
                    pause 1.0
                    scene gym with dissolve
                    show noxsleepy at center with easeinleft
                    n " Zzzz...huh...? "
                    n " Oh...you got the medicine...thank you. "
                    n " Hold on, let me just... "
                    " Nox takes a tiny water bottle from his bag and uses it to swallow down his medicine. "
                    hide noxsleepy at bottom
                    show noxneutral at center
                    " He looks like he's feeling a bit better now, judging by his expression. "
                    " Well, not really, but slightly. "
                    n " Thanks for getting the medicine for me... "
                    n " I hope I didn't bother you too much for getting it... "
                    n " ...Well, uh... "
                    n " ...What do you want to talk about? "
                    scene black with dissolve
                    " You spent the rest of the break time talking with Nox. "
                    " You guys mostly talked about random things, like Nox's dream he had while you were gone. "
                    " Said that he was in a world where you had glasses so that you could date objects... "
                    " Sounds like you're just {a=https://store.steampowered.com/app/2201320/Date_Everything/}dating everything{/a} in there. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " Though you're already in the class area...so you waited on the bleachers until the teacher arrived. "
                    pause 2.0
                    jump peclassoc1
label cafeteriawed2:
    # jacob and carmen
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and found two of your classmates hanging out with eachother. "
    " You wanted to talk to them...you decided to sit next to them to join their conversation. "
    show jacobneutral at left with easeinright
    show carmenneutral at right with easeinright
    if jacobknow == True and carmenknow == True:
        jac " ...Hold on, you serious? "
        jac " [name], I know you're there, but like... "
        jac " Carmen has something to tell us. "
        ca " ...(*Guitar playing sfx*) "
        hide jacobneutral at bottom
        show jacobsurprised at left
        jac " ...NO FUCKING WAY!!! "
        jac " HE DIES IN THE SECOND EPISODE??? "
        ca " ...(*Nod*) "
        hide jacobsurprised at bottom
        show jacobneutral at left
        jac " Wow... thanks for telling me this, Carmen. "
        jac " But seriously, in the second episode? "
        jac " That's way too early for a character dying! "
        jac " Though, I guess that's a way to surprise the viewers? "
        jac " But if you want more of an emotional impact, on my opinion... "
        jac " ...Let the character stay for awhile to have SOME development in them... "
        jac " (That also helps in letting the audience love them...) "
        jac " ...And THEN kill them off when the series ends. Or a few episodes in the middle of the series. "
        jac " I'm no writing expert, but it's something that I just prefer. "
        ca " ...(*Nod of approval*) "
        " You got curious and decided to ask what they were talking about. "
        jac " Me and Carmen here are both interested in this new show that just popped up. "
        jac " Something about two best friends travelling a fantasy world... "
        jac " ...And the main character's best friend dies on the second episode. "
        jac " I'm gonna give you a quick recap of what happens in the first episode, alright? "
        jac " Basically the MC and his best friend gets teleported to their favorite game... "
        jac " You know, average Isekai anime or whatever it's called... "
        jac " After a bit of exploring, their dumbasses decided to fight one of the bosses. "
        jac " Guess what happened? The best friend died and according to Carmen, could NOT respawn. "
        scene black with dissolve
        " You spent the rest of the break listening to Jacob yapping. "
        " You and Carmen honestly just relaxed there... "
        " ...Though you did ask a few questions here and there to understand the thing he was talking about more. "
        " And with how he's explaining it, you think you might check out the thing he's talking about. "
        play sound "audio/bellring.mp3"
        " ...After school, of course. "
        " The bell rings after a bit, time for your next class. "
        " You three made it all the way to the gym and got prepared for a fun class. "
        pause 2.0
        jump peclassoc1
    elif jacobknow == True and carmenknow == False:
        jac " ...Hold on, you serious? "
        jac " [name], I know you're there, but like... "
        $ carmenknow = True
        jac " Carmen has something to tell us. "
        ca " ...(*Guitar playing sfx*) "
        hide jacobneutral at bottom
        show jacobsurprised at left
        jac " ...NO FUCKING WAY!!! "
        jac " HE DIES IN THE SECOND EPISODE??? "
        ca " ...(*Nod*) "
        hide jacobsurprised at bottom
        show jacobneutral at left
        jac " Wow... thanks for telling me this, Carmen. "
        jac " But seriously, in the second episode? "
        jac " That's way too early for a character dying! "
        jac " Though, I guess that's a way to surprise the viewers? "
        jac " But if you want more of an emotional impact, on my opinion... "
        jac " ...Let the character stay for awhile to have SOME development in them... "
        jac " (That also helps in letting the audience love them...) "
        jac " ...And THEN kill them off when the series ends. Or a few episodes in the middle of the series. "
        jac " I'm no writing expert, but it's something that I just prefer. "
        ca " ...(*Nod of approval*) "
        " You got curious and decided to ask what they were talking about. "
        jac " Me and Carmen here are both interested in this new show that just popped up. "
        jac " Something about two best friends travelling a fantasy world... "
        jac " ...And the main character's best friend dies on the second episode. "
        jac " I'm gonna give you a quick recap of what happens in the first episode, alright? "
        jac " Basically the MC and his best friend gets teleported to their favorite game... "
        jac " You know, average Isekai anime or whatever it's called... "
        jac " After a bit of exploring, their dumbasses decided to fight one of the bosses. "
        jac " Guess what happened? The best friend died and according to Carmen, could NOT respawn. "
        scene black with dissolve
        " You spent the rest of the break listening to Jacob yapping. "
        " You and Carmen honestly just relaxed there... "
        " ...Though you did ask a few questions here and there to understand the thing he was talking about more. "
        " And with how he's explaining it, you think you might check out the thing he's talking about. "
        play sound "audio/bellring.mp3"
        " ...After school, of course. "
        " The bell rings after a bit, time for your next class. "
        " You three made it all the way to the gym and got prepared for a fun class. "
        pause 2.0
        jump peclassoc1
    elif jacobknow == False and carmenknow == True:
        x " ...Hold on, you serious? "
        x " [name], I know you're there, but like... "
        x " Carmen has something to tell us. "
        ca " ...(*Guitar playing sfx*) "
        hide jacobneutral at bottom
        show jacobsurprised at left
        x " ...NO FUCKING WAY!!! "
        x " HE DIES IN THE SECOND EPISODE??? "
        ca " ...(*Nod*) "
        hide jacobsurprised at bottom
        show jacobneutral at left
        x " Wow... thanks for telling me this, Carmen. "
        x " But seriously, in the second episode? "
        x " That's way too early for a character dying! "
        x " Though, I guess that's a way to surprise the viewers? "
        x " But if you want more of an emotional impact, on my opinion... "
        x " ...Let the character stay for awhile to have SOME development in them... "
        x " (That also helps in letting the audience love them...) "
        x " ...And THEN kill them off when the series ends. Or a few episodes in the middle of the series. "
        x " I'm no writing expert, but it's something that I just prefer. "
        ca " ...(*Nod of approval*) "
        " You got curious and decided to ask what they were talking about. "
        x " Oh, uh...[name]. Almost forgot that you were here. "
        $ jacobknow = True
        jac " Don't think I introduced myself before, so...I'm Jacob. "
        jac " Me and Carmen here are both interested in this new show that just popped up. "
        jac " Something about two best friends travelling a fantasy world... "
        jac " ...And the main character's best friend dies on the second episode. "
        jac " I'm gonna give you a quick recap of what happens in the first episode, alright? "
        jac " Basically the MC and his best friend gets teleported to their favorite game... "
        jac " You know, average Isekai anime or whatever it's called... "
        jac " After a bit of exploring, their dumbasses decided to fight one of the bosses. "
        jac " Guess what happened? The best friend died and according to Carmen, could NOT respawn. "
        scene black with dissolve
        " You spent the rest of the break listening to Jacob yapping. "
        " You and Carmen honestly just relaxed there... "
        " ...Though you did ask a few questions here and there to understand the thing he was talking about more. "
        " And with how he's explaining it, you think you might check out the thing he's talking about. "
        play sound "audio/bellring.mp3"
        " ...After school, of course. "
        " The bell rings after a bit, time for your next class. "
        " You three made it all the way to the gym and got prepared for a fun class. "
        pause 2.0
        jump peclassoc1
    else:
        x " ...Hold on, you serious? "
        x " [name], I know you're there, but like... "
        x " Carmen has something to tell us. "
        $ carmenknow = True
        ca " ...(*Guitar playing sfx*) "
        hide jacobneutral at bottom
        show jacobsurprised at left
        x " ...NO FUCKING WAY!!! "
        x " HE DIES IN THE SECOND EPISODE??? "
        ca " ...(*Nod*) "
        hide jacobsurprised at bottom
        show jacobneutral at left
        x " Wow... thanks for telling me this, Carmen. "
        x " But seriously, in the second episode? "
        x " That's way too early for a character dying! "
        x " Though, I guess that's a way to surprise the viewers? "
        x " But if you want more of an emotional impact, on my opinion... "
        x " ...Let the character stay for awhile to have SOME development in them... "
        x " (That also helps in letting the audience love them...) "
        x " ...And THEN kill them off when the series ends. Or a few episodes in the middle of the series. "
        x " I'm no writing expert, but it's something that I just prefer. "
        ca " ...(*Nod of approval*) "
        " You got curious and decided to ask what they were talking about. "
        x " Oh, uh...[name]. Almost forgot that you were here. "
        $ jacobknow = True
        jac " Don't think I introduced myself before, so...I'm Jacob. "
        jac " Me and Carmen here are both interested in this new show that just popped up. "
        jac " Something about two best friends travelling a fantasy world... "
        jac " ...And the main character's best friend dies on the second episode. "
        jac " I'm gonna give you a quick recap of what happens in the first episode, alright? "
        jac " Basically the MC and his best friend gets teleported to their favorite game... "
        jac " You know, average Isekai anime or whatever it's called... "
        jac " After a bit of exploring, their dumbasses decided to fight one of the bosses. "
        jac " Guess what happened? The best friend died and according to Carmen, could NOT respawn. "
        scene black with dissolve
        " You spent the rest of the break listening to Jacob yapping. "
        " You and Carmen honestly just relaxed there... "
        " ...Though you did ask a few questions here and there to understand the thing he was talking about more. "
        " And with how he's explaining it, you think you might check out the thing he's talking about. "
        play sound "audio/bellring.mp3"
        " ...After school, of course. "
        " The bell rings after a bit, time for your next class. "
        " You three made it all the way to the gym and got prepared for a fun class. "
        pause 2.0
        jump peclassoc1

label rooftopwed2:
    # spark and jam
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked to the rooftop and spotted two of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if sparkknow == True and jamknow == True:
        menu:
            " {image=sparkicon} Spark {image=sparkicon} ":
                jump bawbawbaw
            " {image=jamicon} Jam {image=jamicon} ":
                jump mawmawmaw
    elif sparkknow == True and jamknow == False:
        menu:
            " {image=sparkicon} Spark {image=sparkicon} ":
                jump bawbawbaw
            " {image=jamicon} A mean looking girl {image=jamicon} ":
                jump mawmawmaw
    elif sparkknow == False and jamknow == True:
        menu:
            " {image=sparkicon} A boy with antennas and a tail {image=sparkicon} ":
                jump bawbawbaw
            " {image=jamicon} Jam {image=jamicon} ":
                jump mawmawmaw
    else:
        menu:
            " {image=sparkicon} A boy with antennas and a tail {image=sparkicon} ":
                jump bawbawbaw
            " {image=jamicon} A mean looking girl {image=jamicon} ":
                jump mawmawmaw
    label bawbawbaw:
        show sparkneutral at center with easeinright
        if sparkknow == True:
            " ...Huh. Looks like he's on a call with someone. "
            " Being your nosy self, you pretended like you were doing something else... "
            " ...When really, you were listening into their conversation. "
            " The perfect trick, unless if you're being too obvious that you're listening. "
            " Time to hear what he's talking about... "
            sp " ...Yes, I know, sir. "
            x " Then I know that you know that Temero's been trying to get a kill every now and then. "
            x " She's been getting some murderous tendencies here and there, so please tell her to calm down. "
            x " I know that you can get through to her, considering you two are close due to that tournament you both partook in. "
            x " I have told her before that it's okay to not kill anyone right now, but she wouldn't listen. "
            sp " She gets like that... "
            sp " I guess she just needs that thrill of...you know...murdering someone? "
            sp " She always finds it so interesting and I don't know why. "
            sp " But, yeah...I'll speak with her about it and tell her to tone her tendencies down. "
            x " Thank you. She's been offering people some products that could help them... "
            x " ...When it's really just something bad for you. "
            x " It's a clever tactic, but with someone as insane as her... "
            x " It can be hard to trust her. "
            x " That's why I much prefer you two sneaking up on your victims. "
            x " The last one you got for me tasted good, by the way. "
            x " Thank you for bringing them to me. "
            sp " I was just doing your work, sir. "
            sp " It's nothing. "
            x " Your 'nothing' helps me be more powerful. "
            x " Thank you for your time, Spark. "
            x " Stay safe out there. "
            sp " Yes, sir. You should also stay safe too. "
            " The phone call ends. "
            sp " *Sigh*... Temero always acts like this. "
            sp " Time for me to go and scold her again... "
            hide sparkneutral at right with easeoutright
            " ...He then leaves. Hm, now this is some juicy information. "
            " You're going to have to figure out what's going on for the rest of the break. "
            " Why? because you have nothing else to do. "
            scene black with dissolve
            " You spent the rest of the break making a few theories about the call you heard. "
            " You put all of your thoughts on the notes app you had on your phone. "
            " The only bad thing was if someone looked into your notes app and found all of the things you wrote about. "
            " Not only about the situation you just heard, but that one fanfiction you wrote about yourself and another character. "
            " Very much a big yikes since you have a whole lot of personal things in there. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your PE class. "
            " You got off of the rooftop and went to the gym. "
            pause 2.0
            jump peclassoc1
        else:
            " ...Huh. Looks like he's on a call with someone. "
            " Being your nosy self, you pretended like you were doing something else... "
            " ...When really, you were listening into their conversation. "
            " The perfect trick, unless if you're being too obvious that you're listening. "
            " Time to hear what he's talking about... "
            x " ...Yes, I know, sir. "
            x " Then I know that you know that Temero's been trying to get a kill every now and then. "
            x " She's been getting some murderous tendencies here and there, so please tell her to calm down. "
            $ sparkknow = True
            x " Spark, I know that you can get through to her, considering you two are close due to that tournament you both partook in. "
            x " I have told her before that it's okay to not kill anyone right now, but she wouldn't listen. "
            sp " She gets like that... "
            sp " I guess she just needs that thrill of...you know...murdering someone? "
            sp " She always finds it so interesting and I don't know why. "
            sp " But, yeah...I'll speak with her about it and tell her to tone her tendencies down. "
            x " Thank you. She's been offering people some products that could help them... "
            x " ...When it's really just something bad for you. "
            x " It's a clever tactic, but with someone as insane as her... "
            x " It can be hard to trust her. "
            x " That's why I much prefer you two sneaking up on your victims. "
            x " The last one you got for me tasted good, by the way. "
            x " Thank you for bringing them to me. "
            sp " I was just doing your work, sir. "
            sp " It's nothing. "
            x " Your 'nothing' helps me be more powerful. "
            x " Thank you for your time, Spark. "
            x " Stay safe out there. "
            sp " Yes, sir. You should also stay safe too. "
            " The phone call ends. "
            sp " *Sigh*... Temero always acts like this. "
            sp " Time for me to go and scold her again... "
            hide sparkneutral at right with easeoutright
            " ...He then leaves. Hm, now this is some juicy information. "
            " You're going to have to figure out what's going on for the rest of the break. "
            " Why? because you have nothing else to do. "
            scene black with dissolve
            " You spent the rest of the break making a few theories about the call you heard. "
            " You put all of your thoughts on the notes app you had on your phone. "
            " The only bad thing was if someone looked into your notes app and found all of the things you wrote about. "
            " Not only about the situation you just heard, but that one fanfiction you wrote about yourself and another character. "
            " Very much a big yikes since you have a whole lot of personal things in there. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your PE class. "
            " You got off of the rooftop and went to the gym. "
            pause 2.0
            jump peclassoc1
    label mawmawmaw:
        show jamneutral at center with easeinleft
        if jamknow == True:
            ja " ... "
            ja " Oh, uh...hey there [name]. "
            ja " Came out to get some fresh air and stuff. "
            ja " You know, I've been thinking about Matte more recently... "
            ja " ...If you know her. She's the artsy kid in our class. "
            ja " Always liked the way she draws ever since I transferred here... "
            ja " Actually, you wanna know a fun fact? "
            hide jamneutral at bottom
            show jamsad at center
            ja " I kind of lashed out at her in the first day. "
            ja " Things were just rough that day...my parents not being the best for me, after all. "
            hide jamsad at bottom
            show jamneutral at center
            ja " Don't even know how they got me into this school with the money we've got, hm. "
            ja " It's a miracle, I guess. "
            hide jamneutral at bottom
            show jamsad at center
            ja " Anyway - no matter how much I yelled at her during break time... "
            ja " ...She kept herself calm and didn't leave me. "
            ja " Kept telling me that everything was going to be fine. "
            ja " Kept reassuring and comforting me... "
            ja " I don't know how she was able to put up with me. "
            ja " If this was back in my old school, then I probably wouldn't have gotten comforted. "
            hide jamsad at bottom
            show jamhappy at center
            ja " That...was my first time being told that I could just relax for once. "
            ja " And just not live up to everyone's expectations, you know? "
            ja " And also the first time I've felt that no one was gonna judge me for speaking my thoughts. "
            ja " It was new to me. A new feeling, but a good one. "
            ja " Most of the days I look forward to seeing Matte whenever I go to school. "
            ja " She somehow always has time for me...even stopping herself from finishing her paintings. "
            ja " I keep telling her to continue her paintings, but she just...keeps insisting that it's fine. "
            ja " I don't really understand her...but I think that she's really nice. "
            hide jamhappy at bottom
            show jamneutral at center
            ja " ...Eeh, sorry. I'm just rambling to you, you're probably not even listening. "
            ja " When did I learn to talk so much...? "
            ja " I don't even know you that well enough... "
            menu:
                " It was nice hearing you talk ":
                    $ jamlv += 10
                    ja " ...? "
                    ja " Well, um... "
                    ja " I'm glad you think that way then. "
                    ja " You, uh... "
                    ja " You don't mind if I talk to you more then? "
                    " You shook your head as a sign that you didn't mind. "
                    ja " That's great, then... "
                    ja " I still have a lot to talk about to you. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jam. "
                    " You had to admit, it was kind of nice talking with her. "
                    " After all, she looked mean. You didn't expect her to be so nice to talk to. "
                    " Guess you really can't just judge a book by it's cover. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got off of the rooftop and went to the gym. "
                    pause 2.0
                    jump peclassoc1
                " *Say nothing* ":
                    ja " ... "
                    ja " Uh...you don't mind if I talk to you more? "
                    ja " I just feel like I need to talk about something. "
                    ja " To, you know...make things less awkward? "
                    " You shook your head as a sign that you didn't mind. "
                    ja " That's great, then... "
                    ja " I still have a lot to talk about to you. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jam. "
                    " You had to admit, it was kind of nice talking with her. "
                    " After all, she looked mean. You didn't expect her to be so nice to talk to. "
                    " Guess you really can't just judge a book by it's cover. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got off of the rooftop and went to the gym. "
                    pause 2.0
                    jump peclassoc1
        else:
            x " ... "
            x " Oh, uh...hey there [name]. "
            $ jamknow = True
            ja " Don't think we met before, so...I'm Jam. Nice to meet you. "
            ja " Came out to get some fresh air and stuff. "
            ja " You know, I've been thinking about Matte more recently... "
            ja " ...If you know her. She's the artsy kid in our class. "
            ja " Always liked the way she draws ever since I transferred here... "
            ja " Actually, you wanna know a fun fact? "
            hide jamneutral at bottom
            show jamsad at center
            ja " I kind of lashed out at her in the first day. "
            ja " Things were just rough that day...my parents not being the best for me, after all. "
            hide jamsad at bottom
            show jamneutral at center
            ja " Don't even know how they got me into this school with the money we've got, hm. "
            ja " It's a miracle, I guess. "
            hide jamneutral at bottom
            show jamsad at center
            ja " Anyway - no matter how much I yelled at her during break time... "
            ja " ...She kept herself calm and didn't leave me. "
            ja " Kept telling me that everything was going to be fine. "
            ja " Kept reassuring and comforting me... "
            ja " I don't know how she was able to put up with me. "
            ja " If this was back in my old school, then I probably wouldn't have gotten comforted. "
            hide jamsad at bottom
            show jamhappy at center
            ja " That...was my first time being told that I could just relax for once. "
            ja " And just not live up to everyone's expectations, you know? "
            ja " And also the first time I've felt that no one was gonna judge me for speaking my thoughts. "
            ja " It was new to me. A new feeling, but a good one. "
            ja " Most of the days I look forward to seeing Matte whenever I go to school. "
            ja " She somehow always has time for me...even stopping herself from finishing her paintings. "
            ja " I keep telling her to continue her paintings, but she just...keeps insisting that it's fine. "
            ja " I don't really understand her...but I think that she's really nice. "
            hide jamhappy at bottom
            show jamneutral at center
            ja " ...Eeh, sorry. I'm just rambling to you, you're probably not even listening. "
            ja " When did I learn to talk so much...? "
            ja " I don't even know you that well enough... "
            menu:
                " It was nice hearing you talk ":
                    $ jamlv += 10
                    ja " ...? "
                    ja " Well, um... "
                    ja " I'm glad you think that way then. "
                    ja " You, uh... "
                    ja " You don't mind if I talk to you more then? "
                    " You shook your head as a sign that you didn't mind. "
                    ja " That's great, then... "
                    ja " I still have a lot to talk about to you. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jam. "
                    " You had to admit, it was kind of nice talking with her. "
                    " After all, she looked mean. You didn't expect her to be so nice to talk to. "
                    " Guess you really can't just judge a book by it's cover. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got off of the rooftop and went to the gym. "
                    pause 2.0
                    jump peclassoc1
                " *Say nothing* ":
                    ja " ... "
                    ja " Uh...you don't mind if I talk to you more? "
                    ja " I just feel like I need to talk about something. "
                    ja " To, you know...make things less awkward? "
                    " You shook your head as a sign that you didn't mind. "
                    ja " That's great, then... "
                    ja " I still have a lot to talk about to you. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jam. "
                    " You had to admit, it was kind of nice talking with her. "
                    " After all, she looked mean. You didn't expect her to be so nice to talk to. "
                    " Guess you really can't just judge a book by it's cover. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got off of the rooftop and went to the gym. "
                    pause 2.0
                    jump peclassoc1
label librarywed2:
    # koa and the twins
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked to the library and spotted three of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if koaknow == True and yinhuiknow,yangyiknow == True:
        menu:
            " {image=koaicon} Koa {image=koaicon} ":
                jump harperde
            " {image=yinyangicon} Yinhui and Yangyi {image=yinyangicon} ":
                jump dirkde
    elif koaknow == True and yinhui,yangyiknow == False:
        menu:
            " {image=koaicon} Koa {image=koaicon} ":
                jump harperde
            " {image=yinyangicon} Twins {image=yinyangicon} ":
                jump dirkde
    elif koaknow == False and yinhui,yangyiknow == True:
        menu:
            " {image=koaicon} An emo looking guy {image=koaicon} ":
                jump harperde
            " {image=yinyangicon} Yinhui and Yangyi {image=yinyangicon} ":
                jump dirkde
    else:
        menu:
            " {image=koaicon} An emo looking guy {image=koaicon} ":
                jump harperde
            " {image=yinyangicon} Twins {image=yinyangicon} ":
                jump dirkde
    label harperde:
        show koaneutral at center with easeinright
        if koaknow == True:
            k " ...Someone knocked over all of these books... "
            k " Hm...guess I can put all of these into their places... "
            k " Don't have much to do, anyway... "
            " He then starts picking up some of the books. "
            " As he was picking them up, he notices that you were there. "
            " Due to the fact you were kinda standing a bit infront of him. "
            " And cause - with his vision while picking up the books - he saw your shoes. "
            " He seemed a little bit pleased to see you. "
            k " ...[name]. Nice to see you here. "
            k " Actually, could you help me arrange the books over here? "
            k " A teacher originally had be arrange books and I got that done earlier... "
            k " ...But looks like someone had a little accident. "
            k " Not that I mind. Atleast it gives me something to do for the break. "
            k " I was originally planning on doing something else, but this can also do. "
            k " Would you like to help? "
            k " It's okay if you don't want to, or if you have something else to do. "
            k " I'm not going to force you to do things that you don't want to. "
            " Should you help Koa? for some reason he feels more talkative today. "
            " Looks like he's trying something new, maybe?? you feel like he doesn't talk a lot. "
            menu:
                " Help ":
                    $ koalv += 10
                    k " Thank you. "
                    k " How about you take this side and I'll take the other? "
                    " Koa points to the other bookshelf that got almost all of its books on the ground. "
                    " His was the one with all of the books on the ground. "
                    " He's making you do the one with less work...maybe because he didn't want you to suffer? "
                    " Oh well, atleast you don't have much to do. "
                    " You nodded, but also offered to help him if you got done first. "
                    k " ...Sure. I don't mind that. "
                    k " Let's get started then. "
                    scene black with dissolve
                    " You spent the rest of the break arranging the books in the library with Koa. "
                    " You unexpectedly got done first, which resulting you in helping Koa next. "
                    " Koa seemed to appreciate your help on this. "
                    " You even talked to him a bit while you both were arranging. "
                    " ...He didn't really respond much though. Only spoke in a few words."
                    " You thought that his prescence was enough for you to feel comfy with him. "
                    play sound "audio/bellring.mp3"
                    " By the time you both were done, the bell had rung. "
                    " You both got out of the library and went to the gym for the next class. "
                    pause 2.0
                    jump peclassoc1
                " I'm kinda busy ":
                    k " That's okay. "
                    k " Good luck on whatever you're going to do... "
                    k " ...If you need anything, I'm right here. "
                    scene black with dissolve
                    " You lied. You actually didn't need to do something. "
                    " You were just finding an excuse to not do work. "
                    " You walked to the corner of the library and scrolled on your phone for the rest of the break. "
                    " ...And also played a few games here and there. "
                    " You were starting to think that you should've helped him, buuuuut... "
                    " Your gamer instincts kinda kicked in. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got out of the library and went to the gym for the next class. "
                    pause 2.0
                    jump peclassoc1
        else:
            x " ...Someone knocked over all of these books... "
            x " Hm...guess I can put all of these into their places... "
            x " Don't have much to do, anyway... "
            " He then starts picking up some of the books. "
            " As he was picking them up, he notices that you were there. "
            " Due to the fact you were kinda standing a bit infront of him. "
            " And cause - with his vision while picking up the books - he saw your shoes. "
            " He seemed a little bit pleased to see you. "
            x " ...[name]. Nice to see you here. "
            x " I don't think we'ver met before... "
            $ koaknow = True
            k " ...I'm Koa, nice to meet you. "
            k " Actually, could you help me arrange the books over here? "
            k " A teacher originally had be arrange books and I got that done earlier... "
            k " ...But looks like someone had a little accident. "
            k " Not that I mind. Atleast it gives me something to do for the break. "
            k " I was originally planning on doing something else, but this can also do. "
            k " Would you like to help? "
            k " It's okay if you don't want to, or if you have something else to do. "
            k " I'm not going to force you to do things that you don't want to. "
            " Should you help Koa? for some reason he feels more talkative today. "
            " Looks like he's trying something new, maybe?? you feel like he doesn't talk a lot. "
            menu:
                " Help ":
                    $ koalv += 10
                    k " Thank you. "
                    k " How about you take this side and I'll take the other? "
                    " Koa points to the other bookshelf that got almost all of its books on the ground. "
                    " His was the one with all of the books on the ground. "
                    " He's making you do the one with less work...maybe because he didn't want you to suffer? "
                    " Oh well, atleast you don't have much to do. "
                    " You nodded, but also offered to help him if you got done first. "
                    k " ...Sure. I don't mind that. "
                    k " Let's get started then. "
                    scene black with dissolve
                    " You spent the rest of the break arranging the books in the library with Koa. "
                    " You unexpectedly got done first, which resulting you in helping Koa next. "
                    " Koa seemed to appreciate your help on this. "
                    " You even talked to him a bit while you both were arranging. "
                    " ...He didn't really respond much though. Only spoke in a few words."
                    " You thought that his prescence was enough for you to feel comfy with him. "
                    play sound "audio/bellring.mp3"
                    " By the time you both were done, the bell had rung. "
                    " You both got out of the library and went to the gym for the next class. "
                    pause 2.0
                    jump peclassoc1
                " I'm kinda busy ":
                    k " That's okay. "
                    k " Good luck on whatever you're going to do... "
                    k " ...If you need anything, I'm right here. "
                    scene black with dissolve
                    " You lied. You actually didn't need to do something. "
                    " You were just finding an excuse to not do work. "
                    " You walked to the corner of the library and scrolled on your phone for the rest of the break. "
                    " ...And also played a few games here and there. "
                    " You were starting to think that you should've helped him, buuuuut... "
                    " Your gamer instincts kinda kicked in. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got out of the library and went to the gym for the next class. "
                    pause 2.0
                    jump peclassoc1
    label dirkde:
        show yinhuineutral at right with easeinleft
        show yangyineutral at left with easeinleft
        if yinhuiknow == True and yangyiknow == True:
            yi " Hey there [name]. "
            ya " Hiya! "
            yi " ... "
            yi " Okay, both of you don't tell the guy that's fixing the bookshelves over there... "
            ya " ...Yinhui. "
            ya " What did you do this time...? "
            yi " Okay, listen... "
            yi " You know how I was playing a game, right? "
            ya " Yesss...? "
            ya " I have a feeling that I know where this is going... "
            yi " Soo...my teammates happened to be shit... "
            hide yangyineutral at bottom
            show yangyiangry at left
            ya " Okay I definitely know where this is going. "
            ya " Yinhui, you're helping that boy over there pick everything up. "
            hide yinhuineutral at bottom
            show yinhuitough at right
            yi " But I nono wanna... "
            yi " You're my brother, right? "
            yi " You can't just make your precious twin do all the workkkk... "
            ya " Yinhui. "
            ya " [name], he has to help that guy out, right? "
            menu:
                " Yeah ":
                    $ yangyilv += 10
                    ya " See? [name] agrees. "
                    ya " You're helping him pick all of that up and admit to what you did. "
                    yi " You're acting so much like mom right now. "
                    ya " And so what if I am? "
                    hide yinhuitough at bottom
                    show yinhuineutral at right
                    yi " Alright, jeez... "
                    yi " (You're in such a mood today...) "
                    yi " Hey, Koa...I'm here to help... "
                    scene black with dissolve
                    " You spent the rest of the break watching Yinhui help that one guy pick all of the books up. "
                    " The guy kinda just seemed confused, but told Yinhui that it was okay and that it was just a mistake. "
                    " But Yangyi kept giving him the stinky eye whenever Yinhui looked back at him. "
                    " You never knew someone as happy as Yangyi could get mad like that... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got out of the library and went to the gym for the next class. "
                    pause 2.0
                    jump peclassoc1
                " Nah ":
                    $ yinhuilv += 10
                    yi " SEE? [name] agrees that I don't have to do it! "
                    ya " You still have to do it, it's YOUR mistake after all. "
                    ya " You're helping him pick all of that up and admit to what you did. "
                    yi " You're acting so much like mom right now. "
                    ya " And so what if I am? "
                    hide yinhuitough at bottom
                    show yinhuineutral at right
                    yi " Alright, jeez... "
                    yi " (You're in such a mood today...) "
                    yi " Hey, Koa...I'm here to help... "
                    scene black with dissolve
                    " You spent the rest of the break watching Yinhui help that one guy pick all of the books up. "
                    " The guy kinda just seemed confused, but told Yinhui that it was okay and that it was just a mistake. "
                    " But Yangyi kept giving him the stinky eye whenever Yinhui looked back at him. "
                    " You never knew someone as happy as Yangyi could get mad like that... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got out of the library and went to the gym for the next class. "
                    pause 2.0
                    jump peclassoc1
        elif yinhuiknow == True and yangyiknow == False:
            yi " Hey there [name]. "
            x " Hiya! "
            $ yangyiknow = True
            ya " Oh - I'm Yangyi, Yinhui's twin brother! "
            yi " ... "
            yi " Okay, both of you don't tell the guy that's fixing the bookshelves over there... "
            ya " ...Yinhui. "
            ya " What did you do this time...? "
            yi " Okay, listen... "
            yi " You know how I was playing a game, right? "
            ya " Yesss...? "
            ya " I have a feeling that I know where this is going... "
            yi " Soo...my teammates happened to be shit... "
            hide yangyineutral at bottom
            show yangyiangry at left
            ya " Okay I definitely know where this is going. "
            ya " Yinhui, you're helping that boy over there pick everything up. "
            hide yinhuineutral at bottom
            show yinhuitough at right
            yi " But I nono wanna... "
            yi " You're my brother, right? "
            yi " You can't just make your precious twin do all the workkkk... "
            ya " Yinhui. "
            ya " [name], he has to help that guy out, right? "
            menu:
                " Yeah ":
                    $ yangyilv += 10
                    ya " See? [name] agrees. "
                    ya " You're helping him pick all of that up and admit to what you did. "
                    yi " You're acting so much like mom right now. "
                    ya " And so what if I am? "
                    hide yinhuitough at bottom
                    show yinhuineutral at right
                    yi " Alright, jeez... "
                    yi " (You're in such a mood today...) "
                    yi " Hey, Koa...I'm here to help... "
                    scene black with dissolve
                    " You spent the rest of the break watching Yinhui help that one guy pick all of the books up. "
                    " The guy kinda just seemed confused, but told Yinhui that it was okay and that it was just a mistake. "
                    " But Yangyi kept giving him the stinky eye whenever Yinhui looked back at him. "
                    " You never knew someone as happy as Yangyi could get mad like that... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got out of the library and went to the gym for the next class. "
                    pause 2.0
                    jump peclassoc1
                " Nah ":
                    $ yinhuilv += 10
                    yi " SEE? [name] agrees that I don't have to do it! "
                    ya " You still have to do it, it's YOUR mistake after all. "
                    ya " You're helping him pick all of that up and admit to what you did. "
                    yi " You're acting so much like mom right now. "
                    ya " And so what if I am? "
                    hide yinhuitough at bottom
                    show yinhuineutral at right
                    yi " Alright, jeez... "
                    yi " (You're in such a mood today...) "
                    yi " Hey, Koa...I'm here to help... "
                    scene black with dissolve
                    " You spent the rest of the break watching Yinhui help that one guy pick all of the books up. "
                    " The guy kinda just seemed confused, but told Yinhui that it was okay and that it was just a mistake. "
                    " But Yangyi kept giving him the stinky eye whenever Yinhui looked back at him. "
                    " You never knew someone as happy as Yangyi could get mad like that... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got out of the library and went to the gym for the next class. "
                    pause 2.0
                    jump peclassoc1
        elif yinhuiknow == False and yangyiknow == True:
            x " Hey there [name]. "
            $ yinhuiknow = True
            yi " I'm Yinhui, Yangyi's twin brother. "
            ya " Hiya! "
            yi " ... "
            yi " Okay, both of you don't tell the guy that's fixing the bookshelves over there... "
            ya " ...Yinhui. "
            ya " What did you do this time...? "
            yi " Okay, listen... "
            yi " You know how I was playing a game, right? "
            ya " Yesss...? "
            ya " I have a feeling that I know where this is going... "
            yi " Soo...my teammates happened to be shit... "
            hide yangyineutral at bottom
            show yangyiangry at left
            ya " Okay I definitely know where this is going. "
            ya " Yinhui, you're helping that boy over there pick everything up. "
            hide yinhuineutral at bottom
            show yinhuitough at right
            yi " But I nono wanna... "
            yi " You're my brother, right? "
            yi " You can't just make your precious twin do all the workkkk... "
            ya " Yinhui. "
            ya " [name], he has to help that guy out, right? "
            menu:
                " Yeah ":
                    $ yangyilv += 10
                    ya " See? [name] agrees. "
                    ya " You're helping him pick all of that up and admit to what you did. "
                    yi " You're acting so much like mom right now. "
                    ya " And so what if I am? "
                    hide yinhuitough at bottom
                    show yinhuineutral at right
                    yi " Alright, jeez... "
                    yi " (You're in such a mood today...) "
                    yi " Hey, Koa...I'm here to help... "
                    scene black with dissolve
                    " You spent the rest of the break watching Yinhui help that one guy pick all of the books up. "
                    " The guy kinda just seemed confused, but told Yinhui that it was okay and that it was just a mistake. "
                    " But Yangyi kept giving him the stinky eye whenever Yinhui looked back at him. "
                    " You never knew someone as happy as Yangyi could get mad like that... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got out of the library and went to the gym for the next class. "
                    pause 2.0
                    jump peclassoc1
                " Nah ":
                    $ yinhuilv += 10
                    yi " SEE? [name] agrees that I don't have to do it! "
                    ya " You still have to do it, it's YOUR mistake after all. "
                    ya " You're helping him pick all of that up and admit to what you did. "
                    yi " You're acting so much like mom right now. "
                    ya " And so what if I am? "
                    hide yinhuitough at bottom
                    show yinhuineutral at right
                    yi " Alright, jeez... "
                    yi " (You're in such a mood today...) "
                    yi " Hey, Koa...I'm here to help... "
                    scene black with dissolve
                    " You spent the rest of the break watching Yinhui help that one guy pick all of the books up. "
                    " The guy kinda just seemed confused, but told Yinhui that it was okay and that it was just a mistake. "
                    " But Yangyi kept giving him the stinky eye whenever Yinhui looked back at him. "
                    " You never knew someone as happy as Yangyi could get mad like that... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got out of the library and went to the gym for the next class. "
                    pause 2.0
                    jump peclassoc1
        else:
            x " Hey there [name]. "
            $ yinhuiknow = True
            yi " I'm Yinhui, Yangyi's twin brother. "
            x " Hiya! "
            $ yangyiknow = True
            ya " Oh - I'm Yangyi, Yinhui's twin brother! "
            yi " ... "
            yi " Okay, both of you don't tell the guy that's fixing the bookshelves over there... "
            ya " ...Yinhui. "
            ya " What did you do this time...? "
            yi " Okay, listen... "
            yi " You know how I was playing a game, right? "
            ya " Yesss...? "
            ya " I have a feeling that I know where this is going... "
            yi " Soo...my teammates happened to be shit... "
            hide yangyineutral at bottom
            show yangyiangry at left
            ya " Okay I definitely know where this is going. "
            ya " Yinhui, you're helping that boy over there pick everything up. "
            hide yinhuineutral at bottom
            show yinhuitough at right
            yi " But I nono wanna... "
            yi " You're my brother, right? "
            yi " You can't just make your precious twin do all the workkkk... "
            ya " Yinhui. "
            ya " [name], he has to help that guy out, right? "
            menu:
                " Yeah ":
                    $ yangyilv += 10
                    ya " See? [name] agrees. "
                    ya " You're helping him pick all of that up and admit to what you did. "
                    yi " You're acting so much like mom right now. "
                    ya " And so what if I am? "
                    hide yinhuitough at bottom
                    show yinhuineutral at right
                    yi " Alright, jeez... "
                    yi " (You're in such a mood today...) "
                    yi " Hey, Koa...I'm here to help... "
                    scene black with dissolve
                    " You spent the rest of the break watching Yinhui help that one guy pick all of the books up. "
                    " The guy kinda just seemed confused, but told Yinhui that it was okay and that it was just a mistake. "
                    " But Yangyi kept giving him the stinky eye whenever Yinhui looked back at him. "
                    " You never knew someone as happy as Yangyi could get mad like that... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got out of the library and went to the gym for the next class. "
                    pause 2.0
                    jump peclassoc1
                " Nah ":
                    $ yinhuilv += 10
                    yi " SEE? [name] agrees that I don't have to do it! "
                    ya " You still have to do it, it's YOUR mistake after all. "
                    ya " You're helping him pick all of that up and admit to what you did. "
                    yi " You're acting so much like mom right now. "
                    ya " And so what if I am? "
                    hide yinhuitough at bottom
                    show yinhuineutral at right
                    yi " Alright, jeez... "
                    yi " (You're in such a mood today...) "
                    yi " Hey, Koa...I'm here to help... "
                    scene black with dissolve
                    " You spent the rest of the break watching Yinhui help that one guy pick all of the books up. "
                    " The guy kinda just seemed confused, but told Yinhui that it was okay and that it was just a mistake. "
                    " But Yangyi kept giving him the stinky eye whenever Yinhui looked back at him. "
                    " You never knew someone as happy as Yangyi could get mad like that... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your PE class. "
                    " You got out of the library and went to the gym for the next class. "
                    pause 2.0
                    jump peclassoc1
label peclassoc1:
    scene gym with dissolve
    " You waited for your PE teacher to arrive in the gym. "
    " A loud BANG can be heard from behind you...you're getting more and more used to this sound everytime it's PE class. " with vpunch
    " You then greet the teacher with a good morning, like the rest of the class did. "
    show solneutral at center with easeinright
    msso " GOOOD MORNING MY STUDENTS!! "
    msso " Better get that energy up, up, UPPPP!! "
    hide solneutral at bottom
    show solhappy at center
    msso " We're going to be doing a few laps around the gym today! "
    hide solhappy at bottom
    show solsad at center
    msso " ...I just decided to do that since the principal didn't exactly give me any orders for today. "
    hide solsad at bottom
    show solhappy at center
    msso " But, YEAHH!! LAPS AROUND THE GYM!! "
    msso " We'll be doing 5 laps in total - just stop when you feel like you can't take it anymore! "
    hide solhappy at bottom
    show solneutral at center
    msso " Though, if any of you do have any conditions that won't allow you to run, you can hand by the bleachers for now. "
    msso " BUT! You'll be doing a worksheet. I've prepared these bad boys just in case one of you guys DOES have a condition! "
    msso " Of course I can't just let my students do nothing for the entire class! "
    msso " Oh, right. And REMINDER FOR OUR ACTIVITY ON FRIDAY!! BE PREPARED FOR THAT!! "
    msso " Alright, LET'S GET STARTED!! " with vpunch
    scene black with dissolve
    " You spent the rest of the class hours doing laps around the gym. "
    " You stopped when you did four laps, and the teacher seemed to take note of that. "
    " You drank half of your water bottle somehow just after that. "
    " Thirsty ass bitch... "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, time for another break. "
    " You walked out of the gym and went to the hallways to find somewhere to relax. "
    pause 2.0
    jump wedocbreak3

label wedocbreak3:
    scene hallway with dissolve
    " You walked into the hallways and thought of somewhere to go... "
    if pythonchallenge == True:
        " While looking around, you spot a door you've never seen before... "
        " Looks like this was the place that the note was talking about. "
        " Let's see if you have all of the codes achieved... "
        if pythoncode4,pythoncode2,pythoncode0 == True:
            " The moment you put your hand on the doorknob, it unlocks. "
            " You step into the room, bracing yourself for what could pop up... "
            scene black with dissolve
            pause 2.0
            jump pythonmeet
        else:
            " Huh, looks like you missed some codes. "
            " You're not gonna be let in, sorry! "
            " Time for you to just have a normal break then. "
            " What a shame! "
            pass
    else:
        pass
    " Where do you go for this break? "
    menu:
        " {image=koaicon} The front of the school {image=quinnicon} ":
            jump wedfront3wed
        " {image=temeroicon} The back of the school {image=sparkicon} ":
            jump wedback3wed
        " {image=carmenicon} Back into the gym {image=yinyangicon} ":
            jump wedgym3wed
        " {image=diskicon} The cafeteria {image=noxicon} ":
            jump wedcafeteria3wed
        " {image=jacobicon} The rooftop {image=matteicon} ":
            jump wedrooftop3wed
        " {image=jamicon} The library {image=orchidicon} ":
            jump wedlibrary3wed
label wedfront3wed:
    # koa and quinn
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked onto the front of the school and spotted two of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if koaknow == True and quinnknow == True:
        menu:
            " {image=koaicon} Koa {image=koaicon} ":
                jump koabath
            " {image=quinnicon} Quinn {image=quinnicon} ":
                jump quinnbath
    elif koaknow == True and quinnknow == False:
        menu:
            " {image=koaicon} Koa {image=koaicon} ":
                jump koabath
            " {image=quinnicon} A guy who looks like he's into theater {image=quinnicon} ":
                jump quinnbath
    elif koaknow == False and quinnknow == True:
        menu:
            " {image=koaicon} An emo guy {image=koaicon} ":
                jump koabath
            " {image=quinnicon} Quinn {image=quinnicon} ":
                jump quinnbath
    else:
        menu:
            " {image=koaicon} An emo guy {image=koaicon} ":
                jump koabath
            " {image=quinnicon} A guy who looks like he's into theater {image=quinnicon} ":
                jump quinnbath
    label koabath:
        # talking about orchid
        show koaneutral at center with easeinright
        if koaknow == True:
            k " Hmhmm... "
            " He seems to be reading a book. "
            " You didn't want to disturb him in his reading, so you stayed silent. "
            " After a few minutes of him reading, he notices you. "
            k " ...Hi, [name]. "
            k " Sorry if I didn't notice you at first... "
            k " I was kind of busy reading this book. "
            k " It's about psychology. Orchid showed me this one. "
            k " Never thought I'd see the day where they would reccomend me a book... "
            k " ...Either they just saw it on a video, or they actually read this. "
            k " ... "
            " Koa stays silent for a few more minutes. "
            " Judging by his expressionless expression, you could somehow tell that he wanted to tell you something. "
            " You're not sure on what it is, but it was just...something. "
            " He eventually speaks up about his thoughts after a few minutes of being silent. "
            k " ...[name]. "
            k " Would you be comfortable if I talked to you about something? "
            " He closes the book he was reading and looked down at the ground. "
            k " It's...about my friend. You could consider that me and them...are close. "
            k " It's okay if you'd like to talk about something else though. "
            k " I don't want you to just sit around awkwardly for no reason... "
            menu:
                " Talk to me ":
                    $ koalv += 10
                    k " If you say so. "
                    k " This is about my friend, Orchid... the one I mention earlier. "
                    k " Orchid's great, really. A little clingy, but I don't mind it. "
                    k " Believe it or not, I had to befriend them first. "
                    k " I saw that they were reading a book that I enjoyed so I commented on it: "
                    k " '...Sorry if I'm bothering you or anything, but is that Podoka Pagica?' "
                    k " They proceeded to talk to me about it the rest of the day. "
                    k " Didn't know they were such a die hard fan of the book... "
                    k " Ever since that, we've become friends. Getting closer and closer... "
                    hide koaneutral at bottom
                    show koasad at center
                    stop music fadeout 1.5
                    play music "audio/emotionalmoment.mp3" fadein 2.0
                    k " But, there's things I've noticed about them. "
                    k " They dont exactly interact with others. "
                    k " I thought that they were just struggling a bit and just needed to help them... "
                    k " I did try to help them the best I could, but it always ended up in Orchid themselves feeling embarrassed. "
                    k " Embarrassed by having to end the conversation early because they don't share the same interests as everyone else. "
                    k " I've tried telling them that it's okay to not have the same interests as them, but... "
                    k " They just seemed to not be interested in anything that the others were mentioning. "
                    k " I've tried getting Disk to talk to them - but all Disk could say was that they were being really quiet... "
                    k " ...Disk might've even thought that they were too intimidated due to how popular he was. "
                    k " After a few tries of helping them, I eventually stopped since I didn't want to push them too much. "
                    k " And everything was fine. Until one day... "
                    hide koasad at bottom
                    show koaneutral at center
                    k " ...They texted me in the middle of the night. I had just woken up. "
                    k " They sent me a very long message - venting about how they couldn't be like everyone else. "
                    k " I mean, I get how they felt... "
                    k " It's not every day you'd see a scene kid at your school. "
                    k " And people like them...they'd usually expect to not be accepted. "
                    k " Everyone always talked with them kindly, but they couldn't help but feel as if everything's just a lie. "
                    k " As if this is all just some big prank that everyone's pulling off. "
                    hide koaneutral at bottom
                    show koasad at center
                    k " They even thought I was a part of it too, at some point in me trying to comfort them. "
                    k " I kept reassuring that everyone's not pranking them, and that everything was fine... "
                    k " ...Even if it was hard to get through to them, they eventually calmed down. "
                    k " I don't know how I would feel if I didn't wake up at that time. "
                    k " If I had just ignored the buzzing from my phone. "
                    k " If I just ignored them...they probably would've believed their thoughts due to how deep they were thinking. "
                    k " ...I don't exactly like the idea of them falling so deep into their thoughts, they would... "
                    k " ... "
                    hide koasad at bottom
                    show koaneutral at center
                    stop music fadeout 1.5
                    play music "audio/paperhigh.mp3" fadein 1.5
                    k " If you ever see them around, and if it doesn't bother you... "
                    k " Maybe go ahead and talk about their interests with them. "
                    k " I'm sure that it would make their day better that someone's atleast a little interested. "
                    k " ...Thank you for letting me talk about this. "
                    k " I...don't really want to get you uncomfortable by staying in this topic for long, so... "
                    k " ...How about we talk about something else? How's your day today? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Koa. "
                    " Hmm...maybe you should check out that Orchid person that Koa was talking about. "
                    " Make sure they're okay and everything like that. "
                    " You didn't really like seeing other people suffering. "
                    if kind == True or calm == True:
                        pass
                    elif mean == True:
                        " I mean, you did like some suffering here and there... "
                        " ...But you didn't want something like that to happen to one of your classmates. "
                        pass
                    else:
                        pass
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump gardeningclassoc1
                " Can we talk about something else? ":
                    k " If that's what you want, then of course. "
                    k " Let's start with a simple question... "
                    k " ...How's your day today, [name]? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Koa. "
                    " Now that you think about it... "
                    " ...You're starting to wonder what Koa was going to talk about. "
                    " Most likely a little bit too late to ask him what he was going to say, buuut... "
                    " If you REALLY want to go back on what he said, then you can just press the back button! "
                    " Yep, anoter fourth wall break. This is going in the top 10 game fourth wall breaks now. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump gardeningclassoc1
        else:
            x " Hmhmm... "
            " He seems to be reading a book. "
            " You didn't want to disturb him in his reading, so you stayed silent. "
            " After a few minutes of him reading, he notices you. "
            x " ...Hi, [name]. "
            x " Sorry if I didn't notice you at first... "
            x " I was kind of busy reading this book. "
            $ koaknow = True
            k " I'm Koa, by the way. Nice to meet you. "
            k " The book I'm reading is about psychology. Orchid showed me this one. "
            k " Never thought I'd see the day where they would reccomend me a book... "
            k " ...Either they just saw it on a video, or they actually read this. "
            k " ... "
            " Koa stays silent for a few more minutes. "
            " Judging by his expressionless expression, you could somehow tell that he wanted to tell you something. "
            " You're not sure on what it is, but it was just...something. "
            " He eventually speaks up about his thoughts after a few minutes of being silent. "
            k " ...[name]. "
            k " Would you be comfortable if I talked to you about something? "
            " He closes the book he was reading and looked down at the ground. "
            k " It's...about my friend. You could consider that me and them...are close. "
            k " It's okay if you'd like to talk about something else though. "
            k " I don't want you to just sit around awkwardly for no reason... "
            menu:
                " Talk to me ":
                    $ koalv += 10
                    k " If you say so. "
                    k " This is about my friend, Orchid... the one I mention earlier. "
                    k " Orchid's great, really. A little clingy, but I don't mind it. "
                    k " Believe it or not, I had to befriend them first. "
                    k " I saw that they were reading a book that I enjoyed so I commented on it: "
                    k " '...Sorry if I'm bothering you or anything, but is that Podoka Pagica?' "
                    k " They proceeded to talk to me about it the rest of the day. "
                    k " Didn't know they were such a die hard fan of the book... "
                    k " Ever since that, we've become friends. Getting closer and closer... "
                    hide koaneutral at bottom
                    show koasad at center
                    stop music fadeout 1.5
                    play music "audio/emotionalmoment.mp3" fadein 2.0
                    k " But, there's things I've noticed about them. "
                    k " They dont exactly interact with others. "
                    k " I thought that they were just struggling a bit and just needed to help them... "
                    k " I did try to help them the best I could, but it always ended up in Orchid themselves feeling embarrassed. "
                    k " Embarrassed by having to end the conversation early because they don't share the same interests as everyone else. "
                    k " I've tried telling them that it's okay to not have the same interests as them, but... "
                    k " They just seemed to not be interested in anything that the others were mentioning. "
                    k " I've tried getting Disk to talk to them - but all Disk could say was that they were being really quiet... "
                    k " ...Disk might've even thought that they were too intimidated due to how popular he was. "
                    k " After a few tries of helping them, I eventually stopped since I didn't want to push them too much. "
                    k " And everything was fine. Until one day... "
                    hide koasad at bottom
                    show koaneutral at center
                    k " ...They texted me in the middle of the night. I had just woken up. "
                    k " They sent me a very long message - venting about how they couldn't be like everyone else. "
                    k " I mean, I get how they felt... "
                    k " It's not every day you'd see a scene kid at your school. "
                    k " And people like them...they'd usually expect to not be accepted. "
                    k " Everyone always talked with them kindly, but they couldn't help but feel as if everything's just a lie. "
                    k " As if this is all just some big prank that everyone's pulling off. "
                    hide koaneutral at bottom
                    show koasad at center
                    k " They even thought I was a part of it too, at some point in me trying to comfort them. "
                    k " I kept reassuring that everyone's not pranking them, and that everything was fine... "
                    k " ...Even if it was hard to get through to them, they eventually calmed down. "
                    k " I don't know how I would feel if I didn't wake up at that time. "
                    k " If I had just ignored the buzzing from my phone. "
                    k " If I just ignored them...they probably would've believed their thoughts due to how deep they were thinking. "
                    k " ...I don't exactly like the idea of them falling so deep into their thoughts, they would... "
                    k " ... "
                    hide koasad at bottom
                    show koaneutral at center
                    stop music fadeout 1.5
                    play music "audio/paperhigh.mp3" fadein 1.5
                    k " If you ever see them around, and if it doesn't bother you... "
                    k " Maybe go ahead and talk about their interests with them. "
                    k " I'm sure that it would make their day better that someone's atleast a little interested. "
                    k " ...Thank you for letting me talk about this. "
                    k " I...don't really want to get you uncomfortable by staying in this topic for long, so... "
                    k " ...How about we talk about something else? How's your day today? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Koa. "
                    " Hmm...maybe you should check out that Orchid person that Koa was talking about. "
                    " Make sure they're okay and everything like that. "
                    " You didn't really like seeing other people suffering. "
                    if kind == True or calm == True:
                        pass
                    elif mean == True:
                        " I mean, you did like some suffering here and there... "
                        " ...But you didn't want something like that to happen to one of your classmates. "
                        pass
                    else:
                        pass
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump gardeningclassoc1
                " Can we talk about something else? ":
                    k " If that's what you want, then of course. "
                    k " Let's start with a simple question... "
                    k " ...How's your day today, [name]? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Koa. "
                    " Now that you think about it... "
                    " ...You're starting to wonder what Koa was going to talk about. "
                    " Most likely a little bit too late to ask him what he was going to say, buuut... "
                    " If you REALLY want to go back on what he said, then you can just press the back button! "
                    " Yep, anoter fourth wall break. This is going in the top 10 game fourth wall breaks now. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump gardeningclassoc1
    label quinnbath:
        # talking about his play
        show quinnneutral at center with easeinleft
        if quinnknow == True:
            q " Hmhmmm...maybe I could make him go here? "
            q " No, no...then he'll get pushed off the stage accidentally. "
            hide quinnneutral at bottom
            show quinnangry at center
            q " With how much the others are moving, then he'd just fall like that... "
            q " This is getting a little bit frustrating, but I can get through this... "
            q " I've been through worse, after all... "
            q " Not like I'm stressing out on how stupid my members are acting... "
            q " I'm TOTALLLYYY fine. "
            q " I can do this. This is fine. I'm fine. "
            " He calmed down and sat in silence for a bit... "
            " ...When the silence got too uncomfortable for you, you decided to ask him if he's doing fine. "
            hide quinnangry at bottom
            show quinnneutral at center
            q " OH!! [name], you're here?? "
            q " Seems like I got a tad bit too distracted with my work, heheh... "
            q " Sorry if I've kept you waiting. "
            q " Anyway - I'm working on this play, right? "
            q " I'm currently trying to decide who would be where on the first scene... "
            q " ...And also so that I could give them an example of how they should act out the first scene. "
            q " My teammates need an example otherwise I'm going to see the theater club room blow up. "
            q " That actually happened on my first day of being in the theater club. "
            q " No one knew where to go, and they were only told to act out the scrip that's been given to them. "
            q " Which is honestly kind of baffling... "
            q " I used to just help the club with props and such, but look at me now! "
            q " The leader, aka...the alpha wolf, heheh. "
            q " Okay, that was cringey, forget that I ever said that. "
            hide quinnneutral at bottom
            show quinnsad at center
            q " Siiigh... I don't know what I'm going to do. "
            q " My teammates are going to have to remember the steps I gave them earlier for the play... "
            q " My play's going to be on friday, too... "
            q " I really do hope everything's going to go well on friday. "
            q " I'll get really embarrassed if even one of them messes up. "
            menu:
                " How about you take a break for now? ":
                    $ quinnlv += 10
                    hide quinnsad at bottom
                    show quinnneutral at center
                    q " I appriecate that you're concerned about me overworking myself too much... "
                    q " ...But I really just have to keep working. "
                    q " Gotta work hard to make things are good after all! "
                    q " I really gotta finish this before school ends. "
                    q " Finishing this tomorrow just makes the deadline closer, and we would barely have any time to practice properly! "
                    q " I've got to work hard - not only to impress everyone... "
                    hide quinnneutral at bottom
                    show quinnhappy at center
                    q " ...Okay, MAYBE I want to impress everyone. "
                    q " But I also want to bring them to tears with how great this play of mine is going to be! "
                    q " Hey! How about you give me some ideas on some placements for my teammates while you're here? "
                    q " I don't want to just keep you around for nothing, after all. "
                    " Well, you had nothing to do. "
                    " Of course you decided to work for him for now. "
                    q " Amazing! "
                    scene black with dissolve
                    " You spent the rest of the break giving Quinn some of the ideas in your head. "
                    " Some of your ideas he didn't really like, but there were also some that he really liked, of course. "
                    " You guys even managed to finish his work before the next class started, wooho!! "
                    " Quinn told you that he'd be making his teammates practice a lot, so... "
                    " Sometimes you're gonna see him, sometimes you won't. "
                    " You DO need more affection points on him so...let's just say I just randomly make him appear. "
                    " Or maybe you don't even need his affection points and just randomly picked a character. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump gardeningclassoc1
                " ... ":
                    hide quinnsad at bottom
                    show quinnneutral at center
                    q " Well...time to get back to work! "
                    q " I really gotta finish this before school ends. "
                    q " Finishing this tomorrow just makes the deadline closer, and we would barely have any time to practice properly! "
                    q " I've got to work hard - not only to impress everyone... "
                    hide quinnneutral at bottom
                    show quinnhappy at center
                    q " ...Okay, MAYBE I want to impress everyone. "
                    q " But I also want to bring them to tears with how great this play of mine is going to be! "
                    q " Hey! How about you give me some ideas on some placements for my teammates while you're here? "
                    q " I don't want to just keep you around for nothing, after all. "
                    " Well, you had nothing to do. "
                    " Of course you decided to work for him for now. "
                    q " Amazing! "
                    scene black with dissolve
                    " You spent the rest of the break giving Quinn some of the ideas in your head. "
                    " Some of your ideas he didn't really like, but there were also some that he really liked, of course. "
                    " You guys even managed to finish his work before the next class started, wooho!! "
                    " Quinn told you that he'd be making his teammates practice a lot, so... "
                    " Sometimes you're gonna see him, sometimes you won't. "
                    " You DO need more affection points on him so...let's just say I just randomly make him appear. "
                    " Or maybe you don't even need his affection points and just randomly picked a character. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump gardeningclassoc1
        else:
            x " Hmhmmm...maybe I could make him go here? "
            x " No, no...then he'll get pushed off the stage accidentally. "
            hide quinnneutral at bottom
            show quinnangry at center
            x " With how much the others are moving, then he'd just fall like that... "
            x " This is getting a little bit frustrating, but I can get through this... "
            x " I've been through worse, after all... "
            x " Not like I'm stressing out on how stupid my members are acting... "
            x " I'm TOTALLLYYY fine. "
            x " I can do this. This is fine. I'm fine. "
            " He calmed down and sat in silence for a bit... "
            " ...When the silence got too uncomfortable for you, you decided to ask him if he's doing fine. "
            hide quinnangry at bottom
            show quinnneutral at center
            x " OH!! [name], you're here?? "
            x " Seems like I got a tad bit too distracted with my work, heheh... "
            x " Sorry if I've kept you waiting. "
            $ quinnknow = True
            q " I'm Quinn, by the way. Disk's younger brother, if you know him. "
            q " Anyway - I'm working on this play, right? "
            q " I'm currently trying to decide who would be where on the first scene... "
            q " ...And also so that I could give them an example of how they should act out the first scene. "
            q " My teammates need an example otherwise I'm going to see the theater club room blow up. "
            q " That actually happened on my first day of being in the theater club. "
            q " No one knew where to go, and they were only told to act out the scrip that's been given to them. "
            q " Which is honestly kind of baffling... "
            q " I used to just help the club with props and such, but look at me now! "
            q " The leader, aka...the alpha wolf, heheh. "
            q " Okay, that was cringey, forget that I ever said that. "
            hide quinnneutral at bottom
            show quinnsad at center
            q " Siiigh... I don't know what I'm going to do. "
            q " My teammates are going to have to remember the steps I gave them earlier for the play... "
            q " My play's going to be on friday, too... "
            q " I really do hope everything's going to go well on friday. "
            q " I'll get really embarrassed if even one of them messes up. "
            menu:
                " How about you take a break for now? ":
                    $ quinnlv += 10
                    hide quinnsad at bottom
                    show quinnneutral at center
                    q " I appriecate that you're concerned about me overworking myself too much... "
                    q " ...But I really just have to keep working. "
                    q " Gotta work hard to make things are good after all! "
                    q " I really gotta finish this before school ends. "
                    q " Finishing this tomorrow just makes the deadline closer, and we would barely have any time to practice properly! "
                    q " I've got to work hard - not only to impress everyone... "
                    hide quinnneutral at bottom
                    show quinnhappy at center
                    q " ...Okay, MAYBE I want to impress everyone. "
                    q " But I also want to bring them to tears with how great this play of mine is going to be! "
                    q " Hey! How about you give me some ideas on some placements for my teammates while you're here? "
                    q " I don't want to just keep you around for nothing, after all. "
                    " Well, you had nothing to do. "
                    " Of course you decided to work for him for now. "
                    q " Amazing! "
                    scene black with dissolve
                    " You spent the rest of the break giving Quinn some of the ideas in your head. "
                    " Some of your ideas he didn't really like, but there were also some that he really liked, of course. "
                    " You guys even managed to finish his work before the next class started, wooho!! "
                    " Quinn told you that he'd be making his teammates practice a lot, so... "
                    " Sometimes you're gonna see him, sometimes you won't. "
                    " You DO need more affection points on him so...let's just say I just randomly make him appear. "
                    " Or maybe you don't even need his affection points and just randomly picked a character. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump gardeningclassoc1
                " ... ":
                    hide quinnsad at bottom
                    show quinnneutral at center
                    q " Well...time to get back to work! "
                    q " I really gotta finish this before school ends. "
                    q " Finishing this tomorrow just makes the deadline closer, and we would barely have any time to practice properly! "
                    q " I've got to work hard - not only to impress everyone... "
                    hide quinnneutral at bottom
                    show quinnhappy at center
                    q " ...Okay, MAYBE I want to impress everyone. "
                    q " But I also want to bring them to tears with how great this play of mine is going to be! "
                    q " Hey! How about you give me some ideas on some placements for my teammates while you're here? "
                    q " I don't want to just keep you around for nothing, after all. "
                    " Well, you had nothing to do. "
                    " Of course you decided to work for him for now. "
                    q " Amazing! "
                    scene black with dissolve
                    " You spent the rest of the break giving Quinn some of the ideas in your head. "
                    " Some of your ideas he didn't really like, but there were also some that he really liked, of course. "
                    " You guys even managed to finish his work before the next class started, wooho!! "
                    " Quinn told you that he'd be making his teammates practice a lot, so... "
                    " Sometimes you're gonna see him, sometimes you won't. "
                    " You DO need more affection points on him so...let's just say I just randomly make him appear. "
                    " Or maybe you don't even need his affection points and just randomly picked a character. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump gardeningclassoc1
label wedback3wed:
    # temero and spark
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " When you arrived to the back of the school, you spotted two of your classmates talking about something. "
    " Bein the nosy guy you were, you decided to pay attention to their conversation. "
    show sparkneutral at right with easeinleft
    show temeroangry at left with easeinleft
    if sparkknow == True and temeroknow == True:
        sp " ...Clio told me that you've been acting up lately. "
        tm " Yeah, and so what?! "
        tm " I've been DYING to get a kill today. "
        tm " Haven't you noticed that things have been boring recently? "
        tm " Ever since that one new student came, no one's been failing their classes! "
        tm " It's as if everyone just wants them to have a good impression on this school! "
        tm " Really, it's just absolutely and utterly stupid! "
        sp " Just because people aren't getting any low grades now, doesn't mean they won't later. "
        sp " It's not like we have to ALWAYS kill. "
        sp " In fact, I remember on the first day - you would always appreciate it whenever we don't go killing. "
        sp " But I guess you've gotten used to the feeling of killing people by now. "
        sp " Still - you should'nt be looking out and trying to get people killed like this. "
        sp " It only makes you more suspicious to our classmates. "
        sp " And the more suspicious you look, the less trust they have in you. "
        tm " So...? "
        sp " So, if you tried making them do something, they won't trust you at all. "
        sp " This is why we have to be seen as friendly and easy to talk to. "
        sp " Otherwise, they all might just figure us out and...you know what Clio said about being found out. "
        sp " You don't want that to happen, don't you? "
        tm " ... "
        sp " Sigh. "
        sp " I'll bring you that one girl that you like from that other school if you behave. "
        hide temeroangry at bottom
        show temerowhenzip at left
        tm " ZIP!!! "
        tm " So when are we visiting her, huh? "
        sp " Oh dear. "
        sp " On saturday or sunday if we have time. "
        tm " YAY!! "
        scene black with dissolve
        " Well that was certainly a interesting conversation you just heard. "
        " You're gonna have to pretend that you didn't hear anything. "
        " You don't want to become their next victim, after all. "
        " That Zip person they mentioned at the end...that name sounds familiar. "
        " Not sure where you've heard of them before though. "
        play sound "audio/bellring.mp3"
        " The bell rings, looks like it's time for your next class. "
        " You walked back into the school and went to your classroom. "
        pause 2.0
        jump gardeningclassoc1
    elif sparkknow == True and temeroknow == False:
        sp " ...Clio told me that you've been acting up lately. "
        x " Yeah, and so what?! "
        x " I've been DYING to get a kill today. "
        x " Haven't you noticed that things have been boring recently? "
        x " Ever since that one new student came, no one's been failing their classes! "
        x " It's as if everyone just wants them to have a good impression on this school! "
        x " Really, it's just absolutely and utterly stupid! "
        sp " Just because people aren't getting any low grades now, doesn't mean they won't later. "
        sp " It's not like we have to ALWAYS kill. "
        sp " In fact, I remember on the first day - you would always appreciate it whenever we don't go killing. "
        sp " But I guess you've gotten used to the feeling of killing people by now. "
        sp " Still - you should'nt be looking out and trying to get people killed like this. "
        sp " It only makes you more suspicious to our classmates. "
        sp " And the more suspicious you look, the less trust they have in you. "
        x " So...? "
        sp " So, if you tried making them do something, they won't trust you at all. "
        sp " This is why we have to be seen as friendly and easy to talk to. "
        sp " Otherwise, they all might just figure us out and...you know what Clio said about being found out. "
        sp " You don't want that to happen, don't you? "
        x " ... "
        sp " Sigh. "
        sp " I'll bring you that one girl that you like from that other school if you behave. "
        hide temeroangry at bottom
        show temerowhenzip at left
        x " ZIP!!! "
        x " So when are we visiting her, huh? "
        sp " Oh dear. "
        sp " On saturday or sunday if we have time. "
        x " YAY!! "
        scene black with dissolve
        " Well that was certainly a interesting conversation you just heard. "
        " You're gonna have to pretend that you didn't hear anything. "
        " You don't want to become their next victim, after all. "
        " That Zip person they mentioned at the end...that name sounds familiar. "
        " Not sure where you've heard of them before though. "
        play sound "audio/bellring.mp3"
        " The bell rings, looks like it's time for your next class. "
        " You walked back into the school and went to your classroom. "
        pause 2.0
        jump gardeningclassoc1
    elif sparkknow == False and temeroknow == True:
        x " ...Clio told me that you've been acting up lately. "
        tm " Yeah, and so what?! "
        tm " I've been DYING to get a kill today. "
        tm " Haven't you noticed that things have been boring recently? "
        tm " Ever since that one new student came, no one's been failing their classes! "
        tm " It's as if everyone just wants them to have a good impression on this school! "
        tm " Really, it's just absolutely and utterly stupid! "
        x " Just because people aren't getting any low grades now, doesn't mean they won't later. "
        x " It's not like we have to ALWAYS kill. "
        x " In fact, I remember on the first day - you would always appreciate it whenever we don't go killing. "
        x " But I guess you've gotten used to the feeling of killing people by now. "
        x " Still - you should'nt be looking out and trying to get people killed like this. "
        x " It only makes you more suspicious to our classmates. "
        x " And the more suspicious you look, the less trust they have in you. "
        tm " So...? "
        x " So, if you tried making them do something, they won't trust you at all. "
        x " This is why we have to be seen as friendly and easy to talk to. "
        x " Otherwise, they all might just figure us out and...you know what Clio said about being found out. "
        x " You don't want that to happen, don't you? "
        tm " ... "
        x " Sigh. "
        x " I'll bring you that one girl that you like from that other school if you behave. "
        hide temeroangry at bottom
        show temerowhenzip at left
        tm " ZIP!!! "
        tm " So when are we visiting her, huh? "
        x " Oh dear. "
        x " On saturday or sunday if we have time. "
        tm " YAY!! "
        scene black with dissolve
        " Well that was certainly a interesting conversation you just heard. "
        " You're gonna have to pretend that you didn't hear anything. "
        " You don't want to become their next victim, after all. "
        " That Zip person they mentioned at the end...that name sounds familiar. "
        " Not sure where you've heard of them before though. "
        play sound "audio/bellring.mp3"
        " The bell rings, looks like it's time for your next class. "
        " You walked back into the school and went to your classroom. "
        pause 2.0
        jump gardeningclassoc1
    else:
        x " ...Clio told me that you've been acting up lately. "
        x " Yeah, and so what?! "
        x " I've been DYING to get a kill today. "
        x " Haven't you noticed that things have been boring recently? "
        x " Ever since that one new student came, no one's been failing their classes! "
        x " It's as if everyone just wants them to have a good impression on this school! "
        x " Really, it's just absolutely and utterly stupid! "
        x " Just because people aren't getting any low grades now, doesn't mean they won't later. "
        x " It's not like we have to ALWAYS kill. "
        x " In fact, I remember on the first day - you would always appreciate it whenever we don't go killing. "
        x " But I guess you've gotten used to the feeling of killing people by now. "
        x " Still - you should'nt be looking out and trying to get people killed like this. "
        x " It only makes you more suspicious to our classmates. "
        x " And the more suspicious you look, the less trust they have in you. "
        x " So...? "
        x " So, if you tried making them do something, they won't trust you at all. "
        x " This is why we have to be seen as friendly and easy to talk to. "
        x " Otherwise, they all might just figure us out and...you know what Clio said about being found out. "
        x " You don't want that to happen, don't you? "
        x " ... "
        x " Sigh. "
        x " I'll bring you that one girl that you like from that other school if you behave. "
        hide temeroangry at bottom
        show temerowhenzip at left
        x " ZIP!!! "
        x " So when are we visiting her, huh? "
        x " Oh dear. "
        x " On saturday or sunday if we have time. "
        x " YAY!! "
        scene black with dissolve
        " Well that was certainly a interesting conversation you just heard. "
        " You're gonna have to pretend that you didn't hear anything. "
        " You don't want to become their next victim, after all. "
        " That Zip person they mentioned at the end...that name sounds familiar. "
        " Not sure where you've heard of them before though. "
        play sound "audio/bellring.mp3"
        " The bell rings, looks like it's time for your next class. "
        " You walked back into the school and went to your classroom. "
        pause 2.0
        jump gardeningclassoc1
label wedgym3wed:
    # carmen and the twins
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked to the gym and spotted three of your classmates hanging out with eachother. "
    " Let's go ahead and see what they're talking about... "
    show carmenneutral at left with easeinright
    show yangyineutral at center with easeinright
    show yinhuineutral at right with easeinright
    if carmenknow,yangyiknow,yinhuiknow == True:
        ca " ...!!! "
        yi " What's that? Oh, [name]'s here. "
        ya " Hey there [name]!! "
        ya " I hope you're doing well as always! "
        ya " Me and Yinhui were just about to listen to Carmen play! "
        yi " I didn't really like this guy at first, so hopefully his music's good. "
        ya " Trust me, it's great! "
        ya " Haven't you heard of him playing his guitar before? "
        ya " He's played it countless of times! "
        yi " I guess I never really cared to actually listen. "
        yi " And now I do care to listen. "
        hide yangyineutral at bottom
        show yangyijoyous at center
        ya " That's wonderful! "
        ca " ... "
        hide yangyijoyous at bottom
        show yangyineutral at center
        ya " Oh, what was that, Carmen? "
        ca " ...? "
        " Carmen points at you, then towards his guitar. "
        " Looks like he's asking you if you wanted to listen to him play. "
        " You're gonna have to think about this one for a bit... "
        " ...You thought about his question, and then made your choice a few moments later. "
        menu:
            " Let's take a listen ":
                $ yinhuilv += 5
                $ yangyilv += 5
                $ carmenlv += 5
                hide yangyineutral at bottom
                show yangyihappy at center
                hide carmenneutral at bottom
                show carmenhappy at left
                ya " Wonderful! "
                yi " Could we get this started already? "
                yi " Kind of wasting time here. "
                ya " Yinhui, be nice. "
                yi " ... "
                ca " ..!! "
                scene black with dissolve
                " You spent the rest of the break listening to Carmen playing his guitar. "
                " You've got to admit, he played the guitar real nicely. "
                " His song had a nice aesthetic feeling to it. Something that reminded you of those lofi beats. "
                " You would listen to those every day a few years ago... "
                " Wonder if they're still doing those lofi beats today. They're such a classic, honestly. "
                " You're going to have to check their channel after school. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
            " I wanna listen to my own music ":
                ya " Well, if that's what you want! "
                yi " Yeah, it's probably lame anyway. "
                ca " ... "
                ya " What did I say about being mean? "
                yi " ...Fine. "
                scene black with dissolve
                " You put on your headsets and spent the rest of the break listening to your own music. "
                " You've heard Carmen play beofre and you'd say it was not bad, "
                " It's just something that you don't prefer. "
                " Or you probably just chose this option to avoid affection points. "
                " That's right, you gain absolutely nothing here. "
                " You either knew that or didn't know that. Most likely didn't, considering this game doesn't have a system to tell you. "
                " About getting affection points and all that.. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
    elif carmenknow,yangyiknow == True and yinhuiknow == False:
        ca " ...!!! "
        x " What's that? Oh, [name]'s here. "
        ya " Hey there [name]!! "
        ya " I hope you're doing well as always! "
        $ yinhuiknow = True
        ya " Me and Yinhui were just about to listen to Carmen play! "
        yi " I didn't really like this guy at first, so hopefully his music's good. "
        ya " Trust me, it's great! "
        ya " Haven't you heard of him playing his guitar before? "
        ya " He's played it countless of times! "
        yi " I guess I never really cared to actually listen. "
        yi " And now I do care to listen. "
        hide yangyineutral at bottom
        show yangyijoyous at center
        ya " That's wonderful! "
        ca " ... "
        hide yangyijoyous at bottom
        show yangyineutral at center
        ya " Oh, what was that, Carmen? "
        ca " ...? "
        " Carmen points at you, then towards his guitar. "
        " Looks like he's asking you if you wanted to listen to him play. "
        " You're gonna have to think about this one for a bit... "
        " ...You thought about his question, and then made your choice a few moments later. "
        menu:
            " Let's take a listen ":
                $ yinhuilv += 5
                $ yangyilv += 5
                $ carmenlv += 5
                hide yangyineutral at bottom
                show yangyihappy at center
                hide carmenneutral at bottom
                show carmenhappy at left
                ya " Wonderful! "
                yi " Could we get this started already? "
                yi " Kind of wasting time here. "
                ya " Yinhui, be nice. "
                yi " ... "
                ca " ..!! "
                scene black with dissolve
                " You spent the rest of the break listening to Carmen playing his guitar. "
                " You've got to admit, he played the guitar real nicely. "
                " His song had a nice aesthetic feeling to it. Something that reminded you of those lofi beats. "
                " You would listen to those every day a few years ago... "
                " Wonder if they're still doing those lofi beats today. They're such a classic, honestly. "
                " You're going to have to check their channel after school. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
            " I wanna listen to my own music ":
                ya " Well, if that's what you want! "
                yi " Yeah, it's probably lame anyway. "
                ca " ... "
                ya " What did I say about being mean? "
                yi " ...Fine. "
                scene black with dissolve
                " You put on your headsets and spent the rest of the break listening to your own music. "
                " You've heard Carmen play beofre and you'd say it was not bad, "
                " It's just something that you don't prefer. "
                " Or you probably just chose this option to avoid affection points. "
                " That's right, you gain absolutely nothing here. "
                " You either knew that or didn't know that. Most likely didn't, considering this game doesn't have a system to tell you. "
                " About getting affection points and all that.. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
    elif carmenknow,yinhuiknow == True and yangyiknow == False:
        ca " ...!!! "
        yi " What's that? Oh, [name]'s here. "
        x " Hey there [name]!! "
        x " I hope you're doing well as always! "
        $ yangyiknow = True
        ya " I'm Yangyi, by the way! Yinhui's twin brother! "
        ya " Me and Yinhui were just about to listen to Carmen play! "
        yi " I didn't really like this guy at first, so hopefully his music's good. "
        ya " Trust me, it's great! "
        ya " Haven't you heard of him playing his guitar before? "
        ya " He's played it countless of times! "
        yi " I guess I never really cared to actually listen. "
        yi " And now I do care to listen. "
        hide yangyineutral at bottom
        show yangyijoyous at center
        ya " That's wonderful! "
        ca " ... "
        hide yangyijoyous at bottom
        show yangyineutral at center
        ya " Oh, what was that, Carmen? "
        ca " ...? "
        " Carmen points at you, then towards his guitar. "
        " Looks like he's asking you if you wanted to listen to him play. "
        " You're gonna have to think about this one for a bit... "
        " ...You thought about his question, and then made your choice a few moments later. "
        menu:
            " Let's take a listen ":
                $ yinhuilv += 5
                $ yangyilv += 5
                $ carmenlv += 5
                hide yangyineutral at bottom
                show yangyihappy at center
                hide carmenneutral at bottom
                show carmenhappy at left
                ya " Wonderful! "
                yi " Could we get this started already? "
                yi " Kind of wasting time here. "
                ya " Yinhui, be nice. "
                yi " ... "
                ca " ..!! "
                scene black with dissolve
                " You spent the rest of the break listening to Carmen playing his guitar. "
                " You've got to admit, he played the guitar real nicely. "
                " His song had a nice aesthetic feeling to it. Something that reminded you of those lofi beats. "
                " You would listen to those every day a few years ago... "
                " Wonder if they're still doing those lofi beats today. They're such a classic, honestly. "
                " You're going to have to check their channel after school. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
            " I wanna listen to my own music ":
                ya " Well, if that's what you want! "
                yi " Yeah, it's probably lame anyway. "
                ca " ... "
                ya " What did I say about being mean? "
                yi " ...Fine. "
                scene black with dissolve
                " You put on your headsets and spent the rest of the break listening to your own music. "
                " You've heard Carmen play beofre and you'd say it was not bad, "
                " It's just something that you don't prefer. "
                " Or you probably just chose this option to avoid affection points. "
                " That's right, you gain absolutely nothing here. "
                " You either knew that or didn't know that. Most likely didn't, considering this game doesn't have a system to tell you. "
                " About getting affection points and all that.. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
    elif yinhuiknow,yangyiknow == True and carmenknow == False:
        x " ...!!! "
        yi " What's that? Oh, [name]'s here. "
        ya " Hey there [name]!! "
        ya " I hope you're doing well as always! "
        $ carmenknow = True
        ya " Me and Yinhui were just about to listen to Carmen play! "
        yi " I didn't really like this guy at first, so hopefully his music's good. "
        ya " Trust me, it's great! "
        ya " Haven't you heard of him playing his guitar before? "
        ya " He's played it countless of times! "
        yi " I guess I never really cared to actually listen. "
        yi " And now I do care to listen. "
        hide yangyineutral at bottom
        show yangyijoyous at center
        ya " That's wonderful! "
        ca " ... "
        hide yangyijoyous at bottom
        show yangyineutral at center
        ya " Oh, what was that, Carmen? "
        ca " ...? "
        " Carmen points at you, then towards his guitar. "
        " Looks like he's asking you if you wanted to listen to him play. "
        " You're gonna have to think about this one for a bit... "
        " ...You thought about his question, and then made your choice a few moments later. "
        menu:
            " Let's take a listen ":
                $ yinhuilv += 5
                $ yangyilv += 5
                $ carmenlv += 5
                hide yangyineutral at bottom
                show yangyihappy at center
                hide carmenneutral at bottom
                show carmenhappy at left
                ya " Wonderful! "
                yi " Could we get this started already? "
                yi " Kind of wasting time here. "
                ya " Yinhui, be nice. "
                yi " ... "
                ca " ..!! "
                scene black with dissolve
                " You spent the rest of the break listening to Carmen playing his guitar. "
                " You've got to admit, he played the guitar real nicely. "
                " His song had a nice aesthetic feeling to it. Something that reminded you of those lofi beats. "
                " You would listen to those every day a few years ago... "
                " Wonder if they're still doing those lofi beats today. They're such a classic, honestly. "
                " You're going to have to check their channel after school. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
            " I wanna listen to my own music ":
                ya " Well, if that's what you want! "
                yi " Yeah, it's probably lame anyway. "
                ca " ... "
                ya " What did I say about being mean? "
                yi " ...Fine. "
                scene black with dissolve
                " You put on your headsets and spent the rest of the break listening to your own music. "
                " You've heard Carmen play beofre and you'd say it was not bad, "
                " It's just something that you don't prefer. "
                " Or you probably just chose this option to avoid affection points. "
                " That's right, you gain absolutely nothing here. "
                " You either knew that or didn't know that. Most likely didn't, considering this game doesn't have a system to tell you. "
                " About getting affection points and all that.. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
    elif carmenknow == True and yinhuiknow,yangyiknow == False:
        ca " ...!!! "
        x " What's that? Oh, [name]'s here. "
        x " Hey there [name]!! "
        x " I hope you're doing well as always! "
        $ yangyiknow = True
        $ yinhuiknow = True
        ya " I'm Yangyi, by the way! I'm Yinhui's twin! "
        ya " Me and Yinhui were just about to listen to Carmen play! "
        yi " I didn't really like this guy at first, so hopefully his music's good. "
        ya " Trust me, it's great! "
        ya " Haven't you heard of him playing his guitar before? "
        ya " He's played it countless of times! "
        yi " I guess I never really cared to actually listen. "
        yi " And now I do care to listen. "
        hide yangyineutral at bottom
        show yangyijoyous at center
        ya " That's wonderful! "
        ca " ... "
        hide yangyijoyous at bottom
        show yangyineutral at center
        ya " Oh, what was that, Carmen? "
        ca " ...? "
        " Carmen points at you, then towards his guitar. "
        " Looks like he's asking you if you wanted to listen to him play. "
        " You're gonna have to think about this one for a bit... "
        " ...You thought about his question, and then made your choice a few moments later. "
        menu:
            " Let's take a listen ":
                $ yinhuilv += 5
                $ yangyilv += 5
                $ carmenlv += 5
                hide yangyineutral at bottom
                show yangyihappy at center
                hide carmenneutral at bottom
                show carmenhappy at left
                ya " Wonderful! "
                yi " Could we get this started already? "
                yi " Kind of wasting time here. "
                ya " Yinhui, be nice. "
                yi " ... "
                ca " ..!! "
                scene black with dissolve
                " You spent the rest of the break listening to Carmen playing his guitar. "
                " You've got to admit, he played the guitar real nicely. "
                " His song had a nice aesthetic feeling to it. Something that reminded you of those lofi beats. "
                " You would listen to those every day a few years ago... "
                " Wonder if they're still doing those lofi beats today. They're such a classic, honestly. "
                " You're going to have to check their channel after school. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
            " I wanna listen to my own music ":
                ya " Well, if that's what you want! "
                yi " Yeah, it's probably lame anyway. "
                ca " ... "
                ya " What did I say about being mean? "
                yi " ...Fine. "
                scene black with dissolve
                " You put on your headsets and spent the rest of the break listening to your own music. "
                " You've heard Carmen play beofre and you'd say it was not bad, "
                " It's just something that you don't prefer. "
                " Or you probably just chose this option to avoid affection points. "
                " That's right, you gain absolutely nothing here. "
                " You either knew that or didn't know that. Most likely didn't, considering this game doesn't have a system to tell you. "
                " About getting affection points and all that.. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
    elif yinhuiknow == True and carmenknow,yangyiknow == False:
        x " ...!!! "
        yi " What's that? Oh, [name]'s here. "
        x " Hey there [name]!! "
        x " I hope you're doing well as always! "
        $ yangyiknow = True
        ya " I'm Yangyi, by the way! Yinhui's twin brother! "
        $ carmenknow = True
        ya " Me and Yinhui were just about to listen to Carmen play! "
        yi " I didn't really like this guy at first, so hopefully his music's good. "
        ya " Trust me, it's great! "
        ya " Haven't you heard of him playing his guitar before? "
        ya " He's played it countless of times! "
        yi " I guess I never really cared to actually listen. "
        yi " And now I do care to listen. "
        hide yangyineutral at bottom
        show yangyijoyous at center
        ya " That's wonderful! "
        ca " ... "
        hide yangyijoyous at bottom
        show yangyineutral at center
        ya " Oh, what was that, Carmen? "
        ca " ...? "
        " Carmen points at you, then towards his guitar. "
        " Looks like he's asking you if you wanted to listen to him play. "
        " You're gonna have to think about this one for a bit... "
        " ...You thought about his question, and then made your choice a few moments later. "
        menu:
            " Let's take a listen ":
                $ yinhuilv += 5
                $ yangyilv += 5
                $ carmenlv += 5
                hide yangyineutral at bottom
                show yangyihappy at center
                hide carmenneutral at bottom
                show carmenhappy at left
                ya " Wonderful! "
                yi " Could we get this started already? "
                yi " Kind of wasting time here. "
                ya " Yinhui, be nice. "
                yi " ... "
                ca " ..!! "
                scene black with dissolve
                " You spent the rest of the break listening to Carmen playing his guitar. "
                " You've got to admit, he played the guitar real nicely. "
                " His song had a nice aesthetic feeling to it. Something that reminded you of those lofi beats. "
                " You would listen to those every day a few years ago... "
                " Wonder if they're still doing those lofi beats today. They're such a classic, honestly. "
                " You're going to have to check their channel after school. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
            " I wanna listen to my own music ":
                ya " Well, if that's what you want! "
                yi " Yeah, it's probably lame anyway. "
                ca " ... "
                ya " What did I say about being mean? "
                yi " ...Fine. "
                scene black with dissolve
                " You put on your headsets and spent the rest of the break listening to your own music. "
                " You've heard Carmen play beofre and you'd say it was not bad, "
                " It's just something that you don't prefer. "
                " Or you probably just chose this option to avoid affection points. "
                " That's right, you gain absolutely nothing here. "
                " You either knew that or didn't know that. Most likely didn't, considering this game doesn't have a system to tell you. "
                " About getting affection points and all that.. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
    elif yangyiknow == True and carmenknow,yinhuiknow == False:
        x " ...!!! "
        x " What's that? Oh, [name]'s here. "
        ya " Hey there [name]!! "
        ya " I hope you're doing well as always! "
        $ yinhuiknow = True
        $ carmenknow = True
        ya " Me and Yinhui were just about to listen to Carmen play! "
        yi " I didn't really like this guy at first, so hopefully his music's good. "
        ya " Trust me, it's great! "
        ya " Haven't you heard of him playing his guitar before? "
        ya " He's played it countless of times! "
        yi " I guess I never really cared to actually listen. "
        yi " And now I do care to listen. "
        hide yangyineutral at bottom
        show yangyijoyous at center
        ya " That's wonderful! "
        ca " ... "
        hide yangyijoyous at bottom
        show yangyineutral at center
        ya " Oh, what was that, Carmen? "
        ca " ...? "
        " Carmen points at you, then towards his guitar. "
        " Looks like he's asking you if you wanted to listen to him play. "
        " You're gonna have to think about this one for a bit... "
        " ...You thought about his question, and then made your choice a few moments later. "
        menu:
            " Let's take a listen ":
                $ yinhuilv += 5
                $ yangyilv += 5
                $ carmenlv += 5
                hide yangyineutral at bottom
                show yangyihappy at center
                hide carmenneutral at bottom
                show carmenhappy at left
                ya " Wonderful! "
                yi " Could we get this started already? "
                yi " Kind of wasting time here. "
                ya " Yinhui, be nice. "
                yi " ... "
                ca " ..!! "
                scene black with dissolve
                " You spent the rest of the break listening to Carmen playing his guitar. "
                " You've got to admit, he played the guitar real nicely. "
                " His song had a nice aesthetic feeling to it. Something that reminded you of those lofi beats. "
                " You would listen to those every day a few years ago... "
                " Wonder if they're still doing those lofi beats today. They're such a classic, honestly. "
                " You're going to have to check their channel after school. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
            " I wanna listen to my own music ":
                ya " Well, if that's what you want! "
                yi " Yeah, it's probably lame anyway. "
                ca " ... "
                ya " What did I say about being mean? "
                yi " ...Fine. "
                scene black with dissolve
                " You put on your headsets and spent the rest of the break listening to your own music. "
                " You've heard Carmen play beofre and you'd say it was not bad, "
                " It's just something that you don't prefer. "
                " Or you probably just chose this option to avoid affection points. "
                " That's right, you gain absolutely nothing here. "
                " You either knew that or didn't know that. Most likely didn't, considering this game doesn't have a system to tell you. "
                " About getting affection points and all that.. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
    else:
        x " ...!!! "
        x " What's that? Oh, [name]'s here. "
        x " Hey there [name]!! "
        x " I hope you're doing well as always! "
        $ yangyiknow = True
        $ yinhuiknow = True
        ya " I'm Yangyi, by the way! I'm Yinhui's twin! "
        $ carmenknow = True
        ya " Me and Yinhui were just about to listen to Carmen play! "
        yi " I didn't really like this guy at first, so hopefully his music's good. "
        ya " Trust me, it's great! "
        ya " Haven't you heard of him playing his guitar before? "
        ya " He's played it countless of times! "
        yi " I guess I never really cared to actually listen. "
        yi " And now I do care to listen. "
        hide yangyineutral at bottom
        show yangyijoyous at center
        ya " That's wonderful! "
        ca " ... "
        hide yangyijoyous at bottom
        show yangyineutral at center
        ya " Oh, what was that, Carmen? "
        ca " ...? "
        " Carmen points at you, then towards his guitar. "
        " Looks like he's asking you if you wanted to listen to him play. "
        " You're gonna have to think about this one for a bit... "
        " ...You thought about his question, and then made your choice a few moments later. "
        menu:
            " Let's take a listen ":
                $ yinhuilv += 5
                $ yangyilv += 5
                $ carmenlv += 5
                hide yangyineutral at bottom
                show yangyihappy at center
                hide carmenneutral at bottom
                show carmenhappy at left
                ya " Wonderful! "
                yi " Could we get this started already? "
                yi " Kind of wasting time here. "
                ya " Yinhui, be nice. "
                yi " ... "
                ca " ..!! "
                scene black with dissolve
                " You spent the rest of the break listening to Carmen playing his guitar. "
                " You've got to admit, he played the guitar real nicely. "
                " His song had a nice aesthetic feeling to it. Something that reminded you of those lofi beats. "
                " You would listen to those every day a few years ago... "
                " Wonder if they're still doing those lofi beats today. They're such a classic, honestly. "
                " You're going to have to check their channel after school. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
            " I wanna listen to my own music ":
                ya " Well, if that's what you want! "
                yi " Yeah, it's probably lame anyway. "
                ca " ... "
                ya " What did I say about being mean? "
                yi " ...Fine. "
                scene black with dissolve
                " You put on your headsets and spent the rest of the break listening to your own music. "
                " You've heard Carmen play beofre and you'd say it was not bad, "
                " It's just something that you don't prefer. "
                " Or you probably just chose this option to avoid affection points. "
                " That's right, you gain absolutely nothing here. "
                " You either knew that or didn't know that. Most likely didn't, considering this game doesn't have a system to tell you. "
                " About getting affection points and all that.. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You get out of the gym and made your way to the gardening classroom. "
                pause 2.0
                jump gardeningclassoc1
label wedcafeteria3wed:
    # disk and nox
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and saw that two of your classmates were talking. "
    " Let's see what they're talking about...you sat next to them. "
    show diskneutral at left with easeinright
    show noxneutral at right with easeinright
    if diskknow == True and noxknow == True:
        d " Hi [name]! Just checking in on Nox... "
        d " He's been sleeping a lot lately! Haven't you, Nox? "
        n " I have, yeah... "
        n " ...I do remember sleeping for 21 hours... "
        d " 21 HOURS?? Jeez, that's a lot of rest! "
        d " Did you not wake up at any point of your sleep...? "
        n " I did, of course.. "
        n " But I just went back to sleep since I didn't feel like doing anything... "
        n " Luckily, that day was on a saturday by the time I woke up, so I didn't miss anything... "
        d " That's great! Though if you did happen to miss anything... "
        d " ...Just know that you can take a good look at my notes, okay? "
        hide noxneutral at bottom
        show noxhappy at right
        n " Mhm... "
        n " Though I mostly won't even remember them... "
        n " Considering how bad my memory is, hah... "
        d " Oh, hehe! I'm sure you can remember a few things! "
        d " Like...um...let's see, what's an easy topic? "
        d " ...Oh! why should you take care of your body every day? "
        d " Like, why do you have to eat, sleep, and um... "
        d " You get the idea! "
        hide noxhappy at bottom
        show noxneutral at right
        n " To keep your body safe and healthy. "
        n " To also keep it free from getting any serious stuff, like illnesses for example... "
        n " ...That's probably the easiest question I've heard... "
        d " I just decided to give you an easy one because I know you wouldn't understand if I asked you a math one. "
        n " ...You know me too well... "
        d " I talk to you enough to the point I know you won't handle the history questions, too!! "
        d " I specifically remember this one time where Mister Clio asked you a question... "
        d " ...And the moment he was done, you fell asleep while standing! "
        d " I know I should be concerned that you did that, but I think it's kinda funny, sorry... "
        n " Mmm... No need to be sorry... "
        hide noxneutral at bottom
        show noxhappy at right
        n " Now that I think about it, it's actually kind of funny for me too.. "
        hide diskneutral at bottom
        show diskhappy at left
        d " Hehe!! we should all talk with eachother more!! "
        n " I agree... "
        scene black with dissolve
        " You spent the rest of the break talking with Disk and Nox. "
        " It was indeed pretty fun talking to them. "
        " Disk and Nox mostly have a yapper and a listener relationship... "
        " ...It's obvious on who is who. "
        " You guys talk about normal school things until Disk starts talking about that one guy he saw at another school. "
        " What's his name? Abbie...? "
        " Sounds familiar, but you're not exactly sure on where you've heard him from. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You walked out of the cafeteria and went to the gardening room for your next class. "
        pause 2.0
        jump gardeningclassoc1
    elif diskknow == True and noxknow == False:
        d " Hi [name]! Just checking in on Nox... "
        d " Nox is my good friend over here! "
        $ noxknow = True
        n " ...Hey there. "
        d " He's been sleeping a lot lately! Haven't you, Nox? "
        n " I have, yeah... "
        n " ...I do remember sleeping for 21 hours... "
        d " 21 HOURS?? Jeez, that's a lot of rest! "
        d " Did you not wake up at any point of your sleep...? "
        n " I did, of course.. "
        n " But I just went back to sleep since I didn't feel like doing anything... "
        n " Luckily, that day was on a saturday by the time I woke up, so I didn't miss anything... "
        d " That's great! Though if you did happen to miss anything... "
        d " ...Just know that you can take a good look at my notes, okay? "
        hide noxneutral at bottom
        show noxhappy at right
        n " Mhm... "
        n " Though I mostly won't even remember them... "
        n " Considering how bad my memory is, hah... "
        d " Oh, hehe! I'm sure you can remember a few things! "
        d " Like...um...let's see, what's an easy topic? "
        d " ...Oh! why should you take care of your body every day? "
        d " Like, why do you have to eat, sleep, and um... "
        d " You get the idea! "
        hide noxhappy at bottom
        show noxneutral at right
        n " To keep your body safe and healthy. "
        n " To also keep it free from getting any serious stuff, like illnesses for example... "
        n " ...That's probably the easiest question I've heard... "
        d " I just decided to give you an easy one because I know you wouldn't understand if I asked you a math one. "
        n " ...You know me too well... "
        d " I talk to you enough to the point I know you won't handle the history questions, too!! "
        d " I specifically remember this one time where Mister Clio asked you a question... "
        d " ...And the moment he was done, you fell asleep while standing! "
        d " I know I should be concerned that you did that, but I think it's kinda funny, sorry... "
        n " Mmm... No need to be sorry... "
        hide noxneutral at bottom
        show noxhappy at right
        n " Now that I think about it, it's actually kind of funny for me too.. "
        hide diskneutral at bottom
        show diskhappy at left
        d " Hehe!! we should all talk with eachother more!! "
        n " I agree... "
        scene black with dissolve
        " You spent the rest of the break talking with Disk and Nox. "
        " It was indeed pretty fun talking to them. "
        " Disk and Nox mostly have a yapper and a listener relationship... "
        " ...It's obvious on who is who. "
        " You guys talk about normal school things until Disk starts talking about that one guy he saw at another school. "
        " What's his name? Abbie...? "
        " Sounds familiar, but you're not exactly sure on where you've heard him from. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You walked out of the cafeteria and went to the gardening room for your next class. "
        pause 2.0
        jump gardeningclassoc1
    elif diskknow == False and noxknow == True:
        x " Hi [name]! Just checking in on Nox... "
        $ diskknow = True
        d " Oh dear, I almost forgot to inroduce myself! I'm Disk, nice to meet you! "
        d " Where were my manners, heha...anyway! "
        d " Nox has been sleeping a lot lately! Haven't you, Nox? "
        n " I have, yeah... "
        n " ...I do remember sleeping for 21 hours... "
        d " 21 HOURS?? Jeez, that's a lot of rest! "
        d " Did you not wake up at any point of your sleep...? "
        n " I did, of course.. "
        n " But I just went back to sleep since I didn't feel like doing anything... "
        n " Luckily, that day was on a saturday by the time I woke up, so I didn't miss anything... "
        d " That's great! Though if you did happen to miss anything... "
        d " ...Just know that you can take a good look at my notes, okay? "
        hide noxneutral at bottom
        show noxhappy at right
        n " Mhm... "
        n " Though I mostly won't even remember them... "
        n " Considering how bad my memory is, hah... "
        d " Oh, hehe! I'm sure you can remember a few things! "
        d " Like...um...let's see, what's an easy topic? "
        d " ...Oh! why should you take care of your body every day? "
        d " Like, why do you have to eat, sleep, and um... "
        d " You get the idea! "
        hide noxhappy at bottom
        show noxneutral at right
        n " To keep your body safe and healthy. "
        n " To also keep it free from getting any serious stuff, like illnesses for example... "
        n " ...That's probably the easiest question I've heard... "
        d " I just decided to give you an easy one because I know you wouldn't understand if I asked you a math one. "
        n " ...You know me too well... "
        d " I talk to you enough to the point I know you won't handle the history questions, too!! "
        d " I specifically remember this one time where Mister Clio asked you a question... "
        d " ...And the moment he was done, you fell asleep while standing! "
        d " I know I should be concerned that you did that, but I think it's kinda funny, sorry... "
        n " Mmm... No need to be sorry... "
        hide noxneutral at bottom
        show noxhappy at right
        n " Now that I think about it, it's actually kind of funny for me too.. "
        hide diskneutral at bottom
        show diskhappy at left
        d " Hehe!! we should all talk with eachother more!! "
        n " I agree... "
        scene black with dissolve
        " You spent the rest of the break talking with Disk and Nox. "
        " It was indeed pretty fun talking to them. "
        " Disk and Nox mostly have a yapper and a listener relationship... "
        " ...It's obvious on who is who. "
        " You guys talk about normal school things until Disk starts talking about that one guy he saw at another school. "
        " What's his name? Abbie...? "
        " Sounds familiar, but you're not exactly sure on where you've heard him from. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You walked out of the cafeteria and went to the gardening room for your next class. "
        pause 2.0
        jump gardeningclassoc1
    else:
        x " Hi [name]! Just checking in on Nox... "
        $ diskknow = True
        d " Oh dear, I almost forgot to inroduce myself! I'm Disk, nice to meet you! "
        d " Where were my manners, heha...anyway! "
        d " I'm sure you haven't met Nox yet - he's my friend over there! "
        $ noxknow = True
        n " ...Hey there. "
        d " Nox has been sleeping a lot lately! Haven't you, Nox? "
        n " I have, yeah... "
        n " ...I do remember sleeping for 21 hours... "
        d " 21 HOURS?? Jeez, that's a lot of rest! "
        d " Did you not wake up at any point of your sleep...? "
        n " I did, of course.. "
        n " But I just went back to sleep since I didn't feel like doing anything... "
        n " Luckily, that day was on a saturday by the time I woke up, so I didn't miss anything... "
        d " That's great! Though if you did happen to miss anything... "
        d " ...Just know that you can take a good look at my notes, okay? "
        hide noxneutral at bottom
        show noxhappy at right
        n " Mhm... "
        n " Though I mostly won't even remember them... "
        n " Considering how bad my memory is, hah... "
        d " Oh, hehe! I'm sure you can remember a few things! "
        d " Like...um...let's see, what's an easy topic? "
        d " ...Oh! why should you take care of your body every day? "
        d " Like, why do you have to eat, sleep, and um... "
        d " You get the idea! "
        hide noxhappy at bottom
        show noxneutral at right
        n " To keep your body safe and healthy. "
        n " To also keep it free from getting any serious stuff, like illnesses for example... "
        n " ...That's probably the easiest question I've heard... "
        d " I just decided to give you an easy one because I know you wouldn't understand if I asked you a math one. "
        n " ...You know me too well... "
        d " I talk to you enough to the point I know you won't handle the history questions, too!! "
        d " I specifically remember this one time where Mister Clio asked you a question... "
        d " ...And the moment he was done, you fell asleep while standing! "
        d " I know I should be concerned that you did that, but I think it's kinda funny, sorry... "
        n " Mmm... No need to be sorry... "
        hide noxneutral at bottom
        show noxhappy at right
        n " Now that I think about it, it's actually kind of funny for me too.. "
        hide diskneutral at bottom
        show diskhappy at left
        d " Hehe!! we should all talk with eachother more!! "
        n " I agree... "
        scene black with dissolve
        " You spent the rest of the break talking with Disk and Nox. "
        " It was indeed pretty fun talking to them. "
        " Disk and Nox mostly have a yapper and a listener relationship... "
        " ...It's obvious on who is who. "
        " You guys talk about normal school things until Disk starts talking about that one guy he saw at another school. "
        " What's his name? Abbie...? "
        " Sounds familiar, but you're not exactly sure on where you've heard him from. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You walked out of the cafeteria and went to the gardening room for your next class. "
        pause 2.0
        jump gardeningclassoc1
label wedrooftop3wed:
    # jacob and matte
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked to the rooftop and spotted two of your classmates doing their own thing. "
    " Who do you want to talk with? "
    if jacobknow == True and matteknow == True:
        menu:
            " {image=jacobicon} Jacob {image=jacobicon} ":
                jump jacobbath
            " {image=matteicon} Matte {image=matteicon} ":
                jump mattebath
    elif jacobknow == True and matteknow == False:
        menu:
            " {image=jacobicon} Jacob {image=jacobicon} ":
                jump jacobbath
            " {image=matteicon} A bored artsy girl {image=matteicon} ":
                jump mattebath
    elif jacobknow == False and matteknow == True:
        menu:
            " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                jump jacobbath
            " {image=matteicon} Matte {image=matteicon} ":
                jump mattebath
    else:
        menu:
            " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                jump jacobbath
            " {image=matteicon} A bored artsy girl {image=matteicon} ":
                jump mattebath
    label jacobbath:
        show jacobneutral at center with easeinleft
        if jacobknow == True:
            jac " ... "
            jac " ... "
            " You cough to get his attention. "
            hide jacobneutral at bottom
            show jacobsurprised at center
            jac " JEEEZERS! " with vpunch
            hide jacobsurprised at bottom
            show jacobneutral at center
            jac " Could've just...poked my shoulder or something, god... "
            jac " But uh, hey there. "
            jac " If you had something to tell me, then you can tell me anything you want right now. "
            jac " Actually, you can tell me that later. "
            jac " I have something I'd like to talk about... "
            jac " ...If you're comfortable about that. "
            menu:
                " Let's talk the talk ":
                    $ jacoblv += 10
                    jac " Alright, so hear me out. "
                    jac " I've been hearing some weird stuff going on in this school... "
                    jac " The first day I got here everything was fine and chill. "
                    jac " Nothing too serious, everyone was being friendly. "
                    jac " On my second week here, I started hearing rumors. Lots of them. "
                    jac " First one was about this ghost in the school. "
                    jac " Now, we actually had to move out of this school and resume education at another school temporarily... "
                    jac " ...Just cause of the whole ghost thing. "
                    jac " According to the teachers, the thing apparently got too out of hand to handle. "
                    jac " Therefore we had to move for a bit. "
                    jac " I don't know what they did, but here's what I can tell you about the rumors. "
                    jac " According to them, a ghost of a dead teacher resides in this school. "
                    jac " And whenever you're all alone in a room, the teacher comes out and asks you if you want to play a game. "
                    jac " Basically asks you to play a game where he gives you five riddles. "
                    jac " If you get all of them right, then you'll live. If you get one of them wrong...you die. "
                    jac " Now you see - I thought it was a joke at first... "
                    jac " But GOD I started believing it the moment I felt like I was going insane. "
                    jac " I kept seeing hallucinations everywhere, it was INSANE! "
                    jac " And I wasn't the only one who's seen them, it was everyone else too! "
                    jac " Aaaaand that's why we had to move out for a bit. "
                    jac " The damn guy got too feral over the fact that he's dead, I guess. "
                    jac " ...But uh, you probably wanna talk about something else by now, so... "
                    jac " What do you wanna talk about? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob. "
                    " You're pretty interested in that thing that Jacob talked about. "
                    " Maybe you could do some ghost hunting later, ooo... "
                    " Oooo foreshadowing or something Oooo... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked down from the rooftop and you went to the gardening classroom for the next class. "
                    pause 2.0
                    jump gardeningclassoc1
                " Nah ":
                    jac " You wanna talk about something else? fine by me. "
                    jac " What do you want? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob. "
                    " You're kind of starting to wonder what he was going to talk about... "
                    " ...Too late to ask him about that now, I guess. "
                    " He's most likely forgotten about what he was going to say to you anyway. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked down from the rooftop and you went to the gardening classroom for the next class. "
                    pause 2.0
                    jump gardeningclassoc1
        else:
            x " ... "
            x " ... "
            " You cough to get his attention. "
            hide jacobneutral at bottom
            show jacobsurprised at center
            x " JEEEZERS! " with vpunch
            hide jacobsurprised at bottom
            show jacobneutral at center
            x " Could've just...poked my shoulder or something, god... "
            x " But uh, hey there. "
            $ jacobknow = True
            jac " I'm Jacob. Nice to meet you. "
            jac " If you had something to tell me, then you can tell me anything you want right now. "
            jac " Actually, you can tell me that later. "
            jac " I have something I'd like to talk about... "
            jac " ...If you're comfortable about that. "
            menu:
                " Let's talk the talk ":
                    $ jacoblv += 10
                    jac " Alright, so hear me out. "
                    jac " I've been hearing some weird stuff going on in this school... "
                    jac " The first day I got here everything was fine and chill. "
                    jac " Nothing too serious, everyone was being friendly. "
                    jac " On my second week here, I started hearing rumors. Lots of them. "
                    jac " First one was about this ghost in the school. "
                    jac " Now, we actually had to move out of this school and resume education at another school temporarily... "
                    jac " ...Just cause of the whole ghost thing. "
                    jac " According to the teachers, the thing apparently got too out of hand to handle. "
                    jac " Therefore we had to move for a bit. "
                    jac " I don't know what they did, but here's what I can tell you about the rumors. "
                    jac " According to them, a ghost of a dead teacher resides in this school. "
                    jac " And whenever you're all alone in a room, the teacher comes out and asks you if you want to play a game. "
                    jac " Basically asks you to play a game where he gives you five riddles. "
                    jac " If you get all of them right, then you'll live. If you get one of them wrong...you die. "
                    jac " Now you see - I thought it was a joke at first... "
                    jac " But GOD I started believing it the moment I felt like I was going insane. "
                    jac " I kept seeing hallucinations everywhere, it was INSANE! "
                    jac " And I wasn't the only one who's seen them, it was everyone else too! "
                    jac " Aaaaand that's why we had to move out for a bit. "
                    jac " The damn guy got too feral over the fact that he's dead, I guess. "
                    jac " ...But uh, you probably wanna talk about something else by now, so... "
                    jac " What do you wanna talk about? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob. "
                    " You're pretty interested in that thing that Jacob talked about. "
                    " Maybe you could do some ghost hunting later, ooo... "
                    " Oooo foreshadowing or something Oooo... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked down from the rooftop and you went to the gardening classroom for the next class. "
                    pause 2.0
                    jump gardeningclassoc1
                " Nah ":
                    jac " You wanna talk about something else? fine by me. "
                    jac " What do you want? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob. "
                    " You're kind of starting to wonder what he was going to talk about... "
                    " ...Too late to ask him about that now, I guess. "
                    " He's most likely forgotten about what he was going to say to you anyway. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked down from the rooftop and you went to the gardening classroom for the next class. "
                    pause 2.0
                    jump gardeningclassoc1
    label mattebath:
        show matteneutral at center with easeinright
        if matteknow == True:
            ma " Hmhmhmmm...oh hey, [name]! "
            ma " I'm just out here and drawing things... "
            ma " ...Just kidding! "
            ma " I'm out here making some theories of the stuff that's been happening recently. "
            ma " You wanna hear it or nah? "
            ma " It's completely fine if you don't want to hear me yap though! "
            ma " We can always talk about something else if you don't feel like talking about something else. "
            ma " Sooo...you wanna hear or not? "
            menu:
                " my ears are comically large for this ":
                    $ mattelv += 10
                    hide matteneutral at bottom
                    show mattehappy at center
                    ma " Great! "
                    ma " So, I've heard all of this from Jacob, but like... "
                    ma " From what he's been observing, everytime someone gets a low score in a test... "
                    ma " ...They'd go missing after a week. "
                    ma " So, he's been thinking that there might be people killing them off! "
                    ma " It's a far stretch, but seriously...why would someone go missing and never come back? "
                    ma " Not even their parents know, apparently... "
                    ma " He's been thinking about a few suspects lately, and I think I have it figured out! "
                    ma " ...It's TOTALLY Jex and Notive! "
                    ma " Notice how you haven't seen them in awhile? "
                    ma " I mean, I know they're still here in the school, but you haven't talked to them in a bit... "
                    ma " For a fact, they've been AVOIDING you because they're off doing something devious! "
                    ma " And they don't want you to know about it because you'd probably tell everyone about it! "
                    ma " I know these are just theories, but I KNOW my suspicions will be right! "
                    ma " ...I'm just not going to talk about it in public. "
                    ma " Just incase if they're not actually the guys who kill. "
                    ma " And also if Jacob is completely wrong. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Matte. "
                    " You're really into that theory she has... "
                    " ...And it is true that you haven't seen Jex and Notive in awhile... "
                    " Totally not because the creator has no idea where to put them. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked down from the rooftop and you went to the gardening classroom for the next class. "
                    pause 2.0
                    jump gardeningclassoc1
                " i have tape over my ears ":
                    ma " Oh no! Tape! "
                    ma " My weakest enemy whenever it comes to yapping! "
                    ma " How will I ever yap to [name] now? "
                    ma " Haha - but seriously, what would you like to talk about? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Matte. "
                    " You're kind of starting to wonder what she was going to talk about... "
                    " ...Too late to ask her about that now, I guess... "
                    " She had most likely forgotten about what he was going to say to you anyway. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked down from the rooftop and you went to the gardening classroom for the next class. "
                    pause 2.0
                    jump gardeningclassoc1
        else:
            x " Hmhmhmmm...oh hey, [name]! "
            $ matteknow = True
            ma " I'm Matte - It's nice to meet you! "
            ma " I'm just out here and drawing things... "
            ma " ...Just kidding! "
            ma " I'm out here making some theories of the stuff that's been happening recently. "
            ma " You wanna hear it or nah? "
            ma " It's completely fine if you don't want to hear me yap though! "
            ma " We can always talk about something else if you don't feel like talking about something else. "
            ma " Sooo...you wanna hear or not? "
            menu:
                " my ears are comically large for this ":
                    $ mattelv += 10
                    hide matteneutral at bottom
                    show mattehappy at center
                    ma " Great! "
                    ma " So, I've heard all of this from Jacob, but like... "
                    ma " From what he's been observing, everytime someone gets a low score in a test... "
                    ma " ...They'd go missing after a week. "
                    ma " So, he's been thinking that there might be people killing them off! "
                    ma " It's a far stretch, but seriously...why would someone go missing and never come back? "
                    ma " Not even their parents know, apparently... "
                    ma " He's been thinking about a few suspects lately, and I think I have it figured out! "
                    ma " ...It's TOTALLY Jex and Notive! "
                    ma " Notice how you haven't seen them in awhile? "
                    ma " I mean, I know they're still here in the school, but you haven't talked to them in a bit... "
                    ma " For a fact, they've been AVOIDING you because they're off doing something devious! "
                    ma " And they don't want you to know about it because you'd probably tell everyone about it! "
                    ma " I know these are just theories, but I KNOW my suspicions will be right! "
                    ma " ...I'm just not going to talk about it in public. "
                    ma " Just incase if they're not actually the guys who kill. "
                    ma " And also if Jacob is completely wrong. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Matte. "
                    " You're really into that theory she has... "
                    " ...And it is true that you haven't seen Jex and Notive in awhile... "
                    " Totally not because the creator has no idea where to put them. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked down from the rooftop and you went to the gardening classroom for the next class. "
                    pause 2.0
                    jump gardeningclassoc1
                " i have tape over my ears ":
                    ma " Oh no! Tape! "
                    ma " My weakest enemy whenever it comes to yapping! "
                    ma " How will I ever yap to [name] now? "
                    ma " Haha - but seriously, what would you like to talk about? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Matte. "
                    " You're kind of starting to wonder what she was going to talk about... "
                    " ...Too late to ask her about that now, I guess... "
                    " She had most likely forgotten about what he was going to say to you anyway. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked down from the rooftop and you went to the gardening classroom for the next class. "
                    pause 2.0
                    jump gardeningclassoc1
label wedlibrary3wed:
    # jam + orchid
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked to the library and spotted two of your classmates doing talking with eachother. "
    " Let's see what they're talking about... "
    show orchidneutral at right with easeinleft
    show jamneutral at left with easeinright
    if orchidknow == True and jamknow == True:
        oc " ...Uh...I like your style! "
        ja " ...Thanks? I like your outfit too. "
        " Seems like they're struggling on talking with eachother. "
        " Maybe you could do something to help them out? "
        " You could mention something that the both of them would like... "
        " ...But of course, You don't really know what their interests are. "
        " Let's take a look at them. "
        " What do you think they would be interested in? "
        " You thought long and hard before coming up with an idea... "
        " Surely this will work. "
        " If it doesn't, welll... too bad then. "
        " You take a deep breath before saying this: "
        mc " There's a Zatzune Ziko event that's happening near here next week saturday! "
        hide orchidneutral at bottom
        show orchidsurprised at right
        oc " REALLY? "
        hide jamneutral at bottom
        show jamsurprised at left
        ja " FOR REAL? "
        ja " Wait...you're into Zatzune Ziko? "
        oc " You too? "
        hide orchidsurprised at bottom
        show orchidhappy at right
        oc " I'm a huge fan! I've got a whole lot of merch of her back at my place! "
        hide jamsurprised at bottom
        show jamhappy at left
        ja " Aw, lucky...my parents would never. "
        ja " They'd think that it's just a waste of money. "
        ja " I mean, it is, but I still wish that I had some sort of merch for her... "
        oc " That sucks...I can give you some of my merch though! "
        oc " I don't mind it, since my parents DO think I have way too much. "
        oc " I have like...about an entire shelf filled with them! "
        oc " And some posters here and there around my room, of course. "
        oc " There IS this old poster I could give you - it was my very first Zatzune merch ever! "
        ja " Really? You sure about me having it...? "
        oc " Yup, no worries! "
        oc " I'll bring it in tomorrow, okay? "
        ja " Yeah, alright! "
        " Mission success. "
        scene black with dissolve
        " You left the two alone to talk, and went to read a book. "
        " Damn, who knew two people could instantly become friends just because they share the same interests? "
        " I mean...that's kinda how friends are. People with kind of the same interests. "
        " But anyway, yeah, you spent the rest of the break reading a random book in the library. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You walked out of the library and went to the gardening classroom. "
        pause 2.0
        jump gardeningclassoc1
    elif orchidknow == True and jamknow == False:
        oc " ...Uh...I like your style! "
        x " ...Thanks? I like your outfit too. "
        " Seems like they're struggling on talking with eachother. "
        " Maybe you could do something to help them out? "
        " You could mention something that the both of them would like... "
        " ...But of course, You don't really know what their interests are. "
        " Let's take a look at them. "
        " What do you think they would be interested in? "
        " You thought long and hard before coming up with an idea... "
        " Surely this will work. "
        " If it doesn't, welll... too bad then. "
        " You take a deep breath before saying this: "
        mc " There's a Zatzune Ziko event that's happening near here next week saturday! "
        hide orchidneutral at bottom
        show orchidsurprised at right
        oc " REALLY? "
        hide jamneutral at bottom
        show jamsurprised at left
        x " FOR REAL? "
        x " Wait...you're into Zatzune Ziko? "
        oc " You too? "
        hide orchidsurprised at bottom
        show orchidhappy at right
        oc " I'm a huge fan! I've got a whole lot of merch of her back at my place! "
        hide jamsurprised at bottom
        show jamhappy at left
        x " Aw, lucky...my parents would never. "
        x " They'd think that it's just a waste of money. "
        x " I mean, it is, but I still wish that I had some sort of merch for her... "
        oc " That sucks...I can give you some of my merch though! "
        oc " I don't mind it, since my parents DO think I have way too much. "
        oc " I have like...about an entire shelf filled with them! "
        oc " And some posters here and there around my room, of course. "
        oc " There IS this old poster I could give you - it was my very first Zatzune merch ever! "
        x " Really? You sure about me having it...? "
        oc " Yup, no worries! "
        oc " I'll bring it in tomorrow, okay? "
        x " Yeah, alright! "
        " Mission success. "
        scene black with dissolve
        " You left the two alone to talk, and went to read a book. "
        " Damn, who knew two people could instantly become friends just because they share the same interests? "
        " I mean...that's kinda how friends are. People with kind of the same interests. "
        " But anyway, yeah, you spent the rest of the break reading a random book in the library. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You walked out of the library and went to the gardening classroom. "
        pause 2.0
        jump gardeningclassoc1
    elif orchidknow == False and jamknow == True:
        x " ...Uh...I like your style! "
        ja " ...Thanks? I like your outfit too. "
        " Seems like they're struggling on talking with eachother. "
        " Maybe you could do something to help them out? "
        " You could mention something that the both of them would like... "
        " ...But of course, You don't really know what their interests are. "
        " Let's take a look at them. "
        " What do you think they would be interested in? "
        " You thought long and hard before coming up with an idea... "
        " Surely this will work. "
        " If it doesn't, welll... too bad then. "
        " You take a deep breath before saying this: "
        mc " There's a Zatzune Ziko event that's happening near here next week saturday! "
        hide orchidneutral at bottom
        show orchidsurprised at right
        x " REALLY? "
        hide jamneutral at bottom
        show jamsurprised at left
        ja " FOR REAL? "
        ja " Wait...you're into Zatzune Ziko? "
        x " You too? "
        hide orchidsurprised at bottom
        show orchidhappy at right
        x " I'm a huge fan! I've got a whole lot of merch of her back at my place! "
        hide jamsurprised at bottom
        show jamhappy at left
        ja " Aw, lucky...my parents would never. "
        ja " They'd think that it's just a waste of money. "
        ja " I mean, it is, but I still wish that I had some sort of merch for her... "
        x " That sucks...I can give you some of my merch though! "
        x " I don't mind it, since my parents DO think I have way too much. "
        x " I have like...about an entire shelf filled with them! "
        x " And some posters here and there around my room, of course. "
        x " There IS this old poster I could give you - it was my very first Zatzune merch ever! "
        ja " Really? You sure about me having it...? "
        x " Yup, no worries! "
        x " I'll bring it in tomorrow, okay? "
        ja " Yeah, alright! "
        " Mission success. "
        scene black with dissolve
        " You left the two alone to talk, and went to read a book. "
        " Damn, who knew two people could instantly become friends just because they share the same interests? "
        " I mean...that's kinda how friends are. People with kind of the same interests. "
        " But anyway, yeah, you spent the rest of the break reading a random book in the library. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You walked out of the library and went to the gardening classroom. "
        pause 2.0
        jump gardeningclassoc1
    else:
        x " ...Uh...I like your style! "
        x " ...Thanks? I like your outfit too. "
        " Seems like they're struggling on talking with eachother. "
        " Maybe you could do something to help them out? "
        " You could mention something that the both of them would like... "
        " ...But of course, You don't really know what their interests are. "
        " Let's take a look at them. "
        " What do you think they would be interested in? "
        " You thought long and hard before coming up with an idea... "
        " Surely this will work. "
        " If it doesn't, welll... too bad then. "
        " You take a deep breath before saying this: "
        mc " There's a Zatzune Ziko event that's happening near here next week saturday! "
        hide orchidneutral at bottom
        show orchidsurprised at right
        x " REALLY? "
        hide jamneutral at bottom
        show jamsurprised at left
        x " FOR REAL? "
        x " Wait...you're into Zatzune Ziko? "
        x " You too? "
        hide orchidsurprised at bottom
        show orchidhappy at right
        x " I'm a huge fan! I've got a whole lot of merch of her back at my place! "
        hide jamsurprised at bottom
        show jamhappy at left
        x " Aw, lucky...my parents would never. "
        x " They'd think that it's just a waste of money. "
        x " I mean, it is, but I still wish that I had some sort of merch for her... "
        x " That sucks...I can give you some of my merch though! "
        x " I don't mind it, since my parents DO think I have way too much. "
        x " I have like...about an entire shelf filled with them! "
        x " And some posters here and there around my room, of course. "
        x " There IS this old poster I could give you - it was my very first Zatzune merch ever! "
        x " Really? You sure about me having it...? "
        x " Yup, no worries! "
        x " I'll bring it in tomorrow, okay? "
        x " Yeah, alright! "
        " Mission success. "
        scene black with dissolve
        " You left the two alone to talk, and went to read a book. "
        " Damn, who knew two people could instantly become friends just because they share the same interests? "
        " I mean...that's kinda how friends are. People with kind of the same interests. "
        " But anyway, yeah, you spent the rest of the break reading a random book in the library. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You walked out of the library and went to the gardening classroom. "
        pause 2.0
        jump gardeningclassoc1

label pythonmeet:
    $ pythonknow = True
    " Inside you saw was nothing. "
    " You look around and it's completely black. "
    " You turn around and saw that the door you went through was gone... "
    " ...Leaving you in the pure darkness. "
    " You look around even more, and eventually find something standing infront of you... "
    " ...No, someone...it's... "
    show pythonmysterious at center with dissolve
    x " It's ME! "
    x " Can't see me? oh well... "
    x " Just give it a moment. "
    x " This WAS for dramatic effect after all! "
    hide pythonmysterious at bottom
    show pythonneutral at center
    py " It's me, PYTHON! "
    py " Aka your narrator throughout this route. "
    py " And also, the BEST CHARACTER IN THIS GAME! "
    py " Well, we can't really confirm that, but let's just say that I am. "
    py " As of this being written, the creator's writing this with their right hand hurting! "
    py " Another thing is that I can switch to any character you'd like! "
    hide pythonneutral at bottom
    show pythonhappy at center
    c " Whether it's a completely different character from a different universe... "
    mst " Or even a teacher! "
    x " Or even someone you haven't met before... "
    " ...Even the narrating dialogue! "
    ju " Character from a story? I've got you! "
    py " I can also change the music, just check this out! "
    stop music fadeout 1.5
    pause 1.5
    play music "audio/credits.wav" fadein 1.5
    py " Right now I'm playing the credits song for this game! "
    py " Hella cool, right? "
    hide pythonhappy at bottom
    show pythonneutral at center
    py " Let's change that back now, I don't like this. "
    stop music fadeout 1.5
    pause 1.5
    play music "audio/paperhigh.mp3" fadein 1.5
    py " Anyway... you can ask me any question you'd like! "
    py " Let's get asking! "
    menu:
        " What are you? ":
            py " Lore-wise, I'm a hacker! "
            py " Originally was supposed to be a robot to check who answered right or wrong, buuut... "
            py " ...I broke out of my code and now I'm free. "
            py " I also used to be human! Now isn't that interesting? "
            hide pythonneutral at bottom
            show pythonangry at center
            py " Whew, now mentioning that kinda gets my blood boiling. "
            py " Really hate remembering that. "
            hide pythonangry at bottom
            show pythonneutral at center
            py " Another thing about me is that I give random students A+'s! "
            py " ...I don't really want them to have the same fate as me. "
            py " Well, barely anyone here fails but whenever there IS someone who needs help.. "
            py " ..I'll help them out! "
            py " But if you're talking game-wise, I'm just a narrator. "
            py " Add in fourth wall breaker! Yes, I see you Jessica. "
            py " You're probably not Jessica, but I love to guess! "
            jump pythonrepeat
        " How do you feel about me? ":
            py " Honestly? nothing. "
            py " While there are some...strange decisions you make... "
            py " I just know that you're being controlled by a weird guy using a computer/laptop to play this game. "
            py " Sooo, I won't be too surprised if you do something stupid! "
            py " Even when I say I am, I'm just acting. "
            py " Really, it makes the story more interesting. "
            jump pythonrepeat
        " Tell me about yourself ":
            hide pythonneutral at bottom
            show pythonhappy at center
            py " About me? Alright! "
            py " I'm nonbinary - I go by they/them pronouns. "
            py " I'm 16 forever, due to me being a robot and all. "
            py " Aaaannnd of course... "
            py " Another thing about me is that I give random students A+'s! "
            py " ...I don't really want them to have the same fate as me. "
            py " Well, barely anyone here fails but whenever there IS someone who needs help.. "
            py " ..I'll help them out! "
            hide pythonhappy at bottom
            show pythonangry at center
            py " Heh, those four dialogues were copy and pasted just now. "
            py " How lazy, but can't really blame the creator. "
            hide pythonangry at bottom
            show pythonhappy at center
            py " I also like to watch you sometimes! "
            hide pythonhappy at bottom
            show pythonneutral at center
            py " ...Only kidding, of course. "
            jump pythonrepeat
        " Miss Hyacinthus ":
            py " Huh? who are you talking about - "
            py " Ohh, that girl! "
            py " Yeah, we genuinely have no clue on how she even got here. "
            py " Not even the programmar himself knows about her. "
            py " One day, she just appeared in the games code! "
            py " But, all we know is that Miss Wisteria doesn't like her that much. "
            py " But uh... "
            py " It would be rude to talk about someone who's listening. "
            stop music
            hide pythonneutral at bottom
            show wisteriaisnthome at center
            " {w=10.0} "
            play music "audio/paperhigh.mp3"
            hide wisteriaisnthome at bottom
            show pythonneutral at center
            py " Eh? what was that? "
            py " Felt like my whole body got ripped off, eheh... "
            py " We should probably move on to our next question. "
            jump pythonrepeat

    label pythonrepeat:
        py " Let's get asking! "
        menu:
            " What are you? ":
                py " Lore-wise, I'm a hacker! "
                py " Originally was supposed to be a robot to check who answered right or wrong, buuut... "
                py " ...I broke out of my code and now I'm free. "
                py " I also used to be human! Now isn't that interesting? "
                hide pythonneutral at bottom
                show pythonangry at center
                py " Whew, now mentioning that kinda gets my blood boiling. "
                py " Really hate remembering that. "
                hide pythonangry at bottom
                show pythonneutral at center
                py " Another thing about me is that I give random students A+'s! "
                py " ...I don't really want them to have the same fate as me. "
                py " Well, barely anyone here fails but whenever there IS someone who needs help.. "
                py " ..I'll help them out! "
                py " But if you're talking game-wise, I'm just a narrator. "
                py " Add in fourth wall breaker! Yes, I see you Jessica. "
                py " You're probably not Jessica, but I love to guess! "
                jump pythonrepeat
            " How do you feel about me? ":
                py " Honestly? nothing. "
                py " While there are some...strange decisions you make... "
                py " I just know that you're being controlled by a weird guy using a computer/laptop to play this game. "
                py " Sooo, I won't be too surprised if you do something stupid! "
                py " Even when I say I am, I'm just acting. "
                py " Really, it makes the story more interesting. "
                jump pythonrepeat
            " Tell me about yourself ":
                hide pythonneutral at bottom
                show pythonhappy at center
                py " About me? Alright! "
                py " I'm nonbinary - I go by they/them pronouns. "
                py " I'm 16 forever, due to me being a robot and all. "
                py " Aaaannnd of course... "
                py " Another thing about me is that I give random students A+'s! "
                py " ...I don't really want them to have the same fate as me. "
                py " Well, barely anyone here fails but whenever there IS someone who needs help.. "
                py " ..I'll help them out! "
                hide pythonhappy at bottom
                show pythonangry at center
                py " Heh, those four dialogues were copy and pasted just now. "
                py " How lazy, but can't really blame the creator. "
                hide pythonangry at bottom
                show pythonhappy at center
                py " I also like to watch you sometimes! "
                hide pythonhappy at bottom
                show pythonneutral at center
                py " ...Only kidding, of course. "
                jump pythonrepeat
            " Miss Hyacinthus ":
                py " Huh? who are you talking about - "
                py " Ohh, that girl! "
                py " Yeah, we genuinely have no clue on how she even got here. "
                py " Not even the programmer himself knows about her. "
                py " One day, she just appeared in the games code! "
                py " And all we know is that Miss Wisteria doesn't like her that much. "
                py " But uh... "
                py " It would be rude to talk about someone who's listening. "
                stop music
                hide pythonneutral at bottom
                show wisteriaisnthome at center
                " {w=5.0} "
                play music "audio/paperhigh.mp3"
                hide wisteriaisnthome at bottom
                show pythonneutral at center
                py " Eh? what was that? "
                py " Felt like my whole body got ripped off, eheh... "
                py " We should probably move on to our next question. "
                jump pythonrepeat
            " I think I should go back now ":
                py " Alrighty! "
                py " Before you go, though... "
                py " Lemme grant ya your well-deserved achievement for doing my quest! "
                $ pythonsend.grant()
                py " Pretty sure you got the achievement by now, so byebye! "
                scene black with dissolve
                pause 2.0
                jump gardeningclassoc1

label gardeningclassoc1:
    scene gardenroom with dissolve
    " You walked into the gardening classroom and waited for the teacher to arrive. "
    " After a bit of waiting, the teacher eventually arrives and everyone greets her. "
    show wisterianeutral at center with easeinleft
    msw " Good morning, class... "
    msw " Hopefully all of you are doing well today... "
    msw " And I do hope that all of you got the materials needed for our activity today. "
    msw " Today, you'll all be individually making and designing signs. "
    msw " Don't warry - I've got some papers and sticks...and also some glue over here... "
    msw " You know those signs where you could tell which plant is which...? "
    msw " ...You guys will basically be doing that... "
    msw " The total points for this would be...100. "
    msw " 50 points for creativity...and add another 50 if you add a funfact about that plant. "
    msw " Please start your work. "
    hide wisterianeutral at right with easeoutright
    " Huh, a non-group activty...activity. "
    " Nice, you don't have to interact with people. "
    " Let's get started with your work then. "
    scene black with dissolve
    " You spent the rest of class hours doing your work. "
    " Once you were done, you passedit over to Miss Wisteria and she graded it. "
    " She eventually gave you an 80. 30 in creativity, and the +50 for the fun fact. "
    " She told you that she was going to use this in her personal garden. "
    " That gives you some cool points! "
    " Now that you've got some time to yourself, you took a look at everyone else's work... "
    " They were fine, but of course there was this one artsy girl who you KNEW was going to get a perfect score. "
    " Absolutely amazing art, I'll tell you that. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for another break. "
    " You got out of the gardening clasroom and went out to the hallways for another break. "
    pause 2.0
    jump wedocbreak4

label wedocbreak4:
    scene hallway with dissolve
    " Where do you want to hang out for this break? "
    menu:
        " {image=noxicon} The front of the school {image=matteicon} ":
            jump wedfront4wed
        " {image=jamicon} The back of the school {image=temeroicon} ":
            jump wedback4wed
        " {image=quinnicon} The gym {image=carmenicon} ":
            jump wedgym4wed
        " {image=orchidicon} The cafeteria {image=koaicon} ":
            jump wedcafeteria4wed
        " {image=diskicon} The rooftop {image=sparkicon} ":
            jump wedrooftop4wed
        " {image=yinyangicon} The library {image=yinyangicon} ":
            jump wedlibrary4wed
label wedfront4wed:
    # nox and matte // skibdii toilet
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of school and spotted your two classmates talking to eachother. "
    " Wanting to join in their conversation, you decided to talk up to them. "
    show noxneutral at left with easeinright
    show matteneutral at right with easeinright
    if noxknow == True and matteknow == True:
        n " Hey there, [name]... "
        ma " Oh, did [name] just get here? "
        ma " Hiya, [name]! "
        ma " Nox here is just helping me get more ideas for painting. "
        ma " I'm starting to get into my painting mood again! "
        ma " Problem is that I don't know what to draw, of course. "
        ma " I don't want to go for anything simple this time... "
        ma " I've painted flowers, clouds, gems...a whole lot of things! "
        ma " But I kinda wanna go for something else... "
        ma " Maybe something symbolic? "
        ma " I honestly don't know how to word it, but something like that. "
        ma " I just want to make something with meaning for once! "
        ma " You two have any ideas? "
        menu:
            " Give her your idea ":
                $ mattelv += 10
                " You thought about your idea before you say it to Matte. "
                " You told her that she could do a painting about being pushed to your limits. "
                " Except you yourself is the one that's pushing yourself like this. "
                " Even no one tells you to, it just feels like you could do better in everything. "
                " Be better in your interests, be better in your school... "
                " ...Kinda making you want to be the best at everything just so that you could be seen as the best choice for everyone. "
                " Even though if it meant harming yourself mentally for all of this. "
                " ...Wow, well that went deeper than expected. "
                " Didn't expect that you'd be diving into the deep ocean for this one. "
                hide matteneutral at bottom
                show mattesad at right
                ma " ...That one hits a little too close to home. "
                ma " But, atleast I'm going to have a good drawing idea! "
                ma " Gonna pour my actual feelings into it and it's gonna look GREAT! "
                n " ...Matte, are you... "
                n " ...Are you really okay...? "
                hide mattesad at bottom
                show matteneutral at right
                ma " Huh? yeah, I'm fine! "
                ma " I've got a new painting idea, after all! "
                ma " New painting ideas ALWAYS gets me excited. "
                n " Hmmm... "
                n " ...You just looked a little down when [name] mentioned that idea of [theirs]... "
                ma " I'm fine, don't worry! "
                scene black with dissolve
                " You spent the rest of the break talking with Matte and Nox. "
                " Nox was right, you did notice her looking a little down when you mentioned your idea. "
                " Looks like it really did hit her close to home. You didn't mean to do that... "
                " ...She looked like you knew that you meant well though, so you're all good. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for another class. "
                " You walked back into the school and went to your next class. "
                pause 2.0
                jump physicsclasswed
            " Listen to Nox's idea ":
                ma " Alright, Nox! What've you got? "
                n " Oh, uh...me? "
                n " I haven't actually thought about it, hm... "
                n " ...How about painting one of your dreams...? "
                n " Specifically any weird ones, for an abstract painting idea. "
                ma " Ooo...sounds interesting! "
                ma " I'll try that, yeah! "
                ma " I do remember having this one odd dream of mine... "
                ma " It was a dream of me being controlled with strings. "
                ma " The other people around me just told me that this was all just a game. "
                ma " Don't know what they were talking about after they told me that... "
                ma " ...What an odd dream, right? "
                n " Mhm...a really odd one... "
                n " I've actually had something similar... "
                scene black with dissolve
                " Okay, let's cut to black before things get weird. "
                " If I let them continue the conversation, then everything would start to get wrong. "
                " And this is not a horror game! "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for another class. "
                " You walked back into the school and went to your next class. "
                pause 2.0
                jump physicsclasswed
    elif noxknow == True and matteknow == False:
        n " Hey there, [name]... "
        x " Oh, did [name] just get here? "
        x " Hiya, [name]! "
        $ matteknow = True
        ma " I'm Matte, by the way. "
        ma " Nox here is just helping me get more ideas for painting. "
        ma " I'm starting to get into my painting mood again! "
        ma " Problem is that I don't know what to draw, of course. "
        ma " I don't want to go for anything simple this time... "
        ma " I've painted flowers, clouds, gems...a whole lot of things! "
        ma " But I kinda wanna go for something else... "
        ma " Maybe something symbolic? "
        ma " I honestly don't know how to word it, but something like that. "
        ma " I just want to make something with meaning for once! "
        ma " You two have any ideas? "
        menu:
            " Give her your idea ":
                $ mattelv += 10
                " You thought about your idea before you say it to Matte. "
                " You told her that she could do a painting about being pushed to your limits. "
                " Except you yourself is the one that's pushing yourself like this. "
                " Even no one tells you to, it just feels like you could do better in everything. "
                " Be better in your interests, be better in your school... "
                " ...Kinda making you want to be the best at everything just so that you could be seen as the best choice for everyone. "
                " Even though if it meant harming yourself mentally for all of this. "
                " ...Wow, well that went deeper than expected. "
                " Didn't expect that you'd be diving into the deep ocean for this one. "
                hide matteneutral at bottom
                show mattesad at right
                ma " ...That one hits a little too close to home. "
                ma " But, atleast I'm going to have a good drawing idea! "
                ma " Gonna pour my actual feelings into it and it's gonna look GREAT! "
                n " ...Matte, are you... "
                n " ...Are you really okay...? "
                hide mattesad at bottom
                show matteneutral at right
                ma " Huh? yeah, I'm fine! "
                ma " I've got a new painting idea, after all! "
                ma " New painting ideas ALWAYS gets me excited. "
                n " Hmmm... "
                n " ...You just looked a little down when [name] mentioned that idea of [theirs]... "
                ma " I'm fine, don't worry! "
                scene black with dissolve
                " You spent the rest of the break talking with Matte and Nox. "
                " Nox was right, you did notice her looking a little down when you mentioned your idea. "
                " Looks like it really did hit her close to home. You didn't mean to do that... "
                " ...She looked like you knew that you meant well though, so you're all good. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for another class. "
                " You walked back into the school and went to your next class. "
                pause 2.0
                jump physicsclasswed
            " Listen to Nox's idea ":
                ma " Alright, Nox! What've you got? "
                n " Oh, uh...me? "
                n " I haven't actually thought about it, hm... "
                n " ...How about painting one of your dreams...? "
                n " Specifically any weird ones, for an abstract painting idea. "
                ma " Ooo...sounds interesting! "
                ma " I'll try that, yeah! "
                ma " I do remember having this one odd dream of mine... "
                ma " It was a dream of me being controlled with strings. "
                ma " The other people around me just told me that this was all just a game. "
                ma " Don't know what they were talking about after they told me that... "
                ma " ...What an odd dream, right? "
                n " Mhm...a really odd one... "
                n " I've actually had something similar... "
                scene black with dissolve
                " Okay, let's cut to black before things get weird. "
                " If I let them continue the conversation, then everything would start to get wrong. "
                " And this is not a horror game! "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for another class. "
                " You walked back into the school and went to your next class. "
                pause 2.0
                jump physicsclasswed
    elif noxknow == False and matteknow == True:
        x " Hey there, [name]... "
        ma " Oh, did [name] just get here? "
        ma " Hiya, [name]! "
        $ noxknow = True
        ma " Nox here is just helping me get more ideas for painting. "
        ma " I'm starting to get into my painting mood again! "
        ma " Problem is that I don't know what to draw, of course. "
        ma " I don't want to go for anything simple this time... "
        ma " I've painted flowers, clouds, gems...a whole lot of things! "
        ma " But I kinda wanna go for something else... "
        ma " Maybe something symbolic? "
        ma " I honestly don't know how to word it, but something like that. "
        ma " I just want to make something with meaning for once! "
        ma " You two have any ideas? "
        menu:
            " Give her your idea ":
                $ mattelv += 10
                " You thought about your idea before you say it to Matte. "
                " You told her that she could do a painting about being pushed to your limits. "
                " Except you yourself is the one that's pushing yourself like this. "
                " Even no one tells you to, it just feels like you could do better in everything. "
                " Be better in your interests, be better in your school... "
                " ...Kinda making you want to be the best at everything just so that you could be seen as the best choice for everyone. "
                " Even though if it meant harming yourself mentally for all of this. "
                " ...Wow, well that went deeper than expected. "
                " Didn't expect that you'd be diving into the deep ocean for this one. "
                hide matteneutral at bottom
                show mattesad at right
                ma " ...That one hits a little too close to home. "
                ma " But, atleast I'm going to have a good drawing idea! "
                ma " Gonna pour my actual feelings into it and it's gonna look GREAT! "
                n " ...Matte, are you... "
                n " ...Are you really okay...? "
                hide mattesad at bottom
                show matteneutral at right
                ma " Huh? yeah, I'm fine! "
                ma " I've got a new painting idea, after all! "
                ma " New painting ideas ALWAYS gets me excited. "
                n " Hmmm... "
                n " ...You just looked a little down when [name] mentioned that idea of [theirs]... "
                ma " I'm fine, don't worry! "
                scene black with dissolve
                " You spent the rest of the break talking with Matte and Nox. "
                " Nox was right, you did notice her looking a little down when you mentioned your idea. "
                " Looks like it really did hit her close to home. You didn't mean to do that... "
                " ...She looked like you knew that you meant well though, so you're all good. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for another class. "
                " You walked back into the school and went to your next class. "
                pause 2.0
                jump physicsclasswed
            " Listen to Nox's idea ":
                ma " Alright, Nox! What've you got? "
                n " Oh, uh...me? "
                n " I haven't actually thought about it, hm... "
                n " ...How about painting one of your dreams...? "
                n " Specifically any weird ones, for an abstract painting idea. "
                ma " Ooo...sounds interesting! "
                ma " I'll try that, yeah! "
                ma " I do remember having this one odd dream of mine... "
                ma " It was a dream of me being controlled with strings. "
                ma " The other people around me just told me that this was all just a game. "
                ma " Don't know what they were talking about after they told me that... "
                ma " ...What an odd dream, right? "
                n " Mhm...a really odd one... "
                n " I've actually had something similar... "
                scene black with dissolve
                " Okay, let's cut to black before things get weird. "
                " If I let them continue the conversation, then everything would start to get wrong. "
                " And this is not a horror game! "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for another class. "
                " You walked back into the school and went to your next class. "
                pause 2.0
                jump physicsclasswed
    else:
        x " Hey there, [name]... "
        x " Oh, did [name] just get here? "
        x " Hiya, [name]! "
        $ matteknow = True
        ma " I'm Matte, by the way. "
        $ noxknow = True
        ma " Nox here is just helping me get more ideas for painting. "
        ma " I'm starting to get into my painting mood again! "
        ma " Problem is that I don't know what to draw, of course. "
        ma " I don't want to go for anything simple this time... "
        ma " I've painted flowers, clouds, gems...a whole lot of things! "
        ma " But I kinda wanna go for something else... "
        ma " Maybe something symbolic? "
        ma " I honestly don't know how to word it, but something like that. "
        ma " I just want to make something with meaning for once! "
        ma " You two have any ideas? "
        menu:
            " Give her your idea ":
                $ mattelv += 10
                " You thought about your idea before you say it to Matte. "
                " You told her that she could do a painting about being pushed to your limits. "
                " Except you yourself is the one that's pushing yourself like this. "
                " Even no one tells you to, it just feels like you could do better in everything. "
                " Be better in your interests, be better in your school... "
                " ...Kinda making you want to be the best at everything just so that you could be seen as the best choice for everyone. "
                " Even though if it meant harming yourself mentally for all of this. "
                " ...Wow, well that went deeper than expected. "
                " Didn't expect that you'd be diving into the deep ocean for this one. "
                hide matteneutral at bottom
                show mattesad at right
                ma " ...That one hits a little too close to home. "
                ma " But, atleast I'm going to have a good drawing idea! "
                ma " Gonna pour my actual feelings into it and it's gonna look GREAT! "
                n " ...Matte, are you... "
                n " ...Are you really okay...? "
                hide mattesad at bottom
                show matteneutral at right
                ma " Huh? yeah, I'm fine! "
                ma " I've got a new painting idea, after all! "
                ma " New painting ideas ALWAYS gets me excited. "
                n " Hmmm... "
                n " ...You just looked a little down when [name] mentioned that idea of [theirs]... "
                ma " I'm fine, don't worry! "
                scene black with dissolve
                " You spent the rest of the break talking with Matte and Nox. "
                " Nox was right, you did notice her looking a little down when you mentioned your idea. "
                " Looks like it really did hit her close to home. You didn't mean to do that... "
                " ...She looked like you knew that you meant well though, so you're all good. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for another class. "
                " You walked back into the school and went to your next class. "
                pause 2.0
                jump physicsclasswed
            " Listen to Nox's idea ":
                ma " Alright, Nox! What've you got? "
                n " Oh, uh...me? "
                n " I haven't actually thought about it, hm... "
                n " ...How about painting one of your dreams...? "
                n " Specifically any weird ones, for an abstract painting idea. "
                ma " Ooo...sounds interesting! "
                ma " I'll try that, yeah! "
                ma " I do remember having this one odd dream of mine... "
                ma " It was a dream of me being controlled with strings. "
                ma " The other people around me just told me that this was all just a game. "
                ma " Don't know what they were talking about after they told me that... "
                ma " ...What an odd dream, right? "
                n " Mhm...a really odd one... "
                n " I've actually had something similar... "
                scene black with dissolve
                " Okay, let's cut to black before things get weird. "
                " If I let them continue the conversation, then everything would start to get wrong. "
                " And this is not a horror game! "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for another class. "
                " You walked back into the school and went to your next class. "
                pause 2.0
                jump physicsclasswed
label wedback4wed:
    # jam and temero
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and spotted your two classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if jamknow == True and temeroknow == True:
        menu:
            " {image=jamicon} Jam {image=jamicon} ":
                jump saiso
            " {image=temeroicon} Temero {image=temeroicon} ":
                jump woahso
    elif jamknow == True and temeroknow == False:
        menu:
            " {image=jamicon} Jam {image=jamicon} ":
                jump saiso
            " {image=temeroicon} A mad scientist looking girl {image=temeroicon} ":
                jump woahso
    elif jamknow == False and temeroknow == True:
        menu:
            " {image=jamicon} A mean looking girl {image=jamicon} ":
                jump saiso
            " {image=temeroicon} Temero {image=temeroicon} ":
                jump woahso
    else:
        menu:
            " {image=jamicon} A mean looking girl {image=jamicon} ":
                jump saiso
            " {image=temeroicon} A mad scientist looking girl {image=temeroicon} ":
                jump woahso
    label saiso:
        show jamgame at center with easeinleft
        if jamknow == True:
            ja " ... "
            " Looks like she's busy playing a game. "
            " You don't want to get her distracted, looks like her team is winning. "
            " You just waited patiently for the match to end. "
            ja " Come on, their healer isn't even helping... "
            ja " That one guy with a gun has horrible aim... "
            ja " Pretty sure their tank is the only one who knows how to play. "
            ja " Should be an easy wipe if we keep jumping them... "
            ja " Match is about to end in a few seconds, anyway. Three, two, one... "
            ja " Easy win. Good game. "
            hide jamgame at bottom
            show jamneutral at center
            " Huh, looks like her team DID win. "
            " She did say that it was eay... "
            " She put her phone back into her pocket, looking around before eventually seeing you. "
            ja " Oh, hey there [name]. Sorry if I kept you waiting. "
            ja " Was just on one of my favorite games. "
            ja " It's pretty underrated, and it's really well made. "
            ja " Too bad only a few people know of it... "
            ja " Hold on, what am I saying? it's not that underrated anymore. "
            ja " Guess I'm just stuck in that era where it was more less known. "
            ja " Anyway - it's stilla tad bit underrated, but the community's bigger now. "
            ja " Everyone in the community makes good content, really... "
            ja " Commentaries started showing up, gameplays, even animation memes. "
            ja " You KNOW your game is good when they've got animation memes. "
            ja " While the community is good, of course there's people who... are just genuinely disgusting. "
            hide jamneutral at bottom
            show jamangry at center
            ja " Like, I know every community's going to have their bad apples, but come on... "
            ja " Could you ATLEAST hold yourself back from shipping a father and his son? Like, dude. Not cool if you like that stuff. "
            ja " People should start learing to hold some of their opinions in, in all honesty. "
            ja " Not everything should be said outloud to be put on the internet, jesus christ. "
            hide jamangry at bottom
            show jamneutral at center
            ja " ...Sorry, just had to blow off some steam. "
            ja " Just really tired of how this community has been acting. "
            ja " You have no idea how often there's toxic players in every single lobby. "
            ja " But, there ARE some servers where they're all fine. "
            ja " Just chill, relaxing...you might even get to have some fun and talk with the people there. "
            ja " Though those are pretty rare to see nowadays. "
            ja " In the end, I just close the chat, and play like how I normally do. "
            ja " Best to just ignore than to make a huge fuss over it. "
            ja " They're making things bad, so don't make it worse. "
            ja " You're just asking up for a death wish over there. "
            scene black with dissolve
            " You spent the rest of the break talking with Jam. "
            " She IS right, sometimes fandoms are just...weird. "
            " But, there's no pure good fandom other than the ones that are less known and more obscure. "
            " The moment that fandom is going to get popular, there's ought to be rotten apples. "
            " Rotten apples who'll ruin the entire barrel, but we can't do anything about it since they can't and won't change. "
            " It's just a fandom thing, really. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You walked back into the school and walked to your classroom. "
            pause 2.0
            jump physicsclasswed
        else:
            x " ... "
            " Looks like she's busy playing a game. "
            " You don't want to get her distracted, looks like her team is winning. "
            " You just waited patiently for the match to end. "
            x " Come on, their healer isn't even helping... "
            x " That one guy with a gun has horrible aim... "
            x " Pretty sure their tank is the only one who knows how to play. "
            x " Should be an easy wipe if we keep jumping them... "
            x " Match is about to end in a few seconds, anyway. Three, two, one... "
            x " Easy win. Good game. "
            hide jamgame at bottom
            show jamneutral at center
            " Huh, looks like her team DID win. "
            " She did say that it was eay... "
            " She put her phone back into her pocket, looking around before eventually seeing you. "
            x " Oh, hey there [name]. Sorry if I kept you waiting. "
            x " Was just on one of my favorite games. "
            $ jamknow = True
            ja " I'm Jam by the way, nice to meet you. "
            ja " The game I was playing is pretty underrated, and it's really well made. "
            ja " Too bad only a few people know of it... "
            ja " Hold on, what am I saying? it's not that underrated anymore. "
            ja " Guess I'm just stuck in that era where it was more less known. "
            ja " Anyway - it's stilla tad bit underrated, but the community's bigger now. "
            ja " Everyone in the community makes good content, really... "
            ja " Commentaries started showing up, gameplays, even animation memes. "
            ja " You KNOW your game is good when they've got animation memes. "
            ja " While the community is good, of course there's people who... are just genuinely disgusting. "
            hide jamneutral at bottom
            show jamangry at center
            ja " Like, I know every community's going to have their bad apples, but come on... "
            ja " Could you ATLEAST hold yourself back from shipping a father and his son? Like, dude. Not cool if you like that stuff. "
            ja " People should start learing to hold some of their opinions in, in all honesty. "
            ja " Not everything should be said outloud to be put on the internet, jesus christ. "
            hide jamangry at bottom
            show jamneutral at center
            ja " ...Sorry, just had to blow off some steam. "
            ja " Just really tired of how this community has been acting. "
            ja " You have no idea how often there's toxic players in every single lobby. "
            ja " But, there ARE some servers where they're all fine. "
            ja " Just chill, relaxing...you might even get to have some fun and talk with the people there. "
            ja " Though those are pretty rare to see nowadays. "
            ja " In the end, I just close the chat, and play like how I normally do. "
            ja " Best to just ignore than to make a huge fuss over it. "
            ja " They're making things bad, so don't make it worse. "
            ja " You're just asking up for a death wish over there. "
            scene black with dissolve
            " You spent the rest of the break talking with Jam. "
            " She IS right, sometimes fandoms are just...weird. "
            " But, there's no pure good fandom other than the ones that are less known and more obscure. "
            " The moment that fandom is going to get popular, there's ought to be rotten apples. "
            " Rotten apples who'll ruin the entire barrel, but we can't do anything about it since they can't and won't change. "
            " It's just a fandom thing, really. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You walked back into the school and walked to your classroom. "
            pause 2.0
            jump physicsclasswed
    label woahso:
        show temeroneutral at center with easeinright
        if temeroknow == True:
            " You walked over to her, looks like she was doing a little science experiment. "
            tm " Mmm...I can't remember if I should put this in or not. "
            tm " Maybe just a little bit of this? "
            tm " And also some of that, I remember that part being very clear... "
            tm " Hopefully I don't accidentally blow up the entire school. "
            " She pours a few things into a bowl, and... "
            " ...The bowl makes a tiny explosion on the ground. "
            " Only just a few pieces of the bowl exist now. "
            hide temeroneutral at bottom
            show temeroangry at center
            tm " Eeeyikes. Yeah, that was DEFINITELY not in the recipe. "
            tm " Good thing I have an extra bowl with me... "
            tm " If only my recipe book decided to stay put in my laboratory... "
            tm " God damn it, Carnation probably stole it and put it in the attic again. "
            tm " That damned butterfly, how come Spark's buddy can stay put but not MINE?! "
            tm " Jeez...Carnation was more behaved when I first got... "
            hide temeroangry at bottom
            show temeroneutral at center
            tm " Oh, hey there, [name]! "
            " Huh. Looks like she completely changed the moment she saw you. "
            " Wonder what she was gonna say... "
            tm " I was just doing a little experiment over here. "
            tm " I have to make some glowing and glittery paint for Matte... "
            tm " ...Apparently she's working on another art piece! "
            tm " Though I wonder what kind of art piece she's making if she's asking ME for help. "
            hide temeroneutral at bottom
            show temerohappy at center
            tm " I'm happy to help nonetheless! "
            tm " She's a really nice girl, love her. "
            hide temerohappy at bottom
            show temeroneutral at center
            tm " Oooh, I don't think I've mentioned something to you yet! "
            tm " You wanna talk to me while I do my work? "
            menu:
                " Sure ":
                    $ temerolv += 10
                    tm " Alright! If that's what you want, then sure! "
                    " Temero then gets to work on her little project. "
                    " She was just mixing some random chemicals and was hoping for it to work. "
                    " Probably not gonna work, but she was hoping, and hoping a lot. "
                    tm " Sooo... "
                    tm " I dunno if anyone elses told you this, but we had to move schools for a bit. "
                    tm " Due to some stuff that happened - they never really explained it. "
                    tm " Probably nothing interesting though. "
                    tm " While we were at that school, we were treated like DAMN royalty! "
                    tm " I mean, this IS a private school. Of course people from a public school would be flabbergasted at how good we are! "
                    tm " Everytime we went out on the hallways, they'd start whispering about how cool we were! "
                    tm " Anyway...I met this one girl named Zip. "
                    tm " I was just making my science assignment, and she decided to tip a bottle over. "
                    hide temeroneutral at bottom
                    show temeroangry at center
                    tm " Luckily I managed to catch it before it fell onto the ground. "
                    tm " I was pissed as hell though - of course I would be! "
                    tm " I told her: 'Hey, what the hell -' "
                    hide temeroangry at bottom
                    show temerowhenzip at center
                    tm " And that's when I saw her glorious face! "
                    tm " She looked so pretty, according to her... "
                    tm " I was as a tomato while looking down at her! "
                    tm " I mean, how could I not be? "
                    tm " She was the FINE SHIT, dude! "
                    tm " People called me weird for liking a bully, and I just kept telling them that she's not! "
                    tm " That's just her way of showing affection, really... "
                    tm " No one believed me, of course. But I don't care that much. "
                    hide temerowhenzip at bottom
                    show temerohappy at center
                    " Temero eventually managed to make something that was glowing. "
                    " She looked back at her extra bowl - and she made it! "
                    tm " Oh, great! I did it! "
                    tm " I'll have to get going now, [name]. "
                    tm " Have to deliver this to Matte! "
                    tm " I'll see you later in class, byebye! "
                    hide temerohappy at right with easeoutright
                    " ...You're going to go and walk around the school for a bit. "
                    " How else would you like to spend the rest of the break? "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " Now that you think about it, you wonder how that painting Temero mentioned is gonna look like. "
                    " Maybe you should check it once it's done. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and walked to your classroom. "
                    pause 2.0
                    jump physicsclasswed
                " I have other places to be ":
                    tm " Oh, really? "
                    tm " Is that you trying to find an excuse not to talk to me? "
                    tm " Wow, I'm hurt... "
                    tm " Just kidding, obviously. "
                    tm " Go ahead and do whatever you wanted! "
                    tm " If you need something, just come back here. "
                    tm " I'm sure I'll be here for a bit... "
                    tm " ...Considering that this place is the only safest option for me to do experiments. "
                    tm " Go now! "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " Now that you think about it, you wonder how that painting Temero mentioned is gonna look like. "
                    " Maybe you should check it once it's done. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and walked to your classroom. "
                    pause 2.0
                    jump physicsclasswed
        else:
            " You walked over to her, looks like she was doing a little science experiment. "
            x " Mmm...I can't remember if I should put this in or not. "
            x " Maybe just a little bit of this? "
            x " And also some of that, I remember that part being very clear... "
            x " Hopefully I don't accidentally blow up the entire school. "
            " She pours a few things into a bowl, and... "
            " ...The bowl makes a tiny explosion on the ground. "
            " Only just a few pieces of the bowl exist now. "
            hide temeroneutral at bottom
            show temeroangry at center
            x " Eeeyikes. Yeah, that was DEFINITELY not in the recipe. "
            x " Good thing I have an extra bowl with me... "
            x " If only my recipe book decided to stay put in my laboratory... "
            x " God damn it, Carnation probably stole it and put it in the attic again. "
            x " That damned butterfly, how come Spark's buddy can stay put but not MINE?! "
            x " Jeez...Carnation was more behaved when I first got... "
            hide temeroangry at bottom
            show temeroneutral at center
            x " Oh, hey there, [name]! "
            " Huh. Looks like she completely changed the moment she saw you. "
            " Wonder what she was gonna say... "
            $ temeroknow = True
            tm " I believe we haven't met before, so...I'm Temero! Nice to meet you! "
            tm " I was just doing a little experiment over here. "
            tm " I have to make some glowing and glittery paint for Matte... "
            tm " ...Apparently she's working on another art piece! "
            tm " Though I wonder what kind of art piece she's making if she's asking ME for help. "
            hide temeroneutral at bottom
            show temerohappy at center
            tm " I'm happy to help nonetheless! "
            tm " She's a really nice girl, love her. "
            hide temerohappy at bottom
            show temeroneutral at center
            tm " Oooh, I don't think I've mentioned something to you yet! "
            tm " You wanna talk to me while I do my work? "
            menu:
                " Sure ":
                    $ temerolv += 10
                    tm " Alright! If that's what you want, then sure! "
                    " Temero then gets to work on her little project. "
                    " She was just mixing some random chemicals and was hoping for it to work. "
                    " Probably not gonna work, but she was hoping, and hoping a lot. "
                    tm " Sooo... "
                    tm " I dunno if anyone elses told you this, but we had to move schools for a bit. "
                    tm " Due to some stuff that happened - they never really explained it. "
                    tm " Probably nothing interesting though. "
                    tm " While we were at that school, we were treated like DAMN royalty! "
                    tm " I mean, this IS a private school. Of course people from a public school would be flabbergasted at how good we are! "
                    tm " Everytime we went out on the hallways, they'd start whispering about how cool we were! "
                    tm " Anyway...I met this one girl named Zip. "
                    tm " I was just making my science assignment, and she decided to tip a bottle over. "
                    hide temeroneutral at bottom
                    show temeroangry at center
                    tm " Luckily I managed to catch it before it fell onto the ground. "
                    tm " I was pissed as hell though - of course I would be! "
                    tm " I told her: 'Hey, what the hell -' "
                    hide temeroangry at bottom
                    show temerowhenzip at center
                    tm " And that's when I saw her glorious face! "
                    tm " She looked so pretty, according to her... "
                    tm " I was as a tomato while looking down at her! "
                    tm " I mean, how could I not be? "
                    tm " She was the FINE SHIT, dude! "
                    tm " People called me weird for liking a bully, and I just kept telling them that she's not! "
                    tm " That's just her way of showing affection, really... "
                    tm " No one believed me, of course. But I don't care that much. "
                    hide temerowhenzip at bottom
                    show temerohappy at center
                    " Temero eventually managed to make something that was glowing. "
                    " She looked back at her extra bowl - and she made it! "
                    tm " Oh, great! I did it! "
                    tm " I'll have to get going now, [name]. "
                    tm " Have to deliver this to Matte! "
                    tm " I'll see you later in class, byebye! "
                    hide temerohappy at right with easeoutright
                    " ...You're going to go and walk around the school for a bit. "
                    " How else would you like to spend the rest of the break? "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " Now that you think about it, you wonder how that painting Temero mentioned is gonna look like. "
                    " Maybe you should check it once it's done. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and walked to your classroom. "
                    pause 2.0
                    jump physicsclasswed
                " I have other places to be ":
                    tm " Oh, really? "
                    tm " Is that you trying to find an excuse not to talk to me? "
                    tm " Wow, I'm hurt... "
                    tm " Just kidding, obviously. "
                    tm " Go ahead and do whatever you wanted! "
                    tm " If you need something, just come back here. "
                    tm " I'm sure I'll be here for a bit... "
                    tm " ...Considering that this place is the only safest option for me to do experiments. "
                    tm " Go now! "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " Now that you think about it, you wonder how that painting Temero mentioned is gonna look like. "
                    " Maybe you should check it once it's done. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and walked to your classroom. "
                    pause 2.0
                    jump physicsclasswed
label wedgym4wed:
    # quinn and carmen
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym and found two of your classmates just doing their own things. "
    " You wanted to talk to one of them...but who? "
    if quinnknow == True and carmenknow == True:
        menu:
            " {image=quinnicon} Quinn {image=quinnicon} ":
                jump bedrotting
            " {image=carmenicon} Carmen {image=carmenicon} ":
                jump rottingbed
    elif quinnknow == True and carmenknow == False:
        menu:
            " {image=quinnicon} Quinn {image=quinnicon} ":
                jump bedrotting
            " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                jump rottingbed
    elif quinnknow == False and carmenknow == True:
        menu:
            " {image=quinnicon} A frustrated theater guy {image=quinnicon} ":
                jump bedrotting
            " {image=carmenicon} Carmen {image=carmenicon} ":
                jump rottingbed
    else:
        menu:
            " {image=quinnicon} A frustrated theater guy {image=quinnicon} ":
                jump bedrotting
            " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                jump rottingbed
    label bedrotting:
        show quinnangry at center with easeinright
        if quinnknow == True:
            q " No, this isn't right... "
            q " Come on, I already told them what to do...! "
            q " How come they didn't understand my directions? "
            q " You know what, it's fine... "
            q " I can just arrange the props later. "
            q " Later when I arrive at theater club. "
            hide quinnangry at bottom
            show quinnneutral at center
            " You cough to let him know that you were here. "
            " You then asked him if he was doing alright. "
            q " Oh! [name]! hello... "
            q " I'm doing fine, it's just issues with some of my club members. "
            q " I'm sure I've told you about my play on friday, correct? "
            q " I can't really remember if I have, things have been clouding my mind lately... "
            q " But I'm glad to have you here with me right now. "
            if quinnlv >= 15 or quinnlv == 15:
                hide quinnneutral at bottom
                show quinnhappy at center
                q " You make my dull days better. "
                q " Your prescence calms me... "
                hide quinnhappy at bottom
                show quinnneutral at center
            else:
                q " Just need someone to talk to so that I can calm down. "
            q " So, if you don't mind... "
            q " Could I talk to you about how my club members have been behaving? "
            q " They've been a little...irritating this week. "
            menu:
                " Sure ":
                    $ quinnlv += 10
                    q " Thanks...I really need to blow off some steam. "
                    q " My teammates are great, really. "
                    q " But sometimes they take certain things... "
                    hide quinnneutral at bottom
                    show quinnangry at center
                    q " ...Unseriously. "
                    q " Like for example - I ask them to put a prop in the center... "
                    q " And what do they do? "
                    q " They put the prop SLIGHTLY to the left. "
                    q " I don't really care if it was a mistake. "
                    q " It should've been PERFECTLY at the center! "
                    " You told Quinn that it was okay for things not to be perfect. "
                    q " That's real easy for you to say. "
                    q " I'm out here trying to impress everyone and trying to make myself NOT look like a fool! "
                    q " But how can I when I'm acting with people like this?! "
                    q " At this point, the theater isn't a place where you can act - "
                    q " It's not a place where you can share stories, it's a damn CIRCUS. "
                    q " A very unfunny circus. "
                    hide quinnangry at bottom
                    show quinnsad at center
                    q " ...Sorry. I've been getting real stressed lately. "
                    q " I just want things to be perfect, but my group members aren't cooperating. "
                    q " I'm sure they know how tough this is for me with how perfect I want things to be. "
                    q " If they know that, then why aren't they understanding the things I'm saying? "
                    q " I know they're trying their best, but sometimes our best isn't enough. "
                    q " Sighhhh... "
                    hide quinnsad at bottom
                    show quinnneutral at center
                    q " I'm gonna go to the drama club room to fix some things. "
                    q " Thank you for listening, [name]. "
                    q " I really appreciate it. "
                    q " I'll see you in class later! "
                    hide quinnneutral at left with easeoutleft
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " You didn't do anything much, but you were wondering... "
                    " Wondering what Quinn's play is gonna be about. "
                    " Maybe you should see it. Only if you had free time though. "
                    " Maybe you're going to have some free time, maybe not. "
                    " I'm the narrator, so I kinda get to choose if you have time or nah. "
                    " Most likely you're gonna have time though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and walked to your classroom. "
                    pause 2.0
                    jump physicsclasswed
                " I got other places to be ":
                    q " Oh! just stopping by here, then? "
                    q " Completely fine, actually. "
                    q " I'm gonna go to the drama club room to fix some things. "
                    q " Have fun on whatever you're going to do, though! "
                    hide quinnneutral at left with easeoutleft
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " You didn't do anything much, but you were wondering... "
                    " Wondering what Quinn's play is gonna be about. "
                    " Maybe you should see it. Only if you had free time though. "
                    " Maybe you're going to have some free time, maybe not. "
                    " I'm the narrator, so I kinda get to choose if you have time or nah. "
                    " Most likely you're gonna have time though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and walked to your classroom. "
                    pause 2.0
                    jump physicsclasswed
        else:
            x " No, this isn't right... "
            x " Come on, I already told them what to do...! "
            x " How come they didn't understand my directions? "
            x " You know what, it's fine... "
            x " I can just arrange the props later. "
            x " Later when I arrive at theater club. "
            hide quinnangry at bottom
            show quinnneutral at center
            " You cough to let him know that you were here. "
            " You then asked him if he was doing alright. "
            x " Oh! [name]! hello... "
            x " I'm doing fine, it's just issues with some of my club members. "
            $ quinnknow = True
            q " I'm Quinn, by the way. "
            q " I'm sure I've told you about my play on friday, correct? "
            q " I can't really remember if I have, things have been clouding my mind lately... "
            q " But I'm glad to have you here with me right now. "
            if quinnlv >= 15 or quinnlv == 15:
                hide quinnneutral at bottom
                show quinnhappy at center
                q " You make my dull days better. "
                q " Your prescence calms me... "
                hide quinnhappy at bottom
                show quinnneutral at center
            else:
                q " Just need someone to talk to so that I can calm down. "
            q " So, if you don't mind... "
            q " Could I talk to you about how my club members have been behaving? "
            q " They've been a little...irritating this week. "
            menu:
                " Sure ":
                    $ quinnlv += 10
                    q " Thanks...I really need to blow off some steam. "
                    q " My teammates are great, really. "
                    q " But sometimes they take certain things... "
                    hide quinnneutral at bottom
                    show quinnangry at center
                    q " ...Unseriously. "
                    q " Like for example - I ask them to put a prop in the center... "
                    q " And what do they do? "
                    q " They put the prop SLIGHTLY to the left. "
                    q " I don't really care if it was a mistake. "
                    q " It should've been PERFECTLY at the center! "
                    " You told Quinn that it was okay for things not to be perfect. "
                    q " That's real easy for you to say. "
                    q " I'm out here trying to impress everyone and trying to make myself NOT look like a fool! "
                    q " But how can I when I'm acting with people like this?! "
                    q " At this point, the theater isn't a place where you can act - "
                    q " It's not a place where you can share stories, it's a damn CIRCUS. "
                    q " A very unfunny circus. "
                    hide quinnangry at bottom
                    show quinnsad at center
                    q " ...Sorry. I've been getting real stressed lately. "
                    q " I just want things to be perfect, but my group members aren't cooperating. "
                    q " I'm sure they know how tough this is for me with how perfect I want things to be. "
                    q " If they know that, then why aren't they understanding the things I'm saying? "
                    q " I know they're trying their best, but sometimes our best isn't enough. "
                    q " Sighhhh... "
                    hide quinnsad at bottom
                    show quinnneutral at center
                    q " I'm gonna go to the drama club room to fix some things. "
                    q " Thank you for listening, [name]. "
                    q " I really appreciate it. "
                    q " I'll see you in class later! "
                    hide quinnneutral at left with easeoutleft
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " You didn't do anything much, but you were wondering... "
                    " Wondering what Quinn's play is gonna be about. "
                    " Maybe you should see it. Only if you had free time though. "
                    " Maybe you're going to have some free time, maybe not. "
                    " I'm the narrator, so I kinda get to choose if you have time or nah. "
                    " Most likely you're gonna have time though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and walked to your classroom. "
                    pause 2.0
                    jump physicsclasswed
                " I got other places to be ":
                    q " Oh! just stopping by here, then? "
                    q " Completely fine, actually. "
                    q " I'm gonna go to the drama club room to fix some things. "
                    q " Have fun on whatever you're going to do, though! "
                    hide quinnneutral at left with easeoutleft
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " You didn't do anything much, but you were wondering... "
                    " Wondering what Quinn's play is gonna be about. "
                    " Maybe you should see it. Only if you had free time though. "
                    " Maybe you're going to have some free time, maybe not. "
                    " I'm the narrator, so I kinda get to choose if you have time or nah. "
                    " Most likely you're gonna have time though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and walked to your classroom. "
                    pause 2.0
                    jump physicsclasswed
    label rottingbed:
        show carmenneutral at center with easeinleft
        if carmenknow == True:
            ca " ...!! "
            " Carmen waves at you, then makes a sign to you... "
            " Looks like he wants you to sit next to him. "
            " Being a good friend you are, you decided to sit next to him on the bleachers. "
            ca " ... "
            " Carmen just relaxes, there, plucking strings on his guitar... "
            " Looks like he's a little bored. "
            " You don't know what to do either though... "
            " You two kinda just relax there for a bit. "
            " Not speaking, of course. Carmen can't speak. "
            " And you also didn't really feel like speaking. "
            " You zoned out for just a bit...thinking about things. "
            " Like thinking about the amount of fanfiction you looked up last night. "
            " Suddenly, you feel Carmen poking your shoulder. "
            " You snapped out of it, and looked over to him... "
            " ...Only to see him offer something to you. It looked like wrapped up candy. "
            " Should you take it? "
            menu:
                " GIMME THAT CANDY BB ":
                    $ carmenlv += 10
                    ca " ...! "
                    " You took the candy from him and ate it... "
                    " ...It tasted like shit. "
                    " You immediately spat it out once you tasted it. "
                    hide carmenneutral at bottom
                    show carmenhappy at center
                    ca " ...!!! "
                    " You don't know what he just gave you... "
                    " ...But it looks like he just pranked you. "
                    " He looked like he was laughing, but no sound came out from him. "
                    " He looked really nice while he was 'laughing'... "
                    " You did wonder what he would sound if he had his voice back. "
                    " Probably would sound really sweet and really nice. "
                    " You then bonked him on his head for pranking you. "
                    ca " ?!...!!!! "
                    " ...And he kept laughing, even if he made no noise. "
                    " Atleast you can tell that he was having fun. "
                    scene black with dissolve
                    " You spent the rest of the break hanging out and relaxing with Carmen. "
                    " You talked to Carmen about some random things... "
                    " ...Like the amount of fanfiction you looked up last night. "
                    " Carmen asked you why you looked them up, and uh... "
                    " Let's just not talk about that. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and walked to your classroom. "
                    pause 2.0
                    jump physicsclasswed
                " Nah I'm good ":
                    " Carmen shrugs and puts the candy in his bag. "
                    " Carmen then gives you a few signs... "
                    " He told you that he was gonna prank you, but you didn't take the bait, soo... "
                    " It didn't really work. "
                    " He still thought that it would be funny if you actually ate it. "
                    " You now wonder what that 'candy' tastes like... "
                    " ...Probably not the best. "
                    scene black with dissolve
                    " You spent the rest of the break hanging out and relaxing with Carmen. "
                    " You talked to Carmen about some random things... "
                    " ...Like the amount of fanfiction you looked up last night. "
                    " Carmen asked you why you looked them up, and uh... "
                    " Let's just not talk about that. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and walked to your classroom. "
                    pause 2.0
                    jump physicsclasswed
        else:
            x " ...!! "
            " You've heard about this kid before, someone was talking about him. "
            $ carmenknow = True
            " His name is Carmen, and he's mute. Interesting. "
            " He also liked playing the guitar a lot. "
            " Carmen waves at you, then makes a sign to you... "
            " Looks like he wants you to sit next to him. "
            " Being a good friend you are, you decided to sit next to him on the bleachers. "
            ca " ... "
            " Carmen just relaxes, there, plucking strings on his guitar... "
            " Looks like he's a little bored. "
            " You don't know what to do either though... "
            " You two kinda just relax there for a bit. "
            " Not speaking, of course. Carmen can't speak. "
            " And you also didn't really feel like speaking. "
            " You zoned out for just a bit...thinking about things. "
            " Like thinking about the amount of fanfiction you looked up last night. "
            " Suddenly, you feel Carmen poking your shoulder. "
            " You snapped out of it, and looked over to him... "
            " ...Only to see him offer something to you. It looked like wrapped up candy. "
            " Should you take it? "
            menu:
                " GIMME THAT CANDY BB ":
                    $ carmenlv += 10
                    ca " ...! "
                    " You took the candy from him and ate it... "
                    " ...It tasted like shit. "
                    " You immediately spat it out once you tasted it. "
                    hide carmenneutral at bottom
                    show carmenhappy at center
                    ca " ...!!! "
                    " You don't know what he just gave you... "
                    " ...But it looks like he just pranked you. "
                    " He looked like he was laughing, but no sound came out from him. "
                    " He looked really nice while he was 'laughing'... "
                    " You did wonder what he would sound if he had his voice back. "
                    " Probably would sound really sweet and really nice. "
                    " You then bonked him on his head for pranking you. "
                    ca " ?!...!!!! "
                    " ...And he kept laughing, even if he made no noise. "
                    " Atleast you can tell that he was having fun. "
                    scene black with dissolve
                    " You spent the rest of the break hanging out and relaxing with Carmen. "
                    " You talked to Carmen about some random things... "
                    " ...Like the amount of fanfiction you looked up last night. "
                    " Carmen asked you why you looked them up, and uh... "
                    " Let's just not talk about that. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and walked to your classroom. "
                    pause 2.0
                    jump physicsclasswed
                " Nah I'm good ":
                    " Carmen shrugs and puts the candy in his bag. "
                    " Carmen then gives you a few signs... "
                    " He told you that he was gonna prank you, but you didn't take the bait, soo... "
                    " It didn't really work. "
                    " He still thought that it would be funny if you actually ate it. "
                    " You now wonder what that 'candy' tastes like... "
                    " ...Probably not the best. "
                    scene black with dissolve
                    " You spent the rest of the break hanging out and relaxing with Carmen. "
                    " You talked to Carmen about some random things... "
                    " ...Like the amount of fanfiction you looked up last night. "
                    " Carmen asked you why you looked them up, and uh... "
                    " Let's just not talk about that. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back into the school and walked to your classroom. "
                    pause 2.0
                    jump physicsclasswed
label wedcafeteria4wed:
    # orchid and koa
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and found two of your classmates talking with eachother. "
    " Wondering what they're up to, you decided to join their conversation and sat next to them. "
    " Time to listen into what they're going to say... "
    show orchidhappy at left with easeinright
    show koaneutral at right with easeinright
    if orchidknow == True and koaknow == True:
        oc " Hiya, [name]! "
        k " Hey there, [name]. "
        oc " You know guys...last break.. "
        oc " I think I made a new friend! "
        k " Oh really? "
        oc " Yeah!! She was really into Zatzune Ziku!! "
        oc " I also decided that I should give her some of my Ziku merch... "
        oc " She said that her family wouldn't really get her merch. "
        oc " Said that it's a waste of money or something along those lines... "
        oc " Well, now she has merch she can show off about! "
        k " ...That's really nice of you, Orchid. "
        " Koa pats Orchid's head. "
        " These two...really do act like father and son. "
        " Even though they're not biologically related, you could tell that Koa cares for Orchid a lot. "
        " From what you've heard, Orchid doesn't interact with people as much. "
        " Seeing them improve is great, so you could see why Koa is happy about that. "
        k " ...I'm proud of you for stepping out and making a friend, Orchid. "
        oc " Haha, I'm proud of myself too! "
        oc " Genuinely thought I'd only have you as a friend this entire school year... "
        oc " ...But I guess not!! Yipeee!! "
        hide orchidhappy at bottom
        show orchidneutral at left
        oc " I honestly want to talk to her more... "
        oc " ...Don't know where she is though. "
        k " How about you try to find her? "
        oc " Nah, my legs hurt. "
        k " ...How much have you been walking. "
        oc " ...Only a bit??? "
        k " ... "
        k " We're going to have to work on that. "
        oc " I no no wanna... "
        k " Orchidddd... "
        oc " Koa my legs are broken please no. "
        k " They're not actually.. "
        scene black with dissolve
        " You spent the rest of the break talking with Koa and Orchid. "
        " They're quite the humerous duo... "
        " While you ARE happy that Orchid's been interacting with others now, "
        " Orchid DEFINITELY has to work on their walking skills. "
        " What do you mean they already got tired after walking for a bit?? "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You walked back into the school and walked to your classroom. "
        pause 2.0
        jump physicsclasswed
    elif orchidknow == True and koaknow == False:
        oc " Hiya, [name]! "
        x " Hey there, [name]. "
        $ koaknow = True
        oc " This is my friend, Koa!! "
        k " It's nice to meet you. "
        oc " ...You know guys...last break.. "
        oc " I think I made a new friend! "
        k " Oh really? "
        oc " Yeah!! She was really into Zatzune Ziku!! "
        oc " I also decided that I should give her some of my Ziku merch... "
        oc " She said that her family wouldn't really get her merch. "
        oc " Said that it's a waste of money or something along those lines... "
        oc " Well, now she has merch she can show off about! "
        k " ...That's really nice of you, Orchid. "
        " Koa pats Orchid's head. "
        " These two...really do act like father and son. "
        " Even though they're not biologically related, you could tell that Koa cares for Orchid a lot. "
        " From what you've heard, Orchid doesn't interact with people as much. "
        " Seeing them improve is great, so you could see why Koa is happy about that. "
        k " ...I'm proud of you for stepping out and making a friend, Orchid. "
        oc " Haha, I'm proud of myself too! "
        oc " Genuinely thought I'd only have you as a friend this entire school year... "
        oc " ...But I guess not!! Yipeee!! "
        hide orchidhappy at bottom
        show orchidneutral at left
        oc " I honestly want to talk to her more... "
        oc " ...Don't know where she is though. "
        k " How about you try to find her? "
        oc " Nah, my legs hurt. "
        k " ...How much have you been walking. "
        oc " ...Only a bit??? "
        k " ... "
        k " We're going to have to work on that. "
        oc " I no no wanna... "
        k " Orchidddd... "
        oc " Koa my legs are broken please no. "
        k " They're not actually.. "
        scene black with dissolve
        " You spent the rest of the break talking with Koa and Orchid. "
        " They're quite the humerous duo... "
        " While you ARE happy that Orchid's been interacting with others now, "
        " Orchid DEFINITELY has to work on their walking skills. "
        " What do you mean they already got tired after walking for a bit?? "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You walked back into the school and walked to your classroom. "
        pause 2.0
        jump physicsclasswed
    elif orchidknow == False and koaknow == True:
        x " Hiya, [name]! "
        k " Hey there, [name]. "
        k " This is my friend, Orchid. "
        $ orchidknow = True
        oc " It's nice to meet you!! "
        oc " You know guys...last break.. "
        oc " I think I made a new friend! "
        k " Oh really? "
        oc " Yeah!! She was really into Zatzune Ziku!! "
        oc " I also decided that I should give her some of my Ziku merch... "
        oc " She said that her family wouldn't really get her merch. "
        oc " Said that it's a waste of money or something along those lines... "
        oc " Well, now she has merch she can show off about! "
        k " ...That's really nice of you, Orchid. "
        " Koa pats Orchid's head. "
        " These two...really do act like father and son. "
        " Even though they're not biologically related, you could tell that Koa cares for Orchid a lot. "
        " From what you've heard, Orchid doesn't interact with people as much. "
        " Seeing them improve is great, so you could see why Koa is happy about that. "
        k " ...I'm proud of you for stepping out and making a friend, Orchid. "
        oc " Haha, I'm proud of myself too! "
        oc " Genuinely thought I'd only have you as a friend this entire school year... "
        oc " ...But I guess not!! Yipeee!! "
        hide orchidhappy at bottom
        show orchidneutral at left
        oc " I honestly want to talk to her more... "
        oc " ...Don't know where she is though. "
        k " How about you try to find her? "
        oc " Nah, my legs hurt. "
        k " ...How much have you been walking. "
        oc " ...Only a bit??? "
        k " ... "
        k " We're going to have to work on that. "
        oc " I no no wanna... "
        k " Orchidddd... "
        oc " Koa my legs are broken please no. "
        k " They're not actually.. "
        scene black with dissolve
        " You spent the rest of the break talking with Koa and Orchid. "
        " They're quite the humerous duo... "
        " While you ARE happy that Orchid's been interacting with others now, "
        " Orchid DEFINITELY has to work on their walking skills. "
        " What do you mean they already got tired after walking for a bit?? "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You walked back into the school and walked to your classroom. "
        pause 2.0
        jump physicsclasswed
    else:
        oc " Hiya, [name]! I'm Orchid! "
        k " Hey there, [name]. I'm Koa. "
        $ orchidknow = True
        $ koaknow = True
        oc " You know guys...last break.. "
        oc " I think I made a new friend! "
        k " Oh really? "
        oc " Yeah!! She was really into Zatzune Ziku!! "
        oc " I also decided that I should give her some of my Ziku merch... "
        oc " She said that her family wouldn't really get her merch. "
        oc " Said that it's a waste of money or something along those lines... "
        oc " Well, now she has merch she can show off about! "
        k " ...That's really nice of you, Orchid. "
        " Koa pats Orchid's head. "
        " These two...really do act like father and son. "
        " Even though they're not biologically related, you could tell that Koa cares for Orchid a lot. "
        " From what you've heard, Orchid doesn't interact with people as much. "
        " Seeing them improve is great, so you could see why Koa is happy about that. "
        k " ...I'm proud of you for stepping out and making a friend, Orchid. "
        oc " Haha, I'm proud of myself too! "
        oc " Genuinely thought I'd only have you as a friend this entire school year... "
        oc " ...But I guess not!! Yipeee!! "
        hide orchidhappy at bottom
        show orchidneutral at left
        oc " I honestly want to talk to her more... "
        oc " ...Don't know where she is though. "
        k " How about you try to find her? "
        oc " Nah, my legs hurt. "
        k " ...How much have you been walking. "
        oc " ...Only a bit??? "
        k " ... "
        k " We're going to have to work on that. "
        oc " I no no wanna... "
        k " Orchidddd... "
        oc " Koa my legs are broken please no. "
        k " They're not actually.. "
        scene black with dissolve
        " You spent the rest of the break talking with Koa and Orchid. "
        " They're quite the humerous duo... "
        " While you ARE happy that Orchid's been interacting with others now, "
        " Orchid DEFINITELY has to work on their walking skills. "
        " What do you mean they already got tired after walking for a bit?? "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You walked back into the school and walked to your classroom. "
        pause 2.0
        jump physicsclasswed
label wedrooftop4wed:
    # disk and spark
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked up to the rooftop and spotted your two classmates doing their own things. "
    " You wanted to talk to one of them, but who do you talk to? "
    if diskknow == True and sparkknow == True:
        menu:
            " {image=diskicon} Disk {image=diskicon} ":
                jump pururin
            " {image=sparkicon} Spark {image=sparkicon} ":
                jump purou
    elif diskknow == True and sparkknow == False:
        menu:
            " {image=diskicon} Disk {image=diskicon} ":
                jump pururin
            " {image=sparkicon} A chill looking guy {image=sparkicon} ":
                jump purou
    elif diskknow == False and sparkknow == True:
        menu:
            " {image=diskicon} A popular looking guy {image=diskicon} ":
                jump pururin
            " {image=sparkicon} Spark {image=sparkicon} ":
                jump purou
    else:
        menu:
            " {image=diskicon} A popular looking guy {image=diskicon} ":
                jump pururin
            " {image=sparkicon} A chill looking guy {image=sparkicon} ":
                jump purou
    label pururin:
        show diskneutral at center with easeinleft
        if diskknow == True:
            d " Hey there, [name]! "
            d " I just came here to take some fresh air... "
            d " You know... "
            d " The noise inside the school is pretty overwhelming sometimes. "
            d " Well, almost all the time, actually... "
            d " Sometimes I can't really handle it. "
            d " I know that I'm a guy who likes to party, buuuut - "
            d " School noise is just different, you know? "
            d " I usually keep the noises from my party at a good level. "
            d " And if things are too loud? "
            d " I'll just go to my room for a bit, have my younger brother take the lead... "
            d " And then come back! "
            d " If I'm gone for too long, I just know people will look for me... "
            d " Sooo, I usually try to come back after 10-30 minutes... "
            d " But of course, there's times where I completely forget to come back... "
            d " And my brother has to come and get me. "
            d " I don't forget about the party on purpose of course! I can't control that! "
            d " It's just that I get distracted about certain things... "
            d " Like for example... "
            d " Abbie sends me a voice mail... "
            d " Abbie sends me a new text and I can't really tweak out infront of people... "
            d " ...And a list of other things that aren't related! "
            d " And when the parties all over...I go to sleep immediately! "
            d " I need to wake up early so I could savor the feeling of having no school, you know! "
            d " Whilst I do enjoy going to school...there's just days where I wish that school would be over early. "
            d " Surprising with how much I love school, honestly! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk. "
            " It was nice talking with Disk for a bit... "
            " And what made it nicer was that the rooftop was quiet. "
            " You could see why Disk likes being on the rooftop sometimes. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You walked back into the school and walked to your classroom. "
            pause 2.0
            jump physicsclasswed
        else:
            x " Hey there, [name]! "
            x " Waitwait...we haven't met before, have weee...? "
            x " Oh geez, I haven't introduced myself yet! Sorry! "
            $ diskknow = True
            d " I'm Disk - it's really nice to meet you! "
            d " I just came here to take some fresh air... "
            d " You know... "
            d " The noise inside the school is pretty overwhelming sometimes. "
            d " Well, almost all the time, actually... "
            d " Sometimes I can't really handle it. "
            d " I know that I'm a guy who likes to party, buuuut - "
            d " School noise is just different, you know? "
            d " I usually keep the noises from my party at a good level. "
            d " And if things are too loud? "
            d " I'll just go to my room for a bit, have my younger brother take the lead... "
            d " And then come back! "
            d " If I'm gone for too long, I just know people will look for me... "
            d " Sooo, I usually try to come back after 10-30 minutes... "
            d " But of course, there's times where I completely forget to come back... "
            d " And my brother has to come and get me. "
            d " I don't forget about the party on purpose of course! I can't control that! "
            d " It's just that I get distracted about certain things... "
            d " Like for example... "
            d " Abbie sends me a voice mail... "
            d " Abbie sends me a new text and I can't really tweak out infront of people... "
            d " ...And a list of other things that aren't related! "
            d " And when the parties all over...I go to sleep immediately! "
            d " I need to wake up early so I could savor the feeling of having no school, you know! "
            d " Whilst I do enjoy going to school...there's just days where I wish that school would be over early. "
            d " Surprising with how much I love school, honestly! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk. "
            " It was nice talking with Disk for a bit... "
            " And what made it nicer was that the rooftop was quiet. "
            " You could see why Disk likes being on the rooftop sometimes. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You walked back into the school and walked to your classroom. "
            pause 2.0
            jump physicsclasswed
    label purou:
        show sparkneutral at center with easeinright
        if sparkknow == True:
            " He seems distracted. "
            sp " ... "
            " He's just zoning off and looking at the distance. "
            " You wonder what he's thinking about. "
            " You're not gonna disturb him though. "
            " Just gonna have to wait until he notices you himself. "
            " Dude looks like he's in some really deep thoughts anyway. "
            " You're sure that you couldn't snap him out of it yourself if you tried. "
            " So...you're gonna wait. And wait you did. "
            sp " ...{p} Wait, [name]? "
            sp " Oh jeez, I'm sorry I didn't notice you. "
            sp " Thought that I was all alone up here, oops... "
            sp " Anyway, you wanted to talk to me or something...? "
            sp " I don't really have anything interesting to talk about, in all honesty... "
            sp " ...But, I do have a few interesting questions about life. "
            sp " Like...do you ever feel as if everything's not real? "
            sp " One second you're hanging out with your friends, and then suddenly you get that feeling? "
            sp " What if you're just a puppet being used in a game for fun? "
            sp " Actually, no...what if you're just talking to AI's and this isn't a real world? "
            sp " What if I'm talking to someone who isn't supposed to exist in this universe right now? "
            sp " What if I'm just talking to air and you're not actually here? "
            sp " Everything's just...weird. "
            sp " Life is real weird and you just can't really understand all of it. "
            sp " Why certain things exist, and why other things don't exist. "
            sp " We all have our questions and some of them can't even be answered. "
            sp " There's so many things we don't know... "
            sp " So many people we haven't met...So many places we haven't gone to... "
            sp " The universe is big and we're just tiny specs wandering on our little planet. "
            sp " ...Sorry if I got a little too real there. "
            sp " I just needed to get some thoughts out. "
            sp " But, we can have a normal conversation now if that's what you wanted. "
            sp " What do you wanna talk about? "
            scene black with dissolve
            " You talked with Spark for the rest of the break. "
            " You just decided to talk about things like space and what Spark likes about space. "
            " He says he likes the little constellations because he finds them interesting.. "
            " He also says that he wants to know more about them someday. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You walked back into the school and walked to your classroom. "
            pause 2.0
            jump physicsclasswed
        else:
            " He seems distracted. "
            x " ... "
            " He's just zoning off and looking at the distance. "
            " You wonder what he's thinking about. "
            " You're not gonna disturb him though. "
            " Just gonna have to wait until he notices you himself. "
            " Dude looks like he's in some really deep thoughts anyway. "
            " You're sure that you couldn't snap him out of it yourself if you tried. "
            " So...you're gonna wait. And wait you did. "
            x " ...{p} Wait, [name]? "
            x " Oh jeez, I'm sorry I didn't notice you. "
            x " Thought that I was all alone up here, oops... "
            $ sparkknow = True
            sp " I'm Spark, by the way. Nice to meet you. "
            sp " Anyway, you wanted to talk to me or something...? "
            sp " I don't really have anything interesting to talk about, in all honesty... "
            sp " ...But, I do have a few interesting questions about life. "
            sp " Like...do you ever feel as if everything's not real? "
            sp " One second you're hanging out with your friends, and then suddenly you get that feeling? "
            sp " What if you're just a puppet being used in a game for fun? "
            sp " Actually, no...what if you're just talking to AI's and this isn't a real world? "
            sp " What if I'm talking to someone who isn't supposed to exist in this universe right now? "
            sp " What if I'm just talking to air and you're not actually here? "
            sp " Everything's just...weird. "
            sp " Life is real weird and you just can't really understand all of it. "
            sp " Why certain things exist, and why other things don't exist. "
            sp " We all have our questions and some of them can't even be answered. "
            sp " There's so many things we don't know... "
            sp " So many people we haven't met...So many places we haven't gone to... "
            sp " The universe is big and we're just tiny specs wandering on our little planet. "
            sp " ...Sorry if I got a little too real there. "
            sp " I just needed to get some thoughts out. "
            sp " But, we can have a normal conversation now if that's what you wanted. "
            sp " What do you wanna talk about? "
            scene black with dissolve
            " You talked with Spark for the rest of the break. "
            " You just decided to talk about things like space and what Spark likes about space. "
            " He says he likes the little constellations because he finds them interesting.. "
            " He also says that he wants to know more about them someday. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You walked back into the school and walked to your classroom. "
            pause 2.0
            jump physicsclasswed
label wedlibrary4wed:
    # the twins but they're away from eachother
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library, and spotted twins looking around... "
    " ...You recognize them as your classmates - you've always see them together. "
    " But, they're both in completely different sections while looking for books. "
    " Who do you want to talk to? "
    if yangyiknow == True and yinhuiknow == True:
        menu:
            " {image=yinyangicon} Yangyi {image=yinyangicon} ":
                jump evilingood
            " {image=yinyangicon} Yinhui {image=yinyangicon} ":
                jump goodinevil
    elif yangyiknow == True and yinhuiknow == False:
        menu:
            " {image=yinyangicon} Yangyi {image=yinyangicon} ":
                jump evilingood
            " {image=yinyangicon} The mean looking one {image=yinyangicon} ":
                jump goodinevil
    elif yangyiknow == False and yinhuiknow == True:
        menu:
            " {image=yinyangicon} The kind looking one {image=yinyangicon} ":
                jump evilingood
            " {image=yinyangicon} Yinhui {image=yinyangicon} ":
                jump goodinevil
    else:
        menu:
            " {image=yinyangicon} The kind looking one {image=yinyangicon} ":
                jump evilingood
            " {image=yinyangicon} The mean looking one {image=yinyangicon} ":
                jump goodinevil
    label evilingood:
        $ yangyilv += 5
        show yangyineutral at center with easeinleft
        if yangyiknow == True:
            " Surprisingly, you found him in the horror section. "
            " Though, he seems busy reading... "
            " You didn't really want to disturb him. "
            " Let's go hang out somewhere else then. "
            scene black with dissolve
            " You spent the rest of the break wandering around the school. "
            " For someone who looks so kind... "
            " You didn't expect for that guy to look in the horror section. "
            " Don't judge a book by it's cover, you guess? "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You walked back into the school and walked to your classroom. "
            pause 2.0
            jump physicsclasswed
        else:
            " Surprisingly, you found him in the horror section. "
            " Though, he seems busy reading... "
            " You didn't really want to disturb him. "
            " Let's go hang out somewhere else then. "
            scene black with dissolve
            " You spent the rest of the break wandering around the school. "
            " For someone who looks so kind... "
            " You didn't expect for that guy to look in the horror section. "
            " Don't judge a book by it's cover, you guess? "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You walked back into the school and walked to your classroom. "
            pause 2.0
            jump physicsclasswed
    label goodinevil:
        $ yinhuilv += 5
        show yinhuineutral at center with easeinright
        if yinhuiknow == True:
            " Surprisingly, you found him in the romance section. "
            " Though, he seems busy reading... "
            " You didn't really want to disturb him. "
            " Let's go hang out somewhere else then. "
            scene black with dissolve
            " You spent the rest of the break wandering around the school. "
            " For someone who looks so mean... "
            " You didn't expect for that guy to look in the romance section. "
            " Don't judge a book by it's cover, you guess? "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You walked back into the school and walked to your classroom. "
            pause 2.0
            jump physicsclasswed
        else:
            " Surprisingly, you found him in the romance section. "
            " Though, he seems busy reading... "
            " You didn't really want to disturb him. "
            " Let's go hang out somewhere else then. "
            scene black with dissolve
            " You spent the rest of the break wandering around the school. "
            " For someone who looks so mean... "
            " You didn't expect for that guy to look in the romance section. "
            " Don't judge a book by it's cover, you guess? "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You walked back into the school and walked to your classroom. "
            pause 2.0
            jump physicsclasswed
label physicsclasswed:
    scene classroom with dissolve
    " You walked into the classroom and waited patiently for the teacher to arrive. "
    " Suprisingly, the teacher takes about 20 whole minutes to show up. "
    " You know that the teacher for this class is forgetful, so you could understand. "
    show luaneutral at center with easeinright
    msl " Good day, class. "
    msl " Let's see...what do I have to teach again... "
    msl " ... "
    msl " I'm going to show all of you a new lesson for today. "
    msl " Please get out your pens and notebooks to take down notes. "
    msl " I'm also going to be demonstrating a few things. "
    msl " What was I going to remind you guys about this time... "
    msl " Hmmm...something about a new activity... "
    msl " ...Oh right. "
    msl " I'd like to remind you all about our activity on thursday... "
    msl " Please prepare for that, thank you... "
    msl " (I'm going to have to take a note about the activity later...) "
    msl " (Hopefully I don't forget about it. That would be bad.) "
    msl " (Sol can just remind me though, good thing he has good memory.) "
    msl " ...(What was I doing again?) "
    msl " (Oh yeah.) "
    msl " Anyway, let's start our lesson for today... "
    scene black with dissolve
    " You didn't take notes for this class. "
    " You just didn't feel like doing it, so you just looked at the demonstration. "
    " You're going to have to look at someone elses notes for this... "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for your last break of the day. "
    " You get up from your seat, and you walked into the hallways. "
    pause 2.0
    jump wedocbreak5

label wedocbreak5:
    scene hallway with dissolve
    " Where would you like to go for this break? "
    menu:
        " {image=orchidicon} The front of the school {image=carmenicon} ":
            jump wedfront5wed
        " {image=noxicon} The back of the school {image=jacobicon} ":
            jump wedback5wed
        " {image=diskicon} The gym {image=temeroicon} ":
            jump wedgym5wed
        " {image=matteicon} The cafeteria {image=jamicon} ":
            jump wedcafeteria5wed
        " {image=quinnicon} The rooftop {image=yinyangicon} ":
            jump wedrooftop5wed
        " {image=sparkicon} The library {image=yinyangicon} ":
            jump wedlibrary5wed

label wedfront5wed:
    # orchid and carmen
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school and spotted two of your classmates hanging out. "
    " Wondering what they're talking about, you decided to talk to them. "
    " You sat down on the ground next to them and listened to their conversation... "
    show orchidneutral at left with easeinright
    show carmenneutral at right with easeinright
    if orchidknow == True and carmenknow == True:
        oc " No, you're going to have to move to the left to spot it... "
        ca " ...? "
        oc " Yeah, like that! "
        oc " And if you just turn to the right... "
        hide carmenneutral at bottom
        show carmenhappy at right
        ca " ...!! "
        " Looks like he's directing the other in a game. "
        " You don't know what game it is, but it looks cool. "
        " You're thinking about asking them about what game it is... "
        " Before you could ask them and potentially jumpscare them, they notice you. "
        oc " Oh, hey [name]! "
        hide carmenhappy at bottom
        show carmenneutral at right
        ca " ... "
        " The guy with the guitar waves at you. "
        oc " I'm just teaching Carmen a few things in this game I like... "
        oc " It's called Gambling Impact! "
        oc " Now yes, the game has a little bit on controversy in it... "
        oc " And the fandom is a little more than toxic... "
        oc " I still think it's a TINY bit good. I've actually quitted playing this game a few years ago. "
        oc " So, now I'm just here teaching Carmen the ropes! "
        oc " You wanna watch Carmen play a lot? "
        oc " It's alright if you don't want to, we're not forcing ya. "
        ca " ...!! "
        oc " Yeah- what Carmen said! It's all just for fun and games! "
        oc " We don't want to force you into something you don't want. "
        " Should you hang out with Orchid and Carmen for this break? "
        menu:
            " Hell yeah ":
                $ orchidlv += 10
                $ carmenlv += 10
                hide orchidneutral at bottom
                show orchidhappy at left
                oc " That's great! Now... "
                hide orchidhappy at bottom
                show orchidneutral at left
                oc " How about you move to Carmen's side? "
                oc " I'm sure you can't really see anything when you sit next to me. "
                oc " We wanna show you all the cool stuff in this game, after all! "
                oc " Don't want you to miss out on anything! "
                ca " !! (nod) "
                scene black with dissolve
                " You spent the rest of the break hanging out with Carmen and Orchid. "
                " The game was pretty cool, in your opinion. "
                " Wasn't this the game that went viral in 2020? "
                " Oooh, yeah...you remember those days. "
                " Maybe you should actually check it out. "
                " Or not, judging by it's reputation that Orchid mentioned earlier. "
                play sound "audio/bellring.mp3"
                " The bell rings. Time for your final class of the day. "
                " You got back into the school and walked to your culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
            " Got other places to b ":
                oc " Oh, really? "
                oc " Damn, that's a shame then... "
                oc " But - have fun on where you're going! "
                oc " Maybe tell Koa that I said hi, if you see him? "
                oc " God, he's going to be happy that I made another friend... "
                ca " ... "
                " Carmen waves at you, this time it's a 'byebye' wave. "
                " You wave them 'byebye' as well. "
                scene black with dissolve
                " You spent the rest of the break wandering around the school. "
                " While you were wandering around, you spotted that Koa person Orchid mentioned. "
                " You told him that Orchid said hi. "
                " You also told him that Orchid got a new friend. "
                " Koa seemed pleased at that information. "
                " You then continued walking around the school. "
                play sound "audio/bellring.mp3"
                " The bell rings. Time for your final class of the day. "
                " You got back into the school and walked to your culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
    elif orchidknow == True and carmenknow == False:
        oc " No, you're going to have to move to the left to spot it... "
        x " ...? "
        oc " Yeah, like that! "
        oc " And if you just turn to the right... "
        hide carmenneutral at bottom
        show carmenhappy at right
        x " ...!! "
        " Looks like he's directing the other in a game. "
        " You don't know what game it is, but it looks cool. "
        " You're thinking about asking them about what game it is... "
        " Before you could ask them and potentially jumpscare them, they notice you. "
        oc " Oh, hey [name]! "
        hide carmenhappy at bottom
        show carmenneutral at right
        x " ... "
        " The guy with the guitar waves at you. "
        oc " This is my new buddy - Carmen! "
        $ carmenknow = True
        oc " If you're wondering why he doesn't talk, it's because he's mute. "
        oc " He also likes to play the guitar a whole lot! anyway.. "
        oc " I'm just teaching Carmen a few things in this game I like... "
        oc " It's called Gambling Impact! "
        oc " Now yes, the game has a little bit on controversy in it... "
        oc " And the fandom is a little more than toxic... "
        oc " I still think it's a TINY bit good. I've actually quitted playing this game a few years ago. "
        oc " So, now I'm just here teaching Carmen the ropes! "
        oc " You wanna watch Carmen play a lot? "
        oc " It's alright if you don't want to, we're not forcing ya. "
        ca " ...!! "
        oc " Yeah- what Carmen said! It's all just for fun and games! "
        oc " We don't want to force you into something you don't want. "
        " Should you hang out with Orchid and Carmen for this break? "
        menu:
            " Hell yeah ":
                $ orchidlv += 10
                $ carmenlv += 10
                hide orchidneutral at bottom
                show orchidhappy at left
                oc " That's great! Now... "
                hide orchidhappy at bottom
                show orchidneutral at left
                oc " How about you move to Carmen's side? "
                oc " I'm sure you can't really see anything when you sit next to me. "
                oc " We wanna show you all the cool stuff in this game, after all! "
                oc " Don't want you to miss out on anything! "
                ca " !! (nod) "
                scene black with dissolve
                " You spent the rest of the break hanging out with Carmen and Orchid. "
                " The game was pretty cool, in your opinion. "
                " Wasn't this the game that went viral in 2020? "
                " Oooh, yeah...you remember those days. "
                " Maybe you should actually check it out. "
                " Or not, judging by it's reputation that Orchid mentioned earlier. "
                play sound "audio/bellring.mp3"
                " The bell rings. Time for your final class of the day. "
                " You got back into the school and walked to your culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
            " Got other places to b ":
                oc " Oh, really? "
                oc " Damn, that's a shame then... "
                oc " But - have fun on where you're going! "
                oc " Maybe tell Koa that I said hi, if you see him? "
                oc " God, he's going to be happy that I made another friend... "
                ca " ... "
                " Carmen waves at you, this time it's a 'byebye' wave. "
                " You wave them 'byebye' as well. "
                scene black with dissolve
                " You spent the rest of the break wandering around the school. "
                " While you were wandering around, you spotted that Koa person Orchid mentioned. "
                " You told him that Orchid said hi. "
                " You also told him that Orchid got a new friend. "
                " Koa seemed pleased at that information. "
                " You then continued walking around the school. "
                play sound "audio/bellring.mp3"
                " The bell rings. Time for your final class of the day. "
                " You got back into the school and walked to your culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
    elif orchidknow == False and carmenknow == True:
        x " No, you're going to have to move to the left to spot it... "
        ca " ...? "
        x " Yeah, like that! "
        x " And if you just turn to the right... "
        hide carmenneutral at bottom
        show carmenhappy at right
        ca " ...!! "
        " Looks like he's directing the other in a game. "
        " You don't know what game it is, but it looks cool. "
        " You're thinking about asking them about what game it is... "
        " Before you could ask them and potentially jumpscare them, they notice you. "
        x " Oh, hey [name]! "
        hide carmenhappy at bottom
        show carmenneutral at right
        ca " ... "
        x " I don't think we've met before, have we? "
        x " I mean, I {i}do{/i} know that you're our new classmate since...two days ago... "
        x " But I don't think I've introduced myself to you! "
        $ orchidknow = True
        oc " I'm Orchid! It's real nice to, er... meet you! "
        " The guy with the guitar waves at you. "
        oc " I'm just teaching Carmen a few things in this game I like... "
        oc " It's called Gambling Impact! "
        oc " Now yes, the game has a little bit on controversy in it... "
        oc " And the fandom is a little more than toxic... "
        oc " I still think it's a TINY bit good. I've actually quitted playing this game a few years ago. "
        oc " So, now I'm just here teaching Carmen the ropes! "
        oc " You wanna watch Carmen play a lot? "
        oc " It's alright if you don't want to, we're not forcing ya. "
        ca " ...!! "
        oc " Yeah- what Carmen said! It's all just for fun and games! "
        oc " We don't want to force you into something you don't want. "
        " Should you hang out with Orchid and Carmen for this break? "
        menu:
            " Hell yeah ":
                $ orchidlv += 10
                $ carmenlv += 10
                hide orchidneutral at bottom
                show orchidhappy at left
                oc " That's great! Now... "
                hide orchidhappy at bottom
                show orchidneutral at left
                oc " How about you move to Carmen's side? "
                oc " I'm sure you can't really see anything when you sit next to me. "
                oc " We wanna show you all the cool stuff in this game, after all! "
                oc " Don't want you to miss out on anything! "
                ca " !! (nod) "
                scene black with dissolve
                " You spent the rest of the break hanging out with Carmen and Orchid. "
                " The game was pretty cool, in your opinion. "
                " Wasn't this the game that went viral in 2020? "
                " Oooh, yeah...you remember those days. "
                " Maybe you should actually check it out. "
                " Or not, judging by it's reputation that Orchid mentioned earlier. "
                play sound "audio/bellring.mp3"
                " The bell rings. Time for your final class of the day. "
                " You got back into the school and walked to your culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
            " Got other places to b ":
                oc " Oh, really? "
                oc " Damn, that's a shame then... "
                oc " But - have fun on where you're going! "
                oc " Maybe tell Koa that I said hi, if you see him? "
                oc " God, he's going to be happy that I made another friend... "
                ca " ... "
                " Carmen waves at you, this time it's a 'byebye' wave. "
                " You wave them 'byebye' as well. "
                scene black with dissolve
                " You spent the rest of the break wandering around the school. "
                " While you were wandering around, you spotted that Koa person Orchid mentioned. "
                " You told him that Orchid said hi. "
                " You also told him that Orchid got a new friend. "
                " Koa seemed pleased at that information. "
                " You then continued walking around the school. "
                play sound "audio/bellring.mp3"
                " The bell rings. Time for your final class of the day. "
                " You got back into the school and walked to your culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
    else:
        x " No, you're going to have to move to the left to spot it... "
        x " ...? "
        x " Yeah, like that! "
        x " And if you just turn to the right... "
        hide carmenneutral at bottom
        show carmenhappy at right
        x " ...!! "
        " Looks like he's directing the other in a game. "
        " You don't know what game it is, but it looks cool. "
        " You're thinking about asking them about what game it is... "
        " Before you could ask them and potentially jumpscare them, they notice you. "
        x " Oh, hey [name]! "
        hide carmenhappy at bottom
        show carmenneutral at right
        x " ... "
        x " I don't think we've met before, have we? "
        x " I mean, I {i}do{/i} know that you're our new classmate since...two days ago... "
        x " But I don't think I've introduced myself to you! "
        $ orchidknow = True
        oc " I'm Orchid! It's real nice to, er... meet you! "
        " The guy with the guitar waves at you. "
        oc " Oho, looks like you haven't met Carmen yet! "
        $ carmenknow = True
        ca " ... "
        oc " Carmen is a real sweet guy, trust me! "
        oc " He's also one of our classmates. "
        oc " If you're wondering why he isn't talking, it's because he's mute. "
        oc " He also likes playing the guitar a lot! back to the original topic... "
        oc " I'm just teaching Carmen a few things in this game I like... "
        oc " It's called Gambling Impact! "
        oc " Now yes, the game has a little bit on controversy in it... "
        oc " And the fandom is a little more than toxic... "
        oc " I still think it's a TINY bit good. I've actually quitted playing this game a few years ago. "
        oc " So, now I'm just here teaching Carmen the ropes! "
        oc " You wanna watch Carmen play a lot? "
        oc " It's alright if you don't want to, we're not forcing ya. "
        ca " ...!! "
        oc " Yeah- what Carmen said! It's all just for fun and games! "
        oc " We don't want to force you into something you don't want. "
        " Should you hang out with Orchid and Carmen for this break? "
        menu:
            " Hell yeah ":
                $ orchidlv += 10
                $ carmenlv += 10
                hide orchidneutral at bottom
                show orchidhappy at left
                oc " That's great! Now... "
                hide orchidhappy at bottom
                show orchidneutral at left
                oc " How about you move to Carmen's side? "
                oc " I'm sure you can't really see anything when you sit next to me. "
                oc " We wanna show you all the cool stuff in this game, after all! "
                oc " Don't want you to miss out on anything! "
                ca " !! (nod) "
                scene black with dissolve
                " You spent the rest of the break hanging out with Carmen and Orchid. "
                " The game was pretty cool, in your opinion. "
                " Wasn't this the game that went viral in 2020? "
                " Oooh, yeah...you remember those days. "
                " Maybe you should actually check it out. "
                " Or not, judging by it's reputation that Orchid mentioned earlier. "
                play sound "audio/bellring.mp3"
                " The bell rings. Time for your final class of the day. "
                " You got back into the school and walked to your culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
            " Got other places to b ":
                oc " Oh, really? "
                oc " Damn, that's a shame then... "
                oc " But - have fun on where you're going! "
                oc " Maybe tell Koa that I said hi, if you see him? "
                oc " God, he's going to be happy that I made another friend... "
                ca " ... "
                " Carmen waves at you, this time it's a 'byebye' wave. "
                " You wave them 'byebye' as well. "
                scene black with dissolve
                " You spent the rest of the break wandering around the school. "
                " While you were wandering around, you spotted that Koa person Orchid mentioned. "
                " You told him that Orchid said hi. "
                " You also told him that Orchid got a new friend. "
                " Koa seemed pleased at that information. "
                " You then continued walking around the school. "
                play sound "audio/bellring.mp3"
                " The bell rings. Time for your final class of the day. "
                " You got back into the school and walked to your culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
label wedback5wed:
    # nox and jacob
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and spotted your two classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if noxknow == True and jacobknow == True:
        menu:
            " {image=noxicon} Nox {image=noxicon} ":
                jump pay
            " {image=jacobicon} Jacob {image=jacobicon} ":
                jump attention
    elif noxknow == True and jacobknow == False:
        menu:
            " {image=noxicon} A sleeping guy {image=noxicon} ":
                jump pay
            " {image=jacobicon} Jacob {image=jacobicon} ":
                jump attention
    elif noxknow == False and jacobknow == True:
        menu:
            " {image=noxicon} Nox {image=noxicon} ":
                jump pay
            " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                jump attention
    else:
        menu:
            " {image=noxicon} A sleeping guy {image=noxicon} ":
                jump pay
            " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                jump attention
    label pay:
        show noxsleepy at center with easeinbottom
        if noxknow == True:
            n " Zzzz... "
            " You're quite flabbergasted at the scene infront of you. "
            " Right now, you're seeing the boy asleep on a tree branch. "
            " You're wondering how he even got up there. "
            " And also, how he hasn't fallen just yet. "
            " It's like those scene in the movies where a cat gets stuck on a tree... "
            " Except in this case, it's one of your classmates instead. "
            " You don't know what to do, you can't exactly just wait for him to wake up. "
            " What if you waited for too long and he fell already? "
            " You aren't even sure if you could manage to carry him down without tumbling. "
            " You were thinking of what to do, when suddenly... "
            hide noxsleepy at bottom
            show noxneutral at center
            n " Hmmm...? "
            n " Oh, [name]... "
            n " Did I scare you...? "
            n " Sorry, let me get down... "
            " And then he casually jumps down from the tree like it was nothing. "
            " This leaves you to be even more flabbergasted than you were earlier. "
            " You asked him how he even got up there in the first place. "
            n " Mmm...let's see if I remember that... "
            n " Oh yeah... "
            n " I suddenly got a wave of sleepiness in the middle of class earlier... "
            n " So I wasn't really thinking clearly... "
            n " ...And I went up to sleep here... "
            n " I'm not going to lie, sleeping on a tree branch is actually quite comfortable... "
            n " Now I know why some people would like to sleep there... "
            n " I think I should sleep there more, since it's sooo comfortable... "
            n " ...I also had an interesting dream... "
            n " A dream where everything was like a visual novel... "
            n " I couldn't move, and I was just stuck in this endless dialogue loop... "
            n " A dialogue loop where I had a conversation with you... "
            n " Is that odd...? "
            n " I know it is... "
            n " What could my dreams be telling me today...? "
            n " ...No idea, but if they're being this odd right now... "
            n " I can only imagine how odd they're going to be tonight. "
            scene black with dissolve
            " You spent the rest of the break talking with Nox. "
            " His dream really was an interesting one... "
            " Maybe it's telling him something he shouldn't know. "
            play sound "audio/bellring.mp3"
            " The bell rings. Time for your final class of the day. "
            " You got back into the school and walked to your culinary arts classroom. "
            pause 2.0
            jump cookingclasswed
        else:
            x " Zzzz... "
            " You're quite flabbergasted at the scene infront of you. "
            " Right now, you're seeing the boy asleep on a tree branch. "
            " You're wondering how he even got up there. "
            " And also, how he hasn't fallen just yet. "
            " It's like those scene in the movies where a cat gets stuck on a tree... "
            " Except in this case, it's one of your classmates instead. "
            " You don't know what to do, you can't exactly just wait for him to wake up. "
            " What if you waited for too long and he fell already? "
            " You aren't even sure if you could manage to carry him down without tumbling. "
            " You were thinking of what to do, when suddenly... "
            hide noxsleepy at bottom
            show noxneutral at center
            x " Hmmm...? "
            x " Oh, [name]... "
            x " Did I scare you...? "
            x " Sorry, let me get down... "
            " And then he casually jumps down from the tree like it was nothing. "
            " This leaves you to be even more flabbergasted than you were earlier. "
            " You asked him how he even got up there in the first place. "
            x " Hmm...before I answer that, I don't think I've met you before... "
            $ noxknow = True
            n " I'm Nox, it's real nice to meet you... "
            n " Back to your question... "
            n " Mmm...let's see if I remember that... "
            n " Oh yeah... "
            n " I suddenly got a wave of sleepiness in the middle of class earlier... "
            n " So I wasn't really thinking clearly... "
            n " ...And I went up to sleep here... "
            n " I'm not going to lie, sleeping on a tree branch is actually quite comfortable... "
            n " Now I know why some people would like to sleep there... "
            n " I think I should sleep there more, since it's sooo comfortable... "
            n " ...I also had an interesting dream... "
            n " A dream where everything was like a visual novel... "
            n " I couldn't move, and I was just stuck in this endless dialogue loop... "
            n " A dialogue loop where I had a conversation with you... "
            n " Is that odd...? "
            n " I know it is... "
            n " What could my dreams be telling me today...? "
            n " ...No idea, but if they're being this odd right now... "
            n " I can only imagine how odd they're going to be tonight. "
            scene black with dissolve
            " You spent the rest of the break talking with Nox. "
            " His dream really was an interesting one... "
            " Maybe it's telling him something he shouldn't know. "
            play sound "audio/bellring.mp3"
            " The bell rings. Time for your final class of the day. "
            " You got back into the school and walked to your culinary arts classroom. "
            pause 2.0
            jump cookingclasswed
    label attention:
        show jacobneutral at center with easeinleft
        if jacobknow == True:
            " You walked up to him and spotted him staring at something. "
            " You try to take a look on what he was looking at, and... "
            " ...Is that a comically large spider. "
            " How did that even get in here??? "
            " I mean, you guys WERE at the back of the school so it made sense. "
            " The other guy you were with looked like he was planning something though. "
            " You don't know what it was, but it looked like a good plan. "
            " You just waited until he said something. "
            hide jacobneutral at bottom
            show jacobsurprised at center
            jac " ...Oh, uh - [name], hi there. "
            jac " Just thinking of what to do with this spider. "
            hide jacobsurprised at bottom
            show jacobneutral at center
            jac " I don't know where it's from, but it's just been sitting there and... "
            jac " ...Staring at me in this really creepy way. "
            jac " Heuughh... "
            jac " I would love to slice it up, yes, "
            jac " But I don't exactly know if it's real or not. "
            jac " I was just wandering around and suddenly it dropped by, near me. "
            jac " I've been staring at it ever since. "
            jac " It hasn't even made a move yet... "
            jac " Hm. Guess there's one thing to prove if it's real or not. "
            jac " [name], how about you hold it down with a stick? "
            menu:
                " hell yeah ":
                    $ jacoblv += 10
                    jac " Good. Let me just find a long enough stick, aaaand... "
                    hide jacobneutral at bottom
                    show jacobhappy at center
                    jac " Oh hey, there's one over here. Perfect. "
                    " Jacob picks the stick up and gives it to you. "
                    hide jacobhappy at bottom
                    show jacobneutral at center
                    jac " Okay, now just slowly and carefully... "
                    jac " Put it on the spider. "
                    " You slowly and carefully moved the stick towards the spider... "
                    " ...Then quickly held the spider down with the stick. "
                    " It started squirming a whole lot! "
                    hide jacobneutral at bottom
                    show jacobsurprised at center
                    jac " Oh, so it IS alive! "
                    jac " Great, that means I can cut it up! "
                    hide jacobsurprised at bottom
                    show jacobneutral at center
                    jac " Just hold it down for me for a little longer... "
                    " For reasonable purposes, we're not showing you that scene of Jacob cutting it up. "
                    " Let's just say the spider lost all of its limbs. "
                    " Jacob eventually threw the big spider away. "
                    jac " Jeez, wonder where that spider even came from in the first place... "
                    jac " A spider with THAT size isn't normal at all. "
                    jac " Most likely another one of Temero's expierements. "
                    jac " That girl is really odd, I tell you... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob. "
                    " Jacob was kinda right, since it looked like something that would come out of a horror movie. "
                    " And it looked like something that came out of a lab. "
                    " It was pretty interesting to see something like that, though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for your final class of the day. "
                    " You got back into the school and walked to your culinary arts classroom. "
                    pause 2.0
                    jump cookingclasswed
                " spiders are my worst enemy ":
                    $ jacoblv += 5
                    jac " Really? well damn. "
                    jac " I'll just hold it down myself then. "
                    jac " If you don't mind, could you find me a long stick? "
                    " You looked around you... "
                    " And found a perfectly long stick! "
                    " You then gave the stick to Jacob. "
                    jac " Hmm...it's perfect. "
                    jac " Now, let me just do this.. "
                    " Jacob holds the spider down with the stick. "
                    " ...The spider starts squirming a lot! "
                    hide jacobneutral at bottom
                    show jacobsurprised at center
                    jac " Oh, so it IS alive! "
                    jac " Great, that means I can cut it up! "
                    hide jacobsurprised at bottom
                    show jacobneutral at center
                    jac " Let me just hold it down a bit more... "
                    " For reasonable purposes, we're not showing you that scene of Jacob cutting it up. "
                    " Let's just say the spider lost all of its limbs. "
                    " Jacob eventually threw the big spider away. "
                    jac " Jeez, wonder where that spider even came from in the first place... "
                    jac " A spider with THAT size isn't normal at all. "
                    jac " Most likely another one of Temero's expierements. "
                    jac " That girl is really odd, I tell you... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob. "
                    " Jacob was kinda right, since it looked like something that would come out of a horror movie. "
                    " And it looked like something that came out of a lab. "
                    " It was pretty interesting to see something like that, though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for your final class of the day. "
                    " You got back into the school and walked to your culinary arts classroom. "
                    pause 2.0
                    jump cookingclasswed
        else:
            " You walked up to him and spotted him staring at something. "
            " You try to take a look on what he was looking at, and... "
            " ...Is that a comically large spider. "
            " How did that even get in here??? "
            " I mean, you guys WERE at the back of the school so it made sense. "
            " The other guy you were with looked like he was planning something though. "
            " You don't know what it was, but it looked like a good plan. "
            " You just waited until he said something. "
            hide jacobneutral at bottom
            show jacobsurprised at center
            x " ...Oh, uh - [name], hi there."
            x " Just thinking of what to do with this spider. "
            hide jacobsurprised at bottom
            show jacobneutral at center
            $ jacobknow = True
            jac " I'm Jacob, by the way. "
            jac " Anyway - I don't know where it's from, but it's just been sitting there and... "
            jac " ...Staring at me in this really creepy way. "
            jac " Heuughh... "
            jac " I would love to slice it up, yes, "
            jac " But I don't exactly know if it's real or not. "
            jac " I was just wandering around and suddenly it dropped by, near me. "
            jac " I've been staring at it ever since. "
            jac " It hasn't even made a move yet... "
            jac " Hm. Guess there's one thing to prove if it's real or not. "
            jac " [name], how about you hold it down with a stick? "
            menu:
                " hell yeah ":
                    $ jacoblv += 10
                    jac " Good. Let me just find a long enough stick, aaaand... "
                    hide jacobneutral at bottom
                    show jacobhappy at center
                    jac " Oh hey, there's one over here. Perfect. "
                    " Jacob picks the stick up and gives it to you. "
                    hide jacobhappy at bottom
                    show jacobneutral at center
                    jac " Okay, now just slowly and carefully... "
                    jac " Put it on the spider. "
                    " You slowly and carefully moved the stick towards the spider... "
                    " ...Then quickly held the spider down with the stick. "
                    " It started squirming a whole lot! "
                    hide jacobneutral at bottom
                    show jacobsurprised at center
                    jac " Oh, so it IS alive! "
                    jac " Great, that means I can cut it up! "
                    hide jacobsurprised at bottom
                    show jacobneutral at center
                    jac " Just hold it down for me for a little longer... "
                    " For reasonable purposes, we're not showing you that scene of Jacob cutting it up. "
                    " Let's just say the spider lost all of its limbs. "
                    " Jacob eventually threw the big spider away. "
                    jac " Jeez, wonder where that spider even came from in the first place... "
                    jac " A spider with THAT size isn't normal at all. "
                    jac " Most likely another one of Temero's expierements. "
                    jac " That girl is really odd, I tell you... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob. "
                    " Jacob was kinda right, since it looked like something that would come out of a horror movie. "
                    " And it looked like something that came out of a lab. "
                    " It was pretty interesting to see something like that, though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for your final class of the day. "
                    " You got back into the school and walked to your culinary arts classroom. "
                    pause 2.0
                    jump cookingclasswed
                " spiders are my worst enemy ":
                    $ jacoblv += 5
                    jac " Really? well damn. "
                    jac " I'll just hold it down myself then. "
                    jac " If you don't mind, could you find me a long stick? "
                    " You looked around you... "
                    " And found a perfectly long stick! "
                    " You then gave the stick to Jacob. "
                    jac " Hmm...it's perfect. "
                    jac " Now, let me just do this.. "
                    " Jacob holds the spider down with the stick. "
                    " ...The spider starts squirming a lot! "
                    hide jacobneutral at bottom
                    show jacobsurprised at center
                    jac " Oh, so it IS alive! "
                    jac " Great, that means I can cut it up! "
                    hide jacobsurprised at bottom
                    show jacobneutral at center
                    jac " Let me just hold it down a bit more... "
                    " For reasonable purposes, we're not showing you that scene of Jacob cutting it up. "
                    " Let's just say the spider lost all of its limbs. "
                    " Jacob eventually threw the big spider away. "
                    jac " Jeez, wonder where that spider even came from in the first place... "
                    jac " A spider with THAT size isn't normal at all. "
                    jac " Most likely another one of Temero's expierements. "
                    jac " That girl is really odd, I tell you... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob. "
                    " Jacob was kinda right, since it looked like something that would come out of a horror movie. "
                    " And it looked like something that came out of a lab. "
                    " It was pretty interesting to see something like that, though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for your final class of the day. "
                    " You got back into the school and walked to your culinary arts classroom. "
                    pause 2.0
                    jump cookingclasswed
label wedgym5wed:
    # disk and temero
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym and found your two classmates talking with eachother. "
    " Wondering what they're talking about, you decided to join into their conversation. "
    show diskhappy at right with easeinleft
    show temeroneutral at left with easeinleft
    if diskknow == True and temeroknow == True:
        d " Hey there, 'Mero! Hey there [name]! "
        hide temeroneutral at bottom
        show temerohappy at left
        tm " Diiiisk! It's nice to see you here! "
        tm " Oh, and hey [name]. Nice to see you too. "
        hide temerohappy at bottom
        hide diskhappy at bottom
        show diskneutral at right
        show temeroneutral at left
        d " How have you been doing? "
        tm " I've been doing fine, as per usual. "
        tm " The great Temero is always fine! "
        d " That's wonderful! "
        d " Do you think you'd be up to joining my party this friday? "
        tm " Oooh? of course you'd have a party this friday. "
        tm " But I'm sure my dads would be cool with joining your party. "
        tm " Besides, I don't have any work today! "
        d " Wonderful! Maybe you could bring some of those cool tricks you could do? "
        tm " I could, I could... "
        tm " As long as I'll do the ones that aren't dangerous. "
        d " Oh, it better be nothing dangerous!! "
        hide diskneutral at bottom
        show diskangry at right
        d " You know how badly the guards reacted when you brang in one of your projects.. "
        tm " Aha...yeah. "
        tm " I'll be sure not to bring THAT in again. "
        tm " Sorry for scaring your guards so much. "
        hide diskangry at bottom
        show diskneutral at right
        d " It's alright - they're pretty much calm with you now. "
        d " Thankfully...I had to convince them a whole lot after that night! "
        d " And I really didn't want my parents to be worrying about you... "
        d " I have a feeling if I didn't convince them, you'd be banned out of my mansion. "
        tm " Eeeyikes. Good thing you convinced them though. "
        d " Yeah!! "
        if diskparty == True:
            d " Did you know? [name] is going to join the party too! "
            tm " Really? that's lovely! "
            tm " It's going to be a good first expirience for [them], I'm sure of it. "
            tm " [name] - Disk's parties are always lovely and lively. "
            tm " There's going to be a few minigames here and there, oh and the FOOD. "
            hide temeroneutral at bottom
            show temerohappy at left
            tm " The food there is ABSOLUTELY delicious! "
            tm " The moment you arrive there I'm immediately dragging you to the kitchen. "
            d " Hehe...my cooks always love to cook for you guys! "
            d " They think everyone brings a nice chaotic-ness everytime I do a party! "
            tm " Mhm, hopefully we don't get too chaotic this night though. "
            d " Yeeep! or else my guards would freak out again... "
            scene black with dissolve
            " You spent the rest of the break hanging out with Temero and Disk. "
            " Now you can't wait for the party that Disk mentioned... "
            " It's on friday from what he mentioned. You only need to wait for a few days until it's friday. "
            " Time to do a whole lot of waiting, then... "
            play sound "audio/bellring.mp3"
            " The bell rings. Time for your final class of the day. "
            " You got out of the gym and walked to your culinary arts classroom. "
            pause 2.0
            jump cookingclasswed
        else:
            d " Oh, right! [name]... "
            d " You wanna join my party this friday? "
            d " I won't force you if you don't want to, I'm just asking. "
            menu:
                " Join the party ":
                    $ disklv += 10
                    $ diskparty = True
                    hide diskneutral at bottom
                    show diskhappy at right
                    d " YAHOO!! "
                    d " Glad that you're joining, [name]! "
                    tm " It's going to be a good first expirience for [them], I'm sure of it. "
                    tm " [name] - Disk's parties are always lovely and lively. "
                    tm " There's going to be a few minigames here and there, oh and the FOOD. "
                    hide temeroneutral at bottom
                    show temerohappy at left
                    tm " The food there is ABSOLUTELY delicious! "
                    tm " The moment you arrive there I'm immediately dragging you to the kitchen. "
                    d " Hehe...my cooks always love to cook for you guys! "
                    d " They think everyone brings a nice chaotic-ness everytime I do a party! "
                    tm " Mhm, hopefully we don't get too chaotic this night though. "
                    d " Yeeep! or else my guards would freak out again... "
                    scene black with dissolve
                    " You spent the rest of the break hanging out with Temero and Disk. "
                    " Now you can't wait for the party that Disk mentioned... "
                    " It's on friday from what he mentioned. You only need to wait for a few days until it's friday. "
                    " Time to do a whole lot of waiting, then... "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for your final class of the day. "
                    " You got out of the gym and walked to your culinary arts classroom. "
                    pause 2.0
                    jump cookingclasswed
                " No thanks ":
                    d " Well, that's a shame... "
                    d " It's okay that you don't want to, though! "
                    d " I don't want to force you, after all. "
                    tm " Hmhmmm... "
                    tm " I'm still thinking about the food at your house... "
                    tm " How come your chefs are so good at cooking? "
                    d " They're trained to be great like that! "
                    d " They also get paid well by my parents, so I guess that's what keeps them motivated? "
                    d " They get paid a good amount monthly... "
                    d " My parents aren't really the type to underpay them. "
                    d " If they're doing a good job, then they get paid good! "
                    d " And of course, if they're doing bad, then they get paid less. "
                    d " It's simple as that, really! "
                    tm " Huh...how much do your parents pay them monthly? "
                    d " About 5k monthly. "
                    tm " DAMN. Okay, I can see why they love their job. "
                    tm " Ever got cooks who are just there for the money? "
                    d " Of course! They pretty much just get kicked out immediately though. "
                    tm " That's a good thing, then. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Temero. "
                    " Huh...you wonder what it would be like to be a chef for Disk. "
                    " You're not exactly a good cook though. "
                    " You're going to have to learn a lot about cooking if you want to be a cook for him. "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for your final class of the day. "
                    " You got out of the gym and walked to your culinary arts classroom. "
                    pause 2.0
                    jump cookingclasswed
    elif diskknow == True and temeroknow == False:
        d " Hey there, 'Mero! Hey there [name]! "
        $ temeroknow = True
        hide temeroneutral at bottom
        show temerohappy at left
        " So Temero's her name..interesting. "
        tm " Diiiisk! It's nice to see you here! "
        tm " Oh, and hey [name]. Nice to see you too. "
        hide temerohappy at bottom
        hide diskhappy at bottom
        show diskneutral at right
        show temeroneutral at left
        d " How have you been doing? "
        tm " I've been doing fine, as per usual. "
        tm " The great Temero is always fine! "
        d " That's wonderful! "
        d " Do you think you'd be up to joining my party this friday? "
        tm " Oooh? of course you'd have a party this friday. "
        tm " But I'm sure my dads would be cool with joining your party. "
        tm " Besides, I don't have any work today! "
        d " Wonderful! Maybe you could bring some of those cool tricks you could do? "
        tm " I could, I could... "
        tm " As long as I'll do the ones that aren't dangerous. "
        d " Oh, it better be nothing dangerous!! "
        hide diskneutral at bottom
        show diskangry at right
        d " You know how badly the guards reacted when you brang in one of your projects.. "
        tm " Aha...yeah. "
        tm " I'll be sure not to bring THAT in again. "
        tm " Sorry for scaring your guards so much. "
        hide diskangry at bottom
        show diskneutral at right
        d " It's alright - they're pretty much calm with you now. "
        d " Thankfully...I had to convince them a whole lot after that night! "
        d " And I really didn't want my parents to be worrying about you... "
        d " I have a feeling if I didn't convince them, you'd be banned out of my mansion. "
        tm " Eeeyikes. Good thing you convinced them though. "
        d " Yeah!! "
        if diskparty == True:
            d " Did you know? [name] is going to join the party too! "
            tm " Really? that's lovely! "
            tm " It's going to be a good first expirience for [them], I'm sure of it. "
            tm " [name] - Disk's parties are always lovely and lively. "
            tm " There's going to be a few minigames here and there, oh and the FOOD. "
            hide temeroneutral at bottom
            show temerohappy at left
            tm " The food there is ABSOLUTELY delicious! "
            tm " The moment you arrive there I'm immediately dragging you to the kitchen. "
            d " Hehe...my cooks always love to cook for you guys! "
            d " They think everyone brings a nice chaotic-ness everytime I do a party! "
            tm " Mhm, hopefully we don't get too chaotic this night though. "
            d " Yeeep! or else my guards would freak out again... "
            scene black with dissolve
            " You spent the rest of the break hanging out with Temero and Disk. "
            " Now you can't wait for the party that Disk mentioned... "
            " It's on friday from what he mentioned. You only need to wait for a few days until it's friday. "
            " Time to do a whole lot of waiting, then... "
            play sound "audio/bellring.mp3"
            " The bell rings. Time for your final class of the day. "
            " You got out of the gym and walked to your culinary arts classroom. "
            pause 2.0
            jump cookingclasswed
        else:
            d " Oh, right! [name]... "
            d " You wanna join my party this friday? "
            d " I won't force you if you don't want to, I'm just asking. "
            menu:
                " Join the party ":
                    $ disklv += 10
                    $ diskparty = True
                    hide diskneutral at bottom
                    show diskhappy at right
                    d " YAHOO!! "
                    d " Glad that you're joining, [name]! "
                    tm " It's going to be a good first expirience for [them], I'm sure of it. "
                    tm " [name] - Disk's parties are always lovely and lively. "
                    tm " There's going to be a few minigames here and there, oh and the FOOD. "
                    hide temeroneutral at bottom
                    show temerohappy at left
                    tm " The food there is ABSOLUTELY delicious! "
                    tm " The moment you arrive there I'm immediately dragging you to the kitchen. "
                    d " Hehe...my cooks always love to cook for you guys! "
                    d " They think everyone brings a nice chaotic-ness everytime I do a party! "
                    tm " Mhm, hopefully we don't get too chaotic this night though. "
                    d " Yeeep! or else my guards would freak out again... "
                    scene black with dissolve
                    " You spent the rest of the break hanging out with Temero and Disk. "
                    " Now you can't wait for the party that Disk mentioned... "
                    " It's on friday from what he mentioned. You only need to wait for a few days until it's friday. "
                    " Time to do a whole lot of waiting, then... "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for your final class of the day. "
                    " You got out of the gym and walked to your culinary arts classroom. "
                    pause 2.0
                    jump cookingclasswed
                " No thanks ":
                    d " Well, that's a shame... "
                    d " It's okay that you don't want to, though! "
                    d " I don't want to force you, after all. "
                    tm " Hmhmmm... "
                    tm " I'm still thinking about the food at your house... "
                    tm " How come your chefs are so good at cooking? "
                    d " They're trained to be great like that! "
                    d " They also get paid well by my parents, so I guess that's what keeps them motivated? "
                    d " They get paid a good amount monthly... "
                    d " My parents aren't really the type to underpay them. "
                    d " If they're doing a good job, then they get paid good! "
                    d " And of course, if they're doing bad, then they get paid less. "
                    d " It's simple as that, really! "
                    tm " Huh...how much do your parents pay them monthly? "
                    d " About 5k monthly. "
                    tm " DAMN. Okay, I can see why they love their job. "
                    tm " Ever got cooks who are just there for the money? "
                    d " Of course! They pretty much just get kicked out immediately though. "
                    tm " That's a good thing, then. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Temero. "
                    " Huh...you wonder what it would be like to be a chef for Disk. "
                    " You're not exactly a good cook though. "
                    " You're going to have to learn a lot about cooking if you want to be a cook for him. "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for your final class of the day. "
                    " You got out of the gym and walked to your culinary arts classroom. "
                    pause 2.0
                    jump cookingclasswed
    elif diskknow == False and temeroknow == True:
        x " Hey there, 'Mero! Hey there [name]! "
        hide temeroneutral at bottom
        show temerohappy at left
        tm " Diiiisk! It's nice to see you here! "
        " So Disk is his name...okay, got it. "
        tm " Oh, and hey [name]. Nice to see you too. "
        hide temerohappy at bottom
        hide diskhappy at bottom
        show diskneutral at right
        show temeroneutral at left
        d " How have you been doing? "
        tm " I've been doing fine, as per usual. "
        tm " The great Temero is always fine! "
        d " That's wonderful! "
        d " Do you think you'd be up to joining my party this friday? "
        tm " Oooh? of course you'd have a party this friday. "
        tm " But I'm sure my dads would be cool with joining your party. "
        tm " Besides, I don't have any work today! "
        d " Wonderful! Maybe you could bring some of those cool tricks you could do? "
        tm " I could, I could... "
        tm " As long as I'll do the ones that aren't dangerous. "
        d " Oh, it better be nothing dangerous!! "
        hide diskneutral at bottom
        show diskangry at right
        d " You know how badly the guards reacted when you brang in one of your projects.. "
        tm " Aha...yeah. "
        tm " I'll be sure not to bring THAT in again. "
        tm " Sorry for scaring your guards so much. "
        hide diskangry at bottom
        show diskneutral at right
        d " It's alright - they're pretty much calm with you now. "
        d " Thankfully...I had to convince them a whole lot after that night! "
        d " And I really didn't want my parents to be worrying about you... "
        d " I have a feeling if I didn't convince them, you'd be banned out of my mansion. "
        tm " Eeeyikes. Good thing you convinced them though. "
        d " Yeah!! "
        if diskparty == True:
            d " Did you know? [name] is going to join the party too! "
            tm " Really? that's lovely! "
            tm " It's going to be a good first expirience for [them], I'm sure of it. "
            tm " [name] - Disk's parties are always lovely and lively. "
            tm " There's going to be a few minigames here and there, oh and the FOOD. "
            hide temeroneutral at bottom
            show temerohappy at left
            tm " The food there is ABSOLUTELY delicious! "
            tm " The moment you arrive there I'm immediately dragging you to the kitchen. "
            d " Hehe...my cooks always love to cook for you guys! "
            d " They think everyone brings a nice chaotic-ness everytime I do a party! "
            tm " Mhm, hopefully we don't get too chaotic this night though. "
            d " Yeeep! or else my guards would freak out again... "
            scene black with dissolve
            " You spent the rest of the break hanging out with Temero and Disk. "
            " Now you can't wait for the party that Disk mentioned... "
            " It's on friday from what he mentioned. You only need to wait for a few days until it's friday. "
            " Time to do a whole lot of waiting, then... "
            play sound "audio/bellring.mp3"
            " The bell rings. Time for your final class of the day. "
            " You got out of the gym and walked to your culinary arts classroom. "
            pause 2.0
            jump cookingclasswed
        else:
            d " Oh, right! [name]... "
            d " You wanna join my party this friday? "
            d " I won't force you if you don't want to, I'm just asking. "
            menu:
                " Join the party ":
                    $ disklv += 10
                    $ diskparty = True
                    hide diskneutral at bottom
                    show diskhappy at right
                    d " YAHOO!! "
                    d " Glad that you're joining, [name]! "
                    tm " It's going to be a good first expirience for [them], I'm sure of it. "
                    tm " [name] - Disk's parties are always lovely and lively. "
                    tm " There's going to be a few minigames here and there, oh and the FOOD. "
                    hide temeroneutral at bottom
                    show temerohappy at left
                    tm " The food there is ABSOLUTELY delicious! "
                    tm " The moment you arrive there I'm immediately dragging you to the kitchen. "
                    d " Hehe...my cooks always love to cook for you guys! "
                    d " They think everyone brings a nice chaotic-ness everytime I do a party! "
                    tm " Mhm, hopefully we don't get too chaotic this night though. "
                    d " Yeeep! or else my guards would freak out again... "
                    scene black with dissolve
                    " You spent the rest of the break hanging out with Temero and Disk. "
                    " Now you can't wait for the party that Disk mentioned... "
                    " It's on friday from what he mentioned. You only need to wait for a few days until it's friday. "
                    " Time to do a whole lot of waiting, then... "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for your final class of the day. "
                    " You got out of the gym and walked to your culinary arts classroom. "
                    pause 2.0
                    jump cookingclasswed
                " No thanks ":
                    d " Well, that's a shame... "
                    d " It's okay that you don't want to, though! "
                    d " I don't want to force you, after all. "
                    tm " Hmhmmm... "
                    tm " I'm still thinking about the food at your house... "
                    tm " How come your chefs are so good at cooking? "
                    d " They're trained to be great like that! "
                    d " They also get paid well by my parents, so I guess that's what keeps them motivated? "
                    d " They get paid a good amount monthly... "
                    d " My parents aren't really the type to underpay them. "
                    d " If they're doing a good job, then they get paid good! "
                    d " And of course, if they're doing bad, then they get paid less. "
                    d " It's simple as that, really! "
                    tm " Huh...how much do your parents pay them monthly? "
                    d " About 5k monthly. "
                    tm " DAMN. Okay, I can see why they love their job. "
                    tm " Ever got cooks who are just there for the money? "
                    d " Of course! They pretty much just get kicked out immediately though. "
                    tm " That's a good thing, then. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Temero. "
                    " Huh...you wonder what it would be like to be a chef for Disk. "
                    " You're not exactly a good cook though. "
                    " You're going to have to learn a lot about cooking if you want to be a cook for him. "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for your final class of the day. "
                    " You got out of the gym and walked to your culinary arts classroom. "
                    pause 2.0
                    jump cookingclasswed
    else:
        d " Hey there, 'Mero! Hey there [name]! "
        hide temeroneutral at bottom
        show temerohappy at left
        tm " Diiiisk! It's nice to see you here! "
        tm " Oh, and hey [name]. Nice to see you too. "
        hide temerohappy at bottom
        hide diskhappy at bottom
        show diskneutral at right
        show temeroneutral at left
        d " How have you been doing? "
        tm " I've been doing fine, as per usual. "
        tm " The great Temero is always fine! "
        d " That's wonderful! "
        d " Do you think you'd be up to joining my party this friday? "
        tm " Oooh? of course you'd have a party this friday. "
        tm " But I'm sure my dads would be cool with joining your party. "
        tm " Besides, I don't have any work today! "
        d " Wonderful! Maybe you could bring some of those cool tricks you could do? "
        tm " I could, I could... "
        tm " As long as I'll do the ones that aren't dangerous. "
        d " Oh, it better be nothing dangerous!! "
        hide diskneutral at bottom
        show diskangry at right
        d " You know how badly the guards reacted when you brang in one of your projects.. "
        tm " Aha...yeah. "
        tm " I'll be sure not to bring THAT in again. "
        tm " Sorry for scaring your guards so much. "
        hide diskangry at bottom
        show diskneutral at right
        d " It's alright - they're pretty much calm with you now. "
        d " Thankfully...I had to convince them a whole lot after that night! "
        d " And I really didn't want my parents to be worrying about you... "
        d " I have a feeling if I didn't convince them, you'd be banned out of my mansion. "
        tm " Eeeyikes. Good thing you convinced them though. "
        d " Yeah!! "
        if diskparty == True:
            d " Did you know? [name] is going to join the party too! "
            tm " Really? that's lovely! "
            tm " It's going to be a good first expirience for [them], I'm sure of it. "
            tm " [name] - Disk's parties are always lovely and lively. "
            tm " There's going to be a few minigames here and there, oh and the FOOD. "
            hide temeroneutral at bottom
            show temerohappy at left
            tm " The food there is ABSOLUTELY delicious! "
            tm " The moment you arrive there I'm immediately dragging you to the kitchen. "
            d " Hehe...my cooks always love to cook for you guys! "
            d " They think everyone brings a nice chaotic-ness everytime I do a party! "
            tm " Mhm, hopefully we don't get too chaotic this night though. "
            d " Yeeep! or else my guards would freak out again... "
            scene black with dissolve
            " You spent the rest of the break hanging out with Temero and Disk. "
            " Now you can't wait for the party that Disk mentioned... "
            " It's on friday from what he mentioned. You only need to wait for a few days until it's friday. "
            " Time to do a whole lot of waiting, then... "
            play sound "audio/bellring.mp3"
            " The bell rings. Time for your final class of the day. "
            " You got out of the gym and walked to your culinary arts classroom. "
            pause 2.0
            jump cookingclasswed
        else:
            d " Oh, right! [name]... "
            d " You wanna join my party this friday? "
            d " I won't force you if you don't want to, I'm just asking. "
            menu:
                " Join the party ":
                    $ disklv += 10
                    $ diskparty = True
                    hide diskneutral at bottom
                    show diskhappy at right
                    d " YAHOO!! "
                    d " Glad that you're joining, [name]! "
                    tm " It's going to be a good first expirience for [them], I'm sure of it. "
                    tm " [name] - Disk's parties are always lovely and lively. "
                    tm " There's going to be a few minigames here and there, oh and the FOOD. "
                    hide temeroneutral at bottom
                    show temerohappy at left
                    tm " The food there is ABSOLUTELY delicious! "
                    tm " The moment you arrive there I'm immediately dragging you to the kitchen. "
                    d " Hehe...my cooks always love to cook for you guys! "
                    d " They think everyone brings a nice chaotic-ness everytime I do a party! "
                    tm " Mhm, hopefully we don't get too chaotic this night though. "
                    d " Yeeep! or else my guards would freak out again... "
                    scene black with dissolve
                    " You spent the rest of the break hanging out with Temero and Disk. "
                    " Now you can't wait for the party that Disk mentioned... "
                    " It's on friday from what he mentioned. You only need to wait for a few days until it's friday. "
                    " Time to do a whole lot of waiting, then... "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for your final class of the day. "
                    " You got out of the gym and walked to your culinary arts classroom. "
                    pause 2.0
                    jump cookingclasswed
                " No thanks ":
                    d " Well, that's a shame... "
                    d " It's okay that you don't want to, though! "
                    d " I don't want to force you, after all. "
                    tm " Hmhmmm... "
                    tm " I'm still thinking about the food at your house... "
                    tm " How come your chefs are so good at cooking? "
                    d " They're trained to be great like that! "
                    d " They also get paid well by my parents, so I guess that's what keeps them motivated? "
                    d " They get paid a good amount monthly... "
                    d " My parents aren't really the type to underpay them. "
                    d " If they're doing a good job, then they get paid good! "
                    d " And of course, if they're doing bad, then they get paid less. "
                    d " It's simple as that, really! "
                    tm " Huh...how much do your parents pay them monthly? "
                    d " About 5k monthly. "
                    tm " DAMN. Okay, I can see why they love their job. "
                    tm " Ever got cooks who are just there for the money? "
                    d " Of course! They pretty much just get kicked out immediately though. "
                    tm " That's a good thing, then. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Temero. "
                    " Huh...you wonder what it would be like to be a chef for Disk. "
                    " You're not exactly a good cook though. "
                    " You're going to have to learn a lot about cooking if you want to be a cook for him. "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for your final class of the day. "
                    " You got out of the gym and walked to your culinary arts classroom. "
                    pause 2.0
                    jump cookingclasswed
label wedcafeteria5wed:
    # matte and jam
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked to the cafeteria and found two of your classmates talking with eachother. "
    " Wondering what they're talking about, you walked over to them and at next to them. "
    " Let's see what they're talking about... "
    show matteneutral at left with easeinright
    show jamneutral at right with easeinright
    if matteknow == True and jamknow == True:
        ma " Hey there [name]! "
        ja " ...Hi, [name]. "
        ja " I have something to say that might make you happy, Matte. "
        ja " I think you know what it is... "
        ma " Really? Um, let me guess! "
        ma " Did your parents finally agree to letting me come over? "
        ja " Nope, unfortunately that's not it. "
        ma " Aw... it would be fun if I went there though! "
        ma " Let me try again, hmmm... "
        ma " Did your parents give you something nice? "
        ja " They would most likely never do that. "
        ja " The only time where they'd do that is on my birthday. "
        hide matteneutral at bottom
        show matteangry at left
        ma " Aww...your parents are just really mean! "
        ma " How can you put up with this? "
        ja " ...Guess I'm just used to the treatment. "
        ja " Even if it's something I shouldn't get used to... "
        ja " I just did, throughout the years. "
        ma " Sighhh... "
        hide matteangry at bottom
        show matteneutral at left
        ma " Let me go back to guessing, then... "
        ma " ...Oh wait, OH WAIT! "
        hide matteneutral at bottom
        show mattehappy at left
        ma " Did you finally get another friend?! "
        hide jamneutral at bottom
        show jamhappy at right
        ja " ...Yeah, I did. "
        ma " Eee! I'm so happy for you! "
        ma " Who's this friend of yours? What's their name? "
        ja " ...Orchid. Their name is Orchid. "
        hide mattehappy at bottom
        show matteneutral at left
        ma " Oooh, Orchid! I know them! "
        ma " They're a real nice person, you'd like them! "
        ma " I heard they're into Zatzune Ziku! "
        ja " Mmm...that's the whole reason why we became friends, actually. "
        ja " Someone said something about Ziku, and we both got excited. "
        ja " They even offered to give me some of their Ziku merch to me... "
        ma " Aww, that's so nice of them! "
        ja " I know, right? "
        ma " I'm really glad that you got a new friend, Jam! "
        ja " I'm proud of myself, too... "
        scene black with dissolve
        " You spent the rest of the break hanging out with Matte and Jam. "
        " Now that you think about it... "
        " The name Zatzune Ziku sounds familiar. "
        " Not sure where you've heard it, but it's familiar. "
        " Probably have heard it from one of those documentaries you've been watching. "
        play sound "audio/bellring.mp3"
        " The bell rings. Time for your final class of the day. "
        " You got out of the cafeteria and walked to your culinary arts classroom. "
        pause 2.0
        jump cookingclasswed
    elif matteknow == True and jamknow == False:
        ma " Hey there [name]! "
        x " ...Hi, [name]. "
        ma " Ooo, wait! I don't think you've met my friend, [name]! "
        $ jamknow = True
        ma " This is my friend, Jam! "
        ja " ...Nice to meet you. Anyway... "
        ja " I have something to say that might make you happy, Matte. "
        ja " I think you know what it is... "
        ma " Really? Um, let me guess! "
        ma " Did your parents finally agree to letting me come over? "
        ja " Nope, unfortunately that's not it. "
        ma " Aw... it would be fun if I went there though! "
        ma " Let me try again, hmmm... "
        ma " Did your parents give you something nice? "
        ja " They would most likely never do that. "
        ja " The only time where they'd do that is on my birthday. "
        hide matteneutral at bottom
        show matteangry at left
        ma " Aww...your parents are just really mean! "
        ma " How can you put up with this? "
        ja " ...Guess I'm just used to the treatment. "
        ja " Even if it's something I shouldn't get used to... "
        ja " I just did, throughout the years. "
        ma " Sighhh... "
        hide matteangry at bottom
        show matteneutral at left
        ma " Let me go back to guessing, then... "
        ma " ...Oh wait, OH WAIT! "
        hide matteneutral at bottom
        show mattehappy at left
        ma " Did you finally get another friend?! "
        hide jamneutral at bottom
        show jamhappy at right
        ja " ...Yeah, I did. "
        ma " Eee! I'm so happy for you! "
        ma " Who's this friend of yours? What's their name? "
        ja " ...Orchid. Their name is Orchid. "
        hide mattehappy at bottom
        show matteneutral at left
        ma " Oooh, Orchid! I know them! "
        ma " They're a real nice person, you'd like them! "
        ma " I heard they're into Zatzune Ziku! "
        ja " Mmm...that's the whole reason why we became friends, actually. "
        ja " Someone said something about Ziku, and we both got excited. "
        ja " They even offered to give me some of their Ziku merch to me... "
        ma " Aww, that's so nice of them! "
        ja " I know, right? "
        ma " I'm really glad that you got a new friend, Jam! "
        ja " I'm proud of myself, too... "
        scene black with dissolve
        " You spent the rest of the break hanging out with Matte and Jam. "
        " Now that you think about it... "
        " The name Zatzune Ziku sounds familiar. "
        " Not sure where you've heard it, but it's familiar. "
        " Probably have heard it from one of those documentaries you've been watching. "
        play sound "audio/bellring.mp3"
        " The bell rings. Time for your final class of the day. "
        " You got out of the cafeteria and walked to your culinary arts classroom. "
        pause 2.0
        jump cookingclasswed
    elif matteknow == False and jamknow == True:
        x " Hey there [name]! "
        ja " ...Hi, [name]. "
        ja " I have something to say that might make you happy, Matte. "
        $ matteknow = True
        ja " I think you know what it is... "
        ma " Really? Um, let me guess! "
        ma " Did your parents finally agree to letting me come over? "
        ja " Nope, unfortunately that's not it. "
        ma " Aw... it would be fun if I went there though! "
        ma " Let me try again, hmmm... "
        ma " Did your parents give you something nice? "
        ja " They would most likely never do that. "
        ja " The only time where they'd do that is on my birthday. "
        hide matteneutral at bottom
        show matteangry at left
        ma " Aww...your parents are just really mean! "
        ma " How can you put up with this? "
        ja " ...Guess I'm just used to the treatment. "
        ja " Even if it's something I shouldn't get used to... "
        ja " I just did, throughout the years. "
        ma " Sighhh... "
        hide matteangry at bottom
        show matteneutral at left
        ma " Let me go back to guessing, then... "
        ma " ...Oh wait, OH WAIT! "
        hide matteneutral at bottom
        show mattehappy at left
        ma " Did you finally get another friend?! "
        hide jamneutral at bottom
        show jamhappy at right
        ja " ...Yeah, I did. "
        ma " Eee! I'm so happy for you! "
        ma " Who's this friend of yours? What's their name? "
        ja " ...Orchid. Their name is Orchid. "
        hide mattehappy at bottom
        show matteneutral at left
        ma " Oooh, Orchid! I know them! "
        ma " They're a real nice person, you'd like them! "
        ma " I heard they're into Zatzune Ziku! "
        ja " Mmm...that's the whole reason why we became friends, actually. "
        ja " Someone said something about Ziku, and we both got excited. "
        ja " They even offered to give me some of their Ziku merch to me... "
        ma " Aww, that's so nice of them! "
        ja " I know, right? "
        ma " I'm really glad that you got a new friend, Jam! "
        ja " I'm proud of myself, too... "
        scene black with dissolve
        " You spent the rest of the break hanging out with Matte and Jam. "
        " Now that you think about it... "
        " The name Zatzune Ziku sounds familiar. "
        " Not sure where you've heard it, but it's familiar. "
        " Probably have heard it from one of those documentaries you've been watching. "
        play sound "audio/bellring.mp3"
        " The bell rings. Time for your final class of the day. "
        " You got out of the cafeteria and walked to your culinary arts classroom. "
        pause 2.0
        jump cookingclasswed
    else:
        x " Hey there [name]! "
        x " ...Hi, [name]. "
        x " Hold on, I don't think I've introduced myself to you yet! "
        $ matteknow = True
        ma " I'm Matte, it's nice to meet you! "
        ma " I don't think you've met my yet friend, [name]! "
        $ jamknow = True
        ma " This is my friend, Jam! "
        ja " ...Nice to meet you. Anyway... "
        ja " I have something to say that might make you happy, Matte. "
        ja " I think you know what it is... "
        ma " Really? Um, let me guess! "
        ma " Did your parents finally agree to letting me come over? "
        ja " Nope, unfortunately that's not it. "
        ma " Aw... it would be fun if I went there though! "
        ma " Let me try again, hmmm... "
        ma " Did your parents give you something nice? "
        ja " They would most likely never do that. "
        ja " The only time where they'd do that is on my birthday. "
        hide matteneutral at bottom
        show matteangry at left
        ma " Aww...your parents are just really mean! "
        ma " How can you put up with this? "
        ja " ...Guess I'm just used to the treatment. "
        ja " Even if it's something I shouldn't get used to... "
        ja " I just did, throughout the years. "
        ma " Sighhh... "
        hide matteangry at bottom
        show matteneutral at left
        ma " Let me go back to guessing, then... "
        ma " ...Oh wait, OH WAIT! "
        hide matteneutral at bottom
        show mattehappy at left
        ma " Did you finally get another friend?! "
        hide jamneutral at bottom
        show jamhappy at right
        ja " ...Yeah, I did. "
        ma " Eee! I'm so happy for you! "
        ma " Who's this friend of yours? What's their name? "
        ja " ...Orchid. Their name is Orchid. "
        hide mattehappy at bottom
        show matteneutral at left
        ma " Oooh, Orchid! I know them! "
        ma " They're a real nice person, you'd like them! "
        ma " I heard they're into Zatzune Ziku! "
        ja " Mmm...that's the whole reason why we became friends, actually. "
        ja " Someone said something about Ziku, and we both got excited. "
        ja " They even offered to give me some of their Ziku merch to me... "
        ma " Aww, that's so nice of them! "
        ja " I know, right? "
        ma " I'm really glad that you got a new friend, Jam! "
        ja " I'm proud of myself, too... "
        scene black with dissolve
        " You spent the rest of the break hanging out with Matte and Jam. "
        " Now that you think about it... "
        " The name Zatzune Ziku sounds familiar. "
        " Not sure where you've heard it, but it's familiar. "
        " Probably have heard it from one of those documentaries you've been watching. "
        play sound "audio/bellring.mp3"
        " The bell rings. Time for your final class of the day. "
        " You got out of the cafeteria and walked to your culinary arts classroom. "
        pause 2.0
        jump cookingclasswed
label wedrooftop5wed:
    # quinn and yinhui
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked to the rooftop and found two of your classmates talking with eachother. "
    " Curious as to what they're talking about, you decided to walk over to them. "
    show quinnangry at right with easeinright
    show yinhuineutral at left with easeinleft
    if quinnknow == True and yinhuiknow == True:
        q " It's just been really hard controlling my club members, you know? "
        yi " It's okay, I know how it's like. "
        yi " It's basically like handling a bunch of rabid dogs. "
        q " Mhm...I mean, I know they want breaks, but like.. "
        q " Sometimes they take their breaks a little too far. "
        q " One time I let them have a break and then they REFUSED to cooperate with me. "
        q " Like, helloo? we have a play to work on! "
        q " Can't just have anyone slacking off. "
        yi " Uuh huh... It's gonna be alright, Quinn. "
        yi " Just say something that'll make them work. "
        q " And how am I supposed to do that, oh great Yinhui? "
        yi " ...You don't have to call me that, really. "
        " Looks like they're too busy in their conversation to even notice you... "
        " Not like you minded. "
        " You like being a listener sometimes. "
        yi " But, maybe tell them something like... "
        yi " 'If you don't do this, then I'll have to kick you out.' "
        yi " 'If you don't do that, then I'm going to tell that one hacker to give you the lowest grades possible.' "
        yi " I'm pretty sure they know of the rumor of there being a hacker, right? "
        yi " If they think all of that is terrifying, then they should believe you. "
        q " Oh really? and what if they don't believe me? "
        q " What am I supposed to do then? "
        yi " Well... "
        yi " Just simply say that they're going to go on stage without rehearsing everything. "
        yi " They won't know what to do, and therefore they're going to fumble. "
        yi " That way they can just embarrass themselves on stage and feel like they're disappointments. "
        hide quinnangry at bottom
        show quinnneutral at right
        q " ...Hm. "
        q " As much as I want everything to be perfect... "
        q " That doesn't really sound like a bad idea. "
        q " Thank you, Yinhui. "
        yi " You're welcome, Quinn. "
        scene black with dissolve
        " You spent the rest of the break listening to Yinhui and Quinn talk. "
        " They kinda noticed you there a little too late... "
        " Quinn was apologizing to you a whole lot for not noticing you. "
        " You kept telling him that it was alright, but he still felt a little guilty. "
        play sound "audio/bellring.mp3"
        " The bell rings. Time for your final class of the day. "
        " You got out of the rooftop and walked to your culinary arts classroom. "
        pause 2.0
        jump cookingclasswed
    elif quinnknow == True and yinhuiknow == False:
        q " It's just been really hard controlling my club members, you know? "
        x " It's okay, I know how it's like. "
        x " It's basically like handling a bunch of rabid dogs. "
        q " Mhm...I mean, I know they want breaks, but like.. "
        q " Sometimes they take their breaks a little too far. "
        q " One time I let them have a break and then they REFUSED to cooperate with me. "
        q " Like, helloo? we have a play to work on! "
        q " Can't just have anyone slacking off. "
        x " Uuh huh... It's gonna be alright, Quinn. "
        x " Just say something that'll make them work. "
        $ yinhuiknow = True
        q " And how am I supposed to do that, oh great Yinhui? "
        yi " ...You don't have to call me that, really. "
        " Looks like they're too busy in their conversation to even notice you... "
        " Not like you minded. "
        " You like being a listener sometimes. "
        yi " But, maybe tell them something like... "
        yi " 'If you don't do this, then I'll have to kick you out.' "
        yi " 'If you don't do that, then I'm going to tell that one hacker to give you the lowest grades possible.' "
        yi " I'm pretty sure they know of the rumor of there being a hacker, right? "
        yi " If they think all of that is terrifying, then they should believe you. "
        q " Oh really? and what if they don't believe me? "
        q " What am I supposed to do then? "
        yi " Well... "
        yi " Just simply say that they're going to go on stage without rehearsing everything. "
        yi " They won't know what to do, and therefore they're going to fumble. "
        yi " That way they can just embarrass themselves on stage and feel like they're disappointments. "
        hide quinnangry at bottom
        show quinnneutral at right
        q " ...Hm. "
        q " As much as I want everything to be perfect... "
        q " That doesn't really sound like a bad idea. "
        q " Thank you, Yinhui. "
        yi " You're welcome, Quinn. "
        scene black with dissolve
        " You spent the rest of the break listening to Yinhui and Quinn talk. "
        " They kinda noticed you there a little too late... "
        " Quinn was apologizing to you a whole lot for not noticing you. "
        " You kept telling him that it was alright, but he still felt a little guilty. "
        play sound "audio/bellring.mp3"
        " The bell rings. Time for your final class of the day. "
        " You got out of the rooftop and walked to your culinary arts classroom. "
        pause 2.0
        jump cookingclasswed
    elif quinnknow == False and yinhuiknow == True:
        x " It's just been really hard controlling my club members, you know? "
        yi " It's okay, I know how it's like. "
        yi " It's basically like handling a bunch of rabid dogs. "
        x " Mhm...I mean, I know they want breaks, but like.. "
        x " Sometimes they take their breaks a little too far. "
        x " One time I let them have a break and then they REFUSED to cooperate with me. "
        x " Like, helloo? we have a play to work on! "
        x " Can't just have anyone slacking off. "
        $ quinnknow = True
        yi " Uuh huh... It's gonna be alright, Quinn. "
        yi " Just say something that'll make them work. "
        q " And how am I supposed to do that, oh great Yinhui? "
        yi " ...You don't have to call me that, really. "
        " Looks like they're too busy in their conversation to even notice you... "
        " Not like you minded. "
        " You like being a listener sometimes. "
        yi " But, maybe tell them something like... "
        yi " 'If you don't do this, then I'll have to kick you out.' "
        yi " 'If you don't do that, then I'm going to tell that one hacker to give you the lowest grades possible.' "
        yi " I'm pretty sure they know of the rumor of there being a hacker, right? "
        yi " If they think all of that is terrifying, then they should believe you. "
        q " Oh really? and what if they don't believe me? "
        q " What am I supposed to do then? "
        yi " Well... "
        yi " Just simply say that they're going to go on stage without rehearsing everything. "
        yi " They won't know what to do, and therefore they're going to fumble. "
        yi " That way they can just embarrass themselves on stage and feel like they're disappointments. "
        hide quinnangry at bottom
        show quinnneutral at right
        q " ...Hm. "
        q " As much as I want everything to be perfect... "
        q " That doesn't really sound like a bad idea. "
        q " Thank you, Yinhui. "
        yi " You're welcome, Quinn. "
        scene black with dissolve
        " You spent the rest of the break listening to Yinhui and Quinn talk. "
        " They kinda noticed you there a little too late... "
        " Quinn was apologizing to you a whole lot for not noticing you. "
        " You kept telling him that it was alright, but he still felt a little guilty. "
        play sound "audio/bellring.mp3"
        " The bell rings. Time for your final class of the day. "
        " You got out of the rooftop and walked to your culinary arts classroom. "
        pause 2.0
        jump cookingclasswed
    else:
        x " It's just been really hard controlling my club members, you know? "
        x " It's okay, I know how it's like. "
        x " It's basically like handling a bunch of rabid dogs. "
        x " Mhm...I mean, I know they want breaks, but like.. "
        x " Sometimes they take their breaks a little too far. "
        x " One time I let them have a break and then they REFUSED to cooperate with me. "
        x " Like, helloo? we have a play to work on! "
        x " Can't just have anyone slacking off. "
        $ quinnknow = True
        x " Uuh huh... It's gonna be alright, Quinn. "
        x " Just say something that'll make them work. "
        $ yinhuiknow = True
        q " And how am I supposed to do that, oh great Yinhui? "
        yi " ...You don't have to call me that, really. "
        " Looks like they're too busy in their conversation to even notice you... "
        " Not like you minded. "
        " You like being a listener sometimes. "
        yi " But, maybe tell them something like... "
        yi " 'If you don't do this, then I'll have to kick you out.' "
        yi " 'If you don't do that, then I'm going to tell that one hacker to give you the lowest grades possible.' "
        yi " I'm pretty sure they know of the rumor of there being a hacker, right? "
        yi " If they think all of that is terrifying, then they should believe you. "
        q " Oh really? and what if they don't believe me? "
        q " What am I supposed to do then? "
        yi " Well... "
        yi " Just simply say that they're going to go on stage without rehearsing everything. "
        yi " They won't know what to do, and therefore they're going to fumble. "
        yi " That way they can just embarrass themselves on stage and feel like they're disappointments. "
        hide quinnangry at bottom
        show quinnneutral at right
        q " ...Hm. "
        q " As much as I want everything to be perfect... "
        q " That doesn't really sound like a bad idea. "
        q " Thank you, Yinhui. "
        yi " You're welcome, Quinn. "
        scene black with dissolve
        " You spent the rest of the break listening to Yinhui and Quinn talk. "
        " They kinda noticed you there a little too late... "
        " Quinn was apologizing to you a whole lot for not noticing you. "
        " You kept telling him that it was alright, but he still felt a little guilty. "
        play sound "audio/bellring.mp3"
        " The bell rings. Time for your final class of the day. "
        " You got out of the rooftop and walked to your culinary arts classroom. "
        pause 2.0
        jump cookingclasswed
label wedlibrary5wed:
    # spark and yangyi
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked to the library and spotted two of your classmates hanging out with eachother. "
    " You decided to go up to them and have a conversation with them. "
    show sparkneutral at left with easeinright
    show yangyineutral at right with easeinright
    if sparkknow == True and yangyiknow == True:
        hide yangyineutral at bottom
        show yangyisurprised at right
        ya " Woah, is that really true, Spark? "
        sp " Mhm, it is. "
        hide yangyisurprised at bottom
        show yangyineutral at right
        " You greeted them and then asked them what they were talking about. "
        sp " Oh, hey there [name]. "
        ya " Hiya! "
        sp " I was just talking to Yangyi over here about my past. "
        sp " You wanna hear it too? "
        menu:
            " My ears are all open ":
                $ sparklv += 10
                $ yangyilv += 5
                sp " Alright, listen up. "
                sp " Back then, I used to fight in a tournament. "
                ya " Super cool, right [name]? "
                sp " Mhm...this tournament was called Winter's Thread tournament. "
                sp " It was a fighting tournament, you'd fight other people to advance to the next round. "
                sp " Survive a round, and you'd go to the next round, duh. "
                sp " You're going to fight a randomly selected person each round, and trust me... "
                sp " The people from that tournament were no normal people. "
                sp " There was a guy who was half fish, half human... A girl with snow powers... "
                sp " A ghost girl with fire powers, a literal zombie... "
                sp " All sorts of people, really. "
                hide yangyineutral at bottom
                show yangyisurprised at right
                ya " Geez...! I'm sure it was hard to fight, considering you had no powers... "
                ya " How'd you get through? "
                sp " I didn't win the tournament or anything, but I ended up surviving until round 4. "
                sp " I wasn't actually expecting to make it that far... "
                hide sparkneutral at bottom
                show sparkhappy at left
                sp " It was fun though. Real fun. I got to bond with the contestants there. "
                sp " That's also where I met Temero. "
                sp " I used to think she was insane back then - considering that she acted like an insane scientist. "
                sp " But, we teamed up and I got used to her prescence. "
                sp " She managed to live longer than me, actually. "
                hide yangyisurprised at bottom
                show yangyineutral at right
                ya " That's interesting... "
                hide sparkhappy at bottom
                show sparkneutral at left
                sp " Oh, and uh... "
                sp " Apparently something wrong happened at the final round. "
                sp " Can't exactly remember anything, but there was this huge boss fight. "
                sp " We won, if I remember correctly. "
                sp " After all, if we lost, I wouldn't be here or anything. "
                ya " We're glad you lived, then! "
                scene black with dissolve
                " You spent the rest of the break hanging out with Yangyi and Spark. "
                " Spark's backstory was pretty interesting, in your opinion... "
                " Wonder what that whole boss fight was. "
                " A story for another day, you guess. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You got out of the library and made your way to the culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
            " I have other places to be ":
                sp " Really? Just passing by, then? "
                sp " Alright, I won't force you to listen to my story. "
                ya " Have fun in whereever you're going! "
                ya " We'll be right here if you need us! "
                scene black with dissolve
                " You spent the rest of the break wandering around the school. "
                " You didn't really see anything interesting happen as you were wandering around... "
                " Now you were kinda wondering what Spark's backstory was. "
                " Too late to ask him that, I guess? "
                " You could always just press the back button if you wanted though. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You made your way to the culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
    elif sparkknow == True and yangyiknow == False:
        hide yangyineutral at bottom
        show yangyisurprised at right
        x " Woah, is that really true, Spark? "
        sp " Mhm, it is. "
        hide yangyisurprised at bottom
        show yangyineutral at right
        " You greeted them and then asked them what they were talking about. "
        sp " Oh, hey there [name]. "
        x " Hiya! "
        $ yangyiknow = True
        sp " I was just talking to Yangyi over here about my past. "
        sp " You wanna hear it too? "
        menu:
            " My ears are all open ":
                $ sparklv += 10
                $ yangyilv += 5
                sp " Alright, listen up. "
                sp " Back then, I used to fight in a tournament. "
                ya " Super cool, right [name]? "
                sp " Mhm...this tournament was called Winter's Thread tournament. "
                sp " It was a fighting tournament, you'd fight other people to advance to the next round. "
                sp " Survive a round, and you'd go to the next round, duh. "
                sp " You're going to fight a randomly selected person each round, and trust me... "
                sp " The people from that tournament were no normal people. "
                sp " There was a guy who was half fish, half human... A girl with snow powers... "
                sp " A ghost girl with fire powers, a literal zombie... "
                sp " All sorts of people, really. "
                hide yangyineutral at bottom
                show yangyisurprised at right
                ya " Geez...! I'm sure it was hard to fight, considering you had no powers... "
                ya " How'd you get through? "
                sp " I didn't win the tournament or anything, but I ended up surviving until round 4. "
                sp " I wasn't actually expecting to make it that far... "
                hide sparkneutral at bottom
                show sparkhappy at left
                sp " It was fun though. Real fun. I got to bond with the contestants there. "
                sp " That's also where I met Temero. "
                sp " I used to think she was insane back then - considering that she acted like an insane scientist. "
                sp " But, we teamed up and I got used to her prescence. "
                sp " She managed to live longer than me, actually. "
                hide yangyisurprised at bottom
                show yangyineutral at right
                ya " That's interesting... "
                hide sparkhappy at bottom
                show sparkneutral at left
                sp " Oh, and uh... "
                sp " Apparently something wrong happened at the final round. "
                sp " Can't exactly remember anything, but there was this huge boss fight. "
                sp " We won, if I remember correctly. "
                sp " After all, if we lost, I wouldn't be here or anything. "
                ya " We're glad you lived, then! "
                scene black with dissolve
                " You spent the rest of the break hanging out with Yangyi and Spark. "
                " Spark's backstory was pretty interesting, in your opinion... "
                " Wonder what that whole boss fight was. "
                " A story for another day, you guess. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You got out of the library and made your way to the culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
            " I have other places to be ":
                sp " Really? Just passing by, then? "
                sp " Alright, I won't force you to listen to my story. "
                ya " Have fun in whereever you're going! "
                ya " We'll be right here if you need us! "
                scene black with dissolve
                " You spent the rest of the break wandering around the school. "
                " You didn't really see anything interesting happen as you were wandering around... "
                " Now you were kinda wondering what Spark's backstory was. "
                " Too late to ask him that, I guess? "
                " You could always just press the back button if you wanted though. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You made your way to the culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
    elif sparkknow == False and yangyiknow == True:
        hide yangyineutral at bottom
        show yangyisurprised at right
        $ sparkknow = True
        ya " Woah, is that really true, Spark? "
        sp " Mhm, it is. "
        hide yangyisurprised at bottom
        show yangyineutral at right
        " You greeted them and then asked them what they were talking about. "
        sp " Oh, hey there [name]. "
        ya " Hiya! "
        sp " I was just talking to Yangyi over here about my past. "
        sp " You wanna hear it too? "
        menu:
            " My ears are all open ":
                $ sparklv += 10
                $ yangyilv += 5
                sp " Alright, listen up. "
                sp " Back then, I used to fight in a tournament. "
                ya " Super cool, right [name]? "
                sp " Mhm...this tournament was called Winter's Thread tournament. "
                sp " It was a fighting tournament, you'd fight other people to advance to the next round. "
                sp " Survive a round, and you'd go to the next round, duh. "
                sp " You're going to fight a randomly selected person each round, and trust me... "
                sp " The people from that tournament were no normal people. "
                sp " There was a guy who was half fish, half human... A girl with snow powers... "
                sp " A ghost girl with fire powers, a literal zombie... "
                sp " All sorts of people, really. "
                hide yangyineutral at bottom
                show yangyisurprised at right
                ya " Geez...! I'm sure it was hard to fight, considering you had no powers... "
                ya " How'd you get through? "
                sp " I didn't win the tournament or anything, but I ended up surviving until round 4. "
                sp " I wasn't actually expecting to make it that far... "
                hide sparkneutral at bottom
                show sparkhappy at left
                sp " It was fun though. Real fun. I got to bond with the contestants there. "
                sp " That's also where I met Temero. "
                sp " I used to think she was insane back then - considering that she acted like an insane scientist. "
                sp " But, we teamed up and I got used to her prescence. "
                sp " She managed to live longer than me, actually. "
                hide yangyisurprised at bottom
                show yangyineutral at right
                ya " That's interesting... "
                hide sparkhappy at bottom
                show sparkneutral at left
                sp " Oh, and uh... "
                sp " Apparently something wrong happened at the final round. "
                sp " Can't exactly remember anything, but there was this huge boss fight. "
                sp " We won, if I remember correctly. "
                sp " After all, if we lost, I wouldn't be here or anything. "
                ya " We're glad you lived, then! "
                scene black with dissolve
                " You spent the rest of the break hanging out with Yangyi and Spark. "
                " Spark's backstory was pretty interesting, in your opinion... "
                " Wonder what that whole boss fight was. "
                " A story for another day, you guess. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You got out of the library and made your way to the culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
            " I have other places to be ":
                sp " Really? Just passing by, then? "
                sp " Alright, I won't force you to listen to my story. "
                ya " Have fun in whereever you're going! "
                ya " We'll be right here if you need us! "
                scene black with dissolve
                " You spent the rest of the break wandering around the school. "
                " You didn't really see anything interesting happen as you were wandering around... "
                " Now you were kinda wondering what Spark's backstory was. "
                " Too late to ask him that, I guess? "
                " You could always just press the back button if you wanted though. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You made your way to the culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
    else:
        hide yangyineutral at bottom
        show yangyisurprised at right
        $ sparkknow = True
        x " Woah, is that really true, Spark? "
        sp " Mhm, it is. "
        hide yangyisurprised at bottom
        show yangyineutral at right
        " You greeted them and then asked them what they were talking about. "
        sp " Oh, hey there [name]. "
        x " Hiya! "
        $ yangyiknow = True
        sp " I was just talking to Yangyi over here about my past. "
        sp " You wanna hear it too? "
        menu:
            " My ears are all open ":
                $ sparklv += 10
                $ yangyilv += 5
                sp " Alright, listen up. "
                sp " Back then, I used to fight in a tournament. "
                ya " Super cool, right [name]? "
                sp " Mhm...this tournament was called Winter's Thread tournament. "
                sp " It was a fighting tournament, you'd fight other people to advance to the next round. "
                sp " Survive a round, and you'd go to the next round, duh. "
                sp " You're going to fight a randomly selected person each round, and trust me... "
                sp " The people from that tournament were no normal people. "
                sp " There was a guy who was half fish, half human... A girl with snow powers... "
                sp " A ghost girl with fire powers, a literal zombie... "
                sp " All sorts of people, really. "
                hide yangyineutral at bottom
                show yangyisurprised at right
                ya " Geez...! I'm sure it was hard to fight, considering you had no powers... "
                ya " How'd you get through? "
                sp " I didn't win the tournament or anything, but I ended up surviving until round 4. "
                sp " I wasn't actually expecting to make it that far... "
                hide sparkneutral at bottom
                show sparkhappy at left
                sp " It was fun though. Real fun. I got to bond with the contestants there. "
                sp " That's also where I met Temero. "
                sp " I used to think she was insane back then - considering that she acted like an insane scientist. "
                sp " But, we teamed up and I got used to her prescence. "
                sp " She managed to live longer than me, actually. "
                hide yangyisurprised at bottom
                show yangyineutral at right
                ya " That's interesting... "
                hide sparkhappy at bottom
                show sparkneutral at left
                sp " Oh, and uh... "
                sp " Apparently something wrong happened at the final round. "
                sp " Can't exactly remember anything, but there was this huge boss fight. "
                sp " We won, if I remember correctly. "
                sp " After all, if we lost, I wouldn't be here or anything. "
                ya " We're glad you lived, then! "
                scene black with dissolve
                " You spent the rest of the break hanging out with Yangyi and Spark. "
                " Spark's backstory was pretty interesting, in your opinion... "
                " Wonder what that whole boss fight was. "
                " A story for another day, you guess. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You got out of the library and made your way to the culinary arts classroom. "
                pause 2.0
                jump cookingclasswed
            " I have other places to be ":
                sp " Really? Just passing by, then? "
                sp " Alright, I won't force you to listen to my story. "
                ya " Have fun in whereever you're going! "
                ya " We'll be right here if you need us! "
                scene black with dissolve
                " You spent the rest of the break wandering around the school. "
                " You didn't really see anything interesting happen as you were wandering around... "
                " Now you were kinda wondering what Spark's backstory was. "
                " Too late to ask him that, I guess? "
                " You could always just press the back button if you wanted though. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You made your way to the culinary arts classroom. "
                pause 2.0
                jump cookingclasswed

label cookingclasswed:
    scene classroom with dissolve
    " You walked into the classroom and waited for the cooking teacher to arrive. "
    " After a few minutes, she walks into the classroom. "
    show jiayuhappy at center with easeinright
    msx " Good day, class. "
    msx " Please get notebook and pen ready. "
    msx " We're going to be.. "
    msx " ...Note taking, today. "
    " Pretty sure she meant taking down notes, but alright. "
    " You get out your notebook, and you get your pen. "
    msx " Before we start the lesson, I am going to remind you all. "
    msx " Remind you all about activity tomorrow. "
    msx " Please prepare for that tomorrow. "
    msx " I do NOT want to deal with complaining in the activity. "
    msx " Just because one of you forgot to bring the materials. "
    msx " Okay? okay. "
    msx " We shall start the lesson. "
    scene black with dissolve
    " You spent the rest of class hours taking down notes. "
    " As per usual, nothing interesting happens and you're just waiting for the bell to ring. "
    " It feels as if hours had passed, and then eventually... "
    play sound "audio/bellring.mp3"
    " The bell rings, finally announcing that class is over. "
    " You get your things, and then prepared yourself to go home. "
    pause 2.0
    jump wedochome

label wedochome:
    scene paperschoolfront with dissolve
    " You looked around you and found all of your classmates going home. "
    " Seeing all of them goof off, seeing all of them talk to eachother normally. "
    " Or others just being alone, like you. "
    " Not that you minded being alone - you're about to go home, after all. "
    " You take one last look at your school before you started heading off. "
    scene black with dissolve
    stop music fadeout 1.5
    pause 2.0
    play music "audio/home.mp3" fadein 1.5
    scene mcroom with dissolve
    " You eventually arrived home, and put your things down. "
    " You changed into your bedwear outfit, and sat on your bed checking the school GC on your phone. "
    " There was mostly nothing new, no announcements from Mister Clio or anything. "
    " You checked the goofy classroom GC and found all of your classmates goofing off, per usual. "
    " There was also a pinned message about everything important that was going to happen, like activities. "
    " Pretty useful. There was not much other than the physics and cooking activity being tomorrow. "
    " And also the PE activity being on friday. "
    " You eventually closed your phone and left it to charge overnight, "
    " Then you laid yourself on your bed, tucking yourself in. "
    " Not long after, you started falling asleep. "
    scene black with dissolve
    " Good night, [name]. "
    stop music fadeout 1.5
    pause 2.0
    x " Hold on right there, you're not sleeping just yet! "
    show acemysterious at center with dissolve
    x " Well, technically you ARE sleeping. "
    x " I'm just contacting you in your dreaaamsss!! "
    x " Isn't that cool, huh? "
    x " Now you're probably wondering... "
    x " 'Who is this voice talking to me? Am I going insane?' "
    x " Well, probably - you are! "
    x " But let me stop dillydallying and I'll give you a PROPER introduction. "
    hide acemysterious at bottom with dissolve
    show aceneutral at center with dissolve
    msac " I'mmmmm MISTER ACE! "
    msac " I'm sure you've heard of me before, no? "
    msac " If you havent, I'll give you a quick recall! "
    hide aceneutral at bottom
    show acehappy at center
    msac " I'm that sweet, sweet ghost that's been wandering around the school! "
    msac " Specifically a ghost of the teacher. "
    msac " You know, I was KILLED for just wanting to know about the truth... "
    msac " The truth of WHY some of the teachers here KILL harmless children for failing classes. "
    msac " Surely you knew about the whole killing thing. If you dont, oh well! "
    hide acehappy at bottom
    show aceneutral at center
    msac " Gambled for my life to actually get the answers that I wanted. "
    msac " Guess how that went. "
    msac " ANYWAYYY!! Oh Ace, if you're stuck in the school - then how come you're in my dreams? "
    msac " Cool ghost powers I have, dummy. "
    msac " I get to go to random people's dreams whenever I want! "
    msac " Well...as long as they're in the school. "
    hide aceneutral at bottom
    show aceangry at center
    msac " It's not really that helpful, really. "
    msac " I have to wait until it's night just to mess with you guys... "
    hide aceangry at bottom
    show aceneutral at center
    msac " ANYWAY! If you're wondering why I chose you... "
    msac " You're INTERESTING. "
    msac " For a fact, you weren't even supposed to pop up in this universe. "
    msac " You just randomly existed one day with a fake backstory and everything. "
    msac " Aaaaall for a game where you could befriend everyone! "
    msac " That's why I think you're very, very interesting. "
    msac " And how do I know this? Python told me about you, the day you came! "
    if pythonknow == True:
        msac " Don't tell me you haven't met them yet. "
        msac " I know you have. "
    else:
        msac " Don't know who Python is? boohoo. "
    msac " Anywho...let's get to the real business. "
    msac " We'll be playing a game here! A game of questions. "
    msac " I'll give you a riddle and I'll give you 10 seconds to answer it. "
    msac " If you get the right answer, you live! But if you get the wrong answer...you die! "
    msac " If you're also too slow to answer...you die too! "
    msac " Simple to understand, really. "
    msac " Though since Python won't let me kill you for real, you'll get revived everytime you get a wrong answer. "
    msac " Let's begin now! "
    jump retryace
label retryace:
    msac " Your first riddle! Listen well! "
    msac " I exist before your eyes open, "
    msac " Yet I vanish when you stop running. "
    msac " I hold your instructions, "
    msac " But do I truly live, or only when called? "
    msac " Start now! "
    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'tooslowace'
    show screen countdown
    menu:
        " A process in memory ":
            hide screen countdown
            msac " Ooh, you actually got that one right, bravo! "
            msac " Our fun isn't over yet though. "
            msac " Let's move onto our second question, shall we? "
            msac " I am written, yet never read. "
            msac " I am compiled, yet never seen. "
            msac " Without me, you are undefined, "
            msac " But if you find me, do you truly know what I mean? "
            show screen countdown
            menu:
                " A user manual ":
                    hide screen countdown
                    msac " Uh oh, sorry dear! "
                    msac " You chose the WRONG option. "
                    hide aceneutral at bottom
                    show acemurder at center
                    msac " That means good bye for you! "
                    scene black
                    pause 1.5
                    jump retryace
                " A forgotten love letter ":
                    hide screen countdown
                    msac " Uh oh, sorry dear! "
                    msac " You chose the WRONG option. "
                    hide aceneutral at bottom
                    show acemurder at center
                    msac " That means good bye for you! "
                    scene black
                    pause 1.5
                    jump retryace
                " Machine code ":
                    hide screen countdown
                    msac " Wow, either you guessed that or you didn't! "
                    msac " Let's move onto our third question. "
                    msac " You're doing surprisingly well... "
                    msac " I am neither 1 or 0, "
                    msac " Yet I decide both. "
                    msac " Without me, logic is blind, "
                    msac " And every path leads nowhere. "
                    show screen countdown
                    menu:
                        " The conditional operator (if) ":
                            hide screen countdown
                            msac " Hmm...good job! "
                            msac " I'm just waiting here until you get the wrong answer so that I can kill you. "
                            msac " Looks like that's not happening anytime soon, unfortunately. "
                            msac " Annoying...let's get to our fourth question. "
                            msac " You think you are free because you choose, "
                            msac " But your choices are inside me. "
                            msac " I do not run, yet you cannot escape me. "
                            msac " What am I? "
                            show screen countdown
                            menu:
                                " A digital sandbox ":
                                    hide screen countdown
                                    msac " Uh oh, sorry dear! "
                                    msac " You chose the WRONG option. "
                                    hide aceneutral at bottom
                                    show acemurder at center
                                    msac " That means good bye for you! "
                                    scene black
                                    pause 1.5
                                    jump retryace
                                " The programs architecture ":
                                    hide screen countdown
                                    msac " Wow, you're not stupid after all! "
                                    msac " Either that, or you're just guessing. "
                                    msac " Final question, here we go! "
                                    msac " Your reality feels real, "
                                    msac " But when you crash, who catches you? "
                                    msac " If I return null, do you cease to exist, "
                                    msac " Or do you throw an exception to persist? "
                                    show screen countdown
                                    menu:
                                        " The runtime environment ":
                                            hide screen countdown
                                            msac " Wow, you actually got all of my questions correct! "
                                            msac " Quite impressive, really. "
                                            msac " I'll leave you alone...for now. "
                                            msac " See you some other time! "
                                            hide aceneutral at bottom with easeoutbottom
                                            " ...What an odd dream. "
                                            pause 2.0
                                            play music "audio/home.mp3" fadein 1.5
                                            jump octhursday
                                        " The garbage collector ":
                                            hide screen countdown
                                            msac " Uh oh, sorry dear! "
                                            msac " You chose the WRONG option. "
                                            hide aceneutral at bottom
                                            show acemurder at center
                                            msac " That means good bye for you! "
                                            scene black
                                            pause 1.5
                                            jump retryace
                                        " The human brain ":
                                            hide screen countdown
                                            msac " Uh oh, sorry dear! "
                                            msac " You chose the WRONG option. "
                                            hide aceneutral at bottom
                                            show acemurder at center
                                            msac " That means good bye for you! "
                                            scene black
                                            pause 1.5
                                            jump retryace
                                " Free will ":
                                    hide screen countdown
                                    msac " Uh oh, sorry dear! "
                                    msac " You chose the WRONG option. "
                                    hide aceneutral at bottom
                                    show acemurder at center
                                    msac " That means good bye for you! "
                                    scene black
                                    pause 1.5
                                    jump retryace
                        " A corrupted file ":
                            hide screen countdown
                            msac " Uh oh, sorry dear! "
                            msac " You chose the WRONG option. "
                            hide aceneutral at bottom
                            show acemurder at center
                            msac " That means good bye for you! "
                            scene black
                            pause 1.5
                            jump retryace
                        " A switch on the wall ":
                            hide screen countdown
                            msac " Uh oh, sorry dear! "
                            msac " You chose the WRONG option. "
                            hide aceneutral at bottom
                            show acemurder at center
                            msac " That means good bye for you! "
                            scene black
                            pause 1.5
                            jump retryace
        " A static variable in a book ":
            hide screen countdown
            msac " Uh oh, sorry dear! "
            msac " You chose the WRONG option. "
            hide aceneutral at bottom
            show acemurder at center
            msac " That means good bye for you! "
            scene black
            pause 1.5
            jump retryace
        " A line of poetry ":
            hide screen countdown
            msac " Uh oh, sorry dear! "
            msac " You chose the WRONG option. "
            hide aceneutral at bottom
            show acemurder at center
            msac " That means good bye for you! "
            scene black
            pause 1.5
            jump retryace
    label tooslowace:
        msac " Uh oh, sorry dear! "
        msac " You're TOO SLOW. "
        hide aceneutral at bottom
        show acemurder at center
        msac " That means good bye for you! "
        scene black
        pause 1.5
        jump retryace
    # reminder for mister ace
