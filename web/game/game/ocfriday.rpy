label ocfriday:
    show text " DAY 5 - FRIDAY "
    pause 1.5
    play music "audio/home.mp3" fadein 1.5
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
    pause 1.0
    scene black with dissolve
    pause 1.0
    scene classroom with dissolve
    jump ochistoryfri

label ochistoryfri:
    show mrclioneutral at center with easeinleft
    mscl " Good morning, class. "
    mscl " Let's not waste any time now. "
    mscl " Let's go on with our lesson for the day. "
    mscl " Remember, no phones, no sleeping... "
    mscl " (Well, except for Nox.) "
    mscl " Just pay attention to class. "
    mscl " With that out of the way... "
    mscl " Let's begin. "
    scene black with dissolve
    " You spent the rest of the class writing down notes for the lesson. "
    " Nothing too special happened while you were in class though... "
    " You were just waiting for the bell to ring. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for a break. "
    " You waited for everybody to get out of the classroom before you did. "
    pause 2.0
    jump ocfribreak1

label ocfribreak1:
    scene hallway with dissolve
    " It's breaktime, and you're thinking of going somewhere in the school. "
    " Where do you want to go? "
    menu:
        " {image=jacobicon} The front of the school {image=sparkicon} ":
            jump ocfrifront1
        " {image=diskicon} The back of the school {image=koaicon} ":
            jump ocfriback1
        " {image=carmenicon} The gym {image=quinnicon} ":
            jump ocfrigym1
        " {image=matteicon} The cafeteria {image=orchidicon} ":
            jump ocfricafeteria1
        " {image=noxicon} The rooftop {image=jamicon} ":
            jump ocfrirooftop1
        " {image=temeroicon} The library {image=yinyangicon} ":
            jump ocfrilibrary1
    label ocfrifront1:
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked to the front of the school and found two of your classmates doing their own things. "
        " Who would you like to talk to? "
        if jacobknow == True and sparkknow == True:
            menu:
                " {image=jacobicon} Jacob {image=jacobicon} ":
                    jump mythologyyay
                " {image=sparkicon} Spark {image=sparkicon} ":
                    jump anthropologyyay
        elif jacobknow == True and sparkknow == False:
            menu:
                " {image=jacobicon} Jacob {image=jacobicon} ":
                    jump mythologyyay
                " {image=sparkicon} A guy with antennas and a tail {image=sparkicon} ":
                    jump anthropologyyay
        elif jacobknow == False and sparkknow == True:
            menu:
                " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                    jump mythologyyay
                " {image=sparkicon} Spark {image=sparkicon} ":
                    jump anthropologyyay
        else:
            menu:
                " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                    jump mythologyyay
                " {image=sparkicon} A guy with antennas and a tail {image=sparkicon} ":
                    jump anthropologyyay
        label mythologyyay:
            show jacobneutral at center with easeinright
            if jacobknow == True:
                " You walked over to him and politely asked him what he was doing. "
                " Looked like he was looking at something on his phone... "
                jac " Huh? oh, you. "
                jac " Just, um... "
                jac " I'm not really into all that nerdy stuff, but this one's just a change of things. "
                jac " You know about the solar eclipse happening soon? "
                " You shook your head as a response. "
                " You didn't know that there was going to be a solar eclipse... "
                " Maybe you should watch if you had the free time. "
                jac " Well it's happening this sunday. "
                jac " I was honestly thinking about taking someone to watch, but... "
                jac " Eeeh, I don't know. "
                jac " I'm not too good at socializing. "
                jac " Besides... "
                jac " Most people kind of avoid me for my attitude. "
                jac " Some people say that I'm pretty...I don't know... "
                jac " There's a lot of things people have called me in the past. "
                jac " They called me rude... "
                jac " A freak...a whole lot of things. "
                jac " Just look at the list of stereotypical bullying nicknames or something and you'd get everything I was called in there. "
                jac " That was way before I got into this school, but... "
                jac " Can't help but think that people in here would call me those things again, you know? "
                jac " That's why I don't really get too close with the people here. "
                jac " You don't know when they can just stab you in the back. "
                jac " I know I should still make friends, but... "
                jac " Ergh, what am I talking about. "
                jac " But uh...yeah, solar eclipse. "
                jac " Kind of still wishing that I would get someone to hang out with there, but uh... "
                jac " I also don't mind being alone at all. "
                jac " So...uh...yeah. "
                if jacoblv >= 20 or jacoblv == 20:
                    menu:
                        " I would like to see the solar eclipse with you!! ":
                            $ jacoblv += 10
                            hide jacobneutral at bottom
                            show jacobsurprised at center
                            jac " ...Oh, what? "
                            jac " You're not joshing me right now? "
                            jac " You serious? "
                            hide jacobsurprised at bottom
                            show jacobneutral at center
                            jac " Um...okay. "
                            jac " If you really want to, then... "
                            jac " I can't really stop you. "
                            jac " Just a quick thing though... "
                            jac " I most likely don't know what to do. "
                            jac " You know... "
                            jac " You're kind of one of the only people who would want to do something with me. "
                            jac " So... "
                            jac " If there's something that you would like to do... "
                            jac " Don't be afraid of telling me, okay? "
                            jac " I'm not forcing you to just sit there and do whatever I say. "
                            jac " That would just be really weird, you know? "
                            jac " But uh... "
                            jac " Let's meet up at aboouut... "
                            jac " How about 30 minutes before the thing starts? "
                            jac " That can give you enough time to get ready, right. "
                            jac " If not, I'm going to get concerned. "
                            jac " But, uh... "
                            jac " Hope you have fun while you're there. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Jacob. "
                            " You never really have seen a solar eclipse before, so... "
                            " This was pretty exciting for you. "
                            " And for you to see it with Jacob? even better. "
                            " But that's just in your opinion. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked back into the school and went to your classroom. "
                            pause 2.0
                            jump ochealthfri
                        " Have fun seeing the solar eclipse dude ":
                            jac " ...Yeah. "
                            jac " I could just hang out in a spot while I'm there... "
                            jac " Just a spot where there's not too many people. "
                            jac " Don't really like interacting with randoms too much... "
                            jac " Probably would just spend the time gaming. "
                            jac " But I would look at the eclipse every now and then, of course. "
                            jac " With those special glasses... "
                            jac " Oh wait, that would mean people would have to... "
                            jac " ...Hm. "
                            jac " I'll figure something out. "
                            " Looks like he doesn't want people to see his eyes... "
                            " You wonder why. "
                            scene black with dissolve
                            " You spent the rest of the break talking to Jacob about the solar eclipse. "
                            " You're considering on going to the park to get a good view of it yourself... "
                            " You'd only check it out if you got the free time, though. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked back into the school and went to your classroom. "
                            pause 2.0
                            jump ochealthfri
                else:
                    " You wished him to have fun while watching. "
                    " You weren't really sure if you could go, so... "
                    " All you could do was just wish for him to have fun. "
                    jac " ...Yeah. "
                    jac " I could just hang out in a spot while I'm there... "
                    jac " Just a spot where there's not too many people. "
                    jac " Don't really like interacting with randoms too much... "
                    jac " Probably would just spend the time gaming. "
                    jac " But I would look at the eclipse every now and then, of course. "
                    jac " With those special glasses... "
                    jac " Oh wait, that would mean people would have to... "
                    jac " ...Hm. "
                    jac " I'll figure something out. "
                    " Looks like he doesn't want people to see his eyes... "
                    " You wonder why. "
                    scene black with dissolve
                    " You spent the rest of the break talking to Jacob about the solar eclipse. "
                    " You're considering on going to the park to get a good view of it yourself... "
                    " You'd only check it out if you got the free time, though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump ochealthfri
            else:
                " You walked over to him and politely asked him what he was doing. "
                " Looked like he was looking at something on his phone... "
                x " Huh? oh, you. "
                x " I don't believe we've met before, now that I think about it. "
                x " How about I introduce myself? "
                $ jacobknow = True
                jac " I'm Jacob. Your classmate. "
                jac " And I was, uh... "
                jac " Just, um... "
                jac " I'm not really into all that nerdy stuff, but this one's just a change of things. "
                jac " You know about the solar eclipse happening soon? "
                " You shook your head as a response. "
                " You didn't know that there was going to be a solar eclipse... "
                " Maybe you should watch if you had the free time. "
                jac " Well it's happening this sunday. "
                jac " I was honestly thinking about taking someone to watch, but... "
                jac " Eeeh, I don't know. "
                jac " I'm not too good at socializing. "
                jac " Besides... "
                jac " Most people kind of avoid me for my attitude. "
                jac " Some people say that I'm pretty...I don't know... "
                jac " There's a lot of things people have called me in the past. "
                jac " They called me rude... "
                jac " A freak...a whole lot of things. "
                jac " Just look at the list of stereotypical bullying nicknames or something and you'd get everything I was called in there. "
                jac " That was way before I got into this school, but... "
                jac " Can't help but think that people in here would call me those things again, you know? "
                jac " That's why I don't really get too close with the people here. "
                jac " You don't know when they can just stab you in the back. "
                jac " I know I should still make friends, but... "
                jac " Ergh, what am I talking about. "
                jac " But uh...yeah, solar eclipse. "
                jac " Kind of still wishing that I would get someone to hang out with there, but uh... "
                jac " I also don't mind being alone at all. "
                jac " So...uh...yeah. "
                " You wished him to have fun while watching. "
                " You weren't really sure if you could go, so... "
                " All you could do was just wish for him to have fun. "
                jac " ...Yeah. "
                jac " I could just hang out in a spot while I'm there... "
                jac " Just a spot where there's not too many people. "
                jac " Don't really like interacting with randoms too much... "
                jac " Probably would just spend the time gaming. "
                jac " But I would look at the eclipse every now and then, of course. "
                jac " With those special glasses... "
                jac " Oh wait, that would mean people would have to... "
                jac " ...Hm. "
                jac " I'll figure something out. "
                " Looks like he doesn't want people to see his eyes... "
                " You wonder why. "
                scene black with dissolve
                " You spent the rest of the break talking to Jacob about the solar eclipse. "
                " You're considering on going to the park to get a good view of it yourself... "
                " You'd only check it out if you got the free time, though. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump ochealthfri
        label anthropologyyay:
            show sparkneutral at center with easeinleft
            if sparkknow == True:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was thinking about something... "
                sp " Huh? "
                sp " Oh, it's just you... "
                sp " Sorry, I was just thinking about something. "
                sp " I kind of forgot my homework yesterday... "
                sp " And now I'm kind of panicking. "
                sp " It isn't really like me to forget something like this... "
                sp " Maybe I got too distracted hanging out with my friends? "
                sp " Probably the reason why. "
                sp " I should get to doing my homework though... "
                sp " Can't just stand here and do nothing. "
                sp " Um... "
                sp " If you need anything, I'll just be sitting on this bench over here. "
                sp " Just talk to me if you want to...you know, talk. "
                sp " Make sure that it's important though. "
                " You nodded and sat down next to him. "
                " You don't really know what to do while you're here with him like this... "
                " I mean, you can't really disturb him. "
                " He's busy doing his homework right now... "
                if sparkformseen == True:
                    " Wait... "
                    " He did say you could talk to him about anything important. "
                    " Maybe you could ask him about what you saw yesterday...? "
                    " Let's just hope that he actually responds tyo your question. "
                    " You poked his shoulder and asked him if you could ask him something. "
                    sp " Huh? "
                    sp " Oh, sure. "
                    sp " What's up? "
                    " You asked him if he wouldn't freak out first when you tell him this. "
                    " But you swore you saw him with this weird TV form yesterday... "
                    " EATING a student. "
                    " You don't know if your mind was playing with you, but... "
                    " It just felt so real to you. "
                    " You waited for him to have a response to that. "
                    hide sparkneutral at bottom
                    show sparksad at center
                    sp " Oh, geez...you saw that? "
                    sp " Um... "
                    sp " Okay, I don't think I can lie myself out of this one. "
                    sp " After all you've seen, all you deserve is the truth. "
                    sp " Okay... "
                    hide sparksad at bottom
                    show sparkneutral at center
                    sp " I don't know if you've hear about this - but I used to be in this tournament. "
                    sp " But before this tournament, I was struggling really hard. "
                    sp " The world is cruel out there, you know? "
                    sp " Can't really just live out there like everything's sunshine and rainbows. "
                    sp " Especially harder for me since I have no relatives. "
                    sp " I heard about the tournament being able to grant people's wishes, only if you won. "
                    sp " I wanted to join, but I had no expirience in fighting. "
                    sp " That was until I found my buddy, Scrap. "
                    sp " According to it...by it, I mean Scrap - it's this little...demon thing. "
                    sp " It could give me all the power I ever wanted. "
                    sp " The power to defend myself. The power to be strong. "
                    sp " But, there came a price to getting that power. "
                    sp " I would get all of the power... "
                    sp " In exchange for me eating other people. "
                    sp " Apparently, that would feed Scrap. "
                    sp " I would have to eat atleast two people for Scrap to be fed... "
                    sp " I got caught eating someone once in this school. "
                    sp " Mister Clio saw me, and... "
                    sp " Surprisingly, he saw some sort of potential in me. "
                    sp " And nooww... "
                    sp " I kind of work for the teachers. "
                    sp " Uh, hope that doesn't weird you out or anything. "
                    sp " ...I think I'll stop talking for now. "
                    " You reassured him that he was fine. "
                    " Besides, that backstory was pretty cool in your opinion. "
                    sp " Oh, uh...thanks? "
                    sp " (Don't really know how to feel about that...) "
                    " And then he goes back to doing his homework. "
                    " You then decide to play games on your phone for the rest of the break to waste time. "
                    scene black with dissolve
                    " You spent the rest of the break playing games on your phone. "
                    " Just random games that you had to waste time... "
                    " Oh hey, you got a new highest score for one of them. Sweet. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went into your classroom after a bit. "
                    pause 2.0
                    jump ochealthfri
                else:
                    " You decided not to bother him for now. "
                    " He seemed pretty concentrated, after all. "
                    " You just decided to play on your phone to pass the time... "
                    scene black with dissolve
                    " You spent the rest of the break playing games on your phone. "
                    " Just random games that you had to waste time... "
                    " Oh hey, you got a new highest score for one of them. Sweet. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went into your classroom after a bit. "
                    pause 2.0
                    jump ochealthfri
            else:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was thinking about something... "
                x " Huh? "
                x " Oh, it's just you... "
                x " Sorry, I was just thinking about something. "
                $ sparkknow = True
                sp " I'm Spark, and uh... "
                sp " I kind of forgot my homework yesterday... "
                sp " And now I'm kind of panicking. "
                sp " It isn't really like me to forget something like this... "
                sp " Maybe I got too distracted hanging out with my friends? "
                sp " Probably the reason why. "
                sp " I should get to doing my homework though... "
                sp " Can't just stand here and do nothing. "
                sp " Um... "
                sp " If you need anything, I'll just be sitting on this bench over here. "
                sp " Just talk to me if you want to...you know, talk. "
                sp " Make sure that it's important though. "
                " You nodded and sat down next to him. "
                " You don't really know what to do while you're here with him like this... "
                " I mean, you can't really disturb him. "
                " He's busy doing his homework right now... "
                " You decided not to bother him for now. "
                " He seemed pretty concentrated, after all. "
                " You just decided to play on your phone to pass the time... "
                scene black with dissolve
                " You spent the rest of the break playing games on your phone. "
                " Just random games that you had to waste time... "
                " Oh hey, you got a new highest score for one of them. Sweet. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went into your classroom after a bit. "
                pause 2.0
                jump ochealthfri
    label ocfriback1:
        # disk and koa
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked into the back of the school and saw two of your classmates talking to eachother. "
        " Wondering what they were talking about, you walked over to them. "
        show diskneutral at left with easeinright
        show koaneutral at right with easeinright
        if diskknow == True and koaknow == True:
            d " Hiya there [name]!! "
            k " ...Hi, [name]. "
            hide diskneutral at bottom
            show diskhappy at center
            d " I'm just so excited right now!! "
            d " Don't you know what day it is today?? "
            k " It's friday today. "
            k " But basically, [name]... "
            k " That means it's party day for Disk. "
            d " Yeah!! "
            d " You see...I always throw parties on friday! "
            d " It's to celebrate that we got through another week of school! "
            d " It does get tiring at times, but... "
            d " I love seeing everyone have fun and being happy! "
            d " It just shows how much I'm making other people enjoy themselves! "
            k " ...That's nice, Disk. "
            k " It's really sweet of you to want others to be happy. "
            k " But what about yourself? "
            hide diskhappy at bottom
            show diskneutral at center
            d " Huh??? "
            k " Don't you want to be happy, too? "
            k " You can make others happy, yes... "
            k " But don't forget to take care of yourself aswell. "
            k " In order to be happy, you must take care of yourself well. "
            k " You don't always have to take care of others. "
            d " Hehe, don't worry! "
            d " I already know that, Koa! "
            d " But thank you very much for reminding me!! "
            d " I don't think I'll get like that anytime soon, but... "
            d " It's good that you reminded me just incase if I ever got like that!! "
            d " Now that I think about it... "
            d " It would be really bad if I got like that, don't you think? "
            k " Mhm... "
            d " Always gotta remember to take care of yourself, hehe! "
            d " But anyways... "
            d " Party day!!! "
            k " Woo. "
            k " (Psst, [name]...) "
            k " (He's kind of always like this.) "
            k " (It's not a bad thing, buuut...) "
            k " (If you ever think that he's too much, just tell him.) "
            k " (Trust me, he wouldn't overreact too bad.) "
            scene black with dissolve
            " You spent the rest of the break talking with Koa and Disk. "
            " Just talking about random things... "
            " Mostly talking about Disk's party though. "
            " You're considering on joining... "
            " Or if you've already joined then uh...yeah good for you "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump ochealthfri
        elif diskknow == True and koaknow == False:
            d " Hiya there [name]!! "
            x " ...Hi, [name]. "
            x " Don't think we've met before, uh... "
            $ koaknow = True
            k " I'm Koa. "
            k " Disk, why don't you tell [them] why you're so excited? "
            hide diskneutral at bottom
            show diskhappy at center
            d " I'm just so excited right now!! "
            d " Don't you know what day it is today?? "
            k " It's friday today. "
            k " But basically, [name]... "
            k " That means it's party day for Disk. "
            d " Yeah!! "
            d " You see...I always throw parties on friday! "
            d " It's to celebrate that we got through another week of school! "
            d " It does get tiring at times, but... "
            d " I love seeing everyone have fun and being happy! "
            d " It just shows how much I'm making other people enjoy themselves! "
            k " ...That's nice, Disk. "
            k " It's really sweet of you to want others to be happy. "
            k " But what about yourself? "
            hide diskhappy at bottom
            show diskneutral at center
            d " Huh??? "
            k " Don't you want to be happy, too? "
            k " You can make others happy, yes... "
            k " But don't forget to take care of yourself aswell. "
            k " In order to be happy, you must take care of yourself well. "
            k " You don't always have to take care of others. "
            d " Hehe, don't worry! "
            d " I already know that, Koa! "
            d " But thank you very much for reminding me!! "
            d " I don't think I'll get like that anytime soon, but... "
            d " It's good that you reminded me just incase if I ever got like that!! "
            d " Now that I think about it... "
            d " It would be really bad if I got like that, don't you think? "
            k " Mhm... "
            d " Always gotta remember to take care of yourself, hehe! "
            d " But anyways... "
            d " Party day!!! "
            k " Woo. "
            k " (Psst, [name]...) "
            k " (He's kind of always like this.) "
            k " (It's not a bad thing, buuut...) "
            k " (If you ever think that he's too much, just tell him.) "
            k " (Trust me, he wouldn't overreact too bad.) "
            scene black with dissolve
            " You spent the rest of the break talking with Koa and Disk. "
            " Just talking about random things... "
            " Mostly talking about Disk's party though. "
            " You're considering on joining... "
            " Or if you've already joined then uh...yeah good for you "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump ochealthfri
        elif diskknow == False and koaknow == True:
            x " Hiya there [name]!! "
            k " ...Hi, [name]. "
            x " Don't think we've met before, so lemme give you an introduction! "
            $ diskknow = True
            d " I'm Disk! it's really nice to meet you! and... "
            hide diskneutral at bottom
            show diskhappy at center
            d " I'm just so excited right now!! "
            d " Don't you know what day it is today?? "
            k " It's friday today. "
            k " But basically, [name]... "
            k " That means it's party day for Disk. "
            d " Yeah!! "
            d " You see...I always throw parties on friday! "
            d " It's to celebrate that we got through another week of school! "
            d " It does get tiring at times, but... "
            d " I love seeing everyone have fun and being happy! "
            d " It just shows how much I'm making other people enjoy themselves! "
            k " ...That's nice, Disk. "
            k " It's really sweet of you to want others to be happy. "
            k " But what about yourself? "
            hide diskhappy at bottom
            show diskneutral at center
            d " Huh??? "
            k " Don't you want to be happy, too? "
            k " You can make others happy, yes... "
            k " But don't forget to take care of yourself aswell. "
            k " In order to be happy, you must take care of yourself well. "
            k " You don't always have to take care of others. "
            d " Hehe, don't worry! "
            d " I already know that, Koa! "
            d " But thank you very much for reminding me!! "
            d " I don't think I'll get like that anytime soon, but... "
            d " It's good that you reminded me just incase if I ever got like that!! "
            d " Now that I think about it... "
            d " It would be really bad if I got like that, don't you think? "
            k " Mhm... "
            d " Always gotta remember to take care of yourself, hehe! "
            d " But anyways... "
            d " Party day!!! "
            k " Woo. "
            k " (Psst, [name]...) "
            k " (He's kind of always like this.) "
            k " (It's not a bad thing, buuut...) "
            k " (If you ever think that he's too much, just tell him.) "
            k " (Trust me, he wouldn't overreact too bad.) "
            scene black with dissolve
            " You spent the rest of the break talking with Koa and Disk. "
            " Just talking about random things... "
            " Mostly talking about Disk's party though. "
            " You're considering on joining... "
            " Or if you've already joined then uh...yeah good for you "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump ochealthfri
        else:
            d " Hiya there [name]!! "
            x " ...Hi, [name]. "
            x " Don't think we've met before, uh... "
            $ koaknow = True
            k " I'm Koa. "
            x " Don't think we've met before either, so lemme give you an introduction! "
            $ diskknow = True
            d " I'm Disk! it's really nice to meet you! and... "
            hide diskneutral at bottom
            show diskhappy at center
            d " I'm just so excited right now!! "
            d " Don't you know what day it is today?? "
            k " It's friday today. "
            k " But basically, [name]... "
            k " That means it's party day for Disk. "
            d " Yeah!! "
            d " You see...I always throw parties on friday! "
            d " It's to celebrate that we got through another week of school! "
            d " It does get tiring at times, but... "
            d " I love seeing everyone have fun and being happy! "
            d " It just shows how much I'm making other people enjoy themselves! "
            k " ...That's nice, Disk. "
            k " It's really sweet of you to want others to be happy. "
            k " But what about yourself? "
            hide diskhappy at bottom
            show diskneutral at center
            d " Huh??? "
            k " Don't you want to be happy, too? "
            k " You can make others happy, yes... "
            k " But don't forget to take care of yourself aswell. "
            k " In order to be happy, you must take care of yourself well. "
            k " You don't always have to take care of others. "
            d " Hehe, don't worry! "
            d " I already know that, Koa! "
            d " But thank you very much for reminding me!! "
            d " I don't think I'll get like that anytime soon, but... "
            d " It's good that you reminded me just incase if I ever got like that!! "
            d " Now that I think about it... "
            d " It would be really bad if I got like that, don't you think? "
            k " Mhm... "
            d " Always gotta remember to take care of yourself, hehe! "
            d " But anyways... "
            d " Party day!!! "
            k " Woo. "
            k " (Psst, [name]...) "
            k " (He's kind of always like this.) "
            k " (It's not a bad thing, buuut...) "
            k " (If you ever think that he's too much, just tell him.) "
            k " (Trust me, he wouldn't overreact too bad.) "
            scene black with dissolve
            " You spent the rest of the break talking with Koa and Disk. "
            " Just talking about random things... "
            " Mostly talking about Disk's party though. "
            " You're considering on joining... "
            " Or if you've already joined then uh...yeah good for you "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump ochealthfri
    label ocfrigym1:
        # carmen and quinn
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked to the gym and found two of your classmates doing their own things. "
        " Who do you talk to for this break? "
        if carmenknow == True and quinnknow == True:
            menu:
                " {image=carmenicon} Carmen {image=carmenicon} ":
                    jump carmenintyeah
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump quinnintyeah
        elif carmenknow == True and quinnknow == False:
            menu:
                " {image=carmenicon} Carmen {image=carmenicon} ":
                    jump carmenintyeah
                " {image=quinnicon} A guy that looks like he's in the theater {image=quinnicon} ":
                    jump quinnintyeah
        elif carmenknow == False and quinnknow == True:
            menu:
                " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                    jump carmenintyeah
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump quinnintyeah
        else:
            menu:
                " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                    jump carmenintyeah
                " {image=quinnicon} A guy that looks like he's in the theater {image=quinnicon} ":
                    jump quinnintyeah
        label carmenintyeah:
            show carmenneutral at center with easeinright
            if carmenknow == True:
                " You walked over to him and asked him what he was doing. "
                ca " ...!! "
                ca " ... "
                " Looked like he was pretty happy to see you. "
                " You sat down next to him on the bleachers so that you could chill with him. "
                " Looking at what he was doing closer... "
                " It looked like he was practicing a song. "
                " It happened to be a song that you liked. "
                " For a fact, said song was on your current playlist right now. "
                " You asked him about it. "
                ca " ...? "
                ca " ...!! "
                " Looks like he didn't know that it was your favorite song. "
                " But, he seemed even more excited to know that it was. "
                " Because with enough practicing, he could play the song just for you. "
                " You were honestly pretty excited to hear him play the song. "
                " You had to wait until he fully mastered the song though. "
                " He was still fiddling around with his guitar as he looked up a tutorial. "
                " Man, sometimes you wish you could be cool like him... "
                " Like being able to play the guitar, I mean. "
                " Or just any instrument in general. "
                " But eh...you'd have to take very good care of it. "
                " Don't think you could handle the responsibility, "
                " Considering how you kept on fumbling with your items back at home. "
                " ...Including two of your plates. "
                ca " ... "
                " Carmen motions for you to pay attention. "
                " Looks like he's going to attempt to play it for the first time. "
                " You patiently waited for him to start playing the song. "
                ca " ... "
                " Carmen then starts playing the guitar whilst following the tutorial on his phone. "
                " He was actually doing pretty good. "
                " You almost caught yourself dozing off, for a fact. "
                hide carmenneutral at bottom
                show carmenangry at center
                " But then he messed up and had a little crashout. "
                ca " ... "
                " He seemed to be just a little bit frustrated that he had messed up. "
                " Looks like he wanted things to go perfectly... "
                " But then he just HAD to mess up. "
                " You reassured him that he played really well. "
                " And that it's okay to make mistakes sometimes. "
                " Mistakes are just a part of learning. "
                ca " ... "
                hide carmenangry at bottom
                show carmenneutral at center
                ca " ... "
                " Carmen soon nodded after you spoke your words... "
                " It was as if he was telling you a little thank you. "
                " He then continued to try and practice the song. "
                " He would have a little crashout every now and then everytime he messed up, but... "
                " Due to your words, he was doing that a little less now. "
                " Good job, dude. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Carmen. "
                " Just hanging out and listening to his tunes... "
                " It felt really relaxing, in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom. "
                pause 2.0
                jump ochealthfri
            else:
                $ carmenknow = True
                " Oh hey, you've seen this guy in your class before. "
                " His name is Carmen. And he's mute. "
                " He likes to play the guitar a whole lot from what you've heard. "
                " You walked over to him and asked him what he was doing. "
                ca " ...!! "
                ca " ... "
                " Looked like he was pretty happy to see you. "
                " You sat down next to him on the bleachers so that you could chill with him. "
                " Looking at what he was doing closer... "
                " It looked like he was practicing a song. "
                " It happened to be a song that you liked. "
                " For a fact, said song was on your current playlist right now. "
                " You asked him about it. "
                ca " ...? "
                ca " ...!! "
                " Looks like he didn't know that it was your favorite song. "
                " But, he seemed even more excited to know that it was. "
                " Because with enough practicing, he could play the song just for you. "
                " You were honestly pretty excited to hear him play the song. "
                " You had to wait until he fully mastered the song though. "
                " He was still fiddling around with his guitar as he looked up a tutorial. "
                " Man, sometimes you wish you could be cool like him... "
                " Like being able to play the guitar, I mean. "
                " Or just any instrument in general. "
                " But eh...you'd have to take very good care of it. "
                " Don't think you could handle the responsibility, "
                " Considering how you kept on fumbling with your items back at home. "
                " ...Including two of your plates. "
                ca " ... "
                " Carmen motions for you to pay attention. "
                " Looks like he's going to attempt to play it for the first time. "
                " You patiently waited for him to start playing the song. "
                ca " ... "
                " Carmen then starts playing the guitar whilst following the tutorial on his phone. "
                " He was actually doing pretty good. "
                " You almost caught yourself dozing off, for a fact. "
                hide carmenneutral at bottom
                show carmenangry at center
                " But then he messed up and had a little crashout. "
                ca " ... "
                " He seemed to be just a little bit frustrated that he had messed up. "
                " Looks like he wanted things to go perfectly... "
                " But then he just HAD to mess up. "
                " You reassured him that he played really well. "
                " And that it's okay to make mistakes sometimes. "
                " Mistakes are just a part of learning. "
                ca " ... "
                hide carmenangry at bottom
                show carmenneutral at center
                ca " ... "
                " Carmen soon nodded after you spoke your words... "
                " It was as if he was telling you a little thank you. "
                " He then continued to try and practice the song. "
                " He would have a little crashout every now and then everytime he messed up, but... "
                " Due to your words, he was doing that a little less now. "
                " Good job, dude. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Carmen. "
                " Just hanging out and listening to his tunes... "
                " It felt really relaxing, in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom. "
                pause 2.0
                jump ochealthfri
        label quinnintyeah:
            show quinnneutral at center with easeinleft
            if quinnknow == True:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was pretty excited about something... "
                " You wonder what it was though. "
                q " Ah, [name]! "
                q " Wonderful to see you here. "
                q " You might ask... "
                q " 'Dearest Quinn - why are you so happy today?' "
                q " Well! if the news hasn't gotten to you yet... "
                q " Then I'll tell you! "
                q " You see, dearest [name]... "
                q " The whole reason why I'm so excited right now... "
                q " Is because offff... "
                q " (Drumroll, please!) "
                hide quinnneutral at bottom
                show quinnhappy at center
                q " Today's going to be the day of my play! "
                q " And we've got everything memorized. "
                q " And when I tell you that, I mean EVERYTHING. "
                q " We've got everything under control! "
                q " Of course, with a play... "
                q " We're going to need quite the audience. "
                q " And I was wondering... "
                hide quinnhappy at bottom
                show quinnneutral at center
                q " Would you like to see my play, [name]? "
                q " It's alright if you don't want to. "
                q " Surely there's other things you're busy with, so... "
                q " I wouldn't want to disrupt that. "
                if quinnlv >= 20 or quinnlv == 20:
                    q " (It would be nice if [they] saw the play though...) "
                    if they == "she","he":
                        q " ([they] has been kind of making me motivated to continue this play, after all.) "
                    elif they == "they":
                        q " ([they] have been kind of making me motivated to continue this play, after all.) "
                    q " (It would be a little weird to go on without [them]...) "
                    q " (But I won't push [them] if they really don't want to go.) "
                    q " (That would just be really weird in all honesty...) "
                    q " (And that wold ruin our little aquaintance relationship we have.) "
                    q " (Wouldn't want that to be happening, hmhm...) "
                else:
                    q " I'm not that type of guy who bothers people for fun. "
                    q " Especially if they have something important to do. "
                q " Ahem... "
                q " On with the question... "
                q " Would you like to see my play, or not? "
                menu:
                    " Yeah! ":
                        $ quinnlv += 10
                        $ quinnshowsee = True
                        q " Oh! really? "
                        q " (I honestly wasn't expecting that.) "
                        q " (But still...) "
                        q " (I's great to have an audience!) "
                        q " That's wonderful, then! "
                        q " The play starts right before Miss Jiayu's class. "
                        q " In our last break period, to be simple. "
                        q " We'll be there at the teacher club room! "
                        q " And, since you're so special... "
                        q " You get to have front row seats! "
                        q " Just to get the perfect front row experience. "
                        q " Sounds good, right? "
                        q " (Hehe...I'm such a good host.) "
                        q " (I've gotta make sure that this story is interesting enough for the audience, too...) "
                        q " (Have to get them to be interested for the story to be good, after all!) "
                        q " Well, anyway... "
                        q " I'm going to discuss what you're going to see in the play. "
                        q " Just a little bit of spoilers... "
                        q " If you don't mind. "
                        " You didn't mind at all. "
                        " In fact, you loved being spoiled. "
                        " Unless it's for a game that you like. "
                        q " Wonderful! "
                        q " Let me begin... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Just talking to him about the play... "
                        " And honestly? you were really interested in the storyline. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a good bit, looks like it's time for another class. "
                        " You walked out of the gym and went to your classroom. "
                        pause 2.0
                        jump ochealthfri
                    " Nah, I'm busy ":
                        q " Really? "
                        q " What a shame, then... "
                        q " It would've been fun to have you there. "
                        q " But I won't force you. "
                        q " Well, anyway... "
                        q " I'm going to discuss what's going on in the play. "
                        q " Just a little bit of spoilers... "
                        q " If you don't mind. "
                        " You didn't mind at all. "
                        " In fact, you loved being spoiled. "
                        " Unless it's for a game that you like. "
                        q " Wonderful! "
                        q " Let me begin... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Just talking to him about the play... "
                        " You were only a little bit interested in the whole storyline. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a good bit, looks like it's time for another class. "
                        " You walked out of the gym and went to your classroom. "
                        pause 2.0
                        jump ochealthfri
            else:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was pretty excited about something... "
                " You wonder what it was though. "
                q " Ah, [name]! "
                q " Wonderful to see you here. "
                q " You might ask... "
                q " 'Dearest Quinn - why are you so happy today?' "
                q " Well! if the news hasn't gotten to you yet... "
                q " Then I'll tell you! "
                q " You see, dearest [name]... "
                q " The whole reason why I'm so excited right now... "
                q " Is because offff... "
                q " (Drumroll, please!) "
                hide quinnneutral at bottom
                show quinnhappy at center
                q " Today's going to be the day of my play! "
                q " And we've got everything memorized. "
                q " And when I tell you that, I mean EVERYTHING. "
                q " We've got everything under control! "
                q " Of course, with a play... "
                q " We're going to need quite the audience. "
                q " And I was wondering... "
                hide quinnhappy at bottom
                show quinnneutral at center
                q " Would you like to see my play, [name]? "
                q " It's alright if you don't want to. "
                q " Surely there's other things you're busy with, so... "
                q " I wouldn't want to disrupt that. "
                q " I'm not that type of guy who bothers people for fun. "
                q " Especially if they have something important to do. "
                q " Ahem... "
                q " On with the question... "
                q " Would you like to see my play, or not? "
                menu:
                    " Yeah! ":
                        $ quinnlv += 10
                        $ quinnshowsee = True
                        q " Oh! really? "
                        q " (I honestly wasn't expecting that.) "
                        q " (But still...) "
                        q " (I's great to have an audience!) "
                        q " That's wonderful, then! "
                        q " The play starts right before Miss Jiayu's class. "
                        q " In our last break period, to be simple. "
                        q " We'll be there at the teacher club room! "
                        q " And, since you're so special... "
                        q " You get to have front row seats! "
                        q " Just to get the perfect front row experience. "
                        q " Sounds good, right? "
                        q " (Hehe...I'm such a good host.) "
                        q " (I've gotta make sure that this story is interesting enough for the audience, too...) "
                        q " (Have to get them to be interested for the story to be good, after all!) "
                        q " Well, anyway... "
                        q " I'm going to discuss what you're going to see in the play. "
                        q " Just a little bit of spoilers... "
                        q " If you don't mind. "
                        " You didn't mind at all. "
                        " In fact, you loved being spoiled. "
                        " Unless it's for a game that you like. "
                        q " Wonderful! "
                        q " Let me begin... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Just talking to him about the play... "
                        " And honestly? you were really interested in the storyline. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a good bit, looks like it's time for another class. "
                        " You walked out of the gym and went to your classroom. "
                        pause 2.0
                        jump ochealthfri
                    " Nah, I'm busy ":
                        q " Really? "
                        q " What a shame, then... "
                        q " It would've been fun to have you there. "
                        q " But I won't force you. "
                        q " Well, anyway... "
                        q " I'm going to discuss what's going on in the play. "
                        q " Just a little bit of spoilers... "
                        q " If you don't mind. "
                        " You didn't mind at all. "
                        " In fact, you loved being spoiled. "
                        " Unless it's for a game that you like. "
                        q " Wonderful! "
                        q " Let me begin... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Just talking to him about the play... "
                        " You were only a little bit interested in the whole storyline. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a good bit, looks like it's time for another class. "
                        " You walked out of the gym and went to your classroom. "
                        pause 2.0
                        jump ochealthfri
    label ocfricafeteria1:
        # matte and orchid
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked to the cafeteria and spotted two of your classmates talking to eachother. "
        " Wondering what they're talking about, you walked over to them. "
        show matteneutral at left with easeinright
        show orchidneutral at right with easeinright
        if matteknow == True and orchidknow == True:
            " You sat down next to them and asked them what they were doing. "
            oc " Oh, hey there [name]!! "
            ma " Ooo, [name]!! hi!! "
            oc " I was just talking to Matte over here... "
            oc " She was asking me how to make bracelets! "
            ma " Yeah, surprisingly with all of my knowledge in arts... "
            ma " I don't actually know how to make bracelets, ehhe... "
            ma " I've been thinking of making some for my friend, Jam... "
            ma " But the only problem is that I don't know how! "
            oc " Oh, giiiirl... "
            oc " (Psst, [name].) "
            oc " (If you haven't been paying much attention...) "
            oc " (Matte's friend has a thing for her.) "
            oc " (The thing is, Matte is completely unaware about it.) "
            oc " (I've been trying to get her to notice, buuut...) "
            oc " (Let's just say that hasn't been going too well right now.) "
            oc " (Ahem...) "
            oc " Don't worry! I'll help you out!! "
            oc " Friendo's help eachother out, after all! "
            ma " I'm glad that you're helping me, Orchid... "
            ma " I just know that Jam would love matching bracelets! "
            ma " Actually, for a fact... "
            ma " Did you know that she actually likes to match a whole lot with me? "
            ma " Matching profile pictures, matching bios... "
            ma " I don't mind it all! In fact... "
            ma " I find it to be quite adorable of her! "
            oc " Aww!! "
            oc " (You see what I'm talking about here?) "
            oc " (Another thing about Jam...) "
            oc " (You ever notice that she's always looking so mean towards others?) "
            oc " (She even looks that way whenever I'm near!) "
            oc " (But whenever she's with Matte...) "
            oc " (It's like her gaze softened or something!) "
            oc " (Like, she's always acting so nice towards her...) "
            oc " (And then what about the others like us?!) "
            oc " (She looks like she would give us a beating whenever it comes to us!) "
            oc " (But whenever it comes to Matte?) "
            oc " (She looks like she could never hurt a fly!) "
            oc " (Insane, right?) "
            oc " (I'm not sure how Matte could ignore all of those signs...) "
            oc " (It's easy to mistake that as just normal friendship behaviour, but come on...) "
            oc " (All of the signs are RIGHT THERE!!!) "
            oc " (Good heavens...) "
            ma " Hey, what're you two talking about over there? "
            oc " Just talking about ideas for the bracelets! "
            ma " Without me?? "
            oc " Oh, uh... "
            oc " I meant bracelets for my other friends! "
            oc " You see, I'm also planning to make one for you! "
            oc " But I didn't want you to hear my super secret plans! "
            ma " Ahhh, I see! "
            ma " How about we talk about the bracelet for me and Jam though...? "
            ma " I want to get this done as soon as possible! "
            ma " You see, I'm planning to give this to her later... "
            oc " Oooh, I see, I see! "
            oc " Let's get started then! "
            ma " Yay! "
            scene black with dissolve
            " You spent the rest of the break talking with Orchid and Matte. "
            " And also watching them make bracelets. "
            " In the end, the braclets looked pretty cool and cute in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump ochealthfri
        elif matteknow == True and orchidknow == False:
            " You sat down next to them and asked them what they were doing. "
            x " Oh, hey there [name]!! "
            ma " Ooo, [name]!! hi!! "
            x " I don't think I've met you before! "
            x " Lemme introduce myself...It would be rude not to! "
            $ orchidknow = True
            oc " I'm Orchid! one of your classmates! "
            oc " I was just talking to Matte over here... "
            oc " She was asking me how to make bracelets! "
            ma " Yeah, surprisingly with all of my knowledge in arts... "
            ma " I don't actually know how to make bracelets, ehhe... "
            ma " I've been thinking of making some for my friend, Jam... "
            ma " But the only problem is that I don't know how! "
            oc " Oh, giiiirl... "
            oc " (Psst, [name].) "
            oc " (If you haven't been paying much attention...) "
            oc " (Matte's friend has a thing for her.) "
            oc " (The thing is, Matte is completely unaware about it.) "
            oc " (I've been trying to get her to notice, buuut...) "
            oc " (Let's just say that hasn't been going too well right now.) "
            oc " (Ahem...) "
            oc " Don't worry! I'll help you out!! "
            oc " Friendo's help eachother out, after all! "
            ma " I'm glad that you're helping me, Orchid... "
            ma " I just know that Jam would love matching bracelets! "
            ma " Actually, for a fact... "
            ma " Did you know that she actually likes to match a whole lot with me? "
            ma " Matching profile pictures, matching bios... "
            ma " I don't mind it all! In fact... "
            ma " I find it to be quite adorable of her! "
            oc " Aww!! "
            oc " (You see what I'm talking about here?) "
            oc " (Another thing about Jam...) "
            oc " (You ever notice that she's always looking so mean towards others?) "
            oc " (She even looks that way whenever I'm near!) "
            oc " (But whenever she's with Matte...) "
            oc " (It's like her gaze softened or something!) "
            oc " (Like, she's always acting so nice towards her...) "
            oc " (And then what about the others like us?!) "
            oc " (She looks like she would give us a beating whenever it comes to us!) "
            oc " (But whenever it comes to Matte?) "
            oc " (She looks like she could never hurt a fly!) "
            oc " (Insane, right?) "
            oc " (I'm not sure how Matte could ignore all of those signs...) "
            oc " (It's easy to mistake that as just normal friendship behaviour, but come on...) "
            oc " (All of the signs are RIGHT THERE!!!) "
            oc " (Good heavens...) "
            ma " Hey, what're you two talking about over there? "
            oc " Just talking about ideas for the bracelets! "
            ma " Without me?? "
            oc " Oh, uh... "
            oc " I meant bracelets for my other friends! "
            oc " You see, I'm also planning to make one for you! "
            oc " But I didn't want you to hear my super secret plans! "
            ma " Ahhh, I see! "
            ma " How about we talk about the bracelet for me and Jam though...? "
            ma " I want to get this done as soon as possible! "
            ma " You see, I'm planning to give this to her later... "
            oc " Oooh, I see, I see! "
            oc " Let's get started then! "
            ma " Yay! "
            scene black with dissolve
            " You spent the rest of the break talking with Orchid and Matte. "
            " And also watching them make bracelets. "
            " In the end, the braclets looked pretty cool and cute in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump ochealthfri
        elif matteknow == False and orchidknow == True:
            " You sat down next to them and asked them what they were doing. "
            oc " Oh, hey there [name]!! "
            x " Ooo, [name]!! hi!! "
            $ matteknow = True
            oc " I was just talking to Matte over here... "
            oc " She was asking me how to make bracelets! "
            ma " Yeah, surprisingly with all of my knowledge in arts... "
            ma " I don't actually know how to make bracelets, ehhe... "
            ma " I've been thinking of making some for my friend, Jam... "
            ma " But the only problem is that I don't know how! "
            oc " Oh, giiiirl... "
            oc " (Psst, [name].) "
            oc " (If you haven't been paying much attention...) "
            oc " (Matte's friend has a thing for her.) "
            oc " (The thing is, Matte is completely unaware about it.) "
            oc " (I've been trying to get her to notice, buuut...) "
            oc " (Let's just say that hasn't been going too well right now.) "
            oc " (Ahem...) "
            oc " Don't worry! I'll help you out!! "
            oc " Friendo's help eachother out, after all! "
            ma " I'm glad that you're helping me, Orchid... "
            ma " I just know that Jam would love matching bracelets! "
            ma " Actually, for a fact... "
            ma " Did you know that she actually likes to match a whole lot with me? "
            ma " Matching profile pictures, matching bios... "
            ma " I don't mind it all! In fact... "
            ma " I find it to be quite adorable of her! "
            oc " Aww!! "
            oc " (You see what I'm talking about here?) "
            oc " (Another thing about Jam...) "
            oc " (You ever notice that she's always looking so mean towards others?) "
            oc " (She even looks that way whenever I'm near!) "
            oc " (But whenever she's with Matte...) "
            oc " (It's like her gaze softened or something!) "
            oc " (Like, she's always acting so nice towards her...) "
            oc " (And then what about the others like us?!) "
            oc " (She looks like she would give us a beating whenever it comes to us!) "
            oc " (But whenever it comes to Matte?) "
            oc " (She looks like she could never hurt a fly!) "
            oc " (Insane, right?) "
            oc " (I'm not sure how Matte could ignore all of those signs...) "
            oc " (It's easy to mistake that as just normal friendship behaviour, but come on...) "
            oc " (All of the signs are RIGHT THERE!!!) "
            oc " (Good heavens...) "
            ma " Hey, what're you two talking about over there? "
            oc " Just talking about ideas for the bracelets! "
            ma " Without me?? "
            oc " Oh, uh... "
            oc " I meant bracelets for my other friends! "
            oc " You see, I'm also planning to make one for you! "
            oc " But I didn't want you to hear my super secret plans! "
            ma " Ahhh, I see! "
            ma " How about we talk about the bracelet for me and Jam though...? "
            ma " I want to get this done as soon as possible! "
            ma " You see, I'm planning to give this to her later... "
            oc " Oooh, I see, I see! "
            oc " Let's get started then! "
            ma " Yay! "
            scene black with dissolve
            " You spent the rest of the break talking with Orchid and Matte. "
            " And also watching them make bracelets. "
            " In the end, the braclets looked pretty cool and cute in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump ochealthfri
        else:
            " You sat down next to them and asked them what they were doing. "
            x " Oh, hey there [name]!! "
            x " Ooo, [name]!! hi!! "
            x " I don't think I've met you before! "
            x " Lemme introduce myself...It would be rude not to! "
            $ orchidknow = True
            oc " I'm Orchid! one of your classmates! "
            $ matteknow = True
            oc " I was just talking to Matte over here... "
            oc " She was asking me how to make bracelets! "
            ma " Yeah, surprisingly with all of my knowledge in arts... "
            ma " I don't actually know how to make bracelets, ehhe... "
            ma " I've been thinking of making some for my friend, Jam... "
            ma " But the only problem is that I don't know how! "
            oc " Oh, giiiirl... "
            oc " (Psst, [name].) "
            oc " (If you haven't been paying much attention...) "
            oc " (Matte's friend has a thing for her.) "
            oc " (The thing is, Matte is completely unaware about it.) "
            oc " (I've been trying to get her to notice, buuut...) "
            oc " (Let's just say that hasn't been going too well right now.) "
            oc " (Ahem...) "
            oc " Don't worry! I'll help you out!! "
            oc " Friendo's help eachother out, after all! "
            ma " I'm glad that you're helping me, Orchid... "
            ma " I just know that Jam would love matching bracelets! "
            ma " Actually, for a fact... "
            ma " Did you know that she actually likes to match a whole lot with me? "
            ma " Matching profile pictures, matching bios... "
            ma " I don't mind it all! In fact... "
            ma " I find it to be quite adorable of her! "
            oc " Aww!! "
            oc " (You see what I'm talking about here?) "
            oc " (Another thing about Jam...) "
            oc " (You ever notice that she's always looking so mean towards others?) "
            oc " (She even looks that way whenever I'm near!) "
            oc " (But whenever she's with Matte...) "
            oc " (It's like her gaze softened or something!) "
            oc " (Like, she's always acting so nice towards her...) "
            oc " (And then what about the others like us?!) "
            oc " (She looks like she would give us a beating whenever it comes to us!) "
            oc " (But whenever it comes to Matte?) "
            oc " (She looks like she could never hurt a fly!) "
            oc " (Insane, right?) "
            oc " (I'm not sure how Matte could ignore all of those signs...) "
            oc " (It's easy to mistake that as just normal friendship behaviour, but come on...) "
            oc " (All of the signs are RIGHT THERE!!!) "
            oc " (Good heavens...) "
            ma " Hey, what're you two talking about over there? "
            oc " Just talking about ideas for the bracelets! "
            ma " Without me?? "
            oc " Oh, uh... "
            oc " I meant bracelets for my other friends! "
            oc " You see, I'm also planning to make one for you! "
            oc " But I didn't want you to hear my super secret plans! "
            ma " Ahhh, I see! "
            ma " How about we talk about the bracelet for me and Jam though...? "
            ma " I want to get this done as soon as possible! "
            ma " You see, I'm planning to give this to her later... "
            oc " Oooh, I see, I see! "
            oc " Let's get started then! "
            ma " Yay! "
            scene black with dissolve
            " You spent the rest of the break talking with Orchid and Matte. "
            " And also watching them make bracelets. "
            " In the end, the braclets looked pretty cool and cute in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump ochealthfri
    label ocfrirooftop1:
        # nox and jam
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked to the rooftop and spotted two of your classmates doing their own things. "
        " Who would you like to talk to? "
        if noxknow == True and jamknow == True:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump slasherballs
                " {image=jamicon} Jam {image=jamicon} ":
                    jump slashermom
        elif noxknow == True and jamknow == False:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump slasherballs
                " {image=jamicon} A mean looking girl {image=jamicon} ":
                    jump slashermom
        elif noxknow == False and jamknow == True:
            menu:
                " {image=noxicon} A guy that looks sleepy {image=noxicon} ":
                    jump slasherballs
                " {image=jamicon} Jam {image=jamicon} ":
                    jump slashermom
        else:
            menu:
                " {image=noxicon} A guy that looks sleepy {image=noxicon} ":
                    jump slasherballs
                " {image=jamicon} A mean looking girl {image=jamicon} ":
                    jump slashermom
        label slasherballs:
            show noxneutral at center with easeinleft
            if noxknow == True:
                " You walked over to him and asked him if he was doing alright. "
                " Looked like he could really use a nap right now... "
                n " Hm...? "
                n " Oh, hey there, [name]... "
                n " I was just admiring the clouds... "
                n " Clouds are really cool, you know...? "
                n " They can make all kinds of shapes... "
                n " And you can just... "
                n " Imagine what they're supposed to be... "
                n " It's a thing I used to do a lot as a kid... "
                n " Just stare up at the clouds... "
                n " And think of what everything could be... "
                n " Now that I think about it... "
                n " I've imagined a lot of things while looking at the clouds... "
                n " A lot of stories... "
                n " A lot of what-if's... "
                n " Looking at the clouds... "
                n " It makes me feel calm... "
                n " And honestly...? "
                n " It feels like the only times where I could take a break from the world... "
                n " I can just imagine whatever I want... "
                n " Think about whatever I want... "
                n " Without having to worry about the things going on in the world. "
                n " It's nice, but... "
                n " I don't want to do it too often. "
                n " I know that it's relaxing to just chill... "
                n " But we can't always relax all the time... "
                n " Even thoughI want to go back to my bed right now... "
                n " I know that I have to do something important. "
                n " And something productive... "
                n " But for now...? "
                n " Since we're given break time... "
                n " I can just relax for now... "
                n " So, um... "
                n " I wouldn't mind if you would want to relax with me. "
                n " In my opinion... "
                n " Relaxing with someone is better than relaxing alone... "
                n " So uhh... "
                n " Feel free to just hangout with me... "
                " You decided to hangout with Nox. "
                " You needed some relaxing, after all. "
                scene black with dissolve
                " You spent the rest of the break just hanging out with Nox. "
                " Just relaxing with him...and looking at the clouds. "
                " It felt really nice. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump ochealthfri
            else:
                " You walked over to him and asked him if he was doing alright. "
                " Looked like he could really use a nap right now... "
                x " Hm...? "
                x " Oh, hey there, [name]... "
                $ noxknow = True
                n " I'm Nox...Nox Cesso... "
                n " I was just admiring the clouds... "
                n " Clouds are really cool, you know...? "
                n " They can make all kinds of shapes... "
                n " And you can just... "
                n " Imagine what they're supposed to be... "
                n " It's a thing I used to do a lot as a kid... "
                n " Just stare up at the clouds... "
                n " And think of what everything could be... "
                n " Now that I think about it... "
                n " I've imagined a lot of things while looking at the clouds... "
                n " A lot of stories... "
                n " A lot of what-if's... "
                n " Looking at the clouds... "
                n " It makes me feel calm... "
                n " And honestly...? "
                n " It feels like the only times where I could take a break from the world... "
                n " I can just imagine whatever I want... "
                n " Think about whatever I want... "
                n " Without having to worry about the things going on in the world. "
                n " It's nice, but... "
                n " I don't want to do it too often. "
                n " I know that it's relaxing to just chill... "
                n " But we can't always relax all the time... "
                n " Even thoughI want to go back to my bed right now... "
                n " I know that I have to do something important. "
                n " And something productive... "
                n " But for now...? "
                n " Since we're given break time... "
                n " I can just relax for now... "
                n " So, um... "
                n " I wouldn't mind if you would want to relax with me. "
                n " In my opinion... "
                n " Relaxing with someone is better than relaxing alone... "
                n " So uhh... "
                n " Feel free to just hangout with me... "
                " You decided to hangout with Nox. "
                " You needed some relaxing, after all. "
                scene black with dissolve
                " You spent the rest of the break just hanging out with Nox. "
                " Just relaxing with him...and looking at the clouds. "
                " It felt really nice. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump ochealthfri
        label slashermom:
            show jamneutral at center with easeinright
            if jamknow == True:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was zoning out a whole lot... "
                ja " Huh? oh. "
                ja " You. "
                ja " ... "
                ja " I was just thinking of something. "
                ja " Thinking of my friend... "
                ja " I've been meaning to tell her something for awhile now. "
                ja " But the only problem is that I don't know how to word it. "
                ja " What if I say the wrong thing, you know? "
                ja " ...It's frustrating. "
                ja " I just want to tell her something, how hard could it be? "
                ja " ... "
                ja " The truth is, it's very hard to tell her something like this. "
                ja " My mom would kill me if I even told her what I wanted to say to my best friend. "
                ja " That's why I can't ask advice from her. "
                " You asked her what her question was gonna be. "
                " You were the curious fella, and maybe you could help her out... "
                " You just needed to know the situation. "
                ja " ...I've been liking my friend for awhile now. "
                ja " She's good at art and everything else... "
                ja " This is gonna sound REALLY corny, but... "
                ja " She's perfect in my eyes. "
                ja " Even if she does something wrong... "
                ja " That doesn't change how I view her. "
                ja " She's still the best to me. "
                ja " But... "
                ja " How do I word that to her without making it sound weird? "
                ja " I don't want to gross her out... "
                ja " What if she doesn't even like girls in the first place. "
                ja " ... "
                ja " Even though I'm not sure of what she thinks... "
                ja " I still have to try. "
                ja " Just to really make sure of how she feels. "
                ja " ... "
                ja " I think... "
                ja " I think I'll just talk to her after gardening class. "
                ja " Would that time be good? "
                ja " I'm not even sure myself. "
                ja " We'll just see, though... "
                " You told her that you were cheering for her. "
                " Surely this will end well. "
                ja " ...Thanks. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Jam. "
                " Talking about what she could do for her friend... "
                " You had multiple ideas to get this ship sailing. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump ochealthfri
            else:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was zoning out a whole lot... "
                x " Huh? oh. "
                x " You. "
                $ jamknow = True
                ja " Uh...I'm Jam. "
                ja " ... "
                ja " I was just thinking of something. "
                ja " Thinking of my friend... "
                ja " I've been meaning to tell her something for awhile now. "
                ja " But the only problem is that I don't know how to word it. "
                ja " What if I say the wrong thing, you know? "
                ja " ...It's frustrating. "
                ja " I just want to tell her something, how hard could it be? "
                ja " ... "
                ja " The truth is, it's very hard to tell her something like this. "
                ja " My mom would kill me if I even told her what I wanted to say to my best friend. "
                ja " That's why I can't ask advice from her. "
                " You asked her what her question was gonna be. "
                " You were the curious fella, and maybe you could help her out... "
                " You just needed to know the situation. "
                ja " ...I've been liking my friend for awhile now. "
                ja " She's good at art and everything else... "
                ja " This is gonna sound REALLY corny, but... "
                ja " She's perfect in my eyes. "
                ja " Even if she does something wrong... "
                ja " That doesn't change how I view her. "
                ja " She's still the best to me. "
                ja " But... "
                ja " How do I word that to her without making it sound weird? "
                ja " I don't want to gross her out... "
                ja " What if she doesn't even like girls in the first place. "
                ja " ... "
                ja " Even though I'm not sure of what she thinks... "
                ja " I still have to try. "
                ja " Just to really make sure of how she feels. "
                ja " ... "
                ja " I think... "
                ja " I think I'll just talk to her after gardening class. "
                ja " Would that time be good? "
                ja " I'm not even sure myself. "
                ja " We'll just see, though... "
                " You told her that you were cheering for her. "
                " Surely this will end well. "
                ja " ...Thanks. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Jam. "
                " Talking about what she could do for her friend... "
                " You had multiple ideas to get this ship sailing. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump ochealthfri
    label ocfrilibrary1:
        # temero and  yinhui
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked into the library and found two of your classmates talking to eachother. "
        " Wondering what they're talking about, you decided to walk over to them. "
        show temeroneutral at right with easeinleft
        show yinhuineutral at left with easeinleft
        if temeroknow == True and yinhuiknow == True:
            " You asked them what they were up to. "
            yi " Oh, it's...you. "
            yi " Temero over here was just showing me one of her experiments. "
            yi " It's insane...the things you come up with. "
            yi " Like what do you mean you turned a butterfly into a burger? "
            tm " Hehe. "
            tm " I did that all with the power of science! "
            yi " Technically speaking... "
            yi " YOUR version of science. "
            yi " There's no way any regular science could make something like that happen. "
            tm " Oh, it CAN happen! "
            tm " You just have to believe very hard. "
            tm " And by hard... "
            tm " I mean VERY hard. "
            yi " ... "
            yi " Anyway...what're you working on now? "
            tm " Just a potion to make flowers grow. "
            tm " Nothing too special or grand. really. "
            tm " Just spray this around and BOOM! flowers. "
            tm " It could be flowers of any kind, too. "
            tm " Just not poisonous ones. "
            tm " Those are for me. "
            yi " Huh. "
            yi " And why are you making a potion for flowers? "
            yi " It seems pretty... "
            yi " ...'Not-useful', in my opinion. "
            yi " Just comparing them to what you've worked on in the past. "
            tm " It's cause Miss Wisteria ordered me to make these. "
            tm " She said that it would give the school more... "
            tm " Pizzazz. "
            yi " As if all the fancy decorations weren't enough, hm. "
            yi " But, I won't judge. "
            yi " This school does look like it needs more plant life around... "
            tm " That's true! "
            tm " It could also make the school look more approachable. "
            tm " And it could make the school look more fancy, in a way. "
            tm " It's always an honor to work for a teacher like this, hehe. "
            yi " I bet you feel really good after getting to do all their work. "
            yi " The teacher's don't really do that a lot, you know. "
            tm " I know, I know! "
            tm " That's why I'm always happy to help them. "
            tm " No matter what they ask for. "
            yi " ... "
            tm " Did I say something weird? "
            yi " You kinda did, with how you worded it. "
            tm " Oh please, I already have someone in my mind. "
            tm " Of course I wouldn't be talking about THAT. "
            tm " Get your mind out of that place, it really isn't good for you. "
            yi " Can't help it. "
            tm " Thanks for the new potion idea, then! "
            yi " ...Hold on, what? "
            scene black with dissolve
            " You spent the rest of the break talking with Temero and Yinhui. "
            " Just talking about the things that Temero was making... "
            " The normal stuff. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump ochealthfri
        elif temeroknow == True and yinhuiknow == False:
            " You asked them what they were up to. "
            x " Oh, it's...you. "
            $ yinhuiknow = True
            yi " I'm Yinhui. "
            yi " Temero over here was just showing me one of her experiments. "
            yi " It's insane...the things you come up with. "
            yi " Like what do you mean you turned a butterfly into a burger? "
            tm " Hehe. "
            tm " I did that all with the power of science! "
            yi " Technically speaking... "
            yi " YOUR version of science. "
            yi " There's no way any regular science could make something like that happen. "
            tm " Oh, it CAN happen! "
            tm " You just have to believe very hard. "
            tm " And by hard... "
            tm " I mean VERY hard. "
            yi " ... "
            yi " Anyway...what're you working on now? "
            tm " Just a potion to make flowers grow. "
            tm " Nothing too special or grand. really. "
            tm " Just spray this around and BOOM! flowers. "
            tm " It could be flowers of any kind, too. "
            tm " Just not poisonous ones. "
            tm " Those are for me. "
            yi " Huh. "
            yi " And why are you making a potion for flowers? "
            yi " It seems pretty... "
            yi " ...'Not-useful', in my opinion. "
            yi " Just comparing them to what you've worked on in the past. "
            tm " It's cause Miss Wisteria ordered me to make these. "
            tm " She said that it would give the school more... "
            tm " Pizzazz. "
            yi " As if all the fancy decorations weren't enough, hm. "
            yi " But, I won't judge. "
            yi " This school does look like it needs more plant life around... "
            tm " That's true! "
            tm " It could also make the school look more approachable. "
            tm " And it could make the school look more fancy, in a way. "
            tm " It's always an honor to work for a teacher like this, hehe. "
            yi " I bet you feel really good after getting to do all their work. "
            yi " The teacher's don't really do that a lot, you know. "
            tm " I know, I know! "
            tm " That's why I'm always happy to help them. "
            tm " No matter what they ask for. "
            yi " ... "
            tm " Did I say something weird? "
            yi " You kinda did, with how you worded it. "
            tm " Oh please, I already have someone in my mind. "
            tm " Of course I wouldn't be talking about THAT. "
            tm " Get your mind out of that place, it really isn't good for you. "
            yi " Can't help it. "
            tm " Thanks for the new potion idea, then! "
            yi " ...Hold on, what? "
            scene black with dissolve
            " You spent the rest of the break talking with Temero and Yinhui. "
            " Just talking about the things that Temero was making... "
            " The normal stuff. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump ochealthfri
        elif temeroknow == False and yinhuiknow == True:
            " You asked them what they were up to. "
            yi " Oh, it's...you. "
            $ temeroknow = True
            yi " Temero over here was just showing me one of her experiments. "
            yi " It's insane...the things you come up with. "
            yi " Like what do you mean you turned a butterfly into a burger? "
            tm " Hehe. "
            tm " I did that all with the power of science! "
            yi " Technically speaking... "
            yi " YOUR version of science. "
            yi " There's no way any regular science could make something like that happen. "
            tm " Oh, it CAN happen! "
            tm " You just have to believe very hard. "
            tm " And by hard... "
            tm " I mean VERY hard. "
            yi " ... "
            yi " Anyway...what're you working on now? "
            tm " Just a potion to make flowers grow. "
            tm " Nothing too special or grand. really. "
            tm " Just spray this around and BOOM! flowers. "
            tm " It could be flowers of any kind, too. "
            tm " Just not poisonous ones. "
            tm " Those are for me. "
            yi " Huh. "
            yi " And why are you making a potion for flowers? "
            yi " It seems pretty... "
            yi " ...'Not-useful', in my opinion. "
            yi " Just comparing them to what you've worked on in the past. "
            tm " It's cause Miss Wisteria ordered me to make these. "
            tm " She said that it would give the school more... "
            tm " Pizzazz. "
            yi " As if all the fancy decorations weren't enough, hm. "
            yi " But, I won't judge. "
            yi " This school does look like it needs more plant life around... "
            tm " That's true! "
            tm " It could also make the school look more approachable. "
            tm " And it could make the school look more fancy, in a way. "
            tm " It's always an honor to work for a teacher like this, hehe. "
            yi " I bet you feel really good after getting to do all their work. "
            yi " The teacher's don't really do that a lot, you know. "
            tm " I know, I know! "
            tm " That's why I'm always happy to help them. "
            tm " No matter what they ask for. "
            yi " ... "
            tm " Did I say something weird? "
            yi " You kinda did, with how you worded it. "
            tm " Oh please, I already have someone in my mind. "
            tm " Of course I wouldn't be talking about THAT. "
            tm " Get your mind out of that place, it really isn't good for you. "
            yi " Can't help it. "
            tm " Thanks for the new potion idea, then! "
            yi " ...Hold on, what? "
            scene black with dissolve
            " You spent the rest of the break talking with Temero and Yinhui. "
            " Just talking about the things that Temero was making... "
            " The normal stuff. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump ochealthfri
        else:
            " You asked them what they were up to. "
            x " Oh, it's...you. "
            $ yinhuiknow = True
            $ temeroknow = True
            yi " I'm Yinhui. "
            yi " Temero over here was just showing me one of her experiments. "
            yi " It's insane...the things you come up with. "
            yi " Like what do you mean you turned a butterfly into a burger? "
            tm " Hehe. "
            tm " I did that all with the power of science! "
            yi " Technically speaking... "
            yi " YOUR version of science. "
            yi " There's no way any regular science could make something like that happen. "
            tm " Oh, it CAN happen! "
            tm " You just have to believe very hard. "
            tm " And by hard... "
            tm " I mean VERY hard. "
            yi " ... "
            yi " Anyway...what're you working on now? "
            tm " Just a potion to make flowers grow. "
            tm " Nothing too special or grand. really. "
            tm " Just spray this around and BOOM! flowers. "
            tm " It could be flowers of any kind, too. "
            tm " Just not poisonous ones. "
            tm " Those are for me. "
            yi " Huh. "
            yi " And why are you making a potion for flowers? "
            yi " It seems pretty... "
            yi " ...'Not-useful', in my opinion. "
            yi " Just comparing them to what you've worked on in the past. "
            tm " It's cause Miss Wisteria ordered me to make these. "
            tm " She said that it would give the school more... "
            tm " Pizzazz. "
            yi " As if all the fancy decorations weren't enough, hm. "
            yi " But, I won't judge. "
            yi " This school does look like it needs more plant life around... "
            tm " That's true! "
            tm " It could also make the school look more approachable. "
            tm " And it could make the school look more fancy, in a way. "
            tm " It's always an honor to work for a teacher like this, hehe. "
            yi " I bet you feel really good after getting to do all their work. "
            yi " The teacher's don't really do that a lot, you know. "
            tm " I know, I know! "
            tm " That's why I'm always happy to help them. "
            tm " No matter what they ask for. "
            yi " ... "
            tm " Did I say something weird? "
            yi " You kinda did, with how you worded it. "
            tm " Oh please, I already have someone in my mind. "
            tm " Of course I wouldn't be talking about THAT. "
            tm " Get your mind out of that place, it really isn't good for you. "
            yi " Can't help it. "
            tm " Thanks for the new potion idea, then! "
            yi " ...Hold on, what? "
            scene black with dissolve
            " You spent the rest of the break talking with Temero and Yinhui. "
            " Just talking about the things that Temero was making... "
            " The normal stuff. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump ochealthfri

