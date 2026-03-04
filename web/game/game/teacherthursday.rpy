label teacherthursday:
    show text " DAY 4 - THURSDAY "
    pause 2.0
    scene mcroom with dissolve
    " Good morning, sunshine. "
    " Time to get through another day of you having to teach kids a few things. "
    " And also help a few teachers, of course. "
    " You get into your uniform, pack your things, and you hop off to school. "
    scene black with dissolve
    pause 2.0
    stop music fadeout 1.5
    pause 1.5
    play music "audio/paperhigh.mp3" fadein 1.5
    scene paperschoolfront with dissolve
    " God, things were really a mess yesterday. "
    " Didn't know being a teacher like this could be real stressful. "
    " But that's the part of being alive, I guess. "
    " You suffer every now and then, whether you like it or not. "
    " But there's also good parts, just remember that. "
    scene black with dissolve
    pause 2.0
    scene gardenroom with dissolve
    " You walked into your classroom, feeling just a bit tired. "
    " You decided that you should sleep for a few minutes. "
    " I mean, it's a few hours before school even starts. "
    " You get real comfy in your chair and start dozing off... "
    scene black with dissolve
    pause 2.0
    play sound "audio/bellring.mp3"
    scene gardenroom with dissolve
    " The bell rings, awakening you from your precious nap. "
    " You've slept for a few hours, and now it's time for class to start. "
    " You get up from your chair and go out of your classroom to go to the hallways. "
    scene black with dissolve
    pause 2.0
    jump tthursclass1

label tthursclass1:
    scene hallway with dissolve
    " Who would you like to help for today? "
    if circleknow,demiknow,emilyknow == True:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump mschelpthurs
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump msdhelpthurs
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump msehelpthurs
    elif circleknow,demiknow == True and emilyknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump mschelpthurs
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump msdhelpthurs
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump msehelpthurs
    elif circleknow,emilyknow == True and demiknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump mschelpthurs
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump msdhelpthurs
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump msehelpthurs
    elif demiknow,emilyknow == True and circleknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump mschelpthurs
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump msdhelpthurs
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump msehelpthurs
    elif circleknow == True and demiknow,emilyknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump mschelpthurs
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump msdhelpthurs
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump msehelpthurs
    elif demiknow == True and circleknow,emilyknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump mschelpthurs
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump msdhelpthurs
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump msehelpthurs
    elif emilyknow == True and circleknow,demiknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump mschelpthurs
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump msdhelpthurs
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump msehelpthurs
    else:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump mschelpthurs
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump msdhelpthurs
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump msehelpthurs
    label mschelpthurs:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom and spotted the math teacher letting the students do an activity. "
        " Looking around the room, you found the math teacher arranging her papers at her desk. "
        " Since she isn't busy with teaching the students, you decided to talk to her for just a bit. "
        " Maybe you could also help in teaching the students on how to do the activity properly... "
        show misscircleneutral at center with easeinleft
        if circleknow == True:
            msc " Hmhmhmm... "
            msc " I should probably do something later... "
            msc " Maybe a round around town? "
            msc " Think my legs need a little work... "
            msc " Yeah, I'll definitely go on a round around town later. "
            " You greeted her and asked if she was doing alright. "
            hide misscircleneutral at bottom
            show misscirclehappy at center
            msc " Oh heyyyy [name]! "
            msc " Was just thinking and arranging my papers. "
            msc " I didn't realize my papers were so messy earlier... "
            msc " That's why I decided to arrange them! "
            msc " And I was also just thinking about going laps around the town. "
            hide misscirclehappy at bottom
            show misscircleneutral at center
            " A whole round around town, huh? "
            " You ask her how she's gonna do that without being completely and utterly exhausted. "
            " Your town was pretty much the average size of a town... "
            " ...Your legs can't handle walking a lot though, "
            " Considering you used to stay in your room and looking at new gambling games online. "
            " Like that one where you get cute anime characters. "
            " Can't remember what that one was called... "
            msc " I have pretty good stamina, sooo... "
            msc " I could pretty much go around without a problem! "
            msc " The highest amount of rounds I've gone around in town is abouuuut... "
            msc " 7 rounds! I usually go on walks and runs on the weekends. "
            msc " I could go higher if I just trained a little bit harder... "
            msc " Oh yeah, right! "
            msc " I forgot to tell you something, [name]... "
            if circlelv >= 15 or circlelv == 15:
                msc " I was thinking... "
                msc " I saw how down you felt yesterday. "
                msc " And trust me when I say this, but a frown doesn't fit you. "
                msc " If you don't mind, would you like me to come over later? "
                msc " We could go ahead and play some games to get your mind off of everything. "
                msc " Just relaxing, you know? like good pals? "
                msc " Only if you want to, of course. "
                msc " I don't want to force you into anything! "
                menu:
                    " Let's hang out ":
                        $ circlelv += 10
                        $ circleinvite = True
                        hide misscircleneutral at bottom
                        show misscirclehappy at center
                        msc " Wonderful! "
                        msc " I have a few snacks in my snack drawer, so I could bring those. "
                        msc " We've gotta focus on teaching first, though. "
                        msc " Maybe you could help with helping some of the students? "
                        msc " I know I see some of them struggling over there. "
                        msc " If you don't mind, could you help them? I still have a lot of arranging to do. "
                        " You don't have a choice, do you? "
                        " You nodded and gave a thumbs up to her, agreeing to help. "
                        hide misscirclehappy at bottom
                        show misscircleneutral at center
                        msc " Thank you. "
                        msc " I appreciate your help! "
                        scene black with dissolve
                        " You spent the rest of class hours helping students in their activities. "
                        " You've gotta admit, you got a tad bit little lost on some of the questions... "
                        " But you eventually managed to help the students answer the question. "
                        " Huh, looks like you're learning while you're doing this, too. "
                        " I guess that's a pretty good thing. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for a break. "
                        " You walked out of Miss Circle's classroom, and went to the hallways to chill out. "
                        pause 2.0
                        jump tthursbreak1
                    " Nah im busy 2nite ":
                        msc " Ah, alright. "
                        msc " I was gonna bring over some snacks incase if you said yes... "
                        msc " You can still have some though! "
                        msc " They're in my snack drawer, which is riiight... "
                        msc " Here! A bar of chocolate! "
                        msc " Take it, it's alllll yours! "
                        " You took the bar of chocolate from Miss Circle, then put it into your pockets. "
                        " You then thanked her for the snack. "
                        msc " You're welcome! "
                        msc " Now we should probably start focusing on class. "
                        msc " Maybe you could help with helping some of the students? "
                        msc " I know I see some of them struggling over there. "
                        msc " If you don't mind, could you help them? I still have a lot of arranging to do. "
                        " You don't have a choice, do you? "
                        " You nodded and gave a thumbs up to her, agreeing to help. "
                        hide misscirclehappy at bottom
                        show misscircleneutral at center
                        msc " Thank you. "
                        msc " I appreciate your help! "
                        scene black with dissolve
                        " You spent the rest of class hours helping students in their activities. "
                        " You've gotta admit, you got a tad bit little lost on some of the questions... "
                        " But you eventually managed to help the students answer the question. "
                        " Huh, looks like you're learning while you're doing this, too. "
                        " I guess that's a pretty good thing. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for a break. "
                        " You walked out of Miss Circle's classroom, and went to the hallways to chill out. "
                        pause 2.0
                        jump tthursbreak1
            else:
                msc " I saw you being really down yesterday. "
                msc " I just wanted to tell you that everything's gonna be fine. "
                msc " Things like that happen in life, and we can't do anything about it. "
                msc " Things may seem bad right now, but the kid's in a better place. "
                msc " You get what I'm saying? "
                msc " How about I give you a snack to make you feel better? "
                msc " They're in my snack drawer, which is riiight... "
                msc " Here! A bar of chocolate! "
                msc " Take it, it's alllll yours! "
                " You took the bar of chocolate from Miss Circle, then put it into your pockets. "
                " You then thanked her for the snack. "
                msc " You're welcome! "
                msc " Now we should probably start focusing on class. "
                msc " Maybe you could help with helping some of the students? "
                msc " I know I see some of them struggling over there. "
                msc " If you don't mind, could you help them? I still have a lot of arranging to do. "
                " You don't have a choice, do you? "
                " You nodded and gave a thumbs up to her, agreeing to help. "
                hide misscirclehappy at bottom
                show misscircleneutral at center
                msc " Thank you. "
                msc " I appreciate your help! "
                scene black with dissolve
                " You spent the rest of class hours helping students in their activities. "
                " You've gotta admit, you got a tad bit little lost on some of the questions... "
                " But you eventually managed to help the students answer the question. "
                " Huh, looks like you're learning while you're doing this, too. "
                " I guess that's a pretty good thing. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for a break. "
                " You walked out of Miss Circle's classroom, and went to the hallways to chill out. "
                pause 2.0
                jump tthursbreak1
        else:
            x " Hmhmhmm... "
            x " I should probably do something later... "
            x " Maybe a round around town? "
            x " Think my legs need a little work... "
            x " Yeah, I'll definitely go on a round around town later. "
            " You greeted her and asked if she was doing alright. "
            hide misscircleneutral at bottom
            show misscirclehappy at center
            x " Oh heyyyy [name]! "
            x " Hold on, I don't think we've met before... "
            x " I know that you're that new teacher though! "
            x " It would be rude of me to not introduce myself to you, sooo... "
            $ circleknow = True
            msc " I'm Miss Circle! It's nice to meet you! "
            msc " Anyway, about your question... "
            msc " Was just thinking and arranging my papers. "
            msc " I didn't realize my papers were so messy earlier... "
            msc " That's why I decided to arrange them! "
            msc " And I was also just thinking about going laps around the town. "
            hide misscirclehappy at bottom
            show misscircleneutral at center
            " A whole round around town, huh? "
            " You ask her how she's gonna do that without being completely and utterly exhausted. "
            " Your town was pretty much the average size of a town... "
            " ...Your legs can't handle walking a lot though, "
            " Considering you used to stay in your room and looking at new gambling games online. "
            " Like that one where you get cute anime characters. "
            " Can't remember what that one was called... "
            msc " I have pretty good stamina, sooo... "
            msc " I could pretty much go around without a problem! "
            msc " The highest amount of rounds I've gone around in town is abouuuut... "
            msc " 7 rounds! I usually go on walks and runs on the weekends. "
            msc " I could go higher if I just trained a little bit harder... "
            msc " Oh yeah, right! "
            msc " I forgot to tell you something, [name]... "
            if circlelv >= 15 or circlelv == 15:
                msc " I was thinking... "
                msc " I saw how down you felt yesterday. "
                msc " And trust me when I say this, but a frown doesn't fit you. "
                msc " If you don't mind, would you like me to come over later? "
                msc " We could go ahead and play some games to get your mind off of everything. "
                msc " Just relaxing, you know? like good pals? "
                msc " Only if you want to, of course. "
                msc " I don't want to force you into anything! "
                menu:
                    " Let's hang out ":
                        $ circlelv += 10
                        $ circleinvite = True
                        hide misscircleneutral at bottom
                        show misscirclehappy at center
                        msc " Wonderful! "
                        msc " I have a few snacks in my snack drawer, so I could bring those. "
                        msc " We've gotta focus on teaching first, though. "
                        msc " Maybe you could help with helping some of the students? "
                        msc " I know I see some of them struggling over there. "
                        msc " If you don't mind, could you help them? I still have a lot of arranging to do. "
                        " You don't have a choice, do you? "
                        " You nodded and gave a thumbs up to her, agreeing to help. "
                        hide misscirclehappy at bottom
                        show misscircleneutral at center
                        msc " Thank you. "
                        msc " I appreciate your help! "
                        scene black with dissolve
                        " You spent the rest of class hours helping students in their activities. "
                        " You've gotta admit, you got a tad bit little lost on some of the questions... "
                        " But you eventually managed to help the students answer the question. "
                        " Huh, looks like you're learning while you're doing this, too. "
                        " I guess that's a pretty good thing. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for a break. "
                        " You walked out of Miss Circle's classroom, and went to the hallways to chill out. "
                        pause 2.0
                        jump tthursbreak1
                    " Nah im busy 2nite ":
                        msc " Ah, alright. "
                        msc " I was gonna bring over some snacks incase if you said yes... "
                        msc " You can still have some though! "
                        msc " They're in my snack drawer, which is riiight... "
                        msc " Here! A bar of chocolate! "
                        msc " Take it, it's alllll yours! "
                        " You took the bar of chocolate from Miss Circle, then put it into your pockets. "
                        " You then thanked her for the snack. "
                        msc " You're welcome! "
                        msc " Now we should probably start focusing on class. "
                        msc " Maybe you could help with helping some of the students? "
                        msc " I know I see some of them struggling over there. "
                        msc " If you don't mind, could you help them? I still have a lot of arranging to do. "
                        " You don't have a choice, do you? "
                        " You nodded and gave a thumbs up to her, agreeing to help. "
                        hide misscirclehappy at bottom
                        show misscircleneutral at center
                        msc " Thank you. "
                        msc " I appreciate your help! "
                        scene black with dissolve
                        " You spent the rest of class hours helping students in their activities. "
                        " You've gotta admit, you got a tad bit little lost on some of the questions... "
                        " But you eventually managed to help the students answer the question. "
                        " Huh, looks like you're learning while you're doing this, too. "
                        " I guess that's a pretty good thing. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for a break. "
                        " You walked out of Miss Circle's classroom, and went to the hallways to chill out. "
                        pause 2.0
                        jump tthursbreak1
            else:
                msc " I saw you being really down yesterday. "
                msc " I just wanted to tell you that everything's gonna be fine. "
                msc " Things like that happen in life, and we can't do anything about it. "
                msc " Things may seem bad right now, but the kid's in a better place. "
                msc " You get what I'm saying? "
                msc " How about I give you a snack to make you feel better? "
                msc " They're in my snack drawer, which is riiight... "
                msc " Here! A bar of chocolate! "
                msc " Take it, it's alllll yours! "
                " You took the bar of chocolate from Miss Circle, then put it into your pockets. "
                " You then thanked her for the snack. "
                msc " You're welcome! "
                msc " Now we should probably start focusing on class. "
                msc " Maybe you could help with helping some of the students? "
                msc " I know I see some of them struggling over there. "
                msc " If you don't mind, could you help them? I still have a lot of arranging to do. "
                " You don't have a choice, do you? "
                " You nodded and gave a thumbs up to her, agreeing to help. "
                hide misscirclehappy at bottom
                show misscircleneutral at center
                msc " Thank you. "
                msc " I appreciate your help! "
                scene black with dissolve
                " You spent the rest of class hours helping students in their activities. "
                " You've gotta admit, you got a tad bit little lost on some of the questions... "
                " But you eventually managed to help the students answer the question. "
                " Huh, looks like you're learning while you're doing this, too. "
                " I guess that's a pretty good thing. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for a break. "
                " You walked out of Miss Circle's classroom, and went to the hallways to chill out. "
                pause 2.0
                jump tthursbreak1
    label msdhelpthurs:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the music teacher's classroom and looked around... "
        " Seems like the students are all answering something. "
        " Looking around, you spotted the music teacher walking around and making sure no one was copying off of eachother. "
        " You wanted to talk to him, but you also didn't want to disturb him. "
        " You look a little awkward just standing there... "
        " Eventually, after a bit of walking around, the music teacher notices you. "
        " He looked a little nervous though since he didn't notice you at all. "
        show mrdemineutral at center with easeinleft
        if demiknow == True:
            msd " Oh geez, I'm sorry that I didn't notice you, [name]... "
            msd " It was just that...I was looking around to see if any of my students would cheat... "
            msd " Please forgive me... "
            " You told him that it was alright. "
            " You totally weren't standing there and waiting for him to notice you. "
            " Totally. That would look too suspicious. "
            msd " ...Whew, okay... "
            msd " But, um... "
            msd " Hold on...I had to tell you something, but... "
            msd " I kinda forgot what it was, um... "
            msd " Give me a few minutes to think, please? "
            " You just gave him a thumbs up and waited for him to think of what he wanted to say. "
            " You were a chill [person], you could wait. "
            " Not for hours though. "
            " Your bored ass would start playing games on your phone. "
            msd " Uh...oh, um, right! "
            if demilv >= 15 or demilv == 15:
                msd " I know how upset you were yesterday... "
                msd " And honestly...? "
                msd " I don't really like seeing a frown on your face... "
                msd " (This is embarrassing to say...) "
                msd " (Good heavens, please save me...) "
                msd " (What else did I have to tell [them]?) "
                msd " (Um...) "
                msd " And I, umm... "
                msd " I want to try making you feel better... "
                msd " I-if you don't mind... "
                msd " Would you...like me to spend time with you...? "
                msd " At y-your house, I mean...! "
                msd " It's okay if you don't want me t-to, really...!!! "
                msd " ...I just...wish I could make you feel better... "
                menu:
                    " lets hang out music boy ":
                        $ demilv += 10
                        $ demiinvite = True
                        hide mrdemineutral at bottom
                        show mrdemiflush at center
                        msd " ...music boy????? "
                        msd " (Did [they] really just call me that???) "
                        msd " (Not htat I mind...) "
                        msd " (It's kinda cute that [they]...) "
                        msd " (WHATHUHWHATWHUHUHUSHADUSAHDJKASHDJKBH){nw} "
                        msd " AHEM...uh... "
                        hide mrdemiflush at bottom
                        show mrdemihappy at center
                        msd " I'll uh... "
                        msd " I'll bring some snacks and maybe we could talk about a few things...? "
                        msd " Like life - things that happened... "
                        msd " ...O-or we could go ahead and play games...! "
                        msd " Anything you want, just so you can feel bette...!! "
                        msd " I'm fine with anything, soo... "
                        msd " ...(cough.) "
                        hide mrdemihappy at bottom
                        show mrdemineutral at center
                        msd " A-anyway... "
                        msd " Do you think you could help in watching over the students...? "
                        msd " I really don't want any one of them to cheat... "
                        msd " I gave them a lot of time to study for this, too.. "
                        msd " So could you...please...help me...? "
                        " You don't really have a choice in this, do you?? "
                        " You nodded in approval, you're gonna help this poor guy out. "
                        msd " O-okay...thank you... "
                        msd " I'll take this side, and you take that side..? "
                        msd " Thanks for choosing to help again, [name]... "
                        msd " I always appreciate your help... "
                        scene black with dissolve
                        " You spent the rest of the class hours helping Mister Demi watch over the students. "
                        " No one would dare cheat under your gaze. "
                        " That goofy ass gaze that you got. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for a break. "
                        " You walked out of Mister Demi's classroom and then went into the hallways. "
                        pause 2.0
                        jump tthursbreak1
                    " I'm busy sorry ":
                        msd " Oouuu...alright.... "
                        msd " I just hope that you feel better later though... "
                        msd " I know how stressed you must've been that day.. "
                        msd " I was, too... "
                        msd " A-anyway... "
                        msd " Do you think you could help in watching over the students...? "
                        msd " I really don't want any one of them to cheat... "
                        msd " I gave them a lot of time to study for this, too.. "
                        msd " So could you...please...help me...? "
                        " You don't really have a choice in this, do you?? "
                        " You nodded in approval, you're gonna help this poor guy out. "
                        msd " O-okay...thank you... "
                        msd " I'll take this side, and you take that side..? "
                        msd " Thanks for choosing to help again, [name]... "
                        msd " I always appreciate your help... "
                        scene black with dissolve
                        " You spent the rest of the class hours helping Mister Demi watch over the students. "
                        " No one would dare cheat under your gaze. "
                        " That goofy ass gaze that you got. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for a break. "
                        " You walked out of Mister Demi's classroom and then went into the hallways. "
                        pause 2.0
                        jump tthursbreak1
            else:
                msd " I saw how upset you were yesterday... "
                msd " A-and I just wanted to say... "
                msd " I, um...I hope you feel better soon... "
                msd " A frown doesn't suit your face, really... "
                msd " (oh my god why does this sound like im flirting with [them]) "
                msd " (I need to figure out how to word things better...) "
                msd " A-anyway... "
                msd " Do you think you could help in watching over the students...? "
                msd " I really don't want any one of them to cheat... "
                msd " I gave them a lot of time to study for this, too.. "
                msd " So could you...please...help me...? "
                " You don't really have a choice in this, do you?? "
                " You nodded in approval, you're gonna help this poor guy out. "
                msd " O-okay...thank you... "
                msd " I'll take this side, and you take that side..? "
                msd " Thanks for choosing to help again, [name]... "
                msd " I always appreciate your help... "
                scene black with dissolve
                " You spent the rest of the class hours helping Mister Demi watch over the students. "
                " No one would dare cheat under your gaze. "
                " That goofy ass gaze that you got. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for a break. "
                " You walked out of Mister Demi's classroom and then went into the hallways. "
                pause 2.0
                jump tthursbreak1
        else:
            x " Oh geez, I'm sorry that I didn't notice you, [name]... "
            x " It was just that...I was looking around to see if any of my students would cheat... "
            x " Please forgive me... "
            " You told him that it was alright. "
            " You totally weren't standing there and waiting for him to notice you. "
            " Totally. That would look too suspicious. "
            x " ...Whew, okay... "
            x " But, um... "
            x " I don't think we've met before... "
            x " I mean, I have seen you around, yes... "
            x " But I don't think I ever got to introduce myself to you... "
            x " Uh, ah...let me do that right now... "
            $ demiknow = True
            msd " I-I'm Mister Demi...the music teacher... "
            msd " And, um... "
            msd " Hold on...I had to tell you something, but... "
            msd " I kinda forgot what it was, um... "
            msd " Give me a few minutes to think, please? "
            " You just gave him a thumbs up and waited for him to think of what he wanted to say. "
            " You were a chill [person], you could wait. "
            " Not for hours though. "
            " Your bored ass would start playing games on your phone. "
            msd " Uh...oh, um, right! "
            if demilv >= 15 or demilv == 15:
                msd " I know how upset you were yesterday... "
                msd " And honestly...? "
                msd " I don't really like seeing a frown on your face... "
                msd " (This is embarrassing to say...) "
                msd " (Good heavens, please save me...) "
                msd " (What else did I have to tell [them]?) "
                msd " (Um...) "
                msd " And I, umm... "
                msd " I want to try making you feel better... "
                msd " I-if you don't mind... "
                msd " Would you...like me to spend time with you...? "
                msd " At y-your house, I mean...! "
                msd " It's okay if you don't want me t-to, really...!!! "
                msd " ...I just...wish I could make you feel better... "
                menu:
                    " lets hang out music boy ":
                        $ demilv += 10
                        $ demiinvite = True
                        hide mrdemineutral at bottom
                        show mrdemiflush at center
                        msd " ...music boy????? "
                        msd " (Did [they] really just call me that???) "
                        msd " (Not htat I mind...) "
                        msd " (It's kinda cute that [they]...) "
                        msd " (WHATHUHWHATWHUHUHUSHADUSAHDJKASHDJKBH){nw} "
                        msd " AHEM...uh... "
                        hide mrdemiflush at bottom
                        show mrdemihappy at center
                        msd " I'll uh... "
                        msd " I'll bring some snacks and maybe we could talk about a few things...? "
                        msd " Like life - things that happened... "
                        msd " ...O-or we could go ahead and play games...! "
                        msd " Anything you want, just so you can feel bette...!! "
                        msd " I'm fine with anything, soo... "
                        msd " ...(cough.) "
                        hide mrdemihappy at bottom
                        show mrdemineutral at center
                        msd " A-anyway... "
                        msd " Do you think you could help in watching over the students...? "
                        msd " I really don't want any one of them to cheat... "
                        msd " I gave them a lot of time to study for this, too.. "
                        msd " So could you...please...help me...? "
                        " You don't really have a choice in this, do you?? "
                        " You nodded in approval, you're gonna help this poor guy out. "
                        msd " O-okay...thank you... "
                        msd " I'll take this side, and you take that side..? "
                        msd " Thanks for choosing to help again, [name]... "
                        msd " I always appreciate your help... "
                        scene black with dissolve
                        " You spent the rest of the class hours helping Mister Demi watch over the students. "
                        " No one would dare cheat under your gaze. "
                        " That goofy ass gaze that you got. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for a break. "
                        " You walked out of Mister Demi's classroom and then went into the hallways. "
                        pause 2.0
                        jump tthursbreak1
                    " I'm busy sorry ":
                        msd " Oouuu...alright.... "
                        msd " I just hope that you feel better later though... "
                        msd " I know how stressed you must've been that day.. "
                        msd " I was, too... "
                        msd " A-anyway... "
                        msd " Do you think you could help in watching over the students...? "
                        msd " I really don't want any one of them to cheat... "
                        msd " I gave them a lot of time to study for this, too.. "
                        msd " So could you...please...help me...? "
                        " You don't really have a choice in this, do you?? "
                        " You nodded in approval, you're gonna help this poor guy out. "
                        msd " O-okay...thank you... "
                        msd " I'll take this side, and you take that side..? "
                        msd " Thanks for choosing to help again, [name]... "
                        msd " I always appreciate your help... "
                        scene black with dissolve
                        " You spent the rest of the class hours helping Mister Demi watch over the students. "
                        " No one would dare cheat under your gaze. "
                        " That goofy ass gaze that you got. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for a break. "
                        " You walked out of Mister Demi's classroom and then went into the hallways. "
                        pause 2.0
                        jump tthursbreak1
            else:
                msd " I saw how upset you were yesterday... "
                msd " A-and I just wanted to say... "
                msd " I, um...I hope you feel better soon... "
                msd " A frown doesn't suit your face, really... "
                msd " (oh my god why does this sound like im flirting with [them]) "
                msd " (I need to figure out how to word things better...) "
                msd " A-anyway... "
                msd " Do you think you could help in watching over the students...? "
                msd " I really don't want any one of them to cheat... "
                msd " I gave them a lot of time to study for this, too.. "
                msd " So could you...please...help me...? "
                " You don't really have a choice in this, do you?? "
                " You nodded in approval, you're gonna help this poor guy out. "
                msd " O-okay...thank you... "
                msd " I'll take this side, and you take that side..? "
                msd " Thanks for choosing to help again, [name]... "
                msd " I always appreciate your help... "
                scene black with dissolve
                " You spent the rest of the class hours helping Mister Demi watch over the students. "
                " No one would dare cheat under your gaze. "
                " That goofy ass gaze that you got. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for a break. "
                " You walked out of Mister Demi's classroom and then went into the hallways. "
                pause 2.0
                jump tthursbreak1
    label msehelpthurs:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the history teachers classroom and looked around for a bit... "
        " Looks like the teacher's making everyone do an activity. "
        " Huh. I just now realized that they all have to be doing activities so that it wouldn't be awkward. "
        " I mean, imagine just stepping into your friends classroom... "
        " ...Only to talk about some stupid shit like gambling. "
        " The students are gonna hear about it. They'll spread information about it. "
        " Just really awkward in all honesty. "
        " Anyway, you looked around a little more and saw the history teacher helping a student. "
        " You waited until she wasn't busy and then walked up to her. "
        show msemilyneutral at center with easeinleft
        if emilyknow == True:
            mse " Hello there, [name]! "
            mse " Lovely seeing you here, as always. "
            mse " You had something to tell me? "
            mse " Actually, since I'm letting my students do their work... "
            hide msemilyneutral at bottom
            show msemilyhappy at center
            mse " We could spend the rest of class hours hanging out! "
            mse " Not like Miss Grace cares that much anyway... "
            hide msemilyhappy at bottom
            show msemilyneutral at center
            mse " As long as we kind of have an excuse to hang out, then we're good. "
            mse " Maybe I could say that you were helping on comforting a student? "
            mse " About their, uhh...project being trash? "
            mse " Does that sound like a reasonable excuse? "
            " You shrug. "
            " You don't really know if it would work or not, but at the same time... "
            " It sounded like something that would totally work. "
            " Considering the fact that Miss Grace doesn't care too much about the stuff you guys do. "
            mse " Yeah, it's probably gonna fool her for a bit... "
            mse " Oooh, wait! I just remembered I had to tell you something... "
            mse " What was it again? hmmm... "
            " You waited patiently for her to remember. "
            " After a bit, she speaks up again. "
            mse " Ohhh...right, right. "
            mse " Look, I don't mean to make you uncomfortable with this, buuuut... "
            mse " I just need you to listen to me real quick, okay? "
            if emilylv >= 15 or emilylv == 15:
                hide msemilyneutral at bottom
                show msemilysad at center
                mse " I know how distraught you must be after what happened. "
                mse " The situation yesterday, I mean. "
                mse " Even if we wanted to save the kid, there's... "
                mse " ...Really nothing we could do about it. "
                mse " Most likely the kid was killed before everyone even got to school. "
                mse " Leaving them to die alone with no one to help them... "
                mse " I can't exactly just revive them to make you feel better, but... "
                mse " I want to atleast try doing something to bring a smile on your face. "
                mse " Seeing you sad makes me upset too. "
                mse " Upset that I couldn't have done better in looking. "
                mse " Upset that I didn't notice what was going wrong. "
                mse " So, I want to atleast try and make your day brighter. "
                mse " I don't know if you actually wanna hang out with me, but uh... "
                mse " Could I come over to your house to spend some time with you? "
                mse " It's of course okay if you don't want to hang out. "
                mse " After all, I respect your decisions...or boundaries, whatever the word was. "
                mse " But, we could maybe...talk and play a few games to get your mind off of things. "
                mse " And we could also get to get to know eachother. "
                mse " Again, completely fine if you don't want to. "
                mse " I don't wanna make you uncomfy, after all! I would be a bad friend if I did that... "
                mse " So, uh...what do you say, [name]? "
                menu:
                    " Let's hangout ":
                        $ emilylv += 10
                        $ emilyinvite = True
                        hide msemilysad at bottom
                        show msemilyhappy at center
                        mse " Great! it's settled, then! "
                        mse " Though I'm going to have to steal some of the snacks from Miss Circle's snack drawer... "
                        mse " I don't really have my own snack drawer because I don't wanna waste money. "
                        mse " I mean, I'll have to restock everything if I do that - "
                        mse " - And that's gonna make me lose a lotta money, even if it seems little! "
                        mse " That's why I kind of just buy from the cafeteria in this school. "
                        mse " Ooooor, I steal from Circle's snack drawer! "
                        mse " She doesn't usually mind, but she does whenever I steal her oreos. "
                        hide msemilyhappy at bottom
                        show msemilyneutral at center
                        mse " One time I tried getting her oreos - "
                        mse " - And mind you, she was FAR, far away. "
                        mse " Like I'm talking the back of school far away! "
                        mse " I opened her snack drawer... "
                        mse " Gently grabbed the oreos... "
                        mse " And the moment I turn back, she was already there!! "
                        mse " I mean, I knew she would kinda be coming after me for taking her oreos... "
                        mse " But I didn't expect her to come over THAT FAST!! "
                        mse " This woman never fails to surprise me, really... "
                        mse " Another time she surprised me was when I saw her feeding her own compass hand a kitkat. "
                        mse " I don't know how to explain it, but that's what I saw! "
                        mse " Like dude??? don't you hate kitkats?? "
                        mse " She literally went on a rant about kitkats this one time... "
                        mse " And now I see her feeding her...thing...kitkats??? "
                        mse " This woman has many surprises up her sleeve, I tell you... "
                        scene black with dissolve
                        " You spent the rest of the class hours talking with Miss Emily. "
                        " You two weren't really talking about anything important, of course. "
                        " Just talking about silly little things. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for a break. "
                        " You walked out of Miss Emily's classroom and went to the hallways. "
                        pause 2.0
                        jump tthursbreak1
                    " I'm busy tonight, sorry ":
                        hide msemilysad at bottom
                        show msemilyneutral at center
                        mse " Oh, that's fine! "
                        mse " While you're here though, you want me to ge you a snack? "
                        mse " Though I'm going to have to steal some of the snacks from Miss Circle's snack drawer... "
                        mse " I don't really have my own snack drawer because I don't wanna waste money. "
                        mse " I mean, I'll have to restock everything if I do that - "
                        mse " - And that's gonna make me lose a lotta money, even if it seems little! "
                        mse " That's why I kind of just buy from the cafeteria in this school. "
                        mse " Ooooor, I steal from Circle's snack drawer! "
                        mse " She doesn't usually mind, but she does whenever I steal her oreos. "
                        hide msemilyhappy at bottom
                        show msemilyneutral at center
                        mse " One time I tried getting her oreos - "
                        mse " - And mind you, she was FAR, far away. "
                        mse " Like I'm talking the back of school far away! "
                        mse " I opened her snack drawer... "
                        mse " Gently grabbed the oreos... "
                        mse " And the moment I turn back, she was already there!! "
                        mse " I mean, I knew she would kinda be coming after me for taking her oreos... "
                        mse " But I didn't expect her to come over THAT FAST!! "
                        mse " This woman never fails to surprise me, really... "
                        mse " Another time she surprised me was when I saw her feeding her own compass hand a kitkat. "
                        mse " I don't know how to explain it, but that's what I saw! "
                        mse " Like dude??? don't you hate kitkats?? "
                        mse " She literally went on a rant about kitkats this one time... "
                        mse " And now I see her feeding her...thing...kitkats??? "
                        mse " This woman has many surprises up her sleeve, I tell you... "
                        scene black with dissolve
                        " You spent the rest of the class hours talking with Miss Emily. "
                        " You two weren't really talking about anything important, of course. "
                        " Just talking about silly little things. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for a break. "
                        " You walked out of Miss Emily's classroom and went to the hallways. "
                        pause 2.0
                        jump tthursbreak1
            else:
                hide msemilyneutral at bottom
                show msemilysad at center
                mse " I saw how stressed you were yesterday... "
                mse " You know, I'm the type of person who doesn't want someone to fele sad. "
                mse " But, then again... "
                mse " We can't really do anything about what has already happened. "
                mse " All I can do is offer you a hug. "
                mse " Hopefully that'll make you feel better... "
                " Miss Emily walks closer to you and gives you a nice warm hug. "
                " It lasts for a few seconds before you pull away. "
                mse " I hope I could've atleast made your day just a bit brighter. "
                mse " Sorry if I brung down the mood a little... "
                mse " But I really just wanted to say that to you. "
                hide msemilysad at bottom
                show msemilyneutral at center
                mse " While you're here though, you want me to ge you a snack? "
                mse " Though I'm going to have to steal some of the snacks from Miss Circle's snack drawer... "
                mse " I don't really have my own snack drawer because I don't wanna waste money. "
                mse " I mean, I'll have to restock everything if I do that - "
                mse " - And that's gonna make me lose a lotta money, even if it seems little! "
                mse " That's why I kind of just buy from the cafeteria in this school. "
                mse " Ooooor, I steal from Circle's snack drawer! "
                mse " She doesn't usually mind, but she does whenever I steal her oreos. "
                hide msemilyhappy at bottom
                show msemilyneutral at center
                mse " One time I tried getting her oreos - "
                mse " - And mind you, she was FAR, far away. "
                mse " Like I'm talking the back of school far away! "
                mse " I opened her snack drawer... "
                mse " Gently grabbed the oreos... "
                mse " And the moment I turn back, she was already there!! "
                mse " I mean, I knew she would kinda be coming after me for taking her oreos... "
                mse " But I didn't expect her to come over THAT FAST!! "
                mse " This woman never fails to surprise me, really... "
                mse " Another time she surprised me was when I saw her feeding her own compass hand a kitkat. "
                mse " I don't know how to explain it, but that's what I saw! "
                mse " Like dude??? don't you hate kitkats?? "
                mse " She literally went on a rant about kitkats this one time... "
                mse " And now I see her feeding her...thing...kitkats??? "
                mse " This woman has many surprises up her sleeve, I tell you... "
                scene black with dissolve
                " You spent the rest of the class hours talking with Miss Emily. "
                " You two weren't really talking about anything important, of course. "
                " Just talking about silly little things. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for a break. "
                " You walked out of Miss Emily's classroom and went to the hallways. "
                pause 2.0
                jump tthursbreak1
        else:
            x " Hello there, [name]! "
            x " Lovely seeing you here, as always. "
            x " Now, I don't think I've ever gotten to introduce myself to you before... "
            x " Apologies, really. "
            $ emilyknow = True
            mse " I'm Miss Emily - history teacher. "
            mse " Loads of people tell me I teach a boring subject, but I honestly don't really care. "
            mse " Ahem...um, anyways. "
            mse " You had something to tell me? "
            mse " Actually, since I'm letting my students do their work... "
            hide msemilyneutral at bottom
            show msemilyhappy at center
            mse " We could spend the rest of class hours hanging out! "
            mse " Not like Miss Grace cares that much anyway... "
            hide msemilyhappy at bottom
            show msemilyneutral at center
            mse " As long as we kind of have an excuse to hang out, then we're good. "
            mse " Maybe I could say that you were helping on comforting a student? "
            mse " About their, uhh...project being trash? "
            mse " Does that sound like a reasonable excuse? "
            " You shrug. "
            " You don't really know if it would work or not, but at the same time... "
            " It sounded like something that would totally work. "
            " Considering the fact that Miss Grace doesn't care too much about the stuff you guys do. "
            mse " Yeah, it's probably gonna fool her for a bit... "
            mse " Oooh, wait! I just remembered I had to tell you something... "
            mse " What was it again? hmmm... "
            " You waited patiently for her to remember. "
            " After a bit, she speaks up again. "
            mse " Ohhh...right, right. "
            mse " Look, I don't mean to make you uncomfortable with this, buuuut... "
            mse " I just need you to listen to me real quick, okay? "
            if emilylv >= 15 or emilylv == 15:
                hide msemilyneutral at bottom
                show msemilysad at center
                mse " I know how distraught you must be after what happened. "
                mse " The situation yesterday, I mean. "
                mse " Even if we wanted to save the kid, there's... "
                mse " ...Really nothing we could do about it. "
                mse " Most likely the kid was killed before everyone even got to school. "
                mse " Leaving them to die alone with no one to help them... "
                mse " I can't exactly just revive them to make you feel better, but... "
                mse " I want to atleast try doing something to bring a smile on your face. "
                mse " Seeing you sad makes me upset too. "
                mse " Upset that I couldn't have done better in looking. "
                mse " Upset that I didn't notice what was going wrong. "
                mse " So, I want to atleast try and make your day brighter. "
                mse " I don't know if you actually wanna hang out with me, but uh... "
                mse " Could I come over to your house to spend some time with you? "
                mse " It's of course okay if you don't want to hang out. "
                mse " After all, I respect your decisions...or boundaries, whatever the word was. "
                mse " But, we could maybe...talk and play a few games to get your mind off of things. "
                mse " And we could also get to get to know eachother. "
                mse " Again, completely fine if you don't want to. "
                mse " I don't wanna make you uncomfy, after all! I would be a bad friend if I did that... "
                mse " So, uh...what do you say, [name]? "
                menu:
                    " Let's hangout ":
                        $ emilylv += 10
                        $ emilyinvite = True
                        hide msemilysad at bottom
                        show msemilyhappy at center
                        mse " Great! it's settled, then! "
                        mse " Though I'm going to have to steal some of the snacks from Miss Circle's snack drawer... "
                        mse " I don't really have my own snack drawer because I don't wanna waste money. "
                        mse " I mean, I'll have to restock everything if I do that - "
                        mse " - And that's gonna make me lose a lotta money, even if it seems little! "
                        mse " That's why I kind of just buy from the cafeteria in this school. "
                        mse " Ooooor, I steal from Circle's snack drawer! "
                        mse " She doesn't usually mind, but she does whenever I steal her oreos. "
                        hide msemilyhappy at bottom
                        show msemilyneutral at center
                        mse " One time I tried getting her oreos - "
                        mse " - And mind you, she was FAR, far away. "
                        mse " Like I'm talking the back of school far away! "
                        mse " I opened her snack drawer... "
                        mse " Gently grabbed the oreos... "
                        mse " And the moment I turn back, she was already there!! "
                        mse " I mean, I knew she would kinda be coming after me for taking her oreos... "
                        mse " But I didn't expect her to come over THAT FAST!! "
                        mse " This woman never fails to surprise me, really... "
                        mse " Another time she surprised me was when I saw her feeding her own compass hand a kitkat. "
                        mse " I don't know how to explain it, but that's what I saw! "
                        mse " Like dude??? don't you hate kitkats?? "
                        mse " She literally went on a rant about kitkats this one time... "
                        mse " And now I see her feeding her...thing...kitkats??? "
                        mse " This woman has many surprises up her sleeve, I tell you... "
                        scene black with dissolve
                        " You spent the rest of the class hours talking with Miss Emily. "
                        " You two weren't really talking about anything important, of course. "
                        " Just talking about silly little things. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for a break. "
                        " You walked out of Miss Emily's classroom and went to the hallways. "
                        pause 2.0
                        jump tthursbreak1
                    " I'm busy tonight, sorry ":
                        hide msemilysad at bottom
                        show msemilyneutral at center
                        mse " Oh, that's fine! "
                        mse " While you're here though, you want me to ge you a snack? "
                        mse " Though I'm going to have to steal some of the snacks from Miss Circle's snack drawer... "
                        mse " I don't really have my own snack drawer because I don't wanna waste money. "
                        mse " I mean, I'll have to restock everything if I do that - "
                        mse " - And that's gonna make me lose a lotta money, even if it seems little! "
                        mse " That's why I kind of just buy from the cafeteria in this school. "
                        mse " Ooooor, I steal from Circle's snack drawer! "
                        mse " She doesn't usually mind, but she does whenever I steal her oreos. "
                        hide msemilyhappy at bottom
                        show msemilyneutral at center
                        mse " One time I tried getting her oreos - "
                        mse " - And mind you, she was FAR, far away. "
                        mse " Like I'm talking the back of school far away! "
                        mse " I opened her snack drawer... "
                        mse " Gently grabbed the oreos... "
                        mse " And the moment I turn back, she was already there!! "
                        mse " I mean, I knew she would kinda be coming after me for taking her oreos... "
                        mse " But I didn't expect her to come over THAT FAST!! "
                        mse " This woman never fails to surprise me, really... "
                        mse " Another time she surprised me was when I saw her feeding her own compass hand a kitkat. "
                        mse " I don't know how to explain it, but that's what I saw! "
                        mse " Like dude??? don't you hate kitkats?? "
                        mse " She literally went on a rant about kitkats this one time... "
                        mse " And now I see her feeding her...thing...kitkats??? "
                        mse " This woman has many surprises up her sleeve, I tell you... "
                        scene black with dissolve
                        " You spent the rest of the class hours talking with Miss Emily. "
                        " You two weren't really talking about anything important, of course. "
                        " Just talking about silly little things. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for a break. "
                        " You walked out of Miss Emily's classroom and went to the hallways. "
                        pause 2.0
                        jump tthursbreak1
            else:
                hide msemilyneutral at bottom
                show msemilysad at center
                mse " I saw how stressed you were yesterday... "
                mse " You know, I'm the type of person who doesn't want someone to fele sad. "
                mse " But, then again... "
                mse " We can't really do anything about what has already happened. "
                mse " All I can do is offer you a hug. "
                mse " Hopefully that'll make you feel better... "
                " Miss Emily walks closer to you and gives you a nice warm hug. "
                " It lasts for a few seconds before you pull away. "
                mse " I hope I could've atleast made your day just a bit brighter. "
                mse " Sorry if I brung down the mood a little... "
                mse " But I really just wanted to say that to you. "
                hide msemilysad at bottom
                show msemilyneutral at center
                mse " While you're here though, you want me to ge you a snack? "
                mse " Though I'm going to have to steal some of the snacks from Miss Circle's snack drawer... "
                mse " I don't really have my own snack drawer because I don't wanna waste money. "
                mse " I mean, I'll have to restock everything if I do that - "
                mse " - And that's gonna make me lose a lotta money, even if it seems little! "
                mse " That's why I kind of just buy from the cafeteria in this school. "
                mse " Ooooor, I steal from Circle's snack drawer! "
                mse " She doesn't usually mind, but she does whenever I steal her oreos. "
                hide msemilyhappy at bottom
                show msemilyneutral at center
                mse " One time I tried getting her oreos - "
                mse " - And mind you, she was FAR, far away. "
                mse " Like I'm talking the back of school far away! "
                mse " I opened her snack drawer... "
                mse " Gently grabbed the oreos... "
                mse " And the moment I turn back, she was already there!! "
                mse " I mean, I knew she would kinda be coming after me for taking her oreos... "
                mse " But I didn't expect her to come over THAT FAST!! "
                mse " This woman never fails to surprise me, really... "
                mse " Another time she surprised me was when I saw her feeding her own compass hand a kitkat. "
                mse " I don't know how to explain it, but that's what I saw! "
                mse " Like dude??? don't you hate kitkats?? "
                mse " She literally went on a rant about kitkats this one time... "
                mse " And now I see her feeding her...thing...kitkats??? "
                mse " This woman has many surprises up her sleeve, I tell you... "
                scene black with dissolve
                " You spent the rest of the class hours talking with Miss Emily. "
                " You two weren't really talking about anything important, of course. "
                " Just talking about silly little things. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for a break. "
                " You walked out of Miss Emily's classroom and went to the hallways. "
                pause 2.0
                jump tthursbreak1
