label teacherfriday:
    show text " DAY 5 - FRIDAY "
    pause 2.0
    play music "audio/home.mp3" fadein 1.5
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
    jump tfhelp1

label tfhelp1:
    scene hallway with dissolve
    " You took a good look around and spotted a few teachers needing help. "
    " Who do you help? "
    if circleknow,thavelknow,bloomieknow == True:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump circlemeatgrinder
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump thavelmeatgrinder
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump bloomiemeatgrinder
    elif circleknow,thavelknow == True and bloomieknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump circlemeatgrinder
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump thavelmeatgrinder
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump bloomiemeatgrinder
    elif circleknow,bloomieknow == True and thavelknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump circlemeatgrinder
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump thavelmeatgrinder
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump bloomiemeatgrinder
    elif thavelknow,bloomieknow == True and circleknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump circlemeatgrinder
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump thavelmeatgrinder
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump bloomiemeatgrinder
    elif circleknow == True and thavelknow,bloomieknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump circlemeatgrinder
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump thavelmeatgrinder
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump bloomiemeatgrinder
    elif thavelknow == True and circleknow,bloomieknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump circlemeatgrinder
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump thavelmeatgrinder
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump bloomiemeatgrinder
    elif bloomieknow == True and circleknow,thavelknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump circlemeatgrinder
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump thavelmeatgrinder
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump bloomiemeatgrinder
    else:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump circlemeatgrinder
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump thavelmeatgrinder
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump bloomiemeatgrinder
    label circlemeatgrinder:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom and looked around at what they were doing. "
        " Looks like they were answering something... "
        " You looked around and spotted the math teacher at the front of the classroom. "
        " You walked over and took a seat next to her. "
        " Hopefully she wasn't doing anything important as you approached her. "
        show misscircleneutral at center with easeinleft
        if circleknow == True:
            msc " Hmhmmm... "
            msc " Let's see what I can do for my students next week. "
            msc " Some of them are failing a little bit... "
            msc " I should make them do even more activities next week. "
            msc " That way, they can get more points! "
            msc " I better not catch them lacking though... "
            " You poked her shoulder and asked her what she was doing. "
            msc " Oh, [name]! "
            msc " Sorry that I didn't notice you, hehe... "
            msc " I was just busy dealing with the grades of my students. "
            msc " Some of them are pretty low, unfortunately... "
            msc " That's why I'm planning to make them do more activities! "
            msc " With the activities, they can get more points. "
            msc " And they can also show what they're really worth to me that way! "
            msc " Hopefully they DO pass the activities... "
            msc " Otherwise I'm going to... "
            msc " ...Make them do even more activities! "
            msc " They need to pass somehow! "
            msc " I hate seeing my students fail, you know? "
            msc " It just pains me a whole lot. "
            msc " That's why I'm making them do an activity right now! "
            " Just to save their asses? "
            msc " Just to save their asses! "
            msc " Anyway... "
            msc " While you're here, could you help me with something? "
            msc " I know that you got nothing to do, so... "
            msc " How about you give me some ideas for activities? "
            msc " Being honest with you, I don't have much ideas in my head right now. "
            msc " I just know that I need them to do more activities. "
            msc " I could make them do a presentation, buuut... "
            msc " What topic should I give them? "
            msc " This is why I need ideas, ehe.. "
            msc " Hopefully this doesn't bother you, [name]. "
            msc " But I just needed some ideas, alright? "
            " This didn't really bother you, actually. "
            " I mean, you did come here to help. "
            " Of course you can help her. "
            hide misscircleneutral at bottom
            show misscirclehappy at center
            msc " Always glad that you're helping, [name]! "
            msc " Now, could you give me some of those ideas of yours? "
            msc " I'm really in need of your ideas! "
            scene black with dissolve
            " You spent the rest of the class hours talking to Miss Circle about some ideas she could do. "
            " You gave her about 5, and she eventually picked out 3 she could do. "
            " She thanked you after that, and you two continued to talk. "
            " Just about random things, this time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for a break. "
            " You waited for all of the students to get out before you did. "
            pause 2.0
            jump tfbreak1
        else:
            x " Hmhmmm... "
            x " Let's see what I can do for my students next week. "
            x " Some of them are failing a little bit... "
            x " I should make them do even more activities next week. "
            x " That way, they can get more points! "
            x " I better not catch them lacking though... "
            " You poked her shoulder and asked her what she was doing. "
            x " Oh, [name]! "
            x " Sorry that I didn't notice you, hehe... "
            $ circleknow = True
            msc " I'm Miss Circle, by the way. Math teacher. "
            msc " I was just busy dealing with the grades of my students. "
            msc " Some of them are pretty low, unfortunately... "
            msc " That's why I'm planning to make them do more activities! "
            msc " With the activities, they can get more points. "
            msc " And they can also show what they're really worth to me that way! "
            msc " Hopefully they DO pass the activities... "
            msc " Otherwise I'm going to... "
            msc " ...Make them do even more activities! "
            msc " They need to pass somehow! "
            msc " I hate seeing my students fail, you know? "
            msc " It just pains me a whole lot. "
            msc " That's why I'm making them do an activity right now! "
            " Just to save their asses? "
            msc " Just to save their asses! "
            msc " Anyway... "
            msc " While you're here, could you help me with something? "
            msc " I know that you got nothing to do, so... "
            msc " How about you give me some ideas for activities? "
            msc " Being honest with you, I don't have much ideas in my head right now. "
            msc " I just know that I need them to do more activities. "
            msc " I could make them do a presentation, buuut... "
            msc " What topic should I give them? "
            msc " This is why I need ideas, ehe.. "
            msc " Hopefully this doesn't bother you, [name]. "
            msc " But I just needed some ideas, alright? "
            " This didn't really bother you, actually. "
            " I mean, you did come here to help. "
            " Of course you can help her. "
            hide misscircleneutral at bottom
            show misscirclehappy at center
            msc " Always glad that you're helping, [name]! "
            msc " Now, could you give me some of those ideas of yours? "
            msc " I'm really in need of your ideas! "
            scene black with dissolve
            " You spent the rest of the class hours talking to Miss Circle about some ideas she could do. "
            " You gave her about 5, and she eventually picked out 3 she could do. "
            " She thanked you after that, and you two continued to talk. "
            " Just about random things, this time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for a break. "
            " You waited for all of the students to get out before you did. "
            pause 2.0
            jump tfbreak1
    label thavelmeatgrinder:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the langauge teacher's classroom... "
        " Hopefully they weren't doing anything important. "
        " And you were right, they weren't doing anything important. "
        " Well, to you atleast. "
        " The students were just answering something. "
        " The teacher was just sitting infront and watching over the students. "
        " You walked over to her and took a seat right next to her. "
        show msthravelneutral at center with easeinleft
        if thavelknow == True:
            mst " Jeez, their grades aren't looking the best right now... "
            mst " Should I just give them more things to work on? "
            mst " Surely, that'll save them... "
            hide msthravelneutral at bottom
            show msthravelangry at center
            mst " God, it's so annoying to see them fail. "
            mst " I really tried my best on teaching them this year, too. "
            mst " Ergh... "
            hide msthravelangry at bottom
            show msthravelsurprised at center
            " You tapped her shoulder and asked her what she was doing. "
            mst " Oh, [name]! "
            mst " Jeez...I didn't notice you there. "
            mst " Sorry about that. "
            hide msthravelsurprised at bottom
            show msthravelneutral at center
            mst " I was just...talking to myself. "
            mst " About my students grades and all. "
            mst " They've been...not the best. "
            mst " That's why I've been thinking about doing some things to improve their grades! "
            mst " Like giving them more activities, after all. "
            mst " Doing activities means really high points... "
            mst " If you didn't know that already, [name]. "
            mst " So if they did a few activities here and there... "
            mst " Their grades would improve a whole lot. "
            mst " I don't want to overdo it, though. "
            mst " Another thing though... "
            mst " I have absolutely no idea on what kind of activity I should give them. "
            mst " I could make them paint something about countries... "
            mst " But then again, I've already done that awhile ago. "
            mst " So that idea is going to have to be scrapped... "
            mst " I could make them do a presentation... "
            mst " That would be good - since our last presentation had to be cancelled. "
            mst " Due to some personal issues that I had. "
            mst " But there's just one little problem... "
            mst " I have no clue on what they should present about. "
            mst " It can't be about any old topic, too. "
            mst " It has to be something new, you know? "
            mst " But we haven't really fully discussed our topic yet. "
            mst " Guh...who knew making activities can be this hard? "
            mst " It's not that much of a pain, just a little bit. "
            mst " But it's still a bit of pain nonetheless. "
            mst " Sighhh... "
            mst " ...Oh, wait! "
            mst " [name], you came here to help, right? "
            mst " Maybe you could help me with this? "
            mst " You know, about thinking for an activity my students could do. "
            mst " You're good with ideas, right? "
            mst " You could most definitely help me with this! "
            mst " ...Well, that is, if you want to help me. "
            mst " Do you? "
            " You DID come here to help... "
            " And you would say that you're pretty good at thinking for ideas... "
            " You agreed to help her. "
            mst " That's great! "
            mst " Now, just give me about... "
            mst " Five ideas, and I'll pick two to do. "
            mst " Should be easy for you, right? "
            " Yup. You gave her a thumbs up. "
            " You then started thinking for ideas. "
            scene black with dissolve
            " You spent the rest of the class hours talking to Miss Thavel about ideas she could do. "
            " Just talking about the things she could do to help her students grades... "
            " You gave her five ideas and she chose two that she liked. "
            " She thanked you afterwards, and you two talked about random things her students did to pass time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for a break. "
            " You waited for all of the students to get out before you did. "
            pause 2.0
            jump tfbreak1
        else:
            x " Jeez, their grades aren't looking the best right now... "
            x " Should I just give them more things to work on? "
            x " Surely, that'll save them... "
            hide msthravelneutral at bottom
            show msthravelangry at center
            x " God, it's so annoying to see them fail. "
            x " I really tried my best on teaching them this year, too. "
            x " Ergh... "
            hide msthravelangry at bottom
            show msthravelsurprised at center
            " You tapped her shoulder and asked her what she was doing. "
            x " Oh, [name]! "
            x " Jeez...I didn't notice you there. "
            x " Sorry about that. "
            hide msthravelsurprised at bottom
            show msthravelneutral at center
            $ thavelknow = True
            mst " I'm Miss Thavel, by the way. "
            mst " I was just...talking to myself. "
            mst " About my students grades and all. "
            mst " They've been...not the best. "
            mst " That's why I've been thinking about doing some things to improve their grades! "
            mst " Like giving them more activities, after all. "
            mst " Doing activities means really high points... "
            mst " If you didn't know that already, [name]. "
            mst " So if they did a few activities here and there... "
            mst " Their grades would improve a whole lot. "
            mst " I don't want to overdo it, though. "
            mst " Another thing though... "
            mst " I have absolutely no idea on what kind of activity I should give them. "
            mst " I could make them paint something about countries... "
            mst " But then again, I've already done that awhile ago. "
            mst " So that idea is going to have to be scrapped... "
            mst " I could make them do a presentation... "
            mst " That would be good - since our last presentation had to be cancelled. "
            mst " Due to some personal issues that I had. "
            mst " But there's just one little problem... "
            mst " I have no clue on what they should present about. "
            mst " It can't be about any old topic, too. "
            mst " It has to be something new, you know? "
            mst " But we haven't really fully discussed our topic yet. "
            mst " Guh...who knew making activities can be this hard? "
            mst " It's not that much of a pain, just a little bit. "
            mst " But it's still a bit of pain nonetheless. "
            mst " Sighhh... "
            mst " ...Oh, wait! "
            mst " [name], you came here to help, right? "
            mst " Maybe you could help me with this? "
            mst " You know, about thinking for an activity my students could do. "
            mst " You're good with ideas, right? "
            mst " You could most definitely help me with this! "
            mst " ...Well, that is, if you want to help me. "
            mst " Do you? "
            " You DID come here to help... "
            " And you would say that you're pretty good at thinking for ideas... "
            " You agreed to help her. "
            mst " That's great! "
            mst " Now, just give me about... "
            mst " Five ideas, and I'll pick two to do. "
            mst " Should be easy for you, right? "
            " Yup. You gave her a thumbs up. "
            " You then started thinking for ideas. "
            scene black with dissolve
            " You spent the rest of the class hours talking to Miss Thavel about ideas she could do. "
            " Just talking about the things she could do to help her students grades... "
            " You gave her five ideas and she chose two that she liked. "
            " She thanked you afterwards, and you two talked about random things her students did to pass time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for a break. "
            " You waited for all of the students to get out before you did. "
            pause 2.0
            jump tfbreak1
    label bloomiemeatgrinder:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked over to the science teachers classroom and prayed that they weren't doing anything important... "
        " And thankfully, they weren't. "
        " The students were just answering something. "
        " You looked around to try and find where the science teacher was... "
        " And she was just sitting infront of the class, looking like she was thinking about something deeply. "
        " You took a seat next to her and observed her for a good bit. "
        show missbloomieneutral at center with easeinleft
        if bloomieknow == True:
            msb " ... "
            msb " ...My students grades aren't going too well. "
            msb " I should do something about that. "
            msb " Shouldn't I, [name]? "
            " Huh, you didn't even notice that she noticed you. "
            " Interesting and also impressive. "
            msb " ...I probably should. "
            msb " Failing students isn't really...acceptable, for me. "
            msb " They should atleast pass. "
            msb " But the thing is... "
            msb " I don't know what to do to improve their grades. "
            msb " I've been sitting here and trying to think of what I could do... "
            msb " I know I should give them some activities because activities gives good points. "
            msb " That would improve their grades greatly. "
            msb " ...But I don't know what actvitiy I should give them. "
            msb " I'm sure you have an idea for that, [name]. "
            msb " You could help me out on this, if you want. "
            msb " I'm not going to force you if you don't want to help. "
            msb " It's fine. "
            msb " I could probably come up with something on the weekends... "
            msb " If I'm not busy enough. "
            " Well, you did come here to help. "
            " You agreed on helping her. "
            msb " Thank you very much. "
            msb " I appreciate you for choosing to help me. "
            msb " I need atleast 5 ideas. "
            msb " I'll pick about 3. "
            " You nodded and started giving her ideas on what she could do. "
            scene black with dissolve
            " You spent the rest of class hours talking with Miss Bloomie about the ideas she could do. "
            " You gave her about 5, and she chose 3. "
            " Pretty good amount, in all honesty. "
            " She didn't talk to you much while you were there though. "
            " She was too busy writing down some things into her notebook. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another break. "
            " You waited for the students to get out before you did. "
            pause 2.0
            jump tfbreak1
        else:
            x " ... "
            x " ...My students grades aren't going too well. "
            x " I should do something about that. "
            x " Shouldn't I, [name]? "
            " Huh, you didn't even notice that she noticed you. "
            " Interesting and also impressive. "
            $ bloomieknow = True
            msb " ...I'm Miss Bloomie, the science teacher. "
            msb " Sorry that I didn't introduce myself earlier, but... "
            msb " ...I probably should do something about their grades. "
            msb " Failing students isn't really...acceptable, for me. "
            msb " They should atleast pass. "
            msb " But the thing is... "
            msb " I don't know what to do to improve their grades. "
            msb " I've been sitting here and trying to think of what I could do... "
            msb " I know I should give them some activities because activities gives good points. "
            msb " That would improve their grades greatly. "
            msb " ...But I don't know what actvitiy I should give them. "
            msb " I'm sure you have an idea for that, [name]. "
            msb " You could help me out on this, if you want. "
            msb " I'm not going to force you if you don't want to help. "
            msb " It's fine. "
            msb " I could probably come up with something on the weekends... "
            msb " If I'm not busy enough. "
            " Well, you did come here to help. "
            " You agreed on helping her. "
            msb " Thank you very much. "
            msb " I appreciate you for choosing to help me. "
            msb " I need atleast 5 ideas. "
            msb " I'll pick about 3. "
            " You nodded and started giving her ideas on what she could do. "
            scene black with dissolve
            " You spent the rest of class hours talking with Miss Bloomie about the ideas she could do. "
            " You gave her about 5, and she chose 3. "
            " Pretty good amount, in all honesty. "
            " She didn't talk to you much while you were there though. "
            " She was too busy writing down some things into her notebook. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another break. "
            " You waited for the students to get out before you did. "
            pause 2.0
            jump tfbreak1
