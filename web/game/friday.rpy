label friday:
    show text " DAY 5 - FRIDAY (the final day!) "
    pause 1.5
    scene mcroom with dissolve
    " Good morning sleepyhead. "
    " I don't really care if you slept good or not. "
    " You get yourself ready for the day, cook yourself some food... "
    " ...Pack your things... "
    " Alright, looks like you're ready for some more hell. "
    " Let's go to school, you don't to be late now, would you? "
    scene black with dissolve
    stop music fadeout 1.5
    pause 2.0
    play music "audio/paperhigh.mp3" fadein 1.5
    scene paperschoolfront with dissolve
    pause 1.0
    scene black with dissolve
    pause 1.0
    scene hallway with dissolve
    pause 1.0
    scene black with dissolve
    pause 1.0
    jump mathclassfri

label mathclassfri:
    scene classroom with dissolve
    " You walked into the classroom, seeing that the math teacher wasn't there yet. "
    " You sat down, looking around for what you could do to pass the time... "
    " You DID have some free time on your hands. "
    " Hmm...let's see... "
    if claengbub == True:
        pause 0.1
        if clairelv >= 30 or clairelv == 30:
            jump claireintlv
        elif engellv >= 30 or engellv == 30:
            jump engelintlv
        elif bubblelv >= 30 or bubblelv == 30:
            jump bubbleintlv
        else:
            jump lonelyassdrawing
    elif abblana == True:
        pause 0.1
        if abbielv >= 30 or abbielv == 30:
            jump abbieintlv
        elif lanalv >= 30 or lanalv == 30:
            jump lanaintlv
        else:
            jump lonelyassdrawing
    elif oligang == True:
        pause 0.1
        if oliganglv >= 30 or oliganglv == 30:
            jump oligangintlv
        else:
            jump lonelyassdrawing
    elif alone == True:
        jump lonelyassdrawing
    else:
        jump lonelyassdrawing
    label claireintlv:
        " You could talk to Claire, she looks like she's doing nothing important. "
        " You scooted a bit closer to her so that you could talk... "
        show claireneutral at center with easeinleft
        " You tapped her shoulder so that you could get her attention. "
        c " Oh, hey there [name]! "
        c " I just remembered what I had to tell you... "
        hide claireneutral at bottom
        show clairehappy at center
        c " I hope you're enjoying your first week in this school! "
        c " If I had to be honest... "
        c " Things have been way more fun for me now that you're here. "
        c " Really, I mean it. "
        c " My days used to be fun, but with you here with us... "
        c " You just made my days even better! "
        c " Even in my darkest of times. "
        c " I feel like you being here... "
        c " Jeez, I don't know what I'm even saying, haha... "
        c " But I just feel really happy that you're here, you know? "
        c " I, uh...appreciate your presense. "
        c " We could read together sometime! "
        hide clairehappy at bottom
        show claireneutral at center
        c " Actually...maybe we could do that right now? "
        c " Miss Circle isn't here yet, after all. "
        c " She said that she was going to be a few minutes late... "
        c " You wanna read for a bit? "
        menu:
            " YEAHHH READING ":
                $ clairelv += 10
                hide claireneutral at bottom
                show clairehappy at center
                c " Yahoo! "
                c " Here, I brought in one of my favorites... "
                c " I wanna know what you think of this one! "
                c " Trust me, it's really really good! "
                scene claireread with dissolve
                " You spent a few minutes reading with Claire. "
                " Just a book about fantasy... "
                " It was pretty good though. The writing. "
                " Well - good from what you could see so far. "
                " Maybe you and Claire could read more on this later... "
                " The teacher had already arrived, so you two had to pause. "
                " Yeah, let's just...continue this later. "
                scene black with dissolve
                " Nothing interesting happened in math class. "
                " Just had to take down a few notes... "
                " And the teacher was just discussing for the most part. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for a break. "
                " You hopped out of your seat and you went out into the hallways to find a place to hangout in. "
                pause 2.0
                jump fribreak1
            " Nah, maybe next time ":
                c " Oh! okay! "
                c " But when you ARE in the mood... "
                c " I could make you read one of my favorite books! "
                c " Trust me - it's really good! "
                scene black with dissolve
                " You and Claire talked for a bit since the teacher wasn't there. "
                " Just for a bit, about the book she was talking about earlier. "
                " It was a fantasy book with apparently a good storyline. "
                " Maybe you should check that out later. "
                " The teacher soon arrives though, and you two stop talking...for now. "
                " Nothing interesting happened in math class. "
                " Just had to take down a few notes... "
                " And the teacher was just discussing for the most part. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for a break. "
                " You hopped out of your seat and you went out into the hallways to find a place to hangout in. "
                pause 2.0
                jump fribreak1
    label engelintlv:
        " You could talk to Engel. "
        " I mean, he doesn't look too busy right now. "
        " You scooted a bit closer so that you could talk to him... "
        show engelhappy at center with easeinright
        e " Hi there, [name]. "
        e " I hope your first week here is going well. "
        e " You know, I've been thinking... "
        e " You ever get that feeling when you meet someone... "
        e " And get a little bit close to them... "
        e " It suddenly feels like you've known them for years? "
        e " Even though you two only have known eachother for a short time. "
        e " That's...how I'm kind of feeling towards you right now. "
        e " I've talked with you for such a short time... "
        e " Hung out with you for just a bit... "
        e " But, it feels like I can talk to you about anything. "
        e " Maybe even some personal things... "
        e " I don't know how I've managed to get so close to you in such a short time, haha. "
        e " But, I think we might just get a little closer as we progress through the school year. "
        e " And honestly? "
        e " I'd love spending more time with you. "
        e " I want to get to know you better... "
        e " And maybe we could hang out with eachother more often. "
        e " That would sound lovely... "
        e " Oh, uh...you don't mind talking to you for a little bit longer, right? "
        e " If you have other things to do, I won't bother you. "
        menu:
            " talk to me feather boy ":
                $ engellv += 10
                e " Pft - feather boy...? "
                e " That's one creative name... "
                e " But, I'll accept it. "
                e " Since it also sounds pretty cute. "
                scene engelhangout with dissolve
                " You and Engel talked for a bit more. "
                " Just talked about random things... "
                " Things like stuff that happened before you even got into this school. "
                " And boy, Engel had a whole lot of interesting stories. "
                " Like, I'm talking INTERESTING interesting. "
                " Who knew a lot of shit happened while you weren't here? "
                " I mean...it's expected, but still. "
                " You would love talking to Engel a bit more... "
                " The teacher had already arrived, so you two had to pause. "
                " Yeah, let's just...continue this later. "
                scene black with dissolve
                " Nothing interesting happened in math class. "
                " Just had to take down a few notes... "
                " And the teacher was just discussing for the most part. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for a break. "
                " You hopped out of your seat and you went out into the hallways to find a place to hangout in. "
                pause 2.0
                jump fribreak1
            " nah hold on i gotta game on my phone ":
                e " Hm...? gaming? "
                e " Alright, go ahead. "
                e " Good luck with your gaming session, [name]! "
                scene black with dissolve
                " You spent the rest of free time playing games on your phone. "
                " Just chilling there, and vibing... "
                " Doing nothing much, but you would sometimes listen to your classmates' conversations. "
                " The teacher soon arrived though, so you put your phone away. "
                " Nothing interesting happened in math class. "
                " Just had to take down a few notes... "
                " And the teacher was just discussing for the most part. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for a break. "
                " You hopped out of your seat and you went out into the hallways to find a place to hangout in. "
                pause 2.0
                jump fribreak1
    label bubbleintlv:
        " Maybe you could talk to Bubble? "
        " She doesn't look too busy right now. "
        " I mean, she never really does look too busy. "
        " You scooted a bit closer so that you could talk to her... "
        show bubbleneutral at center with easeinleft
        b " Hiya, [name]! "
        b " I hope that you've been enjoying your time here at the school so far! "
        b " I have a few things I'd like to say to you, actually... "
        b " If I'm going to be honest... "
        hide bubbleneutral at bottom
        show bubblehappy at center
        b " I've been really enjoying your company! "
        b " Like, really! I mean it! "
        b " You somehow managed to make my days even better! "
        b " And I mean that in a really good way! "
        b " You know... "
        b " We've only known eachother for just a bit, but... "
        b " I feel like we've known eachother for AGES!! "
        b " Is that too insane for me to say? "
        b " Like, it's insane that we got this close in a short time! "
        b " God, I sound like Engel whenever he makes a new friend too fast... "
        b " But that's how I'm feeling right now! "
        b " I'm really glad to have met you, [name]... "
        b " You've made my days brighter. Truly. "
        hide bubblehappy at bottom
        show bubbleneutral at center
        b " Uh...wait, I hope I'm not talking too much to you. "
        b " You wanna keep talking? "
        b " I won't disturb you anymore if you have other things to do! "
        menu:
            " talk to me more ":
                $ bubblelv += 10
                hide bubbleneutral at bottom
                show bubblehappy at center
                b " ...Oh, you wanna talk to me more? "
                b " Well, if you really want to talk, then... "
                b " I don't mind! "
                b " That IS what you want, after all! "
                scene bubblehangout with dissolve
                " You spent a bit of free time talking with Bubble. "
                " Just talking about the things that happened before you even went into this school. "
                " You did NOT know someone attempted to do a backflip 5 times in a row. "
                " ...According to Bubble, that person only got up to two before feeling dizzy. "
                " I mean, no shit. You can't really do that many backflips. "
                " You're gonna get even more dizzy if you manage to do 10. "
                " Lots of crazy shit happened while you weren't even here, huh? "
                " You slightly wish that you were there when everything happened. "
                " You wished you could talk more to Bubble, too... "
                " But looks like the teacher's here. "
                " Yeah...you guys are just gonna continue that later. "
                scene black with dissolve
                " Nothing interesting happened in math class. "
                " Just had to take down a few notes... "
                " And the teacher was just discussing for the most part. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for a break. "
                " You hopped out of your seat and you went out into the hallways to find a place to hangout in. "
                pause 2.0
                jump fribreak1
            " Hold on gng i gotta game ":
                b " Oh! you have a game going on? "
                b " Alright, alright! "
                b " Have fun gaming there, [name]! "
                scene black with dissolve
                " You spent the rest of free time playing games on your phone. "
                " Just chilling there, and vibing... "
                " Doing nothing much, but you would sometimes listen to your classmates' conversations. "
                " The teacher soon arrived though, so you put your phone away. "
                " Nothing interesting happened in math class. "
                " Just had to take down a few notes... "
                " And the teacher was just discussing for the most part. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for a break. "
                " You hopped out of your seat and you went out into the hallways to find a place to hangout in. "
                pause 2.0
                jump fribreak1
    label abbieintlv:
        " You could talk to Abbie, he doesn't look too busy right now. "
        " Infact, he was drawing something... "
        " You scooted closer to him to see what he was drawing. "
        show abbiehappy at center with easeinleft
        a " Hmmhmmm... "
        " Upon closer look, he was drawing...aww... "
        " It was a drawing of you and him hanging out. "
        " He had a pretty cute artstyle, too. "
        " You decided to compliment him for the drawing he had made. "
        hide abbiehappy at bottom
        show abbieneutral at center
        a " !!...[name]?? you were looking? "
        a " S..sorry, I didn't see you... "
        a " I didn't mean to ignore you or anything. "
        hide abbieneutral at bottom
        show abbiehappy at center
        a " B...but, yeah...this is a drawing of us...! "
        a " I just wanted to make this to thank you... "
        a " ...For everything... "
        a " I genuinely have...no words to say but thank you... "
        a " You've been making my days more brighter... "
        a " And I've been smiling more often now... "
        a " And also, I've been learning how to improve in self defense more 'cause of you... "
        a " You actually got me really motivated to do that stuff... "
        a " Because, um...you're so cool... and...I wanted to be strong like you... "
        a " I hope I don't sound weird when I say that, but I really mean it... "
        a " I would love to spend even more time with you... "
        a " ... (AAAA THIS IS SO EMBARRASSING TO SAY GOD HELP ME) "
        a " (I HOPE NO ONE HEARD THATTTT) "
        hide abbiehappy at bottom
        show abbieneutral at center
        a " U-um... "
        a " I was wondering, [name]... "
        a " Would you maybe like to...um... "
        a " Draw together...? "
        a " You don't have to if you don't want to... "
        a " I can just finish this drawing on my own... "
        a " It's fine, really.. "
        menu:
            " lemme draw with you ":
                $ abbielv += 10
                hide abbieneutral at bottom
                show abbiehappy at center
                a " Oh...! "
                a " You actually want to draw with me? "
                a " Well...come here, closer.... "
                a " So you can actually draw and put in the details you want, hehe. "
                a " I don't want you to struggle while you're drawing... "
                a " You can draw anything you want, by the way! "
                a " And I mean that...absolutely anything. "
                " You spent the bit of free time drawing with Abbie. "
                " Your artstyle compared to Abbie's... "
                " Abbie's artstyle honestly looked way better than yours. "
                " But, both of you kept insisting that eachother's artstyles were better. "
                " Abbie wouldn't really accept that his artstyle is good. "
                " If someone hates Abbie's arstyle, you're going to jump them. "
                " His artstyle is like what you'd see in an old anime. "
                " That one anime about magical girls, to be specific. "
                " You wanted to draw with Abbie for a little longer, buuuut... "
                " Of course, the teacher had arrived. "
                " You're gonna have to continue drawing with him some other time. "
                scene black with dissolve
                " Nothing interesting happened in math class. "
                " Just had to take down a few notes... "
                " And the teacher was just discussing for the most part. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for a break. "
                " You hopped out of your seat and you went out into the hallways to find a place to hangout in. "
                pause 2.0
                jump fribreak1
            " sorry Abbie, i need to game ":
                a " Oh, you have a game...? "
                a " Alright, we can just...draw another time then, if you're up for it.. "
                a " G...good luck on your game, though...! "
                scene black with dissolve
                " You spent the rest of free time playing games on your phone. "
                " Just chilling there, and vibing... "
                " Doing nothing much, but you would sometimes listen to your classmates' conversations. "
                " The teacher soon arrived though, so you put your phone away. "
                " Nothing interesting happened in math class. "
                " Just had to take down a few notes... "
                " And the teacher was just discussing for the most part. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for a break. "
                " You hopped out of your seat and you went out into the hallways to find a place to hangout in. "
                pause 2.0
                jump fribreak1
    label lanaintlv:
        " You could talk to Lana. "
        " She doesn't look THAT busy... "
        " You scooted over to see what she was doing. "
        show lananeutral at center with easeinright
        l " Hmhmmm... "
        l " Oh, hiya there [name]! "
        l " Didn't notice that you were watching, hehe... "
        l " I was making another one of my puppets! "
        l " And also, about the Juliana and Pedro thing... "
        l " I kinda need a break from that for now. "
        l " Since I don't know how the ending should go... "
        l " I've been kinda draining myself by constantly making episodes! "
        l " And I don't want to keep doing that. "
        l " Otherwise, I'd drop the series entirely! "
        l " I don't wanna do that, you know? "
        l " Oh, and also, also! "
        l " This new puppet over here? "
        hide lananeutral at bottom
        show lanahappy at center
        l " It's based off of you! "
        l " Since you've been listening to me and my shows a whole lot... "
        l " I decided to make a little fella based off of you! "
        l " I'm glad to have someone who actually listens, hehe. "
        l " And you've been a really great friend to me in general! "
        l " Like, I mean that. Truly. "
        l " I...okay, I don't know what else to say, haha. "
        l " But you're really great, [name]! "
        l " That's all I can say to uh...god, my eNGLISH ISN'T ENGLISHING. "
        l " hjkhgkhgkjhk... "
        hide lanahappy at bottom
        show lananeutral at center
        l " Oh, hey! I just thought of something! "
        l " Would ya perhaps wanna make some puppets with me too? "
        l " I've got an extra sock in need of some decorating here! "
        l " Though, if you don't wanna, then I'm not gonna force you to! "
        l " Don't wanna make a buddy uncomfortable, after all. "
        menu:
            " WOOO SOCK PUPPETS ":
                $ lanalv += 10
                hide lananeutral at bottom
                show lanahappy at center
                l " That's the spirit! "
                l " Here's the sock you're gonne be using... "
                l " And I'm just gonna leave the decorations on the table! "
                l " Just make sure that they don't fall off, though. "
                l " Otherwise, we're gonna have to look for them for a loong time... "
                l " Like, I'm talking a long time! "
                l " I lost one of the decorations once and I couldn't find it until three weeks later... "
                l " Really a pain to look for. "
                l " Anyway, you can go and start now! "
                l " No rush in getting this finished, really. "
                scene lanapuppets with dissolve
                " You spent the bit of free time making puppets with Lana. "
                " Since she was making a puppet based off of you, you made a puppet based off of her. "
                " Because you were doing that though, you would glance at her very often. "
                " Just so that you would get every single detail she had. "
                " Well - not all details of course, but you just gave the puppet that seemed very...lana-like. "
                " That's kind of the bestest way I can explain it. "
                " You were about to finish making your puppet, but of course, the teacher had to come in. "
                " Maybe you're gonna continue this later. "
                scene black with dissolve
                " Nothing interesting happened in math class. "
                " Just had to take down a few notes... "
                " And the teacher was just discussing for the most part. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for a break. "
                " You hopped out of your seat and you went out into the hallways to find a place to hangout in. "
                pause 2.0
                jump fribreak1
            " sock puppets, but later - i got a game. ":
                l " Oooh, a game? "
                l " Good luck, then! "
                l " I'm just gonna continue making your sock puppet over here... "
                scene black with dissolve
                " You spent the rest of free time playing games on your phone. "
                " Just chilling there, and vibing... "
                " Doing nothing much, but you would sometimes listen to your classmates' conversations. "
                " The teacher soon arrived though, so you put your phone away. "
                " Nothing interesting happened in math class. "
                " Just had to take down a few notes... "
                " And the teacher was just discussing for the most part. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for a break. "
                " You hopped out of your seat and you went out into the hallways to find a place to hangout in. "
                pause 2.0
                jump fribreak1
    label oligangintlv:
        " You could talk with your gang over here. "
        " I mean, they look like they're pretty bored. "
        " You turn your chair a bit so that you could properly face them... "
        show edwardneutral at left with easeinright
        show oliverneutral at center with easeinright
        show zipneutral at right with easeinright
        ed " Yoyooo, [name]!! "
        z " It's been one hell of a ride since you've got here, eh? "
        o " Yeah, one hell of a ride, alright. "
        o " So...we've been thinking about a few things. "
        o " Like, you've been REALLY cool to us for these few days. "
        ed " Even though there were some misunderstandings! "
        z " Or not, we can't really remember. "
        z " Probably not too important if we forget, though. "
        z " All we know is that you're really cool. "
        ed " Even if ya may or may not have done some stuff to our group here. "
        ed " It's all in the past, so we don't really mind too much. "
        o " Even if we didn't know you for that long... "
        o " And even if we thought you were a loser at first... "
        o " You're officially cool to us now. "
        ed " You can now flex about that all throughout the school! "
        z " People are probably gonna hate you for being friends with us, buuut... "
        z " Who cares about their opinion, really? "
        ed " Yeah, what she said! "
        o " Anyway, enough of all that. "
        o " We're planning on doing something on the third break of the day. "
        o " You wanna listen in? "
        z " Or do you got something better to do? "
        menu:
            " ooo yeah gimme the plans ":
                $ oliganglv += 10
                hide oliverneutral at bottom
                show oliverhappy at center
                o " Sweet, let's get right into that then. "
                z " We've got a whole lot planned. "
                ed " So you better listen up! "
                scene black with dissolve
                " Due to budget, we don't really have a scene ready for this. "
                " But I can describe what's happening here for you. "
                " You spent the rest of free time talking with Oliver and the gang... "
                " Talking about bullying this guy named Abbie later. "
                " You're not sure how to feel about that, but you're in on that nonetheless. "
                " Even though you've probably defended that guy or not depending on what you chose. "
                " You don't really got a choice here - what the narrator says here is final. "
                " You wanted to talk more about the plan, but... "
                " The teacher came in. Bummer. "
                " You're just gonna have to continue this conversation later. "
                " Nothing interesting happened in math class. "
                " Just had to take down a few notes... "
                " And the teacher was just discussing for the most part. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for a break. "
                " You hopped out of your seat and you went out into the hallways to find a place to hangout in. "
                pause 2.0
                jump fribreak1
            " nah i'd game ":
                o " Haha, nerd. "
                ed " But go and get that grind on! "
                z " We can just tell you the plan later, if you're interested. "
                scene black with dissolve
                " You spent the rest of free time playing games on your phone. "
                " Just chilling there, and vibing... "
                " Doing nothing much, but you would sometimes listen to your classmates' conversations. "
                " The teacher soon arrived though, so you put your phone away. "
                " Nothing interesting happened in math class. "
                " Just had to take down a few notes... "
                " And the teacher was just discussing for the most part. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for a break. "
                " You hopped out of your seat and you went out into the hallways to find a place to hangout in. "
                pause 2.0
                jump fribreak1
    label lonelyassdrawing:
        " You didn't really know who to talk to for the free time. "
        " But you did know another thing that you can do... "
        " Gaming. Why socialize more when you can just game, right? "
        " You boot up your phone and started gaming... "
        scene black with dissolve
        " You spent the rest of free time playing games on your phone. "
        " Just chilling there, and vibing... "
        " Doing nothing much, but you would sometimes listen to your classmates' conversations. "
        " The teacher soon arrived though, so you put your phone away. "
        " Nothing interesting happened in math class. "
        " Just had to take down a few notes... "
        " And the teacher was just discussing for the most part. "
        play sound "audio/bellring.mp3"
        " The bell rings, looks like it's time for a break. "
        " You hopped out of your seat and you went out into the hallways to find a place to hangout in. "
        pause 2.0
        jump fribreak1
    # if mc gets certain amount of lv with a character, they get an interaction (only if they r in the same seat)

label fribreak1:
    scene hallway with dissolve
    if oligangjoin == True:
        jump oligangfri1
    else:
        pass
    " Where are you gonna hang out for this break? "
    menu:
        " {image=popularicon} The front of the school {image=engelicon} ":
            jump frontschoolfri1
        " {image=bubbleicon} The back of the school {image=cubbieicon} ":
            jump backschoolfri1
        " {image=kevinicon} The gym {image=skellicon} ":
            jump gymfri1
        " {image=robbyicon} The cafeteria {image=claireicon} ":
            jump cafeteriafri1
        " {image=abbieicon} The rooftop {image=rileyicon} ":
            jump rooftopfri1
        " {image=rubyicon} The library {image=lanaicon} ":
            jump libraryfri1
    label frontschoolfri1:
        # petunia, lizzy // engel
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked to the front of the school and spotted three of your classmates doing their own thing. "
        " You wanted to talk to them...but who do you talk to? "
        if popularknow == True and engelknow == True:
            menu:
                " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                    jump hermeswoah
                " {image=engelicon} Engel {image=engelicon} ":
                    jump odywoah
        elif popularknow == True and engelknow == False:
            menu:
                " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                    jump hermeswoah
                " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                    jump odywoah
        elif popularknow == False and engelknow == True:
            menu:
                " {image=popularicon} The popular girls {image=popularicon} ":
                    jump hermeswoah
                " {image=engelicon} Engel {image=engelicon} ":
                    jump odywoah
        else:
            menu:
                " {image=popularicon} The popular girls {image=popularicon} ":
                    jump hermeswoah
                " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                    jump odywoah
        label hermeswoah:
            show petunianeutral at left with easeinright
            show lizzyneutral at right with easeinright
            if popularknow == True:
                " You walked over to them and asked if they were doing alright. "
                " I mean, they did argue a whole lot yesterday. "
                " And they also apologized to eachother, and hopefully those apologies were genuine. "
                p " Heya there, [name]!! "
                lz " And yes, we're doing better now. "
                lz " Just a little misunderstanding I had... "
                lz " Honestly? it was a little stupid of me to get mad at something like THAT... "
                " She must be talking about the reason why she was mad in the first place. "
                " Huh...interesting. "
                p " I mean, you could've just said you were feeling down about that. "
                p " Makes you even more of an idiot that you didn't talk to me about it in the first place. "
                p " I don't mean that of course, but really... "
                p " You should start actually talking to me if you have any issues! "
                p " Not like I'd bite your ass for you just simply telling the truth. "
                lz " There ARE times where it felt like you were doing that to me though... "
                hide petunianeutral at bottom
                show petuniasurprised at left
                p " Wait, like...on god? "
                p " What the helly??? "
                p " Damn, sorry that I probably treated you like shit. "
                p " I probably treated you like a joke or something. "
                lz " Yeah, that's...kinda what you did. "
                lz " Everytime I told you about something serious, you took it as a joke. "
                lz " Like remember that one time I told you my cat died? "
                lz " Yeah, I was being serious. "
                p " OH SHIT. I thought you were refferencing that one meme... "
                p " May your cat rest in peace, Liz. "
                p " Sorry for taking that as a joke...really. "
                hide petuniasurprised at bottom
                show petuniasad at left
                p " Damn, now that I think about it... "
                p " I was kinda shitty to you. "
                lz " Yeah, but all of that is in the past now, right? "
                lz " We've already made up. Everything's cool now. "
                lz " Atleast you understand your mistakes and what you did wrong. "
                lz " If you didn't notice that, then I probably would've left forever. "
                lz " I don't really want that to happen... "
                lz " I wouldn't know what to do without you, honestly. "
                hide petuniasad at bottom
                show petunianeutral at left
                p " Well, I don't think you're leaving anytime soon! "
                p " I'm going to learn from my mistakes and take you more seriously!! "
                p " We ARE best friends, after all! "
                lz " ...Aww. "
                lz " Yeah, we're best friends...and I'm glad you're finally taking me more seriously. "
                lz " I really appreciate it. "
                p " I still feel a little bad for taking you as a joke, but... "
                p " I'm gonna prevent myself from doing that again! "
                lz " Nice. "
                scene black with dissolve
                " You spent the rest the of the break talking with Petunia and Lizzy. "
                " You were glad that they were doing well now... "
                " If Lizzy didn't talk with Petunia, they would've probably argued for a long time. "
                " Eeeeyikes. You didn't want to witness that happening. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassfri
            else:
                " You walked over to them and asked if they were doing alright. "
                " I mean, they did argue a whole lot yesterday, from what you've heard. "
                " And they also apologized to eachother, and hopefully those apologies were genuine. "
                x " Heya there, [name]!! "
                $ popularknow = True
                lz " Before we answer your question - I'm Lizzy. "
                p " And I'm Petunia! - and we're best friends! "
                lz " And yes, we're doing better now. "
                lz " Just a little misunderstanding I had... "
                lz " Honestly? it was a little stupid of me to get mad at something like THAT... "
                " She must be talking about the reason why she was mad in the first place. "
                " Huh...interesting. "
                p " I mean, you could've just said you were feeling down about that. "
                p " Makes you even more of an idiot that you didn't talk to me about it in the first place. "
                p " I don't mean that of course, but really... "
                p " You should start actually talking to me if you have any issues! "
                p " Not like I'd bite your ass for you just simply telling the truth. "
                lz " There ARE times where it felt like you were doing that to me though... "
                hide petunianeutral at bottom
                show petuniasurprised at left
                p " Wait, like...on god? "
                p " What the helly??? "
                p " Damn, sorry that I probably treated you like shit. "
                p " I probably treated you like a joke or something. "
                lz " Yeah, that's...kinda what you did. "
                lz " Everytime I told you about something serious, you took it as a joke. "
                lz " Like remember that one time I told you my cat died? "
                lz " Yeah, I was being serious. "
                p " OH SHIT. I thought you were refferencing that one meme... "
                p " May your cat rest in peace, Liz. "
                p " Sorry for taking that as a joke...really. "
                hide petuniasurprised at bottom
                show petuniasad at left
                p " Damn, now that I think about it... "
                p " I was kinda shitty to you. "
                lz " Yeah, but all of that is in the past now, right? "
                lz " We've already made up. Everything's cool now. "
                lz " Atleast you understand your mistakes and what you did wrong. "
                lz " If you didn't notice that, then I probably would've left forever. "
                lz " I don't really want that to happen... "
                lz " I wouldn't know what to do without you, honestly. "
                hide petuniasad at bottom
                show petunianeutral at left
                p " Well, I don't think you're leaving anytime soon! "
                p " I'm going to learn from my mistakes and take you more seriously!! "
                p " We ARE best friends, after all! "
                lz " ...Aww. "
                lz " Yeah, we're best friends...and I'm glad you're finally taking me more seriously. "
                lz " I really appreciate it. "
                p " I still feel a little bad for taking you as a joke, but... "
                p " I'm gonna prevent myself from doing that again! "
                lz " Nice. "
                scene black with dissolve
                " You spent the rest the of the break talking with Petunia and Lizzy. "
                " You were glad that they were doing well now... "
                " If Lizzy didn't talk with Petunia, they would've probably argued for a long time. "
                " Eeeeyikes. You didn't want to witness that happening. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassfri
        label odywoah:
            show engelneutral at center with easeinleft
            if engelknow == True:
                " You walked over to him and asked him what he was doing. "
                " You looked at where he was looking at, and... "
                " Huh. He was looking at some birds in the distance. "
                " They were on one of the trees, on a nest. "
                " You wonder what's so interesting about that... "
                hide engelneutral at bottom
                show engelhappy at center
                e " Hello there, [name]. "
                e " I've kind of noticed that there's been these birds on that tree over there... "
                e " I have never really noticed that they were there before, but now I have. "
                e " You see them? "
                e " That mother bird has been feeding her children very well. "
                e " She would come back every now and then to get some more food for her kids... "
                e " But I've noticed something strange. "
                hide engelhappy at bottom
                show engelneutral at center
                e " You see how there's three kids, right? "
                e " They look all happy, right? "
                e " But I've noticed that the mother won't feed this one child of hers... "
                e " Of course, I know that it isn't uncommon for mother birds to not feed one of their children... "
                e " But that doesn't mean that it isn't concerning. "
                e " I wonder why she doesn't feed them... "
                e " And I also wonder if that kid even got fed at all. "
                e " Poor thing... "
                e " Can't really do anything about it though. "
                e " The mother bird probably would've started going feral on me if I went too close. "
                e " Annnd I don't want to go to the next class with a bunch of scars on my face... "
                e " I have a feeling Miss Thavel would leave me alone for it, buuuut... "
                hide engelneutral at bottom
                show engelcontent at center
                e " I just know that Claire and Bubble would be so worried over me. "
                e " Like, really worried... "
                e " They would probably send me to the school's clinic. "
                e " They just care about me so much... "
                if engellv >= 15 or engellv == 15:
                    e " I care about them too, but... "
                    e " I care about you too. A whole lot. "
                    e " I hope you know that. "
                else:
                    e " And I of course care about them too. "
                    e " I wouldn't be a good friend if I didn't, after all. "
                    e " Friends are supposed to be caring about eachother together, of course. "
                hide engelcontent at bottom
                show engelhappy at center
                e " Hmhmmm... "
                e " I'll just be watching the birds here. "
                e " You can join me, if you feel like watching birds. "
                e " I know bird watching is a bit of a boring activity to some... "
                e " So I understand if you want to leave. "
                " You pretty much wanted to spend time with him, so you stayed. "
                e " Oh? you want to watch with me? "
                e " Well, I think we need some place to sit comfortably, if we're going to be bird watching... "
                e " How about that bench over there? looks like a neat place to sit and watch. "
                e " Cmere. "
                " You sat down on the bench that Engel mentioned, and you watched the birds with him. "
                scene black with dissolve
                " You spent the rest of the break watching birds with Engel. "
                " You and him talked here and there, about birds of course. "
                " It was actually peaceful, just talking with a buddy and relaxing. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassfri
            else:
                " You walked over to him and asked him what he was doing. "
                " You looked at where he was looking at, and... "
                " Huh. He was looking at some birds in the distance. "
                " They were on one of the trees, on a nest. "
                " You wonder what's so interesting about that... "
                hide engelneutral at bottom
                show engelhappy at center
                x " Hello there, [name]. "
                $ engelknow = True
                e " I'm Engel, by the way. I don't think I've introduced myself before to you. "
                e " I've kind of noticed that there's been these birds on that tree over there... "
                e " I have never really noticed that they were there before, but now I have. "
                e " You see them? "
                e " That mother bird has been feeding her children very well. "
                e " She would come back every now and then to get some more food for her kids... "
                e " But I've noticed something strange. "
                hide engelhappy at bottom
                show engelneutral at center
                e " You see how there's three kids, right? "
                e " They look all happy, right? "
                e " But I've noticed that the mother won't feed this one child of hers... "
                e " Of course, I know that it isn't uncommon for mother birds to not feed one of their children... "
                e " But that doesn't mean that it isn't concerning. "
                e " I wonder why she doesn't feed them... "
                e " And I also wonder if that kid even got fed at all. "
                e " Poor thing... "
                e " Can't really do anything about it though. "
                e " The mother bird probably would've started going feral on me if I went too close. "
                e " Annnd I don't want to go to the next class with a bunch of scars on my face... "
                e " I have a feeling Miss Thavel would leave me alone for it, buuuut... "
                hide engelneutral at bottom
                show engelcontent at center
                e " I just know that Claire and Bubble would be so worried over me. "
                e " Like, really worried... "
                e " They would probably send me to the school's clinic. "
                e " They just care about me so much... "
                if engellv >= 25 or engellv == 25:
                    e " I care about them too, but... "
                    e " I care about you too. A whole lot. "
                    e " I hope you know that. "
                else:
                    e " And I of course care about them too. "
                    e " I wouldn't be a good friend if I didn't, after all. "
                    e " Friends are supposed to be caring about eachother together, of course. "
                hide engelcontent at bottom
                show engelhappy at center
                e " Hmhmmm... "
                e " I'll just be watching the birds here. "
                e " You can join me, if you feel like watching birds. "
                e " I know bird watching is a bit of a boring activity to some... "
                e " So I understand if you want to leave. "
                " You pretty much wanted to spend time with him, so you stayed. "
                e " Oh? you want to watch with me? "
                e " Well, I think we need some place to sit comfortably, if we're going to be bird watching... "
                e " How about that bench over there? looks like a neat place to sit and watch. "
                e " Cmere. "
                " You sat down on the bench that Engel mentioned, and you watched the birds with him. "
                scene black with dissolve
                " You spent the rest of the break watching birds with Engel. "
                " You and him talked here and there, about birds of course. "
                " It was actually peaceful, just talking with a buddy and relaxing. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassfri
    label backschoolfri1:
        # bubble and cubbie
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of the school and found two of your classmates talking to eachother. "
        " Wondering what they're talking about, you decided to join their conversation. "
        show bubbleneutral at right with easeinleft
        show cubbieneutral at left with easeinleft
        if bubbleknow == True and cubbieknow == True:
            b " Heya, [name]!! "
            cb " ...!! "
            " The cat guy waves at you. "
            " You wave at him back out of politeness. "
            b " Me and Cubbie were just talking about the stuff for next week! "
            b " We have a lot to do next week... "
            b " Like - a lot, a lot!! "
            b " Hey, hold on... "
            b " That means you're going to suffer with us, too! "
            cb " ...!! "
            b " Don't worry, [name]! "
            b " Me and Cubbie will try our best to carry you! "
            b " Well, not literally, but... "
            b " You know what we mean! "
            b " We don't want you failing on your second week, after all! "
            cb " ... "
            b " That's right, Cubbie... "
            b " It would be really sad seeing you fail like that. "
            b " That's why we want to help you the best we can! "
            b " While we somehow study while doing helping you, too. "
            b " We MAY not understand certain things... "
            b " But we're going to try to explain to you about what we know! "
            cb " !! "
            " Cubbie points at the time on his phone. "
            " Looks like you guys only had a few minutes before break time ends... "
            " Seems like he wants to study right now. "
            hide bubbleneutral at bottom
            show bubbleconfuse at right
            b " Wait, only a few minutes until...oh crap. "
            b " We need to get into studying now! "
            b " I know this stuff is for next week, but... "
            b " We need to get ready and prepared for anything! "
            cb " !! "
            scene black with dissolve
            " You spent the rest of the break studying with Bubble and Cubbie. "
            " You actually learned a few things that you didn't know... "
            " Like learning what a quasar is. "
            " There's some people who don't know about that thing. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump languageclassfri
        elif bubbleknow == True and cubbieknow == False:
            b " Heya, [name]!! "
            x " ...!! "
            " The cat guy waves at you. "
            " You wave at him back out of politeness. "
            $ cubbieknow = True
            b " Me and Cubbie were just talking about the stuff for next week! "
            b " We have a lot to do next week... "
            b " Like - a lot, a lot!! "
            b " Hey, hold on... "
            b " That means you're going to suffer with us, too! "
            cb " ...!! "
            b " Don't worry, [name]! "
            b " Me and Cubbie will try our best to carry you! "
            b " Well, not literally, but... "
            b " You know what we mean! "
            b " We don't want you failing on your second week, after all! "
            cb " ... "
            b " That's right, Cubbie... "
            b " It would be really sad seeing you fail like that. "
            b " That's why we want to help you the best we can! "
            b " While we somehow study while doing helping you, too. "
            b " We MAY not understand certain things... "
            b " But we're going to try to explain to you about what we know! "
            cb " !! "
            " Cubbie points at the time on his phone. "
            " Looks like you guys only had a few minutes before break time ends... "
            " Seems like he wants to study right now. "
            hide bubbleneutral at bottom
            show bubbleconfuse at right
            b " Wait, only a few minutes until...oh crap. "
            b " We need to get into studying now! "
            b " I know this stuff is for next week, but... "
            b " We need to get ready and prepared for anything! "
            cb " !! "
            scene black with dissolve
            " You spent the rest of the break studying with Bubble and Cubbie. "
            " You actually learned a few things that you didn't know... "
            " Like learning what a quasar is. "
            " There's some people who don't know about that thing. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump languageclassfri
        elif bubbleknow == False and cubbieknow == True:
            x " Heya, [name]!! "
            cb " ...!! "
            " The cat guy waves at you. "
            " You wave at him back out of politeness. "
            $ bubbleknow = True
            x " I don't think we've met before, so... "
            b " I'm Bubble! It's nice to meet you! "
            b " Me and Cubbie were just talking about the stuff for next week! "
            b " We have a lot to do next week... "
            b " Like - a lot, a lot!! "
            b " Hey, hold on... "
            b " That means you're going to suffer with us, too! "
            cb " ...!! "
            b " Don't worry, [name]! "
            b " Me and Cubbie will try our best to carry you! "
            b " Well, not literally, but... "
            b " You know what we mean! "
            b " We don't want you failing on your second week, after all! "
            cb " ... "
            b " That's right, Cubbie... "
            b " It would be really sad seeing you fail like that. "
            b " That's why we want to help you the best we can! "
            b " While we somehow study while doing helping you, too. "
            b " We MAY not understand certain things... "
            b " But we're going to try to explain to you about what we know! "
            cb " !! "
            " Cubbie points at the time on his phone. "
            " Looks like you guys only had a few minutes before break time ends... "
            " Seems like he wants to study right now. "
            hide bubbleneutral at bottom
            show bubbleconfuse at right
            b " Wait, only a few minutes until...oh crap. "
            b " We need to get into studying now! "
            b " I know this stuff is for next week, but... "
            b " We need to get ready and prepared for anything! "
            cb " !! "
            scene black with dissolve
            " You spent the rest of the break studying with Bubble and Cubbie. "
            " You actually learned a few things that you didn't know... "
            " Like learning what a quasar is. "
            " There's some people who don't know about that thing. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump languageclassfri
        else:
            x " Heya, [name]!! "
            x " ...!! "
            " The cat guy waves at you. "
            " You wave at him back out of politeness. "
            $ bubbleknow = True
            x " I don't think we've met before, so... "
            b " I'm Bubble! It's nice to meet you! "
            $ cubbieknow = True
            b " Me and Cubbie were just talking about the stuff for next week! "
            b " We have a lot to do next week... "
            b " Like - a lot, a lot!! "
            b " Hey, hold on... "
            b " That means you're going to suffer with us, too! "
            cb " ...!! "
            b " Don't worry, [name]! "
            b " Me and Cubbie will try our best to carry you! "
            b " Well, not literally, but... "
            b " You know what we mean! "
            b " We don't want you failing on your second week, after all! "
            cb " ... "
            b " That's right, Cubbie... "
            b " It would be really sad seeing you fail like that. "
            b " That's why we want to help you the best we can! "
            b " While we somehow study while doing helping you, too. "
            b " We MAY not understand certain things... "
            b " But we're going to try to explain to you about what we know! "
            cb " !! "
            " Cubbie points at the time on his phone. "
            " Looks like you guys only had a few minutes before break time ends... "
            " Seems like he wants to study right now. "
            hide bubbleneutral at bottom
            show bubbleconfuse at right
            b " Wait, only a few minutes until...oh crap. "
            b " We need to get into studying now! "
            b " I know this stuff is for next week, but... "
            b " We need to get ready and prepared for anything! "
            cb " !! "
            scene black with dissolve
            " You spent the rest of the break studying with Bubble and Cubbie. "
            " You actually learned a few things that you didn't know... "
            " Like learning what a quasar is. "
            " There's some people who don't know about that thing. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump languageclassfri
    label gymfri1:
        # kevin and skell
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked to the gym and found two of your classmates doing their own thing. "
        " Who do you talk to? "
        if kevinknow == True and skellknow == True:
            menu:
                " {image=kevinicon} Kevin {image=kevinicon} ":
                    jump nerdington1
                " {image=skellicon} Skell {image=skellicon} ":
                    jump nerdington2
        elif kevinknow == True and skellknow == False:
            menu:
                " {image=kevinicon} Kevin {image=kevinicon} ":
                    jump nerdington1
                " {image=skellicon} An emo guy {image=skellicon} ":
                    jump nerdington2
        elif kevinknow == False and skellknow == True:
            menu:
                " {image=kevinicon} A nerd {image=kevinicon} ":
                    jump nerdington1
                " {image=skellicon} Skell {image=skellicon} ":
                    jump nerdington2
        else:
            menu:
                " {image=kevinicon} A nerd {image=kevinicon} ":
                    jump nerdington1
                " {image=skellicon} An emo guy {image=skellicon} ":
                    jump nerdington2
        label nerdington1:
            show kevinneutral at center with easeinright
            if kevinknow == True:
                " You walked over to him and asked him what he was doing. "
                kv " Oh, [name]. "
                kv " I'm quite glad to see you here. "
                kv " I need to ask you a question.. "
                kv " You do know how 'shipping' works, right? "
                kv " In relationships, not package shipping. "
                kv " If you don't - I'll give you an explanation. "
                kv " So, you know how there's going to be a community if a game gets really popular, right? "
                kv " Like, let's say for exmaple...ummm... "
                kv " Spork 3. That one's pretty popular. "
                kv " There's characters that people are going to ship in that game. "
                kv " In other words, people are going to make unofficial relationships with two characters from that game. "
                kv " Even if they're friends, even if they're enemies. "
                kv " There's also some other concerning ones that I'd rather not mention. "
                kv " Those ones are...pretty disgusting, if you ask me. "
                kv " But, anyway... "
                kv " I've been recently hearing about a pairing in our classroom. "
                kv " I've asked a few people about it, and all they could say was... "
                hide kevinneutral at bottom
                show kevinconfused at center
                kv " Skelvin. "
                kv " I genuinely don't know who they're pairing up. "
                kv " I've tried to figure it out, but I just couldn't find anything about it... "
                kv " But, whoever IS in the pair, hope they're all cool with being a little popular in the classroom. "
                hide kevinconfused at bottom
                show kevinneutral at center
                kv " I might start shipping them myself. "
                kv " Only if they would be a good pair though. "
                kv " I don't want anything toxic. "
                " Due to reasons, Skellvin isn't actually canon in here. "
                " To prevent anyone being mad or anything. "
                " I don't want to wake up with weapons on my neck. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin. "
                " Now you're a little bit interested in that whole pairing thing... "
                " But, you shouldn't really think too much about it. "
                " Pairings and relationships aren't really your thing. "
                " You're in school, after all. Gotta focus on education first. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom. "
                pause 2.0
                jump languageclassfri
            else:
                " You walked over to him and asked him what he was doing. "
                x " Oh, [name]. "
                x " I'm quite glad to see you here. "
                x " I don't believe we've met before... "
                $ kevinknow = True
                kv " I'm Kevin. Your classmate. It's nice to meet you, and... "
                kv " I need to ask you a question.. "
                kv " You do know how 'shipping' works, right? "
                kv " In relationships, not package shipping. "
                kv " If you don't - I'll give you an explanation. "
                kv " So, you know how there's going to be a community if a game gets really popular, right? "
                kv " Like, let's say for exmaple...ummm... "
                kv " Spork 3. That one's pretty popular. "
                kv " There's characters that people are going to ship in that game. "
                kv " In other words, people are going to make unofficial relationships with two characters from that game. "
                kv " Even if they're friends, even if they're enemies. "
                kv " There's also some other concerning ones that I'd rather not mention. "
                kv " Those ones are...pretty disgusting, if you ask me. "
                kv " But, anyway... "
                kv " I've been recently hearing about a pairing in our classroom. "
                kv " I've asked a few people about it, and all they could say was... "
                hide kevinneutral at bottom
                show kevinconfused at center
                kv " Skelvin. "
                kv " I genuinely don't know who they're pairing up. "
                kv " I've tried to figure it out, but I just couldn't find anything about it... "
                kv " But, whoever IS in the pair, hope they're all cool with being a little popular in the classroom. "
                hide kevinconfused at bottom
                show kevinneutral at center
                kv " I might start shipping them myself. "
                kv " Only if they would be a good pair though. "
                kv " I don't want anything toxic. "
                " Due to reasons, Skellvin isn't actually canon in here. "
                " To prevent anyone being mad or anything. "
                " I don't want to wake up with weapons on my neck. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin. "
                " Now you're a little bit interested in that whole pairing thing... "
                " But, you shouldn't really think too much about it. "
                " Pairings and relationships aren't really your thing. "
                " You're in school, after all. Gotta focus on education first. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom. "
                pause 2.0
                jump languageclassfri
        label nerdington2:
            show skellneutral at center with easeinleft
            if skellknow == True:
                " You walked over to him and asked him what he was doing. "
                " Looks like he was looking at stuff on his phone... "
                " Looking at the classrooms GC to be specific. "
                " You took a closer look at the messages he was looking at... "
                " Huh. It's just Oliver saying 'Skellvin is canon'. "
                " Before everyone comes after me, nope - it's not actually canon. "
                " No shipping in this game will ever be canon to prevent anything bad from happening. "
                " Back to the actual game... "
                sk " ...Oh, uh.. "
                sk " Hi there, [name]. "
                " You noticed that he was looking a bit pissed off. "
                " You decided to ask him if he was doing alright. "
                sk " ...Yeah, I'm fine. "
                sk " It's just Oliver trying to ragebait me again. "
                " You politely asked him: how exactly was he ragebaiting him? "
                " You got even more curious now. "
                sk " Well, let me explain that to you... "
                sk " See that message he just recently sent? "
                hide skellneutral at bottom
                show skellangry at center
                sk " Yeah, it's basically him shipping me and Kevin together. "
                sk " I don't...really like hearing that from him. "
                sk " For a fact - I'm not even interested in Kevin that way. "
                sk " I'd rather much look for a partner in the future than right now. "
                sk " He's been...saying stuff like that for awhile now. "
                sk " And I've been trying to get myself to not fall for his ragebaiting technique. "
                sk " I really have been, but... "
                sk " It's been getting hard for me to hold back from throwing an entire chair at him. "
                sk " You have no idea how it feels to get paired with someone you don't even like... "
                sk " It feels really annoying - especially whenever people start believing that it's real. "
                hide skellangry at bottom
                show skellneutral at center
                sk " Eugh... "
                sk " Sorry that I kind of...started ranting to you. "
                sk " But really, I don't like Kevin that way. "
                sk " He's a good dude, truly - but he's just not someone I'd get with. "
                sk " Besides, we barely even talk with eachother. "
                sk " Sigh...I wish there was some way to just stop Oliver from doing shit like this. "
                sk " But we can't do anything. "
                sk " Can't do anything because somehow - he got the teachers favoring him. "
                sk " Like, what kind of bullshit is that?? "
                sk " ...This school drives me insane. "
                sk " I honestly just can't wait for summer break to hit. "
                sk " A break from this school would be really good. "
                scene black with dissolve
                " You spent the rest of the break talking with Skell. "
                " Being shipped with someone you don't know too well? oh boy, that's a nightmare. "
                " You'd never want to expirience that in your life. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom. "
                pause 2.0
                jump languageclassfri
            else:
                " You walked over to him and asked him what he was doing. "
                " Looks like he was looking at stuff on his phone... "
                " Looking at the classrooms GC to be specific. "
                " You took a closer look at the messages he was looking at... "
                " Huh. It's just Oliver saying 'Skellvin is canon'. "
                " Before everyone comes after me, nope - it's not actually canon. "
                " No shipping in this game will ever be canon to prevent anything bad from happening. "
                " Back to the actual game... "
                x " ...Oh, uh.. "
                x " Hi there, [name]. "
                x " Don't think we've met before, so uh... "
                $ skellknow = True
                sk " I'm Skell. It's nice to meet you. "
                " You noticed that he was looking a bit pissed off. "
                " You decided to ask him if he was doing alright. "
                sk " ...Yeah, I'm fine. "
                sk " It's just Oliver trying to ragebait me again. "
                " You politely asked him: how exactly was he ragebaiting him? "
                " You got even more curious now. "
                sk " Well, let me explain that to you... "
                sk " See that message he just recently sent? "
                hide skellneutral at bottom
                show skellangry at center
                sk " Yeah, it's basically him shipping me and Kevin together. "
                sk " I don't...really like hearing that from him. "
                sk " For a fact - I'm not even interested in Kevin that way. "
                sk " I'd rather much look for a partner in the future than right now. "
                sk " He's been...saying stuff like that for awhile now. "
                sk " And I've been trying to get myself to not fall for his ragebaiting technique. "
                sk " I really have been, but... "
                sk " It's been getting hard for me to hold back from throwing an entire chair at him. "
                sk " You have no idea how it feels to get paired with someone you don't even like... "
                sk " It feels really annoying - especially whenever people start believing that it's real. "
                hide skellangry at bottom
                show skellneutral at center
                sk " Eugh... "
                sk " Sorry that I kind of...started ranting to you. "
                sk " But really, I don't like Kevin that way. "
                sk " He's a good dude, truly - but he's just not someone I'd get with. "
                sk " Besides, we barely even talk with eachother. "
                sk " Sigh...I wish there was some way to just stop Oliver from doing shit like this. "
                sk " But we can't do anything. "
                sk " Can't do anything because somehow - he got the teachers favoring him. "
                sk " Like, what kind of bullshit is that?? "
                sk " ...This school drives me insane. "
                sk " I honestly just can't wait for summer break to hit. "
                sk " A break from this school would be really good. "
                scene black with dissolve
                " You spent the rest of the break talking with Skell. "
                " Being shipped with someone you don't know too well? oh boy, that's a nightmare. "
                " You'd never want to expirience that in your life. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom. "
                pause 2.0
                jump languageclassfri
    label cafeteriafri1:
        # robby and claire
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        if clairebeatup == True:
            " Ooops, can't interact with these people. "
            " Sorry, but I'm pretty sure you know the reason why. "
            scene black
            pause 2.0
            jump languageclassfri
        else:
            pass
        " You walked into the cafeteria and spotted two of your classmates talking to eachother. "
        " Wondering what they're talking about, you decided to sit next to them. "
        show robbyneutral at left with easeinright
        show claireneutral at right with easeinright
        if robbyknow == True and claireknow == True:
            rb " Oh hey, [name]'s here. "
            hide claireneutral at bottom
            show clairehappy at right
            c " Hiya, [name]! "
            c " Me and Robby were just talking about this new game that came out! "
            rb " I'm not too much of the type to play games, but... "
            hide clairehappy at bottom
            show claireneutral at right
            rb " I let myself relax sometimes. "
            c " You've gotta get a WHOLE lot of rest, Robby. "
            c " Pretty sure I don't want to see you running on 1 braincell per day. "
            c " That would be very un-Robby like. "
            rb " Hmmm...I'll think about it. "
            rb " I could play the game more, if that's what you wanted. "
            c " Well - you can't just play this game over and over again... "
            c " You've gotta try out other games, too! "
            hide robbyneutral at bottom
            show robbyconfused at left
            rb " ...Like what? "
            rb " I'm not too much of a gamer myself, so... "
            rb " I don't really know my choices here. "
            c " Well, I've got a few good options! "
            c " If you like the game I was talking about earlier... "
            c " You could go to the creator's page and look at their other games! "
            c " ...Uh, that IS if they have any other games. "
            c " I haven't actually checked their page out too much. "
            c " But if you have other creators that you like, you could check their pages too! "
            rb " Hm, interesting... "
            c " And if you don't like those games that they made... "
            c " You could just watch videos reccomending some underrated cool games! "
            c " Or you could go up to me and ask for some game reccomendations, hehe. "
            c " I usually focus on studying here and there...but! "
            c " I also let myself relax every now and then and let myself play some games. "
            c " Though I make sure not to game too much, since I have to study. "
            hide robbyconfused at bottom
            show robbyneutral at left
            rb " Sounds like you've got a solid plan there. "
            c " Yup! "
            c " But there HAVE been some times where I accidentally forgot to study because of games... "
            c " I think this is sort of the reason why parents blame things on the phone. "
            c " You can get distracted easily by enjoying the game and can lose track of time. "
            c " Using games to relax isn't bad, really - "
            c " You just need to keep track of the time to make sure you don't accidentally stay up. "
            c " Otherwiiiisee, you're going to just study at school. "
            c " And that isn't fun when exams are coming up. "
            rb " ...Huh. "
            rb " Alright, thanks for your advice, Claire. "
            c " No problem! "
            c " I just want you to relax more, since... "
            c " I keep seeing you stress yourself out, you know? "
            c " Stressing yourself out constantly isn't a good thing. "
            c " You should atleast take actual breaks here and there! "
            c " Not just short, one minute breaks... "
            c " That's also not good for you. "
            rb " ...I know, but... "
            rb " Can't really have a break with that one person always nagging me. "
            c " ...Ooooh, okay... "
            c " I get who you're trying to get at now. "
            c " But, still... "
            c " Breaks are important! "
            c " Let's just say... "
            c " If you don't take a break, you're going to be burnt out and your project will be all messy, "
            c " You don't want that now, do you? "
            rb " ...I guess not. "
            rb " Okay, fine... "
            rb " I'll start taking breaks more often. "
            c " Good! as you should. "
            scene black with dissolve
            " You spent the rest of the break talking with Claire and Robby. "
            " You wonder who Robby was talking about... "
            " Most likely going to be that Riley girl you've been hearing about. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump languageclassfri
        elif robbyknow == True and claireknow == False:
            rb " Oh hey, [name]'s here. "
            hide claireneutral at bottom
            show clairehappy at right
            x " Hiya, [name]! "
            x " Oh, hold on... I don't think I've met you before! "
            x " Lemme introduce myself... "
            $ claireknow = True
            c " I'm Claire, it's nice to meet you! "
            c " Me and Robby were just talking about this new game that came out! "
            rb " I'm not too much of the type to play games, but... "
            hide clairehappy at bottom
            show claireneutral at right
            rb " I let myself relax sometimes. "
            c " You've gotta get a WHOLE lot of rest, Robby. "
            c " Pretty sure I don't want to see you running on 1 braincell per day. "
            c " That would be very un-Robby like. "
            rb " Hmmm...I'll think about it. "
            rb " I could play the game more, if that's what you wanted. "
            c " Well - you can't just play this game over and over again... "
            c " You've gotta try out other games, too! "
            hide robbyneutral at bottom
            show robbyconfused at left
            rb " ...Like what? "
            rb " I'm not too much of a gamer myself, so... "
            rb " I don't really know my choices here. "
            c " Well, I've got a few good options! "
            c " If you like the game I was talking about earlier... "
            c " You could go to the creator's page and look at their other games! "
            c " ...Uh, that IS if they have any other games. "
            c " I haven't actually checked their page out too much. "
            c " But if you have other creators that you like, you could check their pages too! "
            rb " Hm, interesting... "
            c " And if you don't like those games that they made... "
            c " You could just watch videos reccomending some underrated cool games! "
            c " Or you could go up to me and ask for some game reccomendations, hehe. "
            c " I usually focus on studying here and there...but! "
            c " I also let myself relax every now and then and let myself play some games. "
            c " Though I make sure not to game too much, since I have to study. "
            hide robbyconfused at bottom
            show robbyneutral at left
            rb " Sounds like you've got a solid plan there. "
            c " Yup! "
            c " But there HAVE been some times where I accidentally forgot to study because of games... "
            c " I think this is sort of the reason why parents blame things on the phone. "
            c " You can get distracted easily by enjoying the game and can lose track of time. "
            c " Using games to relax isn't bad, really - "
            c " You just need to keep track of the time to make sure you don't accidentally stay up. "
            c " Otherwiiiisee, you're going to just study at school. "
            c " And that isn't fun when exams are coming up. "
            rb " ...Huh. "
            rb " Alright, thanks for your advice, Claire. "
            c " No problem! "
            c " I just want you to relax more, since... "
            c " I keep seeing you stress yourself out, you know? "
            c " Stressing yourself out constantly isn't a good thing. "
            c " You should atleast take actual breaks here and there! "
            c " Not just short, one minute breaks... "
            c " That's also not good for you. "
            rb " ...I know, but... "
            rb " Can't really have a break with that one person always nagging me. "
            c " ...Ooooh, okay... "
            c " I get who you're trying to get at now. "
            c " But, still... "
            c " Breaks are important! "
            c " Let's just say... "
            c " If you don't take a break, you're going to be burnt out and your project will be all messy, "
            c " You don't want that now, do you? "
            rb " ...I guess not. "
            rb " Okay, fine... "
            rb " I'll start taking breaks more often. "
            c " Good! as you should. "
            scene black with dissolve
            " You spent the rest of the break talking with Claire and Robby. "
            " You wonder who Robby was talking about... "
            " Most likely going to be that Riley girl you've been hearing about. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump languageclassfri
        elif robbyknow == False and claireknow == True:
            x " Oh hey, [name]'s here. "
            hide claireneutral at bottom
            show clairehappy at right
            c " Hiya, [name]! "
            $ robbyknow = True
            c " Me and Robby were just talking about this new game that came out! "
            rb " I'm not too much of the type to play games, but... "
            hide clairehappy at bottom
            show claireneutral at right
            rb " I let myself relax sometimes. "
            c " You've gotta get a WHOLE lot of rest, Robby. "
            c " Pretty sure I don't want to see you running on 1 braincell per day. "
            c " That would be very un-Robby like. "
            rb " Hmmm...I'll think about it. "
            rb " I could play the game more, if that's what you wanted. "
            c " Well - you can't just play this game over and over again... "
            c " You've gotta try out other games, too! "
            hide robbyneutral at bottom
            show robbyconfused at left
            rb " ...Like what? "
            rb " I'm not too much of a gamer myself, so... "
            rb " I don't really know my choices here. "
            c " Well, I've got a few good options! "
            c " If you like the game I was talking about earlier... "
            c " You could go to the creator's page and look at their other games! "
            c " ...Uh, that IS if they have any other games. "
            c " I haven't actually checked their page out too much. "
            c " But if you have other creators that you like, you could check their pages too! "
            rb " Hm, interesting... "
            c " And if you don't like those games that they made... "
            c " You could just watch videos reccomending some underrated cool games! "
            c " Or you could go up to me and ask for some game reccomendations, hehe. "
            c " I usually focus on studying here and there...but! "
            c " I also let myself relax every now and then and let myself play some games. "
            c " Though I make sure not to game too much, since I have to study. "
            hide robbyconfused at bottom
            show robbyneutral at left
            rb " Sounds like you've got a solid plan there. "
            c " Yup! "
            c " But there HAVE been some times where I accidentally forgot to study because of games... "
            c " I think this is sort of the reason why parents blame things on the phone. "
            c " You can get distracted easily by enjoying the game and can lose track of time. "
            c " Using games to relax isn't bad, really - "
            c " You just need to keep track of the time to make sure you don't accidentally stay up. "
            c " Otherwiiiisee, you're going to just study at school. "
            c " And that isn't fun when exams are coming up. "
            rb " ...Huh. "
            rb " Alright, thanks for your advice, Claire. "
            c " No problem! "
            c " I just want you to relax more, since... "
            c " I keep seeing you stress yourself out, you know? "
            c " Stressing yourself out constantly isn't a good thing. "
            c " You should atleast take actual breaks here and there! "
            c " Not just short, one minute breaks... "
            c " That's also not good for you. "
            rb " ...I know, but... "
            rb " Can't really have a break with that one person always nagging me. "
            c " ...Ooooh, okay... "
            c " I get who you're trying to get at now. "
            c " But, still... "
            c " Breaks are important! "
            c " Let's just say... "
            c " If you don't take a break, you're going to be burnt out and your project will be all messy, "
            c " You don't want that now, do you? "
            rb " ...I guess not. "
            rb " Okay, fine... "
            rb " I'll start taking breaks more often. "
            c " Good! as you should. "
            scene black with dissolve
            " You spent the rest of the break talking with Claire and Robby. "
            " You wonder who Robby was talking about... "
            " Most likely going to be that Riley girl you've been hearing about. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump languageclassfri
        else:
            x " Oh hey, [name]'s here. "
            hide claireneutral at bottom
            show clairehappy at right
            x " Hiya, [name]! "
            x " Oh, hold on... I don't think I've met you before! "
            x " Lemme introduce myself... "
            $ claireknow = True
            c " I'm Claire, it's nice to meet you! "
            $ robbyknow = True
            c " Me and Robby were just talking about this new game that came out! "
            rb " I'm not too much of the type to play games, but... "
            hide clairehappy at bottom
            show claireneutral at right
            rb " I let myself relax sometimes. "
            c " You've gotta get a WHOLE lot of rest, Robby. "
            c " Pretty sure I don't want to see you running on 1 braincell per day. "
            c " That would be very un-Robby like. "
            rb " Hmmm...I'll think about it. "
            rb " I could play the game more, if that's what you wanted. "
            c " Well - you can't just play this game over and over again... "
            c " You've gotta try out other games, too! "
            hide robbyneutral at bottom
            show robbyconfused at left
            rb " ...Like what? "
            rb " I'm not too much of a gamer myself, so... "
            rb " I don't really know my choices here. "
            c " Well, I've got a few good options! "
            c " If you like the game I was talking about earlier... "
            c " You could go to the creator's page and look at their other games! "
            c " ...Uh, that IS if they have any other games. "
            c " I haven't actually checked their page out too much. "
            c " But if you have other creators that you like, you could check their pages too! "
            rb " Hm, interesting... "
            c " And if you don't like those games that they made... "
            c " You could just watch videos reccomending some underrated cool games! "
            c " Or you could go up to me and ask for some game reccomendations, hehe. "
            c " I usually focus on studying here and there...but! "
            c " I also let myself relax every now and then and let myself play some games. "
            c " Though I make sure not to game too much, since I have to study. "
            hide robbyconfused at bottom
            show robbyneutral at left
            rb " Sounds like you've got a solid plan there. "
            c " Yup! "
            c " But there HAVE been some times where I accidentally forgot to study because of games... "
            c " I think this is sort of the reason why parents blame things on the phone. "
            c " You can get distracted easily by enjoying the game and can lose track of time. "
            c " Using games to relax isn't bad, really - "
            c " You just need to keep track of the time to make sure you don't accidentally stay up. "
            c " Otherwiiiisee, you're going to just study at school. "
            c " And that isn't fun when exams are coming up. "
            rb " ...Huh. "
            rb " Alright, thanks for your advice, Claire. "
            c " No problem! "
            c " I just want you to relax more, since... "
            c " I keep seeing you stress yourself out, you know? "
            c " Stressing yourself out constantly isn't a good thing. "
            c " You should atleast take actual breaks here and there! "
            c " Not just short, one minute breaks... "
            c " That's also not good for you. "
            rb " ...I know, but... "
            rb " Can't really have a break with that one person always nagging me. "
            c " ...Ooooh, okay... "
            c " I get who you're trying to get at now. "
            c " But, still... "
            c " Breaks are important! "
            c " Let's just say... "
            c " If you don't take a break, you're going to be burnt out and your project will be all messy, "
            c " You don't want that now, do you? "
            rb " ...I guess not. "
            rb " Okay, fine... "
            rb " I'll start taking breaks more often. "
            c " Good! as you should. "
            scene black with dissolve
            " You spent the rest of the break talking with Claire and Robby. "
            " You wonder who Robby was talking about... "
            " Most likely going to be that Riley girl you've been hearing about. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump languageclassfri
    label rooftopfri1:
        # abbie and riley
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked to the rooftop and found two of your classmates doing their own things. "
        " You wanted to talk to one of them...but who do you talk to? "
        if abbieknow == True and rileyknow == True:
            menu:
                " {image=abbieicon} Abbie {image=abbieicon} ":
                    jump mindsconfined
                " {image=rileyicon} Riley {image=rileyicon} ":
                    jump boundtoearth
        elif abbieknow == True and rileyknow == False:
            menu:
                " {image=abbieicon} Abbie {image=abbieicon} ":
                    jump mindsconfined
                " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                    jump boundtoearth
        elif abbieknow == False and rileyknow == True:
            menu:
                " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                    jump mindsconfined
                " {image=rileyicon} Riley {image=rileyicon} ":
                    jump boundtoearth
        else:
            menu:
                " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                    jump mindsconfined
                " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                    jump boundtoearth
        label mindsconfined:
            show abbieneutral at center with easeinleft
            if abbieknow == True:
                " You walked over to him, and asked him what he was doing. "
                a " Oh, um...hi, [name]... "
                a " I've been kind of looking at the clouds for awhile... "
                a " And...um... "
                a " L-listen...I don't want to be mean... "
                a " I-I'm not the type of person to judge, okay...? "
                a " But... "
                a " The reason why I've been looking at the clouds... "
                a " I've been trying to ignore...that girl over there... "
                " He points over to the other girl on the rooftop. "
                " She was staring intensly at a photo on her phone... "
                " Hey, wait...you recognize her as one of your classmates. "
                " She's that one who's obsessed with Oliver. "
                " Yeah, yikes...you can see why Abbie wants to avoid her... "
                a " She's been giggling at that one photo of Oliver for a few minutes now... "
                a " I don't want to judge someone for liking who they like, really... "
                a " ...But...don't you think that...taking photos of someone you like...is a little obsessive...? "
                " I have a strong feeling this is going to call out some of you. "
                " Yeah, you guys aren't that slick. "
                " If you don't do that, good for you. "
                a " ...I don't mean to be mean, but... "
                a " ...Isn't seeing that person everyday enough...? "
                a " B-besides, what would they think if they found out about the photos...? "
                a " They would most certainly think that you're weird, that's for sure... "
                a " ...I h-hope she didn't hear anything of what I said... "
                a " I'm sure if she heard what I said... "
                a " She would probably start chasing me down with a knife... "
                a " I've seen her do it before, and it's scary... "
                a " But I just had to be honest there... "
                a " If I had someone that I'm interested in... "
                a " I most certainly wouldn't want to take photos of them... "
                a " ..I just want to talk with them normally, you know...? "
                a " Instead of...being all creepy with them... "
                a " Please don't tell her I said all of this to you... "
                a " You know what would happen if you did... "
                " Yeah, you're also pretty sure your ass would get beat. "
                " I mean, you telling someone doesn't like her for who she likes... "
                " Pretty sure she would come at you first before going after Abbie. "
                " You did NOT want a knife being shoved up your ass. "
                " You promised Abbie that you won't tell. "
                a " Whew, thanks... "
                a " Um...we should probably talk about something else... "
                a " ...Before she, um... "
                a " Notices that we're kind of talking about her right now... "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie. "
                " Geez...didn't know some people could be so obsessed with someone. "
                " You're not one to judge, but uh... "
                " Abbie was lowkey right with the whole 'seeing them everyday at school is enough'. "
                " If it's not at school, then just keep on texting them if they're free. "
                " Just don't bother them too much if they're busy. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassfri
            else:
                " You walked over to him, and asked him what he was doing. "
                x " Oh, um...hi, [name]... "
                x " I, uh... "
                x " I don't think we've met before... "
                x " Um... "
                x " (Gee, I should probably introduce myself...) "
                x " (This is really awkward...) "
                $ abbieknow = True
                a " I'm Abbie, and uh... "
                a " I've been kind of looking at the clouds for awhile... "
                a " And...um... "
                a " L-listen...I don't want to be mean... "
                a " I-I'm not the type of person to judge, okay...? "
                a " But... "
                a " The reason why I've been looking at the clouds... "
                a " I've been trying to ignore...that girl over there... "
                " He points over to the other girl on the rooftop. "
                " She was staring intensly at a photo on her phone... "
                " Hey, wait...you recognize her as one of your classmates. "
                " She's that one who's obsessed with Oliver. "
                " Yeah, yikes...you can see why Abbie wants to avoid her... "
                a " She's been giggling at that one photo of Oliver for a few minutes now... "
                a " I don't want to judge someone for liking who they like, really... "
                a " ...But...don't you think that...taking photos of someone you like...is a little obsessive...? "
                " I have a strong feeling this is going to call out some of you. "
                " Yeah, you guys aren't that slick. "
                " If you don't do that, good for you. "
                a " ...I don't mean to be mean, but... "
                a " ...Isn't seeing that person everyday enough...? "
                a " B-besides, what would they think if they found out about the photos...? "
                a " They would most certainly think that you're weird, that's for sure... "
                a " ...I h-hope she didn't hear anything of what I said... "
                a " I'm sure if she heard what I said... "
                a " She would probably start chasing me down with a knife... "
                a " I've seen her do it before, and it's scary... "
                a " But I just had to be honest there... "
                a " If I had someone that I'm interested in... "
                a " I most certainly wouldn't want to take photos of them... "
                a " ..I just want to talk with them normally, you know...? "
                a " Instead of...being all creepy with them... "
                a " Please don't tell her I said all of this to you... "
                a " You know what would happen if you did... "
                " Yeah, you're also pretty sure your ass would get beat. "
                " I mean, you telling someone doesn't like her for who she likes... "
                " Pretty sure she would come at you first before going after Abbie. "
                " You did NOT want a knife being shoved up your ass. "
                " You promised Abbie that you won't tell. "
                a " Whew, thanks... "
                a " Um...we should probably talk about something else... "
                a " ...Before she, um... "
                a " Notices that we're kind of talking about her right now... "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie. "
                " Geez...didn't know some people could be so obsessed with someone. "
                " You're not one to judge, but uh... "
                " Abbie was lowkey right with the whole 'seeing them everyday at school is enough'. "
                " If it's not at school, then just keep on texting them if they're free. "
                " Just don't bother them too much if they're busy. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassfri
        label boundtoearth:
            show rileyneutral at center with easeinright
            if rileyknow == True:
                " You walked over to her and asked her what she was doing. "
                ri " Heheh. "
                ri " HEHEHEHH. "
                " Okay now you're starting to think that this was a bad idea. "
                " Walking up to her, I mean. "
                " Maybe you shouldn't have walked over to her. "
                " You can't back out now though. "
                " You already made the choice to talk to her. "
                ri " HehehhhhHEYYYY [name]!! "
                ri " I've just been. Staring at this photo Oliver posted. "
                ri " Can't help but feel a little. Ticked off by it. "
                ri " Just a little though! "
                ri " I'm totally not going to throw a chair off the building right now!! "
                ri " I mean, take a look at this photo!!! "
                " She practically shoves the phone up to your face. "
                " You move the phone back a little bit since it was a little too close for your eyes... "
                " And saw the photo that she was talking about. "
                " It was a photo of Oliver giving someone a gift. "
                " It was a girl with brown hair and a tiara... "
                " She also had a long dark blue-ish dress."
                " You've never really seen this person before, but... "
                " She looks oddly familiar. Oh, I wonder why. "
                " You asked her what the problem was with the photo. "
                hide rileyneutral at bottom
                show rileyangry at center
                ri " DON'T YOU GET IT?! "
                ri " He's supposed to be the one giving gifts to me! "
                ri " Not HER! "
                ri " It should ALWAYS be me! "
                ri " No one else! "
                " ...You told her that she could just imagine Oliver giving gifts to her. "
                " Or she could just draw out a scenario. "
                " It's not real, but atleast your thoughts can feed into your delusions. "
                " Just for a bit, atleast. "
                hide rileyangry at bottom
                show rileyneutral at center
                ri " ...Hmmmm... "
                ri " You're kind of right on that one! "
                ri " Waaaiiit... "
                hide rileyneutral at bottom
                show rileyhappy at center
                ri " Oh, oh! you just gave me a wonderful idea! "
                ri " I can just take the photo, right? "
                ri " Edit the girl out... "
                ri " And then edit myself into the picture! "
                ri " Pretty good idea, right? "
                ri " I could also put this into my page! "
                ri " Aaaah, and then I could flex on the others about this...! "
                ri " Hmmmhmm, what a great plan... "
                ri " Thank you for giving me this idea, [name]! "
                " ...You're not exactly sure on how to feel about this. "
                " But, you just gave her a thumbs up as a response. "
                " Atleast she's happy and not mad? "
                " If she was mad, she'd probably throw all of the chairs in the school down the building. "
                " Yeah, that's most likely to happen if she was mad... "
                " Just judging by how she acts though. "
                scene black with dissolve
                " You spent the rest of the break talking with Riley. "
                " More like listening to her with her ideas... "
                " Her ideas aren't really mad, it's just that all of them are Oliver related. "
                " You're lowkey starting to get tired about the whole Oliver thing going on with her... "
                " But you've gotta pretend that you're actually listening. "
                " Otherwise, you might be thrown off of the building. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassfri
            else:
                " You walked over to her and asked her what she was doing. "
                x " Heheh. "
                x " HEHEHEHH. "
                " Okay now you're starting to think that this was a bad idea. "
                " Walking up to her, I mean. "
                " Maybe you shouldn't have walked over to her. "
                " You can't back out now though. "
                " You already made the choice to talk to her. "
                x " HehehhhhHEYYYY [name]!! "
                $ rileyknow = True
                ri " IT'S ME!! RILEY!! AND!! "
                ri " I've just been. Staring at this photo Oliver posted. "
                ri " Can't help but feel a little. Ticked off by it. "
                ri " Just a little though! "
                ri " I'm totally not going to throw a chair off the building right now!! "
                ri " I mean, take a look at this photo!!! "
                " She practically shoves the phone up to your face. "
                " You move the phone back a little bit since it was a little too close for your eyes... "
                " And saw the photo that she was talking about. "
                " It was a photo of Oliver giving someone a gift. "
                " It was a girl with brown hair and a tiara... "
                " She also had a long dark blue-ish dress."
                " You've never really seen this person before, but... "
                " She looks oddly familiar. Oh, I wonder why. "
                " You asked her what the problem was with the photo. "
                hide rileyneutral at bottom
                show rileyangry at center
                ri " DON'T YOU GET IT?! "
                ri " He's supposed to be the one giving gifts to me! "
                ri " Not HER! "
                ri " It should ALWAYS be me! "
                ri " No one else! "
                " ...You told her that she could just imagine Oliver giving gifts to her. "
                " Or she could just draw out a scenario. "
                " It's not real, but atleast your thoughts can feed into your delusions. "
                " Just for a bit, atleast. "
                hide rileyangry at bottom
                show rileyneutral at center
                ri " ...Hmmmm... "
                ri " You're kind of right on that one! "
                ri " Waaaiiit... "
                hide rileyneutral at bottom
                show rileyhappy at center
                ri " Oh, oh! you just gave me a wonderful idea! "
                ri " I can just take the photo, right? "
                ri " Edit the girl out... "
                ri " And then edit myself into the picture! "
                ri " Pretty good idea, right? "
                ri " I could also put this into my page! "
                ri " Aaaah, and then I could flex on the others about this...! "
                ri " Hmmmhmm, what a great plan... "
                ri " Thank you for giving me this idea, [name]! "
                " ...You're not exactly sure on how to feel about this. "
                " But, you just gave her a thumbs up as a response. "
                " Atleast she's happy and not mad? "
                " If she was mad, she'd probably throw all of the chairs in the school down the building. "
                " Yeah, that's most likely to happen if she was mad... "
                " Just judging by how she acts though. "
                scene black with dissolve
                " You spent the rest of the break talking with Riley. "
                " More like listening to her with her ideas... "
                " Her ideas aren't really mad, it's just that all of them are Oliver related. "
                " You're lowkey starting to get tired about the whole Oliver thing going on with her... "
                " But you've gotta pretend that you're actually listening. "
                " Otherwise, you might be thrown off of the building. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassfri
    label libraryfri1:
        # ruby and lana
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked to the library and found two of your classmates talking to eachother. "
        " Wondering what they're talking about, you walked over to them. "
        show rubyneutral at right with easeinleft
        show lananeutral at left with easeinleft
        if rubyknow == True and lanaknow == True:
            ru " Oooh, [name]'s here! "
            ru " Hi there, [name]! "
            l " Hi, [name]!! "
            l " Me and Ruby were just talking about my sock puppet show! "
            l " You know...Juliana and Pedro? "
            l " I've been thinking a whole lot about it's ending... "
            l " But I just can't figure out how it's ending should go! "
            ru " Yeah, and I've been struggling a bit, too... "
            ru " Most of my ending ideas kind of have plot holes. "
            l " Yeah...so we've been trying to think really hard! "
            l " I don't want to think too hard about it, at the same time though... "
            l " Because if I think too much, then I might lose interest in making the ending! "
            hide rubyneutral at bottom
            show rubysad at right
            ru " Yeah...don't want that to happen! "
            ru " How about we talk about something else instead? "
            ru " Something that isn't about your show? "
            ru " To, you know...distract yourself? "
            hide rubysad at bottom
            show rubyneutral at right
            l " Mmm...yeah, that sounds like a good idea! "
            l " What do we talk about though...? "
            ru " Hm... "
            hide rubyneutral at bottom
            show rubyhappy at right
            ru " Oh! have you heard of this one song? "
            ru " I really like it! "
            ru " It's called: loving machine! "
            ru " It's about a machine that slowly learns to love! "
            hide lananeutral at bottom
            show lanahappy at left
            l " Ohh, you know that one? "
            l " I actually really like that song! "
            l " It's so catchy! and honestly.. "
            l " The song fits you! "
            ru " Whaaat, really? "
            l " Yeah, I mean...you're a machine! "
            l " And you're also really loveable! "
            l " The song is literally about all that! "
            ru " Aww, Lana! "
            ru " I'm flattered that you would say that! "
            ru " Infact, I'm even more flattered because... "
            ru " ...It's actually my favorite song. "
            l " Aw, shoot - really? "
            l " Does this mean that I get bonus points? "
            ru " Haha - I guess so! "
            ru " Bonus points for being cool! "
            l " Aww yeah, cool points! "
            l " But let's be real, you're way cooler than me. "
            ru " Guh - stop it with the complimentsss... "
            ru " I think I'm going to start overheating! "
            l " Hehehe! "
            scene black with dissolve
            " You spent the rest of the break talking with Ruby and Lana. "
            " It felt nice talking to them calmly like this... "
            " You need to relax more often with your homies like this. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump languageclassfri
        elif rubyknow == True and lanaknow == False:
            ru " Oooh, [name]'s here! "
            ru " Hi there, [name]! "
            x " Hi, [name]!! "
            x " I don't think we've met before, hold on... "
            $ lanaknow = True
            l " I'm Lana! Really nice to meet you! "
            l " Me and Ruby were just talking about my sock puppet show! "
            l " You know...Juliana and Pedro? "
            l " I've been thinking a whole lot about it's ending... "
            l " But I just can't figure out how it's ending should go! "
            ru " Yeah, and I've been struggling a bit, too... "
            ru " Most of my ending ideas kind of have plot holes. "
            l " Yeah...so we've been trying to think really hard! "
            l " I don't want to think too hard about it, at the same time though... "
            l " Because if I think too much, then I might lose interest in making the ending! "
            hide rubyneutral at bottom
            show rubysad at right
            ru " Yeah...don't want that to happen! "
            ru " How about we talk about something else instead? "
            ru " Something that isn't about your show? "
            ru " To, you know...distract yourself? "
            hide rubysad at bottom
            show rubyneutral at right
            l " Mmm...yeah, that sounds like a good idea! "
            l " What do we talk about though...? "
            ru " Hm... "
            hide rubyneutral at bottom
            show rubyhappy at right
            ru " Oh! have you heard of this one song? "
            ru " I really like it! "
            ru " It's called: loving machine! "
            ru " It's about a machine that slowly learns to love! "
            hide lananeutral at bottom
            show lanahappy at left
            l " Ohh, you know that one? "
            l " I actually really like that song! "
            l " It's so catchy! and honestly.. "
            l " The song fits you! "
            ru " Whaaat, really? "
            l " Yeah, I mean...you're a machine! "
            l " And you're also really loveable! "
            l " The song is literally about all that! "
            ru " Aww, Lana! "
            ru " I'm flattered that you would say that! "
            ru " Infact, I'm even more flattered because... "
            ru " ...It's actually my favorite song. "
            l " Aw, shoot - really? "
            l " Does this mean that I get bonus points? "
            ru " Haha - I guess so! "
            ru " Bonus points for being cool! "
            l " Aww yeah, cool points! "
            l " But let's be real, you're way cooler than me. "
            ru " Guh - stop it with the complimentsss... "
            ru " I think I'm going to start overheating! "
            l " Hehehe! "
            scene black with dissolve
            " You spent the rest of the break talking with Ruby and Lana. "
            " It felt nice talking to them calmly like this... "
            " You need to relax more often with your homies like this. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump languageclassfri
        elif rubyknow == False and lanaknow == True:
            x " Oooh, [name]'s here! "
            x " Hi there, [name]! "
            l " Hi, [name]!! "
            $ rubyknow = True
            l " Me and Ruby were just talking about my sock puppet show! "
            l " You know...Juliana and Pedro? "
            l " I've been thinking a whole lot about it's ending... "
            l " But I just can't figure out how it's ending should go! "
            ru " Yeah, and I've been struggling a bit, too... "
            ru " Most of my ending ideas kind of have plot holes. "
            l " Yeah...so we've been trying to think really hard! "
            l " I don't want to think too hard about it, at the same time though... "
            l " Because if I think too much, then I might lose interest in making the ending! "
            hide rubyneutral at bottom
            show rubysad at right
            ru " Yeah...don't want that to happen! "
            ru " How about we talk about something else instead? "
            ru " Something that isn't about your show? "
            ru " To, you know...distract yourself? "
            hide rubysad at bottom
            show rubyneutral at right
            l " Mmm...yeah, that sounds like a good idea! "
            l " What do we talk about though...? "
            ru " Hm... "
            hide rubyneutral at bottom
            show rubyhappy at right
            ru " Oh! have you heard of this one song? "
            ru " I really like it! "
            ru " It's called: loving machine! "
            ru " It's about a machine that slowly learns to love! "
            hide lananeutral at bottom
            show lanahappy at left
            l " Ohh, you know that one? "
            l " I actually really like that song! "
            l " It's so catchy! and honestly.. "
            l " The song fits you! "
            ru " Whaaat, really? "
            l " Yeah, I mean...you're a machine! "
            l " And you're also really loveable! "
            l " The song is literally about all that! "
            ru " Aww, Lana! "
            ru " I'm flattered that you would say that! "
            ru " Infact, I'm even more flattered because... "
            ru " ...It's actually my favorite song. "
            l " Aw, shoot - really? "
            l " Does this mean that I get bonus points? "
            ru " Haha - I guess so! "
            ru " Bonus points for being cool! "
            l " Aww yeah, cool points! "
            l " But let's be real, you're way cooler than me. "
            ru " Guh - stop it with the complimentsss... "
            ru " I think I'm going to start overheating! "
            l " Hehehe! "
            scene black with dissolve
            " You spent the rest of the break talking with Ruby and Lana. "
            " It felt nice talking to them calmly like this... "
            " You need to relax more often with your homies like this. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump languageclassfri
        else:
            x " Oooh, [name]'s here! "
            x " Hi there, [name]! "
            x " Hi, [name]!! "
            x " I don't think we've met before, hold on... "
            $ lanaknow = True
            l " I'm Lana! Really nice to meet you! "
            $ rubyknow = True
            l " Me and Ruby were just talking about my sock puppet show! "
            l " You know...Juliana and Pedro? "
            l " I've been thinking a whole lot about it's ending... "
            l " But I just can't figure out how it's ending should go! "
            ru " Yeah, and I've been struggling a bit, too... "
            ru " Most of my ending ideas kind of have plot holes. "
            l " Yeah...so we've been trying to think really hard! "
            l " I don't want to think too hard about it, at the same time though... "
            l " Because if I think too much, then I might lose interest in making the ending! "
            hide rubyneutral at bottom
            show rubysad at right
            ru " Yeah...don't want that to happen! "
            ru " How about we talk about something else instead? "
            ru " Something that isn't about your show? "
            ru " To, you know...distract yourself? "
            hide rubysad at bottom
            show rubyneutral at right
            l " Mmm...yeah, that sounds like a good idea! "
            l " What do we talk about though...? "
            ru " Hm... "
            hide rubyneutral at bottom
            show rubyhappy at right
            ru " Oh! have you heard of this one song? "
            ru " I really like it! "
            ru " It's called: loving machine! "
            ru " It's about a machine that slowly learns to love! "
            hide lananeutral at bottom
            show lanahappy at left
            l " Ohh, you know that one? "
            l " I actually really like that song! "
            l " It's so catchy! and honestly.. "
            l " The song fits you! "
            ru " Whaaat, really? "
            l " Yeah, I mean...you're a machine! "
            l " And you're also really loveable! "
            l " The song is literally about all that! "
            ru " Aww, Lana! "
            ru " I'm flattered that you would say that! "
            ru " Infact, I'm even more flattered because... "
            ru " ...It's actually my favorite song. "
            l " Aw, shoot - really? "
            l " Does this mean that I get bonus points? "
            ru " Haha - I guess so! "
            ru " Bonus points for being cool! "
            l " Aww yeah, cool points! "
            l " But let's be real, you're way cooler than me. "
            ru " Guh - stop it with the complimentsss... "
            ru " I think I'm going to start overheating! "
            l " Hehehe! "
            scene black with dissolve
            " You spent the rest of the break talking with Ruby and Lana. "
            " It felt nice talking to them calmly like this... "
            " You need to relax more often with your homies like this. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump languageclassfri
    label oligangfri1:
        scene black with dissolve
        pause 2.0
        scene oligangclub with dissolve
        " You walked into the room and saw Zip and Oliver doing something... "
        " Wondering what they're doing, you decided to walk over to them. "
        show oliverneutral at left with easeinright
        show zipneutral at right with easeinright
        o " Hey there, idiot. "
        z " Hi [name]. "
        o " Wow, lame. You don't got any insults for [them]? "
        z " Of course I do! "
        z " It's just the fact that [they] [are] really cool to the point I gotta use [their] actual name. "
        o " Well, look at you, dumbass! "
        o " And I'm talking about you, [name]. "
        o " You've already gained the approval of Zip! pretty impressive. "
        o " You're starting to really warm up to us, even though we've only known you for a bit. "
        z " Yeah - guess you're THAT good at making friends. "
        hide oliverneutral at bottom
        show oliversilly at left
        o " Pretty impressive, but can you swallow down 5 bars of soap? "
        z " ...Oliver, we're not doing this. "
        o " Come on, I want [them] to try and beat my record! "
        o " It would be fun, since soap just tastes so good! "
        o " Especially the pink ones. "
        hide zipneutral at bottom
        show zipangry at right
        z " We're not doing this, Oliver. "
        z " You know [they] can't eat soap like you. "
        o " I know [they] can! "
        o " [they] just have to try really hard! "
        z " Oliver... "
        o " What? "
        scene black with dissolve
        " You spent the rest of the break talking with Oliver and Zip. "
        " Now that Oliver's mentioned it... "
        " You lowkey want to try eating soap. "
        " You went to your classroom before Oliver could shove soap down your throat though. "
        pause 2.0
        jump languageclassfri

label languageclassfri:
    scene classroom with dissolve
    " You walked into the classroom and waited for the teacher to arrive. "
    " You didn't have to wait much though, since right after you sat down, the teacher had arrived. "
    " Wow, some good timing - am I right? "
    " Not really good timing if you wanted some more free time. "
    " Too bad you walked in a little bit too late for that. "
    " Oh well, time for some note taking. "
    show msthravelneutral at center with easeinright
    mst " Good morning, class! "
    mst " Woo, it's the final day until the weekend! "
    mst " I'm sure you're all excited, buuut... "
    mst " Remember - you've gotta go through school before you rest! "
    mst " Don't worry, I'm not letting you guys suffer for now. "
    mst " In fact, we're just going to be taking notes for today! "
    mst " Woo, all of you must be SO happy. "
    mst " Well, I'm happy too since I get to have a break from you all. "
    mst " Not a break from my job, of course. "
    mst " Now - get your notebooks and pens before I go on another rambling session. "
    mst " You all better pay attention to the slides. "
    mst " Don't blame me if you get low grades for having no notes to study! "
    scene black with dissolve
    " You spent the rest of this class taking down notes. "
    " ...You're kind of having the feeling that you're going to be taking down notes for every single class. "
    " But hey, atleast you don't have much to do, right? "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for another break. "
    " You got up from your seat and you went out to the hallways. "
    pause 2.0
    jump fribreak2

label fribreak2:
    scene hallway with dissolve
    if oligangjoin == True:
        jump oligangfri2
    else:
        pass
    " Where are you gonna hang out for this break? "
    menu:
        " {image=claireicon} The front of the school {image=cubbieicon} ":
            jump frontschoolfri2
        " {image=kevinicon} The back of the school {image=lanaicon} ":
            jump backschoolfri2
        " {image=rileyicon} The gym {image=engelicon} ":
            jump gymfri2
        " {image=abbieicon} The cafeteria {image=robbyicon} ":
            jump cafeteriafri2
        " {image=popularicon} The rooftop {image=rubyicon} ":
            jump rooftopfri2
        " {image=bubbleicon} The library {image=skellicon} ":
            jump libraryfri2
    label frontschoolfri2:
        # claire and cubbie
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked to the front of the school and spotted two of your classmates talking with eachother. "
        " Wondering what they're talking about, you decided to join their conversation."
        show claireneutral at left with easeinright
        show cubbieneutral at right with easeinright
        if claireknow == True and cubbieknow == True:
            cb " ...! "
            " The cat guy points over to you, getting the girl's attention. "
            " Huh, well this guy noticed you pretty fast. "
            c " Huh? there's someone here...? "
            c " Oh! [name]!! "
            c " Sorry that I didn't notice you earlier, hehe... "
            c " Me and Cubbie were just talking about some stuff! "
            cb " ... "
            c " Huh, what was that, Cubbie? "
            cb " ...!! "
            c " You want to hangout with us sometime? "
            cb " !! "
            c " Oh, Cubbie!! we would love to!! "
            c " Maybe sometime when we're not busy though. "
            c " Perhaps on sunday? I'm not busy that time! "
            " Hanging out on a sunday sounds good... "
            " You also need to socialize a whole lot more. "
            " You're gonna be hanging out with them. "
            " Too bad there's no Sunday in this game... "
            " I've probably said that a million times now, but I've gotta keep reminding you! "
            c " [name]'s free on sunday, too... "
            c " Alright! we can hang out on a sunday! "
            hide cubbieneutral at bottom
            show cubbiehappy at right
            cb " !! "
            " Cubbie seems delighted to hear that you're all going to be hanging out. "
            " Maybe you could get a few drinks while you're hanging out... "
            " You've gotta get them some drinks too while you're getting some. "
            " Always have to share with the homies. "
            c " Just praying that my parents won't let me do anything stupid... "
            c " If we can't be able to meet up on sunday... "
            c " Maybe we can just move that to next week saturday? "
            c " I'm sure I'm free that time! "
            hide cubbiehappy at bottom
            show cubbieneutral at right
            cb " ... "
            " Cubbie does a nod in approval. "
            hide claireneutral at bottom
            show clairehappy at left
            c " Hehe...spending time with you guys is going to be fun, I know it! "
            c " We could go and watch a movie... "
            c " Or we could just get some food and talk! "
            " Damn, both of those sound pretty good. "
            " But you're more into the food thing. "
            " Looks like Cubbie agrees on the food thing, too. "
            c " You guys want food? alright! "
            c " We can go to that good food place that's not too far from here! "
            c " Trust me, the food there is absolutely delicious. "
            c " I've been there before! "
            cb " ... "
            " Cubbie seems familiar with the place... "
            " You haven't went to it before though. "
            " You're just going to have to see if Claire was right. "
            " Even though we don't got a sunday. Or a next week. "
            " Not yet. Maybe. I'm not sure. "
            scene black with dissolve
            " You spent the rest of the break talking with Claire and Cubbie. "
            " Talking about the stuff you're going to do on sunday... "
            " You really needed to step out of your room and hangout with people. "
            " That's why I'm making you do this. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked back into the school and went to your classroom after a bit. "
            pause 2.0
            jump scienceclassfri
        elif claireknow == True and cubbieknow == False:
            x " ...! "
            " The cat guy points over to you, getting the girl's attention. "
            " Huh, well this guy noticed you pretty fast. "
            c " Huh? there's someone here...? "
            c " Oh! [name]!! "
            c " Sorry that I didn't notice you earlier, hehe... "
            $ cubbieknow = True
            c " Me and Cubbie were just talking about some stuff! "
            cb " ... "
            c " Huh, what was that, Cubbie? "
            cb " ...!! "
            c " You want to hangout with us sometime? "
            cb " !! "
            c " Oh, Cubbie!! we would love to!! "
            c " Maybe sometime when we're not busy though. "
            c " Perhaps on sunday? I'm not busy that time! "
            " Hanging out on a sunday sounds good... "
            " You also need to socialize a whole lot more. "
            " You're gonna be hanging out with them. "
            " Too bad there's no Sunday in this game... "
            " I've probably said that a million times now, but I've gotta keep reminding you! "
            c " [name]'s free on sunday, too... "
            c " Alright! we can hang out on a sunday! "
            hide cubbieneutral at bottom
            show cubbiehappy at right
            cb " !! "
            " Cubbie seems delighted to hear that you're all going to be hanging out. "
            " Maybe you could get a few drinks while you're hanging out... "
            " You've gotta get them some drinks too while you're getting some. "
            " Always have to share with the homies. "
            c " Just praying that my parents won't let me do anything stupid... "
            c " If we can't be able to meet up on sunday... "
            c " Maybe we can just move that to next week saturday? "
            c " I'm sure I'm free that time! "
            hide cubbiehappy at bottom
            show cubbieneutral at right
            cb " ... "
            " Cubbie does a nod in approval. "
            hide claireneutral at bottom
            show clairehappy at left
            c " Hehe...spending time with you guys is going to be fun, I know it! "
            c " We could go and watch a movie... "
            c " Or we could just get some food and talk! "
            " Damn, both of those sound pretty good. "
            " But you're more into the food thing. "
            " Looks like Cubbie agrees on the food thing, too. "
            c " You guys want food? alright! "
            c " We can go to that good food place that's not too far from here! "
            c " Trust me, the food there is absolutely delicious. "
            c " I've been there before! "
            cb " ... "
            " Cubbie seems familiar with the place... "
            " You haven't went to it before though. "
            " You're just going to have to see if Claire was right. "
            " Even though we don't got a sunday. Or a next week. "
            " Not yet. Maybe. I'm not sure. "
            scene black with dissolve
            " You spent the rest of the break talking with Claire and Cubbie. "
            " Talking about the stuff you're going to do on sunday... "
            " You really needed to step out of your room and hangout with people. "
            " That's why I'm making you do this. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked back into the school and went to your classroom after a bit. "
            pause 2.0
            jump scienceclassfri
        elif claireknow == False and cubbieknow == True:
            cb " ...! "
            " The cat guy points over to you, getting the girl's attention. "
            " Huh, well this guy noticed you pretty fast. "
            x " Huh? there's someone here...? "
            x " Oh! [name]!! "
            x " Sorry that I didn't notice you earlier, hehe... "
            x " I don't think I've introduced myself to you before! "
            $ claireknow = True
            c " I'm Claire - and I'm one of your classmates! nice to meet you! "
            c " Anyway... me and Cubbie were just talking about some stuff! "
            cb " ... "
            c " Huh, what was that, Cubbie? "
            cb " ...!! "
            c " You want to hangout with us sometime? "
            cb " !! "
            c " Oh, Cubbie!! we would love to!! "
            c " Maybe sometime when we're not busy though. "
            c " Perhaps on sunday? I'm not busy that time! "
            " Hanging out on a sunday sounds good... "
            " You also need to socialize a whole lot more. "
            " You're gonna be hanging out with them. "
            " Too bad there's no Sunday in this game... "
            " I've probably said that a million times now, but I've gotta keep reminding you! "
            c " [name]'s free on sunday, too... "
            c " Alright! we can hang out on a sunday! "
            hide cubbieneutral at bottom
            show cubbiehappy at right
            cb " !! "
            " Cubbie seems delighted to hear that you're all going to be hanging out. "
            " Maybe you could get a few drinks while you're hanging out... "
            " You've gotta get them some drinks too while you're getting some. "
            " Always have to share with the homies. "
            c " Just praying that my parents won't let me do anything stupid... "
            c " If we can't be able to meet up on sunday... "
            c " Maybe we can just move that to next week saturday? "
            c " I'm sure I'm free that time! "
            hide cubbiehappy at bottom
            show cubbieneutral at right
            cb " ... "
            " Cubbie does a nod in approval. "
            hide claireneutral at bottom
            show clairehappy at left
            c " Hehe...spending time with you guys is going to be fun, I know it! "
            c " We could go and watch a movie... "
            c " Or we could just get some food and talk! "
            " Damn, both of those sound pretty good. "
            " But you're more into the food thing. "
            " Looks like Cubbie agrees on the food thing, too. "
            c " You guys want food? alright! "
            c " We can go to that good food place that's not too far from here! "
            c " Trust me, the food there is absolutely delicious. "
            c " I've been there before! "
            cb " ... "
            " Cubbie seems familiar with the place... "
            " You haven't went to it before though. "
            " You're just going to have to see if Claire was right. "
            " Even though we don't got a sunday. Or a next week. "
            " Not yet. Maybe. I'm not sure. "
            scene black with dissolve
            " You spent the rest of the break talking with Claire and Cubbie. "
            " Talking about the stuff you're going to do on sunday... "
            " You really needed to step out of your room and hangout with people. "
            " That's why I'm making you do this. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked back into the school and went to your classroom after a bit. "
            pause 2.0
            jump scienceclassfri
        else:
            x " ...! "
            " The cat guy points over to you, getting the girl's attention. "
            " Huh, well this guy noticed you pretty fast. "
            x " Huh? there's someone here...? "
            x " Oh! [name]!! "
            x " Sorry that I didn't notice you earlier, hehe... "
            x " I don't think I've introduced myself to you before! "
            $ claireknow = True
            c " I'm Claire - and I'm one of your classmates! nice to meet you! "
            $ cubbieknow = True
            c " Anyway... me and Cubbie were just talking about some stuff! "
            cb " ... "
            c " Huh, what was that, Cubbie? "
            cb " ...!! "
            c " You want to hangout with us sometime? "
            cb " !! "
            c " Oh, Cubbie!! we would love to!! "
            c " Maybe sometime when we're not busy though. "
            c " Perhaps on sunday? I'm not busy that time! "
            " Hanging out on a sunday sounds good... "
            " You also need to socialize a whole lot more. "
            " You're gonna be hanging out with them. "
            " Too bad there's no Sunday in this game... "
            " I've probably said that a million times now, but I've gotta keep reminding you! "
            c " [name]'s free on sunday, too... "
            c " Alright! we can hang out on a sunday! "
            hide cubbieneutral at bottom
            show cubbiehappy at right
            cb " !! "
            " Cubbie seems delighted to hear that you're all going to be hanging out. "
            " Maybe you could get a few drinks while you're hanging out... "
            " You've gotta get them some drinks too while you're getting some. "
            " Always have to share with the homies. "
            c " Just praying that my parents won't let me do anything stupid... "
            c " If we can't be able to meet up on sunday... "
            c " Maybe we can just move that to next week saturday? "
            c " I'm sure I'm free that time! "
            hide cubbiehappy at bottom
            show cubbieneutral at right
            cb " ... "
            " Cubbie does a nod in approval. "
            hide claireneutral at bottom
            show clairehappy at left
            c " Hehe...spending time with you guys is going to be fun, I know it! "
            c " We could go and watch a movie... "
            c " Or we could just get some food and talk! "
            " Damn, both of those sound pretty good. "
            " But you're more into the food thing. "
            " Looks like Cubbie agrees on the food thing, too. "
            c " You guys want food? alright! "
            c " We can go to that good food place that's not too far from here! "
            c " Trust me, the food there is absolutely delicious. "
            c " I've been there before! "
            cb " ... "
            " Cubbie seems familiar with the place... "
            " You haven't went to it before though. "
            " You're just going to have to see if Claire was right. "
            " Even though we don't got a sunday. Or a next week. "
            " Not yet. Maybe. I'm not sure. "
            scene black with dissolve
            " You spent the rest of the break talking with Claire and Cubbie. "
            " Talking about the stuff you're going to do on sunday... "
            " You really needed to step out of your room and hangout with people. "
            " That's why I'm making you do this. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You walked back into the school and went to your classroom after a bit. "
            pause 2.0
            jump scienceclassfri
    label backschoolfri2:
        # kevin and lana
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of your school and spotted two of your classmates doing their own things. "
        " Who would you like to talk to? "
        if kevinknow == True and lanaknow == True:
            menu:
                " {image=kevinicon} Kevin {image=kevinicon} ":
                    jump twoxeight
                " {image=lanaicon} Lana {image=lanaicon} ":
                    jump twoxone
        elif kevinknow == True and lanaknow == False:
            menu:
                " {image=kevinicon} Kevin {image=kevinicon} ":
                    jump twoxeight
                " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                    jump twoxone
        elif kevinknow == False and lanaknow == True:
            menu:
                " {image=kevinicon} A nerd {image=kevinicon} ":
                    jump twoxeight
                " {image=lanaicon} Lana {image=lanaicon} ":
                    jump twoxone
        else:
            menu:
                " {image=kevinicon} A nerd {image=kevinicon} ":
                    jump twoxeight
                " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                    jump twoxone
        label twoxeight:
            show kevinneutral at center with easeinright
            if kevinknow == True:
                " You walked over to him and asked him what he was doing. "
                kv " Greetings, [name]. "
                kv " I have been thinking for awhile now... "
                kv " I remember that I had this one quiz where I had gotten a 49/50. "
                kv " A near perfect score! "
                kv " That would be impressive to some, but for me? "
                kv " I want that to be an actual perfect score instead of being one point away. "
                kv " It means that I had one mistake - even though I'm sure that I studied everything correctly! "
                kv " What should I do to prevent this from happening in the future? "
                hide kevinneutral at bottom
                show kevinangry at center
                kv " I should probably, most likely study even more! "
                kv " I don't want to be a constant failure, after all! "
                kv " Ghhh...it just really pisses me off. "
                kv " Pisses me off that I was one point away from being perfect. "
                kv " I wanted to retake the quiz, but I know I can't. "
                kv " All I can do is just try better on the next one. "
                kv " And I know I'll do better! "
                kv " I've been studying a whole lot more lately! "
                kv " And I'm talking a WHOLE LOT. "
                kv " I study more than a discord moderator is online in their server! "
                kv " ...Erh, I studied a lot - if you don't know what that means. "
                hide kevinangry at bottom
                show kevinneutral at center
                kv " I'm sure I won't fail this time. "
                kv " I've gotta make sure of that. "
                kv " There's no way I can fail anyway - "
                kv " I've studied so much... "
                kv " I'm going to be flabbergasted if I get a low score after that. "
                kv " Not as much surprised if I get one point away again. "
                kv " Sigh... "
                kv " I should study even more next break. "
                kv " I don't want to get one point away again. "
                kv " I need to get myself and my grades higher... "
                " You told him that he didn't have to get his grades higher like that. "
                " Infact, they're already high enough as they should be. "
                " He doesn't have to keep trying his best everytime. "
                " You've gotta rest some time, too. "
                kv " ...I know that. "
                kv " I can just try to balance resting and studying at the same time. "
                kv " I'm sure I can do that... "
                kv " Can't just relax all the time, you know. "
                kv " Gotta get certain stuff done first. "
                kv " Like school. "
                kv " You've always gotta put school first before anything else. "
                kv " ...And friends and family, too. "
                " You tell him that he's forgetting something there. "
                kv " ...Sigh. "
                kv " ...You've also got to put yourself first, out of all of those. "
                kv " Putting yourself first matters more than anything. "
                kv " And that means...not pushing myself to my limits. "
                kv " Because that would be unhealthy. "
                kv " There, you happy? "
                " You gave him the thumbs up of approval. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin. "
                " A little concerning that he wants to study so much... "
                " I mean, it's okay if you study - just don't overdo it to the point you're tired. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump scienceclassfri
            else:
                " You walked over to him and asked him what he was doing. "
                x " Greetings, [name]. "
                x " I don't believe I've introduced myself to you before... "
                $ kevinknow = True
                kv " I'm Kevin, one of your classmates. "
                kv " I have been thinking for awhile now... "
                kv " I remember that I had this one quiz where I had gotten a 49/50. "
                kv " A near perfect score! "
                kv " That would be impressive to some, but for me? "
                kv " I want that to be an actual perfect score instead of being one point away. "
                kv " It means that I had one mistake - even though I'm sure that I studied everything correctly! "
                kv " What should I do to prevent this from happening in the future? "
                hide kevinneutral at bottom
                show kevinangry at center
                kv " I should probably, most likely study even more! "
                kv " I don't want to be a constant failure, after all! "
                kv " Ghhh...it just really pisses me off. "
                kv " Pisses me off that I was one point away from being perfect. "
                kv " I wanted to retake the quiz, but I know I can't. "
                kv " All I can do is just try better on the next one. "
                kv " And I know I'll do better! "
                kv " I've been studying a whole lot more lately! "
                kv " And I'm talking a WHOLE LOT. "
                kv " I study more than a discord moderator is online in their server! "
                kv " ...Erh, I studied a lot - if you don't know what that means. "
                hide kevinangry at bottom
                show kevinneutral at center
                kv " I'm sure I won't fail this time. "
                kv " I've gotta make sure of that. "
                kv " There's no way I can fail anyway - "
                kv " I've studied so much... "
                kv " I'm going to be flabbergasted if I get a low score after that. "
                kv " Not as much surprised if I get one point away again. "
                kv " Sigh... "
                kv " I should study even more next break. "
                kv " I don't want to get one point away again. "
                kv " I need to get myself and my grades higher... "
                " You told him that he didn't have to get his grades higher like that. "
                " Infact, they're already high enough as they should be. "
                " He doesn't have to keep trying his best everytime. "
                " You've gotta rest some time, too. "
                kv " ...I know that. "
                kv " I can just try to balance resting and studying at the same time. "
                kv " I'm sure I can do that... "
                kv " Can't just relax all the time, you know. "
                kv " Gotta get certain stuff done first. "
                kv " Like school. "
                kv " You've always gotta put school first before anything else. "
                kv " ...And friends and family, too. "
                " You tell him that he's forgetting something there. "
                kv " ...Sigh. "
                kv " ...You've also got to put yourself first, out of all of those. "
                kv " Putting yourself first matters more than anything. "
                kv " And that means...not pushing myself to my limits. "
                kv " Because that would be unhealthy. "
                kv " There, you happy? "
                " You gave him the thumbs up of approval. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin. "
                " A little concerning that he wants to study so much... "
                " I mean, it's okay if you study - just don't overdo it to the point you're tired. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump scienceclassfri
        label twoxone:
            show lananeutral at center with easeinleft
            if lanaknow == True:
                " You walked over to her and asked her what she was doing. "
                l " Hm? hey there, [name]!! "
                l " I was just thinkin' about you, actually! "
                l " I needed your help on something... "
                l " You see this little stage over here? "
                " She pulls out a box that looks like a stage. "
                " It looked pretty basic, but also nice to look at. "
                " Looks like a stage that you would use for a school project, actually. "
                l " This is the stage I'd usually use for my shows! "
                l " But, recently...I've been thinking, "
                l " I should give it a redesign! "
                l " It looks a little too basic, you know? "
                l " I mean, I know being basic sometimes is good, but... "
                l " You can't ALWAYS be basic! "
                l " That's why I want to remake its design as a whole! "
                l " And I need your help in making that happen! "
                l " I just need you to help make my idea come true! "
                l " You see, I want to make the stage look more decorated... "
                l " And I also want to make a feature where I can just change the scenes more easily... "
                l " And I also want some stuff like little decorations on the stage to change depending on which show I'm doing! "
                l " Don't know how to do that one, but we can make it work, right? "
                l " And don't worry about the materials for this and stuff - "
                l " I've got it all covered in this bad over here! "
                " Lana pulls out a bag filled with all of the materials you guys needed. "
                " Fabrics, cardboard, glue... you name it. "
                " A whole lot of things needed for the redesign. "
                l " See? told you I've got everything! "
                l " We're not gonna have any problems with the materials at all! "
                l " ...That is, if we don't mess up too much. "
                l " I can just get some other stuff on the way home if we mess up a lot, don't worry! "
                l " So, I want you to be the one making the curtains... "
                l " Oh, and also the little decorations! "
                l " I'll be the one to do the whole stage! "
                l " Hehe, I don't want you to suffer too much while making this. "
                l " I'm making the stage more detailed while doing this, too! "
                l " Like...wayy more detailed. "
                l " More detailed than you expect! "
                l " If you need anything or have questions to ask me - just say, okay? "
                l " I'm going to be a little bit locked into this though, so... "
                l " You might need to tap me a few times to get my attention. "
                scene black with dissolve
                " You spent the rest of the break talking and making stuff with Lana. "
                " Just making the curtains and decorations for her... "
                " In the end, the stuff you made didn't look too bad. It actually looked pretty good. "
                " Nice one, you actually made something cool for someone. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump scienceclassfri
            else:
                " You walked over to her and asked her what she was doing. "
                x " Hm? hey there, [name]!! "
                $ lanaknow = True
                l " I'm Lana - and... "
                l " I was just thinkin' about you, actually! "
                l " I needed your help on something... "
                l " You see this little stage over here? "
                " She pulls out a box that looks like a stage. "
                " It looked pretty basic, but also nice to look at. "
                " Looks like a stage that you would use for a school project, actually. "
                l " This is the stage I'd usually use for my shows! "
                l " But, recently...I've been thinking, "
                l " I should give it a redesign! "
                l " It looks a little too basic, you know? "
                l " I mean, I know being basic sometimes is good, but... "
                l " You can't ALWAYS be basic! "
                l " That's why I want to remake its design as a whole! "
                l " And I need your help in making that happen! "
                l " I just need you to help make my idea come true! "
                l " You see, I want to make the stage look more decorated... "
                l " And I also want to make a feature where I can just change the scenes more easily... "
                l " And I also want some stuff like little decorations on the stage to change depending on which show I'm doing! "
                l " Don't know how to do that one, but we can make it work, right? "
                l " And don't worry about the materials for this and stuff - "
                l " I've got it all covered in this bad over here! "
                " Lana pulls out a bag filled with all of the materials you guys needed. "
                " Fabrics, cardboard, glue... you name it. "
                " A whole lot of things needed for the redesign. "
                l " See? told you I've got everything! "
                l " We're not gonna have any problems with the materials at all! "
                l " ...That is, if we don't mess up too much. "
                l " I can just get some other stuff on the way home if we mess up a lot, don't worry! "
                l " So, I want you to be the one making the curtains... "
                l " Oh, and also the little decorations! "
                l " I'll be the one to do the whole stage! "
                l " Hehe, I don't want you to suffer too much while making this. "
                l " I'm making the stage more detailed while doing this, too! "
                l " Like...wayy more detailed. "
                l " More detailed than you expect! "
                l " If you need anything or have questions to ask me - just say, okay? "
                l " I'm going to be a little bit locked into this though, so... "
                l " You might need to tap me a few times to get my attention. "
                scene black with dissolve
                " You spent the rest of the break talking and making stuff with Lana. "
                " Just making the curtains and decorations for her... "
                " In the end, the stuff you made didn't look too bad. It actually looked pretty good. "
                " Nice one, you actually made something cool for someone. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump scienceclassfri
    label gymfri2:
        # riley and engel
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked into the gym and found two of your classmates talking with eachother. "
        " Wondering what they're talking about, you decided to walk over to them. "
        show rileyneutral at left with easeinright
        show engelneutral at right with easeinright
        if rileyknow == True and engelknow == True:
            ri " Engeeell!! "
            e " Oh boy. "
            ri " You're smart, riiiight? "
            e " ...You could say that I am. "
            e " Did you need help with school work? "
            e " Or just had a question about our class earlier? "
            e " (God, hope this conversation won't be too cringe worthy for [name]...) "
            e " (I can't really talk to [them] with Riley being near me.) "
            e " (Keep everything together, Engel...) "
            e " (You have to be nice and polite with her.) "
            ri " Mmmm...actually, no! "
            ri " I have another question for you! "
            ri " A question not relating to school! "
            e " Uh... "
            e " ...Well then, go ahead and ask me your question. "
            e " I don't know if I can answer it, but I can try. "
            ri " Hehe, thankssss Engel!! "
            ri " You know, you're always the besstttt... "
            ri " Since you're smart and all that! "
            ri " But my Oliver is better. "
            e " ...Uh huh. "
            ri " Anyway! back onto my question... "
            ri " Do you think that Oliver would like it if I give him more gifts? "
            ri " And I want you to be completely honest with me! "
            ri " No sweet lies or whatever. "
            e " ...Surprising that you'd want me to be honest... "
            e " But, if you wish for me to be honest, then I'll give you just that. "
            e " Just don't get too mad for me being too honest with you. "
            e " You asked for honesty, so I'll give you honesty. "
            ri " Okay!! "
            ri " I'll try not to get TOO mad! "
            ri " I did ask for this, after all... "
            e " Okay, here we go... "
            e " In my opinion, I don't think Oliver would want more gifts from you. "
            e " Before you ask me why, I'll explain to you. "
            e " Have you ever noticed that he would throw your gifts away after a few minutes? "
            e " He would inspect it for a bit... "
            e " And then he would throw it away. "
            e " Most likely making fun of you for thinking that he would take in something that was made by you. "
            e " You're great, Riley. Really. "
            e " But I'm sure he thinks that you're weird and too obsessed with him. "
            e " Realistically speaking, of course... "
            e " He acts like he's fine with you, but truly? "
            e " He just wants you to get away from him. "
            e " Sorry that I had to tell you the truth like this, Riley... "
            e " But you asked me to be honest, so I gave you that. "
            ri " ...Ah. "
            ri " Thanks for being honest with me, Engel! "
            ri " I think I needed to hear that. "
            e " You're welcome. "
            ri " Also! was [name] always here? "
            e " ...You just noticed [them]?? "
            scene black with dissolve
            " You spent the rest of the break talking with Riley and Engel. "
            " Listening to that conversation was pretty interesting. "
            " But you felt like that Riley really, really needed to hear those words from Engel though. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the gym and went to your classroom. "
            pause 2.0
            jump scienceclassfri
        elif rileyknow == True and engelknow == False:
            ri " Engeeell!! "
            x " Oh boy. "
            ri " You're smart, riiiight? "
            x " ...You could say that I am. "
            x " Did you need help with school work? "
            x " Or just had a question about our class earlier? "
            x " (God, hope this conversation won't be too cringe worthy for [name]...) "
            x " (I can't really talk to [them] with Riley being near me.) "
            $ engelknow = True
            e " (Keep everything together, Engel...) "
            e " (You have to be nice and polite with her.) "
            ri " Mmmm...actually, no! "
            ri " I have another question for you! "
            ri " A question not relating to school! "
            e " Uh... "
            e " ...Well then, go ahead and ask me your question. "
            e " I don't know if I can answer it, but I can try. "
            ri " Hehe, thankssss Engel!! "
            ri " You know, you're always the besstttt... "
            ri " Since you're smart and all that! "
            ri " But my Oliver is better. "
            e " ...Uh huh. "
            ri " Anyway! back onto my question... "
            ri " Do you think that Oliver would like it if I give him more gifts? "
            ri " And I want you to be completely honest with me! "
            ri " No sweet lies or whatever. "
            e " ...Surprising that you'd want me to be honest... "
            e " But, if you wish for me to be honest, then I'll give you just that. "
            e " Just don't get too mad for me being too honest with you. "
            e " You asked for honesty, so I'll give you honesty. "
            ri " Okay!! "
            ri " I'll try not to get TOO mad! "
            ri " I did ask for this, after all... "
            e " Okay, here we go... "
            e " In my opinion, I don't think Oliver would want more gifts from you. "
            e " Before you ask me why, I'll explain to you. "
            e " Have you ever noticed that he would throw your gifts away after a few minutes? "
            e " He would inspect it for a bit... "
            e " And then he would throw it away. "
            e " Most likely making fun of you for thinking that he would take in something that was made by you. "
            e " You're great, Riley. Really. "
            e " But I'm sure he thinks that you're weird and too obsessed with him. "
            e " Realistically speaking, of course... "
            e " He acts like he's fine with you, but truly? "
            e " He just wants you to get away from him. "
            e " Sorry that I had to tell you the truth like this, Riley... "
            e " But you asked me to be honest, so I gave you that. "
            ri " ...Ah. "
            ri " Thanks for being honest with me, Engel! "
            ri " I think I needed to hear that. "
            e " You're welcome. "
            ri " Also! was [name] always here? "
            e " ...You just noticed [them]?? "
            scene black with dissolve
            " You spent the rest of the break talking with Riley and Engel. "
            " Listening to that conversation was pretty interesting. "
            " But you felt like that Riley really, really needed to hear those words from Engel though. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the gym and went to your classroom. "
            pause 2.0
            jump scienceclassfri
        elif rileyknow == False and engelknow == True:
            x " Engeeell!! "
            e " Oh boy. "
            x " You're smart, riiiight? "
            e " ...You could say that I am. "
            e " Did you need help with school work? "
            e " Or just had a question about our class earlier? "
            e " (God, hope this conversation won't be too cringe worthy for [name]...) "
            $ rileyknow = True
            e " (I can't really talk to [them] with Riley being near me.) "
            e " (Keep everything together, Engel...) "
            e " (You have to be nice and polite with her.) "
            ri " Mmmm...actually, no! "
            ri " I have another question for you! "
            ri " A question not relating to school! "
            e " Uh... "
            e " ...Well then, go ahead and ask me your question. "
            e " I don't know if I can answer it, but I can try. "
            ri " Hehe, thankssss Engel!! "
            ri " You know, you're always the besstttt... "
            ri " Since you're smart and all that! "
            ri " But my Oliver is better. "
            e " ...Uh huh. "
            ri " Anyway! back onto my question... "
            ri " Do you think that Oliver would like it if I give him more gifts? "
            ri " And I want you to be completely honest with me! "
            ri " No sweet lies or whatever. "
            e " ...Surprising that you'd want me to be honest... "
            e " But, if you wish for me to be honest, then I'll give you just that. "
            e " Just don't get too mad for me being too honest with you. "
            e " You asked for honesty, so I'll give you honesty. "
            ri " Okay!! "
            ri " I'll try not to get TOO mad! "
            ri " I did ask for this, after all... "
            e " Okay, here we go... "
            e " In my opinion, I don't think Oliver would want more gifts from you. "
            e " Before you ask me why, I'll explain to you. "
            e " Have you ever noticed that he would throw your gifts away after a few minutes? "
            e " He would inspect it for a bit... "
            e " And then he would throw it away. "
            e " Most likely making fun of you for thinking that he would take in something that was made by you. "
            e " You're great, Riley. Really. "
            e " But I'm sure he thinks that you're weird and too obsessed with him. "
            e " Realistically speaking, of course... "
            e " He acts like he's fine with you, but truly? "
            e " He just wants you to get away from him. "
            e " Sorry that I had to tell you the truth like this, Riley... "
            e " But you asked me to be honest, so I gave you that. "
            ri " ...Ah. "
            ri " Thanks for being honest with me, Engel! "
            ri " I think I needed to hear that. "
            e " You're welcome. "
            ri " Also! was [name] always here? "
            e " ...You just noticed [them]?? "
            scene black with dissolve
            " You spent the rest of the break talking with Riley and Engel. "
            " Listening to that conversation was pretty interesting. "
            " But you felt like that Riley really, really needed to hear those words from Engel though. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the gym and went to your classroom. "
            pause 2.0
            jump scienceclassfri
        else:
            x " Engeeell!! "
            x " Oh boy. "
            x " You're smart, riiiight? "
            x " ...You could say that I am. "
            x " Did you need help with school work? "
            x " Or just had a question about our class earlier? "
            x " (God, hope this conversation won't be too cringe worthy for [name]...) "
            $ rileyknow = True
            x " (I can't really talk to [them] with Riley being near me.) "
            $ engelknow = True
            e " (Keep everything together, Engel...) "
            e " (You have to be nice and polite with her.) "
            ri " Mmmm...actually, no! "
            ri " I have another question for you! "
            ri " A question not relating to school! "
            e " Uh... "
            e " ...Well then, go ahead and ask me your question. "
            e " I don't know if I can answer it, but I can try. "
            ri " Hehe, thankssss Engel!! "
            ri " You know, you're always the besstttt... "
            ri " Since you're smart and all that! "
            ri " But my Oliver is better. "
            e " ...Uh huh. "
            ri " Anyway! back onto my question... "
            ri " Do you think that Oliver would like it if I give him more gifts? "
            ri " And I want you to be completely honest with me! "
            ri " No sweet lies or whatever. "
            e " ...Surprising that you'd want me to be honest... "
            e " But, if you wish for me to be honest, then I'll give you just that. "
            e " Just don't get too mad for me being too honest with you. "
            e " You asked for honesty, so I'll give you honesty. "
            ri " Okay!! "
            ri " I'll try not to get TOO mad! "
            ri " I did ask for this, after all... "
            e " Okay, here we go... "
            e " In my opinion, I don't think Oliver would want more gifts from you. "
            e " Before you ask me why, I'll explain to you. "
            e " Have you ever noticed that he would throw your gifts away after a few minutes? "
            e " He would inspect it for a bit... "
            e " And then he would throw it away. "
            e " Most likely making fun of you for thinking that he would take in something that was made by you. "
            e " You're great, Riley. Really. "
            e " But I'm sure he thinks that you're weird and too obsessed with him. "
            e " Realistically speaking, of course... "
            e " He acts like he's fine with you, but truly? "
            e " He just wants you to get away from him. "
            e " Sorry that I had to tell you the truth like this, Riley... "
            e " But you asked me to be honest, so I gave you that. "
            ri " ...Ah. "
            ri " Thanks for being honest with me, Engel! "
            ri " I think I needed to hear that. "
            e " You're welcome. "
            ri " Also! was [name] always here? "
            e " ...You just noticed [them]?? "
            scene black with dissolve
            " You spent the rest of the break talking with Riley and Engel. "
            " Listening to that conversation was pretty interesting. "
            " But you felt like that Riley really, really needed to hear those words from Engel though. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the gym and went to your classroom. "
            pause 2.0
            jump scienceclassfri
    label cafeteriafri2:
        # abbie and robby
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked into the cafeteria and spotted two of your classmates doing their own things. "
        " You wanted to talk to one of them...but who do you talk to? "
        if abbieknow == True and robbyknow == True:
            menu:
                " {image=abbieicon} Abbie {image=abbieicon} ":
                    jump abbietheapple
                " {image=robbyicon} Robby {image=robbyicon} ":
                    jump robbytherobber
        elif abbieknow == True and robbyknow == False:
            menu:
                " {image=abbieicon} Abbie {image=abbieicon} ":
                    jump abbietheapple
                " {image=robbyicon} A guy with a silly hat {image=robbyicon} ":
                    jump robbytherobber
        elif abbieknow == False and robbyknow == True:
            menu:
                " {image=abbieicon} A shy looking guy {image=abbieicon} ":
                    jump abbietheapple
                " {image=robbyicon} Robby {image=robbyicon} ":
                    jump robbytherobber
        else:
            menu:
                " {image=abbieicon} A shy looking guy {image=abbieicon} ":
                    jump abbietheapple
                " {image=robbyicon} A guy with a silly hat {image=robbyicon} ":
                    jump robbytherobber
        label abbietheapple:
            show abbieneutral at center with easeinleft
            if abbieknow == True:
                " You walked over to him and asked him what he was doing. "
                a " Oh, um...hi [name]... "
                a " Uh...you can sit next to me... "
                a " I don't want you to just...stand there... "
                a " It would be really awkward... "
                " You sat down next to him and saw that he was eating some food. "
                " And an apple. "
                a " I decided to eat an apple today... "
                a " ...You know... "
                a " Sometimes I hear people... "
                a " Hear people talking about me an apple...or something... "
                a " They compare me to an apple... "
                a " I don't know whyyy... "
                a " ...I mean, one time... "
                a " I was just doing my stuff on my phone normally, right...? "
                a " And then I noticed that they changed my name in the classroom's GC... "
                a " They changed it to...um... "
                a " ...'Abble'...? with an apple emoji after it... "
                a " I don't know who changed it though...since... "
                a " The message of someone changing it was buried by messages... "
                a " I've tried asking about it, but... "
                a " No one would really explain it to me... "
                a " They just said that I look like an apple... "
                a " And I don't know whether I should take that as a compliment or if I should be concerned... "
                a " Because apples are meant to be eaten... "
                a " And I don't want to be eaten alive... "
                a " That's a very scary thought to think about... "
                a " Sorry that I'm...talking about random stuff right now. "
                a " I just...uh... "
                a " I don't really know what topic to talk about, in all honesty... "
                a " ...I don't really want this to be too awkward... "
                a " Sorry if I sound weird right now... "
                " You reassured him that he was doing alright. "
                " Infact, you just wanted to keep talking to him even more now. "
                " You found his choice of topic to be interesting. "
                a " ...Really...? "
                a " I, um... "
                a " I guess I'll continue talking about stuff to you, then... "
                a " Since you say you want to keep talking to me... "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie. "
                " Just talking about the random things Abbie has in his head... "
                " And relaxing, over all. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classroom. "
                pause 2.0
                jump scienceclassfri
            else:
                " You walked over to him and asked him what he was doing. "
                x " Oh, um...hi [name]... "
                x " I don't think I've introduced myself before, so... "
                $ abbieknow = True
                a " I'm...Abbie...it's nice to meet you... "
                a " Uh...you can sit next to me... "
                a " I don't want you to just...stand there... "
                a " It would be really awkward... "
                " You sat down next to him and saw that he was eating some food. "
                " And an apple. "
                a " I decided to eat an apple today... "
                a " ...You know... "
                a " Sometimes I hear people... "
                a " Hear people talking about me an apple...or something... "
                a " They compare me to an apple... "
                a " I don't know whyyy... "
                a " ...I mean, one time... "
                a " I was just doing my stuff on my phone normally, right...? "
                a " And then I noticed that they changed my name in the classroom's GC... "
                a " They changed it to...um... "
                a " ...'Abble'...? with an apple emoji after it... "
                a " I don't know who changed it though...since... "
                a " The message of someone changing it was buried by messages... "
                a " I've tried asking about it, but... "
                a " No one would really explain it to me... "
                a " They just said that I look like an apple... "
                a " And I don't know whether I should take that as a compliment or if I should be concerned... "
                a " Because apples are meant to be eaten... "
                a " And I don't want to be eaten alive... "
                a " That's a very scary thought to think about... "
                a " Sorry that I'm...talking about random stuff right now. "
                a " I just...uh... "
                a " I don't really know what topic to talk about, in all honesty... "
                a " ...I don't really want this to be too awkward... "
                a " Sorry if I sound weird right now... "
                " You reassured him that he was doing alright. "
                " Infact, you just wanted to keep talking to him even more now. "
                " You found his choice of topic to be interesting. "
                a " ...Really...? "
                a " I, um... "
                a " I guess I'll continue talking about stuff to you, then... "
                a " Since you say you want to keep talking to me... "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie. "
                " Just talking about the random things Abbie has in his head... "
                " And relaxing, over all. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classroom. "
                pause 2.0
                jump scienceclassfri
        label robbytherobber:
            show robbyneutral at center with easeinright
            if robbyknow == True:
                " You walked over to him and asked him what he was doing. "
                rb " Hey there, [name]. "
                rb " Come an sit down with me. "
                rb " Standing there while talking with me would just be...really awkward. "
                " You sat down right next to him comfortably. "
                " As you sat down, you noticed that he was looking at a message on his phone. "
                " You decided to ask him about that. "
                rb " Oh, this? "
                rb " Yeah, Riley sent me an apology last night. "
                rb " ...If you even know who she is. "
                rb " She's that insane girl from our class. "
                rb " Always talking about Oliver and what not... "
                rb " It got to the point that I got fed up with her, annnd... "
                rb " I kind of blew up on her yesterday. "
                rb " Like I was telling her how tired I was... "
                hide robbyneutral at bottom
                show robbyangry at center
                rb " Not only does she constantly talk about Oliver, "
                rb " She also asks me to make things for Oliver. "
                rb " Which is kind of more painful for me because I already have other things I need to work on. "
                rb " Like the projects that I actually want to do. "
                rb " And whenever I try to explain to her that I have better things to do... "
                rb " She just keeps on saying this: "
                rb " Oh, you can just focus on my project first! "
                rb " My Oliver doesn't want to be kept waiting, you know? "
                rb " ...Eugh, I hate it whenever she says that. "
                rb " I can't really argue with her whenever she says those words though. "
                rb " She would NEVER take 'no' as an answer. "
                rb " That's why I just kept on working and working... "
                rb " ...Until I tired myself out. "
                rb " And eventually, I got too tired to the point I just snapped at her. "
                rb " I didn't want to yell at her, but... "
                rb " If she just won't listen, might as well just...you know... "
                hide robbyangry at bottom
                show robbyneutral at center
                rb " Sigh. I didn't like yelling at her. "
                rb " But she's gotta learn that I can't just keep working all the time. "
                rb " That would just cause burnout. "
                rb " And I really don't want to be burnt out... "
                rb " I have so much projects to work on, after all. "
                rb " So much stuff that I actually want to do... "
                rb " I can't just give up on those. "
                rb " But it's honestly really hard to deal with, with someone who wants you to work 24/7... "
                rb " Just for someone that they really like. "
                rb " And you don't even want to work on those - but you can't say no to that person. "
                rb " Because they're persistent and annoying. "
                rb " ...I can't even tell if Riley's apology was genuine, but... "
                rb " I guess, atleast she said something about it. "
                rb " Instead of staying quiet and ignoring everything that happened... "
                rb " ...Like she usually does, whenever we get into an argument. "
                rb " Sigh... "
                rb " I'm sorry that I probably brought down the mood, [name]. "
                rb " You know, the conversation's topic... "
                rb " Probably not a nice thing to hear. "
                rb " I just had to let a few things out though. "
                rb " And by a few things, I mean a lot. "
                rb " ...How about let's talk about something you'd actually want to talk about? "
                rb " I don't want to continue making you uncomfortable, after all. "
                rb " It wouldn't be nice of me. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby. "
                " The whole Riley thing seemed a little...tiring. "
                " Like imagine being constantly asked to make something for someone without break. Yikes. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and wthen went to your classroom. "
                pause 2.0
                jump scienceclassfri
            else:
                " You walked over to him and asked him what he was doing. "
                x " Hey there, [name]. "
                x " Don't think I've introduced myself to you yet, so... "
                $ robbyknow = True
                rb " I'm Robby. Nice to meet you. "
                rb " Come an sit down with me. "
                rb " Standing there while talking with me would just be...really awkward. "
                " You sat down right next to him comfortably. "
                " As you sat down, you noticed that he was looking at a message on his phone. "
                " You decided to ask him about that. "
                rb " Oh, this? "
                rb " Yeah, Riley sent me an apology last night. "
                rb " ...If you even know who she is. "
                rb " She's that insane girl from our class. "
                rb " Always talking about Oliver and what not... "
                rb " It got to the point that I got fed up with her, annnd... "
                rb " I kind of blew up on her yesterday. "
                rb " Like I was telling her how tired I was... "
                hide robbyneutral at bottom
                show robbyangry at center
                rb " Not only does she constantly talk about Oliver, "
                rb " She also asks me to make things for Oliver. "
                rb " Which is kind of more painful for me because I already have other things I need to work on. "
                rb " Like the projects that I actually want to do. "
                rb " And whenever I try to explain to her that I have better things to do... "
                rb " She just keeps on saying this: "
                rb " Oh, you can just focus on my project first! "
                rb " My Oliver doesn't want to be kept waiting, you know? "
                rb " ...Eugh, I hate it whenever she says that. "
                rb " I can't really argue with her whenever she says those words though. "
                rb " She would NEVER take 'no' as an answer. "
                rb " That's why I just kept on working and working... "
                rb " ...Until I tired myself out. "
                rb " And eventually, I got too tired to the point I just snapped at her. "
                rb " I didn't want to yell at her, but... "
                rb " If she just won't listen, might as well just...you know... "
                hide robbyangry at bottom
                show robbyneutral at center
                rb " Sigh. I didn't like yelling at her. "
                rb " But she's gotta learn that I can't just keep working all the time. "
                rb " That would just cause burnout. "
                rb " And I really don't want to be burnt out... "
                rb " I have so much projects to work on, after all. "
                rb " So much stuff that I actually want to do... "
                rb " I can't just give up on those. "
                rb " But it's honestly really hard to deal with, with someone who wants you to work 24/7... "
                rb " Just for someone that they really like. "
                rb " And you don't even want to work on those - but you can't say no to that person. "
                rb " Because they're persistent and annoying. "
                rb " ...I can't even tell if Riley's apology was genuine, but... "
                rb " I guess, atleast she said something about it. "
                rb " Instead of staying quiet and ignoring everything that happened... "
                rb " ...Like she usually does, whenever we get into an argument. "
                rb " Sigh... "
                rb " I'm sorry that I probably brought down the mood, [name]. "
                rb " You know, the conversation's topic... "
                rb " Probably not a nice thing to hear. "
                rb " I just had to let a few things out though. "
                rb " And by a few things, I mean a lot. "
                rb " ...How about let's talk about something you'd actually want to talk about? "
                rb " I don't want to continue making you uncomfortable, after all. "
                rb " It wouldn't be nice of me. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby. "
                " The whole Riley thing seemed a little...tiring. "
                " Like imagine being constantly asked to make something for someone without break. Yikes. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and wthen went to your classroom. "
                pause 2.0
                jump scienceclassfri
    label rooftopfri2:
        # petunia and ruby
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked to the rooftop and found two of your classmates talking to eachother. "
        " Wondering what they're talking about, you walked over to them. "
        show petunianeutral at right with easeinleft
        show rubyneutral at left with easeinleft
        if popularknow == True and rubyknow == True:
            ru " Ah, it's [name]! Hi! "
            p " Oooh, hey there [name]! "
            p " I was just asking Ruby a few questions. "
            p " Like what it was like to be a robot and all that! "
            ru " Well...being a robot is cool, sure! "
            ru " But there ARE it's cons, of course... "
            p " Oooh - like what? "
            hide rubyneutral at bottom
            show rubysad at left
            ru " Like being taken pictures of. "
            ru " Without your permission, too! "
            ru " Like people would just come up to you and take a photo with you... "
            ru " Or they're going to take a picture of you without you knowing... "
            ru " And that's really rude! "
            ru " Just because I'm a robot, doesn't mean that I don't have feelings like you humans do, too! "
            ru " Like come on...did I ask to be taken a photo of? "
            ru " Would've been nice if you asked permission first... "
            hide petunianeutral at bottom
            show petuniasurprised at right
            p " Damn, Ruby. "
            p " That must suck a lot... "
            p " I don't think I want that happening to me, too. "
            ru " Yeah, you don't. "
            hide rubysad at bottom
            show rubyneutral at left
            ru " But thankfully I haven't expirienced that! "
            ru " Well, not yet... "
            ru " But it's something that I should be happy about! "
            ru " Or maybe I already have expirienced that, I just didn't know about it... "
            ru " Oh well! they're going to delete that photo soon anyway... "
            ru " In the end, it's just going to be some boring old photo with no meaning. "
            hide petuniasurprised at bottom
            show petunianeutral at right
            p " Yeah, that's kinda true. "
            p " Still, people shouldn't be taking photos of you for being unique. "
            p " Like yeah, that's a robot. "
            p " Just take one look at her and leave. "
            p " No need to post her up on facebook like some tourist attraction. "
            p " Jeez...people like that piss me off. "
            ru " But then again...people who are like that wouldn't listen to you. "
            ru " They would just keep on insisting and insisting... "
            ru " At that point, I would just leave, haha. "
            ru " I don't really want to deal with that anymore. "
            p " Yeah - leaving is honestly the safest option you could do there. "
            p " Especially if you've got someone protecting you from the people. "
            p " Just make sure that they don't go and try to break your screen... "
            p " From, you know...making them mad that they can't take photos of you. "
            ru " Hehe - yeah! I'll make sure of that! "
            ru " I don't want my precious screen to be broken, after all... "
            ru " This thing costed a lot, you know! "
            p " Yup, I can tell! "
            p " I'm talking to pure high quality robot right now. "
            ru " Hehe - you don't have to say thaaatt... "
            p " What? I'm just complimenting you thoouugh... "
            p " And I mean it when I said that you were high quality! "
            ru " Awww!! "
            ru " So much people at this school are so kind... "
            ru " I appreciate you all, really! "
            p " Haha, and we appreciate you too, Ruby. "
            scene black with dissolve
            " You spent the rest of the break talking with Petunia and Ruby. "
            " It must be painful for people taking photos of you without their permission... "
            " You didn't want that happening to any of your classmates at all. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and went to your classroom. "
            pause 2.0
            jump scienceclassfri
        elif popularknow == True and rubyknow == False:
            x " Ah, it's [name]! Hi! "
            p " Oooh, hey there [name]! "
            $ rubyknow = True
            p " I was just asking Ruby a few questions. "
            p " Like what it was like to be a robot and all that! "
            ru " Well...being a robot is cool, sure! "
            ru " But there ARE it's cons, of course... "
            p " Oooh - like what? "
            hide rubyneutral at bottom
            show rubysad at left
            ru " Like being taken pictures of. "
            ru " Without your permission, too! "
            ru " Like people would just come up to you and take a photo with you... "
            ru " Or they're going to take a picture of you without you knowing... "
            ru " And that's really rude! "
            ru " Just because I'm a robot, doesn't mean that I don't have feelings like you humans do, too! "
            ru " Like come on...did I ask to be taken a photo of? "
            ru " Would've been nice if you asked permission first... "
            hide petunianeutral at bottom
            show petuniasurprised at right
            p " Damn, Ruby. "
            p " That must suck a lot... "
            p " I don't think I want that happening to me, too. "
            ru " Yeah, you don't. "
            hide rubysad at bottom
            show rubyneutral at left
            ru " But thankfully I haven't expirienced that! "
            ru " Well, not yet... "
            ru " But it's something that I should be happy about! "
            ru " Or maybe I already have expirienced that, I just didn't know about it... "
            ru " Oh well! they're going to delete that photo soon anyway... "
            ru " In the end, it's just going to be some boring old photo with no meaning. "
            hide petuniasurprised at bottom
            show petunianeutral at right
            p " Yeah, that's kinda true. "
            p " Still, people shouldn't be taking photos of you for being unique. "
            p " Like yeah, that's a robot. "
            p " Just take one look at her and leave. "
            p " No need to post her up on facebook like some tourist attraction. "
            p " Jeez...people like that piss me off. "
            ru " But then again...people who are like that wouldn't listen to you. "
            ru " They would just keep on insisting and insisting... "
            ru " At that point, I would just leave, haha. "
            ru " I don't really want to deal with that anymore. "
            p " Yeah - leaving is honestly the safest option you could do there. "
            p " Especially if you've got someone protecting you from the people. "
            p " Just make sure that they don't go and try to break your screen... "
            p " From, you know...making them mad that they can't take photos of you. "
            ru " Hehe - yeah! I'll make sure of that! "
            ru " I don't want my precious screen to be broken, after all... "
            ru " This thing costed a lot, you know! "
            p " Yup, I can tell! "
            p " I'm talking to pure high quality robot right now. "
            ru " Hehe - you don't have to say thaaatt... "
            p " What? I'm just complimenting you thoouugh... "
            p " And I mean it when I said that you were high quality! "
            ru " Awww!! "
            ru " So much people at this school are so kind... "
            ru " I appreciate you all, really! "
            p " Haha, and we appreciate you too, Ruby. "
            scene black with dissolve
            " You spent the rest of the break talking with Petunia and Ruby. "
            " It must be painful for people taking photos of you without their permission... "
            " You didn't want that happening to any of your classmates at all. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and went to your classroom. "
            pause 2.0
            jump scienceclassfri
        elif popularknow == False and rubyknow == True:
            ru " Ah, it's [name]! Hi! "
            x " Oooh, hey there [name]! "
            $ popularknow = True
            p " I'm Petunia, by the way. "
            p " I was just asking Ruby a few questions. "
            p " Like what it was like to be a robot and all that! "
            ru " Well...being a robot is cool, sure! "
            ru " But there ARE it's cons, of course... "
            p " Oooh - like what? "
            hide rubyneutral at bottom
            show rubysad at left
            ru " Like being taken pictures of. "
            ru " Without your permission, too! "
            ru " Like people would just come up to you and take a photo with you... "
            ru " Or they're going to take a picture of you without you knowing... "
            ru " And that's really rude! "
            ru " Just because I'm a robot, doesn't mean that I don't have feelings like you humans do, too! "
            ru " Like come on...did I ask to be taken a photo of? "
            ru " Would've been nice if you asked permission first... "
            hide petunianeutral at bottom
            show petuniasurprised at right
            p " Damn, Ruby. "
            p " That must suck a lot... "
            p " I don't think I want that happening to me, too. "
            ru " Yeah, you don't. "
            hide rubysad at bottom
            show rubyneutral at left
            ru " But thankfully I haven't expirienced that! "
            ru " Well, not yet... "
            ru " But it's something that I should be happy about! "
            ru " Or maybe I already have expirienced that, I just didn't know about it... "
            ru " Oh well! they're going to delete that photo soon anyway... "
            ru " In the end, it's just going to be some boring old photo with no meaning. "
            hide petuniasurprised at bottom
            show petunianeutral at right
            p " Yeah, that's kinda true. "
            p " Still, people shouldn't be taking photos of you for being unique. "
            p " Like yeah, that's a robot. "
            p " Just take one look at her and leave. "
            p " No need to post her up on facebook like some tourist attraction. "
            p " Jeez...people like that piss me off. "
            ru " But then again...people who are like that wouldn't listen to you. "
            ru " They would just keep on insisting and insisting... "
            ru " At that point, I would just leave, haha. "
            ru " I don't really want to deal with that anymore. "
            p " Yeah - leaving is honestly the safest option you could do there. "
            p " Especially if you've got someone protecting you from the people. "
            p " Just make sure that they don't go and try to break your screen... "
            p " From, you know...making them mad that they can't take photos of you. "
            ru " Hehe - yeah! I'll make sure of that! "
            ru " I don't want my precious screen to be broken, after all... "
            ru " This thing costed a lot, you know! "
            p " Yup, I can tell! "
            p " I'm talking to pure high quality robot right now. "
            ru " Hehe - you don't have to say thaaatt... "
            p " What? I'm just complimenting you thoouugh... "
            p " And I mean it when I said that you were high quality! "
            ru " Awww!! "
            ru " So much people at this school are so kind... "
            ru " I appreciate you all, really! "
            p " Haha, and we appreciate you too, Ruby. "
            scene black with dissolve
            " You spent the rest of the break talking with Petunia and Ruby. "
            " It must be painful for people taking photos of you without their permission... "
            " You didn't want that happening to any of your classmates at all. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and went to your classroom. "
            pause 2.0
            jump scienceclassfri
        else:
            x " Ah, it's [name]! Hi! "
            x " Oooh, hey there [name]! "
            $ popularknow = True
            p " I'm Petunia, by the way. "
            $ rubyknow = True
            p " I was just asking Ruby a few questions. "
            p " Like what it was like to be a robot and all that! "
            ru " Well...being a robot is cool, sure! "
            ru " But there ARE it's cons, of course... "
            p " Oooh - like what? "
            hide rubyneutral at bottom
            show rubysad at left
            ru " Like being taken pictures of. "
            ru " Without your permission, too! "
            ru " Like people would just come up to you and take a photo with you... "
            ru " Or they're going to take a picture of you without you knowing... "
            ru " And that's really rude! "
            ru " Just because I'm a robot, doesn't mean that I don't have feelings like you humans do, too! "
            ru " Like come on...did I ask to be taken a photo of? "
            ru " Would've been nice if you asked permission first... "
            hide petunianeutral at bottom
            show petuniasurprised at right
            p " Damn, Ruby. "
            p " That must suck a lot... "
            p " I don't think I want that happening to me, too. "
            ru " Yeah, you don't. "
            hide rubysad at bottom
            show rubyneutral at left
            ru " But thankfully I haven't expirienced that! "
            ru " Well, not yet... "
            ru " But it's something that I should be happy about! "
            ru " Or maybe I already have expirienced that, I just didn't know about it... "
            ru " Oh well! they're going to delete that photo soon anyway... "
            ru " In the end, it's just going to be some boring old photo with no meaning. "
            hide petuniasurprised at bottom
            show petunianeutral at right
            p " Yeah, that's kinda true. "
            p " Still, people shouldn't be taking photos of you for being unique. "
            p " Like yeah, that's a robot. "
            p " Just take one look at her and leave. "
            p " No need to post her up on facebook like some tourist attraction. "
            p " Jeez...people like that piss me off. "
            ru " But then again...people who are like that wouldn't listen to you. "
            ru " They would just keep on insisting and insisting... "
            ru " At that point, I would just leave, haha. "
            ru " I don't really want to deal with that anymore. "
            p " Yeah - leaving is honestly the safest option you could do there. "
            p " Especially if you've got someone protecting you from the people. "
            p " Just make sure that they don't go and try to break your screen... "
            p " From, you know...making them mad that they can't take photos of you. "
            ru " Hehe - yeah! I'll make sure of that! "
            ru " I don't want my precious screen to be broken, after all... "
            ru " This thing costed a lot, you know! "
            p " Yup, I can tell! "
            p " I'm talking to pure high quality robot right now. "
            ru " Hehe - you don't have to say thaaatt... "
            p " What? I'm just complimenting you thoouugh... "
            p " And I mean it when I said that you were high quality! "
            ru " Awww!! "
            ru " So much people at this school are so kind... "
            ru " I appreciate you all, really! "
            p " Haha, and we appreciate you too, Ruby. "
            scene black with dissolve
            " You spent the rest of the break talking with Petunia and Ruby. "
            " It must be painful for people taking photos of you without their permission... "
            " You didn't want that happening to any of your classmates at all. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and went to your classroom. "
            pause 2.0
            jump scienceclassfri
    label libraryfri2:
        # bubble and skell
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked over to the library and spotted two of your classmates doing their own things. "
        " Who should you talk to? "
        if bubbleknow == True and skellknow == True:
            menu:
                " {image=bubbleicon} Bubble {image=bubbleicon} ":
                    jump moresaus
                " {image=skellicon} Skell {image=skellicon} ":
                    jump morefood
        elif bubbleknow == True and skellknow == False:
            menu:
                " {image=bubbleicon} Bubble {image=bubbleicon} ":
                    jump moresaus
                " {image=skellicon} An emo guy {image=skellicon} ":
                    jump morefood
        elif bubbleknow == False and skellknow == True:
            menu:
                " {image=bubbleicon} A girl made out of bubbles. {image=bubbleicon} ":
                    jump moresaus
                " {image=skellicon} Skell {image=skellicon} ":
                    jump morefood
        else:
            menu:
                " {image=bubbleicon} A girl made out of bubbles. {image=bubbleicon} ":
                    jump moresaus
                " {image=skellicon} An emo guy {image=skellicon} ":
                    jump morefood
        label moresaus:
            show bubbleneutral at center with easeinright
            if bubbleknow == True:
                " You walked over to her and asked her what she was doing. "
                b " Hmhmmm...hey [name]!! "
                b " I'm just trying to rearrange some of the books here... "
                b " Someone keeps on misplacing them... "
                b " Seeing misplaced books is an absolute ick from me. "
                b " That's why I'm trying to put them back into their place! "
                b " ...While making sure that I don't accidentally pop myself. "
                b " Since I'm made up of bubbles, I've got to be careful of everything! "
                hide bubbleneutral at bottom
                show bubblesad at center
                b " I have to watch every step and...everything! "
                b " You have no idea how many times I've almost popped myself... "
                b " One time, Oliver tried to throw a prank on me - "
                b " - I think you see where this is going. "
                b " He tried to get me to pop SO many times!! "
                b " He started by putting pins on the ground... "
                b " And Engel luckily noticed them, so I survived THAT... "
                b " And ever since that day - he still tries to pop me!! "
                b " And I don't want that happening! "
                b " So...I can't just walk around without worrying something's gonna pop me! "
                b " I've always got to be careful, no matter what! "
                b " Siiighh...sometimes I don't like being a bubble... "
                b " You get to deal with this type of stuff every now and then... "
                b " But I can't just change myself to be like everyone else! "
                b " I was literally born like this, how am I supposed to change that? "
                b " Life is a struggle in this school, really... "
                hide bubblesad at bottom
                show bubbleneutral at center
                b " But again - we can't do anything about it. "
                b " We just gotta continue living on... "
                b " Because we've still gotta continue and finish school! "
                b " Can't just go out to the real world without learning anything! "
                b " Oh, uh...what was I doing again? "
                b " I think I might've gotten a little too distracted, hehe... "
                " You tell her that she was trying to rearrange the books... "
                " ...Because someone kept on misplacing them. "
                " You wonder how she even forgot that fast... "
                b " Oh! oh right, oopsies... "
                b " I completely forgot since I was so focused on talking to you. "
                b " It's kind of...a thing that I do every now and then. "
                b " Hey...since you're here... "
                b " You wanna help me with arranging? "
                b " I wouldn't want to do this stuff alone, after all! "
                b " Things are better when you do it with friends, is what they say... "
                " Well, you had nothing else to do in this break. "
                " So, you agreed to help Bubble. "
                b " Allllright! "
                b " Just move the books to where you think they should be, okay? "
                b " Take a look at their titles and put them in the section they should be in! "
                b " Like if it looks horror, put it in the horror section! "
                b " I think you already get the idea for the rest. "
                b " I'll take that side and you'll take this side! "
                b " If you feel like you can't go on anymore, just tell me, okay? "
                " You gave her a thumbs up before you started to go back to work. "
                scene black with dissolve
                " You spent the rest of the break talking with and helping Bubble. "
                " Just rearranging the books... "
                " You saw some dust bunnies here and there while you were arranging. "
                " Cute. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the library and went to your classroom. "
                pause 2.0
                jump scienceclassfri
            else:
                " You walked over to her and asked her what she was doing. "
                x " Hmhmmm...hey [name]!! "
                $ bubbleknow = True
                b " I'm Bubble, by the way. "
                b " I'm just trying to rearrange some of the books here... "
                b " Someone keeps on misplacing them... "
                b " Seeing misplaced books is an absolute ick from me. "
                b " That's why I'm trying to put them back into their place! "
                b " ...While making sure that I don't accidentally pop myself. "
                b " Since I'm made up of bubbles, I've got to be careful of everything! "
                hide bubbleneutral at bottom
                show bubblesad at center
                b " I have to watch every step and...everything! "
                b " You have no idea how many times I've almost popped myself... "
                b " One time, Oliver tried to throw a prank on me - "
                b " - I think you see where this is going. "
                b " He tried to get me to pop SO many times!! "
                b " He started by putting pins on the ground... "
                b " And Engel luckily noticed them, so I survived THAT... "
                b " And ever since that day - he still tries to pop me!! "
                b " And I don't want that happening! "
                b " So...I can't just walk around without worrying something's gonna pop me! "
                b " I've always got to be careful, no matter what! "
                b " Siiighh...sometimes I don't like being a bubble... "
                b " You get to deal with this type of stuff every now and then... "
                b " But I can't just change myself to be like everyone else! "
                b " I was literally born like this, how am I supposed to change that? "
                b " Life is a struggle in this school, really... "
                hide bubblesad at bottom
                show bubbleneutral at center
                b " But again - we can't do anything about it. "
                b " We just gotta continue living on... "
                b " Because we've still gotta continue and finish school! "
                b " Can't just go out to the real world without learning anything! "
                b " Oh, uh...what was I doing again? "
                b " I think I might've gotten a little too distracted, hehe... "
                " You tell her that she was trying to rearrange the books... "
                " ...Because someone kept on misplacing them. "
                " You wonder how she even forgot that fast... "
                b " Oh! oh right, oopsies... "
                b " I completely forgot since I was so focused on talking to you. "
                b " It's kind of...a thing that I do every now and then. "
                b " Hey...since you're here... "
                b " You wanna help me with arranging? "
                b " I wouldn't want to do this stuff alone, after all! "
                b " Things are better when you do it with friends, is what they say... "
                " Well, you had nothing else to do in this break. "
                " So, you agreed to help Bubble. "
                b " Allllright! "
                b " Just move the books to where you think they should be, okay? "
                b " Take a look at their titles and put them in the section they should be in! "
                b " Like if it looks horror, put it in the horror section! "
                b " I think you already get the idea for the rest. "
                b " I'll take that side and you'll take this side! "
                b " If you feel like you can't go on anymore, just tell me, okay? "
                " You gave her a thumbs up before you started to go back to work. "
                scene black with dissolve
                " You spent the rest of the break talking with and helping Bubble. "
                " Just rearranging the books... "
                " You saw some dust bunnies here and there while you were arranging. "
                " Cute. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the library and went to your classroom. "
                pause 2.0
                jump scienceclassfri
        label morefood:
            show skellneutral at center with easeinleft
            if skellknow == True:
                " You walked over to him and asked what he was doing. "
                sk " ...Hi, [name]. "
                sk " I've been sitting here and watching my phone... "
                sk " But I've noticed something. "
                sk " See that girl over there? her name's Bubble. "
                sk " One of our classmates, if you don't know her. "
                sk " She's been trying to organize the books... "
                sk " But I've noticed that Zip has been messing with her. "
                sk " Like - she's been going and messing up the books everytime Bubble fixes them. "
                sk " And the thing is - Bubble hasn't even noticed Zip. "
                sk " So she's been going back and forth rearranging the books... "
                sk " Without even noticing that someone's been messing with her. "
                sk " Honestly, I feel a little bad, but... "
                sk " I know that if I interefered, I'd probably get my ass beat. "
                sk " Zip is short and looks innocent, but you can't fall for that. "
                sk " She's a good fighter, and even worse... "
                sk " A good ankle biter. "
                sk " I most certainly don't want my ankles to be bitten by her. "
                sk " All we can pretty much do is just...watch. "
                sk " Even if that's the thing that we don't want to do. "
                sk " Zip can basically just ruin your life if you don't let her do what she wants to do. "
                sk " She knows a lot of things, actually. "
                sk " Due to how Oliver and Edward keeps her getting information from every person in this school... "
                sk " She knows everyone's secrets, even if you whisper them. "
                sk " Now that I think about it, she's got some good hearing. "
                sk " I wouldn't be surprised if Zip's listening in right now. "
                sk " But like I said... "
                sk " Don't let her do whatever she wants, and your secrets are coming out. "
                sk " She won't hesitate to spread it all throughout the school... "
                sk " All just to see you suffer. "
                sk " Oliver's gang are menaces, but there's nothing we can do about them. "
                sk " Not when they can beat our ass up anytime they want. "
                sk " Not when they're favored by the teachers. "
                sk " ...It sucks, but we've just gotta live through this. "
                sk " Just gotta wait for any breaks and we're free... "
                scene black with dissolve
                " You spent the rest of the break talking with Skell. "
                " You did feel like you should help Bubble, but... "
                " You really didn't want to get your ankles broken. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked out of the library and went to your classroom. "
                pause 2.0
                jump scienceclassfri
            else:
                " You walked over to him and asked what he was doing. "
                x " ...Hi, [name]. "
                $ skellknow = True
                sk " I'm Skell. It's nice to meet you. "
                sk " I've been sitting here and watching my phone... "
                sk " But I've noticed something. "
                sk " See that girl over there? her name's Bubble. "
                sk " One of our classmates, if you don't know her. "
                sk " She's been trying to organize the books... "
                sk " But I've noticed that Zip has been messing with her. "
                sk " Like - she's been going and messing up the books everytime Bubble fixes them. "
                sk " And the thing is - Bubble hasn't even noticed Zip. "
                sk " So she's been going back and forth rearranging the books... "
                sk " Without even noticing that someone's been messing with her. "
                sk " Honestly, I feel a little bad, but... "
                sk " I know that if I interefered, I'd probably get my ass beat. "
                sk " Zip is short and looks innocent, but you can't fall for that. "
                sk " She's a good fighter, and even worse... "
                sk " A good ankle biter. "
                sk " I most certainly don't want my ankles to be bitten by her. "
                sk " All we can pretty much do is just...watch. "
                sk " Even if that's the thing that we don't want to do. "
                sk " Zip can basically just ruin your life if you don't let her do what she wants to do. "
                sk " She knows a lot of things, actually. "
                sk " Due to how Oliver and Edward keeps her getting information from every person in this school... "
                sk " She knows everyone's secrets, even if you whisper them. "
                sk " Now that I think about it, she's got some good hearing. "
                sk " I wouldn't be surprised if Zip's listening in right now. "
                sk " But like I said... "
                sk " Don't let her do whatever she wants, and your secrets are coming out. "
                sk " She won't hesitate to spread it all throughout the school... "
                sk " All just to see you suffer. "
                sk " Oliver's gang are menaces, but there's nothing we can do about them. "
                sk " Not when they can beat our ass up anytime they want. "
                sk " Not when they're favored by the teachers. "
                sk " ...It sucks, but we've just gotta live through this. "
                sk " Just gotta wait for any breaks and we're free... "
                scene black with dissolve
                " You spent the rest of the break talking with Skell. "
                " You did feel like you should help Bubble, but... "
                " You really didn't want to get your ankles broken. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked out of the library and went to your classroom. "
                pause 2.0
                jump scienceclassfri
    label oligangfri2:
        scene black with dissolve
        pause 2.0
        scene oligangclub with dissolve
        " You walked into the room and saw Edward and Oliver hanging out. "
        " Wondering what they're doing, you walked over to them. "
        show edwardneutral at left with easeinright
        show oliverneutral at right with easeinright
        o " Hey look, it's dumbass. "
        ed " Yo yo, [name]!! "
        o " Oh geez, you too? "
        ed " ...Haven't I been calling [them] by [their] name for awhile now? "
        ed " Like, I'm pretty sure I did that. "
        ed " It's not a new thing or anything... "
        ed " Maybe ya just weren't paying attention. "
        o " Yeah, because I was paying attention to my girlfriend's fine ass. "
        hide edwardneutral at bottom
        show edwardangry at left
        ed " Wow - she's not even here, dude. "
        ed " If you start going on a whole thing about your girlfriend I'm going to leave this room. "
        ed " I do NOT want to hear another word about her. "
        ed " Ya talk about her wayyyy too much, dude... "
        ed " Like - I know ya love her, but ya don't gotta keep talking about her. "
        ed " Ya talk sooo much about her, ya practically got me and Zip ripping our ears out. "
        ed " Disgusting, really... "
        o " You guys just can't handle true love! "
        o " I doubt you guys would know anything about that. "
        o " And I bet you guys are just jealous just cause I pulled a hot babe! "
        o " Heheheee, I got someone hot, and you guys doont... "
        ed " Oooh my god, I'm leaving. "
        ed " I am NOT dealing with this. "
        o " No, Eddieeeee...don't leaveeee... "
        o " We still gotta hang out togetherrrr... "
        ed " Nah, I'm out. Not dealing with this today. "
        hide edwardangry at right with easeoutright
        show oliverneutral at center with move
        o " Heh, he's so easy to ragebait. "
        o " He's a funny one. "
        scene black with dissolve
        " You spent the rest of the break talking with Oliver. "
        " ...The topic was just mostly about Oliver's girlfriend. "
        " Now you can see why Zip and Edward wanted to rip their ears out. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You waited for a bit before you went to your classroom. "
        pause 2.0
        jump scienceclassfri

label scienceclassfri:
    scene classroom with dissolve
    " You walked into the classroom and spotted that the science teacher was already there. "
    " You wasted no time, and you went to your assigned seat and got out your notebook and pen. "
    " You didn't want your ass to be beat for just standing there, after all. "
    " And you also didn't want your ass to fail for having no notes to study. "
    " Nope, not in this universe. You're not failing here. "
    show missbloomieneutral at center with easeinleft
    msb " Hello, class. "
    msb " We're going to be taking down notes for today. "
    msb " I better not catch any of you falling asleep in class. "
    msb " I know it's the last day for school this week, but... "
    msb " Remember that we're having a class here. "
    msb " And having a class means that you have to pay attention. "
    msb " You may sleep when you get back home. "
    msb " You can pretty much just sleep anywhere as long as it isn't in the classroom, actually. "
    msb " If I catch you distracted, don't be surprised if I yell at you to wake you up. "
    msb " Or maybe even have your classmates start yelling in your ear if you're distracted. "
    msb " I'm the teacher here, I can make you guys do whatever I say. "
    msb " Now, back to our lesson. "
    msb " Make sure to pay attention to the slides. "
    msb " Remember what I'm going to do if I catch you sleeping. "
    msb " I'm watching all of you. "
    scene black with dissolve
    " You spent the rest of this class taking down notes. "
    " Yep, you're probably right. All of the classes are just gonna be note taking. "
    " Not that you minded too much though. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for another break. "
    " You hop off of your seat and walked to the hallways. "
    pause 2.0
    jump fribreak3

label fribreak3:
    # abbie end + oligang end
    scene hallway with dissolve
    if oligangjoin == True:
        jump oligangfri3
    else:
        pass
    " Where are you gonna hang out for this break? "
    menu:
        " {image=bubbleicon} The front of the school {image=kevinicon} ":
            jump frontschoolfri3
        " {image=popularicon} The back of the school {image=robbyicon} ":
            jump backschoolfri3
        " {image=abbieicon} The gym {image=rubyicon} ":
            jump gymfri3
            # abbie and oliver
        " {image=rileyicon} The cafeteria {image=lanaicon} ":
            jump cafeteriafri3
        " {image=claireicon} The rooftop {image=skellicon} ":
            jump rooftopfri3
        " {image=cubbieicon} The library {image=engelicon} ":
            jump libraryfri3
    label frontschoolfri3:
        # bubble and kevin // not interact
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked to the front of the school and spotted two of your classmates doing their own things. "
        " You wanted to talk to one of them...but who do you talk to? "
        if bubbleknow == True and kevinknow == True:
            menu:
                " {image=bubbleicon} Bubble {image=bubbleicon} ":
                    jump chaosblast
                " {image=kevinicon} Kevin {image=kevinicon} ":
                    jump altergate
        elif bubbleknow == True and kevinknow == False:
            menu:
                " {image=bubbleicon} Bubble {image=bubbleicon} ":
                    jump chaosblast
                " {image=kevinicon} A nerd {image=kevinicon} ":
                    jump altergate
        elif bubbleknow == False and kevinknow == True:
            menu:
                " {image=bubbleicon} A girl made up of bubbles {image=bubbleicon} ":
                    jump chaosblast
                " {image=kevinicon} Kevin {image=kevinicon} ":
                    jump altergate
        else:
            menu:
                " {image=bubbleicon} A girl made up of bubbles {image=bubbleicon} ":
                    jump chaosblast
                " {image=kevinicon} A nerd {image=kevinicon} ":
                    jump altergate
        label chaosblast:
            show bubbleneutral at center with easeinleft
            if bubbleknow == True:
                " You walked over to her and asked her what she was doing. "
                b " Hi [name]!! "
                b " Today would be a perfect day to go on a walk, right? "
                b " ...Okay, that just makes me sound so boring. "
                b " But I really mean it! "
                b " The sun is shining, birds are chirping... "
                b " On days like these, kids like us should probably get to doing our schoolwork... "
                b " But maybe after school I could go on a quick walk around town! "
                b " Wouldn't hurt to do that, right? "
                b " After all, it's just a walk! "
                b " Maybe I might see some interesting stuff going on... "
                b " Like I don't know...seeing drama? "
                b " Though if I do see drama, I have to make it not obvious that I'm listening in! "
                b " You know how it'll end up if I get caught eavesdropping. "
                b " Ough... "
                b " Anyway, I hope you have a good day today, [name]!! "
                b " I'm sure you're probably having a good day right now, soo... "
                b " I hope you have an even BETTER day! "
                " ...Huh. "
                " All I can say for this girl is that she's really positive. "
                " Kind of reminds me of those girls in anime who's really energetic... "
                " Like those really happy anime girls you see smiling 24/7. "
                " She doesn't smile too much though...wait. "
                " She doesn't even have a mouth. "
                b " Mmm... "
                b " On another topic, I think I should actually get to doing my missing requirements. "
                b " According to Miss Emily - I have...a few missing things. "
                b " Like...totally just a few missing things. "
                b " I'm totally not missing five whole performance tasks right now. "
                b " ...My grades are going to be doomed if I don't do them. "
                b " Could you help me in looking for some references, [name]? "
                b " Most of the performances I'm missing are just art and essays. "
                b " Nothing too bad, right? "
                b " I have to make art based off on certan periods... "
                b " Annnd then I have to explain what certain things are in essays. "
                b " Nothing too hard, but I still need some references, you know! "
                b " Mostly for the art part. "
                " You agreed to help Bubble for this break. "
                " I mean, you had nothing else to do for this break. "
                scene black with dissolve
                " You spent the rest of the break helping Bubble with her performance tasks. "
                " Just giving her some references and talking with her every now and then.. "
                " You like being helpful like this sometimes. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump historyclassfri
            else:
                " You walked over to her and asked her what she was doing. "
                x " Hi [name]!! "
                x " I don't think I've met you before, so... "
                $ bubbleknow = True
                b " I'm Bubble - one of your classmates! "
                b " It's nice to meet you! "
                b " Today would be a perfect day to go on a walk, right? "
                b " ...Okay, that just makes me sound so boring. "
                b " But I really mean it! "
                b " The sun is shining, birds are chirping... "
                b " On days like these, kids like us should probably get to doing our schoolwork... "
                b " But maybe after school I could go on a quick walk around town! "
                b " Wouldn't hurt to do that, right? "
                b " After all, it's just a walk! "
                b " Maybe I might see some interesting stuff going on... "
                b " Like I don't know...seeing drama? "
                b " Though if I do see drama, I have to make it not obvious that I'm listening in! "
                b " You know how it'll end up if I get caught eavesdropping. "
                b " Ough... "
                b " Anyway, I hope you have a good day today, [name]!! "
                b " I'm sure you're probably having a good day right now, soo... "
                b " I hope you have an even BETTER day! "
                " ...Huh. "
                " All I can say for this girl is that she's really positive. "
                " Kind of reminds me of those girls in anime who's really energetic... "
                " Like those really happy anime girls you see smiling 24/7. "
                " She doesn't smile too much though...wait. "
                " She doesn't even have a mouth. "
                b " Mmm... "
                b " On another topic, I think I should actually get to doing my missing requirements. "
                b " According to Miss Emily - I have...a few missing things. "
                b " Like...totally just a few missing things. "
                b " I'm totally not missing five whole performance tasks right now. "
                b " ...My grades are going to be doomed if I don't do them. "
                b " Could you help me in looking for some references, [name]? "
                b " Most of the performances I'm missing are just art and essays. "
                b " Nothing too bad, right? "
                b " I have to make art based off on certan periods... "
                b " Annnd then I have to explain what certain things are in essays. "
                b " Nothing too hard, but I still need some references, you know! "
                b " Mostly for the art part. "
                " You agreed to help Bubble for this break. "
                " I mean, you had nothing else to do for this break. "
                scene black with dissolve
                " You spent the rest of the break helping Bubble with her performance tasks. "
                " Just giving her some references and talking with her every now and then.. "
                " You like being helpful like this sometimes. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump historyclassfri
        label altergate:
            show kevinneutral at center with easeinright
            if kevinknow == True:
                " You walked over to him and asked him what he was doing. "
                kv " Hm? ah, [name]. "
                kv " It's nice to see you here. "
                kv " I was just looking at some books for history later. "
                kv " I'm going to tell you something surprising, but... "
                kv " I don't actually pay that much attention to history unless if we have something important to do. "
                kv " That's why I'm doing a whole lot of research right now. "
                kv " Like, a whole whole lot. "
                kv " I don't want to fail history, after all... "
                kv " I don't want to fail any class. "
                kv " I have a feeling we're going to have something important to do next week... "
                kv " That's also another reason why I'm studying a lot right now. "
                kv " I know I might forget about all this information later, but... "
                kv " Studying can do no harm, right? "
                kv " Well, unless if you overdo the studying. "
                kv " And another thing - studying can also be a good time waster. "
                kv " Since you're so focused on getting more information, "
                kv " You wouldn't be able to notice the time. "
                kv " That's why I like to study a whole lot whenever I don't have something important to do. "
                kv " Even though I don't need the information... "
                kv " I probably will need it at some point. "
                kv " Like in tests, for example. "
                kv " Or whenever I have to recite verbally. "
                kv " It would be embarrassing if I just stand there and say nothing, after all... "
                kv " Actually, while you're here... "
                kv " Would you want to study with me? "
                kv " I understand if you don't want to. "
                kv " Some people - no, most people don't like studying... "
                kv " Mostly because they think that it's a waste of time. "
                kv " But it's a good waste of time, like I said earlier. "
                kv " I'd completely understand if you don't want to study with me. "
                kv " So, uh... "
                kv " Don't worry about me forcing you to study with me or something. "
                kv " I'm fine with studying on my own. "
                " You didn't have anything else to do for this break, so... "
                " You decided to go and study with Kevin, as much as you hated studying. "
                kv " Oh? you want to study with me? "
                kv " Alright... "
                kv " Come and sit on this bench with me. "
                kv " Don't want you to be uncomfortable after all. "
                scene black with dissolve
                " You spent the rest of the break studying with Kevin. "
                " You're definitely forgetting about this information the moment the bell rings. "
                " Which is in three...twoo..one... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump historyclassfri
            else:
                " You walked over to him and asked him what he was doing. "
                x " Hm? ah, [name]. "
                x " It's nice to see you here. "
                x " I don't think I've introduced myself to you before, so... "
                x " I think it would be best if I do that right now. "
                $ kevinknow = True
                kv " I'm Kevin, one of your classmates. "
                kv " It's nice to meet you. "
                kv " I was just looking at some books for history later. "
                kv " I'm going to tell you something surprising, but... "
                kv " I don't actually pay that much attention to history unless if we have something important to do. "
                kv " That's why I'm doing a whole lot of research right now. "
                kv " Like, a whole whole lot. "
                kv " I don't want to fail history, after all... "
                kv " I don't want to fail any class. "
                kv " I have a feeling we're going to have something important to do next week... "
                kv " That's also another reason why I'm studying a lot right now. "
                kv " I know I might forget about all this information later, but... "
                kv " Studying can do no harm, right? "
                kv " Well, unless if you overdo the studying. "
                kv " And another thing - studying can also be a good time waster. "
                kv " Since you're so focused on getting more information, "
                kv " You wouldn't be able to notice the time. "
                kv " That's why I like to study a whole lot whenever I don't have something important to do. "
                kv " Even though I don't need the information... "
                kv " I probably will need it at some point. "
                kv " Like in tests, for example. "
                kv " Or whenever I have to recite verbally. "
                kv " It would be embarrassing if I just stand there and say nothing, after all... "
                kv " Actually, while you're here... "
                kv " Would you want to study with me? "
                kv " I understand if you don't want to. "
                kv " Some people - no, most people don't like studying... "
                kv " Mostly because they think that it's a waste of time. "
                kv " But it's a good waste of time, like I said earlier. "
                kv " I'd completely understand if you don't want to study with me. "
                kv " So, uh... "
                kv " Don't worry about me forcing you to study with me or something. "
                kv " I'm fine with studying on my own. "
                " You didn't have anything else to do for this break, so... "
                " You decided to go and study with Kevin, as much as you hated studying. "
                kv " Oh? you want to study with me? "
                kv " Alright... "
                kv " Come and sit on this bench with me. "
                kv " Don't want you to be uncomfortable after all. "
                scene black with dissolve
                " You spent the rest of the break studying with Kevin. "
                " You're definitely forgetting about this information the moment the bell rings. "
                " Which is in three...twoo..one... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump historyclassfri
    label backschoolfri3:
        # lizzy and robby // interact
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of the school and found two of your classmates talking with eachother. "
        " Wondering what they're talking about, you decided to join their conversation. "
        show lizzyneutral at right with easeinleft
        show robbyneutral at left with easeinleft
        if popularknow == True and robbyknow == True:
            lz " Oh look, [name] is here. "
            rb " ...Hi, [name]. "
            rb " Me and Lizzy were just talking about a project we're planning to do. "
            lz " Yeah, just make a figure of me and Petunia. "
            lz " Of course, I don't want you to stress out over this thing getting done in a day. "
            lz " So...you can finish this whenever you're free. "
            lz " I'm not just gonna force you to finish it it in 1 second. "
            lz " That's quite literally impossible. "
            lz " So, you've got all the time in the world to make that thing. "
            lz " I don't mind if you take a year, a month... "
            lz " As long as you're all comfortable and not stressed out. "
            lz " Being stressed can make you burnt out, you know. "
            lz " And I heard that isn't a good thing. "
            lz " Apparently it makes you less motivated to do stuff. "
            rb " Yeah, you're right about that... "
            rb " But, just one problem. "
            rb " What if I forget about the project entirely? "
            lz " I don't care if you forget about the project, "
            lz " Just put it on like...a white board or something. "
            lz " You got one of those, right? "
            rb " Of course I do. "
            rb " That's where I list down all of my projects. "
            lz " Then you can put my project down there, so you won't forget. "
            lz " Do I have to pay you for this sort of thing? "
            rb " Well, no. "
            rb " I don't usually want to get paid. "
            rb " But, if you want to, then... "
            lz " Dude, just say that you want to get paid. "
            lz " You clearly don't get paid enough for Riley's bullshit. "
            lz " You know...whenever she asks you to make something. "
            rb " ...Yeah, I don't get paid enough. "
            rb " She doesn't pay me at all, unsurprisingly. "
            lz " Then I'll be sort of the first one to pay you for your works. "
            lz " Judging by how the final product will look... "
            " Lizzy reaches into her pocket for her wallet. "
            " You're starting to wonder a bit how much money she has... "
            " Hold on, why are you thinking about her money? "
            " You've got your own, dumbass. "
            lz " That should be about 350$. "
            lz " Here you go, no complaints. "
            hide robbyneutral at bottom
            show robbyhappy at left
            rb " Woah, really? "
            rb " Thanks so much, Lizzy! "
            rb " (Never knew you could be this kind...) "
            lz " It's the least of what I could do. "
            lz " I know you work hard on these projects... "
            lz " Paying you is the only right choice here. "
            rb " Thans again, Liz... "
            rb " I really appreciate this. "
            lz " It's no problem. "
            lz " For a fact, I probably would've paid you more. "
            lz " But, my mom would get too mad at me for spending too much. "
            lz " Maybe next time, Robby. "
            rb " ...Maybe. "
            rb " I'll put your idea on my white board for sure. "
            rb " Thanks for not pressuring me, unlike for a certain someone... "
            lz " Artists need time. "
            lz " I have enough braincells to understand that. "
            scene black with dissolve
            " You spent the rest of the break talking with Lizzy and Robby. "
            " Talking about the whole project... "
            " You're wondering how the final thing is going to look like. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump historyclassfri
        elif popularknow == True and robbyknow == False:
            lz " Oh look, [name] is here. "
            x " ...Hi, [name]. "
            $ robbyknow = True
            rb " Oh, uh...I'm Robby. "
            rb " Me and Lizzy were just talking about a project we're planning to do. "
            lz " Yeah, just make a figure of me and Petunia. "
            lz " Of course, I don't want you to stress out over this thing getting done in a day. "
            lz " So...you can finish this whenever you're free. "
            lz " I'm not just gonna force you to finish it it in 1 second. "
            lz " That's quite literally impossible. "
            lz " So, you've got all the time in the world to make that thing. "
            lz " I don't mind if you take a year, a month... "
            lz " As long as you're all comfortable and not stressed out. "
            lz " Being stressed can make you burnt out, you know. "
            lz " And I heard that isn't a good thing. "
            lz " Apparently it makes you less motivated to do stuff. "
            rb " Yeah, you're right about that... "
            rb " But, just one problem. "
            rb " What if I forget about the project entirely? "
            lz " I don't care if you forget about the project, "
            lz " Just put it on like...a white board or something. "
            lz " You got one of those, right? "
            rb " Of course I do. "
            rb " That's where I list down all of my projects. "
            lz " Then you can put my project down there, so you won't forget. "
            lz " Do I have to pay you for this sort of thing? "
            rb " Well, no. "
            rb " I don't usually want to get paid. "
            rb " But, if you want to, then... "
            lz " Dude, just say that you want to get paid. "
            lz " You clearly don't get paid enough for Riley's bullshit. "
            lz " You know...whenever she asks you to make something. "
            rb " ...Yeah, I don't get paid enough. "
            rb " She doesn't pay me at all, unsurprisingly. "
            lz " Then I'll be sort of the first one to pay you for your works. "
            lz " Judging by how the final product will look... "
            " Lizzy reaches into her pocket for her wallet. "
            " You're starting to wonder a bit how much money she has... "
            " Hold on, why are you thinking about her money? "
            " You've got your own, dumbass. "
            lz " That should be about 350$. "
            lz " Here you go, no complaints. "
            hide robbyneutral at bottom
            show robbyhappy at left
            rb " Woah, really? "
            rb " Thanks so much, Lizzy! "
            rb " (Never knew you could be this kind...) "
            lz " It's the least of what I could do. "
            lz " I know you work hard on these projects... "
            lz " Paying you is the only right choice here. "
            rb " Thans again, Liz... "
            rb " I really appreciate this. "
            lz " It's no problem. "
            lz " For a fact, I probably would've paid you more. "
            lz " But, my mom would get too mad at me for spending too much. "
            lz " Maybe next time, Robby. "
            rb " ...Maybe. "
            rb " I'll put your idea on my white board for sure. "
            rb " Thanks for not pressuring me, unlike for a certain someone... "
            lz " Artists need time. "
            lz " I have enough braincells to understand that. "
            scene black with dissolve
            " You spent the rest of the break talking with Lizzy and Robby. "
            " Talking about the whole project... "
            " You're wondering how the final thing is going to look like. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump historyclassfri
        elif popularknow == False and robbyknow == True:
            x " Oh look, [name] is here. "
            rb " ...Hi, [name]. "
            $ popularknow = True
            rb " Me and Lizzy were just talking about a project we're planning to do. "
            lz " Yeah, just make a figure of me and Petunia. "
            lz " Of course, I don't want you to stress out over this thing getting done in a day. "
            lz " So...you can finish this whenever you're free. "
            lz " I'm not just gonna force you to finish it it in 1 second. "
            lz " That's quite literally impossible. "
            lz " So, you've got all the time in the world to make that thing. "
            lz " I don't mind if you take a year, a month... "
            lz " As long as you're all comfortable and not stressed out. "
            lz " Being stressed can make you burnt out, you know. "
            lz " And I heard that isn't a good thing. "
            lz " Apparently it makes you less motivated to do stuff. "
            rb " Yeah, you're right about that... "
            rb " But, just one problem. "
            rb " What if I forget about the project entirely? "
            lz " I don't care if you forget about the project, "
            lz " Just put it on like...a white board or something. "
            lz " You got one of those, right? "
            rb " Of course I do. "
            rb " That's where I list down all of my projects. "
            lz " Then you can put my project down there, so you won't forget. "
            lz " Do I have to pay you for this sort of thing? "
            rb " Well, no. "
            rb " I don't usually want to get paid. "
            rb " But, if you want to, then... "
            lz " Dude, just say that you want to get paid. "
            lz " You clearly don't get paid enough for Riley's bullshit. "
            lz " You know...whenever she asks you to make something. "
            rb " ...Yeah, I don't get paid enough. "
            rb " She doesn't pay me at all, unsurprisingly. "
            lz " Then I'll be sort of the first one to pay you for your works. "
            lz " Judging by how the final product will look... "
            " Lizzy reaches into her pocket for her wallet. "
            " You're starting to wonder a bit how much money she has... "
            " Hold on, why are you thinking about her money? "
            " You've got your own, dumbass. "
            lz " That should be about 350$. "
            lz " Here you go, no complaints. "
            hide robbyneutral at bottom
            show robbyhappy at left
            rb " Woah, really? "
            rb " Thanks so much, Lizzy! "
            rb " (Never knew you could be this kind...) "
            lz " It's the least of what I could do. "
            lz " I know you work hard on these projects... "
            lz " Paying you is the only right choice here. "
            rb " Thans again, Liz... "
            rb " I really appreciate this. "
            lz " It's no problem. "
            lz " For a fact, I probably would've paid you more. "
            lz " But, my mom would get too mad at me for spending too much. "
            lz " Maybe next time, Robby. "
            rb " ...Maybe. "
            rb " I'll put your idea on my white board for sure. "
            rb " Thanks for not pressuring me, unlike for a certain someone... "
            lz " Artists need time. "
            lz " I have enough braincells to understand that. "
            scene black with dissolve
            " You spent the rest of the break talking with Lizzy and Robby. "
            " Talking about the whole project... "
            " You're wondering how the final thing is going to look like. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump historyclassfri
        else:
            x " Oh look, [name] is here. "
            x " ...Hi, [name]. "
            $ robbyknow = True
            rb " Oh, uh...I'm Robby. "
            $ lizzyknow = True
            rb " Me and Lizzy were just talking about a project we're planning to do. "
            lz " Yeah, just make a figure of me and Petunia. "
            lz " Of course, I don't want you to stress out over this thing getting done in a day. "
            lz " So...you can finish this whenever you're free. "
            lz " I'm not just gonna force you to finish it it in 1 second. "
            lz " That's quite literally impossible. "
            lz " So, you've got all the time in the world to make that thing. "
            lz " I don't mind if you take a year, a month... "
            lz " As long as you're all comfortable and not stressed out. "
            lz " Being stressed can make you burnt out, you know. "
            lz " And I heard that isn't a good thing. "
            lz " Apparently it makes you less motivated to do stuff. "
            rb " Yeah, you're right about that... "
            rb " But, just one problem. "
            rb " What if I forget about the project entirely? "
            lz " I don't care if you forget about the project, "
            lz " Just put it on like...a white board or something. "
            lz " You got one of those, right? "
            rb " Of course I do. "
            rb " That's where I list down all of my projects. "
            lz " Then you can put my project down there, so you won't forget. "
            lz " Do I have to pay you for this sort of thing? "
            rb " Well, no. "
            rb " I don't usually want to get paid. "
            rb " But, if you want to, then... "
            lz " Dude, just say that you want to get paid. "
            lz " You clearly don't get paid enough for Riley's bullshit. "
            lz " You know...whenever she asks you to make something. "
            rb " ...Yeah, I don't get paid enough. "
            rb " She doesn't pay me at all, unsurprisingly. "
            lz " Then I'll be sort of the first one to pay you for your works. "
            lz " Judging by how the final product will look... "
            " Lizzy reaches into her pocket for her wallet. "
            " You're starting to wonder a bit how much money she has... "
            " Hold on, why are you thinking about her money? "
            " You've got your own, dumbass. "
            lz " That should be about 350$. "
            lz " Here you go, no complaints. "
            hide robbyneutral at bottom
            show robbyhappy at left
            rb " Woah, really? "
            rb " Thanks so much, Lizzy! "
            rb " (Never knew you could be this kind...) "
            lz " It's the least of what I could do. "
            lz " I know you work hard on these projects... "
            lz " Paying you is the only right choice here. "
            rb " Thans again, Liz... "
            rb " I really appreciate this. "
            lz " It's no problem. "
            lz " For a fact, I probably would've paid you more. "
            lz " But, my mom would get too mad at me for spending too much. "
            lz " Maybe next time, Robby. "
            rb " ...Maybe. "
            rb " I'll put your idea on my white board for sure. "
            rb " Thanks for not pressuring me, unlike for a certain someone... "
            lz " Artists need time. "
            lz " I have enough braincells to understand that. "
            scene black with dissolve
            " You spent the rest of the break talking with Lizzy and Robby. "
            " Talking about the whole project... "
            " You're wondering how the final thing is going to look like. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump historyclassfri
    label gymfri3:
        # abbie and ruby // not interact
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked into the gym and found two of your classmates doing their own things. "
        " Who do you want to talk to? "
        if abbieknow == True and rubyknow == True:
            menu:
                " {image=abbieicon} Abbie {image=abbieicon} ":
                    jump dualdependency
                " {image=rubyicon} Ruby {image=rubyicon} ":
                    jump lilly
        elif abbieknow == True and rubyknow == False:
            menu:
                " {image=abbieicon} Abbie {image=abbieicon} ":
                    jump dualdependency
                " {image=rubyicon} A girl that has a TV for a head {image=rubyicon} ":
                    jump lilly
        elif abbieknow == False and rubyknow == True:
            menu:
                " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                    jump dualdependency
                " {image=rubyicon} Ruby {image=rubyicon} ":
                    jump lilly
        else:
            menu:
                " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                    jump dualdependency
                " {image=rubyicon} A girl that has a TV for a head {image=rubyicon} ":
                    jump lilly
        label dualdependency:
            show abbieneutral at center with easeinleft
            if abbieknow == True:
                pause 0.1
                if abbielv >= 30 or abbielv == 30:
                    " You walked over to him and asked him if he was doing okay. "
                    " He looked a little down, and that got you a bit concerned... "
                    a " H...huh...? "
                    a " Oh, I'm fine... "
                    a " It's just that... "
                    a " I overhead that Oliver is coming after me this break... "
                    a " I'm not sure if I can really stand up for myself... "
                    a " Am I strong enough for this...? "
                    " You reassured him that he was probably going to be fine. "
                    " And if things don't go the right way, you'll step in. "
                    " You're going to be there for him. No matter what. "
                    a " ...You... "
                    hide abbieneutral at bottom
                    show abbiehappy at center
                    a " ...You're the best, [name]... "
                    a " Really, you are... "
                    a " I don't know how to thank you for everything that you've done for me... "
                    a " All I can do is... "
                    a " Give you a hug, if you're comfortable with that...? "
                    " You open up your arms for a hug. "
                    " Abbie gladly wraps his arms around you. "
                    " You feel very joyous at this moment. "
                    a " ...This feels really nice... "
                    hide abbiehappy at bottom
                    show abbieneutral at center
                    " You were just enjoying the moment, until you heard the gym doors bust open. "
                    " Uh oh. Sounds like Oliver. "
                    " Abbie immediately lets go of you and acts as if nothing happened. "
                    " ...You lowkey wanted to hug him a bit longer. "
                    " But now's not the time. "
                    a " ...Oh geez... "
                    show abbieneutral at right with move
                    show oliverneutral at left with easeinleft
                    o " Sup idiots. "
                    o " Don't act like I didn't see you two hugging and stuff. "
                    if they == "he":
                        o " That's kinda gay, bro. "
                    elif they == "she":
                        o " That's kinda straight, bro. "
                    elif they == "they":
                        o " Uh...that's kinda gay, I guess??? "
                        o " I don't know how your gender works. "
                        o " But like, I'm trying to be respectful here. "
                    else:
                        pass
                    o " Anyway, enough of that... "
                    hide oliverneutral at bottom
                    show oliverhappy at left
                    o " Me and my gang had some plans for you, Abbie!! "
                    a " Oh, um...really..? "
                    o " Yeah, some REAL fun plans. "
                    o " We're totally going to take you to disney world! "
                    a " ... (I very much doubt that.) "
                    o " No, no!! trust me on this one!! "
                    o " We're going to change our minds and we're gonna take you out to go there!! "
                    o " I'm sure [name] would like to go there too, right? "
                    " You don't feel like going out to disney world right now. "
                    " Maybe you'll go there sometime, but not right now. "
                    o " See, [name] really wants to go!! "
                    a " [they]...didn't say anything, though...? "
                    a " I don't think [they] want to go, sorry... "
                    o " ...O-kay. "
                    o " How about I just... "
                    o " Take your hand, and... "
                    " Oliver snatches Abbie's hand and quickly tries to drag him to the restroom. " with vpunch
                    hide abbieneutral at bottom
                    show abbiesad at right
                    a " ...Oliver...!! what are you doing...?! " with vpunch
                    o " I just need to talk to you privately, of course!! "
                    o " We've gotta talk about the whole plan for disney land!! "
                    hide oliverhappy at bottom
                    show oliverangry at left
                    o " In the restroom so that no one else your screams while I drown you in toilet water. "
                    o " You've always been a pain in my ass, Abbie. "
                    o " It's gonna be REAL great once you're gone from this world!! "
                    o " So stop struggling and let me do you a favor. "
                    o " You want to stop suffering, don't you? "
                    o " So why aren't you letting me end that right here and now? "
                    o " If this was you back then...you'd probably let me just drown you, won't you? "
                    o " I don't remember you being this strong to hold me back... "
                    o " The hell changed? "
                    o " This is stupid. I'm not backing down though. "
                    a " ...I... "
                    o " What, you saying something? "
                    o " Speak up so I can hear you clearly, loser. "
                    o " Then again, you never really spoke up for yourself. "
                    o " You just let people do whatever they want to you. "
                    o " So if you want to say something, it's probably not worth my time {nw} "
                    stop music
                    a " GET OFF OF ME!! " with vpunch
                    hide oliverangry at bottom
                    show oliverconcerned at left
                    hide oliverconcerned at bottom with easeoutbottom
                    " ...Abbie kicked him in the balls and now he's stomping on him. "
                    o " OW!!! OW!! OWW!! "
                    o " JESUS CHRIST, I DIDN'T KNOW YOU HAD THE BALLS TO DO THAT!! "
                    o " OWW!! MY PEEEEEEEEENISSSSSSSSSSSSSSSSSSSSS!!! "
                    o " OKAY, JEEZ! I'll leave you alone!! "
                    o " GOD DAMNED QUIET KIDS!! "
                    hide abbiesad at bottom
                    show abbieneutral at right
                    " And with that, Oliver skedaddled away. "
                    show abbieneutral at center with move
                    a " ...I can't believe I actually did that... "
                    a " There's no way... "
                    a " I.. "
                    hide abbieneutral at bottom
                    show abbiehappy at center
                    play music "audio/emotionalmoment.mp3" fadein 1.5
                    a " ...I actually did it!! "
                    a " I actually...managed to.. "
                    a " ...You have no idea how happy I am right now!! "
                    a " Though I do feel bad for hurting him... "
                    a " I'm happy that I managed to finally stand up for myself...!! "
                    a " You...[name]... "
                    a " You've taught me so much... "
                    a " I don't know how to thank you, really... "
                    a " ...I... "
                    a " I think you might be my bestest friend ever...! "
                    a " Um...would you be fine with...us being that...? "
                    a " You know...best friends...? "
                    menu:
                        " HELL YEAH!! ":
                            $ abbiesend.grant()
                            a " Really...? "
                            a " Yay, I'm so...I'm so happy...!! "
                            a " Let's...let's hang out more, okay...? "
                            a " Best friend... "
                            a " (I can't believe I've gotten this close with [them] for only a week...) "
                            a " (But, I can't help but be happy...!) "
                            a " (I've got a true friend by my side, how could I not be...!!!) "
                            a " (Things are going to be much brighter from now on...) "
                            scene abbieending with dissolve
                            " And with that, you became Abbie's best friend. "
                            " You've officially gotten his achievement, and more importantly, his ending! "
                            " Congratulations! Abbie is proud to have you as his friend... "
                            " ...Especially after all you've done for him. "
                            " Now you two can be strong in the real way! "
                            jump credits
                else:
                    " You walked over to him and asked him if he was doing alright. "
                    " He looked like he was looking for something... "
                    " Maybe you could help him out. "
                    a " Huh...? oh, [name]... "
                    a " I hope I'm not bothering you, but... "
                    a " I've recently lost this thing here... "
                    a " It's this yellow star keychain... "
                    a " It's important to me, because...well.. "
                    a " One of my friends gave it to me... "
                    a " So losing it is like a big mistake...well, to me at least... "
                    a " That keychain means a lot to me... "
                    a " It's also one of the only gifts I've gotten... "
                    a " ...That isn't from my family... "
                    a " Have you seen in anywhere...? "
                    a " I really don't want to lose it forever... "
                    a " That would just break my heart... "
                    " You told him that you didn't see anything like that. "
                    " Since it's a keychain, it would be small. "
                    " Of course you wouldn't see anything, "
                    " But, you were willing enough to help him look. "
                    a " Huh...? "
                    a " You want to help me...? "
                    a " Um...are you sure...? "
                    a " I don't want to be a btoher to you, after all... "
                    a " Besides, I think I can look for it on my own.. "
                    a " I {i}am{/i} the one who lost it, after all... "
                    a " You don't have to help if you don't feel like it... "
                    " You insisted on helping him. "
                    " You didn't want him to lose something THAT important to him... "
                    a " Okay...if you say so... "
                    a " I'll go look at this side of the gym, okay...? "
                    " You gave him a thumbs up before starting to look everywhere. "
                    scene black with dissolve
                    " You spent the rest of the break helping Abbie look for his keychain. "
                    " You eventually found it in the trash can and gave it back to Abbie, all cleaned up. "
                    " Someone must've put it there while he wasn't looking. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the gym and went to your classroom. "
                    pause 2.0
                    jump historyclassfri
            else:
                " You walked over to him and asked him if he was doing alright. "
                " He looked like he was looking for something... "
                " Maybe you could help him out. "
                x " Huh...? oh, [name]... "
                $ abbieknow = True
                x " Um, I don't think I've met you before, so... "
                a " I'm Abbie...i-it's nice to meet you... "
                a " Um... "
                a " I hope I'm not bothering you, but... "
                a " I've recently lost this thing here... "
                a " It's this yellow star keychain... "
                a " It's important to me, because...well.. "
                a " One of my friends gave it to me... "
                a " So losing it is like a big mistake...well, to me at least... "
                a " That keychain means a lot to me... "
                a " It's also one of the only gifts I've gotten... "
                a " ...That isn't from my family... "
                a " Have you seen in anywhere...? "
                a " I really don't want to lose it forever... "
                a " That would just break my heart... "
                " You told him that you didn't see anything like that. "
                " Since it's a keychain, it would be small. "
                " Of course you wouldn't see anything, "
                " But, you were willing enough to help him look. "
                a " Huh...? "
                a " You want to help me...? "
                a " Um...are you sure...? "
                a " I don't want to be a btoher to you, after all... "
                a " Besides, I think I can look for it on my own.. "
                a " I {i}am{/i} the one who lost it, after all... "
                a " You don't have to help if you don't feel like it... "
                " You insisted on helping him. "
                " You didn't want him to lose something THAT important to him... "
                a " Okay...if you say so... "
                a " I'll go look at this side of the gym, okay...? "
                " You gave him a thumbs up before starting to look everywhere. "
                scene black with dissolve
                " You spent the rest of the break helping Abbie look for his keychain. "
                " You eventually found it in the trash can and gave it back to Abbie, all cleaned up. "
                " Someone must've put it there while he wasn't looking. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom. "
                pause 2.0
                jump historyclassfri
            # abbie's ending reminder, if mc doesnt have enough lv abbie will talk normally
            # if mc does have enough lv then oliver comes to bully and blablabla ending stuff
        label lilly:
            show rubyneutral at center with easeinright
            if rubyknow == True:
                " You walked over to her and asked her what she was doing. "
                " Now that you look at her more closely, you can pretty much tell what she was doing. "
                " She was trying to clean up a spot on her screen... "
                ru " Hi there, [name]!! "
                ru " You're wondering what I'm doing, huh? "
                ru " Well...you see... "
                hide rubyneutral at bottom
                show rubyangry at center
                ru " Oliver decided to...do a little prank on me... "
                ru " And he...(*aggressive wiping*) "
                ru " His dumbass... "
                ru " Decided to put glue on my screen...!! "
                ru " And he prevented me from getting anything to clean it up... "
                ru " So it started to dry a bit and now.. "
                ru " NOW I'm struggling to get it off!! "
                ru " Jesus christ... "
                ru " I never knew that glue could be this annnoying to get rid of! "
                " ...You're trying to hold back so many jokes right now. "
                " You can't say anything though. "
                " I know what you're thinking right now. "
                " You are NOT slick. "
                " If you're not thinking of making any jokes right now, good for you. "
                ru " Jeez... "
                ru " I really don't want to go to history like this...!! "
                ru " So...annoying... "
                ru " GUHHH!! Can't this just get off of my screen already?! "
                ru " I won't be able to see things properly!! "
                ru " And this is why I hate Oliver so much... "
                ru " The guy NEVER gives me a break. "
                ru " Well, he never does give anyone a break, but... "
                ru " It's still so annoying to deal with him! "
                ru " God... "
                ru " [name], you think you can help me here? "
                ru " You don't have to, but... "
                ru " I kind of need a hand right now. "
                menu:
                    " Help Ruby ":
                        $ rubylv += 10
                        hide rubyangry at bottom
                        show rubyneutral at center
                        ru " Whew...thanks! "
                        ru " I can feel my robot hand hurting, haha... "
                        ru " I want you to wipe all the glue away, alright? "
                        ru " And wipe it hard! "
                        ru " I've been trying my best to wipe it, but... "
                        ru " It just won't come off! "
                        ru " Just don't wipe it too hard to the point my screen breaks, okay? "
                        ru " This thing costs a lot, you know! "
                        scene black with dissolve
                        " You spent the rest of the break helping Ruby get the glue off her screen. "
                        " Damn, she was right. This glue was TOUGH. "
                        " You eventually got all of it off her screen though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the gym and went to your classroom. "
                        pause 2.0
                        jump historyclassfri
                    " I've got things to do ":
                        hide rubyangry at bottom
                        show rubyneutral at center
                        ru " Oh, you got somewhere to go? "
                        ru " That's fine! "
                        ru " I'll just be here... "
                        ru " Trying to get this glue off of my screen... "
                        ru " Come back if you need anything from me!! "
                        scene black with dissolve
                        " You spent the rest of the break wandering around the school. "
                        " You didn't really see anything interesting happen... "
                        " You just continued to walk around and scroll on your favorite app. "
                        " Pretty sure you know what it is at this point. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You walked over to your classroom after a bit. "
                        pause 2.0
                        jump historyclassfri
            else:
                " You walked over to her and asked her what she was doing. "
                " Now that you look at her more closely, you can pretty much tell what she was doing. "
                " She was trying to clean up a spot on her screen... "
                x " Hi there, [name]!! "
                $ rubyknow = True
                ru " I'm Ruby, by the way! Nice to meet you! "
                ru " You're wondering what I'm doing, huh? "
                ru " Well...you see... "
                hide rubyneutral at bottom
                show rubyangry at center
                ru " Oliver decided to...do a little prank on me... "
                ru " And he...(*aggressive wiping*) "
                ru " His dumbass... "
                ru " Decided to put glue on my screen...!! "
                ru " And he prevented me from getting anything to clean it up... "
                ru " So it started to dry a bit and now.. "
                ru " NOW I'm struggling to get it off!! "
                ru " Jesus christ... "
                ru " I never knew that glue could be this annnoying to get rid of! "
                " ...You're trying to hold back so many jokes right now. "
                " You can't say anything though. "
                " I know what you're thinking right now. "
                " You are NOT slick. "
                " If you're not thinking of making any jokes right now, good for you. "
                ru " Jeez... "
                ru " I really don't want to go to history like this...!! "
                ru " So...annoying... "
                ru " GUHHH!! Can't this just get off of my screen already?! "
                ru " I won't be able to see things properly!! "
                ru " And this is why I hate Oliver so much... "
                ru " The guy NEVER gives me a break. "
                ru " Well, he never does give anyone a break, but... "
                ru " It's still so annoying to deal with him! "
                ru " God... "
                ru " [name], you think you can help me here? "
                ru " You don't have to, but... "
                ru " I kind of need a hand right now. "
                menu:
                    " Help Ruby ":
                        $ rubylv += 10
                        hide rubyangry at bottom
                        show rubyneutral at center
                        ru " Whew...thanks! "
                        ru " I can feel my robot hand hurting, haha... "
                        ru " I want you to wipe all the glue away, alright? "
                        ru " And wipe it hard! "
                        ru " I've been trying my best to wipe it, but... "
                        ru " It just won't come off! "
                        ru " Just don't wipe it too hard to the point my screen breaks, okay? "
                        ru " This thing costs a lot, you know! "
                        scene black with dissolve
                        " You spent the rest of the break helping Ruby get the glue off her screen. "
                        " Damn, she was right. This glue was TOUGH. "
                        " You eventually got all of it off her screen though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the gym and went to your classroom. "
                        pause 2.0
                        jump historyclassfri
                    " I've got things to do ":
                        hide rubyangry at bottom
                        show rubyneutral at center
                        ru " Oh, you got somewhere to go? "
                        ru " That's fine! "
                        ru " I'll just be here... "
                        ru " Trying to get this glue off of my screen... "
                        ru " Come back if you need anything from me!! "
                        scene black with dissolve
                        " You spent the rest of the break wandering around the school. "
                        " You didn't really see anything interesting happen... "
                        " You just continued to walk around and scroll on your favorite app. "
                        " Pretty sure you know what it is at this point. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You walked over to your classroom after a bit. "
                        pause 2.0
                        jump historyclassfri
    label cafeteriafri3:
        # riley and lana // interact
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked into the cafeteria and spotted two of your classmates talking. "
        " Wondering what they're talking about, you decided to sit next to them and join their conversation. "
        show rileyneutral at right with easeinleft
        show lananeutral at left with easeinleft
        if rileyknow == True and lanaknow == True:
            l " Hiya there, [name]!! "
            ri " Oh, whaaat? [name]'s here? "
            ri " Cool coo! Hi there!! "
            ri " I was just talking about Oliver to Lana over here!! "
            ri " He's just the coolest, isn't he...?! "
            l " Uh, yeah...! Cool! "
            l " (Psst, [name]?) "
            l " (Being honest here, but...) "
            l " (I've actually been trying to get Riley away from me for awhile now.) "
            l " (She just came up to me earlier and uh...) "
            l " (Now I can't get her to stop talking about Oliver.) "
            l " (Well, if they can't leave you alone...) "
            l " (Might as well join them, right?) "
            l " (Not like she's that much of a problem now, anyway...) "
            l " Hey, Riley! "
            ri " Huh? what, what? "
            ri " You got a sweet idea for me? "
            l " You bet I do! "
            l " Okay, so I know you love Oliver very much... "
            ri " I'm already liking where this is going! "
            ri " Tell me more, Lana! "
            " Okay, you have a feeling this idea was either good or bad. "
            " Probably a mix of both. Probably. "
            l " How about... "
            l " We make sock puppets of you and Oliver? "
            l " You get to design Oliver's puppet, of course! "
            l " With your sock puppets, you can act out your thoughts! "
            l " You can also roleplay with them and think it's real! "
            l " Isn't that a great idea, Riley? "
            ri " Oh, I'm SO DOWN FOR THAT. "
            ri " I like that you're making me design Oliver, too! "
            ri " I was actually thinking of saying that I should design Oliver!! "
            ri " It's like you know what I'm thinking about!! "
            ri " You know me soooo well!! "
            ri " Even though we don't talk too much!! "
            l " Hehe, yeah! "
            l " Here's your decorations by the way... "
            l " ...And the sock you're going to decorate! "
            l " If you need more stuff, you can tell me! "
            l " I've got a lot of decorations in this bag. "
            ri " Woahz!! "
            ri " You're really awesome, Lana!! "
            ri " Maybe I should start asking you to make projects for me more... "
            l " Yeah, that sounds great!! "
            l " ...Hold on, what did you say? "
            ri " Nothing!! "
            l " ...Okay...? "
            scene black with dissolve
            " You spent the rest of the break watching Lana and Riley make sock puppets. "
            " You thought letting Riley make a sock puppet based off of Oliver was bad, but... "
            " You can't really stop her now. They're already making him. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump historyclassfri
        elif rileyknow == True and lanaknow == False:
            x " Hiya there, [name]!! "
            ri " Oh, whaaat? [name]'s here? "
            ri " Cool coo! Hi there!! "
            ri " I was just talking about Oliver to Lana over here!! "
            ri " He's just the coolest, isn't he...?! "
            x " Uh, yeah...! Cool! "
            x " (Psst, [name]?) "
            x " (Before I say anything else, lemme introduce myself...) "
            $ lanaknow = True
            l " (I'm Lana! one of your classmates! and, uh...) "
            l " (Being honest here, but...) "
            l " (I've actually been trying to get Riley away from me for awhile now.) "
            l " (She just came up to me earlier and uh...) "
            l " (Now I can't get her to stop talking about Oliver.) "
            l " (Well, if they can't leave you alone...) "
            l " (Might as well join them, right?) "
            l " (Not like she's that much of a problem now, anyway...) "
            l " Hey, Riley! "
            ri " Huh? what, what? "
            ri " You got a sweet idea for me? "
            l " You bet I do! "
            l " Okay, so I know you love Oliver very much... "
            ri " I'm already liking where this is going! "
            ri " Tell me more, Lana! "
            " Okay, you have a feeling this idea was either good or bad. "
            " Probably a mix of both. Probably. "
            l " How about... "
            l " We make sock puppets of you and Oliver? "
            l " You get to design Oliver's puppet, of course! "
            l " With your sock puppets, you can act out your thoughts! "
            l " You can also roleplay with them and think it's real! "
            l " Isn't that a great idea, Riley? "
            ri " Oh, I'm SO DOWN FOR THAT. "
            ri " I like that you're making me design Oliver, too! "
            ri " I was actually thinking of saying that I should design Oliver!! "
            ri " It's like you know what I'm thinking about!! "
            ri " You know me soooo well!! "
            ri " Even though we don't talk too much!! "
            l " Hehe, yeah! "
            l " Here's your decorations by the way... "
            l " ...And the sock you're going to decorate! "
            l " If you need more stuff, you can tell me! "
            l " I've got a lot of decorations in this bag. "
            ri " Woahz!! "
            ri " You're really awesome, Lana!! "
            ri " Maybe I should start asking you to make projects for me more... "
            l " Yeah, that sounds great!! "
            l " ...Hold on, what did you say? "
            ri " Nothing!! "
            l " ...Okay...? "
            scene black with dissolve
            " You spent the rest of the break watching Lana and Riley make sock puppets. "
            " You thought letting Riley make a sock puppet based off of Oliver was bad, but... "
            " You can't really stop her now. They're already making him. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump historyclassfri
        elif rileyknow == False and lanaknow == True:
            l " Hiya there, [name]!! "
            x " Oh, whaaat? [name]'s here? "
            x " Cool coo! Hi there!! "
            $ rileyknow = True
            ri " I'm Riley, by the way!! nice to meet you!! "
            ri " I was just talking about Oliver to Lana over here!! "
            ri " He's just the coolest, isn't he...?! "
            l " Uh, yeah...! Cool! "
            l " (Psst, [name]?) "
            l " (Being honest here, but...) "
            l " (I've actually been trying to get Riley away from me for awhile now.) "
            l " (She just came up to me earlier and uh...) "
            l " (Now I can't get her to stop talking about Oliver.) "
            l " (Well, if they can't leave you alone...) "
            l " (Might as well join them, right?) "
            l " (Not like she's that much of a problem now, anyway...) "
            l " Hey, Riley! "
            ri " Huh? what, what? "
            ri " You got a sweet idea for me? "
            l " You bet I do! "
            l " Okay, so I know you love Oliver very much... "
            ri " I'm already liking where this is going! "
            ri " Tell me more, Lana! "
            " Okay, you have a feeling this idea was either good or bad. "
            " Probably a mix of both. Probably. "
            l " How about... "
            l " We make sock puppets of you and Oliver? "
            l " You get to design Oliver's puppet, of course! "
            l " With your sock puppets, you can act out your thoughts! "
            l " You can also roleplay with them and think it's real! "
            l " Isn't that a great idea, Riley? "
            ri " Oh, I'm SO DOWN FOR THAT. "
            ri " I like that you're making me design Oliver, too! "
            ri " I was actually thinking of saying that I should design Oliver!! "
            ri " It's like you know what I'm thinking about!! "
            ri " You know me soooo well!! "
            ri " Even though we don't talk too much!! "
            l " Hehe, yeah! "
            l " Here's your decorations by the way... "
            l " ...And the sock you're going to decorate! "
            l " If you need more stuff, you can tell me! "
            l " I've got a lot of decorations in this bag. "
            ri " Woahz!! "
            ri " You're really awesome, Lana!! "
            ri " Maybe I should start asking you to make projects for me more... "
            l " Yeah, that sounds great!! "
            l " ...Hold on, what did you say? "
            ri " Nothing!! "
            l " ...Okay...? "
            scene black with dissolve
            " You spent the rest of the break watching Lana and Riley make sock puppets. "
            " You thought letting Riley make a sock puppet based off of Oliver was bad, but... "
            " You can't really stop her now. They're already making him. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump historyclassfri
        else:
            x " Hiya there, [name]!! "
            x " Oh, whaaat? [name]'s here? "
            x " Cool coo! Hi there!! "
            $ rileyknow = True
            ri " I'm Riley, by the wayyy!! "
            ri " I was just talking about Oliver to Lana over here!! "
            ri " He's just the coolest, isn't he...?! "
            x " Uh, yeah...! Cool! "
            x " (Psst, [name]?) "
            x " (Before I say anything else, lemme introduce myself...) "
            $ lanaknow = True
            l " (I'm Lana! one of your classmates! and, uh...) "
            l " (Being honest here, but...) "
            l " (I've actually been trying to get Riley away from me for awhile now.) "
            l " (She just came up to me earlier and uh...) "
            l " (Now I can't get her to stop talking about Oliver.) "
            l " (Well, if they can't leave you alone...) "
            l " (Might as well join them, right?) "
            l " (Not like she's that much of a problem now, anyway...) "
            l " Hey, Riley! "
            ri " Huh? what, what? "
            ri " You got a sweet idea for me? "
            l " You bet I do! "
            l " Okay, so I know you love Oliver very much... "
            ri " I'm already liking where this is going! "
            ri " Tell me more, Lana! "
            " Okay, you have a feeling this idea was either good or bad. "
            " Probably a mix of both. Probably. "
            l " How about... "
            l " We make sock puppets of you and Oliver? "
            l " You get to design Oliver's puppet, of course! "
            l " With your sock puppets, you can act out your thoughts! "
            l " You can also roleplay with them and think it's real! "
            l " Isn't that a great idea, Riley? "
            ri " Oh, I'm SO DOWN FOR THAT. "
            ri " I like that you're making me design Oliver, too! "
            ri " I was actually thinking of saying that I should design Oliver!! "
            ri " It's like you know what I'm thinking about!! "
            ri " You know me soooo well!! "
            ri " Even though we don't talk too much!! "
            l " Hehe, yeah! "
            l " Here's your decorations by the way... "
            l " ...And the sock you're going to decorate! "
            l " If you need more stuff, you can tell me! "
            l " I've got a lot of decorations in this bag. "
            ri " Woahz!! "
            ri " You're really awesome, Lana!! "
            ri " Maybe I should start asking you to make projects for me more... "
            l " Yeah, that sounds great!! "
            l " ...Hold on, what did you say? "
            ri " Nothing!! "
            l " ...Okay...? "
            scene black with dissolve
            " You spent the rest of the break watching Lana and Riley make sock puppets. "
            " You thought letting Riley make a sock puppet based off of Oliver was bad, but... "
            " You can't really stop her now. They're already making him. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump historyclassfri
    label rooftopfri3:
        # claire and skell // not interact
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        if clairebeatup == True:
            " Oops, can't talk, sorry. "
            " You know exactly why. "
            scene black
            pause 2.0
            jump historyclassfri
        else:
            pass
        " You walked to the rooftop and spotted two of your classmates doing their own things. "
        " Who do you want to talk to? "
        if claireknow == True and skellknow == True:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    jump crystalgravity
                " {image=skellicon} Skell {image=skellicon} ":
                    jump paperwitch
        elif claireknow == True and skellknow == False:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    jump crystalgravity
                " {image=skellicon} An emo guy {image=skellicon} ":
                    jump paperwitch
        elif claireknow == False and skellknow == True:
            menu:
                " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                    jump crystalgravity
                " {image=skellicon} Skell {image=skellicon} ":
                    jump paperwitch
        else:
            menu:
                " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                    jump crystalgravity
                " {image=skellicon} An emo guy {image=skellicon} ":
                    jump paperwitch
        label crystalgravity:
            show claireneutral at center with easeinleft
            if claireknow == True:
                " You walked over to her and asked what she was doing. "
                c " Hm? oh hey there, [name]! "
                c " I just came up here to get some nice fresh air... "
                c " And also to take a break from my phone, hehe. "
                c " You know... "
                c " Sorry if I get a little real here, but... "
                c " I just gotta let a few things out, hehe. "
                c " Sometimes it feels like we don't appreciate nature a lot! "
                c " I mean, sure there's some people who appreciate it, but... "
                c " Most of the time, we just walk pass it - "
                c " ...Since we're so busy doing our own thing... "
                c " And the more we get busy... "
                c " The more we kinda just forget to relax. "
                c " We don't get to remember the feeling of what relaxing was because of how busy we are. "
                c " So much work to do... "
                c " ...And so little time to rest... "
                c " It feels unfair, but we can't do anything to change that. "
                c " And after we're done working... "
                c " We either go on our phones or actually look at nature! "
                c " Well...most people would go on the phone. But... "
                c " We gotta learn that sometimes we have to appreciate the things in life - "
                c " Like nature...friends...family... "
                c " We don't have to keep pushing ourselves to work the best we can. "
                c " We have to remind ourselves that we need breaks sometimes. "
                c " We can't just keep working - that's just going to stress us out even more! "
                c " And eventually...we're going to stress ourselves out to the point that... "
                c " We're going to feel burnt out. "
                c " And really, really tired... "
                c " It's really sad that people won't let other people have breaks nowadays. "
                c " Like, hello? we're humans, not robots. "
                c " I know your company is big and all but we need to rest sometime. "
                c " Gosh... "
                c " Companies are ridiculous. "
                c " Again - sorry if I got too real here. "
                c " Just needed to let a few things out. "
                c " Hmhmmm... "
                c " I like relaxing like this, you know? "
                c " A nice break from all the school work I have to do, haha. "
                c " I can get even more of a break since it's a saturday tomorrow. "
                c " I could go for some jogging tomorrow... "
                c " Or do my work. "
                c " But I think I'll let myself relax first before doing all that. "
                c " Gotta put myself before anything, after all. "
                c " Anyway...how was your day today? "
                scene black with dissolve
                " You spent the rest of the break talking with Claire. "
                " Just talking about stuff like... "
                " ...The pretty stuff in nature. "
                " Very interesting to be talking to her like this. "
                " And also relaxing. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walkeddown from the rooftop and went to your classroom. "
                pause 2.0
                jump historyclassfri
            else:
                " You walked over to her and asked what she was doing. "
                x " Hm? oh hey there, [name]! "
                x " I just came up here to get some nice fresh air... "
                x " And also to take a break from my phone, hehe. "
                $ claireknow = True
                c " I'm Claire, by the way! nice to meet you! "
                " She stays silent for a bit, before she spoke up again. "
                c " You know... "
                c " Sorry if I get a little real here, but... "
                c " I just gotta let a few things out, hehe. "
                c " Sometimes it feels like we don't appreciate nature a lot! "
                c " I mean, sure there's some people who appreciate it, but... "
                c " Most of the time, we just walk pass it - "
                c " ...Since we're so busy doing our own thing... "
                c " And the more we get busy... "
                c " The more we kinda just forget to relax. "
                c " We don't get to remember the feeling of what relaxing was because of how busy we are. "
                c " So much work to do... "
                c " ...And so little time to rest... "
                c " It feels unfair, but we can't do anything to change that. "
                c " And after we're done working... "
                c " We either go on our phones or actually look at nature! "
                c " Well...most people would go on the phone. But... "
                c " We gotta learn that sometimes we have to appreciate the things in life - "
                c " Like nature...friends...family... "
                c " We don't have to keep pushing ourselves to work the best we can. "
                c " We have to remind ourselves that we need breaks sometimes. "
                c " We can't just keep working - that's just going to stress us out even more! "
                c " And eventually...we're going to stress ourselves out to the point that... "
                c " We're going to feel burnt out. "
                c " And really, really tired... "
                c " It's really sad that people won't let other people have breaks nowadays. "
                c " Like, hello? we're humans, not robots. "
                c " I know your company is big and all but we need to rest sometime. "
                c " Gosh... "
                c " Companies are ridiculous. "
                c " Again - sorry if I got too real here. "
                c " Just needed to let a few things out. "
                c " Hmhmmm... "
                c " I like relaxing like this, you know? "
                c " A nice break from all the school work I have to do, haha. "
                c " I can get even more of a break since it's a saturday tomorrow. "
                c " I could go for some jogging tomorrow... "
                c " Or do my work. "
                c " But I think I'll let myself relax first before doing all that. "
                c " Gotta put myself before anything, after all. "
                c " Anyway...how was your day today? "
                scene black with dissolve
                " You spent the rest of the break talking with Claire. "
                " Just talking about stuff like... "
                " ...The pretty stuff in nature. "
                " Very interesting to be talking to her like this. "
                " And also relaxing. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walkeddown from the rooftop and went to your classroom. "
                pause 2.0
                jump historyclassfri
        label paperwitch:
            show skellneutral at center with easeinright
            if skellknow == True:
                " You walked over to him and asked him what he was doing. "
                sk " Oh - hi [name]. "
                sk " Just came up here to chill. "
                sk " And play some games, most likely. "
                sk " I haven't been finding any good games lately though... "
                sk " It's all just been brainrot slop. "
                hide skellneutral at bottom
                show skellangry at center
                sk " And I do NOT like brainrot slop. "
                sk " Everyday I open the fucking playstore... "
                sk " It's like all just waiting for me in there... "
                sk " ...Eugh. "
                sk " Seriously, who actually enjoys that content and is a grown adult? "
                sk " I'm about to be really concerned if someone's actually into this stuff. "
                sk " What do you mean you're 21 and are into skibidi toilet? "
                sk " I'd start reccomending to find help. "
                sk " People under the age of 10 should be the only ones playing these... "
                sk " Not grown adults. You're mature and old, come on. "
                sk " Don't care if you like it - you need to learn to grow up. "
                sk " Geez...so sick and tired of seeing these. "
                sk " Wonder who even created those things in the first place. "
                sk " Starting to really not like them. "
                sk " Even though I don't know them. "
                hide skellangry at bottom
                show skellneutral at center
                sk " Other than that... "
                sk " I think it's kind of unfair that the good games are always underrated. "
                sk " It always feels like I'm the only person in the fandom, you know? "
                sk " And it always feels so lonely. "
                sk " Like, come onnn...start giving this good piece of art attention!! "
                sk " Then again...fame to it can either be a good or a bad thing. "
                sk " On one hand - it's finally getting the recognition it deserves. "
                sk " It's got fans, fanart - everything a fandom could want. "
                sk " But then there's the bad side of a fandom. "
                sk " Of course every fandom has a bad side too it - not everything is pure and happy. "
                sk " No matter how hard you try, it'll always have a toxic side. "
                sk " So, sometimes... "
                sk " I think it's just better to have a fandom be unknown. "
                sk " If you don't want toxicity coming out, of course. "
                sk " Being a creator for a fandom is a huge responsibility... "
                sk " You have to make the right choices and say the right words. "
                sk " Otherwise, you're going to get bombarded with threats. "
                sk " Guh...now that I think about it... "
                sk " Creators have to deal with so much, jeez. "
                sk " Like imagine having to deal with angry fans just for forgetting something. "
                sk " God, that must be horrible. "
                sk " Sighhhh... "
                scene black with dissolve
                " You spent the rest of the break talking to Skell about fandoms. "
                " And honestly? all of his words were so true. "
                " It's just unfortunate that people have to deal with toxicity like that. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump historyclassfri
            else:
                " You walked over to him and asked him what he was doing. "
                x " Oh - hi [name]. "
                $ skellknow = True
                sk " I'm SKell, by the way. "
                sk " Just came up here to chill. "
                sk " And play some games, most likely. "
                sk " I haven't been finding any good games lately though... "
                sk " It's all just been brainrot slop. "
                hide skellneutral at bottom
                show skellangry at center
                sk " And I do NOT like brainrot slop. "
                sk " Everyday I open the fucking playstore... "
                sk " It's like all just waiting for me in there... "
                sk " ...Eugh. "
                sk " Seriously, who actually enjoys that content and is a grown adult? "
                sk " I'm about to be really concerned if someone's actually into this stuff. "
                sk " What do you mean you're 21 and are into skibidi toilet? "
                sk " I'd start reccomending to find help. "
                sk " People under the age of 10 should be the only ones playing these... "
                sk " Not grown adults. You're mature and old, come on. "
                sk " Don't care if you like it - you need to learn to grow up. "
                sk " Geez...so sick and tired of seeing these. "
                sk " Wonder who even created those things in the first place. "
                sk " Starting to really not like them. "
                sk " Even though I don't know them. "
                hide skellangry at bottom
                show skellneutral at center
                sk " Other than that... "
                sk " I think it's kind of unfair that the good games are always underrated. "
                sk " It always feels like I'm the only person in the fandom, you know? "
                sk " And it always feels so lonely. "
                sk " Like, come onnn...start giving this good piece of art attention!! "
                sk " Then again...fame to it can either be a good or a bad thing. "
                sk " On one hand - it's finally getting the recognition it deserves. "
                sk " It's got fans, fanart - everything a fandom could want. "
                sk " But then there's the bad side of a fandom. "
                sk " Of course every fandom has a bad side too it - not everything is pure and happy. "
                sk " No matter how hard you try, it'll always have a toxic side. "
                sk " So, sometimes... "
                sk " I think it's just better to have a fandom be unknown. "
                sk " If you don't want toxicity coming out, of course. "
                sk " Being a creator for a fandom is a huge responsibility... "
                sk " You have to make the right choices and say the right words. "
                sk " Otherwise, you're going to get bombarded with threats. "
                sk " Guh...now that I think about it... "
                sk " Creators have to deal with so much, jeez. "
                sk " Like imagine having to deal with angry fans just for forgetting something. "
                sk " God, that must be horrible. "
                sk " Sighhhh... "
                scene black with dissolve
                " You spent the rest of the break talking to Skell about fandoms. "
                " And honestly? all of his words were so true. "
                " It's just unfortunate that people have to deal with toxicity like that. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump historyclassfri
    label libraryfri3:
        # cubbie and engel // interact
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked into the library and found two of your classmates talking with eachother. "
        " Wondering what they're up to, you decided to talk with them. "
        show engelneutral at left with easeinright
        show cubbieneutral at right with easeinright
        if engelknow == True and cubbieknow == True:
            " You walked over to them and asked them what they were doing. "
            e " Hey there, [name]. "
            e " I'm just helping Cubbie sort out some books over here. "
            cb " ... "
            " The cat guy politely waves at you. "
            e " The teachers just asked us to sort some books, since... "
            e " There's just some books that the old librarian forgot to put in. "
            e " And by some...I mean a lot. "
            e " I mean - take a look at the basket we have here. "
            cb " ... "
            " Cubbie pointed over to the basket filled with books. "
            " You took a good look, and...yup. "
            " There sure was a lot of books that were there. "
            " You even saw some old books that used to be popular. "
            " Huh. They're THAT old. "
            e " This is gonna take us longer than just one break, I bet... "
            e " Even with two people working on this. "
            e " I don't mind working, but... "
            e " I don't want to work for the entire school day, you get me? "
            cb " ... "
            " Cubbie does a little nod of agreement. "
            " Honestly, you didn't want to work for an entire break, too. "
            " Working for that long is honestly just really painful. "
            e " It's also a little hard sorting things out. "
            e " For example: I've got a romance book here. "
            e " I have to read a few pages and turns out, it's actually a horror book. "
            e " I'm already at the romance section, so I have to go alll the way to the horror section... "
            e " Which is over at the left side of the library. "
            e " Great, isn't it? "
            cb " ... "
            " Yeah, no...that's just... "
            " That's just really annoying, at that point. "
            e " So we have to go back and forth every time we get a genre wrong... "
            e " It's honestly a bit tiring for me. "
            e " Actually, now that you're here... "
            e " I was wondering if you could help us. "
            e " With three people, things could be faster around here. "
            cb " ... "
            e " Right, Cubbie - "
            e " We also don't want to force you into this. "
            e " So...what do you say? "
            " You pretty much have nothing to do for this break, so... "
            " You agreed on helping them. "
            e " Nice, nice... "
            e " Just start by picking out some books from the basket. "
            e " Then, you can go and find their respective sections. "
            e " That DOES mean you have to walk around the library though. "
            e " ...A lot. "
            e " But I'm sure you don't mind. "
            " You gave him a thumbs up before starting to work. "
            scene black with dissolve
            " You spent the rest of the break helping Engel and Cubbie. "
            " And honestly? you were feeling their pain. "
            " You encountered some of the problems they had. But, you eventually got everything done. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump historyclassfri
        elif engelknow == True and cubbieknow == False:
            " You walked over to them and asked them what they were doing. "
            e " Hey there, [name]. "
            $ cubbieknow = True
            e " I'm just helping Cubbie sort out some books over here. "
            cb " ... "
            " The cat guy politely waves at you. "
            e " The teachers just asked us to sort some books, since... "
            e " There's just some books that the old librarian forgot to put in. "
            e " And by some...I mean a lot. "
            e " I mean - take a look at the basket we have here. "
            cb " ... "
            " Cubbie pointed over to the basket filled with books. "
            " You took a good look, and...yup. "
            " There sure was a lot of books that were there. "
            " You even saw some old books that used to be popular. "
            " Huh. They're THAT old. "
            e " This is gonna take us longer than just one break, I bet... "
            e " Even with two people working on this. "
            e " I don't mind working, but... "
            e " I don't want to work for the entire school day, you get me? "
            cb " ... "
            " Cubbie does a little nod of agreement. "
            " Honestly, you didn't want to work for an entire break, too. "
            " Working for that long is honestly just really painful. "
            e " It's also a little hard sorting things out. "
            e " For example: I've got a romance book here. "
            e " I have to read a few pages and turns out, it's actually a horror book. "
            e " I'm already at the romance section, so I have to go alll the way to the horror section... "
            e " Which is over at the left side of the library. "
            e " Great, isn't it? "
            cb " ... "
            " Yeah, no...that's just... "
            " That's just really annoying, at that point. "
            e " So we have to go back and forth every time we get a genre wrong... "
            e " It's honestly a bit tiring for me. "
            e " Actually, now that you're here... "
            e " I was wondering if you could help us. "
            e " With three people, things could be faster around here. "
            cb " ... "
            e " Right, Cubbie - "
            e " We also don't want to force you into this. "
            e " So...what do you say? "
            " You pretty much have nothing to do for this break, so... "
            " You agreed on helping them. "
            e " Nice, nice... "
            e " Just start by picking out some books from the basket. "
            e " Then, you can go and find their respective sections. "
            e " That DOES mean you have to walk around the library though. "
            e " ...A lot. "
            e " But I'm sure you don't mind. "
            " You gave him a thumbs up before starting to work. "
            scene black with dissolve
            " You spent the rest of the break helping Engel and Cubbie. "
            " And honestly? you were feeling their pain. "
            " You encountered some of the problems they had. But, you eventually got everything done. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump historyclassfri
        elif engelknow == False and cubbieknow == True:
            " You walked over to them and asked them what they were doing. "
            x " Hey there, [name]. "
            $ engelknow = True
            e " I'm Engel, and... "
            e " I'm just helping Cubbie sort out some books over here. "
            cb " ... "
            " The cat guy politely waves at you. "
            e " The teachers just asked us to sort some books, since... "
            e " There's just some books that the old librarian forgot to put in. "
            e " And by some...I mean a lot. "
            e " I mean - take a look at the basket we have here. "
            cb " ... "
            " Cubbie pointed over to the basket filled with books. "
            " You took a good look, and...yup. "
            " There sure was a lot of books that were there. "
            " You even saw some old books that used to be popular. "
            " Huh. They're THAT old. "
            e " This is gonna take us longer than just one break, I bet... "
            e " Even with two people working on this. "
            e " I don't mind working, but... "
            e " I don't want to work for the entire school day, you get me? "
            cb " ... "
            " Cubbie does a little nod of agreement. "
            " Honestly, you didn't want to work for an entire break, too. "
            " Working for that long is honestly just really painful. "
            e " It's also a little hard sorting things out. "
            e " For example: I've got a romance book here. "
            e " I have to read a few pages and turns out, it's actually a horror book. "
            e " I'm already at the romance section, so I have to go alll the way to the horror section... "
            e " Which is over at the left side of the library. "
            e " Great, isn't it? "
            cb " ... "
            " Yeah, no...that's just... "
            " That's just really annoying, at that point. "
            e " So we have to go back and forth every time we get a genre wrong... "
            e " It's honestly a bit tiring for me. "
            e " Actually, now that you're here... "
            e " I was wondering if you could help us. "
            e " With three people, things could be faster around here. "
            cb " ... "
            e " Right, Cubbie - "
            e " We also don't want to force you into this. "
            e " So...what do you say? "
            " You pretty much have nothing to do for this break, so... "
            " You agreed on helping them. "
            e " Nice, nice... "
            e " Just start by picking out some books from the basket. "
            e " Then, you can go and find their respective sections. "
            e " That DOES mean you have to walk around the library though. "
            e " ...A lot. "
            e " But I'm sure you don't mind. "
            " You gave him a thumbs up before starting to work. "
            scene black with dissolve
            " You spent the rest of the break helping Engel and Cubbie. "
            " And honestly? you were feeling their pain. "
            " You encountered some of the problems they had. But, you eventually got everything done. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump historyclassfri
        else:
            " You walked over to them and asked them what they were doing. "
            x " Hey there, [name]. "
            $ engelknow = True
            $ cubbieknow = True
            e " I'm Engel, and... "
            e " I'm just helping Cubbie sort out some books over here. "
            cb " ... "
            " The cat guy politely waves at you. "
            e " The teachers just asked us to sort some books, since... "
            e " There's just some books that the old librarian forgot to put in. "
            e " And by some...I mean a lot. "
            e " I mean - take a look at the basket we have here. "
            cb " ... "
            " Cubbie pointed over to the basket filled with books. "
            " You took a good look, and...yup. "
            " There sure was a lot of books that were there. "
            " You even saw some old books that used to be popular. "
            " Huh. They're THAT old. "
            e " This is gonna take us longer than just one break, I bet... "
            e " Even with two people working on this. "
            e " I don't mind working, but... "
            e " I don't want to work for the entire school day, you get me? "
            cb " ... "
            " Cubbie does a little nod of agreement. "
            " Honestly, you didn't want to work for an entire break, too. "
            " Working for that long is honestly just really painful. "
            e " It's also a little hard sorting things out. "
            e " For example: I've got a romance book here. "
            e " I have to read a few pages and turns out, it's actually a horror book. "
            e " I'm already at the romance section, so I have to go alll the way to the horror section... "
            e " Which is over at the left side of the library. "
            e " Great, isn't it? "
            cb " ... "
            " Yeah, no...that's just... "
            " That's just really annoying, at that point. "
            e " So we have to go back and forth every time we get a genre wrong... "
            e " It's honestly a bit tiring for me. "
            e " Actually, now that you're here... "
            e " I was wondering if you could help us. "
            e " With three people, things could be faster around here. "
            cb " ... "
            e " Right, Cubbie - "
            e " We also don't want to force you into this. "
            e " So...what do you say? "
            " You pretty much have nothing to do for this break, so... "
            " You agreed on helping them. "
            e " Nice, nice... "
            e " Just start by picking out some books from the basket. "
            e " Then, you can go and find their respective sections. "
            e " That DOES mean you have to walk around the library though. "
            e " ...A lot. "
            e " But I'm sure you don't mind. "
            " You gave him a thumbs up before starting to work. "
            scene black with dissolve
            " You spent the rest of the break helping Engel and Cubbie. "
            " And honestly? you were feeling their pain. "
            " You encountered some of the problems they had. But, you eventually got everything done. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom. "
            pause 2.0
            jump historyclassfri
    label oligangfri3:
        scene black with dissolve
        pause 2.0
        scene oligangclub with dissolve
        " You walked into the room and spotted Oliver just standing there. "
        " Wondering what he's up to, you walk over to him. "
        show oliverneutral at center with easeinleft
        if oliganglv >= 30 or oliganglv == 30:
            o " Hey there, idiot. "
            o " So! "
            o " I'm sure you know the plan already. "
            o " ...If you were listening to me earlier. "
            o " Basically we bully this kid named Abbie. "
            o " Easy peasy, right? "
            o " And even more of an easy thing since Abbie's an easy target. "
            o " Dude's basically a crybaby! "
            o " And he's so weak, too. "
            o " We can get him crying by doing the simplest things ever. "
            o " Trust me on this one. "
            o " You wanna go right now? "
            o " The others are waiting for ya, you know. "
            o " Been waiting for a good while now, actually. "
            o " So, what you gonna do? "
            menu:
                " LETS GOOO!! ":
                    hide oliverneutral at bottom
                    show oliverhappy at center
                    o " Oho, now THAT'S the spirit! "
                    o " Come on, let's go break his legs. "
                    o " Not in the gay way though. "
                    o " I have a girlfriend. "
                    o " Let's go, let's go!! "
                    scene black with dissolve
                    " A bit of bullying later... "
                    " Sorry, can't show this. "
                    " This is too high school bully stereotype for this game. "
                    " I can't be saying that though when I literally typed out the mean mc's...situations. "
                    " But uh. Yeah. Skipping. "
                    scene oligangclub with dissolve
                    show oliverneutral at center with easeinright
                    o " Geez, that was real fun! "
                    o " You were a natural, as I expected. "
                    o " You're pretty good at this stuff, [name]. "
                    o " I'm thinking about having you on the team for way longer! "
                    o " You wanna do that shit? like be real good friends with us? "
                    menu:
                        " you bet!! ":
                            $ oligangsend.grant()
                            hide oliverneutral at bottom
                            show oliverhappy at center
                            o " Awesome. "
                            o " You're truly a part of us now! "
                            o " Welcome to the gang, truly. "
                            o " We're happy to have you. "
                            scene oligangending with dissolve
                            " You've somehow managed to get along with the mean guys... "
                            " ...And have become their bestest friend! "
                            " You've also got their sweet achievement. Check your achievements tab! "
                            " Congratulations! now you get to do cool pranks with them... "
                            " All while the teacher lets you do anything you want. "
                            " Sweet. "
                            jump credits
                        " Nah, ts was temporary ":
                            o " Oh damn. "
                            o " I've been bamboozled, then! "
                            o " Okay, but for real, you ain't leaving. "
                            o " Would be a waste if I just threw you out. "
                            o " I'm gonna go eat soap now... "
                            o " You can just chill here if you want. "
                            o " Cya. "
                            hide oliverneutral at right with easeoutright
                            scene black with dissolve
                            " You spent the rest of the break just hanging out in the room. "
                            " Just playing games on your phone... "
                            " It was pretty chill without Oliver and the gang there. "
                            " Just straight up relaxing... "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You got out of the room after a bit of gaming. "
                            pause 2.0
                            jump historyclassfri
                " I have something else to do ":
                    o " Oh, on god? "
                    o " Damn, alright... "
                    o " Well, I'll get going then. "
                    o " Cya, idiot. "
                    hide oliverneutral at right with easeoutright
                    scene black with dissolve
                    " You spent the rest of the break just hanging out in the room. "
                    " Just playing games on your phone... "
                    " It was pretty chill without Oliver and the gang there. "
                    " Just straight up relaxing... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You got out of the room after a bit of gaming. "
                    pause 2.0
                    jump historyclassfri
        else:
            o " Hey dude, you know about the plan I talked about earlier? "
            o " If you were listening properly, then I had this plan to bully this kid named Abbie... "
            o " Buuut, Zip and Edward has got things they're dealing with, "
            o " So therefore, cancelled. "
            o " Damn, I didn't want it to get cancelled though... "
            o " Pretty unfortunate since I had big plans. "
            o " Oh well, it's whatever. "
            o " We can just do that stuff next week, after all! "
            o " Anyway, I'm off to go and get a new pack of soap. "
            o " Just chill here if you want. "
            o " Cya. "
            hide oliverneutral at right with easeoutright
            scene black with dissolve
            " You spent the rest of the break just hanging out in the room. "
            " Just playing games on your phone... "
            " It was pretty chill without Oliver and the gang there. "
            " Just straight up relaxing... "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You got out of the room after a bit of gaming. "
            pause 2.0
            jump historyclassfri
        # if oligang has enough lv, then move to the plan with abbie at the gym
        # and then mc recieves ending.
        # if mc doesnt have enough lv, oliver says plan was cancelled.

label historyclassfri:
    scene classroom with dissolve
    " You walked into the classroom and waited for the teacher to arrive. "
    " As you were writing, you noticed a bug on the wall. "
    " Huh. Wonder how that got there. "
    " As if the bug knew that you were looking at it, it skedaddled away. "
    " Aw, a shame... it was a really pretty bug. "
    " You lowkey wanted to see a little bit more of it. "
    " Oh wait, the teacher's here. "
    " Time to lock in. "
    show msemilyneutral at center with easeinright
    mse " Hey there, class! "
    mse " I hope you all have had an amazing week so far! "
    mse " And I also hope that all of you are going to have a wonderful weekend. "
    mse " Buut, before that... "
    mse " We're going to have our class, of course! "
    mse " For our class today, we're just going to have some note taking. "
    mse " So get your notebooks and pens out! "
    mse " And I better not catch all of you sleeping on this though. "
    mse " And by that - I mean not paying attention, not copying...you get the idea. "
    mse " Don't start complaining if you get a low grade from having no notes to study for. "
    mse " ...Okay, my english might've died there, but you get the idea. "
    mse " Time to copy some notes, class! "
    scene black with dissolve
    " Yet again, you spent the class time copying down notes. "
    " Atleast this is better than doing projects for class. "
    " You didn't have to do much this way. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, time for another break. "
    " You got off of your chair and went to the hallway. "
    pause 2.0
    jump fribreak4

label fribreak4:
    # claire's, engel's, bubbles, lanas endings
    scene hallway with dissolve
    if oligangjoin == True:
        " Huh, looks like no one's in the room right now. "
        " Oh well, guess you're going to have to look elsewhere. Finally.. "
        pass
    else:
        pass
    " Where are you gonna hang out for this break? "
    menu:
        " {image=abbieicon} The front of the school {image=skellicon} ":
            jump frontschoolfri4
        " {image=claireicon} The back of the school {image=rubyicon} ":
            jump backschoolfri4
        " {image=bubbleicon} The gym {image=popularicon} ":
            jump gymfri4
        " {image=cubbieicon} The cafeteria {image=lanaicon} ":
            jump cafeteriafri4
        " {image=kevinicon} The rooftop {image=robbyicon} ":
            jump rooftopfri4
        " {image=engelicon} The library {image=rileyicon} ":
            jump libraryfri4
    label frontschoolfri4:
        # abbie and skell // interact
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked to the front of the school and found two of your classmates talking to eachother. "
        " Wondering what they're talking about, you walked over to them. "
        show abbieneutral at left with easeinright
        show skellneutral at right with easeinright
        if abbieknow == True and skellknow == True:
            " You walked over to them and asked them what they were doing. "
            " Just being your curious self, as per usual... "
            sk " Hi there, [name]. "
            a " ...Um...hi... "
            sk " Me and Abbie over here were just talking about a few things. "
            sk " Like talking about a new movie coming out this sunday. "
            sk " It's basically a comic turned into a whole ass anime... "
            sk " God, this is so embarrassing to talk about. "
            sk " I've already said my words now though, so... "
            sk " I guess I have to explain everything to you now. "
            a " Um...I think I've heard...Bubble talking about it before... "
            a " I've seen her draw some characters in that show, too... "
            sk " Wow, really? "
            sk " I mean, I know the shows popular, but... "
            sk " Didn't expect Bubble to be into it. "
            sk " Can't judge a book by it's cover, I guess. "
            sk " Anyway... "
            sk " The whole thing of this is that they're fighting demons. "
            sk " In the newest movie, they're taking on the king of demons. "
            sk " They're off to kill that guy because killing the king = killing every single demon that exists. "
            sk " The whole demon thing has been going for a good period now... "
            sk " You could say it's like this ongoing war between humans and demons. "
            sk " Except there's like special people with powers who take them down. "
            sk " ...The powers part is mostly the ones who rank higher in the special people thing. "
            sk " I'm honestly a little surprised that Abbie over here is into this. "
            sk " Never thought you'd be into violence. "
            a " Uh...um... "
            hide abbieneutral at bottom
            show abbiehappy at left
            a " ...N...Never judge a book by it's cover...? "
            hide skellneutral at bottom
            show skellhappy at right
            sk " Heh - wow, using my own words against me. "
            sk " But yeah, that's also right. "
            hide abbiehappy at bottom
            show abbieneutral at left
            sk " I can see why you're into this stuff though. "
            hide skellhappy at bottom
            show skellneutral at right
            sk " It's got good fighting scenes, and the artstyle is nice, too. "
            sk " And I mean the artstyle is REALLY nice to look at. "
            sk " Really shows how much passion and work it's being put into it. "
            sk " Which is nice instead of burning out your workers and making them make something horrible. "
            sk " Their work paid off. "
            a " Y...yeah... "
            a " It really did... "
            a " All of the fighting scenes look so nice and well made... "
            sk " Mhm. "
            sk " Anyway - we're gonna get tickets on sunday. "
            sk " It's going to be a pain if we arrive late and people are gonna start flooding in, so... "
            sk " Me and Abbie are planning to go there the earliest we can for the first schedule. "
            a " Yeah... "
            a " Don't really want to stay too late for the movies... "
            a " Things could get a bit scary in the night... "
            sk " Hey, if we ever DO end up having to go for the last schedule... "
            sk " I'll make sure to walk you all the way home. "
            sk " Don't want you to be going alone at such hours, after all. "
            sk " It's those hours where the creeps come out. "
            a " Really...? "
            a " ...Thanks in advance, Skell... "
            sk " It's no problem. "
            sk " Just want my classmates to be safe. "
            scene black with dissolve
            " You spent the rest of the break talking with Skell and Abbie. "
            " That movie they were talking about sounds interesting... "
            " You should look it up later when you have the time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into your school, and went to your classroom. "
            pause 2.0
            jump musicclassfri
        elif abbieknow == True and skellknow == False:
            " You walked over to them and asked them what they were doing. "
            " Just being your curious self, as per usual... "
            x " Hi there, [name]. "
            a " ...Um...hi... "
            $ skellknow = True
            sk " I'm Skell, one of your classmates. "
            sk " Me and Abbie over here were just talking about a few things. "
            sk " Like talking about a new movie coming out this sunday. "
            sk " It's basically a comic turned into a whole ass anime... "
            sk " God, this is so embarrassing to talk about. "
            sk " I've already said my words now though, so... "
            sk " I guess I have to explain everything to you now. "
            a " Um...I think I've heard...Bubble talking about it before... "
            a " I've seen her draw some characters in that show, too... "
            sk " Wow, really? "
            sk " I mean, I know the shows popular, but... "
            sk " Didn't expect Bubble to be into it. "
            sk " Can't judge a book by it's cover, I guess. "
            sk " Anyway... "
            sk " The whole thing of this is that they're fighting demons. "
            sk " In the newest movie, they're taking on the king of demons. "
            sk " They're off to kill that guy because killing the king = killing every single demon that exists. "
            sk " The whole demon thing has been going for a good period now... "
            sk " You could say it's like this ongoing war between humans and demons. "
            sk " Except there's like special people with powers who take them down. "
            sk " ...The powers part is mostly the ones who rank higher in the special people thing. "
            sk " I'm honestly a little surprised that Abbie over here is into this. "
            sk " Never thought you'd be into violence. "
            a " Uh...um... "
            hide abbieneutral at bottom
            show abbiehappy at left
            a " ...N...Never judge a book by it's cover...? "
            hide skellneutral at bottom
            show skellhappy at right
            sk " Heh - wow, using my own words against me. "
            sk " But yeah, that's also right. "
            hide abbiehappy at bottom
            show abbieneutral at left
            sk " I can see why you're into this stuff though. "
            hide skellhappy at bottom
            show skellneutral at right
            sk " It's got good fighting scenes, and the artstyle is nice, too. "
            sk " And I mean the artstyle is REALLY nice to look at. "
            sk " Really shows how much passion and work it's being put into it. "
            sk " Which is nice instead of burning out your workers and making them make something horrible. "
            sk " Their work paid off. "
            a " Y...yeah... "
            a " It really did... "
            a " All of the fighting scenes look so nice and well made... "
            sk " Mhm. "
            sk " Anyway - we're gonna get tickets on sunday. "
            sk " It's going to be a pain if we arrive late and people are gonna start flooding in, so... "
            sk " Me and Abbie are planning to go there the earliest we can for the first schedule. "
            a " Yeah... "
            a " Don't really want to stay too late for the movies... "
            a " Things could get a bit scary in the night... "
            sk " Hey, if we ever DO end up having to go for the last schedule... "
            sk " I'll make sure to walk you all the way home. "
            sk " Don't want you to be going alone at such hours, after all. "
            sk " It's those hours where the creeps come out. "
            a " Really...? "
            a " ...Thanks in advance, Skell... "
            sk " It's no problem. "
            sk " Just want my classmates to be safe. "
            scene black with dissolve
            " You spent the rest of the break talking with Skell and Abbie. "
            " That movie they were talking about sounds interesting... "
            " You should look it up later when you have the time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into your school, and went to your classroom. "
            pause 2.0
            jump musicclassfri
        elif abbieknow == False and skellknow == True:
            " You walked over to them and asked them what they were doing. "
            " Just being your curious self, as per usual... "
            sk " Hi there, [name]. "
            x " ...Um...hi... "
            $ abbieknow = True
            sk " Me and Abbie over here were just talking about a few things. "
            sk " Like talking about a new movie coming out this sunday. "
            sk " It's basically a comic turned into a whole ass anime... "
            sk " God, this is so embarrassing to talk about. "
            sk " I've already said my words now though, so... "
            sk " I guess I have to explain everything to you now. "
            a " Um...I think I've heard...Bubble talking about it before... "
            a " I've seen her draw some characters in that show, too... "
            sk " Wow, really? "
            sk " I mean, I know the shows popular, but... "
            sk " Didn't expect Bubble to be into it. "
            sk " Can't judge a book by it's cover, I guess. "
            sk " Anyway... "
            sk " The whole thing of this is that they're fighting demons. "
            sk " In the newest movie, they're taking on the king of demons. "
            sk " They're off to kill that guy because killing the king = killing every single demon that exists. "
            sk " The whole demon thing has been going for a good period now... "
            sk " You could say it's like this ongoing war between humans and demons. "
            sk " Except there's like special people with powers who take them down. "
            sk " ...The powers part is mostly the ones who rank higher in the special people thing. "
            sk " I'm honestly a little surprised that Abbie over here is into this. "
            sk " Never thought you'd be into violence. "
            a " Uh...um... "
            hide abbieneutral at bottom
            show abbiehappy at left
            a " ...N...Never judge a book by it's cover...? "
            hide skellneutral at bottom
            show skellhappy at right
            sk " Heh - wow, using my own words against me. "
            sk " But yeah, that's also right. "
            hide abbiehappy at bottom
            show abbieneutral at left
            sk " I can see why you're into this stuff though. "
            hide skellhappy at bottom
            show skellneutral at right
            sk " It's got good fighting scenes, and the artstyle is nice, too. "
            sk " And I mean the artstyle is REALLY nice to look at. "
            sk " Really shows how much passion and work it's being put into it. "
            sk " Which is nice instead of burning out your workers and making them make something horrible. "
            sk " Their work paid off. "
            a " Y...yeah... "
            a " It really did... "
            a " All of the fighting scenes look so nice and well made... "
            sk " Mhm. "
            sk " Anyway - we're gonna get tickets on sunday. "
            sk " It's going to be a pain if we arrive late and people are gonna start flooding in, so... "
            sk " Me and Abbie are planning to go there the earliest we can for the first schedule. "
            a " Yeah... "
            a " Don't really want to stay too late for the movies... "
            a " Things could get a bit scary in the night... "
            sk " Hey, if we ever DO end up having to go for the last schedule... "
            sk " I'll make sure to walk you all the way home. "
            sk " Don't want you to be going alone at such hours, after all. "
            sk " It's those hours where the creeps come out. "
            a " Really...? "
            a " ...Thanks in advance, Skell... "
            sk " It's no problem. "
            sk " Just want my classmates to be safe. "
            scene black with dissolve
            " You spent the rest of the break talking with Skell and Abbie. "
            " That movie they were talking about sounds interesting... "
            " You should look it up later when you have the time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into your school, and went to your classroom. "
            pause 2.0
            jump musicclassfri
        else:
            " You walked over to them and asked them what they were doing. "
            " Just being your curious self, as per usual... "
            x " Hi there, [name]. "
            x " ...Um...hi... "
            $ skellknow = True
            sk " I'm Skell, one of your classmates. "
            $ abbieknow = True
            sk " Me and Abbie over here were just talking about a few things. "
            sk " Like talking about a new movie coming out this sunday. "
            sk " It's basically a comic turned into a whole ass anime... "
            sk " God, this is so embarrassing to talk about. "
            sk " I've already said my words now though, so... "
            sk " I guess I have to explain everything to you now. "
            a " Um...I think I've heard...Bubble talking about it before... "
            a " I've seen her draw some characters in that show, too... "
            sk " Wow, really? "
            sk " I mean, I know the shows popular, but... "
            sk " Didn't expect Bubble to be into it. "
            sk " Can't judge a book by it's cover, I guess. "
            sk " Anyway... "
            sk " The whole thing of this is that they're fighting demons. "
            sk " In the newest movie, they're taking on the king of demons. "
            sk " They're off to kill that guy because killing the king = killing every single demon that exists. "
            sk " The whole demon thing has been going for a good period now... "
            sk " You could say it's like this ongoing war between humans and demons. "
            sk " Except there's like special people with powers who take them down. "
            sk " ...The powers part is mostly the ones who rank higher in the special people thing. "
            sk " I'm honestly a little surprised that Abbie over here is into this. "
            sk " Never thought you'd be into violence. "
            a " Uh...um... "
            hide abbieneutral at bottom
            show abbiehappy at left
            a " ...N...Never judge a book by it's cover...? "
            hide skellneutral at bottom
            show skellhappy at right
            sk " Heh - wow, using my own words against me. "
            sk " But yeah, that's also right. "
            hide abbiehappy at bottom
            show abbieneutral at left
            sk " I can see why you're into this stuff though. "
            hide skellhappy at bottom
            show skellneutral at right
            sk " It's got good fighting scenes, and the artstyle is nice, too. "
            sk " And I mean the artstyle is REALLY nice to look at. "
            sk " Really shows how much passion and work it's being put into it. "
            sk " Which is nice instead of burning out your workers and making them make something horrible. "
            sk " Their work paid off. "
            a " Y...yeah... "
            a " It really did... "
            a " All of the fighting scenes look so nice and well made... "
            sk " Mhm. "
            sk " Anyway - we're gonna get tickets on sunday. "
            sk " It's going to be a pain if we arrive late and people are gonna start flooding in, so... "
            sk " Me and Abbie are planning to go there the earliest we can for the first schedule. "
            a " Yeah... "
            a " Don't really want to stay too late for the movies... "
            a " Things could get a bit scary in the night... "
            sk " Hey, if we ever DO end up having to go for the last schedule... "
            sk " I'll make sure to walk you all the way home. "
            sk " Don't want you to be going alone at such hours, after all. "
            sk " It's those hours where the creeps come out. "
            a " Really...? "
            a " ...Thanks in advance, Skell... "
            sk " It's no problem. "
            sk " Just want my classmates to be safe. "
            scene black with dissolve
            " You spent the rest of the break talking with Skell and Abbie. "
            " That movie they were talking about sounds interesting... "
            " You should look it up later when you have the time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into your school, and went to your classroom. "
            pause 2.0
            jump musicclassfri
    label backschoolfri4:
        # claire and ruby // not interact
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of the school and spotted two of your classmates doing their own things. "
        " Who do you talk to for this break? "
        if claireknow == True and rubyknow == True:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    jump gordonlavie
                " {image=rubyicon} Ruby {image=rubyicon} ":
                    jump weddingteto
        elif claireknow == True and rubyknow == False:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    jump gordonlavie
                " {image=rubyicon} A girl with a TV for a head {image=rubyicon} ":
                    jump weddingteto
        elif claireknow == False and rubyknow == True:
            menu:
                " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                    jump gordonlavie
                " {image=rubyicon} Ruby {image=rubyicon} ":
                    jump weddingteto
        else:
            menu:
                " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                    jump gordonlavie
                " {image=rubyicon} A girl with a TV for a head {image=rubyicon} ":
                    jump weddingteto
        label gordonlavie:
            # claire ending
            show claireneutral at center with easeinleft
            if claireknow == True:
                pause 0.1
                if clairelv >= 30 or clairelv == 30:
                    " You walked over to her and asked her what she was reading. "
                    " Looked like something interesting, that's for sure. "
                    " You sat down next to her to get a better look at what she's reading. "
                    c " Hiya, [name]! "
                    c " Just reading a book about fantasy... "
                    c " ...To be honest... "
                    c " All genres of a book is good - "
                    c " As long as they're written well, that is. "
                    c " It's just like how I've been thinking lately... "
                    c " Everyone's good as long as they ARE good. "
                    c " Something may look good at first, but when you really take a look at it... "
                    c " ...It's gonna turn out bad. "
                    c " That's why we need to be careful of certain things. "
                    c " As an example - we need to be careful of the people we're around. "
                    c " They look harmless at first, but when you get to know them... "
                    c " They're just hurting you from the inside and out, "
                    c " ...And you wouldn't even notice it until you're far too late. "
                    c " But...[name], if I can be honest with you... "
                    hide claireneutral at bottom
                    show clairehappy at center
                    c " You've been one of the greatest people to appear in my life. "
                    c " Even though we've only known eachother for a week.. "
                    c " It feels like it's been aeons. "
                    c " And lightyears are a long, long time - you know! "
                    c " It's insane how we got this close in a short time, hehe... "
                    c " But I'm happy that we met! "
                    c " You somehow became the highlight of my days... "
                    c " Is that a little too early to say? "
                    c " Hehe...sorry... "
                    c " I've got one thing to ask you though! "
                    c " ...Would you want to be best friends with me? "
                    c " I know it's a little too soon to say that, buut... "
                    c " Okay - listen - you have best friend material! "
                    c " And that's really good!! "
                    c " So...um...you wanna...become best friends? "
                    menu:
                        " YEAAAHHH ":
                            $ clairesend.grant()
                            c " Really?! "
                            c " That's wonderful news! "
                            c " Hey, um... "
                            c " If you ever want to hang out, or need anything... "
                            c " Just tell me, okay? "
                            c " I've always got your back, no matter what! "
                            c " As long as you've got mine, hehe. "
                            scene claireend with dissolve
                            " Congratulations - you've just made a great best friend in this school! "
                            " Not only will she help you with your homework, but she will also comfort you at times! "
                            " And you've got her nice achievement. Check your achievement tab! "
                            " You and Claire are gonna have a nice and healthy best-friendship. "
                            jump credits
                        " can we just be normal friends ":
                            hide clairehappy at bottom
                            show claireneutral at center
                            c " Oh - uh, sure! "
                            c " It's completely fine that you want to be that way. "
                            c " Not gonna force you, you know? "
                            c " I'm big on people being comfortable, so...yeah. "
                            c " Uh, while you're here, you wanna read this book with me? "
                            c " I don't want this to be just awkward silence, after all! "
                            c " That would be way too uncomfy. "
                            " Well, you had nothing to do for this break, so... "
                            " You agreed to read with Claire. "
                            c " Okay! let me just position the book properly... "
                            scene black with dissolve
                            " You spent the rest of the break talking with Claire. "
                            " And also reading a book with her. Woops, forgot to mention that... "
                            " It was a pretty good book. Maybe you should read books more often. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked back into the school and went to your classroom. "
                            pause 2.0
                            jump musicclassfri
                else:
                    " You walked over to her and asked her what she was doing. "
                    " Looked like she was drawing something on a folded piece of paper. "
                    " You sat down next to her to get a closer look at what she was doing. "
                    c " Hey there, [name]! "
                    c " Nice to see you here... "
                    c " I've been trying to think of a bookmark design that I could use! "
                    c " And yes, I know that I can just use basically anything for a bookmark, but... "
                    c " I think it's better if I make my own. "
                    c " Making things yourself is nice, you know! "
                    c " Like those DIY videos I used to keep seeing. "
                    c " Ah, those were good... "
                    c " ...For memories, not actual stuff. "
                    c " In all honesty, some of them were pretty stupid. "
                    c " Actually - most of them. "
                    c " I don't know what went through people's heads when they were making that stuff... "
                    c " But anyway...bookmark ideas. "
                    c " I need them. "
                    c " Could ya help me on this one? "
                    c " And I don't want to put my favorite character there. "
                    c " I want something unique, you know! "
                    c " Putting my favorite character on there seems a little bit...obvious and unoriginal. "
                    c " But then again...not everything is original, right? "
                    c " Still though, I want some ideas. "
                    c " ...If you don't mind helping me, of course. "
                    c " You don't have to if you don't want to! "
                    c " Just give me reccomendations or pictures from google as a reference. "
                    " Well...you had nothing better to do for this break. "
                    " You decided to help her. "
                    c " Oh, cool! "
                    c " Like I said... "
                    c " Reccomendations or pictures from google. "
                    " You gave her a thumbs up before looking at your phone. "
                    " Time to get reference searching.. "
                    scene black with dissolve
                    " You spent the rest of the break helping Claire with finding a reference. "
                    " You eventually found one that looked good and simple.. "
                    " Pretty good. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump musicclassfri
            else:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was drawing something on a folded piece of paper. "
                " You sat down next to her to get a closer look at what she was doing. "
                x " Hey there, [name]! "
                x " Nice to see you here... "
                $ claireknow = True
                c " I'm Claire, by the way! one of your classmates! "
                c " I've been trying to think of a bookmark design that I could use! "
                c " And yes, I know that I can just use basically anything for a bookmark, but... "
                c " I think it's better if I make my own. "
                c " Making things yourself is nice, you know! "
                c " Like those DIY videos I used to keep seeing. "
                c " Ah, those were good... "
                c " ...For memories, not actual stuff. "
                c " In all honesty, some of them were pretty stupid. "
                c " Actually - most of them. "
                c " I don't know what went through people's heads when they were making that stuff... "
                c " But anyway...bookmark ideas. "
                c " I need them. "
                c " Could ya help me on this one? "
                c " And I don't want to put my favorite character there. "
                c " I want something unique, you know! "
                c " Putting my favorite character on there seems a little bit...obvious and unoriginal. "
                c " But then again...not everything is original, right? "
                c " Still though, I want some ideas. "
                c " ...If you don't mind helping me, of course. "
                c " You don't have to if you don't want to! "
                c " Just give me reccomendations or pictures from google as a reference. "
                " Well...you had nothing better to do for this break. "
                " You decided to help her. "
                c " Oh, cool! "
                c " Like I said... "
                c " Reccomendations or pictures from google. "
                " You gave her a thumbs up before looking at your phone. "
                " Time to get reference searching.. "
                scene black with dissolve
                " You spent the rest of the break helping Claire with finding a reference. "
                " You eventually found one that looked good and simple.. "
                " Pretty good. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump musicclassfri
        label weddingteto:
            show rubyneutral at center with easeinright
            if rubyknow == True:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was staring at something... "
                " But you don't really know what she's staring at. "
                ru " ... "
                " I mean, she's staring at a tree. "
                " Is this how robots zone out? "
                " You don't know, but it looks like she's doing it right now. "
                " You're just going to have to wait for her to come back to reality then. "
                ru " ... "
                ru " Oh, sorry [name]! "
                ru " I didn't mean to keep you waiting... "
                ru " I was just installing a new update! "
                ru " I can do some cool stuff now... "
                ru " Like show bubbles on my screen whenever I'm thinking about something! "
                ru " Watch this... "
                ru " I'm going to think about math problems... "
                " You waited for it to happen... "
                " ...And eventually, a gif of bubbles going around her screen started playing. "
                " You have the urge to actually attempt to pop them. "
                " Though you're going to have to tell about this to the teachers... "
                " Since the teachers are most likely going to think she's distracted. "
                " Eventually, her screen goes back to normal. "
                ru " See? wasn't that cool! "
                hide rubyneutral at bottom
                show rubysad at center
                ru " I'm gonna have to talk to the teachers about it though... "
                ru " I know well that they're going to think that I'm distracted. "
                ru " Even though I'm not and I'm just thinking really hard... "
                ru " I need my own cool loading screen, too! "
                ru " So many of the others got it... "
                hide rubysad at bottom
                show rubyneutral at center
                ru " That's why I installed it in the first place! "
                ru " Though now that I think about it more... "
                hide rubyneutral at bottom
                show rubysad at center
                ru " The loading screen I chose wasn't that good. "
                ru " I mean...it looks like I'm distracted! "
                ru " I should have those cool circle ones... "
                hide rubysad at bottom
                show rubyhappy at center
                ru " But just make it fitting to my colors! "
                ru " That would look pretty neat, right? "
                ru " I'll just uninstall this loading screen later at home though... "
                ru " It doesn't really let me uninstall it after a few minutes of installing it. "
                ru " A pain, but...a reasonable thing to do. "
                ru " Then, after that...I'm gonna go install the circle thingies! "
                ru " Really exciting for me, hehe!! "
                ru " If you were someone like me, [name]... "
                ru " You'd probably be really excited for me! "
                ru " I think you can still be excited as a human, but... "
                ru " You wouldn't really understand this since you're, you know...not like me. "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby. "
                " Just talking about robot stuff... "
                " Ruby would often do her bubble thing whenever you asked her a question. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump musicclassfri
            else:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was staring at something... "
                " But you don't really know what she's staring at. "
                x " ... "
                " I mean, she's staring at a tree. "
                " Is this how robots zone out? "
                " You don't know, but it looks like she's doing it right now. "
                " You're just going to have to wait for her to come back to reality then. "
                x " ... "
                x " Oh, sorry [name]! "
                x " I didn't mean to keep you waiting... "
                $ rubyknow = True
                ru " I'm Ruby, by the way! "
                ru " I was just installing a new update! "
                ru " I can do some cool stuff now... "
                ru " Like show bubbles on my screen whenever I'm thinking about something! "
                ru " Watch this... "
                ru " I'm going to think about math problems... "
                " You waited for it to happen... "
                " ...And eventually, a gif of bubbles going around her screen started playing. "
                " You have the urge to actually attempt to pop them. "
                " Though you're going to have to tell about this to the teachers... "
                " Since the teachers are most likely going to think she's distracted. "
                " Eventually, her screen goes back to normal. "
                ru " See? wasn't that cool! "
                hide rubyneutral at bottom
                show rubysad at center
                ru " I'm gonna have to talk to the teachers about it though... "
                ru " I know well that they're going to think that I'm distracted. "
                ru " Even though I'm not and I'm just thinking really hard... "
                ru " I need my own cool loading screen, too! "
                ru " So many of the others got it... "
                hide rubysad at bottom
                show rubyneutral at center
                ru " That's why I installed it in the first place! "
                ru " Though now that I think about it more... "
                hide rubyneutral at bottom
                show rubysad at center
                ru " The loading screen I chose wasn't that good. "
                ru " I mean...it looks like I'm distracted! "
                ru " I should have those cool circle ones... "
                hide rubysad at bottom
                show rubyhappy at center
                ru " But just make it fitting to my colors! "
                ru " That would look pretty neat, right? "
                ru " I'll just uninstall this loading screen later at home though... "
                ru " It doesn't really let me uninstall it after a few minutes of installing it. "
                ru " A pain, but...a reasonable thing to do. "
                ru " Then, after that...I'm gonna go install the circle thingies! "
                ru " Really exciting for me, hehe!! "
                ru " If you were someone like me, [name]... "
                ru " You'd probably be really excited for me! "
                ru " I think you can still be excited as a human, but... "
                ru " You wouldn't really understand this since you're, you know...not like me. "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby. "
                " Just talking about robot stuff... "
                " Ruby would often do her bubble thing whenever you asked her a question. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump musicclassfri
    label gymfri4:
        # bubble, lizzy and petunia // not interact
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked into the gym and and found two of your classmates doing their own things. "
        " Who do you want to talk to for this break? "
        if bubbleknow == True and popularknow == True:
            menu:
                " {image=bubbleicon} Bubble {image=bubbleicon} ":
                    jump mikumonitoringyay
                " {image=popularicon} Lizzy and Petunia {image=popularicon} ":
                    jump mikumonitoringno
        elif bubbleknow == True and popularknow == False:
            menu:
                " {image=bubbleicon} Bubble {image=bubbleicon} ":
                    jump mikumonitoringyay
                " {image=popularicon} The popular girls {image=popularicon} ":
                    jump mikumonitoringno
        elif bubbleknow == False and popularknow == True:
            menu:
                " {image=bubbleicon} A girl made up of bubbles {image=bubbleicon} ":
                    jump mikumonitoringyay
                " {image=popularicon} Lizzy and Petunia {image=popularicon} ":
                    jump mikumonitoringno
        else:
            menu:
                " {image=bubbleicon} A girl made up of bubbles {image=bubbleicon} ":
                    jump mikumonitoringyay
                " {image=popularicon} The popular girls {image=popularicon} ":
                    jump mikumonitoringno
        label mikumonitoringyay:
            # bubble's ending
            show bubbleneutral at center with easeinright
            if bubbleknow == True:
                pause 0.1
                if bubblelv >= 30 or bubblelv == 30:
                    " You walked over to her and asked her what she was doing. "
                    " Looked like she was playing with a flower she got from the back of the school. "
                    " And she looked very bored... "
                    " You sat down next to her on the bleachers where she was. "
                    b " Hi there, [name]! "
                    b " Just a ittle...bored, you know? "
                    b " I got this flower from the back of the school! "
                    b " Not sure if I was even allowed to take it, but... "
                    b " Uh...I guess I'll just put this back later. "
                    b " I couldn't really help myself - it was too pretty! "
                    b " Sorry to whoever planted them, though... "
                    b " I'll put this flower back when I can... "
                    b " ...If I don't forget to do that! "
                    b " Hmmhmmm... "
                    " Bubble continued to play with the flower, being careful that she wouldn't break it. "
                    " Taking a closer look at the flower... "
                    " It was really beautiful, just like what she said about it. "
                    scene bubbleend with dissolve
                    b " ...You know, [name]... "
                    b " This flower over here reminds me of you! "
                    b " Very beautiful... "
                    b " But you've also got to be really careful while handling it. "
                    b " I don't mean that in a bad way, of course! "
                    b " And uh... "
                    b " Going to be honest with you, but... "
                    b " You've been the absolute best to me these past few days! "
                    b " Even though I've only known you for a week... "
                    b " Things have really been better for me ever since you came here! "
                    b " You've made me happier, and I mean that! "
                    b " I...I don't even know what to say anymore, haha... "
                    b " I've always kind of considered you as a friend from the start, but... "
                    b " Would you like to be even better than that? Best friends? "
                    b " It's okay if you don't want to! "
                    b " ...Really. "
                    menu:
                        " BEST FRIENDS FOREVER! ":
                            $ bubblesend.grant()
                            scene bubbleend1 with dissolve
                            b " YAY!! "
                            b " Best friends forever and ever! "
                            b " Let's go get a nice snack once class is over, okay? "
                            b " I'll be paying! "
                            " Congratulations, you've gotten Bubble's ending! "
                            " Not only that, but you've also got her achievement. Check your achievements list! "
                            " You and Bubble became best friends forever...and now you're also defending her from every single one of Oliver's attacks on her. "
                            " You'd make sure you'd never accidentally pop her... "
                            " And with that, you've gained a whole lot of her respect! "
                            " Nice one, [name]! "
                            jump credits
                        " Man I don't know you too well ":
                            scene bubbleend2 with dissolve
                            b " Oh, uh...yeah, right. "
                            b " Sorry if me asking you to be best friends was a little too soon! "
                            b " I just felt like we were getting really close, you know...? "
                            b " But it's okay if you don't want to be like that! "
                            scene bubbleend with dissolve
                            b " We can just stay like normal friends, like you said! "
                            b " Don't want to make you uncomfortable, after all! "
                            scene black with dissolve
                            " You spent the rest of the break talking with Bubble. "
                            " Just talking about the types of flowers... "
                            " Nothing too interesting, in my opinion. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked out of the gym and went to your classroom. "
                            pause 2.0
                            jump musicclassfri
                else:
                    " You walked over to her and asked what she was doing. "
                    " Looked like she was very bored... "
                    " You then sat down next to her on the bleachers. "
                    b " Hi there, [name]! "
                    b " I'm kinda bored right now... "
                    b " I don't know what to do... "
                    b " And all of my other friends are off doing their own things... "
                    b " I don't want to bother them, you know? "
                    b " So I'm just out here, relaxing... "
                    b " And also taking a break from my phone! "
                    b " Feels like I've been looking at it too much these past few days... "
                    b " We need breaks from our phones every now and then, too! "
                    b " Can't always be on it, hehe... "
                    b " I mean, I get it if you want the latest news, but... "
                    b " You can also look at the TV for that... "
                    b " Or you can get some news from other people spreading information! "
                    b " We don't ALWAYS need to look at our phones for news! "
                    b " And other stuff, too! "
                    b " You can make art on paper instead of doing it on your phone... "
                    b " You can actually talk to people instead of messaging them... "
                    b " And you can play games with people in real life, too! "
                    b " Like we could play all those good games we played back then when we were kids... "
                    b " Like hide and seek! "
                    b " ...Okay, now listen...before you come at me... "
                    b " I think that you can still play hide and seek and other games, no matter what age you are! "
                    b " As long as you're having fun, then you're all good! "
                    b " Games are meant to make people have fun, after all! "
                    b " Not making people uncomfortable! "
                    b " You can play all sorts of games in real life, too.. "
                    b " Like board games, and other stuff! "
                    b " I personally really liked playing snake and ladders back then. "
                    b " That game was really a classic! "
                    b " I would always play it with my parents... "
                    b " And I would always win! "
                    b " Those times were the best, honestly... "
                    b " Maybe we could play some snakes and ladders sometime, [name]! "
                    b " If I could bring the whole board here, hehe. "
                    b " I don't think my parents would agree cause some stuff would get lost...but... "
                    b " I'll try! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Bubble. "
                    " Just talking about board games you guys liked... "
                    " Pretty cool. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the gym and went to yuor classroom. "
                    pause 2.0
                    jump musicclassfri
                # if no enough love talk normally
            else:
                " You walked over to her and asked what she was doing. "
                " Looked like she was very bored... "
                " You then sat down next to her on the bleachers. "
                x " Hi there, [name]! "
                x " I don't think we've met before, so... "
                $ bubbleknow = True
                b " I'm Bubble - one of your classmates! "
                b " It's nice to meet you!! "
                b " I'm kinda bored right now... "
                b " I don't know what to do... "
                b " And all of my other friends are off doing their own things... "
                b " I don't want to bother them, you know? "
                b " So I'm just out here, relaxing... "
                b " And also taking a break from my phone! "
                b " Feels like I've been looking at it too much these past few days... "
                b " We need breaks from our phones every now and then, too! "
                b " Can't always be on it, hehe... "
                b " I mean, I get it if you want the latest news, but... "
                b " You can also look at the TV for that... "
                b " Or you can get some news from other people spreading information! "
                b " We don't ALWAYS need to look at our phones for news! "
                b " And other stuff, too! "
                b " You can make art on paper instead of doing it on your phone... "
                b " You can actually talk to people instead of messaging them... "
                b " And you can play games with people in real life, too! "
                b " Like we could play all those good games we played back then when we were kids... "
                b " Like hide and seek! "
                b " ...Okay, now listen...before you come at me... "
                b " I think that you can still play hide and seek and other games, no matter what age you are! "
                b " As long as you're having fun, then you're all good! "
                b " Games are meant to make people have fun, after all! "
                b " Not making people uncomfortable! "
                b " You can play all sorts of games in real life, too.. "
                b " Like board games, and other stuff! "
                b " I personally really liked playing snake and ladders back then. "
                b " That game was really a classic! "
                b " I would always play it with my parents... "
                b " And I would always win! "
                b " Those times were the best, honestly... "
                b " Maybe we could play some snakes and ladders sometime, [name]! "
                b " If I could bring the whole board here, hehe. "
                b " I don't think my parents would agree cause some stuff would get lost...but... "
                b " I'll try! "
                scene black with dissolve
                " You spent the rest of the break talking with Bubble. "
                " Just talking about board games you guys liked... "
                " Pretty cool. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to yuor classroom. "
                pause 2.0
                jump musicclassfri
        label mikumonitoringno:
            show lizzyneutral at right with easeinleft
            show petunianeutral at left with easeinleft
            if popularknow == True:
                " You walked over to them and asked them what they were doing. "
                p " Heya there, [name]! "
                lz " Hi there. "
                p " Me and Lizzy were just thinking of what we should do for our next video! "
                p " We could do a trend that's going on right now... "
                p " Honestly? there's always a trend going on. "
                p " As long as there's a good song - then a trend is gonna be made out of it! "
                lz " Yeah, that's true... "
                lz " There have been a lot of trends over the years. "
                lz " I can remember this one iconic one... "
                p " Really, Liz? "
                lz " Yup. I remember it was from this musical. "
                lz " Could remember even animators doing it... "
                lz " There was a lot of creativity going into those animations. "
                lz " And there were cosplays, too. "
                lz " Nowadays... "
                lz " It's kind of just white blonde girls doing trends. "
                lz " Rarely seeing any cosplayers or animators doing anything... "
                lz " Well, unless if the trend gets popular enough. "
                p " Hm, yeah.. "
                p " Sad that we don't get to see much creativity in trends nowadays. "
                p " But can we really do anything about it? "
                lz " Guess not. "
                lz " That's just how things are... "
                p " Yup. "
                p " And trends die out way too quickly in the first place... "
                p " Rarely ever seen one that lasts for a month. "
                p " Sigh... "
                lz " ...Back to the original topic, though. "
                lz " You said you wanted to do a trend? "
                p " Yup yup! "
                p " Even though trends are pretty much boring nowadays... "
                p " They can also get more people to follow you! "
                lz " That IS true... "
                lz " I'll go ahead and look for a trend we could do. "
                p " Yay! thanks, Liz! "
                lz " No problem, Petunia. "
                p " Hehe... "
                scene black with dissolve
                " You spent the rest of the break talking with Lizzy and Petunia. "
                " You also watched them do a trend. "
                " It took them a couple of tries to get it right, but they got it. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom. "
                pause 2.0
                jump musicclassfri
            else:
                " You walked over to them and asked them what they were doing. "
                x " Heya there, [name]! "
                x " Hi there. "
                $ popularknow = True
                p " I'm Petunia! "
                lz " And I'm Lizzy. "
                p " Me and Lizzy were just thinking of what we should do for our next video! "
                p " We could do a trend that's going on right now... "
                p " Honestly? there's always a trend going on. "
                p " As long as there's a good song - then a trend is gonna be made out of it! "
                lz " Yeah, that's true... "
                lz " There have been a lot of trends over the years. "
                lz " I can remember this one iconic one... "
                p " Really, Liz? "
                lz " Yup. I remember it was from this musical. "
                lz " Could remember even animators doing it... "
                lz " There was a lot of creativity going into those animations. "
                lz " And there were cosplays, too. "
                lz " Nowadays... "
                lz " It's kind of just white blonde girls doing trends. "
                lz " Rarely seeing any cosplayers or animators doing anything... "
                lz " Well, unless if the trend gets popular enough. "
                p " Hm, yeah.. "
                p " Sad that we don't get to see much creativity in trends nowadays. "
                p " But can we really do anything about it? "
                lz " Guess not. "
                lz " That's just how things are... "
                p " Yup. "
                p " And trends die out way too quickly in the first place... "
                p " Rarely ever seen one that lasts for a month. "
                p " Sigh... "
                lz " ...Back to the original topic, though. "
                lz " You said you wanted to do a trend? "
                p " Yup yup! "
                p " Even though trends are pretty much boring nowadays... "
                p " They can also get more people to follow you! "
                lz " That IS true... "
                lz " I'll go ahead and look for a trend we could do. "
                p " Yay! thanks, Liz! "
                lz " No problem, Petunia. "
                p " Hehe... "
                scene black with dissolve
                " You spent the rest of the break talking with Lizzy and Petunia. "
                " You also watched them do a trend. "
                " It took them a couple of tries to get it right, but they got it. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom. "
                pause 2.0
                jump musicclassfri
    label cafeteriafri4:
        # cubbie and lana // not interact
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked into the library and spotted two of your classmates doing their own things. "
        " Who do you talk to for this break? "
        if lanaknow == True and cubbieknow == True:
            menu:
                " {image=lanaicon} Lana {image=lanaicon} ":
                    jump laiguana
                " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                    jump iguanarana
        elif lanaknow == True and cubbieknow == False:
            menu:
                " {image=lanaicon} Lana {image=lanaicon} ":
                    jump laiguana
                " {image=cubbieicon} A cat guy! {image=cubbieicon} ":
                    jump iguanarana
        elif lanaknow == False and cubbieknow == True:
            menu:
                " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                    jump laiguana
                " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                    jump iguanarana
        else:
            menu:
                " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                    jump laiguana
                " {image=cubbieicon} A cat guy! {image=cubbieicon} ":
                    jump iguanarana
        label laiguana:
            # lana's ending
            show lananeutral at center with easeinright
            if lanaknow == True:
                pause 0.1
                if lanalv >= 30 or lanalv == 30:
                    " You walked over to her and asked her what she's doing. "
                    " Looked like she wasn't making puppets for once... "
                    " Infact, she was just drawing something on one of her papers. "
                    " Curious to what she's drawing, you got a little more closer to her. "
                    l " Hi there, [name]! "
                    l " Was just doing a little something... "
                    l " I pretty much don't got anything to do for the break, so... "
                    l " I decided to draw the best person in this school! "
                    l " You wanna take a good guess at who that is? "
                    l " I think it's a little obvious... "
                    l " Atleast in my opinion! "
                    " You thought for a good minute at who Lana could draw... "
                    " And then jokingly, you told her that it was you. "
                    " You weren't expecting for it to be right, since it was just a joke. "
                    l " Actually...you're right! "
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " I'm drawing you! "
                    l " I think you've been the best to me, lately... "
                    l " Like, you've been listening to my shows... "
                    l " Spending time with me... "
                    l " I know it's only been a week, but! "
                    l " I've just been feeling really close to you, you know? "
                    l " Like...really close! "
                    l " It's insane how we got like this...cool friendship between us!! "
                    l " And only during a week, too! "
                    l " It's very insane that I got this close with you!! "
                    l " In like a short time!! "
                    l " Can you tell how happy I am right now?? "
                    hide lanahappy at bottom
                    show lananeutral at center
                    l " Uh...wait. I forgot what I was gonna ask you. "
                    l " Lemme think for a bit... "
                    l " Oh, right!! "
                    l " Ya wanna perhaps.... "
                    l " Wanna be best friends??? "
                    menu:
                        " YEEEAHHH ":
                            $ lanasend.grant()
                            hide lananeutral at bottom
                            show lanahappy at center
                            l " Really?? "
                            l " YAY!! "
                            l " Now that you're my best friend...!! "
                            l " I'm gonna let you make some shows like I do!! "
                            l " Isn't that great?? "
                            scene lanaend with dissolve
                            " Congratulations, you've gotten Lana's ending! "
                            " And her achievement, too. Check your achievements page! "
                            " With your new acting companion, you're going to make great shows with her! "
                            " You weren't going for an acting life, but Lana has inspired you to make your own stories. "
                            jump credits
                        " i dont know you well enough sorry ":
                            l " Oh, uh... "
                            l " That's completely fine!! "
                            l " I understand why since like...you know... "
                            l " It's only been a week! "
                            l " Not really a week but like...during a week??? "
                            l " Sorry, my words are fumbling, hehe... "
                            l " You wanna see me complete this drawing though? "
                            l " I'm working really hard on it! "
                            " Of course you wanted to see her drawing. "
                            " You looked closer so that you could get a better look at it... "
                            scene black with dissolve
                            " You spent the rest of the break talking with Lana and watched her draw. "
                            " The drawing of you was actually really well made... "
                            " If you could, you wanted to get a copy of it tapes onto your wall. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked out of the cafeteria before going to your classroom. "
                            pause 2.0
                            jump musicclassfri
                else:
                    " You walked over to her and asked her what she was doing. "
                    " Looked like she was looking for something... "
                    " You might be able to help with this. "
                    l " Oh, hey there, [name]! "
                    l " I'm in quite of a pickle right now... "
                    l " That. That term is so weird to say. "
                    l " But really - I'm in some trouble right now... "
                    l " Not actually in trouble as in with teachers, but... "
                    l " You know how I make sock puppets? "
                    l " So...I may or may not have lost one of my decorations. "
                    l " You know, what makes my sock puppets unique! "
                    l " Someone might've already taken it... "
                    l " I mean - I'm not TOO upset that I lost it, but... "
                    hide lananeutral at bottom
                    show lanaangry at center
                    l " Getting new materials is a pain, you know! "
                    l " Especially when you don't have enough money... "
                    l " God, it's frustrating to deal with. "
                    l " That's why I kind of need your help finding the decorations I lost. "
                    hide lanaangry at bottom
                    show lananeutral at center
                    l " I'm sure I can't really look through the entire cafeteria alone... "
                    l " It's going to take me too long that way! "
                    l " Besides... "
                    l " It's a little embarrassing having to ask every single person in the room. "
                    l " Like, I don't talk to people that much... "
                    l " So it's pretty much awkward for me. "
                    l " Hope you understand that. "
                    l " If I'm not bothering you right now... "
                    l " Could you help me on this? "
                    l " I'll pay you after this, I swear! "
                    l " I've got an extra 20$! "
                    l " So...what do you say? "
                    " Well, you don't have much to do for this break, so... "
                    " You agreed on helping her. "
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " Yaaay, thanks!! "
                    l " I'll be looking everywhere in the cafeteria... "
                    l " And you can just go and ask everyone if they've seen anything!! "
                    l " READY SET GO!! "
                    hide lanahappy at right with easeoutright
                    " And with that, she skedaddled away. "
                    " You then started asking people, as you were tasked... "
                    scene black with dissolve
                    " You spent the rest of the break asking people around for Lana's decorations. "
                    " And eventually, you got this one person who had gotten her decorations. "
                    " You got the decorations and gave it back to Lana, who was very happy that you found it. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the cafeteria and went to your classroom. "
                    pause 2.0
                    jump musicclassfri
            else:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was looking for something... "
                " You might be able to help with this. "
                x " Oh, hey there, [name]! "
                $ lanaknow = True
                l " I'm Lana, and uh... "
                l " I'm in quite of a pickle right now... "
                l " That. That term is so weird to say. "
                l " But really - I'm in some trouble right now... "
                l " Not actually in trouble as in with teachers, but... "
                l " You know how I make sock puppets? "
                l " So...I may or may not have lost one of my decorations. "
                l " You know, what makes my sock puppets unique! "
                l " Someone might've already taken it... "
                l " I mean - I'm not TOO upset that I lost it, but... "
                hide lananeutral at bottom
                show lanaangry at center
                l " Getting new materials is a pain, you know! "
                l " Especially when you don't have enough money... "
                l " God, it's frustrating to deal with. "
                l " That's why I kind of need your help finding the decorations I lost. "
                hide lanaangry at bottom
                show lananeutral at center
                l " I'm sure I can't really look through the entire cafeteria alone... "
                l " It's going to take me too long that way! "
                l " Besides... "
                l " It's a little embarrassing having to ask every single person in the room. "
                l " Like, I don't talk to people that much... "
                l " So it's pretty much awkward for me. "
                l " Hope you understand that. "
                l " If I'm not bothering you right now... "
                l " Could you help me on this? "
                l " I'll pay you after this, I swear! "
                l " I've got an extra 20$! "
                l " So...what do you say? "
                " Well, you don't have much to do for this break, so... "
                " You agreed on helping her. "
                hide lananeutral at bottom
                show lanahappy at center
                l " Yaaay, thanks!! "
                l " I'll be looking everywhere in the cafeteria... "
                l " And you can just go and ask everyone if they've seen anything!! "
                l " READY SET GO!! "
                hide lanahappy at right with easeoutright
                " And with that, she skedaddled away. "
                " You then started asking people, as you were tasked... "
                scene black with dissolve
                " You spent the rest of the break asking people around for Lana's decorations. "
                " And eventually, you got this one person who had gotten her decorations. "
                " You got the decorations and gave it back to Lana, who was very happy that you found it. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classroom. "
                pause 2.0
                jump musicclassfri
        label iguanarana:
            show cubbieneutralb2 at center with easeinleft
            if cubbieknow == True:
                " You walked over to him, and... "
                " Wait, is he sleeping? "
                cb " ... "
                " You took a closer look at him... "
                " Yeah, he's definitely sleeping. "
                " You wonder how he could sleep in such a noisy place... "
                " But honestly, sleeping in school is so real. "
                " Like for some reason... "
                " The seats in school are just good sleeping material. "
                " Like real good sleeping material. "
                " They hit harder than your own bed, even. "
                " Everyone has atleast one expirience of sleeping in class. "
                " There's no way you haven't done that. "
                " If you didn't sleep in class then you're lying. "
                " I am NOT believing you. "
                " Anyway... "
                " You pretty much had no idea what to do while Cubbie's asleep. "
                " You also didn't want to disturb his sleep. "
                " Like come on...he's clearly getting that quality rest over there. "
                " You didn't want to ruin that for him. "
                " All you could do is just...kinda relax here. "
                " Like, I don't know...think about life. "
                " And your choices in this game so far. "
                " Why'd you play this game again? "
                " You wanted to play a FPE dating sim? "
                " Wow, yeah, that reason is pretty goofy now that you think about it more. "
                " I mean, this isn't a dating sim but atleast you've got something to play now. "
                " This is a befriending sim instead of a dating sim. "
                " An FPE game where you can actually interact with other characters... "
                " Like Cubbie over here for example. "
                " ...I'm just rambling to you at this point, actually. "
                " Little Alice talking too much again. "
                " To the people who didn't know that I'm the narrator here, get surprised. "
                " Yes, I'm the narrator for the normal route and teacher route. "
                " I might have given someone spoilers but I'd hardly believe someone would want to go for Cubbie first, so...yeah. "
                " There's someone else who takes over the narrator role for the OC route. "
                " I'll let you figure that out. "
                scene black with dissolve
                " You spent the rest of the break just scrolling on your phone... "
                " And also seeing if Cubbie would wake up or not. "
                " Geez, he's really getting that good rest... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classroom. "
                pause 2.0
                jump musicclassfri
            else:
                " Oh hey, you've seen this guy before. "
                $ cubbieknow = True
                " His name is Cubbie. "
                " He doesn't really talk much. "
                " You walked over to him, and... "
                " Wait, is he sleeping? "
                cb " ... "
                " You took a closer look at him... "
                " Yeah, he's definitely sleeping. "
                " You wonder how he could sleep in such a noisy place... "
                " But honestly, sleeping in school is so real. "
                " Like for some reason... "
                " The seats in school are just good sleeping material. "
                " Like real good sleeping material. "
                " They hit harder than your own bed, even. "
                " Everyone has atleast one expirience of sleeping in class. "
                " There's no way you haven't done that. "
                " If you didn't sleep in class then you're lying. "
                " I am NOT believing you. "
                " Anyway... "
                " You pretty much had no idea what to do while Cubbie's asleep. "
                " You also didn't want to disturb his sleep. "
                " Like come on...he's clearly getting that quality rest over there. "
                " You didn't want to ruin that for him. "
                " All you could do is just...kinda relax here. "
                " Like, I don't know...think about life. "
                " And your choices in this game so far. "
                " Why'd you play this game again? "
                " You wanted to play a FPE dating sim? "
                " Wow, yeah, that reason is pretty goofy now that you think about it more. "
                " I mean, this isn't a dating sim but atleast you've got something to play now. "
                " This is a befriending sim instead of a dating sim. "
                " An FPE game where you can actually interact with other characters... "
                " Like Cubbie over here for example. "
                " ...I'm just rambling to you at this point, actually. "
                " Little Alice talking too much again. "
                " To the people who didn't know that I'm the narrator here, get surprised. "
                " Yes, I'm the narrator for the normal route and teacher route. "
                " I might have given someone spoilers but I'd hardly believe someone would want to go for Cubbie first, so...yeah. "
                " There's someone else who takes over the narrator role for the OC route. "
                " I'll let you figure that out. "
                scene black with dissolve
                " You spent the rest of the break just scrolling on your phone... "
                " And also seeing if Cubbie would wake up or not. "
                " Geez, he's really getting that good rest... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classroom. "
                pause 2.0
                jump musicclassfri
    label rooftopfri4:
        # kevin and robby // interact
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked onto the rooftop and spotted two of your classmates talking to eachother. "
        " Wondering what they're talking about, you walked over to them. "
        show kevinneutral at left with easeinright
        show robbyneutral at right with easeinright
        if kevinknow == True and robbyknow == True:
            " Looks like they're discussing something important. "
            " You don't think you'll be apart of their conversation, so... "
            " You just decided to listen in, for now. "
            " Until they notice you, atleast. "
            kv " Being honest with you, Robby... "
            kv " I don't really think aesthetics matter that much, honestly.. "
            kv " I mean - yes, it gives the thing you're making a theme, but... "
            kv " Overall? it's only so that it makes the thing you have looks nice. "
            kv " Nice to the people who like the vibe of your theme. "
            kv " But if I had to choose a theme or something... "
            kv " I think I'd pick the one that's like... "
            kv " What's it called again? dark something. "
            rb " I think you might be looking for dark academia, Kevin. "
            rb " Lots of people actually like that theme. "
            kv " Oh really? "
            kv " I mean, I can see why. "
            rb " Mhm. "
            rb " Don't tell anyone about what I like, but... "
            rb " Surpisingly, I like frutiger aero stuff. "
            kv " What's that you said...? "
            kv " I don't think I really understood. "
            rb " Frutiger aero. "
            rb " To put it simply - it's kinda futuristic. "
            rb " But in the way of how aesthetic 2000's people would imagine. "
            rb " Like old vibes, old aesthetics...crunchy windows sound effects... "
            kv " Huh, interesting. "
            kv " Wasn't there subtypes for that theme? "
            kv " From what I remember, there was. "
            rb " Yup, there's a whole lot of them. "
            rb " I personally like Cyber Angel...more known as Frutiger Angelic. "
            rb " Not much people talk about it, but it's interesting. "
            kv " Do you think there's a type that I would like? "
            rb " Hm... "
            rb " You look like you'd like Dark Aero or Frutiger Eco. "
            rb " Dark Aero is basically the emo version and Frutiger Eco is more on about plants. "
            kv " Huh... "
            rb " People also make playlists based off of the types. "
            rb " Mostly frutiger aero though. "
            kv " Maybe I should check it out, then. "
            kv " Who knows - maybe it could be my thing. "
            rb " Most of the playlists I've heard were pretty relaxing. "
            rb " I even sometimes listen to them while I'm working on something. "
            rb " Really helps calm down the stress while I'm working. "
            kv " Hmmm... "
            kv " Perhaps I could use this for studying. "
            rb " Sure, you can do that. "
            rb " Whatever makes you think better. "
            scene black with dissolve
            " You spent the rest of the break talking with Robby and Kevin, after they noticed you. "
            " Honestly, you look like a Frutiger Metro type of [person]. "
            " Maybe you should check out some of this frutiger stuff when you have the time. "
            " It sounds cool. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and went to your classroom. "
            pause 2.0
            jump musicclassfri
        elif kevinknow == True and robbyknow == False:
            " Looks like they're discussing something important. "
            " You don't think you'll be apart of their conversation, so... "
            " You just decided to listen in, for now. "
            " Until they notice you, atleast. "
            $ robbyknow = True
            kv " Being honest with you, Robby... "
            kv " I don't really think aesthetics matter that much, honestly.. "
            kv " I mean - yes, it gives the thing you're making a theme, but... "
            kv " Overall? it's only so that it makes the thing you have looks nice. "
            kv " Nice to the people who like the vibe of your theme. "
            kv " But if I had to choose a theme or something... "
            kv " I think I'd pick the one that's like... "
            kv " What's it called again? dark something. "
            rb " I think you might be looking for dark academia, Kevin. "
            rb " Lots of people actually like that theme. "
            kv " Oh really? "
            kv " I mean, I can see why. "
            rb " Mhm. "
            rb " Don't tell anyone about what I like, but... "
            rb " Surpisingly, I like frutiger aero stuff. "
            kv " What's that you said...? "
            kv " I don't think I really understood. "
            rb " Frutiger aero. "
            rb " To put it simply - it's kinda futuristic. "
            rb " But in the way of how aesthetic 2000's people would imagine. "
            rb " Like old vibes, old aesthetics...crunchy windows sound effects... "
            kv " Huh, interesting. "
            kv " Wasn't there subtypes for that theme? "
            kv " From what I remember, there was. "
            rb " Yup, there's a whole lot of them. "
            rb " I personally like Cyber Angel...more known as Frutiger Angelic. "
            rb " Not much people talk about it, but it's interesting. "
            kv " Do you think there's a type that I would like? "
            rb " Hm... "
            rb " You look like you'd like Dark Aero or Frutiger Eco. "
            rb " Dark Aero is basically the emo version and Frutiger Eco is more on about plants. "
            kv " Huh... "
            rb " People also make playlists based off of the types. "
            rb " Mostly frutiger aero though. "
            kv " Maybe I should check it out, then. "
            kv " Who knows - maybe it could be my thing. "
            rb " Most of the playlists I've heard were pretty relaxing. "
            rb " I even sometimes listen to them while I'm working on something. "
            rb " Really helps calm down the stress while I'm working. "
            kv " Hmmm... "
            kv " Perhaps I could use this for studying. "
            rb " Sure, you can do that. "
            rb " Whatever makes you think better. "
            scene black with dissolve
            " You spent the rest of the break talking with Robby and Kevin, after they noticed you. "
            " Honestly, you look like a Frutiger Metro type of [person]. "
            " Maybe you should check out some of this frutiger stuff when you have the time. "
            " It sounds cool. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and went to your classroom. "
            pause 2.0
            jump musicclassfri
        elif kevinknow == False and robbyknow == True:
            " Looks like they're discussing something important. "
            " You don't think you'll be apart of their conversation, so... "
            " You just decided to listen in, for now. "
            " Until they notice you, atleast. "
            x " Being honest with you, Robby... "
            x " I don't really think aesthetics matter that much, honestly.. "
            x " I mean - yes, it gives the thing you're making a theme, but... "
            x " Overall? it's only so that it makes the thing you have looks nice. "
            x " Nice to the people who like the vibe of your theme. "
            x " But if I had to choose a theme or something... "
            x " I think I'd pick the one that's like... "
            x " What's it called again? dark something. "
            $ kevinknow = True
            rb " I think you might be looking for dark academia, Kevin. "
            rb " Lots of people actually like that theme. "
            kv " Oh really? "
            kv " I mean, I can see why. "
            rb " Mhm. "
            rb " Don't tell anyone about what I like, but... "
            rb " Surpisingly, I like frutiger aero stuff. "
            kv " What's that you said...? "
            kv " I don't think I really understood. "
            rb " Frutiger aero. "
            rb " To put it simply - it's kinda futuristic. "
            rb " But in the way of how aesthetic 2000's people would imagine. "
            rb " Like old vibes, old aesthetics...crunchy windows sound effects... "
            kv " Huh, interesting. "
            kv " Wasn't there subtypes for that theme? "
            kv " From what I remember, there was. "
            rb " Yup, there's a whole lot of them. "
            rb " I personally like Cyber Angel...more known as Frutiger Angelic. "
            rb " Not much people talk about it, but it's interesting. "
            kv " Do you think there's a type that I would like? "
            rb " Hm... "
            rb " You look like you'd like Dark Aero or Frutiger Eco. "
            rb " Dark Aero is basically the emo version and Frutiger Eco is more on about plants. "
            kv " Huh... "
            rb " People also make playlists based off of the types. "
            rb " Mostly frutiger aero though. "
            kv " Maybe I should check it out, then. "
            kv " Who knows - maybe it could be my thing. "
            rb " Most of the playlists I've heard were pretty relaxing. "
            rb " I even sometimes listen to them while I'm working on something. "
            rb " Really helps calm down the stress while I'm working. "
            kv " Hmmm... "
            kv " Perhaps I could use this for studying. "
            rb " Sure, you can do that. "
            rb " Whatever makes you think better. "
            scene black with dissolve
            " You spent the rest of the break talking with Robby and Kevin, after they noticed you. "
            " Honestly, you look like a Frutiger Metro type of [person]. "
            " Maybe you should check out some of this frutiger stuff when you have the time. "
            " It sounds cool. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and went to your classroom. "
            pause 2.0
            jump musicclassfri
        else:
            " Looks like they're discussing something important. "
            " You don't think you'll be apart of their conversation, so... "
            " You just decided to listen in, for now. "
            " Until they notice you, atleast. "
            $ robbyknow = True
            $ kevinknow = True
            x " Being honest with you, Robby... "
            x " I don't really think aesthetics matter that much, honestly.. "
            x " I mean - yes, it gives the thing you're making a theme, but... "
            x " Overall? it's only so that it makes the thing you have looks nice. "
            x " Nice to the people who like the vibe of your theme. "
            x " But if I had to choose a theme or something... "
            x " I think I'd pick the one that's like... "
            x " What's it called again? dark something. "
            rb " I think you might be looking for dark academia, Kevin. "
            rb " Lots of people actually like that theme. "
            kv " Oh really? "
            kv " I mean, I can see why. "
            rb " Mhm. "
            rb " Don't tell anyone about what I like, but... "
            rb " Surpisingly, I like frutiger aero stuff. "
            kv " What's that you said...? "
            kv " I don't think I really understood. "
            rb " Frutiger aero. "
            rb " To put it simply - it's kinda futuristic. "
            rb " But in the way of how aesthetic 2000's people would imagine. "
            rb " Like old vibes, old aesthetics...crunchy windows sound effects... "
            kv " Huh, interesting. "
            kv " Wasn't there subtypes for that theme? "
            kv " From what I remember, there was. "
            rb " Yup, there's a whole lot of them. "
            rb " I personally like Cyber Angel...more known as Frutiger Angelic. "
            rb " Not much people talk about it, but it's interesting. "
            kv " Do you think there's a type that I would like? "
            rb " Hm... "
            rb " You look like you'd like Dark Aero or Frutiger Eco. "
            rb " Dark Aero is basically the emo version and Frutiger Eco is more on about plants. "
            kv " Huh... "
            rb " People also make playlists based off of the types. "
            rb " Mostly frutiger aero though. "
            kv " Maybe I should check it out, then. "
            kv " Who knows - maybe it could be my thing. "
            rb " Most of the playlists I've heard were pretty relaxing. "
            rb " I even sometimes listen to them while I'm working on something. "
            rb " Really helps calm down the stress while I'm working. "
            kv " Hmmm... "
            kv " Perhaps I could use this for studying. "
            rb " Sure, you can do that. "
            rb " Whatever makes you think better. "
            scene black with dissolve
            " You spent the rest of the break talking with Robby and Kevin, after they noticed you. "
            " Honestly, you look like a Frutiger Metro type of [person]. "
            " Maybe you should check out some of this frutiger stuff when you have the time. "
            " It sounds cool. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and went to your classroom. "
            pause 2.0
            jump musicclassfri
    label libraryfri4:
        # engel and riley // not interact
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked to the library and spotted two of your classmates doing their own things. "
        " Who do you want to talk to for this break? "
        if engelknow == True and rileyknow == True:
            menu:
                " {image=engelicon} Engel {image=engelicon} ":
                    jump plumberbroom
                " {image=rileyicon} Riley {image=rileyicon} ":
                    jump engineerbroom
        elif engelknow == True and rileyknow == False:
            menu:
                " {image=engelicon} Engel {image=engelicon} ":
                    jump plumberbroom
                " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                    jump engineerbroom
        elif engelknow == False and rileyknow == True:
            menu:
                " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                    jump plumberbroom
                " {image=rileyicon} Riley {image=rileyicon} ":
                    jump engineerbroom
        else:
            menu:
                " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                    jump plumberbroom
                " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                    jump engineerbroom
        label plumberbroom:
            # engel's ending
            show engelneutral at center with easeinleft
            if engelknow == True:
                pause 0.1
                if engellv >= 30 or engellv == 30:
                    " You walked over to him and asked him what he was doing. "
                    " Looked like he was thinking about a few things... "
                    " He didn't respond to you the first time you asked, so you asked him again. "
                    " This time while shaking him a little. "
                    e " Huh? oh! "
                    hide engelneutral at bottom
                    show engelhappy at center
                    e " Sorry if I was keeping you waiting, [name]... "
                    e " A lot has been on my mind, lately. "
                    e " Just thinking about some stuff like schoolwork, and... "
                    e " (God, this is really embarrassing.) "
                    e " (Come on, Engel...you can do this.) "
                    e " (You've been practicing this in your head for awhile now...) "
                    e " (There's nothing to be afraid of.) "
                    e " (Just think...like you're talking to Claire.) "
                    e " (Everything should go fine and well.) "
                    e " ...Let me just, breathe for a momemt. "
                    " You let Engel breathe for a minute. "
                    " There's a whole lot of stuff in his head, so you wanted him to clear some stuff out before talking. "
                    " You know how difficult some stuff is...like talking about certain things. "
                    " So you waited patiently for when he was ready. "
                    scene engelending1 with dissolve
                    e " Whew...okay... "
                    e " Think I'm ready enough. "
                    e " So... "
                    e " You know how I've been thinking a lot lately, right? "
                    e " And...um... "
                    e " It's been surprising how you've gotten this close to me in 4 days, ahha... "
                    e " And I've been thinking about asking you this... "
                    e " For awhile now. "
                    e " I hope this isn't too sudden, but... "
                    e " Would you like to be my best friend...? "
                    e " It's just that...you've been making my days more brighter. "
                    e " I've even caught myself smiling more because of you... "
                    e " It's okay if you don't want to be my best friend! "
                    e " I know that it's way too soon for that, so... "
                    e " (I'm not expecting anything too much from this...) "
                    e " (But I hope [they] say yes.) "
                    menu:
                        " YEAAAHHH!! ":
                            scene engelending2 with dissolve
                            $ engelsend.grant()
                            e " Hold on, really? "
                            e " Uh...I actually didn't expect for you to say that, but... "
                            e " I'm happy that I'm your best friend now. "
                            e " You wanna...maybe...hangout after school for a bit? "
                            e " If you're free, of course. "
                            " Congratulations, you've gotten Engel's ending! "
                            " And also the privilege to copy his homework. "
                            " And also also his achievement! go ahead and check your achievements tab! "
                            " He'll help you with your homework anytime, and he'll be there to comfort you. "
                            " You're going to have one strong friendship with him! "
                            jump credits
                        " nah sorry it's only been 4 days ":
                            scene engelending3 with dissolve
                            e " Ah... "
                            e " Okay, that's understandable. "
                            e " Let's just be normal friends then? "
                            e " (I knew it was too soon.) "
                            e " (Maybe I shouldn't have asked in the first place...) "
                            e " (Atleast I'm still friends with [them] though.) "
                            e " Hm...let's maybe clean up the library a bit to pass time. "
                            e " I don't want you to just stand there and do nothing, after all. "
                            e " The library's been getting really dusty lately anyway... "
                            " You agreed to help Engel clean. "
                            scene black with dissolve
                            " You spent the rest of the break cleaning library with Engel. "
                            " Just cleaning some of the dust bunnies you saw... "
                            " And also rearranging some books. "
                            " Some idiots misplaced them. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked out of the library and went to your classroom. "
                            pause 2.0
                            jump musicclassfri
                else:
                    " You walked over to him and asked him what he was doing. "
                    " Looked like he was cleaning up the library a bit... "
                    " You swear you've seen someone clean up this library twice now. "
                    hide engelneutral at bottom
                    show engelhappy at center
                    e " Oh, hello there, [name]. "
                    e " I just decided to clean the library... "
                    e " It's been really dusty lately. "
                    e " I mean, a few people have cleaned this library including me before, yes... "
                    e " But it just keeps getting dusty over and over again. "
                    e " Either someone's pouring buckets of dust everytime its class hours... "
                    e " Or the library's just like this. "
                    e " It probably just likes watching me suffer... "
                    e " But anyway. "
                    e " As a person who likes seeing things clean... "
                    e " And as a person who likes the library... "
                    e " You can tell how much of a pain this is for me. "
                    e " So, I'm going to be cleaning this library slowly... "
                    e " ...Though I could use more help here. "
                    e " I don't want to be cleaning for the entire break, after all. "
                    e " I want to get atleast a bit of rest in... "
                    e " A break is supposed to be a time where the students can rest, not work. "
                    e " So...if you don't mind... "
                    e " Could you help me out here, [name]? "
                    e " If it doesn't bother you. "
                    e " Two people cleaning could make this whole process faster. "
                    e " And I could maybe give you a little snack after you're done... "
                    e " I've got extra coffee candy in my pocket. "
                    " ...You really want that coffee candy. "
                    " You agreed to helping him and immediately got a feather duster. "
                    e " ...Never knew you liked coffee candy. "
                    e " But, thanks for the help, [name]. "
                    e " I'll clean the right side, and you can clean the left side. "
                    e " Just tell me when you're done. "
                    hide engelhappy at right with easeoutright
                    " And Engel goes to clean... "
                    " You started cleaning on the left side of the library. "
                    " All for that coffee candy. What? it tastes good. "
                    scene black with dissolve
                    " You spent the rest of the break helping Engel clean the library. "
                    " You got done pretty fast, and you went over to Engel's side to help. "
                    " Engel gave you two coffee candies just for that. Yay! "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the library and went back to your classroom. "
                    pause 2.0
                    jump musicclassfri
            else:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was cleaning up the library a bit... "
                " You swear you've seen someone clean up this library twice now. "
                hide engelneutral at bottom
                show engelhappy at center
                x " Oh, hello there, [name]. "
                $ engelknow = True
                e " I'm Engel, it's nice to meet you. "
                e " I just decided to clean the library... "
                e " It's been really dusty lately. "
                e " I mean, a few people have cleaned this library including me before, yes... "
                e " But it just keeps getting dusty over and over again. "
                e " Either someone's pouring buckets of dust everytime its class hours... "
                e " Or the library's just like this. "
                e " It probably just likes watching me suffer... "
                e " But anyway. "
                e " As a person who likes seeing things clean... "
                e " And as a person who likes the library... "
                e " You can tell how much of a pain this is for me. "
                e " So, I'm going to be cleaning this library slowly... "
                e " ...Though I could use more help here. "
                e " I don't want to be cleaning for the entire break, after all. "
                e " I want to get atleast a bit of rest in... "
                e " A break is supposed to be a time where the students can rest, not work. "
                e " So...if you don't mind... "
                e " Could you help me out here, [name]? "
                e " If it doesn't bother you. "
                e " Two people cleaning could make this whole process faster. "
                e " And I could maybe give you a little snack after you're done... "
                e " I've got extra coffee candy in my pocket. "
                " ...You really want that coffee candy. "
                " You agreed to helping him and immediately got a feather duster. "
                e " ...Never knew you liked coffee candy. "
                e " But, thanks for the help, [name]. "
                e " I'll clean the right side, and you can clean the left side. "
                e " Just tell me when you're done. "
                hide engelhappy at right with easeoutright
                " And Engel goes to clean... "
                " You started cleaning on the left side of the library. "
                " All for that coffee candy. What? it tastes good. "
                scene black with dissolve
                " You spent the rest of the break helping Engel clean the library. "
                " You got done pretty fast, and you went over to Engel's side to help. "
                " Engel gave you two coffee candies just for that. Yay! "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the library and went back to your classroom. "
                pause 2.0
                jump musicclassfri
        label engineerbroom:
            show rileyneutral at center with easeinright
            if rileyknow == True:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was staring at a photo of Oliver... "
                " You have a feeling she's done this multiple times before. "
                ri " Hhhh...hi there, [name]!! "
                ri " You know... "
                ri " With how addicted I am with Oliver - "
                ri " You'd think I know everything about him! "
                ri " But everytime I look at a new photo of him... "
                ri " I keep on spotting something new! "
                ri " Like what kind of food he likes to eat... "
                ri " Like, he didn't tell me he likes to eat grass??? "
                ri " What the helly?? "
                ri " But, I guess it's a good thing that I'm learning more things about him... "
                ri " It means that I'm getting closer and closer to knowing absolutely everything about him! "
                ri " And that means... "
                ri " As soon as I know everything about him... "
                ri " There's a lower chance of me getting the things he likes wrong! "
                ri " My Oliver deserves the utter best!! "
                ri " That's why I want to know everything about him! "
                ri " No mistakes for my Oliver... "
                ri " He deserves utter perfection! "
                ri " And, heh... "
                ri " I'm perfection, no offense to anyone else out there. "
                ri " Sorry - but he's mine. "
                ri " I've gotta find out more about my sweet Oliver! "
                ri " I need every single thing that I can find about him. "
                ri " And I mean every single thing. "
                ri " I'm not letting a single fact run away! "
                ri " Hehe... "
                " Wow, this girl is insane. "
                " Atleast you're not someone like this. "
                " I'd be really concerned if you were. "
                ri " I should feed him some soap later! "
                ri " Do you think he'd like the pink soap or the white soap? "
                ri " ...Actually, he'd like any kind of soap now that I think about it! "
                ri " Except for that one where it's orange and tastes bad. "
                ri " I'm pretty sure that one was just for the skin. "
                ri " Like...as in skin care and not meant for actual eating. "
                ri " I'll get him some soap later on the way home, hehe!! "
                scene black with dissolve
                " You spent the rest of the break talking to Riley. "
                " Just talking about Oliver... "
                " Nothing interesting, really. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for the next class. "
                " You walked out of the library and went to your classroom. "
                pause 2.0
                jump musicclassfri
            else:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was staring at a photo of Oliver... "
                " You have a feeling she's done this multiple times before. "
                x " Hhhh...hi there, [name]!! "
                $ rileyknow = True
                ri " I'm Riley!! Oliver's wife and girlfriend!! "
                ri " You know... "
                ri " With how addicted I am with Oliver - "
                ri " You'd think I know everything about him! "
                ri " But everytime I look at a new photo of him... "
                ri " I keep on spotting something new! "
                ri " Like what kind of food he likes to eat... "
                ri " Like, he didn't tell me he likes to eat grass??? "
                ri " What the helly?? "
                ri " But, I guess it's a good thing that I'm learning more things about him... "
                ri " It means that I'm getting closer and closer to knowing absolutely everything about him! "
                ri " And that means... "
                ri " As soon as I know everything about him... "
                ri " There's a lower chance of me getting the things he likes wrong! "
                ri " My Oliver deserves the utter best!! "
                ri " That's why I want to know everything about him! "
                ri " No mistakes for my Oliver... "
                ri " He deserves utter perfection! "
                ri " And, heh... "
                ri " I'm perfection, no offense to anyone else out there. "
                ri " Sorry - but he's mine. "
                ri " I've gotta find out more about my sweet Oliver! "
                ri " I need every single thing that I can find about him. "
                ri " And I mean every single thing. "
                ri " I'm not letting a single fact run away! "
                ri " Hehe... "
                " Wow, this girl is insane. "
                " Atleast you're not someone like this. "
                " I'd be really concerned if you were. "
                ri " I should feed him some soap later! "
                ri " Do you think he'd like the pink soap or the white soap? "
                ri " ...Actually, he'd like any kind of soap now that I think about it! "
                ri " Except for that one where it's orange and tastes bad. "
                ri " I'm pretty sure that one was just for the skin. "
                ri " Like...as in skin care and not meant for actual eating. "
                ri " I'll get him some soap later on the way home, hehe!! "
                scene black with dissolve
                " You spent the rest of the break talking to Riley. "
                " Just talking about Oliver... "
                " Nothing interesting, really. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for the next class. "
                " You walked out of the library and went to your classroom. "
                pause 2.0
                jump musicclassfri

label musicclassfri:
    scene classroom with dissolve
    " You walked into the classroom, and...hold on. "
    " Where's the teacher? "
    " Oh wait, there's a note on his desk. "
    " Looks like he isn't gonna be in for the day. "
    " Said that he needed a break for a bit. "
    " But he did say that you needed to copy a few things... "
    " And the few things being underneath that note he wrote. "
    " You took the picture of the stuff, and went to your seat to copy... "
    scene black with dissolve
    " Yet again, you spent the class time copying down notes. "
    " Atleast this is better than doing projects for class. "
    " You didn't have to do much this way. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, time for another break. "
    " You got off of your chair and went to the hallway. "
    pause 2.0
    jump fribreak5

label fribreak5:
    # the other endings for the characters
    scene hallway with dissolve
    if oligangjoin == True:
        " The room's still empty... "
        " Let's go somewhere else. "
        pass
    else:
        pass
    " Where are you gonna hang out for this break? "
    menu:
        " {image=popularicon} The front of the school {image=cubbieicon} ":
            jump frontschoolfri5
        " {image=claireicon} The back of the school {image=kevinicon} ":
            jump backschoolfri5
        " {image=rubyicon} The gym {image=engelicon} ":
            jump gymfri5
        " {image=robbyicon} The cafeteria {image=rileyicon} ":
            jump cafeteriafri5
        " {image=bubbleicon} The rooftop {image=skellicon} ":
            jump rooftopfri5
        " {image=lanaicon} The library {image=abbieicon} ":
            jump libraryfri5
    label frontschoolfri5:
        # petunia lizzy and cubbie
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked over to the front of the school and found three of your classmates doing their own things. "
        " Who would you like to talk to for this break? "
        if popularknow == True and cubbieknow == True:
            menu:
                " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                    jump buffpomniya
                " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                    jump buffkingerya
        elif popularknow == True and cubbieknow == False:
                menu:
                    " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                        jump buffpomniya
                    " {image=cubbieicon} A cat guy! {image=cubbieicon} ":
                        jump buffkingerya
        elif popularknow == False and cubbieknow == True:
                menu:
                    " {image=popularicon} The popular girls {image=popularicon} ":
                        jump buffpomniya
                    " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                        jump buffkingerya
        else:
            menu:
                " {image=popularicon} The popular girls {image=popularicon} ":
                    jump buffpomniya
                " {image=cubbieicon} A cat guy! {image=cubbieicon} ":
                    jump buffkingerya
        label buffpomniya:
            show petunianeutral at left with easeinright
            show lizzyneutral at right with easeinright
            if popularknow == True:
                pause 0.1
                if popularlv >= 30 or popularlv == 30:
                    " You walked over to them and asked what they were doing. "
                    " Looked like they were trying to take a photo... "
                    " ...But they just couldn't get the right angle for them. "
                    p " Heyaaa, [name]!! "
                    lz " Hi there. "
                    p " Me and Lizzy were trying to find the right angle... "
                    p " Cause we were talking a selfie, right? "
                    lz " But we just couldn't get it right, "
                    lz " Which is surprising because we look good in every single angle. "
                    p " But! we realized something was missing... "
                    lz " A very important thing for this photo was gone. "
                    p " And we were about to look for it! "
                    p " But you wanna know what happened? "
                    lz " Turns out, the thing that we were missing, was... "
                    hide petunianeutral at bottom
                    hide lizzyneutral at bottom
                    show petuniahappy at left
                    show lizzyhappy at right
                    p " You! "
                    p " We can't just leave a diva like you out! "
                    lz " Yeah, that would be really bad. "
                    lz " Leaving out someone like you would be a huge mistake. "
                    p " Especially after all you've done for us! "
                    p " We can't thank you enough, [name]! "
                    lz " We don't do this often, but... "
                    lz " We'd like to give you an offer. "
                    p " We're not gonna ask you this again soon, so... "
                    p " You happen to want to be besties with us? "
                    lz " I mean, you're a homie, yes... "
                    lz " But not a bestie. "
                    hide petuniahappy at bottom
                    hide lizzyhappy at bottom
                    show petunianeutral at left
                    show lizzyneutral at right
                    p " We promise that we'll lend you, like... "
                    p " 20$ per day! "
                    lz " Trust me, we have a lot to spend. "
                    lz " So...what do you say? "
                    menu:
                        " BESTIES 4 LIFE !! ":
                            $ popularsend.grant()
                            hide petunianeutral at bottom
                            hide lizzyneutral at bottom
                            show petuniahappy at left
                            show lizzyhappy at right
                            p " Oh, hell yeah! "
                            p " We knew you would say yes! "
                            lz " You could never resist us. "
                            lz " We're just that amazing. "
                            p " Like, literally amazing. "
                            p " Now you can be amazing with us! "
                            lz " Come here [name], "
                            lz " We still need you for our cool photo. "
                            p " Yeah, and make sure you make yourself look good! "
                            p " As if you don't look good enough... "
                            lz " Alright, three, two, one... "
                            p " BESTIES 4 LIFE!! "
                            lz " Besties 4 life. "
                            " Best friends 4ever!! "
                            scene popularend with dissolve
                            " Congratulations - you've gotten Petunia and Lizzy's ending! "
                            " Now you can be literally amazing with them... "
                            " And you've also got their literally amazing achievement. "
                            " Check your achievements tab! "
                            " You also got 20$ every day now that you're besties with them. "
                            " Nice one! "
                            jump credits
                        " nah its too soon ":
                            p " Oh, for real? "
                            p " I mean...it's true. "
                            lz " Now feeling a little cringe that we asked this. "
                            lz " This is going into a cringe compilation, isn't it? "
                            p " Atleast we asked! "
                            p " I think [they] just wanna take it slow. "
                            lz " Understandable. "
                            lz " We should still take a photo with [them] though. "
                            p " Yeah!! "
                            p " Cmere, you... "
                            scene black with dissolve
                            " You spent the rest of the break taking photos with Petunia and Lizzy. "
                            " You just took a lot of photos, and I mean a LOT. "
                            " And in all sorts of different places, too. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked back into the school and went to your classroom. "
                            pause 2.0
                            jump artclassfri
                else:
                    " You walked over to them and asked them what they were doing. "
                    " Looked like they were having some trouble trying to find the right angle... "
                    " Like they were struggling, a lot. "
                    " You don't know anything about photography, but you could try to help them. "
                    p " Hi there, [name]! "
                    lz " Hello, [name]. "
                    p " As you can see... "
                    p " We're kind of struggling to get the perfect angle here... "
                    lz " Even though we're utterly perfect ourselves, "
                    lz " We still need to make sure that we look even more divine than we usually do. "
                    p " Yup! "
                    p " Gotta make sure we look as pretty as possible in these photos! "
                    lz " Otherwise, we're just going to keep deleting these photos... "
                    lz " ...Until we finally get the perfect photo. "
                    p " That's right! "
                    p " Though we don't know if it's just the lighting... "
                    lz " Or if it's just the angle. "
                    lz " We've been struggling for a few minutes at this now... "
                    p " I would know if it's the lighting! "
                    p " But this...this has me struggling. "
                    lz " Maybe we should go to a different place? "
                    lz " Like, a different spot in the school. "
                    p " I mean, for aesthetics, yes... "
                    p " But I also want to take a photo here! "
                    lz " Hm...what can we do? "
                    lz " I don't want to struggle with this for the entire break. "
                    p " Yeah, that would just be really tiring... "
                    p " All for a photo, too. "
                    " You thought long and hard for what they might be missing. "
                    " You then politely asked them to see their phone. "
                    p " Huh? "
                    lz " Sure, as long as you help. "
                    " They then gave you their phone. "
                    " You decided to look through their filters and selected one that you thought looked really good. "
                    " For good measure, you tried it on yourself and it looked nice. "
                    " You then got in a pretty good angle and told them to pose. "
                    " Despite not knowing anything about photography, you're surprisingly good at this. "
                    p " Oh, you wanna be the one to take the photo of us? "
                    lz " Hm...okay. "
                    " You waited for them to get into a good position patiently. "
                    " Once they got into a nice position, you took a few photos of them. "
                    " After you were done, you gave them a look at the photos you took. "
                    hide petunianeutral at bottom
                    show petuniasurprised at left
                    p " Woah, these are pretty good! "
                    p " Like, really really good! "
                    lz " Hm...these don't look too bad. "
                    lz " These are definitely going on our page. "
                    hide petuniasurprised at bottom
                    show petunianeutral at left
                    p " Thanks for helping, [name]! "
                    p " If you don't mind, could you take more pictures of us? "
                    lz " Yeah, we need more if all of this is going on our page. "
                    lz " Really need those good photos. "
                    " You had nothing to do for the rest of the break, so... "
                    " You agreed on helping them do photos. "
                    scene black with dissolve
                    " You spent the rest of the break being Petunia and Lizzy's camera[person]. "
                    " Just taking photos for them around the school... "
                    " You looked like you didn't get paid enough for this. "
                    play sound "audio/bellring.mp3"
                    " The bell rang, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump artclassfri
            else:
                " You walked over to them and asked them what they were doing. "
                " Looked like they were having some trouble trying to find the right angle... "
                " Like they were struggling, a lot. "
                " You don't know anything about photography, but you could try to help them. "
                x " Hi there, [name]! "
                x " Hello, [name]. "
                $ popularknow = True
                p " I'm Petunia! "
                lz " And I'm Lizzy. "
                p " And as you can see... "
                p " We're kind of struggling to get the perfect angle here... "
                lz " Even though we're utterly perfect ourselves, "
                lz " We still need to make sure that we look even more divine than we usually do. "
                p " Yup! "
                p " Gotta make sure we look as pretty as possible in these photos! "
                lz " Otherwise, we're just going to keep deleting these photos... "
                lz " ...Until we finally get the perfect photo. "
                p " That's right! "
                p " Though we don't know if it's just the lighting... "
                lz " Or if it's just the angle. "
                lz " We've been struggling for a few minutes at this now... "
                p " I would know if it's the lighting! "
                p " But this...this has me struggling. "
                lz " Maybe we should go to a different place? "
                lz " Like, a different spot in the school. "
                p " I mean, for aesthetics, yes... "
                p " But I also want to take a photo here! "
                lz " Hm...what can we do? "
                lz " I don't want to struggle with this for the entire break. "
                p " Yeah, that would just be really tiring... "
                p " All for a photo, too. "
                " You thought long and hard for what they might be missing. "
                " You then politely asked them to see their phone. "
                p " Huh? "
                lz " Sure, as long as you help. "
                " They then gave you their phone. "
                " You decided to look through their filters and selected one that you thought looked really good. "
                " For good measure, you tried it on yourself and it looked nice. "
                " You then got in a pretty good angle and told them to pose. "
                " Despite not knowing anything about photography, you're surprisingly good at this. "
                p " Oh, you wanna be the one to take the photo of us? "
                lz " Hm...okay. "
                " You waited for them to get into a good position patiently. "
                " Once they got into a nice position, you took a few photos of them. "
                " After you were done, you gave them a look at the photos you took. "
                hide petunianeutral at bottom
                show petuniasurprised at left
                p " Woah, these are pretty good! "
                p " Like, really really good! "
                lz " Hm...these don't look too bad. "
                lz " These are definitely going on our page. "
                hide petuniasurprised at bottom
                show petunianeutral at left
                p " Thanks for helping, [name]! "
                p " If you don't mind, could you take more pictures of us? "
                lz " Yeah, we need more if all of this is going on our page. "
                lz " Really need those good photos. "
                " You had nothing to do for the rest of the break, so... "
                " You agreed on helping them do photos. "
                scene black with dissolve
                " You spent the rest of the break being Petunia and Lizzy's camera[person]. "
                " Just taking photos for them around the school... "
                " You looked like you didn't get paid enough for this. "
                play sound "audio/bellring.mp3"
                " The bell rang, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump artclassfri
        label buffkingerya:
            show cubbieneutral at center with easeinleft
            if cubbieknow == True:
                pause 0.1
                if cubbielv >= 30 or cubbielv == 30:
                    " You walked over to him and asked him what he was doing. "
                    " He looked like he had something to say... "
                    " You wonder what he was going to say to you. "
                    cb " ... "
                    " He signed to you that he had something to show you. "
                    " Or more like, something you can hear. "
                    " You wondered what it was... "
                    " You waited patiently for Cubbie to say what he had to say. "
                    " You were wondering if he was going to use his voice... "
                    cb " ... "
                    " He took a deep breath in, preparing himself... "
                    " You patiently waited for him to talk. "
                    cb " ...{p} Hi. "
                    " Woah, his voice sounded very soft. "
                    " And also very nice... "
                    cb " ...Does...does my voice sound okay...? "
                    cb " It doesn't disappoint you or anything...? "
                    " You gave him a thumbs up and said that you thought his voice sounded nice. "
                    " You told him not to worry about it too much. "
                    cb " Okay...good. "
                    cb " This is...my first time speaking with you like this, if I remember correctly. "
                    cb " Um... "
                    cb " I wanted to tell you something. "
                    cb " Something that I've been meaning to say for a bit now... "
                    cb " I hope this doesn't come off as weird to you... "
                    " You reassured him that he was probably going to be fine. "
                    " You weren't the type to judge, anyway. "
                    " You were just chill like that. "
                    cb " Okay...good... "
                    cb " ...This is really embarrassing for me to ask you this, but... "
                    cb " ...Would you like to be best friends with me? "
                    cb " I know we've known eachother for only four days, but... "
                    cb " Spending time with you...talking to you... "
                    cb " All of that has made my days better... "
                    cb " It's fine if you just want to stay as normal friends... "
                    cb " I don't mind, really. "
                    menu:
                        " best friends!! ":
                            $ cubbiesend.grant()
                            hide cubbieneutral at bottom
                            show cubbiehappy at center
                            cb " ...Wait, seriously? "
                            cb " I...honestly can't believe that you said that. "
                            cb " But, I'm happy. "
                            cb " Let's hang out later, after school... "
                            cb " If you're free. "
                            scene cubbieend with dissolve
                            " Congratulations! you've managed to get Cubbie to speak, and get his ending! "
                            " And also you got his sweet achievement. "
                            " Check your achievements tab! "
                            " Now you guys can be true homies and hang out. "
                            jump credits
                        " nah normal friends better ":
                            cb " I understand. "
                            cb " This IS a little bit too soon, after all... "
                            cb " Um...let's just talk. "
                            cb " Don't know what else to talk about, though... "
                            cb " Uh...how was your day today? "
                            scene black with dissolve
                            " You spent the rest of the break talking with Cubbie. "
                            " Just talking about random stuff, nothing important. "
                            " Random random stuff. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked back into the school and went to your classroom. "
                            pause 2.0
                            jump artclassfri
                else:
                    " You walked over to him and asked him what he was doing. "
                    " Looked like he was looking at something... "
                    " You sat down on the ground next to him to see what he's looking at. "
                    cb " ... "
                    " He waves at you before pointing at the ground. "
                    " You took a look closer, and... "
                    " Oh hey, it's an ant mound. "
                    " You casually poked at it and saw the ants skedaddle around. "
                    cb " ... "
                    " Cubbie grabs something nearby... "
                    " A water bottle. "
                    " Looks like he wanted to see what would happen. "
                    " And honestly, you did too. "
                    " This is basically just torture for ants, buuut... "
                    " Let's just say this is for science. "
                    cb " ... "
                    " Cubbie then slowly starts pouring the water down onto the ants. "
                    " This is probably like a tsunami or a flash flood for the ants. "
                    " Some of them start getting out of the mound, but you think most of them died inside. "
                    " The lucky ones that lived were probably outside of the mound, or escaped in time. "
                    " Now the ants have to build a new home. "
                    cb " ... "
                    " Cubbie looked like he didn't care too much though. "
                    " Infact, he poured even more water into the mound. "
                    " Just to make sure that everything there was really dead. "
                    " Wow, didn't know Cubbie was even like that... "
                    " That just makes him a little bit more cooler in your eyes. "
                    " You spot another ant mound nearby... "
                    " You had a whole lot of ideas of how you could torture these little fellas. "
                    " You poked Cubbie and pointed at the ant mound nearby. "
                    cb " ... "
                    " It looks like Cubbie got the same idea as you. "
                    " The poor ants... "
                    scene black with dissolve
                    " You spent the rest of the break looking for a lot of ways to torutre some ants. "
                    " Only some though. "
                    " You let the rest of them live. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked back inside of the school and went to your classroom. "
                    pause 2.0
                    jump artclassfri
            else:
                " Oh hey, you've seen this guy before. "
                $ cubbieknow = True
                " His name is Cubbie, and he doesn't really talk much. "
                " You walked over to him and asked him what he was doing. "
                " Looked like he was looking at something... "
                " You sat down on the ground next to him to see what he's looking at. "
                cb " ... "
                " He waves at you before pointing at the ground. "
                " You took a look closer, and... "
                " Oh hey, it's an ant mound. "
                " You casually poked at it and saw the ants skedaddle around. "
                cb " ... "
                " Cubbie grabs something nearby... "
                " A water bottle. "
                " Looks like he wanted to see what would happen. "
                " And honestly, you did too. "
                " This is basically just torture for ants, buuut... "
                " Let's just say this is for science. "
                cb " ... "
                " Cubbie then slowly starts pouring the water down onto the ants. "
                " This is probably like a tsunami or a flash flood for the ants. "
                " Some of them start getting out of the mound, but you think most of them died inside. "
                " The lucky ones that lived were probably outside of the mound, or escaped in time. "
                " Now the ants have to build a new home. "
                cb " ... "
                " Cubbie looked like he didn't care too much though. "
                " Infact, he poured even more water into the mound. "
                " Just to make sure that everything there was really dead. "
                " Wow, didn't know Cubbie was even like that... "
                " That just makes him a little bit more cooler in your eyes. "
                " You spot another ant mound nearby... "
                " You had a whole lot of ideas of how you could torture these little fellas. "
                " You poked Cubbie and pointed at the ant mound nearby. "
                cb " ... "
                " It looks like Cubbie got the same idea as you. "
                " The poor ants... "
                scene black with dissolve
                " You spent the rest of the break looking for a lot of ways to torutre some ants. "
                " Only some though. "
                " You let the rest of them live. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked back inside of the school and went to your classroom. "
                pause 2.0
                jump artclassfri
    label backschoolfri5:
        # claire and kevin
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of the school and found two of your classmates doing their own things. "
        " Who do you talk to for this break? "
        if claireknow == True and kevinknow == True:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    jump tetostress
                " {image=kevinicon} Kevin {image=kevinicon} ":
                    jump tetoerin
        elif claireknow == True and kevinknow == False:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    jump tetostress
                " {image=kevinicon} A nerd {image=kevinicon} ":
                    jump tetoerin
        elif claireknow == False and kevinknow == True:
            menu:
                " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                    jump tetostress
                " {image=kevinicon} Kevin {image=kevinicon} ":
                    jump tetoerin
        else:
            menu:
                " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                    jump tetostress
                " {image=kevinicon} A nerd {image=kevinicon} ":
                    jump tetoerin
        label tetostress:
            show claireneutral at center with easeinright
            if claireknow == True:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was reading an interesting book... "
                " You sat down next to her and looked at what she was reading. "
                c " Hey there, [name]!! "
                c " Just reading this sweet new book I found... "
                c " It's got a really interesting story! "
                c " Lemme explain this to you quickly... "
                c " So basically, there's this girl that falls inlove with another girl! "
                c " And they're both witches! "
                c " The other girl is like, kinda explaining her how to do some magic... "
                c " Since the main girl didn't really pay attention to classes. "
                c " They're like, best friends, by the way! "
                c " Well, not until the end, hehe. "
                c " And then... "
                " Before Claire could continue explaining, "
                " Something mysterious dropped on her book. "
                hide claireneutral at bottom
                show claireconfused at center
                c " Huh? hold on...what is this thing? "
                c " It looks weird... "
                c " Wait, is that...? "
                hide claireconfused at bottom
                show claireangry at center
                c " Oh hell no. "
                c " Someone just SOMEHOW poured shampoo on my book! "
                c " I don't even know how they can aim that far from here... "
                c " Who could be the one who did this... "
                " You looked above you and saw Oliver snickering. "
                " You poked Claire and pointed at him. "
                o " Your fault for sitting near a window!! "
                o " Maybe sit somewhere safer, yeah? "
                o " Guess you aren't so smart after all. "
                " ...And he then left. "
                c " Ough, he's so annoying. "
                c " But, can't really do anything about him, really... "
                hide claireangry at bottom
                show claireneutral at center
                c " Besides, I can just wipe this off! "
                c " If the page does get ruined... "
                c " Then I'm just going to have to deal with that. "
                c " Not too much of a problem, really! "
                c " Whatever happens, just happens... "
                c " And I'm fine with that. "
                c " Unless if it's Oliver bullying someone. "
                c " I'm gonna have to report that to Miss Grace. "
                c " Anywho, where were we? "
                c " Oh, right! "
                c " The story! "
                c " Sorry that I kind of forgot a little, hehe... "
                c " Let me continue explaining, okay? "
                c " Just tell me when you want me to stop explaining. "
                c " Don't want to be too annoying, you know? "
                c " Hehe... "
                c " Alright, let's continue! "
                c " What part was I...? "
                c " Oh, right!!! "
                scene black with dissolve
                " You spent the rest of the break talking with Claire. "
                " Just talking about the book she was reading... "
                " Seemed pretty interesting. You should check it out. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump artclassfri
            else:
                " You walked over to her and asked her what she was doing. "
                " Looked like she was reading an interesting book... "
                " You sat down next to her and looked at what she was reading. "
                x " Hey there, [name]!! "
                $ claireknow = True
                c " I'm Claire! and I was just... "
                c " Just reading this sweet new book I found... "
                c " It's got a really interesting story! "
                c " Lemme explain this to you quickly... "
                c " So basically, there's this girl that falls inlove with another girl! "
                c " And they're both witches! "
                c " The other girl is like, kinda explaining her how to do some magic... "
                c " Since the main girl didn't really pay attention to classes. "
                c " They're like, best friends, by the way! "
                c " Well, not until the end, hehe. "
                c " And then... "
                " Before Claire could continue explaining, "
                " Something mysterious dropped on her book. "
                hide claireneutral at bottom
                show claireconfused at center
                c " Huh? hold on...what is this thing? "
                c " It looks weird... "
                c " Wait, is that...? "
                hide claireconfused at bottom
                show claireangry at center
                c " Oh hell no. "
                c " Someone just SOMEHOW poured shampoo on my book! "
                c " I don't even know how they can aim that far from here... "
                c " Who could be the one who did this... "
                " You looked above you and saw Oliver snickering. "
                " You poked Claire and pointed at him. "
                o " Your fault for sitting near a window!! "
                o " Maybe sit somewhere safer, yeah? "
                o " Guess you aren't so smart after all. "
                " ...And he then left. "
                c " Ough, he's so annoying. "
                c " But, can't really do anything about him, really... "
                hide claireangry at bottom
                show claireneutral at center
                c " Besides, I can just wipe this off! "
                c " If the page does get ruined... "
                c " Then I'm just going to have to deal with that. "
                c " Not too much of a problem, really! "
                c " Whatever happens, just happens... "
                c " And I'm fine with that. "
                c " Unless if it's Oliver bullying someone. "
                c " I'm gonna have to report that to Miss Grace. "
                c " Anywho, where were we? "
                c " Oh, right! "
                c " The story! "
                c " Sorry that I kind of forgot a little, hehe... "
                c " Let me continue explaining, okay? "
                c " Just tell me when you want me to stop explaining. "
                c " Don't want to be too annoying, you know? "
                c " Hehe... "
                c " Alright, let's continue! "
                c " What part was I...? "
                c " Oh, right!!! "
                scene black with dissolve
                " You spent the rest of the break talking with Claire. "
                " Just talking about the book she was reading... "
                " Seemed pretty interesting. You should check it out. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump artclassfri
        label tetoerin:
            show kevinneutral at center with easeinleft
            if kevinknow == True:
                pause 0.1
                if kevinlv >= 30 or kevinlv == 30:
                    " You walked over to him and asked him what he was doing. "
                    " Looks like he was doing something else other than studying... "
                    " Which is actually surprising. "
                    kv " Ah, [name]. "
                    kv " I've been waiting for you. "
                    kv " ...And I may have been messaging you. "
                    kv " You weren't really checking out my messages. "
                    kv " But, I assume that you were busy. "
                    kv " And I completely understand that. "
                    kv " Anyway... "
                    kv " There's something important that I want to talk about to you. "
                    kv " You see... "
                    kv " Friendships usually form after a few days of talking. "
                    kv " Sometimes one day, sometimes even a whole month. "
                    kv " But the whole thing is best friends. "
                    kv " When do best friends really form? "
                    kv " Is it when you talk to someone too much? "
                    kv " Or can you consider someone a best friend after a day? "
                    kv " Surely, not. "
                    kv " But the thing I'm trying to ask you is a little odd... "
                    kv " Something relating to my questions. "
                    kv " And what I'm trying to ask you... "
                    kv " ...Is would you like to be best friends with me? "
                    kv " Now, you can reject me and I'm fine with it. "
                    kv " After all, it's only been four days. "
                    kv " So, I'm completely fine with whatever reaction you have. "
                    kv " What do you say? "
                    kv " Be my best friend, or should we stay as normal friends? "
                    menu:
                        " study buddies 4 life!! ":
                            $ kevinsend.grant()
                            hide kevinneutral at bottom
                            show kevinhappy at center
                            kv " ...Hold on, you're being serious? "
                            kv " Well...if you say so. "
                            kv " As a perk to being my best friend... "
                            kv " I'll let you copy my answers. "
                            kv " Probably not the best choice, but I want you to pass. "
                            kv " Just hope that the teachers don't find out too quick. "
                            kv " And don't make it too obvious that you copied me, of course. "
                            kv " Let's maybe go hang out after school, if you're free. "
                            kv " (Best friend...) "
                            kv " (Never thought I'd have one.) "
                            scene kevinend with dissolve
                            " Congratulations, you've got Kevin's ending! "
                            " And also his sweet achievement. Check your achievements tab! "
                            " Nice, you get to copy his answers and notes now. "
                            " For free, too! "
                            jump credits
                        " normal friends better ":
                            kv " Understandable. "
                            kv " While you're here though... "
                            kv " We should probably talk about something else. "
                            kv " To not embarass myself of asking you to be my best friend for longer. "
                            kv " Let's see... "
                            kv " How was your day today? "
                            scene black with dissolve
                            " You spent the rest of the break talking with Kevin. "
                            " Just talking about how your day went... "
                            " Nothing too special, really. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked back into the school and went to your classroom. "
                            pause 2.0
                            jump artclassfri
                else:
                    " You walked over to him and asked him what he was doing. "
                    " He wasn't studying for once... "
                    " How surprising. Truly baffling. "
                    kv " Hello there, [name]. "
                    kv " I've been struggling to see a bit lately... "
                    kv " Everything's been slightly blurry. "
                    kv " I mean, I can see you just fine... "
                    kv " The only problem is that you're just a little bit blurry. "
                    kv " Even if it's only just a little bit, "
                    kv " It still makes me a little pissed off that my vision isn't clear. "
                    kv " I might need to get some new glasses soon... "
                    kv " But not right now. "
                    kv " I'll wait until my vision is blurry blurry. "
                    kv " Then I can get new glasses. "
                    kv " My parents don't like to spend too much on my vision. "
                    kv " So, I have to wait for a bit until my vision gets really bad... "
                    kv " Then I can tell them to get me new glasses. "
                    kv " They test my vision before I go to the eye doctor. "
                    kv " Just to make sure I'm not lying or anything. "
                    kv " I don't mind it, but... "
                    kv " I just think that it's a little bit much. "
                    kv " I don't question them though. "
                    kv " They do whatever they do... "
                    kv " And I do whatever I do. "
                    kv " If they don't bother me, I don't bother them... "
                    kv " You get the whole idea. "
                    " Just to test him, you put two fingers up. "
                    kv " ...I can still see that, you know. "
                    kv " Try getting farther. "
                    " You walked back a good bit and threw him the middle finger. "
                    " Hopefully he doesn't actually see that. "
                    " You think he'd be just a little pissed off if he did. "
                    kv " ... "
                    hide kevinneutral at bottom
                    show kevinconfused at center
                    kv " Is... "
                    kv " Hold on, sorry... "
                    kv " Is that three??? "
                    kv " No, wait... "
                    kv " That looks like a five. "
                    kv " Is that a five? "
                    kv " I'm not even sure at this point. "
                    " You told him it was a one. "
                    kv " Okay, I think I really need to get my eyes checked out. "
                    kv " I'm gonna tell my parents later. "
                    kv " There's no way I saw a one as a five... "
                    kv " That's just stupid. "
                    hide kevinconfused at bottom
                    show kevinneutral at center
                    kv " Thank you for showing how blind I am, though. "
                    kv " I probably would've suffered with my eyesight a little longer if you didn't do this. "
                    kv " Probably. "
                    scene black with dissolve
                    " You spent the rest of the break talking to Kevin about his eyesight. "
                    " Yeah...his eyesight was BAD bad. "
                    " He should get that checked out tomorrow. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump artclassfri
            else:
                " You walked over to him and asked him what he was doing. "
                " He wasn't studying for once... "
                " How surprising. Truly baffling. "
                x " Hello there, [name]. "
                $ kevinknow =True
                kv " I'm Kevin. Nice to meet you. "
                kv " I've been struggling to see a bit lately... "
                kv " Everything's been slightly blurry. "
                kv " I mean, I can see you just fine... "
                kv " The only problem is that you're just a little bit blurry. "
                kv " Even if it's only just a little bit, "
                kv " It still makes me a little pissed off that my vision isn't clear. "
                kv " I might need to get some new glasses soon... "
                kv " But not right now. "
                kv " I'll wait until my vision is blurry blurry. "
                kv " Then I can get new glasses. "
                kv " My parents don't like to spend too much on my vision. "
                kv " So, I have to wait for a bit until my vision gets really bad... "
                kv " Then I can tell them to get me new glasses. "
                kv " They test my vision before I go to the eye doctor. "
                kv " Just to make sure I'm not lying or anything. "
                kv " I don't mind it, but... "
                kv " I just think that it's a little bit much. "
                kv " I don't question them though. "
                kv " They do whatever they do... "
                kv " And I do whatever I do. "
                kv " If they don't bother me, I don't bother them... "
                kv " You get the whole idea. "
                " Just to test him, you put two fingers up. "
                kv " ...I can still see that, you know. "
                kv " Try getting farther. "
                " You walked back a good bit and threw him the middle finger. "
                " Hopefully he doesn't actually see that. "
                " You think he'd be just a little pissed off if he did. "
                kv " ... "
                hide kevinneutral at bottom
                show kevinconfused at center
                kv " Is... "
                kv " Hold on, sorry... "
                kv " Is that three??? "
                kv " No, wait... "
                kv " That looks like a five. "
                kv " Is that a five? "
                kv " I'm not even sure at this point. "
                " You told him it was a one. "
                kv " Okay, I think I really need to get my eyes checked out. "
                kv " I'm gonna tell my parents later. "
                kv " There's no way I saw a one as a five... "
                kv " That's just stupid. "
                hide kevinconfused at bottom
                show kevinneutral at center
                kv " Thank you for showing how blind I am, though. "
                kv " I probably would've suffered with my eyesight a little longer if you didn't do this. "
                kv " Probably. "
                scene black with dissolve
                " You spent the rest of the break talking to Kevin about his eyesight. "
                " Yeah...his eyesight was BAD bad. "
                " He should get that checked out tomorrow. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump artclassfri
    label gymfri5:
        # ruby and engel
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked to the gym and spotted two of your classmates doing their own things. "
        " Who would you want to talk to for this break? "
        if rubyknow == True and engelknow == True:
            menu:
                " {image=rubyicon} Ruby {image=rubyicon} ":
                    jump nolesdeergolly
                " {image=engelicon} Engel {image=engelicon} ":
                    jump dessdeergolly
        elif rubyknow == True and engelknow == False:
            menu:
                " {image=rubyicon} Ruby {image=rubyicon} ":
                    jump nolesdeergolly
                " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                    jump dessdeergolly
        elif rubyknow == False and engelknow == True:
            menu:
                " {image=rubyicon} A girl with a TV for her head {image=rubyicon} ":
                    jump nolesdeergolly
                " {image=engelicon} Engel {image=engelicon} ":
                    jump dessdeergolly
        else:
            menu:
                " {image=rubyicon} A girl with a TV for her head {image=rubyicon} ":
                    jump nolesdeergolly
                " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                    jump dessdeergolly
        label nolesdeergolly:
            show rubyneutral at center with easeinleft
            if rubyknow == True:
                pause 0.1
                if rubylv >= 30 or rubylv == 30:
                    " You walked over to her and asked her what she was doing. "
                    " It looked like she was expecting you... "
                    " Interesting. "
                    ru " Ah, [name]! "
                    ru " It's so, so nice to see you here! "
                    ru " I've been waiting for you, actually.. "
                    ru " I tried messaging you, but... "
                    ru " Turns out I had ran out of mobile data, aha... "
                    ru " I should've checked before sending something, hehe. "
                    ru " But, anyway... "
                    ru " I was waiting for you for a reason! "
                    ru " I mean, of course there would be.. "
                    ru " Why would I wait for you without a reason, hehe... "
                    ru " Getting to the said reason... "
                    ru " I have...something to admit to you. "
                    ru " We've been getting really close lately! "
                    ru " Which is really surprising considering I've known you for 4 days only! "
                    ru " But... "
                    ru " The thing I want to ask you is... "
                    ru " ..Would you perhaps want to be best friends with me? "
                    ru " I know that it might be too soon, but... "
                    ru " You're one of the only people in this school who has made be feel...real. "
                    ru " Like, I've been feeling so many new emotions that I thought I couldn't feel! "
                    ru " Everytime I put on a happy smile... "
                    ru " That was just my code trying to make me look friendly and approachable! "
                    ru " But now? "
                    ru " You've been getting me to smile...for real! "
                    ru " I haven't smiled this much since...awhile now. "
                    ru " I mostly smile around my friends, hehe. "
                    ru " So, um...best friends? "
                    menu:
                        " best friends!! ":
                            $ rubysend.grant()
                            hide rubyneutral at bottom
                            show rubyhappy at center
                            ru " Oh, I'm so glad!! "
                            ru " Hehe, I'm really glad that you want to be my best friend!! "
                            ru " Let's spend the best time with eachother, bestie!! "
                            ru " Is that the short term for best friend? "
                            ru " I think so! "
                            scene rubyend with dissolve
                            " Congratulations, you've gotten Ruby's ending! "
                            " And also her nice achievement. Go and check your achievements page! "
                            " You made a robot feel real. Be proud of that. "
                            " You've just made her really happy. "
                            jump credits
                        " normal friends pls ":
                            ru " Oh... "
                            ru " Understandable, though! "
                            ru " Let's just be normal friends, then. "
                            ru " Erh...what do normal friends talk about...? "
                            ru " Um...how's your day today? "
                            scene black with dissolve
                            " You spent the rest of the break talking with Ruby. "
                            " Just talking to her about how your day went. "
                            " Nothing too special, truly. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked out of the gym and went to your classroom. "
                            pause 2.0
                            jump artclassfri
                else:
                    " You walked over to her and asked her what she's doing. "
                    " Looked like she was thinking about a few things... "
                    ru " Hi there, [name]! "
                    ru " Almost didn't notice you there for a hot minute, hehe.. "
                    ru " I was just in deep thought. "
                    ru " I'm...sorry if I may seem too 'real' about this, but... "
                    ru " I just need someone to talk to right now. "
                    ru " If...that's okay with you. "
                    " You'd say that you're a pretty good listener. "
                    " You gave her a thumbs up and get ready for when she's ready to talk. "
                    ru " ...Okay...so... "
                    ru " Have you ever felt that nothing in life is really real? "
                    ru " Feels like everything's just scripted, to be honest... "
                    ru " We're all just playing our part in our lives, "
                    ru " Acting out the character we wanted to be when we were just auditioning. "
                    ru " Just acting our character really well. "
                    ru " Acting so well, that no one really notices that it's just an act. "
                    ru " They got too used to living this weird life. "
                    ru " But, there are times where I feel real... "
                    ru " And it's when I hang out with my friends. "
                    ru " Is that normal? "
                    ru " For robots to feel like real beings for once? "
                    ru " I don't really think so... "
                    ru " Robots are mostly seen being emotionless people in movies. "
                    ru " Should I be even showing emotion? "
                    ru " But...showing emotion makes me feel happy. "
                    ru " Happy that I get to expirience things like this. "
                    ru " Happy that I exist. "
                    ru " But... "
                    ru " Robots like me also get times where we question our existance. "
                    ru " Was I just made to live a normal school girl life? "
                    ru " To make me feel more human? "
                    ru " Or did I have bigger things planned but I forgot about them later on? "
                    ru " I can't remember, honestly... "
                    ru " But, I do know that I have a goal of finishing school. "
                    ru " Life as a robot feels so weird sometimes... "
                    ru " The moment you're created, you're given a task. "
                    ru " You can't function properly without a task. "
                    ru " And I was given the task to live a normal life. "
                    ru " ...I was given a whole lot of tasks after that. "
                    ru " Make friends, finish school... "
                    ru " Every single thing a human would have as a goal. "
                    ru " It's...honestly overwhelming with how much I have to do, but... "
                    ru " My current task is to finish school right now. "
                    ru " Not all of that. "
                    ru " ...Whew, sorry if I got too real, again... "
                    ru " (If [they] had a skip button, they probably skipped through all of my dialogue, haha...) "
                    ru " (Hopefully they didn't, though.) "
                    ru " Let's talk about something else, shall we? "
                    ru " Um...how was your day today? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Ruby. "
                    " Just talking to her about how your day went. "
                    " Nothing too special, truly. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the gym and went to your classroom. "
                    pause 2.0
                    jump artclassfri
            else:
                " You walked over to her and asked her what she's doing. "
                " Looked like she was thinking about a few things... "
                x " Hi there, [name]! "
                x " Almost didn't notice you there for a hot minute, hehe.. "
                $ rubyknow = True
                ru " I'm Ruby, it's nice to meet you! and.. "
                ru " I was just in deep thought. "
                ru " I'm...sorry if I may seem too 'real' about this, but... "
                ru " I just need someone to talk to right now. "
                ru " If...that's okay with you. "
                " You'd say that you're a pretty good listener. "
                " You gave her a thumbs up and get ready for when she's ready to talk. "
                ru " ...Okay...so... "
                ru " Have you ever felt that nothing in life is really real? "
                ru " Feels like everything's just scripted, to be honest... "
                ru " We're all just playing our part in our lives, "
                ru " Acting out the character we wanted to be when we were just auditioning. "
                ru " Just acting our character really well. "
                ru " Acting so well, that no one really notices that it's just an act. "
                ru " They got too used to living this weird life. "
                ru " But, there are times where I feel real... "
                ru " And it's when I hang out with my friends. "
                ru " Is that normal? "
                ru " For robots to feel like real beings for once? "
                ru " I don't really think so... "
                ru " Robots are mostly seen being emotionless people in movies. "
                ru " Should I be even showing emotion? "
                ru " But...showing emotion makes me feel happy. "
                ru " Happy that I get to expirience things like this. "
                ru " Happy that I exist. "
                ru " But... "
                ru " Robots like me also get times where we question our existance. "
                ru " Was I just made to live a normal school girl life? "
                ru " To make me feel more human? "
                ru " Or did I have bigger things planned but I forgot about them later on? "
                ru " I can't remember, honestly... "
                ru " But, I do know that I have a goal of finishing school. "
                ru " Life as a robot feels so weird sometimes... "
                ru " The moment you're created, you're given a task. "
                ru " You can't function properly without a task. "
                ru " And I was given the task to live a normal life. "
                ru " ...I was given a whole lot of tasks after that. "
                ru " Make friends, finish school... "
                ru " Every single thing a human would have as a goal. "
                ru " It's...honestly overwhelming with how much I have to do, but... "
                ru " My current task is to finish school right now. "
                ru " Not all of that. "
                ru " ...Whew, sorry if I got too real, again... "
                ru " (If [they] had a skip button, they probably skipped through all of my dialogue, haha...) "
                ru " (Hopefully they didn't, though.) "
                ru " Let's talk about something else, shall we? "
                ru " Um...how was your day today? "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby. "
                " Just talking to her about how your day went. "
                " Nothing too special, truly. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom. "
                pause 2.0
                jump artclassfri
        label dessdeergolly:
            show engelneutral at center with easeinright
            if engelknow == True:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was arranging things in his bag.. "
                hide engelneutral at bottom
                show engelhappy at center
                e " Hey there, [name]. "
                e " I'm just arranging things in my bag... "
                e " I realized that I've been collecting a lot of things and putting them in my bag for awhile now... "
                e " And so I'm trying to clean out my bag and arranging everything. "
                e " Because, honestly...the arrangement I had originally was kind of irking me. "
                e " There's a lot of things that I've been putting in here... "
                e " And I'm really indecisive on keeping things or not, so... "
                e " Could you help me for this? "
                e " I'm sure this won't take too much time. "
                e " I promise you. "
                e " If you want to stop, you can just tell me. "
                e " Let's start, alright? "
                e " First thing I've got in here... "
                e " Awh, it's that heart candy Claire gave to me... "
                e " It does look like it's been in here for awhile now though. "
                e " Like, awhile awhile. "
                e " I remember this being...last month? "
                e " I'm not even sure if it's even edible. "
                e " Wait, let me try it real quick... "
                hide engelhappy at bottom
                show engelneutral at center
                " Engel unwraps the wrapper the candy had. "
                " ...And the candy is melted. "
                " Engel immediately threw it away in the nearby trash can. "
                e " ...I wonder how I've ignored that thing in my bag. "
                e " I mean, it WAS buried deep into my bag... "
                e " I guess I thought that I'd just save it for later. "
                hide engelneutral at bottom
                show engelhappy at center
                e " Anyways, let's keep going. "
                e " I've got a lot of old trinkets in here... "
                e " So lets take a good look at all of them. "
                scene black with dissolve
                " You spent the rest of the break helping Engel sort out his bag. "
                " Just doing stuff and even more stuff. "
                " In the end, Engel's bag looked really, really organized and nice. "
                play sound "audio/bellring.mp3"
                " The bel rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom. "
                pause 2.0
                jump artclassfri
            else:
                " You walked over to him and asked him what he was doing. "
                " Looked like he was arranging things in his bag.. "
                hide engelneutral at bottom
                show engelhappy at center
                x " Hey there, [name]. "
                $ engelknow = True
                e " I'm Engel, one of your classmates. "
                e " And I'm just arranging things in my bag... "
                e " I realized that I've been collecting a lot of things and putting them in my bag for awhile now... "
                e " And so I'm trying to clean out my bag and arranging everything. "
                e " Because, honestly...the arrangement I had originally was kind of irking me. "
                e " There's a lot of things that I've been putting in here... "
                e " And I'm really indecisive on keeping things or not, so... "
                e " Could you help me for this? "
                e " I'm sure this won't take too much time. "
                e " I promise you. "
                e " If you want to stop, you can just tell me. "
                e " Let's start, alright? "
                e " First thing I've got in here... "
                e " Awh, it's that heart candy Claire gave to me... "
                e " It does look like it's been in here for awhile now though. "
                e " Like, awhile awhile. "
                e " I remember this being...last month? "
                e " I'm not even sure if it's even edible. "
                e " Wait, let me try it real quick... "
                hide engelhappy at bottom
                show engelneutral at center
                " Engel unwraps the wrapper the candy had. "
                " ...And the candy is melted. "
                " Engel immediately threw it away in the nearby trash can. "
                e " ...I wonder how I've ignored that thing in my bag. "
                e " I mean, it WAS buried deep into my bag... "
                e " I guess I thought that I'd just save it for later. "
                hide engelneutral at bottom
                show engelhappy at center
                e " Anyways, let's keep going. "
                e " I've got a lot of old trinkets in here... "
                e " So lets take a good look at all of them. "
                scene black with dissolve
                " You spent the rest of the break helping Engel sort out his bag. "
                " Just doing stuff and even more stuff. "
                " In the end, Engel's bag looked really, really organized and nice. "
                play sound "audio/bellring.mp3"
                " The bel rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom. "
                pause 2.0
                jump artclassfri
    label cafeteriafri5:
        # robby and riley
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked to the cafeteria and spotted two of your classmates talking to eachother. "
        " Wondering what they're talking about, you sat down next to them. "
        show robbyneutral at right with easeinleft
        show rileyneutral at left with easeinright
        if robbyknow == True and rileyknow == True:
            pause 0.1
            if robbrileylv >= 30 or robbrileylv == 30:
                " You walked over to them and asked them what they were doing. "
                " Looked like they were discussing things normally for once... "
                " They stopped when they noticed you though. "
                rb " Hello there, [name]. "
                ri " Hi!! "
                rb " So we've been thinking about a few things... "
                rb " Regarding to the stuff that happened ever since you got here. "
                ri " Let me word this since Robby over here isn't good with talking... "
                rb " Hey...??? "
                ri " So...me and Robby have been thinking about a few things! "
                ri " Like, a whole lot of things. "
                ri " A whole whole lot of things. "
                rb " Riley, can you just get to the point... "
                ri " Whoops, sorry! "
                ri " And we've been thinking about this specific question a whole lot... "
                ri " A question that we were going to ask you! "
                rb " You've listened to my ramblings a whole lot.. "
                ri " And also mine! "
                rb " I didn't think people would listen to me. "
                ri " I didn't think that someone would listen to me either! "
                rb " But, you stayed and listened. "
                ri " Something that someone ever rarely does! "
                rb " And we've been happy that you stayed... "
                ri " And listened, of course! "
                rb " And now we've got that one question to ask you. "
                ri " Which iiiiis...!! "
                rb " ...I'm not being the one to say it. "
                ri " Oh, fine. You big baby... "
                ri " Would you like to be best friends with us?! "
                menu:
                    " YEAAH ":
                        $ robrileysend.grant()
                        hide robbyneutral at bottom
                        hide rileyneutral at bottom
                        show robbyhappy at right
                        show rileyhappy at left
                        rb " ...Huh, I can't believe you actually said yes. "
                        rb " That was surprising, considering the fact that... "
                        ri " Yeah, yeah!! considering the fact that it's only been four days!! "
                        ri " Now shut up!! we've got a best friend!! "
                        rb " I haven't seen you this excited in a good bit. "
                        ri " Of course I would be!! "
                        scene robbrileyend with dissolve
                        " Congratulations! you've gotten Robby and Riley's ending! "
                        " And their sweet achievement. Check your achievements tab! "
                        " Now you get to deal with more of Riley and Robby's yapping... "
                        " Not that you're complaining though. "
                        jump credits
                    " nahh normal friends pls ":
                        rb " ...See? I told you it would be too soon. "
                        ri " Aww, it was worth a shot though! "
                        rb " Yeah, yeah... "
                        rb " Better talk about something else to not make them uncomfortable. "
                        ri " Alrighty!! "
                        ri " Can we talk about my darling Oliver, then? "
                        rb " No. "
                        ri " Aww... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Robby and Riley about random stuff. "
                        " Just talking about random random stuff... "
                        " As long as it's not about Oliver, then you're fine. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the cafeteria and went to your classroom. "
                        pause 2.0
                        jump artclassfri
            else:
                " Actually, looks like they're talking about something important. "
                " Maybe you shouldn't eavesdrop this time... "
                " You should leave. This isn't conversation isn't for you. "
                " They look pretty serious, anyway... "
                scene black with dissolve
                " You spent the rest of the break wandering around the school. "
                " You didn't really see anything interesting while you were wandering... "
                " You just spent most of your time looking at your phone. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You then walked to your classroom after a bit. "
                pause 2.0
                jump artclassfri
        elif robbyknow == True and rileyknow == False:
            " Actually, looks like they're talking about something important. "
            " Maybe you shouldn't eavesdrop this time... "
            " You should leave. This isn't conversation isn't for you. "
            " They look pretty serious, anyway... "
            scene black with dissolve
            " You spent the rest of the break wandering around the school. "
            " You didn't really see anything interesting while you were wandering... "
            " You just spent most of your time looking at your phone. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You then walked to your classroom after a bit. "
            pause 2.0
            jump artclassfri
        elif robbyknow == False and rileyknow == True:
            " Actually, looks like they're talking about something important. "
            " Maybe you shouldn't eavesdrop this time... "
            " You should leave. This isn't conversation isn't for you. "
            " They look pretty serious, anyway... "
            scene black with dissolve
            " You spent the rest of the break wandering around the school. "
            " You didn't really see anything interesting while you were wandering... "
            " You just spent most of your time looking at your phone. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You then walked to your classroom after a bit. "
            pause 2.0
            jump artclassfri
        else:
            " Actually, looks like they're talking about something important. "
            " Maybe you shouldn't eavesdrop this time... "
            " You should leave. This isn't conversation isn't for you. "
            " They look pretty serious, anyway... "
            scene black with dissolve
            " You spent the rest of the break wandering around the school. "
            " You didn't really see anything interesting while you were wandering... "
            " You just spent most of your time looking at your phone. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You then walked to your classroom after a bit. "
            pause 2.0
            jump artclassfri
    label rooftopfri5:
        # bubble and skell
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked to the rooftop and spotted two of your classmates doing their own things. "
        " Who do you talk to for this break? "
        if skellknow == True and bubbleknow == True:
            menu:
                " {image=skellicon} Skell {image=skellicon} ":
                    jump strategygay
                " {image=bubbleicon} Bubble {image=bubbleicon} ":
                    jump strategystraight
        elif skellknow == True and bubbleknow == False:
            menu:
                " {image=skellicon} Skell {image=skellicon} ":
                    jump strategygay
                " {image=bubbleicon} A girl made out of bubbles {image=bubbleicon} ":
                    jump strategystraight
        elif skellknow == False and bubbleknow == True:
            menu:
                " {image=skellicon} An emo {image=skellicon} ":
                    jump strategygay
                " {image=bubbleicon} Bubble {image=bubbleicon} ":
                    jump strategystraight
        else:
            menu:
                " {image=skellicon} An emo {image=skellicon} ":
                    jump strategygay
                " {image=bubbleicon} A girl made out of bubbles {image=bubbleicon} ":
                    jump strategystraight
        label strategygay:
            show skellneutral at center with easeinright
            if skellknow == True:
                pause 0.1
                if skelllv >= 30 or skelllv == 30:
                    " You walked over to him and asked him what he was doing. "
                    " Hopefully, you weren't interrupting anything important... "
                    " Just hopefully, otherwise that would be embarrassing. "
                    sk " Huh?? "
                    sk " Oh shit. "
                    sk " Um...hi [name]. "
                    sk " I uh... "
                    sk " ... "
                    sk " Okay, listen... "
                    sk " I was actually planning on telling you something. "
                    sk " And I was trying to practice... "
                    sk " But uh... "
                    sk " I just can't get my words right. "
                    sk " So... "
                    sk " I decided to write it down on my phone over here... "
                    sk " And uh... "
                    sk " I'm just going to read it out, okay? "
                    sk " If you're fine with that. "
                    " You gave him thumbs up. "
                    " You're pretty fine with the whole reading thing. "
                    " This is just like you struggling to present something in front of the class. "
                    " Of course, you're not gonna judge Skell for reading off of his phone. "
                    sk " ...Okay, if you say so. "
                    sk " Ahem... "
                    sk " [name] - I've been thinking a lot of things lately. "
                    sk " Mostly thinking about the time we've spent together. "
                    sk " You've listened to me talk...hung out with me... "
                    sk " Honestly, I thought you'd be a little intimidated by me at first. "
                    sk " People keep on saying that I'm quite intimidating, so... "
                    sk " I thought you'd just run away after that first interaction we've had. "
                    sk " But...you kept talking with me and hanging out with me. "
                    sk " I was surprised - why would you want to talk to someone like me? "
                    sk " I thought you were just going to leave as time passes, but... "
                    sk " These past few days, you've just gotten more and more close to me. "
                    sk " Which is insane - since it's only been two days since you've arrived. "
                    sk " But...I'm also glad that we met. "
                    sk " Hanging out with you has been the highlight of my days. "
                    sk " Just spending time with you...talking... "
                    sk " Every night I was hoping that you'd talk to me, in all honesty... "
                    sk " ...Sorry if that sounds weird, but I'm being honest. "
                    sk " And I've been thinking of asking a certain question to you for awhile now... "
                    sk " You can say no if you just want to stay as normal friends. "
                    sk " I know that it's sudden, so... "
                    sk " Would you maybe...like to be best friends with me? "
                    menu:
                        " yeah!!! ":
                            $ skellsend.grant()
                            hide skellneutral at bottom
                            show skellhappy at center
                            sk " ...I'm glad that you said yes, then. "
                            sk " I would've been fine if you said no, but... "
                            sk " I'm feeling pretty happy with the decision you've made. "
                            sk " Let's go hang out when you're free, alright? "
                            scene skellend with dissolve
                            " Congratulations! you've gotten Skell's ending! "
                            " And his sweet achievement. Check your achievements tab! "
                            " Now you can be emo together. "
                            jump credits
                        " Normal friends please ":
                            sk " Yeah, I guessed it was too fast. "
                            sk " I understand that you want to take it slow, don't worry. "
                            sk " Not going to force you, you know. "
                            sk " Anyway, let's talk about something else... "
                            sk " I feel a little embarrassed now that I asked you to be my best friend early. "
                            sk " Uh, um... "
                            sk " Okay, gonna go on a basic one. "
                            sk " How's your day been? "
                            scene black with dissolve
                            " You spent the rest of the break talking with Skell. "
                            " Just talking to him about how your day went... "
                            " Nothing too special, really. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for another class. "
                            " You walked down from the rooftop and went to your classroom. "
                            pause 2.0
                            jump artclassfri
                else:
                    " You walked over to him, and took a look at what he was doing... "
                    sk " ... "
                    " Seems like he's busy typing something out on his phone. "
                    " Looked like a really long message, too. "
                    " You decided not to bother him. "
                    " The thing he's writing down looks important. "
                    " Looked like plans, actually. "
                    " You then walked down from the rooftop... "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " You didn't really see anything interesting while you were wandering... "
                    " You just spent most of your time looking at your phone. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for another class. "
                    " You then walked to your classroom after a bit. "
                    pause 2.0
                    jump artclassfri
            else:
                " You walked over to him, and took a look at what he was doing... "
                x " ... "
                " Seems like he's busy typing something out on his phone. "
                " Looked like a really long message, too. "
                " You decided not to bother him. "
                " The thing he's writing down looks important. "
                " Looked like plans, actually. "
                " You then walked down from the rooftop... "
                scene black with dissolve
                " You spent the rest of the break wandering around the school. "
                " You didn't really see anything interesting while you were wandering... "
                " You just spent most of your time looking at your phone. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You then walked to your classroom after a bit. "
                pause 2.0
                jump artclassfri
        label strategystraight:
            show bubbleneutralb2 at center with easeinleft
            if bubbleknow == True:
                b " Zzz... "
                " Huh, looks like she's taking a nap. "
                " Seems like she's really tired out... "
                " You decided not to bother her. "
                " You walked down from the rooftop... "
                scene black with dissolve
                " You spent the rest of the break wandering around the school. "
                " You didn't really see anything interesting while you were wandering... "
                " You just spent most of your time looking at your phone. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You then walked to your classroom after a bit. "
                pause 2.0
                jump artclassfri
            else:
                x " Zzz... "
                " Huh, looks like she's taking a nap. "
                " Seems like she's really tired out... "
                " You decided not to bother her. "
                " You walked down from the rooftop... "
                scene black with dissolve
                " You spent the rest of the break wandering around the school. "
                " You didn't really see anything interesting while you were wandering... "
                " You just spent most of your time looking at your phone. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You then walked to your classroom after a bit. "
                pause 2.0
                jump artclassfri
    label libraryfri5:
        # lana and abbie // interact
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked into the library and spotted two of your classmates talking to eachother. "
        " Wondering what they're doing, you walked over to them. "
        show lananeutral at left with easeinright
        show abbieneutral at right with easeinright
        if lanaknow == True and abbieknow == True:
            " You walked over to them and were about to ask them what they were doing, and.. "
            l " Oh hey there, [name]! "
            a " Um... "
            l " It's nice to see you, but... "
            l " Me and Abbie are kind of busy working on our project that we have to pass on monday. "
            l " And we don't really want any distractions... "
            a " Uh...we could still hang out with you next week, though... "
            l " Yeah, when we're not busy! "
            l " Hope you understand! "
            " You respect their work. "
            " You then left the library... "
            scene black with dissolve
            " You spent the rest of the break wandering around the school. "
            " You didn't really see anything interesting while you were wandering... "
            " You just spent most of your time looking at your phone. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You then walked to your classroom after a bit. "
            pause 2.0
            jump artclassfri
        elif lanaknow == True and abbieknow == False:
            " You walked over to them and were about to ask them what they were doing, and.. "
            l " Oh hey there, [name]! "
            x " Um... "
            l " It's nice to see you, but... "
            l " Me and Abbie are kind of busy working on our project that we have to pass on monday. "
            l " And we don't really want any distractions... "
            x " Uh...we could still hang out with you next week, though... "
            l " Yeah, when we're not busy! "
            l " Hope you understand! "
            " You respect their work. "
            " You then left the library... "
            scene black with dissolve
            " You spent the rest of the break wandering around the school. "
            " You didn't really see anything interesting while you were wandering... "
            " You just spent most of your time looking at your phone. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You then walked to your classroom after a bit. "
            pause 2.0
            jump artclassfri
        elif lanaknow == False and abbieknow == True:
            " You walked over to them and were about to ask them what they were doing, and.. "
            x " Oh hey there, [name]! "
            a " Um... "
            x " It's nice to see you, but... "
            x " Me and Abbie are kind of busy working on our project that we have to pass on monday. "
            x " And we don't really want any distractions... "
            a " Uh...we could still hang out with you next week, though... "
            x " Yeah, when we're not busy! "
            x " Hope you understand! "
            " You respect their work. "
            " You then left the library... "
            scene black with dissolve
            " You spent the rest of the break wandering around the school. "
            " You didn't really see anything interesting while you were wandering... "
            " You just spent most of your time looking at your phone. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You then walked to your classroom after a bit. "
            pause 2.0
            jump artclassfri
        else:
            " You walked over to them and were about to ask them what they were doing, and.. "
            x " Oh hey there, [name]! "
            x " Um... "
            x " It's nice to see you, but... "
            x " Me and Abbie are kind of busy working on our project that we have to pass on monday. "
            x " And we don't really want any distractions... "
            x " Uh...we could still hang out with you next week, though... "
            x " Yeah, when we're not busy! "
            x " Hope you understand! "
            " You respect their work. "
            " You then left the library... "
            scene black with dissolve
            " You spent the rest of the break wandering around the school. "
            " You didn't really see anything interesting while you were wandering... "
            " You just spent most of your time looking at your phone. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You then walked to your classroom after a bit. "
            pause 2.0
            jump artclassfri

label artclassfri:
    scene classroom with dissolve
    " You walked into the classroom and got onto your seat. "
    " Waiting for the teacher to arrive... "
    " Just waiting and staring around the room. "
    " Yeah you had nothing to do here. "
    " All you could do was just wait... "
    " Oh hey, the teacher's here. "
    " Time flies by really fast, huh? "
    show sashaneutral at center with easeinright
    mss " Hey there, class! "
    mss " Sorry that I'm a little late, hehe... "
    mss " Turns out I got a liiiiittle too excited to go home. "
    mss " But, now that I'm here... "
    mss " Since I don't want both of us to suffer - "
    mss " We're going to be taking down notes! "
    mss " Just get out your notes and copy the things I have on my slides, 'kay? "
    mss " Shouldn't be too hard, right? "
    mss " Now, time for copying! "
    scene black with dissolve
    " Yet again, you spent the class time copying down notes. "
    " Atleast this is better than doing projects for class. "
    " You didn't have to do much this way. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, time for you to go home. "
    " You got off of your chair, got your things ready and went out of the school. "
    pause 2.0
    jump mcfri

label mcfri:
    scene paperschoolfront with dissolve
    " Looks like it's the end of the day. "
    " You took one last look at your school before leaving. "
    " Something is nagging at you, though... "
    " That feeling of absolute lonliness in your heart. "
    " You tried to ignore it as you went home. "
    scene black with dissolve
    pause 1.0
    scene mcroom with dissolve
    $ lonelyend.grant()
    " As you got home, you couldn't deny it anymore. "
    " You felt extremely lonely. "
    " Maybe you should've talked more... "
    " Or maybe you should've hung out more. "
    " But you can't really do anything about that now. "
    " It's time for you to sleep. "
    scene black with dissolve
    " Good night, [name]. "
    " Enjoy your eternal rest. "
    scene lonelyend with dissolve
    " Dude I thought you knew how this game worked. "
    " Oh well, have this ending I guess. "
    jump credits
    # reminder for alone ending and credits