label tthursbreak1:
    scene hallway with dissolve
    " You walked into the hallways and noticed a lot of trash on the floor in an empty hallway. "
    " You're wondering if this is just bait for the janitor. "
    " Well, you're not letting anyone getting strangled today. "
    " You're just gonna have to do this job yourself. "
    " I mean, atleast it gives you something to do in your free time. "
    " The teachers you hang out with aren't here, soo.... "
    " This is basically your only source of entertainment. "
    " Other than looking at your phone, of course. "
    " But we're not using your phone this time. "
    " Let's do something productive for once!! "
    " ...Is it productive though? not sure. "
    " Anyway, you grab a broom from the cleaning closet nearby and started cleaning. "
    " While you were cleaning, you decided to do a little trash-basketball. "
    " You grabbed a ball of paper anndddd... "
    " Boom! nice shot, you landed it in perfectly. "
    " Extra points for being far away, too. "
    " This makes you feel cooler in your own way. "
    " Even if someone thinks that you're being weird right now, "
    " This is just peak sports that they will never understand. "
    " Huh. Trashket-ball...they could make that a sport. "
    " Somehow. "
    scene black with dissolve
    " You spent the rest of the break cleaning a few hallways. "
    " You knew that these were just going to get dirty again, "
    " But things still look nicer while they're clean. "
    " Even if they're just going to get dirty all over again. "
    " We all get dirty here and there. "
    " But not we're not getting down dirty. This is a befriending sim. "
    " Come on man go take that somewhere else. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit. Looks like it's time to help someone again. "
    " You then started walking around to see who needed help... "
    pause 2.0
    jump tthursclass2