label tfbreak1:
    scene hallway with dissolve
    " You walked around, looking at the things happening near you... "
    " Just listening to the students talking about random things. "
    " Like drama and stuff. "
    " You swear, there's new drama every single day. "
    " Atleast it keeps the school interesting... "
    " Hearing drama isn't bad, as long as nothing serious happens. "
    " I feel like I've said that before... "
    " But, yeah. "
    " Drama is interesting. "
    " Very interesting. "
    " Maybe you should listen to those drama youtube videos if you wanted more of it. "
    " Something's always going on in the internet nowadays... "
    " You could quite literally get caught if you do the smallest thing. "
    " No matter if its a small thing or a big thing, "
    " There's always a chance for you to get caught, "
    " As long as you said or did something wrong to someone. "
    " Or if you just said or did something problematic. "
    " ...Yeah, suddenly, your playlist is filled with youtube drama videos. "
    " You feel like watching those to get you to sleep at night. "
    " Sleeping to videos is really good... "
    scene black with dissolve
    " You spent the rest of the break walking around the hallways. "
    " Just wandering around... "
    " You also found 20$ on the floor. Nice. "
    " You quickly took it and continued walking around the hallways. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for you to help someone else again. "
    " You started looking around to see if anyone needed help... "
    pause 2.0
    jump tfhelp2