label ochealthfri:
    scene classroom with dissolve
    " You walked into the classroom and waited for the health teacher to arrive. "
    " Whilst you were waiting, you decided to draw in your notebook. "
    " Just drawing random things...nothing too special, really. "
    " After a few minutes of drawing, you heard the door open. "
    " Looks like the teacher has arrived. "
    show altrixneutral at center with easeinright
    msa " Sorry that I'm late, class! "
    msa " Just had to deal with a few things... "
    msa " Mister Sol had an accident in the hallway, so... "
    msa " I had to help! "
    msa " Anyway... "
    msa " Let's get to our lesson of the day, okay? "
    msa " Let's begin! "
    scene black with dissolve
    " You sort of fell asleep in the middle of class. "
    " Mister Altrix let you sleep, surprisingly. "
    " He could probably tell that you were very tired. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for another break. "
    " You waited for everyone to get out of the classroom before you did. "
    pause 2.0
    jump ocfribreak2

label ocfribreak2:
    scene hallway with dissolve
    " Looks like it's time for another break. "
    " Where are you gonna hangout this time? "
    menu:
        " {image=matteicon} The front of the school {image=yinyangicon} ":
            jump ocfrifront
        " {image=jacobicon} The back of the school {image=jamicon} ":
            jump ocfriback
        " {image=diskicon} The gym {image=temeroicon}":
            jump ocfrigym
        " {image=koaicon} The cafeteria {image=carmenicon} ":
            jump ocfricafeteria
        " {image=orchidicon} The rooftop {image=sparkicon} ":
            jump ocfrirooftop
        " {image=noxicon} The library {image=quinnicon} ":
            jump ocfrilibrary
    label ocfrifront:
        # interact // matte and yangyi
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked to the front of the school and spotted your two classmates talking to eachother. "
        " Being curious on what they're talking about, you walked over to them. "
        show matteneutral at left with easeinright
        show yangyineutral at right with easeinright
        if matteknow == True and yangyiknow == True:
            ma " Hi there, [name]!! "
            ya " Oooh, [name]!! hi hi!! "
            ya " I was just talking to Matte over here!! "
            ya " You know... "
            ya " Her art is really good! "
            ma " Awww, Yangyi!! "
            ma " I'm just doing what I do best! "
            ma " And hey... "
            ma " Your mom likes paintings, right? "
            ya " Yes, why? "
            ya " Are you thinking of painting her? "
            ma " Yep! "
            ma " Maybe sometime when all of you are free? "
            ma " And by all of you, I mean you, your brother, and your mom. "
            ya " Oh, don't worry! "
            ya " We're all free tomorrow! "
            ya " You could come by and paint us! "
            ya " I think mom would really enjoy it if she got a painting of us!! "
            ya " Do we need to pay you for this? "
            ma " No, not at all! "
            hide yangyineutral at bottom
            show yangyisurprised at right
            ya " Really...? "
            ya " Are you sure about that? "
            ma " Yeah, I'm really sure! "
            ma " You don't have to pay me for this, or for anything... "
            ma " Besides, it's just a painting! "
            ma " Nothing too important, right? "
            ya " ... "
            hide yangyisurprised at bottom
            show yangyihappy at right
            ya " Even if you say that... "
            ya " I'm still going to pay you!! "
            ma " ...I'm sorry, what? "
            ya " Your artwork is really good, Matte! "
            ya " In fact, so good... "
            ya " That you should get paid for it! "
            ma " Oh, come on now... "
            ma " It's not that good! "
            ma " I don't think it should be in a museum or anything, ehe... "
            ya " Trust me, it's really good! "
            ya " It deserves being in the museum like the other paintings there! "
            ya " No matter what you say... "
            ya " I'll think that it's great no matter what!! "
            ya " And I'd still pay you everytime I ask you for a painting! "
            ya " Getting it free just feels like a crime, you know? "
            ma " ...I guess you're right. "
            ma " Still a little insane that you would pay me for this, though... "
            ma " This is the first time someone has paid me, believe it or not. "
            ya " REALLY??? "
            ya " Then I'm glad to have the honor of being the first one to pay you!! "
            ya " You should really do more paid works... "
            ya " That could really help you in the future! "
            ma " Yeah, you're right! "
            ma " I should look for some websites to help me with that... "
            ma " Thanks for planning on paying me again, Yangyi! "
            ya " No problem! "
            scene black with dissolve
            " You spent the rest of the break talking with Yangyi and Matte. "
            " Now you kind of want a painting from Matte... "
            " Only if you weren't so poor. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump ocpefri
        elif matteknow == True and yangyiknow == False:
            ma " Hi there, [name]!! "
            x " Oooh, [name]!! hi hi!! "
            x " Don't think we'vemet before, so... "
            $ yangyiknow = True
            ya " I'm Yangyi! son of Miss Jiayu!! "
            ya " I was just talking to Matte over here!! "
            ya " You know... "
            ya " Her art is really good! "
            ma " Awww, Yangyi!! "
            ma " I'm just doing what I do best! "
            ma " And hey... "
            ma " Your mom likes paintings, right? "
            ya " Yes, why? "
            ya " Are you thinking of painting her? "
            ma " Yep! "
            ma " Maybe sometime when all of you are free? "
            ma " And by all of you, I mean you, your brother, and your mom. "
            ya " Oh, don't worry! "
            ya " We're all free tomorrow! "
            ya " You could come by and paint us! "
            ya " I think mom would really enjoy it if she got a painting of us!! "
            ya " Do we need to pay you for this? "
            ma " No, not at all! "
            hide yangyineutral at bottom
            show yangyisurprised at right
            ya " Really...? "
            ya " Are you sure about that? "
            ma " Yeah, I'm really sure! "
            ma " You don't have to pay me for this, or for anything... "
            ma " Besides, it's just a painting! "
            ma " Nothing too important, right? "
            ya " ... "
            hide yangyisurprised at bottom
            show yangyihappy at right
            ya " Even if you say that... "
            ya " I'm still going to pay you!! "
            ma " ...I'm sorry, what? "
            ya " Your artwork is really good, Matte! "
            ya " In fact, so good... "
            ya " That you should get paid for it! "
            ma " Oh, come on now... "
            ma " It's not that good! "
            ma " I don't think it should be in a museum or anything, ehe... "
            ya " Trust me, it's really good! "
            ya " It deserves being in the museum like the other paintings there! "
            ya " No matter what you say... "
            ya " I'll think that it's great no matter what!! "
            ya " And I'd still pay you everytime I ask you for a painting! "
            ya " Getting it free just feels like a crime, you know? "
            ma " ...I guess you're right. "
            ma " Still a little insane that you would pay me for this, though... "
            ma " This is the first time someone has paid me, believe it or not. "
            ya " REALLY??? "
            ya " Then I'm glad to have the honor of being the first one to pay you!! "
            ya " You should really do more paid works... "
            ya " That could really help you in the future! "
            ma " Yeah, you're right! "
            ma " I should look for some websites to help me with that... "
            ma " Thanks for planning on paying me again, Yangyi! "
            ya " No problem! "
            scene black with dissolve
            " You spent the rest of the break talking with Yangyi and Matte. "
            " Now you kind of want a painting from Matte... "
            " Only if you weren't so poor. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump ocpefri
        elif matteknow == False and yangyiknow == True:
            x " Hi there, [name]!! "
            ya " Oooh, [name]!! hi hi!! "
            $ matteknow = True
            ya " I was just talking to Matte over here!! "
            ya " You know... "
            ya " Her art is really good! "
            ma " Awww, Yangyi!! "
            ma " I'm just doing what I do best! "
            ma " And hey... "
            ma " Your mom likes paintings, right? "
            ya " Yes, why? "
            ya " Are you thinking of painting her? "
            ma " Yep! "
            ma " Maybe sometime when all of you are free? "
            ma " And by all of you, I mean you, your brother, and your mom. "
            ya " Oh, don't worry! "
            ya " We're all free tomorrow! "
            ya " You could come by and paint us! "
            ya " I think mom would really enjoy it if she got a painting of us!! "
            ya " Do we need to pay you for this? "
            ma " No, not at all! "
            hide yangyineutral at bottom
            show yangyisurprised at right
            ya " Really...? "
            ya " Are you sure about that? "
            ma " Yeah, I'm really sure! "
            ma " You don't have to pay me for this, or for anything... "
            ma " Besides, it's just a painting! "
            ma " Nothing too important, right? "
            ya " ... "
            hide yangyisurprised at bottom
            show yangyihappy at right
            ya " Even if you say that... "
            ya " I'm still going to pay you!! "
            ma " ...I'm sorry, what? "
            ya " Your artwork is really good, Matte! "
            ya " In fact, so good... "
            ya " That you should get paid for it! "
            ma " Oh, come on now... "
            ma " It's not that good! "
            ma " I don't think it should be in a museum or anything, ehe... "
            ya " Trust me, it's really good! "
            ya " It deserves being in the museum like the other paintings there! "
            ya " No matter what you say... "
            ya " I'll think that it's great no matter what!! "
            ya " And I'd still pay you everytime I ask you for a painting! "
            ya " Getting it free just feels like a crime, you know? "
            ma " ...I guess you're right. "
            ma " Still a little insane that you would pay me for this, though... "
            ma " This is the first time someone has paid me, believe it or not. "
            ya " REALLY??? "
            ya " Then I'm glad to have the honor of being the first one to pay you!! "
            ya " You should really do more paid works... "
            ya " That could really help you in the future! "
            ma " Yeah, you're right! "
            ma " I should look for some websites to help me with that... "
            ma " Thanks for planning on paying me again, Yangyi! "
            ya " No problem! "
            scene black with dissolve
            " You spent the rest of the break talking with Yangyi and Matte. "
            " Now you kind of want a painting from Matte... "
            " Only if you weren't so poor. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to the gym. "
            pause 2.0
            jump ocpefri
        else:
            x " Hi there, [name]!! "
            x " Oooh, [name]!! hi hi!! "
            x " Don't think we'vemet before, so... "
            $ yangyiknow = True
            $ matteknow = True
            ya " I'm Yangyi! son of Miss Jiayu!! "
            ya " I was just talking to Matte over here!! "
            ya " You know... "
            ya " Her art is really good! "
            ma " Awww, Yangyi!! "
            ma " I'm just doing what I do best! "
            ma " And hey... "
            ma " Your mom likes paintings, right? "
            ya " Yes, why? "
            ya " Are you thinking of painting her? "
            ma " Yep! "
            ma " Maybe sometime when all of you are free? "
            ma " And by all of you, I mean you, your brother, and your mom. "
            ya " Oh, don't worry! "
            ya " We're all free tomorrow! "
            ya " You could come by and paint us! "
            ya " I think mom would really enjoy it if she got a painting of us!! "
            ya " Do we need to pay you for this? "
            ma " No, not at all! "
            hide yangyineutral at bottom
            show yangyisurprised at right
            ya " Really...? "
            ya " Are you sure about that? "
            ma " Yeah, I'm really sure! "
            ma " You don't have to pay me for this, or for anything... "
            ma " Besides, it's just a painting! "
            ma " Nothing too important, right? "
            ya " ... "
            hide yangyisurprised at bottom
            show yangyihappy at right
            ya " Even if you say that... "
            ya " I'm still going to pay you!! "
            ma " ...I'm sorry, what? "
            ya " Your artwork is really good, Matte! "
            ya " In fact, so good... "
            ya " That you should get paid for it! "
            ma " Oh, come on now... "
            ma " It's not that good! "
            ma " I don't think it should be in a museum or anything, ehe... "
            ya " Trust me, it's really good! "
            ya " It deserves being in the museum like the other paintings there! "
            ya " No matter what you say... "
            ya " I'll think that it's great no matter what!! "
            ya " And I'd still pay you everytime I ask you for a painting! "
            ya " Getting it free just feels like a crime, you know? "
            ma " ...I guess you're right. "
            ma " Still a little insane that you would pay me for this, though... "
            ma " This is the first time someone has paid me, believe it or not. "
            ya " REALLY??? "
            ya " Then I'm glad to have the honor of being the first one to pay you!! "
            ya " You should really do more paid works... "
            ya " That could really help you in the future! "
            ma " Yeah, you're right! "
            ma " I should look for some websites to help me with that... "
            ma " Thanks for planning on paying me again, Yangyi! "
            ya " No problem! "
            scene black with dissolve
            " You spent the rest of the break talking with Yangyi and Matte. "
            " Now you kind of want a painting from Matte... "
            " Only if you weren't so poor. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to the gym. "
            pause 2.0
            jump ocpefri
    label ocfriback:
        # jacob and jam not interact
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of the school and spotted two of your classmates doing their own things. "
        " Who would you talk to here? "
        if jacobknow == True and jamknow == True:
            menu:
                " {image=jacobicon} Jacob {image=jacobicon} ":
                    jump jacobgameyoo
                " {image=jamicon} Jam {image=jamicon} ":
                    jump jamgameyoo
        elif jacobknow == True and jamknow == False:
            menu:
                " {image=jacobicon} Jacob {image=jacobicon} ":
                    jump jacobgameyoo
                " {image=jamicon} A mean looking girl {image=jamicon} ":
                    jump jamgameyoo
        elif jacobknow == False and jamknow == True:
            menu:
                " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                    jump jacobgameyoo
                " {image=jamicon} Jam {image=jamicon} ":
                    jump jamgameyoo
        else:
            menu:
                " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                    jump jacobgameyoo
                " {image=jamicon} A mean looking girl {image=jamicon} ":
                    jump jamgameyoo
        label jamgameyoo:
            show jamneutral at center with easeinright
            if jamknow == True:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was picking out some flowers... "
                " But for what? "
                ja " ?? "
                ja " Oh, it's just you. "
                ja " Um... "
                ja " Don't tell Mia I picked out her flowers. "
                ja " I just... "
                ja " I just wanted to give these to a certain someone. "
                ja " They looked very pretty... "
                ja " A very pretty person deserves a very pretty gift, right...? "
                ja " Hopefully she'll like this... "
                ja " But then again, "
                ja " She likes anything I get her. "
                ja " But I hope this is going to go fine... "
                " You told her that you were cheering for her. "
                " You hoped for the best for both her and the person she's giving the flowers to. "
                ja " Thank you. "
                ja " I appreciate you...cheering on for me. "
                ja " This is all nerve-wracking.... "
                ja " I know that she'll like the flowers, but... "
                hide jamneutral at bottom
                show jamsad at center
                ja " There's this voice at the back of mind. "
                ja " The voice telling me that everything will go wrong. "
                ja " What if she doesn't like them? "
                ja " What if she makes fun of me for not getting her those fancy ones at the store? "
                ja " I wish I could get her those, but... "
                ja " I don't got any money for her. "
                ja " Sigh... "
                ja " And what if she doesn't even like me in the first place? "
                ja " ... "
                ja " Is this what those movie highschoolers have to deal with when confessing to their crush? "
                ja " Probably. "
                ja " Now I understand why they're so panicked... "
                ja " Hhhhghhh... "
                hide jamsad at bottom
                show jamneutral at center
                " You told her that things will go fine. "
                " Even though her mind is telling her that it won't, "
                " It's going to go fine. "
                " You know that it would. "
                ja " ...If you say so, then... "
                ja " I hope it will. "
                ja " She's really nice, [name]... "
                ja " I wouldn't want to lose her. "
                ja " I wouldn't know what to do if she's gone... "
                " You reassured her that she wouldn't lose her. "
                " You're going to be there to make sure of that. "
                ja " ...You know, that sounds a little weird, but... "
                ja " Kind of reassuring, in a way. "
                ja " Thanks again for listening to me talk. "
                ja " I think I'm having more confidence to talk to her now... "
                " You told her that was good. "
                " You're going to be cheering for them, and cheering hard. "
                ja " Hmhmmm... "
                ja " I should get more flowers for her. "
                ja " Just praying that Mia wouldn't kill me. "
                ja " Praying really hard. "
                scene black with dissolve
                " You spent the rest of the break talking with Jam. "
                " Just talking about how she's going to confess to her crush. "
                " You were going to do everything to make this yuri sail. "
                " Or was it ship? ship sail...? "
                " I have no idea what I'm saying, I'm sorry. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to the gym. "
                pause 2.0
                jump ocpefri
            else:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was picking out some flowers... "
                " But for what? "
                x " ?? "
                x " Oh, it's just you. "
                x " Don't think I've introduced myself to you before, so... "
                $ jamknow = True
                ja " I'm Jam. It's nice to meet you. "
                ja " Um... "
                ja " Don't tell Mia I picked out her flowers. "
                ja " I just... "
                ja " I just wanted to give these to a certain someone. "
                ja " They looked very pretty... "
                ja " A very pretty person deserves a very pretty gift, right...? "
                ja " Hopefully she'll like this... "
                ja " But then again, "
                ja " She likes anything I get her. "
                ja " But I hope this is going to go fine... "
                " You told her that you were cheering for her. "
                " You hoped for the best for both her and the person she's giving the flowers to. "
                ja " Thank you. "
                ja " I appreciate you...cheering on for me. "
                ja " This is all nerve-wracking.... "
                ja " I know that she'll like the flowers, but... "
                hide jamneutral at bottom
                show jamsad at center
                ja " There's this voice at the back of mind. "
                ja " The voice telling me that everything will go wrong. "
                ja " What if she doesn't like them? "
                ja " What if she makes fun of me for not getting her those fancy ones at the store? "
                ja " I wish I could get her those, but... "
                ja " I don't got any money for her. "
                ja " Sigh... "
                ja " And what if she doesn't even like me in the first place? "
                ja " ... "
                ja " Is this what those movie highschoolers have to deal with when confessing to their crush? "
                ja " Probably. "
                ja " Now I understand why they're so panicked... "
                ja " Hhhhghhh... "
                hide jamsad at bottom
                show jamneutral at center
                " You told her that things will go fine. "
                " Even though her mind is telling her that it won't, "
                " It's going to go fine. "
                " You know that it would. "
                ja " ...If you say so, then... "
                ja " I hope it will. "
                ja " She's really nice, [name]... "
                ja " I wouldn't want to lose her. "
                ja " I wouldn't know what to do if she's gone... "
                " You reassured her that she wouldn't lose her. "
                " You're going to be there to make sure of that. "
                ja " ...You know, that sounds a little weird, but... "
                ja " Kind of reassuring, in a way. "
                ja " Thanks again for listening to me talk. "
                ja " I think I'm having more confidence to talk to her now... "
                " You told her that was good. "
                " You're going to be cheering for them, and cheering hard. "
                ja " Hmhmmm... "
                ja " I should get more flowers for her. "
                ja " Just praying that Mia wouldn't kill me. "
                ja " Praying really hard. "
                scene black with dissolve
                " You spent the rest of the break talking with Jam. "
                " Just talking about how she's going to confess to her crush. "
                " You were going to do everything to make this yuri sail. "
                " Or was it ship? ship sail...? "
                " I have no idea what I'm saying, I'm sorry. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to the gym. "
                pause 2.0
                jump ocpefri
        label jacobgameyoo:
            show jacobneutral at center with easeinleft
            if jacobknow == True:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was cleaning his saw on his hand... "
                " Wonder what happened. "
                jac " Oh, uh...you. Hi there. "
                jac " Just cleaning my saw over here... "
                jac " I think you might be wondering why I'm cleaning it right now, but... "
                jac " It's cause I had a little bit of an accident at the cafeteria. "
                jac " As soon as breaktime started before health class... "
                jac " I made my way to the cafeteria to get a snack. "
                jac " Just a burger, nothing too special. "
                jac " And then some guy accidentally spills the ketchup on my saw. "
                jac " Like?? hello?? "
                jac " It isn't that hard to NOT spell the ketchup on me. "
                jac " And right now... "
                jac " I'm kind of struggling to get it off. "
                jac " I did wash it, yes... "
                jac " But I STILL smell the ketchup on it. "
                jac " I do NOT like that. "
                jac " I'm going to have to need mutliple tissues to fully clean this... "
                jac " I don't care how painful it's going to be, "
                jac " I just need to get this clean... "
                " You told him that it looked crystal clean though. "
                " And then you had a thought... "
                " What was he even using this saw for? "
                jac " What do I use this saw for? "
                jac " Mostly basic stuff. "
                jac " Like cutting things like vegetables... "
                jac " And not trees, of course. "
                jac " I'm not that type of guy to ruin nature, actually. "
                jac " And sometimes... "
                jac " The teachers actually make me do things with this saw. "
                jac " Like cutting down specific things for them. "
                jac " It doesn't really bother me. "
                jac " I mean, atleast I have something to do, right? "
                jac " But uh, yeah. "
                jac " Still struggling to get this fully clean. "
                jac " God. This is painful to do. "
                jac " This is gonna take me the entire break to do. "
                jac " ...Probably. "
                " Maybe you could help with this?? "
                jac " I guess you could try to help. "
                scene black with dissolve
                " You spent the rest of the break cleaning Jacob's saw arm with tissues. "
                " Wow, he was right...this was pretty much a pain to do. "
                " But eventually you got everything all clean. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to the gym. "
                pause 2.0
                jump ocpefri
            else:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was cleaning his saw on his hand... "
                " Wonder what happened. "
                x " Oh, uh...you. Hi there. "
                x " Don't think I've met you before, so... "
                $ jacobknow = True
                jac " I'm Jacob, your classmate. "
                jac " Just cleaning my saw over here... "
                jac " I think you might be wondering why I'm cleaning it right now, but... "
                jac " It's cause I had a little bit of an accident at the cafeteria. "
                jac " As soon as breaktime started before health class... "
                jac " I made my way to the cafeteria to get a snack. "
                jac " Just a burger, nothing too special. "
                jac " And then some guy accidentally spills the ketchup on my saw. "
                jac " Like?? hello?? "
                jac " It isn't that hard to NOT spell the ketchup on me. "
                jac " And right now... "
                jac " I'm kind of struggling to get it off. "
                jac " I did wash it, yes... "
                jac " But I STILL smell the ketchup on it. "
                jac " I do NOT like that. "
                jac " I'm going to have to need mutliple tissues to fully clean this... "
                jac " I don't care how painful it's going to be, "
                jac " I just need to get this clean... "
                " You told him that it looked crystal clean though. "
                " And then you had a thought... "
                " What was he even using this saw for? "
                jac " What do I use this saw for? "
                jac " Mostly basic stuff. "
                jac " Like cutting things like vegetables... "
                jac " And not trees, of course. "
                jac " I'm not that type of guy to ruin nature, actually. "
                jac " And sometimes... "
                jac " The teachers actually make me do things with this saw. "
                jac " Like cutting down specific things for them. "
                jac " It doesn't really bother me. "
                jac " I mean, atleast I have something to do, right? "
                jac " But uh, yeah. "
                jac " Still struggling to get this fully clean. "
                jac " God. This is painful to do. "
                jac " This is gonna take me the entire break to do. "
                jac " ...Probably. "
                " Maybe you could help with this?? "
                jac " I guess you could try to help. "
                scene black with dissolve
                " You spent the rest of the break cleaning Jacob's saw arm with tissues. "
                " Wow, he was right...this was pretty much a pain to do. "
                " But eventually you got everything all clean. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to the gym. "
                pause 2.0
                jump ocpefri
    label ocfrigym:
        # disk and temero not interact
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked to the gym and found two of your classmates doing their own things. "
        " Who would you like to talk to? "
        if temeroknow == True and diskknow == True:
            menu:
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump temerotruthwoah
                " {image=diskicon} Disk {image=diskicon} ":
                    jump disktruthwoah
        elif temeroknow == True and diskknow == False:
            menu:
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump temerotruthwoah
                " {image=diskicon} A very energetic guy {image=diskicon} ":
                    jump disktruthwoah
        elif temeroknow == False and diskknow == True:
            menu:
                " {image=temeroicon} An insane scientist looking girl {image=temeroicon} ":
                    jump temerotruthwoah
                " {image=diskicon} Disk {image=diskicon} ":
                    jump disktruthwoah
        else:
            menu:
                " {image=temeroicon} An insane scientist looking girl {image=temeroicon} ":
                    jump temerotruthwoah
                " {image=diskicon} A very energetic guy {image=diskicon} ":
                    jump disktruthwoah
        label temerotruthwoah:
            show temeroneutral at center with easeinleft
            if temeroknow == True:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was busy doing something... "
                tm " Oh hey there!! "
                tm " Sorry that I didn't notice you, hehe. "
                tm " I was just busy taking care of something. "
                tm " So... "
                tm " I'm actually making someting for the school right now! "
                tm " One of the teachers ordered me to make this, hehe. "
                tm " By 'this', I mean a potion! "
                tm " It's a potion to make the school have more flowers and stuff. "
                tm " You could guess who asked me to make this, hehe. "
                tm " It's the gardening teacher! "
                tm " She was really sweet about asking me for this... "
                tm " And she even paid me!! "
                tm " Not much people pay me for making potions, you know. "
                tm " That's why I'm gonna work hard for this! "
                tm " And uh... "
                tm " Not to be rude, but I kind of need complete concentration for this. "
                tm " You can just sit there on the bleachers near me!! "
                tm " Watch as I make something great! "
                tm " As long as you don't bother me, then you're all good. "
                " You took a seat on the bleachers and watched her make her potion. "
                " You wanted to talk to her a bit more... "
                " But you also didn't want to disturb her too much. "
                if temeroformseen == True:
                    " You then remembered something you saw from her. "
                    " After a few minutes, you asked her about her whole butterfly form you saw the other day. "
                    " You were pretty curious about it... "
                    hide temeroneutral at bottom
                    show temerosad at center
                    tm " ...Hold on, hold on. "
                    tm " You're telling me you saw me like that? "
                    tm " Ah hell nah... "
                    tm " Guess I'm gonna have to explain to you how I got like that. "
                    tm " I know you deserve the truth, [name]. "
                    tm " You don't deserve any lies. "
                    tm " So, let me be honest about this. "
                    tm " Okay, deep breaths, Temero... "
                    tm " Let me go back to when I first got my powers and shit. "
                    tm " Back then, I had a normal childhood. "
                    tm " Pretty neat, right? "
                    tm " It's not gonna be like that soon. "
                    tm " When my biological parents saw how smart I was... "
                    tm " They sent me to a lab - maybe I could use my smarts over there. "
                    tm " And guess what those scientists did. "
                    tm " They didn't actually get me to help them... "
                    tm " But what they DID do was test on me. "
                    tm " Test on me for multiple things. "
                    tm " They told me that I was too smart for my own good... "
                    tm " So surely, I would be able to get out of certain testing situations...right? "
                    tm " Wrong. I almost died multiple times there. "
                    tm " Thankfully, one of the other experiments there had a breakout and I managed to escape. "
                    tm " First few days of being out...I had to wear a gas mask. "
                    tm " Due to some testing, I had a few scars on my mouth that I wouldn't want to show. "
                    tm " So I hid them with the mask. "
                    tm " I wandered around for a bit...and due to all the tests I had gone through, I was really weak. "
                    hide temerosad at bottom
                    show temeroneutral at center
                    tm " That was when a pink butterfly came to me. "
                    tm " It said that it would grant me it's power, with a cost... "
                    tm " I would have to kill and eat other humans in order for it to be satisfied. "
                    tm " Otherwise, both me and the butterfly would die. "
                    tm " I would have to eat atleast 2 humans in one month. "
                    tm " It took me awhile to get used to the powers, but I got the hang of it. "
                    tm " I even entered a tournament while I was practicing. "
                    tm " The same tournament where I became friends with Spark. "
                    tm " ...Okay, this is probably way too awkward for you now. "
                    tm " How about you just... "
                    tm " Continue whatever you were doing earlier? "
                    tm " Didn't mean to make you uncomfortable. "
                    scene black with dissolve
                    " You spent the rest of the break watching Temero make her potion. "
                    " And also doing stuff on your phone. "
                    " That story you just heard about her though... "
                    " It sounded really cool, but then again... "
                    " She suffered a whole lot. "
                    " You felt bad for her. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " But you're already in the classroom, so... you just waited for the teacher to arrive. "
                    pause 2.0
                    jump ocpefri
                else:
                    " Nah, you're not gonna bother her. "
                    " Instead, you're just going to game on your phone. "
                    " A good gaming session for the break...absolute peak. "
                    scene black with dissolve
                    " You spent the rest of the break playing games on your phone. "
                    " And you also looked over at what Temero was doing every now and then. "
                    " You were just gaming for most of the break though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " But you're already in the classroom, so... you just waited for the teacher to arrive. "
                    pause 2.0
                    jump ocpefri
            else:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was busy doing something... "
                x " Oh hey there!! "
                x " Sorry that I didn't notice you, hehe. "
                x " Don't think we've met before, actually... "
                $ temeroknow = True
                tm " I'm Temero NEO! Call me Temero or Neo, I don't mind. "
                tm " I was just busy taking care of something. "
                tm " So... "
                tm " I'm actually making someting for the school right now! "
                tm " One of the teachers ordered me to make this, hehe. "
                tm " By 'this', I mean a potion! "
                tm " It's a potion to make the school have more flowers and stuff. "
                tm " You could guess who asked me to make this, hehe. "
                tm " It's the gardening teacher! "
                tm " She was really sweet about asking me for this... "
                tm " And she even paid me!! "
                tm " Not much people pay me for making potions, you know. "
                tm " That's why I'm gonna work hard for this! "
                tm " And uh... "
                tm " Not to be rude, but I kind of need complete concentration for this. "
                tm " You can just sit there on the bleachers near me!! "
                tm " Watch as I make something great! "
                tm " As long as you don't bother me, then you're all good. "
                " You took a seat on the bleachers and watched her make her potion. "
                " You wanted to talk to her a bit more... "
                " But you also didn't want to disturb her too much. "
                " Nah, you're not gonna bother her. "
                " Instead, you're just going to game on your phone. "
                " A good gaming session for the break...absolute peak. "
                scene black with dissolve
                " You spent the rest of the break playing games on your phone. "
                " And you also looked over at what Temero was doing every now and then. "
                " You were just gaming for most of the break though. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " But you're already in the classroom, so... you just waited for the teacher to arrive. "
                pause 2.0
                jump ocpefri
        label disktruthwoah:
            show diskneutral at center with easeinright
            if diskknow == True:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was planning something with that checklist of his... "
                " Wonder what he was planning for though. "
                d " Oh!! hey there, [name]!! "
                d " I'm just soooo excited...!! "
                d " But I bet you're wondering about the checklist I have here! "
                d " You see... "
                d " This checklist is for all of the things I'm going to do for my party tonight! "
                d " I already have everything ready... "
                d " Oh right! "
                d " This checklist if also a thing to make sure that everyone's there! "
                d " If everyone's not there... "
                d " I'd just have to text them to make sure if they're actually going or not. "
                d " Gotta know what happened, after all! "
                d " Let's see here... "
                d " I've already got everything prepared... "
                d " I'm sure the chefs have already cooked everything needed... "
                d " And I'm also sure that the servants have prepared everything... "
                d " Now all that's needed is to wait for school to be over!! "
                hide diskneutral at bottom
                show diskhappy at center
                d " Aaah, I can't wait!! "
                d " I'm so excited, [name]!! "
                d " I know this happens every friday for me, buuut... "
                d " I can't help but get excited, you know? "
                d " Parties are my whole thing! "
                d " I just can't help but be excited! "
                d " Most people wouldn't be able to handle parties on every friday... "
                d " But I would!! "
                d " Hehe... "
                d " It would be fun if you're there, [name]! "
                if diskparty == True:
                    d " Ah, wait...you're already going!! "
                    d " Oops, hehe... "
                else:
                    " You told him that parties weren't really your thing. "
                    d " Oh yeah, right... "
                    d " It's okay though! "
                d " Hmhmmm... "
                d " Hey! While you're here... "
                d " Maybe you could give me some ideas on some games I could do? "
                d " I mean, I already have some ideas, buuut... "
                d " Maybe you have some interesting ideas? "
                d " Only if you want to though! "
                " You were up to giving Disk some ideas. "
                " You were pretty bored, anyway. "
                d " Alrighty!! "
                d " Let's see...here are my current ideas!! "
                scene black with dissolve
                " You spent the rest of the break giving Disk ideas for his party later, "
                " You actually managed to give him ideas that he actually really liked... "
                " Nice one. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for class. "
                " But you're already in the classroom, so... you just waited for the teacher to arrive. "
                pause 2.0
                jump ocpefri
            else:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was planning something with that checklist of his... "
                " Wonder what he was planning for though. "
                x " Oh!! hey there, [name]!! "
                x " I don't know if we've met before, buuut... "
                $ diskknow = True
                d " I'm Disk! It's nice to meet you! "
                d " I'm just soooo excited...!! "
                d " But I bet you're wondering about the checklist I have here! "
                d " You see... "
                d " This checklist is for all of the things I'm going to do for my party tonight! "
                d " I already have everything ready... "
                d " Oh right! "
                d " This checklist if also a thing to make sure that everyone's there! "
                d " If everyone's not there... "
                d " I'd just have to text them to make sure if they're actually going or not. "
                d " Gotta know what happened, after all! "
                d " Let's see here... "
                d " I've already got everything prepared... "
                d " I'm sure the chefs have already cooked everything needed... "
                d " And I'm also sure that the servants have prepared everything... "
                d " Now all that's needed is to wait for school to be over!! "
                hide diskneutral at bottom
                show diskhappy at center
                d " Aaah, I can't wait!! "
                d " I'm so excited, [name]!! "
                d " I know this happens every friday for me, buuut... "
                d " I can't help but get excited, you know? "
                d " Parties are my whole thing! "
                d " I just can't help but be excited! "
                d " Most people wouldn't be able to handle parties on every friday... "
                d " But I would!! "
                d " Hehe... "
                d " It would be fun if you're there, [name]! "
                if diskparty == True:
                    d " Ah, wait...you're already going!! "
                    d " Oops, hehe... "
                else:
                    " You told him that parties weren't really your thing. "
                    d " Oh yeah, right... "
                    d " It's okay though! "
                d " Hmhmmm... "
                d " Hey! While you're here... "
                d " Maybe you could give me some ideas on some games I could do? "
                d " I mean, I already have some ideas, buuut... "
                d " Maybe you have some interesting ideas? "
                d " Only if you want to though! "
                " You were up to giving Disk some ideas. "
                " You were pretty bored, anyway. "
                d " Alrighty!! "
                d " Let's see...here are my current ideas!! "
                scene black with dissolve
                " You spent the rest of the break giving Disk ideas for his party later, "
                " You actually managed to give him ideas that he actually really liked... "
                " Nice one. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for class. "
                " But you're already in the classroom, so... you just waited for the teacher to arrive. "
                pause 2.0
                jump ocpefri
    label ocfricafeteria:
        # koa and carmen not interact
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked into the cafeteria and spotted two of your classmates just doing their own things. "
        " Who would you like to talk to? "
        if koaknow == True and carmenknow == True:
            menu:
                " {image=koaicon} Koa {image=koaicon} ":
                    jump koapookiebearwoah
                " {image=carmenicon} Carmen {image=carmenicon} ":
                    jump carmenpookiebearwoah
        elif koaknow == True and carmenknow == False:
            menu:
                " {image=koaicon} Koa {image=koaicon} ":
                    jump koapookiebearwoah
                " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                    jump carmenpookiebearwoah
        elif koaknow == False and carmenknow == True:
            menu:
                " {image=koaicon} An emo guy {image=koaicon} ":
                    jump koapookiebearwoah
                " {image=carmenicon} Carmen {image=carmenicon} ":
                    jump carmenpookiebearwoah
        else:
            menu:
                " {image=koaicon} An emo guy {image=koaicon} ":
                    jump koapookiebearwoah
                " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                    jump carmenpookiebearwoah
        label koapookiebearwoah:
            show koaneutral at center with easeinleft
            if koaknow == True:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was thinking about something... "
                " And he was thinking about it really hard, from what you could tell. "
                k " Hm? oh, [name]. "
                k " Sorry, I was just thinking about something. "
                k " You see... "
                k " I have three siblings. "
                k " And I was wondering... "
                k " Maybe I should get them something nice. "
                k " I care for them a lot, and I really want to get them something nice. "
                k " The only problem is that I don't have much money. "
                " You told him that you could give him some of yours. "
                " You didn't mind sharing some money with him. "
                k " No, you can keep it. "
                k " I appreciate it, but I can figure out another way to get money. "
                k " Hmmhmm... "
                " After a little bit of more thinking... "
                " He pulled out his phone and started to look at the photos he had. "
                " You were looking a little bit, too. "
                " Though you were trying to not make it obvious that you were looking. "
                " ...You were failing pretty bad at that. "
                " But, after a bit of scrolling that he did... "
                hide koaneutral at bottom
                show koasurprised at center
                " You saw a photo of him in a princess outfit. "
                " He tried to scroll away but you managed to keep the photo in place. "
                " You asked him about it. "
                k " Uh... "
                hide koasurprised at bottom
                show koaneutral at center
                k " ...Well, let me explain... "
                k " One of my siblings were bored. "
                k " Annd... "
                k " They said they wanted a princess party with me. "
                k " Of course I had to disagree... "
                k " I'm not exactly comfortable in princess outfits. "
                k " But, they kept on insisting, annnd... "
                k " That's how that photo got there. "
                k " I actually don't remember taking this photo... "
                k " Must've been one of them taking a photo of me in a fit like that. "
                k " I know Orchid would laugh so hard if they saw this... "
                k " Best to just not show him my photos in the first place. "
                k " I don't want to get TOO embarrassed. "
                k " Another thing if Orchid saw that photo... "
                k " He would most definitely use that as blackmail on me. "
                k " Just for fun, of course. "
                k " But still... "
                k " ...Sigh. The things I do for my siblings... "
                k " I care about them though. "
                k " I just couldn't resist their cute eyes... "
                scene black with dissolve
                " You spent the rest of the break talking with Koa. "
                " You thought you'd never live to see the day of Koa wearing a princess outfit, but... "
                " Here you are. And it's funny as hell. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out fo the cafeteria and went to your classroom. "
                pause 2.0
                jump ocpefri
            else:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was thinking about something... "
                " And he was thinking about it really hard, from what you could tell. "
                x " Hm? oh, [name]. "
                x " Sorry, I was just thinking about something. "
                $ koaknow = True
                k " I'm Koa, it's nice to meet you. "
                k " And the thing I was talking about? well, you see... "
                k " I have three siblings. "
                k " And I was wondering... "
                k " Maybe I should get them something nice. "
                k " I care for them a lot, and I really want to get them something nice. "
                k " The only problem is that I don't have much money. "
                " You told him that you could give him some of yours. "
                " You didn't mind sharing some money with him. "
                k " No, you can keep it. "
                k " I appreciate it, but I can figure out another way to get money. "
                k " Hmmhmm... "
                " After a little bit of more thinking... "
                " He pulled out his phone and started to look at the photos he had. "
                " You were looking a little bit, too. "
                " Though you were trying to not make it obvious that you were looking. "
                " ...You were failing pretty bad at that. "
                " But, after a bit of scrolling that he did... "
                hide koaneutral at bottom
                show koasurprised at center
                " You saw a photo of him in a princess outfit. "
                " He tried to scroll away but you managed to keep the photo in place. "
                " You asked him about it. "
                k " Uh... "
                hide koasurprised at bottom
                show koaneutral at center
                k " ...Well, let me explain... "
                k " One of my siblings were bored. "
                k " Annd... "
                k " They said they wanted a princess party with me. "
                k " Of course I had to disagree... "
                k " I'm not exactly comfortable in princess outfits. "
                k " But, they kept on insisting, annnd... "
                k " That's how that photo got there. "
                k " I actually don't remember taking this photo... "
                k " Must've been one of them taking a photo of me in a fit like that. "
                k " I know Orchid would laugh so hard if they saw this... "
                k " Best to just not show him my photos in the first place. "
                k " I don't want to get TOO embarrassed. "
                k " Another thing if Orchid saw that photo... "
                k " He would most definitely use that as blackmail on me. "
                k " Just for fun, of course. "
                k " But still... "
                k " ...Sigh. The things I do for my siblings... "
                k " I care about them though. "
                k " I just couldn't resist their cute eyes... "
                scene black with dissolve
                " You spent the rest of the break talking with Koa. "
                " You thought you'd never live to see the day of Koa wearing a princess outfit, but... "
                " Here you are. And it's funny as hell. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out fo the cafeteria and went to your classroom. "
                pause 2.0
                jump ocpefri
        label carmenpookiebearwoah:
            show carmenneutral at center with easeinright
            if carmenknow == True:
                " You walked over to him and asked what he was doing. "
                " He looked like he was staring at something in his food... "
                " You wonder what that was. "
                hide carmenneutral at bottom
                show carmensad at center
                ca " ... "
                " You couldn't tell by his expression, but... "
                " He was clearly concerned about something. "
                " Something that was in his food... "
                " You asked him if he just didn't like the food he picked out. "
                ca " ... "
                " He shook his head. "
                " Then what could be the problem here...? "
                " He then pointed at the food that was on his tray. "
                " It's as if he was asking you to check out his food. "
                " At first, you didn't really see anything wrong... "
                " But when you looked closer - wait... "
                " Hold on, why the hell is there worms? "
                ca " ... "
                " Okay now this is just downright disgusting. "
                " How did worms end up in his food though? "
                " You told him that he should talk about it to the lunch ladies. "
                " There's no way he's going to eat this. "
                ca " ... "
                " He told you that he was too shy to do so. "
                " And he didn't really want to be a bother... "
                " You offered to help him talk to the lunch ladies. "
                " You understood because he couldn't really talk, and...you can. "
                " The lunch ladies might have a hard time talking to them. "
                " Due to the fact that Carmen could just do sign language. "
                " And talking to them with a guitar just sounds weird. "
                ca " ... "
                hide carmensad at bottom
                show carmenneutral at center
                " It took a bit for Carmen to agree, but he eventually did. "
                " And so, you did all the talking for Carmen. "
                " The lunch ladies immediately apologized and gave him another burger. "
                " This time, with no worms or anything. "
                " Carmen looked pretty happy the moment you two got back to his seat. "
                " Finally, he can eat something good... "
                " You even got yourself a snack while you were helping him out. "
                " Nice. "
                scene black with dissolve
                " You spent the rest of the break talking with Carmen. "
                " You still found it insane that there were worms in his food, but... "
                " Atleast that situation was resolved now. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out fo the cafeteria and went to your classroom. "
                pause 2.0
                jump ocpefri
            else:
                " Oh hey, you've seen this kid before. "
                $ carmenknow = True
                " His name is Carmen, and he's mute. He likes to play the guitar a lot. "
                " You walked over to him and asked what he was doing. "
                " He looked like he was staring at something in his food... "
                " You wonder what that was. "
                hide carmenneutral at bottom
                show carmensad at center
                ca " ... "
                " You couldn't tell by his expression, but... "
                " He was clearly concerned about something. "
                " Something that was in his food... "
                " You asked him if he just didn't like the food he picked out. "
                ca " ... "
                " He shook his head. "
                " Then what could be the problem here...? "
                " He then pointed at the food that was on his tray. "
                " It's as if he was asking you to check out his food. "
                " At first, you didn't really see anything wrong... "
                " But when you looked closer - wait... "
                " Hold on, why the hell is there worms? "
                ca " ... "
                " Okay now this is just downright disgusting. "
                " How did worms end up in his food though? "
                " You told him that he should talk about it to the lunch ladies. "
                " There's no way he's going to eat this. "
                ca " ... "
                " He told you that he was too shy to do so. "
                " And he didn't really want to be a bother... "
                " You offered to help him talk to the lunch ladies. "
                " You understood because he couldn't really talk, and...you can. "
                " The lunch ladies might have a hard time talking to them. "
                " Due to the fact that Carmen could just do sign language. "
                " And talking to them with a guitar just sounds weird. "
                ca " ... "
                hide carmensad at bottom
                show carmenneutral at center
                " It took a bit for Carmen to agree, but he eventually did. "
                " And so, you did all the talking for Carmen. "
                " The lunch ladies immediately apologized and gave him another burger. "
                " This time, with no worms or anything. "
                " Carmen looked pretty happy the moment you two got back to his seat. "
                " Finally, he can eat something good... "
                " You even got yourself a snack while you were helping him out. "
                " Nice. "
                scene black with dissolve
                " You spent the rest of the break talking with Carmen. "
                " You still found it insane that there were worms in his food, but... "
                " Atleast that situation was resolved now. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out fo the cafeteria and went to your classroom. "
                pause 2.0
                jump ocpefri
    label ocfrirooftop:
        # orchid and spark interact
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked to the rooftop and spotted two of your classmates talking to eachother. "
        " Wondering what they're talking about, you walked over to them. "
        show orchidneutral at right with easeinleft
        show sparkneutral at left with easeinleft
        if orchidknow == True and sparkknow == True:
            sp " Hi there, [name]. "
            oc " Hiii, [name]!! "
            oc " I was talking to Spark over here about a game that just got popular!! "
            oc " I've been hearing a lot about it lately... "
            oc " And I was thinking... "
            oc " Since Spark has played it a lot from what I've seen, how about I play it with him? "
            oc " From what I've heard, it's a 1 vs all game! "
            sp " It's based off of this creepypasta. "
            sp " A popular one, at that. "
            sp " You know the funny blue hedgehog? "
            oc " Oh! ooooh... "
            oc " So that's why it looked familliar! "
            sp " Yup. "
            sp " Would love to play with you later. "
            oc " Yeah! cause we've gotta go to Disk's party!! "
            sp " Mhmmm...wait. "
            sp " I'm surprised that you want to go to Disk's party now. "
            sp " I remember you not even attending those... "
            oc " Welll... "
            oc " I'm trying to get myself to be more social! "
            oc " And what better way to do that is to go to a party! "
            oc " Hehe...right? "
            sp " Hmm, true. "
            sp " But don't force yourself to socialize too often. "
            sp " If you force yourself... "
            sp " You'd probably go back to that depressing mindset that you had. "
            oc " Oh yeah, true... "
            oc " Thanks for giving me some advice, Spark! "
            sp " No problem, I'm just here to help you. "
            sp " It's nice that you're finally breaking out of your shell. "
            oc " Hehe, I know! "
            oc " It just feels so...refreshing, honestly. "
            sp " I can tell. "
            sp " You look way more happier than you did before. "
            sp " I always saw you trying your best to look happy. "
            sp " Always laughing at our classmates jokes, even though they're not funny... "
            sp " I'm glad you changed for the better. "
            oc " Hehe...honestly, me too! "
            oc " Anyway, let's play after Disk's party, okay? "
            sp " Alrighty, I'll text you when I'm free. "
            scene black with dissolve
            " You spent the rest of the break talking with Spark and Orchid. "
            " That game they were talking about sounds interesting... "
            " Maybe you should check it out later. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and then went to the gym. "
            pause 2.0
            jump ocpefri
        elif orchidknow == True and sparkknow == False:
            x " Hi there, [name]. "
            oc " Hiii, [name]!! "
            $ sparkknow = True
            oc " I was talking to Spark over here about a game that just got popular!! "
            oc " I've been hearing a lot about it lately... "
            oc " And I was thinking... "
            oc " Since Spark has played it a lot from what I've seen, how about I play it with him? "
            oc " From what I've heard, it's a 1 vs all game! "
            sp " It's based off of this creepypasta. "
            sp " A popular one, at that. "
            sp " You know the funny blue hedgehog? "
            oc " Oh! ooooh... "
            oc " So that's why it looked familliar! "
            sp " Yup. "
            sp " Would love to play with you later. "
            oc " Yeah! cause we've gotta go to Disk's party!! "
            sp " Mhmmm...wait. "
            sp " I'm surprised that you want to go to Disk's party now. "
            sp " I remember you not even attending those... "
            oc " Welll... "
            oc " I'm trying to get myself to be more social! "
            oc " And what better way to do that is to go to a party! "
            oc " Hehe...right? "
            sp " Hmm, true. "
            sp " But don't force yourself to socialize too often. "
            sp " If you force yourself... "
            sp " You'd probably go back to that depressing mindset that you had. "
            oc " Oh yeah, true... "
            oc " Thanks for giving me some advice, Spark! "
            sp " No problem, I'm just here to help you. "
            sp " It's nice that you're finally breaking out of your shell. "
            oc " Hehe, I know! "
            oc " It just feels so...refreshing, honestly. "
            sp " I can tell. "
            sp " You look way more happier than you did before. "
            sp " I always saw you trying your best to look happy. "
            sp " Always laughing at our classmates jokes, even though they're not funny... "
            sp " I'm glad you changed for the better. "
            oc " Hehe...honestly, me too! "
            oc " Anyway, let's play after Disk's party, okay? "
            sp " Alrighty, I'll text you when I'm free. "
            scene black with dissolve
            " You spent the rest of the break talking with Spark and Orchid. "
            " That game they were talking about sounds interesting... "
            " Maybe you should check it out later. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and then went to the gym. "
            pause 2.0
            jump ocpefri
        elif orchidknow == False and sparkknow == True:
            sp " Hi there, [name]. "
            x " Hiii, [name]!! "
            $ orchidknow = True
            oc " I'm Orchid! "
            oc " I was talking to Spark over here about a game that just got popular!! "
            oc " I've been hearing a lot about it lately... "
            oc " And I was thinking... "
            oc " Since Spark has played it a lot from what I've seen, how about I play it with him? "
            oc " From what I've heard, it's a 1 vs all game! "
            sp " It's based off of this creepypasta. "
            sp " A popular one, at that. "
            sp " You know the funny blue hedgehog? "
            oc " Oh! ooooh... "
            oc " So that's why it looked familliar! "
            sp " Yup. "
            sp " Would love to play with you later. "
            oc " Yeah! cause we've gotta go to Disk's party!! "
            sp " Mhmmm...wait. "
            sp " I'm surprised that you want to go to Disk's party now. "
            sp " I remember you not even attending those... "
            oc " Welll... "
            oc " I'm trying to get myself to be more social! "
            oc " And what better way to do that is to go to a party! "
            oc " Hehe...right? "
            sp " Hmm, true. "
            sp " But don't force yourself to socialize too often. "
            sp " If you force yourself... "
            sp " You'd probably go back to that depressing mindset that you had. "
            oc " Oh yeah, true... "
            oc " Thanks for giving me some advice, Spark! "
            sp " No problem, I'm just here to help you. "
            sp " It's nice that you're finally breaking out of your shell. "
            oc " Hehe, I know! "
            oc " It just feels so...refreshing, honestly. "
            sp " I can tell. "
            sp " You look way more happier than you did before. "
            sp " I always saw you trying your best to look happy. "
            sp " Always laughing at our classmates jokes, even though they're not funny... "
            sp " I'm glad you changed for the better. "
            oc " Hehe...honestly, me too! "
            oc " Anyway, let's play after Disk's party, okay? "
            sp " Alrighty, I'll text you when I'm free. "
            scene black with dissolve
            " You spent the rest of the break talking with Spark and Orchid. "
            " That game they were talking about sounds interesting... "
            " Maybe you should check it out later. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and then went to the gym. "
            pause 2.0
            jump ocpefri
        else:
            x " Hi there, [name]. "
            x " Hiii, [name]!! "
            $ orchidknow = True
            $ sparkknow = True
            oc " I'm Orchid! "
            oc " I was talking to Spark over here about a game that just got popular!! "
            oc " I've been hearing a lot about it lately... "
            oc " And I was thinking... "
            oc " Since Spark has played it a lot from what I've seen, how about I play it with him? "
            oc " From what I've heard, it's a 1 vs all game! "
            sp " It's based off of this creepypasta. "
            sp " A popular one, at that. "
            sp " You know the funny blue hedgehog? "
            oc " Oh! ooooh... "
            oc " So that's why it looked familliar! "
            sp " Yup. "
            sp " Would love to play with you later. "
            oc " Yeah! cause we've gotta go to Disk's party!! "
            sp " Mhmmm...wait. "
            sp " I'm surprised that you want to go to Disk's party now. "
            sp " I remember you not even attending those... "
            oc " Welll... "
            oc " I'm trying to get myself to be more social! "
            oc " And what better way to do that is to go to a party! "
            oc " Hehe...right? "
            sp " Hmm, true. "
            sp " But don't force yourself to socialize too often. "
            sp " If you force yourself... "
            sp " You'd probably go back to that depressing mindset that you had. "
            oc " Oh yeah, true... "
            oc " Thanks for giving me some advice, Spark! "
            sp " No problem, I'm just here to help you. "
            sp " It's nice that you're finally breaking out of your shell. "
            oc " Hehe, I know! "
            oc " It just feels so...refreshing, honestly. "
            sp " I can tell. "
            sp " You look way more happier than you did before. "
            sp " I always saw you trying your best to look happy. "
            sp " Always laughing at our classmates jokes, even though they're not funny... "
            sp " I'm glad you changed for the better. "
            oc " Hehe...honestly, me too! "
            oc " Anyway, let's play after Disk's party, okay? "
            sp " Alrighty, I'll text you when I'm free. "
            scene black with dissolve
            " You spent the rest of the break talking with Spark and Orchid. "
            " That game they were talking about sounds interesting... "
            " Maybe you should check it out later. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and then went to the gym. "
            pause 2.0
            jump ocpefri
    label ocfrilibrary:
        # nox and quinn not interact
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked to the library and found two of your classmates doing their own things. "
        " Who would you like to talk to? "
        if noxknow == True and quinnknow == True:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump ballsnoxballs
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump ballsquinnballs
        elif noxknow == True and quinnknow == False:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump ballsnoxballs
                " {image=quinnicon} An acting guy {image=quinnicon} ":
                    jump ballsquinnballs
        elif noxknow == False and quinnknow == True:
            menu:
                " {image=noxicon} A sleepy guy {image=noxicon} ":
                    jump ballsnoxballs
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump ballsquinnballs
        else:
            menu:
                " {image=noxicon} A sleepy guy {image=noxicon} ":
                    jump ballsnoxballs
                " {image=quinnicon} An acting guy {image=quinnicon} ":
                    jump ballsquinnballs
        label ballsnoxballs:
            show noxneutral at center with easeinright
            if noxknow == True:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was reading something... "
                " You wonder what he was reading about. "
                n " Hmmm...Hi, [name]... "
                n " Just reading a book about geek mythology... "
                n " It also has a few lesser known gods in here... "
                n " I don't think I've seen anyone talk about Hypnos before... "
                n " I don't know about you, but... "
                n " I think Hypnos is kind of cool... "
                n " I mean, I've seen a few people talking about Hypnos before, but... "
                n " They aren't really that popular, from what I've seen so far... "
                n " *yawn*... "
                n " I honestly didn't think that I would get into greek mythology, but... "
                n " It's kind of... "
                n " Interesting, actually.. "
                n " I quite like it... "
                n " It's not everyones thing, but... "
                n " It certainly is mine, now. "
                n " Hmhmmm... "
                " He continues reading the book silently. "
                " You also took a good read at the book as he was reading. "
                " And he was right, it was pretty interesting. "
                " You could probably read more of these. "
                " All of the things mentioned here sounded pretty cool to you. "
                " Probably terrifying for people in the past, buuut... "
                " Guess it's pretty cool to other people now. "
                n " ...Hmmm... "
                n " Oh, um... "
                n " Did you want to...read with me...? "
                n " I noticed that you were reading a bit... "
                n " It's okay if you were just taking a good look... "
                n " But I wouldn't mind it if you would like to read with me, either... "
                n " In fact, it's nice...to have a reading partner... "
                n " Um... "
                n " It's fine if you were just taking a look though... "
                n " I don't want to bother you... "
                " Well, you could use something top pass the time. "
                " You agreed to read with Nox. "
                n " Oh, um...really..? "
                n " Okay...let me just... "
                " He puts the book in a position where you both can read. "
                " You two started reading... "
                scene black with dissolve
                " You spent the rest of the break reading with Nox. "
                " Every now and then, you and Nox would make a comment about something. "
                " Cool. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the library and then went to the gym. "
                pause 2.0
                jump ocpefri
            else:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was reading something... "
                " You wonder what he was reading about. "
                x " Hmmm...Hi, [name]... "
                x " I don't think I introduced myself yet, hm...let's fix that... "
                $ noxknow = True
                n " I'm Nox...Nox Cesso... "
                n " I was...Just reading a book about geek mythology... "
                n " It also has a few lesser known gods in here... "
                n " I don't think I've seen anyone talk about Hypnos before... "
                n " I don't know about you, but... "
                n " I think Hypnos is kind of cool... "
                n " I mean, I've seen a few people talking about Hypnos before, but... "
                n " They aren't really that popular, from what I've seen so far... "
                n " *yawn*... "
                n " I honestly didn't think that I would get into greek mythology, but... "
                n " It's kind of... "
                n " Interesting, actually.. "
                n " I quite like it... "
                n " It's not everyones thing, but... "
                n " It certainly is mine, now. "
                n " Hmhmmm... "
                " He continues reading the book silently. "
                " You also took a good read at the book as he was reading. "
                " And he was right, it was pretty interesting. "
                " You could probably read more of these. "
                " All of the things mentioned here sounded pretty cool to you. "
                " Probably terrifying for people in the past, buuut... "
                " Guess it's pretty cool to other people now. "
                n " ...Hmmm... "
                n " Oh, um... "
                n " Did you want to...read with me...? "
                n " I noticed that you were reading a bit... "
                n " It's okay if you were just taking a good look... "
                n " But I wouldn't mind it if you would like to read with me, either... "
                n " In fact, it's nice...to have a reading partner... "
                n " Um... "
                n " It's fine if you were just taking a look though... "
                n " I don't want to bother you... "
                " Well, you could use something top pass the time. "
                " You agreed to read with Nox. "
                n " Oh, um...really..? "
                n " Okay...let me just... "
                " He puts the book in a position where you both can read. "
                " You two started reading... "
                scene black with dissolve
                " You spent the rest of the break reading with Nox. "
                " Every now and then, you and Nox would make a comment about something. "
                " Cool. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the library and then went to the gym. "
                pause 2.0
                jump ocpefri
        label ballsquinnballs:
            show quinnneutral at center with easeinleft
            if quinnknow == True:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was busy with doing something. "
                q " Ah, hellot ehre, [name]! "
                q " I'm sorry, but... "
                q " I'm a little busy over here. "
                q " And by busy, I mean doing last minute rehearsals on my own! "
                q " Have to make sure that everything is perfect, after all. "
                q " So... "
                q " I'm going to have full concentration for this. "
                q " And that mneans...I kind of need you out of here. "
                q " Or you could just watch my performance over there on the bleachers! "
                q " Thats actually better for me if you choose to watch. "
                q " Because it would feel like I'm really on stage, performing infront of an audience! "
                q " You can go and sit on the bleachers now. "
                q " I'll get started in a bit! "
                q " Make sure you've got some sort of snack in your pocket for this. "
                " You sat on the bleachers and waited for Quinn to start. "
                " And hey, you got pretty lucky. "
                " There was some left over candy in your pocket for you to eat while watching. "
                " Very nice, very nice... "
                " After a good bit of preparing, Quinn starts performing. "
                " And time for you to watch, too. "
                scene black with dissolve
                " You spent the rest of the break watching Quinn preform. "
                " You could say that it was pretty good, in your opinion. "
                " The chocolate from your pocket tasted pretty good too. "
                " Would be better if it wasn't melted though. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the library and then went to the gym. "
                pause 2.0
                jump ocpefri
            else:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was busy with doing something. "
                x " Ah, hellot ehre, [name]! "
                x " I'm sorry, but... "
                x " I'm a little busy over here. "
                x " And by busy, I mean doing last minute rehearsals on my own! "
                x " Have to make sure that everything is perfect, after all. "
                x " So... "
                x " I'm going to have full concentration for this. "
                x " And that mneans...I kind of need you out of here. "
                x " Or you could just watch my performance over there on the bleachers! "
                x " Thats actually better for me if you choose to watch. "
                x " Because it would feel like I'm really on stage, performing infront of an audience! "
                x " You can go and sit on the bleachers now. "
                x " I'll get started in a bit! "
                x " Make sure you've got some sort of snack in your pocket for this. "
                " You sat on the bleachers and waited for him to start. "
                " And hey, you got pretty lucky. "
                " There was some left over candy in your pocket for you to eat while watching. "
                " Very nice, very nice... "
                " After a good bit of preparing, the boy starts performing. "
                " And time for you to watch, too. "
                scene black with dissolve
                " You spent the rest of the break watching him preform. "
                " You could say that it was pretty good, in your opinion. "
                " The chocolate from your pocket tasted pretty good too. "
                " Would be better if it wasn't melted though. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the library and then went to the gym. "
                pause 2.0
                jump ocpefri