label tthursclass2:
    scene hallway with dissolve
    " Who do you wanna help for today? "
    if bloomieknow,thavelknow,sashaknow == True:
        menu:
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump msbthurshelp
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump mstthurshelp
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump mssthurshelp
    elif bloomieknow,thavelknow == True and sashaknow == False:
        menu:
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump msbthurshelp
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump mstthurshelp
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump mssthurshelp
    elif bloomieknow,sashaknow == True and thavelknow == False:
        menu:
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump msbthurshelp
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump mstthurshelp
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump mssthurshelp
    elif sashaknow,thavelknow == True and bloomieknow == False:
        menu:
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump msbthurshelp
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump mstthurshelp
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump mssthurshelp
    elif bloomieknow == True and thavelknow,sashaknow == False:
        menu:
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump msbthurshelp
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump mstthurshelp
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump mssthurshelp
    elif thavelknow == True and bloomieknow,sashaknow == False:
        menu:
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump msbthurshelp
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump mstthurshelp
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump mssthurshelp
    elif sashaknow == True and bloomieknow,thavelknow == False:
        menu:
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump msbthurshelp
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump mstthurshelp
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump mssthurshelp
    else:
        menu:
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump msbthurshelp
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump mstthurshelp
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump mssthurshelp
    label msbthurshelp:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked to the science teacher's classroom... "
        " Looks like the teacher is making the students make potions. "
        " Interesting...they're making a firework potion. "
        " Wonder what they're going to do with that. "
        " You looked around and spotted the science teacher in the corner, observing her students. "
        " You decided to walk over to her and make some conversation. "
        show missbloomieneutral at center with easeinleft
        if bloomieknow == True:
            msb " Hmm... "
            msb " My students are doing particulary well today. "
            msb " That's good... "
            msb " Perhaps they've been finally paying attention. "
            msb " That's really good, if that's the case. "
            " You greeted her and asked what she was doing. "
            msb " Hm? oh. [name], hello there. "
            msb " I'm just observing my students on doing their activity. "
            msb " Making sure they don't do anything wrong... "
            msb " I wouldn't want my entire classroom to get blown up, after all. "
            msb " That...situation has happened before in the past, actually. "
            msb " That's why I'm looking after my students more. "
            msb " So that they won't do anything idiotic to cancel school. "
            msb " They're always finding ways to cancel school... "
            msb " And I don't want Miss Grace to get mad at me for letting them have no school. "
            msb " I remember how she reacted when she found my classroom being blown up... "
            msb " Hoouughh...not good times, I'll tell you that. "
            msb " Oh, and uh...before I forget. "
            msb " I had something to tell you. "
            if bloomielv >= 15 or bloomielv == 15:
                msb " I saw how upset you were yesterday. "
                msb " And, I have to admit... "
                msb " Seeing you sad kind of shattered my heart just a bit. "
                msb " I expected myself not to really care, but... "
                msb " I uh...felt really sad the moment I saw you stressing out. "
                msb " I honestly thought that I was being a little dramatic, yes... "
                msb " But the more I saw you being upset about the situation, the more bad I felt. "
                msb " I couldn't just stand there and do nothing about it. "
                msb " So, I requested Miss Grace to let you rest for the rest of the day. "
                msb " That's the reason why you weren't a part of the lookout thing we did yesterday. "
                msb " I thought that while you were gone, my thoughts of you would dissolve, too... "
                msb " But the thoughts kept coming back over and over again. "
                msb " I can't believe I'm saying this to you, but... "
                msb " Would you let me try to make you feel better? "
                msb " I uh...we could hang out at your place. "
                msb " And we could also do whatever you'd want to do, "
                msb " As long as you feel better about everything. "
                msb " (God, I feel stupid for asking this...) "
                msb " (I haven't even known this [person] for a week and I'm already feeling like this.) "
                msb " (This is really insane...) "
                msb " (I should probably do some research on what I'm feeling.) "
                " Do you want to hang out with Miss Bloomie later? "
                menu:
                    " lets hang out vro ":
                        $ bloomielv += 10
                        $ bloomieinvite = True
                        hide missbloomieneutral at bottom
                        show missbloomiehappy at center
                        msb " Oh, um...? "
                        msb " I wasn't actually expecting for you to agree to my idea. "
                        msb " But, I'm glad I can help you in these times. "
                        msb " I'm going to have to think about what we're going to do though... "
                        msb " Can't just play games the entire time. "
                        msb " We've gotta do something productive together as well. "
                        msb " ...As long as you're fine with that, of course. "
                        msb " We could relax all you want if you don't want to work. "
                        msb " I don't want to stress you out... "
                        hide missbloomiehappy at bottom
                        show missbloomieneutral at center
                        msb " But, we're going to have to - as the kids say... "
                        msb " 'Lock in' for now. "
                        msb " You're going to have to go around and make sure the kids are doing all the right potions. "
                        msb " Meanwhile, I'm going to be observing them from here. "
                        msb " I want to see how well they're actually going to do in a group. "
                        msb " Usually they'd pick who they're close with. "
                        msb " So, I decided to make them work randomly. "
                        msb " They seem like they're doing well... "
                        msb " But, who knows? they might need some guidance. "
                        msb " I can trust that you'll help them, [name]. "
                        " You really just had no choice in this. "
                        " You nodded and agreed to help Miss Bloomie with the students. "
                        msb " Wonderful. "
                        msb " If you have any questions, just come up to me. "
                        msb " And also if something serious is going on. "
                        msb " I appreciate your help, [name]. "
                        scene black with dissolve
                        " You spent the rest of the class hours looking at students and making sure they're doing the right things. "
                        " Some groups were definitely struggling, but there were some who were doing well. "
                        " You helped the groups who were struggling and also gave the other ones tips on what they should do. "
                        " All of those tips came from Miss Bloomie though, "
                        " Science and potions weren't that much of your thing. "
                        " But you knew a thing or two about them. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to walk out of the classroom before you went out too. "
                        pause 2.0
                        jump tthursbreak2
                    " I'm busy tonight, sorry ":
                        msb " Alright, alright... "
                        msb " I just don't want to see you stressed out like that again. "
                        msb " Make sure to rest up, okay? "
                        msb " Ahem... "
                        msb " Now, we're going to have to - as the kids say... "
                        msb " 'Lock in' for now. "
                        msb " You're going to have to go around and make sure the kids are doing all the right potions. "
                        msb " Meanwhile, I'm going to be observing them from here. "
                        msb " I want to see how well they're actually going to do in a group. "
                        msb " Usually they'd pick who they're close with. "
                        msb " So, I decided to make them work randomly. "
                        msb " They seem like they're doing well... "
                        msb " But, who knows? they might need some guidance. "
                        msb " I can trust that you'll help them, [name]. "
                        " You really just had no choice in this. "
                        " You nodded and agreed to help Miss Bloomie with the students. "
                        msb " Wonderful. "
                        msb " If you have any questions, just come up to me. "
                        msb " And also if something serious is going on. "
                        msb " I appreciate your help, [name]. "
                        scene black with dissolve
                        " You spent the rest of the class hours looking at students and making sure they're doing the right things. "
                        " Some groups were definitely struggling, but there were some who were doing well. "
                        " You helped the groups who were struggling and also gave the other ones tips on what they should do. "
                        " All of those tips came from Miss Bloomie though, "
                        " Science and potions weren't that much of your thing. "
                        " But you knew a thing or two about them. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to walk out of the classroom before you went out too. "
                        pause 2.0
                        jump tthursbreak2
            else:
                msb " I saw how stressed you were yesterday. "
                msb " I don't really know you that well enough to know how to make you feel better, but... "
                msb " Get some rest, okay? "
                msb " Don't want you to worry about something like that again. "
                msb " Hope you feel better soon. "
                msb " Ahem... "
                msb " Now, we're going to have to - as the kids say... "
                msb " 'Lock in' for now. "
                msb " You're going to have to go around and make sure the kids are doing all the right potions. "
                msb " Meanwhile, I'm going to be observing them from here. "
                msb " I want to see how well they're actually going to do in a group. "
                msb " Usually they'd pick who they're close with. "
                msb " So, I decided to make them work randomly. "
                msb " They seem like they're doing well... "
                msb " But, who knows? they might need some guidance. "
                msb " I can trust that you'll help them, [name]. "
                " You really just had no choice in this. "
                " You nodded and agreed to help Miss Bloomie with the students. "
                msb " Wonderful. "
                msb " If you have any questions, just come up to me. "
                msb " And also if something serious is going on. "
                msb " I appreciate your help, [name]. "
                scene black with dissolve
                " You spent the rest of the class hours looking at students and making sure they're doing the right things. "
                " Some groups were definitely struggling, but there were some who were doing well. "
                " You helped the groups who were struggling and also gave the other ones tips on what they should do. "
                " All of those tips came from Miss Bloomie though, "
                " Science and potions weren't that much of your thing. "
                " But you knew a thing or two about them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You waited for everyone else to walk out of the classroom before you went out too. "
                pause 2.0
                jump tthursbreak2
        else:
            x " Hmm... "
            x " My students are doing particulary well today. "
            x " That's good... "
            x " Perhaps they've been finally paying attention. "
            x " That's really good, if that's the case. "
            " You greeted her and asked what she was doing. "
            x " Hm? oh. [name], hello there. "
            x " Before I answer your question, I don't think I've introduced myself to you before. "
            x " Let's get straight to the introduction... "
            $ bloomieknow = True
            msb " I'm Miss Bloomie. The science teacher. Lovely to meet you. "
            msb " Anyway, about your question... "
            msb " I'm just observing my students on doing their activity. "
            msb " Making sure they don't do anything wrong... "
            msb " I wouldn't want my entire classroom to get blown up, after all. "
            msb " That...situation has happened before in the past, actually. "
            msb " That's why I'm looking after my students more. "
            msb " So that they won't do anything idiotic to cancel school. "
            msb " They're always finding ways to cancel school... "
            msb " And I don't want Miss Grace to get mad at me for letting them have no school. "
            msb " I remember how she reacted when she found my classroom being blown up... "
            msb " Hoouughh...not good times, I'll tell you that. "
            msb " Oh, and uh...before I forget. "
            msb " I had something to tell you. "
            if bloomielv >= 15 or bloomielv == 15:
                msb " I saw how upset you were yesterday. "
                msb " And, I have to admit... "
                msb " Seeing you sad kind of shattered my heart just a bit. "
                msb " I expected myself not to really care, but... "
                msb " I uh...felt really sad the moment I saw you stressing out. "
                msb " I honestly thought that I was being a little dramatic, yes... "
                msb " But the more I saw you being upset about the situation, the more bad I felt. "
                msb " I couldn't just stand there and do nothing about it. "
                msb " So, I requested Miss Grace to let you rest for the rest of the day. "
                msb " That's the reason why you weren't a part of the lookout thing we did yesterday. "
                msb " I thought that while you were gone, my thoughts of you would dissolve, too... "
                msb " But the thoughts kept coming back over and over again. "
                msb " I can't believe I'm saying this to you, but... "
                msb " Would you let me try to make you feel better? "
                msb " I uh...we could hang out at your place. "
                msb " And we could also do whatever you'd want to do, "
                msb " As long as you feel better about everything. "
                msb " (God, I feel stupid for asking this...) "
                msb " (I haven't even known this [person] for a week and I'm already feeling like this.) "
                msb " (This is really insane...) "
                msb " (I should probably do some research on what I'm feeling.) "
                " Do you want to hang out with Miss Bloomie later? "
                menu:
                    " lets hang out vro ":
                        $ bloomielv += 10
                        $ bloomieinvite = True
                        hide missbloomieneutral at bottom
                        show missbloomiehappy at center
                        msb " Oh, um...? "
                        msb " I wasn't actually expecting for you to agree to my idea. "
                        msb " But, I'm glad I can help you in these times. "
                        msb " I'm going to have to think about what we're going to do though... "
                        msb " Can't just play games the entire time. "
                        msb " We've gotta do something productive together as well. "
                        msb " ...As long as you're fine with that, of course. "
                        msb " We could relax all you want if you don't want to work. "
                        msb " I don't want to stress you out... "
                        hide missbloomiehappy at bottom
                        show missbloomieneutral at center
                        msb " But, we're going to have to - as the kids say... "
                        msb " 'Lock in' for now. "
                        msb " You're going to have to go around and make sure the kids are doing all the right potions. "
                        msb " Meanwhile, I'm going to be observing them from here. "
                        msb " I want to see how well they're actually going to do in a group. "
                        msb " Usually they'd pick who they're close with. "
                        msb " So, I decided to make them work randomly. "
                        msb " They seem like they're doing well... "
                        msb " But, who knows? they might need some guidance. "
                        msb " I can trust that you'll help them, [name]. "
                        " You really just had no choice in this. "
                        " You nodded and agreed to help Miss Bloomie with the students. "
                        msb " Wonderful. "
                        msb " If you have any questions, just come up to me. "
                        msb " And also if something serious is going on. "
                        msb " I appreciate your help, [name]. "
                        scene black with dissolve
                        " You spent the rest of the class hours looking at students and making sure they're doing the right things. "
                        " Some groups were definitely struggling, but there were some who were doing well. "
                        " You helped the groups who were struggling and also gave the other ones tips on what they should do. "
                        " All of those tips came from Miss Bloomie though, "
                        " Science and potions weren't that much of your thing. "
                        " But you knew a thing or two about them. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to walk out of the classroom before you went out too. "
                        pause 2.0
                        jump tthursbreak2
                    " I'm busy tonight, sorry ":
                        msb " Alright, alright... "
                        msb " I just don't want to see you stressed out like that again. "
                        msb " Make sure to rest up, okay? "
                        msb " Ahem... "
                        msb " Now, we're going to have to - as the kids say... "
                        msb " 'Lock in' for now. "
                        msb " You're going to have to go around and make sure the kids are doing all the right potions. "
                        msb " Meanwhile, I'm going to be observing them from here. "
                        msb " I want to see how well they're actually going to do in a group. "
                        msb " Usually they'd pick who they're close with. "
                        msb " So, I decided to make them work randomly. "
                        msb " They seem like they're doing well... "
                        msb " But, who knows? they might need some guidance. "
                        msb " I can trust that you'll help them, [name]. "
                        " You really just had no choice in this. "
                        " You nodded and agreed to help Miss Bloomie with the students. "
                        msb " Wonderful. "
                        msb " If you have any questions, just come up to me. "
                        msb " And also if something serious is going on. "
                        msb " I appreciate your help, [name]. "
                        scene black with dissolve
                        " You spent the rest of the class hours looking at students and making sure they're doing the right things. "
                        " Some groups were definitely struggling, but there were some who were doing well. "
                        " You helped the groups who were struggling and also gave the other ones tips on what they should do. "
                        " All of those tips came from Miss Bloomie though, "
                        " Science and potions weren't that much of your thing. "
                        " But you knew a thing or two about them. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to walk out of the classroom before you went out too. "
                        pause 2.0
                        jump tthursbreak2
            else:
                msb " I saw how stressed you were yesterday. "
                msb " I don't really know you that well enough to know how to make you feel better, but... "
                msb " Get some rest, okay? "
                msb " Don't want you to worry about something like that again. "
                msb " Hope you feel better soon. "
                msb " Ahem... "
                msb " Now, we're going to have to - as the kids say... "
                msb " 'Lock in' for now. "
                msb " You're going to have to go around and make sure the kids are doing all the right potions. "
                msb " Meanwhile, I'm going to be observing them from here. "
                msb " I want to see how well they're actually going to do in a group. "
                msb " Usually they'd pick who they're close with. "
                msb " So, I decided to make them work randomly. "
                msb " They seem like they're doing well... "
                msb " But, who knows? they might need some guidance. "
                msb " I can trust that you'll help them, [name]. "
                " You really just had no choice in this. "
                " You nodded and agreed to help Miss Bloomie with the students. "
                msb " Wonderful. "
                msb " If you have any questions, just come up to me. "
                msb " And also if something serious is going on. "
                msb " I appreciate your help, [name]. "
                scene black with dissolve
                " You spent the rest of the class hours looking at students and making sure they're doing the right things. "
                " Some groups were definitely struggling, but there were some who were doing well. "
                " You helped the groups who were struggling and also gave the other ones tips on what they should do. "
                " All of those tips came from Miss Bloomie though, "
                " Science and potions weren't that much of your thing. "
                " But you knew a thing or two about them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You waited for everyone else to walk out of the classroom before you went out too. "
                pause 2.0
                jump tthursbreak2
    label mstthurshelp:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom and looked around for the language teacher... "
        " Looks like they're all busy answering something right now. "
        " The students, I mean. "
        " Everyone's answering something and it's all quiet... "
        " Looking around, you saw the language teacher sitting infront of the class. "
        " It would probably be bad to distract her, but you DID come here to talk.. "
        " And also help her for a bit. But how could you help? "
        " Probably watch over the students. Probably. "
        " You walked over to her to see if she was doing alright. "
        show msthravelneutral at center with easeinleft
        if thavelknow == True:
            mst " ... "
            " At first, she's completely silent. "
            " Looks like she was focusing on getting her students to actually do work. "
            " You've noticed that the students seem to concentrate a bit more whenever she's around... "
            " Maybe she was a little strict on them? "
            " Yeah, probably why they're a whole lot more locked in whenever she was around. "
            " She DOES look like she could be a terrifying teacher... "
            " You pulled over a chair and sat down next to her, waiting for her to notice you. "
            " And eventually, she does! Huzzah!! "
            mst " [name]!! sorry that I didn't notice you, haha... "
            mst " I guess I was too focused on making sure my students were doing well? "
            mst " I don't want them to cheat, after all. "
            mst " A student from my class shouldn't cheat at all! "
            mst " They should know better than that, in all honesty. "
            mst " If I ever catch a student cheating in my class... "
            mst " I don't think their grades would survive. "
            mst " As a fact - I actually told them that if I caught them cheating... "
            mst " I'm going to minus about 10 points from them in the quiz. "
            mst " That's also gonna be for everytime I catch them cheating. "
            mst " You're gonna cheat? okay, let's have your score as a one, then! "
            mst " I'm sure you're going to be proud of you grades after that, hmm? "
            mst " Oh yeah, they'll be veeery proud of that one, for sure. "
            mst " They're totally going to survive college with that one hell of a grade! "
            mst " Totally, haha. "
            mst " That's why - while I'm here, I'm trying my best to not get them to be dumbasses. "
            mst " They need to figure out how to do school stuff properly, you know? "
            mst " Can't just have them slacking off... "
            mst " Oh, right! I had to tell you something... "
            mst " Almost completely forgot about what I was gonna say there, haha. "
            if thavellv >= 15 or thavellv == 15:
                hide msthravelneutral at bottom
                show msthravelsad at center
                mst " You know...I got a little bit worried for you yesterday. "
                mst " You looked so upset and stressed about what happened. "
                mst " And I can understand - I was feeling stressed too. "
                mst " (For a completely different reason, if you get what I mean.) "
                mst " Seeing you stressed made me feel...oddly worried for you. "
                mst " I just wanted to make you feel better, but I didn't know how. "
                mst " Besides, I was so busy with dealing with all of the things Miss Grace was letting me do... "
                mst " I couldn't really talk to you because of how busy I was. "
                mst " And I felt bad whenever I saw you walk down the hallways with such a concerned look... "
                mst " In short, I wanted to make you feel better but I didn't have time to. "
                mst " That's why I'm planning on doing it right now. "
                mst " Do you perhaps want to hang out later tonight at you place? "
                mst " It's okay if you don't want to, of course. "
                mst " I just want to make you feel better. "
                mst " We coud hang out, play games...do boring important stuff. "
                mst " Anything you want, just to make you feel better. "
                menu:
                    " Let's hang out ":
                        $ thavellv += 10
                        hide msthravelsad at bottom
                        show msthravelhappy at center
                        mst " Really? that's great then!! "
                        mst " I could steal some of Circle's snacks again. "
                        mst " Just, uh... remind me not to take her oreos. "
                        mst " She's really big on not letting anyone touching her oreos. "
                        mst " I saw Miss Emily try to steal her oreos once... "
                        mst " Let's just say that she didn't react too well to that. "
                        mst " And at that time, Circle was on the other side of the school... "
                        mst " Her speed surprises the others, me included. "
                        mst " I can run fast, but not THAT fast. "
                        mst " Impressive, yet scary at the same time. "
                        mst " Imagine a very angry Circle running at you full speed... "
                        mst " Wouldn't be the best experience, really. "
                        hide msthravelhappy at bottom
                        show msthravelneutral at center
                        mst " Oh, we should probably start looking out for the students, though. "
                        mst " They might've been cheating while we were talking. "
                        mst " How about we both stare at the students menacingly? "
                        mst " Trust me, I always get them to behave when I stare. "
                        mst " I don't know if it's because I look intimidating, buuut... "
                        mst " Atleast they're behaving! "
                        " You actually had no choice in this. "
                        " You agreed and nodded that you were going to help Miss Thavel in this. "
                        " How fun, a staring contest with the students! "
                        mst " Wonderful! "
                        mst " Just remember to call them out if they're cheating. "
                        mst " That gets them to go back in line! "
                        scene black with dissolve
                        " You spent the rest of class hours looking at students to make sure they didn't cheat. "
                        " You were kind of playing ping pong in your mind while doing this... "
                        " And you were pretty sure Miss Thavel was playing a game of her own too, in her mind. "
                        " Probably playing that one thing where you drink a beer and drive then hit something. "
                        " It also has a song for it. It goes... "
                        " Driving in my caaaar right after a beeer, hey that bummpppp is shaped like a deer... "
                        " I forgot the other lyrics, but it goes like that. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to get out before you did. "
                        pause 2.0
                        jump tthursbreak2
                    " I'm busy tonight, sorry ":
                        hide msthravelsad at bottom
                        show msthravelneutral at center
                        mst " Oh, okay! "
                        mst " Just, uh... "
                        mst " Remmeber to get some rest every now and then, okay? "
                        mst " Seeing you being stressed out really displeases me. "
                        mst " Remember: don't overwork yourself and don't force yourself to work! "
                        mst " And also not to worry about little things here and there. "
                        mst " Oh, we should probably start looking out for the students, though. "
                        mst " They might've been cheating while we were talking. "
                        mst " How about we both stare at the students menacingly? "
                        mst " Trust me, I always get them to behave when I stare. "
                        mst " I don't know if it's because I look intimidating, buuut... "
                        mst " Atleast they're behaving! "
                        " You actually had no choice in this. "
                        " You agreed and nodded that you were going to help Miss Thavel in this. "
                        " How fun, a staring contest with the students! "
                        mst " Wonderful! "
                        mst " Just remember to call them out if they're cheating. "
                        mst " That gets them to go back in line! "
                        scene black with dissolve
                        " You spent the rest of class hours looking at students to make sure they didn't cheat. "
                        " You were kind of playing ping pong in your mind while doing this... "
                        " And you were pretty sure Miss Thavel was playing a game of her own too, in her mind. "
                        " Probably playing that one thing where you drink a beer and drive then hit something. "
                        " It also has a song for it. It goes... "
                        " Driving in my caaaar right after a beeer, hey that bummpppp is shaped like a deer... "
                        " I forgot the other lyrics, but it goes like that. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to get out before you did. "
                        pause 2.0
                        jump tthursbreak2
            else:
                mst " I saw how upset you were yesterday, and.. "
                mst " I just wanted to say that I hope you feel better soon. "
                mst " Dealing with death is tough, I get that. "
                mst " But it's something that we should accept, because that's just life. "
                mst " We can't really do something if that person is already gone, unfortunately. "
                mst " I really do hope that you feel better soon, [name]. "
                mst " ...We should probably start looking out for the students, though. "
                mst " They might've been cheating while we were talking. "
                mst " How about we both stare at the students menacingly? "
                mst " Trust me, I always get them to behave when I stare. "
                mst " I don't know if it's because I look intimidating, buuut... "
                mst " Atleast they're behaving! "
                " You actually had no choice in this. "
                " You agreed and nodded that you were going to help Miss Thavel in this. "
                " How fun, a staring contest with the students! "
                mst " Wonderful! "
                mst " Just remember to call them out if they're cheating. "
                mst " That gets them to go back in line! "
                scene black with dissolve
                " You spent the rest of class hours looking at students to make sure they didn't cheat. "
                " You were kind of playing ping pong in your mind while doing this... "
                " And you were pretty sure Miss Thavel was playing a game of her own too, in her mind. "
                " Probably playing that one thing where you drink a beer and drive then hit something. "
                " It also has a song for it. It goes... "
                " Driving in my caaaar right after a beeer, hey that bummpppp is shaped like a deer... "
                " I forgot the other lyrics, but it goes like that. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You waited for everyone else to get out before you did. "
                pause 2.0
                jump tthursbreak2
        else:
            x " ... "
            " At first, she's completely silent. "
            " Looks like she was focusing on getting her students to actually do work. "
            " You've noticed that the students seem to concentrate a bit more whenever she's around... "
            " Maybe she was a little strict on them? "
            " Yeah, probably why they're a whole lot more locked in whenever she was around. "
            " She DOES look like she could be a terrifying teacher... "
            " You pulled over a chair and sat down next to her, waiting for her to notice you. "
            " And eventually, she does! Huzzah!! "
            x " [name]!! sorry that I didn't notice you, haha... "
            x " Hold on, I don't think I've introduced myself to you before! "
            x " Geez, really sorry about that... "
            $ thavelknow = True
            mst " I'm Miss Thavel! The language teacher! "
            mst " I'm sorry for not noticing you again... "
            mst " I guess I was too focused on making sure my students were doing well? "
            mst " I don't want them to cheat, after all. "
            mst " A student from my class shouldn't cheat at all! "
            mst " They should know better than that, in all honesty. "
            mst " If I ever catch a student cheating in my class... "
            mst " I don't think their grades would survive. "
            mst " As a fact - I actually told them that if I caught them cheating... "
            mst " I'm going to minus about 10 points from them in the quiz. "
            mst " That's also gonna be for everytime I catch them cheating. "
            mst " You're gonna cheat? okay, let's have your score as a one, then! "
            mst " I'm sure you're going to be proud of you grades after that, hmm? "
            mst " Oh yeah, they'll be veeery proud of that one, for sure. "
            mst " They're totally going to survive college with that one hell of a grade! "
            mst " Totally, haha. "
            mst " That's why - while I'm here, I'm trying my best to not get them to be dumbasses. "
            mst " They need to figure out how to do school stuff properly, you know? "
            mst " Can't just have them slacking off... "
            mst " Oh, right! I had to tell you something... "
            mst " Almost completely forgot about what I was gonna say there, haha. "
            if thavellv >= 15 or thavellv == 15:
                hide msthravelneutral at bottom
                show msthravelsad at center
                mst " You know...I got a little bit worried for you yesterday. "
                mst " You looked so upset and stressed about what happened. "
                mst " And I can understand - I was feeling stressed too. "
                mst " (For a completely different reason, if you get what I mean.) "
                mst " Seeing you stressed made me feel...oddly worried for you. "
                mst " I just wanted to make you feel better, but I didn't know how. "
                mst " Besides, I was so busy with dealing with all of the things Miss Grace was letting me do... "
                mst " I couldn't really talk to you because of how busy I was. "
                mst " And I felt bad whenever I saw you walk down the hallways with such a concerned look... "
                mst " In short, I wanted to make you feel better but I didn't have time to. "
                mst " That's why I'm planning on doing it right now. "
                mst " Do you perhaps want to hang out later tonight at you place? "
                mst " It's okay if you don't want to, of course. "
                mst " I just want to make you feel better. "
                mst " We coud hang out, play games...do boring important stuff. "
                mst " Anything you want, just to make you feel better. "
                menu:
                    " Let's hang out ":
                        $ thavellv += 10
                        hide msthravelsad at bottom
                        show msthravelhappy at center
                        mst " Really? that's great then!! "
                        mst " I could steal some of Circle's snacks again. "
                        mst " Just, uh... remind me not to take her oreos. "
                        mst " She's really big on not letting anyone touching her oreos. "
                        mst " I saw Miss Emily try to steal her oreos once... "
                        mst " Let's just say that she didn't react too well to that. "
                        mst " And at that time, Circle was on the other side of the school... "
                        mst " Her speed surprises the others, me included. "
                        mst " I can run fast, but not THAT fast. "
                        mst " Impressive, yet scary at the same time. "
                        mst " Imagine a very angry Circle running at you full speed... "
                        mst " Wouldn't be the best experience, really. "
                        hide msthravelhappy at bottom
                        show msthravelneutral at center
                        mst " Oh, we should probably start looking out for the students, though. "
                        mst " They might've been cheating while we were talking. "
                        mst " How about we both stare at the students menacingly? "
                        mst " Trust me, I always get them to behave when I stare. "
                        mst " I don't know if it's because I look intimidating, buuut... "
                        mst " Atleast they're behaving! "
                        " You actually had no choice in this. "
                        " You agreed and nodded that you were going to help Miss Thavel in this. "
                        " How fun, a staring contest with the students! "
                        mst " Wonderful! "
                        mst " Just remember to call them out if they're cheating. "
                        mst " That gets them to go back in line! "
                        scene black with dissolve
                        " You spent the rest of class hours looking at students to make sure they didn't cheat. "
                        " You were kind of playing ping pong in your mind while doing this... "
                        " And you were pretty sure Miss Thavel was playing a game of her own too, in her mind. "
                        " Probably playing that one thing where you drink a beer and drive then hit something. "
                        " It also has a song for it. It goes... "
                        " Driving in my caaaar right after a beeer, hey that bummpppp is shaped like a deer... "
                        " I forgot the other lyrics, but it goes like that. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to get out before you did. "
                        pause 2.0
                        jump tthursbreak2
                    " I'm busy tonight, sorry ":
                        hide msthravelsad at bottom
                        show msthravelneutral at center
                        mst " Oh, okay! "
                        mst " Just, uh... "
                        mst " Remmeber to get some rest every now and then, okay? "
                        mst " Seeing you being stressed out really displeases me. "
                        mst " Remember: don't overwork yourself and don't force yourself to work! "
                        mst " And also not to worry about little things here and there. "
                        mst " Oh, we should probably start looking out for the students, though. "
                        mst " They might've been cheating while we were talking. "
                        mst " How about we both stare at the students menacingly? "
                        mst " Trust me, I always get them to behave when I stare. "
                        mst " I don't know if it's because I look intimidating, buuut... "
                        mst " Atleast they're behaving! "
                        " You actually had no choice in this. "
                        " You agreed and nodded that you were going to help Miss Thavel in this. "
                        " How fun, a staring contest with the students! "
                        mst " Wonderful! "
                        mst " Just remember to call them out if they're cheating. "
                        mst " That gets them to go back in line! "
                        scene black with dissolve
                        " You spent the rest of class hours looking at students to make sure they didn't cheat. "
                        " You were kind of playing ping pong in your mind while doing this... "
                        " And you were pretty sure Miss Thavel was playing a game of her own too, in her mind. "
                        " Probably playing that one thing where you drink a beer and drive then hit something. "
                        " It also has a song for it. It goes... "
                        " Driving in my caaaar right after a beeer, hey that bummpppp is shaped like a deer... "
                        " I forgot the other lyrics, but it goes like that. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to get out before you did. "
                        pause 2.0
                        jump tthursbreak2
            else:
                mst " I saw how upset you were yesterday, and.. "
                mst " I just wanted to say that I hope you feel better soon. "
                mst " Dealing with death is tough, I get that. "
                mst " But it's something that we should accept, because that's just life. "
                mst " We can't really do something if that person is already gone, unfortunately. "
                mst " I really do hope that you feel better soon, [name]. "
                mst " ...We should probably start looking out for the students, though. "
                mst " They might've been cheating while we were talking. "
                mst " How about we both stare at the students menacingly? "
                mst " Trust me, I always get them to behave when I stare. "
                mst " I don't know if it's because I look intimidating, buuut... "
                mst " Atleast they're behaving! "
                " You actually had no choice in this. "
                " You agreed and nodded that you were going to help Miss Thavel in this. "
                " How fun, a staring contest with the students! "
                mst " Wonderful! "
                mst " Just remember to call them out if they're cheating. "
                mst " That gets them to go back in line! "
                scene black with dissolve
                " You spent the rest of class hours looking at students to make sure they didn't cheat. "
                " You were kind of playing ping pong in your mind while doing this... "
                " And you were pretty sure Miss Thavel was playing a game of her own too, in her mind. "
                " Probably playing that one thing where you drink a beer and drive then hit something. "
                " It also has a song for it. It goes... "
                " Driving in my caaaar right after a beeer, hey that bummpppp is shaped like a deer... "
                " I forgot the other lyrics, but it goes like that. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You waited for everyone else to get out before you did. "
                pause 2.0
                jump tthursbreak2
    label mssthurshelp:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the art classroom and looked around.. "
        " Looks like all of the students were doing some paintings. "
        " Some random paintings depicting their feelings... "
        " Most people were painting themselves being happy, "
        " But you saw some who were expressing other emotions. "
        " Either the people wanted to impress the art teacher by making them do a happy painting... "
        " ...Or they just genuinely feel happy. "
        " You looked around and found the art teacher looking at a few drawings in the back. "
        " You wanted to have a talk with her and decided to walk up to her. "
        show sashaneutral at center with easeinleft
        if sashaknow == True:
            mss " Awww, this one's so sweet! "
            mss " A drawing of them and their family... "
            mss " It's even got that classic happy sun in the corner! "
            mss " Aaaah...this one is getting a 35/50. "
            mss " Not only does it look good, it also gives me nostalgia! "
            mss " ...Nostalgia because of how I used to draw, haha. "
            " You greeted her and asked what she was doing. "
            mss " Oh, hey there [name]! "
            mss " I'm just checking out the kindergarten student's works. "
            mss " If you didn't know - I'm also the teacher for the younger students here! "
            hide sashaneutral at bottom
            show sashahappy at center
            mss " And right now...aww, look at this precious drawing! "
            " She shows you a drawing of a cute puppy. "
            mss " Isn't this adorable?! "
            mss " I should give this one a 50/50, right? "
            mss " The colors on it also work really well! "
            mss " I'm pretty impressed by this, in all honesty! "
            mss " Let me just add a little comment there... "
            hide sashahappy at bottom
            show sashaneutral at center
            mss " There we go! "
            mss " Looks like those were all of the drawings I had to check! "
            mss " Now we could really hang out... "
            hide sashaneutral at bottom
            show sashaconfused at center
            mss " ...Hm. "
            mss " I remember that I had to tell you something... "
            mss " But I kind of forgot...hehehh... "
            mss " Sorry, sorry...let me figure it out. "
            mss " I don't want to keep you waiting for too long! "
            " You patiently waited for Sasha to finish thinking. "
            " While you were waiting, you spent the time playing ping pong in your head. "
            " She eventually spoke up again after a good bit. "
            mss " Oooh, yeah...right... "
            if sashalv >= 15 or sashalv == 15:
                hide sashaconfused at bottom
                show sashasad at center
                mss " I saw how sad you were yesterday... "
                mss " And honestly...? "
                mss " Seeing you sad motivated me to find that student even more, but then... "
                mss " ...The news broke out that they were already gone... "
                mss " I felt so guilty that I couldn't do anything to help them... "
                mss " The rest of the day, I kept thinking about how upset you'd be if I told you... "
                mss " I didn't want to see you upset, really!! "
                mss " But, I knew I'd have to tell you in the end... "
                mss " As they say...saying the truth is better than saying a lie... "
                mss " Since I couldn't make you feel better... "
                mss " I wanted to find another way to make you feel happier... "
                mss " And, uh...this is really embarrassing to ask... "
                mss " You know??? considering we've only known eachother for less then a week?? "
                mss " Feels really awkward doesn't it??? "
                mss " Uh, ahem... "
                mss " Would you let me hang over at your house? "
                mss " I'm not planning to stay the night, I promise!! "
                mss " I'm just there to give you emotional support or whatever!!!! "
                mss " We could play games, make art...do whatever you'd like!! "
                mss " ...I just want to see you smile... "
                menu:
                    " Let's hang out ":
                        $ sashalv += 10
                        hide sashasad at bottom
                        show sashahappy at center
                        mss " Wait, really?! "
                        mss " Eeek, this is gonna be really fun!! "
                        mss " I haven't really visited anyone's house before... "
                        mss " Excluding the time me and the other teachers did a whole sleepover. "
                        mss " God, that night was so much fun!! "
                        mss " I'm sure we're gonna have a lot of fun too, [name]! "
                        mss " Besides...everything's better with you. "
                        mss " You make my days brighter, in all honesty... "
                        mss " I hope I can light up your night later! "
                        hide sashahappy at bottom
                        show sashaneutral at center
                        mss " Oooh, wait! I almost forgot about my job! "
                        mss " Let's go around and check on what everyone painted, okay? "
                        mss " I'm sure everyone painted such wonderful paintings! "
                        mss " Everyone in this class is so expressive with their work... "
                        mss " I love it! "
                        " Well, you can't exactly say no to those eyes... "
                        " And you don't even have a choice in this. "
                        " So, you agreed to check peoples paintings with Sasha. "
                        mss " Yahoo! "
                        mss " Okay, let's get started ooon... "
                        mss " Petunia and Lizzy!! "
                        scene black with dissolve
                        " You spent the rest of the class hours looking at peoples paintings. "
                        " A lot of peoples paintings were pretty good, some were... "
                        " Let's say they were alright. You didn't want to be mean. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to get out of the classroom before you did. "
                        pause 2.0
                        jump tthursbreak2
                    " I'm busy tonight, sorry ":
                        hide sashasad at bottom
                        show sashaneutral at center
                        mss " Ooooh...okay! "
                        mss " I hope you feel better tonight though... "
                        mss " I know it sucks, but I'm sure things will get better, alright? "
                        mss " I don't wanna see you frowning whenever I'm around! "
                        mss " Oooh, wait! I almost forgot about my job! "
                        mss " Let's go around and check on what everyone painted, okay? "
                        mss " I'm sure everyone painted such wonderful paintings! "
                        mss " Everyone in this class is so expressive with their work... "
                        mss " I love it! "
                        " Well, you can't exactly say no to those eyes... "
                        " And you don't even have a choice in this. "
                        " So, you agreed to check peoples paintings with Sasha. "
                        mss " Yahoo! "
                        mss " Okay, let's get started ooon... "
                        mss " Petunia and Lizzy!! "
                        scene black with dissolve
                        " You spent the rest of the class hours looking at peoples paintings. "
                        " A lot of peoples paintings were pretty good, some were... "
                        " Let's say they were alright. You didn't want to be mean. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to get out of the classroom before you did. "
                        pause 2.0
                        jump tthursbreak2
            else:
                hide sashaconfused at bottom
                show sashasad at center
                mss " I saw how upset you were yesterday, and... "
                mss " I just wanna say that I hope things get better. "
                mss " I can't really do anything to, uh... "
                mss " Make wishes come true or anything, like making that kid...alive and well... "
                mss " But, what I can offer you is a hug! "
                " You opened your arms for a hug. "
                hide sashasad at bottom
                show sashaneutral at center
                mss " Yay! "
                " She seemed really happy that you wanted a hug from her. "
                " She hugs you for a good bit before she let go. "
                mss " I hope you feel better tonight though... "
                mss " I know it sucks, but I'm sure things will get better, alright? "
                mss " I don't wanna see you frowning whenever I'm around! "
                mss " Oooh, wait! I almost forgot about my job! "
                mss " Let's go around and check on what everyone painted, okay? "
                mss " I'm sure everyone painted such wonderful paintings! "
                mss " Everyone in this class is so expressive with their work... "
                mss " I love it! "
                " Well, you can't exactly say no to those eyes... "
                " And you don't even have a choice in this. "
                " So, you agreed to check peoples paintings with Sasha. "
                mss " Yahoo! "
                mss " Okay, let's get started ooon... "
                mss " Petunia and Lizzy!! "
                scene black with dissolve
                " You spent the rest of the class hours looking at peoples paintings. "
                " A lot of peoples paintings were pretty good, some were... "
                " Let's say they were alright. You didn't want to be mean. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You waited for everyone else to get out of the classroom before you did. "
                pause 2.0
                jump tthursbreak2
        else:
            x " Awww, this one's so sweet! "
            x " A drawing of them and their family... "
            x " It's even got that classic happy sun in the corner! "
            x " Aaaah...this one is getting a 35/50. "
            x " Not only does it look good, it also gives me nostalgia! "
            x " ...Nostalgia because of how I used to draw, haha. "
            " You greeted her and asked what she was doing. "
            x " Oh, hey there [name]! "
            x " Waaait, have I introduced myself to you before...? "
            x " I don't think so... "
            x " Welp, time to do that now then! "
            $ sashaknow = True
            mss " I'm Miss Sasha! The art teacher! and about your question... "
            mss " I'm just checking out the kindergarten student's works. "
            mss " If you didn't know - I'm also the teacher for the younger students here! "
            hide sashaneutral at bottom
            show sashahappy at center
            mss " And right now...aww, look at this precious drawing! "
            " She shows you a drawing of a cute puppy. "
            mss " Isn't this adorable?! "
            mss " I should give this one a 50/50, right? "
            mss " The colors on it also work really well! "
            mss " I'm pretty impressed by this, in all honesty! "
            mss " Let me just add a little comment there... "
            hide sashahappy at bottom
            show sashaneutral at center
            mss " There we go! "
            mss " Looks like those were all of the drawings I had to check! "
            mss " Now we could really hang out... "
            hide sashaneutral at bottom
            show sashaconfused at center
            mss " ...Hm. "
            mss " I remember that I had to tell you something... "
            mss " But I kind of forgot...hehehh... "
            mss " Sorry, sorry...let me figure it out. "
            mss " I don't want to keep you waiting for too long! "
            " You patiently waited for Sasha to finish thinking. "
            " While you were waiting, you spent the time playing ping pong in your head. "
            " She eventually spoke up again after a good bit. "
            mss " Oooh, yeah...right... "
            if sashalv >= 15 or sashalv == 15:
                hide sashaconfused at bottom
                show sashasad at center
                mss " I saw how sad you were yesterday... "
                mss " And honestly...? "
                mss " Seeing you sad motivated me to find that student even more, but then... "
                mss " ...The news broke out that they were already gone... "
                mss " I felt so guilty that I couldn't do anything to help them... "
                mss " The rest of the day, I kept thinking about how upset you'd be if I told you... "
                mss " I didn't want to see you upset, really!! "
                mss " But, I knew I'd have to tell you in the end... "
                mss " As they say...saying the truth is better than saying a lie... "
                mss " Since I couldn't make you feel better... "
                mss " I wanted to find another way to make you feel happier... "
                mss " And, uh...this is really embarrassing to ask... "
                mss " You know??? considering we've only known eachother for less then a week?? "
                mss " Feels really awkward doesn't it??? "
                mss " Uh, ahem... "
                mss " Would you let me hang over at your house? "
                mss " I'm not planning to stay the night, I promise!! "
                mss " I'm just there to give you emotional support or whatever!!!! "
                mss " We could play games, make art...do whatever you'd like!! "
                mss " ...I just want to see you smile... "
                menu:
                    " Let's hang out ":
                        $ sashalv += 10
                        hide sashasad at bottom
                        show sashahappy at center
                        mss " Wait, really?! "
                        mss " Eeek, this is gonna be really fun!! "
                        mss " I haven't really visited anyone's house before... "
                        mss " Excluding the time me and the other teachers did a whole sleepover. "
                        mss " God, that night was so much fun!! "
                        mss " I'm sure we're gonna have a lot of fun too, [name]! "
                        mss " Besides...everything's better with you. "
                        mss " You make my days brighter, in all honesty... "
                        mss " I hope I can light up your night later! "
                        hide sashahappy at bottom
                        show sashaneutral at center
                        mss " Oooh, wait! I almost forgot about my job! "
                        mss " Let's go around and check on what everyone painted, okay? "
                        mss " I'm sure everyone painted such wonderful paintings! "
                        mss " Everyone in this class is so expressive with their work... "
                        mss " I love it! "
                        " Well, you can't exactly say no to those eyes... "
                        " And you don't even have a choice in this. "
                        " So, you agreed to check peoples paintings with Sasha. "
                        mss " Yahoo! "
                        mss " Okay, let's get started ooon... "
                        mss " Petunia and Lizzy!! "
                        scene black with dissolve
                        " You spent the rest of the class hours looking at peoples paintings. "
                        " A lot of peoples paintings were pretty good, some were... "
                        " Let's say they were alright. You didn't want to be mean. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to get out of the classroom before you did. "
                        pause 2.0
                        jump tthursbreak2
                    " I'm busy tonight, sorry ":
                        hide sashasad at bottom
                        show sashaneutral at center
                        mss " Ooooh...okay! "
                        mss " I hope you feel better tonight though... "
                        mss " I know it sucks, but I'm sure things will get better, alright? "
                        mss " I don't wanna see you frowning whenever I'm around! "
                        mss " Oooh, wait! I almost forgot about my job! "
                        mss " Let's go around and check on what everyone painted, okay? "
                        mss " I'm sure everyone painted such wonderful paintings! "
                        mss " Everyone in this class is so expressive with their work... "
                        mss " I love it! "
                        " Well, you can't exactly say no to those eyes... "
                        " And you don't even have a choice in this. "
                        " So, you agreed to check peoples paintings with Sasha. "
                        mss " Yahoo! "
                        mss " Okay, let's get started ooon... "
                        mss " Petunia and Lizzy!! "
                        scene black with dissolve
                        " You spent the rest of the class hours looking at peoples paintings. "
                        " A lot of peoples paintings were pretty good, some were... "
                        " Let's say they were alright. You didn't want to be mean. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to get out of the classroom before you did. "
                        pause 2.0
                        jump tthursbreak2
            else:
                hide sashaconfused at bottom
                show sashasad at center
                mss " I saw how upset you were yesterday, and... "
                mss " I just wanna say that I hope things get better. "
                mss " I can't really do anything to, uh... "
                mss " Make wishes come true or anything, like making that kid...alive and well... "
                mss " But, what I can offer you is a hug! "
                " You opened your arms for a hug. "
                hide sashasad at bottom
                show sashaneutral at center
                mss " Yay! "
                " She seemed really happy that you wanted a hug from her. "
                " She hugs you for a good bit before she let go. "
                mss " I hope you feel better tonight though... "
                mss " I know it sucks, but I'm sure things will get better, alright? "
                mss " I don't wanna see you frowning whenever I'm around! "
                mss " Oooh, wait! I almost forgot about my job! "
                mss " Let's go around and check on what everyone painted, okay? "
                mss " I'm sure everyone painted such wonderful paintings! "
                mss " Everyone in this class is so expressive with their work... "
                mss " I love it! "
                " Well, you can't exactly say no to those eyes... "
                " And you don't even have a choice in this. "
                " So, you agreed to check peoples paintings with Sasha. "
                mss " Yahoo! "
                mss " Okay, let's get started ooon... "
                mss " Petunia and Lizzy!! "
                scene black with dissolve
                " You spent the rest of the class hours looking at peoples paintings. "
                " A lot of peoples paintings were pretty good, some were... "
                " Let's say they were alright. You didn't want to be mean. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You waited for everyone else to get out of the classroom before you did. "
                pause 2.0
                jump tthursbreak2