label tfhelp2:
    scene hallway with dissolve
    " You took a good look around and found three teachers who need help. "
    " Who do you help for this break? "
    if emilyknow,demiknow,sashaknow == True:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump emilyhideaway
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump demihideaway
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump sashahideaway
    elif emilyknow,demiknow == True and sashaknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump emilyhideaway
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump demihideaway
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump sashahideaway
    elif emilyknow,sashaknow == True and demiknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump emilyhideaway
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump demihideaway
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump sashahideaway
    elif demiknow,sashaknow == True and emilyknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump emilyhideaway
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump demihideaway
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump sashahideaway
    elif emilyknow == True and demiknow,sashaknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump emilyhideaway
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump demihideaway
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump sashahideaway
    elif demiknow == True and emilyknow,sashaknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump emilyhideaway
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump demihideaway
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump sashahideaway
    elif sashaknow == True and emilykno,demiknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump emilyhideaway
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump demihideaway
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump sashahideaway
    else:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump emilyhideaway
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump demihideaway
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump sashahideaway
    label emilyhideaway:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the history teacher's classroom... "
        " Hopefully, they have absolutely nothing to do right now. "
        " And you were right, they were doing nothing. "
        " They were just doing research on something. "
        " You looked around and spotted the history teacher looking at something at the back of the class. "
        " Let's see what she's looking at... "
        show msemilyneutral at center with easeinleft
        if emilyknow == True:
            mse " Geez... "
            mse " I've been trying my best, haven't I? "
            hide msemilyneutral at bottom
            show msemilysad at center
            mse " I've been teaching them all the right things... "
            mse " I'm pretty sure that I made them copy all the notes I had... "
            mse " So why are their grades still failing? "
            mse " ...Should I just give them more activities to do? "
            mse " I mean... "
            " You tapped her shoulder and asked her what she was talking about. "
            hide msemilysad at bottom
            show msemilyshock at center
            mse " Oh heyyy, [name]!! "
            mse " I'm sorry that I didn't notice you... "
            mse " I think I was... "
            mse " ...A little too lost in my thoughts there, hehe. "
            hide msemilyshock at bottom
            show msemilyneutral at center
            mse " I was thinking about the grades of my students. "
            mse " And most of them...aren't looking the best. "
            mse " Now, I'm kind of wondering what I did wrong, but... "
            mse " Then again, it's only the start of second quarter, so... "
            mse " I don't think I should worry about it too much, right? "
            mse " ...It still pains me to see their grades so low though. "
            mse " I cringe whenever I see low grades. "
            mse " Like hello??? "
            mse " I did my best teaching you, come on... "
            mse " Don't tell me you didn't pay attention. "
            mse " Geez... "
            mse " But, if their grades ARE still low after awhile... "
            mse " I'm gonna have to do some stuff to improve them. "
            mse " Of course - a teacher's worst nightmare is a failing student... "
            mse " Or not - if you really hate that specific student. "
            mse " That's why I'm trying to think of ideas so that I could improve their grades later on! "
            mse " Not right now, since it's the start of everything at the moment. "
            mse " But only later in the middle of the quarter. "
            mse " Hm....what should I do, [name]? "
            mse " I need some really good ideas to help my students. "
            mse " I can't just throw quizzes at them... "
            mse " It would be way too soon for that. "
            mse " And besides...quizzes are just gonna give low points. "
            mse " That won't really do. "
            mse " Hm... "
            mse " I could make them do an activity! "
            mse " Believe it or not, "
            mse " Activities give the most points than other things. "
            mse " That's why you've GOT to do them! "
            mse " But what kind of activity should I give them...? "
            mse " ...Eh, I have no idea. "
            mse " Maybe you could give me some ideas, [name]? "
            mse " I'm sure you've got some good ideas in that noggin of yours! "
            " You did come over here to help... "
            " You agreed on helping Miss Emily come up with an idea. "
            hide msemilyneutral at bottom
            show msemilyhappy at center
            mse " Thanks a lot, [name]! "
            mse " I can always trust you, hehe. "
            mse " Now, time for the ideas to flow in... "
            scene black with dissolve
            " You spent the rest of the class hours giving Miss Emily ideas for her activities. "
            " You gave her a lot of ideas, but there was one that she liked the most. "
            " Afterwards, she thanked you. "
            " You and Emily then talked about random things for the rest of the period to pass time. "
            " It was nice, talking to her... "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak2
        else:
            x " Geez... "
            x " I've been trying my best, haven't I? "
            hide msemilyneutral at bottom
            show msemilysad at center
            x " I've been teaching them all the right things... "
            x " I'm pretty sure that I made them copy all the notes I had... "
            x " So why are their grades still failing? "
            x " ...Should I just give them more activities to do? "
            x " I mean... "
            " You tapped her shoulder and asked her what she was talking about. "
            hide msemilysad at bottom
            show msemilyshock at center
            x " Oh heyyy, [name]!! "
            x " I'm sorry that I didn't notice you... "
            $ emilyknow = True
            mse " Uh...I'm Miss Emily, by the way. History teacher. "
            mse " I think I was... "
            mse " ...A little too lost in my thoughts there, hehe. "
            hide msemilyshock at bottom
            show msemilyneutral at center
            mse " I was thinking about the grades of my students. "
            mse " And most of them...aren't looking the best. "
            mse " Now, I'm kind of wondering what I did wrong, but... "
            mse " Then again, it's only the start of second quarter, so... "
            mse " I don't think I should worry about it too much, right? "
            mse " ...It still pains me to see their grades so low though. "
            mse " I cringe whenever I see low grades. "
            mse " Like hello??? "
            mse " I did my best teaching you, come on... "
            mse " Don't tell me you didn't pay attention. "
            mse " Geez... "
            mse " But, if their grades ARE still low after awhile... "
            mse " I'm gonna have to do some stuff to improve them. "
            mse " Of course - a teacher's worst nightmare is a failing student... "
            mse " Or not - if you really hate that specific student. "
            mse " That's why I'm trying to think of ideas so that I could improve their grades later on! "
            mse " Not right now, since it's the start of everything at the moment. "
            mse " But only later in the middle of the quarter. "
            mse " Hm....what should I do, [name]? "
            mse " I need some really good ideas to help my students. "
            mse " I can't just throw quizzes at them... "
            mse " It would be way too soon for that. "
            mse " And besides...quizzes are just gonna give low points. "
            mse " That won't really do. "
            mse " Hm... "
            mse " I could make them do an activity! "
            mse " Believe it or not, "
            mse " Activities give the most points than other things. "
            mse " That's why you've GOT to do them! "
            mse " But what kind of activity should I give them...? "
            mse " ...Eh, I have no idea. "
            mse " Maybe you could give me some ideas, [name]? "
            mse " I'm sure you've got some good ideas in that noggin of yours! "
            " You did come over here to help... "
            " You agreed on helping Miss Emily come up with an idea. "
            hide msemilyneutral at bottom
            show msemilyhappy at center
            mse " Thanks a lot, [name]! "
            mse " I can always trust you, hehe. "
            mse " Now, time for the ideas to flow in... "
            scene black with dissolve
            " You spent the rest of the class hours giving Miss Emily ideas for her activities. "
            " You gave her a lot of ideas, but there was one that she liked the most. "
            " Afterwards, she thanked you. "
            " You and Emily then talked about random things for the rest of the period to pass time. "
            " It was nice, talking to her... "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak2
    label demihideaway:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the music teachers classroom, hoping that nothing important was going on. "
        " And you were lucky this time, nothing too important was going on. "
        " Looks like the students just had to answer something on their papers. "
        " You looked around the classroom to try and find the music teacher.. "
        " And you found him at the very back of the classroom, cleaning one of the instruments. "
        " You yoinked a nearby empty chair and you took a seat next to him. "
        show mrdemineutral at center with easeinleft
        if demiknow == True:
            msd " Oh gosh, what should I do... "
            msd " I know it's just the start of second quarter, but... "
            msd " Their grades aren't looking the best right now... "
            msd " Oh gosh, oh geez... "
            msd " I should do something about it later in the quarter... "
            msd " Not right now... "
            " You tapped his shoulder to get his attention. "
            hide mrdemineutral at bottom
            show mrdemisurprised at center
            " Looks like he didn't know that you were there. "
            " He just got a tad bit jumpscared by you. "
            msd " ...Eek!! "
            msd " Oh, um...hi there, [name]... "
            hide mrdemisurprised at bottom
            show mrdemineutral at center
            msd " You, uh... "
            msd " You must be wondering what I was talking about... "
            msd " Well, you see... "
            msd " I was talking to myself about my students grades... "
            msd " And I know that I shouldn't worry too much about them... "
            msd " It's the start of second quarter, after all... "
            msd " Of course their grades are going to be astronomically low... "
            msd " But I can't help but worry... "
            msd " What if their grades don't get any higher...? "
            msd " What if they're going to fail...? "
            msd " I don't want that... "
            msd " And I don't want to just give them free points out of nowhere, too... "
            msd " I would get an earful from Miss Grace if I did that... "
            msd " Sighh... "
            msd " Maybe I should just... "
            msd " Give them an activity to do...? "
            msd " I mean... "
            msd " From what I remember - activities give the most points over anything... "
            msd " Not tests, not anything else... "
            msd " That's what I should probably do, right...? "
            msd " But... "
            msd " What should I give them an activity about...? "
            msd " That's the only problem I have right now... "
            msd " I have absolutely no idea on what activity I should give them... "
            msd " It should be about a new topic, right...? "
            msd " Hmhmmm... "
            msd " ...I'm...sorry if I'm bothering you about this, but... "
            msd " Do you think...you could... "
            msd " Give me some ideas for an activity...? "
            msd " I really have no clue on what to give them... "
            msd " It's okay if you don't want to help... "
            msd " I think I can figure something out in the weekends... "
            msd " But... "
            msd " I would prefer if...I figured something out right now... "
            msd " It would be much faster, I think...? "
            msd " I don't know what I'm getting at, but I think you know... "
            " Well, you did come over here to help. "
            " You agreed on helping Mister Demi. "
            msd " T...thanks a lot, [name]... "
            msd " (I really hope I'm not bothering [them] right now...) "
            msd " (But...[they] look like [they] really want to help...) "
            msd " (Well, if [they] really want to, then...) "
            msd " (I don't mind that...) "
            scene black with dissolve
            " You spent the rest of the class hours giving Mister Demi activity ideas. "
            " You gave him a few, and there was one that he really liked. "
            " He thanked you after all of that. "
            " You then talked with him for the rest of the period to pass time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak2
        else:
            x " Oh gosh, what should I do... "
            x " I know it's just the start of second quarter, but... "
            x " Their grades aren't looking the best right now... "
            x " Oh gosh, oh geez... "
            x " I should do something about it later in the quarter... "
            x " Not right now... "
            " You tapped his shoulder to get his attention. "
            hide mrdemineutral at bottom
            show mrdemisurprised at center
            " Looks like he didn't know that you were there. "
            " He just got a tad bit jumpscared by you. "
            x " ...Eek!! "
            x " Oh, um...hi there, [name]... "
            hide mrdemisurprised at bottom
            show mrdemineutral at center
            $ demiknow = True
            msd " Um...I'm Mister Demi, by the way...music teacher... "
            msd " ...You, uh... "
            msd " You must be wondering what I was talking about... "
            msd " Well, you see... "
            msd " I was talking to myself about my students grades... "
            msd " And I know that I shouldn't worry too much about them... "
            msd " It's the start of second quarter, after all... "
            msd " Of course their grades are going to be astronomically low... "
            msd " But I can't help but worry... "
            msd " What if their grades don't get any higher...? "
            msd " What if they're going to fail...? "
            msd " I don't want that... "
            msd " And I don't want to just give them free points out of nowhere, too... "
            msd " I would get an earful from Miss Grace if I did that... "
            msd " Sighh... "
            msd " Maybe I should just... "
            msd " Give them an activity to do...? "
            msd " I mean... "
            msd " From what I remember - activities give the most points over anything... "
            msd " Not tests, not anything else... "
            msd " That's what I should probably do, right...? "
            msd " But... "
            msd " What should I give them an activity about...? "
            msd " That's the only problem I have right now... "
            msd " I have absolutely no idea on what activity I should give them... "
            msd " It should be about a new topic, right...? "
            msd " Hmhmmm... "
            msd " ...I'm...sorry if I'm bothering you about this, but... "
            msd " Do you think...you could... "
            msd " Give me some ideas for an activity...? "
            msd " I really have no clue on what to give them... "
            msd " It's okay if you don't want to help... "
            msd " I think I can figure something out in the weekends... "
            msd " But... "
            msd " I would prefer if...I figured something out right now... "
            msd " It would be much faster, I think...? "
            msd " I don't know what I'm getting at, but I think you know... "
            " Well, you did come over here to help. "
            " You agreed on helping Mister Demi. "
            msd " T...thanks a lot, [name]... "
            msd " (I really hope I'm not bothering [them] right now...) "
            msd " (But...[they] look like [they] really want to help...) "
            msd " (Well, if [they] really want to, then...) "
            msd " (I don't mind that...) "
            scene black with dissolve
            " You spent the rest of the class hours giving Mister Demi activity ideas. "
            " You gave him a few, and there was one that he really liked. "
            " He thanked you after all of that. "
            " You then talked with him for the rest of the period to pass time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak2
    label sashahideaway:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the art teachers classroom... "
        " Nothing important was going on, just the teacher letting students do arts and crafts. "
        " You saw someone making a robot with cardboard. Yowza. "
        " You also saw a whole lot of cool things. "
        " Didn't know the students here could be so talented... "
        " You looked around to check where the art teacher is... "
        " And found her at the back of the classroom, thinking about something. "
        " You walked over to her, curious about what she might be thinking about. "
        show sashaneutral at center with easeinleft
        if sashaknow == True:
            mss " Hmhm, looks like all of my students are enjoying themselves! "
            mss " I love it when everyone just gets to relax like this and have fun... "
            mss " Reminds me of my own good days, hehe. "
            mss " The good days while I was still in school, while Demi and Emily... "
            mss " My grades were fumbling so bad back then, hehe! "
            hide sashaneutral at bottom
            show sashaconfused at center
            mss " Hmm... "
            mss " I know I shouldn't be worrying about this too much, but... "
            mss " Their grades are kind of...low right now. "
            mss " I don't want them to end up like me back then. "
            mss " Always worrying about my grades at the last minute... "
            mss " I should probably do something about that. "
            hide sashaconfused at bottom
            show sashaneutral at center
            mss " Oh hey there, [name]! "
            mss " I didn't notice you being there at first, haha... "
            mss " Was just deep in my thoughts. "
            mss " I was thinking... "
            mss " These kids sort of remind my of my own golden days. "
            mss " You know, when I was still young like them... "
            mss " Now look at me! I'm a grown and responsible adult! "
            mss " Well, not really responsible, hehe. "
            mss " They're just having fun....relaxing... "
            mss " Something that a kid should be doing. "
            mss " They shouldn't have to stress out all the time, you know? "
            mss " But then... "
            mss " If I keep on making them relaxed like this... "
            mss " I think they'll get too used to it. "
            mss " I've gotta be atleast a little strict to them! "
            mss " Just so that they won't be too relaxed. "
            mss " And I've also been worrying about their grades... "
            mss " It's only been the start of second quarter this week, but... "
            mss " Can't help but worry, you know? "
            mss " Almost reminds me of the times where I would worry over my own grades, hehe... "
            mss " I would always pass things in very late! "
            mss " I was too busy having fun with my own friends at those times... "
            mss " And now I have to make sure that these students won't fail my class. "
            mss " Hm... "
            mss " Maybe I should give them a few activities  to boost their grades in the middle of the quarter? "
            mss " Should be a good idea, right [name]? "
            mss " The problem is, I have no idea what activities I should give them. "
            mss " I've been trying to think about that for awhile now... "
            mss " I mean, I know I can just think about it later in the weekends... "
            mss " But I think it's better to think of something right now, right? "
            mss " Just so that I wouldn't have to worry on sunday! "
            mss " Hm...do you perhaps have any ideas, [name]? "
            mss " You could help me out on this if you want to! "
            mss " I'm not gonna force you if you don't want to help, of course. "
            " You did come over here to help her... "
            " You agreed on helping Miss Sasha for this period. "
            hide sashaneutral at bottom
            show sashahappy at center
            mss " Thanks, [name]! "
            mss " Always happy whenever you help me and the other teachers! "
            mss " Now, time for those ideas... "
            scene black with dissolve
            " You spent a few minutes giving Miss Sasha some ideas for activities. "
            " You gave her a lot, and she picked two that she really liked. "
            " After that, she thanked you for your help. "
            " You and Miss Sasha then talked about the days when you two were kids to pass the time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone else to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak2
        else:
            x " Hmhm, looks like all of my students are enjoying themselves! "
            x " I love it when everyone just gets to relax like this and have fun... "
            x " Reminds me of my own good days, hehe. "
            x " The good days while I was still in school, while Demi and Emily... "
            x " My grades were fumbling so bad back then, hehe! "
            hide sashaneutral at bottom
            show sashaconfused at center
            x " Hmm... "
            x " I know I shouldn't be worrying about this too much, but... "
            x " Their grades are kind of...low right now. "
            x " I don't want them to end up like me back then. "
            x " Always worrying about my grades at the last minute... "
            x " I should probably do something about that. "
            hide sashaconfused at bottom
            show sashaneutral at center
            x " Oh hey there, [name]! "
            x " I didn't notice you being there at first, haha... "
            x " Was just deep in my thoughts. "
            $ sashaknow = True
            mss " I'm Miss Sasha, by the way! art teacher! "
            mss " And, uh...I was thinking... "
            mss " These kids sort of remind my of my own golden days. "
            mss " You know, when I was still young like them... "
            mss " Now look at me! I'm a grown and responsible adult! "
            mss " Well, not really responsible, hehe. "
            mss " They're just having fun....relaxing... "
            mss " Something that a kid should be doing. "
            mss " They shouldn't have to stress out all the time, you know? "
            mss " But then... "
            mss " If I keep on making them relaxed like this... "
            mss " I think they'll get too used to it. "
            mss " I've gotta be atleast a little strict to them! "
            mss " Just so that they won't be too relaxed. "
            mss " And I've also been worrying about their grades... "
            mss " It's only been the start of second quarter this week, but... "
            mss " Can't help but worry, you know? "
            mss " Almost reminds me of the times where I would worry over my own grades, hehe... "
            mss " I would always pass things in very late! "
            mss " I was too busy having fun with my own friends at those times... "
            mss " And now I have to make sure that these students won't fail my class. "
            mss " Hm... "
            mss " Maybe I should give them a few activities  to boost their grades in the middle of the quarter? "
            mss " Should be a good idea, right [name]? "
            mss " The problem is, I have no idea what activities I should give them. "
            mss " I've been trying to think about that for awhile now... "
            mss " I mean, I know I can just think about it later in the weekends... "
            mss " But I think it's better to think of something right now, right? "
            mss " Just so that I wouldn't have to worry on sunday! "
            mss " Hm...do you perhaps have any ideas, [name]? "
            mss " You could help me out on this if you want to! "
            mss " I'm not gonna force you if you don't want to help, of course. "
            " You did come over here to help her... "
            " You agreed on helping Miss Sasha for this period. "
            hide sashaneutral at bottom
            show sashahappy at center
            mss " Thanks, [name]! "
            mss " Always happy whenever you help me and the other teachers! "
            mss " Now, time for those ideas... "
            scene black with dissolve
            " You spent a few minutes giving Miss Sasha some ideas for activities. "
            " You gave her a lot, and she picked two that she really liked. "
            " After that, she thanked you for your help. "
            " You and Miss Sasha then talked about the days when you two were kids to pass the time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone else to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak2
label tfbreak2:
    scene hallway with dissolve
    " You walked around the hallways, just doing your job... "
    " As you walked around, you spotted a whole lot of dirt lying around in a corner. "
    " And also some of the trash in a trash bin overflowing. "
    " You wonder if the janitor here does their job... "
    " As much as you didn't want to do the work, someone has to do it. "
    " If that trash bin overflowed too much... "
    " You have a feeling the school hallways would be utterly filled with trash. "
    " And you didn't want to smell someone's rotten food in the hallways everyday. "
    " You're gonna do this job, whether you like it or not... "
    " As long as you don't get some of that weird garbage juice, then you're fine. "
    " You probably should've just taken the job as a janitor in here. "
    " You also look a tad bit weird since you're a teacher doing this stuff... "
    " Normally, the janitor does it. "
    " You haven't seen a single teacher do this. "
    " Throwing away the trash, I mean. "
    " But, I guess it gives you something to do for this break. "
    " Something to do instead of checking on your students all the time. "
    " And also talking to other people. "
    " Anyway, let's get cleaning... "
    scene black with dissolve
    " You spent the rest of the break cleaning out some trash cans. "
    " You found more than one trash cans that were overflowing, so.. "
    " More work for you, I guess. "
    " Again, atleast it gives you something to do. "
    " Even though it's kind of a pain in your ass. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for you to help the teachers again. "
    " You walked around to see if who needed the help the most... "
    pause 2.0
    jump tfhelp3