label ocpefri:
    scene gym with dissolve
    " Looks like the PE teacher is already there. "
    " Something looks wrong with his knee... "
    " Let's see what's going to happen. "
    show solneutral at center with easeinleft
    msso " Hello, class! "
    msso " So, unfortunately... "
    msso " Due to me having an accident in the hallways... "
    msso " I'm not going to do the planned activity I had. "
    msso " But, I have another activity for you! "
    msso " How about...we do some... "
    hide solneutral at bottom
    show solhappy at center
    msso " DODGEBALL!! " with vpunch
    msso " It's been awhile since we've done this, right? "
    msso " I'm gonna have to stay out of this though. "
    msso " Don't want to injure my leg even more now!! "
    msso " I'll be watching on the bleachers, alright? "
    msso " Make sure not to play too rough now! "
    msso " The team who wins gets +50 points! "
    msso " The losing team gets +30! "
    scene black with dissolve
    " You played dodgeball for your PE class. "
    " Somehow, your team won. "
    " Nice, you get +50 points. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for another break. "
    " You waited for everyone to get out of the classroom before you did. "
    pause 2.0
    jump ocfribreak3

label ocfribreak3:
    scene hallway with dissolve
    " Looks like it's time for you to hangout somewhere else. "
    " Where do you wanna go? "
    menu:
        " {image=orchidicon} The front of the school {image=temeroicon} ":
            jump ocfrifront3
        " {image=matteicon} The back of the school {image=yinyangicon} ":
            jump ocfriback3
        " {image=noxicon} The gym (again) {image=jamicon} ":
            jump ocfrigym3
        " {image=diskicon} The cafeteria {image=carmenicon} ":
            jump ocfricafeteria3
        " {image=jacobicon} The rooftop {image=quinnicon} ":
            jump ocfrirooftop3
        " {image=sparkicon} The library {image=koaicon} ":
            jump ocfrilibrary3
    label ocfrifront3:
        # orchid and temero
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked to the front of the school and spotted two of your classmates doing their own things. "
        " Who would you like to talk to for this break? "
        if orchidknow == True and temeroknow == True:
            menu:
                " {image=orchidicon} Orchid {image=orchidicon} ":
                    jump orchidscene
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump temeroscene
        elif orchidknow == True and temeroknow == False:
            menu:
                " {image=orchidicon} Orchid {image=orchidicon} ":
                    jump orchidscene
                " {image=temeroicon} A scientist kid {image=temeroicon} ":
                    jump temeroscene
        elif orchidknow == False and temeroknow == True:
            menu:
                " {image=orchidicon} A scene kid {image=orchidicon} ":
                    jump orchidscene
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump temeroscene
        else:
            menu:
                " {image=orchidicon} A scene kid {image=orchidicon} ":
                    jump orchidscene
                " {image=temeroicon} A scientist kid {image=temeroicon} ":
                    jump temeroscene
        label orchidscene:
            show orchidneutral at center with easeinleft
            if orchidknow == True:
                " You walked over to them and asked them what they were doing. "
                oc " Oh hey there, [name]!! "
                oc " I was just taking a good look at the flowers... "
                oc " And also taking a breather! "
                oc " You know... "
                oc " This week has been the best! "
                oc " I rarely even say that, ehe. "
                oc " Infact, I've never even said that before. "
                oc " I've always wanted the week to just end... "
                oc " So that I could just rot in my bed for the rest of the weekend... "
                oc " But right now? "
                oc " I'm actually learning to appreciate the little things in life! "
                oc " A fun fact about me... "
                hide orchidneutral at bottom
                show orchidsad at center
                oc " Well, not so fun fact the more I think about it now. "
                oc " I usually just kept myself in my room most of the time. "
                oc " Not going out to eat, just to game here and there... "
                oc " And also to rot in my bed for hours. "
                oc " Then my mom decided that I should go here. "
                oc " At first, I was very nervous. "
                oc " It had been awhile since I had gone to school. "
                oc " I honestly didn't know what to do there. "
                oc " I knew that I had to learn there, but... "
                oc " What about the whole making friends thing? "
                oc " I wasn't really the best at socializing. "
                oc " I was actually so worried about my appearance, first day of school. "
                oc " I didn't wear the same stuff I'm wearing right now! "
                oc " I dressed up all emo and stuff... "
                oc " I thought no one would really talk to me. "
                oc " I mean, sure, everyone is nice, but... "
                oc " I never really got to form an actual connection with them. "
                oc " But then, the person who changed my life came in. "
                hide orchidsad at bottom
                show orchidneutral at center
                oc " I think you know who it is, considering I hang out with him a lot! "
                hide orchidneutral at bottom
                show orchidhappy at center
                oc " It's my boy, Koaaaa!! "
                oc " I'm really glad he stepped into my life. "
                oc " Otherwise, I don't think I could've reached this amount of happiness. "
                hide orchidhappy at bottom
                show orchidneutral at center
                oc " I haven't felt this happy in...forever, honestly. "
                oc " It's refreshing to feel something like this again. "
                oc " Oh, right...since you're here! "
                oc " You wanna just...sit on the ground and talk for a bit? "
                oc " My old self would've probably just left you alone, but, hehe... "
                oc " I've grown from that. "
                oc " Only if you want to hangout with me of course! "
                oc " Don't want to force you into anything. "
                " Well, you could use a little yapping session right now. "
                " You pointed at a spot you and Orchid could sit at and went over there. "
                oc " Alrighty! "
                oc " Now I actually have some stories for me to tell! "
                oc " So, back in the day... "
                scene black with dissolve
                " You spent the rest of the break talking with Orchid. "
                " Just talking about the games that he likes... "
                " Pretty chill, if you ask me. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into your school and went to your classroom. "
                pause 2.0
                jump ocgardeningfri
            else:
                " You walked over to them and asked them what they were doing. "
                x " Oh hey there, [name]!! "
                x " Don't think we've met before, hmm... "
                $ orchidknow = True
                oc " I'm Orchid, it's nice to meet you! "
                oc " I was just taking a good look at the flowers... "
                oc " And also taking a breather! "
                oc " You know... "
                oc " This week has been the best! "
                oc " I rarely even say that, ehe. "
                oc " Infact, I've never even said that before. "
                oc " I've always wanted the week to just end... "
                oc " So that I could just rot in my bed for the rest of the weekend... "
                oc " But right now? "
                oc " I'm actually learning to appreciate the little things in life! "
                oc " A fun fact about me... "
                hide orchidneutral at bottom
                show orchidsad at center
                oc " Well, not so fun fact the more I think about it now. "
                oc " I usually just kept myself in my room most of the time. "
                oc " Not going out to eat, just to game here and there... "
                oc " And also to rot in my bed for hours. "
                oc " Then my mom decided that I should go here. "
                oc " At first, I was very nervous. "
                oc " It had been awhile since I had gone to school. "
                oc " I honestly didn't know what to do there. "
                oc " I knew that I had to learn there, but... "
                oc " What about the whole making friends thing? "
                oc " I wasn't really the best at socializing. "
                oc " I was actually so worried about my appearance, first day of school. "
                oc " I didn't wear the same stuff I'm wearing right now! "
                oc " I dressed up all emo and stuff... "
                oc " I thought no one would really talk to me. "
                oc " I mean, sure, everyone is nice, but... "
                oc " I never really got to form an actual connection with them. "
                oc " But then, the person who changed my life came in. "
                hide orchidsad at bottom
                show orchidneutral at center
                oc " I think you know who it is, considering I hang out with him a lot! "
                hide orchidneutral at bottom
                show orchidhappy at center
                oc " It's my boy, Koaaaa!! "
                oc " I'm really glad he stepped into my life. "
                oc " Otherwise, I don't think I could've reached this amount of happiness. "
                hide orchidhappy at bottom
                show orchidneutral at center
                oc " I haven't felt this happy in...forever, honestly. "
                oc " It's refreshing to feel something like this again. "
                oc " Oh, right...since you're here! "
                oc " You wanna just...sit on the ground and talk for a bit? "
                oc " My old self would've probably just left you alone, but, hehe... "
                oc " I've grown from that. "
                oc " Only if you want to hangout with me of course! "
                oc " Don't want to force you into anything. "
                " Well, you could use a little yapping session right now. "
                " You pointed at a spot you and Orchid could sit at and went over there. "
                oc " Alrighty! "
                oc " Now I actually have some stories for me to tell! "
                oc " So, back in the day... "
                scene black with dissolve
                " You spent the rest of the break talking with Orchid. "
                " Just talking about the games that he likes... "
                " Pretty chill, if you ask me. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into your school and went to your classroom. "
                pause 2.0
                jump ocgardeningfri
        label temeroscene:
            show temeroneutral at center with easeinright
            if temeroknow == True:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was testing out a potion of sorts... "
                tm " Hi there, [name]! "
                tm " I was just testing this new potion I made! "
                tm " You see... "
                tm " Miss Wisteria actually asked me to make a potion that can make flowers. "
                tm " Now that I've sent a few copies of this potion over to her... "
                tm " I'm free to do whatever I want with this now! "
                tm " I've been testing it out with my other potions... "
                tm " Like this one that can make it explode! "
                tm " By it, I mean the flowers, hehe. "
                tm " Watch this! "
                " Temero pours some of the potion onto the flower... "
                " And it makes a tiny little explosion of flowers. "
                tm " It's not too special, really. "
                tm " Could use a little more effects here and there... "
                tm " Then again, this would also be great for graduation things! "
                tm " You know, where you walk up on the stage and suddenly flowers are being thrown all around you... "
                tm " That mixed with the feeling of freshly getting out of highschool must feel wonderful! "
                tm " Don't you think so, [name]? "
                tm " ...Gee, now that we're talking about graduation and stuff... "
                tm " It's kind of baffling that in a few years, we're all gonna graduate. "
                tm " Then we gotta get jobs and all that... "
                tm " And basically just start our own lives. "
                tm " It's baffling, it truly is. "
                tm " But it has to happen at some point, doesn't it? "
                " You nodded in agreement. "
                " Thinking about graduation already is starting to make you feel a little... "
                " Nostalgic, for some reason. "
                " Maybe you should talk to her about something else. "
                " You asked her if she had any other potion ideas in her head. "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " Of course I do! "
                tm " I always have ideas in my head. "
                tm " The ideas just keep pouring in, you know? "
                tm " Can't rest when there's so many things we haven't discovered yet! "
                tm " And by so many... "
                tm " I really mean it!! "
                tm " Like for all I know, there could be life on mars! "
                tm " The scientists just aren't telling us the truth! "
                tm " And if we go there...who KNOWS how many breakthroughs we can get! "
                tm " Ohohoooo... "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " But for now, I'll stick with exploring the earth. "
                tm " And I'll explore until there's nothing left for me to study! "
                scene black with dissolve
                " You spent the rest of the break talking with Temero. "
                " Just talking to her about her projects... "
                " Nothing too special, really. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and went into your classroom. "
                pause 2.0
                jump ocgardeningfri
            else:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was testing out a potion of sorts... "
                x " Hi there, [name]! "
                x " Don't think I've introduced myself to ya before... "
                $ temeroknow = True
                tm " I'm Temero! Temero Neo! just call me Temero or Neo though, I don't mind. "
                tm " I was just testing this new potion I made! "
                tm " You see... "
                tm " Miss Wisteria actually asked me to make a potion that can make flowers. "
                tm " Now that I've sent a few copies of this potion over to her... "
                tm " I'm free to do whatever I want with this now! "
                tm " I've been testing it out with my other potions... "
                tm " Like this one that can make it explode! "
                tm " By it, I mean the flowers, hehe. "
                tm " Watch this! "
                " Temero pours some of the potion onto the flower... "
                " And it makes a tiny little explosion of flowers. "
                tm " It's not too special, really. "
                tm " Could use a little more effects here and there... "
                tm " Then again, this would also be great for graduation things! "
                tm " You know, where you walk up on the stage and suddenly flowers are being thrown all around you... "
                tm " That mixed with the feeling of freshly getting out of highschool must feel wonderful! "
                tm " Don't you think so, [name]? "
                tm " ...Gee, now that we're talking about graduation and stuff... "
                tm " It's kind of baffling that in a few years, we're all gonna graduate. "
                tm " Then we gotta get jobs and all that... "
                tm " And basically just start our own lives. "
                tm " It's baffling, it truly is. "
                tm " But it has to happen at some point, doesn't it? "
                " You nodded in agreement. "
                " Thinking about graduation already is starting to make you feel a little... "
                " Nostalgic, for some reason. "
                " Maybe you should talk to her about something else. "
                " You asked her if she had any other potion ideas in her head. "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " Of course I do! "
                tm " I always have ideas in my head. "
                tm " The ideas just keep pouring in, you know? "
                tm " Can't rest when there's so many things we haven't discovered yet! "
                tm " And by so many... "
                tm " I really mean it!! "
                tm " Like for all I know, there could be life on mars! "
                tm " The scientists just aren't telling us the truth! "
                tm " And if we go there...who KNOWS how many breakthroughs we can get! "
                tm " Ohohoooo... "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " But for now, I'll stick with exploring the earth. "
                tm " And I'll explore until there's nothing left for me to study! "
                scene black with dissolve
                " You spent the rest of the break talking with Temero. "
                " Just talking to her about her projects... "
                " Nothing too special, really. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and went into your classroom. "
                pause 2.0
                jump ocgardeningfri
    label ocfriback3:
        # matte and yinhui
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of the school and spotted two of your classmates talking to eachother. "
        " Wondering what they're talking about, you walk over to them. "
        show matteneutral at right with easeinleft
        show yinhuineutral at left with easeinleft
        if matteknow == True and yinhuiknow == True:
            " You asked them what they were talking about politely. "
            ma " Oh, hey there [name]! "
            yi " You know [them]? "
            hide matteneutral at bottom
            show mattehappy at center
            ma " Yup yup! "
            ma " I've talked to [them] a few times now! "
            yi " Hm. "
            hide mattehappy at bottom
            show matteneutral at center
            ma " Anyway, me and Yinhui were just talking about a few things! "
            yi " Mainly stuff for the next class. "
            yi " Just...wanted to learn about some specific plants. "
            ma " That, and the fact he wanted to know how to take care of plants better! "
            hide yinhuineutral at bottom
            show yinhuisurprised at left
            yi " ...!!! "
            yi " (She was NOT supposed to say that.) "
            yi " (Keep yourself calm, Yinhui...) "
            yi " (You can't be crashing out over something like this.) "
            yi " (And you ESPECIALLY can't crashout to a woman.) "
            yi " (Mom would kill you if that happened.) "
            yi " (And you wouldn't want to get killed, right?) "
            hide yinhuisurprised at bottom
            show yinhuineutral at left
            ma " As I was saying! "
            ma " I remember this one time in gardening class... "
            ma " We had to take care of a plant! "
            ma " We all got our own individual plants to take care of, given by Miss Wisteria... "
            ma " And after a week, Miss Wisteria found that Yinhui had accidentally broken his pot! "
            ma " Nobody knows about this except me, buuut... "
            ma " Yinhui felt really bad about it and tried his best to apologize to Miss Wisteria! "
            ma " Even though Miss Wisteria told him that it was okay and that mistakes happen. "
            yi " ...I felt guilty. "
            yi " I didn't expect myself to feel guilty over a plant. "
            ma " Hehe, well... "
            ma " Sometimes we feel the most unexpected things! "
            ma " Like love, for example! "
            ma " And another example is your love for that plant! "
            yi " I didn't say anything about loving it. "
            yi " I just thought about how long Miss Wisteria must've bought for the pot... "
            yi " And the seeds too. "
            yi " I bet it costed a lot... "
            ma " Oh, not at all, actually! "
            ma " It's actually quite cheap! "
            yi " Not cheap if you buy a lot of it. "
            yi " Money is still money... "
            ma " Huh, okay... "
            ma " (Yinhui's family really does care about price...) "
            ma " (But he IS right!) "
            ma " (Money is still money...) "
            ma " (Even if you can just replace the pot or something.) "
            scene black with dissolve
            " You spent the rest of the break talking with Matte and Yinhui. "
            " Just talking about plants and stuff... "
            " Nothing too special in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump ocgardeningfri
        elif matteknow == True and yinhuiknow == False:
            " You asked them what they were talking about politely. "
            ma " Oh, hey there [name]! "
            x " You know [them]? "
            hide matteneutral at bottom
            show mattehappy at center
            ma " Yup yup! "
            ma " I've talked to [them] a few times now! "
            x " Hm. "
            hide mattehappy at bottom
            show matteneutral at center
            ma " Anyway, me and Yinhui were just talking about a few things! "
            x " Mainly stuff for the next class. "
            x " Just...wanted to learn about some specific plants. "
            ma " That, and the fact he wanted to know how to take care of plants better! "
            hide yinhuineutral at bottom
            show yinhuisurprised at left
            x " ...!!! "
            x " (She was NOT supposed to say that.) "
            $ yinhuiknow = True
            yi " (Keep yourself calm, Yinhui...) "
            yi " (You can't be crashing out over something like this.) "
            yi " (And you ESPECIALLY can't crashout to a woman.) "
            yi " (Mom would kill you if that happened.) "
            yi " (And you wouldn't want to get killed, right?) "
            hide yinhuisurprised at bottom
            show yinhuineutral at left
            ma " As I was saying! "
            ma " I remember this one time in gardening class... "
            ma " We had to take care of a plant! "
            ma " We all got our own individual plants to take care of, given by Miss Wisteria... "
            ma " And after a week, Miss Wisteria found that Yinhui had accidentally broken his pot! "
            ma " Nobody knows about this except me, buuut... "
            ma " Yinhui felt really bad about it and tried his best to apologize to Miss Wisteria! "
            ma " Even though Miss Wisteria told him that it was okay and that mistakes happen. "
            yi " ...I felt guilty. "
            yi " I didn't expect myself to feel guilty over a plant. "
            ma " Hehe, well... "
            ma " Sometimes we feel the most unexpected things! "
            ma " Like love, for example! "
            ma " And another example is your love for that plant! "
            yi " I didn't say anything about loving it. "
            yi " I just thought about how long Miss Wisteria must've bought for the pot... "
            yi " And the seeds too. "
            yi " I bet it costed a lot... "
            ma " Oh, not at all, actually! "
            ma " It's actually quite cheap! "
            yi " Not cheap if you buy a lot of it. "
            yi " Money is still money... "
            ma " Huh, okay... "
            ma " (Yinhui's family really does care about price...) "
            ma " (But he IS right!) "
            ma " (Money is still money...) "
            ma " (Even if you can just replace the pot or something.) "
            scene black with dissolve
            " You spent the rest of the break talking with Matte and Yinhui. "
            " Just talking about plants and stuff... "
            " Nothing too special in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump ocgardeningfri
        elif matteknow == False and yinhuiknow == True:
            " You asked them what they were talking about politely. "
            x " Oh, hey there [name]! "
            yi " You know [them]? "
            hide matteneutral at bottom
            show mattehappy at center
            x " Actually, nah...I just know [them] as our classmate! "
            yi " You should probably introduce yourself then. "
            x " Okay! "
            $ matteknow = True
            ma " I'm Matte! It's nice to meet you! "
            hide mattehappy at bottom
            show matteneutral at center
            ma " Me and Yinhui were just talking about a few things! "
            yi " Mainly stuff for the next class. "
            yi " Just...wanted to learn about some specific plants. "
            ma " That, and the fact he wanted to know how to take care of plants better! "
            hide yinhuineutral at bottom
            show yinhuisurprised at left
            yi " ...!!! "
            yi " (She was NOT supposed to say that.) "
            yi " (Keep yourself calm, Yinhui...) "
            yi " (You can't be crashing out over something like this.) "
            yi " (And you ESPECIALLY can't crashout to a woman.) "
            yi " (Mom would kill you if that happened.) "
            yi " (And you wouldn't want to get killed, right?) "
            hide yinhuisurprised at bottom
            show yinhuineutral at left
            ma " As I was saying! "
            ma " I remember this one time in gardening class... "
            ma " We had to take care of a plant! "
            ma " We all got our own individual plants to take care of, given by Miss Wisteria... "
            ma " And after a week, Miss Wisteria found that Yinhui had accidentally broken his pot! "
            ma " Nobody knows about this except me, buuut... "
            ma " Yinhui felt really bad about it and tried his best to apologize to Miss Wisteria! "
            ma " Even though Miss Wisteria told him that it was okay and that mistakes happen. "
            yi " ...I felt guilty. "
            yi " I didn't expect myself to feel guilty over a plant. "
            ma " Hehe, well... "
            ma " Sometimes we feel the most unexpected things! "
            ma " Like love, for example! "
            ma " And another example is your love for that plant! "
            yi " I didn't say anything about loving it. "
            yi " I just thought about how long Miss Wisteria must've bought for the pot... "
            yi " And the seeds too. "
            yi " I bet it costed a lot... "
            ma " Oh, not at all, actually! "
            ma " It's actually quite cheap! "
            yi " Not cheap if you buy a lot of it. "
            yi " Money is still money... "
            ma " Huh, okay... "
            ma " (Yinhui's family really does care about price...) "
            ma " (But he IS right!) "
            ma " (Money is still money...) "
            ma " (Even if you can just replace the pot or something.) "
            scene black with dissolve
            " You spent the rest of the break talking with Matte and Yinhui. "
            " Just talking about plants and stuff... "
            " Nothing too special in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump ocgardeningfri
        else:
            " You asked them what they were talking about politely. "
            x " Oh, hey there [name]! "
            x " You know [them]? "
            hide matteneutral at bottom
            show mattehappy at center
            x " Actually, nah...I just know [them] as our classmate! "
            x " You should probably introduce yourself then. "
            x " Okay! "
            $ matteknow = True
            ma " I'm Matte! It's nice to meet you! "
            hide mattehappy at bottom
            show matteneutral at center
            ma " Me and Yinhui were just talking about a few things! "
            x " Mainly stuff for the next class. "
            x " Just...wanted to learn about some specific plants. "
            ma " That, and the fact he wanted to know how to take care of plants better! "
            hide yinhuineutral at bottom
            show yinhuisurprised at left
            x " ...!!! "
            x " (She was NOT supposed to say that.) "
            $ yinhuiknow = True
            yi " (Keep yourself calm, Yinhui...) "
            yi " (You can't be crashing out over something like this.) "
            yi " (And you ESPECIALLY can't crashout to a woman.) "
            yi " (Mom would kill you if that happened.) "
            yi " (And you wouldn't want to get killed, right?) "
            hide yinhuisurprised at bottom
            show yinhuineutral at left
            ma " As I was saying! "
            ma " I remember this one time in gardening class... "
            ma " We had to take care of a plant! "
            ma " We all got our own individual plants to take care of, given by Miss Wisteria... "
            ma " And after a week, Miss Wisteria found that Yinhui had accidentally broken his pot! "
            ma " Nobody knows about this except me, buuut... "
            ma " Yinhui felt really bad about it and tried his best to apologize to Miss Wisteria! "
            ma " Even though Miss Wisteria told him that it was okay and that mistakes happen. "
            yi " ...I felt guilty. "
            yi " I didn't expect myself to feel guilty over a plant. "
            ma " Hehe, well... "
            ma " Sometimes we feel the most unexpected things! "
            ma " Like love, for example! "
            ma " And another example is your love for that plant! "
            yi " I didn't say anything about loving it. "
            yi " I just thought about how long Miss Wisteria must've bought for the pot... "
            yi " And the seeds too. "
            yi " I bet it costed a lot... "
            ma " Oh, not at all, actually! "
            ma " It's actually quite cheap! "
            yi " Not cheap if you buy a lot of it. "
            yi " Money is still money... "
            ma " Huh, okay... "
            ma " (Yinhui's family really does care about price...) "
            ma " (But he IS right!) "
            ma " (Money is still money...) "
            ma " (Even if you can just replace the pot or something.) "
            scene black with dissolve
            " You spent the rest of the break talking with Matte and Yinhui. "
            " Just talking about plants and stuff... "
            " Nothing too special in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump ocgardeningfri
    label ocfrigym3:
        # nox and jam
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked to the gym and found two of your classmates doing their own things. "
        " Who would you like to talk to? "
        if noxknow == True and jamknow == True:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump specklepsmp
                " {image=jamicon} Jam {image=jamicon} ":
                    jump roropsmp
        elif noxknow == True and jamknow == False:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump specklepsmp
                " {image=jamicon} A mean looking girl {image=jamicon} ":
                    jump roropsmp
        elif noxknow == False and jamknow == True:
            menu:
                " {image=noxicon} A sleepy guy {image=noxicon} ":
                    jump specklepsmp
                " {image=jamicon} Jam {image=jamicon} ":
                    jump roropsmp
        else:
            menu:
                " {image=noxicon} A sleepy guy {image=noxicon} ":
                    jump specklepsmp
                " {image=jamicon} A mean looking girl {image=jamicon} ":
                    jump roropsmp
        label specklepsmp:
            show noxneutral at center with easeinleft
            if noxknow == True:
                " You walked over to him and asked him what he was doing. "
                " He looked like he was pretty bored right now... "
                n " Oh um...hey there, [name]... "
                n " I'm actually pretty bored right now... "
                n " I could fall asleep, but... "
                n " I don't feel tired right now, surprisingly... "
                n " I would like to do something, but... "
                n " I don't know what... "
                n " I mean... "
                n " I am technically doing something right now... "
                n " Talking to you, I mean... "
                n " But... "
                n " I want to also do something productive... "
                n " Maybe I could even do my homework, but... "
                n " I don't have anything to do... "
                n " All of my homework is done... "
                n " Hmhmmm... "
                n " Maybe we could... "
                n " Do something together...? "
                n " I don't have any ideas, though... "
                n " Maybe you have any ideas...? "
                n " I'll be fine with whatever you want to do... "
                n " As long as it gets me distracted... "
                n " Then I'll be fine with it... "
                " You thought about what you two could do. "
                " Something interesting... "
                " You didn't really know what kind of interesting thing you two could do. "
                " You thought for a bit longer. "
                " Surprisingly, you had to think long and hard for this one. "
                " You continued to think and think... "
                " Until you got an idea. "
                " It's not that much of a good idea, but atleast it's something. "
                " You suggested that you and Nox just walk around the school and get some food. "
                " It wasn't too bad of an idea in your opinion. "
                n " Hm...? "
                n " Okay, we do that then... "
                n " Let's go... "
                n " Maybe we could talk about something, while we're walking around... "
                " Or maybe even talk about some drama. "
                n " Oh, drama...? "
                n " I'm not really the one to talk about drama, but... "
                n " If that's what you want, then I don't mind talking about it... "
                n " Anyway...let's go already... "
                scene black with dissolve
                " You spent the rest of the break walking and talking with Nox. "
                " And also eating up the snacks you got from the cafeteria. "
                " You guys witnessed a bit of drama while you two were walking around. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back to the classroom with Nox after a bit. "
                pause 2.0
                jump ocgardeningfri
            else:
                " You walked over to him and asked him what he was doing. "
                " He looked like he was pretty bored right now... "
                x " Oh um...hey there, [name]... "
                x " I don't think I've met you before, um... "
                $ noxknow = True
                n " I'm Nox...It's nice to meet you... "
                n " I'm actually pretty bored right now... "
                n " I could fall asleep, but... "
                n " I don't feel tired right now, surprisingly... "
                n " I would like to do something, but... "
                n " I don't know what... "
                n " I mean... "
                n " I am technically doing something right now... "
                n " Talking to you, I mean... "
                n " But... "
                n " I want to also do something productive... "
                n " Maybe I could even do my homework, but... "
                n " I don't have anything to do... "
                n " All of my homework is done... "
                n " Hmhmmm... "
                n " Maybe we could... "
                n " Do something together...? "
                n " I don't have any ideas, though... "
                n " Maybe you have any ideas...? "
                n " I'll be fine with whatever you want to do... "
                n " As long as it gets me distracted... "
                n " Then I'll be fine with it... "
                " You thought about what you two could do. "
                " Something interesting... "
                " You didn't really know what kind of interesting thing you two could do. "
                " You thought for a bit longer. "
                " Surprisingly, you had to think long and hard for this one. "
                " You continued to think and think... "
                " Until you got an idea. "
                " It's not that much of a good idea, but atleast it's something. "
                " You suggested that you and Nox just walk around the school and get some food. "
                " It wasn't too bad of an idea in your opinion. "
                n " Hm...? "
                n " Okay, we do that then... "
                n " Let's go... "
                n " Maybe we could talk about something, while we're walking around... "
                " Or maybe even talk about some drama. "
                n " Oh, drama...? "
                n " I'm not really the one to talk about drama, but... "
                n " If that's what you want, then I don't mind talking about it... "
                n " Anyway...let's go already... "
                scene black with dissolve
                " You spent the rest of the break walking and talking with Nox. "
                " And also eating up the snacks you got from the cafeteria. "
                " You guys witnessed a bit of drama while you two were walking around. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back to the classroom with Nox after a bit. "
                pause 2.0
                jump ocgardeningfri
        label roropsmp:
            show jamneutral at center with easeinright
            if jamknow == True:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was in some deep thought... "
                ja " Oh, uh.... "
                ja " Just you, huh? "
                ja " ...Well. "
                ja " I don't think I've told you about this before, but... "
                ja " I was thinking of what I should say to my friend. "
                ja " Considering the fact I'm giving her a gift right after this class.. "
                ja " I'm very nervous, if you can't tell. "
                ja " And I keep on thinking... "
                ja " What if she doesn't even like the gift? "
                ja " And, you know... "
                ja " All the other of those 'what-if' thoughts. "
                ja " I know that I shouldn't believe them, but... "
                " You told her that everything's going to be okay. "
                " And if not, that means that you two can still be friends. "
                " Even if she doesn't like the gift. "
                " She's just going to consider it as a tiny mistake and nothing more. "
                " And tiny mistakes happen in friendships. "
                " And that's okay because not every friendship is perfect. "
                " So, even if she doesn't like it... "
                " It'll be fine. "
                " The memory of you getting the wrong thing to her will pass. "
                " And the two of you could just laugh it off in the future. "
                " Like some big old joke that only you two know about. "
                ja " ...Thanks, [name]. "
                ja " I...appreciate your words. "
                " You gave her a thumbs up and noticed her flowers. "
                " You immediately guessed that she was going to confess. "
                " You then said that you would cheer for her. "
                ja " Oh, uh...really? "
                ja " Thanks again, then. "
                ja " I appreciate the fact that you would cheer for me. "
                ja " Now, um.. "
                ja " As I was saying, I'm struggling to find the right words to say to her. "
                ja " So, uh... "
                ja " Could you help me...? "
                ja " With, you know... what I have to say. "
                ja " It's going to be weird if I just say to her that I like her and give her the flowers. "
                ja " I need to give her a reason on why I like her, and all of that... "
                ja " I have many, many reasons, but... "
                ja " I just don't know how to put them all in a sentence. "
                ja " Sighhhh...could you help me out, [name]? "
                ja " It's fine if you don't want to. "
                ja " I think I can come up with something on my own. "
                ja " (Keyword....I think.) "
                ja " (I'm not really the best at words.) "
                " You thought about it for a bit before you agreed on helping her. "
                ja " Thanks, [name]. "
                scene black with dissolve
                " You spent the rest of the break talking with Jam. "
                " Just talking to her about what she should say to her friend... "
                " You were cheering for her as you were doing this. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for another class. "
                " You walked to the gym and went to your classroom. "
                pause 2.0
                jump ocgardeningfri
            else:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was in some deep thought... "
                x " Oh, uh.... "
                x " Just you, huh? "
                x " Don't think we've met before, so... "
                $ jamknow = True
                ja " I'm Jam, and uh... "
                ja " ...Well. "
                ja " I don't think I've told you about this before, but... "
                ja " I was thinking of what I should say to my friend. "
                ja " Considering the fact I'm giving her a gift right after this class.. "
                ja " I'm very nervous, if you can't tell. "
                ja " And I keep on thinking... "
                ja " What if she doesn't even like the gift? "
                ja " And, you know... "
                ja " All the other of those 'what-if' thoughts. "
                ja " I know that I shouldn't believe them, but... "
                " You told her that everything's going to be okay. "
                " And if not, that means that you two can still be friends. "
                " Even if she doesn't like the gift. "
                " She's just going to consider it as a tiny mistake and nothing more. "
                " And tiny mistakes happen in friendships. "
                " And that's okay because not every friendship is perfect. "
                " So, even if she doesn't like it... "
                " It'll be fine. "
                " The memory of you getting the wrong thing to her will pass. "
                " And the two of you could just laugh it off in the future. "
                " Like some big old joke that only you two know about. "
                ja " ...Thanks, [name]. "
                ja " I...appreciate your words. "
                " You gave her a thumbs up and noticed her flowers. "
                " You immediately guessed that she was going to confess. "
                " You then said that you would cheer for her. "
                ja " Oh, uh...really? "
                ja " Thanks again, then. "
                ja " I appreciate the fact that you would cheer for me. "
                ja " Now, um.. "
                ja " As I was saying, I'm struggling to find the right words to say to her. "
                ja " So, uh... "
                ja " Could you help me...? "
                ja " With, you know... what I have to say. "
                ja " It's going to be weird if I just say to her that I like her and give her the flowers. "
                ja " I need to give her a reason on why I like her, and all of that... "
                ja " I have many, many reasons, but... "
                ja " I just don't know how to put them all in a sentence. "
                ja " Sighhhh...could you help me out, [name]? "
                ja " It's fine if you don't want to. "
                ja " I think I can come up with something on my own. "
                ja " (Keyword....I think.) "
                ja " (I'm not really the best at words.) "
                " You thought about it for a bit before you agreed on helping her. "
                ja " Thanks, [name]. "
                scene black with dissolve
                " You spent the rest of the break talking with Jam. "
                " Just talking to her about what she should say to her friend... "
                " You were cheering for her as you were doing this. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for another class. "
                " You walked to the gym and went to your classroom. "
                pause 2.0
                jump ocgardeningfri
    label ocfricafeteria3:
        # disk and carmen
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked to the cafeteria and spotted two of your classmates talking to eachother. "
        " Wondering what they're talking about, you walked over to them and sat next to them. "
        show diskneutral at left with easeinright
        show carmenneutral at right with easeinright
        if diskknow == True and carmenknow == True:
            d " Heya there, [name]! "
            ca " ... "
            " The other guy waves at you. "
            d " I was just talking to Carmen over here! "
            d " You know how I'm hosting this party later after school, right? "
            d " And you know how Carmen over here plays the guitar, right? "
            d " I think you see where I'm going with this! "
            d " Buuuut, if you don't... "
            d " I'm planning to get Carmen to play live! "
            hide carmenneutral at bottom
            show carmensad at right
            ca " ... "
            d " Oh, I'm sure you'll do great, Carmen! "
            d " Listen... "
            d " I've heard your music before, and it's all good! "
            d " And there's other people who have said your music is great! "
            d " So... "
            d " You don't need to worry about people not liking your song! "
            d " There's a lot of people who would agree with me right now... "
            d " Like [name] over here! "
            d " Right, [name]? "
            " You did a nod of approval. "
            " You haven't really heard Carmen's music before, only snippets. "
            " But... "
            " You're sure it's great considering how Disk is complimenting him like this. "
            " Even though you haven't really heard of it before. "
            d " See! [name] agrees with me! "
            d " If you don't feel like doing it though... "
            d " It's still completely fine if you don't want to! "
            d " Only do it if you really think that you can, okay? "
            d " I don't want you to push yourself... "
            d " Pushing yourself is bad, remember? "
            ca " ... "
            " Carmen seems to be thinking about Disk's words. "
            " He kept on thinking and thinking... "
            hide carmensad at bottom
            show carmenhappy at right
            ca " ...!! "
            " He finally agreed to play for Disk. "
            hide diskneutral at bottom
            show diskhappy at left
            d " Yay! "
            d " But, um... "
            d " Remember, Carmen. "
            hide diskhappy at bottom
            show disksad at left
            d " If you ever feel like you don't feel like doing it... "
            d " You can always tell me, okay? "
            d " Trust me, I won't be mad or disappointed. "
            d " Only do things when you really want to. "
            d " I don't want to make you feel uncomfortable, after all... "
            d " Even if you tell me when you're about to perform. "
            d " I'm big on making others feel comfortable, so... "
            d " It would break my heart if you felt uncomfortable whilst performing. "
            d " So, just... "
            d " Just tell me if you don't want to, okay? "
            hide carmenhappy at bottom
            show carmenneutral at right
            ca " ... "
            " Carmen gives him a nod and a thumbsup. "
            " It was as if he was trying to reassure Disk that he could really do it. "
            hide disksad at bottom
            show diskneutral at center
            d " Okay...good to know, then! "
            d " I hope everything goes well later! "
            ca " ...!! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Carmen. "
            " Just talking about the party Disk was gonna have... "
            " Maybe you could get a recording of Carmen playing his guitar later. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump ocgardeningfri
        elif diskknow == True and carmenknow == False:
            d " Heya there, [name]! "
            x " ... "
            " The other guy waves at you. "
            $ carmenknow = True
            d " I was just talking to Carmen over here! "
            d " You know how I'm hosting this party later after school, right? "
            d " And you know how Carmen over here plays the guitar, right? "
            d " I think you see where I'm going with this! "
            d " Buuuut, if you don't... "
            d " I'm planning to get Carmen to play live! "
            hide carmenneutral at bottom
            show carmensad at right
            ca " ... "
            d " Oh, I'm sure you'll do great, Carmen! "
            d " Listen... "
            d " I've heard your music before, and it's all good! "
            d " And there's other people who have said your music is great! "
            d " So... "
            d " You don't need to worry about people not liking your song! "
            d " There's a lot of people who would agree with me right now... "
            d " Like [name] over here! "
            d " Right, [name]? "
            " You did a nod of approval. "
            " You haven't really heard Carmen's music before, only snippets. "
            " But... "
            " You're sure it's great considering how Disk is complimenting him like this. "
            " Even though you haven't really heard of it before. "
            d " See! [name] agrees with me! "
            d " If you don't feel like doing it though... "
            d " It's still completely fine if you don't want to! "
            d " Only do it if you really think that you can, okay? "
            d " I don't want you to push yourself... "
            d " Pushing yourself is bad, remember? "
            ca " ... "
            " Carmen seems to be thinking about Disk's words. "
            " He kept on thinking and thinking... "
            hide carmensad at bottom
            show carmenhappy at right
            ca " ...!! "
            " He finally agreed to play for Disk. "
            hide diskneutral at bottom
            show diskhappy at left
            d " Yay! "
            d " But, um... "
            d " Remember, Carmen. "
            hide diskhappy at bottom
            show disksad at left
            d " If you ever feel like you don't feel like doing it... "
            d " You can always tell me, okay? "
            d " Trust me, I won't be mad or disappointed. "
            d " Only do things when you really want to. "
            d " I don't want to make you feel uncomfortable, after all... "
            d " Even if you tell me when you're about to perform. "
            d " I'm big on making others feel comfortable, so... "
            d " It would break my heart if you felt uncomfortable whilst performing. "
            d " So, just... "
            d " Just tell me if you don't want to, okay? "
            hide carmenhappy at bottom
            show carmenneutral at right
            ca " ... "
            " Carmen gives him a nod and a thumbsup. "
            " It was as if he was trying to reassure Disk that he could really do it. "
            hide disksad at bottom
            show diskneutral at center
            d " Okay...good to know, then! "
            d " I hope everything goes well later! "
            ca " ...!! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Carmen. "
            " Just talking about the party Disk was gonna have... "
            " Maybe you could get a recording of Carmen playing his guitar later. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump ocgardeningfri
        elif diskknow == False and carmenknow == True:
            x " Heya there, [name]! "
            ca " ... "
            " The other guy waves at you. "
            x " Don't think I've introduced myself to you yet, hmmm... "
            $ diskknow = True
            d " I'm Disk! It's really nice to meet you!!! "
            d " I was just talking to Carmen over here! "
            d " You know how I'm hosting this party later after school, right? "
            d " And you know how Carmen over here plays the guitar, right? "
            d " I think you see where I'm going with this! "
            d " Buuuut, if you don't... "
            d " I'm planning to get Carmen to play live! "
            hide carmenneutral at bottom
            show carmensad at right
            ca " ... "
            d " Oh, I'm sure you'll do great, Carmen! "
            d " Listen... "
            d " I've heard your music before, and it's all good! "
            d " And there's other people who have said your music is great! "
            d " So... "
            d " You don't need to worry about people not liking your song! "
            d " There's a lot of people who would agree with me right now... "
            d " Like [name] over here! "
            d " Right, [name]? "
            " You did a nod of approval. "
            " You haven't really heard Carmen's music before, only snippets. "
            " But... "
            " You're sure it's great considering how Disk is complimenting him like this. "
            " Even though you haven't really heard of it before. "
            d " See! [name] agrees with me! "
            d " If you don't feel like doing it though... "
            d " It's still completely fine if you don't want to! "
            d " Only do it if you really think that you can, okay? "
            d " I don't want you to push yourself... "
            d " Pushing yourself is bad, remember? "
            ca " ... "
            " Carmen seems to be thinking about Disk's words. "
            " He kept on thinking and thinking... "
            hide carmensad at bottom
            show carmenhappy at right
            ca " ...!! "
            " He finally agreed to play for Disk. "
            hide diskneutral at bottom
            show diskhappy at left
            d " Yay! "
            d " But, um... "
            d " Remember, Carmen. "
            hide diskhappy at bottom
            show disksad at left
            d " If you ever feel like you don't feel like doing it... "
            d " You can always tell me, okay? "
            d " Trust me, I won't be mad or disappointed. "
            d " Only do things when you really want to. "
            d " I don't want to make you feel uncomfortable, after all... "
            d " Even if you tell me when you're about to perform. "
            d " I'm big on making others feel comfortable, so... "
            d " It would break my heart if you felt uncomfortable whilst performing. "
            d " So, just... "
            d " Just tell me if you don't want to, okay? "
            hide carmenhappy at bottom
            show carmenneutral at right
            ca " ... "
            " Carmen gives him a nod and a thumbsup. "
            " It was as if he was trying to reassure Disk that he could really do it. "
            hide disksad at bottom
            show diskneutral at center
            d " Okay...good to know, then! "
            d " I hope everything goes well later! "
            ca " ...!! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Carmen. "
            " Just talking about the party Disk was gonna have... "
            " Maybe you could get a recording of Carmen playing his guitar later. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump ocgardeningfri
        else:
            x " Heya there, [name]! "
            x " ... "
            " The other guy waves at you. "
            x " Don't think I've introduced myself to you yet, hmmm... "
            $ diskknow = True
            $ carmenknow = True
            d " I'm Disk! It's really nice to meet you!!! "
            d " I was just talking to Carmen over here! "
            d " You know how I'm hosting this party later after school, right? "
            d " And you know how Carmen over here plays the guitar, right? "
            d " I think you see where I'm going with this! "
            d " Buuuut, if you don't... "
            d " I'm planning to get Carmen to play live! "
            hide carmenneutral at bottom
            show carmensad at right
            ca " ... "
            d " Oh, I'm sure you'll do great, Carmen! "
            d " Listen... "
            d " I've heard your music before, and it's all good! "
            d " And there's other people who have said your music is great! "
            d " So... "
            d " You don't need to worry about people not liking your song! "
            d " There's a lot of people who would agree with me right now... "
            d " Like [name] over here! "
            d " Right, [name]? "
            " You did a nod of approval. "
            " You haven't really heard Carmen's music before, only snippets. "
            " But... "
            " You're sure it's great considering how Disk is complimenting him like this. "
            " Even though you haven't really heard of it before. "
            d " See! [name] agrees with me! "
            d " If you don't feel like doing it though... "
            d " It's still completely fine if you don't want to! "
            d " Only do it if you really think that you can, okay? "
            d " I don't want you to push yourself... "
            d " Pushing yourself is bad, remember? "
            ca " ... "
            " Carmen seems to be thinking about Disk's words. "
            " He kept on thinking and thinking... "
            hide carmensad at bottom
            show carmenhappy at right
            ca " ...!! "
            " He finally agreed to play for Disk. "
            hide diskneutral at bottom
            show diskhappy at left
            d " Yay! "
            d " But, um... "
            d " Remember, Carmen. "
            hide diskhappy at bottom
            show disksad at left
            d " If you ever feel like you don't feel like doing it... "
            d " You can always tell me, okay? "
            d " Trust me, I won't be mad or disappointed. "
            d " Only do things when you really want to. "
            d " I don't want to make you feel uncomfortable, after all... "
            d " Even if you tell me when you're about to perform. "
            d " I'm big on making others feel comfortable, so... "
            d " It would break my heart if you felt uncomfortable whilst performing. "
            d " So, just... "
            d " Just tell me if you don't want to, okay? "
            hide carmenhappy at bottom
            show carmenneutral at right
            ca " ... "
            " Carmen gives him a nod and a thumbsup. "
            " It was as if he was trying to reassure Disk that he could really do it. "
            hide disksad at bottom
            show diskneutral at center
            d " Okay...good to know, then! "
            d " I hope everything goes well later! "
            ca " ...!! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Carmen. "
            " Just talking about the party Disk was gonna have... "
            " Maybe you could get a recording of Carmen playing his guitar later. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump ocgardeningfri
    label ocfrirooftop3:
        # jacob and quinn
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked to the rooftop and spotted two of your classmates just doing their own things. "
        " Who would you like to talk to for this break? "
        if jacobknow == True and quinnknow == True:
            menu:
                " {image=jacobicon} Jacob {image=jacobicon} ":
                    jump birdbrainjacob
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump birdbrainquinn
        elif jacobknow == True and quinnknow == False:
            menu:
                " {image=jacobicon} Jacob {image=jacobicon} ":
                    jump birdbrainjacob
                " {image=quinnicon} A theater-y kid {image=quinnicon} ":
                    jump birdbrainquinn
        elif jacobknow == False and quinnknow == True:
            menu:
                " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                    jump birdbrainjacob
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump birdbrainquinn
        else:
            menu:
                " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                    jump birdbrainjacob
                " {image=quinnicon} A theater-y kid {image=quinnicon} ":
                    jump birdbrainquinn
        label birdbrainjacob:
            show jacobneutral at center with easeinright
            if jacobknow == True:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was looking at something... "
                jac " Huh? oh, it's you. "
                jac " Sorry, was just looking at something... "
                jac " You see that couple out there? "
                jac " They probably don't know that I'm talking about them right now, but... "
                jac " They've been arguing for the past few minutes now. "
                jac " I think they've been going on for longer than that, but... "
                jac " Still, they've been arguing. "
                jac " Apparently the girl is mad because the guy isn't paying attention to her. "
                jac " The guy was just ignoring her because he needed to focus on his studies. "
                jac " And now he's telling her that he can't have his attention fully revolved around her... "
                jac " And honestly? it's really reasonable. "
                jac " You've gotta finish school first to get a good job. "
                jac " And honestly, in my opinion... "
                jac " I don't think the girl should be mad about something like that. "
                jac " She should've tried to understand... "
                jac " I mean... "
                jac " I get that you want attention from your boyfriend, but... "
                jac " Your boyfriend has other things to do, too. "
                jac " Like school and stuff. "
                jac " Don't you want your boyfriend to have a good life? "
                jac " A good job, good everything so that he can support you or give you nice things... "
                jac " Don't you want all of that? "
                jac " Wait, hold on... "
                jac " Lemme listen to them again. "
                jac " Looks like something's happening. "
                jac " ... "
                jac " Oh damn, the girl's having a tantrum. "
                jac " It's kind of insane how the guy's just keeping calm... "
                jac " I respect that though. "
                jac " Ough. "
                jac " Looks like the girl wants a break up... "
                jac " Surprisingly the guy doesn't get mad over that. "
                jac " He just accepts it, from what I can tell. "
                jac " Huh...what a nice guy. "
                jac " I don't think he deserves that girl, in all honesty... "
                jac " If you have a partner, you can't expect them to give you attention 24/7. "
                jac " If you want that, they're just going to get tired at some point. "
                jac " You've got to be understanding and give them a break at some point. "
                jac " ... "
                jac " But here I am, talking about couple stuff. "
                jac " I haven't even been in a relationship before... "
                jac " And yet I'm talking like I'm a professional. "
                jac " Sigh... "
                scene black with dissolve
                " You spent the rest of the break talking with Jacob. "
                " You didn't know he could be good at advice like that... "
                " Interesting new fun fact, I guess. "
                " But I also guess that it's just common sense or something. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump ocgardeningfri
            else:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was looking at something... "
                x " Huh? oh, it's you. "
                x " Sorry, was just looking at something... "
                x " Don't think I've introduced myself to you yet. "
                $ jacobknow = True
                jac " I'm Jacob, it's nice to meet you. "
                jac " You wanna know what I'm looking at? "
                jac " Uh...okay. "
                jac " You see that couple out there? "
                jac " They probably don't know that I'm talking about them right now, but... "
                jac " They've been arguing for the past few minutes now. "
                jac " I think they've been going on for longer than that, but... "
                jac " Still, they've been arguing. "
                jac " Apparently the girl is mad because the guy isn't paying attention to her. "
                jac " The guy was just ignoring her because he needed to focus on his studies. "
                jac " And now he's telling her that he can't have his attention fully revolved around her... "
                jac " And honestly? it's really reasonable. "
                jac " You've gotta finish school first to get a good job. "
                jac " And honestly, in my opinion... "
                jac " I don't think the girl should be mad about something like that. "
                jac " She should've tried to understand... "
                jac " I mean... "
                jac " I get that you want attention from your boyfriend, but... "
                jac " Your boyfriend has other things to do, too. "
                jac " Like school and stuff. "
                jac " Don't you want your boyfriend to have a good life? "
                jac " A good job, good everything so that he can support you or give you nice things... "
                jac " Don't you want all of that? "
                jac " Wait, hold on... "
                jac " Lemme listen to them again. "
                jac " Looks like something's happening. "
                jac " ... "
                jac " Oh damn, the girl's having a tantrum. "
                jac " It's kind of insane how the guy's just keeping calm... "
                jac " I respect that though. "
                jac " Ough. "
                jac " Looks like the girl wants a break up... "
                jac " Surprisingly the guy doesn't get mad over that. "
                jac " He just accepts it, from what I can tell. "
                jac " Huh...what a nice guy. "
                jac " I don't think he deserves that girl, in all honesty... "
                jac " If you have a partner, you can't expect them to give you attention 24/7. "
                jac " If you want that, they're just going to get tired at some point. "
                jac " You've got to be understanding and give them a break at some point. "
                jac " ... "
                jac " But here I am, talking about couple stuff. "
                jac " I haven't even been in a relationship before... "
                jac " And yet I'm talking like I'm a professional. "
                jac " Sigh... "
                scene black with dissolve
                " You spent the rest of the break talking with Jacob. "
                " You didn't know he could be good at advice like that... "
                " Interesting new fun fact, I guess. "
                " But I also guess that it's just common sense or something. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump ocgardeningfri
        label birdbrainquinn:
            show quinnneutral at center with easeinleft
            if quinnknow == True:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was doing some cool tricks for his play that you heard of. "
                " Apparently it's starting before cooking class... "
                q " Greetings, [name]! "
                q " I was just practicing for my play, you see. "
                q " The play I made has me doing some tricks here... "
                q " So I have to practice until I can get it right! "
                q " Practice does make perfect, after all. "
                q " And I have to practice before my play to make it even better! "
                q " Perfection matters a whole lot in plays, you know. "
                q " Can't just go around expecting for everything to be okay without a rehearsal... "
                q " Like seriously - "
                hide quinnneutral at bottom
                show quinnangry at center
                q " You can't just have one rehearsal... "
                q " And expect for everything to go okay. "
                q " Like for example... "
                q " You practice for one day. "
                q " You get every member to practice, right? "
                q " And then you suddenly say that this is the last practice you guys get. "
                q " Like, hello? "
                q " Do you expect them to memorize everything all in one day? "
                q " If you can do that, then... "
                q " Good for you, I guess. "
                q " But you've also got to think of your members. "
                q " What kind of club leader would you be if you can't even think of the others? "
                q " Geez... "
                q " I hate people who are like that. "
                q " That's why I'm trying my best to avoid being like that. "
                q " People who are like that are lazy... "
                q " And I'm NOT lazy, mind you! "
                q " I'm productive, I'm what some say...a workaholic. "
                q " Does my work get me tired? yes. "
                q " But is it worth it for a good outcome? "
                q " Absolutely! "
                q " That's why I want to practice whenever I can! "
                q " Even if it tired me out! "
                q " (Unlike some people out there...) "
                q " (Someone's probably sitting in their chair and playing a dating sim right now.) "
                q " (Not doing anything productive like their homework...) "
                q " (Eugh.) "
                hide quinnangry at bottom
                show quinnneutral at center
                q " Anyway, I'm going to go back to practicing! "
                q " You can watch me of course, [name]. "
                q " I need an audience who can give me an honest opinion, after all! "
                q " Really, just be honest with me. "
                q " I don't want some sweet lies or whatever you call it. "
                scene black with dissolve
                " You spent the rest of the break talking with Quinn. "
                " You watched him practice and gave him your honest opinions. "
                " And you had to admit, his tricks WERE pretty cool. "
                " Seems like he's putting a lot of effort into this play of his. "
                " Impressive. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your school. "
                pause 2.0
                jump ocgardeningfri
            else:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was doing some cool tricks for his play that you heard of. "
                " Apparently it's starting before cooking class... "
                x " Greetings, [name]! "
                x " Hm, I don't think I've introduced myself before to you. "
                x " Let me fix that! "
                $ quinnknow = True
                q " I'm Quinn. Disk's younger brother and a part of the theater club. "
                q " I was just practicing for my play, you see. "
                q " The play I made has me doing some tricks here... "
                q " So I have to practice until I can get it right! "
                q " Practice does make perfect, after all. "
                q " And I have to practice before my play to make it even better! "
                q " Perfection matters a whole lot in plays, you know. "
                q " Can't just go around expecting for everything to be okay without a rehearsal... "
                q " Like seriously - "
                hide quinnneutral at bottom
                show quinnangry at center
                q " You can't just have one rehearsal... "
                q " And expect for everything to go okay. "
                q " Like for example... "
                q " You practice for one day. "
                q " You get every member to practice, right? "
                q " And then you suddenly say that this is the last practice you guys get. "
                q " Like, hello? "
                q " Do you expect them to memorize everything all in one day? "
                q " If you can do that, then... "
                q " Good for you, I guess. "
                q " But you've also got to think of your members. "
                q " What kind of club leader would you be if you can't even think of the others? "
                q " Geez... "
                q " I hate people who are like that. "
                q " That's why I'm trying my best to avoid being like that. "
                q " People who are like that are lazy... "
                q " And I'm NOT lazy, mind you! "
                q " I'm productive, I'm what some say...a workaholic. "
                q " Does my work get me tired? yes. "
                q " But is it worth it for a good outcome? "
                q " Absolutely! "
                q " That's why I want to practice whenever I can! "
                q " Even if it tired me out! "
                q " (Unlike some people out there...) "
                q " (Someone's probably sitting in their chair and playing a dating sim right now.) "
                q " (Not doing anything productive like their homework...) "
                q " (Eugh.) "
                hide quinnangry at bottom
                show quinnneutral at center
                q " Anyway, I'm going to go back to practicing! "
                q " You can watch me of course, [name]. "
                q " I need an audience who can give me an honest opinion, after all! "
                q " Really, just be honest with me. "
                q " I don't want some sweet lies or whatever you call it. "
                scene black with dissolve
                " You spent the rest of the break talking with Quinn. "
                " You watched him practice and gave him your honest opinions. "
                " And you had to admit, his tricks WERE pretty cool. "
                " Seems like he's putting a lot of effort into this play of his. "
                " Impressive. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your school. "
                pause 2.0
                jump ocgardeningfri
    label ocfrilibrary3:
        # spark and koa
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked to the library and found two of your classmates talking with eachother. "
        " Wondering what they're talking about, you walked over to them. "
        show sparkneutral at left with easeinright
        show koaneutral at right with easeinright
        if sparkknow == True and koaknow == True:
            sp " Hey there, [name]. "
            k " ...Hi, [name]. "
            sp " I was just talking to Koa over here... "
            sp " About the whole new thing they're adding to this school. "
            " Huh? there's something being added here? "
            " You didn't know that. "
            " You asked them what they were talking about. "
            k " Well, to put it simply... "
            k " They're adding those robots that would monitor you whenever there's an exam. "
            k " Just to make sure that you won't cheat. "
            sp " And from what I've heard... "
            sp " They've had this thing in the past before. "
            sp " But, one of them kind of... "
            sp " I don't know how to explain it. Gone rogue? "
            k " That's the best way you can explain it, I guess. "
            " I had a reason for that, you know. "
            " They would never understand. "
            " ...Uh, anyway. "
            k " I think it's kind of pointless, in my opinion. "
            k " Yes, it's to make sure that no one cheats, but... "
            k " It's also kind of wasting money. "
            sp " I mean...I can see where you're coming from. "
            sp " I think it's sort of better if the teachers would be the ones checking. "
            sp " Having robots would only make them lazier. "
            sp " And robots aren't always right, too... "
            k " Sometimes they can make mistakes. "
            k " Like they could just call out someone random... "
            k " When they didn't even do anything wrong. "
            sp " And also the fact that it could make the teachers lazy. "
            sp " Like they could just rely on the bots... "
            k " I'm sure they won't be like that though. "
            k " By they, I mean all of our subject teachers. "
            sp " Yup. "
            sp " They're all too smart to depend on a robot. "
            sp " Most likely they won't be using them. "
            k " If they do, I'd be surprised. "
            k " Even more surprised if one of them has a...accident. "
            sp " Like that one from before? "
            k " Yup. "
            " Hey...I'm listening, you know... "
            scene black with dissolve
            " You spent the rest of the break talking with Spark and Koa. "
            " Hearing about robots being added was interesting... "
            " But also you agreed with Koa's and Spark's opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump ocgardeningfri
        elif sparkknow == True and koaknow == False:
            sp " Hey there, [name]. "
            x " ...Hi, [name]. "
            $ koaknow = True
            sp " I was just talking to Koa over here... "
            sp " About the whole new thing they're adding to this school. "
            " Huh? there's something being added here? "
            " You didn't know that. "
            " You asked them what they were talking about. "
            k " Well, to put it simply... "
            k " They're adding those robots that would monitor you whenever there's an exam. "
            k " Just to make sure that you won't cheat. "
            sp " And from what I've heard... "
            sp " They've had this thing in the past before. "
            sp " But, one of them kind of... "
            sp " I don't know how to explain it. Gone rogue? "
            k " That's the best way you can explain it, I guess. "
            " I had a reason for that, you know. "
            " They would never understand. "
            " ...Uh, anyway. "
            k " I think it's kind of pointless, in my opinion. "
            k " Yes, it's to make sure that no one cheats, but... "
            k " It's also kind of wasting money. "
            sp " I mean...I can see where you're coming from. "
            sp " I think it's sort of better if the teachers would be the ones checking. "
            sp " Having robots would only make them lazier. "
            sp " And robots aren't always right, too... "
            k " Sometimes they can make mistakes. "
            k " Like they could just call out someone random... "
            k " When they didn't even do anything wrong. "
            sp " And also the fact that it could make the teachers lazy. "
            sp " Like they could just rely on the bots... "
            k " I'm sure they won't be like that though. "
            k " By they, I mean all of our subject teachers. "
            sp " Yup. "
            sp " They're all too smart to depend on a robot. "
            sp " Most likely they won't be using them. "
            k " If they do, I'd be surprised. "
            k " Even more surprised if one of them has a...accident. "
            sp " Like that one from before? "
            k " Yup. "
            " Hey...I'm listening, you know... "
            scene black with dissolve
            " You spent the rest of the break talking with Spark and Koa. "
            " Hearing about robots being added was interesting... "
            " But also you agreed with Koa's and Spark's opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump ocgardeningfri
        elif sparkknow == False and koaknow == True:
            x " Hey there, [name]. "
            k " ...Hi, [name]. "
            $ sparkknow = True
            sp " I'm Spark. Nice to meet you. "
            sp " I was just talking to Koa over here... "
            sp " About the whole new thing they're adding to this school. "
            " Huh? there's something being added here? "
            " You didn't know that. "
            " You asked them what they were talking about. "
            k " Well, to put it simply... "
            k " They're adding those robots that would monitor you whenever there's an exam. "
            k " Just to make sure that you won't cheat. "
            sp " And from what I've heard... "
            sp " They've had this thing in the past before. "
            sp " But, one of them kind of... "
            sp " I don't know how to explain it. Gone rogue? "
            k " That's the best way you can explain it, I guess. "
            " I had a reason for that, you know. "
            " They would never understand. "
            " ...Uh, anyway. "
            k " I think it's kind of pointless, in my opinion. "
            k " Yes, it's to make sure that no one cheats, but... "
            k " It's also kind of wasting money. "
            sp " I mean...I can see where you're coming from. "
            sp " I think it's sort of better if the teachers would be the ones checking. "
            sp " Having robots would only make them lazier. "
            sp " And robots aren't always right, too... "
            k " Sometimes they can make mistakes. "
            k " Like they could just call out someone random... "
            k " When they didn't even do anything wrong. "
            sp " And also the fact that it could make the teachers lazy. "
            sp " Like they could just rely on the bots... "
            k " I'm sure they won't be like that though. "
            k " By they, I mean all of our subject teachers. "
            sp " Yup. "
            sp " They're all too smart to depend on a robot. "
            sp " Most likely they won't be using them. "
            k " If they do, I'd be surprised. "
            k " Even more surprised if one of them has a...accident. "
            sp " Like that one from before? "
            k " Yup. "
            " Hey...I'm listening, you know... "
            scene black with dissolve
            " You spent the rest of the break talking with Spark and Koa. "
            " Hearing about robots being added was interesting... "
            " But also you agreed with Koa's and Spark's opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump ocgardeningfri
        else:
            x " Hey there, [name]. "
            x " ...Hi, [name]. "
            $ sparkknow = True
            $ koaknow = True
            sp " I'm Spark, nice to meet you. "
            sp " I was just talking to Koa over here... "
            sp " About the whole new thing they're adding to this school. "
            " Huh? there's something being added here? "
            " You didn't know that. "
            " You asked them what they were talking about. "
            k " Well, to put it simply... "
            k " They're adding those robots that would monitor you whenever there's an exam. "
            k " Just to make sure that you won't cheat. "
            sp " And from what I've heard... "
            sp " They've had this thing in the past before. "
            sp " But, one of them kind of... "
            sp " I don't know how to explain it. Gone rogue? "
            k " That's the best way you can explain it, I guess. "
            " I had a reason for that, you know. "
            " They would never understand. "
            " ...Uh, anyway. "
            k " I think it's kind of pointless, in my opinion. "
            k " Yes, it's to make sure that no one cheats, but... "
            k " It's also kind of wasting money. "
            sp " I mean...I can see where you're coming from. "
            sp " I think it's sort of better if the teachers would be the ones checking. "
            sp " Having robots would only make them lazier. "
            sp " And robots aren't always right, too... "
            k " Sometimes they can make mistakes. "
            k " Like they could just call out someone random... "
            k " When they didn't even do anything wrong. "
            sp " And also the fact that it could make the teachers lazy. "
            sp " Like they could just rely on the bots... "
            k " I'm sure they won't be like that though. "
            k " By they, I mean all of our subject teachers. "
            sp " Yup. "
            sp " They're all too smart to depend on a robot. "
            sp " Most likely they won't be using them. "
            k " If they do, I'd be surprised. "
            k " Even more surprised if one of them has a...accident. "
            sp " Like that one from before? "
            k " Yup. "
            " Hey...I'm listening, you know... "
            scene black with dissolve
            " You spent the rest of the break talking with Spark and Koa. "
            " Hearing about robots being added was interesting... "
            " But also you agreed with Koa's and Spark's opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump ocgardeningfri