label tthursbreak2:
    scene hallway with dissolve
    " You walked into the hallways and spotted none of your teacher friends once more. "
    " You wonder what you could do for the rest of the break... "
    " Oh right. "
    " You've heard that there was someone who kept skipping their classes. "
    " Why not figure out who that person is? "
    " Should be pretty easy if they're being talked about a lot. "
    " The problem is, finding their classmates who know them. "
    " You're just going to tell them that you're gonna have to talk with them... "
    " In a very non-threatening way. "
    " Totally not about to scold them for skipping. "
    " I mean, they HAVE been skipping a lot, so... "
    " Only reasonable for them to get a scolding. "
    " And you can't really just...stand around and let them skip. "
    " You're a teacher, you have to do your job. "
    " Plus, Miss Grace is just gonna kill you if you're not doing your job correctly. "
    " Not literally, but I meant that as in kicking you out. "
    " Alright, without all of the yapping... "
    " Let's get asking. You've got all break to do this. "
    scene black with dissolve
    " You spent the rest of the break asking around for the skipping kid's name. "
    " You eventually figured out who it was and found them at the back of the school. "
    " Of course, you had a nice and calm talk with them about how they should be in class... "
    " Though when you saw them not listening, you grabbed their headsets away. "
    " You told them they're not gonna have this until your class is over. "
    " And that's when they really started listening to you... "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time to help someone else. "
    " You went back into the school and guided the student to their classroom. "
    " You then looked around for anyone who might need help from you. "
    pause 2.0
    jump tthursclass3