label tfhelp3:
    scene hallway with dissolve
    " Looks like it's time for you to help another teacher. "
    " Who do you want to help for this time? "
    if circleknow,thavelknow,bloomieknow == True:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump uhcircle
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump uhthavel
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump uhbloomie
    elif circleknow,thavelknow == True and bloomieknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump uhcircle
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump uhthavel
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump uhbloomie
    elif circleknow,bloomieknow == True and thavelknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump uhcircle
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump uhthavel
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump uhbloomie
    elif thavelknow,bloomieknow == True and circleknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump uhcircle
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump uhthavel
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump uhbloomie
    elif circleknow == True and thavelknow,bloomieknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump uhcircle
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump uhthavel
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump uhbloomie
    elif thavelknow == True and circleknow,bloomieknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump uhcircle
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump uhthavel
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump uhbloomie
    elif bloomieknow == True and circleknow,thavelknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump uhcircle
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump uhthavel
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump uhbloomie
    else:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump uhcircle
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump uhthavel
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump uhbloomie
    label uhcircle:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom and looked around if they're doing anything important. "
        " Looks like they're not... "
        " They're just asking eachother for notes and such. "
        " Wonder why that is... "
        " You looked around so that you could find the teacher... "
        " You found the teacher at the very back of the school after a good amount of looking. "
        " You walked over to her and you stood next to her. "
        show misscircleneutral at center with easeinleft
        if circleknow == True:
            msc " Hey there, [name]! "
            msc " I was just watching over my students. "
            msc " Hmhmmm... "
            msc " Looks like they're actually asking eachother for notes! "
            msc " I like the fact that they aren't slacking off for once. "
            msc " Looks like Engel's the one that's being asked the most, hehe. "
            msc " Of course he would be - he's the star student! "
            msc " He's got all the notes and everything... "
            msc " Impressive that he could pick up with my speed, honestly. "
            msc " Should probably give him some snacks for that... "
            msc " Maybe some of the candy that I have in my drawer? "
            " You said thought that Engel would like some candy. "
            " But then again, some students are going to start asking from you a whole lot. "
            " If you want to reward him, then just give him some plus points for now. "
            " But when no one's looking? give him some chocolate. "
            hide misscircleneutral at bottom
            show misscirclehappy at center
            msc " Hm, good point and good idea! "
            msc " Always appreciate you giving good ideas to us like these, [name]. "
            msc " Really helps, you know? "
            msc " Even though this one's just for candy. "
            hide misscirclehappy at bottom
            show misscircleneutral at center
            " You just nodded in response. "
            " You then asked her why her students were asking for notes... "
            " I mean, they can't be asking around for notes for no reason. "
            msc " That's because I told them they're going to have a test on monday! "
            msc " Which means, they're going to need all the notes they can get to study. "
            msc " No notes means no studying, after all! "
            msc " Atleast that's how I see it. "
            msc " Hopefully I won't see any students just slacking off... "
            msc " Because they really need to study hard for this test! "
            msc " I saw some students not paying attention, so... "
            msc " That's why I decided to test them in the first place! "
            msc " I doubt they could even memorize all the things they studied about, now that I think about it... "
            msc " But a little too late to regret things now. "
            msc " I already gave them the activity after all! "
            msc " I can't just go back on that as a teacher... "
            msc " Oh well, just hopefully at monday... "
            msc " ...There's going to be atleast 5 people that passed. "
            msc " Even better if theres 10 people and above! "
            msc " Hopefully that happens, hmhm. "
            msc " But you know what they say... "
            msc " Don't put your expectations high for certain things! "
            msc " You're only preparing yourself for disappointment that way! "
            msc " ...Atleast that's what I think that they say. "
            scene black with dissolve
            " You spent the class hours talking to Miss Circle. "
            " Now that she mentioned giving one of her students candy... "
            " You're kind of craving chocolates right now. "
            play sound "audio/bellring.mp3"
            " Looks like it's time for a break. "
            " You waited for everyone to get out of the class before you did. "
            pause 2.0
            jump tfbreak3
        else:
            x " Hey there, [name]! "
            $ circleknow = True
            msc " Miss Circle, by the way. Math teacher. "
            msc " I was just watching over my students. "
            msc " Hmhmmm... "
            msc " Looks like they're actually asking eachother for notes! "
            msc " I like the fact that they aren't slacking off for once. "
            msc " Looks like Engel's the one that's being asked the most, hehe. "
            msc " Of course he would be - he's the star student! "
            msc " He's got all the notes and everything... "
            msc " Impressive that he could pick up with my speed, honestly. "
            msc " Should probably give him some snacks for that... "
            msc " Maybe some of the candy that I have in my drawer? "
            " You said thought that Engel would like some candy. "
            " But then again, some students are going to start asking from you a whole lot. "
            " If you want to reward him, then just give him some plus points for now. "
            " But when no one's looking? give him some chocolate. "
            hide misscircleneutral at bottom
            show misscirclehappy at center
            msc " Hm, good point and good idea! "
            msc " Always appreciate you giving good ideas to us like these, [name]. "
            msc " Really helps, you know? "
            msc " Even though this one's just for candy. "
            hide misscirclehappy at bottom
            show misscircleneutral at center
            " You just nodded in response. "
            " You then asked her why her students were asking for notes... "
            " I mean, they can't be asking around for notes for no reason. "
            msc " That's because I told them they're going to have a test on monday! "
            msc " Which means, they're going to need all the notes they can get to study. "
            msc " No notes means no studying, after all! "
            msc " Atleast that's how I see it. "
            msc " Hopefully I won't see any students just slacking off... "
            msc " Because they really need to study hard for this test! "
            msc " I saw some students not paying attention, so... "
            msc " That's why I decided to test them in the first place! "
            msc " I doubt they could even memorize all the things they studied about, now that I think about it... "
            msc " But a little too late to regret things now. "
            msc " I already gave them the activity after all! "
            msc " I can't just go back on that as a teacher... "
            msc " Oh well, just hopefully at monday... "
            msc " ...There's going to be atleast 5 people that passed. "
            msc " Even better if theres 10 people and above! "
            msc " Hopefully that happens, hmhm. "
            msc " But you know what they say... "
            msc " Don't put your expectations high for certain things! "
            msc " You're only preparing yourself for disappointment that way! "
            msc " ...Atleast that's what I think that they say. "
            scene black with dissolve
            " You spent the class hours talking to Miss Circle. "
            " Now that she mentioned giving one of her students candy... "
            " You're kind of craving chocolates right now. "
            play sound "audio/bellring.mp3"
            " Looks like it's time for a break. "
            " You waited for everyone to get out of the class before you did. "
            pause 2.0
            jump tfbreak3
    label uhthavel:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom and prayed they weren't doing anything important... "
        " And wow, gee...they weren't doing anything important. "
        " The students were just answering something in their notebooks. "
        " You looked around to spot where the language teacher is... "
        " And found her at the very back of the class. "
        " You walked over to her and stood right next to her. "
        " Let's see what she's thinking about... "
        show msthravelneutral at center with easeinleft
        if thavelknow == True:
            mst " Hola, [name]! "
            mst " I'm just watching over my students right now! "
            mst " Gave them something to answer, hehe. "
            mst " Kinda felt like giving myself a break from teaching them for now. "
            mst " Like, talking and all of that stuff. "
            mst " That's why I made them answer something! "
            mst " Talking in front can be a pain, you know... "
            mst " Like, there can be students who don't pay attention... "
            mst " Students talking to eachother... "
            mst " Students just sleeping in their chairs... "
            mst " And all you want is for everyone to listen to you. "
            mst " You also know that they won't listen to you easily if you just yell at them. "
            mst " People don't learn that quick, after all! "
            mst " So... "
            mst " The thing you can do here is just give them a test. "
            mst " Any kind of test, really... "
            mst " As long as it's hard enough to the point it makes the people who haven't studied; bamboozled. "
            mst " It's a little unfair, yes... "
            mst " But is it my fault that they chose not to listen? "
            mst " Not listening was completely their choice. "
            mst " It's only fair if I give them something to answer to test their 'knowledge'... "
            mst " ...If they didn't listen at all. "
            mst " Do you get what I'm getting at here, [name]? "
            mst " Some people may call me unfair, but really... "
            mst " You'd probably do the same if you were in my shoes. "
            mst " Even though I'm kind of praying for their downfall... "
            mst " I'm still hoping that some would get a high score. "
            mst " Just some. "
            mst " Knowing some of my students are failures is fun and not fun at the same time. "
            mst " Fun because you get to see them suffer... "
            mst " But that means you'd have to deal with their bullshit for longer. "
            mst " And if you have to deal with that... "
            mst " Then you'd have to deal with trying to get them to pass their missing requirements. "
            mst " Which is really annoying as hell, in all honesty. "
            mst " Because some would just forget about all of their missing requirements... "
            mst " Even though I've told them about it a whole lot of times. "
            mst " It really gets under my skin. "
            mst " Sighhh... "
            mst " ... "
            " Looks like she doesn't have anything else to say. "
            " Time for some nice silence... "
            scene black with dissolve
            " You spent the rest of the class hours just chilling with Miss Thavel. "
            " Just standing there in silence.. "
            " And also watching over her students. "
            play sound "aduio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone else to get out of the classroom before you went out. "
            pause 2.0
            jump tfbreak3
        else:
            x " Hola, [name]! "
            $ thavelknow = True
            mst " I'm Miss Thavel, by the way. The language teacher! "
            mst " I'm just watching over my students right now! "
            mst " Gave them something to answer, hehe. "
            mst " Kinda felt like giving myself a break from teaching them for now. "
            mst " Like, talking and all of that stuff. "
            mst " That's why I made them answer something! "
            mst " Talking in front can be a pain, you know... "
            mst " Like, there can be students who don't pay attention... "
            mst " Students talking to eachother... "
            mst " Students just sleeping in their chairs... "
            mst " And all you want is for everyone to listen to you. "
            mst " You also know that they won't listen to you easily if you just yell at them. "
            mst " People don't learn that quick, after all! "
            mst " So... "
            mst " The thing you can do here is just give them a test. "
            mst " Any kind of test, really... "
            mst " As long as it's hard enough to the point it makes the people who haven't studied; bamboozled. "
            mst " It's a little unfair, yes... "
            mst " But is it my fault that they chose not to listen? "
            mst " Not listening was completely their choice. "
            mst " It's only fair if I give them something to answer to test their 'knowledge'... "
            mst " ...If they didn't listen at all. "
            mst " Do you get what I'm getting at here, [name]? "
            mst " Some people may call me unfair, but really... "
            mst " You'd probably do the same if you were in my shoes. "
            mst " Even though I'm kind of praying for their downfall... "
            mst " I'm still hoping that some would get a high score. "
            mst " Just some. "
            mst " Knowing some of my students are failures is fun and not fun at the same time. "
            mst " Fun because you get to see them suffer... "
            mst " But that means you'd have to deal with their bullshit for longer. "
            mst " And if you have to deal with that... "
            mst " Then you'd have to deal with trying to get them to pass their missing requirements. "
            mst " Which is really annoying as hell, in all honesty. "
            mst " Because some would just forget about all of their missing requirements... "
            mst " Even though I've told them about it a whole lot of times. "
            mst " It really gets under my skin. "
            mst " Sighhh... "
            mst " ... "
            " Looks like she doesn't have anything else to say. "
            " Time for some nice silence... "
            scene black with dissolve
            " You spent the rest of the class hours just chilling with Miss Thavel. "
            " Just standing there in silence.. "
            " And also watching over her students. "
            play sound "aduio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone else to get out of the classroom before you went out. "
            pause 2.0
            jump tfbreak3
    label uhbloomie:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the science teacher's classroom. "
        " Looks like nothing important is really going on... "
        " The science teacher was just letting her students copy down some notes on a powerpoint presentation. "
        " A student is taking care of the powerpoint presentation and skipping to other slides... "
        " Seems like the teacher wanted a break. "
        " You looked around and found the science teacher sitting down at the back of the class. "
        " Wondering what she's doing, you walked over to her and took a seat next to her. "
        show missbloomieneutral at center with easeinleft
        if bloomieknow == True:
            msb " ...Hello there, [name]. "
            msb " I'm just.. "
            msb " ...Look. "
            msb " I don't really want to seem lazy right now, but... "
            msb " I just want a break for now. "
            msb " Working tirelessly as a teacher... "
            msb " Having students who are stubborn... "
            msb " It really tires you out. "
            msb " That's why I want to take a break right now... "
            msb " Just to relax for a good bit. "
            msb " I'm sure I'll be fine for my next class with this. "
            msb " ... "
            " Looks like she has nothing else to say... "
            " As much as you don't want to be lazy... "
            " You lowkey wanted to take a good break too. "
            " Being a teacher is not easy. "
            " You just took this time to relax for a good bit. "
            " You didn't try talking to Miss Bloomie as you two were relaxing. "
            " You both needed a break, after all. "
            scene black with dissolve
            " You spent the rest of the class hours just relaxing in the chair that you had. "
            " Just relaxing with Miss Bloomie... "
            " You honestly felt like you could fall asleep at this time. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for a break. "
            " You waited for everyone in the classroom to leave before you did. "
            pause 2.0
            jump tfbreak3
        else:
            x " ...Hello there, [name]. "
            $ bloomieknow = True
            msb " I'm, uh...Miss Bloomie. Science teacher. "
            msb " I'm just.. "
            msb " ...Look. "
            msb " I don't really want to seem lazy right now, but... "
            msb " I just want a break for now. "
            msb " Working tirelessly as a teacher... "
            msb " Having students who are stubborn... "
            msb " It really tires you out. "
            msb " That's why I want to take a break right now... "
            msb " Just to relax for a good bit. "
            msb " I'm sure I'll be fine for my next class with this. "
            msb " ... "
            " Looks like she has nothing else to say... "
            " As much as you don't want to be lazy... "
            " You lowkey wanted to take a good break too. "
            " Being a teacher is not easy. "
            " You just took this time to relax for a good bit. "
            " You didn't try talking to Miss Bloomie as you two were relaxing. "
            " You both needed a break, after all. "
            scene black with dissolve
            " You spent the rest of the class hours just relaxing in the chair that you had. "
            " Just relaxing with Miss Bloomie... "
            " You honestly felt like you could fall asleep at this time. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for a break. "
            " You waited for everyone in the classroom to leave before you did. "
            pause 2.0
            jump tfbreak3
