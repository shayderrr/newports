label octuesday:
    show text " DAY 2 - TUESDAY "
    pause 1.5
    play music "audio/home.mp3"
    scene mcroom with dissolve
    " Good morning. Did you sleep well today? "
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
    if matteknow == True:
        " As you were on your way to your classroom, you spotted Matte struggling to carry her art materials. "
    else:
        " As you were on your way to your classroom, you spotted an artsy girl struggling to carry her art materials."
    " Do you want to help her? "
    menu:
        " Let's help! ":
            $ mattelv += 5
            " You decided to come over and help her out with her materials. "
            " You picked a few up that were accidentally dropped on the ground, and asked if it was alright for you to carry these things. "
            show matteneutral at center with dissolve
            hide matteneutral at bottom
            show mattehappy at center
            if matteknow == True:
                ma " I'm alright! "
                ma " Thanks for choosing to help though, [name]... "
                ma " No one really helps me out. But I think it's because I keep saying that I'll be fine... "
                " Yeah, no wonder why no one helps you out. "
                " You told her that it would've been fine if she asked for help. "
                hide mattehappy at bottom
                show matteneutral at center
                ma " Yeah, I know that. "
                ma " But, I, erh... "
                ma " I kinda get nervous whenever I'm asking for help, you know? "
                ma " I feel like people are gonna think I'm a little stupid for asking help on something simple. "
                ma " I know it's not good to be thinking like that, but I really can't help it... "
                ma " It just feels right for me to say, you know? "
                ma " I don't really want people to worry about me over something so stupid. "
                " You told her that you understood her. "
                " And you also told her that you'll always be there to help her whenever she needs it. "
                hide matteneutral at bottom
                show mattehappy at center
                ma " Awww, [name]... "
                ma " You're too nice, you know that? "
                scene black with dissolve
                " You helped Matte carry her art materials, and also talked with her. "
                " Once you two arrived at her locker, you went on your way to class. "
                play sound "audio/bellring.mp3"
                " ...Perfect timing, then. "
                pause 2.0
                jump ochistoryclass2
            else:
                x " I'm alright! "
                $ matteknow = True
                ma " I'm Matte by the way, don't think I got to introduce myself. Heh. "
                ma " Thanks for choosing to help though, [name]... "
                ma " No one really helps me out. But I think it's because I keep saying that I'll be fine... "
                " Yeah, no wonder why no one helps you out. "
                " You told her that it would've been fine if she asked for help. "
                hide mattehappy at bottom
                show matteneutral at center
                ma " Yeah, I know that. "
                ma " But, I, erh... "
                ma " I kinda get nervous whenever I'm asking for help, you know? "
                ma " I feel like people are gonna think I'm a little stupid for asking help on something simple. "
                ma " I know it's not good to be thinking like that, but I really can't help it... "
                ma " It just feels right for me to say, you know? "
                ma " I don't really want people to worry about me over something so stupid. "
                " You told her that you understood her. "
                " And you also told her that you'll always be there to help her whenever she needs it. "
                hide matteneutral at bottom
                show mattehappy at center
                ma " Awww, [name]... "
                ma " You're too nice, you know that? "
                scene black with dissolve
                " You helped Matte carry her art materials, and also talked with her. "
                " Once you two arrived at her locker, you went on your way to class. "
                play sound "audio/bellring.mp3"
                " ...Perfect timing, then. "
                pause 2.0
                jump ochistoryclass2
        " Nah, not my problem ":
            if matteknow == True:
                " You decided not to help Matte out. "
            else:
                " You decided not to help the girl out. "
            " On your way to your classroom then... "
            scene black with dissolve
            pause 2.0
            jump ochistoryclass2

label ochistoryclass2:
    scene classroom with dissolve
    " You walked into your classroom and sat into your seat... "
    " ...And started to wait for the teacher to arrive. "
    " Whilst you were waiting, you scrolled on your phone to see if there's anything new. "
    " ...Looks like the chapter 3-4 just released for a popular game. "
    " Nice. Maybe you should check that game out once you're done with school... "
    " It's got a weird yet cool name. but it's called...RuneDelta. "
    " Yeah, you're definitely checking this game out. "
    " The comments say that it's really good. And you trust those comments."
    " Peak! "
    " After a few minutes of even more scrolling, the teacher walks in. "
    " You hide your phone, and pretend like you were doing nothing interesting. "
    " The classroom gets silent. prepared for the lesson today. "
    show mrclioneutral at center with easeinright
    mscl " Good morning, class. "
    mscl " Let's get started with our lesson for today. "
    mscl " Before we continue... "
    mscl " Could someone give me an explanation of what we learnt yesterday? "
    if diskknow == True:
        " You looked around to see if anyone would actually want to answer that... "
        " ...And a few students did. Including Disk. "
    else:
        " You looked around to see if anyone would actually want to answer that... "
        " ...And a few students did. Including that one popular guy you keep hearing about in your GC. "
    mscl " Disk, I know you want points, but you should really give others a chance. "
    mscl " Besides, you already have high grades in my class. There's nothing to worry about. "
    mscl " How about we have miss Neo explain? "
    show temeroneutral at left with easeinleft
    if temeroknow == True:
        tm " Of course I'll explain! "
        tm " I remember everything we've learnt, after all. "
        mscl " Alright, let's hear your explanation. "
        tm " Okay, so! the first thing we learnt yesterday was... "
    else:
        x " Of course I'll explain! "
        x " I remember everything we've learnt, after all. "
        mscl " Alright, let's hear your explanation. "
        x " Okay, so! the first thing we learnt yesterday was... "
    " Hearing the girl start her explanation, your eyes feel heavy... "
    " You tried to fight off the sleepiness, but you couldn't resist. "
    " Wait, did you not get proper sleep? Or are you just that bored??? "
    " ...Well, whatever. Have a good nap. "
    " You're definitely gonna have to ask one of your classmates what happened in class later. "
    pause 2.0
    play sound "audio/bellring.mp3"
    " The bell ringing got you awake. "
    " The last thing you heard from your teacher was that there's going to be an activity on thursday. "
    " Huh. Better get prepared for that then, I guess. "
    " You get up from your chair and go into the hallways. "
    pause 2.0
    jump octbreak1

label octbreak1:
    scene hallway with dissolve
    " You walk into the hallways, getting that nice rich feeling of being in a prestigious school. "
    " Though, you feel like walking around and talking to people. "
    " Or not. But this game basically forces you to be social, so... have fun with that. "
    if pythonchallenge == True:
        " As you were about to decide where you want to go... "
        " A card flew into your face. Amazing. "
        " This must be apart of that challenge... you look at the back to see what the hint is for today. "
        " Let's see here... "
        " 'Silent halls where stories sleep,' "
        " 'Knowledge buried, secrets deep.' "
        " 'Between the pages, truths are stored -' "
        " 'Your number waits where minds are soard.' "
        " Not as difficult as the one from yesterday, it's pretty obvious where it is. "
        " Where are you gonna look? "
        menu:
            " {image=quinnicon} The front of the school {image=temeroicon} ":
                jump octfrontschool1
            " {image=sparkicon} The back of the school {image=matteicon} ":
                jump octbackschool1
            " {image=miaicon} The gym {image=orchidicon} ":
                jump octgym1
            " The cafeteria ":
                jump octcafe1
            " {image=carmenicon} The rooftop {image=jamicon} ":
                jump octrooftop1
            " {image=koaicon} The library {image=jexicon} ":
                jump octlibrary1
    else:
        pass
    " Anyway, where do you want to go? "
    menu:
        " {image=quinnicon} The front of the school {image=temeroicon} ":
            jump octfrontschool1
        " {image=sparkicon} The back of the school {image=matteicon} ":
            jump octbackschool1
        " {image=miaicon} The gym {image=orchidicon} ":
            jump octgym1
        " The cafeteria ":
            jump octcafe1
        " {image=carmenicon} The rooftop {image=jamicon} ":
            jump octrooftop1
        " {image=koaicon} The library {image=jexicon} ":
            jump octlibrary1

label octfrontschool1:
    # quinn and temero, temero suggests a very dangerous idea for a play
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school, feeling the nice, morning air hit you. "
    " You walked around a bit more and found two of your classmates talking about something. "
    " Being the curious little being that you are, you walked on over to them. "
    " ...At this point, you're going to have to walk in on everyone. But, who cares? "
    " This is how the game works, gang. "
    show quinnangry at left with easeinright
    show temeroneutral at right with easeinright
    if quinnknow == True and temeroknow == True:
        tm " Dude, I'm telling you, it's a good idea. "
        q " I like your idea, yes... "
        q " But don't you think its dangerous? Just for some simple effects...? "
        hide temeroneutral at bottom
        show temerohappy at right
        tm " Oho, trust me! "
        tm " I know of the PERFECT way to make it less dangerous! "
        q " Judging by how you are... "
        q " ...I have a feeling you're only going to make it more dangerous... "
        q " For both the performers, and ther audience.. "
        tm " Oh come on, Quinny! Don't you think it would be cool to have some really sweet effects? "
        tm " To get the audience a really good feel of what's going on? "
        tm " To keep them hooked on the story even more with such dazzling effects? "
        tm " I know you want it, deep down. "
        tm " Didn't you want to be a well-known actor? "
        tm " If someone catches everything on video... "
        tm " ...Who knows how much popularity your play will get! "
        q " That...is quite tempting, but... "
        hide quinnangry at bottom
        show quinnneutral at left
        hide temerohappy at bottom
        show temeroneutral at right
        " Quinn looks to your direction and he looked like he had an idea for a split second. "
        q " Ah, [name]! right on time. "
        q " Would it be alright if I asked you a question? "
        " You nodded. "
        q " Very well! "
        q " Should I let Temero over here add special effects for my play? (it...might be dangerous.) "
        " Let's think about it... "
        menu:
            " Let Temero add special effects even though it could be dangerous for both actors and audience ":
                $ temerolv += 5
                hide temeroneutral at bottom
                show temerohappy at right
                hide quinnneutral at bottom
                show quinnangry at left
                tm " Yess!! See, even [name] agrees that I should add cool effects. "
                " Quinn looks like he's regretting the choice of making you choose this option. "
                " Looks like he knows that he can't turn back at this point now, too. "
                q " Sigh...I'll talk about it to the rest of the members, I guess. "
                q " But if the stage randomly sets on fire at one point, I'm blaming you. "
                tm " But the blame can also be on you since you let me add these, so... "
                q " Just shut up. "
                tm " No can do! "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Quinn. "
                " Temero just kept on yapping about the things she wanted to be added in the play... "
                " ...And Quinn just looked like he was done with life. "
                " Hey, he's just like you fr! "
                " Done with life and all of that! "
                " Too bad you're going to have to stay on this life until you eventually expire! "
                play sound "audio/bellring.mp3"
                " The bell rings eventually, looks like it's time for health class. "
                " You walk back into the school and made your way back into the classroom. "
                pause 2.0
                jump ochealthclass2
            " Nah, should be more safe ":
                $ quinnlv += 5
                hide quinnneutral at bottom
                show quinnhappy at left
                hide temeroneutral at bottom
                show temeroangry at right
                tm " Boo, boring... "
                q " (Thanks for this, [name]...) "
                q " Temero, I think [name] agrees that your idea can be dangerous. "
                q " I most certainly don't want to be known as...um... "
                q " 'The student that almost burnt down the school'. That's not a pleasant title. "
                q " I deserve better than that, heh. "
                tm " Heeuughh... still though, it would've been fun! "
                q " Yes, but what matters most is safety. "
                tm " You should live a little and be dangerous sometimes. "
                q " I'd rather live and breathe normally than risk my life, thank you. "
                tm " Lame. Wonder why I'm friends with you. "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Quinn. "
                " Temero just kept on yapping about the things she wanted to be added in the play... "
                " And complaining about why she CAN'T add dangerous things in there. "
                " ...And Quinn just looked like he was done with life. Not even bothering to explain why to Temero at this point."
                " Hey, he's just like you fr! "
                " Done with life and all of that! "
                " Too bad you're going to have to stay on this life until you eventually expire! "
                play sound "audio/bellring.mp3"
                " The bell rings eventually, looks like it's time for health class. "
                " You walk back into the school and made your way back into the classroom. "
                pause 2.0
                jump ochealthclass2
    elif quinnknow == True and temeroknow == False:
        x " Dude, I'm telling you, it's a good idea. "
        q " I like your idea, yes... "
        q " But don't you think its dangerous? Just for some simple effects...? "
        hide temeroneutral at bottom
        show temerohappy at right
        x " Oho, trust me! "
        x " I know of the PERFECT way to make it less dangerous! "
        q " Judging by how you are... "
        q " ...I have a feeling you're only going to make it more dangerous... "
        q " For both the performers, and ther audience.. "
        x " Oh come on, Quinny! Don't you think it would be cool to have some really sweet effects? "
        x " To get the audience a really good feel of what's going on? "
        x " To keep them hooked on the story even more with such dazzling effects? "
        x " I know you want it, deep down. "
        x " Didn't you want to be a well-known actor? "
        x " If someone catches everything on video... "
        x " ...Who knows how much popularity your play will get! "
        q " That...is quite tempting, but... "
        hide quinnangry at bottom
        show quinnneutral at left
        hide temerohappy at bottom
        show temeroneutral at right
        " Quinn looks to your direction and he looked like he had an idea for a split second. "
        q " Ah, [name]! right on time. "
        q " Would it be alright if I asked you a question? "
        " You nodded. "
        $ temeroknow = True
        q " Very well! You see, my friend, Temero... "
        " Temero does a little wave at you. You wave back. "
        q " Should I let Temero over here add special effects for my play? (it...might be dangerous.) "
        " Let's think about it... "
        menu:
            " Let Temero add special effects even though it could be dangerous for both actors and audience ":
                $ temerolv += 5
                hide temeroneutral at bottom
                show temerohappy at right
                hide quinnneutral at bottom
                show quinnangry at left
                tm " Yess!! See, even [name] agrees that I should add cool effects. "
                " Quinn looks like he's regretting the choice of making you choose this option. "
                " Looks like he knows that he can't turn back at this point now, too. "
                q " Sigh...I'll talk about it to the rest of the members, I guess. "
                q " But if the stage randomly sets on fire at one point, I'm blaming you. "
                tm " But the blame can also be on you since you let me add these, so... "
                q " Just shut up. "
                tm " No can do! "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Quinn. "
                " Temero just kept on yapping about the things she wanted to be added in the play... "
                " ...And Quinn just looked like he was done with life. "
                " Hey, he's just like you fr! "
                " Done with life and all of that! "
                " Too bad you're going to have to stay on this life until you eventually expire! "
                play sound "audio/bellring.mp3"
                " The bell rings eventually, looks like it's time for health class. "
                " You walk back into the school and made your way back into the classroom. "
                pause 2.0
                jump ochealthclass2
            " Nah, should be more safe ":
                $ quinnlv += 5
                hide quinnneutral at bottom
                show quinnhappy at left
                hide temeroneutral at bottom
                show temeroangry at right
                tm " Boo, boring... "
                q " (Thanks for this, [name]...) "
                q " Temero, I think [name] agrees that your idea can be dangerous. "
                q " I most certainly don't want to be known as...um... "
                q " 'The student that almost burnt down the school'. That's not a pleasant title. "
                q " I deserve better than that, heh. "
                tm " Heeuughh... still though, it would've been fun! "
                q " Yes, but what matters most is safety. "
                tm " You should live a little and be dangerous sometimes. "
                q " I'd rather live and breathe normally than risk my life, thank you. "
                tm " Lame. Wonder why I'm friends with you. "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Quinn. "
                " Temero just kept on yapping about the things she wanted to be added in the play... "
                " And complaining about why she CAN'T add dangerous things in there. "
                " ...And Quinn just looked like he was done with life. Not even bothering to explain why to Temero at this point."
                " Hey, he's just like you fr! "
                " Done with life and all of that! "
                " Too bad you're going to have to stay on this life until you eventually expire! "
                play sound "audio/bellring.mp3"
                " The bell rings eventually, looks like it's time for health class. "
                " You walk back into the school and made your way back into the classroom. "
                pause 2.0
                jump ochealthclass2
    elif quinnknow == False and temeroknow == True:
        tm " Dude, I'm telling you, it's a good idea. "
        x " I like your idea, yes... "
        x " But don't you think its dangerous? Just for some simple effects...? "
        hide temeroneutral at bottom
        show temerohappy at right
        tm " Oho, trust me! "
        tm " I know of the PERFECT way to make it less dangerous! "
        x " Judging by how you are... "
        x " ...I have a feeling you're only going to make it more dangerous... "
        x " For both the performers, and ther audience.. "
        tm " Oh come on, Quinny! Don't you think it would be cool to have some really sweet effects? "
        tm " To get the audience a really good feel of what's going on? "
        tm " To keep them hooked on the story even more with such dazzling effects? "
        tm " I know you want it, deep down. "
        tm " Didn't you want to be a well-known actor? "
        tm " If someone catches everything on video... "
        tm " ...Who knows how much popularity your play will get! "
        x " That...is quite tempting, but... "
        hide quinnangry at bottom
        show quinnneutral at left
        hide temerohappy at bottom
        show temeroneutral at right
        " The stressed out boy looks to your direction and he looked like he had an idea for a split second. "
        x " Ah, [name]! right on time. "
        x " Would it be alright if I asked you a question? "
        " You nodded. "
        x " Very well! "
        $ quinnknow = True
        q " I'm Quinn, by the way. I'm in the drama club. "
        q " You see, my friend Temero wants to add something dangerous into my play to add some cool effects.. "
        q " Should I let Temero over here add special effects for my play? (it...might be dangerous.) "
        " Let's think about it... "
        menu:
            " Let Temero add special effects even though it could be dangerous for both actors and audience ":
                $ temerolv += 5
                hide temeroneutral at bottom
                show temerohappy at right
                hide quinnneutral at bottom
                show quinnangry at left
                tm " Yess!! See, even [name] agrees that I should add cool effects. "
                " Quinn looks like he's regretting the choice of making you choose this option. "
                " Looks like he knows that he can't turn back at this point now, too. "
                q " Sigh...I'll talk about it to the rest of the members, I guess. "
                q " But if the stage randomly sets on fire at one point, I'm blaming you. "
                tm " But the blame can also be on you since you let me add these, so... "
                q " Just shut up. "
                tm " No can do! "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Quinn. "
                " Temero just kept on yapping about the things she wanted to be added in the play... "
                " ...And Quinn just looked like he was done with life. "
                " Hey, he's just like you fr! "
                " Done with life and all of that! "
                " Too bad you're going to have to stay on this life until you eventually expire! "
                play sound "audio/bellring.mp3"
                " The bell rings eventually, looks like it's time for health class. "
                " You walk back into the school and made your way back into the classroom. "
                pause 2.0
                jump ochealthclass2
            " Nah, should be more safe ":
                $ quinnlv += 5
                hide quinnneutral at bottom
                show quinnhappy at left
                hide temeroneutral at bottom
                show temeroangry at right
                tm " Boo, boring... "
                q " (Thanks for this, [name]...) "
                q " Temero, I think [name] agrees that your idea can be dangerous. "
                q " I most certainly don't want to be known as...um... "
                q " 'The student that almost burnt down the school'. That's not a pleasant title. "
                q " I deserve better than that, heh. "
                tm " Heeuughh... still though, it would've been fun! "
                q " Yes, but what matters most is safety. "
                tm " You should live a little and be dangerous sometimes. "
                q " I'd rather live and breathe normally than risk my life, thank you. "
                tm " Lame. Wonder why I'm friends with you. "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Quinn. "
                " Temero just kept on yapping about the things she wanted to be added in the play... "
                " And complaining about why she CAN'T add dangerous things in there. "
                " ...And Quinn just looked like he was done with life. Not even bothering to explain why to Temero at this point."
                " Hey, he's just like you fr! "
                " Done with life and all of that! "
                " Too bad you're going to have to stay on this life until you eventually expire! "
                play sound "audio/bellring.mp3"
                " The bell rings eventually, looks like it's time for health class. "
                " You walk back into the school and made your way back into the classroom. "
                pause 2.0
                jump ochealthclass2
    else:
        x " Dude, I'm telling you, it's a good idea. "
        x " I like your idea, yes... "
        x " But don't you think its dangerous? Just for some simple effects...? "
        hide temeroneutral at bottom
        show temerohappy at right
        x " Oho, trust me! "
        x " I know of the PERFECT way to make it less dangerous! "
        x " Judging by how you are... "
        x " ...I have a feeling you're only going to make it more dangerous... "
        x " For both the performers, and ther audience.. "
        x " Oh come on, Quinny! Don't you think it would be cool to have some really sweet effects? "
        x " To get the audience a really good feel of what's going on? "
        x " To keep them hooked on the story even more with such dazzling effects? "
        x " I know you want it, deep down. "
        x " Didn't you want to be a well-known actor? "
        x " If someone catches everything on video... "
        x " ...Who knows how much popularity your play will get! "
        x " That...is quite tempting, but... "
        hide quinnangry at bottom
        show quinnneutral at left
        hide temerohappy at bottom
        show temeroneutral at right
        " The boy looks to your direction and he looked like he had an idea for a split second. "
        x " Ah, [name]! right on time. "
        x " Would it be alright if I asked you a question? "
        " You nodded. "
        $ temeroknow = True
        $ quinnknow = True
        x " Very well! "
        q " I'm Quinn, by the way. I'm in the drama club. "
        q " You see, my friend, Temero... "
        " Temero does a little wave at you. You wave back. "
        x " She wants something dangerous in my play to add some cool effects. "
        q " Should I let Temero over here add special effects for my play? (it...might be dangerous.) "
        " Let's think about it... "
        menu:
            " Let Temero add special effects even though it could be dangerous for both actors and audience ":
                $ temerolv += 5
                hide temeroneutral at bottom
                show temerohappy at right
                hide quinnneutral at bottom
                show quinnangry at left
                tm " Yess!! See, even [name] agrees that I should add cool effects. "
                " Quinn looks like he's regretting the choice of making you choose this option. "
                " Looks like he knows that he can't turn back at this point now, too. "
                q " Sigh...I'll talk about it to the rest of the members, I guess. "
                q " But if the stage randomly sets on fire at one point, I'm blaming you. "
                tm " But the blame can also be on you since you let me add these, so... "
                q " Just shut up. "
                tm " No can do! "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Quinn. "
                " Temero just kept on yapping about the things she wanted to be added in the play... "
                " ...And Quinn just looked like he was done with life. "
                " Hey, he's just like you fr! "
                " Done with life and all of that! "
                " Too bad you're going to have to stay on this life until you eventually expire! "
                play sound "audio/bellring.mp3"
                " The bell rings eventually, looks like it's time for health class. "
                " You walk back into the school and made your way back into the classroom. "
                pause 2.0
                jump ochealthclass2
            " Nah, should be more safe ":
                $ quinnlv += 5
                hide quinnneutral at bottom
                show quinnhappy at left
                hide temeroneutral at bottom
                show temeroangry at right
                tm " Boo, boring... "
                q " (Thanks for this, [name]...) "
                q " Temero, I think [name] agrees that your idea can be dangerous. "
                q " I most certainly don't want to be known as...um... "
                q " 'The student that almost burnt down the school'. That's not a pleasant title. "
                q " I deserve better than that, heh. "
                tm " Heeuughh... still though, it would've been fun! "
                q " Yes, but what matters most is safety. "
                tm " You should live a little and be dangerous sometimes. "
                q " I'd rather live and breathe normally than risk my life, thank you. "
                tm " Lame. Wonder why I'm friends with you. "
                scene black with dissolve
                " You spent the rest of the break talking with Temero and Quinn. "
                " Temero just kept on yapping about the things she wanted to be added in the play... "
                " And complaining about why she CAN'T add dangerous things in there. "
                " ...And Quinn just looked like he was done with life. Not even bothering to explain why to Temero at this point."
                " Hey, he's just like you fr! "
                " Done with life and all of that! "
                " Too bad you're going to have to stay on this life until you eventually expire! "
                play sound "audio/bellring.mp3"
                " The bell rings eventually, looks like it's time for health class. "
                " You walk back into the school and made your way back into the classroom. "
                pause 2.0
                jump ochealthclass2
label octbackschool1:
    # spark and matte, matte wants to paint you and spark
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walk into the back of the school, taking in that nice fresh air. "
    " You walked around to find a nice place to sit, and found two of your classmates vibing. "
    " One of them was painting, and another was...posing. "
    " Huh. Maybe you should ask what's going on. "
    " You walk over to them to see what they're doing. "
    show sparkneutral at right with easeinleft
    show matteneutral at left with easeinleft
    if sparkknow == True and matteknow == True:
        ma " Hmmm...something's missing here. "
        sp " Yeah, it kinda feels a little... "
        sp " Awkward with me posing like this. It's gonna look real weird if someone walks by... "
        ma " Speaking of someone... [name]'s here. "
        sp " Oh, uh, shit. Hi [name]. "
        " You said hi back, and then asked them what they were doing. "
        ma " Well, you see...I'm painting Spark. "
        ma " Miss Wisteria wanted a nice painting related to plants and stuff... "
        ma " ...With one or two people in it. "
        ma " Spark was the only one who volunteered, so I'm painting him holding a few plants. "
        sp " It' also perfect since there's many other plants in the area right now. "
        ma " That's true! But I feel like my painting is missing something... "
        sp " Maybe you're not missing someTHING, but someone? "
        ma " Hmmm...Oh yeah, you're right... "
        ma " The pose you're doing right now looks a bit...lonely, in a way? "
        ma " Looks like you need a partner somehow. "
        sp " ...Yeah. I guess you can say it like that. "
        ma " But Mia's busy...Orchid's busy doing their own thing... "
        ma " I'm sure no one else would like to volunteer either... "
        ma " Hmmm...this is slightly frustrating. "
        sp " ...Why don't you just ask [name]? "
        sp " I mean, I'm sure they'd be fine with it. Or not. "
        ma " Oh, right! "
        ma " [name], do you want to be apart of the painting? "
        sp " It's okay if you say no though. "
        menu:
            " Be apart of the painting and strike a cool pose near Spark ":
                $ sparklv += 5
                $ mattelv += 5
                hide sparkneutral at bottom
                hide matteneutral at bottom
                show sparkhappy at right
                show mattehappy at left
                sp " Sweet. "
                ma " Splendid! Just move a little closer to Spark, then... "
                ma " Just hold that one plant over there, and... "
                ma " Perfect! Absolutely and utterly perfect stunning! "
                ma " Let's get to painting! "
                scene black with dissolve
                " You spent the rest of the break letting Matte paint you and Spark. "
                " You kind of just...stood there with Spark until Matte was done painting. "
                " Hey, atleast you get to be in something cool I guess. "
                " Other than being in a game. "
                play sound "audio/bellring.mp3"
                " The bell rings right after Matte is done painting. "
                " You and Spark place down the plants you two were holding back into their original places. "
                " You all then went to your next class. "
                pause 2.0
                jump ochealthclass2
            " You'd rather watch Spark get embarrassed over doing a stupid pose ":
                hide sparkneutral at bottom
                show sparkangry at right
                sp " Woooow, [name]. "
                ma " Heheh, you sure do want Spark to suffer, huh? "
                sp " [name] I'm going to strangle you if you take a photo of me and post it on our GC. "
                ma " Don't worry, I'm sure [name] wouldn't do that! "
                ma " Now stand still... "
                scene black with dissolve
                " You spent the rest of the break watching Matta paint Spark. "
                " You would talk to the two every now and then about random things. "
                " ...You also managed to snag a goofy picture of Spark. "
                " You're definitely sending this to the GC later. "
                play sound "audio/bellring.mp3"
                " The bell rings right after Matte is done painting. "
                " Spark puts down the plants he was holding back into their original places. "
                " You all then went to your next class. "
                pause 2.0
                jump ochealthclass2
    elif sparkknow == True and matteknow == False:
        x " Hmmm...something's missing here. "
        sp " Yeah, it kinda feels a little... "
        sp " Awkward with me posing like this. It's gonna look real weird if someone walks by... "
        x " Speaking of someone... [name]'s here. "
        sp " Oh, uh, shit. Hi [name]. "
        $ matteknow = True
        sp " This is my friend. Matte. SHe's cool. "
        " You said hi back, and then asked them what they were doing. "
        ma " Well, you see...I'm painting Spark. "
        ma " Miss Wisteria wanted a nice painting related to plants and stuff... "
        ma " ...With one or two people in it. "
        ma " Spark was the only one who volunteered, so I'm painting him holding a few plants. "
        sp " It' also perfect since there's many other plants in the area right now. "
        ma " That's true! But I feel like my painting is missing something... "
        sp " Maybe you're not missing someTHING, but someone? "
        ma " Hmmm...Oh yeah, you're right... "
        ma " The pose you're doing right now looks a bit...lonely, in a way? "
        ma " Looks like you need a partner somehow. "
        sp " ...Yeah. I guess you can say it like that. "
        ma " But Mia's busy...Orchid's busy doing their own thing... "
        ma " I'm sure no one else would like to volunteer either... "
        ma " Hmmm...this is slightly frustrating. "
        sp " ...Why don't you just ask [name]? "
        sp " I mean, I'm sure they'd be fine with it. Or not. "
        ma " Oh, right! "
        ma " [name], do you want to be apart of the painting? "
        sp " It's okay if you say no though. "
        menu:
            " Be apart of the painting and strike a cool pose near Spark ":
                $ sparklv += 5
                $ mattelv += 5
                hide sparkneutral at bottom
                hide matteneutral at bottom
                show sparkhappy at right
                show mattehappy at left
                sp " Sweet. "
                ma " Splendid! Just move a little closer to Spark, then... "
                ma " Just hold that one plant over there, and... "
                ma " Perfect! Absolutely and utterly perfect stunning! "
                ma " Let's get to painting! "
                scene black with dissolve
                " You spent the rest of the break letting Matte paint you and Spark. "
                " You kind of just...stood there with Spark until Matte was done painting. "
                " Hey, atleast you get to be in something cool I guess. "
                " Other than being in a game. "
                play sound "audio/bellring.mp3"
                " The bell rings right after Matte is done painting. "
                " You and Spark place down the plants you two were holding back into their original places. "
                " You all then went to your next class. "
                pause 2.0
                jump ochealthclass2
            " You'd rather watch Spark get embarrassed over doing a stupid pose ":
                hide sparkneutral at bottom
                show sparkangry at right
                sp " Woooow, [name]. "
                ma " Heheh, you sure do want Spark to suffer, huh? "
                sp " [name] I'm going to strangle you if you take a photo of me and post it on our GC. "
                ma " Don't worry, I'm sure [name] wouldn't do that! "
                ma " Now stand still... "
                scene black with dissolve
                " You spent the rest of the break watching Matta paint Spark. "
                " You would talk to the two every now and then about random things. "
                " ...You also managed to snag a goofy picture of Spark. "
                " You're definitely sending this to the GC later. "
                play sound "audio/bellring.mp3"
                " The bell rings right after Matte is done painting. "
                " Spark puts down the plants he was holding back into their original places. "
                " You all then went to your next class. "
                pause 2.0
                jump ochealthclass2
    elif sparkknow == False and matteknow == True:
        ma " Hmmm...something's missing here. "
        x " Yeah, it kinda feels a little... "
        x " Awkward with me posing like this. It's gonna look real weird if someone walks by... "
        ma " Speaking of someone... [name]'s here. "
        x " Oh, uh, shit. Hi [name]. "
        $ sparkknow = True
        ma " This is my friend, Spark! He's nice, don't worry. "
        " You said hi back, and then asked them what they were doing. "
        ma " Well, you see...I'm painting Spark. "
        ma " Miss Wisteria wanted a nice painting related to plants and stuff... "
        ma " ...With one or two people in it. "
        ma " Spark was the only one who volunteered, so I'm painting him holding a few plants. "
        sp " It' also perfect since there's many other plants in the area right now. "
        ma " That's true! But I feel like my painting is missing something... "
        sp " Maybe you're not missing someTHING, but someone? "
        ma " Hmmm...Oh yeah, you're right... "
        ma " The pose you're doing right now looks a bit...lonely, in a way? "
        ma " Looks like you need a partner somehow. "
        sp " ...Yeah. I guess you can say it like that. "
        ma " But Mia's busy...Orchid's busy doing their own thing... "
        ma " I'm sure no one else would like to volunteer either... "
        ma " Hmmm...this is slightly frustrating. "
        sp " ...Why don't you just ask [name]? "
        sp " I mean, I'm sure they'd be fine with it. Or not. "
        ma " Oh, right! "
        ma " [name], do you want to be apart of the painting? "
        sp " It's okay if you say no though. "
        menu:
            " Be apart of the painting and strike a cool pose near Spark ":
                $ sparklv += 5
                $ mattelv += 5
                hide sparkneutral at bottom
                hide matteneutral at bottom
                show sparkhappy at right
                show mattehappy at left
                sp " Sweet. "
                ma " Splendid! Just move a little closer to Spark, then... "
                ma " Just hold that one plant over there, and... "
                ma " Perfect! Absolutely and utterly perfect stunning! "
                ma " Let's get to painting! "
                scene black with dissolve
                " You spent the rest of the break letting Matte paint you and Spark. "
                " You kind of just...stood there with Spark until Matte was done painting. "
                " Hey, atleast you get to be in something cool I guess. "
                " Other than being in a game. "
                play sound "audio/bellring.mp3"
                " The bell rings right after Matte is done painting. "
                " You and Spark place down the plants you two were holding back into their original places. "
                " You all then went to your next class. "
                pause 2.0
                jump ochealthclass2
            " You'd rather watch Spark get embarrassed over doing a stupid pose ":
                hide sparkneutral at bottom
                show sparkangry at right
                sp " Woooow, [name]. "
                ma " Heheh, you sure do want Spark to suffer, huh? "
                sp " [name] I'm going to strangle you if you take a photo of me and post it on our GC. "
                ma " Don't worry, I'm sure [name] wouldn't do that! "
                ma " Now stand still... "
                scene black with dissolve
                " You spent the rest of the break watching Matta paint Spark. "
                " You would talk to the two every now and then about random things. "
                " ...You also managed to snag a goofy picture of Spark. "
                " You're definitely sending this to the GC later. "
                play sound "audio/bellring.mp3"
                " The bell rings right after Matte is done painting. "
                " Spark puts down the plants he was holding back into their original places. "
                " You all then went to your next class. "
                pause 2.0
                jump ochealthclass2
    else:
        x " Hmmm...something's missing here. "
        x " Yeah, it kinda feels a little... "
        x " Awkward with me posing like this. It's gonna look real weird if someone walks by... "
        x " Speaking of someone... [name]'s here. "
        x " Oh, uh, shit. Hi [name]. "
        $ sparkknow = True
        $ matteknow = True
        sp " I'm Spark. And this is my friend, Matte. She's cool. "
        " You said hi back, and then asked them what they were doing. "
        ma " Well, you see...I'm painting Spark. "
        ma " Miss Wisteria wanted a nice painting related to plants and stuff... "
        ma " ...With one or two people in it. "
        ma " Spark was the only one who volunteered, so I'm painting him holding a few plants. "
        sp " It' also perfect since there's many other plants in the area right now. "
        ma " That's true! But I feel like my painting is missing something... "
        sp " Maybe you're not missing someTHING, but someone? "
        ma " Hmmm...Oh yeah, you're right... "
        ma " The pose you're doing right now looks a bit...lonely, in a way? "
        ma " Looks like you need a partner somehow. "
        sp " ...Yeah. I guess you can say it like that. "
        ma " But Mia's busy...Orchid's busy doing their own thing... "
        ma " I'm sure no one else would like to volunteer either... "
        ma " Hmmm...this is slightly frustrating. "
        sp " ...Why don't you just ask [name]? "
        sp " I mean, I'm sure they'd be fine with it. Or not. "
        ma " Oh, right! "
        ma " [name], do you want to be apart of the painting? "
        sp " It's okay if you say no though. "
        menu:
            " Be apart of the painting and strike a cool pose near Spark ":
                $ sparklv += 5
                $ mattelv += 5
                hide sparkneutral at bottom
                hide matteneutral at bottom
                show sparkhappy at right
                show mattehappy at left
                sp " Sweet. "
                ma " Splendid! Just move a little closer to Spark, then... "
                ma " Just hold that one plant over there, and... "
                ma " Perfect! Absolutely and utterly perfect stunning! "
                ma " Let's get to painting! "
                scene black with dissolve
                " You spent the rest of the break letting Matte paint you and Spark. "
                " You kind of just...stood there with Spark until Matte was done painting. "
                " Hey, atleast you get to be in something cool I guess. "
                " Other than being in a game. "
                play sound "audio/bellring.mp3"
                " The bell rings right after Matte is done painting. "
                " You and Spark place down the plants you two were holding back into their original places. "
                " You all then went to your next class. "
                pause 2.0
                jump ochealthclass2
            " You'd rather watch Spark get embarrassed over doing a stupid pose ":
                hide sparkneutral at bottom
                show sparkangry at right
                sp " Woooow, [name]. "
                ma " Heheh, you sure do want Spark to suffer, huh? "
                sp " [name] I'm going to strangle you if you take a photo of me and post it on our GC. "
                ma " Don't worry, I'm sure [name] wouldn't do that! "
                ma " Now stand still... "
                scene black with dissolve
                " You spent the rest of the break watching Matta paint Spark. "
                " You would talk to the two every now and then about random things. "
                " ...You also managed to snag a goofy picture of Spark. "
                " You're definitely sending this to the GC later. "
                play sound "audio/bellring.mp3"
                " The bell rings right after Matte is done painting. "
                " Spark puts down the plants he was holding back into their original places. "
                " You all then went to your next class. "
                pause 2.0
                jump ochealthclass2
label octgym1:
    # mia and orchid, talking about plants
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym and tried to find a perfect place to sit. "
    " As you were walking around, you found two of your classmates talking to eachother on the bleachers. "
    " The scene kid and that one flower kid... "
    " You should probably talk to them. You're bored as hell. "
    " You walked to where they were and sat next to them. "
    show mianeutral at left with easeinright
    show orchidneutral at right with easeinright
    if miaknow == True and orchidknow == True:
        oc " Hiya, [name]! "
        m " Heeeyy!! "
        " You said hello back. "
        " You then asked them what they were talking about. "
        oc " What we were talking about? "
        m " Oh, nothing interesting, really! "
        oc " Just talking about flowers and stuff. "
        oc " You know... "
        oc " Despite my name being Orchid and all, my favorite flower is actually the nightshade. "
        hide mianeutral at bottom
        show miahappy at left
        m " Oooh! That's a pretty good choice! "
        hide miahappy at bottom
        show mianeutral at left
        m " I don't really have any favorites... "
        m " I think all flowers and plants are cool! "
        oc " Even the deadly ones? "
        m " Yuppp!! Being deadly is what makes them cooler! "
        oc " Heh, true. "
        oc " Hey, wait. Isn't Matte painting something for the gardening class right now? "
        m " ... "
        hide mianeutral at bottom
        show miaangry at left
        m " WHAT. How come she didn't tell me?!? "
        oc " Well, I don't know... "
        oc " Maybe cause you looked pretty busy taking care of your flowers earlier? "
        m " That's stupid! Really stupid! "
        m " Honestly she could've just... "
        scene black with dissolve
        " You spent the rest of the break talking to Mia and Orchid. "
        " Well...you were mostly listening to Mia rant about how Matte not asking her to be in a painting. "
        " And Orchid trying their best to calm Mia down... "
        " Jeez, Mia can talk a lot when she's mad, can she? "
        " You just sat there and enjoyed the show. "
        play sound "audio/bellring.mp3"
        " The bell rings, stopping Mia from ranting any further...thankfully. "
        " You get up from where you were sitting and walked over to your classroom for your next class. "
        pause 2.0
        jump ochealthclass2
    elif miaknow == True and orchidknow == False:
        x " Hiya, [name]! "
        m " Heeeyy!! "
        $ orchidknow = True
        m " This is my friend, Orchid! They're really cool! "
        " You said hello back. "
        " You then asked them what they were talking about. "
        oc " What we were talking about? "
        m " Oh, nothing interesting, really! "
        oc " Just talking about flowers and stuff. "
        oc " You know... "
        oc " Despite my name being Orchid and all, my favorite flower is actually the nightshade. "
        hide mianeutral at bottom
        show miahappy at left
        m " Oooh! That's a pretty good choice! "
        hide miahappy at bottom
        show mianeutral at left
        m " I don't really have any favorites... "
        m " I think all flowers and plants are cool! "
        oc " Even the deadly ones? "
        m " Yuppp!! Being deadly is what makes them cooler! "
        oc " Heh, true. "
        oc " Hey, wait. Isn't Matte painting something for the gardening class right now? "
        m " ... "
        hide mianeutral at bottom
        show miaangry at left
        m " WHAT. How come she didn't tell me?!? "
        oc " Well, I don't know... "
        oc " Maybe cause you looked pretty busy taking care of your flowers earlier? "
        m " That's stupid! Really stupid! "
        m " Honestly she could've just... "
        scene black with dissolve
        " You spent the rest of the break talking to Mia and Orchid. "
        " Well...you were mostly listening to Mia rant about how Matte not asking her to be in a painting. "
        " And Orchid trying their best to calm Mia down... "
        " Jeez, Mia can talk a lot when she's mad, can she? "
        " You just sat there and enjoyed the show. "
        play sound "audio/bellring.mp3"
        " The bell rings, stopping Mia from ranting any further...thankfully. "
        " You get up from where you were sitting and walked over to your classroom for your next class. "
        pause 2.0
        jump ochealthclass2
    elif miaknow == False and orchidknow == True:
        oc " Hiya, [name]! "
        x " Heeeyy!! "
        $ miaknow = True
        oc " This is my friend, Mia! She's cool. "
        " You said hello back. "
        " You then asked them what they were talking about. "
        oc " What we were talking about? "
        m " Oh, nothing interesting, really! "
        oc " Just talking about flowers and stuff. "
        oc " You know... "
        oc " Despite my name being Orchid and all, my favorite flower is actually the nightshade. "
        hide mianeutral at bottom
        show miahappy at left
        m " Oooh! That's a pretty good choice! "
        hide miahappy at bottom
        show mianeutral at left
        m " I don't really have any favorites... "
        m " I think all flowers and plants are cool! "
        oc " Even the deadly ones? "
        m " Yuppp!! Being deadly is what makes them cooler! "
        oc " Heh, true. "
        oc " Hey, wait. Isn't Matte painting something for the gardening class right now? "
        m " ... "
        hide mianeutral at bottom
        show miaangry at left
        m " WHAT. How come she didn't tell me?!? "
        oc " Well, I don't know... "
        oc " Maybe cause you looked pretty busy taking care of your flowers earlier? "
        m " That's stupid! Really stupid! "
        m " Honestly she could've just... "
        scene black with dissolve
        " You spent the rest of the break talking to Mia and Orchid. "
        " Well...you were mostly listening to Mia rant about how Matte not asking her to be in a painting. "
        " And Orchid trying their best to calm Mia down... "
        " Jeez, Mia can talk a lot when she's mad, can she? "
        " You just sat there and enjoyed the show. "
        play sound "audio/bellring.mp3"
        " The bell rings, stopping Mia from ranting any further...thankfully. "
        " You get up from where you were sitting and walked over to your classroom for your next class. "
        pause 2.0
        jump ochealthclass2
    else:
        x " Hiya, [name]! "
        x " Heeeyy!! "
        $ orchidknow = True
        $ miaknow = True
        oc " I'm Orchid! "
        m " And I'm Mia! It's nice to meet you! "
        " You said hello back and told them that it's nice to meet them too. "
        " You then asked them what they were talking about. "
        oc " What we were talking about? "
        m " Oh, nothing interesting, really! "
        oc " Just talking about flowers and stuff. "
        oc " You know... "
        oc " Despite my name being Orchid and all, my favorite flower is actually the nightshade. "
        hide mianeutral at bottom
        show miahappy at left
        m " Oooh! That's a pretty good choice! "
        hide miahappy at bottom
        show mianeutral at left
        m " I don't really have any favorites... "
        m " I think all flowers and plants are cool! "
        oc " Even the deadly ones? "
        m " Yuppp!! Being deadly is what makes them cooler! "
        oc " Heh, true. "
        oc " Hey, wait. Isn't Matte painting something for the gardening class right now? "
        m " ... "
        hide mianeutral at bottom
        show miaangry at left
        m " WHAT. How come she didn't tell me?!? "
        oc " Well, I don't know... "
        oc " Maybe cause you looked pretty busy taking care of your flowers earlier? "
        m " That's stupid! Really stupid! "
        m " Honestly she could've just... "
        scene black with dissolve
        " You spent the rest of the break talking to Mia and Orchid. "
        " Well...you were mostly listening to Mia rant about how Matte not asking her to be in a painting. "
        " And Orchid trying their best to calm Mia down... "
        " Jeez, Mia can talk a lot when she's mad, can she? "
        " You just sat there and enjoyed the show. "
        play sound "audio/bellring.mp3"
        " The bell rings, stopping Mia from ranting any further...thankfully. "
        " You get up from where you were sitting and walked over to your classroom for your next class. "
        pause 2.0
        jump ochealthclass2
label octcafe1:
    # Disk, yinhui and yangyi, jacob
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted three of your classmates vibing. "
    " You're thinking about talking to one of them... "
    " Who do you talk to? "
    if diskknow,yinhuiknow,yangyiknow,jacobknow == True:
        menu:
            " {image=diskicon} Disk {image=diskicon} ":
                jump letsknock
            " {image=yinyangicon} Yinhui and Yangyi {image=yinyangicon} ":
                jump emdead
            " {image=jacobicon} Jacob {image=jacobicon} ":
                jump intothenight
    elif diskknow,yinhuiknow,yangyiknow == True and jacobknow == False:
        menu:
            " {image=diskicon} Disk {image=diskicon} ":
                jump letsknock
            " {image=yinyangicon} Yinhui and Yangyi {image=yinyangicon} ":
                jump emdead
            " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                jump intothenight
    elif yinhuiknow,yangyiknow,jacobknow == True and diskknow == False:
        menu:
            " {image=diskicon} The popular kid {image=diskicon} ":
                jump letsknock
            " {image=yinyangicon} Yinhui and Yangyi {image=yinyangicon} ":
                jump emdead
            " {image=jacobicon} Jacob {image=jacobicon} ":
                jump intothenight
    elif diskknow,jacobknow == True and yinhuiknow,yangyiknow == False:
        menu:
            " {image=diskicon} Disk {image=diskicon} ":
                jump letsknock
            " {image=yinyangicon} Odd looking twins {image=yinyangicon} ":
                jump emdead
            " {image=jacobicon} Jacob {image=jacobicon} ":
                jump intothenight
    elif diskknow == True and yinhuiknow,yangyiknow,jacobknow == False:
        menu:
            " {image=diskicon} Disk {image=diskicon} ":
                jump letsknock
            " {image=yinyangicon} Odd looking twins {image=yinyangicon} ":
                jump emdead
            " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                jump intothenight
    elif yinhuiknow,yangyiknow == True and diskknow,jacobknow == False:
        menu:
            " {image=diskicon} The popular kid {image=diskicon} ":
                jump letsknock
            " {image=yinyangicon} Yinhui and Yangyi {image=yinyangicon} ":
                jump emdead
            " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                jump intothenight
    elif jacobknow == True and diskknow,yinhuiknow,yangyiknow == False:
        menu:
            " {image=diskicon} The popular kid {image=diskicon} ":
                jump letsknock
            " {image=yinyangicon} Odd looking twins {image=yinyangicon} ":
                jump emdead
            " {image=jacobicon} Jacob {image=jacobicon} ":
                jump intothenight
    else:
        menu:
            " {image=diskicon} The popular kid {image=diskicon} ":
                jump letsknock
            " {image=yinyangicon} Odd looking kids {image=yinyangicon} ":
                jump emdead
            " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                jump intothenight
    label letsknock:
        show diskneutral at center with easeinright
        if diskknow == True:
            " You walked up to him and greeted him. "
            d " Hiya, [name]!! I'm happy to see you today! "
            d " You know... "
            hide diskneutral at bottom
            show diskhappy at center
            d " My little brother's doing a play! "
            hide diskhappy at bottom
            show diskneutral at center
            d " Have I told you about it before? I can't remember... "
            d " But still! he's working on a very cool play! "
            d " Well...all of his plays are very cool! At least in my opinion. "
            d " ... "
            d " Actually, you wanna know a secret about me and my brother? "
            menu:
                " Listen in ":
                    $ disklv += 5
                    d " Okay!! "
                    d " What you're about to hear is gonna be...kinda sudden or something... "
                    d " Especially since we just met a day ago... "
                    d " And...Quinn kinda hates this whenever I say this to someone, soooo.. "
                    d " Promise me that you won't tell him that I told him! "
                    " You pinky promised with Disk that you wouldn't tell Quinn. "
                    stop music fadeout 1.5
                    d " Okay...here we go. "
                    " Even though Disk has that cheery smile on his face... "
                    hide diskneutral at bottom
                    show diskserious at center
                    " He looks different. And sounds different. "
                    " Sounded like he's actually being a bit serious for once. "
                    " That's odd...must be something deep, then. "
                    d " Me and Quinn actually used to go to a different school before we ended up here. "
                    d " It was...way different than this school. "
                    hide diskserious at bottom
                    show disksad at center
                    d " Everyone was mean. Say a single word and you're already a target for bullying. "
                    d " When everyone found out that I was a part of a wealthy family... "
                    d " ...They started asking me and my brother for money. "
                    d " Of course, we thought that they were just borrowing some money normally. "
                    d " Like, they probably didn't have enough money to buy food and stuff! "
                    d " But it...kind of got out of hand once we started saying no. "
                    d " Everytime they asked, we said no...everytime we did... "
                    d " ...They started being more aggressive. "
                    d " They would give us threats, if we didn't give them money. "
                    d " Eventually, it got so out of hand that they... "
                    d " ...Started targetting our more personal stuff. "
                    d " They told Quinn that he'll never be a popular actor and will die alone. "
                    d " They told me that... "
                    d " ... "
                    d " ...They said mean words about my skin color. "
                    " Oh. Oh HELL no. "
                    d " And my sexuality, since someone had managed to figure out that I was...not exactly straight. "
                    d " In that school, if you even had a slight bit of uniqueness... "
                    d " ...You'd be made fun of, of course. Including your skin color, sexuality...even your personality or your hair. "
                    d " It wasn't a nice place to be in. "
                    hide disksad at bottom
                    show diskneutral at center
                    play music "audio/paperhigh.mp3" fadein 1.5
                    d " But, thankfully... my parents saw how bad it was getting and transferred us here. "
                    d " Our parents didn't really believe how bad that old school was until they came over there. "
                    d " I'm glad to be out of that place now though! "
                    d " ...Quinn doesn't exactly like being reminded of that place. "
                    d " And, neither do I. "
                    hide diskneutral at bottom
                    show diskjoyous at center
                    d " I'm glad we transferred here so that I could meet a wonderful person like you, [name]!! "
                    d " You're a very cool [person]!! "
                    scene black with dissolve
                    " You spent the rest of the break talking to Disk. "
                    " You felt a little bad, since you heard what Disk had to go through... "
                    " But you feel better now knowing that he's safe from the horros of his old school now. "
                    " If you see anyone being mean to this guy, you're gonna strangle them. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, interrupting your conversation with Disk. "
                    " You get up from where you were sitting and you walked to your classroom for the next class. "
                    pause 2.0
                    jump ochealthclass2
                " Nah, sorry ":
                    d " Oh, okay! "
                    d " How about we talk about something else then? "
                    d " Like... "
                    d " What kinds of animals we like! "
                    d " Lemme start first! I really like dogs, and... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk. "
                    " You don't know why, but you kinda feel like it's obvious that Disk likes dogs. "
                    " I mean, he acts like a golden retriever boy or whatever they call them. "
                    " Like those really nice guys with a golden heart or whatever. "
                    " Geez, people use confusing terms. "
                    " That's nothing new though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, stopping your conversation with Disk. "
                    " You get up from where you were sitting and walked back to your classroom for the next class. "
                    pause 2.0
                    jump ochealthclass2
        else:
            " You walked up to him and greeted him. "
            x " Hiya, [name]!! I'm happy to see you today! "
            $ diskknow = True
            d " I'm Disk, by the way! It's nice to meet you! "
            d " You know... "
            hide diskneutral at bottom
            show diskhappy at center
            d " My little brother's doing a play! "
            hide diskhappy at bottom
            show diskneutral at center
            d " Have I told you about it before? I can't remember... "
            d " But still! he's working on a very cool play! "
            d " Well...all of his plays are very cool! At least in my opinion. "
            d " ... "
            d " Actually, you wanna know a secret about me and my brother? "
            menu:
                " Listen in ":
                    $ disklv += 5
                    d " Okay!! "
                    d " What you're about to hear is gonna be...kinda sudden or something... "
                    d " Especially since we just met right now... "
                    d " And...Quinn kinda hates this whenever I say this to someone, soooo.. "
                    d " Promise me that you won't tell him that I told him! "
                    " You pinky promised with Disk that you wouldn't tell Quinn. "
                    stop music fadeout 1.5
                    d " Okay...here we go. "
                    " Even though Disk has that cheery smile on his face... "
                    hide diskneutral at bottom
                    show diskserious at center
                    " He looks different. And sounds different. "
                    " Sounded like he's actually being a bit serious for once. "
                    " That's odd...must be something deep, then. "
                    d " Me and Quinn actually used to go to a different school before we ended up here. "
                    d " It was...way different than this school. "
                    hide diskserious at bottom
                    show disksad at center
                    d " Everyone was mean. Say a single word and you're already a target for bullying. "
                    d " When everyone found out that I was a part of a wealthy family... "
                    d " ...They started asking me and my brother for money. "
                    d " Of course, we thought that they were just borrowing some money normally. "
                    d " Like, they probably didn't have enough money to buy food and stuff! "
                    d " But it...kind of got out of hand once we started saying no. "
                    d " Everytime they asked, we said no...everytime we did... "
                    d " ...They started being more aggressive. "
                    d " They would give us threats, if we didn't give them money. "
                    d " Eventually, it got so out of hand that they... "
                    d " ...Started targetting our more personal stuff. "
                    d " They told Quinn that he'll never be a popular actor and will die alone. "
                    d " They told me that... "
                    d " ... "
                    d " ...They said mean words about my skin color. "
                    " Oh. Oh HELL no. "
                    d " And my sexuality, since someone had managed to figure out that I was...not exactly straight. "
                    d " In that school, if you even had a slight bit of uniqueness... "
                    d " ...You'd be made fun of, of course. Including your skin color, sexuality...even your personality or your hair. "
                    d " It wasn't a nice place to be in. "
                    hide disksad at bottom
                    show diskneutral at center
                    play music "audio/paperhigh.mp3" fadein 1.5
                    d " But, thankfully... my parents saw how bad it was getting and transferred us here. "
                    d " Our parents didn't really believe how bad that old school was until they came over there. "
                    d " I'm glad to be out of that place now though! "
                    d " ...Quinn doesn't exactly like being reminded of that place. "
                    d " And, neither do I. "
                    hide diskneutral at bottom
                    show diskjoyous at center
                    d " I'm glad we transferred here so that I could meet a wonderful person like you, [name]!! "
                    d " You're a very cool [person]!! "
                    scene black with dissolve
                    " You spent the rest of the break talking to Disk. "
                    " You felt a little bad, since you heard what Disk had to go through... "
                    " But you feel better now knowing that he's safe from the horros of his old school now. "
                    " If you see anyone being mean to this guy, you're gonna strangle them. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, interrupting your conversation with Disk. "
                    " You get up from where you were sitting and you walked to your classroom for the next class. "
                    pause 2.0
                    jump ochealthclass2
                " Nah, sorry ":
                    d " Oh, okay! "
                    d " How about we talk about something else then? "
                    d " Like... "
                    d " What kinds of animals we like! "
                    d " Lemme start first! I really like dogs, and... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk. "
                    " You don't know why, but you kinda feel like it's obvious that Disk likes dogs. "
                    " I mean, he acts like a golden retriever boy or whatever they call them. "
                    " Like those really nice guys with a golden heart or whatever. "
                    " Geez, people use confusing terms. "
                    " That's nothing new though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, stopping your conversation with Disk. "
                    " You get up from where you were sitting and walked back to your classroom for the next class. "
                    pause 2.0
                    jump ochealthclass2
    label emdead:
        show yinhuineutral at right with easeinleft
        show yangyineutral at left with easeinleft
        " You walked up to them and greeted them. "
        " Then asked them what they're doing. "
        if yinhuiknow,yangyiknow == True:
            ya " Heya, [name]! "
            yi " ...Hi. "
            ya " We were both thinking of going to Disk's party this friday... "
            ya " Speaking of his party, are you coming? "
            if diskparty == True:
                " You told them that you were, for a fact, going. "
                hide yangyineutral at bottom
                show yangyihappy at left
                ya " Splendid!! "
                yi " ...Great, I guess. "
                hide yangyihappy at bottom
                show yangyineutral at left
                ya " Anyway...Disk's party, right? "
                ya " We're thinking of going, buuuutt... "
                yi " Our mom only lets one of us go everytime Disk throws a party. "
                yi " Which is a little annoying since I want to watch over Yang, but I know if I complained our mom wouldn't like it. "
                ya " Hehe... "
                ya " Anywho, [name]! "
                ya " Just a simple question... "
                ya " If you could take one of us to Disk's party...who would you choose? "
                yi " The way you worded it sounds weird. "
                ya " Come on, don't be thinking like that... "
                ya " Besides, it would be fun if we went out with [name], would it not? "
                yi " ...I guess. "
                " The both of them stare at you, waiting for your response. "
                menu:
                    " Why can't I take both of you out (+25 pts on both!) ":
                        $ yinyangparty = True
                        $ yangyilv += 25
                        $ yinhuilv += 25
                        hide yangyineutral at bottom
                        hide yinhuineutral at bottom
                        show yangyisurprised at left
                        show yinhuisurprised at right
                        ya " ...! "
                        yi " ...? "
                        " Looks like you gained a lot of affection points for that. "
                        " This is probably going to be the only time I'll say something about it. "
                        ya " Hold on, are you serious? "
                        yi " ...There's no way. "
                        yi " I mean, you literally met us a day ago. "
                        yi " Are you absolutely SURE you would want to take us out? "
                        ya " I don't even know how mom will react...! "
                        hide yinhuisurprised at bottom
                        show yinhuineutral at right
                        yi " Dude... "
                        yi " You know, we could just try calling mom right now... "
                        yi " ...And ask her if we really could go. "
                        ya " ARE YOU SURE??? "
                        ya " She looked like she was in a really scary mood today {nw} "
                        ya " And I don't want to bother her {nw} "
                        ya " I just really don't want to get my ass beat {nw} "
                        ya " and {nw} "
                        hide yinhuineutral at bottom
                        show yinhuiangry at right
                        hide yangyisurprised at bottom
                        show yangyisad at left
                        yi " ALRIGHT!!! I'll ask her myself, then! " with vpunch
                        " ...His voice was so loud, the entire cafeteria shook. "
                        " Though the other students seemed to be...used to it, in a way. "
                        " Interesting... "
                        hide yinhuiangry at bottom
                        show yinhuineutral at right
                        hide yangyisad at bottom
                        show yangyineutral at left
                        " Yinhui calls his mom and speaks to her in a foreign language... "
                        " It sounded like it as chinese. Huh, you didn't know these two were chinese. "
                        " Or did you? I don't know if I mentioned it to you but whatever. "
                        " Then, Yinhui hangs up and looks... "
                        hide yinhuineutral at bottom
                        show yinhuiheh at right
                        " Happy. Did their mom actually agree? "
                        yi " Heh, guess what mom said. "
                        ya " ...? "
                        yi " Since we did good in her class yesterday she's letting us BOTH go. "
                        ya " Wait, really? "
                        hide yangyineutral at bottom
                        show yangyihappy at left
                        ya " Oh, how wonderful!! I'm so happy!! "
                        yi " We can tell, idiot. "
                        scene black with dissolve
                        " You spent the rest of the break talking to Yinhui and Yangyi about Disk's party. "
                        " Both of them seemed to be pretty happy that the both of them can go... "
                        " ..Now that you think about it, Disk throws parties a whole lot, doesn't he? "
                        " Considering the fact that you've heard that he throws them every friday. "
                        " I mean, it's nice that he decided to throw something like that, since you know, last day of school for the week. "
                        " Pretty neat. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, meaning that it's time for another class. "
                        " You get up from where you were sitting, and you walked back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
                    " Why are you asking me this ":
                        yi " Because we need help on deciding who should go to the party, idiot. "
                        ya " Mhm, since...you know...our mom... "
                        yi " Now pick already, I'm getting impatient. "
                        menu:
                            " Choose Yangyi (+20 pts) ":
                                $ yangyiparty = True
                                $ yangyilv += 20
                                hide yangyineutral at bottom
                                show yangyihappy at left
                                ya " Oh, yay!! I do feel bad that my brother can't join... "
                                yi " ... "
                                yi " Whatever, as long as my brother is safe with you, [name]. "
                                yi " If he gets hurt there, I'm going to kill you. "
                                hide yangyihappy at bottom
                                show yangyineutral at left
                                ya " Oh, brother... it's just a party! "
                                ya " I won't get hurt or anything, trust me! "
                                ya " And even if I do, I'm old enough to defend myself, remember? "
                                yi " ...Okay. "
                                " Yinhui sounded like he didn't believe his brother... "
                                " Ah, brotherly love. "
                                scene black with dissolve
                                " You spent the rest of the break talking to Yinhui and Yangyi. "
                                " Yangyi seemed to be pretty excited to go to the party this friday... "
                                " Though Yinhui looked like he was about to kill you at any moment. "
                                " Not because you didn't choose him, but because he wanted to make sure if his brother is truly going to be safe with someone like you. "
                                " Geez, he really is that portective, huh? "
                                " Brothers...smh... "
                                play sound "audio/bellring.mp3"
                                " The bell rings after a bit, meaning that it's time for another class. "
                                " You get up from where you were sitting and you walk back to your classroom for your next class. "
                                pause 2.0
                                jump ochealthclass2
                            " Choose Yinhui (+20 pts) ":
                                $ yinhuiparty = True
                                $ yinhuilv += 20
                                hide yinhuineutral at bottom
                                show yinhuisurprised at right
                                yi " ...? You serious? "
                                yi " I rarely even go to these things. "
                                ya " Come on, brother! You've gotta get out and socialize! "
                                yi " I do that a lot, thank you very much. "
                                yi " But, uh... "
                                yi " Guess I'm going with you then, [name]. "
                                ya " (Psst! [name]!) "
                                ya " (This is going tobe a good bonding expirience with you and Yinhui!) "
                                ya " (Perhaps you two could become very good friends in the party!) "
                                ya " (Or, maybe...) "
                                hide yinhuisurprised at bottom
                                show yinhuineutral at right
                                yi " Hey, what're you whispering to [them]? "
                                hide yangyineutral at bottom
                                show yangyihappy at left
                                ya " Oh, nothing! "
                                " Yinhui looked like he didn't believe his brother... "
                                " But he didn't question about what Yangyi was whispering to you. "
                                scene black with dissolve
                                " You spent the rest of the break talking to Yinhui and Yangyi. "
                                " Yangyi was trying to get Yinhui to be excited that he's going to a party... "
                                " ...But Yinhui seemed like he was just zoning out to Yangyi's attempts. "
                                " Brothers, smh.. "
                                play sound "audio/bellring.mp3"
                                " The bell rings after a bit, meaning that it's time for another class. "
                                " You get up from where you were sitting and you walked back to your classroom for the next class. "
                                pause 2.0
                                jump ochealthclass2
            else:
                " You told them that you weren't going, unfortunately. "
                " Either you knew that there was a party, or you didn't. Depends on what you did when you first met Disk yesterday. "
                " Too bad you can't go that far back to change your decision anymore. "
                " Unless you have a save file that's saved at that point. Which is unlikely. "
                ya " Ah... well! "
                yi " Me and Yangyi are trying to decide who goes to the party this time. "
                ya " Disk does this every friday, so we both decide who's turn it is to go! "
                yi " Though, we may or may not have lost track of who's turn it is. "
                ya " So...we need your help, [name]! "
                yi " Who should go to Disk's party this friday? "
                yi " Hurry up and start thinking, I'm starting to get impatient. "
                menu:
                    " Yangyi should go (+5 pts) ":
                        $ yangyilv += 5
                        hide yangyineutral at bottom
                        show yangyihappy at left
                        ya " Woohoo!! Okay!! "
                        yi " ...I'm going to have to ask Disk to look if you do anything stupid again. "
                        ya " Come on brother, I know that you know that I won't do anything dumb! "
                        yi " ...Just incase. "
                        yi " And remember, if anyone dares to touch you in a weird way or talks to you in a weird way... "
                        hide yinhuineutral at bottom
                        show yinhuiheh at right
                        yi " Call me or mom. We're gonna have to beat them up. "
                        yi " Don't care if we're causing a scene, I just want you to be safe. "
                        hide yangyihappy at bottom
                        show yangyijoyous at left
                        ya " Awww, Yin!! "
                        yi " Yeah, yeah, whatever. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Yinhui and Yangyi. "
                        " You honestly found it sweetthat Yinhui wants his brother to be safe... "
                        " Though, you'd honestly do the same and beat up any stranger talking weird to your sibling, if you had one. "
                        " Even though siblings can probably get annoying, you still gotta look after them. "
                        " Otherwise your parents are gonna beat your ass. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, meaning that it's time for another class. "
                        " You get up from where you were sitting and you walk back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
                    " Yinhui should go (+5 pts) ":
                        $ yinhuilv += 5
                        yi " Alright, i don't mind going. "
                        ya " Come on, brother! You gotta atleast sound excited to go! "
                        hide yinhuineutral at bottom
                        show yinhuiheh at right
                        yi " Oh yeah? well how about this: "
                        yi " OoooOoOOoh, I'm soooooo excited to go to Disk's party or whatever!! "
                        yi " I'm gonna go and break a lot of rules without mom knowing!! "
                        ya " Wh - heh, hey! I didn't mean it like that! "
                        ya " You gotta be genuinely excited to go to Disk's party! "
                        yi " I {i}was{/i}being genuinely excited to go to Disk's party, what do you mean? "
                        ya " Nuh uh!!! "
                        scene black with dissolve
                        " You spent the rest of the break talking to Yinhui and Yangyi. "
                        " Yangyi was trying his best to get Yinhui to be excited about the party... "
                        " But Yinhui seemed to be just fooling around with Yangyi. "
                        " Brothers, am I right? "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, meaning that it's time for another class. "
                        " You get up from where you were sitting and walked back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
        else:
            x " Heya, [name]! "
            x " ...Hi. "
            $ yinhuiknow = True
            $ yangyiknow = True
            ya " I'm Yangyi - the twin on the left! "
            yi " And I'm Yinhui...the twin on the right. "
            ya " We're brothers! and uh... "
            ya " We were both thinking of going to Disk's party this friday... "
            ya " Speaking of his party, are you coming? "
            if diskparty == True:
                " You told them that you were, for a fact, going. "
                hide yangyineutral at bottom
                show yangyihappy at left
                ya " Splendid!! "
                yi " ...Great, I guess. "
                hide yangyihappy at bottom
                show yangyineutral at left
                ya " Anyway...Disk's party, right? "
                ya " We're thinking of going, buuuutt... "
                yi " Our mom only lets one of us go everytime Disk throws a party. "
                yi " Which is a little annoying since I want to watch over Yang, but I know if I complained our mom wouldn't like it. "
                ya " Hehe... "
                ya " Anywho, [name]! "
                ya " Just a simple question... "
                ya " If you could take one of us to Disk's party...who would you choose? "
                yi " The way you worded it sounds weird. "
                ya " Come on, don't be thinking like that... "
                ya " Besides, it would be fun if we went out with [name], would it not? "
                yi " ...I guess. "
                " The both of them stare at you, waiting for your response. "
                menu:
                    " Why can't I take both of you out (+25 pts on both!) ":
                        $ yinyangparty = True
                        $ yangyilv += 25
                        $ yinhuilv += 25
                        hide yangyineutral at bottom
                        hide yinhuineutral at bottom
                        show yangyisurprised at left
                        show yinhuisurprised at right
                        ya " ...! "
                        yi " ...? "
                        " Looks like you gained a lot of affection points for that. "
                        " This is probably going to be the only time I'll say something about it. "
                        ya " Hold on, are you serious? "
                        yi " ...There's no way. "
                        yi " I mean, you literally met us today. "
                        yi " Are you absolutely SURE you would want to take us out? "
                        ya " I don't even know how mom will react...! "
                        hide yinhuisurprised at bottom
                        show yinhuineutral at right
                        yi " Dude... "
                        yi " You know, we could just try calling mom right now... "
                        yi " ...And ask her if we really could go. "
                        ya " ARE YOU SURE??? "
                        ya " She looked like she was in a really scary mood today {nw} "
                        ya " And I don't want to bother her {nw} "
                        ya " I just really don't want to get my ass beat {nw} "
                        ya " and {nw} "
                        hide yinhuineutral at bottom
                        show yinhuiangry at right
                        hide yangyisurprised at bottom
                        show yangyisad at left
                        yi " ALRIGHT!!! I'll ask her myself, then! " with vpunch
                        " ...His voice was so loud, the entire cafeteria shook. "
                        " Though the other students seemed to be...used to it, in a way. "
                        " Interesting... "
                        hide yinhuiangry at bottom
                        show yinhuineutral at right
                        hide yangyisad at bottom
                        show yangyineutral at left
                        " Yinhui calls his mom and speaks to her in a foreign language... "
                        " It sounded like it as chinese. Huh, you didn't know these two were chinese. "
                        " Or did you? I don't know if I mentioned it to you but whatever. "
                        " Then, Yinhui hangs up and looks... "
                        hide yinhuineutral at bottom
                        show yinhuiheh at right
                        " Happy. Did their mom actually agree? "
                        yi " Heh, guess what mom said. "
                        ya " ...? "
                        yi " Since we did good in her class yesterday she's letting us BOTH go. "
                        ya " Wait, really? "
                        hide yangyineutral at bottom
                        show yangyihappy at left
                        ya " Oh, how wonderful!! I'm so happy!! "
                        yi " We can tell, idiot. "
                        scene black with dissolve
                        " You spent the rest of the break talking to Yinhui and Yangyi about Disk's party. "
                        " Both of them seemed to be pretty happy that the both of them can go... "
                        " ..Now that you think about it, Disk throws parties a whole lot, doesn't he? "
                        " Considering the fact that you've heard that he throws them every friday. "
                        " I mean, it's nice that he decided to throw something like that, since you know, last day of school for the week. "
                        " Pretty neat. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, meaning that it's time for another class. "
                        " You get up from where you were sitting, and you walked back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
                    " Why are you asking me this ":
                        yi " Because we need help on deciding who should go to the party, idiot. "
                        ya " Mhm, since...you know...our mom... "
                        yi " Now pick already, I'm getting impatient. "
                        menu:
                            " Choose Yangyi (+20 pts) ":
                                $ yangyiparty = True
                                $ yangyilv += 20
                                hide yangyineutral at bottom
                                show yangyihappy at left
                                ya " Oh, yay!! I do feel bad that my brother can't join... "
                                yi " ... "
                                yi " Whatever, as long as my brother is safe with you, [name]. "
                                yi " If he gets hurt there, I'm going to kill you. "
                                hide yangyihappy at bottom
                                show yangyineutral at left
                                ya " Oh, brother... it's just a party! "
                                ya " I won't get hurt or anything, trust me! "
                                ya " And even if I do, I'm old enough to defend myself, remember? "
                                yi " ...Okay. "
                                " Yinhui sounded like he didn't believe his brother... "
                                " Ah, brotherly love. "
                                scene black with dissolve
                                " You spent the rest of the break talking to Yinhui and Yangyi. "
                                " Yangyi seemed to be pretty excited to go to the party this friday... "
                                " Though Yinhui looked like he was about to kill you at any moment. "
                                " Not because you didn't choose him, but because he wanted to make sure if his brother is truly going to be safe with someone like you. "
                                " Geez, he really is that portective, huh? "
                                " Brothers...smh... "
                                play sound "audio/bellring.mp3"
                                " The bell rings after a bit, meaning that it's time for another class. "
                                " You get up from where you were sitting and you walk back to your classroom for your next class. "
                                pause 2.0
                                jump ochealthclass2
                            " Choose Yinhui (+20 pts) ":
                                $ yinhuiparty = True
                                $ yinhuilv += 20
                                hide yinhuineutral at bottom
                                show yinhuisurprised at right
                                yi " ...? You serious? "
                                yi " I rarely even go to these things. "
                                ya " Come on, brother! You've gotta get out and socialize! "
                                yi " I do that a lot, thank you very much. "
                                yi " But, uh... "
                                yi " Guess I'm going with you then, [name]. "
                                ya " (Psst! [name]!) "
                                ya " (This is going tobe a good bonding expirience with you and Yinhui!) "
                                ya " (Perhaps you two could become very good friends in the party!) "
                                ya " (Or, maybe...) "
                                hide yinhuisurprised at bottom
                                show yinhuineutral at right
                                yi " Hey, what're you whispering to [them]? "
                                hide yangyineutral at bottom
                                show yangyihappy at left
                                ya " Oh, nothing! "
                                " Yinhui looked like he didn't believe his brother... "
                                " But he didn't question about what Yangyi was whispering to you. "
                                scene black with dissolve
                                " You spent the rest of the break talking to Yinhui and Yangyi. "
                                " Yangyi was trying to get Yinhui to be excited that he's going to a party... "
                                " ...But Yinhui seemed like he was just zoning out to Yangyi's attempts. "
                                " Brothers, smh.. "
                                play sound "audio/bellring.mp3"
                                " The bell rings after a bit, meaning that it's time for another class. "
                                " You get up from where you were sitting and you walked back to your classroom for the next class. "
                                pause 2.0
                                jump ochealthclass2
            else:
                " You told them that you weren't going, unfortunately. "
                " Either you knew that there was a party, or you didn't. Depends on what you did when you first met Disk yesterday. "
                " Too bad you can't go that far back to change your decision anymore. "
                " Unless you have a save file that's saved at that point. Which is unlikely. "
                ya " Ah... well! "
                yi " Me and Yangyi are trying to decide who goes to the party this time. "
                ya " Disk does this every friday, so we both decide who's turn it is to go! "
                yi " Though, we may or may not have lost track of who's turn it is. "
                ya " So...we need your help, [name]! "
                yi " Who should go to Disk's party this friday? "
                yi " Hurry up and start thinking, I'm starting to get impatient. "
                menu:
                    " Yangyi should go (+5 pts) ":
                        $ yangyilv += 5
                        hide yangyineutral at bottom
                        show yangyihappy at left
                        ya " Woohoo!! Okay!! "
                        yi " ...I'm going to have to ask Disk to look if you do anything stupid again. "
                        ya " Come on brother, I know that you know that I won't do anything dumb! "
                        yi " ...Just incase. "
                        yi " And remember, if anyone dares to touch you in a weird way or talks to you in a weird way... "
                        hide yinhuineutral at bottom
                        show yinhuiheh at right
                        yi " Call me or mom. We're gonna have to beat them up. "
                        yi " Don't care if we're causing a scene, I just want you to be safe. "
                        hide yangyihappy at bottom
                        show yangyijoyous at left
                        ya " Awww, Yin!! "
                        yi " Yeah, yeah, whatever. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Yinhui and Yangyi. "
                        " You honestly found it sweetthat Yinhui wants his brother to be safe... "
                        " Though, you'd honestly do the same and beat up any stranger talking weird to your sibling, if you had one. "
                        " Even though siblings can probably get annoying, you still gotta look after them. "
                        " Otherwise your parents are gonna beat your ass. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, meaning that it's time for another class. "
                        " You get up from where you were sitting and you walk back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
                    " Yinhui should go (+5 pts) ":
                        $ yinhuilv += 5
                        yi " Alright, i don't mind going. "
                        ya " Come on, brother! You gotta atleast sound excited to go! "
                        hide yinhuineutral at bottom
                        show yinhuiheh at right
                        yi " Oh yeah? well how about this: "
                        yi " OoooOoOOoh, I'm soooooo excited to go to Disk's party or whatever!! "
                        yi " I'm gonna go and break a lot of rules without mom knowing!! "
                        ya " Wh - heh, hey! I didn't mean it like that! "
                        ya " You gotta be genuinely excited to go to Disk's party! "
                        yi " I {i}was{/i}being genuinely excited to go to Disk's party, what do you mean? "
                        ya " Nuh uh!!! "
                        scene black with dissolve
                        " You spent the rest of the break talking to Yinhui and Yangyi. "
                        " Yangyi was trying his best to get Yinhui to be excited about the party... "
                        " But Yinhui seemed to be just fooling around with Yangyi. "
                        " Brothers, am I right? "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, meaning that it's time for another class. "
                        " You get up from where you were sitting and walked back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
    label intothenight:
        show jacobsleepy at center with dissolve
        if jacobknow == True:
            " You walked up to him and sat next to him. "
            jac " ... "
            " ...Well, he's oddly quiet. "
            " It took a good while for you to notice that he's actually sleeping while sitting. "
            " Huh, impressive... "
            if noxknow == True:
                " Nox would probably somehow sleep on the ceiling though. "
                " So not too impressive. "
            else:
                " Someone in your class could do better though. "
            " You just sat there for a bit... "
            " Chilling and seeing if he would wake up or not... "
            " ... "
            " Yeah, this is taking a bit long. "
            " You're starting to think that you should probably do something to wake him up. "
            " You thought of what to do and then your eyes landed on his goggles and bandana. "
            " Hmmm...maybe you should take a look. "
            " Though, you've heard to not do that...but why? "
            " Should you look at what's underneath his goggles and bandana? "
            menu:
                " Take a small peek ":
                    " You lifted up his goggles first... "
                    " ...Oh my, is that how his eyes really look? "
                    " Surely, his bottom half of his face wouldn't look too bad... "
                    " You put his goggles back own and lifted up his bandana. "
                    " ...Oh. "
                    " Maybe you shouldn't have taken a peek. "
                    " You can't unsee the things you've seen now though. "
                    " Unfortunately. "
                    " Thank the heavens this guy isn't awake right now. "
                    " Otherwise he'd probably kick your ass for looking. "
                    " Not probably, but most likely. "
                    " Let's just pray that he somehow doesn't find out that you took a look. "
                    " With that saw on his hand...something bad might happen. "
                    " You're not gonna die to a student, you're atleast going to die to a teacher. "
                    scene black with dissolve
                    " You spent the rest of the break vibing with a sleeping Jacob. "
                    " You just scrolled your phone as you waited for him to wake up... "
                    " He kinda just kept sleeping though. "
                    " You're starting to wonder if he got proper sleep last night. "
                    " Probably not, considering he's sleeping in the cafeteria. "
                    " At least he gets a few minutes of sleep. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, effectively waking Jacob up. "
                    " It also means that it's time for another class. "
                    " You get up from where you were seated and you walk back to your classroom for the next class. "
                    pause 2.0
                    jump ochealthclass2
                " Nah, let's respect his privacy ":
                    $ jacoblv += 10
                    " Yeah, it's best to not take a look. "
                    " From what you've heard, he doesn't like it when someone touches his bandana or goggles. "
                    " Who know's what he'd do if he saw you touch him... "
                    " ...Actually, that saw on his hand is already giving you ideas. "
                    " Not so nice ideas. "
                    " You don't wanna die to this emo bad boy guy. "
                    " You're gonna have to atleast die to something else. Like a teacher for example. "
                    " How are you gonna get killed by a teacher? Well, uh... "
                    " Mister Clio has a spear. He can use that. "
                    " Or...wait, now that you think about it, most of the teachers dont have weapons. "
                    " Maybe they just haven't revealed them yet? You don't know. "
                    scene black with dissolve
                    " You spent the rest of the break vibing with a sleeping Jacob. "
                    " You just scrolled your phone as you waited for him to wake up... "
                    " He kinda just kept sleeping though. "
                    " You're starting to wonder if he got proper sleep last night. "
                    " Probably not, considering he's sleeping in the cafeteria. "
                    " At least he gets a few minutes of sleep. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, effectively waking Jacob up. "
                    " It also means that it's time for another class. "
                    " You get up from where you were seated and you walk back to your classroom for the next class. "
                    pause 2.0
                    jump ochealthclass2
        else:
            " You walked up to him and sat next to him. "
            x " ... "
            " ...Well, he's oddly quiet. "
            " It took a good while for you to notice that he's actually sleeping while sitting. "
            " Huh, impressive... "
            if noxknow == True:
                " Nox would probably somehow sleep on the ceiling though. "
                " So not too impressive. "
            else:
                " Someone in your class could do better though. "
            " You just sat there for a bit... "
            " Chilling and seeing if he would wake up or not... "
            " ... "
            " Yeah, this is taking a bit long. "
            " You're starting to think that you should probably do something to wake him up. "
            " You thought of what to do and then your eyes landed on his goggles and bandana. "
            " Hmmm...maybe you should take a look. "
            " Though, you've heard to not do that...but why? "
            " Should you look at what's underneath his goggles and bandana? "
            menu:
                " Take a small peek ":
                    " You lifted up his goggles first... "
                    " ...Oh my, is that how his eyes really look? "
                    " Surely, his bottom half of his face wouldn't look too bad... "
                    " You put his goggles back own and lifted up his bandana. "
                    " ...Oh. "
                    " Maybe you shouldn't have taken a peek. "
                    " You can't unsee the things you've seen now though. "
                    " Unfortunately. "
                    " Thank the heavens this guy isn't awake right now. "
                    " Otherwise he'd probably kick your ass for looking. "
                    " Not probably, but most likely. "
                    " Let's just pray that he somehow doesn't find out that you took a look. "
                    " With that saw on his hand...something bad might happen. "
                    " You're not gonna die to a student, you're atleast going to die to a teacher. "
                    scene black with dissolve
                    " You spent the rest of the break vibing with a sleeping guy. "
                    " You just scrolled your phone as you waited for him to wake up... "
                    " He kinda just kept sleeping though. "
                    " You're starting to wonder if he got proper sleep last night. "
                    " Probably not, considering he's sleeping in the cafeteria. "
                    " At least he gets a few minutes of sleep. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, effectively waking the guy up. "
                    " It also means that it's time for another class. "
                    " You get up from where you were seated and you walk back to your classroom for the next class. "
                    pause 2.0
                    jump ochealthclass2
                " Nah, let's respect his privacy ":
                    $ jacoblv += 10
                    " Yeah, it's best to not take a look. "
                    " From what you've heard, he doesn't like it when someone touches his bandana or goggles. "
                    " Who know's what he'd do if he saw you touch him... "
                    " ...Actually, that saw on his hand is already giving you ideas. "
                    " Not so nice ideas. "
                    " You don't wanna die to this emo bad boy guy. "
                    " You're gonna have to atleast die to something else. Like a teacher for example. "
                    " How are you gonna get killed by a teacher? Well, uh... "
                    " Mister Clio has a spear. He can use that. "
                    " Or...wait, now that you think about it, most of the teachers dont have weapons. "
                    " Maybe they just haven't revealed them yet? You don't know. "
                    scene black with dissolve
                    " You spent the rest of the break vibing with a sleeping guy. "
                    " You just scrolled your phone as you waited for him to wake up... "
                    " He kinda just kept sleeping though. "
                    " You're starting to wonder if he got proper sleep last night. "
                    " Probably not, considering he's sleeping in the cafeteria. "
                    " At least he gets a few minutes of sleep. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, effectively waking the guy up. "
                    " It also means that it's time for another class. "
                    " You get up from where you were seated and you walk back to your classroom for the next class. "
                    pause 2.0
                    jump ochealthclass2
label octrooftop1:
    # carmen and jam, arguing over something dumb
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked up to the rooftop and immediately hear two of your classmates arguing. "
    " Wonder what they're fighting about this time... "
    " You walked to where all the noise was so that you could see what's going on. "
    show carmenangry at right with easeinleft
    show jamangry at left with easeinleft
    if carmenknow == True and jamknow == True:
        ja " What do you MEAN you spent time with HER??? "
        ca " ...!!!!! (I SPENT TIME WITH HER IN A FRIENDLY WAY, IDIOT!!) "
        ja " A friendly way, really?! "
        ja " Then tell me, why were you holding her hand??! "
        ca " ??? (DOESN'T SHE DO THAT TO EVERYONE WHENEVER SHES WALKING WITH SOMEONE??) "
        ja " You're just making up bullshit at this point. "
        ca " !!! (I REALLY AM NOT!!) " with vpunch
        " Carmen takes a deep breath, and pulls out his guitar... "
        hide jamangry at bottom
        show jamsurprised at left
        " ...And then starts rapidly playing it. "
        " Jam looks surprised...oh right, this guy can sometimes talk with his guitar. "
        " And it seems like he's real mad right now. "
        " Looks like he's calling her a lot of insults... "
        " You're starting to wonder how can people understand him. "
        " Game logic, I guess. "
        hide carmenangry at right with easeoutright
        show jamsurprised at center with move
        " Carmen eventually stops and he storms off. "
        ja " ... "
        hide jamsurprised at bottom
        show jamsad at center
        ja " ...Damn it. Not again. "
        menu:
            " Go and comfort Carmen ":
                $ carmencomfort = True
                $ carmenlv += 15
                scene black with dissolve
                " You walked back down to the hallways, where Carmen went. "
                " You wonder what was even happening in the first place to get them to be so mad at eachother... "
                " You'll ask him in a bit. "
                pause 1.0
                scene hallway with dissolve
                show carmenangry at center with easeinleft
                " You managed to catch up with Carmen and asked him if he was okay. "
                ca " ... "
                " ...He shook his head no. "
                " You then asked him what happened earlier. "
                ca " ... "
                hide carmenangry at bottom
                show carmenneutral at center
                ca " ... "
                " He pulls out his guitar once more before he starts playing a nice tune... "
                " And somehow, you're slowly starting to understand what he's saying through the guitar. "
                ca " ...Me and Jam were fighting because... "
                ca " ...Jam got jealous that I spent time with Matte, even though she just wanted to hang out with me... "
                ca " ...I told Jam that I didn't want to start anything romantic with Matte, Matte's not even my type.. "
                ca " I don't even like girls to begin with, yes I'm not straight, real shocker... "
                ca " But, Jam didn't believe me and the arguing escalated... "
                ca " ...I know Jam can get super jealous, but I've never seen her get this mad... "
                ca " Jeez...she really needs to calm down sometimes... "
                ca " Though, I doubt that you even understand me right now... "
                ca " You're probably just listening to my tunes and nodding... "
                " You tell him that you understood him perfectly. "
                hide carmenneutral at bottom
                show carmensurprised at center
                ca " Wait, you can? "
                ca " I'm surprised that you could understand me this quickly... "
                hide carmensurprised at bottom
                show carmenhappy at center
                ca " How interesting...I'm glad that you can understand me though. "
                ca " It makes me...happy. "
                ca " You know, some people don't understand what I'm saying sometimes. "
                ca " So I've always had someone to translate for me... "
                ca " And everytime someone starts understanding what I'm saying... "
                ca " ..It makes my day a whole lot better. "
                ca " I think you've known this before, but...I'm mute. "
                ca " It was hard trying to communicate with people at first, but... "
                ca " Now that everyone's starting to understand, I feel better. "
                ca " ...I don't know where this conversation is going at this point, but... "
                ca " Thank you, [name]. For being here. "
                " Carmen stops playing his guitar, and he pats your head. "
                " He seems really happy that you have understood him. "
                " You give him a headpat back. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Carmen. "
                " You just talked to him about random things to get him distracted... "
                " ...And not get reminded of what went on earlier. "
                " Wow, you're such a good friend! "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it's time for another class. "
                " You walk over to your classroom to get to your second class of the day. "
                pause 2.0
                jump ochealthclass2
            " Comfort Jam ":
                $ jamcomfort = True
                $ jamlv += 15
                ja " ...I shouldn't have gotten jealous. "
                ja " I know Matte's just making friends, but seeing her with someone else... "
                ja " ...It makes my blood boil. I can't understand why. "
                ja " I don't...want to be some protective freak over her. "
                ja " I don't want to be some weirdo who says: "
                ja " 'Matte is mine, you can't have her!' "
                ja " That's just...weird. Why am I like this? "
                ja " I've never been like this before. It's...odd. "
                ja " I don't understand what I'm feeling. "
                ja " ...Why am I acting this way, even if I know that she probably doesn't like me back? "
                ja " My mom wouldn't even approve of my feelings right now. "
                ja " I have to be strong. Cold. Mean. "
                ja " I have to...get with a nice guy. "
                " As Jam mentions that she should be with a guy and not a girl, you could hear her voice sound... "
                " ...Disgusted. "
                ja " These feelings aren't right, is what mom would say. "
                menu:
                    " It's okay to feel that way towards Matte ":
                        $ jamlv += 5
                        ja " Is it really? "
                        ja " I don't think so. "
                        ja " Mom would kill me if she found out that I like a girl... "
                        ja " Probably would give me the worst death ever. "
                        ja " Uh, thanks for...trying to comfort me, [name]. "
                        ja " You did your best. "
                        hide jamsad at right with easeoutright
                        " ...She walked away. "
                        scene black with dissolve
                        " You spent the rest of the break chilling on the rooftop. "
                        " You were wondering if Jam and Carmen would be alright, after what happened... "
                        " You could only hope they'd make up. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walk down from the rooftop, and you walk back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
                    " It's a normal feeling ":
                        $ jamlv += 5
                        ja " Is it really? "
                        ja " I don't think so. "
                        ja " Mom would kill me if she found out that I like a girl... "
                        ja " Probably would give me the worst death ever. "
                        ja " Uh, thanks for...trying to comfort me, [name]. "
                        ja " You did your best. "
                        hide jamsad at right with easeoutright
                        " ...She walked away. "
                        scene black with dissolve
                        " You spent the rest of the break chilling on the rooftop. "
                        " You were wondering if Jam and Carmen would be alright, after what happened... "
                        " You could only hope they'd make up. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walk down from the rooftop, and you walk back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
    elif carmenknow == True and jamknow == False:
        x " What do you MEAN you spent time with HER??? "
        ca " ...!!!!! (I SPENT TIME WITH HER IN A FRIENDLY WAY, IDIOT!!) "
        x " A friendly way, really?! "
        x " Then tell me, why were you holding her hand??! "
        ca " ??? (DOESN'T SHE DO THAT TO EVERYONE WHENEVER SHES WALKING WITH SOMEONE??) "
        x " You're just making up bullshit at this point. "
        ca " !!! (I REALLY AM NOT!!) " with vpunch
        " Carmen takes a deep breath, and pulls out his guitar... "
        hide jamangry at bottom
        show jamsurprised at left
        " ...And then starts rapidly playing it. "
        " The girl looks surprised...oh right, this guy can sometimes talk with his guitar. "
        " And it seems like he's real mad right now. "
        " Looks like he's calling her a lot of insults... "
        " You're starting to wonder how can people understand him. "
        " Game logic, I guess. "
        hide carmenangry at right with easeoutright
        show jamsurprised at center with move
        " Carmen eventually stops and he storms off. "
        x " ... "
        hide jamsurprised at bottom
        show jamsad at center
        x " ...Damn it. Not again. "
        menu:
            " Go and comfort Carmen ":
                $ carmencomfort = True
                $ carmenlv += 15
                scene black with dissolve
                " You walked back down to the hallways, where Carmen went. "
                " You wonder what was even happening in the first place to get them to be so mad at eachother... "
                " You'll ask him in a bit. "
                pause 1.0
                scene hallway with dissolve
                show carmenangry at center with easeinleft
                " You managed to catch up with Carmen and asked him if he was okay. "
                ca " ... "
                " ...He shook his head no. "
                " You then asked him what happened earlier. "
                ca " ... "
                hide carmenangry at bottom
                show carmenneutral at center
                ca " ... "
                " He pulls out his guitar once more before he starts playing a nice tune... "
                " And somehow, you're slowly starting to understand what he's saying through the guitar. "
                ca " ...Me and Jam were fighting because... "
                ca " ...Jam got jealous that I spent time with Matte, even though she just wanted to hang out with me... "
                ca " ...I told Jam that I didn't want to start anything romantic with Matte, Matte's not even my type.. "
                ca " I don't even like girls to begin with, yes I'm not straight, real shocker... "
                ca " But, Jam didn't believe me and the arguing escalated... "
                ca " ...I know Jam can get super jealous, but I've never seen her get this mad... "
                ca " Jeez...she really needs to calm down sometimes... "
                ca " Though, I doubt that you even understand me right now... "
                ca " You're probably just listening to my tunes and nodding... "
                " You tell him that you understood him perfectly. "
                hide carmenneutral at bottom
                show carmensurprised at center
                ca " Wait, you can? "
                ca " I'm surprised that you could understand me this quickly... "
                hide carmensurprised at bottom
                show carmenhappy at center
                ca " How interesting...I'm glad that you can understand me though. "
                ca " It makes me...happy. "
                ca " You know, some people don't understand what I'm saying sometimes. "
                ca " So I've always had someone to translate for me... "
                ca " And everytime someone starts understanding what I'm saying... "
                ca " ..It makes my day a whole lot better. "
                ca " I think you've known this before, but...I'm mute. "
                ca " It was hard trying to communicate with people at first, but... "
                ca " Now that everyone's starting to understand, I feel better. "
                ca " ...I don't know where this conversation is going at this point, but... "
                ca " Thank you, [name]. For being here. "
                " Carmen stops playing his guitar, and he pats your head. "
                " He seems really happy that you have understood him. "
                " You give him a headpat back. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Carmen. "
                " You just talked to him about random things to get him distracted... "
                " ...And not get reminded of what went on earlier. "
                " Wow, you're such a good friend! "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it's time for another class. "
                " You walk over to your classroom to get to your second class of the day. "
                pause 2.0
                jump ochealthclass2
            " Comfort the girl ":
                $ jamcomfort = True
                $ jamlv += 15
                x " ...I shouldn't have gotten jealous. "
                x " I know Matte's just making friends, but seeing her with someone else... "
                x " ...It makes my blood boil. I can't understand why. "
                x " I don't...want to be some protective freak over her. "
                x " I don't want to be some weirdo who says: "
                x " 'Matte is mine, you can't have her!' "
                x " That's just...weird. Why am I like this? "
                x " I've never been like this before. It's...odd. "
                x " I don't understand what I'm feeling. "
                x " ...Why am I acting this way, even if I know that she probably doesn't like me back? "
                x " My mom wouldn't even approve of my feelings right now. "
                x " I have to be strong. Cold. Mean. "
                x " I have to...get with a nice guy. "
                " As she mentions that she should be with a guy and not a girl, you could hear her voice sound... "
                " ...Disgusted. "
                x " These feelings aren't right, is what mom would say. "
                menu:
                    " It's okay to feel that way towards Matte ":
                        $ jamlv += 5
                        x " Is it really? "
                        x " I don't think so. "
                        x " Mom would kill me if she found out that I like a girl... "
                        x " Probably would give me the worst death ever. "
                        x " Uh, thanks for...trying to comfort me, [name]. "
                        x " You did your best. "
                        hide jamsad at right with easeoutright
                        " ...She walked away. "
                        scene black with dissolve
                        " You spent the rest of the break chilling on the rooftop. "
                        " You were wondering if that girl and Carmen would be alright, after what happened... "
                        " You could only hope they'd make up. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walk down from the rooftop, and you walk back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
                    " It's a normal feeling ":
                        $ jamlv += 5
                        x " Is it really? "
                        x " I don't think so. "
                        x " Mom would kill me if she found out that I like a girl... "
                        x " Probably would give me the worst death ever. "
                        x " Uh, thanks for...trying to comfort me, [name]. "
                        x " You did your best. "
                        hide jamsad at right with easeoutright
                        " ...She walked away. "
                        scene black with dissolve
                        " You spent the rest of the break chilling on the rooftop. "
                        " You were wondering if that girl and Carmen would be alright, after what happened... "
                        " You could only hope they'd make up. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walk down from the rooftop, and you walk back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
    elif carmenknow == False and jamknow == True:
        ja " What do you MEAN you spent time with HER??? "
        x " ...!!!!! (I SPENT TIME WITH HER IN A FRIENDLY WAY, IDIOT!!) "
        ja " A friendly way, really?! "
        ja " Then tell me, why were you holding her hand??! "
        x " ??? (DOESN'T SHE DO THAT TO EVERYONE WHENEVER SHES WALKING WITH SOMEONE??) "
        ja " You're just making up bullshit at this point. "
        x " !!! (I REALLY AM NOT!!) " with vpunch
        " The boy takes a deep breath, and pulls out his guitar... "
        hide jamangry at bottom
        show jamsurprised at left
        " ...And then starts rapidly playing it. "
        " Jam looks surprised...oh right, this guy can sometimes talk with his guitar. "
        " And it seems like he's real mad right now. "
        " Looks like he's calling her a lot of insults... "
        " You're starting to wonder how can people understand him. "
        " Game logic, I guess. "
        hide carmenangry at right with easeoutright
        show jamsurprised at center with move
        " The boy then eventually stops and he storms off. "
        ja " ... "
        hide jamsurprised at bottom
        show jamsad at center
        ja " ...Damn it. Not again. "
        menu:
            " Go and comfort the boy ":
                $ carmencomfort = True
                $ carmenlv += 15
                scene black with dissolve
                " You walked back down to the hallways, where that boy went. "
                " You wonder what was even happening in the first place to get them to be so mad at eachother... "
                " You'll ask him in a bit. "
                pause 1.0
                scene hallway with dissolve
                show carmenangry at center with easeinleft
                " You managed to catch up with him and asked him if he was okay. "
                x " ... "
                " ...He shook his head no. "
                " You then asked him what happened earlier. "
                x " ... "
                hide carmenangry at bottom
                show carmenneutral at center
                x " ... "
                " He pulls out his guitar once more before he starts playing a nice tune... "
                " And somehow, you're slowly starting to understand what he's saying through the guitar. "
                x " ...Me and Jam were fighting because... "
                x " ...Jam got jealous that I spent time with Matte, even though she just wanted to hang out with me... "
                x " ...I told Jam that I didn't want to start anything romantic with Matte, Matte's not even my type.. "
                x " I don't even like girls to begin with, yes I'm not straight, real shocker... "
                x " But, Jam didn't believe me and the arguing escalated... "
                x " ...I know Jam can get super jealous, but I've never seen her get this mad... "
                x " Jeez...she really needs to calm down sometimes... "
                x " Though, I doubt that you even understand me right now... "
                x " You're probably just listening to my tunes and nodding... "
                " You tell him that you understood him perfectly. "
                hide carmenneutral at bottom
                show carmensurprised at center
                x " Wait, you can? "
                x " I'm surprised that you could understand me this quickly... "
                $ carmenknow = True
                hide carmensurprised at bottom
                show carmenneutral at center
                ca " Ah, um...I'm Carmen, by the way. Nice to meet you. "
                ca " I'm mute, but...I usually use my guitar to speak. Or use sign language. "
                hide carmenneutral at bottom
                show carmenhappy at center
                ca " How interesting...I'm glad that you can understand me though. "
                ca " It makes me...happy. "
                ca " You know, some people don't understand what I'm saying sometimes. "
                ca " So I've always had someone to translate for me... "
                ca " And everytime someone starts understanding what I'm saying... "
                ca " ..It makes my day a whole lot better. "
                ca " I think you've known this before, but...I'm mute. "
                ca " It was hard trying to communicate with people at first, but... "
                ca " Now that everyone's starting to understand, I feel better. "
                ca " ...I don't know where this conversation is going at this point, but... "
                ca " Thank you, [name]. For being here. "
                " Carmen stops playing his guitar, and he pats your head. "
                " He seems really happy that you have understood him. "
                " You give him a headpat back. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Carmen. "
                " You just talked to him about random things to get him distracted... "
                " ...And not get reminded of what went on earlier. "
                " Wow, you're such a good friend! "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it's time for another class. "
                " You walk over to your classroom to get to your second class of the day. "
                pause 2.0
                jump ochealthclass2
            " Comfort Jam ":
                $ jamcomfort = True
                $ jamlv += 15
                ja " ...I shouldn't have gotten jealous. "
                ja " I know Matte's just making friends, but seeing her with someone else... "
                ja " ...It makes my blood boil. I can't understand why. "
                ja " I don't...want to be some protective freak over her. "
                ja " I don't want to be some weirdo who says: "
                ja " 'Matte is mine, you can't have her!' "
                ja " That's just...weird. Why am I like this? "
                ja " I've never been like this before. It's...odd. "
                ja " I don't understand what I'm feeling. "
                ja " ...Why am I acting this way, even if I know that she probably doesn't like me back? "
                ja " My mom wouldn't even approve of my feelings right now. "
                ja " I have to be strong. Cold. Mean. "
                ja " I have to...get with a nice guy. "
                " As Jam mentions that she should be with a guy and not a girl, you could hear her voice sound... "
                " ...Disgusted. "
                ja " These feelings aren't right, is what mom would say. "
                menu:
                    " It's okay to feel that way towards Matte ":
                        $ jamlv += 5
                        ja " Is it really? "
                        ja " I don't think so. "
                        ja " Mom would kill me if she found out that I like a girl... "
                        ja " Probably would give me the worst death ever. "
                        ja " Uh, thanks for...trying to comfort me, [name]. "
                        ja " You did your best. "
                        hide jamsad at right with easeoutright
                        " ...She walked away. "
                        scene black with dissolve
                        " You spent the rest of the break chilling on the rooftop. "
                        " You were wondering if Jam and that boy would be alright, after what happened... "
                        " You could only hope they'd make up. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walk down from the rooftop, and you walk back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
                    " It's a normal feeling ":
                        $ jamlv += 5
                        ja " Is it really? "
                        ja " I don't think so. "
                        ja " Mom would kill me if she found out that I like a girl... "
                        ja " Probably would give me the worst death ever. "
                        ja " Uh, thanks for...trying to comfort me, [name]. "
                        ja " You did your best. "
                        hide jamsad at right with easeoutright
                        " ...She walked away. "
                        scene black with dissolve
                        " You spent the rest of the break chilling on the rooftop. "
                        " You were wondering if Jam and that boy would be alright, after what happened... "
                        " You could only hope they'd make up. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walk down from the rooftop, and you walk back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
    else:
        x " What do you MEAN you spent time with HER??? "
        x " ...!!!!! (I SPENT TIME WITH HER IN A FRIENDLY WAY, IDIOT!!) "
        x " A friendly way, really?! "
        x " Then tell me, why were you holding her hand??! "
        x " ??? (DOESN'T SHE DO THAT TO EVERYONE WHENEVER SHES WALKING WITH SOMEONE??) "
        x " You're just making up bullshit at this point. "
        x " !!! (I REALLY AM NOT!!) " with vpunch
        " The boy takes a deep breath, and pulls out his guitar... "
        hide jamangry at bottom
        show jamsurprised at left
        " ...And then starts rapidly playing it. "
        " The girl looks surprised...oh right, this guy can sometimes talk with his guitar. "
        " And it seems like he's real mad right now. "
        " Looks like he's calling her a lot of insults... "
        " You're starting to wonder how can people understand him. "
        " Game logic, I guess. "
        hide carmenangry at right with easeoutright
        show jamsurprised at center with move
        " The boy then eventually stops and he storms off. "
        x " ... "
        hide jamsurprised at bottom
        show jamsad at center
        x " ...Damn it. Not again. "
        menu:
            " Go and comfort the boy ":
                $ carmencomfort = True
                $ carmenlv += 15
                scene black with dissolve
                " You walked back down to the hallways, where that boy went. "
                " You wonder what was even happening in the first place to get them to be so mad at eachother... "
                " You'll ask him in a bit. "
                pause 1.0
                scene hallway with dissolve
                show carmenangry at center with easeinleft
                " You managed to catch up with him and asked him if he was okay. "
                x " ... "
                " ...He shook his head no. "
                " You then asked him what happened earlier. "
                x " ... "
                hide carmenangry at bottom
                show carmenneutral at center
                x " ... "
                " He pulls out his guitar once more before he starts playing a nice tune... "
                " And somehow, you're slowly starting to understand what he's saying through the guitar. "
                x " ...Me and Jam were fighting because... "
                x " ...Jam got jealous that I spent time with Matte, even though she just wanted to hang out with me... "
                x " ...I told Jam that I didn't want to start anything romantic with Matte, Matte's not even my type.. "
                x " I don't even like girls to begin with, yes I'm not straight, real shocker... "
                x " But, Jam didn't believe me and the arguing escalated... "
                x " ...I know Jam can get super jealous, but I've never seen her get this mad... "
                x " Jeez...she really needs to calm down sometimes... "
                x " Though, I doubt that you even understand me right now... "
                x " You're probably just listening to my tunes and nodding... "
                " You tell him that you understood him perfectly. "
                hide carmenneutral at bottom
                show carmensurprised at center
                x " Wait, you can? "
                x " I'm surprised that you could understand me this quickly... "
                $ carmenknow = True
                hide carmensurprised at bottom
                show carmenneutral at center
                ca " Ah, um...I'm Carmen, by the way. Nice to meet you. "
                ca " I'm mute, but...I usually use my guitar to speak. Or use sign language. "
                hide carmenneutral at bottom
                show carmenhappy at center
                ca " How interesting...I'm glad that you can understand me though. "
                ca " It makes me...happy. "
                ca " You know, some people don't understand what I'm saying sometimes. "
                ca " So I've always had someone to translate for me... "
                ca " And everytime someone starts understanding what I'm saying... "
                ca " ..It makes my day a whole lot better. "
                ca " I think you've known this before, but...I'm mute. "
                ca " It was hard trying to communicate with people at first, but... "
                ca " Now that everyone's starting to understand, I feel better. "
                ca " ...I don't know where this conversation is going at this point, but... "
                ca " Thank you, [name]. For being here. "
                " Carmen stops playing his guitar, and he pats your head. "
                " He seems really happy that you have understood him. "
                " You give him a headpat back. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Carmen. "
                " You just talked to him about random things to get him distracted... "
                " ...And not get reminded of what went on earlier. "
                " Wow, you're such a good friend! "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it's time for another class. "
                " You walk over to your classroom to get to your second class of the day. "
                pause 2.0
                jump ochealthclass2
            " Comfort the girl ":
                $ jamcomfort = True
                $ jamlv += 15
                x " ...I shouldn't have gotten jealous. "
                x " I know Matte's just making friends, but seeing her with someone else... "
                x " ...It makes my blood boil. I can't understand why. "
                x " I don't...want to be some protective freak over her. "
                x " I don't want to be some weirdo who says: "
                x " 'Matte is mine, you can't have her!' "
                x " That's just...weird. Why am I like this? "
                x " I've never been like this before. It's...odd. "
                x " I don't understand what I'm feeling. "
                x " ...Why am I acting this way, even if I know that she probably doesn't like me back? "
                x " My mom wouldn't even approve of my feelings right now. "
                x " I have to be strong. Cold. Mean. "
                x " I have to...get with a nice guy. "
                " As she mentions that she should be with a guy and not a girl, you could hear her voice sound... "
                " ...Disgusted. "
                x " These feelings aren't right, is what mom would say. "
                menu:
                    " It's okay to feel that way towards Matte ":
                        $ jamlv += 5
                        x " Is it really? "
                        x " I don't think so. "
                        x " Mom would kill me if she found out that I like a girl... "
                        x " Probably would give me the worst death ever. "
                        x " Uh, thanks for...trying to comfort me, [name]. "
                        x " You did your best. "
                        hide jamsad at right with easeoutright
                        " ...She walked away. "
                        scene black with dissolve
                        " You spent the rest of the break chilling on the rooftop. "
                        " You were wondering if that girl and that boy would be alright, after what happened... "
                        " You could only hope they'd make up. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walk down from the rooftop, and you walk back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
                    " It's a normal feeling ":
                        $ jamlv += 5
                        x " Is it really? "
                        x " I don't think so. "
                        x " Mom would kill me if she found out that I like a girl... "
                        x " Probably would give me the worst death ever. "
                        x " Uh, thanks for...trying to comfort me, [name]. "
                        x " You did your best. "
                        hide jamsad at right with easeoutright
                        " ...She walked away. "
                        scene black with dissolve
                        " You spent the rest of the break chilling on the rooftop. "
                        " You were wondering if that girl and that boy would be alright, after what happened... "
                        " You could only hope they'd make up. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walk down from the rooftop, and you walk back to your classroom for the next class. "
                        pause 2.0
                        jump ochealthclass2
label octlibrary1:
    # koa, jex and nox
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and spotted three of your classmates hanging out. "
    if pythonchallenge == True:
        $ pythoncode2 = True
        " Before you could walk over to one of them, you spotted a card on the ground, near a book... "
        " You picked it up and it had the number '2' on it. "
        " Time to save that in your pocket for later... "
        " One more code left, you're nearly there. "
        " Anyway, onto your classmates... "
    else:
        pass
    " Who do you talk to? "
    if koaknow,jexknow,noxknow == True:
        menu:
            " {image=koaicon} Koa {image=koaicon} ":
                jump pyschomode
            " {image=jexicon} Jex {image=jexicon} ":
                jump mochimochi
            " {image=noxicon} Nox {image=noxicon} ":
                jump lemonmeloncookie
    elif koaknow,jexknow == True and noxknow == False:
        menu:
            " {image=koaicon} Koa {image=koaicon} ":
                jump pyschomode
            " {image=jexicon} Jex {image=jexicon} ":
                jump mochimochi
            " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                jump lemonmeloncookie
    elif koaknow,noxknow == True and jexknow == False:
        menu:
            " {image=koaicon} Koa {image=koaicon} ":
                jump pyschomode
            " {image=jexicon} A very tall guy {image=jexicon} ":
                jump mochimochi
            " {image=noxicon} Nox {image=noxicon} ":
                jump lemonmeloncookie
    elif jexknow,noxknow == True and koaknow == False:
        menu:
            " {image=koaicon} An emo looking guy {image=koaicon} ":
                jump pyschomode
            " {image=jexicon} Jex {image=jexicon} ":
                jump mochimochi
            " {image=noxicon} Nox {image=noxicon} ":
                jump lemonmeloncookie
    elif koaknow == True and jexknow,noxknow == False:
        menu:
            " {image=koaicon} Koa {image=koaicon} ":
                jump pyschomode
            " {image=jexicon} A very tall guy {image=jexicon} ":
                jump mochimochi
            " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                jump lemonmeloncookie
    elif jexknow == True and koaknow,noxknow == False:
        menu:
            " {image=koaicon} An emo looking guy {image=koaicon} ":
                jump pyschomode
            " {image=jexicon} Jex {image=jexicon} ":
                jump mochimochi
            " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                jump lemonmeloncookie
    elif noxknow == True and koaknow,jexknow == False:
        menu:
            " {image=koaicon} An emo looking guy {image=koaicon} ":
                jump pyschomode
            " {image=jexicon} A very tall guy {image=jexicon} ":
                jump mochimochi
            " {image=noxicon} Nox {image=noxicon} ":
                jump lemonmeloncookie
    else:
        menu:
            " {image=koaicon} An emo looking guy {image=koaicon} ":
                jump pyschomode
            " {image=jexicon} A very tall guy {image=jexicon} ":
                jump mochimochi
            " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                jump lemonmeloncookie
    label pyschomode:
        $ koalv += 10
        if koaknow == True:
            " You were just about to walk up to Koa.. "
        else:
            " You were just about to walk up to him.. "
        " ..but you managed to slip and fall to the ground looney tunes style. "
        " You look around and it was because you didn't notice that the floor had been recently cleaned... "
        " And was wet. You should've been looking more carefully. "
        " You were just about to get yourself back up, but you saw someone lending you a hand. "
        " You looked up and saw that it was none other than the guy you were trying to talk to... "
        show koaneutral at center with dissolve
        if koaknow == True:
            k " ...Here, take my hand. "
            " You take his hand and slowly got up. "
            " You dusted yourself and made sure that you had nothing else on you... "
            " No, but really, falling like that was so embarrassing... "
            " Atleast you didn't fall and slip in the hallways. It would've been more embarrassing. "
            k " Are you okay? Did you not see the sign...? "
            " He pointed at the little thing that warned people that this spot had been recently cleaned and was wet. "
            " You scratched the back of your head. Yeah, you might be a bit blind. "
            k " ... "
            k " ...You should look more carefully next time. "
            k " I know that the sign is a bit small, but... "
            k " It would've been easy to see it with how bright it is. "
            k " ... "
            k " But, um...just be more careful, alright? "
            " You nodded. He was about to return to where he was sitting, but you followed him... "
            " ...And sat next to him. "
            k " ...Oh, did you want to talk to me about something? "
            " You nodded once more. "
            k " Well...okay. "
            scene black with dissolve
            " You spent the rest of the break talking with Koa. "
            " You were going to ask him about the bandage on one of his eyes... "
            " ...But he would change the topic and say that it's a story for another time. "
            " Maybe he's not comfortable with saying it yet? "
            " You understand though. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get up from where you were sitting and you walk back to your classroom for the next class. "
            pause 2.0
            jump ochealthclass2
        else:
            x " ...Here, take my hand. "
            " You take his hand and slowly got up. "
            " You dusted yourself and made sure that you had nothing else on you... "
            " No, but really, falling like that was so embarrassing... "
            " Atleast you didn't fall and slip in the hallways. It would've been more embarrassing. "
            x " Are you okay? Did you not see the sign...? "
            " He pointed at the little thing that warned people that this spot had been recently cleaned and was wet. "
            " You scratched the back of your head. Yeah, you might be a bit blind. "
            x " ... "
            x " ...You should look more carefully next time. "
            x " I know that the sign is a bit small, but... "
            x " It would've been easy to see it with how bright it is. "
            x " ... "
            x " But, um...just be more careful, alright? "
            " You nodded. He was about to return to where he was sitting, but you followed him... "
            " ...And sat next to him. "
            x " ...Oh, did you want to talk to me about something? "
            " You nodded once more. "
            x " Well...okay. "
            $ koaknow = True
            k " I'm Koa, by the way, it's nice to meet you. "
            scene black with dissolve
            " You spent the rest of the break talking with Koa. "
            " You were going to ask him about the bandage on one of his eyes... "
            " ...But he would change the topic and say that it's a story for another time. "
            " Maybe he's not comfortable with saying it yet? "
            " You understand though. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get up from where you were sitting and you walk back to your classroom for the next class. "
            pause 2.0
            jump ochealthclass2
    label mochimochi:
        " You walked up to him to take a good look on what he's doing... "
        " ..Wait, is he doing science stuff in the middle of the library? "
        " Is that allowed??? At this point, you're gonna have to believe that it is, considering how wild this school is. "
        " You then grab his attention by poking his shoulder. "
        show jexneutral at center with dissolve
        if jexknow == True:
            j " Hm? Ah, [name]. "
            j " You almost scared me there... "
            j " I'm simply just testing if this book about science stuff is actually spitting the truth. "
            j " Though, you did surprise me for a bit... "
            j " ...And you almost made me drop my materials... "
            j " But, I'm alright. Just a pinch of this... "
            j " And a little bit of that... "
            " Jex pours multiple things into one bottle. "
            " ...The substances in that bottle proceed to glow and let out a little glittering effect. "
            j " Interesting, so it does work. "
            j " I'll have to research this a bit more in my home... "
            " Jex closes the bottle and he puts it in his bag. "
            j " Anywho, while you're here... "
            j " Would you like to talk about something? "
            " You didn't have anything better to do, so you agreed. "
            j " Alrighty. "
            scene black with dissolve
            " You spent the rest of the break talking with Jex. "
            " Jex was talking about school stuff... "
            " ...While you were kinda just...zoning out. "
            " Pretty sure that he knew that you were zoning out, with how you looked. "
            " He looked like he didn't mind though. "
            play sound "audio/bellring.mp3"
            " The bell rang, interrupting your conversation with Jex. "
            " Also got you out of your zoning out session. "
            " You get up from where you were seated, and you walked back to your classroom for the next class. "
            pause 2.0
            jump ochealthclass2
        else:
            x " Hm? Ah, [name]. "
            x " You almost scared me there... "
            $ jexknow = True
            j " I'm Jex, by the way. We're classmates. As for what I'm doing... "
            j " I'm simply just testing if this book about science stuff is actually spitting the truth. "
            j " Though, you did surprise me for a bit... "
            j " ...And you almost made me drop my materials... "
            j " But, I'm alright. Just a pinch of this... "
            j " And a little bit of that... "
            " Jex pours multiple things into one bottle. "
            " ...The substances in that bottle proceed to glow and let out a little glittering effect. "
            j " Interesting, so it does work. "
            j " I'll have to research this a bit more in my home... "
            " Jex closes the bottle and he puts it in his bag. "
            j " Anywho, while you're here... "
            j " Would you like to talk about something? "
            " You didn't have anything better to do, so you agreed. "
            j " Alrighty. "
            scene black with dissolve
            " You spent the rest of the break talking with Jex. "
            " Jex was talking about school stuff... "
            " ...While you were kinda just...zoning out. "
            " Pretty sure that he knew that you were zoning out, with how you looked. "
            " He looked like he didn't mind though. "
            play sound "audio/bellring.mp3"
            " The bell rang, interrupting your conversation with Jex. "
            " Also got you out of your zoning out session. "
            " You get up from where you were seated, and you walked back to your classroom for the next class. "
            pause 2.0
            jump ochealthclass2
    label lemonmeloncookie:
        $ noxlv += 10
        " You walked to him and sat next to him to see what he was doing... "
        show noxneutral at center with easeinleft
        if noxknow == True:
            " You look closer and...no way! "
            " He's actually reading something - oh, never mind. "
            " He's looking at one singular page of a book and wastrying to get himself to read the entire thing. "
            hide noxneutral at bottom
            show noxsleepy at center
            " Though, it was obvious that he was struggling a lot. "
            " Maybe you should help him...but how? "
            " You then had an idea. You tapped Nox's shoulder and asked him what he was doing. "
            " Even though you already knew what he was doing in the first place. "
            n " Huh...? "
            n " Oh, um...Hi, [name]... "
            n " Mister Altrix told me to challenge myself by staying awake and reading an entire book, but... "
            n " As you can see...*yawn*...I'm stuck on the first page... "
            n " I don't know if you could help in this situation but...could you try...? "
            " You nodded, since you already had an idea in your mind. "
            " You told him that he just needed to read the story out loud... "
            " And everytime he tried to fall asleep, you'd just slap him awake! "
            " Wow, you have such a great idea! "
            n " ...Sounds a little...ehhh... "
            n " But, we could try.... "
            n " Alright, um...first words... "
            scene black with dissolve
            " You spent the rest of the break making sure that Nox could stay awake reading the entire book. "
            " At first, he couldn't go a single page without trying to fall asleep 3 times... "
            " But, the more you progressed...he was slowly starting to become less sleepy. "
            " Probably because you were kinda pressuring him to be awake otherwise you'd hit him a bit, but uh...it's progress nonetheless, I guess? "
            " Yeah. Atleast it's progress, or something. "
            play sound "audio/bellring.mp3"
            " The bell rang, interrupting your reading session with Nox. "
            " You get up from where you were sitting, and you walked back to your classroom for the next class. "
            pause 2.0
            jump ochealthclass2
        else:
            " You look closer and...no way! "
            " Someone who's actually reading something - oh, never mind. "
            " He's looking at one singular page of a book and wastrying to get himself to read the entire thing. "
            hide noxneutral at bottom
            show noxsleepy at center
            " Though, it was obvious that he was struggling a lot. "
            " Maybe you should help him...but how? "
            " You then had an idea. You tapped his shoulder and asked him what he was doing. "
            " Even though you already knew what he was doing in the first place. "
            x " Huh...? "
            x " Oh, um...Hi, [name]... "
            $ noxknow = True
            n " I don't think I've introduced myself to you yet, so...I'm Nox... "
            n " And uh... "
            n " Mister Altrix told me to challenge myself by staying awake and reading an entire book, but... "
            n " As you can see...*yawn*...I'm stuck on the first page... "
            n " I don't know if you could help in this situation but...could you try...? "
            " You nodded, since you already had an idea in your mind. "
            " You told him that he just needed to read the story out loud... "
            " And everytime he tried to fall asleep, you'd just slap him awake! "
            " Wow, you have such a great idea! "
            n " ...Sounds a little...ehhh... "
            n " But, we could try.... "
            n " Alright, um...first words... "
            scene black with dissolve
            " You spent the rest of the break making sure that Nox could stay awake reading the entire book. "
            " At first, he couldn't go a single page without trying to fall asleep 3 times... "
            " But, the more you progressed...he was slowly starting to become less sleepy. "
            " Probably because you were kinda pressuring him to be awake otherwise you'd hit him a bit, but uh...it's progress nonetheless, I guess? "
            " Yeah. Atleast it's progress, or something. "
            play sound "audio/bellring.mp3"
            " The bell rang, interrupting your reading session with Nox. "
            " You get up from where you were sitting, and you walked back to your classroom for the next class. "
            pause 2.0
            jump ochealthclass2

label ochealthclass2:
    scene classroom with dissolve
    " You walked into your classroom and you sat down on your seat, waiting for the teacher to arrive. "
    " As you were waiting, you looked around to see if you could find anything interesting... "
    " Unfortunately nothing interesting was currently going on. Boohoo. "
    " The teacher comes in a few minutes later, and you act like you totally weren't looking to see if anyone was doing anything funny. "
    " Gotta look good infront of the teachers, otherwise your ass might get beat. "
    " Unfortunate that some teachers aren't as cool as your PE teacher... "
    " ...Then again you probably wouldn't learn as quick if every teacher was cool. But who cares about that? "
    " The nerds, duh. "
    show altrixneutral at center with easeinright
    msa " Hello, class.. "
    msa " Just a reminder that we're going to be having an activity on wednesday! "
    msa " Please prepare your materials for tomorrow, thank you... "
    " Huh. You're gonna have to ask what the activity is for tomorrow. "
    " Looks like class is starting...time to pay attention. "
    " Or not. "
    scene black with dissolve
    " You had to take down a few notes for health class. "
    " That's all you really did, and nothing else. "
    " A little boring, yes, but atleast you did something that isn't zoning out for the entire class. "
    " Good job on actually doing something. "
    play sound "audio/bellring.mp3"
    " The bell rings, ending the class. "
    " You get up from your seat and walked back into the hallways... "
    " ...You're thinking about hanging out somewhere. "
    pause 2.0
    jump octbreak2

label octbreak2:
    scene hallway with dissolve
    " You walked into the hallways, thinking of hanging out somewhere... "
    " Where should you go? "
    menu:
        " {image=diskicon} The front of the school {image=koaicon} ":
            jump octfrontschool2
        " {image=carmenicon} The back of the school {image=notiveicon} ":
            jump octbackschool2
        " {image=sparkicon} The gym {image=temeroicon} ":
            jump octgym2
        " The cafeteria ":
            jump octcafe2
        " {image=yinyangicon} The rooftop {image=noxicon} ":
            jump octrooftop2
        " {image=miaicon} The library {image=matteicon} ":
            jump octlibrary2

label octfrontschool2:
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked into the front of the school and saw two of your classmates talking to eachother. "
    " Curious on what they're talking about, you walk over to them. "
    show diskneutral at left with easeinright
    show koaneutral at right with easeinright
    if diskknow == True and koaknow == True:
        d " Come on, Koa! I know you'll like it! "
        k " Disk, I know you want me to be there, and I would've loved to go, but... "
        k " ...I don't think I want to go to your party, and I don't think I even can. "
        hide diskneutral at bottom
        show disksad at left
        d " Awh, really? but why? "
        k " ...I kind of have three siblings to take care of. "
        hide disksad at bottom
        show diskneutral at left
        d " Woah, wait...THREE whole siblings? "
        k " Mhm. "
        " Koa didn't notice that you were standing there until he glanced at you and saw your shocked expression. "
        " I mean, who wouldn't be surprised at someone who had three whole siblings? "
        " Sure, there's some people who have way more siblings than that, but it's still surprising to hear. "
        k " Oh, look. [name] is here. "
        d " Hi [name]!! sorry, was just asking Koa if he wanted to come to my party this friday... "
        d " But I understand that you can't Koa!! I know that you gotta take care of your siblings... "
        d " On the topic of your siblings, could you tell us more about them? Please? "
        k " Eeeh, I think it's a conversation for another time... "
        hide diskneutral at bottom
        show diskhappy at left
        d " Pleeeasseee??? "
        k " Disk, come on - "
        scene black with dissolve
        " You spent the rest of the break talking to Disk and Koa. "
        " Well..it was more of listening to Disk yap about Koa's siblings... "
        " ...Asking questions about them and talking about his own little brother. "
        " Disk is a sweet soul. "
        " You don't know how Koa thinks of him though. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for the next class. "
        " You walk back into the school and go to the gym for the next class. "
        pause 2.0
        jump octpeclass2
    elif diskknow == True and koaknow == False:
        d " Come on, Koa! I know you'll like it! "
        x " Disk, I know you want me to be there, and I would've loved to go, but... "
        x " ...I don't think I want to go to your party, and I don't think I even can. "
        hide diskneutral at bottom
        show disksad at left
        d " Awh, really? but why? "
        x " ...I kind of have three siblings to take care of. "
        hide disksad at bottom
        show diskneutral at left
        d " Woah, wait...THREE whole siblings? "
        x " Mhm. "
        " The emo boy didn't notice that you were standing there until he glanced at you and saw your shocked expression. "
        " I mean, who wouldn't be surprised at someone who had three whole siblings? "
        " Sure, there's some people who have way more siblings than that, but it's still surprising to hear. "
        x " Oh, look. [name] is here. "
        x " Uh, hi there... "
        $ koaknow = True
        k " ...I'm Koa. "
        " Oh wow, that's it? That's all you're getting for an introduction? "
        " You didn't mind though. You understand the struggles of not cringing while introducing yourself. "
        d " Hi [name]!! sorry, was just asking Koa if he wanted to come to my party this friday... "
        d " But I understand that you can't Koa!! I know that you gotta take care of your siblings... "
        d " On the topic of your siblings, could you tell us more about them? Please? "
        k " Eeeh, I think it's a conversation for another time... "
        hide diskneutral at bottom
        show diskhappy at left
        d " Pleeeasseee??? "
        k " Disk, come on - "
        scene black with dissolve
        " You spent the rest of the break talking to Disk and Koa. "
        " Well..it was more of listening to Disk yap about Koa's siblings... "
        " ...Asking questions about them and talking about his own little brother. "
        " Disk is a sweet soul. "
        " You don't know how Koa thinks of him though. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for the next class. "
        " You walk back into the school and go to the gym for the next class. "
        pause 2.0
        jump octpeclass2
    elif diskknow == False and koaknow == True:
        x " Come on, Koa! I know you'll like it! "
        k " Disk, I know you want me to be there, and I would've loved to go, but... "
        k " ...I don't think I want to go to your party, and I don't think I even can. "
        hide diskneutral at bottom
        show disksad at left
        x " Awh, really? but why? "
        k " ...I kind of have three siblings to take care of. "
        hide disksad at bottom
        show diskneutral at left
        x " Woah, wait...THREE whole siblings? "
        k " Mhm. "
        " Koa didn't notice that you were standing there until he glanced at you and saw your shocked expression. "
        " I mean, who wouldn't be surprised at someone who had three whole siblings? "
        " Sure, there's some people who have way more siblings than that, but it's still surprising to hear. "
        k " Oh, look. [name] is here. "
        x " Oh, hey!! I don't think I got to introduce myself to [them]... "
        $ diskknow = True
        d " I'm Disk! It's nice to meet you! "
        d " Anyway... I was just asking Koa if he wanted to come to my party this friday... "
        d " But I understand that you can't Koa!! I know that you gotta take care of your siblings... "
        d " On the topic of your siblings, could you tell us more about them? Please? "
        k " Eeeh, I think it's a conversation for another time... "
        hide diskneutral at bottom
        show diskhappy at left
        d " Pleeeasseee??? "
        k " Disk, come on - "
        scene black with dissolve
        " You spent the rest of the break talking to Disk and Koa. "
        " Well..it was more of listening to Disk yap about Koa's siblings... "
        " ...Asking questions about them and talking about his own little brother. "
        " Disk is a sweet soul. "
        " You don't know how Koa thinks of him though. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for the next class. "
        " You walk back into the school and go to the gym for the next class. "
        pause 2.0
        jump octpeclass2
    else:
        x " Come on, Koa! I know you'll like it! "
        x " Disk, I know you want me to be there, and I would've loved to go, but... "
        x " ...I don't think I want to go to your party, and I don't think I even can. "
        hide diskneutral at bottom
        show disksad at left
        x " Awh, really? but why? "
        x " ...I kind of have three siblings to take care of. "
        hide disksad at bottom
        show diskneutral at left
        x " Woah, wait...THREE whole siblings? "
        x " Mhm. "
        " The emo boy didn't notice that you were standing there until he glanced at you and saw your shocked expression. "
        " I mean, who wouldn't be surprised at someone who had three whole siblings? "
        " Sure, there's some people who have way more siblings than that, but it's still surprising to hear. "
        x " Oh, look. [name] is here. "
        $ koaknow = True
        k " I don't think I got to introduce myself...I'm Koa. "
        x " Oh, hey!! I don't think I got to introduce myself to [them] either ... "
        $ diskknow = True
        d " I'm Disk! It's nice to meet you! "
        d " Anyway... I was just asking Koa if he wanted to come to my party this friday... "
        d " But I understand that you can't Koa!! I know that you gotta take care of your siblings... "
        d " On the topic of your siblings, could you tell us more about them? Please? "
        k " Eeeh, I think it's a conversation for another time... "
        hide diskneutral at bottom
        show diskhappy at left
        d " Pleeeasseee??? "
        k " Disk, come on - "
        scene black with dissolve
        " You spent the rest of the break talking to Disk and Koa. "
        " Well..it was more of listening to Disk yap about Koa's siblings... "
        " ...Asking questions about them and talking about his own little brother. "
        " Disk is a sweet soul. "
        " You don't know how Koa thinks of him though. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for the next class. "
        " You walk back into the school and go to the gym for the next class. "
        pause 2.0
        jump octpeclass2
label octbackschool2:
    # carmen notive
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and heard some nice guitar noises... "
    " Wondering who was playing the guitar so well, you decided to come over to where the noise was coming from. "
    show carmenneutral at left with easeinright
    show notiveneutral at right with easeinright
    " You looked around and spotted one of your classmates with a guitar, and the other just listening. "
    " You lowkey want to listen in, too... "
    " It takes them awhile to even notice you, but they eventually do. "
    if carmenknow == True and notiveknow == True:
        no " Oh, hiya, [name]! "
        no " I'm just listening to Carmen playing the guitar... "
        no " You should come here and listen, too! "
        no " Trust me, he's really good!! "
        ca " ...(shakes head) "
        no " Come on, Carmen! Don't downplay yourself like that! "
        ca " ... "
        no " I know [name]'s gonna like it, come on!! "
        ca " ...? "
        " Looks like Carmen's asking you if you wanted to hear him play a tune. "
        " Listen to him play? "
        menu:
            " Listen to Camren playing the guitar ":
                $ carmenlv += 5
                hide carmenneutral at bottom
                show carmensurprised at left
                hide notiveneutral at bottom
                show notivehappy at right
                ca " ...?!! "
                no " See, I told you! You're good, Carmen..! "
                no " If you tell yourself that you're not being good enough one more time... "
                no " ...I'm gonna have to strangle you, 'kay? "
                hide carmensurprised at bottom
                show carmenhappy at left
                ca " ... "
                " Carmen looks pretty excited to play a tune now. "
                " He picks up his guitar again...and starts playing his guitar once more. "
                " You sat down next to Notive and starting to listen to Carmen's nice song... "
                " ...You could listen to this forever with how nice he plays. "
                scene black with dissolve
                " You spent the rest of the break listening to Carmen playing his guitar. "
                " It was pretty nice... you even got sleepy at some point. "
                " Though you managed to keep yourself awake because you knew that the bell could ring at any moment... "
                " ...And you'd have to skedaddle all the way to the gym while you're still feeling dizzy and sleepy. "
                play sound "audio/bellring.mp3"
                " Speaking of the bell... it rang. "
                " You wished you could hear more, but you knew you couldn't unless if Carmen wanted to after class. "
                " You get up from where you were sitting and you walked to the gym for your next class. "
                pause 2.0
                jump octpeclass2
            " Nah, I'd rather listen to my own music ":
                no " Well...you do you, I guess. "
                no " But, just know this: Carmen's music is better!! totally!! "
                ca " ... "
                " For a moment there, it looked like Carmen silently told Notive to stop complimenting him... "
                " Looks like that worked, and Carmen started playing his guitar again. "
                " Meanwhile, you sat down somewhere else and put on your earphones so that you could listen to your playlist that you had downloaded. "
                " Time to listen to some nice tunes... "
                scene black with dissolve
                " You spent the rest of the break listening to music and vibing. "
                " Nothing much really happened as you just chilled. "
                " Which is surprising since I tell you everytime that something happens while you're chilling. "
                " Nice change, I guess? "
                " No idea, but uh...yeah. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, it somehow being loud enough to pause your listening session. "
                " You put your earphones back into your pocket and you get up from where you were sitting... "
                " ...And you walked to the gym for the next class. "
                pause 2.0
                jump octpeclass2
    elif carmenknow == True and notiveknow == False:
        x " Oh, hiya, [name]! "
        $ notiveknow = True
        no " I'm Notive, nice to meet you. Though, enough about me for a bit... "
        no " I'm just listening to Carmen playing the guitar... "
        no " You should come here and listen, too! "
        no " Trust me, he's really good!! "
        ca " ...(shakes head) "
        no " Come on, Carmen! Don't downplay yourself like that! "
        ca " ... "
        no " I know [name]'s gonna like it, come on!! "
        ca " ...? "
        " Looks like Carmen's asking you if you wanted to hear him play a tune. "
        " Listen to him play? "
        menu:
            " Listen to Camren playing the guitar ":
                $ carmenlv += 5
                hide carmenneutral at bottom
                show carmensurprised at left
                hide notiveneutral at bottom
                show notivehappy at right
                ca " ...?!! "
                no " See, I told you! You're good, Carmen..! "
                no " If you tell yourself that you're not being good enough one more time... "
                no " ...I'm gonna have to strangle you, 'kay? "
                hide carmensurprised at bottom
                show carmenhappy at left
                ca " ... "
                " Carmen looks pretty excited to play a tune now. "
                " He picks up his guitar again...and starts playing his guitar once more. "
                " You sat down next to Notive and starting to listen to Carmen's nice song... "
                " ...You could listen to this forever with how nice he plays. "
                scene black with dissolve
                " You spent the rest of the break listening to Carmen playing his guitar. "
                " It was pretty nice... you even got sleepy at some point. "
                " Though you managed to keep yourself awake because you knew that the bell could ring at any moment... "
                " ...And you'd have to skedaddle all the way to the gym while you're still feeling dizzy and sleepy. "
                play sound "audio/bellring.mp3"
                " Speaking of the bell... it rang. "
                " You wished you could hear more, but you knew you couldn't unless if Carmen wanted to after class. "
                " You get up from where you were sitting and you walked to the gym for your next class. "
                pause 2.0
                jump octpeclass2
            " Nah, I'd rather listen to my own music ":
                no " Well...you do you, I guess. "
                no " But, just know this: Carmen's music is better!! totally!! "
                ca " ... "
                " For a moment there, it looked like Carmen silently told Notive to stop complimenting him... "
                " Looks like that worked, and Carmen started playing his guitar again. "
                " Meanwhile, you sat down somewhere else and put on your earphones so that you could listen to your playlist that you had downloaded. "
                " Time to listen to some nice tunes... "
                scene black with dissolve
                " You spent the rest of the break listening to music and vibing. "
                " Nothing much really happened as you just chilled. "
                " Which is surprising since I tell you everytime that something happens while you're chilling. "
                " Nice change, I guess? "
                " No idea, but uh...yeah. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, it somehow being loud enough to pause your listening session. "
                " You put your earphones back into your pocket and you get up from where you were sitting... "
                " ...And you walked to the gym for the next class. "
                pause 2.0
                jump octpeclass2
    elif carmenknow == False and notiveknow == True:
        no " Oh, hiya, [name]! "
        no " I'm just listening to Carmen playing the guitar... "
        $ carmenknow = True
        no " Wait...hey! you haven't met him before! "
        no " You should come here and listen, too! "
        no " Trust me, he's really good!! Just listen!!"
        ca " ...(shakes head) "
        no " Come on, Carmen! Don't downplay yourself like that! "
        ca " ... "
        no " I know [name]'s gonna like it, come on!! "
        ca " ...? "
        " Looks like Carmen's asking you if you wanted to hear him play a tune. "
        " Listen to him play? "
        menu:
            " Listen to Camren playing the guitar ":
                $ carmenlv += 5
                hide carmenneutral at bottom
                show carmensurprised at left
                hide notiveneutral at bottom
                show notivehappy at right
                ca " ...?!! "
                no " See, I told you! You're good, Carmen..! "
                no " If you tell yourself that you're not being good enough one more time... "
                no " ...I'm gonna have to strangle you, 'kay? "
                hide carmensurprised at bottom
                show carmenhappy at left
                ca " ... "
                " Carmen looks pretty excited to play a tune now. "
                " He picks up his guitar again...and starts playing his guitar once more. "
                " You sat down next to Notive and starting to listen to Carmen's nice song... "
                " ...You could listen to this forever with how nice he plays. "
                scene black with dissolve
                " You spent the rest of the break listening to Carmen playing his guitar. "
                " It was pretty nice... you even got sleepy at some point. "
                " Though you managed to keep yourself awake because you knew that the bell could ring at any moment... "
                " ...And you'd have to skedaddle all the way to the gym while you're still feeling dizzy and sleepy. "
                play sound "audio/bellring.mp3"
                " Speaking of the bell... it rang. "
                " You wished you could hear more, but you knew you couldn't unless if Carmen wanted to after class. "
                " You get up from where you were sitting and you walked to the gym for your next class. "
                pause 2.0
                jump octpeclass2
            " Nah, I'd rather listen to my own music ":
                no " Well...you do you, I guess. "
                no " But, just know this: Carmen's music is better!! totally!! "
                ca " ... "
                " For a moment there, it looked like Carmen silently told Notive to stop complimenting him... "
                " Looks like that worked, and Carmen started playing his guitar again. "
                " Meanwhile, you sat down somewhere else and put on your earphones so that you could listen to your playlist that you had downloaded. "
                " Time to listen to some nice tunes... "
                scene black with dissolve
                " You spent the rest of the break listening to music and vibing. "
                " Nothing much really happened as you just chilled. "
                " Which is surprising since I tell you everytime that something happens while you're chilling. "
                " Nice change, I guess? "
                " No idea, but uh...yeah. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, it somehow being loud enough to pause your listening session. "
                " You put your earphones back into your pocket and you get up from where you were sitting... "
                " ...And you walked to the gym for the next class. "
                pause 2.0
                jump octpeclass2
    else:
        x " Oh, hiya, [name]! "
        $ notiveknow = True
        $ carmenknow =True
        no " I'm Notive, nice to meet you. But enough about me for a bit... "
        no " I'm just listening to Carmen playing the guitar... "
        no " Hold on, wait. I don't think you and Carmen have met before! "
        no " You should come here and listen, too! "
        no " Trust me, he's really good!! "
        ca " ...(shakes head) "
        no " Come on, Carmen! Don't downplay yourself like that! "
        ca " ... "
        no " I know [name]'s gonna like it, come on!! "
        ca " ...? "
        " Looks like Carmen's asking you if you wanted to hear him play a tune. "
        " Listen to him play? "
        menu:
            " Listen to Camren playing the guitar ":
                $ carmenlv += 5
                hide carmenneutral at bottom
                show carmensurprised at left
                hide notiveneutral at bottom
                show notivehappy at right
                ca " ...?!! "
                no " See, I told you! You're good, Carmen..! "
                no " If you tell yourself that you're not being good enough one more time... "
                no " ...I'm gonna have to strangle you, 'kay? "
                hide carmensurprised at bottom
                show carmenhappy at left
                ca " ... "
                " Carmen looks pretty excited to play a tune now. "
                " He picks up his guitar again...and starts playing his guitar once more. "
                " You sat down next to Notive and starting to listen to Carmen's nice song... "
                " ...You could listen to this forever with how nice he plays. "
                scene black with dissolve
                " You spent the rest of the break listening to Carmen playing his guitar. "
                " It was pretty nice... you even got sleepy at some point. "
                " Though you managed to keep yourself awake because you knew that the bell could ring at any moment... "
                " ...And you'd have to skedaddle all the way to the gym while you're still feeling dizzy and sleepy. "
                play sound "audio/bellring.mp3"
                " Speaking of the bell... it rang. "
                " You wished you could hear more, but you knew you couldn't unless if Carmen wanted to after class. "
                " You get up from where you were sitting and you walked to the gym for your next class. "
                pause 2.0
                jump octpeclass2
            " Nah, I'd rather listen to my own music ":
                no " Well...you do you, I guess. "
                no " But, just know this: Carmen's music is better!! totally!! "
                ca " ... "
                " For a moment there, it looked like Carmen silently told Notive to stop complimenting him... "
                " Looks like that worked, and Carmen started playing his guitar again. "
                " Meanwhile, you sat down somewhere else and put on your earphones so that you could listen to your playlist that you had downloaded. "
                " Time to listen to some nice tunes... "
                scene black with dissolve
                " You spent the rest of the break listening to music and vibing. "
                " Nothing much really happened as you just chilled. "
                " Which is surprising since I tell you everytime that something happens while you're chilling. "
                " Nice change, I guess? "
                " No idea, but uh...yeah. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, it somehow being loud enough to pause your listening session. "
                " You put your earphones back into your pocket and you get up from where you were sitting... "
                " ...And you walked to the gym for the next class. "
                pause 2.0
                jump octpeclass2
label octgym2:
    # spark temero
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym and spotted two of your classmates talking with eachother. "
    " They seemed like they were having a serious conversation... "
    " You can't help but wonder what they're talking about. You should probably listen to what they're talking about... "
    " ...Though, it's not good to listen into people's conversations especially when it's something serious. "
    " But then againnnn... "
    " Well, this is a hard choice. "
    " Should you listen into your classmates conversation? "
    menu:
        " Listen into their conversation ":
            $ sparklv += 5
            $ temerolv += 5
            $ sparklistenin = True
            $ temerolistenin = True
            " You hide behind a conveniently placed and shaped object that was near them... "
            " ...And started listening into their conversation. "
            " Hopefully you can hear them properly...but you ARE near them, so... "
            " Hey, look. They're starting to talk again. "
            " Time to lock in and listen. "
            if sparkknow == True and temeroknow == True:
                tm " ...I'm honestly a bit tired of doing all of this, you know? "
                show sparkneutral at right with easeinleft
                show temerosad at left with easeinleft
                sp " What - the job that Mister Clio gave us? "
                sp " Never thought I'd see the day where you'd get tired of all of that. "
                tm " I mean, it's fun, yes, but do we really have to...? "
                sp " I can't believe I'm saying this, but... "
                sp " It's the only way I'd get paid. I live alone, remember? "
                sp " I basically have to take care of myself and give me and {color=#ffae42}Scrap{/color} food... "
                sp " ...Without having any parents to give me all of that. "
                tm " Look, I get it dude. You don't got anyone to support you other than yourself. "
                tm " But hell, I've got everything - parents, my absolutely genius ideas... "
                tm " ...You know, the more I do this, the more boring it gets. "
                hide temerosad at bottom
                show temeroangry at left
                tm " It's all the same - I show them my form, they get scared and try to run away... "
                tm " Then I kill them. It's like the most predictable thing ever. "
                tm " I need something new for once in my life, maybe new murder methods? "
                sp " Mmm...yeah, perhaps. "
                sp " Have you tried melting them with acid and holding them down? "
                hide temeroangry at bottom
                show temeroneutral at left
                tm " Oooh! Haven't tried that one out yet. "
                tm " You know, you always have the best ideas, Spark. "
                hide sparkneutral at bottom
                show sparkhappy at right
                sp " Heh, I'm happy to help a friend in need. "
                scene black with dissolve
                " You stopped listening to them once they stoped talking about something interesting. "
                " You get up from where you were hiding and sat on the bleachers, pretending as if you didn't just eavesdrop on them. "
                " From what you've heard...they were given a job by Mister Clio. "
                " And judging from what Temero was saying, it was a job where they kill people... "
                " But why? You could only hope that they weren't killing students. "
                " Hopefully they aren't. Hopefully. "
                play sound "audio/bellring.mp3"
                " You were so deep into your thinking, that you didn't realize the bell had rung. "
                " Well, you're already in the gym. You can just get off the bleachers and wait for the teacher to arrive. "
                " You get up from where you were sitting and you waited with the other students for the PE teacher to come by. "
                pause 2.0
                jump octpeclass2
            elif sparkknow == True and temeroknow == False:
                x " ...I'm honestly a bit tired of doing all of this, you know? "
                show sparkneutral at right with easeinleft
                show temerosad at left with easeinleft
                sp " What - the job that Mister Clio gave us? "
                sp " Never thought I'd see the day where you'd get tired of all of that. "
                x " I mean, it's fun, yes, but do we really have to...? "
                sp " I can't believe I'm saying this, but... "
                sp " It's the only way I'd get paid. I live alone, remember? "
                sp " I basically have to take care of myself and give me and {color=#ffae42}Scrap{/color} food... "
                sp " ...Without having any parents to give me all of that. "
                x " Look, I get it dude. You don't got anyone to support you other than yourself. "
                x " But hell, I've got everything - parents, my absolutely genius ideas... "
                x " ...You know, the more I do this, the more boring it gets. "
                hide temerosad at bottom
                show temeroangry at left
                x " It's all the same - I show them my form, they get scared and try to run away... "
                x " Then I kill them. It's like the most predictable thing ever. "
                x " I need something new for once in my life, maybe new murder methods? "
                sp " Mmm...yeah, perhaps. "
                sp " Have you tried melting them with acid and holding them down? "
                hide temeroangry at bottom
                show temeroneutral at left
                x " Oooh! Haven't tried that one out yet. "
                x " You know, you always have the best ideas, Spark. "
                hide sparkneutral at bottom
                show sparkhappy at right
                sp " Heh, I'm happy to help a friend in need. "
                scene black with dissolve
                " You stopped listening to them once they stoped talking about something interesting. "
                " You get up from where you were hiding and sat on the bleachers, pretending as if you didn't just eavesdrop on them. "
                " From what you've heard...they were given a job by Mister Clio. "
                " And judging from what that girl was saying, it was a job where they kill people... "
                " But why? You could only hope that they weren't killing students. "
                " Hopefully they aren't. Hopefully. "
                play sound "audio/bellring.mp3"
                " You were so deep into your thinking, that you didn't realize the bell had rung. "
                " Well, you're already in the gym. You can just get off the bleachers and wait for the teacher to arrive. "
                " You get up from where you were sitting and you waited with the other students for the PE teacher to come by. "
                pause 2.0
                jump octpeclass2
            elif sparkknow == False and temeroknow == True:
                tm " ...I'm honestly a bit tired of doing all of this, you know? "
                show sparkneutral at right with easeinleft
                show temerosad at left with easeinleft
                x " What - the job that Mister Clio gave us? "
                x " Never thought I'd see the day where you'd get tired of all of that. "
                tm " I mean, it's fun, yes, but do we really have to...? "
                x " I can't believe I'm saying this, but... "
                x " It's the only way I'd get paid. I live alone, remember? "
                x " I basically have to take care of myself and give me and {color=#ffae42}Scrap{/color} food... "
                x " ...Without having any parents to give me all of that. "
                tm " Look, I get it dude. You don't got anyone to support you other than yourself. "
                tm " But hell, I've got everything - parents, my absolutely genius ideas... "
                tm " ...You know, the more I do this, the more boring it gets. "
                hide temerosad at bottom
                show temeroangry at left
                tm " It's all the same - I show them my form, they get scared and try to run away... "
                tm " Then I kill them. It's like the most predictable thing ever. "
                tm " I need something new for once in my life, maybe new murder methods? "
                x " Mmm...yeah, perhaps. "
                x " Have you tried melting them with acid and holding them down? "
                hide temeroangry at bottom
                show temeroneutral at left
                tm " Oooh! Haven't tried that one out yet. "
                tm " You know, you always have the best ideas, Spark. "
                hide sparkneutral at bottom
                show sparkhappy at right
                x " Heh, I'm happy to help a friend in need. "
                scene black with dissolve
                " You stopped listening to them once they stoped talking about something interesting. "
                " You get up from where you were hiding and sat on the bleachers, pretending as if you didn't just eavesdrop on them. "
                " From what you've heard...they were given a job by Mister Clio. "
                " And judging from what Temero was saying, it was a job where they kill people... "
                " But why? You could only hope that they weren't killing students. "
                " Hopefully they aren't. Hopefully. "
                play sound "audio/bellring.mp3"
                " You were so deep into your thinking, that you didn't realize the bell had rung. "
                " Well, you're already in the gym. You can just get off the bleachers and wait for the teacher to arrive. "
                " You get up from where you were sitting and you waited with the other students for the PE teacher to come by. "
                pause 2.0
                jump octpeclass2
            else:
                x " ...I'm honestly a bit tired of doing all of this, you know? "
                show sparkneutral at right with easeinleft
                show temerosad at left with easeinleft
                x " What - the job that Mister Clio gave us? "
                x " Never thought I'd see the day where you'd get tired of all of that. "
                x " I mean, it's fun, yes, but do we really have to...? "
                x " I can't believe I'm saying this, but... "
                x " It's the only way I'd get paid. I live alone, remember? "
                x " I basically have to take care of myself and give me and {color=#ffae42}Scrap{/color} food... "
                x " ...Without having any parents to give me all of that. "
                x " Look, I get it dude. You don't got anyone to support you other than yourself. "
                x " But hell, I've got everything - parents, my absolutely genius ideas... "
                x " ...You know, the more I do this, the more boring it gets. "
                hide temerosad at bottom
                show temeroangry at left
                x " It's all the same - I show them my form, they get scared and try to run away... "
                x " Then I kill them. It's like the most predictable thing ever. "
                x " I need something new for once in my life, maybe new murder methods? "
                x " Mmm...yeah, perhaps. "
                x " Have you tried melting them with acid and holding them down? "
                hide temeroangry at bottom
                show temeroneutral at left
                x " Oooh! Haven't tried that one out yet. "
                x " You know, you always have the best ideas, Spark. "
                hide sparkneutral at bottom
                show sparkhappy at right
                x " Heh, I'm happy to help a friend in need. "
                scene black with dissolve
                " You stopped listening to them once they stoped talking about something interesting. "
                " You get up from where you were hiding and sat on the bleachers, pretending as if you didn't just eavesdrop on them. "
                " From what you've heard...they were given a job by Mister Clio. "
                " And judging from what that girl was saying, it was a job where they kill people... "
                " But why? You could only hope that they weren't killing students. "
                " Hopefully they aren't. Hopefully. "
                play sound "audio/bellring.mp3"
                " You were so deep into your thinking, that you didn't realize the bell had rung. "
                " Well, you're already in the gym. You can just get off the bleachers and wait for the teacher to arrive. "
                " You get up from where you were sitting and you waited with the other students for the PE teacher to come by. "
                pause 2.0
                jump octpeclass2
        " Nah, let's not ":
            " Yeah, as much as you'd want to know... "
            " ...It's probably just best to leave them be. "
            " You went over to the bleaches and found a nice spot to hang out in... "
            " ...Then pulled out your phone and scrolled on it. "
            " Jesus christ, you gotta find something else to do other than scrolling on your phone whenever you don't have anything to do. "
            " But then again, I'm the narrator and I'm the one saying that you're doing all of this... "
            " ...Whatever, best to not think about it too much. "
            scene black with dissolve
            " You spent the rest of the break scrolling on your phone in the gym. "
            " Oh, hey, there's something interesting that popped up. "
            " No literally, it's just a post saying that something interesting popped up. "
            " How very interesting! "
            " ...Can you tell I'm running out of ideas on what to say. "
            play sound "audio/bellring.mp3"
            " The bell rings after a few minutes of you scrolling. "
            " Well, you're already in the gym. You can just get off the bleachers and wait for the teacher to arrive. "
            " You get up from where you were sitting and you waited with the other students for the PE teacher to come by. "
            pause 2.0
            jump octpeclass2
label octcafe2:
    # Orchid, all alone
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted one of your classmate just hanging out... "
    " ...Actually, now that you think about it, they kind of looked lonely with how they're sitting all alone. "
    " You should probably walk up to them and check on how they're doing. "
    if orchidknow == True:
        " Spend the break with Orchid? "
    else:
        " Spend the break with the scene kid? "
    menu:
        " Yeah, let's spend time with them ":
            $ orchidlv += 5
            show orchidneutral at center with easeinleft
            " You walked over to them and you asked them how they're doing. "
            if orchidknow == True:
                oc " Oh, um...hey [name]! "
                oc " I was actually in the middle of zoning, out, haha. "
                oc " Thanks for snapping me out of it. But, uh... "
                oc " ...How I'm doing? Ehh... "
                oc " Just feelin' a little lonely, no big deal now that you're here though. "
                oc " You know, usually I have someone to talk with. Have you noticed that? "
                " You may or may not have noticed that. "
                oc " Welll...I usually hang out with Koa. You know, that one emo guy that likes reading books? "
                oc " Yeah, that guy. He's actually the one kid in this school that I'm very comfortable with. "
                oc " Not because he's cool and all, but because he kind of treats me like I'm his kid or something. "
                oc " Sounds corny, but really - I'm speaking the truth. "
                oc " Must've been the instincts kicking in considering he has to take care of his three siblings. "
                oc " What? you look surprised that he has that much. "
                oc " Come on dude, look atthat one kid from that one show...what's it called again? "
                oc " The show with the family that has 11 kids or something? "
                oc " Eh, whatever, you get the idea. "
                oc " Look, he may seem like a nerd... "
                oc " But he's really nice, alright? "
                oc " Dude actually gives me help whenever I need it the most. "
                oc " And also does really well in distracting me whenever I have some of my... "
                oc " ...Moments, is what I'll call them. "
                scene black with dissolve
                " You spent the rest of the break talking with Orchid. "
                " You were glad that they weren't feeling lonely now that you were there with them. "
                " They did mention that they got lonely every now and then but didn't want to bother people... "
                " ...Which is honestly kind of sad. "
                " They probably should've just gone to that Koa person they were talking about. "
                " Then again, you wouldn't know how they would feel about that. "
                " Maybe you shouldn't think about this too much. "
                " Or I'm just saying this because I'm running out of ideas again. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for PE class. "
                " You get up from where you were sitting and you walked over to the gym for the next class. "
                pause 2.0
                jump octpeclass2
            else:
                x " Oh, um...hey [name]! "
                $ orchidknow = True
                oc " I'm Orchid, by the way. We're classmates. "
                oc " I was actually in the middle of zoning, out, haha. "
                oc " Thanks for snapping me out of it. But, uh... "
                oc " ...How I'm doing? Ehh... "
                oc " Just feelin' a little lonely, no big deal now that you're here though. "
                oc " You know, usually I have someone to talk with. Have you noticed that? "
                " You may or may not have noticed that. "
                oc " Welll...I usually hang out with Koa. You know, that one emo guy that likes reading books? "
                oc " Yeah, that guy. He's actually the one kid in this school that I'm very comfortable with. "
                oc " Not because he's cool and all, but because he kind of treats me like I'm his kid or something. "
                oc " Sounds corny, but really - I'm speaking the truth. "
                oc " Must've been the instincts kicking in considering he has to take care of his three siblings. "
                oc " What? you look surprised that he has that much. "
                oc " Come on dude, look atthat one kid from that one show...what's it called again? "
                oc " The show with the family that has 11 kids or something? "
                oc " Eh, whatever, you get the idea. "
                oc " Look, he may seem like a nerd... "
                oc " But he's really nice, alright? "
                oc " Dude actually gives me help whenever I need it the most. "
                oc " And also does really well in distracting me whenever I have some of my... "
                oc " ...Moments, is what I'll call them. "
                scene black with dissolve
                " You spent the rest of the break talking with Orchid. "
                " You were glad that they weren't feeling lonely now that you were there with them. "
                " They did mention that they got lonely every now and then but didn't want to bother people... "
                " ...Which is honestly kind of sad. "
                " They probably should've just gone to that Koa person they were talking about. "
                " Then again, you wouldn't know how they would feel about that. "
                " Maybe you shouldn't think about this too much. "
                " Or I'm just saying this because I'm running out of ideas again. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for PE class. "
                " You get up from where you were sitting and you walked over to the gym for the next class. "
                pause 2.0
                jump octpeclass2
        " Nah, I'd rather go get my own food and hang out on my own ":
            " Well, you do you. "
            " Let's go buy ourselves some food then. "
            scene black with dissolve
            " You spent the rest of the break just chilling out in your own seat and eating your food that you brought. "
            if orchidknow == True:
                " You could see Orchid looking at you every now and then... "
                " But, everytime you looked back at them, they would look away out of embarrassment. "
            else:
                " You could see the scene kid looking at you every now and then... "
                " But, everytime you looked back at them, they would look away out of embarrassment. "
            " They really look lonely, hm... "
            " You probably should've talked to them. Or not. "
            " I mean, you made this choice anyway. "
            " Why they didn't just come up to you? well... "
            " Let's just say that they've got those introvert issues. "
            play sound "audio/bellring.mp3"
            " You finished up your food as soon as the bell rang. Time for PE class.. "
            " You get up from where you were sitting and you walked over to the gym for the next class. "
            pause 2.0
            jump octpeclass2
label octrooftop2:
    # yinhui yangyi nox
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked up onto the rooftop and found three of your classmates hanging out. "
    " You wanted to talk to one of them...but who do you talk to? "
    if yinhuiknow,yangyiknow,noxknow == True:
        menu:
            " {image=yinyangicon} Talk to Yinhui {image=yinyangicon} ":
                jump ohhaveyou
            " {image=yinyangicon} Talk to Yangyi {image=yinyangicon} ":
                jump heardaboutthe
            " {image=noxicon} Talk to Nox {image=noxicon} ":
                jump flightlessbirdabout
    elif yinhuiknow,yangyiknow == True and noxknow == False:
        menu:
            " {image=yinyangicon} Talk to Yinhui {image=yinyangicon} ":
                jump ohhaveyou
            " {image=yinyangicon} Talk to Yangyi {image=yinyangicon} ":
                jump heardaboutthe
            " {image=noxicon} Talk to a sleepy looking guy {image=noxicon} ":
                jump flightlessbirdabout
    elif yinhuiknow,noxknow == True and yangyiknow == False:
        menu:
            " {image=yinyangicon} Talk to Yinhui {image=yinyangicon} ":
                jump ohhaveyou
            " {image=yinyangicon} Talk to a kind looking person {image=yinyangicon} ":
                jump heardaboutthe
            " {image=noxicon} Talk to Nox {image=noxicon} ":
                jump flightlessbirdabout
    elif yangyiknow,noxknow == True and yinhuiknow == False:
        menu:
            " {image=yinyangicon} Talk to a mean looking person {image=yinyangicon} ":
                jump ohhaveyou
            " {image=yinyangicon} Talk to Yangyi {image=yinyangicon} ":
                jump heardaboutthe
            " {image=noxicon} Talk to Nox {image=noxicon} ":
                jump flightlessbirdabout
    elif yinhuiknow == True and yangyiknow,noxknow == False:
        menu:
            " {image=yinyangicon} Talk to Yinhui {image=yinyangicon} ":
                jump ohhaveyou
            " {image=yinyangicon} Talk to a kind looking person {image=yinyangicon} ":
                jump heardaboutthe
            " {image=noxicon} Talk to a sleepy looking guy {image=noxicon} ":
                jump flightlessbirdabout
    elif yangyiknow == True and yinhuiknow,noxknow == False:
        menu:
            " {image=yinyangicon} Talk to a mean looking person {image=yinyangicon} ":
                jump ohhaveyou
            " {image=yinyangicon} Talk to Yangyi {image=yinyangicon} ":
                jump heardaboutthe
            " {image=noxicon} Talk to a sleepy looking guy {image=noxicon} ":
                jump flightlessbirdabout
    elif noxknow == True and yinhuiknow,yangyiknow == False:
        menu:
            " {image=yinyangicon} Talk to a mean looking person {image=yinyangicon} ":
                jump ohhaveyou
            " {image=yinyangicon} Talk to a kind looking person {image=yinyangicon} ":
                jump heardaboutthe
            " {image=noxicon} Talk to Nox {image=noxicon} ":
                jump flightlessbirdabout
    else:
        menu:
            " {image=yinyangicon} Talk to a mean looking person {image=yinyangicon} ":
                jump ohhaveyou
            " {image=yinyangicon} Talk to a kind looking person {image=yinyangicon} ":
                jump heardaboutthe
            " {image=noxicon} Talk to a sleepy looking person {image=noxicon} ":
                jump flightlessbirdabout
    label ohhaveyou:
        " You walked up to him and checked on what he was doing... "
        show yinhuineutral at center with easeinleft
        " You greeted him before you asked him what he was doing on the rooftop. "
        if yinhuiknow == True:
            yi " Oh, it's you. "
            yi " I guess I'm not really doing anything much... "
            yi " Other than watching that weird sleepy guy. "
            yi " I don't like the way he's looking at my brother. "
            " You look around to see the weird sleepy guy in question... "
            " He doesn't even look like he's doing anything wrong. "
            " He just looks more confused than weird. "
            yi " What? he doesn't look weird? well... "
            yi " He may look like that, but you'll never know what he's thinking. "
            yi " You may think that you're safe, but you're not safe in the other person's thoughts... "
            yi " ...You get what I'm trying to get at? "
            " You awkwardly nod your head before looking at the guy he was mentioning once more. "
            " ...He's walking away out of pure confusion. "
            " Looks like he heard everything the guy had to say about him. "
            " But this is also probably because he didn't want to make himself look more weird than he already did. "
            yi " ...Huh. He's walking away? "
            hide yinhuineutral at bottom
            show yinhuiheh at center
            yi " Looks like they got too intimidated by me. "
            yi " You know, my brother does call me a... "
            yi " ...An angry chihuahua, sometimes. "
            yi " Now I have absolutely no clue on what that is - but I'm sure it's something badass. "
            yi " Like a very cool strong dog type thing... "
            yi " Hell yeah. "
            yi " My brother really knows what he's talking about! "
            scene black with dissolve
            " You spent the rest of the break talking with Yinhui... "
            " ...You were also trying not to laugh at the fact that he didn't know what a chihuahua was. "
            " You decided not to tell him though, just to make it funnier. "
            " It's gonna be real funny the day he finds out. "
            play sound "audio/bellring.mp3"
            " The bell rings after a few minutes of talking. "
            " You walked down from the rooftop and went over to the gym for your next class. "
            pause 2.0
            jump octpeclass2
        else:
            x " Oh, it's you. "
            x " Well, uh...bes to introduce myself then. "
            x " Yang would be pissed if I didn't, since according to him I need to make some new friends or something... "
            $ yinhuiknow = True
            yi " I'm Yinhui. Yangyi's brother and Miss Jiayu's son. "
            yi " As for what I'm doing? "
            yi " I guess I'm not really doing anything much... "
            yi " Other than watching that weird sleepy guy. "
            yi " I don't like the way he's looking at my brother. "
            " You look around to see the weird sleepy guy in question... "
            " He doesn't even look like he's doing anything wrong. "
            " He just looks more confused than weird. "
            yi " What? he doesn't look weird? well... "
            yi " He may look like that, but you'll never know what he's thinking. "
            yi " You may think that you're safe, but you're not safe in the other person's thoughts... "
            yi " ...You get what I'm trying to get at? "
            " You awkwardly nod your head before looking at the guy he was mentioning once more. "
            " ...He's walking away out of pure confusion. "
            " Looks like he heard everything the guy had to say about him. "
            " But this is also probably because he didn't want to make himself look more weird than he already did. "
            yi " ...Huh. He's walking away? "
            hide yinhuineutral at bottom
            show yinhuiheh at center
            yi " Looks like they got too intimidated by me. "
            yi " You know, my brother does call me a... "
            yi " ...An angry chihuahua, sometimes. "
            yi " Now I have absolutely no clue on what that is - but I'm sure it's something badass. "
            yi " Like a very cool strong dog type thing... "
            yi " Hell yeah. "
            yi " My brother really knows what he's talking about! "
            scene black with dissolve
            " You spent the rest of the break talking with Yinhui... "
            " ...You were also trying not to laugh at the fact that he didn't know what a chihuahua was. "
            " You decided not to tell him though, just to make it funnier. "
            " It's gonna be real funny the day he finds out. "
            play sound "audio/bellring.mp3"
            " The bell rings after a few minutes of talking. "
            " You walked down from the rooftop and went over to the gym for your next class. "
            pause 2.0
            jump octpeclass2
    label heardaboutthe:
        " You walked up to him and checked on what he was doing... "
        " Suddenly you feel as if someone's staring right at you. "
        " You try your best to ignore it though. "
        show yangyineutral at center with easeinright
        " You greeted him before asking what he was doing. "
        if yangyiknow == True:
            ya " Hey there, [name]! "
            ya " I'm doing nothing much...just looking at the sky and all the clouds... "
            ya " Taking a breather, you know? "
            ya " The world can get a little stressful for me, so all I do whenever I feel that way is just... "
            ya " ...Look at nature or the sky. "
            hide yangyineutral at bottom
            show yangyihappy at center
            ya " It's calming, really! You should try it out! "
            " You said that you would, but then you commented about the fact that you're feeling watched. "
            hide yangyihappy at bottom
            show yangyineutral at center
            ya " Oh, that? "
            ya " Hehe, that's just my brother keeping an eye on you. "
            ya " Makin' sure that you're not gonna do anything suspicious to me... "
            ya " He's always like that, don't worry! "
            ya " There are times where it gets out of hand, though... "
            ya " Sometimes he would get too mad to the point he would just... "
            ya " Start acting like a very angry chihuahua. "
            ya " He's scared a lot of people, but I can't help but find it funny and cute! "
            ya " Though I do get concerned after a bit. "
            ya " Another thing - he doesn't know what a chihuahua is. "
            ya " I plan not to tell him just so that I could poke fun of him in the future. "
            ya " It's gonna be great, trust me when I tell you that! "
            ya " ...Now that I think about it... "
            ya " He's been staring at Nox for a good while now...well, until you came and talked to me. "
            ya " Hopefuly he isn't gonna maul him later... "
            ya " ...Just for taking a quick look at me. "
            scene black with dissolve
            " You spent the rest of the break talking with Yangyi. "
            " And as you were talking with him, you of course, felt the very intense stare of his brother on your back. "
            " You know that he was probably plotting your death in many ways, but you tried not to care. "
            " Tried not to care because you wanted to look cool and you wanted to ragebait him. "
            " And that looked like it worked...a bit. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, interrupting your conversation with Yangyi. "
            " You walked down from the rooftop and went over to the gym for your next class. "
            pause 2.0
            jump octpeclass2
        else:
            x " Hey there, [name]! "
            x " Oh my, I haven't introduced myself to you yet, have I? "
            $ yangyiknow = True
            ya " Well...I'm Yangyi! The brother of Yinhui, and Miss Jiayu's son! "
            ya " As for what I'm doing? "
            ya " I'm doing nothing much...just looking at the sky and all the clouds... "
            ya " Taking a breather, you know? "
            ya " The world can get a little stressful for me, so all I do whenever I feel that way is just... "
            ya " ...Look at nature or the sky. "
            hide yangyineutral at bottom
            show yangyihappy at center
            ya " It's calming, really! You should try it out! "
            " You said that you would, but then you commented about the fact that you're feeling watched. "
            hide yangyihappy at bottom
            show yangyineutral at center
            ya " Oh, that? "
            ya " Hehe, that's just my brother keeping an eye on you. "
            ya " Makin' sure that you're not gonna do anything suspicious to me... "
            ya " He's always like that, don't worry! "
            ya " There are times where it gets out of hand, though... "
            ya " Sometimes he would get too mad to the point he would just... "
            ya " Start acting like a very angry chihuahua. "
            ya " He's scared a lot of people, but I can't help but find it funny and cute! "
            ya " Though I do get concerned after a bit. "
            ya " Another thing - he doesn't know what a chihuahua is. "
            ya " I plan not to tell him just so that I could poke fun of him in the future. "
            ya " It's gonna be great, trust me when I tell you that! "
            ya " ...Now that I think about it... "
            ya " He's been staring at Nox for a good while now...well, until you came and talked to me. "
            ya " Hopefuly he isn't gonna maul him later... "
            ya " ...Just for taking a quick look at me. "
            scene black with dissolve
            " You spent the rest of the break talking with Yangyi. "
            " And as you were talking with him, you of course, felt the very intense stare of his brother on your back. "
            " You know that he was probably plotting your death in many ways, but you tried not to care. "
            " Tried not to care because you wanted to look cool and you wanted to ragebait him. "
            " And that looked like it worked...a bit. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, interrupting your conversation with Yangyi. "
            " You walked down from the rooftop and went over to the gym for your next class. "
            pause 2.0
            jump octpeclass2
    label flightlessbirdabout:
        " You walked up to him to see how he's doing... "
        " Getting a closer look onto his face, he seemed to be...very confused and uncomfortable. "
        " Wonder why that is. You're gonna have to ask him if he's alright. "
        show noxsleepy at center with easeinleft
        " Once you got close enough to him, you asked him if he's doing okay. "
        " ...Actually it was pretty obvious on what he was feeling right now, but you still had to ask. "
        if noxknow == True:
            n " ...I'm doing fine, thanks... "
            n " But...*yawn*...ever since I woke up from my nap... "
            n " This guy's been staring down at me real hard... "
            n " I don't know if I did something wrong or not...I mean, I was sleeping... "
            n " Was I sleep talking or something...? I dunnooo... "
            " You look around to find the guy he was mentioning... "
            " Looks like they've got their eyes on something else now. "
            hide noxsleepy at bottom
            show noxneutral at center
            n " Oh, hey...they stopped looking... "
            n " ...Mmm... I don't know what to talk about now... "
            n " How about...the dream I had...? "
            n " It's nothing interesting though, so... "
            n " We could talk about something else...if that's what you want... "
            menu:
                " Listen to Nox's dream ":
                    $ noxlv += 5
                    n " Mmm...okay... "
                    n " So... "
                    scene black with dissolve
                    " You spent the rest of the break listening to Nox talk about his dream. "
                    " You could tell that he was trying his best not to fall asleep as he was talking to you. "
                    " He would often repeat things that he had already said, thinking he hasn't mentioned them before. "
                    " You would reassure him that he's already told him this though. "
                    " ...You're starting to worry about his sleep schedule for a bit. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked down from the rooftop and went over to the gym for your next class. "
                    pause 2.0
                    jump octpeclass2
                " Nah, let's talk about something else ":
                    n " Mmm...okay... "
                    n " So... "
                    scene black with dissolve
                    " You spent the rest of the break talking to Nox. "
                    " Just...talking about random things that comes up in yours or Nox's head. "
                    " Like you'd be talking to him about drawings and then... "
                    " ...You guys just suddenly start talking about sans fan girls. "
                    " You two have very interesting minds. "
                    " Very, very interesting minds. "
                    " ...Look, what am I supposed to say here? "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked down from the rooftop and went over to the gym for your next class. "
                    pause 2.0
                    jump octpeclass2
        else:
            x " ...I'm doing fine, thanks... "
            $ noxknow = True
            n " ...I'm Nox, by the way... "
            n " But...*yawn*...ever since I woke up from my nap... "
            n " This guy's been staring down at me real hard... "
            n " I don't know if I did something wrong or not...I mean, I was sleeping... "
            n " Was I sleep talking or something...? I dunnooo... "
            " You look around to find the guy he was mentioning... "
            " Looks like they've got their eyes on something else now. "
            hide noxsleepy at bottom
            show noxneutral at center
            n " Oh, hey...they stopped looking... "
            n " ...Mmm... I don't know what to talk about now... "
            n " How about...the dream I had...? "
            n " It's nothing interesting though, so... "
            n " We could talk about something else...if that's what you want... "
            menu:
                " Listen to Nox's dream ":
                    $ noxlv += 5
                    n " Mmm...okay... "
                    n " So... "
                    scene black with dissolve
                    " You spent the rest of the break listening to Nox talk about his dream. "
                    " You could tell that he was trying his best not to fall asleep as he was talking to you. "
                    " He would often repeat things that he had already said, thinking he hasn't mentioned them before. "
                    " You would reassure him that he's already told him this though. "
                    " ...You're starting to worry about his sleep schedule for a bit. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked down from the rooftop and went over to the gym for your next class. "
                    pause 2.0
                    jump octpeclass2
                " Nah, let's talk about something else ":
                    n " Mmm...okay... "
                    n " So... "
                    scene black with dissolve
                    " You spent the rest of the break talking to Nox. "
                    " Just...talking about random things that comes up in yours or Nox's head. "
                    " Like you'd be talking to him about drawings and then... "
                    " ...You guys just suddenly start talking about sans fan girls. "
                    " You two have very interesting minds. "
                    " Very, very interesting minds. "
                    " ...Look, what am I supposed to say here? "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked down from the rooftop and went over to the gym for your next class. "
                    pause 2.0
                    jump octpeclass2
label octlibrary2:
    # mia matte
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and spotted two of your classmates talking to eachother. "
    " Curious as ever, you decided to walk up to them and see what they're talking about. "
    " Now that you look more closely, it seems like a one-sided argument or something. "
    " Still doesn't stop your curiousity though. "
    show miaangry at left with easeinright
    show mattesad at right with easeinright
    if miaknow == True and matteknow == True:
        m " Why didn't you include me in your painting earlier, huuuh?! "
        ma " Look Mia... "
        ma " I know that you're upset, but I didn't know that you wanted to be in the painting, okay? "
        ma " You looked busy, so i kind of just thought that I shouldn't bother you and all... "
        m " You could've just asked me!! "
        m " I would've been fine if you just did that instead of using someone as lame as Spark to be in the painting! "
        ma " Woah there, girly. Spark's a cool guy. "
        ma " You're cool too, you know. Everyone's cool. "
        ma " No need to get so mad about something like this... "
        " Looks like she needs some help trying to calm Mia down. "
        " Should you go and help her? "
        menu:
            " Help her deal with Mia ":
                $ mattelv += 5
                " You cut Mia off - who was about to say something mean again. "
                " You then suggested that you and Matte could draw Mia to calm her down. "
                " You said that yours wasn't gonna be the best, but you're going to atleast try... "
                " ...If that's what makes her happy. "
                m " ... "
                hide miaangry at bottom
                show miahappy at left
                m " Awww, [name]!! of course I'll let you draw me!! "
                m " Quick, Matte, getyour sketchbook and pencil!! Draw me!! "
                hide mattesad at bottom
                show matteneutral at center
                ma " Alright, alright... "
                ma " Here [name], a pencil to draw with and some paper. "
                ma " You're lucky that I have some extra. "
                scene black with dissolve
                " You spent the rest of the break drawing Mia with Matte. "
                " Mia lookedwayyy happier than she was earlier... "
                " ...Probably because she's finally getting some attention out of the two of you. "
                " One day she'll look back at how she used to act and she's gonna make fun of herself. "
                play sound "audio/bellring.mp3"
                " You finish drawing her the moment the bell rings. "
                " You and Matte give her your drawings and you guys walked to the gym for the next class. "
                pause 2.0
                jump octpeclass2
            " Nah, I'd rather do something else ":
                " You decided not to help Matte. "
                " Instead, you just sat down on a nearby chair and watched everything go down. "
                scene black with dissolve
                " You spent the rest of the break watching Matte deal with Mia. "
                " You honestly just couldn't be bothered to help her. "
                " Or you were just curious to see what could happen if you picked this option. "
                " Or you just genuinely didn't want to help Matte. "
                " I mean, kind of reasonable if you're feeling lazy or something. "
                " ... "
                " Okay yeah I have nothing to say here, let's skip to the next class. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for PE class. "
                " You get up from where you were sitting and you walked to the gym for your next class."
                pause 2.0
                jump octpeclass2
    elif miaknow == True and matteknow == False:
        m " Why didn't you include me in your painting earlier, huuuh?! "
        x " Look Mia... "
        x " I know that you're upset, but I didn't know that you wanted to be in the painting, okay? "
        x " You looked busy, so i kind of just thought that I shouldn't bother you and all... "
        m " You could've just asked me!! "
        m " I would've been fine if you just did that instead of using someone as lame as Spark to be in the painting! "
        x " Woah there, girly. Spark's a cool guy. "
        x " You're cool too, you know. Everyone's cool. "
        x " No need to get so mad about something like this... "
        " Looks like she needs some help trying to calm Mia down. "
        " Should you go and help her? "
        menu:
            " Help her deal with Mia ":
                $ mattelv += 5
                " You cut Mia off - who was about to say something mean again. "
                " You then suggested that you and the artsy girl could draw Mia to calm her down. "
                " You said that yours wasn't gonna be the best, but you're going to atleast try... "
                " ...If that's what makes her happy. "
                m " ... "
                hide miaangry at bottom
                show miahappy at left
                m " Awww, [name]!! of course I'll let you draw me!! "
                m " Quick, Matte, getyour sketchbook and pencil!! Draw me!! "
                hide mattesad at bottom
                show matteneutral at center
                $ matteknow = True
                ma " Alright, alright... "
                ma " Here [name], a pencil to draw with and some paper. "
                ma " You're lucky that I have some extra. "
                scene black with dissolve
                " You spent the rest of the break drawing Mia with Matte. "
                " Mia lookedwayyy happier than she was earlier... "
                " ...Probably because she's finally getting some attention out of the two of you. "
                " One day she'll look back at how she used to act and she's gonna make fun of herself. "
                play sound "audio/bellring.mp3"
                " You finish drawing her the moment the bell rings. "
                " You and Matte give her your drawings and you guys walked to the gym for the next class. "
                pause 2.0
                jump octpeclass2
            " Nah, I'd rather do something else ":
                " You decided not to help the artsy girl. "
                " Instead, you just sat down on a nearby chair and watched everything go down. "
                scene black with dissolve
                " You spent the rest of the break watching that artsy girl deal with Mia. "
                " You honestly just couldn't be bothered to help her. "
                " Or you were just curious to see what could happen if you picked this option. "
                " Or you just genuinely didn't want to help Matte. "
                " I mean, kind of reasonable if you're feeling lazy or something. "
                " ... "
                " Okay yeah I have nothing to say here, let's skip to the next class. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for PE class. "
                " You get up from where you were sitting and you walked to the gym for your next class."
                pause 2.0
                jump octpeclass2
    elif miaknow == False and matteknow == True:
        x " Why didn't you include me in your painting earlier, huuuh?! "
        $ miaknow = True
        ma " Look Mia... "
        ma " I know that you're upset, but I didn't know that you wanted to be in the painting, okay? "
        ma " You looked busy, so i kind of just thought that I shouldn't bother you and all... "
        m " You could've just asked me!! "
        m " I would've been fine if you just did that instead of using someone as lame as Spark to be in the painting! "
        ma " Woah there, girly. Spark's a cool guy. "
        ma " You're cool too, you know. Everyone's cool. "
        ma " No need to get so mad about something like this... "
        " Looks like she needs some help trying to calm Mia down. "
        " Should you go and help her? "
        menu:
            " Help her deal with Mia ":
                $ mattelv += 5
                " You cut Mia off - who was about to say something mean again. "
                " You then suggested that you and Matte could draw Mia to calm her down. "
                " You said that yours wasn't gonna be the best, but you're going to atleast try... "
                " ...If that's what makes her happy. "
                m " ... "
                hide miaangry at bottom
                show miahappy at left
                m " Awww, [name]!! of course I'll let you draw me!! "
                m " Quick, Matte, getyour sketchbook and pencil!! Draw me!! "
                hide mattesad at bottom
                show matteneutral at center
                ma " Alright, alright... "
                ma " Here [name], a pencil to draw with and some paper. "
                ma " You're lucky that I have some extra. "
                scene black with dissolve
                " You spent the rest of the break drawing Mia with Matte. "
                " Mia lookedwayyy happier than she was earlier... "
                " ...Probably because she's finally getting some attention out of the two of you. "
                " One day she'll look back at how she used to act and she's gonna make fun of herself. "
                play sound "audio/bellring.mp3"
                " You finish drawing her the moment the bell rings. "
                " You and Matte give her your drawings and you guys walked to the gym for the next class. "
                pause 2.0
                jump octpeclass2
            " Nah, I'd rather do something else ":
                " You decided not to help Matte. "
                " Instead, you just sat down on a nearby chair and watched everything go down. "
                scene black with dissolve
                " You spent the rest of the break watching Matte deal with Mia. "
                " You honestly just couldn't be bothered to help her. "
                " Or you were just curious to see what could happen if you picked this option. "
                " Or you just genuinely didn't want to help Matte. "
                " I mean, kind of reasonable if you're feeling lazy or something. "
                " ... "
                " Okay yeah I have nothing to say here, let's skip to the next class. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for PE class. "
                " You get up from where you were sitting and you walked to the gym for your next class."
                pause 2.0
                jump octpeclass2
    else:
        x " Why didn't you include me in your painting earlier, huuuh?! "
        x " Look Mia... "
        $ miaknow = True
        x " I know that you're upset, but I didn't know that you wanted to be in the painting, okay? "
        x " You looked busy, so i kind of just thought that I shouldn't bother you and all... "
        m " You could've just asked me!! "
        m " I would've been fine if you just did that instead of using someone as lame as Spark to be in the painting! "
        x " Woah there, girly. Spark's a cool guy. "
        x " You're cool too, you know. Everyone's cool. "
        x " No need to get so mad about something like this... "
        " Looks like she needs some help trying to calm Mia down. "
        " Should you go and help her? "
        menu:
            " Help her deal with Mia ":
                $ mattelv += 5
                " You cut Mia off - who was about to say something mean again. "
                " You then suggested that you and the artsy girl could draw Mia to calm her down. "
                " You said that yours wasn't gonna be the best, but you're going to atleast try... "
                " ...If that's what makes her happy. "
                m " ... "
                hide miaangry at bottom
                show miahappy at left
                m " Awww, [name]!! of course I'll let you draw me!! "
                m " Quick, Matte, getyour sketchbook and pencil!! Draw me!! "
                hide mattesad at bottom
                show matteneutral at center
                $ matteknow = True
                ma " Alright, alright... "
                ma " Here [name], a pencil to draw with and some paper. "
                ma " You're lucky that I have some extra. "
                scene black with dissolve
                " You spent the rest of the break drawing Mia with Matte. "
                " Mia lookedwayyy happier than she was earlier... "
                " ...Probably because she's finally getting some attention out of the two of you. "
                " One day she'll look back at how she used to act and she's gonna make fun of herself. "
                play sound "audio/bellring.mp3"
                " You finish drawing her the moment the bell rings. "
                " You and Matte give her your drawings and you guys walked to the gym for the next class. "
                pause 2.0
                jump octpeclass2
            " Nah, I'd rather do something else ":
                " You decided not to help the artsy girl. "
                " Instead, you just sat down on a nearby chair and watched everything go down. "
                scene black with dissolve
                " You spent the rest of the break watching that artsy girl deal with Mia. "
                " You honestly just couldn't be bothered to help her. "
                " Or you were just curious to see what could happen if you picked this option. "
                " Or you just genuinely didn't want to help Matte. "
                " I mean, kind of reasonable if you're feeling lazy or something. "
                " ... "
                " Okay yeah I have nothing to say here, let's skip to the next class. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for PE class. "
                " You get up from where you were sitting and you walked to the gym for your next class."
                pause 2.0
                jump octpeclass2
label octpeclass2:
    scene gym with dissolve
    " You looked around in the gym and waited for the PE teacher to arrive. "
    " You're pretty sure you're gonna hear the doors bust open again, considering how all your classmates looked like they were used to it... "
    " And BOOM! the door busts open again." with vpunch
    " Looks like this is a normal thing...you're going to have to get used to this then. "
    show solneutral at center with easeinleft
    msso " Heyooo, fam!! "
    msso " You all better got a lot of energy today, because we're going to do a LOT of work. "
    msso " Now I know that you all hate this, and trust me, I hate making you guys go through pain. "
    msso " BUT! I gotta do this since it's my job of being a teacher. "
    msso " Can't risk being paid low for makingyou guys slack off in my class, you know? "
    msso " Oh! and before we start our workout session today, or in otherwords, our class... "
    msso " A friendly reminder that we're going to be having a activity on friday! "
    msso " I expect you all to be on high energy that day! Especially since little Disky boy over there is gonna be throwing a party. "
    msso " And if I even see one of you on low energy... "
    msso " I'm throwing buckets of cold water on all of you!! Trust me, I'll do it! "
    msso " Anywho...let's get on with class! "
    scene black with dissolve
    " PE class wasn't that interesting. "
    " You just had to do a few things the teacher told you to do... "
    " ...Like run around the gym 2 times. "
    " And also copy things down since you heard that if you managed to copy everything you're gonna get candy. "
    " Mister Sol was going a bit fast at first, but you ended up getting used to it and copied everything he had to show for today. "
    play sound "audio/bellring.mp3"
    " Once class was over, you handed him your notebook and he checked your work... "
    " ...Before he gave you two whole chocolate bars! "
    " He's definitely one of the cool teachers, that's for sure. "
    " You headed out of the gym so that you could chill in the hallways once more. "
    pause 2.0
    jump octbreak3

label octbreak3:
    # add stuff later
    scene hallway with dissolve
    " You wanted to hangout somewhere for this break like you usually do. "
    " Where do you want to go? "
    menu:
        " {image=matteicon} The front of the school {image=jacobicon} ":
            jump octfrontschool3
        " {image=jamicon} The back of the school {image=orchidicon} ":
            jump octbackschool3
        " {image=quinnicon} Back into the gym {image=yinyangicon} ":
            jump octgym3
        " The cafeteria ":
            jump octcafe3
        " {image=koaicon} The rooftop {image=miaicon} ":
            jump octrooftop3
        " {image=sparkicon} The library {image=carmenicon} ":
            jump octlibrary3
label octfrontschool3:
    # matte and jacob
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school and spotted two of your classmates chilling. "
    " You wanted to talk to one of them, as always. "
    " Who do you talk to for this break? "
    if matteknow == True and jacobknow == True:
        menu:
            " {image=matteicon} Talk with Matte {image=matteicon} ":
                jump sinking
            " {image=jacobicon} Talk with Jacob {image=jacobicon} ":
                jump island
    elif matteknow == True and jacobknow == False:
        menu:
            " {image=matteicon} Talk with Matte {image=matteicon} ":
                jump sinking
            " {image=jacobicon} Talk with a guy with goggles and a bandana {image=jacobicon} ":
                jump island
    elif matteknow == False and jacobknow == True:
        menu:
            " {image=matteicon} Talk with an artsy girl {image=matteicon} ":
                jump sinking
            " {image=jacobicon} Talk with Jacob {image=jacobicon} ":
                jump island
    else:
        menu:
            " {image=matteicon} Talk with an artsy girl {image=matteicon} ":
                jump sinking
            " {image=jacobicon} Talk with a guy with goggles and a bandana {image=jacobicon} ":
                jump island
    label sinking:
        " You walked up to her to see what she was up to. "
        show matteneutral at center with easeinleft
        if matteknow == True:
            ma " Hmmm...oh, hey [name]! "
            ma " Sorry, was just thinking about a few things. "
            ma " You see...one of my friends have been really upset lately. "
            ma " I don't know if you know her, but her name's Jam! "
            ma " She's a really cool person...defended me whenever I got into arguments accidentally... "
            ma " ...Helped me put my things into my locker whenever I was struggling... "
            ma " A real nice girl, even though she looks mean on the outside! "
            hide matteneutral at bottom
            show mattesad at center
            ma " But uh... "
            ma " Ever since I told her that I hung out with one of our classmates last night... "
            ma " ...She's been acting off. She keeps telling me that she's fine when I know that she isn't. "
            ma " I wonder what she thought when I told her... "
            ma " I just wanted someone to talk to as I was painting... "
            hide mattesad at bottom
            show matteneutral at center
            ma " Plus, it was nice hearing Carmen's guitar as I painted! gives an aesthetic vibe, don't you think? "
            ma " ...Errh, back to the original topic... "
            ma " What should I do to cheer Jam up? You have any ideas? "
            menu:
                " Tell her your idea ":
                    $ mattelv += 5
                    " You told her your idea... "
                    " ...Which was getting Jam a game that she really wanted. "
                    " And hanging out at Jam's house, if Jam was available. "
                    " If not, then they could just hang out at Matte's house. "
                    " Maybe Jam could stay over, too... "
                    " Wow, you actually had a somewhat good idea. "
                    hide matteneutral at bottom
                    show mattehappy at center
                    ma " Hmm...that actually doesn't sound that bad! "
                    ma " There {i}is{/i} this game that Jam's been wanting... "
                    ma " ...Though her parents wouldn't get her the game because they thought it would be a horrible influence. "
                    hide mattehappy at bottom
                    show mattesad at center
                    ma " Now that I think about it...she's probably going to be yelled at if they found out that I got her the game. "
                    hide mattesad at bottom
                    show mattehappy at center
                    ma " But, if they ever do yell at her... "
                    ma " I'll just have to yell at them back! "
                    ma " I won't take Jam being yelled at... "
                    ma " She's one of the coolest friends I've ever had! "
                    ma " Don't know why her parents are treating her like that... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Matte. "
                    if jamcomfort == True:
                        " You kind of explained to her what happened earlier... "
                        " ...And she was a tad bit surprised at what happened. "
                        " She just told you that she's gonna check up on Jam after class and hang out with her. "
                        " Hopefully Jam is gonna be alright. "
                    elif carmencomfort == True:
                        " You kind of explained to her what happened earlier... "
                        " ...And she was a tad bit surprised at what happened. "
                        " She just told you that she's gonna check up on Jam after class and hang out with her. "
                        " Hopefully that Jam girl is gonna be alright. "
                    else:
                        " You hoped that Jam girl is gonna be alright. "
                        " Hopefully... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit of talking, looks like it's time for another class. "
                    " You walked back into the school and walked to your classroom for the next class. "
                    pause 2.0
                    jump octgardeningclass2
                " Tell her that you don't know ":
                    ma " Ah, that's fine. "
                    ma " I think I'm gonna have to hang out with her at the park once school's over... "
                    ma " She usually gets better whenever I'm around her! "
                    ma " That should do the trick, right [name]...? "
                    ma " ...I do wonder what got her upset in the first place... "
                    ma " Was she upset that I hung out with someone that isn't her? "
                    ma " That's pretty understandable, since she gets a bit jealous often..."
                    ma " Didn't think she'd get jealous of me hanging out with Carmen though. "
                    ma " Really unexpected, you know? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Matte. "
                    if jamcomfort == True:
                        " You kind of explained to her what happened earlier... "
                        " ...And she was a tad bit surprised at what happened. "
                        " She just told you that she's gonna check up on Jam after class and hang out with her. "
                        " Hopefully Jam is gonna be alright. "
                    elif carmencomfort == True:
                        " You kind of explained to her what happened earlier... "
                        " ...And she was a tad bit surprised at what happened. "
                        " She just told you that she's gonna check up on Jam after class and hang out with her. "
                        " Hopefully that Jam girl is gonna be alright. "
                    else:
                        " You hoped that Jam girl is gonna be alright. "
                        " Hopefully... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit of talking, looks like it's time for another class. "
                    " You walked back into the school and walked to your classroom for the next class. "
                    pause 2.0
                    jump octgardeningclass2
        else:
            x " Hmmm...oh, hey [name]! "
            x " Sorry, was just thinking about a few things. "
            $ matteknow = True
            ma " I'm Matte, by the way! We're classmates! and uh... "
            ma " You see...one of my friends have been really upset lately. "
            ma " I don't know if you know her, but her name's Jam! "
            ma " She's a really cool person...defended me whenever I got into arguments accidentally... "
            ma " ...Helped me put my things into my locker whenever I was struggling... "
            ma " A real nice girl, even though she looks mean on the outside! "
            hide matteneutral at bottom
            show mattesad at center
            ma " But uh... "
            ma " Ever since I told her that I hung out with one of our classmates last night... "
            ma " ...She's been acting off. She keeps telling me that she's fine when I know that she isn't. "
            ma " I wonder what she thought when I told her... "
            ma " I just wanted someone to talk to as I was painting... "
            hide mattesad at bottom
            show matteneutral at center
            ma " Plus, it was nice hearing Carmen's guitar as I painted! gives an aesthetic vibe, don't you think? "
            ma " ...Errh, back to the original topic... "
            ma " What should I do to cheer Jam up? You have any ideas? "
            menu:
                " Tell her your idea ":
                    $ mattelv += 5
                    " You told her your idea... "
                    " ...Which was getting Jam a game that she really wanted. "
                    " And hanging out at Jam's house, if Jam was available. "
                    " If not, then they could just hang out at Matte's house. "
                    " Maybe Jam could stay over, too... "
                    " Wow, you actually had a somewhat good idea. "
                    hide matteneutral at bottom
                    show mattehappy at center
                    ma " Hmm...that actually doesn't sound that bad! "
                    ma " There {i}is{/i} this game that Jam's been wanting... "
                    ma " ...Though her parents wouldn't get her the game because they thought it would be a horrible influence. "
                    hide mattehappy at bottom
                    show mattesad at center
                    ma " Now that I think about it...she's probably going to be yelled at if they found out that I got her the game. "
                    hide mattesad at bottom
                    show mattehappy at center
                    ma " But, if they ever do yell at her... "
                    ma " I'll just have to yell at them back! "
                    ma " I won't take Jam being yelled at... "
                    ma " She's one of the coolest friends I've ever had! "
                    ma " Don't know why her parents are treating her like that... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Matte. "
                    if jamcomfort == True:
                        " You kind of explained to her what happened earlier... "
                        " ...And she was a tad bit surprised at what happened. "
                        " She just told you that she's gonna check up on Jam after class and hang out with her. "
                        " Hopefully Jam is gonna be alright. "
                    elif carmencomfort == True:
                        " You kind of explained to her what happened earlier... "
                        " ...And she was a tad bit surprised at what happened. "
                        " She just told you that she's gonna check up on Jam after class and hang out with her. "
                        " Hopefully that Jam girl is gonna be alright. "
                    else:
                        " You hoped that Jam girl is gonna be alright. "
                        " Hopefully... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit of talking, looks like it's time for another class. "
                    " You walked back into the school and walked to your classroom for the next class. "
                    pause 2.0
                    jump octgardeningclass2
                " Tell her that you don't know ":
                    ma " Ah, that's fine. "
                    ma " I think I'm gonna have to hang out with her at the park once school's over... "
                    ma " She usually gets better whenever I'm around her! "
                    ma " That should do the trick, right [name]...? "
                    ma " ...I do wonder what got her upset in the first place... "
                    ma " Was she upset that I hung out with someone that isn't her? "
                    ma " That's pretty understandable, since she gets a bit jealous often..."
                    ma " Didn't think she'd get jealous of me hanging out with Carmen though. "
                    ma " Really unexpected, you know? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Matte. "
                    if jamcomfort == True:
                        " You kind of explained to her what happened earlier... "
                        " ...And she was a tad bit surprised at what happened. "
                        " She just told you that she's gonna check up on Jam after class and hang out with her. "
                        " Hopefully Jam is gonna be alright. "
                    elif carmencomfort == True:
                        " You kind of explained to her what happened earlier... "
                        " ...And she was a tad bit surprised at what happened. "
                        " She just told you that she's gonna check up on Jam after class and hang out with her. "
                        " Hopefully that Jam girl is gonna be alright. "
                    else:
                        " You hoped that Jam girl is gonna be alright. "
                        " Hopefully... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit of talking, looks like it's time for another class. "
                    " You walked back into the school and walked to your classroom for the next class. "
                    pause 2.0
                    jump octgardeningclass2
    label island:
        " You walked up to him to see what he was up to. "
        show jacobneutral at center with easeinright
        if jacobknow == True:
            " You greeted him and asked him if he's doing alright. "
            jac " Oh, uh... "
            jac " Hi. How I'm doing? well... "
            jac " A little bit bad. "
            jac " I have this very strong feeling that someone took off my goggles while I was asleep... "
            jac " ...And I also have this strong feeling that they looked underneath my bandana. "
            jac " I'm sure you know that I don't like it whenever someone does that, right? Hopefully you do. "
            hide jacobneutral at bottom
            show jacobangry at center
            jac " Whoever looked underneath my bandana, I'm gonna kill them... "
            hide jacobangry at bottom
            show jacobneutral at center
            jac " Hey, wait... "
            jac " You weren't the one that looked underneath my bandana and goggles... "
            jac " Right? "
            menu:
                " Yes I did look underneath your bandana and goggles ":
                    $ jacoblv += 5
                    jac " ... "
                    jac " Nah, you're probably just saying that to mess with me. "
                    jac " Besides, you don't look like the type of person to do that. "
                    jac " You'd probably never do that to me, anyway. "
                    " Yeah...never. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob. "
                    " Whether you looked underneath his bandana and goggles or not... "
                    " ...He wouldn't believe you if you told him that you did, anyway. "
                    " He would also kick your ass if he actually found out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, stopping your conversation with Jacob. "
                    " You walked back into the school and walked to your classroom for the next class. "
                    pause 2.0
                    jump octgardeningclass2
                " No I didn't look underneath your bandana and goggles ":
                    $ jacoblv += 10
                    hide jacobneutral at bottom
                    show jacobhappy at center
                    jac " ...I knew I could trust on you, [name]. "
                    jac " Besides, you don't look like the type of person to do that. "
                    jac " You'd probably never do that to me, anyway. "
                    " Yeah...never. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob. "
                    " Whether you looked underneath his bandana and goggles or not... "
                    " ...He wouldn't believe you if you told him that you did, anyway. "
                    " He would also kick your ass if he actually found out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, stopping your conversation with Jacob. "
                    " You walked back into the school and walked to your classroom for the next class. "
                    pause 2.0
                    jump octgardeningclass2
        else:
            " You greeted him and asked him if he's doing alright. "
            x " Oh, uh... "
            $ jacobknow = True
            jac " Hi. I'm Jacob. How I'm doing? well... "
            jac " A little bit bad. "
            jac " I have this very strong feeling that someone took off my goggles while I was asleep... "
            jac " ...And I also have this strong feeling that they looked underneath my bandana. "
            jac " I'm sure you know that I don't like it whenever someone does that, right? Hopefully you do. "
            hide jacobneutral at bottom
            show jacobangry at center
            jac " Whoever looked underneath my bandana, I'm gonna kill them... "
            hide jacobangry at bottom
            show jacobneutral at center
            jac " Hey, wait... "
            jac " You weren't the one that looked underneath my bandana and goggles... "
            jac " Right? "
            menu:
                " Yes I did look underneath your bandana and goggles ":
                    $ jacoblv += 5
                    jac " ... "
                    jac " Nah, you're probably just saying that to mess with me. "
                    jac " Besides, you don't look like the type of person to do that. "
                    jac " You'd probably never do that to me, anyway. "
                    " Yeah...never. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob. "
                    " Whether you looked underneath his bandana and goggles or not... "
                    " ...He wouldn't believe you if you told him that you did, anyway. "
                    " He would also kick your ass if he actually found out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, stopping your conversation with Jacob. "
                    " You walked back into the school and walked to your classroom for the next class. "
                    pause 2.0
                    jump octgardeningclass2
                " No I didn't look underneath your bandana and goggles ":
                    $ jacoblv += 10
                    hide jacobneutral at bottom
                    show jacobhappy at center
                    jac " ...I knew I could trust on you, [name]. "
                    jac " Besides, you don't look like the type of person to do that. "
                    jac " You'd probably never do that to me, anyway. "
                    " Yeah...never. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob. "
                    " Whether you looked underneath his bandana and goggles or not... "
                    " ...He wouldn't believe you if you told him that you did, anyway. "
                    " He would also kick your ass if he actually found out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, stopping your conversation with Jacob. "
                    " You walked back into the school and walked to your classroom for the next class. "
                    pause 2.0
                    jump octgardeningclass2
label octbackschool3:
    # jam and orchid
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked into the back of your school and spotted two of your classmates just hanging out and chilling. "
    " As always, you wanted to talk to one of them... "
    " Who do you talk to? "
    if jamknow == True and orchidknow == True:
        menu:
            " {image=jamicon} Talk with Jam {image=jamicon} ":
                jump jambalaya
            " {image=orchidicon} Talk with Orchid {image=orchidicon} ":
                jump orchidling
    elif jamknow == True and orchidknow == False:
        menu:
            " {image=jamicon} Talk with Jam {image=jamicon} ":
                jump jambalaya
            " {image=orchidicon} Talk with a scene kid {image=orchidicon} ":
                jump orchidling
    elif jamknow == False and orchidknow == True:
        menu:
            " {image=jamicon} Talk with a mean looking girl {image=jamicon} ":
                jump jambalaya
            " {image=orchidicon} Talk with Orchid {image=orchidicon} ":
                jump orchidling
    else:
        menu:
            " {image=jamicon} Talk with a mean looking girl {image=jamicon} ":
                jump jambalaya
            " {image=orchidicon} Talk with a scene kid {image=orchidicon} ":
                jump orchidling
    label jambalaya:
        " You walked up to her and sat down next to her, curious to what she's doing. "
        show jamgame at center with easeinleft
        if jamknow == True:
            " You looked over at her and saw that she was playing a game on her phone. "
            " Looking closely, it's like a mix of a pet game and a therapy game. "
            " It looks pretty neat, too... "
            " You poked her shoulder to get her attention and asked her what game that is. "
            ja " Hm? This game? "
            ja " It's called PetVoid. It's like a therapy game or something. "
            ja " You collect these little void things and they're based off of emotions... "
            ja " ...They also check on you every day. "
            ja " There's also this feature where you water and grow a tree... "
            ja " ...By giving it positive thoughts and stuff. "
            ja " It's basically like pokemon, but more therapeutic...or whatever the word was. "
            ja " Playing this game actually helps me calm down. "
            " You took a look and asked why there was one pet named Matte. "
            " ...It also looked really cute. "
            hide jamgame at bottom
            show jamhappy at center
            ja " ...We don't talk about that. "
            hide jamhappy at bottom
            show jamgame at center
            " Jam looks at the main screen of the game where the pets usually show up... "
            " And there's this really badass looking thing that appeared. "
            ja " Oh hey, look. "
            ja " One of the things appeared. "
            ja " It's also one that I haven't caught yet...wonder what this is. "
            ja " I should name this one after you since it looks so badass. "
            " You asked her why she didn't just name it after herself, considering how badass it looked. "
            ja " Ehhh, I already have one named after me. "
            ja " Besides, I think you're more badass than me. "
            " Jam caught the little thing by saying some words of affirmation to it... "
            " ...And named it after you. Little [name] jr. "
            " That's your child now. "
            scene black with dissolve
            " You spent the rest of the break watching Jam playing her game. "
            " You two talked to eachother as you watched her play her game. "
            " Talking about random things... "
            " Though you didn't forget easily about that one pet called Matte. "
            " You knew one of your classmates was named Matte, so you're probably telling her about that. "
            " Or she might've already known that, considering the fact you saw Jam hang out with Matte a lot. "
            " And Jam would've kicked your ass if she found out that you told her. "
            play sound "audio/bellring.mp3"
            " The bell rings, interrupting your gaming session with Jam. "
            " You get up from where you were sitting, and you walked back into school to get to your classroom. "
            pause 2.0
            jump octgardeningclass2
        else:
            " You looked over at her and saw that she was playing a game on her phone. "
            " Looking closely, it's like a mix of a pet game and a therapy game. "
            " It looks pretty neat, too... "
            " You poked her shoulder to get her attention and asked her what game that is. "
            x " Hm? This game? "
            x " It's called PetVoid. It's like a therapy game or something. "
            x " You collect these little void things and they're based off of emotions... "
            x " ...They also check on you every day. "
            x " There's also this feature where you water and grow a tree... "
            x " ...By giving it positive thoughts and stuff. "
            x " It's basically like pokemon, but more therapeutic...or whatever the word was. "
            x " Playing this game actually helps me calm down. "
            $ jamknow = True
            ja " Oh, uh...I'm Jam, by the way. "
            ja " Almost forgot to introduce myself. "
            ja " We're uh, classmates. "
            " You told her that it was nice to meet her, and then looked back at her phone. "
            " You took a look and asked why there was one pet named Matte. "
            " ...It also looked really cute. "
            hide jamgame at bottom
            show jamhappy at center
            ja " ...We don't talk about that. "
            hide jamhappy at bottom
            show jamgame at center
            " Jam looks at the main screen of the game where the pets usually show up... "
            " And there's this really badass looking thing that appeared. "
            ja " Oh hey, look. "
            ja " One of the things appeared. "
            ja " It's also one that I haven't caught yet...wonder what this is. "
            ja " I should name this one after you since it looks so badass. "
            " You asked her why she didn't just name it after herself, considering how badass it looked. "
            ja " Ehhh, I already have one named after me. "
            ja " Besides, I think you're more badass than me. "
            " Jam caught the little thing by saying some words of affirmation to it... "
            " ...And named it after you. Little [name] jr. "
            " That's your child now. "
            scene black with dissolve
            " You spent the rest of the break watching Jam playing her game. "
            " You two talked to eachother as you watched her play her game. "
            " Talking about random things... "
            " Though you didn't forget easily about that one pet called Matte. "
            " You knew one of your classmates was named Matte, so you're probably telling her about that. "
            " Or she might've already known that, considering the fact you saw Jam hang out with Matte a lot. "
            " And Jam would've kicked your ass if she found out that you told her. "
            play sound "audio/bellring.mp3"
            " The bell rings, interrupting your gaming session with Jam. "
            " You get up from where you were sitting, and you walked back into school to get to your classroom. "
            pause 2.0
            jump octgardeningclass2
    label orchidling:
        " You walked up to him and sat down next to him, curious to what he's doing. "
        show orchidneutral at center with easeinright
        if orchidknow == True:
            " You greeted him and then asked him if he's doing alright. "
            oc " Oh, hey [name]!! "
            oc " I was thinking about doing something for my friends! "
            oc " Like, um...giving them a gift!! "
            oc " Problem is, I don't know what to give them... "
            oc " Maybe I could give them bracelets, right? "
            oc " But uh, should I? "
            oc " Making bracelts is kinda tiring, especially for someone as lazy as me... "
            oc " And also because I get distracted easily. "
            oc " But I really wanna do it... "
            oc " Tell me, [name]. Should I? "
            menu:
                " You should ":
                    $ orchidlv += 5
                    hide orchidneutral at bottom
                    show orchidhappy at center
                    oc " Yeah!! Even though I'll probably forget about doing it, two bracelets in... "
                    oc " I still wanna do something nice for my friends! "
                    oc " I should make Koa's look really nerdy and Disk's should be really party-like... "
                    oc " Ooooh, I have so much ideas!!~ "
                    scene black with dissolve
                    " You spent the rest of the break talking to Orchid about the bracelets they were going to make. "
                    " They seemed to be really excited about making bracelets for their friends... "
                    " You even asked if you could get a bracelet too, and they said they could make you one. "
                    " They're gonna make it look cool...because you're cool yourself, according to them. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, stopping your conversation with Orchid. "
                    " You get up from where you were sitting, and you walked back into the school to get to your classroom for the next class. "
                    pause 2.0
                    jump octgardeningclass2
                " Nah ":
                    oc " Yeah, I'd most likely get distracted and forget about my work... "
                    oc " ...And then remember that I was doing that stuff a year later. "
                    oc " Sigh...I'll get just them some nice stickers! "
                    oc " I'm sure Disk would love those! Koa too! actually, not too sure about him... "
                    oc " He'd probably just give those to his siblings. It's fine though! "
                    oc " As long as I'm making someone happy, I'm happy! "
                    scene black with dissolve
                    " You spent the rest of the break talking to Orchid. "
                    " You gave them ideas on what kind of stickers they could get for each of their friends. "
                    " You're such a good idea giver, to the point that Orchid decided to... "
                    " ...Give you some stickers that they had in their pocket!! "
                    " Great!! You're gonna stick these onto your books later. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, stopping your conversation with Orchid. "
                    " You get up from where you were sitting, and you walked back into the school to get to your classroom for the next class. "
                    pause 2.0
                    jump octgardeningclass2
        else:
            " You greeted him and then asked him if he's doing alright. "
            x " Oh, hey [name]!! "
            $ orchidknow = True
            oc " I'm Orchid, by the way! We're classmates. "
            oc " I was thinking about doing something for my friends! "
            oc " Like, um...giving them a gift!! "
            oc " Problem is, I don't know what to give them... "
            oc " Maybe I could give them bracelets, right? "
            oc " But uh, should I? "
            oc " Making bracelts is kinda tiring, especially for someone as lazy as me... "
            oc " And also because I get distracted easily. "
            oc " But I really wanna do it... "
            oc " Tell me, [name]. Should I? "
            menu:
                " You should ":
                    $ orchidlv += 5
                    hide orchidneutral at bottom
                    show orchidhappy at center
                    oc " Yeah!! Even though I'll probably forget about doing it, two bracelets in... "
                    oc " I still wanna do something nice for my friends! "
                    oc " I should make Koa's look really nerdy and Disk's should be really party-like... "
                    oc " Ooooh, I have so much ideas!!~ "
                    scene black with dissolve
                    " You spent the rest of the break talking to Orchid about the bracelets they were going to make. "
                    " They seemed to be really excited about making bracelets for their friends... "
                    " You even asked if you could get a bracelet too, and they said they could make you one. "
                    " They're gonna make it look cool...because you're cool yourself, according to them. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, stopping your conversation with Orchid. "
                    " You get up from where you were sitting, and you walked back into the school to get to your classroom for the next class. "
                    pause 2.0
                    jump octgardeningclass2
                " Nah ":
                    oc " Yeah, I'd most likely get distracted and forget about my work... "
                    oc " ...And then remember that I was doing that stuff a year later. "
                    oc " Sigh...I'll get just them some nice stickers! "
                    oc " I'm sure Disk would love those! Koa too! actually, not too sure about him... "
                    oc " He'd probably just give those to his siblings. It's fine though! "
                    oc " As long as I'm making someone happy, I'm happy! "
                    scene black with dissolve
                    " You spent the rest of the break talking to Orchid. "
                    " You gave them ideas on what kind of stickers they could get for each of their friends. "
                    " You're such a good idea giver, to the point that Orchid decided to... "
                    " ...Give you some stickers that they had in their pocket!! "
                    " Great!! You're gonna stick these onto your books later. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, stopping your conversation with Orchid. "
                    " You get up from where you were sitting, and you walked back into the school to get to your classroom for the next class. "
                    pause 2.0
                    jump octgardeningclass2
label octgym3:
    # quinn and yangyi
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym and spotted your two classmates talking about something. "
    " Curious as ever, you decided to walk over to them and check out on what they're doing. "
    show quinnneutral at left with easeinright
    show yangyineutral at right with easeinright
    if quinnknow == True and yangyiknow == True:
        q " Mmmm...have you or your brother considered acting? "
        ya " Well, I have! but I'm not sure if acting is kinda his thing... "
        q " Well, yeah. Considering how he is. "
        ya " He'd probably crush everything on set... "
        q " Mmm, yeah, and I don't want to pay for all of that... "
        " Quinn notices you and he pulls you over closer to them. "
        hide quinnneutral at bottom
        show quinnhappy at left
        q " Though, I'm sure [name] can agree that you'd be a great actor! "
        ya " Hi [name]! Also...really? "
        q " Yeah! Yangyi's a good actor, right [name]? "
        menu:
            " Yeah ":
                $ yangyilv += 5
                hide yangyineutral at bottom
                show yangyihappy at right
                ya " Aw, thanks [name]! "
                q " See? I told you you'd be a great actor! "
                q " You'd be on stage and everyone's going to love you... "
                ya " Aw, gee, Quinn... "
                ya " I find it nice that you're saying all of this, but... "
                ya " I don't think I'd be too comfortable being on stage... "
                q " Mmm, stage fright? "
                ya " Uh huh. "
                q " Don't worry, I understand. "
                q " I had stage fright when I first started acting... "
                q " But uh, if you want to join the drama club. "
                q " Just tell me, alright? "
                ya " Mhm, I'll think about it! "
                q " Great. "
                scene black with dissolve
                " You spent the rest of the break talking with Quinn and Yangyi. "
                " Hmm...maybe you could act too... "
                " Then again, I don't think you could handle being on stage and having a lot of people have their eyes on you. "
                " I mean, one wrong move and you're already going to cringe at yourself. "
                " And the audience is gonna notice that and they're gonna comment about that. "
                " Even though the show goes on, you'll never live that moment down. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes, looks like it's time for another class. "
                " You get out of the gym and walked to your classroom for the next class. "
                pause 2.0
                jump octgardeningclass2
            " I haven't seen him act yet, so I don't have an opinion ":
                hide quinnhappy at bottom
                show quinnneutral at left
                q " Ahhh, makes sense. "
                q " Still though, Yang, you'd make a great actor! "
                q " You'd be on stage and everyone's going to love you... "
                ya " Aw, gee, Quinn... "
                ya " I find it nice that you're saying all of this, but... "
                ya " I don't think I'd be too comfortable being on stage... "
                q " Mmm, stage fright? "
                ya " Uh huh. "
                q " Don't worry, I understand. "
                q " I had stage fright when I first started acting... "
                q " But uh, if you want to join the drama club. "
                q " Just tell me, alright? "
                ya " Mhm, I'll think about it! "
                q " Great. "
                scene black with dissolve
                " You spent the rest of the break talking with Quinn and Yangyi. "
                " Hmm...maybe you could act too... "
                " Then again, I don't think you could handle being on stage and having a lot of people have their eyes on you. "
                " I mean, one wrong move and you're already going to cringe at yourself. "
                " And the audience is gonna notice that and they're gonna comment about that. "
                " Even though the show goes on, you'll never live that moment down. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes, looks like it's time for another class. "
                " You get out of the gym and walked to your classroom for the next class. "
                pause 2.0
                jump octgardeningclass2
    elif quinnknow == True and yangyiknow == False:
        q " Mmmm...have you or your brother considered acting? "
        x " Well, I have! but I'm not sure if acting is kinda his thing... "
        q " Well, yeah. Considering how he is. "
        x " He'd probably crush everything on set... "
        q " Mmm, yeah, and I don't want to pay for all of that... "
        " Quinn notices you and he pulls you over closer to them. "
        hide quinnneutral at bottom
        show quinnhappy at left
        q " Though, I'm sure [name] can agree that you'd be a great actor! "
        x " Hi [name]! Also...really? "
        $ yangyiknow = True
        q " Yeah! Yangyi's a good actor, right [name]? "
        menu:
            " Yeah ":
                $ yangyilv += 5
                hide yangyineutral at bottom
                show yangyihappy at right
                ya " Aw, thanks [name]! "
                q " See? I told you you'd be a great actor! "
                q " You'd be on stage and everyone's going to love you... "
                ya " Aw, gee, Quinn... "
                ya " I find it nice that you're saying all of this, but... "
                ya " I don't think I'd be too comfortable being on stage... "
                q " Mmm, stage fright? "
                ya " Uh huh. "
                q " Don't worry, I understand. "
                q " I had stage fright when I first started acting... "
                q " But uh, if you want to join the drama club. "
                q " Just tell me, alright? "
                ya " Mhm, I'll think about it! "
                q " Great. "
                scene black with dissolve
                " You spent the rest of the break talking with Quinn and Yangyi. "
                " Hmm...maybe you could act too... "
                " Then again, I don't think you could handle being on stage and having a lot of people have their eyes on you. "
                " I mean, one wrong move and you're already going to cringe at yourself. "
                " And the audience is gonna notice that and they're gonna comment about that. "
                " Even though the show goes on, you'll never live that moment down. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes, looks like it's time for another class. "
                " You get out of the gym and walked to your classroom for the next class. "
                pause 2.0
                jump octgardeningclass2
            " I haven't seen him act yet, so I don't have an opinion ":
                hide quinnhappy at bottom
                show quinnneutral at left
                q " Ahhh, makes sense. "
                q " Still though, Yang, you'd make a great actor! "
                q " You'd be on stage and everyone's going to love you... "
                ya " Aw, gee, Quinn... "
                ya " I find it nice that you're saying all of this, but... "
                ya " I don't think I'd be too comfortable being on stage... "
                q " Mmm, stage fright? "
                ya " Uh huh. "
                q " Don't worry, I understand. "
                q " I had stage fright when I first started acting... "
                q " But uh, if you want to join the drama club. "
                q " Just tell me, alright? "
                ya " Mhm, I'll think about it! "
                q " Great. "
                scene black with dissolve
                " You spent the rest of the break talking with Quinn and Yangyi. "
                " Hmm...maybe you could act too... "
                " Then again, I don't think you could handle being on stage and having a lot of people have their eyes on you. "
                " I mean, one wrong move and you're already going to cringe at yourself. "
                " And the audience is gonna notice that and they're gonna comment about that. "
                " Even though the show goes on, you'll never live that moment down. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes, looks like it's time for another class. "
                " You get out of the gym and walked to your classroom for the next class. "
                pause 2.0
                jump octgardeningclass2
    elif quinnknow == False and yangyiknow == True:
        x " Mmmm...have you or your brother considered acting? "
        ya " Well, I have! but I'm not sure if acting is kinda his thing... "
        x " Well, yeah. Considering how he is. "
        ya " He'd probably crush everything on set... "
        x " Mmm, yeah, and I don't want to pay for all of that... "
        " Quinn notices you and he pulls you over closer to them. "
        hide quinnneutral at bottom
        show quinnhappy at left
        x " Ah, hello [name]! "
        $ quinnknow = True
        q " I'm Quinn, by the way. I'm in drama club. "
        q " Anywho, I'm sure [name] can agree that you'd be a great actor! "
        ya " Hi [name]! Also...really? "
        q " Yeah! Yangyi's a good actor, right [name]? "
        menu:
            " Yeah ":
                $ yangyilv += 5
                hide yangyineutral at bottom
                show yangyihappy at right
                ya " Aw, thanks [name]! "
                q " See? I told you you'd be a great actor! "
                q " You'd be on stage and everyone's going to love you... "
                ya " Aw, gee, Quinn... "
                ya " I find it nice that you're saying all of this, but... "
                ya " I don't think I'd be too comfortable being on stage... "
                q " Mmm, stage fright? "
                ya " Uh huh. "
                q " Don't worry, I understand. "
                q " I had stage fright when I first started acting... "
                q " But uh, if you want to join the drama club. "
                q " Just tell me, alright? "
                ya " Mhm, I'll think about it! "
                q " Great. "
                scene black with dissolve
                " You spent the rest of the break talking with Quinn and Yangyi. "
                " Hmm...maybe you could act too... "
                " Then again, I don't think you could handle being on stage and having a lot of people have their eyes on you. "
                " I mean, one wrong move and you're already going to cringe at yourself. "
                " And the audience is gonna notice that and they're gonna comment about that. "
                " Even though the show goes on, you'll never live that moment down. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes, looks like it's time for another class. "
                " You get out of the gym and walked to your classroom for the next class. "
                pause 2.0
                jump octgardeningclass2
            " I haven't seen him act yet, so I don't have an opinion ":
                hide quinnhappy at bottom
                show quinnneutral at left
                q " Ahhh, makes sense. "
                q " Still though, Yang, you'd make a great actor! "
                q " You'd be on stage and everyone's going to love you... "
                ya " Aw, gee, Quinn... "
                ya " I find it nice that you're saying all of this, but... "
                ya " I don't think I'd be too comfortable being on stage... "
                q " Mmm, stage fright? "
                ya " Uh huh. "
                q " Don't worry, I understand. "
                q " I had stage fright when I first started acting... "
                q " But uh, if you want to join the drama club. "
                q " Just tell me, alright? "
                ya " Mhm, I'll think about it! "
                q " Great. "
                scene black with dissolve
                " You spent the rest of the break talking with Quinn and Yangyi. "
                " Hmm...maybe you could act too... "
                " Then again, I don't think you could handle being on stage and having a lot of people have their eyes on you. "
                " I mean, one wrong move and you're already going to cringe at yourself. "
                " And the audience is gonna notice that and they're gonna comment about that. "
                " Even though the show goes on, you'll never live that moment down. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes, looks like it's time for another class. "
                " You get out of the gym and walked to your classroom for the next class. "
                pause 2.0
                jump octgardeningclass2
    else:
        x " Mmmm...have you or your brother considered acting? "
        x " Well, I have! but I'm not sure if acting is kinda his thing... "
        x " Well, yeah. Considering how he is. "
        x " He'd probably crush everything on set... "
        x " Mmm, yeah, and I don't want to pay for all of that... "
        " Quinn notices you and he pulls you over closer to them. "
        hide quinnneutral at bottom
        show quinnhappy at left
        x " Ah, hello [name]! "
        $ quinnknow = True
        q " I'm Quinn, by the way. I'm in drama club. "
        q " Anywho, I'm sure [name] can agree that you'd be a great actor! "
        x " Hi [name]! Also...really? "
        $ yangyiknow = True
        q " Yeah! Yangyi's a good actor, right [name]? "
        menu:
            " Yeah ":
                $ yangyilv += 5
                hide yangyineutral at bottom
                show yangyihappy at right
                ya " Aw, thanks [name]! "
                q " See? I told you you'd be a great actor! "
                q " You'd be on stage and everyone's going to love you... "
                ya " Aw, gee, Quinn... "
                ya " I find it nice that you're saying all of this, but... "
                ya " I don't think I'd be too comfortable being on stage... "
                q " Mmm, stage fright? "
                ya " Uh huh. "
                q " Don't worry, I understand. "
                q " I had stage fright when I first started acting... "
                q " But uh, if you want to join the drama club. "
                q " Just tell me, alright? "
                ya " Mhm, I'll think about it! "
                q " Great. "
                scene black with dissolve
                " You spent the rest of the break talking with Quinn and Yangyi. "
                " Hmm...maybe you could act too... "
                " Then again, I don't think you could handle being on stage and having a lot of people have their eyes on you. "
                " I mean, one wrong move and you're already going to cringe at yourself. "
                " And the audience is gonna notice that and they're gonna comment about that. "
                " Even though the show goes on, you'll never live that moment down. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes, looks like it's time for another class. "
                " You get out of the gym and walked to your classroom for the next class. "
                pause 2.0
                jump octgardeningclass2
            " I haven't seen him act yet, so I don't have an opinion ":
                hide quinnhappy at bottom
                show quinnneutral at left
                q " Ahhh, makes sense. "
                q " Still though, Yang, you'd make a great actor! "
                q " You'd be on stage and everyone's going to love you... "
                ya " Aw, gee, Quinn... "
                ya " I find it nice that you're saying all of this, but... "
                ya " I don't think I'd be too comfortable being on stage... "
                q " Mmm, stage fright? "
                ya " Uh huh. "
                q " Don't worry, I understand. "
                q " I had stage fright when I first started acting... "
                q " But uh, if you want to join the drama club. "
                q " Just tell me, alright? "
                ya " Mhm, I'll think about it! "
                q " Great. "
                scene black with dissolve
                " You spent the rest of the break talking with Quinn and Yangyi. "
                " Hmm...maybe you could act too... "
                " Then again, I don't think you could handle being on stage and having a lot of people have their eyes on you. "
                " I mean, one wrong move and you're already going to cringe at yourself. "
                " And the audience is gonna notice that and they're gonna comment about that. "
                " Even though the show goes on, you'll never live that moment down. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes, looks like it's time for another class. "
                " You get out of the gym and walked to your classroom for the next class. "
                pause 2.0
                jump octgardeningclass2
label octcafe3:
    # temero, nox, notive
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted three of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if temeroknow,noxknow,notiveknow == True:
        menu:
            " {image=temeroicon} Temero NEO {image=temeroicon} ":
                jump crashout
            " {image=noxicon} Nox {image=noxicon} ":
                jump heartbeat
            " {image=notiveicon} Notive {image=notiveicon} ":
                jump bluutoday
    elif temeroknow,noxknow == True and notiveknow == False:
        menu:
            " {image=temeroicon} Temero NEO {image=temeroicon} ":
                jump crashout
            " {image=noxicon} Nox {image=noxicon} ":
                jump heartbeat
            " {image=notiveicon} A guy thats just...staring into the void {image=notiveicon} ":
                jump bluutoday
    elif temeroknow,notiveknow == True and noxknow == False:
        menu:
            " {image=temeroicon} Temero NEO {image=temeroicon} ":
                jump crashout
            " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                jump heartbeat
            " {image=notiveicon} Notive {image=notiveicon} ":
                jump bluutoday
    elif noxknow,notiveknow == True and temeroknow == False:
        menu:
            " {image=temeroicon} A insane scientist looking girl {image=temeroicon} ":
                jump crashout
            " {image=noxicon} Nox {image=noxicon} ":
                jump heartbeat
            " {image=notiveicon} Notive {image=notiveicon} ":
                jump bluutoday
    elif temeroknow == True and noxknow,notiveknow == False:
        menu:
            " {image=temeroicon} Temero NEO {image=temeroicon} ":
                jump crashout
            " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                jump heartbeat
            " {image=notiveicon} A guy that's just...staring into the void {image=notiveicon} ":
                jump bluutoday
    elif noxknow == True and temeroknow,notiveknow == False:
        menu:
            " {image=temeroicon} A insane scientist looking girl {image=temeroicon} ":
                jump crashout
            " {image=noxicon} Nox {image=noxicon} ":
                jump heartbeat
            " {image=notiveicon} A guy that's just...staring into the void. {image=notiveicon} ":
                jump bluutoday
    elif notiveknow == True and temeroknow,noxknow == False:
        menu:
            " {image=temeroicon} A insane scientist looking girl {image=temeroicon} ":
                jump crashout
            " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                jump heartbeat
            " {image=notiveicon} Notive {image=notiveicon} ":
                jump bluutoday
    else:
        menu:
            " {image=temeroicon} A insane scientist looking girl {image=temeroicon} ":
                jump crashout
            " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                jump heartbeat
            " {image=notiveicon} A guy that's just...staring into the void {image=notiveicon} ":
                jump bluutoday
    label crashout:
        " You walked up to her to check on what she's doing. "
        " Wait...is she doing a science experiment in the middle of the cafeteria? "
        " Well, not the first time you've heard of something like this. "
        show temeroneutral at center with easeinleft
        if temeroknow == True:
            " She seems pretty concentrated on what she's doing... "
            " On a closer look, it seems like she's experimenting on a butterfly. "
            " It's also the same color as her bow. "
            tm " Hm... how about some of that... "
            tm " No, maybe a pinch of this...? "
            " She couldn't decide between two bottles who had liquids in them. "
            " One of them was green, while the other was bright pink. "
            " In the end, she decided to grab both of them to see what they would do. "
            tm " You know what, screw this! "
            " She poured both of the bottles onto the butterfly. "
            " At first, nothing happened. But then the butterfly started to grow rapidly... "
            " And was about the size of the cafeteria table. "
            hide temeroneutral at bottom
            show temerohappy at center
            tm " HAHA, YES!! IT WORKED!! "
            tm " Though I have no idea where to put this thing now... "
            tm " Maybe in my secret room would do. "
            " She had her other butterflies carrying the big one away outside. "
            " After a few moments of being proud, she finally noticed you. "
            hide temerohappy at bottom
            show temeroneutral at center
            tm " Oh, sup [name]! "
            tm " You saw that, right? "
            tm " You've gotta admit, that was one of the coolest things you've ever seen. "
            tm " Eh..? why do I use butterflies as experiment thingies? "
            tm " Well! I feel like it'd be less harmful to use them rather than using other animals, like dogs. "
            tm " These butterflies were specifically made by me to use as test subjects! "
            tm " Just added a butterfly's DNA...then some potions here and there... "
            tm " And BOOM! I've got myself a test subject. "
            tm " I don't actually use actual butterflies otherwise twitter would hate me. "
            tm " Then again, butterflies are considered animals, so... "
            tm " ...Yeah, I don't know what people would think of me. "
            scene black with dissolve
            " You spent the rest of the break talking with Temero. "
            " You didn't really know that she used butterflies as test subjects.. "
            " You actually thought that they were her favorite animal considering her bow. "
            " ...Actually she did say that they were her favorite. "
            " Uh, okay I'm not gonna continue this, this is getting a bit confusing. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get up from where you were sitting and you walked back to your classroom for the next class. "
            pause 2.0
            jump octgardeningclass2
        else:
            " She seems pretty concentrated on what she's doing... "
            " On a closer look, it seems like she's experimenting on a butterfly. "
            " It's also the same color as her bow. "
            x " Hm... how about some of that... "
            x " No, maybe a pinch of this...? "
            " She couldn't decide between two bottles who had liquids in them. "
            " One of them was green, while the other was bright pink. "
            " In the end, she decided to grab both of them to see what they would do. "
            x " You know what, screw this! "
            " She poured both of the bottles onto the butterfly. "
            " At first, nothing happened. But then the butterfly started to grow rapidly... "
            " And was about the size of the cafeteria table. "
            hide temeroneutral at bottom
            show temerohappy at center
            x " HAHA, YES!! IT WORKED!! "
            x " Though I have no idea where to put this thing now... "
            x " Maybe in my secret room would do. "
            " She had her other butterflies carrying the big one away outside. "
            " After a few moments of being proud, she finally noticed you. "
            hide temerohappy at bottom
            show temeroneutral at center
            x " Oh, sup [name]! "
            $ temeroknow = True
            tm " I'm Temero, by the way. But enough about me... "
            tm " You saw that, right? "
            tm " You've gotta admit, that was one of the coolest things you've ever seen. "
            tm " Eh..? why do I use butterflies as experiment thingies? "
            tm " Well! I feel like it'd be less harmful to use them rather than using other animals, like dogs. "
            tm " These butterflies were specifically made by me to use as test subjects! "
            tm " Just added a butterfly's DNA...then some potions here and there... "
            tm " And BOOM! I've got myself a test subject. "
            tm " I don't actually use actual butterflies otherwise twitter would hate me. "
            tm " Then again, butterflies are considered animals, so... "
            tm " ...Yeah, I don't know what people would think of me. "
            scene black with dissolve
            " You spent the rest of the break talking with Temero. "
            " You didn't really know that she used butterflies as test subjects.. "
            " You actually thought that they were her favorite animal considering her bow. "
            " ...Actually she did say that they were her favorite. "
            " Uh, okay I'm not gonna continue this, this is getting a bit confusing. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get up from where you were sitting and you walked back to your classroom for the next class. "
            pause 2.0
            jump octgardeningclass2
    label heartbeat:
        " You walked up to see what he was doing. "
        " Wait, where'd he get that cute sleep plushie? "
        " You've never seen anything like that before... "
        " You lowkey wanna touch it. "
        show noxneutral at center with easeinright
        if noxknow == True:
            " You greeted him before you asked him where he got that plushie. "
            n " ...Mmm...? This...? "
            n " My mom got this custom made for me... "
            n " I like to carry around sometimes... "
            n " It comforts me a whole lot... "
            n " It also makes me feel more sleepy at times... "
            n " I'm sure I can...stay up until class starts... "
            hide noxneutral at bottom
            show noxsleepy at center
            n " ...I'm sure...*yawn*... "
            scene black with dissolve
            " Not even a few minutes later, Nox fell asleep as he held that plushie. "
            " He honestly looked really cute holding it like that. "
            " You could take a photo, but you shouldn't take a photo of someone without their permission. "
            " You also just let him sleep because he looked like he needed it. "
            " While you were waiting for him to wake up, you decided to check your messages for a bit. "
            " Oh hey, someone sent you a link to get a free car! "
            " Wait, you're not even old enough to get a car. "
            " Scam. Get out. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, and you woke him up once you saw that he didn't wake up to the loud sund. "
            " Once you got him up, you got up from your own seat and you walked to your classroom for the next class. "
            pause 2.0
            jump octgardeningclass2
        else:
            x " Oh, hey...you're that...new kid...? "
            $ noxknow = True
            n " Hhhh...I'm Nox...did I introduce myself to you yet...? "
            n " Sorry, I forgot...but it's nice to meet you... "
            " You greeted him before you asked him where he got that plushie. "
            n " ...Mmm...? This...? "
            n " My mom got this custom made for me... "
            n " I like to carry around sometimes... "
            n " It comforts me a whole lot... "
            n " It also makes me feel more sleepy at times... "
            n " I'm sure I can...stay up until class starts... "
            hide noxneutral at bottom
            show noxsleepy at center
            n " ...I'm sure...*yawn*... "
            scene black with dissolve
            " Not even a few minutes later, Nox fell asleep as he held that plushie. "
            " He honestly looked really cute holding it like that. "
            " You could take a photo, but you shouldn't take a photo of someone without their permission. "
            " You also just let him sleep because he looked like he needed it. "
            " While you were waiting for him to wake up, you decided to check your messages for a bit. "
            " Oh hey, someone sent you a link to get a free car! "
            " Wait, you're not even old enough to get a car. "
            " Scam. Get out. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, and you woke him up once you saw that he didn't wake up to the loud sund. "
            " Once you got him up, you got up from your own seat and you walked to your classroom for the next class. "
            pause 2.0
            jump octgardeningclass2
    label bluutoday:
        " You walked up to them to see what they're doing. "
        " They're just...staring at you. Menacingly. "
        " You probably need to stop them staring at you for too long. "
        show notiveneutral at center with dissolve
        if notiveknow == True:
            no " ... "
            " ... "
            hide notiveneutral at bottom
            show notivehappy at center
            no " ... "
            " ... "
            scene black with dissolve
            " You spent the rest of the break just staring at Notive. "
            " Nothing really interesting happened as you stared. "
            " But a few people did think you two were doing a staring contest. "
            " ...They tried to snap the both of you out of it but it didn't work. "
            " Eventually it was just you and Notive staring at eachother once again. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, stopping your staring session. "
            " As you walked to your classroom, you and Notive continued to stare at eachother... "
            " ...Until they blinked. You made fun for them afterwards. "
            pause 2.0
            jump octgardeningclass2
        else:
            x " ... "
            " ... "
            hide notiveneutral at bottom
            show notivehappy at center
            x " ... "
            " ... "
            scene black with dissolve
            " You spent the rest of the break just staring at the guy. "
            " Nothing really interesting happened as you stared. "
            " But a few people did think you two were doing a staring contest. "
            " ...They tried to snap the both of you out of it but it didn't work. "
            " Eventually it was just you and Notive staring at eachother once again. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, stopping your staring session. "
            " As you walked to your classroom, you and the guy continued to stare at eachother... "
            " ...Until they blinked. You made fun for them afterwards. "
            pause 2.0
            jump octgardeningclass2
label octrooftop3:
    # koa and mia
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked to the rooftop and spotted two of your classmates chilling. "
    " You wanted to talk to one of them...but who do you talk to? "
    if koaknow == True and miaknow == True:
        menu:
            " {image=koaicon} Koa {image=koaicon} ":
                jump mavuika
            " {image=miaicon} Mia {image=miaicon} ":
                jump furina
    elif koaknow == True and miaknow == False:
        menu:
            " {image=koaicon} Koa {image=koaicon} ":
                jump mavuika
            " {image=miaicon} A girl with a flower on her head {image=miaicon} ":
                jump furina
    elif koaknow == False and miaknow == True:
        menu:
            " {image=koaicon} An emo looking guy {image=koaicon} ":
                jump mavuika
            " {image=miaicon} Mia {image=miaicon} ":
                jump furina
    else:
        menu:
            " {image=koaicon} An emo looking guy {image=koaicon} ":
                jump mavuika
            " {image=miaicon} A girl with a flower on her head {image=miaicon} ":
                jump furina
    label mavuika:
        " You walked up to him to see what he was doing. "
        show koaneutral at center with easeinright
        if koaknow == True:
            " You poked his shoulder to get his attention, then asked him what he was doing. "
            k " ...? Oh, [name]. "
            k " It's nice to have you here. "
            if koalv == 10:
                k " I was just admiring the view. You know... "
                k " Back then, I would go stargazing with my siblings. "
                k " Cloudgazing, too, since they would ask to spend time with me. "
                k " But, after I got my bandage on my eye right here... "
                k " They kind of stopped because they were worried about me. "
                k " Something like...they were worried about me not being able to see the whole thing. "
                k " Like the view in the sky, what they mean. "
                k " Though I always reassure them that I'll be fine, "
                k " Even if I can't really see properly. "
                " Koa stays silent for a moment. "
                " As he stays silent, you decided to stand next to him... "
                " ...And watched the view with him. "
                " It was nice looking at something so appealing like the sky for once... "
                " ...And not having to look at italian brainrot on your phone. "
                " Everything was nice and quiet... "
            else:
                " Koa stays silent for a moment. "
                " As he stays silent, you decided to stand next to him... "
                " ...And watched the view with him. "
                " It was nice looking at something so appealing like the sky for once... "
                " ...And not having to look at italian brainrot on your phone. "
                " Everything was nice and quiet... "
            hide koaneutral at bottom
            show koasurprised at center
            " Until you heard a pot falling and breaking. "
            " Seems like Koa heard it too, and he looked like he was very surprised. "
            " You could hear someone panicking and yelling 'MY FLOWER!!' in the background. "
            " ...Someone must've dropped it accidentally. "
            k " ... "
            k " ...Rest in piece to their flower, I guess... "
            scene black with dissolve
            " You spent the rest of the break talking and hanging out with Koa. "
            " He was mostly just very chill as you two were hanging out... "
            " ...He also talked about the flower pot situation that happened earlier. "
            " And may or may not have made a few jokes about it. "
            " Overall pretty chill. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You get down from the rooftop and you walked back to your classroom for your next class. "
            pause 2.0
            jump octgardeningclass2
        else:
            " You poked his shoulder to get his attention, then asked him what he was doing. "
            x " ...? Oh, [name]. "
            x " It's nice to have you here. "
            $ koaknow = True
            k " I'm Koa, by the way. "
            k " It's nice to meet you. "
            if koalv == 10:
                k " I was just admiring the view. You know... "
                k " Back then, I would go stargazing with my siblings. "
                k " Cloudgazing, too, since they would ask to spend time with me. "
                k " But, after I got my bandage on my eye right here... "
                k " They kind of stopped because they were worried about me. "
                k " Something like...they were worried about me not being able to see the whole thing. "
                k " Like the view in the sky, what they mean. "
                k " Though I always reassure them that I'll be fine, "
                k " Even if I can't really see properly. "
                " Koa stays silent for a moment. "
                " As he stays silent, you decided to stand next to him... "
                " ...And watched the view with him. "
                " It was nice looking at something so appealing like the sky for once... "
                " ...And not having to look at italian brainrot on your phone. "
                " Everything was nice and quiet... "
            else:
                " Koa stays silent for a moment. "
                " As he stays silent, you decided to stand next to him... "
                " ...And watched the view with him. "
                " It was nice looking at something so appealing like the sky for once... "
                " ...And not having to look at italian brainrot on your phone. "
                " Everything was nice and quiet... "
            hide koaneutral at bottom
            show koasurprised at center
            " Until you heard a pot falling and breaking. "
            " Seems like Koa heard it too, and he looked like he was very surprised. "
            " You could hear someone panicking and yelling 'MY FLOWER!!' in the background. "
            " ...Someone must've dropped it accidentally. "
            k " ... "
            k " ...Rest in piece to their flower, I guess... "
            scene black with dissolve
            " You spent the rest of the break talking and hanging out with Koa. "
            " He was mostly just very chill as you two were hanging out... "
            " ...He also talked about the flower pot situation that happened earlier. "
            " And may or may not have made a few jokes about it. "
            " Overall pretty chill. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You get down from the rooftop and you walked back to your classroom for your next class. "
            pause 2.0
            jump octgardeningclass2
    label furina:
        " You walked up to her to see what she was doing. "
        show mianeutral at center with easeinleft
        if miaknow == True:
            " You poked her shoulder so that you could get her attention. "
            m " Woah, [name]!! "
            m " You almost made me accidentally push off my flower pot!! "
            m " It's alright, since it didn't fall. "
            m " Anyway, I just decided to decorate the rooftop more with plants! "
            m " I mean, this place DOES look like it needs more decorations, right? "
            m " Lemme just put this one on the rails, hopefully it doesn't fall.. "
            m " Anyway... "
            m " Did you want to talk to me about something? "
            m " Oooh, actually!! "
            m " This is one of my favorite flowers! "
            m " I kinda wanna say a few facts about it, if you don't mind. "
            m " So, first of all, this is actually - {nw} "
            " Mia accidentally leaned onto the flower pot, resulting in it falling to the ground... "
            hide mianeutral at bottom
            show miaworried at center
            " ...And making a loud breaking noise. "
            " Geez, I wonder how you could hear it from up here. "
            " Once again, game logic. "
            " Back to how Mia's doing... "
            m " ... "
            m " ...MY FLOWER!!! " with vpunch
            scene black with dissolve
            " You spent the rest of the break comforting Mia about her flower. "
            " You reassured her that she was just gonna get a new one that's the same as her old flower... "
            " ...But it seems like she just got more upset when you told her that. "
            " Geez, that one must've been special or something. "
            " Yo're lowkey starting to feel a tad bit bad for her. "
            play sound "audio/bellring.mp3"
            " The bell rings after a few more minutes of comforting. "
            " You make sure Mia is okay before you walked down from the rooftop and went to your classroom for the next class. "
            pause 2.0
            jump octgardeningclass2
        else:
            " You poked her shoulder so that you could get her attention. "
            x " Woah, [name]!! "
            x " You almost made me accidentally push off my flower pot!! "
            x " It's alright, since it didn't fall. "
            $ miaknow = True
            m " I'm Mia, by the way! we're classmates, if I remember correctly. "
            m " Anyway, I just decided to decorate the rooftop more with plants! "
            m " I mean, this place DOES look like it needs more decorations, right? "
            m " Lemme just put this one on the rails, hopefully it doesn't fall.. "
            m " Anyway... "
            m " Did you want to talk to me about something? "
            m " Oooh, actually!! "
            m " This is one of my favorite flowers! "
            m " I kinda wanna say a few facts about it, if you don't mind. "
            m " So, first of all, this is actually - {nw} "
            " Mia accidentally leaned onto the flower pot, resulting in it falling to the ground... "
            hide mianeutral at bottom
            show miaworried at center
            " ...And making a loud breaking noise. "
            " Geez, I wonder how you could hear it from up here. "
            " Once again, game logic. "
            " Back to how Mia's doing... "
            m " ... "
            m " ...MY FLOWER!!! " with vpunch
            scene black with dissolve
            " You spent the rest of the break comforting Mia about her flower. "
            " You reassured her that she was just gonna get a new one that's the same as her old flower... "
            " ...But it seems like she just got more upset when you told her that. "
            " Geez, that one must've been special or something. "
            " Yo're lowkey starting to feel a tad bit bad for her. "
            play sound "audio/bellring.mp3"
            " The bell rings after a few more minutes of comforting. "
            " You make sure Mia is okay before you walked down from the rooftop and went to your classroom for the next class. "
            pause 2.0
            jump octgardeningclass2
label octlibrary3:
    # carmen and spark
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and spotted two of your classmates reading some books. "
    " You wanted to talk to them...and wanted to check out what they're reading. "
    " Who should you talk to, though? "
    if carmenknow == True and sparkknow == True:
        menu:
            " {image=carmenicon} Carmen {image=carmenicon} ":
                jump frozensoul
            " {image=sparkicon} Spark {image=sparkicon} ":
                jump lastjulymidsummer
    elif carmenknow == True and sparkknow == False:
        menu:
            " {image=carmenicon} Carmen {image=carmenicon} ":
                jump frozensoul
            " {image=sparkicon} A guy with antennas and a tail {image=sparkicon} ":
                jump lastjulymidsummer
    elif carmenknow == False and sparkknow == True:
        menu:
            " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                jump frozensoul
            " {image=sparkicon} Spark {image=sparkicon} ":
                jump lastjulymidsummer
    else:
        menu:
            " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                jump frozensoul
            " {image=sparkicon} A guy with antennas and a tail {image=sparkicon} ":
                jump lastjulymidsummer
    label frozensoul:
        " You walked up to him to see what he was doing. "
        show carmenneutral at center with easeinleft
        if carmenknow == True:
            " You looked closer and it looked like he was looking at a book on how to play the guitar better. "
            " You also noticed that he hasn't noticed you were there yet... "
            " You sat next to him and poked his shoulder to get his attention, and then greeted him. "
            ca " ...!! (*waves*) "
            ca " ... (*points at book, then guitar...*) "
            hide carmenneutral at bottom
            show carmensad at center
            ca " ...:( (*gang im so bad at the guitar*) "
            " You reassured him that he probably wasn't bad at the guitar. "
            " You asked him if he could play a short tune for you. "
            " At this point anything was allowed since the librarian wasn't actually on their job. "
            " He looks a little nervous before he sighs and gives in... "
            " ...He starts playing a really nice and short tune but stops after about 2 minutes of playing. "
            " He looked like he didn't really like how he played. "
            " But, you gave him a thumbs up as if you're silently saying that he's doing good. "
            " ...Looks like he doesn't believe you. You're gonna have to try harder than that. "
            scene black with dissolve
            " You spent the rest of the break making sure that Carmen knew that he was good at playing the guitar. "
            " You kept throwing compliments and compliments at him... "
            " ...Until you finally got him to admit that he was good. Big win for you."
            " You then proceed to do a trickshot or whatever they're called, and somehow threw the book back into it's original place on the shelf. "
            " You felt really cool after that happened. "
            " You're a very cool [person]. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get up from where you were sitting and you walked back to your classroom for your next class. "
            pause 2.0
            jump octgardeningclass2
        else:
            $ carmenknow = True
            " From what you remember, this guy's name was Carmen. "
            " You're his classmate, and he's also mute. And he likes playing on his guitar. "
            " You looked closer and it looked like he was looking at a book on how to play the guitar better. "
            " You also noticed that he hasn't noticed you were there yet... "
            " You sat next to him and poked his shoulder to get his attention, and then greeted him. "
            ca " ...!! (*waves*) "
            ca " ... (*points at book, then guitar...*) "
            hide carmenneutral at bottom
            show carmensad at center
            ca " ...:( (*gang im so bad at the guitar*) "
            " You reassured him that he probably wasn't bad at the guitar. "
            " You asked him if he could play a short tune for you. "
            " At this point anything was allowed since the librarian wasn't actually on their job. "
            " He looks a little nervous before he sighs and gives in... "
            " ...He starts playing a really nice and short tune but stops after about 2 minutes of playing. "
            " He looked like he didn't really like how he played. "
            " But, you gave him a thumbs up as if you're silently saying that he's doing good. "
            " ...Looks like he doesn't believe you. You're gonna have to try harder than that. "
            scene black with dissolve
            " You spent the rest of the break making sure that Carmen knew that he was good at playing the guitar. "
            " You kept throwing compliments and compliments at him... "
            " ...Until you finally got him to admit that he was good. Big win for you."
            " You then proceed to do a trickshot or whatever they're called, and somehow threw the book back into it's original place on the shelf. "
            " You felt really cool after that happened. "
            " You're a very cool [person]. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get up from where you were sitting and you walked back to your classroom for your next class. "
            pause 2.0
            jump octgardeningclass2
    label lastjulymidsummer:
        " You walked up to him to see what he was doing. "
        show sparkneutral at center with easeinright
        if sparkknow == True:
            " You took a look closer on what he's reading... "
            " ...Looks like he's reading a book about robots and stuff... "
            " There's also another book that he's holding about... "
            " ...Demons? why the hell would he want to learn about demons? "
            " It didn't take too long for him to notice that you were there though. "
            sp " Oh, uh, [name]. Hi. "
            " You greeted him before you asked about the books he was reading. "
            " You honestly didn't expect him to be reading something, considering how he is from what you've heard. "
            " Apparently he just chills around in class, and somehow he passes. "
            " There's gotta be something up if he's like that. "
            sp " What book I'm reading...? "
            sp " Well, you see..it's for this personal project I'm working. "
            sp " Just making something cool to impress this one guy I met while I was visiting a school... "
            sp " Heard he liked to make robots and stuff, so I decided to try and make one, too. "
            " That explains the robot book and all... "
            " ...But it doesn't explain the demon one. "
            sp " Oh, that? "
            sp " Just picked out something random. "
            sp " It's pretty good. "
            scene black with dissolve
            " You spent the rest of the break talking with Spark. "
            " He felt...really mysterious whenever you talked about the other book. "
            " As if he wasn't admitting something... "
            " It's best not to pry, but you can't help but get curious on what's going on in his brain. "
            " It's also best to not think about this too much. "
            " Probably. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time to go to another class. "
            " You get up from where you were sitting and you walked back to your classroom for your next class. "
            pause 2.0
            jump octgardeningclass2
        else:
            " You took a look closer on what he's reading... "
            " ...Looks like he's reading a book about robots and stuff... "
            " There's also another book that he's holding about... "
            " ...Demons? why the hell would he want to learn about demons? "
            " It didn't take too long for him to notice that you were there though. "
            x " Oh, uh, [name]. Hi. "
            $ sparkknow = True
            sp " I don't think I got to introduce myself to you before. I'm Spark, we're classmates. "
            " You greeted him before you asked about the books he was reading. "
            " You honestly didn't expect him to be reading something, considering how he is from what you've heard. "
            " Apparently he just chills around in class, and somehow he passes. "
            " There's gotta be something up if he's like that. "
            sp " What book I'm reading...? "
            sp " Well, you see..it's for this personal project I'm working. "
            sp " Just making something cool to impress this one guy I met while I was visiting a school... "
            sp " Heard he liked to make robots and stuff, so I decided to try and make one, too. "
            " That explains the robot book and all... "
            " ...But it doesn't explain the demon one. "
            sp " Oh, that? "
            sp " Just picked out something random. "
            sp " It's pretty good. "
            scene black with dissolve
            " You spent the rest of the break talking with Spark. "
            " He felt...really mysterious whenever you talked about the other book. "
            " As if he wasn't admitting something... "
            " It's best not to pry, but you can't help but get curious on what's going on in his brain. "
            " It's also best to not think about this too much. "
            " Probably. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time to go to another class. "
            " You get up from where you were sitting and you walked back to your classroom for your next class. "
            pause 2.0
            jump octgardeningclass2
label octgardeningclass2:
    scene gardenroom with dissolve
    " You walked into the classroom and patiently waited for the teacher to arrive. "
    " As you waited, you took a look around the plants that was near you. "
    " All of them looked so pretty...some of them looked like they would taste pretty good. "
    " ...Wait, what? what were you thinking? "
    " You then heard the door opening. That must be your gardening teacher. "
    show wisterianeutral at center with easeinleft
    msw " Hello, my students... "
    msw " I hope you're all feeling good today... "
    msw " Before we'd start our class, I'd like to remind you all.. "
    msw " ...Of the activity we have tomorrow. "
    msw " Please prepare your materials in advance for tomorrow, thank you... "
    msw " I wouldn't want you all worrying about buying it all tomorrow because you guys forgot. "
    msw " Anywho, onto our lesson for the day... "
    scene black with dissolve
    " You spent the rest of the class copying down some notes for your notebook. "
    " You learned what things to do and not to do while you're gardening something... "
    " ...Though you'd probably never do some gardening, it does sound like a fun hobby. "
    " Somehow. Look, you just wanna see the pretty plants. "
    " And honestly, that's pretty reasonable. "
    " As long as you remember to water them every day. "
    play sound "audio/bellring.mp3"
    " The bell rings, looks like it's time for another break. "
    " You get up from your seat and you walk back into the hallways. "
    " Time to find another spot to hangout in... "
    pause 2.0
    jump octbreak4
label octbreak4:
    # add characters later
    scene hallway with dissolve
    " You're thinking about hanging out somewhere again for this break. "
    " Where do you head off to, this time? "
    menu:
        " {image=jacobicon} The front of the school {image=matteicon} ":
            jump octfrontschool4
        " {image=noxicon} The back of the school {image=koaicon} ":
            jump octbackschool4
        " {image=diskicon} The gym {image=jamicon} ":
            jump octgym4
        " {image=carmenicon} The cafeteria {image=sparkicon} ":
            jump octcafe4
        " {image=quinnicon} The rooftop {image=orchidicon} ":
            jump octrooftop4
        " {image=yinyangicon} The library {image=temeroicon} ":
            jump octlibrary4
label octfrontschool4:
    # jacob, matte
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of your school and spotted two of your classmates hanging out. "
    " As always, you wanted to hang out with one of them. "
    " Who do you hang out with for this break? "
    if jacobknow == True and matteknow == True:
        menu:
            " {image=jacobicon} Jacob {image=jacobicon} ":
                jump pxrn
            " {image=matteicon} Matte {image=matteicon} ":
                jump star
    elif jacobknow == True and matteknow == False:
        menu:
            " {image=jacobicon} Jacob {image=jacobicon} ":
                jump pxrn
            " {image=matteicon} An artsy looking girl {image=matteicon} ":
                jump star
    elif jacobknow == False and matteknow == True:
        menu:
            " {image=jacobicon} A guy with a bandana and goggles {image=jacobicon} ":
                jump pxrn
            " {image=matteicon} Matte {image=matteicon} ":
                jump star
    else:
        menu:
            " {image=jacobicon} A guy with a bandana and goggles {image=jacobicon} ":
                jump pxrn
            " {image=matteicon} An artsy looking girl {image=matteicon} ":
                jump star
    label pxrn:
        " You walked up to him, wanting to know what he was up to this time. "
        show jacobneutral at center with easeinleft
        if jacobknow == True:
            " Looks like he's cleaning up his saw... "
            " It's still got a few dirt stains on it. Wonder what happened. "
            " You asked him what he did to get it to be so dirty. "
            jac " Oh, my saw? "
            jac " ... "
            jac " ...It's gonna be embarrassing if I told you. "
            jac " Promise you won't laugh? "
            " You promised that you wouldn't laugh at him. "
            " And if you did, he was free to kick your ass. "
            " ...Actually, you might get your ass kicked if he's telling you to not laugh. "
            " Or not. That depends on what I say will happen. "
            " It's a part of the script, gang. "
            jac " Okay... "
            jac " ...So, I hadto check something outside of school... "
            jac " ...Then I rushed here thinking class was starting... "
            jac " But then I tripped and fell into the dirt causing my saw to get dirty. "
            jac " Thankfully no one else saw that... "
            jac " I would've been doomed if someone saw me fall and trip like that. "
            jac " I know for sure they're going to make a meme out of me if someone saw me... "
            jac " ...And I wouldn't want that to happen. "
            jac " Thankfully, most of the students here are nice... "
            jac " ...So they wouldn't be doing any of that soon, I'm sure. "
            jac " Don't tell anyone else about this. "
            jac " Even though everyone's nice, I'm still not sure if they won't spread it around like a virus. "
            jac " If you tell anyone, I'm coming after you, got that? "
            " You nodded your head. "
            " You were probably gonna forget about this anyway. "
            " ...In about an hour or a day. "
            scene black with dissolve
            " You spent the rest of the break talking with Jacob. "
            " You guys were just hanging and chilling out... "
            " ...Honestly, if you had good memory and if you were devious you would probably spread what Jacob said around the school. "
            " But you woudln't do that...right? "
            if kind == True:
                " You're just a kind [person]! "
            elif calm == True:
                " You're just a chill [person]! "
            elif mean == True:
                " You're a mean [person], but not THAT mean...right? "
            " ...Right??? "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school to go to your classroom for the next class. "
            pause 2.0
            jump octphysicsclass2
        else:
            x " Oh, uh...hey [name]. "
            $ jacobknow = True
            jac " I'm Jacob. It's nice to meet you. "
            " Looks like he's cleaning up his saw... "
            " It's still got a few dirt stains on it. Wonder what happened. "
            " You asked him what he did to get it to be so dirty. "
            jac " Oh, my saw? "
            jac " ... "
            jac " ...It's gonna be embarrassing if I told you. "
            jac " Promise you won't laugh? "
            " You promised that you wouldn't laugh at him. "
            " And if you did, he was free to kick your ass. "
            " ...Actually, you might get your ass kicked if he's telling you to not laugh. "
            " Or not. That depends on what I say will happen. "
            " It's a part of the script, gang. "
            jac " Okay... "
            jac " ...So, I hadto check something outside of school... "
            jac " ...Then I rushed here thinking class was starting... "
            jac " But then I tripped and fell into the dirt causing my saw to get dirty. "
            jac " Thankfully no one else saw that... "
            jac " I would've been doomed if someone saw me fall and trip like that. "
            jac " I know for sure they're going to make a meme out of me if someone saw me... "
            jac " ...And I wouldn't want that to happen. "
            jac " Thankfully, most of the students here are nice... "
            jac " ...So they wouldn't be doing any of that soon, I'm sure. "
            jac " Don't tell anyone else about this. "
            jac " Even though everyone's nice, I'm still not sure if they won't spread it around like a virus. "
            jac " If you tell anyone, I'm coming after you, got that? "
            " You nodded your head. "
            " You were probably gonna forget about this anyway. "
            " ...In about an hour or a day. "
            scene black with dissolve
            " You spent the rest of the break talking with Jacob. "
            " You guys were just hanging and chilling out... "
            " ...Honestly, if you had good memory and if you were devious you would probably spread what Jacob said around the school. "
            " But you woudln't do that...right? "
            if kind == True:
                " You're just a kind [person]! "
            elif calm == True:
                " You're just a chill [person]! "
            elif mean == True:
                " You're a mean [person], but not THAT mean...right? "
            else:
                pass
            " ...Right??? "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school to go to your classroom for the next class. "
            pause 2.0
            jump octphysicsclass2
    label star:
        " You walked up to her, wanting to know what she was up to this time. "
        show matteneutral at center with easeinright
        if matteknow == True:
            " Looks like she's painting something... "
            " You didn't want to disturb her from her work, but you also wanted to talk to her. "
            " You just sat still and admired her work and waited for her to notice you. "
            " Eventually, after a few minutes of painting, she noticed you standing there. "
            ma " Oh, hiya [name]! "
            ma " I'm just working on a painting of the front of the school... "
            ma " It doesn't look bad now, does it? "
            " You took a look at her painting... "
            " It wasn't bad, it was actually really good. "
            " Pretty impressive for a girl her age. "
            " You reassured her that her painting was fine and that it looked really cool. "
            ma " Hehe, I'm glad you think so, [name]! "
            ma " I'm definitely gonna hang this up in my room later... "
            ma " ...This has to be one of my greatest artworks yet! "
            " You nodded, and took a look at her painting once more... "
            if jacobknow == True:
                " Then noticed a boy that fell onto the ground - wait, isn't that Jacob? "
            else:
                " Then noticed a boy that fell onto the ground. "
            " You were curious and decided to ask Matte about the boy. "
            " Wonder why she added him in there... "
            ma " Oh, that guy? "
            ma " Well, he sort of rushed over here for a bit...and fell... "
            ma " I thought he'd make a funny detail onto my work! "
            ma " Though I'm pretty sure that he wouldn't want me to show this to anyone else... "
            ma " If I'm gonna post this online, I'm gonna have to blur him out. "
            ma " Should be alright, right? "
            " You shrugged. You didn't really know if it's alright. "
            scene black with dissolve
            " You spent the rest of the break watching Matte paint. "
            " You liked how she added all of the tiny details into everything... "
            " You're surprised that she has this much talent considering how she's only 16. "
            " Very impressive...atleast it's not as bad as a 9 year old drawing Mona Lisa though. "
            " She must've took so long to learn all of this... "
            " It also probably was tiring to work on things like these. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit. Looks like Matte's gonna have to continue this later. "
            " You walked back into the school and you go to your classroom for the next class. "
            pause 2.0
            jump octphysicsclass2
        else:
            " Looks like she's painting something... "
            " You didn't want to disturb her from her work, but you also wanted to talk to her. "
            " You just sat still and admired her work and waited for her to notice you. "
            " Eventually, after a few minutes of painting, she noticed you standing there. "
            x " Oh, hiya [name]! "
            $ matteknow = True
            ma " I'm Matte! I like to paint n stuff...we're also classmates! "
            ma " The thing I'm working on right now? well...it's kind of obvious, don't you think? "
            ma " I'm just working on a painting of the front of the school... "
            ma " It doesn't look bad now, does it? "
            " You took a look at her painting... "
            " It wasn't bad, it was actually really good. "
            " Pretty impressive for a girl her age. "
            " You reassured her that her painting was fine and that it looked really cool. "
            ma " Hehe, I'm glad you think so, [name]! "
            ma " I'm definitely gonna hang this up in my room later... "
            ma " ...This has to be one of my greatest artworks yet! "
            " You nodded, and took a look at her painting once more... "
            if jacobknow == True:
                " Then noticed a boy that fell onto the ground - wait, isn't that Jacob? "
            else:
                " Then noticed a boy that fell onto the ground. "
            " You were curious and decided to ask Matte about the boy. "
            " Wonder why she added him in there... "
            ma " Oh, that guy? "
            ma " Well, he sort of rushed over here for a bit...and fell... "
            ma " I thought he'd make a funny detail onto my work! "
            ma " Though I'm pretty sure that he wouldn't want me to show this to anyone else... "
            ma " If I'm gonna post this online, I'm gonna have to blur him out. "
            ma " Should be alright, right? "
            " You shrugged. You didn't really know if it's alright. "
            scene black with dissolve
            " You spent the rest of the break watching Matte paint. "
            " You liked how she added all of the tiny details into everything... "
            " You're surprised that she has this much talent considering how she's only 16. "
            " Very impressive...atleast it's not as bad as a 9 year old drawing Mona Lisa though. "
            " She must've took so long to learn all of this... "
            " It also probably was tiring to work on things like these. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit. Looks like Matte's gonna have to continue this later. "
            " You walked back into the school and you go to your classroom for the next class. "
            pause 2.0
            jump octphysicsclass2
label octbackschool4:
    # nox, koa
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and spotted two of your classmates hanging out. "
    " Of course, you wanted to talk to one of them. "
    " But who do you talk to for this break? "
    if noxknow == True and koaknow == True:
        menu:
            " {image=noxicon} Nox {image=noxicon} ":
                jump mewmewmew
            " {image=koaicon} Koa {image=koaicon} ":
                jump barkbarkbark
    elif noxknow == True and koaknow == False:
        menu:
            " {image=noxicon} Nox {image=noxicon} ":
                jump mewmewmew
            " {image=koaicon} An emo looking guy {image=koaicon} ":
                jump barkbarkbark
    elif noxknow == False and koaknow == True:
        menu:
            " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                jump mewmewmew
            " {image=koaicon} Koa {image=koaicon} ":
                jump barkbarkbark
    else:
        menu:
            " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                jump mewmewmew
            " {image=koaicon} An emo looking guy {image=koaicon} ":
                jump barkbarkbark
    label mewmewmew:
        " You sat down on the ground next to him to see what he was doing. "
        show noxneutral at center with easeinleft
        if noxknow == True:
            n " ...Heya, [name]... "
            " You told him 'hello', and asked him what he was doing on his phone. "
            n " Just...*yawn*...playing a game to keep myself awake... "
            n " This is a game that I really like... "
            n " It's like, a rhythm game... I really like rhythm games... "
            n " And it's got lore, too... "
            n " Basically, there used to be a kingdom filled with music and magic... "
            n " But then, one day... "
            n " A queen who wanted complete silence attacked the kingdom... "
            n " And corrupted the beings of that kingdom and even the queen herself into being evil... "
            n " The last remaining non-corrupted beings prayed that the heroes would come and save them... "
            n " ...And then did...those heroes are all based off of the seven deadly sins... "
            n " The first character you unlock is basedoff of wrath, and she has a very cool guitar... "
            n " The second is based off of sloth, and she has a flute and this really cute bunny plushie... "
            n " I honestly relate to her a lot since she's often really sleepy... "
            n " And there's a lot more cool character's that I'd like to unlock... "
            n " But I'm still at level 15, so I only have a few and not all of them... "
            n " There's also tiny skins for these characters and I really want to 100 percent the game... "
            n " The songs are really good, too... "
            n " You should check this game out soon, [name]... "
            n " It's called: Sweet Sins Superstars... "
            n " Actually... you wanna watch me play right now...? "
            n " I'm trying to grind to get to level 30, which is the max level... "
            n " I don't mind if you want to watch me or anything... "
            " You had nothing else to do, so you decided to watch him. "
            n " Okayyyy... "
            scene black with dissolve
            " You spent the rest of the break watching Nox play a rhythm game... "
            " ...It honestly looked pretty fun to play. "
            " You should really check this game out one day. "
            " Even though it didn't really have a story other than the opening part, it still looked pretty well made. "
            " And cute. The characters looked really, really cute. "
            if kind == True:
                " You honestly liked that one character that was based off of gluttony. "
                " She looked really, really cute! "
            elif calm == True:
                " You honestly liked that one character that was based off of envy. "
                " She acted like a tsundere of some sorts, but she was adorable! "
            elif mean == True:
                " Out of all the characters, you really liked that one that was based off of wrath... "
                " ...Which was the first character you unlock, according to Nox. "
                " You didn't care if she was weak, you thought she looked really badass. "
            else:
                pause
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, stopping your gaming session with Nox. "
            " You get up from where you were sitting and you walked back to your classroom for the next class. "
            pause 2.0
            jump octphysicsclass2
        else:
            x " ...Heya, [name]... "
            $ noxknow = True
            n " I'm Nox, by the way....we're...*yawn*...classmates... "
            " You told him 'hello', and asked him what he was doing on his phone. "
            n " Just...*yawn*...playing a game to keep myself awake... "
            n " This is a game that I really like... "
            n " It's like, a rhythm game... I really like rhythm games... "
            n " And it's got lore, too... "
            n " Basically, there used to be a kingdom filled with music and magic... "
            n " But then, one day... "
            n " A queen who wanted complete silence attacked the kingdom... "
            n " And corrupted the beings of that kingdom and even the queen herself into being evil... "
            n " The last remaining non-corrupted beings prayed that the heroes would come and save them... "
            n " ...And then did...those heroes are all based off of the seven deadly sins... "
            n " The first character you unlock is basedoff of wrath, and she has a very cool guitar... "
            n " The second is based off of sloth, and she has a flute and this really cute bunny plushie... "
            n " I honestly relate to her a lot since she's often really sleepy... "
            n " And there's a lot more cool character's that I'd like to unlock... "
            n " But I'm still at level 15, so I only have a few and not all of them... "
            n " There's also tiny skins for these characters and I really want to 100 percent the game... "
            n " The songs are really good, too... "
            n " You should check this game out soon, [name]... "
            n " It's called: Sweet Sins Superstars... "
            n " Actually... you wanna watch me play right now...? "
            n " I'm trying to grind to get to level 30, which is the max level... "
            n " I don't mind if you want to watch me or anything... "
            " You had nothing else to do, so you decided to watch him. "
            n " Okayyyy... "
            scene black with dissolve
            " You spent the rest of the break watching Nox play a rhythm game... "
            " ...It honestly looked pretty fun to play. "
            " You should really check this game out one day. "
            " Even though it didn't really have a story other than the opening part, it still looked pretty well made. "
            " And cute. The characters looked really, really cute. "
            if kind == True:
                " You honestly liked that one character that was based off of gluttony. "
                " She looked really, really cute! "
            elif calm == True:
                " You honestly liked that one character that was based off of envy. "
                " She acted like a tsundere of some sorts, but she was adorable! "
            elif mean == True:
                " Out of all the characters, you really liked that one that was based off of wrath... "
                " ...Which was the first character you unlock, according to Nox. "
                " You didn't care if she was weak, you thought she looked really badass. "
            else:
                pause
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, stopping your gaming session with Nox. "
            " You get up from where you were sitting and you walked back to your classroom for the next class. "
            pause 2.0
            jump octphysicsclass2
    label barkbarkbark:
        " You sat down next to him to see what he was doing. "
        show koaneutral at center with easeinright
        if koaknow == True:
            " Looks like he was watching a youtube video. "
            " Didn't know he had managed to download something to watch... "
            " He didn't really look like the type to watch something in the middle of school. "
            " Maybe it's something that someone recommended to him? "
            " Probably. "
            " You poked his shoulder and asked him what video he was watching. "
            k " Hmmm? Oh, this? "
            k " This was just a video that my friend, Orchid, recommended me watching. "
            k " They told me that I would find this funny... "
            hide koaneutral at bottom
            show koahappy at center
            k " And honestly, they're right. "
            k " I laughed a bit here and there looking at this video... "
            k " Geez, Orchid really knows how to make me laugh. "
            k " You should watch this video with me, [name]. "
            k " Uh, er...only if you want to, of course. I'm not forcing you to watch with me. "
            k " I'm not that kind of guy. "
            " You had nothing to do, so of course you wanted to watch with him. "
            k " Alright, cmere...a little closer... "
            " Koa puts the phone between you two so that you two could watch properly... "
            " ...And he then unpauses the video he was watching. "
            scene black with dissolve
            " You spent the rest of thebreak watching a video with Koa. "
            " This Orchid person knew how to make people laugh, because you even got some laughs here and there. "
            " The video was really, really funny. "
            " You wonder how they even found such a golden video... "
            " ...No way they just found this in their for you page. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit of watching, interrupting your watching session with Koa. "
            " Looks like you're gonna have to watch that video later... "
            " You get up from where you were sitting and you walked back into the school to go to your classroom for the next class. "
            pause 2.0
            jump octphysicsclass2
        else:
            " Looks like he was watching a youtube video. "
            " Didn't know he had managed to download something to watch... "
            " He didn't really look like the type to watch something in the middle of school. "
            " Maybe it's something that someone recommended to him? "
            " Probably. "
            " You poked his shoulder and asked him what video he was watching. "
            x " Hmmm? Oh, this? "
            x " This was just a video that my friend, Orchid, recommended me watching. "
            x " They told me that I would find this funny... "
            hide koaneutral at bottom
            show koahappy at center
            x " And honestly, they're right. "
            x " I laughed a bit here and there looking at this video... "
            $ koaknow = True
            k " I'm uh, Koa, by the way. It's nice to meet you. "
            k " But geez, Orchid really knows how to make me laugh. "
            k " You should watch this video with me, [name]. "
            k " Uh, er...only if you want to, of course. I'm not forcing you to watch with me. "
            k " I'm not that kind of guy. "
            " You had nothing to do, so of course you wanted to watch with him. "
            k " Alright, cmere...a little closer... "
            " Koa puts the phone between you two so that you two could watch properly... "
            " ...And he then unpauses the video he was watching. "
            scene black with dissolve
            " You spent the rest of thebreak watching a video with Koa. "
            " This Orchid person knew how to make people laugh, because you even got some laughs here and there. "
            " The video was really, really funny. "
            " You wonder how they even found such a golden video... "
            " ...No way they just found this in their for you page. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit of watching, interrupting your watching session with Koa. "
            " Looks like you're gonna have to watch that video later... "
            " You get up from where you were sitting and you walked back into the school to go to your classroom for the next class. "
            pause 2.0
            jump octphysicsclass2
label octgym4:
    # disk, jam
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym and found two of your classmates talking to eachother. "
    " Wondering what they were talking about, you decided to walk to them and ask them whats up. "
    " Hopefully you weren't interrupting anything important... "
    show diskneutral at left with easeinright
    show jamneutral at right with easeinright
    if diskknow == True and jamknow == True:
        d " Mmm.. have you ever noticed that we look alike, Jam? "
        ja " Eh? Not really. "
        ja " I mean, I don't have poofy hair just like you. "
        ja " And my skin's kinda lighter than yours. "
        d " Yeah, but to someone random we kinda look alike! "
        d " I've been told that by some of the younger students here, eheh... "
        ja " Really...? "
        d " Mhm! They were like... "
        hide diskneutral at bottom
        show diskhappy at left
        d " Uncle Disk! Is Auntie Jam your sister? "
        d " You two really look alike! "
        ja " ...Is that really what they said? No way I look like you. "
        hide diskhappy at bottom
        show diskneutral at left
        d " Yes!! That's really what they said, no joke!! "
        ja " ...Interesting. "
        ja " You did tell them that we're not siblings, right? "
        d " Of course I did! Why wouldn't I? "
        d " They didn't believe me for a bit though, until Quinn came in. "
        hide diskneutral at bottom
        show diskjoyous at left
        d " What little cuties!! "
        d " Taking care of them has to be one of my favorite activities while we don't have class! "
        d " It's like I'm their very cool uncle that lets them do fun stuff! "
        ja " Well... you do give them a lot of candy for doing something simple. "
        hide diskjoyous at bottom
        show diskneutral at left
        d " The children must be fed! "
        " He notices you from the corner of his eye and he drags you over to him. "
        d " Heeeyy, [name]! Don't just be standing there! "
        d " Come and interact with us! "
        ja " You sure they want to? "
        d " I mean, why wouldn't they? If they didn't want to talk to us though, I'd feel really bad. "
        d " I don't wanna force people, you know! "
        d " Hey, wait...while [name]'s here... "
        d " [name]!! Do you think me and Jam look alike? "
        ja " ...(please say no) "
        menu:
            " You two look alike ":
                hide jamneutral at bottom
                show jamconfused at right
                ja " Oh come on, we're not even THAT similar! "
                hide diskneutral at bottom
                show diskhappy at left
                d " See? we really do look alike! "
                d " We should enter a contest where they'd make people guess if we're siblings or not! "
                hide jamconfused at bottom
                show jamangry at right
                ja " We are NOT doing that. "
                hide diskhappy at bottom
                show diskneutral at left
                d " Okay, okay1 Jeez...!! "
                scene black with dissolve
                " You spent the rest of the break talking to Disk and Jam. "
                " Jam still didn't believe that she and Disk looked alike... "
                " ...While Disk just continued commenting about how similar they looked. "
                " You could tell Jam was getitng annoyed, but you also found it funny, somehow. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time to go to another class. "
                " You walk back to your classroom for your next class. "
                pause 2.0
                jump octphysicsclass2
            " Nah ":
                hide jamneutral at bottom
                show jamhappy at right
                ja " See? told you that we don't look alike. "
                d " But that's just [name]'s opinion! "
                d " There could be other people who think that we're siblings! "
                d " We should enter a contest where they'd make people guess if we're siblings or not! "
                hide jamhappy at bottom
                show jamangry at right
                ja " We are NOT doing that. "
                d " Okay, okay1 Jeez...!! "
                scene black with dissolve
                " You spent the rest of the break talking to Disk and Jam. "
                " Jam still didn't believe that she and Disk looked alike... "
                " ...While Disk just continued commenting about how similar they looked. "
                " You could tell Jam was getitng annoyed, but you also found it funny, somehow. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time to go to another class. "
                " You walk back to your classroom for your next class. "
                pause 2.0
                jump octphysicsclass2
    elif diskknow == True and jamknow == False:
        d " Mmm.. have you ever noticed that we look alike, Jam? "
        x " Eh? Not really. "
        x " I mean, I don't have poofy hair just like you. "
        x " And my skin's kinda lighter than yours. "
        d " Yeah, but to someone random we kinda look alike! "
        d " I've been told that by some of the younger students here, eheh... "
        x " Really...? "
        d " Mhm! They were like... "
        hide diskneutral at bottom
        show diskhappy at left
        d " Uncle Disk! Is Auntie Jam your sister? "
        d " You two really look alike! "
        x " ...Is that really what they said? No way I look like you. "
        hide diskhappy at bottom
        show diskneutral at left
        d " Yes!! That's really what they said, no joke!! "
        x " ...Interesting. "
        x " You did tell them that we're not siblings, right? "
        d " Of course I did! Why wouldn't I? "
        d " They didn't believe me for a bit though, until Quinn came in. "
        hide diskneutral at bottom
        show diskjoyous at left
        d " What little cuties!! "
        d " Taking care of them has to be one of my favorite activities while we don't have class! "
        d " It's like I'm their very cool uncle that lets them do fun stuff! "
        x " Well... you do give them a lot of candy for doing something simple. "
        hide diskjoyous at bottom
        show diskneutral at left
        d " The children must be fed! "
        " He notices you from the corner of his eye and he drags you over to him. "
        d " Heeeyy, [name]! Don't just be standing there! "
        d " Come and interact with us! "
        x  " You sure they want to? "
        d " I mean, why wouldn't they? If they didn't want to talk to us though, I'd feel really bad. "
        d " I don't wanna force people, you know! "
        d " Hey, wait...while [name]'s here... "
        $ jamknow = True
        d " This is my friend, Jam!! Tell me, [name]... "
        d " Do you think me and Jam look alike? "
        ja " ...(please say no) "
        menu:
            " You two look alike ":
                hide jamneutral at bottom
                show jamconfused at right
                ja " Oh come on, we're not even THAT similar! "
                hide diskneutral at bottom
                show diskhappy at left
                d " See? we really do look alike! "
                d " We should enter a contest where they'd make people guess if we're siblings or not! "
                hide jamconfused at bottom
                show jamangry at right
                ja " We are NOT doing that. "
                hide diskhappy at bottom
                show diskneutral at left
                d " Okay, okay1 Jeez...!! "
                scene black with dissolve
                " You spent the rest of the break talking to Disk and Jam. "
                " Jam still didn't believe that she and Disk looked alike... "
                " ...While Disk just continued commenting about how similar they looked. "
                " You could tell Jam was getitng annoyed, but you also found it funny, somehow. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time to go to another class. "
                " You walk back to your classroom for your next class. "
                pause 2.0
                jump octphysicsclass2
            " Nah ":
                hide jamneutral at bottom
                show jamhappy at right
                ja " See? told you that we don't look alike. "
                d " But that's just [name]'s opinion! "
                d " There could be other people who think that we're siblings! "
                d " We should enter a contest where they'd make people guess if we're siblings or not! "
                hide jamhappy at bottom
                show jamangry at right
                ja " We are NOT doing that. "
                d " Okay, okay1 Jeez...!! "
                scene black with dissolve
                " You spent the rest of the break talking to Disk and Jam. "
                " Jam still didn't believe that she and Disk looked alike... "
                " ...While Disk just continued commenting about how similar they looked. "
                " You could tell Jam was getitng annoyed, but you also found it funny, somehow. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time to go to another class. "
                " You walk back to your classroom for your next class. "
                pause 2.0
                jump octphysicsclass2
    elif diskknow == False and jamknow == True:
        x " Mmm.. have you ever noticed that we look alike, Jam? "
        ja " Eh? Not really. "
        ja " I mean, I don't have poofy hair just like you. "
        ja " And my skin's kinda lighter than yours. "
        x " Yeah, but to someone random we kinda look alike! "
        x " I've been told that by some of the younger students here, eheh... "
        ja " Really...? "
        x " Mhm! They were like... "
        hide diskneutral at bottom
        show diskhappy at left
        $ diskknow = True
        d " Uncle Disk! Is Auntie Jam your sister? "
        d " You two really look alike! "
        " ...Huh, so Disk's his name. Cool. "
        ja " ...Is that really what they said? No way I look like you. "
        hide diskhappy at bottom
        show diskneutral at left
        d " Yes!! That's really what they said, no joke!! "
        ja " ...Interesting. "
        ja " You did tell them that we're not siblings, right? "
        d " Of course I did! Why wouldn't I? "
        d " They didn't believe me for a bit though, until Quinn came in. "
        hide diskneutral at bottom
        show diskjoyous at left
        d " What little cuties!! "
        d " Taking care of them has to be one of my favorite activities while we don't have class! "
        d " It's like I'm their very cool uncle that lets them do fun stuff! "
        ja " Well... you do give them a lot of candy for doing something simple. "
        hide diskjoyous at bottom
        show diskneutral at left
        d " The children must be fed! "
        " He notices you from the corner of his eye and he drags you over to him. "
        d " Heeeyy, [name]! Don't just be standing there! "
        d " Come and interact with us! "
        ja " You sure they want to? "
        d " I mean, why wouldn't they? If they didn't want to talk to us though, I'd feel really bad. "
        d " I don't wanna force people, you know! "
        d " Hey, wait...while [name]'s here... "
        d " [name]!! Do you think me and Jam look alike? "
        ja " ...(please say no) "
        menu:
            " You two look alike ":
                hide jamneutral at bottom
                show jamconfused at right
                ja " Oh come on, we're not even THAT similar! "
                hide diskneutral at bottom
                show diskhappy at left
                d " See? we really do look alike! "
                d " We should enter a contest where they'd make people guess if we're siblings or not! "
                hide jamconfused at bottom
                show jamangry at right
                ja " We are NOT doing that. "
                hide diskhappy at bottom
                show diskneutral at left
                d " Okay, okay1 Jeez...!! "
                scene black with dissolve
                " You spent the rest of the break talking to Disk and Jam. "
                " Jam still didn't believe that she and Disk looked alike... "
                " ...While Disk just continued commenting about how similar they looked. "
                " You could tell Jam was getitng annoyed, but you also found it funny, somehow. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time to go to another class. "
                " You walk back to your classroom for your next class. "
                pause 2.0
                jump octphysicsclass2
            " Nah ":
                hide jamneutral at bottom
                show jamhappy at right
                ja " See? told you that we don't look alike. "
                d " But that's just [name]'s opinion! "
                d " There could be other people who think that we're siblings! "
                d " We should enter a contest where they'd make people guess if we're siblings or not! "
                hide jamhappy at bottom
                show jamangry at right
                ja " We are NOT doing that. "
                d " Okay, okay1 Jeez...!! "
                scene black with dissolve
                " You spent the rest of the break talking to Disk and Jam. "
                " Jam still didn't believe that she and Disk looked alike... "
                " ...While Disk just continued commenting about how similar they looked. "
                " You could tell Jam was getitng annoyed, but you also found it funny, somehow. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time to go to another class. "
                " You walk back to your classroom for your next class. "
                pause 2.0
                jump octphysicsclass2
    else:
        x " Mmm.. have you ever noticed that we look alike, Jam? "
        x " Eh? Not really. "
        x " I mean, I don't have poofy hair just like you. "
        x " And my skin's kinda lighter than yours. "
        x " Yeah, but to someone random we kinda look alike! "
        x " I've been told that by some of the younger students here, eheh... "
        x " Really...? "
        x " Mhm! They were like... "
        hide diskneutral at bottom
        show diskhappy at left
        $ diskknow = True
        d " Uncle Disk! Is Auntie Jam your sister? "
        d " You two really look alike! "
        " Huh. So Disk's his name. Cool. "
        x " ...Is that really what they said? No way I look like you. "
        hide diskhappy at bottom
        show diskneutral at left
        d " Yes!! That's really what they said, no joke!! "
        x " ...Interesting. "
        x " You did tell them that we're not siblings, right? "
        d " Of course I did! Why wouldn't I? "
        d " They didn't believe me for a bit though, until Quinn came in. "
        hide diskneutral at bottom
        show diskjoyous at left
        d " What little cuties!! "
        d " Taking care of them has to be one of my favorite activities while we don't have class! "
        d " It's like I'm their very cool uncle that lets them do fun stuff! "
        x " Well... you do give them a lot of candy for doing something simple. "
        hide diskjoyous at bottom
        show diskneutral at left
        d " The children must be fed! "
        " He notices you from the corner of his eye and he drags you over to him. "
        d " Heeeyy, [name]! Don't just be standing there! "
        d " Come and interact with us! "
        x  " You sure they want to? "
        d " I mean, why wouldn't they? If they didn't want to talk to us though, I'd feel really bad. "
        d " I don't wanna force people, you know! "
        d " Hey, wait...while [name]'s here... "
        $ jamknow = True
        d " This is my friend, Jam!! Tell me, [name]... "
        d " Do you think me and Jam look alike? "
        ja " ...(please say no) "
        menu:
            " You two look alike ":
                hide jamneutral at bottom
                show jamconfused at right
                ja " Oh come on, we're not even THAT similar! "
                hide diskneutral at bottom
                show diskhappy at left
                d " See? we really do look alike! "
                d " We should enter a contest where they'd make people guess if we're siblings or not! "
                hide jamconfused at bottom
                show jamangry at right
                ja " We are NOT doing that. "
                hide diskhappy at bottom
                show diskneutral at left
                d " Okay, okay1 Jeez...!! "
                scene black with dissolve
                " You spent the rest of the break talking to Disk and Jam. "
                " Jam still didn't believe that she and Disk looked alike... "
                " ...While Disk just continued commenting about how similar they looked. "
                " You could tell Jam was getitng annoyed, but you also found it funny, somehow. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time to go to another class. "
                " You walk back to your classroom for your next class. "
                pause 2.0
                jump octphysicsclass2
            " Nah ":
                hide jamneutral at bottom
                show jamhappy at right
                ja " See? told you that we don't look alike. "
                d " But that's just [name]'s opinion! "
                d " There could be other people who think that we're siblings! "
                d " We should enter a contest where they'd make people guess if we're siblings or not! "
                hide jamhappy at bottom
                show jamangry at right
                ja " We are NOT doing that. "
                d " Okay, okay1 Jeez...!! "
                scene black with dissolve
                " You spent the rest of the break talking to Disk and Jam. "
                " Jam still didn't believe that she and Disk looked alike... "
                " ...While Disk just continued commenting about how similar they looked. "
                " You could tell Jam was getitng annoyed, but you also found it funny, somehow. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time to go to another class. "
                " You walk back to your classroom for your next class. "
                pause 2.0
                jump octphysicsclass2
label octcafe4:
    # carmen, spark
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted two of your classmates talking to eachother. "
    " Curious on what they're talking about, you decided to talk to them. "
    " Just praying that you don't accidentally walk into something important. "
    show sparkneutral at left with easeinright
    show carmenneutral at right with easeinright
    if carmenknow == True and sparkknow == True:
        sp " I just don't know what to do, Carmen. "
        sp " I mean - it's insane to think I actually fell inlove with someone. "
        sp " What makes it crazier is that they aren't even from this school. "
        ca " ...? "
        sp " Okay, so - "
        " He interrupts himself when he notices that you were there. "
        sp " Oh, hey [name]. "
        sp " We're just talking about some guy I met at another school... "
        sp " You wanna hear about the story? "
        " Well, you did come here to talk, so... "
        " You nodded your head, sitting down near Carmen and getting ready to hear Spark's story. "
        sp " Okay, here we go... "
        sp " So, everyone including me had to retreat to this one school called... "
        sp " 'Paper school' or something, right? "
        sp " We had to stay there for a week because of some issues, apparently. "
        sp " They didn't specify what issues, they just said...issues. "
        sp " We didn't really question it, so we spent our time learning there. "
        sp " We all had to sit in the back of their classrooms everytime it was time to learn something new.. "
        sp " ...Taking down notes and everything... "
        sp " Though, there was this one time where I was scrolling on my phone, and this shrot ass guy... "
        sp " Came up to me and snatched it away. "
        sp " Obviously, I was annoyed, but I also thought that he was... "
        hide sparkneutral at bottom
        show sparkshit at left
        sp " ...Hot???? Like, he was one of the troublemakers, yes, but I somehow thought he was CUTE. "
        hide carmenneutral at bottom
        show carmenhappy at right
        " Spark didn't notice that Carmen started playing careless whisper on his guitar. "
        " This honestly just makes the situation funnier. "
        sp " And I was like - no, I can't be falling for this guy! "
        sp " He's literally one of the school bullies, that's just fucking insane! "
        sp " I eventually took back my phone since I was taller than him, but... "
        sp " ARGHHHHHH ever since that day I've been SO flustered and Temero keeps on teasing me about it - "
        sp " AND HE EVEN GAVE ME HIS PHONE NUMBER TOO ONCE THE WEEK WAS OVER??? "
        sp " HE STILL TEXTS ME TO THIS DAY AND HE'S JUST SO - "
        " Spark finally notices what song Carmen was playing. "
        sp " ...H-hey! cut that out! "
        ca " ...:D (bro im js helping out wdym) "
        scene black with dissolve
        " You spent the rest of the break talking with Spark and Carmen. "
        " You and Carmen kinda just teased him about his crush on the guy... "
        " ...You also made 'what ifs' for Spark. Like for exameple... "
        " What if his crush visits him and takes him out on a date? Sounds insane, I know, but it's a what if, so... "
        " Spark went insane over all of those what if's you and Carmen made. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, unfortunately stopping your teasing session. "
        " You get up from where you were sitting, and you walked back to your classroom for the next class. "
        pause 2.0
        jump octphysicsclass2
    elif carmenknow == True and sparkknow == False:
        x " I just don't know what to do, Carmen. "
        x " I mean - it's insane to think I actually fell inlove with someone. "
        x " What makes it crazier is that they aren't even from this school. "
        ca " ...? "
        x " Okay, so - "
        " He interrupts himself when he notices that you were there. "
        x " Oh, hey [name]. "
        $ sparkknow = True
        sp " I'm Spark by the way. And uh... "
        sp " We're just talking about some guy I met at another school... "
        sp " You wanna hear about the story? "
        " Well, you did come here to talk, so... "
        " You nodded your head, sitting down near Carmen and getting ready to hear Spark's story. "
        sp " Okay, here we go... "
        sp " So, everyone including me had to retreat to this one school called... "
        sp " 'Paper school' or something, right? "
        sp " We had to stay there for a week because of some issues, apparently. "
        sp " They didn't specify what issues, they just said...issues. "
        sp " We didn't really question it, so we spent our time learning there. "
        sp " We all had to sit in the back of their classrooms everytime it was time to learn something new.. "
        sp " ...Taking down notes and everything... "
        sp " Though, there was this one time where I was scrolling on my phone, and this shrot ass guy... "
        sp " Came up to me and snatched it away. "
        sp " Obviously, I was annoyed, but I also thought that he was... "
        hide sparkneutral at bottom
        show sparkshit at left
        sp " ...Hot???? Like, he was one of the troublemakers, yes, but I somehow thought he was CUTE. "
        hide carmenneutral at bottom
        show carmenhappy at right
        " Spark didn't notice that Carmen started playing careless whisper on his guitar. "
        " This honestly just makes the situation funnier. "
        sp " And I was like - no, I can't be falling for this guy! "
        sp " He's literally one of the school bullies, that's just fucking insane! "
        sp " I eventually took back my phone since I was taller than him, but... "
        sp " ARGHHHHHH ever since that day I've been SO flustered and Temero keeps on teasing me about it - "
        sp " AND HE EVEN GAVE ME HIS PHONE NUMBER TOO ONCE THE WEEK WAS OVER??? "
        sp " HE STILL TEXTS ME TO THIS DAY AND HE'S JUST SO - "
        " Spark finally notices what song Carmen was playing. "
        sp " ...H-hey! cut that out! "
        ca " ...:D (bro im js helping out wdym) "
        scene black with dissolve
        " You spent the rest of the break talking with Spark and Carmen. "
        " You and Carmen kinda just teased him about his crush on the guy... "
        " ...You also made 'what ifs' for Spark. Like for exameple... "
        " What if his crush visits him and takes him out on a date? Sounds insane, I know, but it's a what if, so... "
        " Spark went insane over all of those what if's you and Carmen made. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, unfortunately stopping your teasing session. "
        " You get up from where you were sitting, and you walked back to your classroom for the next class. "
        pause 2.0
        jump octphysicsclass2
    elif carmenknow == False and sparkknow == True:
        sp " I just don't know what to do, Carmen. "
        $ carmenknow = True
        " So Carmen's that guys name...huh. "
        " The one with the guitar, I mean. "
        sp " I mean - it's insane to think I actually fell inlove with someone. "
        sp " What makes it crazier is that they aren't even from this school. "
        ca " ...? "
        sp " Okay, so - "
        " He interrupts himself when he notices that you were there. "
        sp " Oh, hey [name]. "
        sp " We're just talking about some guy I met at another school... "
        sp " You wanna hear about the story? "
        " Well, you did come here to talk, so... "
        " You nodded your head, sitting down near Carmen and getting ready to hear Spark's story. "
        sp " Okay, here we go... "
        sp " So, everyone including me had to retreat to this one school called... "
        sp " 'Paper school' or something, right? "
        sp " We had to stay there for a week because of some issues, apparently. "
        sp " They didn't specify what issues, they just said...issues. "
        sp " We didn't really question it, so we spent our time learning there. "
        sp " We all had to sit in the back of their classrooms everytime it was time to learn something new.. "
        sp " ...Taking down notes and everything... "
        sp " Though, there was this one time where I was scrolling on my phone, and this shrot ass guy... "
        sp " Came up to me and snatched it away. "
        sp " Obviously, I was annoyed, but I also thought that he was... "
        hide sparkneutral at bottom
        show sparkshit at left
        sp " ...Hot???? Like, he was one of the troublemakers, yes, but I somehow thought he was CUTE. "
        hide carmenneutral at bottom
        show carmenhappy at right
        " Spark didn't notice that Carmen started playing careless whisper on his guitar. "
        " This honestly just makes the situation funnier. "
        sp " And I was like - no, I can't be falling for this guy! "
        sp " He's literally one of the school bullies, that's just fucking insane! "
        sp " I eventually took back my phone since I was taller than him, but... "
        sp " ARGHHHHHH ever since that day I've been SO flustered and Temero keeps on teasing me about it - "
        sp " AND HE EVEN GAVE ME HIS PHONE NUMBER TOO ONCE THE WEEK WAS OVER??? "
        sp " HE STILL TEXTS ME TO THIS DAY AND HE'S JUST SO - "
        " Spark finally notices what song Carmen was playing. "
        sp " ...H-hey! cut that out! "
        ca " ...:D (bro im js helping out wdym) "
        scene black with dissolve
        " You spent the rest of the break talking with Spark and Carmen. "
        " You and Carmen kinda just teased him about his crush on the guy... "
        " ...You also made 'what ifs' for Spark. Like for exameple... "
        " What if his crush visits him and takes him out on a date? Sounds insane, I know, but it's a what if, so... "
        " Spark went insane over all of those what if's you and Carmen made. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, unfortunately stopping your teasing session. "
        " You get up from where you were sitting, and you walked back to your classroom for the next class. "
        pause 2.0
        jump octphysicsclass2
    else:
        x " I just don't know what to do, Carmen. "
        $ carmenknow = True
        " So Carmen's that guys name...huh. "
        " The one with the guitar, I mean. "
        x " I mean - it's insane to think I actually fell inlove with someone. "
        x " What makes it crazier is that they aren't even from this school. "
        ca " ...? "
        x " Okay, so - "
        " He interrupts himself when he notices that you were there. "
        x " Oh, hey [name]. "
        $ sparkknow = True
        sp " I'm Spark by the way. And uh... "
        sp " We're just talking about some guy I met at another school... "
        sp " You wanna hear about the story? "
        " Well, you did come here to talk, so... "
        " You nodded your head, sitting down near Carmen and getting ready to hear Spark's story. "
        sp " Okay, here we go... "
        sp " So, everyone including me had to retreat to this one school called... "
        sp " 'Paper school' or something, right? "
        sp " We had to stay there for a week because of some issues, apparently. "
        sp " They didn't specify what issues, they just said...issues. "
        sp " We didn't really question it, so we spent our time learning there. "
        sp " We all had to sit in the back of their classrooms everytime it was time to learn something new.. "
        sp " ...Taking down notes and everything... "
        sp " Though, there was this one time where I was scrolling on my phone, and this shrot ass guy... "
        sp " Came up to me and snatched it away. "
        sp " Obviously, I was annoyed, but I also thought that he was... "
        hide sparkneutral at bottom
        show sparkshit at left
        sp " ...Hot???? Like, he was one of the troublemakers, yes, but I somehow thought he was CUTE. "
        hide carmenneutral at bottom
        show carmenhappy at right
        " Spark didn't notice that Carmen started playing careless whisper on his guitar. "
        " This honestly just makes the situation funnier. "
        sp " And I was like - no, I can't be falling for this guy! "
        sp " He's literally one of the school bullies, that's just fucking insane! "
        sp " I eventually took back my phone since I was taller than him, but... "
        sp " ARGHHHHHH ever since that day I've been SO flustered and Temero keeps on teasing me about it - "
        sp " AND HE EVEN GAVE ME HIS PHONE NUMBER TOO ONCE THE WEEK WAS OVER??? "
        sp " HE STILL TEXTS ME TO THIS DAY AND HE'S JUST SO - "
        " Spark finally notices what song Carmen was playing. "
        sp " ...H-hey! cut that out! "
        ca " ...:D (bro im js helping out wdym) "
        scene black with dissolve
        " You spent the rest of the break talking with Spark and Carmen. "
        " You and Carmen kinda just teased him about his crush on the guy... "
        " ...You also made 'what ifs' for Spark. Like for exameple... "
        " What if his crush visits him and takes him out on a date? Sounds insane, I know, but it's a what if, so... "
        " Spark went insane over all of those what if's you and Carmen made. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, unfortunately stopping your teasing session. "
        " You get up from where you were sitting, and you walked back to your classroom for the next class. "
        pause 2.0
        jump octphysicsclass2
label octrooftop4:
    # quinn, orchid
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked onto the rooftop and found two of your classmates just hanging out. "
    " You wanted to talk to one of them...but who do you talk to? "
    if quinnknow == True and orchidknow == True:
        menu:
            " {image=quinnicon} Quinn {image=quinnicon} ":
                jump ohmybackhurts
            " {image=orchidicon} Orchid {image=orchidicon} ":
                jump ohmylegshurt
    elif quinnknow == True and orchidknow == False:
        menu:
            " {image=quinnicon} Quinn {image=quinnicon} ":
                jump ohmybackhurts
            " {image=orchidicon} A scene kid {image=orchidicon} ":
                jump ohmylegshurt
    elif quinnknow == False and orchidknow == True:
        menu:
            " {image=quinnicon} A drama kid {image=quinnicon} ":
                jump ohmybackhurts
            " {image=orchidicon} Orchid {image=orchidicon} ":
                jump ohmylegshurt
    else:
        menu:
            " {image=quinnicon} A drama kid {image=quinnicon} ":
                jump ohmybackhurts
            " {image=orchidicon} A scene kid {image=orchidicon} ":
                jump ohmylegshurt
    label ohmybackhurts:
        " You walked up to him to check on on what he's doing. "
        show quinnneutral at center with easeinleft
        if quinnknow == True:
            q " Ah, [name]! lovely to see you up here. "
            q " You see, I just wanted to come up here to take some fresh air... "
            hide quinnneutral at bottom
            show quinnangry at center
            q " Because of my club members being really infuriating nowadays. "
            q " Seriously, I tell them to do something one time, right? "
            q " And then they would keep asking me: 'What do I need to do again?' "
            q " I mean, it's fine by me if you asked me about three times... "
            q " BUT SIX WHOLE TIMES?? "
            q " It's kind of annoying at that point, like geez... "
            q " How can you get this forgetful? "
            q " I get that I have to be open minded and all of that, but DAMN... "
            q " You could've alteast taken down a few notes and looked at it to remember what you had to do. "
            q " Jesus christ... "
            hide quinnangry at bottom
            show quinnneutral at center
            q " ...Annnnd that's why I came up here. "
            q " My brother, Disk doesn't really like it whenever I get mad. "
            q " So I find other places to calm down in, like the rooftop for example. "
            q " Someplace where Disk isn't here to see me like this. "
            q " ... "
            hide quinnneutral at bottom
            show quinnsad at center
            q " ...Speaking of my brother, he's such a ball of sunshine... "
            q " Not that it's a problem, but uh... "
            q " If you've ever met him, you know how he's really energetic, right? "
            q " His energy is...let's say it's infectious. "
            q " Even when I'm feeling down, he somehow manages to cheer me up. "
            q " I don't understand how he could be this happy... "
            q " ...Even when I know there's times where he doesn't feel okay... "
            q " ...He's always smiling. Even when I tell him it's okay not to. "
            q " I asked him why he keeps smiling even after all we've been through, and he just responded with this: "
            q " 'Because smiling means that I haven't let anything break me...' "
            q " 'Because I still believe that there's light at the end of this, and that we're worth something better...' "
            q " 'Because as long as I can smile, I know there's hope - for the both of us.' "
            q " 'That's why I keep smiling.' "
            q " ...God, that idiot sometimes makes me so happy to the point I cry... "
            hide quinnsad at bottom
            show quinnneutral at center
            q " ...He's a good older brother. "
            scene black with dissolve
            " You spent the rest of the break talking with Quinn about his older brother. "
            " He shared some nice stories about his older brother, some cool ones, some sad ones... "
            " He really likes his brother a whole lot, huh? "
            " You can see why. His brother is really inspiring with what he said about smiling. "
            " You wished you had someone like that in your life. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get off of the rooftop and you walked back down to get to your classroom for the next class. "
            pause 2.0
            jump octphysicsclass2
        else:
            x " Ah, [name]! lovely to see you up here. "
            $ quinnknow = True
            q " I'm Quinn, by the way. I'm in the drama club. "
            q " You see, I just wanted to come up here to take some fresh air... "
            hide quinnneutral at bottom
            show quinnangry at center
            q " Because of my club members being really infuriating nowadays. "
            q " Seriously, I tell them to do something one time, right? "
            q " And then they would keep asking me: 'What do I need to do again?' "
            q " I mean, it's fine by me if you asked me about three times... "
            q " BUT SIX WHOLE TIMES?? "
            q " It's kind of annoying at that point, like geez... "
            q " How can you get this forgetful? "
            q " I get that I have to be open minded and all of that, but DAMN... "
            q " You could've alteast taken down a few notes and looked at it to remember what you had to do. "
            q " Jesus christ... "
            hide quinnangry at bottom
            show quinnneutral at center
            q " ...Annnnd that's why I came up here. "
            q " My brother, Disk doesn't really like it whenever I get mad. "
            q " So I find other places to calm down in, like the rooftop for example. "
            q " Someplace where Disk isn't here to see me like this. "
            q " ... "
            hide quinnneutral at bottom
            show quinnsad at center
            q " ...Speaking of my brother, he's such a ball of sunshine... "
            q " Not that it's a problem, but uh... "
            q " If you've ever met him, you know how he's really energetic, right? "
            q " His energy is...let's say it's infectious. "
            q " Even when I'm feeling down, he somehow manages to cheer me up. "
            q " I don't understand how he could be this happy... "
            q " ...Even when I know there's times where he doesn't feel okay... "
            q " ...He's always smiling. Even when I tell him it's okay not to. "
            q " I asked him why he keeps smiling even after all we've been through, and he just responded with this: "
            q " 'Because smiling means that I haven't let anything break me...' "
            q " 'Because I still believe that there's light at the end of this, and that we're worth something better...' "
            q " 'Because as long as I can smile, I know there's hope - for the both of us.' "
            q " 'That's why I keep smiling.' "
            q " ...God, that idiot sometimes makes me so happy to the point I cry... "
            hide quinnsad at bottom
            show quinnneutral at center
            q " ...He's a good older brother. "
            scene black with dissolve
            " You spent the rest of the break talking with Quinn about his older brother. "
            " He shared some nice stories about his older brother, some cool ones, some sad ones... "
            " He really likes his brother a whole lot, huh? "
            " You can see why. His brother is really inspiring with what he said about smiling. "
            " You wished you had someone like that in your life. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get off of the rooftop and you walked back down to get to your classroom for the next class. "
            pause 2.0
            jump octphysicsclass2
    label ohmylegshurt:
        " You walked up to them to check out on what they're doing. "
        show orchidneutral at center with easeinright
        if orchidknow == True:
            oc " Heya, [name]!! "
            oc " You know, I've been listening to this song recently... "
            oc " It's about this girl in a yellow cardigan! "
            oc " The song meaning is sad, yes, but it's tune is also catchy... "
            oc " Geez, why do sad songs have to be so catchy and why do happy songs have to sound so... "
            oc " Eeeh, you get the idea. "
            oc " So, basically this song is about a girl comforting other people who want to...you know... "
            oc " Reset character? yes, that's the best way I can describe it. "
            oc " And at the end part, turns out those people were just fake... "
            oc " ...And that was her trying to stop herself from just ending it all. "
            oc " But in the end, she ended up doing it, and couldn't stop herself... "
            oc " It's sad, but the song... "
            hide orchidneutral at bottom
            show orchidangry at center
            oc " IT'S WAY TOO CATCHY!!! "
            oc " Like, good heavens, I know you're trying to make a good story, but... "
            oc " You didn't have to make a sad song sound so good!! "
            oc " Like good lord!! "
            scene black with dissolve
            " You spent the rest of the break listening to Orchid go on a rampage about the song. "
            " They played the song for you, and you agreed, it was pretty catchy. "
            " And the song meaning was pretty sad... "
            " ...You should add this song into your playlist, but before you do that... "
            " If any of you playing this is suffering through tough times, please talk to someone who you trust. "
            " Whether it's your family, your friends...even an object, talk to whatever comforts you. "
            " Remember that there's always gonna be someone there for you, even though right now there seems to be no one. "
            " You're gonna be alright, dude. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get off of the rooftop and you walked back down to get to your classroom for the next class. "
            pause 2.0
            jump octphysicsclass2
        else:
            x " Heya, [name]!! "
            $ orchidknow = True
            oc " I'm Orchid, by the way! We're classmates! "
            oc " You know, I've been listening to this song recently... "
            oc " It's about this girl in a yellow cardigan! "
            oc " The song meaning is sad, yes, but it's tune is also catchy... "
            oc " Geez, why do sad songs have to be so catchy and why do happy songs have to sound so... "
            oc " Eeeh, you get the idea. "
            oc " So, basically this song is about a girl comforting other people who want to...you know... "
            oc " Reset character? yes, that's the best way I can describe it. "
            oc " And at the end part, turns out those people were just fake... "
            oc " ...And that was her trying to stop herself from just ending it all. "
            oc " But in the end, she ended up doing it, and couldn't stop herself... "
            oc " It's sad, but the song... "
            hide orchidneutral at bottom
            show orchidangry at center
            oc " IT'S WAY TOO CATCHY!!! "
            oc " Like, good heavens, I know you're trying to make a good story, but... "
            oc " You didn't have to make a sad song sound so good!! "
            oc " Like good lord!! "
            scene black with dissolve
            " You spent the rest of the break listening to Orchid go on a rampage about the song. "
            " They played the song for you, and you agreed, it was pretty catchy. "
            " And the song meaning was pretty sad... "
            " ...You should add this song into your playlist, but before you do that... "
            " If any of you playing this is suffering through tough times, please talk to someone who you trust. "
            " Whether it's your family, your friends...even an object, talk to whatever comforts you. "
            " Remember that there's always gonna be someone there for you, even though right now there seems to be no one. "
            " You're gonna be alright, dude. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get off of the rooftop and you walked back down to get to your classroom for the next class. "
            pause 2.0
            jump octphysicsclass2
label octlibrary4:
    # yinhui and temero
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the classroom and spotted two of your classmates talking with eachother. "
    " Curious on what they're talking about, you decided to walk up to them and talk with them. "
    " Hopefully you're not walking into something important. "
    show temeroneutral at left with easeinright
    show yinhuineutral at right with easeinright
    if temeroknow == True and yinhuiknow == True:
        tm " Come on, you suuuure you don't want this potion? "
        tm " I know you want your brother to be safe, so I made this! "
        tm " Keeps anyone from ever touching him. "
        yi " ... "
        yi " Look Temero, yes I do want my brother to be safe, but I don't trust you. "
        hide temeroneutral at bottom
        show temerohappy at left
        tm " Aww, come on, Yinhuiii! What's there NOT to trust about me? "
        tm " I'm 100 percent trustable, you see? "
        tm " Remember that one time I grew Mia's plants? "
        tm " She looked really happy that they instantly grew!! "
        yi " ...You mean that one time the other day where you 'accidentally blew up' her plants? "
        yi " Yeah, no. "
        yi " And besides, why would I rely on a potion to keep my brother safe? "
        yi " I know better than to trust someone like you. "
        yi " You could do very horrible things to my brother without me even knowing. "
        yi " Therefore, I'm not taking your potion. "
        tm " Aww, come on! "
        tm " It's not gonna be that bad!! "
        " She notices that you were there, and you immediately got pulled close to her. "
        tm " See, [name] trust me!! right, [name]? "
        " You shrugged. You don't really know if she's really trustable or not. "
        " She does have that suspicious energy within her.. "
        yi " ...Yeah, no, I'm out. "
        tm " Come on, Yinn!! "
        scene black with dissolve
        " You spent the rest of the break watching Temero convince Yinhui to take her potion.. "
        " Though, it didn't work and Yinhui left. "
        " And now you had to deal with Temero ranting to you about it. "
        " Honestly, you were kind of just zoning out as she ranted to you... "
        " Playing some card games in your head as she yapped. "
        " You were just waiting for when the bell would finally ring... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit of you having to endure the pain of hearing someone ranting to you. "
        " You immediately walked out of the library so that you could get to your classroom for the next class. "
        pause 2.0
        jump octphysicsclass2
    elif temeroknow == True and yinhuiknow == False:
        tm " Come on, you suuuure you don't want this potion? "
        tm " I know you want your brother to be safe, so I made this! "
        tm " Keeps anyone from ever touching him. "
        x " ... "
        x " Look Temero, yes I do want my brother to be safe, but I don't trust you. "
        hide temeroneutral at bottom
        show temerohappy at left
        $ yinhuiknow = True
        tm " Aww, come on, Yinhuiii! What's there NOT to trust about me? "
        " ...So Yinhui's that guys name. "
        tm " I'm 100 percent trustable, you see? "
        tm " Remember that one time I grew Mia's plants? "
        tm " She looked really happy that they instantly grew!! "
        yi " ...You mean that one time the other day where you 'accidentally blew up' her plants? "
        yi " Yeah, no. "
        yi " And besides, why would I rely on a potion to keep my brother safe? "
        yi " I know better than to trust someone like you. "
        yi " You could do very horrible things to my brother without me even knowing. "
        yi " Therefore, I'm not taking your potion. "
        tm " Aww, come on! "
        tm " It's not gonna be that bad!! "
        " She notices that you were there, and you immediately got pulled close to her. "
        tm " See, [name] trust me!! right, [name]? "
        " You shrugged. You don't really know if she's really trustable or not. "
        " She does have that suspicious energy within her.. "
        yi " ...Yeah, no, I'm out. "
        tm " Come on, Yinn!! "
        scene black with dissolve
        " You spent the rest of the break watching Temero convince Yinhui to take her potion.. "
        " Though, it didn't work and Yinhui left. "
        " And now you had to deal with Temero ranting to you about it. "
        " Honestly, you were kind of just zoning out as she ranted to you... "
        " Playing some card games in your head as she yapped. "
        " You were just waiting for when the bell would finally ring... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit of you having to endure the pain of hearing someone ranting to you. "
        " You immediately walked out of the library so that you could get to your classroom for the next class. "
        pause 2.0
        jump octphysicsclass2
    elif temeroknow == False and yinhuiknow == True:
        x " Come on, you suuuure you don't want this potion? "
        x " I know you want your brother to be safe, so I made this! "
        x " Keeps anyone from ever touching him. "
        yi " ... "
        yi " Look Temero, yes I do want my brother to be safe, but I don't trust you. "
        $ temeroknow = True
        " ...So Temero's that girls name. "
        hide temeroneutral at bottom
        show temerohappy at left
        tm " Aww, come on, Yinhuiii! What's there NOT to trust about me? "
        tm " I'm 100 percent trustable, you see? "
        tm " Remember that one time I grew Mia's plants? "
        tm " She looked really happy that they instantly grew!! "
        yi " ...You mean that one time the other day where you 'accidentally blew up' her plants? "
        yi " Yeah, no. "
        yi " And besides, why would I rely on a potion to keep my brother safe? "
        yi " I know better than to trust someone like you. "
        yi " You could do very horrible things to my brother without me even knowing. "
        yi " Therefore, I'm not taking your potion. "
        tm " Aww, come on! "
        tm " It's not gonna be that bad!! "
        " She notices that you were there, and you immediately got pulled close to her. "
        tm " See, [name] trust me!! right, [name]? "
        " You shrugged. You don't really know if she's really trustable or not. "
        " She does have that suspicious energy within her.. "
        yi " ...Yeah, no, I'm out. "
        tm " Come on, Yinn!! "
        scene black with dissolve
        " You spent the rest of the break watching Temero convince Yinhui to take her potion.. "
        " Though, it didn't work and Yinhui left. "
        " And now you had to deal with Temero ranting to you about it. "
        " Honestly, you were kind of just zoning out as she ranted to you... "
        " Playing some card games in your head as she yapped. "
        " You were just waiting for when the bell would finally ring... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit of you having to endure the pain of hearing someone ranting to you. "
        " You immediately walked out of the library so that you could get to your classroom for the next class. "
        pause 2.0
        jump octphysicsclass2
    else:
        x " Come on, you suuuure you don't want this potion? "
        x " I know you want your brother to be safe, so I made this! "
        x " Keeps anyone from ever touching him. "
        x " ... "
        x " Look Temero, yes I do want my brother to be safe, but I don't trust you. "
        $ temeroknow = True
        " So Temero's that girls name. "
        hide temeroneutral at bottom
        show temerohappy at left
        tm " Aww, come on, Yinhuiii! What's there NOT to trust about me? "
        $ yinhuiknow = True
        " And Yinhui's that guys name. The guy on the right. "
        " OKay... "
        tm " I'm 100 percent trustable, you see? "
        tm " Remember that one time I grew Mia's plants? "
        tm " She looked really happy that they instantly grew!! "
        yi " ...You mean that one time the other day where you 'accidentally blew up' her plants? "
        yi " Yeah, no. "
        yi " And besides, why would I rely on a potion to keep my brother safe? "
        yi " I know better than to trust someone like you. "
        yi " You could do very horrible things to my brother without me even knowing. "
        yi " Therefore, I'm not taking your potion. "
        tm " Aww, come on! "
        tm " It's not gonna be that bad!! "
        " She notices that you were there, and you immediately got pulled close to her. "
        tm " See, [name] trust me!! right, [name]? "
        " You shrugged. You don't really know if she's really trustable or not. "
        " She does have that suspicious energy within her.. "
        yi " ...Yeah, no, I'm out. "
        tm " Come on, Yinn!! "
        scene black with dissolve
        " You spent the rest of the break watching Temero convince Yinhui to take her potion.. "
        " Though, it didn't work and Yinhui left. "
        " And now you had to deal with Temero ranting to you about it. "
        " Honestly, you were kind of just zoning out as she ranted to you... "
        " Playing some card games in your head as she yapped. "
        " You were just waiting for when the bell would finally ring... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit of you having to endure the pain of hearing someone ranting to you. "
        " You immediately walked out of the library so that you could get to your classroom for the next class. "
        pause 2.0
        jump octphysicsclass2
label octphysicsclass2:
    scene classroom with dissolve
    " You walked into the classroom and sat down on your seat. "
    " You waited for the teacher to walk into the classroom...hopefully she remembers that she has class today. "
    " As you waited for her to come in, you took a look at the area around you. "
    " Hopefully catching something interesting as you did... "
    " ...Oh hey, there's some cool drawing that someone did on the ground. "
    " You should probably go find who made this cool art, but you're too lazy to do so. "
    " Eventually, after a few minutes, the teacher walks in. "
    " Quick, act like you're doing nothing stupid! "
    show luaneutral at center with easeinright
    msl " Okay, class... "
    msl " Please get your notebooks out, we're going to be copying a few things for today. "
    msl " And...a reminder before I forget about this... "
    msl " ...We're going to be having an activity this thursday... "
    msl " So, please get prepared for that. "
    msl " Anyway, onto what we're going to copy for today... "
    scene black with dissolve
    " You spent the rest of the class taking down some notes. "
    " You're wondering what that activity could be for thursday... "
    " You might want to ask someone about that once you get home. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit of copying. "
    " You waited for everyone else to get out of the classroom before you could. "
    " Just one more class, and then you're going to be done for the day... "
    " So close to just resting on that nice bed of yours. "
    pause 2.0
    jump octbreak5

label octbreak5:
    scene hallway with dissolve
    " You walked into the hallways, wanting to spend time somewhere for your last break. "
    " Where do you want to go? "
    menu:
        " {image=carmenicon} The front of the school {image=yinyangicon} ":
            jump octfrontschool5
        " The back of the school ":
            jump octbackschool5
        " {image=sparkicon} The gym {image=jexicon} ":
            jump octgym5
        " {image=koaicon} The cafeteria {image=matteicon} ":
            jump octcafe5
        " {image=miaicon} The rooftop {image=jacobicon} ":
            jump octrooftop5
        " {image=jamicon} The library {image=orchidicon} ":
            jump octlibrary5

label octfrontschool5:
    # carmen and yinhui
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked onto the front of the school, it's starting to get a bit darker considering the fact it's almost timeto go home. "
    " Wait, you guys should be going home at 5:45 pm. "
    " You then spotted two of your classmates hanging out. You wanted to talk to one of them... "
    " But who do you talk to? "
    if carmenknow == True and yinhuiknow == True:
        menu:
            " {image=carmenicon} Carmen {image=carmenicon} ":
                jump themain
            " {image=yinyangicon} Yinhui {image=yinyangicon} ":
                jump character
    elif carmenknow == True and yinhuiknow == False:
        menu:
            " {image=carmenicon} Carmen {image=carmenicon} ":
                jump themain
            " {image=yinyangicon} A guy who looks mean {image=yinyangicon} ":
                jump character
    elif carmenknow == False and yinhuiknow == True:
        menu:
            " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                jump themain
            " {image=yinyangicon} Yinhui {image=yinyangicon} ":
                jump character
    else:
        menu:
            " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                jump themain
            " {image=yinyangicon} A guy who looks mean {image=yinyangicon} ":
                jump character
    label themain:
        " You walked up to him to see what he was doing. "
        show carmenneutral at center with easeinright
        if carmenknow == True:
            ca " ...!! "
            " He waves a little 'hello' to you. "
            " You said him a little 'hi' before you asked him what he was doing. "
            " As you were asking, you sat down next to him. "
            ca " ... "
            " You saw that he pulled out his phone and pointed at a song he was playing right now... "
            " ...And then pointed at his guitar. "
            " Looks like he wants to do a nice little guitar cover of this song. "
            " You honestly wanted to listen to how it would sound. "
            hide carmenneutral at bottom
            show carmensurprised at center
            ca " ...? "
            " Carmen looks like he was asking if you were really sure. "
            " You nodded and gave him a thumbs up, showing that you really were sure. "
            hide carmensurprised at bottom
            show carmenhappy at center
            ca " ...!! "
            " Carmen takes a deep breath... "
            " ..And he starts playing his guitar for you. "
            scene black with dissolve
            " You spent the rest of the break listening to Carmen play his guitar. "
            " It was honestly really nice, listening to him play his guitar... "
            " ...And looking up at the sky. "
            " It felt like a nice relaxing summer break even though you just started school. "
            " Still though, it felt that way. And it was comforting. "
            " Felt like you could just chill for a bit... "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your last class. "
            " You get up from where you were sitting, and you walked back to your classroom for the next class. "
            pause 2.0
            jump octcookingclass2
        else:
            x " ...!! "
            " He waves a little 'hello' to you. "
            $ carmenknow = True
            " You've heard that this kid's name was Carmen, and that he was mute. "
            " You know about this because you've heard a few people talk about him before. "
            " You said him a little 'hi' before you asked him what he was doing. "
            " As you were asking, you sat down next to him. "
            ca " ... "
            " You saw that he pulled out his phone and pointed at a song he was playing right now... "
            " ...And then pointed at his guitar. "
            " Looks like he wants to do a nice little guitar cover of this song. "
            " You honestly wanted to listen to how it would sound. "
            hide carmenneutral at bottom
            show carmensurprised at center
            ca " ...? "
            " Carmen looks like he was asking if you were really sure. "
            " You nodded and gave him a thumbs up, showing that you really were sure. "
            hide carmensurprised at bottom
            show carmenhappy at center
            ca " ...!! "
            " Carmen takes a deep breath... "
            " ..And he starts playing his guitar for you. "
            scene black with dissolve
            " You spent the rest of the break listening to Carmen play his guitar. "
            " It was honestly really nice, listening to him play his guitar... "
            " ...And looking up at the sky. "
            " It felt like a nice relaxing summer break even though you just started school. "
            " Still though, it felt that way. And it was comforting. "
            " Felt like you could just chill for a bit... "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your last class. "
            " You get up from where you were sitting, and you walked back to your classroom for the next class. "
            pause 2.0
            jump octcookingclass2
    label character:
        " You walked up to him to see what he was doing. "
        show yinhuineutral at center with easeinleft
        if yinhuiknow == True:
            " He seemed to be admiring the sky... "
            " Looks and sounds pretty insane, since he looked like a person who wouldn't do these types of things. "
            " But, eh...things just surprise you here and there. "
            " You poked his shoulder to get his attention and you asked him what he was doing. "
            yi " Huh? Oh. You. "
            yi " Just admiring the sky and stuff... "
            yi " Yang told me that this would help me clam down or something. "
            yi " And uh, honestly, it does. "
            yi " I think I should do this more often whenever I get mad. "
            yi " ... "
            yi " ...You know, Yang would've loved these types of things. "
            yi " Most of his gallery is actually pretty good pictures of the sky... "
            yi " Nature, some pictures of cats, and of course me and him. "
            yi " He really likes to take pictures or whatever's around him. "
            hide yinhuineutral at bottom
            show yinhuiheh at center
            yi " Meanwhile my gallery is just memes and shit. "
            yi " You'd think that Yinhui would have some in his gallery, and uh... "
            yi " You're kind of right about that, except they're all just wholesome. "
            yi " But mine? "
            hide yinhuiheh at bottom
            show yinhuineutral at center
            yi " ...You wouldn't really want to know what I have saved on my phone. "
            yi " Seriously, mom would've killed me if she figured out what I had saved on my phone. "
            yi " Thankfully she doesn't check my phone for anything. "
            scene black with dissolve
            " You spent the rest of the break talking with Yinhui. "
            " Just talking about random things here and there... "
            " And just mainly chilling for the last break of the day. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your last class. "
            " You get up from where you were sitting, and you walked back to your classroom for the next class. "
            pause 2.0
            jump octcookingclass2
        else:
            " He seemed to be admiring the sky... "
            " Looks and sounds pretty insane, since he looked like a person who wouldn't do these types of things. "
            " But, eh...things just surprise you here and there. "
            " You poked his shoulder to get his attention and you asked him what he was doing. "
            x " Huh? Oh. You. "
            $ yinhuiknow = True
            yi " I'm Yinhui. Don't think I got to introduce myself to you yet. And uh...I'm just... "
            yi " Just admiring the sky and stuff... "
            yi " Yang told me that this would help me clam down or something. "
            yi " And uh, honestly, it does. "
            yi " I think I should do this more often whenever I get mad. "
            yi " ... "
            yi " ...You know, Yang would've loved these types of things. "
            yi " Most of his gallery is actually pretty good pictures of the sky... "
            yi " Nature, some pictures of cats, and of course me and him. "
            yi " He really likes to take pictures or whatever's around him. "
            hide yinhuineutral at bottom
            show yinhuiheh at center
            yi " Meanwhile my gallery is just memes and shit. "
            yi " You'd think that Yinhui would have some in his gallery, and uh... "
            yi " You're kind of right about that, except they're all just wholesome. "
            yi " But mine? "
            hide yinhuiheh at bottom
            show yinhuineutral at center
            yi " ...You wouldn't really want to know what I have saved on my phone. "
            yi " Seriously, mom would've killed me if she figured out what I had saved on my phone. "
            yi " Thankfully she doesn't check my phone for anything. "
            scene black with dissolve
            " You spent the rest of the break talking with Yinhui. "
            " Just talking about random things here and there... "
            " And just mainly chilling for the last break of the day. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your last class. "
            " You walked back to your classroom for the next class. "
            pause 2.0
            jump octcookingclass2

label octbackschool5:
    # disk, nox, and yangyi, admiring the flowers mia planted
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and spotted three of your classmates hanging out with eachother. "
    " You wondered what they were doing... "
    " You decided to check on what they were doing. "
    show diskneutral at right with easeinleft
    show noxneutral at center with easeinleft
    show yangyineutral at left with easeinleft
    if diskknow,noxknow,yangyiknow == True:
        " Looks like they're looking around the flowers that one of your classmates planted down. "
        " All of them looked really nice! "
        " Though you didn't know what type of flowers these were, they were still interesting. "
        " You decided to take a look of the flowers too. "
        d " Oh, heya [name]! Didn't expect you to be here!! "
        n " ...Huh?...[name]'s here...? that's nice... "
        ya " Hi, [name]!! It's nice to have you here! "
        " You told them it was nice to see all of them. "
        " You then asked them about the flowers. "
        d " Oh, the flowers? we were just checking them out! "
        ya " Actually, we just found out that someone had planted these here... "
        n " Hhhh...I'm only here because Disk is trying to keep me awake until later night... "
        d " Mhm!! "
        d " Wait, you know what would be a fun idea? "
        n " Eeeh...? "
        hide diskneutral at bottom
        show diskhappy at right
        d " What if we all assign eachother some flowers that are here! "
        hide yangyineutral at bottom
        show yangyihappy at left
        ya " Oooh, sounds fun! "
        hide noxneutral at bottom
        show noxhappy at center
        n " Wooo...fun... "
        d " You should join us, [name]! "
        " Without you having to respond, Disk immediately starts looking around at the flowers... "
        " ...This was quite the energetic bunch. Excluding Nox, of course. "
        scene black with dissolve
        " You spent the rest of the break hanging out with Disk, Nox, and Yangyi. "
        " Everyone seemed to be having fun, especially Nox who was usually so sleepy. "
        " You're surprised that he's actually managing to stay awake. "
        " You eventually got assigned a nice and pretty white flower... "
        " Disk got a very cool looking flower, and Yangyi and Nox got a pretty looking flower. "
        " Nice. Your flower was nothing special, but you still considered that it was pretty. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your last class. "
        " You walked back to your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
    elif diskknow,noxknow == True and yangyiknow == False:
        " Looks like they're looking around the flowers that one of your classmates planted down. "
        " All of them looked really nice! "
        " Though you didn't know what type of flowers these were, they were still interesting. "
        " You decided to take a look of the flowers too. "
        d " Oh, heya [name]! Didn't expect you to be here!! "
        n " ...Huh?...[name]'s here...? that's nice... "
        x " Hi, [name]!! It's nice to have you here! "
        x " Actually, I don't think I've introduced myself to you before... "
        $ yangyiknow = True
        ya " I'm Yangyi! It's nice to meet you! "
        ya " I'm the brother of Yinhui, and I'm the son of Miss Jiayu! "
        " You told them it was nice to see all of them. "
        " You then asked them about the flowers. "
        d " Oh, the flowers? we were just checking them out! "
        ya " Actually, we just found out that someone had planted these here... "
        n " Hhhh...I'm only here because Disk is trying to keep me awake until later night... "
        d " Mhm!! "
        d " Wait, you know what would be a fun idea? "
        n " Eeeh...? "
        hide diskneutral at bottom
        show diskhappy at right
        d " What if we all assign eachother some flowers that are here! "
        hide yangyineutral at bottom
        show yangyihappy at left
        ya " Oooh, sounds fun! "
        hide noxneutral at bottom
        show noxhappy at center
        n " Wooo...fun... "
        d " You should join us, [name]! "
        " Without you having to respond, Disk immediately starts looking around at the flowers... "
        " ...This was quite the energetic bunch. Excluding Nox, of course. "
        scene black with dissolve
        " You spent the rest of the break hanging out with Disk, Nox, and Yangyi. "
        " Everyone seemed to be having fun, especially Nox who was usually so sleepy. "
        " You're surprised that he's actually managing to stay awake. "
        " You eventually got assigned a nice and pretty white flower... "
        " Disk got a very cool looking flower, and Yangyi and Nox got a pretty looking flower. "
        " Nice. Your flower was nothing special, but you still considered that it was pretty. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your last class. "
        " You walked back to your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
    elif diskknow,yangyiknow == True and noxknow == False:
        " Looks like they're looking around the flowers that one of your classmates planted down. "
        " All of them looked really nice! "
        " Though you didn't know what type of flowers these were, they were still interesting. "
        " You decided to take a look of the flowers too. "
        d " Oh, heya [name]! Didn't expect you to be here!! "
        x " ...Huh?...[name]'s here...? that's nice... "
        ya " Hi, [name]!! It's nice to have you here! "
        d " Wait, I don't think [name] has met Nox yet! "
        $ noxknow = True
        d " [name], the sleepy guy in the center is Nox! "
        d " He's really cool! "
        n " ...Hi... "
        " You told them it was nice to see all of them. "
        " You then asked them about the flowers. "
        d " Oh, the flowers? we were just checking them out! "
        ya " Actually, we just found out that someone had planted these here... "
        n " Hhhh...I'm only here because Disk is trying to keep me awake until later night... "
        d " Mhm!! "
        d " Wait, you know what would be a fun idea? "
        n " Eeeh...? "
        hide diskneutral at bottom
        show diskhappy at right
        d " What if we all assign eachother some flowers that are here! "
        hide yangyineutral at bottom
        show yangyihappy at left
        ya " Oooh, sounds fun! "
        hide noxneutral at bottom
        show noxhappy at center
        n " Wooo...fun... "
        d " You should join us, [name]! "
        " Without you having to respond, Disk immediately starts looking around at the flowers... "
        " ...This was quite the energetic bunch. Excluding Nox, of course. "
        scene black with dissolve
        " You spent the rest of the break hanging out with Disk, Nox, and Yangyi. "
        " Everyone seemed to be having fun, especially Nox who was usually so sleepy. "
        " You're surprised that he's actually managing to stay awake. "
        " You eventually got assigned a nice and pretty white flower... "
        " Disk got a very cool looking flower, and Yangyi and Nox got a pretty looking flower. "
        " Nice. Your flower was nothing special, but you still considered that it was pretty. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your last class. "
        " You walked back to your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
    elif noxknow,yangyiknow == True and diskknow == False:
        " Looks like they're looking around the flowers that one of your classmates planted down. "
        " All of them looked really nice! "
        " Though you didn't know what type of flowers these were, they were still interesting. "
        " You decided to take a look of the flowers too. "
        x " Oh, heya [name]! Didn't expect you to be here!! "
        n " ...Huh?...[name]'s here...? that's nice... "
        ya " Hi, [name]!! It's nice to have you here! "
        x " Wait, I don't think I've met [name] before! "
        $ diskknow = True
        d " I'm Disk - we're classmates! "
        d " It's nice to say you! "
        " You told them it was nice to see all of them. "
        " You then asked them about the flowers. "
        d " Oh, the flowers? we were just checking them out! "
        ya " Actually, we just found out that someone had planted these here... "
        n " Hhhh...I'm only here because Disk is trying to keep me awake until later night... "
        d " Mhm!! "
        d " Wait, you know what would be a fun idea? "
        n " Eeeh...? "
        hide diskneutral at bottom
        show diskhappy at right
        d " What if we all assign eachother some flowers that are here! "
        hide yangyineutral at bottom
        show yangyihappy at left
        ya " Oooh, sounds fun! "
        hide noxneutral at bottom
        show noxhappy at center
        n " Wooo...fun... "
        d " You should join us, [name]! "
        " Without you having to respond, Disk immediately starts looking around at the flowers... "
        " ...This was quite the energetic bunch. Excluding Nox, of course. "
        scene black with dissolve
        " You spent the rest of the break hanging out with Disk, Nox, and Yangyi. "
        " Everyone seemed to be having fun, especially Nox who was usually so sleepy. "
        " You're surprised that he's actually managing to stay awake. "
        " You eventually got assigned a nice and pretty white flower... "
        " Disk got a very cool looking flower, and Yangyi and Nox got a pretty looking flower. "
        " Nice. Your flower was nothing special, but you still considered that it was pretty. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your last class. "
        " You walked back to your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
    elif diskknow == True and noxknow,yangyiknow == False:
        " Looks like they're looking around the flowers that one of your classmates planted down. "
        " All of them looked really nice! "
        " Though you didn't know what type of flowers these were, they were still interesting. "
        " You decided to take a look of the flowers too. "
        d " Oh, heya [name]! Didn't expect you to be here!! "
        x " ...Huh?...[name]'s here...? that's nice... "
        x " Hi, [name]!! It's nice to have you here! "
        x " ...mmmm...wait, I don't think I got to introduce myself yet to [name]... "
        x " Wait, me neither!! "
        d " Go introduce yourself, guys!! "
        $ noxknow = True
        $ yangyiknow = True
        n " Hi...I'm Nox...the sleepy guy in the center... "
        ya " And I'm Yangyi! It's nice to meet you!! "
        " You told them it was nice to see all of them. "
        " You then asked them about the flowers. "
        d " Oh, the flowers? we were just checking them out! "
        ya " Actually, we just found out that someone had planted these here... "
        n " Hhhh...I'm only here because Disk is trying to keep me awake until later night... "
        d " Mhm!! "
        d " Wait, you know what would be a fun idea? "
        n " Eeeh...? "
        hide diskneutral at bottom
        show diskhappy at right
        d " What if we all assign eachother some flowers that are here! "
        hide yangyineutral at bottom
        show yangyihappy at left
        ya " Oooh, sounds fun! "
        hide noxneutral at bottom
        show noxhappy at center
        n " Wooo...fun... "
        d " You should join us, [name]! "
        " Without you having to respond, Disk immediately starts looking around at the flowers... "
        " ...This was quite the energetic bunch. Excluding Nox, of course. "
        scene black with dissolve
        " You spent the rest of the break hanging out with Disk, Nox, and Yangyi. "
        " Everyone seemed to be having fun, especially Nox who was usually so sleepy. "
        " You're surprised that he's actually managing to stay awake. "
        " You eventually got assigned a nice and pretty white flower... "
        " Disk got a very cool looking flower, and Yangyi and Nox got a pretty looking flower. "
        " Nice. Your flower was nothing special, but you still considered that it was pretty. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your last class. "
        " You walked back to your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
    elif noxknow == True and diskknow,yangyiknow == False:
        " Looks like they're looking around the flowers that one of your classmates planted down. "
        " All of them looked really nice! "
        " Though you didn't know what type of flowers these were, they were still interesting. "
        " You decided to take a look of the flowers too. "
        x " Oh, heya [name]! Didn't expect you to be here!! "
        n " ...Huh?...[name]'s here...? that's nice... "
        x " Hi, [name]!! It's nice to have you here! "
        n " Hmmm...wait...did you guys get to introduce yourselves to [name]...? "
        x " Wait, no! I haven't yet! "
        x " Same here!! "
        n " Introduce yourselves then...*yawn*... "
        $ diskknow = True
        $ yangyiknow = True
        d " I'm Disk! I'm Quinn's older brother! "
        ya " And I'm Yangyi - the one on the left! It's nice to meet you! "
        " You told them it was nice to see all of them. "
        " You then asked them about the flowers. "
        d " Oh, the flowers? we were just checking them out! "
        ya " Actually, we just found out that someone had planted these here... "
        n " Hhhh...I'm only here because Disk is trying to keep me awake until later night... "
        d " Mhm!! "
        d " Wait, you know what would be a fun idea? "
        n " Eeeh...? "
        hide diskneutral at bottom
        show diskhappy at right
        d " What if we all assign eachother some flowers that are here! "
        hide yangyineutral at bottom
        show yangyihappy at left
        ya " Oooh, sounds fun! "
        hide noxneutral at bottom
        show noxhappy at center
        n " Wooo...fun... "
        d " You should join us, [name]! "
        " Without you having to respond, Disk immediately starts looking around at the flowers... "
        " ...This was quite the energetic bunch. Excluding Nox, of course. "
        scene black with dissolve
        " You spent the rest of the break hanging out with Disk, Nox, and Yangyi. "
        " Everyone seemed to be having fun, especially Nox who was usually so sleepy. "
        " You're surprised that he's actually managing to stay awake. "
        " You eventually got assigned a nice and pretty white flower... "
        " Disk got a very cool looking flower, and Yangyi and Nox got a pretty looking flower. "
        " Nice. Your flower was nothing special, but you still considered that it was pretty. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your last class. "
        " You walked back to your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
    elif yangyiknow == True and diskknow,noxknow == False:
        " Looks like they're looking around the flowers that one of your classmates planted down. "
        " All of them looked really nice! "
        " Though you didn't know what type of flowers these were, they were still interesting. "
        " You decided to take a look of the flowers too. "
        x " Oh, heya [name]! Didn't expect you to be here!! "
        x " ...Huh?...[name]'s here...? that's nice... "
        ya " Hi, [name]!! It's nice to have you here! "
        ya " Wait, I don't think you guys got to introduce yourselves to [name] yet! "
        x " Oh, right!! Almost forgot!! "
        x " mmm...okay... "
        $ noxknow = True
        $ diskknow = True
        n " I'm Nox...the sleepy one in the center... "
        d " And I'm Disk - the onein the right! It's nice to meet you!! "
        " You told them it was nice to see all of them. "
        " You then asked them about the flowers. "
        d " Oh, the flowers? we were just checking them out! "
        ya " Actually, we just found out that someone had planted these here... "
        n " Hhhh...I'm only here because Disk is trying to keep me awake until later night... "
        d " Mhm!! "
        d " Wait, you know what would be a fun idea? "
        n " Eeeh...? "
        hide diskneutral at bottom
        show diskhappy at right
        d " What if we all assign eachother some flowers that are here! "
        hide yangyineutral at bottom
        show yangyihappy at left
        ya " Oooh, sounds fun! "
        hide noxneutral at bottom
        show noxhappy at center
        n " Wooo...fun... "
        d " You should join us, [name]! "
        " Without you having to respond, Disk immediately starts looking around at the flowers... "
        " ...This was quite the energetic bunch. Excluding Nox, of course. "
        scene black with dissolve
        " You spent the rest of the break hanging out with Disk, Nox, and Yangyi. "
        " Everyone seemed to be having fun, especially Nox who was usually so sleepy. "
        " You're surprised that he's actually managing to stay awake. "
        " You eventually got assigned a nice and pretty white flower... "
        " Disk got a very cool looking flower, and Yangyi and Nox got a pretty looking flower. "
        " Nice. Your flower was nothing special, but you still considered that it was pretty. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your last class. "
        " You walked back to your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
    else:
        " Looks like they're looking around the flowers that one of your classmates planted down. "
        " All of them looked really nice! "
        " Though you didn't know what type of flowers these were, they were still interesting. "
        " You decided to take a look of the flowers too. "
        x " Oh, heya [name]! Didn't expect you to be here!! "
        x " ...Huh?...[name]'s here...? that's nice... "
        x " Hi, [name]!! It's nice to have you here! "
        x " Wait, I don't think we've all introduced ourselves to [name] yet!! "
        x " oh...really...? "
        x " Yeah, we should do that!! "
        $ yangyiknow = True
        $ noxknow = True
        $ disknow = True
        ya " I'm Yangyi, Yinhui's brother and Miss Jiayu's son! - I'm the one on the left! "
        n " I'm Nox...the sleepy one on the center... "
        d " And I'm Disk! Quinn's older brother and the one on the right! "
        d " It's nice to meet you! "
        " You told them it was nice to see all of them. "
        " You then asked them about the flowers. "
        d " Oh, the flowers? we were just checking them out! "
        ya " Actually, we just found out that someone had planted these here... "
        n " Hhhh...I'm only here because Disk is trying to keep me awake until later night... "
        d " Mhm!! "
        d " Wait, you know what would be a fun idea? "
        n " Eeeh...? "
        hide diskneutral at bottom
        show diskhappy at right
        d " What if we all assign eachother some flowers that are here! "
        hide yangyineutral at bottom
        show yangyihappy at left
        ya " Oooh, sounds fun! "
        hide noxneutral at bottom
        show noxhappy at center
        n " Wooo...fun... "
        d " You should join us, [name]! "
        " Without you having to respond, Disk immediately starts looking around at the flowers... "
        " ...This was quite the energetic bunch. Excluding Nox, of course. "
        scene black with dissolve
        " You spent the rest of the break hanging out with Disk, Nox, and Yangyi. "
        " Everyone seemed to be having fun, especially Nox who was usually so sleepy. "
        " You're surprised that he's actually managing to stay awake. "
        " You eventually got assigned a nice and pretty white flower... "
        " Disk got a very cool looking flower, and Yangyi and Nox got a pretty looking flower. "
        " Nice. Your flower was nothing special, but you still considered that it was pretty. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your last class. "
        " You walked back to your classroom for the next class. "
        pause 2.0
        jump octcookingclass2

label octgym5:
    # jex comforting spark about his crush
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym and found two of your classmates hanging out. "
    " Curious on what they were talking about, you decided to walk up to them and talk to them for a bit. "
    show sparkneutral at left with easeinright
    show jexneutral at right with easeinright
    if sparkknow == True and jexknow == True:
        sp " Hi, [name]. "
        j " Hello, [name]. "
        j " Spark was just talking to me about his - {nw} "
        hide sparkneutral at bottom
        show sparkangry at left
        sp " You are NOT saying anything. "
        j " ... "
        hide sparkangry at bottom
        show sparkneutral at left
        sp " There, much better. "
        sp " We weren't talking about anything important, [name]. "
        sp " Just talking about random things here and there... "
        sp " Jex wasn't gonna say anything important or anything. "
        sp " Just talking about random things. "
        j " But Spark, it's pride month. "
        sp " What about pride month, Jex? "
        j " It's okay to show your feelings towards that one guy that you like. "
        j " That one from another school... "
        j " Be who you are, I guess. "
        sp " ... "
        hide sparkneutral at bottom
        show sparkshit at left
        sp " Jex, I'm so doomed. "
        j " I know Spark, I know. "
        scene black with dissolve
        " You spent the rest of the break talking with Jex and Spark. "
        " For context on the pride month part, I wrote this in pride month. "
        " This isn't gonna make sense in the future, but eh... "
        " Atleast you guys now know what month I wrote this in so that you guys wont get confused. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your last class. "
        " You walked back to your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
    elif sparkknow == True and jexknow == False:
        sp " Hi, [name]. "
        x " Hello, [name]. "
        x " Spark was just talking to me about his - {nw} "
        hide sparkneutral at bottom
        show sparkangry at left
        sp " You are NOT saying anything. "
        x " ... "
        hide sparkangry at bottom
        show sparkneutral at left
        sp " There, much better. "
        sp " We weren't talking about anything important, [name]. "
        sp " Just talking about random things here and there... "
        $ jexknow = True
        sp " Jex wasn't gonna say anything important or anything. "
        sp " Just talking about random things. "
        j " But Spark, it's pride month. "
        sp " What about pride month, Jex? "
        j " It's okay to show your feelings towards that one guy that you like. "
        j " That one from another school... "
        j " Be who you are, I guess. "
        sp " ... "
        hide sparkneutral at bottom
        show sparkshit at left
        sp " Jex, I'm so doomed. "
        j " I know Spark, I know. "
        scene black with dissolve
        " You spent the rest of the break talking with Jex and Spark. "
        " For context on the pride month part, I wrote this in pride month. "
        " This isn't gonna make sense in the future, but eh... "
        " Atleast you guys now know what month I wrote this in so that you guys wont get confused. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your last class. "
        " You walked back to your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
    elif sparkknow == False and jexknow == True:
        x " Hi, [name]. "
        j " Hello, [name]. "
        $ sparkknow = True
        j " Spark was just talking to me about his - {nw} "
        hide sparkneutral at bottom
        show sparkangry at left
        sp " You are NOT saying anything. "
        j " ... "
        hide sparkangry at bottom
        show sparkneutral at left
        sp " There, much better. "
        sp " We weren't talking about anything important, [name]. "
        sp " Just talking about random things here and there... "
        sp " Jex wasn't gonna say anything important or anything. "
        sp " Just talking about random things. "
        j " But Spark, it's pride month. "
        sp " What about pride month, Jex? "
        j " It's okay to show your feelings towards that one guy that you like. "
        j " That one from another school... "
        j " Be who you are, I guess. "
        sp " ... "
        hide sparkneutral at bottom
        show sparkshit at left
        sp " Jex, I'm so doomed. "
        j " I know Spark, I know. "
        scene black with dissolve
        " You spent the rest of the break talking with Jex and Spark. "
        " For context on the pride month part, I wrote this in pride month. "
        " This isn't gonna make sense in the future, but eh... "
        " Atleast you guys now know what month I wrote this in so that you guys wont get confused. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your last class. "
        " You walked back to your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
    else:
        x " Hi, [name]. "
        x " Hello, [name]. "
        $ sparkknow = True
        x " Spark was just talking to me about his - {nw} "
        hide sparkneutral at bottom
        show sparkangry at left
        sp " You are NOT saying anything. "
        x " ... "
        hide sparkangry at bottom
        show sparkneutral at left
        sp " There, much better. "
        sp " We weren't talking about anything important, [name]. "
        sp " Just talking about random things here and there... "
        $ jexknow = True
        sp " Jex wasn't gonna say anything important or anything. "
        sp " Just talking about random things. "
        j " But Spark, it's pride month. "
        sp " What about pride month, Jex? "
        j " It's okay to show your feelings towards that one guy that you like. "
        j " That one from another school... "
        j " Be who you are, I guess. "
        sp " ... "
        hide sparkneutral at bottom
        show sparkshit at left
        sp " Jex, I'm so doomed. "
        j " I know Spark, I know. "
        scene black with dissolve
        " You spent the rest of the break talking with Jex and Spark. "
        " For context on the pride month part, I wrote this in pride month. "
        " This isn't gonna make sense in the future, but eh... "
        " Atleast you guys now know what month I wrote this in so that you guys wont get confused. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your last class. "
        " You walked back to your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
label octcafe5:
    # matte asking koa if she could paint him
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted two of your classmates talking to eachother. "
    " You wanted to talk to them...you walked up to them and sat next to them. "
    show koaneutral at right with easeinleft
    show matteneutral at left with easeinleft
    if koaknow == True and matteknow == True:
        ma " Hi, [name]!! "
        k " ...Hello, [name]. "
        ma " I was just asking Koa here if I could draw him! "
        ma " I mean, I've drawn everyone here in this school except you! "
        k " Eeeeh, I don't know... "
        ma " Come on, Koa! A little drawing won't hurt! "
        ma " Plus, your siblings might love it too! "
        k " ... "
        k " Fine...you can draw me. "
        hide matteneutral at bottom
        show mattehappy at left
        ma " Wooohoo!! "
        ma " Alright, let me just get my drawing materials... "
        ma " Actually, [name]! do you wanna draw Koa too? "
        k " Why would [they] wanna draw me... "
        ma " Because you're cool, duh. "
        k " I don't really think I'm THAT cool. "
        ma " Oh, shut up... "
        " You nodded. You kinda had nothing to do, so you could use this time to improve your drawing skills. "
        " You asked Matte for some art materials. "
        ma " Ooo, alright! "
        ma " You're lucky that I've still got some extra. "
        scene black with dissolve
        " You spent the rest of the break drawing Koa with Matte. "
        " You eventually finished drawing, and compared to Matte's... "
        " Hers definitely looked much more realistic than yours. "
        " She's really just too good at art. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your final class. "
        " You get up from where you were sitting and you walked back into your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
    elif koaknow == True and matteknow == False:
        x " Hi, [name]!! "
        k " ...Hello, [name]. "
        x " Oh, wait! I haven't introduced myself to you yet! "
        x " Sorry [name], eheh... "
        $ matteknow = True
        ma " I'm Matte! I like to do painting, and other stuff! I'm also Disk's cousin! "
        ma " I was also just asking Koa here if I could draw him! "
        ma " I mean, I've drawn everyone here in this school except you! "
        k " Eeeeh, I don't know... "
        ma " Come on, Koa! A little drawing won't hurt! "
        ma " Plus, your siblings might love it too! "
        k " ... "
        k " Fine...you can draw me. "
        hide matteneutral at bottom
        show mattehappy at left
        ma " Wooohoo!! "
        ma " Alright, let me just get my drawing materials... "
        ma " Actually, [name]! do you wanna draw Koa too? "
        k " Why would [they] wanna draw me... "
        ma " Because you're cool, duh. "
        k " I don't really think I'm THAT cool. "
        ma " Oh, shut up... "
        " You nodded. You kinda had nothing to do, so you could use this time to improve your drawing skills. "
        " You asked Matte for some art materials. "
        ma " Ooo, alright! "
        ma " You're lucky that I've still got some extra. "
        scene black with dissolve
        " You spent the rest of the break drawing Koa with Matte. "
        " You eventually finished drawing, and compared to Matte's... "
        " Hers definitely looked much more realistic than yours. "
        " She's really just too good at art. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your final class. "
        " You get up from where you were sitting and you walked back into your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
    elif koaknow == False and matteknow == True:
        ma " Hi, [name]!! "
        x " ...Hello, [name]. "
        ma " I was just asking Koa here if I could draw him! "
        $ koaknow = True
        " So that guy's name is Koa... "
        ma " I mean, I've drawn everyone here in this school except you! "
        k " Eeeeh, I don't know... "
        ma " Come on, Koa! A little drawing won't hurt! "
        ma " Plus, your siblings might love it too! "
        k " ... "
        k " Fine...you can draw me. "
        hide matteneutral at bottom
        show mattehappy at left
        ma " Wooohoo!! "
        ma " Alright, let me just get my drawing materials... "
        ma " Actually, [name]! do you wanna draw Koa too? "
        k " Why would [they] wanna draw me... "
        ma " Because you're cool, duh. "
        k " I don't really think I'm THAT cool. "
        ma " Oh, shut up... "
        " You nodded. You kinda had nothing to do, so you could use this time to improve your drawing skills. "
        " You asked Matte for some art materials. "
        ma " Ooo, alright! "
        ma " You're lucky that I've still got some extra. "
        scene black with dissolve
        " You spent the rest of the break drawing Koa with Matte. "
        " You eventually finished drawing, and compared to Matte's... "
        " Hers definitely looked much more realistic than yours. "
        " She's really just too good at art. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your final class. "
        " You get up from where you were sitting and you walked back into your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
    else:
        x " Hi, [name]!! "
        x " ...Hello, [name]. "
        x " Oh, wait! I haven't introduced myself to you yet! "
        x " Sorry [name], eheh... "
        $ matteknow = True
        ma " I'm Matte! I like to do painting, and other stuff! I'm also Disk's cousin! "
        ma " I was also just asking Koa here if I could draw him! "
        $ koaknow = True
        " So Koa's that guys name... "
        ma " I mean, I've drawn everyone here in this school except you! "
        k " Eeeeh, I don't know... "
        ma " Come on, Koa! A little drawing won't hurt! "
        ma " Plus, your siblings might love it too! "
        k " ... "
        k " Fine...you can draw me. "
        hide matteneutral at bottom
        show mattehappy at left
        ma " Wooohoo!! "
        ma " Alright, let me just get my drawing materials... "
        ma " Actually, [name]! do you wanna draw Koa too? "
        k " Why would [they] wanna draw me... "
        ma " Because you're cool, duh. "
        k " I don't really think I'm THAT cool. "
        ma " Oh, shut up... "
        " You nodded. You kinda had nothing to do, so you could use this time to improve your drawing skills. "
        " You asked Matte for some art materials. "
        ma " Ooo, alright! "
        ma " You're lucky that I've still got some extra. "
        scene black with dissolve
        " You spent the rest of the break drawing Koa with Matte. "
        " You eventually finished drawing, and compared to Matte's... "
        " Hers definitely looked much more realistic than yours. "
        " She's really just too good at art. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your final class. "
        " You get up from where you were sitting and you walked back into your classroom for the next class. "
        pause 2.0
        jump octcookingclass2
label octrooftop5:
    # mia and jacob, coping about the fact one of her favorite flowers fell.
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked onto the rooftop and spotted two of your classmates hanging out. "
    " You wanted to talk to them... you walked up to them and stood next to them to see what they're talking about. "
    show jacobneutral at left with easeinright
    show miasad at right with easeinright
    if jacobknow == True and miaknow == True:
        " You walked up to them and noticed that the girl looked pretty sad. "
        " You then remember a pot that was broken on the front of the school... "
        " That was probably hers. Ruh roh. "
        jac " ...Uh. Hi, [name]. "
        jac " So...her favorite flower-{nw} "
        m " I ACCIDENTALLY DROPPED MY FAVORITE FLOWER!! " with vpunch
        m " WAAAHHHH!! WHAT AM I SUPPOSED TO DO NOW!!! " with vpunch
        jac " ...Yeah, she's been like this for awhile now. "
        jac " I've been trying to calm her down, but she just won't... "
        jac " Please help me, I don't know how people calm other people down... "
        " Help him? "
        menu:
            " Attempt to stop the girl crying ":
                $ jacoblv += 5
                " You attempted to calm Mia down... "
                if kind,calm == True:
                    " You promised to Mia that you're gonna get some seeds for that flower... "
                    " ...And you're gonna get her some nice and fancy flower pots for her! "
                    " Even though your wallet is gonna cry. "
                    " You just didn't want to see her being so upset like this. "
                    m " ... "
                    m " ...Okay... "
                    jac " Wow, uh...that worked. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob and Mia. "
                    " You were also discussing what kind of pot Mia wanted. "
                    " ...Jacob looked like he was considering that he should get something for Mia too. "
                    " But he just decided not to in the end, once you pointed him out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your final class. "
                    " You get down from the rooftop and you walked back to your classroom for the final class. "
                    pause 2.0
                    jump octcookingclass2
                elif mean == True:
                    " Somehow your scary looks calmed Mia down already. "
                    " Probably because she thought that you were gonna beat her ass for acting like a baby. "
                    " Yeah, most likely that, actually. "
                    jac " Wow, uh...that worked. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob and Mia. "
                    " You were also discussing what kind of pot Mia wanted, since you also told her that you're gonna get her a new flower pot. "
                    " ...Jacob looked like he was considering that he should get something for Mia too. "
                    " But he just decided not to in the end, once you pointed him out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your final class. "
                    " You get down from the rooftop and you walked back to your classroom for the final class. "
                    pause 2.0
                    jump octcookingclass2
                else:
                    " You promised to Mia that you're gonna get some seeds for that flower... "
                    " ...And you're gonna get her some nice and fancy flower pots for her! "
                    " Even though your wallet is gonna cry. "
                    " You just didn't want to see her being so upset like this. "
                    m " ... "
                    m " ...Okay... "
                    jac " Wow, uh...that worked. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob and Mia. "
                    " You were also discussing what kind of pot Mia wanted. "
                    " ...Jacob looked like he was considering that he should get something for Mia too. "
                    " But he just decided not to in the end, once you pointed him out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your final class. "
                    " You get down from the rooftop and you walked back to your classroom for the final class. "
                    pause 2.0
                    jump octcookingclass2
            " Nah, not my problem ":
                jac " Uh, try again...? "
                jac " Okay...I'll try... "
                jac " Uh, Mia - {nw} "
                m " WAAAAAAAAAAAAAAAAAAAAAAAAAAHHH!! " with vpunch
                jac " ...{p}Mia - {nw} "
                m " I MISS MY FLOWER SO MUCH!!!!!!!!!!!!!! " with vpunch
                jac " ...This is gonna take the entire break, I swear... "
                scene black with dissolve
                " You spent the rest of the break watching Jacob attempt to calm Mia down. "
                " ...Which he miserably failed in doing. "
                " You could only watch since you didn't really know what to do to comfort the girl either. "
                " You wish you could help, but you just chose not to. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your final class. "
                " You get down from the rooftop and you walked back to your classroom for the final class. "
                pause 2.0
                jump octcookingclass2
    elif jacobknow == True and miaknow == False:
        " You walked up to them and noticed that the girl looked pretty sad. "
        " You then remember a pot that was broken on the front of the school... "
        " That was probably hers. Ruh roh. "
        jac " ...Uh. Hi, [name]. "
        $ miaknow = True
        jac " This is my friend, Mia, and uh... "
        jac " So...her favorite flower-{nw} "
        m " I ACCIDENTALLY DROPPED MY FAVORITE FLOWER!! " with vpunch
        m " WAAAHHHH!! WHAT AM I SUPPOSED TO DO NOW!!! " with vpunch
        jac " ...Yeah, she's been like this for awhile now. "
        jac " I've been trying to calm her down, but she just won't... "
        jac " Please help me, I don't know how people calm other people down... "
        " Help him? "
        menu:
            " Attempt to stop the girl crying ":
                $ jacoblv += 5
                " You attempted to calm Mia down... "
                if kind,calm == True:
                    " You promised to Mia that you're gonna get some seeds for that flower... "
                    " ...And you're gonna get her some nice and fancy flower pots for her! "
                    " Even though your wallet is gonna cry. "
                    " You just didn't want to see her being so upset like this. "
                    m " ... "
                    m " ...Okay... "
                    jac " Wow, uh...that worked. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob and Mia. "
                    " You were also discussing what kind of pot Mia wanted. "
                    " ...Jacob looked like he was considering that he should get something for Mia too. "
                    " But he just decided not to in the end, once you pointed him out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your final class. "
                    " You get down from the rooftop and you walked back to your classroom for the final class. "
                    pause 2.0
                    jump octcookingclass2
                elif mean == True:
                    " Somehow your scary looks calmed Mia down already. "
                    " Probably because she thought that you were gonna beat her ass for acting like a baby. "
                    " Yeah, most likely that, actually. "
                    jac " Wow, uh...that worked. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob and Mia. "
                    " You were also discussing what kind of pot Mia wanted, since you also told her that you're gonna get her a new flower pot. "
                    " ...Jacob looked like he was considering that he should get something for Mia too. "
                    " But he just decided not to in the end, once you pointed him out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your final class. "
                    " You get down from the rooftop and you walked back to your classroom for the final class. "
                    pause 2.0
                    jump octcookingclass2
                else:
                    " You promised to Mia that you're gonna get some seeds for that flower... "
                    " ...And you're gonna get her some nice and fancy flower pots for her! "
                    " Even though your wallet is gonna cry. "
                    " You just didn't want to see her being so upset like this. "
                    m " ... "
                    m " ...Okay... "
                    jac " Wow, uh...that worked. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob and Mia. "
                    " You were also discussing what kind of pot Mia wanted. "
                    " ...Jacob looked like he was considering that he should get something for Mia too. "
                    " But he just decided not to in the end, once you pointed him out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your final class. "
                    " You get down from the rooftop and you walked back to your classroom for the final class. "
                    pause 2.0
                    jump octcookingclass2
            " Nah, not my problem ":
                jac " Uh, try again...? "
                jac " Okay...I'll try... "
                jac " Uh, Mia - {nw} "
                m " WAAAAAAAAAAAAAAAAAAAAAAAAAAHHH!! " with vpunch
                jac " ...{p}Mia - {nw} "
                m " I MISS MY FLOWER SO MUCH!!!!!!!!!!!!!! " with vpunch
                jac " ...This is gonna take the entire break, I swear... "
                scene black with dissolve
                " You spent the rest of the break watching Jacob attempt to calm Mia down. "
                " ...Which he miserably failed in doing. "
                " You could only watch since you didn't really know what to do to comfort the girl either. "
                " You wish you could help, but you just chose not to. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your final class. "
                " You get down from the rooftop and you walked back to your classroom for the final class. "
                pause 2.0
                jump octcookingclass2
    elif jacobknow == False and miaknow == True:
        " You walked up to them and noticed that the girl looked pretty sad. "
        " You then remember a pot that was broken on the front of the school... "
        " That was probably hers. Ruh roh. "
        x " ...Uh. Hi, [name]. "
        $ jacobknow = True
        jac " I'm Jacob by the way, just saying this because I haven't introduced myself to you yet... "
        jac " So...her favorite flower-{nw} "
        m " I ACCIDENTALLY DROPPED MY FAVORITE FLOWER!! " with vpunch
        m " WAAAHHHH!! WHAT AM I SUPPOSED TO DO NOW!!! " with vpunch
        jac " ...Yeah, she's been like this for awhile now. "
        jac " I've been trying to calm her down, but she just won't... "
        jac " Please help me, I don't know how people calm other people down... "
        " Help him? "
        menu:
            " Attempt to stop the girl crying ":
                $ jacoblv += 5
                " You attempted to calm Mia down... "
                if kind,calm == True:
                    " You promised to Mia that you're gonna get some seeds for that flower... "
                    " ...And you're gonna get her some nice and fancy flower pots for her! "
                    " Even though your wallet is gonna cry. "
                    " You just didn't want to see her being so upset like this. "
                    m " ... "
                    m " ...Okay... "
                    jac " Wow, uh...that worked. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob and Mia. "
                    " You were also discussing what kind of pot Mia wanted. "
                    " ...Jacob looked like he was considering that he should get something for Mia too. "
                    " But he just decided not to in the end, once you pointed him out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your final class. "
                    " You get down from the rooftop and you walked back to your classroom for the final class. "
                    pause 2.0
                    jump octcookingclass2
                elif mean == True:
                    " Somehow your scary looks calmed Mia down already. "
                    " Probably because she thought that you were gonna beat her ass for acting like a baby. "
                    " Yeah, most likely that, actually. "
                    jac " Wow, uh...that worked. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob and Mia. "
                    " You were also discussing what kind of pot Mia wanted, since you also told her that you're gonna get her a new flower pot. "
                    " ...Jacob looked like he was considering that he should get something for Mia too. "
                    " But he just decided not to in the end, once you pointed him out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your final class. "
                    " You get down from the rooftop and you walked back to your classroom for the final class. "
                    pause 2.0
                    jump octcookingclass2
                else:
                    " You promised to Mia that you're gonna get some seeds for that flower... "
                    " ...And you're gonna get her some nice and fancy flower pots for her! "
                    " Even though your wallet is gonna cry. "
                    " You just didn't want to see her being so upset like this. "
                    m " ... "
                    m " ...Okay... "
                    jac " Wow, uh...that worked. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob and Mia. "
                    " You were also discussing what kind of pot Mia wanted. "
                    " ...Jacob looked like he was considering that he should get something for Mia too. "
                    " But he just decided not to in the end, once you pointed him out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your final class. "
                    " You get down from the rooftop and you walked back to your classroom for the final class. "
                    pause 2.0
                    jump octcookingclass2
            " Nah, not my problem ":
                jac " Uh, try again...? "
                jac " Okay...I'll try... "
                jac " Uh, Mia - {nw} "
                m " WAAAAAAAAAAAAAAAAAAAAAAAAAAHHH!! " with vpunch
                jac " ...{p}Mia - {nw} "
                m " I MISS MY FLOWER SO MUCH!!!!!!!!!!!!!! " with vpunch
                jac " ...This is gonna take the entire break, I swear... "
                scene black with dissolve
                " You spent the rest of the break watching Jacob attempt to calm Mia down. "
                " ...Which he miserably failed in doing. "
                " You could only watch since you didn't really know what to do to comfort the girl either. "
                " You wish you could help, but you just chose not to. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your final class. "
                " You get down from the rooftop and you walked back to your classroom for the final class. "
                pause 2.0
                jump octcookingclass2
    else:
        " You walked up to them and noticed that the girl looked pretty sad. "
        " You then remember a pot that was broken on the front of the school... "
        " That was probably hers. Ruh roh. "
        x " ...Uh. Hi, [name]. "
        $ jacobknow = True
        jac " I'm Jacob by the way, just saying this because I haven't introduced myself to you yet... "
        $ miaknow = True
        jac " This is my friend, Mia, and uh... "
        jac " So...her favorite flower-{nw} "
        m " I ACCIDENTALLY DROPPED MY FAVORITE FLOWER!! " with vpunch
        m " WAAAHHHH!! WHAT AM I SUPPOSED TO DO NOW!!! " with vpunch
        jac " ...Yeah, she's been like this for awhile now. "
        jac " I've been trying to calm her down, but she just won't... "
        jac " Please help me, I don't know how people calm other people down... "
        " Help him? "
        menu:
            " Attempt to stop the girl crying ":
                $ jacoblv += 5
                " You attempted to calm Mia down... "
                if kind,calm == True:
                    " You promised to Mia that you're gonna get some seeds for that flower... "
                    " ...And you're gonna get her some nice and fancy flower pots for her! "
                    " Even though your wallet is gonna cry. "
                    " You just didn't want to see her being so upset like this. "
                    m " ... "
                    m " ...Okay... "
                    jac " Wow, uh...that worked. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob and Mia. "
                    " You were also discussing what kind of pot Mia wanted. "
                    " ...Jacob looked like he was considering that he should get something for Mia too. "
                    " But he just decided not to in the end, once you pointed him out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your final class. "
                    " You get down from the rooftop and you walked back to your classroom for the final class. "
                    pause 2.0
                    jump octcookingclass2
                elif mean == True:
                    " Somehow your scary looks calmed Mia down already. "
                    " Probably because she thought that you were gonna beat her ass for acting like a baby. "
                    " Yeah, most likely that, actually. "
                    jac " Wow, uh...that worked. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob and Mia. "
                    " You were also discussing what kind of pot Mia wanted, since you also told her that you're gonna get her a new flower pot. "
                    " ...Jacob looked like he was considering that he should get something for Mia too. "
                    " But he just decided not to in the end, once you pointed him out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your final class. "
                    " You get down from the rooftop and you walked back to your classroom for the final class. "
                    pause 2.0
                    jump octcookingclass2
                else:
                    " You promised to Mia that you're gonna get some seeds for that flower... "
                    " ...And you're gonna get her some nice and fancy flower pots for her! "
                    " Even though your wallet is gonna cry. "
                    " You just didn't want to see her being so upset like this. "
                    m " ... "
                    m " ...Okay... "
                    jac " Wow, uh...that worked. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Jacob and Mia. "
                    " You were also discussing what kind of pot Mia wanted. "
                    " ...Jacob looked like he was considering that he should get something for Mia too. "
                    " But he just decided not to in the end, once you pointed him out. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your final class. "
                    " You get down from the rooftop and you walked back to your classroom for the final class. "
                    pause 2.0
                    jump octcookingclass2
            " Nah, not my problem ":
                jac " Uh, try again...? "
                jac " Okay...I'll try... "
                jac " Uh, Mia - {nw} "
                m " WAAAAAAAAAAAAAAAAAAAAAAAAAAHHH!! " with vpunch
                jac " ...{p}Mia - {nw} "
                m " I MISS MY FLOWER SO MUCH!!!!!!!!!!!!!! " with vpunch
                jac " ...This is gonna take the entire break, I swear... "
                scene black with dissolve
                " You spent the rest of the break watching Jacob attempt to calm Mia down. "
                " ...Which he miserably failed in doing. "
                " You could only watch since you didn't really know what to do to comfort the girl either. "
                " You wish you could help, but you just chose not to. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your final class. "
                " You get down from the rooftop and you walked back to your classroom for the final class. "
                pause 2.0
                jump octcookingclass2
label octlibrary5:
    # jam asking orchid if she's good enough for matte
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and spotted two of your classmates hanging out. "
    " You wanted to talk to them... you walked up to them and stood next to them to see what they're talking about. "
    show jamneutral at right with easeinleft
    show orchidneutral at left with easeinleft
    if jamknow == True and orchidknow == True:
        ja " I dunno Orchid, I just don't think I'm good enough for her... "
        oc " Oh, please! "
        oc " You're good enough, don't worry, Jam. "
        oc " Actually - you're great for her! "
        oc " You've protected her many times, comforted her many times...stayed with her a lot... "
        oc " ..I'm sure that she feels happy that you did all of that for her! "
        oc " There's no reason for you to feel so upset if she feels so happy that she's with you, right? "
        oc " So don't be thinking like that if she's always happy with you! "
        oc " So, for short...you're the alpha to her omega. "
        hide jamneutral at bottom
        show jamhappy at right
        ja " Ohmygoddon'tsayitlikethatplease "
        hide orchidneutral at bottom
        show orchidhappy at left
        oc " HEY!! you look like you're liking it!! "
        ja " nonoIdontthisisalsobadbecause [name] ishere "
        oc " Heyyy, [name] is just here to support you, girlie. "
        oc " Right, [name]? "
        " You nodded and did a thumbsup. "
        mc " ...Show her your inner alpha Jam!! awwooo!!! "
        hide orchidhappy at bottom
        show orchidsurprised at left
        hide jamhappy at bottom
        show jamsurprised at right
        " They were both surprised that you actually talked. "
        " Absolutely shocked. Flabbergasted. "
        ja " ...DID YOU REALLY JUST SPEAK JUST TO SAY THAT?? "
        " You gave another thumbs up. "
        oc " OH COME ON, [name]!! TALK MORE!! YOUR VOICE IS SO NICE!! "
        scene black with dissolve
        " You spent the rest of the break talking with Jam and Orchid. "
        " Well, not really talking, you were just nodding and shaking your head. "
        " You were not gonna let them hear your voice again. "
        " I know that I've been saying that you were talking, but in reality... "
        " You were just nodding and shaking your head. "
        " For the times I did say that you were telling someone something? "
        " You shoved your phones notes app into their face. "
        " Simple explanation, sorry for the disappointment. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit of 'talking' with them. "
        " You then walked all the way back to your classroom for the final class. "
        " No one's ever gonna believe that you actually talked to them. "
        pause 2.0
        jump octcookingclass2
    elif jamknow == True and orchidknow == False:
        ja " I dunno Orchid, I just don't think I'm good enough for her... "
        x " Oh, please! "
        x " You're good enough, don't worry, Jam. "
        x " Actually - you're great for her! "
        x " You've protected her many times, comforted her many times...stayed with her a lot... "
        x " ..I'm sure that she feels happy that you did all of that for her! "
        x " There's no reason for you to feel so upset if she feels so happy that she's with you, right? "
        x " So don't be thinking like that if she's always happy with you! "
        x " So, for short...you're the alpha to her omega. "
        hide jamneutral at bottom
        show jamhappy at right
        ja " Ohmygoddon'tsayitlikethatplease "
        hide orchidneutral at bottom
        show orchidhappy at left
        x " HEY!! you look like you're liking it!! "
        ja " nonoIdontthisisalsobadbecause [name] ishere "
        x " Heyyy, [name] is just here to support you, girlie. "
        x " Right, [name]? "
        " You nodded and did a thumbsup. "
        mc " ...Show her your inner alpha Jam!! awwooo!!! "
        hide orchidhappy at bottom
        show orchidsurprised at left
        hide jamhappy at bottom
        show jamsurprised at right
        " They were both surprised that you actually talked. "
        " Absolutely shocked. Flabbergasted. "
        ja " ...DID YOU REALLY JUST SPEAK JUST TO SAY THAT?? "
        " You gave another thumbs up. "
        x " OH COME ON, [name]!! TALK MORE!! YOUR VOICE IS SO NICE!! "
        scene black with dissolve
        " You spent the rest of the break talking with Jam and the scene kid. "
        " Well, not really talking, you were just nodding and shaking your head. "
        " You were not gonna let them hear your voice again. "
        " I know that I've been saying that you were talking, but in reality... "
        " You were just nodding and shaking your head. "
        " For the times I did say that you were telling someone something? "
        " You shoved your phones notes app into their face. "
        " Simple explanation, sorry for the disappointment. "
        $ orchidknow = True
        " You also learned that the scene kid's name was Orchid. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit of 'talking' with them. "
        " You then walked all the way back to your classroom for the final class. "
        " No one's ever gonna believe that you actually talked to them. "
        pause 2.0
        jump octcookingclass2
    elif jamknow == False and orchidknow == True:
        x " I dunno Orchid, I just don't think I'm good enough for her... "
        oc " Oh, please! "
        oc " You're good enough, don't worry, Jam. "
        $ jamknow = True
        " So Jam is that girl on the right's name... "
        oc " Actually - you're great for her! "
        oc " You've protected her many times, comforted her many times...stayed with her a lot... "
        oc " ..I'm sure that she feels happy that you did all of that for her! "
        oc " There's no reason for you to feel so upset if she feels so happy that she's with you, right? "
        oc " So don't be thinking like that if she's always happy with you! "
        oc " So, for short...you're the alpha to her omega. "
        hide jamneutral at bottom
        show jamhappy at right
        ja " Ohmygoddon'tsayitlikethatplease "
        hide orchidneutral at bottom
        show orchidhappy at left
        oc " HEY!! you look like you're liking it!! "
        ja " nonoIdontthisisalsobadbecause [name] ishere "
        oc " Heyyy, [name] is just here to support you, girlie. "
        oc " Right, [name]? "
        " You nodded and did a thumbsup. "
        mc " ...Show her your inner alpha Jam!! awwooo!!! "
        hide orchidhappy at bottom
        show orchidsurprised at left
        hide jamhappy at bottom
        show jamsurprised at right
        " They were both surprised that you actually talked. "
        " Absolutely shocked. Flabbergasted. "
        ja " ...DID YOU REALLY JUST SPEAK JUST TO SAY THAT?? "
        " You gave another thumbs up. "
        oc " OH COME ON, [name]!! TALK MORE!! YOUR VOICE IS SO NICE!! "
        scene black with dissolve
        " You spent the rest of the break talking with Jam and Orchid. "
        " Well, not really talking, you were just nodding and shaking your head. "
        " You were not gonna let them hear your voice again. "
        " I know that I've been saying that you were talking, but in reality... "
        " You were just nodding and shaking your head. "
        " For the times I did say that you were telling someone something? "
        " You shoved your phones notes app into their face. "
        " Simple explanation, sorry for the disappointment. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit of 'talking' with them. "
        " You then walked all the way back to your classroom for the final class. "
        " No one's ever gonna believe that you actually talked to them. "
        pause 2.0
        jump octcookingclass2
    else:
        ja " I dunno Orchid, I just don't think I'm good enough for her... "
        x " Oh, please! "
        x " You're good enough, don't worry. Jam. "
        $ jamknow = True
        " So Jam is that girl on the right's name... "
        x " Actually - you're great for her! "
        x " You've protected her many times, comforted her many times...stayed with her a lot... "
        x " ..I'm sure that she feels happy that you did all of that for her! "
        x " There's no reason for you to feel so upset if she feels so happy that she's with you, right? "
        x " So don't be thinking like that if she's always happy with you! "
        x " So, for short...you're the alpha to her omega. "
        hide jamneutral at bottom
        show jamhappy at right
        ja " Ohmygoddon'tsayitlikethatplease "
        hide orchidneutral at bottom
        show orchidhappy at left
        x " HEY!! you look like you're liking it!! "
        ja " nonoIdontthisisalsobadbecause [name] ishere "
        x " Heyyy, [name] is just here to support you, girlie. "
        x " Right, [name]? "
        " You nodded and did a thumbsup. "
        mc " ...Show her your inner alpha Jam!! awwooo!!! "
        hide orchidhappy at bottom
        show orchidsurprised at left
        hide jamhappy at bottom
        show jamsurprised at right
        " They were both surprised that you actually talked. "
        " Absolutely shocked. Flabbergasted. "
        ja " ...DID YOU REALLY JUST SPEAK JUST TO SAY THAT?? "
        " You gave another thumbs up. "
        x " OH COME ON, [name]!! TALK MORE!! YOUR VOICE IS SO NICE!! "
        scene black with dissolve
        " You spent the rest of the break talking with Jam and the scene kid. "
        " Well, not really talking, you were just nodding and shaking your head. "
        " You were not gonna let them hear your voice again. "
        " I know that I've been saying that you were talking, but in reality... "
        " You were just nodding and shaking your head. "
        " For the times I did say that you were telling someone something? "
        " You shoved your phones notes app into their face. "
        " Simple explanation, sorry for the disappointment. "
        $ orchidknow = True
        " You also learned that the scene kid's name was Orchid. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit of 'talking' with them. "
        " You then walked all the way back to your classroom for the final class. "
        " No one's ever gonna believe that you actually talked to them. "
        pause 2.0
        jump octcookingclass2
label octcookingclass2:
    scene classroom with dissolve
    " You walked into the classroom to see that the teacher was already there. "
    " You sat down onto your seat and you got out your notebook and pencil. "
    " You're pretty sure that you're just gonna have to copy things again for this class. "
    show jiayuneutral at center with easeinleft
    msx " Good morning, class. "
    msx " Please get your notebooks, we are going to be copying down today. "
    msx " If you don't pay attention, good luck to your grades. "
    scene black with dissolve
    " You spent the rest of class copying things down about cooking stuff. "
    " Nothing interesting really happened while you were writing things here and there... "
    " ...But you did hear some students whispering something about a ghost in this school. "
    " The ghost being called Mister Ace...and only came out at whenever you and someone else was alone at night. "
    " You weren't sure if it was real, so you didn't believe it. "
    " But if it was, you're definitely checking it out. "
    play sound "audio/bellring.mp3"
    " The bell rings, finally - class is over. "
    " You can now go back to your bed and rest... "
    " You get all of your stuff packed and you walked out of the school to go to your home. "
    pause 2.0
    jump octendday
label octendday:
    scene paperschoolfront with dissolve
    " You walked out of your school, finally being able to go back to your sweet sweet bed. "
    " You looked around you and your classmates are just hanging out with eachother, or being alone. "
    " You took one last look at your school before you went on your way to your home. "
    scene black with dissolve
    stop music fadeout 1.5
    pause 2.0
    play music "audio/home.mp3" fadein 1.5
    scene mcroom with dissolve
    " You finally got to your home. "
    " You changed out of your school clothes, made yourself dinner... "
    " Then finally checked your school GC to see if there's any homework. "
    " Surprisingly, there's none. Only activities you guys had to do. "
    " You closed your phone and let it charge overnight... "
    " You then tucked yourself into your bed and closed your eyes... "
    scene black with dissolve
    stop music fadeout 1.5
    " ...And you fell asleep. Good night, [name]. "
    pause 2.0
    jump ocwednesday