label tthursclass3:
    scene hallway with dissolve
    " Who would you like to help for this break? "
    if circleknow,emilyknow,demiknow == True:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump circlesaja
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump emilysaja
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump demisaja
    elif circleknow,emilyknow == True and demiknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump circlesaja
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump emilysaja
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump demisaja
    elif circleknow,demiknow == True and emilyknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump circlesaja
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump emilysaja
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump demisaja
    elif demiknow,emilyknow == True and circleknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump circlesaja
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump emilysaja
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump demisaja
    elif circleknow == True and emilyknow,demiknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump circlesaja
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump emilysaja
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump demisaja
    elif emilyknow == True and circleknow,demiknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump circlesaja
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump emilysaja
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump demisaja
    elif demiknow == True and circleknow,emilyknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump circlesaja
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump emilysaja
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump demisaja
    else:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump circlesaja
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump emilysaja
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump demisaja
    label circlesaja:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom, hopefully nothing important is going on... "
        " And you were right, nothing important was going on. "
        " Looks like they were just copying from the math teacher's slides. "
        " The teacher just had to press a button and boop, next slide. "
        " Pretty easy thing to do, but you've also gotta make sure that students are actually copying. "
        " If not, thennn...seems like their grades are gonna be doomed. "
        " You wanted to talk to the math teacher though, so you walked over to her and grabbed a seat next to her. "
        show misscircleneutral at center with easeinleft
        if circleknow == True:
            msc " Hmmmhmmm... "
            msc " I should probably restock my oreo stash. "
            msc " Even tho it's got like... "
            msc " 250 oreos in total, it could never hurt to add more! "
            msc " More oreos a day, more happiness coming your way! "
            hide misscircleneutral at bottom
            show misscirclehappy at center
            msc " Oh, hey [name]! almost didn't notice ya. "
            msc " Just letting my students do their thing and copy for their notes... "
            msc " Atleast now they have SOMETHING in their notebooks now. "
            msc " I wouldn't wanna open them just for them to be empty pages! "
            msc " That just shows that I haven't been a good teacher! "
            hide misscirclehappy at bottom
            show misscircleneutral at center
            msc " And I don't wanna do a bad job at well...my job. "
            msc " That'd just be weird if I come here and do nothing at all. "
            msc " I'm sure if Miss Grace noticed that I was doing nothing.. "
            msc " She'd probably be a whole lot mad. "
            msc " I mean, I get it! I'm not doing my job right! "
            msc " Actually...she'd be way more mad than you think. "
            msc " I know that it kinda looks like she's doing nothing, but uh... "
            msc " Yeah. She's really doing something while we're doing all our jobs, really. "
            msc " Even if it looks like she's slacking off most of the time. "
            msc " Kinda find it cool that she always looks like she's doing nothing serious even though she is... "
            msc " Lowkey wanna do that some day to cause fear on some of my students, too! "
            msc " You know...to get them back in line. "
            msc " They cause trouble every now and then and I just wanna thwack them in the head for that. "
            msc " Iffff only Miss Grace would kinda allow me to do that... "
            msc " I would get in trouble if I tried to. "
            msc " I tried to do that once and she kind of lowered my paymenttt... "
            msc " I don't think I'd want to get it any lower. "
            msc " But, uh...on a different topic! "
            msc " Which one do you think is better? "
            msc " Kitkats, or oreos? "
            menu:
                " Oreos, duh ":
                    $ circlelv += 10
                    hide misscircleneutral at bottom
                    show misscirclehappy at center
                    msc " Aha, you get me! "
                    msc " Oreos are just IT. And I mean that in a very good way. "
                    msc " Like, I mean...the flavor... "
                    msc " Don't you think that it's just utterly divine? "
                    msc " I think anyone who doesn't like oreos are wrong. "
                    msc " Just my opinion though. "
                    msc " Oreos are the best!! "
                    scene black with dissolve
                    " You spent the rest of the class hours talking to Miss Circle about oreos. "
                    " This was...doing anything but helping her, "
                    " But you're pretty much just fine hanging out with her for the time being. "
                    " Atleast you get some sort of relaxation time. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak3
                " Kitkats, duh ":
                    $ circlelv += 5
                    msc " You see, I would be judging you hard right now... "
                    msc " But I literally have a friend who enjoys kitkats. "
                    msc " I can't be saying mean stuff about that. "
                    msc " Otherwise that friend is gonna come out and start going on a rant. "
                    msc " And I don't want them interrupting class. "
                    msc " Would just be really awkward if they showed up... "
                    scene black with dissolve
                    " You spent the rest of the class hours talking to Miss Circle about oreos. "
                    " This was...doing anything but helping her, "
                    " But you're pretty much just fine hanging out with her for the time being. "
                    " Atleast you get some sort of relaxation time. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak3
        else:
            x " Hmmmhmmm... "
            x " I should probably restock my oreo stash. "
            x " Even tho it's got like... "
            x " 250 oreos in total, it could never hurt to add more! "
            x " More oreos a day, more happiness coming your way! "
            hide misscircleneutral at bottom
            show misscirclehappy at center
            x " Oh, hey [name]! almost didn't notice ya. "
            x " Ooooh, hold on, hold on! I don't think we've met before! "
            x " Or, introduced myself to you, at least. "
            x " I should probably do that right now. "
            x " Would be bad if we were coworkers and didn't know eachothers name! "
            x " Or...something. "
            $ circleknow = True
            msc " I'm Miss Circle, the math teacher! pleased to meet you! "
            " You greeted her politely before asking her what she was doing. "
            msc " Just letting my students do their thing and copy for their notes... "
            msc " Atleast now they have SOMETHING in their notebooks now. "
            msc " I wouldn't wanna open them just for them to be empty pages! "
            msc " That just shows that I haven't been a good teacher! "
            hide misscirclehappy at bottom
            show misscircleneutral at center
            msc " And I don't wanna do a bad job at well...my job. "
            msc " That'd just be weird if I come here and do nothing at all. "
            msc " I'm sure if Miss Grace noticed that I was doing nothing.. "
            msc " She'd probably be a whole lot mad. "
            msc " I mean, I get it! I'm not doing my job right! "
            msc " Actually...she'd be way more mad than you think. "
            msc " I know that it kinda looks like she's doing nothing, but uh... "
            msc " Yeah. She's really doing something while we're doing all our jobs, really. "
            msc " Even if it looks like she's slacking off most of the time. "
            msc " Kinda find it cool that she always looks like she's doing nothing serious even though she is... "
            msc " Lowkey wanna do that some day to cause fear on some of my students, too! "
            msc " You know...to get them back in line. "
            msc " They cause trouble every now and then and I just wanna thwack them in the head for that. "
            msc " Iffff only Miss Grace would kinda allow me to do that... "
            msc " I would get in trouble if I tried to. "
            msc " I tried to do that once and she kind of lowered my paymenttt... "
            msc " I don't think I'd want to get it any lower. "
            msc " But, uh...on a different topic! "
            msc " Which one do you think is better? "
            msc " Kitkats, or oreos? "
            menu:
                " Oreos, duh ":
                    $ circlelv += 10
                    hide misscircleneutral at bottom
                    show misscirclehappy at center
                    msc " Aha, you get me! "
                    msc " Oreos are just IT. And I mean that in a very good way. "
                    msc " Like, I mean...the flavor... "
                    msc " Don't you think that it's just utterly divine? "
                    msc " I think anyone who doesn't like oreos are wrong. "
                    msc " Just my opinion though. "
                    msc " Oreos are the best!! "
                    scene black with dissolve
                    " You spent the rest of the class hours talking to Miss Circle about oreos. "
                    " This was...doing anything but helping her, "
                    " But you're pretty much just fine hanging out with her for the time being. "
                    " Atleast you get some sort of relaxation time. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak3
                " Kitkats, duh ":
                    $ circlelv += 5
                    msc " You see, I would be judging you hard right now... "
                    msc " But I literally have a friend who enjoys kitkats. "
                    msc " I can't be saying mean stuff about that. "
                    msc " Otherwise that friend is gonna come out and start going on a rant. "
                    msc " And I don't want them interrupting class. "
                    msc " Would just be really awkward if they showed up... "
                    scene black with dissolve
                    " You spent the rest of the class hours talking to Miss Circle about oreos. "
                    " This was...doing anything but helping her, "
                    " But you're pretty much just fine hanging out with her for the time being. "
                    " Atleast you get some sort of relaxation time. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak3
    label emilysaja:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the history teacher's classroom, hoping nothing important is happening... "
        " Annnd you were right, nothing important was happening. "
        " Looks like the students were just answeing yet another activity. "
        " God, they're really making them do a lot of activities today. "
        " I mean...the programmer has to somehow keep the normal route's thing going on. "
        " Interacting with the teachers every time it's class hours. "
        " Okay, anyway... "
        " You look around and found the history teacher arranging a few things at the back. "
        " Let's see if you could help with that... "
        show msemilyneutral at center with easeinleft
        if emilyknow == True:
            mse " Hmhmmm... "
            mse " Maybe I could move this here? "
            mse " No, it would look too odd. "
            mse " Maybe if I just move this to the side... "
            mse " ...Yes, this looks better! "
            mse " Now I just have to arrange the rest... "
            " You greeted her politely before asking if you could help with what shes doing. "
            " You wanted to help her, a lot. "
            " That's what a good coworker should do, right? "
            mse " Oh, [name]! "
            mse " You wanted to help me? "
            mse " Hehe, that's really sweet of you... "
            mse " I'm just arranging things to make the room look better. "
            mse " It...does look better in the new arrangement I put it in, right? "
            mse " I'm gonna have to need your opinion in order for me to improve it! "
            mse " Otherwise I think it's gonna look a bit bad without the criticism. "
            mse " Don't you think? "
            " You nodded, before you thought about her question. "
            " What do you think about Miss Emily's layout? "
            " Can't really show you a picture of it, so you can just imagine in your head. "
            " So...what do you think? "
            menu:
                " It looks great! ":
                    $ emilylv += 10
                    hide msemilyneutral at bottom
                    show msemilyhappy at center
                    mse " Really? I'm glad you think so! "
                    mse " Kind of had to ask everyone if this looked good or not... "
                    mse " Most people think that it looks awesome! "
                    mse " And I kinda want it to be that way...you know, awesome? "
                    mse " But I don't know how to keep it that way. "
                    mse " Sooo...I might just need your help for this one. "
                    mse " If you don't mind, of course! "
                    mse " We don't really do forcing around this school. "
                    " Well, you did come over just to help... "
                    " You gave her a thumbs up and told her that you'll help. "
                    mse " Wonderful! "
                    mse " We've basically got the whole period to redesign everything. "
                    mse " And we should start now - for the best. "
                    mse " You take that side and I take this side, okay? "
                    mse " And if we're not sure on where to put something... "
                    mse " We should just ask eachother if it looks good or not! "
                    mse " Alright, let's begin! "
                    scene black with dissolve
                    " You spent the rest of the class hours helping Miss Emily. "
                    " And boy, you two asked if things looked good a LOT. "
                    " I mean, it's to be expected since you're both trying to make everything look good. "
                    " In the end, the result turned out absolutely wonderful. "
                    " You two talked for the rest of the period after you guys were done. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak3
                " It looks fine ":
                    $ emilylv += 5
                    mse " I'm glad you think so! "
                    mse " Kind of had to ask everyone if this looked good or not... "
                    mse " Most people think that it looks awesome! "
                    mse " And I kinda want it to be that way...you know, awesome? "
                    mse " But I don't know how to keep it that way. "
                    mse " Sooo...I might just need your help for this one. "
                    mse " If you don't mind, of course! "
                    mse " We don't really do forcing around this school. "
                    " Well, you did come over just to help... "
                    " You gave her a thumbs up and told her that you'll help. "
                    mse " Wonderful! "
                    mse " We've basically got the whole period to redesign everything. "
                    mse " And we should start now - for the best. "
                    mse " You take that side and I take this side, okay? "
                    mse " And if we're not sure on where to put something... "
                    mse " We should just ask eachother if it looks good or not! "
                    mse " Alright, let's begin! "
                    scene black with dissolve
                    " You spent the rest of the class hours helping Miss Emily. "
                    " And boy, you two asked if things looked good a LOT. "
                    " I mean, it's to be expected since you're both trying to make everything look good. "
                    " In the end, the result turned out absolutely wonderful. "
                    " You two talked for the rest of the period after you guys were done. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak3
        else:
            x " Hmhmmm... "
            x " Maybe I could move this here? "
            x " No, it would look too odd. "
            x " Maybe if I just move this to the side... "
            x " ...Yes, this looks better! "
            x " Now I just have to arrange the rest... "
            " You greeted her politely before asking if you could help with what shes doing. "
            " You wanted to help her, a lot. "
            " That's what a good coworker should do, right? "
            x " Oh, [name]! "
            x " You wanted to help me? "
            x " Hehe, that's really sweet of you... "
            x " Hold on, wait... "
            x " I don't think I've introduced myself to you before! "
            $ emilyknow = True
            mse " I'm Miss Emily, the history teacher! "
            mse " A lot of people told me I taught a boring subject, but I don't really care. "
            mse " It's my choice on what I teach, get your hands off of what I do! "
            mse " Anywho, before I go on another rant... "
            mse " I'm just arranging things to make the room look better. "
            mse " It...does look better in the new arrangement I put it in, right? "
            mse " I'm gonna have to need your opinion in order for me to improve it! "
            mse " Otherwise I think it's gonna look a bit bad without the criticism. "
            mse " Don't you think? "
            " You nodded, before you thought about her question. "
            " What do you think about Miss Emily's layout? "
            " Can't really show you a picture of it, so you can just imagine in your head. "
            " So...what do you think? "
            menu:
                " It looks great! ":
                    $ emilylv += 10
                    hide msemilyneutral at bottom
                    show msemilyhappy at center
                    mse " Really? I'm glad you think so! "
                    mse " Kind of had to ask everyone if this looked good or not... "
                    mse " Most people think that it looks awesome! "
                    mse " And I kinda want it to be that way...you know, awesome? "
                    mse " But I don't know how to keep it that way. "
                    mse " Sooo...I might just need your help for this one. "
                    mse " If you don't mind, of course! "
                    mse " We don't really do forcing around this school. "
                    " Well, you did come over just to help... "
                    " You gave her a thumbs up and told her that you'll help. "
                    mse " Wonderful! "
                    mse " We've basically got the whole period to redesign everything. "
                    mse " And we should start now - for the best. "
                    mse " You take that side and I take this side, okay? "
                    mse " And if we're not sure on where to put something... "
                    mse " We should just ask eachother if it looks good or not! "
                    mse " Alright, let's begin! "
                    scene black with dissolve
                    " You spent the rest of the class hours helping Miss Emily. "
                    " And boy, you two asked if things looked good a LOT. "
                    " I mean, it's to be expected since you're both trying to make everything look good. "
                    " In the end, the result turned out absolutely wonderful. "
                    " You two talked for the rest of the period after you guys were done. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak3
                " It looks fine ":
                    $ emilylv += 5
                    mse " I'm glad you think so! "
                    mse " Kind of had to ask everyone if this looked good or not... "
                    mse " Most people think that it looks awesome! "
                    mse " And I kinda want it to be that way...you know, awesome? "
                    mse " But I don't know how to keep it that way. "
                    mse " Sooo...I might just need your help for this one. "
                    mse " If you don't mind, of course! "
                    mse " We don't really do forcing around this school. "
                    " Well, you did come over just to help... "
                    " You gave her a thumbs up and told her that you'll help. "
                    mse " Wonderful! "
                    mse " We've basically got the whole period to redesign everything. "
                    mse " And we should start now - for the best. "
                    mse " You take that side and I take this side, okay? "
                    mse " And if we're not sure on where to put something... "
                    mse " We should just ask eachother if it looks good or not! "
                    mse " Alright, let's begin! "
                    scene black with dissolve
                    " You spent the rest of the class hours helping Miss Emily. "
                    " And boy, you two asked if things looked good a LOT. "
                    " I mean, it's to be expected since you're both trying to make everything look good. "
                    " In the end, the result turned out absolutely wonderful. "
                    " You two talked for the rest of the period after you guys were done. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak3
    label demisaja:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the music teachers classroom and prayed nothing interesting was going on... "
        " Aaaand looks like everyone was just doing a group activity, interesting. "
        " You heard a lot of people singing - most likely a singing activity. "
        " And also noticed that a lot of them had homemade instruments with them. Huh. "
        " They might be making a song for a specific topic... "
        " You looked around and saw the music teacher at the back cleaning some instruments. "
        " I mean, you've walked in here before and noticed that they DID look a little dusty... "
        " Maybe you could help in cleaning them. "
        " You walked over to him and grabbed a seat next to him. "
        show mrdemineutral at center with easeinleft
        if demiknow == True:
            msd " Oh, these poor things really have been dirty... "
            msd " Wonder why the others never bothered to look at them... "
            msd " Were these just for display...? "
            msd " They're still pretty expensive instruments, "
            msd " They should still be cleaned and used every now and then... "
            msd " ...I mean, what if someone wanted to use these for a project...? "
            msd " And then when they try it infront of the class, they'll get embarrassed because it doesn't work... "
            msd " Geez, I'm rambling again... "
            " You greeted him politely before asking if you could help with cleaning. "
            msd " O-oh! uh, [name]... "
            msd " Lovely to see you here... "
            msd " ...I was just cleaning these instruments, as you can see... "
            msd " These look like they haven't even been cleaned in a long time... "
            msd " That makes me a little sad to think about... "
            msd " These things are really expensive, afer all...! "
            msd " They should be well taken cared of, not to be on display... "
            msd " Siighhh...I'm gonna go on another rant, aren't I...? "
            msd " ...I don't want to blow your ears off though... "
            msd " I would just be bothering you if I did... "
            menu:
                " It's okay, I like instruments too ":
                    $ demilv += 10
                    msd " ...Yeah... "
                    msd " A-anyway, I think you should clean those instruments over there... "
                    msd " If you're struggling on how to clean it, just ask me.. "
                    msd " You've got to be really careful with these, since they're so expensive... "
                    msd " I wouldn't want to break any one of these... "
                    msd " ...They're still school property, and I would have to pay a lot if they got broken... "
                    msd " That would be bad, since I don't have a lot of money... "
                    msd " Siiigh... "
                    msd " We should probably start working now though... "
                    msd " I don't want to waste time, for now... "
                    msd " W-we could also talk while working, if you want... "
                    msd " I don't want things to be awkward, either... "
                    msd " Um...let's get started...? "
                    scene black with dissolve
                    " You spent the rest of class hours helping Mister Demi clean the instruments. "
                    " You two talked about various things, like the new trend going around. "
                    " What was it again...? "
                    " People kept saying, uh...SDIYBT???? Start digging in yo... "
                    " Oh wait, sorry, the higher ups won't let me say this one. "
                    " As much as I'd like to for the funnies, I don't wanna get fired. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak3
                " It's fine ":
                    msd " ...Yeah... "
                    msd " A-anyway, I think you should clean those instruments over there... "
                    msd " If you're struggling on how to clean it, just ask me.. "
                    msd " You've got to be really careful with these, since they're so expensive... "
                    msd " I wouldn't want to break any one of these... "
                    msd " ...They're still school property, and I would have to pay a lot if they got broken... "
                    msd " That would be bad, since I don't have a lot of money... "
                    msd " Siiigh... "
                    msd " We should probably start working now though... "
                    msd " I don't want to waste time, for now... "
                    msd " W-we could also talk while working, if you want... "
                    msd " I don't want things to be awkward, either... "
                    msd " Um...let's get started...? "
                    scene black with dissolve
                    " You spent the rest of class hours helping Mister Demi clean the instruments. "
                    " You two talked about various things, like the new trend going around. "
                    " What was it again...? "
                    " People kept saying, uh...SDIYBT???? Start digging in yo... "
                    " Oh wait, sorry, the higher ups won't let me say this one. "
                    " As much as I'd like to for the funnies, I don't wanna get fired. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak3
        else:
            x " Oh, these poor things really have been dirty... "
            x " Wonder why the others never bothered to look at them... "
            x " Were these just for display...? "
            x " They're still pretty expensive instruments, "
            x " They should still be cleaned and used every now and then... "
            x " ...I mean, what if someone wanted to use these for a project...? "
            x " And then when they try it infront of the class, they'll get embarrassed because it doesn't work... "
            x " Geez, I'm rambling again... "
            " You greeted him politely before asking if you could help with cleaning. "
            x " O-oh! uh, [name]... "
            x " Lovely to see you here... "
            x " Um... "
            x " Excuse me, but...I don't think I've itnroduced myself to you yet before... "
            x " I'm sorry, I should probably do that right now... "
            $ demiknow = True
            msd " I-I'm Mister Demi...the music teacher...and, uh... "
            msd " ...I was just cleaning these instruments, as you can see... "
            msd " These look like they haven't even been cleaned in a long time... "
            msd " That makes me a little sad to think about... "
            msd " These things are really expensive, afer all...! "
            msd " They should be well taken cared of, not to be on display... "
            msd " Siighhh...I'm gonna go on another rant, aren't I...? "
            msd " ...I don't want to blow your ears off though... "
            msd " I would just be bothering you if I did... "
            menu:
                " It's okay, I like instruments too ":
                    $ demilv += 10
                    msd " ...Yeah... "
                    msd " A-anyway, I think you should clean those instruments over there... "
                    msd " If you're struggling on how to clean it, just ask me.. "
                    msd " You've got to be really careful with these, since they're so expensive... "
                    msd " I wouldn't want to break any one of these... "
                    msd " ...They're still school property, and I would have to pay a lot if they got broken... "
                    msd " That would be bad, since I don't have a lot of money... "
                    msd " Siiigh... "
                    msd " We should probably start working now though... "
                    msd " I don't want to waste time, for now... "
                    msd " W-we could also talk while working, if you want... "
                    msd " I don't want things to be awkward, either... "
                    msd " Um...let's get started...? "
                    scene black with dissolve
                    " You spent the rest of class hours helping Mister Demi clean the instruments. "
                    " You two talked about various things, like the new trend going around. "
                    " What was it again...? "
                    " People kept saying, uh...SDIYBT???? Start digging in yo... "
                    " Oh wait, sorry, the higher ups won't let me say this one. "
                    " As much as I'd like to for the funnies, I don't wanna get fired. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak3
                " It's fine ":
                    msd " ...Yeah... "
                    msd " A-anyway, I think you should clean those instruments over there... "
                    msd " If you're struggling on how to clean it, just ask me.. "
                    msd " You've got to be really careful with these, since they're so expensive... "
                    msd " I wouldn't want to break any one of these... "
                    msd " ...They're still school property, and I would have to pay a lot if they got broken... "
                    msd " That would be bad, since I don't have a lot of money... "
                    msd " Siiigh... "
                    msd " We should probably start working now though... "
                    msd " I don't want to waste time, for now... "
                    msd " W-we could also talk while working, if you want... "
                    msd " I don't want things to be awkward, either... "
                    msd " Um...let's get started...? "
                    scene black with dissolve
                    " You spent the rest of class hours helping Mister Demi clean the instruments. "
                    " You two talked about various things, like the new trend going around. "
                    " What was it again...? "
                    " People kept saying, uh...SDIYBT???? Start digging in yo... "
                    " Oh wait, sorry, the higher ups won't let me say this one. "
                    " As much as I'd like to for the funnies, I don't wanna get fired. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak3
label tthursbreak3:
    scene hallway with dissolve
    " You looked around and saw a student struggling to carry their books. "
    " Huh. You wonder why they have that many books in the first place... "
    " Nonetheless, you should help them. "
    " I mean, no one's helping them so you've got to do it. "
    " You've gotta be a good rolemodel somehow. "
    " As you were thinking, you noticed that the kid was about to trip a little bit. "
    " You immediately rushed over to them and made sure they were alright. "
    " You took half of the books so they could balance themselves, and you asked where they were headed. "
    " They told you that they were going to the library to study. "
    " Wow, someone who actually studies? insane. "
    " Atleast they're actually trying to learn though. "
    " That's pretty good, in all honesty. "
    " A rare thing you'd see in a student, but good nonetheless. "
    " You then started walking with the student to the library. "
    scene black with dissolve
    " You spent the rest of the break walking over to the library. "
    " The library was a tad bit far from where you were at, so you had to walk a long bit. "
    " You didn't want to make things awkward, so you made conversation with the student. "
    " They were really sweet and kind... "
    " You could tell that they had a bright future ahead of them. "
    " They had everything all planned out. Sweet, right? "
    " Eventually, you two got to the library. "
    " You placed all of their books down and went to do some gaming. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time to help someone again. "
    " You walked out of the library and went to the hallways to check if someone needed help. "
    pause 2.0
    jump tthursclass4