label ocgardeningfri:
    scene gardenroom with dissolve
    " Looks like the teacher is already here. "
    " Let's see what you have for your class today... "
    show wisterianeutral at center with easeinleft
    msw " Good morning, class... "
    msw " I heard you all played dodgeball for PE today...? "
    msw " All of you must've felt so energetic... "
    msw " Well, I might need you guys to calm down for now... "
    msw " This is gardening class, after all. "
    msw " Now, let's begin with our lesson... "
    scene black with dissolve
    " You spent the rest of class just zoning out. "
    " Nothing important really happened. "
    " You probably should get others notes later. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for another break. "
    " You waited for everyone to leave before you did. "
    pause 2.0
    jump ocfribreak4

label ocfribreak4:
    # matte and jam's ending including others
    scene hallway with dissolve
    " Looks like it's break time. "
    " You're thinking of where you should go... "
    " Where do you go for this break? "
    menu:
        " {image=matteicon} The front of the school {image=jamicon} ":
            jump ocfrifront4
        " {image=sparkicon} The back of the school {image=temeroicon} ":
            jump ocfriback4
        " {image=diskicon} The gym {image=quinnicon} ":
            jump ocfrigym4
        " {image=noxicon} The cafeteria {image=jacobicon} ":
            jump ocfricafeteria4
        " {image=orchidicon} The rooftop {image=carmenicon} ":
            jump ocfrirooftop4
        " {image=koaicon} The library {image=koaicon} ":
            jump ocfrilibrary4
    label ocfrifront4:
        # matte and jam's ending
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked to the front of the school and spotted two of your classmates talking to eachother. "
        " Wondering what they're doing, you walked over to them. "
        show matteneutral at left with easeinright
        show jamneutral at right with easeinright
        if matteknow == True and jamknow == True:
            ma " Hey there, [name]! "
            ja " ...Hi, [name]. "
            ma " I was just painting Jam over here! "
            ma " I thought the lighting looked pretty good here, so... "
            ma " I just wanted to capture my best friend's beauty! "
            ja " ...You don't have to say that about me... "
            ma " Oh, but I have to! "
            ma " You're the most prettiest thing I've laid my eyes on! "
            ma " And I'm not lying when I say that, hehe. "
            ja " ...You're too sweet. "
            ma " Nothing's wrong with being a little sweet, you know! "
            ja " I know. "
            ja " Just that... "
            ja " You know. "
            ma " Mhm, I do... "
            ma " But just know that I care for you a lot, okay? "
            ma " I won't let anyone's words change my view of you. "
            ja " ... "
            " Looks like they're pretty busy right now. "
            " You look at Matte's painting... "
            " It looks pretty well made so far. "
            " You wish you could get a painting of you. "
            " Matte would probably ask you for money if you asked though. "
            if mattelv >= 20 or jamlv >= 20:
                ja " Actually, uh... "
                ja " Matte. "
                hide matteneutral at bottom
                show mattesurprised at left
                ma " Hm? "
                ma " Yes, Jam? "
                ja " I have...something to tell you. "
                " Oh wait, what's this? "
                " You're gonna stay and listen for this. "
                " This is going to get really interesting. "
                ma " Really? let me hear it, then! "
                ma " Remember that you can tell me anything, okay? "
                ja " ... "
                ja " It's been a thing that I've been wanting to tell you for awhile now. "
                ja " Like, for a long time now. "
                ma " Oh, really? "
                ma " That's interesting... "
                ja " I know, right? "
                hide jamneutral at bottom
                show jamsad at right
                ja " But, um... "
                ja " God, I'm fumbling with my words here. "
                hide mattesurprised at bottom
                show matteneutral at left
                ma " It's okay, Jam! "
                ma " Take your time! "
                ja " ...Alright. "
                ja " (Deep breaths, Jam...) "
                ja " (This is the moment.) "
                ja " (Nothing to be afraid of.) "
                ja " ...So... "
                ja " Like I said, this thing has been in my head for awhile now. "
                ja " And...I decided that I should tell you about this today. "
                ja " It's a little nerve-wracking for me, but... "
                ja " I know I have to say this to you at some point. "
                ja " I just can't keep these thoughts bottled up anymore. "
                ja " Uh... "
                ja " You know, Matte... "
                ja " You've been...affecting my life greatly. "
                ja " In a positive way, of course. "
                ja " I've been catching myself to be more positive at times... "
                ja " And I've been looking at nature more often and appreciating the smallest things in life. "
                ja " That's how much I've been feeling better because of you, Matte. "
                ja " You've made me feel things that I've never felt before. "
                ja " And I'm glad that you changed my life like this. "
                ja " I don't know how to thank you, but um... "
                " Jam holds out some flowers that she picked out for her. "
                ma " Aww, these are for me...? "
                ja " Mhm. "
                ja " I picked them out just for you. "
                ja " And...I have something else to admit. "
                ma " Oh? "
                ja " ...I have to admit that I... "
                ja " ...I really... "
                " You can do it Jam. "
                hide jamsad at bottom
                show jamhappy at right
                stop music
                hide matteneutral at bottom
                show mattesurprised at left
                ja " I really, really like you. "
                ja " And I mean that in a non-friend way. "
                ma " ...! "
                ma " Hold on, Jam...you...? "
                play music "audio/emotionalmoment.mp3" fadein 1.5
                ja " Yes, I have... "
                ja " I've been liking you for awhile now. "
                ja " At first, I denied it. "
                ja " With...you know how my mother is. "
                ja " But I slowly started accepting it. "
                ja " Accepting the feelings I felt. "
                ja " I've been struggling to say these words to you for awhile now, but here I am... "
                ja " If you don't wish to be THAT way with me, I'm fine with sticking as friends. "
                ja " But, I still have to ask the question... "
                ja " Will you be my girlfriend, and make me the luckiest girl alive? "
                hide mattesurprised at bottom
                show mattesad at left
                ma " Jam, I... "
                ma " I never knew you felt this way. "
                ma " I always thought that you were into guys, considering how you acted, but... "
                ma " Now knowing how you feel about me... "
                ma " I think I can say my answer now... "
                hide mattesad at bottom
                show mattehappy at left
                ma " Yes, I'll be your girlfriend! " with vpunch
                ma " I don't care what anyone says about us... "
                ma " As long as I'm with you, I feel my best! "
                ja " ...Same with me. "
                ja " I'm glad you said yes... "
                ja " I was actually a little worried that you wouldn't. "
                ma " Why would I? "
                ma " You're literally the best person I could ever ask for! "
                ma " How could I reject you, Jam? "
                if mattelv >= 30 or mattelv == 30:
                    ja " You're...way too sweet. "
                    ja " That's one of the things that I love about you. "
                    ja " I...I think I've gotta go. "
                    ja " Gotta go celebrate, I mean. "
                    ja " I've gotta go tell all my guy friends to celebrate. "
                    ma " Hehe, okay! "
                    ma " See you later, then! "
                    hide jamhappy at right with easeoutright
                    show mattehappy at center with move
                    " And Jam leaves. "
                    " Looks like it's just you and Matte now. "
                    hide mattehappy at bottom
                    show matteneutral at center
                    " Matte turns to you. Looks like she has to say something. "
                    ma " Hey, [name]... "
                    ma " I just wanted to say something! "
                    ma " Even though we haven't known eachother for long... "
                    ma " I'd like to thank you for sticking around! "
                    ma " And, honestly? "
                    ma " I think I might want you as a best friend. "
                    ma " You wanna be that? or nah? "
                    menu:
                        " Art besties!! and congrats!! ":
                            hide matteneutral at bottom
                            show mattehappy at center
                            $ mattesend.grant()
                            ma " Hehe, yay! "
                            ma " And thanks, too! "
                            ma " This is officially the best day of my life! "
                            ma " Don't worry, me and Jam will spoil like parents! "
                            scene matteend with dissolve
                            " Congratulations! You've gotten Matte's ending! "
                            " And her sweet achievement. Check your achievements tab! "
                            " I think I might just cry after witnessing this ending. "
                            " Good for Matte and Jam! atleast you're getting spoiled as the third wheel. "
                            jump credits
                        " Normal friends, and congrats!! ":
                            ma " Ah, understandable... "
                            ma " But thanks for the congratulations! "
                            ma " This is offically the best day of my life... "
                            ma " Don't be surprised if me and Jam spoil you out of nowhere, hehe. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Matte. "
                            " You were pretty happy that Matte got herself a nice girlfriend. "
                            " Good for her! good for her. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked back into the school and went to your classroom. "
                            pause 2.0
                            jump ocphysicsfri
                elif jamlv >= 30 or jamlv == 30:
                    ja " You're...way too sweet. "
                    ja " That's one of the things that I love about you. "
                    ma " Hehe, aww!! "
                    ma " I think I'm gonna go tell my dad about this! "
                    ma " He's gonna be so happy to hear the news! "
                    ma " I'll see you later, hun!! "
                    ja " S...see you. "
                    hide mattehappy at right with easeoutright
                    show jamhappy at center with move
                    " Woah, nicknames already? "
                    " They're going with this fast, but it's sweet to hear. "
                    " Looks like Jam has to say something to you, though. "
                    " Let's see what she has to say about this... "
                    hide jamhappy at bottom
                    show jamneutral at center
                    ja " ...[name]. "
                    ja " I have something to say to you, too. "
                    ja " I'd like to thank you for being there for me. "
                    ja " Even if I haven't known you well enough... "
                    ja " You've been the absolute best for me, lately. "
                    ja " And, I feel like... "
                    ja " Maybe, if you feel like it... "
                    ja " We could be best friends? "
                    ja " It's fine if you don't want to, of course. "
                    menu:
                        " Besties!! and congratulations!! ":
                            $ jamsend.grant()
                            hide jamneutral at bottom
                            show jamhappy at center
                            ja " ...I'm glad that you'd want to be best friends. "
                            ja " And, thank you. For the congrats. "
                            ja " This might just be the greatest day of my life... "
                            ja " And I wouldn't have gotten here without you. "
                            scene jamend with dissolve
                            " Congratulations! You've gotten Jam's ending! "
                            " And her sweet achievement. Check your achievements tab! "
                            " I think i might just cry after that ending. "
                            " This whole thing was just so sweet! "
                            jump credits
                        " Normal friends, and congrats!! ":
                            ja " Reasonable. We only have known eachother for four days. "
                            ja " And, thanks... "
                            ja " This might just be the greatest day of my life. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Jam. "
                            " You were pretty happy that Jam got herself a nice girlfriend. "
                            " Good for her! good for her. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked back into the school and went to your classroom. "
                            pause 2.0
                            jump ocphysicsfri
                else:
                    " Aww, what a sweet ending... "
                    " You didn't want to ruin the moment by being there, though. "
                    " And you also didn't want to be a third wheel in this. "
                    " You walked back into the school and walked around. "
                    scene black with dissolve
                    " You spent the rest of the break just wandering around the school. "
                    " Just scrolling on your phone... "
                    " You didn't really see anything that caught your attention. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked into your classroom after a bit of walking. "
                    pause 2.0
                    jump ocphysicsfri
            else:
                " Maybe it's best to leave them alone for now. "
                " It looked like they had something important to do right now. "
                " Besides, they look pretty cute together at the moment. "
                " You walked back into the school and walked around. "
                scene black with dissolve
                " You spent the rest of the break just wandering around the school. "
                " Just scrolling on your phone... "
                " You didn't really see anything that caught your attention. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked into your classroom after a bit of walking. "
                pause 2.0
                jump ocphysicsfri
        elif matteknow == True and jamknow == False:
            ma " Hey there, [name]! "
            x " ...Hi, [name]. "
            $ jamknow = True
            ma " I was just painting Jam over here! "
            ma " I thought the lighting looked pretty good here, so... "
            ma " I just wanted to capture my best friend's beauty! "
            ja " ...You don't have to say that about me... "
            ma " Oh, but I have to! "
            ma " You're the most prettiest thing I've laid my eyes on! "
            ma " And I'm not lying when I say that, hehe. "
            ja " ...You're too sweet. "
            ma " Nothing's wrong with being a little sweet, you know! "
            ja " I know. "
            ja " Just that... "
            ja " You know. "
            ma " Mhm, I do... "
            ma " But just know that I care for you a lot, okay? "
            ma " I won't let anyone's words change my view of you. "
            ja " ... "
            " Looks like they're pretty busy right now. "
            " You look at Matte's painting... "
            " It looks pretty well made so far. "
            " You wish you could get a painting of you. "
            " Matte would probably ask you for money if you asked though. "
            if mattelv >= 20 and jamlv >= 20:
                ja " Actually, uh... "
                ja " Matte. "
                hide matteneutral at bottom
                show mattesurprised at left
                ma " Hm? "
                ma " Yes, Jam? "
                ja " I have...something to tell you. "
                " Oh wait, what's this? "
                " You're gonna stay and listen for this. "
                " This is going to get really interesting. "
                ma " Really? let me hear it, then! "
                ma " Remember that you can tell me anything, okay? "
                ja " ... "
                ja " It's been a thing that I've been wanting to tell you for awhile now. "
                ja " Like, for a long time now. "
                ma " Oh, really? "
                ma " That's interesting... "
                ja " I know, right? "
                hide jamneutral at bottom
                show jamsad at right
                ja " But, um... "
                ja " God, I'm fumbling with my words here. "
                hide mattesurprised at bottom
                show matteneutral at left
                ma " It's okay, Jam! "
                ma " Take your time! "
                ja " ...Alright. "
                ja " (Deep breaths, Jam...) "
                ja " (This is the moment.) "
                ja " (Nothing to be afraid of.) "
                ja " ...So... "
                ja " Like I said, this thing has been in my head for awhile now. "
                ja " And...I decided that I should tell you about this today. "
                ja " It's a little nerve-wracking for me, but... "
                ja " I know I have to say this to you at some point. "
                ja " I just can't keep these thoughts bottled up anymore. "
                ja " Uh... "
                ja " You know, Matte... "
                ja " You've been...affecting my life greatly. "
                ja " In a positive way, of course. "
                ja " I've been catching myself to be more positive at times... "
                ja " And I've been looking at nature more often and appreciating the smallest things in life. "
                ja " That's how much I've been feeling better because of you, Matte. "
                ja " You've made me feel things that I've never felt before. "
                ja " And I'm glad that you changed my life like this. "
                ja " I don't know how to thank you, but um... "
                " Jam holds out some flowers that she picked out for her. "
                ma " Aww, these are for me...? "
                ja " Mhm. "
                ja " I picked them out just for you. "
                ja " And...I have something else to admit. "
                ma " Oh? "
                ja " ...I have to admit that I... "
                ja " ...I really... "
                " You can do it Jam. "
                hide jamsad at bottom
                show jamhappy at right
                stop music
                hide matteneutral at bottom
                show mattesurprised at left
                ja " I really, really like you. "
                ja " And I mean that in a non-friend way. "
                ma " ...! "
                ma " Hold on, Jam...you...? "
                play music "audio/emotionalmoment.mp3" fadein 1.5
                ja " Yes, I have... "
                ja " I've been liking you for awhile now. "
                ja " At first, I denied it. "
                ja " With...you know how my mother is. "
                ja " But I slowly started accepting it. "
                ja " Accepting the feelings I felt. "
                ja " I've been struggling to say these words to you for awhile now, but here I am... "
                ja " If you don't wish to be THAT way with me, I'm fine with sticking as friends. "
                ja " But, I still have to ask the question... "
                ja " Will you be my girlfriend, and make me the luckiest girl alive? "
                hide mattesurprised at bottom
                show mattesad at left
                ma " Jam, I... "
                ma " I never knew you felt this way. "
                ma " I always thought that you were into guys, considering how you acted, but... "
                ma " Now knowing how you feel about me... "
                ma " I think I can say my answer now... "
                hide mattesad at bottom
                show mattehappy at left
                ma " Yes, I'll be your girlfriend! " with vpunch
                ma " I don't care what anyone says about us... "
                ma " As long as I'm with you, I feel my best! "
                ja " ...Same with me. "
                ja " I'm glad you said yes... "
                ja " I was actually a little worried that you wouldn't. "
                ma " Why would I? "
                ma " You're literally the best person I could ever ask for! "
                ma " How could I reject you, Jam? "
                if mattelv >= 30 or mattelv == 30:
                    ja " You're...way too sweet. "
                    ja " That's one of the things that I love about you. "
                    ja " I...I think I've gotta go. "
                    ja " Gotta go celebrate, I mean. "
                    ja " I've gotta go tell all my guy friends to celebrate. "
                    ma " Hehe, okay! "
                    ma " See you later, then! "
                    hide jamhappy at right with easeoutright
                    show mattehappy at center with move
                    " And Jam leaves. "
                    " Looks like it's just you and Matte now. "
                    hide mattehappy at bottom
                    show matteneutral at center
                    " Matte turns to you. Looks like she has to say something. "
                    ma " Hey, [name]... "
                    ma " I just wanted to say something! "
                    ma " Even though we haven't known eachother for long... "
                    ma " I'd like to thank you for sticking around! "
                    ma " And, honestly? "
                    ma " I think I might want you as a best friend. "
                    ma " You wanna be that? or nah? "
                    menu:
                        " Art besties!! and congrats!! ":
                            hide matteneutral at bottom
                            show mattehappy at center
                            $ mattesend.grant()
                            ma " Hehe, yay! "
                            ma " And thanks, too! "
                            ma " This is officially the best day of my life! "
                            ma " Don't worry, me and Jam will spoil like parents! "
                            scene matteend with dissolve
                            " Congratulations! You've gotten Matte's ending! "
                            " And her sweet achievement. Check your achievements tab! "
                            " I think I might just cry after witnessing this ending. "
                            " Good for Matte and Jam! atleast you're getting spoiled as the third wheel. "
                            jump credits
                        " Normal friends, and congrats!! ":
                            ma " Ah, understandable... "
                            ma " But thanks for the congratulations! "
                            ma " This is offically the best day of my life... "
                            ma " Don't be surprised if me and Jam spoil you out of nowhere, hehe. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Matte. "
                            " You were pretty happy that Matte got herself a nice girlfriend. "
                            " Good for her! good for her. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked back into the school and went to your classroom. "
                            pause 2.0
                            jump ocphysicsfri
                elif jamlv >= 30 or jamlv == 30:
                    " Aww, what a sweet ending... "
                    " You didn't want to ruin the moment by being there, though. "
                    " And you also didn't want to be a third wheel in this. "
                    " You walked back into the school and walked around. "
                    scene black with dissolve
                    " You spent the rest of the break just wandering around the school. "
                    " Just scrolling on your phone... "
                    " You didn't really see anything that caught your attention. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked into your classroom after a bit of walking. "
                    pause 2.0
                    jump ocphysicsfri
                else:
                    " Aww, what a sweet ending... "
                    " You didn't want to ruin the moment by being there, though. "
                    " And you also didn't want to be a third wheel in this. "
                    " You walked back into the school and walked around. "
                    scene black with dissolve
                    " You spent the rest of the break just wandering around the school. "
                    " Just scrolling on your phone... "
                    " You didn't really see anything that caught your attention. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked into your classroom after a bit of walking. "
                    pause 2.0
                    jump ocphysicsfri
            else:
                " Maybe it's best to leave them alone for now. "
                " It looked like they had something important to do right now. "
                " Besides, they look pretty cute together at the moment. "
                " You walked back into the school and walked around. "
                scene black with dissolve
                " You spent the rest of the break just wandering around the school. "
                " Just scrolling on your phone... "
                " You didn't really see anything that caught your attention. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked into your classroom after a bit of walking. "
                pause 2.0
                jump ocphysicsfri
        elif matteknow == False and jamknow == True:
            x " Hey there, [name]! "
            ja " ...Hi, [name]. "
            $ matteknow = True
            ma " I'm Matte! "
            ma " I was just painting Jam over here! "
            ma " I thought the lighting looked pretty good here, so... "
            ma " I just wanted to capture my best friend's beauty! "
            ja " ...You don't have to say that about me... "
            ma " Oh, but I have to! "
            ma " You're the most prettiest thing I've laid my eyes on! "
            ma " And I'm not lying when I say that, hehe. "
            ja " ...You're too sweet. "
            ma " Nothing's wrong with being a little sweet, you know! "
            ja " I know. "
            ja " Just that... "
            ja " You know. "
            ma " Mhm, I do... "
            ma " But just know that I care for you a lot, okay? "
            ma " I won't let anyone's words change my view of you. "
            ja " ... "
            " Looks like they're pretty busy right now. "
            " You look at Matte's painting... "
            " It looks pretty well made so far. "
            " You wish you could get a painting of you. "
            " Matte would probably ask you for money if you asked though. "
            if mattelv >= 20 and jamlv >= 20:
                ja " Actually, uh... "
                ja " Matte. "
                hide matteneutral at bottom
                show mattesurprised at left
                ma " Hm? "
                ma " Yes, Jam? "
                ja " I have...something to tell you. "
                " Oh wait, what's this? "
                " You're gonna stay and listen for this. "
                " This is going to get really interesting. "
                ma " Really? let me hear it, then! "
                ma " Remember that you can tell me anything, okay? "
                ja " ... "
                ja " It's been a thing that I've been wanting to tell you for awhile now. "
                ja " Like, for a long time now. "
                ma " Oh, really? "
                ma " That's interesting... "
                ja " I know, right? "
                hide jamneutral at bottom
                show jamsad at right
                ja " But, um... "
                ja " God, I'm fumbling with my words here. "
                hide mattesurprised at bottom
                show matteneutral at left
                ma " It's okay, Jam! "
                ma " Take your time! "
                ja " ...Alright. "
                ja " (Deep breaths, Jam...) "
                ja " (This is the moment.) "
                ja " (Nothing to be afraid of.) "
                ja " ...So... "
                ja " Like I said, this thing has been in my head for awhile now. "
                ja " And...I decided that I should tell you about this today. "
                ja " It's a little nerve-wracking for me, but... "
                ja " I know I have to say this to you at some point. "
                ja " I just can't keep these thoughts bottled up anymore. "
                ja " Uh... "
                ja " You know, Matte... "
                ja " You've been...affecting my life greatly. "
                ja " In a positive way, of course. "
                ja " I've been catching myself to be more positive at times... "
                ja " And I've been looking at nature more often and appreciating the smallest things in life. "
                ja " That's how much I've been feeling better because of you, Matte. "
                ja " You've made me feel things that I've never felt before. "
                ja " And I'm glad that you changed my life like this. "
                ja " I don't know how to thank you, but um... "
                " Jam holds out some flowers that she picked out for her. "
                ma " Aww, these are for me...? "
                ja " Mhm. "
                ja " I picked them out just for you. "
                ja " And...I have something else to admit. "
                ma " Oh? "
                ja " ...I have to admit that I... "
                ja " ...I really... "
                " You can do it Jam. "
                hide jamsad at bottom
                show jamhappy at right
                stop music
                hide matteneutral at bottom
                show mattesurprised at left
                ja " I really, really like you. "
                ja " And I mean that in a non-friend way. "
                ma " ...! "
                ma " Hold on, Jam...you...? "
                play music "audio/emotionalmoment.mp3" fadein 1.5
                ja " Yes, I have... "
                ja " I've been liking you for awhile now. "
                ja " At first, I denied it. "
                ja " With...you know how my mother is. "
                ja " But I slowly started accepting it. "
                ja " Accepting the feelings I felt. "
                ja " I've been struggling to say these words to you for awhile now, but here I am... "
                ja " If you don't wish to be THAT way with me, I'm fine with sticking as friends. "
                ja " But, I still have to ask the question... "
                ja " Will you be my girlfriend, and make me the luckiest girl alive? "
                hide mattesurprised at bottom
                show mattesad at left
                ma " Jam, I... "
                ma " I never knew you felt this way. "
                ma " I always thought that you were into guys, considering how you acted, but... "
                ma " Now knowing how you feel about me... "
                ma " I think I can say my answer now... "
                hide mattesad at bottom
                show mattehappy at left
                ma " Yes, I'll be your girlfriend! " with vpunch
                ma " I don't care what anyone says about us... "
                ma " As long as I'm with you, I feel my best! "
                ja " ...Same with me. "
                ja " I'm glad you said yes... "
                ja " I was actually a little worried that you wouldn't. "
                ma " Why would I? "
                ma " You're literally the best person I could ever ask for! "
                ma " How could I reject you, Jam? "
                if mattelv >= 30 or mattelv == 30:
                    " Aww, what a sweet ending... "
                    " You didn't want to ruin the moment by being there, though. "
                    " And you also didn't want to be a third wheel in this. "
                    " You walked back into the school and walked around. "
                    scene black with dissolve
                    " You spent the rest of the break just wandering around the school. "
                    " Just scrolling on your phone... "
                    " You didn't really see anything that caught your attention. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked into your classroom after a bit of walking. "
                    pause 2.0
                    jump ocphysicsfri
                elif jamlv >= 30 or jamlv == 30:
                    ja " You're...way too sweet. "
                    ja " That's one of the things that I love about you. "
                    ma " Hehe, aww!! "
                    ma " I think I'm gonna go tell my dad about this! "
                    ma " He's gonna be so happy to hear the news! "
                    ma " I'll see you later, hun!! "
                    ja " S...see you. "
                    hide mattehappy at right with easeoutright
                    show jamhappy at center with move
                    " Woah, nicknames already? "
                    " They're going with this fast, but it's sweet to hear. "
                    " Looks like Jam has to say something to you, though. "
                    " Let's see what she has to say about this... "
                    hide jamhappy at bottom
                    show jamneutral at center
                    ja " ...[name]. "
                    ja " I have something to say to you, too. "
                    ja " I'd like to thank you for being there for me. "
                    ja " Even if I haven't known you well enough... "
                    ja " You've been the absolute best for me, lately. "
                    ja " And, I feel like... "
                    ja " Maybe, if you feel like it... "
                    ja " We could be best friends? "
                    ja " It's fine if you don't want to, of course. "
                    menu:
                        " Besties!! and congratulations!! ":
                            $ jamsend.grant()
                            hide jamneutral at bottom
                            show jamhappy at center
                            ja " ...I'm glad that you'd want to be best friends. "
                            ja " And, thank you. For the congrats. "
                            ja " This might just be the greatest day of my life... "
                            ja " And I wouldn't have gotten here without you. "
                            scene jamend with dissolve
                            " Congratulations! You've gotten Jam's ending! "
                            " And her sweet achievement. Check your achievements tab! "
                            " I think i might just cry after that ending. "
                            " This whole thing was just so sweet! "
                            jump credits
                        " Normal friends, and congrats!! ":
                            ja " Reasonable. We only have known eachother for four days. "
                            ja " And, thanks... "
                            ja " This might just be the greatest day of my life. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Jam. "
                            " You were pretty happy that Jam got herself a nice girlfriend. "
                            " Good for her! good for her. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked back into the school and went to your classroom. "
                            pause 2.0
                            jump ocphysicsfri
                else:
                    " Aww, what a sweet ending... "
                    " You didn't want to ruin the moment by being there, though. "
                    " And you also didn't want to be a third wheel in this. "
                    " You walked back into the school and walked around. "
                    scene black with dissolve
                    " You spent the rest of the break just wandering around the school. "
                    " Just scrolling on your phone... "
                    " You didn't really see anything that caught your attention. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked into your classroom after a bit of walking. "
                    pause 2.0
                    jump ocphysicsfri
            else:
                " Maybe it's best to leave them alone for now. "
                " It looked like they had something important to do right now. "
                " Besides, they look pretty cute together at the moment. "
                " You walked back into the school and walked around. "
                scene black with dissolve
                " You spent the rest of the break just wandering around the school. "
                " Just scrolling on your phone... "
                " You didn't really see anything that caught your attention. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked into your classroom after a bit of walking. "
                pause 2.0
                jump ocphysicsfri
        else:
            x " Hey there, [name]! "
            ja " ...Hi, [name]. "
            $ matteknow = True
            ma " I'm Matte! "
            ma " I was just painting Jam over here! "
            ma " I thought the lighting looked pretty good here, so... "
            ma " I just wanted to capture my best friend's beauty! "
            ja " ...You don't have to say that about me... "
            ma " Oh, but I have to! "
            ma " You're the most prettiest thing I've laid my eyes on! "
            ma " And I'm not lying when I say that, hehe. "
            ja " ...You're too sweet. "
            ma " Nothing's wrong with being a little sweet, you know! "
            ja " I know. "
            ja " Just that... "
            ja " You know. "
            ma " Mhm, I do... "
            ma " But just know that I care for you a lot, okay? "
            ma " I won't let anyone's words change my view of you. "
            ja " ... "
            " Looks like they're pretty busy right now. "
            " You look at Matte's painting... "
            " It looks pretty well made so far. "
            " You wish you could get a painting of you. "
            " Matte would probably ask you for money if you asked though. "
            " Maybe it's best to leave them alone for now. "
            " It looked like they had something important to do right now. "
            " Besides, they look pretty cute together at the moment. "
            " You walked back into the school and walked around. "
            scene black with dissolve
            " You spent the rest of the break just wandering around the school. "
            " Just scrolling on your phone... "
            " You didn't really see anything that caught your attention. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked into your classroom after a bit of walking. "
            pause 2.0
            jump ocphysicsfri

    label ocfriback4:
        # spark and temero's ending, seperated
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of the school and found two of your classmates doing their own things. "
        " Who would you like to talk to for this break? "
        if sparkknow == True and temeroknow == True:
            menu:
                " {image=sparkicon} Spark {image=sparkicon} ":
                    jump mylittlespark
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump mylittletemero
        elif sparkknow == True and temeroknow == False:
            menu:
                " {image=sparkicon} Spark {image=sparkicon} ":
                    jump mylittlespark
                " {image=temeroicon} A science-y looking girl {image=temeroicon} ":
                    jump mylittletemero
        elif sparkknow == False and temeroknow == True:
            menu:
                " {image=sparkicon} A guy with an antenna and a tail {image=sparkicon} ":
                    jump mylittlespark
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump mylittletemero
        else:
            menu:
                " {image=sparkicon} A guy with an antenna and a tail {image=sparkicon} ":
                    jump mylittlespark
                " {image=temeroicon} A science-y looking girl {image=temeroicon} ":
                    jump mylittletemero
        label mylittlespark:
            show sparkneutral at center with easeinleft
            if sparkknow == True:
                pause 0.1
                if sparklv >= 30 or sparklv == 30:
                    " You walked over to him and asked him what he was doing. "
                    " He seemed a little surprised to see you here... "
                    " He calmed down after a bit though. "
                    sp " [name]... "
                    sp " I'm sorry, I didn't notice you. "
                    sp " I was just in deep thought. "
                    sp " Uh... "
                    sp " Just thinking about all the homework I missed. "
                    sp " Yeah, surprisingly I missed some homework again. "
                    sp " Pretty embarrassing, I know... "
                    sp " But uh... "
                    sp " I think I'll get working on them next break. "
                    sp " I don't want to fail some classes, after all. "
                    sp " Failing classes would be horrible, honestly... "
                    sp " I wouldn't want to expirience that at all. "
                    " ...You could tell that he was trying to hide something from you. "
                    " You don't know what, but he was most definitely hiding something. "
                    " You have a feeling you should probably ask him what he's thinking about... "
                    " Maybe you should. "
                    " Yeah, you definitely should. "
                    " You told him that his lies weren't really going to bait you. "
                    sp " ... "
                    sp " ...Okay, sorry for trying to lie to you there. "
                    sp " I just didn't know what to say, in all honesty. "
                    sp " But uh... "
                    sp " The only thing that I wasn't lying about is the fact that I was thinking about something. "
                    sp " I was...thinking about asking you something. "
                    sp " And that thing is... "
                    sp " Would you want to be best friends with me? "
                    sp " It's okay if you don't want to, I know we've only known eachother for four days. "
                    sp " But...you've been really great to me, you know? "
                    sp " Been listening to everything I say...and all that. "
                    sp " You're a nice fella to hang out with, really. "
                    sp " And I would really want to spend more time with you. "
                    sp " Uh...what do you say? you wanna be besties, or... "
                    menu:
                        " Besties!! ":
                            $ sparksend.grant()
                            hide sparkneutral at bottom
                            show sparkhappy at center
                            sp " ...That makes me happy. "
                            sp " I'm glad that we're best firends now... "
                            sp " Let's go hangout after today, alright? "
                            sp " Only if you're free though. "
                            sp " We could go get pizza and stuff... "
                            sp " And I'm paying. "
                            sp " Only if you don't decide to pull on my tail though. "
                            sp " That shit hurts. "
                            scene sparkend with dissolve
                            " Congratulations! You've gotten Spark's ending! "
                            " And his sweet achievement, too. Check your achievements tab! "
                            " What's also nice is that you get free pizza. "
                            " Yay! "
                            jump credits
                        " Normal friends please ":
                            sp " Okay...that's understandable. "
                            sp " Don't worry, I'm not mad or anything. "
                            sp " I'm glad you're being honest with me. "
                            sp " Uh... to not make this awkward... "
                            sp " Let's just talk about something else. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Spark. "
                            " Just talking to him about random things... "
                            " Nothing too special, in all honesty. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, looks like it's time for another class. "
                            " You walked back into the school and went to your classroom. "
                            pause 2.0
                            jump ocphysicsfri
                else:
                    " You walked over to him and asked him what he was doing. "
                    " He seemed a little surprised to see you here... "
                    " He calmed down after a bit though. "
                    sp " [name]... "
                    sp " I'm sorry, I didn't notice you. "
                    sp " I was just in deep thought. "
                    sp " Uh... "
                    sp " Just thinking about all the homework I missed. "
                    sp " Yeah, surprisingly I missed some homework again. "
                    sp " Pretty embarrassing, I know... "
                    sp " But uh... "
                    sp " I think I'll get working on them next break. "
                    sp " I don't want to fail some classes, after all. "
                    sp " Failing classes would be horrible, honestly... "
                    sp " I wouldn't want to expirience that at all. "
                    " ...You could tell that he was trying to hide something from you. "
                    " You don't know what, but he was most definitely hiding something. "
                    " You have a feeling you should probably ask him what he's thinking about... "
                    " But nah, maybe he really is struggling with some homework. "
                    " You told him that maybe you could help with some of his homework. "
                    sp " Oh, uh...sure. "
                    sp " Here's what it looks like. "
                    " ...Okay, wow. "
                    " This is some high effort lying here, but good job. "
                    " You're still gonna help him out with this, though. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Spark. "
                    " Just talking to him about random things... "
                    " Nothing too special, in all honesty. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump ocphysicsfri
            else:
                " You walked over to him and asked him what he was doing. "
                " He seemed a little surprised to see you here... "
                " He calmed down after a bit though. "
                x " [name]... "
                x " I'm sorry, I didn't notice you. "
                $ sparkknow = True
                sp " I'm Spark, by the way. "
                sp " I was just in deep thought. "
                sp " Uh... "
                sp " Just thinking about all the homework I missed. "
                sp " Yeah, surprisingly I missed some homework again. "
                sp " Pretty embarrassing, I know... "
                sp " But uh... "
                sp " I think I'll get working on them next break. "
                sp " I don't want to fail some classes, after all. "
                sp " Failing classes would be horrible, honestly... "
                sp " I wouldn't want to expirience that at all. "
                " ...You could tell that he was trying to hide something from you. "
                " You don't know what, but he was most definitely hiding something. "
                " You have a feeling you should probably ask him what he's thinking about... "
                " But nah, maybe he really is struggling with some homework. "
                " You told him that maybe you could help with some of his homework. "
                sp " Oh, uh...sure. "
                sp " Here's what it looks like. "
                " ...Okay, wow. "
                " This is some high effort lying here, but good job. "
                " You're still gonna help him out with this, though. "
                scene black with dissolve
                " You spent the rest of the break talking with Spark. "
                " Just talking to him about random things... "
                " Nothing too special, in all honesty. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump ocphysicsfri
        label mylittletemero:
            show temeroneutral at center with easeinright
            if temeroknow == True:
                pause 0.1
                if temerolv >= 30 or temerolv == 30:
                    " You walked over to her and asked her what she was doing. "
                    " Looked like she was doing something important. "
                    " Hopefully you weren't disrupting her or anything! "
                    tm " Oh, hey there [name]! "
                    tm " Just working on a new potion, as you can see. "
                    tm " I've been working on this one really hard this week! "
                    tm " There have been multiple failures, but... "
                    tm " I think I've finally gotten it! "
                    tm " I've finally got everything right for once! "
                    tm " Now, all I need is a test subject... "
                    tm " I don't want to test it on you, of course. "
                    tm " What if it explodes? "
                    tm " I'm pretty sure the principal won't be too happy about that, hehe. "
                    tm " Hmmm, let's see... "
                    tm " What could I use as a test subject? "
                    " You looked around for anything that could be used as a test subject... "
                    " Something that isn't alive. "
                    " Let's see what else you can look at.... "
                    " You then pointed at a mushroom on the ground. "
                    " Technically, it is somewhat alive, but... "
                    " It's like a plant or something, so it should be a good test subject. "
                    tm " That tiny mushroom over there? "
                    tm " Alrighty, if you say so! "
                    tm " Now let me just drop a little bit of this on there... "
                    tm " Hopefully this doesn't explode. "
                    " She pours a drop of her potion onto the mushroom. "
                    " You waited for something to happen... "
                    " And then after a bit, the mushroom slowly turned into a nice rose. "
                    tm " See? it worked! "
                    tm " Finally, it didn't explode or anything-{nw} "
                    " It exploded. " with vpunch
                    hide temeroneutral at bottom
                    show temeroangry at center
                    tm " ... "
                    tm " Well, atleast it worked only for a little bit. "
                    hide temeroangry at bottom
                    show temeroneutral at center
                    tm " ...Hey, [name]. "
                    tm " During these four days... "
                    tm " I've realized something. "
                    tm " You've been listening to all of my stories... "
                    tm " Checking out all of the potions I've been making... "
                    tm " And no matter what I did or said... "
                    tm " You stuck there by my side. "
                    tm " I'm honestly happy to have you here with me, and... "
                    tm " I have just one simple question to ask you. "
                    tm " Would you like to be my best friend? "
                    menu:
                        " SCIENCE RULES ":
                            $ temerosend.grant()
                            hide temeroneutral at bottom
                            show temerohappy at center
                            tm " Great minds think alike! "
                            tm " Good choice. "
                            tm " I've realized something... "
                            tm " No potion's power can compare to the feeling of having a best friend by your side. "
                            tm " And that best friend is YOU! "
                            tm " Let's go do some more expiriments, okay? "
                            scene temeroend with dissolve
                            " Congratulations, you've gotten Temero's ending! "
                            " And her sweet achievement, check your achievements tab! "
                            " You and Temero do some weird expiriements every now and then. "
                            " But are they fun? absolutely. "
                            jump credits
                        " Normal friends vro ":
                            tm " Understandable, actually. "
                            tm " It's only been four days, after all! "
                            tm " But who knows... "
                            tm " Maybe you'll change your mind? "
                            tm " Okay, no. "
                            tm " I'm not that desperate for a best friend. "
                            scene black with dissolve
                            " You spent the rest of the break just talking with Temero. "
                            " Just talking about random stuff... "
                            " Nothing too special. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, looks like it's time for another class. "
                            " You walked back into the school and went to your classroom. "
                            pause 2.0
                            jump ocphysicsfri
                else:
                    " You walked over to her and asked her what she was doing. "
                    " Looked like she was doing something important. "
                    " Hopefully you weren't disrupting her or anything! "
                    tm " Oh, hey there [name]! "
                    tm " Just working on a new potion, as you can see. "
                    tm " I've been working on this one really hard this week! "
                    tm " There have been multiple failures, but... "
                    tm " I think I've finally gotten it! "
                    tm " I've finally got everything right for once! "
                    tm " Now, all I need is a test subject... "
                    tm " I don't want to test it on you, of course. "
                    tm " What if it explodes? "
                    tm " I'm pretty sure the principal won't be too happy about that, hehe. "
                    tm " Hmmm, let's see... "
                    tm " What could I use as a test subject? "
                    " You looked around for anything that could be used as a test subject... "
                    " Something that isn't alive. "
                    " Let's see what else you can look at.... "
                    " You then pointed at a mushroom on the ground. "
                    " Technically, it is somewhat alive, but... "
                    " It's like a plant or something, so it should be a good test subject. "
                    tm " That tiny mushroom over there? "
                    tm " Alrighty, if you say so! "
                    tm " Now let me just drop a little bit of this on there... "
                    tm " Hopefully this doesn't explode. "
                    " She pours a drop of her potion onto the mushroom. "
                    " You waited for something to happen... "
                    " And then after a bit, the mushroom slowly turned into a nice rose. "
                    tm " See? it worked! "
                    tm " Finally, it didn't explode or anything-{nw} "
                    " It exploded. " with vpunch
                    hide temeroneutral at bottom
                    show temeroangry at center
                    tm " ... "
                    tm " Well, atleast it worked only for a little bit. "
                    hide temeroangry at bottom
                    show temeroneutral at center
                    tm " I guess I'll just keep working! "
                    tm " You can watch me if you want to. "
                    tm " I don't mind! "
                    scene black with dissolve
                    " You spent the rest of the break just talking with Temero. "
                    " Just talking about random stuff... "
                    " Nothing too special. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump ocphysicsfri
            else:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was doing something important. "
                " Hopefully you weren't disrupting her or anything! "
                x " Oh, hey there [name]! "
                x " I don't think we've met before, hm... "
                $ temeroknow = True
                tm " I'm Temero, it's nice to meet you! "
                tm " Just working on a new potion, as you can see. "
                tm " I've been working on this one really hard this week! "
                tm " There have been multiple failures, but... "
                tm " I think I've finally gotten it! "
                tm " I've finally got everything right for once! "
                tm " Now, all I need is a test subject... "
                tm " I don't want to test it on you, of course. "
                tm " What if it explodes? "
                tm " I'm pretty sure the principal won't be too happy about that, hehe. "
                tm " Hmmm, let's see... "
                tm " What could I use as a test subject? "
                " You looked around for anything that could be used as a test subject... "
                " Something that isn't alive. "
                " Let's see what else you can look at.... "
                " You then pointed at a mushroom on the ground. "
                " Technically, it is somewhat alive, but... "
                " It's like a plant or something, so it should be a good test subject. "
                tm " That tiny mushroom over there? "
                tm " Alrighty, if you say so! "
                tm " Now let me just drop a little bit of this on there... "
                tm " Hopefully this doesn't explode. "
                " She pours a drop of her potion onto the mushroom. "
                " You waited for something to happen... "
                " And then after a bit, the mushroom slowly turned into a nice rose. "
                tm " See? it worked! "
                tm " Finally, it didn't explode or anything-{nw} "
                " It exploded. " with vpunch
                hide temeroneutral at bottom
                show temeroangry at center
                tm " ... "
                tm " Well, atleast it worked only for a little bit. "
                hide temeroangry at bottom
                show temeroneutral at center
                tm " I guess I'll just keep working! "
                tm " You can watch me if you want to. "
                tm " I don't mind! "
                scene black with dissolve
                " You spent the rest of the break just talking with Temero. "
                " Just talking about random stuff... "
                " Nothing too special. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump ocphysicsfri
    label ocfrigym4:
        # disk and quinn
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked to the gym and spotted two of your classmates talking to eachother. "
        " Wondering what they're doing, you walked over to them. "
        show diskneutral at left with easeinright
        show quinnneutral at right with easeinright
        if diskknow == True and quinnknow == True:
            d " Hi there, [name]!! "
            q " Hello there, [name]. "
            d " It's nice to see you here!! "
            d " I was just cheering for my brother over here! "
            d " You see... "
            d " It's his play next break! "
            d " I'm gonna go and see his play, like I always do! "
            d " All of them are so great and wonderful... "
            q " Aww, you don't have to say all that stuff about my plays. "
            q " They're just things that I came up in my head. "
            q " Nothing more. "
            d " So you're saying that all of those works of art come from your head? "
            q " Yup. "
            q " Every artist's ideas starts forming in their mind. "
            q " That's how they get their ideas. "
            d " I know that, but still... "
            d " It's uneblievable that you can come up with such amazing things! "
            d " Really, you're so cool, lil bro!! "
            q " Thanks, big bro. "
            q " I'll be delighted to see you at my performance. "
            d " And I'll be cheering for you while you perform! "
            d " I hope I don't accidentally cheer too loud, though... "
            q " Haha, yeah. "
            q " Like that one time you got so excited... "
            q " You screamed to the top of your lungs. "
            q " I actually found that a little bit endearing. "
            d " Huh? really? "
            d " I found that embarrassing, huhuuuu... "
            d " It was so quiet, too! "
            d " Everyone was probably so focused, and then I just... "
            q " Disk, it's okay. "
            q " You were just happy to see me perform so well. "
            q " But, you've gotta promise me and my other club members... "
            q " That you don't do that again. "
            q " I mean, you can do it, just a little lower. "
            q " It pretty much distracts us. "
            d " Understood! "
            d " Just have to remind me to do it lowly! "
            q " I'll be sure to remind you later. "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Quinn. "
            " Just talking about the play and all of that... "
            " Nothing too special, in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked out of the gym and went to your classroom. "
            pause 2.0
            jump ocphysicsfri
        elif diskknow == True and quinnknow == False:
            d " Hi there, [name]!! "
            x " Hello there, [name]. "
            d " It's nice to see you here!! "
            $ quinnknow = True
            d " I was just cheering for my brother over here! "
            d " You see... "
            d " It's his play next break! "
            d " I'm gonna go and see his play, like I always do! "
            d " All of them are so great and wonderful... "
            q " Aww, you don't have to say all that stuff about my plays. "
            q " They're just things that I came up in my head. "
            q " Nothing more. "
            d " So you're saying that all of those works of art come from your head? "
            q " Yup. "
            q " Every artist's ideas starts forming in their mind. "
            q " That's how they get their ideas. "
            d " I know that, but still... "
            d " It's uneblievable that you can come up with such amazing things! "
            d " Really, you're so cool, lil bro!! "
            q " Thanks, big bro. "
            q " I'll be delighted to see you at my performance. "
            d " And I'll be cheering for you while you perform! "
            d " I hope I don't accidentally cheer too loud, though... "
            q " Haha, yeah. "
            q " Like that one time you got so excited... "
            q " You screamed to the top of your lungs. "
            q " I actually found that a little bit endearing. "
            d " Huh? really? "
            d " I found that embarrassing, huhuuuu... "
            d " It was so quiet, too! "
            d " Everyone was probably so focused, and then I just... "
            q " Disk, it's okay. "
            q " You were just happy to see me perform so well. "
            q " But, you've gotta promise me and my other club members... "
            q " That you don't do that again. "
            q " I mean, you can do it, just a little lower. "
            q " It pretty much distracts us. "
            d " Understood! "
            d " Just have to remind me to do it lowly! "
            q " I'll be sure to remind you later. "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Quinn. "
            " Just talking about the play and all of that... "
            " Nothing too special, in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked out of the gym and went to your classroom. "
            pause 2.0
            jump ocphysicsfri
        elif diskknow == False and quinnknow == True:
            x " Hi there, [name]!! "
            q " Hello there, [name]. "
            x " It's nice to see you here!! "
            $ diskknow = True
            d " I'm Disk! it's nice to meet you! "
            d " I was just cheering for my brother over here! "
            d " You see... "
            d " It's his play next break! "
            d " I'm gonna go and see his play, like I always do! "
            d " All of them are so great and wonderful... "
            q " Aww, you don't have to say all that stuff about my plays. "
            q " They're just things that I came up in my head. "
            q " Nothing more. "
            d " So you're saying that all of those works of art come from your head? "
            q " Yup. "
            q " Every artist's ideas starts forming in their mind. "
            q " That's how they get their ideas. "
            d " I know that, but still... "
            d " It's uneblievable that you can come up with such amazing things! "
            d " Really, you're so cool, lil bro!! "
            q " Thanks, big bro. "
            q " I'll be delighted to see you at my performance. "
            d " And I'll be cheering for you while you perform! "
            d " I hope I don't accidentally cheer too loud, though... "
            q " Haha, yeah. "
            q " Like that one time you got so excited... "
            q " You screamed to the top of your lungs. "
            q " I actually found that a little bit endearing. "
            d " Huh? really? "
            d " I found that embarrassing, huhuuuu... "
            d " It was so quiet, too! "
            d " Everyone was probably so focused, and then I just... "
            q " Disk, it's okay. "
            q " You were just happy to see me perform so well. "
            q " But, you've gotta promise me and my other club members... "
            q " That you don't do that again. "
            q " I mean, you can do it, just a little lower. "
            q " It pretty much distracts us. "
            d " Understood! "
            d " Just have to remind me to do it lowly! "
            q " I'll be sure to remind you later. "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Quinn. "
            " Just talking about the play and all of that... "
            " Nothing too special, in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked out of the gym and went to your classroom. "
            pause 2.0
            jump ocphysicsfri
        else:
            x " Hi there, [name]!! "
            x " Hello there, [name]. "
            x " It's nice to see you here!! "
            $ diskknow = True
            d " I'm Disk! it's nice to meet you! "
            $ quinnknow = True
            d " I was just cheering for my brother over here! "
            d " You see... "
            d " It's his play next break! "
            d " I'm gonna go and see his play, like I always do! "
            d " All of them are so great and wonderful... "
            q " Aww, you don't have to say all that stuff about my plays. "
            q " They're just things that I came up in my head. "
            q " Nothing more. "
            d " So you're saying that all of those works of art come from your head? "
            q " Yup. "
            q " Every artist's ideas starts forming in their mind. "
            q " That's how they get their ideas. "
            d " I know that, but still... "
            d " It's uneblievable that you can come up with such amazing things! "
            d " Really, you're so cool, lil bro!! "
            q " Thanks, big bro. "
            q " I'll be delighted to see you at my performance. "
            d " And I'll be cheering for you while you perform! "
            d " I hope I don't accidentally cheer too loud, though... "
            q " Haha, yeah. "
            q " Like that one time you got so excited... "
            q " You screamed to the top of your lungs. "
            q " I actually found that a little bit endearing. "
            d " Huh? really? "
            d " I found that embarrassing, huhuuuu... "
            d " It was so quiet, too! "
            d " Everyone was probably so focused, and then I just... "
            q " Disk, it's okay. "
            q " You were just happy to see me perform so well. "
            q " But, you've gotta promise me and my other club members... "
            q " That you don't do that again. "
            q " I mean, you can do it, just a little lower. "
            q " It pretty much distracts us. "
            d " Understood! "
            d " Just have to remind me to do it lowly! "
            q " I'll be sure to remind you later. "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Quinn. "
            " Just talking about the play and all of that... "
            " Nothing too special, in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked out of the gym and went to your classroom. "
            pause 2.0
            jump ocphysicsfri
    label ocfricafeteria4:
        # nox and orchid's ending, seperated
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked to the cafeteria and spotted two of your classmates doing their own things. "
        " Who would you like to talk to? "
        if noxknow == True and jacobknow == True:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump huehuenox
                " {image=jacobicon} Jacob {image=jacobicon} ":
                    jump huehuejacob
        elif noxknow == True and jacobknow == False:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump huehuenox
                " {image=jacobicon}  {image=jacobicon} ":
                    jump huehuejacob
        elif noxknow == False and jacobknow == True:
            menu:
                " {image=noxicon} A sleepy guy {image=noxicon} ":
                    jump huehuenox
                " {image=jacobicon} A guy with goggles and a mask {image=jacobicon} ":
                    jump huehuejacob
        else:
            menu:
                " {image=noxicon} A sleepy guy {image=noxicon} ":
                    jump huehuenox
                " {image=jacobicon} A guy with goggles and a mask {image=jacobicon} ":
                    jump huehuejacob
        label huehuenox:
            show noxneutral at center with easeinleft
            if noxknow == True:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was bored and had nothing to do. "
                n " Hi there, [name]... "
                n " I've been getting kind of bored lately... "
                n " Like a whole lot bored... "
                n " Things are honestly boring without sleeping... "
                n " I can get the most wildest dreams... "
                n " Anything I could want could be true... "
                n " But I've been kind of stuck here and thinking... "
                n " And not sleeping at all. "
                n " I could sleep right now, but... "
                n " The only problem is that I can't sleep. "
                n " My body won't allow me to. "
                n " Since, you know...meds and stuff. "
                n " They prevent me from sleeping too much, basically. "
                n " And I can't really do anything about it if I take them... "
                n " It just makes me less sleepy. "
                n " Sigh... "
                n " I already just want to go to my bed... "
                n " I just want this school day to be over, in all honesty... "
                if noxlv >= 30 or noxlv == 30:
                    n " But... "
                    n " I also don't want to go back... "
                    n " I just want to stay here, with you... "
                    n " You're one of the people who actually make me feel really comfortable... "
                    n " You listen to whatever I talk to... "
                    n " Even though we haven't known eachother for a long time... "
                    n " You've made me feel so...so... "
                    n " ...So great, is all I can say. "
                    n " And, I really, really... "
                    n " ...Really want you to be my best friend. "
                    n " What do you say to that? "
                    menu:
                        " Sleepover bestie!! ":
                            $ noxsend.grant()
                            hide noxneutral at bottom
                            show noxhappy at center
                            n " ...I'm glad that you said that. "
                            n " And also...sleepover besties? "
                            n " Would you really want to have a sleepover with me? "
                            n " I'm sure I'd fall asleep first. "
                            n " But...if that's what you want, then... "
                            n " I'm fine with it. "
                            scene noxend with dissolve
                            " Congratulations! you'e gotten Nox's ending! "
                            " And his sweet achievement, too. "
                            " Check your achievements tab! "
                            " You and Nox are gonna have a sleep over next saturday. "
                            " Sweet. "
                            jump credits
                        " Normal friends! ":
                            n " Eehh... understandable... "
                            n " I mean, we've only known eachother for four days... "
                            n " It's fine if you want to take it slow... "
                            n " Let's talk about something else to not make it awkward... "
                            scene black with dissolve
                            " You spent the rest of the break talking with Nox. "
                            " Just talking to him about dreams he's had... "
                            " Nothing too special, in your opinion. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked out of the cafeteria and went to your classrom. "
                            pause 2.0
                            jump ocphysicsfri
                else:
                    " You walked over to him and asked him what he was doing. "
                    " Looked like he was bored and had nothing to do. "
                    n " Hi there, [name]... "
                    n " I've been getting kind of bored lately... "
                    n " Like a whole lot bored... "
                    n " Things are honestly boring without sleeping... "
                    n " I can get the most wildest dreams... "
                    n " Anything I could want could be true... "
                    n " But I've been kind of stuck here and thinking... "
                    n " And not sleeping at all. "
                    n " I could sleep right now, but... "
                    n " The only problem is that I can't sleep. "
                    n " My body won't allow me to. "
                    n " Since, you know...meds and stuff. "
                    n " They prevent me from sleeping too much, basically. "
                    n " And I can't really do anything about it if I take them... "
                    n " It just makes me less sleepy. "
                    n " Sigh... "
                    n " I already just want to go to my bed... "
                    n " I just want this school day to be over, in all honesty... "
                    n " School can get so boring just so quickly... "
                    n " Unless if you talk with someone to pass the time... "
                    n " Like you, for example... "
                    n " It's nice talking to you, in all honesty... "
                    n " Talking to people can be a nice time waster. "
                    n " Uh...we could talk aboutttt...  "
                    n " Maybe talk about the dreams I've had...? "
                    n " I've had a whole lot new interesting ones... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Nox. "
                    " Just talking to him about dreams he's had... "
                    " Nothing too special, in your opinion. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the cafeteria and went to your classrom. "
                    pause 2.0
                    jump ocphysicsfri
            else:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was bored and had nothing to do. "
                x " Hi there, [name]... "
                x " I don't think I've introduced myself to you yet... "
                $ noxknow = True
                n " I'm Nox, Nox cesso... "
                n " I've been getting kind of bored lately... "
                n " Like a whole lot bored... "
                n " Things are honestly boring without sleeping... "
                n " I can get the most wildest dreams... "
                n " Anything I could want could be true... "
                n " But I've been kind of stuck here and thinking... "
                n " And not sleeping at all. "
                n " I could sleep right now, but... "
                n " The only problem is that I can't sleep. "
                n " My body won't allow me to. "
                n " Since, you know...meds and stuff. "
                n " They prevent me from sleeping too much, basically. "
                n " And I can't really do anything about it if I take them... "
                n " It just makes me less sleepy. "
                n " Sigh... "
                n " I already just want to go to my bed... "
                n " I just want this school day to be over, in all honesty... "
                n " School can get so boring just so quickly... "
                n " Unless if you talk with someone to pass the time... "
                n " Like you, for example... "
                n " It's nice talking to you, in all honesty... "
                n " Talking to people can be a nice time waster. "
                n " Uh...we could talk aboutttt...  "
                n " Maybe talk about the dreams I've had...? "
                n " I've had a whole lot new interesting ones... "
                scene black with dissolve
                " You spent the rest of the break talking with Nox. "
                " Just talking to him about dreams he's had... "
                " Nothing too special, in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classrom. "
                pause 2.0
                jump ocphysicsfri
        label huehuejacob:
            show jacobneutral at center with easeinleft
            if jacobknow == True:
                pause 0.1
                if jacoblv >= 30 or jacoblv == 30:
                    " You walked over to him and asked him what he was doing. "
                    " Looked like he was thinking about something deeply... "
                    " You wonder what's on his mind. "
                    jac " Hello there, [name]. "
                    jac " I have...something to ask of you. "
                    jac " Just a simple question. "
                    jac " But first, I've gotta explain something else to you. "
                    jac " During these past four days... "
                    jac " You've been talking with me normally and all that. "
                    jac " Listening to everything I say... "
                    jac " And not running away. "
                    jac " Some people think that I'm too intimidating to talk to. "
                    jac " Some people have spread many false things about me. "
                    jac " But you? "
                    jac " You didn't do any of that. "
                    jac " You stayed, despite the way I act. "
                    jac " All I can ask is why, but... "
                    jac " At the same time...I'm also thankful for you being there for me. "
                    jac " When others have not. "
                    jac " I'm really thankful for that. "
                    jac " And, uh... "
                    jac " I've been thinking about this for the past few minutes now. "
                    jac " Would you want to be best friends with me? "
                    jac " It's okay if you don't want to. "
                    menu:
                        " Best friends bro ":
                            $ jacobsend.grant()
                            hide jacobneutral at bottom
                            show jacobhappy at center
                            jac " I'm...glad to hear that. "
                            jac " Hey, if you want to hangout later... "
                            jac " I'm completely fine with that. "
                            jac " We can do whatever you want. "
                            scene jacobend with dissolve
                            " Congratulations! you've gotten Jacob's ending! "
                            " And his sweet achievement, too. "
                            " Check your achievements tab! "
                            jump credits
                        " Normal friends bro ":
                            jac " Understandable. "
                            jac " I mean, we've only known eachother for four days... "
                            jac " So, I understand. "
                            jac " Uh...let's just talk about something else. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Jacob. "
                            " Just talking about random things... "
                            " Nothing too special, in your opinion. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked out of the cafeteria and went to your classrom. "
                            pause 2.0
                            jump ocphysicsfri
                else:
                    " You were about to ask him what he was doing, but... "
                    " It looked like he was busy doing something. "
                    " You decided not to disturb him. "
                    " You were planning to play on your phone, anyway. "
                    " You pulled out your phone and started playing some random game on it. "
                    scene black with dissolve
                    " You spent the rest of the break playing with your phone. "
                    " Just playing games on your phone... "
                    " Nothing too special, really. "
                    pause 2.0
                    jump ocphysicsfri
            else:
                " You were about to ask him what he was doing, but... "
                " It looked like he was busy doing something. "
                " You decided not to disturb him. "
                " You were planning to play on your phone, anyway. "
                " You pulled out your phone and started playing some random game on it. "
                scene black with dissolve
                " You spent the rest of the break playing with your phone. "
                " Just playing games on your phone... "
                " Nothing too special, really. "
                pause 2.0
                jump ocphysicsfri
    label ocfrirooftop4:
        # orchid and carmen's ending, seperated
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked up to the rooftop and spotted two of your classmates doing their own things. "
        " Who would you like to talk to for this break? "
        if orchidknow == True and carmenknow == True:
            menu:
                " {image=orchidicon} Orchid {image=orchidicon} ":
                    jump orchidball
                " {image=carmenicon} Carmen {image=carmenicon} ":
                    jump carmenball
        elif orchidknow == True and carmenknow == False:
            menu:
                " {image=orchidicon} Orchid {image=orchidicon} ":
                    jump orchidball
                " {image=carmenicon} A kid with a guitar {image=carmenicon} ":
                    jump carmenball
        elif orchidknow == False and carmenknow == True:
            menu:
                " {image=orchidicon} A scene kid {image=orchidicon} ":
                    jump orchidball
                " {image=carmenicon} Carmen {image=carmenicon} ":
                    jump carmenball
        else:
            menu:
                " {image=orchidicon} A scene kid {image=orchidicon} ":
                    jump orchidball
                " {image=carmenicon} A kid with a guitar {image=carmenicon} ":
                    jump carmenball
        label orchidball:
            show orchidneutral at center with easeinleft
            if orchidknow == True:
                " You walked over to them and asked them what they're doing. "
                " Looked like they were staring up the clouds, thinking about something... "
                " But you wonder what could it be that they're thinking about. "
                oc " Heya there, [name]! "
                oc " I was just relaxing up here and thinking... "
                oc " Sounds boring, but! "
                oc " It's actually quite refreshing when you think in a quiet place, don't you think? "
                oc " It just leaves you and your thoughts alone... "
                oc " No noise, no disturbances... "
                oc " Feels really nice to just think so clearly without my mind being all jumbled up! "
                oc " Hmhmmm... "
                oc " ...You know, [name]... "
                oc " I think we should appreciate the little things in life. "
                oc " Appreciate the fact that we get to see beautiful sights like the clouds... "
                oc " Appreciate getting to see and meet nice people... "
                oc " Appreciate having all of your nice friends caring for you, no matter what... "
                oc " Appreciate having your family love you no matter what... "
                oc " Appreciate having the chance to be alive, you know? "
                oc " A lot of people don't think that way, for a fact. "
                oc " They're all too busy doing their own thing. "
                oc " Like focusing on work and school, getting stressed about it... "
                oc " But sometimes, all you need is a good break, and that's okay. "
                oc " Maybe you just need to sit and think for a good while before making a decision. "
                oc " I know that it's easier said than done, but... "
                oc " Maybe someday in the future my words will make someone listen to them. "
                oc " Just someday, not right now. "
                if orchidlv >= 30 or orchidlv == 30:
                    oc " And I'd also like to appreciate the fact that I got to meet you. "
                    oc " Even if you felt like you did nothing... "
                    oc " You were there to listen to me talk about the most randomest things. "
                    oc " And you were even there at my lowest. "
                    oc " You were there to witness it all. "
                    oc " But did you ever leave because of all of it? "
                    oc " You didn't. You stayed. "
                    oc " And I appreciate you for doing that. "
                    oc " Now, there's one thing I'd like to ask you... "
                    oc " Even though we've only known eachother for four days... "
                    oc " Would you like to be my best friend? "
                    menu:
                        " Yess!! ":
                            $ orchidsend.grant()
                            hide orchidneutral at bottom
                            show orchidhappy at center
                            oc " I'm glad...! "
                            oc " Maybe I could make some friendship bracelets if you want me to... "
                            oc " And we could do so much things together! "
                            oc " Well, only if you want to do those things together of course. "
                            oc " I'm glad to have met you! "
                            scene orchidend with dissolve
                            " Congratulations! You've gotten Orchid's ending! "
                            " And his sweet achievement. Check your achievements tab! "
                            " Orchid would sometimes give you some scene kid stuff, but... "
                            " You're okay with it, since you somewhat like the style. "
                            jump credits
                        " Normal friends, this is too fast ":
                            oc " Oh, too fast for you...? "
                            oc " That's okay, I understand. "
                            oc " Let's take it slow then, if that's what you want. "
                            oc " And to not make this any more awkward for me... "
                            oc " How about we talk about something else? "
                            scene black with dissolve
                            " You spent the rest of the break talking with Orchid. "
                            " Just talking about new games and stuff... "
                            " Nothing too special to you, in your opinion. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked down from the rooftop and went to your classroom. "
                            pause 2.0
                            jump ocphysicsfri
                else:
                    scene black with dissolve
                    " You spent the rest of the break talking with Orchid. "
                    " Just talking about new games and stuff... "
                    " Nothing too special to you, in your opinion. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked down from the rooftop and went to your classroom. "
                    pause 2.0
                    jump ocphysicsfri
            else:
                " You walked over to them and asked them what they're doing. "
                " Looked like they were staring up the clouds, thinking about something... "
                " But you wonder what could it be that they're thinking about. "
                x " Heya there, [name]! "
                $ orchidknow = True
                oc " I'm Orchid, it's nice to meet you! "
                oc " I was just relaxing up here and thinking... "
                oc " Sounds boring, but! "
                oc " It's actually quite refreshing when you think in a quiet place, don't you think? "
                oc " It just leaves you and your thoughts alone... "
                oc " No noise, no disturbances... "
                oc " Feels really nice to just think so clearly without my mind being all jumbled up! "
                oc " Hmhmmm... "
                oc " ...You know, [name]... "
                oc " I think we should appreciate the little things in life. "
                oc " Appreciate the fact that we get to see beautiful sights like the clouds... "
                oc " Appreciate getting to see and meet nice people... "
                oc " Appreciate having all of your nice friends caring for you, no matter what... "
                oc " Appreciate having your family love you no matter what... "
                oc " Appreciate having the chance to be alive, you know? "
                oc " A lot of people don't think that way, for a fact. "
                oc " They're all too busy doing their own thing. "
                oc " Like focusing on work and school, getting stressed about it... "
                oc " But sometimes, all you need is a good break, and that's okay. "
                oc " Maybe you just need to sit and think for a good while before making a decision. "
                oc " I know that it's easier said than done, but... "
                oc " Maybe someday in the future my words will make someone listen to them. "
                oc " Just someday, not right now. "
                scene black with dissolve
                " You spent the rest of the break talking with Orchid. "
                " Just talking about new games and stuff... "
                " Nothing too special to you, in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump ocphysicsfri
        label carmenball:
            show carmenneutral at center with easeinright
            if carmenknow == True:
                pause 0.1
                if carmenlv >= 30 or carmenlv == 30:
                    " You walked over to him and asked him what he was doing. "
                    " Looked like he was doing something with his guitar... "
                    " Just plucking the strings or getting ready to play a song. "
                    ca " ...! "
                    " He waved at you. "
                    " It felt as if he was waiting for you to come over to him. "
                    " Huh...wonder why. "
                    " Well, you're about to find out. "
                    ca " ... "
                    " Carmen lets out some gesutres to show that he's feeling pretty nervous right now. "
                    " Pretty nervous about telling you something. "
                    " He hesitates for a bit before doing some more gestures. "
                    ca " ... "
                    " He tells you that he's been thinking about telling you this for awhile now. "
                    " Ever since tuesday, he's been feeling better because of you. "
                    " He's been catching himself being way more happy than before... "
                    " All of that stuff. "
                    " And he's been thinking about this one specific question. "
                    " But he didn't know if it would be awkward or not... "
                    " Due to the fact that you guys have only known eachother for four days. "
                    " But, he feels like he's got enough confidence to ask you this. "
                    " He gestures to you: 'will you be my...' "
                    " He pulls out his phone and puts on a song called best friend. "
                    " Basically asking you to be his bestie. Do you? "
                    menu:
                        " HELL YEAH!! ":
                            $ carmensend.grant()
                            hide carmenneutral at bottom
                            show carmenhappy at center
                            ca " ...!! "
                            " Carmen seemed pretty surprised that you even said yes, but... "
                            " You could really tell that he felt really happy that you said that. "
                            " Great, now you've got a nice music buddy that's probably going to be popular in a few years. "
                            scene carmenend with dissolve
                            " Congratulations! You've gotten Carmen's ending! "
                            " And his sweet achievement. Look at your achievements tab! "
                            " You and Carmen make a pretty great duo, in my opinion. "
                            " Since you could talk sometimes (with my command), you two could make songs with lyrics. "
                            " I wouldn't say you're the best singer, but you were on the good side of singing. "
                            jump credits
                        " Normal friends, this is too fast ":
                            ca " ... "
                            " Carmen gives a nod of understanding. "
                            " He understands that he might be going a little too fast right now... "
                            " Instead, he plays a song to distract himself from the embarrassment of asking you that question. "
                            " And you listen to his very well played song. "
                            scene black with dissolve
                            " You spent the rest of the break just hanging out with Carmen. "
                            " Just listening to his song... "
                            " Nothing too special, really. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked down from the rooftop and went to your classroom. "
                            pause 2.0
                            jump ocphysicsfri
                else:
                    " You were about to ask him what he was doing, but... "
                    " It looked like he was too busy doing something on his guitar. "
                    " You decided not to disturb him. "
                    " You were planning to play on your phone, anyway. "
                    " You pulled out your phone and started playing some random game on it. "
                    scene black with dissolve
                    " You spent the rest of the break playing with your phone. "
                    " Just playing games on your phone... "
                    " Nothing too special, really. "
                    pause 2.0
                    jump ocphysicsfri
            else:
                " You were about to ask him what he was doing, but... "
                " It looked like he was too busy doing something on his guitar. "
                " You decided not to disturb him. "
                " You were planning to play on your phone, anyway. "
                " You pulled out your phone and started playing some random game on it. "
                scene black with dissolve
                " You spent the rest of the break playing with your phone. "
                " Just playing games on your phone... "
                " Nothing too special, really. "
                pause 2.0
                jump ocphysicsfri
    label ocfrilibrary4:
        # and koa's ending
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked to the library and found one of your classmates just hanging out. "
        " Wondering what he's doing, you walked over to him. "
        show koaneutral at center with easeinleft
        if koaknow == True:
            pause 0.1
            if koalv >= 30 or koalv == 30:
                " You walked over to him and asked him what he was doing. "
                " I mean, you knew he was reading a book, buuuut... "
                " You were kind of wondering what kind of book he was reading. "
                k " Oh, hello there, [name]. "
                k " I was actually just thinking about you. "
                k " You see... "
                k " I was thinking of telling you something. "
                k " But...as you can sort of tell... "
                k " I've been kind of struggling to come up with words to say. "
                k " I'll try my best to explain what I'm feeling though. "
                k " Um... "
                k " This is a little odd, since we've only known eachother for four days, but... "
                k " In these four days, let's say... "
                k " ...You've been giving me quite the impression. "
                k " And I mean that in the best ways possible. "
                k " You've been treating my friends well... "
                k " Hanging out with me... "
                k " And just being a great [person] overall. "
                k " And... "
                k " The thing I've been wanting to ask you is... "
                k " Would you like to be best friends with me? "
                k " It's okay if you don't want to, of course. "
                k " We've only known eachother for four days, after all. "
                k " But..what do you say? "
                menu:
                    " Best friends! ":
                        $ koasend.grant()
                        hide koaneutral at bottom
                        show koahappy at center
                        k " ...I'm glad that you said that. "
                        k " Uh... "
                        k " If you ever want to hang out or anything... "
                        k " I'll see when I'm free, okay? "
                        scene koaend with dissolve
                        " Congratulations, you've gotten Koa's ending! "
                        " And you've gotten his sweet achievement too. "
                        " Check your achievements tab! "
                        " Since you're best friends with Koa now, you've most certainly met his three siblings... "
                        " They're a chaotic bunch, but all of them are cool. Especially Koa. "
                        jump credits
                    " Normal friends ":
                        k " Understandable... "
                        k " To not make this anything awkward, uh... "
                        k " How about we talk about something else? "
                        scene black with dissolve
                        " You spent the rest of the break talking with Koa. "
                        " Just talking to him about the books that you guys like... "
                        " Nothing too special, in your opinion... "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the library and went to your classroom. "
                        pause 2.0
                        jump ocphysicsfri
            else:
                " You were about to ask him what he was doing, but... "
                " It looked like he was too busy doing reading a book. "
                " You decided not to disturb him. "
                " You were planning to play on your phone, anyway. "
                " You pulled out your phone and started playing some random game on it. "
                scene black with dissolve
                " You spent the rest of the break playing with your phone. "
                " Just playing games on your phone... "
                " Nothing too special, really. "
                pause 2.0
                jump ocphysicsfri
        else:
            " You were about to ask him what he was doing, but... "
            " It looked like he was too busy doing reading a book. "
            " You decided not to disturb him. "
            " You were planning to play on your phone, anyway. "
            " You pulled out your phone and started playing some random game on it. "
            scene black with dissolve
            " You spent the rest of the break playing with your phone. "
            " Just playing games on your phone... "
            " Nothing too special, really. "
            pause 2.0
            jump ocphysicsfri