label tfbreak3:
    scene hallway with dissolve
    " You walked around the hallways looking around for something to do. "
    " Just wandering and wandering... "
    " Jeez, nothing interesting is really catching your eye right now. "
    " Maybe you should go and look at your phone? "
    " Something interesting is always happening online, after all. "
    " But, nah... "
    " You should take a break from your phone every now and then. "
    " Can't always be looking at it. "
    " Hm...what to do, what to do... "
    " As you were thinking of what you should do for this break, you spotted something at the corner of your eye... "
    " You were just on your way to the back of the school, and you spotted a student doing something.. "
    " What was that something, you may ask? "
    " They were smoking, that's what they were doing. "
    " You should definitely do something about that. "
    " Take that cigarette away, and have a nice talk with them... "
    " And maybe take them to the principal's office if they react violently. "
    " They probably need someone to talk to. "
    " Just your guess though. "
    " You walked over to that student and took away their cigarette and threw it into the trash can.. "
    " Let's see if you can help them out. "
    scene black with dissolve
    " You spent the rest of the break having a nice and long talk with a student. "
    " Talking to them gently about not smoking in school... "
    " And also talking to them about what's been going on in their life. "
    " And you were right, something was definitely going on back at home. "
    " You told them that everything was going to be alright after a good bit. "
    " They just had to live out this part of life for a good bit. "
    " The cruel part of life. "
    " You decided to call Miss Grace about that situation after you were done. "
    " She said that she'll look into it. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for you to help someone else. "
    " Let's see who you can help this time... "
    pause 2.0
    jump tfhelp4
label tfhelp4:
    scene hallway with dissolve
    " Looks like it's time for you to help someone right now. "
    " Who do you want to help for this break? "
    if emilyknow,demiknow,sashaknow == True:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump laidbackintime
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump depthsofadream
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump driftingdrifting
    elif emilyknow,demiknow == True and sashaknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump laidbackintime
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump depthsofadream
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump driftingdrifting
    elif emilyknow,sashaknow == True and demiknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump laidbackintime
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump depthsofadream
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump driftingdrifting
    elif demiknow,sashaknow == True and emilyknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump laidbackintime
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump depthsofadream
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump driftingdrifting
    elif emilyknow == True and demiknow,sashaknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump laidbackintime
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump depthsofadream
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump driftingdrifting
    elif demiknow == True and emilyknow,sashaknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump laidbackintime
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump depthsofadream
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump driftingdrifting
    elif sashaknow == True and emilyknow,demiknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump laidbackintime
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump depthsofadream
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump driftingdrifting
    else:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump laidbackintime
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump depthsofadream
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump driftingdrifting
    label laidbackintime:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the history teacher's classroom... "
        " Looks like they aren't really doing anything important. "
        " Just the students answering a few things again... "
        " You looked around to find the teacher sitting infront of the class. "
        " You grabbed an empty seat and took a seat next to her. "
        show msemilyneutral at center with easeinleft
        if emilyknow == True:
            mse " Hmhm... "
            mse " Let's see...what should I do for the weekends? "
            mse " I could go on a run tomorrow... "
            mse " A run around the park would be good. "
            " You asked her politely on what she was doing. "
            mse " Oh! hey there, [name]! "
            mse " I was just uh...talking to myself. "
            mse " Does that sound weird? talking to yourself? "
            mse " ...I guess not really - some people still do that kind of stuff. "
            mse " But I was just talking about going on a walk around the park. "
            mse " You know...that park near this school? "
            mse " It's a good space to take a nice walk around! "
            mse " And not only that... "
            mse " But it's also a nice place to look at!! "
            mse " Like, I don't know if you've ever actually been there, but... "
            mse " The flowers are really nice to see there! "
            mse " And also, that lake at the very back of it... "
            mse " It's just the perfect place to hangout in! "
            mse " And, uh... "
            hide msemilyneutral at bottom
            show msemilyshock at center
            mse " Look, don't tell anyone I told you this, but... "
            mse " I've actually seen a few people do...other things there. "
            mse " Like hugging, cuddling... "
            mse " A whole lot more stuff that I wouldn't like to mention. "
            mse " I've actually been there last week sunday, and uh... "
            mse " Okay, let me tell you a story. "
            hide msemilyshock at bottom
            show msemilyneutral at center
            mse " So...while I was walking around in the park. "
            mse " I wanted to take a small break at that lake part I mentioned. "
            mse " So I went there and sat down on the ground, looked at the water... "
            mse " And then I hear some talking nearby. "
            mse " I was trying to ignore it, buuut... "
            mse " I couldn't really help myself. "
            mse " So, I listened into what they were talking about. "
            mse " At first, they were being all lovey dovey... "
            mse " Normal couple things, you know? "
            mse " I was about to ignore them and put on my headsets, but... "
            mse " They started talking about something that interested me. "
            mse " Something about the other's contacts on their phone. "
            mse " Looks like the other person saw someone unknown on their partners phone. "
            mse " It sounded interesting, so I continued listening. "
            mse " And the more I listened... "
            hide msemilyneutral at bottom
            show msemilysad at center
            mse " The more violent they got with their conversation. "
            mse " Thinking of what they're saying... "
            mse " It really breaks my heart, you know? "
            mse " I know couples are meant to have their fights every now and then, but... "
            mse " It still makes me feel upset. "
            mse " Sigh... "
            mse " Hearing people fight kind of upsets me. "
            mse " But, whatever happens, happens. "
            mse " Can't really just step in and tell them to stop fighting... "
            mse " Since, you know...I'm a stranger to them. "
            mse " But, erhhh...I still wish that I could do something. "
            mse " Hmhmmm... "
            hide msemilysad at bottom
            show msemilyneutral at center
            mse " But other than that sad story... "
            mse " I've had a good time relaxing there. "
            mse " I just wish that people would stop being so loud there... "
            mse " Like, no...you're not the only ones here. "
            mse " There still might be some people wandering around. "
            mse " It IS a park, after all. "
            scene black with dissolve
            " You spent the rest of the break talking with Miss Emily. "
            " Just talking with her... "
            " It felt pretty calming, in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for a break. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak4
        else:
            x " Hmhm... "
            x " Let's see...what should I do for the weekends? "
            x " I could go on a run tomorrow... "
            x " A run around the park would be good. "
            " You asked her politely on what she was doing. "
            x " Oh! hey there, [name]! "
            $ emilyknow = True
            mse " I'm Miss Emily, by the way. History teacher. "
            mse " I was just uh...talking to myself. "
            mse " Does that sound weird? talking to yourself? "
            mse " ...I guess not really - some people still do that kind of stuff. "
            mse " But I was just talking about going on a walk around the park. "
            mse " You know...that park near this school? "
            mse " It's a good space to take a nice walk around! "
            mse " And not only that... "
            mse " But it's also a nice place to look at!! "
            mse " Like, I don't know if you've ever actually been there, but... "
            mse " The flowers are really nice to see there! "
            mse " And also, that lake at the very back of it... "
            mse " It's just the perfect place to hangout in! "
            mse " And, uh... "
            hide msemilyneutral at bottom
            show msemilyshock at center
            mse " Look, don't tell anyone I told you this, but... "
            mse " I've actually seen a few people do...other things there. "
            mse " Like hugging, cuddling... "
            mse " A whole lot more stuff that I wouldn't like to mention. "
            mse " I've actually been there last week sunday, and uh... "
            mse " Okay, let me tell you a story. "
            hide msemilyshock at bottom
            show msemilyneutral at center
            mse " So...while I was walking around in the park. "
            mse " I wanted to take a small break at that lake part I mentioned. "
            mse " So I went there and sat down on the ground, looked at the water... "
            mse " And then I hear some talking nearby. "
            mse " I was trying to ignore it, buuut... "
            mse " I couldn't really help myself. "
            mse " So, I listened into what they were talking about. "
            mse " At first, they were being all lovey dovey... "
            mse " Normal couple things, you know? "
            mse " I was about to ignore them and put on my headsets, but... "
            mse " They started talking about something that interested me. "
            mse " Something about the other's contacts on their phone. "
            mse " Looks like the other person saw someone unknown on their partners phone. "
            mse " It sounded interesting, so I continued listening. "
            mse " And the more I listened... "
            hide msemilyneutral at bottom
            show msemilysad at center
            mse " The more violent they got with their conversation. "
            mse " Thinking of what they're saying... "
            mse " It really breaks my heart, you know? "
            mse " I know couples are meant to have their fights every now and then, but... "
            mse " It still makes me feel upset. "
            mse " Sigh... "
            mse " Hearing people fight kind of upsets me. "
            mse " But, whatever happens, happens. "
            mse " Can't really just step in and tell them to stop fighting... "
            mse " Since, you know...I'm a stranger to them. "
            mse " But, erhhh...I still wish that I could do something. "
            mse " Hmhmmm... "
            hide msemilysad at bottom
            show msemilyneutral at center
            mse " But other than that sad story... "
            mse " I've had a good time relaxing there. "
            mse " I just wish that people would stop being so loud there... "
            mse " Like, no...you're not the only ones here. "
            mse " There still might be some people wandering around. "
            mse " It IS a park, after all. "
            scene black with dissolve
            " You spent the rest of the break talking with Miss Emily. "
            " Just talking with her... "
            " It felt pretty calming, in your opinion. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for a break. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak4
    label depthsofadream:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the music teacher's classroom. "
        " Looks like they still aren't doing anything important... "
        " Just answering certain things on their papers. "
        " You looked around and saw the music teacher cleaning a few corners up. "
        " Maybe you could help in cleaning with him... "
        " You walked over to him to check what you could do. "
        show mrdemineutral at center with easeinleft
        if demiknow == True:
            msd " Just a few corners here... "
            msd " Hmhmm... "
            msd " Gosh, these corners are really dusty... "
            msd " I should probably clean this room more. "
            msd " If it's so dirty like this... "
            msd " I should probably ask the janitor to clean a bit more. "
            msd " But, if I want them to clean more... "
            msd " I should atleast pay them a little bit. "
            msd " Even if they deny it at first. "
            msd " I want them to be paid well.. "
            msd " I know that they don't really get paid well, so.. "
            msd " I should pay them atleast 50$. "
            msd " That's the least I could do... "
            " You poked his shoulder so that you could get his attention. "
            " Then, you politely asked him what he was doing. "
            hide mrdemineutral at bottom
            show mrdemisurprised at center
            msd " ...Eeek!! "
            " Well, looks like you scared him a little. "
            " Oopsies. "
            msd " Oh, it's just you...[name]... "
            hide mrdemisurprised at bottom
            show mrdemineutral at center
            msd " I was just cleaning around the corners of the room... "
            msd " I noticed how everything was dirty, so I... "
            msd " I decided to clean... "
            msd " Uh... "
            msd " I wasn't talking to myself too loudly, was I...? "
            msd " Sorry if I was bothering you a little...from, you know... "
            msd " From me talking to myself... "
            msd " Now that I think about it.. "
            msd " I think I was being a little too loud... "
            msd " A little too loud to the point that my students might've heard me... "
            msd " Oopsies... "
            msd " I didn't mean to do that... "
            " You told him that he was fine. "
            " He wasn't talking too loudly or anything... "
            " He was just speaking out his thoughts. "
            " You also found it really nice that he wanted to pay the janitor. "
            msd " ...Well... "
            msd " It's the least I could do, you know... "
            msd " They're cleaning so much... "
            msd " I don't think they even get paid for their hard work. "
            msd " Well, they do, but... "
            msd " I know that they would get paid only so little. "
            msd " Sigh... "
            " Huh. Now you're feeling a little bad for the janitor. "
            " The students kind of throw a whole lot of trash on the ground... "
            " Imagine having to clean a whole lot of that every day. "
            " Must be really tiring... "
            " Before you could get even more lost into your thoughts, "
            " You asked Mister Demi if you could help in cleaning around a bit. "
            msd " Oh, you... "
            msd " ...You want to help me...? "
            msd " Are you sure it won't be too boring for you? "
            " You nodded. "
            " Atleast it gives you something to do to pass the time. "
            " And it's also somewhat productive, too. "
            msd " ...Okay... "
            msd " You can clean this corner, then... "
            msd " I can clean the other corner over there... "
            scene black with dissolve
            " You spent the rest of the period cleaning with Mister Demi. "
            " Just cleaning here and there... "
            " He was right, these corners were pretty dusty and dirty. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone to leave before you did. "
            pause 2.0
            jump tfbreak4
        else:
            x " Just a few corners here... "
            x " Hmhmm... "
            x " Gosh, these corners are really dusty... "
            x " I should probably clean this room more. "
            x " If it's so dirty like this... "
            x " I should probably ask the janitor to clean a bit more. "
            x " But, if I want them to clean more... "
            x " I should atleast pay them a little bit. "
            x " Even if they deny it at first. "
            x " I want them to be paid well.. "
            x " I know that they don't really get paid well, so.. "
            x " I should pay them atleast 50$. "
            x " That's the least I could do... "
            " You poked his shoulder so that you could get his attention. "
            " Then, you politely asked him what he was doing. "
            hide mrdemineutral at bottom
            show mrdemisurprised at center
            x " ...Eeek!! "
            " Well, looks like you scared him a little. "
            " Oopsies. "
            x " Oh, it's just you...[name]... "
            hide mrdemisurprised at bottom
            show mrdemineutral at center
            $ demiknow = True
            msd "I'm um...Mister Demi, by the way. "
            msd " I was just cleaning around the corners of the room... "
            msd " I noticed how everything was dirty, so I... "
            msd " I decided to clean... "
            msd " Uh... "
            msd " I wasn't talking to myself too loudly, was I...? "
            msd " Sorry if I was bothering you a little...from, you know... "
            msd " From me talking to myself... "
            msd " Now that I think about it.. "
            msd " I think I was being a little too loud... "
            msd " A little too loud to the point that my students might've heard me... "
            msd " Oopsies... "
            msd " I didn't mean to do that... "
            " You told him that he was fine. "
            " He wasn't talking too loudly or anything... "
            " He was just speaking out his thoughts. "
            " You also found it really nice that he wanted to pay the janitor. "
            msd " ...Well... "
            msd " It's the least I could do, you know... "
            msd " They're cleaning so much... "
            msd " I don't think they even get paid for their hard work. "
            msd " Well, they do, but... "
            msd " I know that they would get paid only so little. "
            msd " Sigh... "
            " Huh. Now you're feeling a little bad for the janitor. "
            " The students kind of throw a whole lot of trash on the ground... "
            " Imagine having to clean a whole lot of that every day. "
            " Must be really tiring... "
            " Before you could get even more lost into your thoughts, "
            " You asked Mister Demi if you could help in cleaning around a bit. "
            msd " Oh, you... "
            msd " ...You want to help me...? "
            msd " Are you sure it won't be too boring for you? "
            " You nodded. "
            " Atleast it gives you something to do to pass the time. "
            " And it's also somewhat productive, too. "
            msd " ...Okay... "
            msd " You can clean this corner, then... "
            msd " I can clean the other corner over there... "
            scene black with dissolve
            " You spent the rest of the period cleaning with Mister Demi. "
            " Just cleaning here and there... "
            " He was right, these corners were pretty dusty and dirty. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone to leave before you did. "
            pause 2.0
            jump tfbreak4
    label driftingdrifting:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the art teacher's classroom. "
        " Looks like they were doing some painting this time... "
        " You don't know what they're painting about, but it looked cool. "
        " You looked around and spotted the art teacher arranging a few things. "
        " Let's see if you can help with that. "
        " You walked over to her after a good bit of looking around. "
        show sashaneutral at center with easeinleft
        if sashaknow == True:
            mss " Let's see here... "
            mss " Does the painting look good on this side, or on this side? "
            mss " Maybe it should move a little to the left... "
            mss " Hm. Still doesn't look too right. "
            mss " Oh! maybe I should move it to the right, then? "
            mss " ...No, still doesn't look too right. "
            hide sashaneutral at bottom
            show sashasad at center
            mss " Dangit, who knew placement could be so hard!! "
            mss " Maybe I should just put this at the back?? "
            mss " But it would be too much of a waste... "
            mss " It looks really good, too!! "
            mss " It's alright, Sasha... "
            mss " You've just gotta find the right placement for this painting... "
            mss " Even though it's going to be a little hard to do... "
            mss " I just need to... "
            mss " Find the right position for this painting... "
            hide sashasad at bottom
            show sashaneutral at center
            " You poked her to get her attention. "
            " You were about to ask her what she was doing, but... "
            " Looks like you scared her a little. "
            " Maybe you should stop poking people like that... "
            mss " Eh? - "
            mss " Oh, hey there, [name] - woah! "
            mss " Wait, hold on... "
            hide sashaneutral at bottom
            show sashahappy at center
            mss " Hey, wait! "
            mss " Looks like you pushed me a little to the point the painting got to a position that I like! "
            mss " Could you help me hold the painting still for a bit? "
            mss " Just hold it down by the sides like this... "
            " You hold the painting down for Miss Sasha. "
            " Then she gets ready to actually put the painting in place with the wall. "
            " It took her a bit, before she eventually got it. "
            mss " Woah, it looks so nice!! "
            mss " You can let go of it now, by the way. "
            hide sashahappy at bottom
            show sashaneutral at center
            mss " Actually, before this... "
            mss " I was just planning to put ups some of my students works on the walls! "
            mss " And for the other ones that can't be put on the walls... "
            mss " I'll put them on the empty shelves over here! "
            mss " And, now that you're here... "
            mss " Maybe you could help me? "
            mss " There's a whole lot of stuff in the boxes over there... "
            mss " And honestly? I don't want to spend all break doing this! "
            mss " So, if you're fine with it... "
            mss " Could you help me on this? "
            mss " It's completely fine if you don't want to! "
            " You DID come in here to help... "
            " You agreed on helping her. "
            mss " Thanks, [name]! "
            mss " I can always count on you, hehe... "
            mss " Here, let me grab the box of arts and stuff... "
            mss " It's a bit heavy, but I can handle it! "
            scene black with dissolve
            " You spent the rest of the class hours helping Miss Sasha. "
            " Whilst you were helping her, you were also talking a bit with her. "
            " Mostly about the works of the kids that you were help putting up. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone to get outside of the classroom before you did. "
            pause 2.0
            jump tfbreak4
        else:
            x " Let's see here... "
            x " Does the painting look good on this side, or on this side? "
            x " Maybe it should move a little to the left... "
            x " Hm. Still doesn't look too right. "
            x " Oh! maybe I should move it to the right, then? "
            x " ...No, still doesn't look too right. "
            hide sashaneutral at bottom
            show sashasad at center
            x " Dangit, who knew placement could be so hard!! "
            x " Maybe I should just put this at the back?? "
            x " But it would be too much of a waste... "
            x " It looks really good, too!! "
            x " It's alright, Sasha... "
            x " You've just gotta find the right placement for this painting... "
            x " Even though it's going to be a little hard to do... "
            x " I just need to... "
            x " Find the right position for this painting... "
            hide sashasad at bottom
            show sashaneutral at center
            " You poked her to get her attention. "
            " You were about to ask her what she was doing, but... "
            " Looks like you scared her a little. "
            " Maybe you should stop poking people like that... "
            x " Eh? - "
            x " Oh, hey there, [name] - woah! "
            x " Wait, hold on... "
            hide sashaneutral at bottom
            show sashahappy at center
            x " Hey, wait! "
            x " Looks like you pushed me a little to the point the painting got to a position that I like! "
            x " Could you help me hold the painting still for a bit? "
            x " Just hold it down by the sides like this... "
            " You hold the painting down for her. "
            " Then she gets ready to actually put the painting in place with the wall. "
            " It took her a bit, before she eventually got it. "
            x " Woah, it looks so nice!! "
            x " You can let go of it now, by the way. "
            hide sashahappy at bottom
            show sashaneutral at center
            $ sashaknow = True
            mss " Oh, uh...right! I'm Miss Sasha! art teacher! "
            mss " Actually, before this... "
            mss " I was just planning to put ups some of my students works on the walls! "
            mss " And for the other ones that can't be put on the walls... "
            mss " I'll put them on the empty shelves over here! "
            mss " And, now that you're here... "
            mss " Maybe you could help me? "
            mss " There's a whole lot of stuff in the boxes over there... "
            mss " And honestly? I don't want to spend all break doing this! "
            mss " So, if you're fine with it... "
            mss " Could you help me on this? "
            mss " It's completely fine if you don't want to! "
            " You DID come in here to help... "
            " You agreed on helping her. "
            mss " Thanks, [name]! "
            mss " I can always count on you, hehe... "
            mss " Here, let me grab the box of arts and stuff... "
            mss " It's a bit heavy, but I can handle it! "
            scene black with dissolve
            " You spent the rest of the class hours helping Miss Sasha. "
            " Whilst you were helping her, you were also talking a bit with her. "
            " Mostly about the works of the kids that you were help putting up. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone to get outside of the classroom before you did. "
            pause 2.0
            jump tfbreak4