label tthursclass4:
    scene hallway with dissolve
    " Who do you wanna help for today? "
    if sashaknow,bloomieknow,thavelknow == True:
        menu:
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump drivinginmysasha
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump rightafterabloomie
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump heythatbumpisshapedlikeathavel
    elif sashaknow,bloomieknow == True and thavelknow == False:
        menu:
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump drivinginmysasha
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump rightafterabloomie
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump heythatbumpisshapedlikeathavel
    elif sashaknow,thavelknow == True and bloomieknow == False:
        menu:
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump drivinginmysasha
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump rightafterabloomie
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump heythatbumpisshapedlikeathavel
    elif bloomieknow,thavelknow == True and sashaknow == False:
        menu:
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump drivinginmysasha
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump rightafterabloomie
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump heythatbumpisshapedlikeathavel
    elif sashaknow == True and bloomieknow,thavelknow == False:
        menu:
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump drivinginmysasha
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump rightafterabloomie
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump heythatbumpisshapedlikeathavel
    elif bloomieknow == True and sashaknow,thavelknow == False:
        menu:
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump drivinginmysasha
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump rightafterabloomie
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump heythatbumpisshapedlikeathavel
    elif thavelknow == True and sashaknow,bloomieknow == False:
        menu:
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump drivinginmysasha
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump rightafterabloomie
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump heythatbumpisshapedlikeathavel
    else:
        menu:
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump drivinginmysasha
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump rightafterabloomie
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump heythatbumpisshapedlikeathavel
    label drivinginmysasha:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom to make sure nothing was going on... "
        " And nothing really was going on. "
        " Other than the students painting on their own vases. "
        " Must be another activity that the teacher put up with. "
        " Interesting...you lowkey wanna know how it feels like to paint on a vase. "
        " You looked around and spotted the teacher doing a vase painting herself at her desk. "
        " You wanted to see how it looked, so you walked over to her and asked how she was doing. "
        show sashaneutral at center with easeinleft
        if sashaknow == True:
            mss " Hmhmmm... "
            mss " Just a little paint over there... "
            mss " And a little more there... "
            mss " Aaaah, it's so perfect! "
            " You greeted her politely and asked her what she was painting. "
            mss " Oooh, [name]! Right on time! "
            mss " I needed someone's opinion on my vase painting, hehe. "
            mss " You see - I let my students do some vase painting as an activity! "
            mss " Turns out I had an extra one and I kind of wanted to do a painting myself... "
            mss " You know, to pass the time? "
            mss " I don't really wanna always use my phone for breaks... "
            mss " That's why I decided to do some vase painting for now! "
            mss " And like I said, I needed someone's opinion on this! "
            " Miss Sasha then turns her vase around to be facing you. "
            " It was a very colorful vase with a nice painting of Sasha and her students. "
            " All of them getting together and being happy... "
            " A nice painting, truly. "
            mss " This painting shows me and my students! "
            mss " Why I made a painting about myself and them? well... "
            mss " I think all of my students are wonderful! "
            mss " And I also wanted to have something to remind me of them, sooo... "
            mss " That's why I put them in here, too! "
            mss " Sooo...what do you think? "
            menu:
                " It looks amazing! ":
                    $ sashalv += 10
                    hide sashaneutral at bottom
                    show sashahappy at center
                    mss " Really??? Yay!! "
                    mss " I'm glad you said it looked nice! "
                    mss " If you said it looked a little...ehh... "
                    mss " I would've gone and changed it all entirely, haha. "
                    mss " I don't really care if it's more work for me - "
                    mss " Atleast I have something to do that can make me entertained! "
                    hide sashahappy at bottom
                    show sashaneutral at center
                    mss " Hey..speaking of vase painting... "
                    mss " I actually have another vase just sitting around! "
                    mss " It was reserved for another student, but they told me that they didn't want to do the activity, so... "
                    mss " You can go ahead and try vase painting if you want to! "
                    mss " Not gonna force ya if you don't want to! "
                    " You had no choice here. "
                    " You nodded and told her that you wanted to try out vase painting. "
                    " Atleast this gives you something to do. "
                    mss " Great! "
                    mss " You can borrow some of my paint over there... "
                    mss " I don't mind! "
                    scene black with dissolve
                    " You spent the rest of the class hours vase painting with Miss Sasha. "
                    " And honestly? it was pretty fun. "
                    " You made a pretty basic design, but it looked good. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak4
                " It looks nice ":
                    hide sashaneutral at bottom
                    show sashahappy at center
                    mss " Glad you think so! "
                    mss " I'm glad you said it looked nice! "
                    mss " If you said it looked a little...ehh... "
                    mss " I would've gone and changed it all entirely, haha. "
                    mss " I don't really care if it's more work for me - "
                    mss " Atleast I have something to do that can make me entertained! "
                    hide sashahappy at bottom
                    show sashaneutral at center
                    mss " Hey..speaking of vase painting... "
                    mss " I actually have another vase just sitting around! "
                    mss " It was reserved for another student, but they told me that they didn't want to do the activity, so... "
                    mss " You can go ahead and try vase painting if you want to! "
                    mss " Not gonna force ya if you don't want to! "
                    " You had no choice here. "
                    " You nodded and told her that you wanted to try out vase painting. "
                    " Atleast this gives you something to do. "
                    mss " Great! "
                    mss " You can borrow some of my paint over there... "
                    mss " I don't mind! "
                    scene black with dissolve
                    " You spent the rest of the class hours vase painting with Miss Sasha. "
                    " And honestly? it was pretty fun. "
                    " You made a pretty basic design, but it looked good. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak4
        else:
            x " Hmhmmm... "
            x " Just a little paint over there... "
            x " And a little more there... "
            x " Aaaah, it's so perfect! "
            " You greeted her politely and asked her what she was painting. "
            x " Oooh, [name]! Right on time! "
            x " I needed someone's opinion on my vase painting, hehe. "
            x " But before you get to do that - I gotta introduce myself! "
            x " I just now realized that I haven't introduced myself to you yet, I'm really sorryfor that, hehe... "
            x " Anyway! "
            $ sashaknow = True
            mss " I'm Miss Sasha, nice to meet you! "
            mss " I'm the art teacher, and for what I'm doing today... "
            mss " You see - I let my students do some vase painting as an activity! "
            mss " Turns out I had an extra one and I kind of wanted to do a painting myself... "
            mss " You know, to pass the time? "
            mss " I don't really wanna always use my phone for breaks... "
            mss " That's why I decided to do some vase painting for now! "
            mss " And like I said, I needed someone's opinion on this! "
            " Miss Sasha then turns her vase around to be facing you. "
            " It was a very colorful vase with a nice painting of Sasha and her students. "
            " All of them getting together and being happy... "
            " A nice painting, truly. "
            mss " This painting shows me and my students! "
            mss " Why I made a painting about myself and them? well... "
            mss " I think all of my students are wonderful! "
            mss " And I also wanted to have something to remind me of them, sooo... "
            mss " That's why I put them in here, too! "
            mss " Sooo...what do you think? "
            menu:
                " It looks amazing! ":
                    $ sashalv += 10
                    hide sashaneutral at bottom
                    show sashahappy at center
                    mss " Really??? Yay!! "
                    mss " I'm glad you said it looked nice! "
                    mss " If you said it looked a little...ehh... "
                    mss " I would've gone and changed it all entirely, haha. "
                    mss " I don't really care if it's more work for me - "
                    mss " Atleast I have something to do that can make me entertained! "
                    hide sashahappy at bottom
                    show sashaneutral at center
                    mss " Hey..speaking of vase painting... "
                    mss " I actually have another vase just sitting around! "
                    mss " It was reserved for another student, but they told me that they didn't want to do the activity, so... "
                    mss " You can go ahead and try vase painting if you want to! "
                    mss " Not gonna force ya if you don't want to! "
                    " You had no choice here. "
                    " You nodded and told her that you wanted to try out vase painting. "
                    " Atleast this gives you something to do. "
                    mss " Great! "
                    mss " You can borrow some of my paint over there... "
                    mss " I don't mind! "
                    scene black with dissolve
                    " You spent the rest of the class hours vase painting with Miss Sasha. "
                    " And honestly? it was pretty fun. "
                    " You made a pretty basic design, but it looked good. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak4
                " It looks nice ":
                    hide sashaneutral at bottom
                    show sashahappy at center
                    mss " Glad you think so! "
                    mss " I'm glad you said it looked nice! "
                    mss " If you said it looked a little...ehh... "
                    mss " I would've gone and changed it all entirely, haha. "
                    mss " I don't really care if it's more work for me - "
                    mss " Atleast I have something to do that can make me entertained! "
                    hide sashahappy at bottom
                    show sashaneutral at center
                    mss " Hey..speaking of vase painting... "
                    mss " I actually have another vase just sitting around! "
                    mss " It was reserved for another student, but they told me that they didn't want to do the activity, so... "
                    mss " You can go ahead and try vase painting if you want to! "
                    mss " Not gonna force ya if you don't want to! "
                    " You had no choice here. "
                    " You nodded and told her that you wanted to try out vase painting. "
                    " Atleast this gives you something to do. "
                    mss " Great! "
                    mss " You can borrow some of my paint over there... "
                    mss " I don't mind! "
                    scene black with dissolve
                    " You spent the rest of the class hours vase painting with Miss Sasha. "
                    " And honestly? it was pretty fun. "
                    " You made a pretty basic design, but it looked good. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak4
    label rightafterabloomie:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the science teachers classroom and looked around to see if they're doing something important... "
        " Huh. Looks like they're doing nothing important right now... "
        " Again. Most classes aren't doing anything important for the day. "
        " Important as in discussing a lesson. "
        " Looks like they're all getting prepared for a reporting... "
        " They're currently working on a design for their topic. "
        " You looked around and spotted the science teacher in the corner. "
        " You then walked over to her to see what she was doing over there. "
        show missbloomieneutral at center with easeinleft
        if bloomieknow == True:
            msb " ...Hm. "
            msb " Hi there, [name]. "
            msb " You must be wondering why I'm hanging out in a corner right now... "
            msb " It's just that I feel most comfortable in this corner. "
            msb " I usually hang here whenever I feel like the noise is too loud. "
            msb " Or whenever I feel like I need a break, in other words. "
            msb " Sometimes these students can really tick me off. "
            msb " And that's why I need a break every now and then. "
            msb " I don't really want to waste my breath on them, so I stay here to calm myself down... "
            msb " And whenever I feel like I'm ready, I come back to teach them. "
            msb " I really hate it whenever they ask the same question over and over again... "
            msb " That's actually one of the reasons why I come over to this corner most of the time. "
            msb " Asking what to do is okay 3 times, but above that? "
            msb " I'm going to have to start thinking that you're braindead. "
            msb " It's real annoying and I don't like it... "
            msb " Siigh. I wish these students can just be fast learners... "
            msb " Things would've been easier if they were. "
            msb " Way more easier than having to deal with them being nuisances... "
            msb " Sorry that I'm kind of ranting to you right now, [name]. "
            msb " I just need to say a few things to cool myself off. "
            msb " I hope I wasn't bothering you with my talking. "
            menu:
                " It's alright, you can talk to me ":
                    $ bloomielv += 10
                    msb " ...Thanks. I appreciate that. "
                    msb " You sure you really want me to talk to you? "
                    msb " I mean, I can get a bit much while ranting. "
                    msb " Trust me, Circle and Thavel have heard me rant before. "
                    msb " They said I was a little too intense for ranting... "
                    " You told her it was fine. "
                    " After all, she was just venting her frustrations out. "
                    " There's nothing wrong with that at all. "
                    msb " ...Well, if you say so, then... "
                    msb " I'll start talking since you want me to. "
                    msb " Thanks for letting me talk with you, [name]. "
                    msb " I would've kinda bottled up how I felt if you didn't talk to me. "
                    msb " Or I would've just gone to Circle's classroom... "
                    msb " Or Thavel's, if those two aren't doing anything important. "
                    msb " I'm actually pretty close with them. "
                    msb " If you...somehow haven't noticed that. "
                    msb " We've been friends ever since highschool, actually. "
                    msb " But uh...you wanted to hear me rant, right? "
                    msb " Let's do that then. "
                    msb " Still need to vent out my frustrations to you... "
                    scene black with dissolve
                    " You spent the rest of class hours listening to Miss Bloomie rant about her students. "
                    " And god damn, you could see why she's mad about them. "
                    " She gave off a list of reasons why her head always aches whenever she has to teach them... "
                    " And if I listen all of them down right now, the games code would probably go to the point that it would break the game itself. "
                    " And I don't want that to happen. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak4
                " Its fine ":
                    msb " ...Thanks. "
                    msb " You sure you really want me to talk to you? "
                    msb " I mean, I can get a bit much while ranting. "
                    msb " Trust me, Circle and Thavel have heard me rant before. "
                    msb " They said I was a little too intense for ranting... "
                    " You told her it was fine. "
                    " After all, she was just venting her frustrations out. "
                    " There's nothing wrong with that at all. "
                    msb " ...Well, if you say so, then... "
                    msb " I'll start talking since you want me to. "
                    msb " Thanks for letting me talk with you, [name]. "
                    msb " I would've kinda bottled up how I felt if you didn't talk to me. "
                    msb " Or I would've just gone to Circle's classroom... "
                    msb " Or Thavel's, if those two aren't doing anything important. "
                    msb " I'm actually pretty close with them. "
                    msb " If you...somehow haven't noticed that. "
                    msb " We've been friends ever since highschool, actually. "
                    msb " But uh...you wanted to hear me rant, right? "
                    msb " Let's do that then. "
                    msb " Still need to vent out my frustrations to you... "
                    scene black with dissolve
                    " You spent the rest of class hours listening to Miss Bloomie rant about her students. "
                    " And god damn, you could see why she's mad about them. "
                    " She gave off a list of reasons why her head always aches whenever she has to teach them... "
                    " And if I listen all of them down right now, the games code would probably go to the point that it would break the game itself. "
                    " And I don't want that to happen. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak4
        else:
            x " ...Hm. "
            x " Hi there, [name]. "
            $ bloomieknow = True
            msb " I'm Miss Bloomie, the science teacher. Nice to meet you. "
            msb " You must be wondering why I'm hanging out in a corner right now... "
            msb " It's just that I feel most comfortable in this corner. "
            msb " I usually hang here whenever I feel like the noise is too loud. "
            msb " Or whenever I feel like I need a break, in other words. "
            msb " Sometimes these students can really tick me off. "
            msb " And that's why I need a break every now and then. "
            msb " I don't really want to waste my breath on them, so I stay here to calm myself down... "
            msb " And whenever I feel like I'm ready, I come back to teach them. "
            msb " I really hate it whenever they ask the same question over and over again... "
            msb " That's actually one of the reasons why I come over to this corner most of the time. "
            msb " Asking what to do is okay 3 times, but above that? "
            msb " I'm going to have to start thinking that you're braindead. "
            msb " It's real annoying and I don't like it... "
            msb " Siigh. I wish these students can just be fast learners... "
            msb " Things would've been easier if they were. "
            msb " Way more easier than having to deal with them being nuisances... "
            msb " Sorry that I'm kind of ranting to you right now, [name]. "
            msb " I just need to say a few things to cool myself off. "
            msb " I hope I wasn't bothering you with my talking. "
            menu:
                " It's alright, you can talk to me ":
                    $ bloomielv += 10
                    msb " ...Thanks. I appreciate that. "
                    msb " You sure you really want me to talk to you? "
                    msb " I mean, I can get a bit much while ranting. "
                    msb " Trust me, Circle and Thavel have heard me rant before. "
                    msb " They said I was a little too intense for ranting... "
                    " You told her it was fine. "
                    " After all, she was just venting her frustrations out. "
                    " There's nothing wrong with that at all. "
                    msb " ...Well, if you say so, then... "
                    msb " I'll start talking since you want me to. "
                    msb " Thanks for letting me talk with you, [name]. "
                    msb " I would've kinda bottled up how I felt if you didn't talk to me. "
                    msb " Or I would've just gone to Circle's classroom... "
                    msb " Or Thavel's, if those two aren't doing anything important. "
                    msb " I'm actually pretty close with them. "
                    msb " If you...somehow haven't noticed that. "
                    msb " We've been friends ever since highschool, actually. "
                    msb " But uh...you wanted to hear me rant, right? "
                    msb " Let's do that then. "
                    msb " Still need to vent out my frustrations to you... "
                    scene black with dissolve
                    " You spent the rest of class hours listening to Miss Bloomie rant about her students. "
                    " And god damn, you could see why she's mad about them. "
                    " She gave off a list of reasons why her head always aches whenever she has to teach them... "
                    " And if I listen all of them down right now, the games code would probably go to the point that it would break the game itself. "
                    " And I don't want that to happen. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak4
                " Its fine ":
                    msb " ...Thanks. "
                    msb " You sure you really want me to talk to you? "
                    msb " I mean, I can get a bit much while ranting. "
                    msb " Trust me, Circle and Thavel have heard me rant before. "
                    msb " They said I was a little too intense for ranting... "
                    " You told her it was fine. "
                    " After all, she was just venting her frustrations out. "
                    " There's nothing wrong with that at all. "
                    msb " ...Well, if you say so, then... "
                    msb " I'll start talking since you want me to. "
                    msb " Thanks for letting me talk with you, [name]. "
                    msb " I would've kinda bottled up how I felt if you didn't talk to me. "
                    msb " Or I would've just gone to Circle's classroom... "
                    msb " Or Thavel's, if those two aren't doing anything important. "
                    msb " I'm actually pretty close with them. "
                    msb " If you...somehow haven't noticed that. "
                    msb " We've been friends ever since highschool, actually. "
                    msb " But uh...you wanted to hear me rant, right? "
                    msb " Let's do that then. "
                    msb " Still need to vent out my frustrations to you... "
                    scene black with dissolve
                    " You spent the rest of class hours listening to Miss Bloomie rant about her students. "
                    " And god damn, you could see why she's mad about them. "
                    " She gave off a list of reasons why her head always aches whenever she has to teach them... "
                    " And if I listen all of them down right now, the games code would probably go to the point that it would break the game itself. "
                    " And I don't want that to happen. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak4
    label heythatbumpisshapedlikeathavel:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the language teachers classroom, praying that there's nothing important to do... "
        " And you were right, they were doing absolutely nothing. "
        " Well, the students were all working on their own individual projects. "
        " So they were doing something - but not the teacher. "
        " The language teacher was just roaming around and helping the other students make their things. "
        " Maybe you could help her in helping other students? "
        " You walked over to her to see if you could help her or not. "
        show msthravelneutral at center with easeinleft
        if thavelknow == True:
            $ thavellv += 10
            mst " So then you do fold that to make a square, and then... "
            mst " Oh! one of my teacher friends is here, sorry kid... "
            mst " How about you look at this youtube tutorial for a bit? "
            mst " I'm sure it's going to be really helpful! "
            " She puts a youtube tutorial on the kids phone and gives the phone back to the kid a bit after. "
            " She then turns to you. "
            mst " Hiya there, [name]! "
            mst " You must be looking around to help me, aren't you? "
            mst " Well I'm actually pretty happy that you came here! "
            mst " You see, I'm making my students do their own projects... "
            mst " They get to make something related to a country they pick! "
            mst " No matter what it is, as long as it resembles a country! "
            mst " And as long as it isn't making fun of that country. "
            mst " I wouldn't accept anything like that in my classroom. "
            mst " If I ever had a student like that, I'd probably eat their skin. "
            mst " Then again, their skin probably wouldn't taste too good if they're acting like that... "
            mst " Way too salty for my liking, in all honesty. "
            mst " Anyway! Help, right? "
            mst " You can go ahead and help the students at the other side of the classroom! "
            mst " Remember to do a little research first in what they're making before you do! "
            mst " Don't want them to mess up now, do we? "
            mst " Anyway, good luck good luck! "
            scene black with dissolve
            " You spent the rest of the class hours helping Miss Thavel's students. "
            " Atleast you learned a few things about some countries while doing this. "
            " Pretty cool funfacts, really. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone else to get out of the classroom before you did. "
            pause 2.0
            jump tthursbreak4
        else:
            x " So then you do fold that to make a square, and then... "
            x " Oh! one of my teacher friends is here, sorry kid... "
            x " How about you look at this youtube tutorial for a bit? "
            x " I'm sure it's going to be really helpful! "
            " She puts a youtube tutorial on the kids phone and gives the phone back to the kid a bit after. "
            " She then turns to you. "
            x " Hiya there, [name]! "
            x " Oh, hold on... I don't think I've introduced myself to you yet... "
            $ thavelknow = True
            mst " I'm Miss Thavel - language teacher, nice to meet you! anywho... "
            mst " You must be looking around to help me, aren't you? "
            mst " Well I'm actually pretty happy that you came here! "
            mst " You see, I'm making my students do their own projects... "
            mst " They get to make something related to a country they pick! "
            mst " No matter what it is, as long as it resembles a country! "
            mst " And as long as it isn't making fun of that country. "
            mst " I wouldn't accept anything like that in my classroom. "
            mst " If I ever had a student like that, I'd probably eat their skin. "
            mst " Then again, their skin probably wouldn't taste too good if they're acting like that... "
            mst " Way too salty for my liking, in all honesty. "
            mst " Anyway! Help, right? "
            mst " You can go ahead and help the students at the other side of the classroom! "
            mst " Remember to do a little research first in what they're making before you do! "
            mst " Don't want them to mess up now, do we? "
            mst " Anyway, good luck good luck! "
            scene black with dissolve
            " You spent the rest of the class hours helping Miss Thavel's students. "
            " Atleast you learned a few things about some countries while doing this. "
            " Pretty cool funfacts, really. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone else to get out of the classroom before you did. "
            pause 2.0
            jump tthursbreak4
label tthursbreak4:
    scene hallway with dissolve
    " You walked into the hallways and spotted a kid being mistreated. "
    " Looks like they're being left out by their friend group... "
    " They've been trying to get into their conversation for a bit now, "
    " But they've only been getting ignored and ignored all over again. "
    " You felt a little bad... "
    " Being ignored like that isn't fun at all. "
    " You wanted to do something to make them feel better, but don't know what to do. "
    " Maybe you could give them some candy to cheer them up? "
    " But then again, nothing is better than the warmth of a friendship... "
    " You're thinking of what to do... "
    " You then remembered that one of your relatives got you this card before you started working here. "
    " This card would let them buy anything they wanted at a specific restaurant... "
    " The good thing is that this card expires in 2 months. "
    " Maybe they could invite their friends over to eat out with them... "
    " And maybe they could let them back into their conversations. "
    " Wow, you love being a helpful teacher! "
    " Let's walk over to them and talk to them about this. "
    scene black with dissolve
    " You walked over to the kid and gave them the card. "
    " Immediately, they felt pretty happy about getting it and even thanked you... "
    " But the other kid's friends didn't really pay attention. "
    " You told them to just ignore them for now and use that card to spend time with family. "
    " If friends are being unimportant to you, you should put family first next. "
    " The kid felt better just by hearing your words. "
    " You're starting to think that you probably should've been a therapist... "
    " But too late to back out now, I guess. "
    " After watching the kid happily walk away with the card, you wandered around the school. "
    " Catching people talking about things they probably shouldn't... "
    " Just doing your job as a good teacher. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, it's time for your class. "
    " You then walked to your classroom so that you could start teaching. "
    pause 2.0
    jump tthursmcclass
label tthursmcclass:
    scene gardenroom with dissolve
    " You walked into your classroom and found that your students were already there. "
    " Huh. Looks like you're the one who's late this time... "
    " Not that you were complaining though. "
    " You're actually pretty happy that they arrived early. "
    " You used to kinda come to class just a few minutes late back in your days... "
    " But that's all in the past now cause you have a job, of course. "
    " You then went infront of the class to start your lesson for the day... "
    scene black with dissolve
    " You spent the rest of class hours teaching your class about...well, gardening. "
    " Suprisingly, some of them noticed that you were looking down. "
    " Was you looking upset really that obvious? "
    " I mean, you DID try to act like your normal self. "
    " Guess that there was something that just felt so fake about it. "
    " Nonetheless, you're impressed that they actually noticed. "
    " And cared to notice, too. "
    " They told you to get better soon. "
    " What nice students you have.. "
    play sound "audio/bellring.mp3"
    " The bell rings, ending your time for your class. "
    " You watched the students go out before you went out to the hallways as well. "
    pause 2.0
    jump tthursbreak5
label tthursbreak5:
    scene hallway with dissolve
    " You walked into the hallway and noticed that a few students were talking about some sort of drama... "
    " Drama going on between students. "
    " Being the nosy teacher you are, you decided to listen in for more information. "
    " You also kinda had to pretend that you weren't listening in... "
    " By pretending you had something important to do in your phone and texting someone. "
    " Totally not listening at all. "
    " From what you've heard, the drama was between two popular girls. "
    " They were apparently best friends. "
    " Wow, that's a bit shocking. Best friends arguing? "
    " This is getting a little interesting... "
    " You need to listen more though. "
    " As you listened, turns out... "
    " They kind of do this every now and then. "
    " But they've never really gone too far to the point they were cursing at eachother. "
    " Is that how bad the situation is? "
    " If things are gonna get worse, you're going to have to call Miss Grace... "
    " You don't want anyone to fight, after all. "
    " For now, things seem a little tame. "
    " After all, it's just insults for now. "
    " Not fighting as in...actual fighting. "
    " You're going to have to see if things get worse later. "
    scene black with dissolve
    " You spent the rest of hthe break hanging out in the hallways. "
    " Doing nothing important, really. "
    " But you were also making sure no one decides to pick a fight with anyone. "
    " That would've been bad...but you also wanna know what that means? "
    " Principal's office! in case if they do fight! "
    " You knew Miss Grace would just leave them off in a warning, but that just gives more of a highschool experience, honestly. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for another class. "
    " You then started to walk around to see if anyone needed help. "
    pause 2.0
    jump tthursclass5