label ocphysicsfri:
    scene classroom with dissolve
    " Looks like the teacher's here already. "
    " Let's see what you're gonna do this time... "
    show luaneutral at center with easeinleft
    msl " ...Hello...class... "
    msl " ...Let's get class started... "
    msl " ...Before I start forgetting... "
    msl " ...Uh... "
    msl " ...Actually, before that. "
    msl " What did I teach you guys yesterday again...? "
    msl " Oh right, um... "
    msl " You guys had an activity. "
    msl " Let me check everyone's papers right now... "
    msl " I actually forgot to do that yesterday... "
    scene black with dissolve
    " You actually didn't do anything for the rest of the class. "
    " The teacher fell asleep in the middle of checking. "
    " You spent the rest of the break gaming on your phone. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for another break. "
    " You waited for everyone to get out of the classroom before you did. "
    pause 2.0
    jump ocfribreak5

label ocfribreak5:
    # reminder for quinn's play
    scene hallway with dissolve
    " Looks like it's time for the last break of the day. Where do you want to go? "
    menu:
        " The front of the school ":
            jump ocfrontfri5
        " The back of the school ":
            jump ocbackfri5
        " {image=quinnicon} The gym {image=quinnicon} ":
            jump ocgymfri5
        " The cafeteria ":
            jump occafeteriafri5
        " The rooftop ":
            jump ocrooftopfri5
        " The library ":
            jump oclibraryfri5
    # everywhere is empty except gym
    label ocfrontfri5:
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked to the front of the school, and... "
        " Huh. "
        " Surprisingly, no one's here. "
        " Usually there would be someone here. "
        " That's odd... "
        " But, oh well I guess. "
        " This just gives you more time to game with your phone. "
        " And to also scroll on your phone. "
        " With that being said... "
        " Let's start doing some phone gaming. "
        " You got your phone from your pocket... "
        " And started to play some games on your phone. "
        " Epic gaming session! "
        " Though you kinda wish you had someone to talk to while gaming. "
        " Oh well, I guess... "
        scene black with dissolve
        " You spent the rest of the break playing games on your phone... "
        " And also scrolling on social media. "
        " You didn't do anything too productive this break. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your final class of the day. "
        " You walked back into the school and went to your classroom. "
        pause 2.0
        jump occookingfri
    label ocbackfri5:
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of the school, and... "
        " Huh. "
        " Surprisingly, no one's here. "
        " Usually there would be someone here. "
        " That's odd... "
        " But, oh well I guess. "
        " This just gives you more time to game with your phone. "
        " And to also scroll on your phone. "
        " With that being said... "
        " Let's start doing some phone gaming. "
        " You got your phone from your pocket... "
        " And started to play some games on your phone. "
        " Epic gaming session! "
        " Though you kinda wish you had someone to talk to while gaming. "
        " Oh well, I guess... "
        scene black with dissolve
        " You spent the rest of the break playing games on your phone... "
        " And also scrolling on social media. "
        " You didn't do anything too productive this break. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your final class of the day. "
        " You walked back into the school and went to your classroom. "
        pause 2.0
        jump occookingfri
    label ocgymfri5:
        # quinn's ending
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked to the gym and spotted someone doing a play. "
        " It seemed like it was one of your classmates performing... "
        " Should you watch? "
        menu:
            " Watch the play ":
                $ quinnlv += 10
                " You decided to watch the play. "
                " You found an empty seat and started to watch... "
                scene black with dissolve
                " You watched your classmate's play for a bit. "
                " You weren't paying that much attention to the story, but... "
                " From what you could tell, it was pretty cool. "
                " A whole lot of drama and a whole lot of funny parts. "
                " Everything looks like it went perfect, from what you could tell. "
                " They really worked hard on this, huh? "
                " You wouldn't admit it outloud, buuuuut... "
                " You were actually kind of impressed from this. "
                " After a bit, the play ended, and your classmate walked down from the stage. "
                scene gym with dissolve
                show quinnneutral at center with easeinright
                if quinnknow == True:
                    q " Oh, hello there, [name]. "
                    q " I wasn't expecting for you to come to my play, but... "
                    q " I'm glad that you came to watch. "
                    q " I've actually worked really hard to make everything perfect... "
                    q " And I'm glad that everything all went fine. "
                    q " Otherwise, I probably would've cancelled this entire thing. "
                    q " Even though I was really excited about it... "
                    q " I just can't have imperfections in my play, you know? "
                    q " Really makes the play less interesting to watch. "
                    q " And I also made sure to have everyone really get into their roles. "
                    q " I don't want them to be reading out their lines as if they're working at minimum wage! "
                    q " It's just gonna sound like I'm not treating them right! "
                    q " And I do, for a fact, treat them right. "
                    q " I take them out to eat after every successful play! "
                    q " And yes, there HAVE been unsuccessful plays we've had. "
                    q " But, all of those are in the past now. "
                    q " All we have is complete and utter perfection. "
                    q " Hmmm... "
                    q " I feel like I was going to say something, but... "
                    q " I forgot what I was going to say... "
                    q " Hm, let me try to remember real quick... "
                    " You waited for him to remember what he had to say. "
                    " You were getting pretty curious as you waited... "
                    if quinnlv >= 25 or quinnlv == 25:
                        q " Oh, that's right! "
                        q " There was this...question that I had to ask you. "
                        q " I know we've only known eachohter for four days, but... "
                        q " Is it quite odd that I consider you as my best friend? "
                        q " I mean, do you want to? "
                        q " Be best friends, I mean. "
                        q " I don't want to force you to be my best friend, you know. "
                        q " That would be really weird and very uncool of me. "
                        q " So, um... "
                        q " Would you perhaps want to be my best friend? "
                        menu:
                            " Besties!! ":
                                $ quinnsend.grant()
                                hide quinnneutral at bottom
                                show quinnhappy at center
                                q " ...I'm glad! "
                                q " Hm, now that you're my best friend... "
                                q " I'll try to sneak you into my practices. "
                                q " And I'll even get you front row seats onto my plays! "
                                q " Sounds great, doesn't it? "
                                q " And I'll also get you some food along with my club members! "
                                scene quinnend with dissolve
                                " Congratulations! you've gotten Quinn's ending! "
                                " And his sweet achievement. Check your achievements tab! "
                                " Nice, you get food for checking out his plays. "
                                " Winning hard! "
                                jump credits
                            " Normal friends please ":
                                q " Ah, okay...understandable. "
                                q " I'd like to talk to you more today though. "
                                q " Let's see... "
                                scene black with dissolve
                                " You spent the rest of the break talking with Quinn. "
                                " Just talking to him about his play and everything... "
                                " Nothing too special, in your opinion. "
                                play sound "audio/bellring.mp3"
                                " The bell rings after a bit, looks like it's time for another class. "
                                " You walked out of the gym and went to your classroom. "
                                pause 2.0
                                jump occookingfri
                    else:
                        q " Ah, I'm sure that it wasn't that important. "
                        q " I've got other things to talk about, anyway! "
                        q " Let's see, what to talk about first, what to talk about first... "
                        q " Oh right! "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Just talking to him about his play and everything... "
                        " Nothing too special, in your opinion. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the gym and went to your classroom. "
                        pause 2.0
                        jump occookingfri
                else:
                    x " Oh, hello there, [name]. "
                    x " I don't think I've introduced myself before to you, hm... "
                    $ quinnknow = True
                    q " I'm Quinn! Disk's younger brother and a member of the theater club. "
                    q " I wasn't expecting for you to come to my play, but... "
                    q " I'm glad that you came to watch. "
                    q " I've actually worked really hard to make everything perfect... "
                    q " And I'm glad that everything all went fine. "
                    q " Otherwise, I probably would've cancelled this entire thing. "
                    q " Even though I was really excited about it... "
                    q " I just can't have imperfections in my play, you know? "
                    q " Really makes the play less interesting to watch. "
                    q " And I also made sure to have everyone really get into their roles. "
                    q " I don't want them to be reading out their lines as if they're working at minimum wage! "
                    q " It's just gonna sound like I'm not treating them right! "
                    q " And I do, for a fact, treat them right. "
                    q " I take them out to eat after every successful play! "
                    q " And yes, there HAVE been unsuccessful plays we've had. "
                    q " But, all of those are in the past now. "
                    q " All we have is complete and utter perfection. "
                    q " Hmmm... "
                    q " I feel like I was going to say something, but... "
                    q " I forgot what I was going to say... "
                    q " Hm, let me try to remember real quick... "
                    " You waited for him to remember what he had to say. "
                    " You were getting pretty curious as you waited... "
                    q " Ah, I'm sure that it wasn't that important. "
                    q " I've got other things to talk about, anyway! "
                    q " Let's see, what to talk about first, what to talk about first... "
                    q " Oh right! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Quinn. "
                    " Just talking to him about his play and everything... "
                    " Nothing too special, in your opinion. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the gym and went to your classroom. "
                    pause 2.0
                    jump occookingfri
            " No, I'd rather game ":
                " Yeah, let's just go somewhere else and game. "
                scene black with dissolve
                " You spent the rest of the break playing games on your phone... "
                " And also scrolling on social media. "
                " You didn't do anything too productive this break. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your final class of the day. "
                " You walked back to your classroom after a bit of gaming. "
                pause 2.0
                jump occookingfri
    label occafeteriafri5:
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked to the cafeteria, and... "
        " Huh. "
        " Surprisingly, no one's here. "
        " Usually there would be someone here. "
        " That's odd... "
        " But, oh well I guess. "
        " This just gives you more time to game with your phone. "
        " And to also scroll on your phone. "
        " With that being said... "
        " Let's start doing some phone gaming. "
        " You got your phone from your pocket... "
        " And started to play some games on your phone. "
        " Epic gaming session! "
        " Though you kinda wish you had someone to talk to while gaming. "
        " Oh well, I guess... "
        scene black with dissolve
        " You spent the rest of the break playing games on your phone... "
        " And also scrolling on social media. "
        " You didn't do anything too productive this break. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your final class of the day. "
        " You walked out of the cafeteria and went to your classroom. "
        pause 2.0
        jump occookingfri
    label ocrooftopfri5:
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked to the rooftop, and... "
        " Huh. "
        " Surprisingly, no one's here. "
        " Usually there would be someone here. "
        " That's odd... "
        " But, oh well I guess. "
        " This just gives you more time to game with your phone. "
        " And to also scroll on your phone. "
        " With that being said... "
        " Let's start doing some phone gaming. "
        " You got your phone from your pocket... "
        " And started to play some games on your phone. "
        " Epic gaming session! "
        " Though you kinda wish you had someone to talk to while gaming. "
        " Oh well, I guess... "
        scene black with dissolve
        " You spent the rest of the break playing games on your phone... "
        " And also scrolling on social media. "
        " You didn't do anything too productive this break. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your final class of the day. "
        " You walked out of the rooftop and went to your classroom. "
        pause 2.0
        jump occookingfri
    label oclibraryfri5:
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked to the library, and... "
        " Huh. "
        " Surprisingly, no one's here. "
        " Usually there would be someone here. "
        " That's odd... "
        " But, oh well I guess. "
        " This just gives you more time to game with your phone. "
        " And to also scroll on your phone. "
        " With that being said... "
        " Let's start doing some phone gaming. "
        " You got your phone from your pocket... "
        " And started to play some games on your phone. "
        " Epic gaming session! "
        " Though you kinda wish you had someone to talk to while gaming. "
        " Oh well, I guess... "
        scene black with dissolve
        " You spent the rest of the break playing games on your phone... "
        " And also scrolling on social media. "
        " You didn't do anything too productive this break. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your final class of the day. "
        " You walked out of the library and went to your classroom. "
        pause 2.0
        jump occookingfri