label tfbreak4:
    scene hallway with dissolve
    " You walked around the hallways after you were done helping a teacher. "
    " Looks like it's your class that's next... "
    " Probably should prepare for that. "
    " But then again, you're always prepared. "
    " Not really, but the narrator says what they say. "
    " You continued wandering around the halls... "
    " You caught some students bullying some guy as you were walking. "
    " You quickly went over to them and stopped the bullying. "
    " Those students were pretty familiar to you... "
    " Infact, they looked like students from your class. "
    " You should keep an eye on them. "
    " You don't want them causing trouble in your class at all. "
    " And more importantly... "
    " You didn't want them to be bullying any other students. "
    " Not on your watch, no. "
    " If you did catch them bullying again... "
    " You're going to have to send them to the principal. "
    " That's for sure. "
    " You then made sure the other student was okay. "
    " Luckily, just some bruises and no fatal injuries. "
    " You told them to go to the school's clinic to get patched up a bit. "
    " You then continued roaming around the school. "
    scene black with dissolve
    " You spent the rest of the break just wandering and wandering around your school... "
    " Every now and then, you'd see those bullies you encountered earlier. "
    " Thankfully they weren't doing anything funny, but... "
    " You just decided to give them the stink eye to let them know that you're watching. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for your class. "
    " You walked on over to your classroom... "
    pause 2.0
    jump tfmcclass
label tfmcclass:
    scene gardenroom with dissolve
    " You walked into your classroom and found all of your students already there. "
    " Impressive... "
    " You're the one that's sort of late this time. "
    " Well, not really. "
    " You arrived one minute early. "
    " That's not really being late... "
    " Anyway, enough talking. "
    " You greeted your students. "
    " They greeted you back politely. "
    " You walked to the front of your classroom and got ready to teach them about plants... "
    " Time for you to start your lesson. "
    scene black with dissolve
    " You taught your students about other things about planting. "
    " You ARE the gardening teacher, after all. "
    " You explained things very easily so that they could get a good idea... "
    " And it seems that everyone got a pretty nice idea of what they should study about. "
    " You're happy with that. "
    play sound "audio/bellring.mp3"
    " The bell rings, time for another break. "
    " You waited for all of your students to get out before you did. "
    pause 2.0
    jump tfbreak5
label tfbreak5:
    scene hallway with dissolve
    " You walked out of your classroom after your students left. "
    " Looks like it's time for you to wander the hallway again... "
    " Time to make sure no one's doing anything mischevious. "
    " If you did let someone do something mischevious without your permission... "
    " You just knew that you were going to get an earful from Miss Grace. "
    " As you were walking around... "
    " You caught a student trying to sneak into the teachers office. "
    " Immediately, you yoinked them. "
    " What could they want from the teachers office? "
    " Probably trying to steal test answers. "
    " Like in that one game that's kinda controversial... "
    " Eeeyikes. Let's not talk about that game. "
    " They told you that they were having a talk with one of the teachers in there earlier... "
    " And told you that they had left something in there. "
    " That something being their phone. "
    " You told them that they could get in, BUT... "
    " You're going to have to keep an eye on them. "
    " You didn't want them to steal anything important, after all. "
    " Without further a do, you walked into the teachers office with them... "
    scene black with dissolve
    " You spent the rest of the break watching over a student in the teachers office. "
    " They looked like they were struggling hard... "
    " You decided to help them after a bit. "
    " Of course you did this while keeping an eye on them. "
    " Just making sure that they didn't do anything stupid... "
    " The moment they found their phone, you yoinked them out. "
    " Had to remind them that they can't always get in there. "
    " You then continued to walk around the school. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for you to help some more teachers. "
    " You walked around and looked for people who were struggling... "
    pause 2.0
    jump tfhelp6