label tthursclass5:
    scene hallway with dissolve
    " Who would you like to help for this break? "
    if demiknow,emilyknow,circleknow == True:
        menu:
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump skybeefbeef
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump skygeefgeef
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump skyteefteef
    elif demiknow,emilyknow == True and circleknow == False:
        menu:
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump skybeefbeef
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump skygeefgeef
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump skyteefteef
    elif demiknow,circleknow == True and emilyknow == False:
        menu:
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump skybeefbeef
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump skygeefgeef
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump skyteefteef
    elif emilyknow,circleknow == True and demiknow == False:
        menu:
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump skybeefbeef
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump skygeefgeef
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump skyteefteef
    elif demiknow == True and emilyknow,circleknow == False:
        menu:
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump skybeefbeef
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump skygeefgeef
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump skyteefteef
    elif emilyknow == True and demiknow,circleknow == False:
        menu:
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump skybeefbeef
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump skygeefgeef
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump skyteefteef
    elif circleknow == True and demiknow,emilyknow == False:
        menu:
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump skybeefbeef
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump skygeefgeef
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump skyteefteef
    else:
        menu:
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump skybeefbeef
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump skygeefgeef
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump skyteefteef
    label skybeefbeef:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom and surprise surprise, they weren't doing anything important. "
        " Like with the other teachers, the students are busy doing something else. "
        " Something else that isn't taking down notes from the screen or talking. "
        " They were just there and discussing things for their projects. "
        " Projects that you don't really care about since you were here for the teacher. "
        " You looked around and eventually found the music teacher looking at something on the ceiling. "
        " Wonder what that's about... "
        " You walked over to him so that you could have a better look. "
        show mrdemineutral at center with easeinleft
        if demiknow == True:
            " You greeted him before asking him what he was looking at. "
            " The ceiling looked fine to you, so you don't know what he really was looking at. "
            " Maybe there was something that you couldn't see? "
            " Or you're just blind and you should probably get glasses. "
            msd " Oh - [name]...! "
            msd " I'm so glad that you're here... "
            msd " But, um... "
            msd " To answer your question... "
            msd " I've been kind of noticing that whenever it rains... "
            msd " This part of the classroom starts dripping a little... "
            msd " O-of course it's not a lot - but there have been a lot of times that my students have complained about it... "
            msd " So, um...right now... "
            msd " I'm trying to figure out how to fix this... "
            msd " Without bothering the other teachers, of course... "
            msd " I'd hate being a bother to them... "
            msd " I hope I'm not bothering you... "
            " You reassured him that he wasn't bothering you at all. "
            " You then thought of how you could help Mister Demi in this situation... "
            " ...You had a few ideas, let's hear one of them. "
            menu:
                " tape. ":
                    $ demilv += 5
                    msd " W...what's that you said...? "
                    msd " ...Tape...? "
                    msd " Are you sure that's going to work...? "
                    msd " N-not that I don't trust you or anything, but what if the tape falls..? "
                    msd " I know that the water isn't even that bad, but still... "
                    msd " Eerh...you know what, I'll trust you on this one... "
                    " You reached into your pocket and magically got some tape. "
                    " Some magical pocket tape could never hurt! "
                    " You then used a chair so that you could get on it and put the tape on the ceiling. "
                    " That should hold it up long enough until they get a good replacement to stop the dripping. "
                    " You then put the chair back to it's original place and you gave Mister Demi a thumbs up. "
                    msd " T-thanks, [name]... "
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " Your help is always appreciated... "
                    msd " Don't forget that, okay...? "
                    msd " We really enjoy your company around here... "
                    msd " By we, uh...I mean me and the other teachers... "
                    msd " I, um...hope to hang out with you more soon...! "
                    msd " Oh uh, um... "
                    msd " We could also hang out here for a bit if you want...? "
                    msd " I don't want to force you or anything, so... "
                    msd " Um...your choice if you wanna hang out with me or not? "
                    " Well, the programmer isn't adding more line of dialogue for this. "
                    " You gave him a thumbs up as a sign that you were gonna stay here for the break. "
                    msd " That's great, [name]...! "
                    msd " Well, um... we could hang out at my desk? "
                    msd " It's over here... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Mister Demi. "
                    " Talking about the kinds of music that you two enjoy... "
                    " Both of you were pretty much fine with anything as long as it sounds like a banger. "
                    " If it's not a banger? "
                    " Just ignore it and put the next song on. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak6
                " put a bucket under the spot temporarily ":
                    $ demilv += 10
                    msd " Hmm, yeah... "
                    msd " That sounds like a reasonable thing to do... "
                    msd " ...We can just keep it there until I actually get something that could stop the dripping... "
                    msd " Now I feel a little stupid for not thinking of that in the first place... "
                    msd " Wait, where are we even gonna get a bucket...??? "
                    " You thought long and hard. "
                    " Where would there be a bucket in this school? "
                    " A bucket that hasn't been used in a long time, specifically. "
                    " You don't wanna use a bucket that people have been using a lot. "
                    " What if someone needed that? "
                    " Hmm... "
                    " You then remembered that there were some old buckets in the janitor's closet. "
                    msd " Oh! the janitor's closet? "
                    msd " I'll go ahead and get the bucket for you... "
                    msd " Don't want to tire you out, since the janitor's closet is a bit far from this classroom... "
                    msd " Stay right here, okay? "
                    hide mrdemineutral at right with easeoutright
                    " Mister Demi gets out of the classroom to get the buckets. "
                    " While you were waiting, you decided to look around the classroom. "
                    " A lot of different musical instruments that you didn't recognize... "
                    " And also a lot of musical decorations here and there. "
                    " Pretty nice, really fits the description of an average music classroom. "
                    " Mister Demi then comes back into the classroom, with one of the old buckets. "
                    show mrdemineutral at center with easeinright
                    msd " Here we are... "
                    " Mister Demi then put the bucket underneath the spot he was talking about earlier. "
                    msd " T-thanks for the idea, [name]... "
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " Your help is always appreciated... "
                    msd " Don't forget that, okay...? "
                    msd " We really enjoy your company around here... "
                    msd " By we, uh...I mean me and the other teachers... "
                    msd " I, um...hope to hang out with you more soon...! "
                    msd " Oh uh, um... "
                    msd " We could also hang out here for a bit if you want...? "
                    msd " I don't want to force you or anything, so... "
                    msd " Um...your choice if you wanna hang out with me or not? "
                    " Well, the programmer isn't adding more line of dialogue for this. "
                    " You gave him a thumbs up as a sign that you were gonna stay here for the break. "
                    msd " That's great, [name]...! "
                    msd " Well, um... we could hang out at my desk? "
                    msd " It's over here... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Mister Demi. "
                    " Talking about the kinds of music that you two enjoy... "
                    " Both of you were pretty much fine with anything as long as it sounds like a banger. "
                    " If it's not a banger? "
                    " Just ignore it and put the next song on. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak6
        else:
            " You greeted him before asking him what he was looking at. "
            " The ceiling looked fine to you, so you don't know what he really was looking at. "
            " Maybe there was something that you couldn't see? "
            " Or you're just blind and you should probably get glasses. "
            x " Oh - [name]...! "
            x " I'm so glad that you're here... "
            x " Wait...I haven't even introduced myself to you yet... "
            x " I'm sorry about that... "
            $ demiknow = True
            msd " I'm Mister Demi - the music teacher... "
            msd " And, um... "
            msd " To answer your question... "
            msd " I've been kind of noticing that whenever it rains... "
            msd " This part of the classroom starts dripping a little... "
            msd " O-of course it's not a lot - but there have been a lot of times that my students have complained about it... "
            msd " So, um...right now... "
            msd " I'm trying to figure out how to fix this... "
            msd " Without bothering the other teachers, of course... "
            msd " I'd hate being a bother to them... "
            msd " I hope I'm not bothering you... "
            " You reassured him that he wasn't bothering you at all. "
            " You then thought of how you could help Mister Demi in this situation... "
            " ...You had a few ideas, let's hear one of them. "
            menu:
                " tape. ":
                    $ demilv += 5
                    msd " W...what's that you said...? "
                    msd " ...Tape...? "
                    msd " Are you sure that's going to work...? "
                    msd " N-not that I don't trust you or anything, but what if the tape falls..? "
                    msd " I know that the water isn't even that bad, but still... "
                    msd " Eerh...you know what, I'll trust you on this one... "
                    " You reached into your pocket and magically got some tape. "
                    " Some magical pocket tape could never hurt! "
                    " You then used a chair so that you could get on it and put the tape on the ceiling. "
                    " That should hold it up long enough until they get a good replacement to stop the dripping. "
                    " You then put the chair back to it's original place and you gave Mister Demi a thumbs up. "
                    msd " T-thanks, [name]... "
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " Your help is always appreciated... "
                    msd " Don't forget that, okay...? "
                    msd " We really enjoy your company around here... "
                    msd " By we, uh...I mean me and the other teachers... "
                    msd " I, um...hope to hang out with you more soon...! "
                    msd " Oh uh, um... "
                    msd " We could also hang out here for a bit if you want...? "
                    msd " I don't want to force you or anything, so... "
                    msd " Um...your choice if you wanna hang out with me or not? "
                    " Well, the programmer isn't adding more line of dialogue for this. "
                    " You gave him a thumbs up as a sign that you were gonna stay here for the break. "
                    msd " That's great, [name]...! "
                    msd " Well, um... we could hang out at my desk? "
                    msd " It's over here... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Mister Demi. "
                    " Talking about the kinds of music that you two enjoy... "
                    " Both of you were pretty much fine with anything as long as it sounds like a banger. "
                    " If it's not a banger? "
                    " Just ignore it and put the next song on. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak6
                " put a bucket under the spot temporarily ":
                    $ demilv += 10
                    msd " Hmm, yeah... "
                    msd " That sounds like a reasonable thing to do... "
                    msd " ...We can just keep it there until I actually get something that could stop the dripping... "
                    msd " Now I feel a little stupid for not thinking of that in the first place... "
                    msd " Wait, where are we even gonna get a bucket...??? "
                    " You thought long and hard. "
                    " Where would there be a bucket in this school? "
                    " A bucket that hasn't been used in a long time, specifically. "
                    " You don't wanna use a bucket that people have been using a lot. "
                    " What if someone needed that? "
                    " Hmm... "
                    " You then remembered that there were some old buckets in the janitor's closet. "
                    msd " Oh! the janitor's closet? "
                    msd " I'll go ahead and get the bucket for you... "
                    msd " Don't want to tire you out, since the janitor's closet is a bit far from this classroom... "
                    msd " Stay right here, okay? "
                    hide mrdemineutral at right with easeoutright
                    " Mister Demi gets out of the classroom to get the buckets. "
                    " While you were waiting, you decided to look around the classroom. "
                    " A lot of different musical instruments that you didn't recognize... "
                    " And also a lot of musical decorations here and there. "
                    " Pretty nice, really fits the description of an average music classroom. "
                    " Mister Demi then comes back into the classroom, with one of the old buckets. "
                    show mrdemineutral at center with easeinright
                    msd " Here we are... "
                    " Mister Demi then put the bucket underneath the spot he was talking about earlier. "
                    msd " T-thanks for the idea, [name]... "
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " Your help is always appreciated... "
                    msd " Don't forget that, okay...? "
                    msd " We really enjoy your company around here... "
                    msd " By we, uh...I mean me and the other teachers... "
                    msd " I, um...hope to hang out with you more soon...! "
                    msd " Oh uh, um... "
                    msd " We could also hang out here for a bit if you want...? "
                    msd " I don't want to force you or anything, so... "
                    msd " Um...your choice if you wanna hang out with me or not? "
                    " Well, the programmer isn't adding more line of dialogue for this. "
                    " You gave him a thumbs up as a sign that you were gonna stay here for the break. "
                    msd " That's great, [name]...! "
                    msd " Well, um... we could hang out at my desk? "
                    msd " It's over here... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Mister Demi. "
                    " Talking about the kinds of music that you two enjoy... "
                    " Both of you were pretty much fine with anything as long as it sounds like a banger. "
                    " If it's not a banger? "
                    " Just ignore it and put the next song on. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak6
    label skygeefgeef:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom and prayed that nothing important is going on... "
        " And surprise surprise, they weren't doing anything important. "
        " They were just mainly talking about a project they were supposed to be doing... "
        " A project about history of course. "
        " This IS history class. "
        " You looked around and found the history teacher doing things on her laptop. "
        " Wondering what she's doing on there, you walked over to her. "
        " Let's see what she's looking at... "
        show msemilyneutral at center with easeinleft
        if emilyknow == True:
            mse " Oh geez... "
            mse " This student's grades aren't doing the best... "
            mse " I should give them a +10 so save them a little bit... "
            mse " I feel nice today, hmhm... "
            " She types for a bit in her laptop, not knowing you were there yet. "
            " After she was done typing for a bit, she finally noticed you. "
            " You then greeted her politely and asked what she was doing. "
            mse " [name]!! nice to see you!! "
            mse " I was just doing the grades for some of the students... "
            mse " And gee, let me tell you...some of them were failing. "
            hide msemilyneutral at bottom
            show msemilysad at center
            mse " I don't know what I've been doing wrong, but... "
            mse " They've been failing more this quarter... "
            mse " And I don't really like that...students failing is basically a teacher's nightmare. "
            mse " Well, for me, atleast. "
            mse " I hate seeing my students fail! "
            mse " Should I throw in another project for them to do...? "
            mse " But what should I even do..? "
            mse " I think I've done all the ideas that I could... "
            hide msemilysad at bottom
            show msemilyneutral at center
            mse " Do you have any ideas though? "
            mse " I'm sure you've got some ideas there in your mind! "
            mse " Don't worry, I think no idea is stupid! "
            mse " Let me hear some of your ideas... "
            menu:
                " Make them draw something history related ":
                    $ emilylv += 5
                    mse " Oooh, oh! "
                    mse " Yeah, I could do that! "
                    mse " I haven't actually thought of this yet, surprisingly... "
                    mse " I'll put that in my to-do list! "
                    mse " Lemme just write that down... "
                    " Miss Emily writes your idea down in a notebook. "
                    " It seems like her book is filled with ideas... "
                    " Most of them are crossed out, meaning that they're already done. "
                    " And some are given question marks, meaning that they're being worked on. "
                    " And there's some that were completely erased - you could see bits of it... "
                    " Probably for ideas that never really pleased Miss Emily. "
                    " She finishes writing down your idea and looks like she made the activity to be worth 60 points. "
                    mse " 60 points would be good enough to save them, right? "
                    mse " I'm gonna get a little bit concerned if they don't answer it though... "
                    mse " But then again, students can still pass something late... "
                    mse " I'll just give them a 38 if they manage to pass it late. "
                    mse " I just don't want my students to fail, you know? "
                    mse " It would really upset me if I saw them fail... "
                    mse " That would just show how bad of a teacher I am! "
                    mse " And I don't want to be seen as a bad teacher.. "
                    mse " Hmhmmm... "
                    mse " Hey [name], how about you help me grade for a bit? "
                    mse " Just look at the papers over here and tell me what score they got. "
                    mse " Then I'll put them in this grading thingy that we teachers use... "
                    mse " Simple enough task to do, right? "
                    " You don't really have a choice in this... "
                    " You agreed in helping Miss Emily grade just for a bit. "
                    mse " Thanks, I appreciate it! "
                    mse " Just go ahead and grab a seat next to me... "
                    mse " I don't want you to be standing all the time, after all! "
                    mse " Come here... "
                    scene black with dissolve
                    " You spent the rest of class hours helping Miss Emily. "
                    " While you were helping her, you saw one student who somehow got a 10/50. "
                    " This one was definitely going to do that idea you had. "
                    " There's no way they're going home with that low of a score... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak6
                " Make them make a essay ":
                    $ emilylv += 5
                    mse " Oooh, oh! "
                    mse " Yeah, I could do that! "
                    mse " I haven't actually thought of this yet, surprisingly... "
                    mse " I'll put that in my to-do list! "
                    mse " Lemme just write that down... "
                    " Miss Emily writes your idea down in a notebook. "
                    " It seems like her book is filled with ideas... "
                    " Most of them are crossed out, meaning that they're already done. "
                    " And some are given question marks, meaning that they're being worked on. "
                    " And there's some that were completely erased - you could see bits of it... "
                    " Probably for ideas that never really pleased Miss Emily. "
                    " She finishes writing down your idea and looks like she made the activity to be worth 60 points. "
                    mse " 60 points would be good enough to save them, right? "
                    mse " I'm gonna get a little bit concerned if they don't answer it though... "
                    mse " But then again, students can still pass something late... "
                    mse " I'll just give them a 38 if they manage to pass it late. "
                    mse " I just don't want my students to fail, you know? "
                    mse " It would really upset me if I saw them fail... "
                    mse " That would just show how bad of a teacher I am! "
                    mse " And I don't want to be seen as a bad teacher.. "
                    mse " Hmhmmm... "
                    mse " Hey [name], how about you help me grade for a bit? "
                    mse " Just look at the papers over here and tell me what score they got. "
                    mse " Then I'll put them in this grading thingy that we teachers use... "
                    mse " Simple enough task to do, right? "
                    " You don't really have a choice in this... "
                    " You agreed in helping Miss Emily grade just for a bit. "
                    mse " Thanks, I appreciate it! "
                    mse " Just go ahead and grab a seat next to me... "
                    mse " I don't want you to be standing all the time, after all! "
                    mse " Come here... "
                    scene black with dissolve
                    " You spent the rest of class hours helping Miss Emily. "
                    " While you were helping her, you saw one student who somehow got a 10/50. "
                    " This one was definitely going to do that idea you had. "
                    " There's no way they're going home with that low of a score... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak6
        else:
            x " Oh geez... "
            x " This student's grades aren't doing the best... "
            x " I should give them a +10 so save them a little bit... "
            x " I feel nice today, hmhm... "
            " She types for a bit in her laptop, not knowing you were there yet. "
            " After she was done typing for a bit, she finally noticed you. "
            " You then greeted her politely and asked what she was doing. "
            x " [name]!! nice to see you!! "
            x " Ooo, wait... "
            x " I have a feeling I haven't introduced myself to you yet! "
            x " Lemme do that right now, sorry... "
            $ emilyknow = True
            mse " I'm Miss Emily! the history teacher! and about your question... "
            mse " I was just doing the grades for some of the students... "
            mse " And gee, let me tell you...some of them were failing. "
            hide msemilyneutral at bottom
            show msemilysad at center
            mse " I don't know what I've been doing wrong, but... "
            mse " They've been failing more this quarter... "
            mse " And I don't really like that...students failing is basically a teacher's nightmare. "
            mse " Well, for me, atleast. "
            mse " I hate seeing my students fail! "
            mse " Should I throw in another project for them to do...? "
            mse " But what should I even do..? "
            mse " I think I've done all the ideas that I could... "
            hide msemilysad at bottom
            show msemilyneutral at center
            mse " Do you have any ideas though? "
            mse " I'm sure you've got some ideas there in your mind! "
            mse " Don't worry, I think no idea is stupid! "
            mse " Let me hear some of your ideas... "
            menu:
                " Make them draw something history related ":
                    $ emilylv += 5
                    mse " Oooh, oh! "
                    mse " Yeah, I could do that! "
                    mse " I haven't actually thought of this yet, surprisingly... "
                    mse " I'll put that in my to-do list! "
                    mse " Lemme just write that down... "
                    " Miss Emily writes your idea down in a notebook. "
                    " It seems like her book is filled with ideas... "
                    " Most of them are crossed out, meaning that they're already done. "
                    " And some are given question marks, meaning that they're being worked on. "
                    " And there's some that were completely erased - you could see bits of it... "
                    " Probably for ideas that never really pleased Miss Emily. "
                    " She finishes writing down your idea and looks like she made the activity to be worth 60 points. "
                    mse " 60 points would be good enough to save them, right? "
                    mse " I'm gonna get a little bit concerned if they don't answer it though... "
                    mse " But then again, students can still pass something late... "
                    mse " I'll just give them a 38 if they manage to pass it late. "
                    mse " I just don't want my students to fail, you know? "
                    mse " It would really upset me if I saw them fail... "
                    mse " That would just show how bad of a teacher I am! "
                    mse " And I don't want to be seen as a bad teacher.. "
                    mse " Hmhmmm... "
                    mse " Hey [name], how about you help me grade for a bit? "
                    mse " Just look at the papers over here and tell me what score they got. "
                    mse " Then I'll put them in this grading thingy that we teachers use... "
                    mse " Simple enough task to do, right? "
                    " You don't really have a choice in this... "
                    " You agreed in helping Miss Emily grade just for a bit. "
                    mse " Thanks, I appreciate it! "
                    mse " Just go ahead and grab a seat next to me... "
                    mse " I don't want you to be standing all the time, after all! "
                    mse " Come here... "
                    scene black with dissolve
                    " You spent the rest of class hours helping Miss Emily. "
                    " While you were helping her, you saw one student who somehow got a 10/50. "
                    " This one was definitely going to do that idea you had. "
                    " There's no way they're going home with that low of a score... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak6
                " Make them make a essay ":
                    $ emilylv += 5
                    mse " Oooh, oh! "
                    mse " Yeah, I could do that! "
                    mse " I haven't actually thought of this yet, surprisingly... "
                    mse " I'll put that in my to-do list! "
                    mse " Lemme just write that down... "
                    " Miss Emily writes your idea down in a notebook. "
                    " It seems like her book is filled with ideas... "
                    " Most of them are crossed out, meaning that they're already done. "
                    " And some are given question marks, meaning that they're being worked on. "
                    " And there's some that were completely erased - you could see bits of it... "
                    " Probably for ideas that never really pleased Miss Emily. "
                    " She finishes writing down your idea and looks like she made the activity to be worth 60 points. "
                    mse " 60 points would be good enough to save them, right? "
                    mse " I'm gonna get a little bit concerned if they don't answer it though... "
                    mse " But then again, students can still pass something late... "
                    mse " I'll just give them a 38 if they manage to pass it late. "
                    mse " I just don't want my students to fail, you know? "
                    mse " It would really upset me if I saw them fail... "
                    mse " That would just show how bad of a teacher I am! "
                    mse " And I don't want to be seen as a bad teacher.. "
                    mse " Hmhmmm... "
                    mse " Hey [name], how about you help me grade for a bit? "
                    mse " Just look at the papers over here and tell me what score they got. "
                    mse " Then I'll put them in this grading thingy that we teachers use... "
                    mse " Simple enough task to do, right? "
                    " You don't really have a choice in this... "
                    " You agreed in helping Miss Emily grade just for a bit. "
                    mse " Thanks, I appreciate it! "
                    mse " Just go ahead and grab a seat next to me... "
                    mse " I don't want you to be standing all the time, after all! "
                    mse " Come here... "
                    scene black with dissolve
                    " You spent the rest of class hours helping Miss Emily. "
                    " While you were helping her, you saw one student who somehow got a 10/50. "
                    " This one was definitely going to do that idea you had. "
                    " There's no way they're going home with that low of a score... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another break. "
                    " You waited for everyone else to get out of the classroom before you did. "
                    pause 2.0
                    jump tthursbreak6
    label skyteefteef:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom and looked around in case if the students were doing anything important. "
        " And surprise surprise, they weren't. "
        " I mean, they were answering an activity... "
        " It's important to them, but not really for the teachers. "
        " And you're a teacher, so you don't really care. "
        " You looked around everywhere and found the math teacher hanging out at her desk. "
        " Eating some oreos...maybe you could ask for some if you're lucky enough. "
        show misscircleneutral at center with easeinleft
        if circleknow == True:
            $ circlelv += 5
            msc " Heya there, [name]! "
            msc " I know you're eyeing at my oreos, don't lie. "
            msc " Annnnd...sorry, I don't really share. "
            msc " You could have some of my other snacks though! "
            msc " Here, it's in this snack drawer right here... "
            msc " This is actually my snack drawer to reward students if they did good enough. "
            msc " Surprisingly, this actually works to get them motivated to work. "
            msc " I guess snacks can really work on people to get them to be motivated? "
            msc " Some students DID tell me that I chose the good snacks... "
            msc " Pretty sure that's a thing I should be happy about. "
            msc " If I got the good snacks, then that means I got the right stuff for the kids, right? "
            msc " And if I got the right stuff for the kids... "
            msc " That means they'll focus more on the lesson, riiight? "
            msc " Hmhmmm...never knew that I just needed snacks to get them to lock in! "
            msc " Did I...use that word right? "
            msc " Lock in? "
            msc " Okay, I probably didn't, but I don't care. "
            msc " I'm too busy being happy over this new found information! "
            msc " Heeeyy...you wanna hang out with me for a bit? "
            msc " Since we're just going to be here doing nothing considering the fact I'm letting my students discuss for once. "
            msc " We could also go and shit talk about our own students... "
            msc " Because trust me, I have a lot of stories to tell you! "
            msc " You wanna hear 'em or nah? "
            " Who could say no to a little drama? "
            " Besides, you needed something interesting for your day. "
            msc " Great! "
            msc " Just sit a little closer to me - I don't want the students listneing in. "
            scene black with dissolve
            " You spent the rest of class hours listening to Miss Circle talk about her students. "
            " And god damn, she really did have some interesting stories. "
            " What do you mean one of her students willingly picked up a snake and got bit twice by it? "
            " I mean, atleast that kid is okay, but jesus christ. "
            " Honestly pretty wild to hear that. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tthursbreak6
        else:
            x " Heya there, [name]! "
            $ circleknow = True
            msc " Oh - before you say anything...I'm Miss Circle - math teacher.... "
            msc " I know you're eyeing at my oreos, don't lie. "
            msc " Annnnd...sorry, I don't really share. "
            msc " You could have some of my other snacks though! "
            msc " Here, it's in this snack drawer right here... "
            msc " This is actually my snack drawer to reward students if they did good enough. "
            msc " Surprisingly, this actually works to get them motivated to work. "
            msc " I guess snacks can really work on people to get them to be motivated? "
            msc " Some students DID tell me that I chose the good snacks... "
            msc " Pretty sure that's a thing I should be happy about. "
            msc " If I got the good snacks, then that means I got the right stuff for the kids, right? "
            msc " And if I got the right stuff for the kids... "
            msc " That means they'll focus more on the lesson, riiight? "
            msc " Hmhmmm...never knew that I just needed snacks to get them to lock in! "
            msc " Did I...use that word right? "
            msc " Lock in? "
            msc " Okay, I probably didn't, but I don't care. "
            msc " I'm too busy being happy over this new found information! "
            msc " Heeeyy...you wanna hang out with me for a bit? "
            msc " Since we're just going to be here doing nothing considering the fact I'm letting my students discuss for once. "
            msc " We could also go and shit talk about our own students... "
            msc " Because trust me, I have a lot of stories to tell you! "
            msc " You wanna hear 'em or nah? "
            " Who could say no to a little drama? "
            " Besides, you needed something interesting for your day. "
            msc " Great! "
            msc " Just sit a little closer to me - I don't want the students listneing in. "
            scene black with dissolve
            " You spent the rest of class hours listening to Miss Circle talk about her students. "
            " And god damn, she really did have some interesting stories. "
            " What do you mean one of her students willingly picked up a snake and got bit twice by it? "
            " I mean, atleast that kid is okay, but jesus christ. "
            " Honestly pretty wild to hear that. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tthursbreak6