label occookingfri:
    scene classroom with dissolve
    " Huh...looks like the teacher isn't here. "
    " Guess this is just more freetime for you. "
    " Time for more gaming... "
    scene black with dissolve
    " You spent the rest of the class hour playing games on your phone. "
    " Just gaming and gaming... "
    " Nothing too important happened while you were in class. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for you to go home. "
    " You waited for everyone to leave the classroom before you did. "
    pause 2.0
    jump ocfrigohome

label ocfrigohome:
    # reminder for disk's, yinhui, and yangyi's ending
    scene paperschoolfront with dissolve
    " You walked out of your school, looks like it's time to go home. "
    if diskparty == True:
        " Is what I would say if you hadn't agreed to go to Disk's party. "
        " It's time for you to go over to Disk's house... "
        " Thankfully, Disk gave you the directions to his house. "
        " Let's go and have fun. "
        " And because we don't have anymore budget for this scene... "
        " We don't actually have a picture of Disk's house. "
        " But just imagine yourself in a huge mansion and everyone partying. "
        " It was fun, but you were not allowed to go to certain places. "
        " You ate a lot, drank soda a lot... "
        " All of the food was good there, probably because Disk got it made by his personal chefs. "
        " Man, think it was a good idea for you to go here... "
        " And then after a few hours, before it got too late... "
        " The party ended. "
        if disklv >= 30 or disklv == 30:
            " But, as you were about to leave... "
            " Someone wanted to have a little talk with you. "
            " It was Disk. "
            show diskneutral at center with easeinleft
            d " Hey there, [name]! "
            d " I really appreciated the fact that you went here... "
            d " I hope you had fun! "
            d " Considering that this is the first time you've went to one of my parties, eheh. "
            d " It would be upsetting to hear that you didn't have any fun. "
            d " If that was the case... "
            d " I would've tried to improve to make the expirience better on the next part!! "
            d " Anyway... "
            d " There's been something that I've been thinking about to tell you!! "
            d " I'm just going to be really straight forward here... "
            d " Would you like to be my best friend?? "
            d " I know it sounds weird, because we've only known eachother for four days, but... "
            d " You're just so cool! "
            d " So, um... "
            d " Do you want to be best friends with me? "
            d " It's okay if you don't want to! "
            menu:
                " BESTIES!! ":
                    $ disksend.grant()
                    hide diskneutral at bottom
                    show diskhappy at center
                    d " Yayy!! "
                    d " I'm glad that we're best friends now!! "
                    d " You wanna go get some food sometime? "
                    d " I'll be paying, of course! "
                    scene diskend with dissolve
                    " Congratulations, you've gotten Disk's ending! "
                    " And his sweet achievement, check your achievements tab! "
                    " Wow, good job on befriending the popular rich boy. "
                    " Just don't use him for his money, you're gonna get your ass kicked by his yougner brother. "
                    jump credits
                " Normal friends!! ":
                    d " Oh...okay!! "
                    d " I understand, don't worry! "
                    d " But, I was thinking... "
                    d " Maybe we could go out to get some food sometime? "
                    d " I'm paying, of course!! "
                    d " Just tell me when you're free, alright? "
                    hide diskneutral at right with easeoutright
                    " And Disk left. "
                    " You took some of the food home with you since they were just so good... "
                    " And then you left. "
                    stop music fadeout 1.5
                    pause 2.0
                    play music "audio/home.mp3" fadein 1.5
                    jump mcgohomefrioc
        elif yinhuilv >= 45 or yinhuilv == 45:
            " But, as you were about to leave... "
            " Someone wanted to have a little talk with you. "
            " It was Yinhui. "
            show yinhuineutral at center with easeinleft
            yi " Uh...hey there, [name]. "
            yi " Um. "
            yi " Okay, thank god Yangyi isn't here to hear me say this. "
            yi " But... "
            yi " I have to admit. "
            yi " I had fun with you...while we were here. "
            yi " And... "
            yi " I'm looking forward to hanging out with you more. "
            yi " And... "
            yi " I have something else to ask you. "
            yi " Something that's been in my head for awhile now... "
            yi " (It's embarrassing saying this.) "
            yi " (Especially since I've got that whole cool guy personality...) "
            yi " (But Yang did say that I have to be honest.) "
            yi " (Keeping my emotions in would only do me more harm than good.) "
            yi " (Okay, you can do this...) "
            yi " (Just take some deep breaths and you'll be fine.) "
            yi " ...Alright. "
            yi " I don't really ask this to just anyone, but... "
            yi " You've been pretty good at being friends with my brother. "
            yi " Talking to him, making him laugh and all that... "
            yi " And I finally trust you enough to say this. "
            yi " Would you...perhaps... "
            yi " Want to be my best friend? "
            yi " It's okay if you just want to be my normal friend or something. "
            yi " Not gonna force you over here. "
            menu:
                " Besties!! ":
                    $ persistent.yinhuiend = True
                    $ yinhuisend.grant()
                    if persistent.yinhuiend == True and persistent.yangyiend == True:
                        $ yinyangend.grant()
                    else:
                        pass
                    hide yinhuineutral at bottom
                    show yinhuihappy at center
                    yi " ...Heh. "
                    yi " I'm actually...pretty happy that you said that. "
                    yi " Let's just say that since you're friends with me now... "
                    yi " My mom's going to be extra chill with you. "
                    yi " Not in school, but whenever we hang out. "
                    scene yinhuiend with dissolve
                    " Congratulations! You've gotten Yinhui's ending! "
                    " And also his sweet achievement. Check your achievements tab. "
                    " You've managed to befriend the angry emo boy! congrats! "
                    " You also get to taste good food made by his mom every now and then too. "
                    jump credits
                " Normal friends, please. ":
                    yi " Okay, that's understandable. "
                    yi " We've only known eachother for four days. "
                    yi " Uh... "
                    yi " Hope you're safe while walking home though. "
                    yi " I gotta bounce. Mom's gonna kill me if I stay for too long. "
                    hide yinhuineutral at right with easeoutright
                    " ...And he left. "
                    " You took some of the food home with you since they were just so good... "
                    " And then you left. "
                    stop music fadeout 1.5
                    pause 2.0
                    play music "audio/home.mp3" fadein 1.5
                    jump mcgohomefrioc
        elif yangyilv >= 30 or yangyilv == 30:
            " But, as you were about to leave... "
            " Someone wanted to have a little talk with you. "
            " It was Yangyi. "
            show yangyineutral at center with easeinleft
            ya " Hello there, [name]! "
            ya " After everything that we've done here... "
            ya " I have to say, this is the most fun I've had in ages! "
            ya " Well, not really ages. "
            ya " I mean, I go here every two weeks or soo... "
            ya " But yeah, everything was all fun! "
            ya " And...honestly? "
            ya " I'm glad to have spent my time here with you. "
            ya " And...I wish to spend even more time with you! "
            ya " And there's another thing I want to tell you about... "
            ya " God, Yinhui would kill me if he was here right now... "
            ya " But, I have to say it! "
            ya " He did tell me to be honest after all, hehe! "
            ya " Anyway... "
            ya " The thing I've been meaning to ask you is... "
            ya " Would you like to be my best friend? "
            menu:
                " Besties!! ":
                    $ yangyisend.grant()
                    $ persistent.yangyiend = True
                    if persistent.yangyiend == True and persistent.yinhuiend == True:
                        $ yinyangend.grant()
                    else:
                        pass
                    hide yangyineutral at bottom
                    show yangyihappy at center
                    ya " Yay! I'm glad that you wanted to me my best friend!! "
                    ya " And, uhhh... "
                    ya " Now that we're best friends... "
                    ya " My mom's probably gonna cook you something everytime you come over, hehe. "
                    ya " She likes to treat others nicely! "
                    scene yangyiend with dissolve
                    " Congratulations! You've gotten Yangyi's ending! "
                    " And his sweet achievement. Check your achievement's tab! "
                    " Sweet, now you can get some good food whenever you come over. "
                    jump credits
                " Normal friends!! ":
                    ya " Ah, understandable... "
                    ya " It's fine if you want to stay as normal friends though! "
                    ya " I'm not mad! "
                    ya " Anyway... "
                    ya " I hope you're safe while you're walking back home! "
                    ya " I gotta go already... "
                    ya " Mom's gonna kill me if I stay here for too long! "
                    ya " See you! "
                    hide yangyineutral at right with easeoutright
                    " ...And he left. "
                    " You took some of the food home with you since they were just so good... "
                    " And then you left. "
                    stop music fadeout 1.5
                    pause 2.0
                    play music "audio/home.mp3" fadein 1.5
                    jump mcgohomefrioc
        else:
            " You took some of the food home with you since they were just so good... "
            " And then you left. "
            stop music fadeout 1.5
            pause 2.0
            play music "audio/home.mp3" fadein 1.5
            jump mcgohomefrioc
    else:
        " You took one good look at your school and your classmates... "
        " Everyone seems to be excited about Disk's party. "
        " Hm...maybe you should go the next time he throws one again. "
        " Not right now, but some other time. "
        " Well, time for you to go home. "
        " You began walking home after a good bit... "
        scene black with dissolve
        stop music fadeout 1.5
        pause 2.0
        play music "audio/home.mp3"
        jump mcgohomefrioc
label mcgohomefrioc:
    scene mcroom with dissolve
    " As you laid down in your bed, you couldn't help but feel a sense of lonliness in your heart. "
    " You've met so many nice people in this school... "
    " But you didn't really bother getting to know them that well. "
    " Maybe you should've talked to them more. "
    " You lonely asshole {nw} "
    scene lonelyend with dissolve
    " ...Wow buddy I thought I taught you how this game works "
    " But alright man "
    jump credits