label tfhelp6:
    # circle, bloomie, thavel end
    scene hallway with dissolve
    " Looks like it's time to help someone again. "
    " Who do you help for this break? "
    if circleknow,thavelknow,bloomieknow == True:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump howigotthisway
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump waythisgotihow
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump millieyay
    elif circleknow,thavelknow == True and bloomieknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump howigotthisway
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump waythisgotihow
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump millieyay
    elif circleknow,bloomieknow == True and thavelknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump howigotthisway
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump waythisgotihow
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump millieyay
    elif thavelknow,bloomieknow == True and circleknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump howigotthisway
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump waythisgotihow
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump millieyay
    elif circleknow == True and thavelknow,bloomieknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump howigotthisway
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump waythisgotihow
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump millieyay
    elif thavelknow == True and circleknow,bloomieknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump howigotthisway
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump waythisgotihow
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump millieyay
    elif bloomieknow == True and circleknow,thavelknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump howigotthisway
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump waythisgotihow
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump millieyay
    else:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump howigotthisway
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump waythisgotihow
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump millieyay
    label howigotthisway:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the math teachers room... "
        " Looks like they aren't doing anything productive here, either. "
        " Just the students doing the productive stuff... "
        " But not the teacher, apparently. "
        " The teachers just sitting there infront of class. "
        if circlelv <= 20:
            " Looks like you shouldn't bother her right now, actually. "
            " Maybe you could do something else while you're here? "
            " Maybe you should clean around, the room does look a bit dusty after all. "
            scene black with dissolve
            " You spent the rest of the class hours cleaning the math teachers room. "
            " And with your help, it looked just a bit cleaner. "
            " Nice one. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone else to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak6
        else:
            pass
        show misscircleneutral at center with easeinleft
        if circleknow == True:
            pause 0.1
            if circlelv >= 20 or circlelv == 20:
                msc " Oh, [name]!! "
                msc " I've been actually thinking of talking to you. "
                msc " Like, a lot. "
                " You asked what she wanted to talk to you about. "
                " You seemed pretty curious now... "
                msc " Well, I don't think the class would like to hear this, buuuut... "
                msc " It's nothing too serious, anyway. "
                msc " It should be fine if I talk to you right now! "
                msc " Besides... "
                msc " They're all focusing on their work right now anyways. "
                msc " So... "
                msc " I've been thinking of asking you something for awhile now. "
                msc " We've been getting a bit close, actually! "
                msc " Even though all you've been doing is just helping me out... "
                msc " I've been really enjoying our time together. "
                msc " Like, a lot. "
                msc " And I admit... "
                msc " I sometimes wish that I would talk with you more. "
                msc " And uh...I don't know if this is gonna sound weird to you, but... "
                msc " I would like to ask you something. "
                msc " Would you like to be best friends with me? "
                msc " I don't ask a lot of people this question, by the way. "
                msc " It's fine if you don't want to be that way yet, "
                msc " I know it's a really sudden question. "
                msc " It's fine if you just want to stay as normal friends for now. "
                msc " So, uh...what do you say? "
                menu:
                    " Give me oreos first ":
                        $ circlesend.grant()
                        hide misscircleneutral at bottom
                        show misscirclehappy at center
                        msc " Hehe, wow.... "
                        msc " Asking for oreos? alrighty... "
                        msc " Here you go. "
                        msc " Just cause I want you to be my best friend. "
                        msc " This doesn't mean that I'll give you oreos 24/7 though. "
                        scene circleend with dissolve
                        " Congratulations, you've gotten Miss Circle's ending! "
                        " And also her achievement. Check your achievements tab! "
                        " She may not share oreos with you all the time... "
                        " But she will. Only sometimes though. "
                        jump credits
                    " Normal friends please ":
                        msc " Well, alrighty. "
                        msc " Understandable. "
                        msc " How about we talk about something else? "
                        msc " Don't want to get this to be too awkward, after all. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Miss Circle. "
                        " Just talking to her about random things... "
                        " Like oreos and other snacks. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to get out of the classroom before you did. "
                        pause 2.0
                        jump tfbreak6
            else:
                " Looks like you shouldn't bother her right now, actually. "
                " Maybe you could do something else while you're here? "
                " Maybe you should clean around, the room does look a bit dusty after all. "
                scene black with dissolve
                " You spent the rest of the class hours cleaning the math teachers room. "
                " And with your help, it looked just a bit cleaner. "
                " Nice one. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You waited for everyone else to get out of the classroom before you did. "
                pause 2.0
                jump tfbreak6
        else:
            " Looks like you shouldn't bother her right now, actually. "
            " Maybe you could do something else while you're here? "
            " Maybe you should clean around, the room does look a bit dusty after all. "
            scene black with dissolve
            " You spent the rest of the class hours cleaning the math teachers room. "
            " And with your help, it looked just a bit cleaner. "
            " Nice one. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone else to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak6
    label waythisgotihow:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the language teacher's classroom... "
        " Looks like they weren't doing anything important though. "
        if thavellv <= 20:
            " And it also looks like you shouldn't bother the language teacher right now. "
            " Maybe you should do something else? "
            " Hm...the room looks like it could use some cleaning. "
            " Maybe you should just clean for now. "
            " Time for some cleaning. "
            scene black with dissolve
            " You spent the rest of the class hours cleaning the language teacher's room. "
            " And withthat, the room looked just a little bit more cleaning. "
            " Nice work you did there. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone else to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak6
        else:
            " You looked around and spotted the langauge teacher sitting infront of the class. "
            " You took an empty seat before sitting right next to her. "
            pass
        show msthravelneutral at center with easeinleft
        if thavelknow == True:
            pause 0.1
            if thavellv >= 20 or thavellv == 20:
                mst " Oh, hola [name]! "
                mst " I was just thinking about you! "
                mst " You see... "
                mst " I was thinking about talking to you for a bit. "
                mst " I've wanted to talk to you about a certain thing now. "
                mst " You see, I've been thinking... "
                mst " Since we've gotten a little bit closer... "
                mst " Even though all you've been doing is helping me... "
                mst " I've been really enjoying your company. "
                mst " Like a whole lot. "
                mst " Sometimes I wanted to talk to you a little bit more. "
                mst " Just sometimes, though. "
                mst " And I've been thinking of asking you this for awhile now... "
                mst " Would you want to be my best friend? "
                mst " I know it's a little sudden, but... "
                mst " You've been the best for me, lately. "
                mst " I don't know how to describe it, but... "
                mst " That's the best I can say. "
                mst " It's fine if you don't want to be best friends. "
                mst " We can stay as normal friends, if you'd like. "
                menu:
                    " Lets be best amigos!!! ":
                        $ thavelsend.grant()
                        hide msthravelneutral at bottom
                        show msthravelhappy at center
                        mst " Wow, you? speaking spanish? "
                        mst " Pretty cute attempt. "
                        mst " But, alright. "
                        mst " Let us be the bestest of amigos! "
                        scene thavelend with dissolve
                        " Congratulations, you've gotten Miss Thavel's ending! "
                        " And you've gotten her sweet achievement, too. "
                        " Check your achievements tab! "
                        " She would give you language lessons every now and then... "
                        " And your knowledge on languages has improved since then. "
                        " All thanks to your new best amigo. "
                        jump credits
                    " Normal amigos please ":
                        mst " Oh? understandable then. "
                        mst " Well, uh... "
                        mst " I don't want you to be uncomfortable, so... "
                        mst " How about we talk about something else? "
                        scene black with dissolve
                        " You spent the rest of the class hours talking with Miss Thavel. "
                        " Just talking with her about random things... "
                        " Nothing too special, to be honest. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another break. "
                        " You waited for everyone else to get out of the classroom before you did. "
                        pause 2.0
                        jump tfbreak6
            else:
                " Looks like you shouldn't bother the language teacher right now. "
                " Maybe you should do something else? "
                " Hm...the room looks like it could use some cleaning. "
                " Maybe you should just clean for now. "
                " Time for some cleaning. "
                scene black with dissolve
                " You spent the rest of the class hours cleaning the language teacher's room. "
                " And withthat, the room looked just a little bit more cleaning. "
                " Nice work you did there. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You waited for everyone else to get out of the classroom before you did. "
                pause 2.0
                jump tfbreak6
        else:
            " Looks like you shouldn't bother the language teacher right now. "
            " Maybe you should do something else? "
            " Hm...the room looks like it could use some cleaning. "
            " Maybe you should just clean for now. "
            " Time for some cleaning. "
            scene black with dissolve
            " You spent the rest of the class hours cleaning the language teacher's room. "
            " And withthat, the room looked just a little bit more cleaning. "
            " Nice work you did there. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone else to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak6
    label millieyay:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked to the science teacher's classroom. "
        " Looks like the students aren't doing anything... "
        if bloomielv <= 20:
            " Looks like you shouldn't bother the science teacher right now. "
            " She looks a little bit intimidating to talk to right now... "
            " Maybe you could do something else while you're here? "
            " The room DOES look a little dusty in the back... "
            " You decided to clean a little bit. "
            scene black with dissolve
            " You spent the rest of the class hours cleaning up the back of the class. "
            " And with your help, the classroom looks a little bit cleaner. "
            " Nice work you did. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone else to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak6
        else:
            " After a bit of looking, you spotted the teacher sitting at the front of the class. "
            " You took an empty chair and took a seat next to her. "
            pass
        show missbloomieneutral at center with easeinleft
        if bloomieknow == True:
            pause 0.1
            if bloomielv >= 20 or bloomielv == 20:
                msb " ...Hello there, [name]. "
                msb " I've been thinking about something recently. "
                msb " I've been thinking about this something for awhile now... "
                msb " I'm going to be really honest with you right now. "
                msb " I've been wanting to be best friends with you for awhile now. "
                msb " I know that it's too sudden... "
                msb " And I know that it's only been awhile... "
                msb " And by awhile, I mean a four days. "
                msb " I understand if you want to stay as normal friends. "
                msb " I don't mind at all. "
                msb " So...what do you say? "
                menu:
                    " Let's be besties!! ":
                        $ bloomiesend.grant()
                        hide missbloomieneutral at bottom
                        show missbloomiehappy at center
                        msb " ...Well, if you say so. "
                        msb " (It feels nice...) "
                        msb " (Having a best friend.) "
                        msb " (Even though we haven't known eachother for long...) "
                        msb " (I can't help but feel happy.) "
                        scene bloomieend with dissolve
                        " Congratulations, you've gotten Miss Bloomie's ending! "
                        " And including her very cool achievement. Check your achievements tab! "
                        " Miss Bloomie teaches you some cool science stuff every now and then. "
                        " You've learnt a whole lot more things with her by your side. "
                        jump credits
                    " Normal friends ":
                        msb " Understandable. "
                        msb " So, as to not make you uncomfortable... "
                        msb " How about we talk about something else? "
                        scene black with dissolve
                        " You spent the rest of the class hours talking with Miss Bloomie. "
                        " Just talking about cool science stuff... "
                        " Nothing too special, in all honesty. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for a break. "
                        " You waited for everyone to get out of the classroom before you did. "
                        pause 2.0
                        jump tfbreak6
            else:
                " Looks like you shouldn't bother the science teacher right now. "
                " She looks a little bit intimidating to talk to right now... "
                " Maybe you could do something else while you're here? "
                " The room DOES look a little dusty in the back... "
                " You decided to clean a little bit. "
                scene black with dissolve
                " You spent the rest of the class hours cleaning up the back of the class. "
                " And with your help, the classroom looks a little bit cleaner. "
                " Nice work you did. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another break. "
                " You waited for everyone else to get out of the classroom before you did. "
                pause 2.0
                jump tfbreak6
        else:
            " Looks like you shouldn't bother the science teacher right now. "
            " She looks a little bit intimidating to talk to right now... "
            " Maybe you could do something else while you're here? "
            " The room DOES look a little dusty in the back... "
            " You decided to clean a little bit. "
            scene black with dissolve
            " You spent the rest of the class hours cleaning up the back of the class. "
            " And with your help, the classroom looks a little bit cleaner. "
            " Nice work you did. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You waited for everyone else to get out of the classroom before you did. "
            pause 2.0
            jump tfbreak6
label tfbreak6:
    scene hallway with dissolve
    " You walked around the school for a good bit. "
    " Looks like it's almost time for this school day to end. "
    " Then it can be the weekends, and you can relax for a bit... "
    " Well, not really. "
    " You've still got some work to work on. "
    " Like, a bunch of things to work on. "
    " Like figuring out what to do for your classes next week. "
    " And also handling your students grades. "
    " Now that you got reminded of your students grades... "
    " You should probably check in to see who was failing. "
    " You didn't want anyone to fail in the first week of class. "
    " You should probably start giving them more activities... "
    " Just for them sweet, sweet points. "
    " But if someone keeps on failing... "
    " You're going to have to do something about that. "
    " Maybe even contact their parents if it gets THAT bad. "
    " Yeah...most definitely. "
    scene black with dissolve
    " You spent the rest of the break wandering around the school. "
    " Just doing your normal things... "
    " Like making sure students didn't do anything devious. "
    " Just your normal everyday stuff. "
    " You spotted nothing new though. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for you to help one last time for this week. "
    " You walked around and tried looking around for people who might need help... "
    pause 2.0
    jump tfhelp7