label tthursbreak6:
    scene hallway with dissolve
    " Huh. "
    " It's already the last break of the day. "
    " Didn't know that time could fly by so fast... "
    " You didn't really know what to do for the rest of the break now that you're here. "
    " Actually, you DO remember seeing this one door before... "
    " Had this creepy vibe to it - "
    " The walls near the door had strange scratch marks on them. "
    " You were warned not to check it out, but you were starting to get curious. "
    " Should you check the door out? "
    menu:
        " Yeah lol ":
            " You opened the door... "
            " Huh, looks like you were seeing something unexpected. "
            " A whole line of code... "
            " You saw a whole lot of it before the room eventually turned pitch black. "
            " Aaaannd then gave you an error screen. "
            " Looks like the game didn't know what to put there. "
            " Or, you were seeing something you weren't supposed to. "
            " Yeah, maybe that option right there. "
            " You close the door - you didn't want anyone to see what you just did. "
            " People would probably throw rumors about you if they saw. "
            " Aaaannnd that was going to lead to a visit to ms. principal herself. "
            " You don't wanna get in trouble in the first week you have, dude... "
            " You then walked around school pretending like you didn't do anything wrong. "
            " Yeah, just walking around... "
            " Totally didn't open that door right there... "
            scene black with dissolve
            " You spent the rest of the break walking around the school. "
            " You had a feeling someone saw you open that door... "
            " And you were praying a whole lot that they won't spread rumors about you. "
            " And make fun of you for opening the door for some reason. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for you to help someone. "
            " You started looking around to see who you could help... "
            pause 2.0
            jump tthursclass6
        " Nah ":
            " Wise choice. "
            " Now, let's walk around... "
            scene black with dissolve
            " You spent the rest of the break walking around the school. "
            " You had a feeling someone was looking at you staring at that door... "
            " Hopefully they didn't get the wrong idea. "
            " Because you thought if someone saw you opening that door, they'd probably think: "
            " 'Ew why is that weirdo of a teacher looking into that door?' "
            " '[they] know[s] [they] aren't supposed to lmao' "
            " Weirdo stinky... "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for you to help someone. "
            " You started looking around to see who you could help... "
            pause 2.0
            jump tthursclass6
label tthursclass6:
    scene hallway with dissolve
    " Who do you wanna help for this break? "
    if thavelknow,sashaknow,bloomieknow == True:
        menu:
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump hikariarcaea
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump tairitsuarcaea
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump arcaeafunny
    elif thavelknow,sashaknow == True and bloomieknow == False:
        menu:
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump hikariarcaea
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump tairitsuarcaea
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump arcaeafunny
    elif thavelknow,bloomieknow == True and sashaknow == False:
        menu:
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump hikariarcaea
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump tairitsuarcaea
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump arcaeafunny
    elif sashaknow,bloomieknow == True and thavelknow == False:
        menu:
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump hikariarcaea
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump tairitsuarcaea
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump arcaeafunny
    elif thavelknow == True and sashaknow,bloomieknow == False:
        menu:
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump hikariarcaea
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump tairitsuarcaea
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump arcaeafunny
    elif sashaknow == True and thavelknow,bloomieknow == False:
        menu:
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump hikariarcaea
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump tairitsuarcaea
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump arcaeafunny
    elif bloomieknow == True and thavelknow,sashaknow == False:
        menu:
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump hikariarcaea
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump tairitsuarcaea
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump arcaeafunny
    else:
        menu:
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump hikariarcaea
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump tairitsuarcaea
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump arcaeafunny
    label hikariarcaea:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom and guess what... "
        " They aren't doing important once again. "
        " Though you did notice that the different students were doing another project. "
        " The same project that the other students were doing earlier... "
        " Hm. Teacher stuff, you see. "
        " You then looked around to try and find the teacher... "
        " And eventually spot her putting on some posters. "
        " Wondering what that was, you walked over to her to ask her what she was doing. "
        show msthravelneutral at center with easeinleft
        if thavelknow == True:
            " You greeted her politely and asked her what she was doing. "
            mst " Oh hey there, [name]! "
            mst " I was just putting up some posters for my little contest... "
            mst " My little contest that Miss Grace herself allowed, of course! "
            mst " Don't want to be rude and not ask for permission to do this stuff first. "
            mst " Anyway, I'm sure you wanna know more about my contest, so - "
            mst " This contest is where students will show off how much they know about a certain country and it's language! "
            mst " Pretty basic, I know... "
            mst " But I added some trick questions in there to spice it up! "
            mst " Just to REALLY test their knowledge. "
            mst " I know people won't really play this, but I'll atleast try to advertise! "
            mst " Oh, and the prize? "
            mst " About 10 snacks and 100$. "
            mst " I know it doesn't seem like a lot to SOME, "
            mst " But hey - if people are gonna be picky like that, maybe just don't participate if you're not interested? "
            mst " Better than hearing all of your complaining, really. "
            mst " I have better things to do than listen to all of that yapping. "
            mst " I know some students are probably gonna guess their answers... "
            mst " But, uh... "
            mst " Look, I really need to get rid of this money and these snacks. "
            mst " I kind of bought too many snacks earlier and uh. "
            mst " Yeah. "
            mst " And I don't really know what to use this money for, so uhhh... "
            mst " Anyway - could you help me put these around the school? "
            mst " I still gotta manage the class somehow, so... "
            mst " Could you? Could you help me? "
            " Guess what I'm gonna say here. "
            " You don't really have any choice here. "
            " Plus points for you if you got it right. "
            " You agreed to helping Miss Thavel with her little project. "
            mst " That's great! "
            mst " Here, take these. "
            " You took some of the posters Miss Thavel handed you and went off to put them on the walls. "
            " Time to go and get posting those posters...or whatever. "
            scene black with dissolve
            " You spent the rest of the class hours helping Miss Thavel put some posters on the walls. "
            " As you were looking at them, you thought that the posters were pretty well designed. "
            " Credits to whoever designed them, god damn. "
            " Too bad that I can't really show you what it looks like. "
            " Cause of, you know...budget. "
            " And the artist doesn't want to suffer more. "
            play sound "aduio/bellring.mp3"
            " The bell rings after a bit, and you're already done putting up all of the posters... "
            " You're also already in the hallways, so...wait, hold on. "
            " This is literally the last class of the day. "
            " Meaning that you can go home now. Let's go and pack your things... "
            pause 2.0
            jump tthursmcgohome
        else:
            " You greeted her politely and asked her what she was doing. "
            x " Oh hey there, [name]! "
            $ thavelknow = True
            mst " Uh - before you say anything else, I'm Miss Thavel, the language teacher. "
            mst " I was just putting up some posters for my little contest... "
            mst " My little contest that Miss Grace herself allowed, of course! "
            mst " Don't want to be rude and not ask for permission to do this stuff first. "
            mst " Anyway, I'm sure you wanna know more about my contest, so - "
            mst " This contest is where students will show off how much they know about a certain country and it's language! "
            mst " Pretty basic, I know... "
            mst " But I added some trick questions in there to spice it up! "
            mst " Just to REALLY test their knowledge. "
            mst " I know people won't really play this, but I'll atleast try to advertise! "
            mst " Oh, and the prize? "
            mst " About 10 snacks and 100$. "
            mst " I know it doesn't seem like a lot to SOME, "
            mst " But hey - if people are gonna be picky like that, maybe just don't participate if you're not interested? "
            mst " Better than hearing all of your complaining, really. "
            mst " I have better things to do than listen to all of that yapping. "
            mst " I know some students are probably gonna guess their answers... "
            mst " But, uh... "
            mst " Look, I really need to get rid of this money and these snacks. "
            mst " I kind of bought too many snacks earlier and uh. "
            mst " Yeah. "
            mst " And I don't really know what to use this money for, so uhhh... "
            mst " Anyway - could you help me put these around the school? "
            mst " I still gotta manage the class somehow, so... "
            mst " Could you? Could you help me? "
            " Guess what I'm gonna say here. "
            " You don't really have any choice here. "
            " Plus points for you if you got it right. "
            " You agreed to helping Miss Thavel with her little project. "
            mst " That's great! "
            mst " Here, take these. "
            " You took some of the posters Miss Thavel handed you and went off to put them on the walls. "
            " Time to go and get posting those posters...or whatever. "
            scene black with dissolve
            " You spent the rest of the class hours helping Miss Thavel put some posters on the walls. "
            " As you were looking at them, you thought that the posters were pretty well designed. "
            " Credits to whoever designed them, god damn. "
            " Too bad that I can't really show you what it looks like. "
            " Cause of, you know...budget. "
            " And the artist doesn't want to suffer more. "
            play sound "aduio/bellring.mp3"
            " The bell rings after a bit, and you're already done putting up all of the posters... "
            " You're also already in the hallways, so...wait, hold on. "
            " This is literally the last class of the day. "
            " Meaning that you can go home now. Let's go and pack your things... "
            pause 2.0
            jump tthursmcgohome
    label tairitsuarcaea:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom, and guess what I'm about to say... "
        " They weren't doing anything too important for this class. "
        " Actually, they were looking at a photo on the big TV screen. "
        " And from what you could tell, they were writing their interpretations of the art. "
        " It looked pretty cool. Looked like something from the renaissance period. "
        " Huh...sometimes you wonder when you could be able to paint like that. "
        " Probably never, but with enough practice, then maybe you could. "
        " You looked around and spotted the arts teacher looking around at the other students work. "
        " You walked over to her, wanting to talk to her for a bit. "
        " A little conversation won't hurt anyone, right? "
        show sashaneutral at center with easeinleft
        if sashaknow == True:
            mss " Hey there, [name]! "
            mss " Love to see you around here, really! "
            mss " I hope your day has been going well so far! "
            mss " I'm sure you're wondering what I'm letting my students do right now... "
            mss " ...So I'm going to explain it all to you! "
            mss " Even though it's a little bit obvious on what they're doing, haha... "
            mss " I just like explaining a lot, alright? "
            mss " I don't really think that should be a problem... "
            mss " It's just what I like to do! "
            mss " Jeez, look at me... "
            mss " I'm rambling again, ahah... "
            mss " Better start explaining before I go on another one of my sessions! "
            mss " ...As my students like to call it sometimes. "
            mss " Anyway - I have this random name wheel, right? "
            mss " Really useful whenever I want to call someone randomly! "
            mss " I don't really like looking at the sheet of student's names on it, "
            mss " It makes me feel...a little indecisive on who to pick. "
            mss " So I just use a random name wheel to decide for me! "
            mss " Some people would probably call me lazy, but... I don't really care. "
            mss " Annywaaaayy...the wheel generator was different for today, obviously! "
            mss " This time, I made it so that it would pick a different type of painting for the students to interpret! "
            mss " And as you can see... "
            mss " It picked a renaissance themed painting! "
            mss " I had to go on Google so that I could get an easy looking painting... "
            mss " Annnd I found that one! "
            mss " Looks pretty easy, right? "
            " You looked at the painting that Miss Sasha had on her TV. "
            " And yeah, it looked pretty easy to explain. "
            " But then again, there could be a deeper meaning to this. "
            mss " Hmhm...what a pretty painting! "
            mss " I wonder when I'll be able to paint like that! "
            mss " I just need a little bit more practice, then I can get to that level! "
            mss " Ooor, maybe not... "
            mss " It's pretty advanced for me, now that I think about it... "
            mss " Don't you think? "
            scene black with dissolve
            " You spent the rest of class hours talking with Miss Sasha about the painting. "
            " Talking about art skills and what not... "
            " You know, the usual art class stuff. "
            play sound "audio/bellring.mp3"
            " The bell rings, and you were about to go to the hallways to hangout for a bit... "
            " But then you realized that it was really time to go home. "
            " You then walked to your classroom so that you could pack up your things. "
            pause 2.0
            jump tthursmcgohome
        else:
            x " Hey there, [name]! "
            x " Love to see you around here, really! "
            x " I hope your day has been going well so far! "
            $ sashaknow = True
            mss " Oh, uh - I'm Miss Sasha by the way! art teacher! "
            mss " I'm sure you're wondering what I'm letting my students do right now... "
            mss " ...So I'm going to explain it all to you! "
            mss " Even though it's a little bit obvious on what they're doing, haha... "
            mss " I just like explaining a lot, alright? "
            mss " I don't really think that should be a problem... "
            mss " It's just what I like to do! "
            mss " Jeez, look at me... "
            mss " I'm rambling again, ahah... "
            mss " Better start explaining before I go on another one of my sessions! "
            mss " ...As my students like to call it sometimes. "
            mss " Anyway - I have this random name wheel, right? "
            mss " Really useful whenever I want to call someone randomly! "
            mss " I don't really like looking at the sheet of student's names on it, "
            mss " It makes me feel...a little indecisive on who to pick. "
            mss " So I just use a random name wheel to decide for me! "
            mss " Some people would probably call me lazy, but... I don't really care. "
            mss " Annywaaaayy...the wheel generator was different for today, obviously! "
            mss " This time, I made it so that it would pick a different type of painting for the students to interpret! "
            mss " And as you can see... "
            mss " It picked a renaissance themed painting! "
            mss " I had to go on Google so that I could get an easy looking painting... "
            mss " Annnd I found that one! "
            mss " Looks pretty easy, right? "
            " You looked at the painting that Miss Sasha had on her TV. "
            " And yeah, it looked pretty easy to explain. "
            " But then again, there could be a deeper meaning to this. "
            mss " Hmhm...what a pretty painting! "
            mss " I wonder when I'll be able to paint like that! "
            mss " I just need a little bit more practice, then I can get to that level! "
            mss " Ooor, maybe not... "
            mss " It's pretty advanced for me, now that I think about it... "
            mss " Don't you think? "
            scene black with dissolve
            " You spent the rest of class hours talking with Miss Sasha about the painting. "
            " Talking about art skills and what not... "
            " You know, the usual art class stuff. "
            play sound "audio/bellring.mp3"
            " The bell rings, and you were about to go to the hallways to hangout for a bit... "
            " But then you realized that it was really time to go home. "
            " You then walked to your classroom so that you could pack up your things. "
            pause 2.0
            jump tthursmcgohome
    label arcaeafunny:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom and looked around to make sure they weren't doing anything important... "
        " And guess what? they weren't doing anything important! "
        " Instead, they look like they're trying to solve something. "
        " You almost forgot that math and science are also a thing together. "
        " Silly you...maybe you should go back to school. "
        " Technically you are already in school, but not really learning. "
        " Instead, you're the one teaching the students about everything you know. "
        " You looked around to try and find where the science teacher was... "
        " And you spotted her cleaning the back of her classroom. "
        " It did look pretty dusty...maybe you should help her out. "
        " Plus, it would be way faster with two people. "
        " After a bit of looking, you decided to go over and help her. "
        show missbloomieneutral at center with easeinleft
        if bloomieknow == True:
            msb " ... "
            msb " You came to help me, didn't you? "
            msb " That's honestly really nice of you, [name]... "
            msb " I was gonna say that I can do this on my own... "
            msb " But it would be faster if I had someone like you to help. "
            msb " The students keep forgetting to clean this part of the classroom when it's cleaning hours. "
            msb " Aka, the moments before school really ends. "
            msb " I don't really know how they forget to clean this part of the classroom... "
            msb " They think it looks so clean even though it's pretty dirty and has a lot of dust here and there. "
            msb " And I most certainly don't want dust on my materials... "
            msb " So, uh... "
            msb " You can go ahead and help me if you really want to. "
            msb " The brooms are in that closet over there. "
            msb " Make sure to put it back in the closet after you're done cleaning, don't forget about that. "
            msb " Sometimes my students just...leave it on tables. "
            msb " It's been getting really irritating for me. "
            " You grabbed one of the brooms from the closet and started cleaning with her. "
            " This should be fun... "
            " Atleast you're doing something and actually helping the other teacher. "
            " Instead of just hanging around and talking with them. "
            " How fun! "
            scene black with dissolve
            " You spent the rest of class hours helping Bloomie clean everything. "
            " It was very fun, for a fact. "
            " You saw a lot of old things behind certain stuff... "
            " Like a really crappy drawing of an idol behind some stuff. "
            " This person really msut've been into kpop. "
            " Too bad you weren't too interested in those types of things. "
            play sound "audio/bellring.mp3"
            " The bell rings, and you were about to go to the hallways to hangout for a bit... "
            " But then you realized that it was really time to go home. "
            " You then walked to your classroom so that you could pack up your things. "
            pause 2.0
            jump tthursmcgohome
        else:
            " You looked at her totally real ID, and... "
            " Huh, looks like her name is Miss Bloomie. Cool. "
            $ bloomieknow = True
            " Anyway, back to your regular shenanigans... "
            msb " ... "
            msb " You came to help me, didn't you? "
            msb " That's honestly really nice of you, [name]... "
            msb " I was gonna say that I can do this on my own... "
            msb " But it would be faster if I had someone like you to help. "
            msb " The students keep forgetting to clean this part of the classroom when it's cleaning hours. "
            msb " Aka, the moments before school really ends. "
            msb " I don't really know how they forget to clean this part of the classroom... "
            msb " They think it looks so clean even though it's pretty dirty and has a lot of dust here and there. "
            msb " And I most certainly don't want dust on my materials... "
            msb " So, uh... "
            msb " You can go ahead and help me if you really want to. "
            msb " The brooms are in that closet over there. "
            msb " Make sure to put it back in the closet after you're done cleaning, don't forget about that. "
            msb " Sometimes my students just...leave it on tables. "
            msb " It's been getting really irritating for me. "
            " You grabbed one of the brooms from the closet and started cleaning with her. "
            " This should be fun... "
            " Atleast you're doing something and actually helping the other teacher. "
            " Instead of just hanging around and talking with them. "
            " How fun! "
            scene black with dissolve
            " You spent the rest of class hours helping Bloomie clean everything. "
            " It was very fun, for a fact. "
            " You saw a lot of old things behind certain stuff... "
            " Like a really crappy drawing of an idol behind some stuff. "
            " This person really msut've been into kpop. "
            " Too bad you weren't too interested in those types of things. "
            play sound "audio/bellring.mp3"
            " The bell rings, and you were about to go to the hallways to hangout for a bit... "
            " But then you realized that it was really time to go home. "
            " You then walked to your classroom so that you could pack up your things. "
            pause 2.0
            jump tthursmcgohome
label tthursmcgohome:
    scene gardenroom with dissolve
    " You got your things and put it in your bag. "
    " You thought about your day today... "
    " And it was pretty calm, unlike yesterday. "
    " Guess you could say today really was better. "
    " You were hoping that tomorrow would be good too. "
    " A good day where you can just relax and have fun... "
    " Having fun and hanging out with your friends... "
    " That would be a pretty good thing to happen to you. "
    " Maybe you should schedule a hangout session with them sometime... "
    " If they're free, that is. "
    " You finished packing up your things and you went out of the school. "
    scene black with dissolve
    " Driving away to your home... "
    if circleinvite == True:
        $ circlelv += 10
        " Because you had hung out with Miss Circle... "
        " You get 10+ points! "
        " She left before it got too late though. "
        " Said she had to rest after all the oreos she ate. "
    elif thavelinvite == True:
        $ thavellv += 10
        " Because you had hung out with Miss Thavel... "
        " You get 10+ points! "
        " She left before it got too late though. "
        " She taught you a few words in a different language while she was there though! "
    elif bloomieinvite == True:
        $ bloomielv += 10
        " Because you had hung out with Miss Bloomie... "
        " You get 10+ points! "
        " She left before it got too late though. "
        " She showed you a few things she could do with science while she was there though! "
    elif emilyinvite == True:
        $ emilylv += 10
        " Because you had hung out with Miss Emily... "
        " You get 10+ points! "
        " She left before it got too late though. "
        " She taught you a few cool fun facts about history though! "
    elif demiinvite == True:
        $ demilv += 10
        " Because you had hung out with Mister Demi... "
        " You get 10+ points! "
        " He left before it got too late though. "
        " You and him listened to eachothers music playlist though! "
    elif sashainvite == True:
        $ sashalv += 10
        " Because you had hung out with Miss Sasha... "
        " You get 10+ points! "
        " She left before it got too late though. "
        " You two drew some drawings while she was there though! "
    else:
        pass
    stop music fadeout 1.0
    pause 1.0
    play music "audio/home.mp3" fadein 1.5
    scene mcroom with dissolve
    " You were already in your sleep wear and you were looking at your phone. "
    " Looks like there's nothing new in the teacher's GC... "
    " And you don't really have anything to do for your students. "
    " You're wondering if your students have this cool GC without you. "
    " Now you feel a little left out, you wanna know what kind of gossip they're talking about... "
    " Then again, it's not allowed because it would be seen in the wrong way if you were there. "
    " And you don't wanna be THAT type of person, so you just closed your phone.. "
    " And started falling asleep on your bed. "
    scene black with dissolve
    stop music fadeout 0.5
    " Good night, [name]. "
    pause 2.0
    jump teacherfriday