label tfhelp7:
    # emily, sasha, demi end
    scene hallway with dissolve
    " Looks like it's time to help for the last time this week. "
    " Who would you like to help this time? "
    if emilyknow,demiknow,sashaknow == True:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump jaketmf
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump haileytmf
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump zandertmf
    elif emilyknow,demiknow == True and sashaknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump jaketmf
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump haileytmf
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump zandertmf
    elif emilyknow,sashaknow == True and demiknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump jaketmf
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump haileytmf
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump zandertmf
    elif demiknow,sashaknow == True and emilyknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump jaketmf
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump haileytmf
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump zandertmf
    elif emilyknow == True and demiknow,sashaknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump jaketmf
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump haileytmf
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump zandertmf
    elif demiknow == True and emilyknow,sashaknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump jaketmf
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump haileytmf
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump zandertmf
    elif sashaknow == True and emilyknow,demiknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump jaketmf
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump haileytmf
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump zandertmf
    else:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump jaketmf
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump haileytmf
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump zandertmf
    label jaketmf:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the history teachers classroom... "
        " Looks like they weren't doing anything important. "
        if emilylv <= 20:
            " And it also looks like you shouldn't bother the history teacher right now. "
            " Looked like she was pretty busy right now... "
            " Maybe you should do something else? "
            " The classroom did look a little dusty in some places... "
            " You decided to clean to pass the time. "
            scene black with dissolve
            " You spent the rest of the class hours cleaning corners of the classroom. "
            " And with your help, looks like everything's just a bit cleaner. "
            " Nice work. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for you to go home. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tfmcgohome
        else:
            " After a bit of looking around, you spotted the history teacher at the back of the school. "
            " Wondering what she's thinking about... "
            " Let's go and walk over to her. "
        show msemilyneutral at center with easeinleft
        if emilyknow == True:
            pause 0.1
            if emilylv >= 20 or emilylv == 20:
                mse " Oh, hey there, [name]! "
                mse " I was actually planning on talking to you after school was over, hehe. "
                mse " But now you're here, so... "
                mse " I guess I don't have to wait for that long, hehe! "
                mse " Anyway... "
                mse " I've been thinking about talking to you for a good bit now. "
                mse " I just wanted to talk to you about something that's... "
                mse " Something that's been on my mind for awhile now. "
                mse " So...we've been getting close lately. "
                mse " Even though it's only been four days... "
                mse " Even though all you've been doing is helping me... "
                mse " I've been wanting to talk to you more and more now. "
                mse " And uh...there's been this thing that I've been wanting to ask you, too. "
                mse " Would you want to be best friends? "
                mse " I know that it's a little too soon, so... "
                mse " It would be completely fine if you don't want to. "
                mse " So...do you? "
                menu:
                    " Bestest friends in all of history! ":
                        $ emilysend.grant()
                        hide msemilyneutral at bottom
                        show msemilyhappy at center
                        mse " Woah, really? "
                        mse " ...Well, if we want to become the bestest friends in history... "
                        mse " Let's go and hangout tomorrow! "
                        mse " I'll go ahead and take you out for lunch! "
                        scene emilyend with dissolve
                        " Congratulations! you've gotten Miss Emily's ending! "
                        " And her sweet achievement too, look at your achievements tab! "
                        " You two officially became the bestest friends in history... "
                        " Atleast that's in your book. "
                        " And also, in Emily's. "
                        jump credits
                    " Normal friends for now ":
                        mse " Reasonable, reasonable... "
                        mse " Now to not make you uncomfortable... "
                        mse " How about we talk about something else? "
                        scene black with dissolve
                        " You spent the rest of the break talking with Miss Emily. "
                        " Just talking about history and things... "
                        " Nothing too special, in your opinion. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for you to go home. "
                        " You waited for everyone to get out of the classroom before you did. "
                        pause 2.0
                        jump tfmcgohome
            else:
                " Looks like you shouldn't bother the history teacher right now. "
                " Looked like she was pretty busy right now... "
                " Maybe you should do something else? "
                " The classroom did look a little dusty in some places... "
                " You decided to clean to pass the time. "
                scene black with dissolve
                " You spent the rest of the class hours cleaning corners of the classroom. "
                " And with your help, looks like everything's just a bit cleaner. "
                " Nice work. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for you to go home. "
                " You waited for everyone to get out of the classroom before you did. "
                pause 2.0
                jump tfmcgohome
        else:
            " Looks like you shouldn't bother the history teacher right now. "
            " Looked like she was pretty busy right now... "
            " Maybe you should do something else? "
            " The classroom did look a little dusty in some places... "
            " You decided to clean to pass the time. "
            scene black with dissolve
            " You spent the rest of the class hours cleaning corners of the classroom. "
            " And with your help, looks like everything's just a bit cleaner. "
            " Nice work. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for you to go home. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tfmcgohome
    label haileytmf:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the music teacher's classroom... "
        " Looks like the students aren't doing anything important. "
        if demilv <= 20:
            " And it also looks like you shouldn't bother the music teacher right now. "
            " Looked like he was pretty busy right now... "
            " Maybe you should do something else? "
            " The classroom did look a little dusty in some places... "
            " You decided to clean to pass the time. "
            scene black with dissolve
            " You spent the rest of the class hours cleaning corners of the classroom. "
            " And with your help, looks like everything's just a bit cleaner. "
            " Nice work. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for you to go home. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tfmcgohome
        else:
            " After a good bit of looking around, you spotted the music teacher at the back of the class. "
            " Wondering what he's doing, you walked over to him. "
            pass
        show mrdemineutral at center with easeinleft
        if demiknow == True:
            pause 0.1
            if demilv >= 20 or demilv == 20:
                msd " Oh, um... "
                msd " ..Hey there, [name]... "
                msd " I was actually...thinking about you... "
                msd " (God, that sounds so weird...) "
                msd " (Hopefully [they] don't get weirded out...) "
                msd " Um... "
                msd " I've been meaning to talk to you about something... "
                msd " I've been thinking... "
                msd " We've been getting a little close lately... "
                msd " Even though it's only been four days... "
                msd " And even though all you've been doing is helping me out... "
                msd " I...um... "
                msd " I've been thinking of asking you this for awhile now... "
                msd " Like, awhile now... "
                msd " (I hope I don't mess this up...) "
                msd " Um...would you... "
                msd " Would you...like to be best friends with me...? "
                msd " ...It's okay if you don't want to... "
                msd " It's a little too soon for that, after all... "
                msd " But, um... "
                msd " What do you say...? "
                menu:
                    " Let's be best friends!! ":
                        $ demisend.grant()
                        hide mrdemineutral at bottom
                        show mrdemihappy at center
                        msd " Really...? "
                        msd " Well, if you want to, then... "
                        msd " I don't mind... "
                        msd " (Wow, a best friend...!) "
                        msd " (This must be my luckiest day yet...!) "
                        scene demiend with dissolve
                        " Congratulations, you've gotten Mister Demi's ending! "
                        " And also his achievement. Check your achievements tab! "
                        " You sometimes visit Demi's house... "
                        " And get your ears blessed with Demi's piano playing. "
                        jump credits
                    " Normal friends please ":
                        msd " Oh, uh... "
                        msd " Reasonable, actually... "
                        msd " Um... "
                        msd " To not make this awkward... "
                        msd " How about we talk about something else...? "
                        scene black with dissolve
                        " You spent the rest of the class hours talking with Mister Demi. "
                        " Just talking about random music things... "
                        " Nothing too special, in all honesty. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for you to go home. "
                        " You waited for everyone to get out of the classroom before you did. "
                        pause 2.0
                        jump tfmcgohome
            else:
                " Looks like you shouldn't bother the music teacher right now. "
                " Looked like he was pretty busy right now... "
                " Maybe you should do something else? "
                " The classroom did look a little dusty in some places... "
                " You decided to clean to pass the time. "
                scene black with dissolve
                " You spent the rest of the class hours cleaning corners of the classroom. "
                " And with your help, looks like everything's just a bit cleaner. "
                " Nice work. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for you to go home. "
                " You waited for everyone to get out of the classroom before you did. "
                pause 2.0
                jump tfmcgohome
        else:
            " Looks like you shouldn't bother the music teacher right now. "
            " Looked like he was pretty busy right now... "
            " Maybe you should do something else? "
            " The classroom did look a little dusty in some places... "
            " You decided to clean to pass the time. "
            scene black with dissolve
            " You spent the rest of the class hours cleaning corners of the classroom. "
            " And with your help, looks like everything's just a bit cleaner. "
            " Nice work. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for you to go home. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tfmcgohome
    label zandertmf:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the art teachers classroom... "
        " Looks like the students were just doing something. "
        if sashalv <= 20:
            " And it also looks like you shouldn't bother the art teacher right now. "
            " Looked like she was pretty busy right now... "
            " Maybe you should do something else? "
            " The classroom did look a little dusty in some places... "
            " You decided to clean to pass the time. "
            scene black with dissolve
            " You spent the rest of the class hours cleaning corners of the classroom. "
            " And with your help, looks like everything's just a bit cleaner. "
            " Nice work. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for you to go home. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tfmcgohome
        else:
            " After a bit of looking, looks like the art teacher was at the back of the school. "
            " You decided to walk over to her after a good bit. "
        show sashaneutral at center with easeinleft
        if sashaknow == True:
            pause 0.1
            if sashalv >= 20 or sashalv == 20:
                mss " Oh!! hi, [name]!! "
                mss " I was just thinking about you!! "
                mss " I was thinking about a few things, actually.. "
                mss " You know how we've been getting close lately? "
                mss " Even though if it's only been four days... "
                mss " I've been thinking about a question! "
                mss " A question that I've been meaning to ask you! "
                mss " So, um... "
                mss " Would you...uh... "
                mss " Would you like to be best friends with me? "
                mss " It's okay if you don't want to be friends with me! "
                mss " I know it's a little too sudden... "
                mss " So I understand if you don't want to! "
                mss " But, uh...what do you say? "
                menu:
                    " Best friends!! ":
                        $ sashasend.grant()
                        hide sashaneutral at bottom
                        show sashahappy at center
                        mss " Really?? "
                        mss " Yayyy!! "
                        mss " How about we go to get a snack tomorrow? "
                        mss " I still have a few dollars left, after all! "
                        scene sashaend with dissolve
                        " Congratulations! You've gotten Miss Sasha's ending! "
                        " And her sweet achievement, too. Check your achievements tab! "
                        " Miss Sasha would come over every now and then and ask you to pose for her paintings... "
                        " You didn't mind, of course. "
                        jump credits
                    " Normal friends ":
                        mss " Awww...okay! "
                        mss " How about we talk about something else though... "
                        mss " I don't want you to feel too awkward, after all! "
                        scene black with dissolve
                        " You spent the rest of the class hours talking with Miss Sasha. "
                        " Just talking about arts and crafts... "
                        " Nothing too important to you, really. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for you to go home. "
                        " You waited for everyone to get out of the classroom before you did. "
                        pause 2.0
                        jump tfmcgohome
            else:
                " Looks like you shouldn't bother the art teacher right now. "
                " Looked like she was pretty busy right now... "
                " Maybe you should do something else? "
                " The classroom did look a little dusty in some places... "
                " You decided to clean to pass the time. "
                scene black with dissolve
                " You spent the rest of the class hours cleaning corners of the classroom. "
                " And with your help, looks like everything's just a bit cleaner. "
                " Nice work. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for you to go home. "
                " You waited for everyone to get out of the classroom before you did. "
                pause 2.0
                jump tfmcgohome
        else:
            " Looks like you shouldn't bother the art teacher right now. "
            " Looked like she was pretty busy right now... "
            " Maybe you should do something else? "
            " The classroom did look a little dusty in some places... "
            " You decided to clean to pass the time. "
            scene black with dissolve
            " You spent the rest of the class hours cleaning corners of the classroom. "
            " And with your help, looks like everything's just a bit cleaner. "
            " Nice work. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for you to go home. "
            " You waited for everyone to get out of the classroom before you did. "
            pause 2.0
            jump tfmcgohome
label tfmcgohome:
    scene paperschoolfront with dissolve
    " Looks like it's time for you to go home. "
    " As you were going home, you couldn't help but feel some sort of lonliness. "
    " You tried to ignore the feeling... "
    " Maybe it's just your head messing with you. "
    " You can't be feeling lonely for something like this... "
    " You continued on your way home. "
    scene black with dissolve
    stop music fadeout 1.5
    pause 2.0
    play music "audio/home.mp3" fadein 1.5
    scene mcroom with dissolve
    " By the time you got home, you couldn't deny it anymore. "
    " You felt extremely lonely. "
    " Maybe you should've talked to the others more. "
    " Oh well, you can do that next week. "
    " Time for you to get some rest. "
    scene black with dissolve
    " Good night, [name]. "
    " Enjoy your eternal rest. "
    pause 2.0
    scene lonelyend with dissolve
    " Wow, uh... "
    " Yeah. Lonely ending. "
    " Nice one, I guess. "
    jump credits
