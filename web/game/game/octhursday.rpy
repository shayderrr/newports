label octhursday:
    show text " DAY 4 - THURSDAY "
    pause 1.5
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
    jump octhursclass1
label octhursclass1:
    " You sat down in your seat and waited for class to start patiently. "
    " You're starting to be more comfortable the more you're here... "
    " Starting to be comfortable with all of the loud noises from your classmates... "
    " Even started to somehow be more comfortable in your seat. "
    " That's how good this school is, really. "
    " After a bit of waiting, the history teacher arrives. "
    " He looks a little troubled today... "
    " Might be best to just not be annoying for that. "
    " And it seems like the entire class thought the same thing... "
    " Everyone seemed quiet when he came in with that look. "
    " Usually the classroom would be a tad bit noisy, but now it's just... "
    " Dead silent. Time to actually pay attention to class... "
    " Just so that you don't get your head potentially chopped off. "
    show mrclioangry at center with easeinright
    mscl " Ugh, I'm 5 minutes late... "
    mscl " Great. This is just great. "
    mscl " All thanks to my alarm clock breaking... "
    mscl " This is gonna be a WONDERFUL day for me, surely. "
    mscl " ...I'm sorry class, I'm just in a...bad mood today. "
    mscl " (As all of you can probably tell.) "
    mscl " Ahem - now, I don't want any of you to be annoying to me today. "
    mscl " If you don't understand something I say - ask your classmates about it. "
    mscl " Or, just ask me about it later in our GC. "
    mscl " I don't want to deal with stupidity at this moment. "
    mscl " And by the way, about the activity we're supposed to be doing today... "
    mscl " That will be an assignment that's due next week monday. "
    mscl " I will send the assignment to the GC we're in. "
    mscl " Please do it - it's worth 50 points in total. "
    mscl " Let's get started with the lesson now. "
    " Jeez... okay, you could see why people didn't like him whenever he was mad. "
    " Let's actually pay attention so that you don't piss him off. "
    " You don't want to get all your limbs chopped off, after all. "
    scene black with dissolve
    " You spent the rest of class hours actually paying attention to the lesson. "
    " The classroom was silent as everything happened. "
    " And since you focused so much, you somehow understood the lesson! "
    " Wow, you understood something for once in your life! "
    " But of course you didn't understand your existence here. "
    play sound "audio/bellring.mp3"
    " The bell rings after a little bit, looks like it's time for a break. "
    " You walked out of the classroom after a good bit. "
    pause 2.0
    jump octhursbreak1
label octhursbreak1:
    scene hallway with dissolve
    " Where would you like to hang out for this break? "
    menu:
        " {image=sparkicon} The front of the school {image=orchidicon} ":
            jump octhursfront1
        " {image=koaicon} The back of the school {image=temeroicon} ":
            jump octhursback1
        " {image=jacobicon} The gym {image=matteicon} ":
            jump octhursgym1
        " {image=noxicon} The cafeteria {image=carmenicon} ":
            jump octhurscafeteria1
        " {image=diskicon} The rooftop {image=jamicon} ":
            jump octhursrooftop1
        " {image=yinyangicon} The library {image=quinnicon} ":
            jump octhurslibrary1
    label octhursfront1:
        # orchid and spark
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked to the front of the school and spotted two of your classmates talking. "
        " Wondering what they were talking about, you walked over to them. "
        " Let's go ahead and join their wonderful conversation they're having. "
        show sparkneutral at left with easeinright
        show orchidneutral at right with easeinright
        if sparkknow == True and orchidknow == True:
            sp " You sure about this, Orchid? "
            sp " I mean, the game IS kinda scary... "
            sp " I don't know if you're into that stuff. "
            oc " Trust me, I can handle it! "
            oc " I'm really into horror stuff anyway. "
            oc " I'm not a baby after all! "
            sp " Okay, if you say so. "
            sp " I'll hop on right after school. "
            sp " If you're not online at that time then I won't hesitate to spam your messages. "
            oc " Hah - okay! "
            " You greeted the both of them politely, and asked what they were talking about. "
            oc " Oh heyyy, it's you! "
            oc " Me and Spark were just talking about playing a game later! "
            sp " It's a horror game. "
            sp " It's basically about urban legends around the world. "
            sp " Our MC doesn't really know how they got to see them, but we're being chased by them. "
            sp " They're constantly trying to escape that hell they're in. "
            sp " I'm pretty into it because I'm big into urban legends. "
            oc " And I'm getting into it because I love horror! "
            oc " Actually...you wanna hang out with us later? "
            oc " Not gonna force you if you don't want to - this is all for fun! "
            sp " Yup. "
            sp " Actually, I could play right now and show you guys what it's like. "
            oc " Oh! really? "
            sp " Yeah, I got enough mobile data for that. "
            sp " You wanna watch, [name]? "
            menu:
                " Hang out with Spark and Orchid ":
                    $ orchidlv += 5
                    $ sparklv += 5
                    hide orchidneutral at bottom
                    show orchidhappy at right
                    oc " Awesome! "
                    sp " Great, let me just boot the game up... "
                    sp " It's gonna take a bit due to how low the signal here is. "
                    sp " You'd expect this school to have good signal, but nah. "
                    hide orchidhappy at bottom
                    show orchidneutral at right
                    oc " Hey, what about that one wifi network I see you using...? "
                    oc " You could just...you know, connect to that? "
                    oc " It's got pretty good signal! "
                    sp " Oh, that? "
                    sp " Don't tell anyone, but that wifi network is for the teachers. "
                    sp " Found it one day and now I can just connect to it whenever I want. "
                    sp " Though I'm pretty sure if I keep using it, they're gonna find out. "
                    oc " Aw, bummer. "
                    " You have a feeling Spark was lying just a bit when he said that... "
                    " Let's not think too hard about it though. "
                    " Spark boots up the game on his phone and he starts playing for the both of you... "
                    scene black with dissolve
                    " You spent the rest of the break watching Spark play a horror game. "
                    " You weren't gonna lie, some parts did jumpscare you for a bit. "
                    " But other than that, you were doing pretty fine. "
                    " The game was really well made with well designed characters. "
                    " And yes, there WAS a design for the MC. "
                    " Looks pretty basic, but in a good way. "
                    " Spark only showed you and Orchid what chapter 1 looked like because he didn't want to spoil you two too much. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump thealthclass1
                " I've got other places to be ":
                    hide orchidneutral at bottom
                    show orchidsad at right
                    oc " Oh wait, you were just passing by then? "
                    oc " Gee, didn't mean to stop whatever you were doing... "
                    oc " But still - we could hang out later if you want to! "
                    sp " You can go ahead and do whatever you wanted to do, [name]. "
                    sp " We won't bother you more. "
                    hide orchidsad at bottom
                    show orchidneutral at right
                    oc " Yeah! Have fun in whatever you're doing! "
                    sp " Mhmmm. "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " Just wandering around...doing nothing. "
                    " You were also listening into peoples conversations while you were doing this. "
                    " You know it's not good to eavesdrop, buuuuuut... "
                    " Maybe this would be an exception. "
                    " I mean, come on - the dramas interesting. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit while you were walking around. "
                    " You walked to your next class after a bit. "
                    pause 2.0
                    jump thealthclass1
        elif sparkknow == True and orchidknow == False:
            sp " You sure about this, Orchid? "
            $ orchidknow = True
            sp " I mean, the game IS kinda scary... "
            sp " I don't know if you're into that stuff. "
            oc " Trust me, I can handle it! "
            oc " I'm really into horror stuff anyway. "
            oc " I'm not a baby after all! "
            sp " Okay, if you say so. "
            sp " I'll hop on right after school. "
            sp " If you're not online at that time then I won't hesitate to spam your messages. "
            oc " Hah - okay! "
            " You greeted the both of them politely, and asked what they were talking about. "
            oc " Oh heyyy, it's you! "
            oc " Me and Spark were just talking about playing a game later! "
            sp " It's a horror game. "
            sp " It's basically about urban legends around the world. "
            sp " Our MC doesn't really know how they got to see them, but we're being chased by them. "
            sp " They're constantly trying to escape that hell they're in. "
            sp " I'm pretty into it because I'm big into urban legends. "
            oc " And I'm getting into it because I love horror! "
            oc " Actually...you wanna hang out with us later? "
            oc " Not gonna force you if you don't want to - this is all for fun! "
            sp " Yup. "
            sp " Actually, I could play right now and show you guys what it's like. "
            oc " Oh! really? "
            sp " Yeah, I got enough mobile data for that. "
            sp " You wanna watch, [name]? "
            menu:
                " Hang out with Spark and Orchid ":
                    $ orchidlv += 5
                    $ sparklv += 5
                    hide orchidneutral at bottom
                    show orchidhappy at right
                    oc " Awesome! "
                    sp " Great, let me just boot the game up... "
                    sp " It's gonna take a bit due to how low the signal here is. "
                    sp " You'd expect this school to have good signal, but nah. "
                    hide orchidhappy at bottom
                    show orchidneutral at right
                    oc " Hey, what about that one wifi network I see you using...? "
                    oc " You could just...you know, connect to that? "
                    oc " It's got pretty good signal! "
                    sp " Oh, that? "
                    sp " Don't tell anyone, but that wifi network is for the teachers. "
                    sp " Found it one day and now I can just connect to it whenever I want. "
                    sp " Though I'm pretty sure if I keep using it, they're gonna find out. "
                    oc " Aw, bummer. "
                    " You have a feeling Spark was lying just a bit when he said that... "
                    " Let's not think too hard about it though. "
                    " Spark boots up the game on his phone and he starts playing for the both of you... "
                    scene black with dissolve
                    " You spent the rest of the break watching Spark play a horror game. "
                    " You weren't gonna lie, some parts did jumpscare you for a bit. "
                    " But other than that, you were doing pretty fine. "
                    " The game was really well made with well designed characters. "
                    " And yes, there WAS a design for the MC. "
                    " Looks pretty basic, but in a good way. "
                    " Spark only showed you and Orchid what chapter 1 looked like because he didn't want to spoil you two too much. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump thealthclass1
                " I've got other places to be ":
                    hide orchidneutral at bottom
                    show orchidsad at right
                    oc " Oh wait, you were just passing by then? "
                    oc " Gee, didn't mean to stop whatever you were doing... "
                    oc " But still - we could hang out later if you want to! "
                    sp " You can go ahead and do whatever you wanted to do, [name]. "
                    sp " We won't bother you more. "
                    hide orchidsad at bottom
                    show orchidneutral at right
                    oc " Yeah! Have fun in whatever you're doing! "
                    sp " Mhmmm. "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " Just wandering around...doing nothing. "
                    " You were also listening into peoples conversations while you were doing this. "
                    " You know it's not good to eavesdrop, buuuuuut... "
                    " Maybe this would be an exception. "
                    " I mean, come on - the dramas interesting. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit while you were walking around. "
                    " You walked to your next class after a bit. "
                    pause 2.0
                    jump thealthclass1
        elif sparkknow == False and orchidknow == True:
            x " You sure about this, Orchid? "
            x " I mean, the game IS kinda scary... "
            x " I don't know if you're into that stuff. "
            oc " Trust me, I can handle it! "
            oc " I'm really into horror stuff anyway. "
            oc " I'm not a baby after all! "
            x " Okay, if you say so. "
            x " I'll hop on right after school. "
            x " If you're not online at that time then I won't hesitate to spam your messages. "
            oc " Hah - okay! "
            " You greeted the both of them politely, and asked what they were talking about. "
            oc " Oh heyyy, it's you! "
            $ sparkknow = True
            oc " Me and Spark were just talking about playing a game later! "
            sp " It's a horror game. "
            sp " It's basically about urban legends around the world. "
            sp " Our MC doesn't really know how they got to see them, but we're being chased by them. "
            sp " They're constantly trying to escape that hell they're in. "
            sp " I'm pretty into it because I'm big into urban legends. "
            oc " And I'm getting into it because I love horror! "
            oc " Actually...you wanna hang out with us later? "
            oc " Not gonna force you if you don't want to - this is all for fun! "
            sp " Yup. "
            sp " Actually, I could play right now and show you guys what it's like. "
            oc " Oh! really? "
            sp " Yeah, I got enough mobile data for that. "
            sp " You wanna watch, [name]? "
            menu:
                " Hang out with Spark and Orchid ":
                    $ orchidlv += 5
                    $ sparklv += 5
                    hide orchidneutral at bottom
                    show orchidhappy at right
                    oc " Awesome! "
                    sp " Great, let me just boot the game up... "
                    sp " It's gonna take a bit due to how low the signal here is. "
                    sp " You'd expect this school to have good signal, but nah. "
                    hide orchidhappy at bottom
                    show orchidneutral at right
                    oc " Hey, what about that one wifi network I see you using...? "
                    oc " You could just...you know, connect to that? "
                    oc " It's got pretty good signal! "
                    sp " Oh, that? "
                    sp " Don't tell anyone, but that wifi network is for the teachers. "
                    sp " Found it one day and now I can just connect to it whenever I want. "
                    sp " Though I'm pretty sure if I keep using it, they're gonna find out. "
                    oc " Aw, bummer. "
                    " You have a feeling Spark was lying just a bit when he said that... "
                    " Let's not think too hard about it though. "
                    " Spark boots up the game on his phone and he starts playing for the both of you... "
                    scene black with dissolve
                    " You spent the rest of the break watching Spark play a horror game. "
                    " You weren't gonna lie, some parts did jumpscare you for a bit. "
                    " But other than that, you were doing pretty fine. "
                    " The game was really well made with well designed characters. "
                    " And yes, there WAS a design for the MC. "
                    " Looks pretty basic, but in a good way. "
                    " Spark only showed you and Orchid what chapter 1 looked like because he didn't want to spoil you two too much. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump thealthclass1
                " I've got other places to be ":
                    hide orchidneutral at bottom
                    show orchidsad at right
                    oc " Oh wait, you were just passing by then? "
                    oc " Gee, didn't mean to stop whatever you were doing... "
                    oc " But still - we could hang out later if you want to! "
                    sp " You can go ahead and do whatever you wanted to do, [name]. "
                    sp " We won't bother you more. "
                    hide orchidsad at bottom
                    show orchidneutral at right
                    oc " Yeah! Have fun in whatever you're doing! "
                    sp " Mhmmm. "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " Just wandering around...doing nothing. "
                    " You were also listening into peoples conversations while you were doing this. "
                    " You know it's not good to eavesdrop, buuuuuut... "
                    " Maybe this would be an exception. "
                    " I mean, come on - the dramas interesting. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit while you were walking around. "
                    " You walked to your next class after a bit. "
                    pause 2.0
                    jump thealthclass1
        else:
            x " You sure about this, Orchid? "
            $ orchidknow = True
            x " I mean, the game IS kinda scary... "
            x " I don't know if you're into that stuff. "
            oc " Trust me, I can handle it! "
            oc " I'm really into horror stuff anyway. "
            oc " I'm not a baby after all! "
            x " Okay, if you say so. "
            x " I'll hop on right after school. "
            x " If you're not online at that time then I won't hesitate to spam your messages. "
            oc " Hah - okay! "
            " You greeted the both of them politely, and asked what they were talking about. "
            oc " Oh heyyy, it's you! "
            $ sparkknow = True
            oc " Me and Spark were just talking about playing a game later! "
            sp " It's a horror game. "
            sp " It's basically about urban legends around the world. "
            sp " Our MC doesn't really know how they got to see them, but we're being chased by them. "
            sp " They're constantly trying to escape that hell they're in. "
            sp " I'm pretty into it because I'm big into urban legends. "
            oc " And I'm getting into it because I love horror! "
            oc " Actually...you wanna hang out with us later? "
            oc " Not gonna force you if you don't want to - this is all for fun! "
            sp " Yup. "
            sp " Actually, I could play right now and show you guys what it's like. "
            oc " Oh! really? "
            sp " Yeah, I got enough mobile data for that. "
            sp " You wanna watch, [name]? "
            menu:
                " Hang out with Spark and Orchid ":
                    $ orchidlv += 5
                    $ sparklv += 5
                    hide orchidneutral at bottom
                    show orchidhappy at right
                    oc " Awesome! "
                    sp " Great, let me just boot the game up... "
                    sp " It's gonna take a bit due to how low the signal here is. "
                    sp " You'd expect this school to have good signal, but nah. "
                    hide orchidhappy at bottom
                    show orchidneutral at right
                    oc " Hey, what about that one wifi network I see you using...? "
                    oc " You could just...you know, connect to that? "
                    oc " It's got pretty good signal! "
                    sp " Oh, that? "
                    sp " Don't tell anyone, but that wifi network is for the teachers. "
                    sp " Found it one day and now I can just connect to it whenever I want. "
                    sp " Though I'm pretty sure if I keep using it, they're gonna find out. "
                    oc " Aw, bummer. "
                    " You have a feeling Spark was lying just a bit when he said that... "
                    " Let's not think too hard about it though. "
                    " Spark boots up the game on his phone and he starts playing for the both of you... "
                    scene black with dissolve
                    " You spent the rest of the break watching Spark play a horror game. "
                    " You weren't gonna lie, some parts did jumpscare you for a bit. "
                    " But other than that, you were doing pretty fine. "
                    " The game was really well made with well designed characters. "
                    " And yes, there WAS a design for the MC. "
                    " Looks pretty basic, but in a good way. "
                    " Spark only showed you and Orchid what chapter 1 looked like because he didn't want to spoil you two too much. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump thealthclass1
                " I've got other places to be ":
                    hide orchidneutral at bottom
                    show orchidsad at right
                    oc " Oh wait, you were just passing by then? "
                    oc " Gee, didn't mean to stop whatever you were doing... "
                    oc " But still - we could hang out later if you want to! "
                    sp " You can go ahead and do whatever you wanted to do, [name]. "
                    sp " We won't bother you more. "
                    hide orchidsad at bottom
                    show orchidneutral at left
                    oc " Yeah! Have fun in whatever you're doing! "
                    sp " Mhmmm. "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " Just wandering around...doing nothing. "
                    " You were also listening into peoples conversations while you were doing this. "
                    " You know it's not good to eavesdrop, buuuuuut... "
                    " Maybe this would be an exception. "
                    " I mean, come on - the dramas interesting. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit while you were walking around. "
                    " You walked to your next class after a bit. "
                    pause 2.0
                    jump thealthclass1
    label octhursback1:
        # koa and temero
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of the school and spotted two of your classmates talking with eachother. "
        " Wondering what they're talking about, you decided to join their conversation. "
        show koaneutral at right with easeinleft
        show temeroneutral at left with easeinright
        if koaknow == True and temeroknow == True:
            tm " - And that's why we need to use different needles instead of the same ones! "
            tm " Write that down into your notes. "
            k " ... "
            " You greeted them politely before asking them what they're doing. "
            tm " Oh heeey, [name]! "
            tm " I was just letting Koa over here copy my notes. "
            tm " Turns out he got a little distracted in class. "
            tm " Mister Clio would kill you for that, Koa. "
            k " ...I know. "
            k " Orchid was just sending me some notes. "
            tm " Ohooo...now you're blaming it on your friend? "
            tm " That's pretty rudeof you, Koa. "
            hide koaneutral at bottom
            show koaangry at right
            k " I'm not... blaming Orchid. "
            k " I was just simply giving you a reason on why I wasn't paying attention... "
            k " I didn't mean it in that way. "
            tm " Yeah, alright. "
            hide koaangry at bottom
            show koaneutral at right
            tm " How's Orchid anyway? "
            tm " They been actually making friends, or...? "
            k " I'm pretty sure that he has. "
            k " [name] - has Orchid been making more friends...? "
            menu:
                " Saw them talking with someone at the front of the school ":
                    $ koalv += 5
                    $ temerolv += 5
                    k " Really..? "
                    k " That's wonderful to hear, then. "
                    k " Unless if that person is someone who isn't from this school of course. "
                    k " I'm going to get really concerned if that's the case. "
                    tm " Oh riiiight, Orchid was talking with Spark. "
                    tm " Spark told me about this game he wanted to show them. "
                    tm " Since Orchid was big into horror, he thought they'd be real into it. "
                    k " Huh...Orchid IS into horror. "
                    k " It's good that Orchid's interacting with Spark now though. "
                    k " But, if it turns out that Orchid isn't comfortable with him... "
                    tm " Yeah, yeah I know. "
                    tm " You wanna protect 'em cause they're like family to you. "
                    tm " No need to throw paragraphs at me. "
                    k " ... "
                    tm " Anywayyy, I'm pretty sure [name] would like to hang out with us. "
                    tm " Would be good for [them] since they could also take notes from MY notes. "
                    tm " Cmere, [name]!! "
                    " You couldn't even say anything and you were pulled down onto the ground with Temero and Koa. "
                    " It was basically one of those awkward group hugs that you and Koa don't want to be in. "
                    " But Temero was holding on pretty tight, so... "
                    tm " This is gonna be the best note taking session ever! "
                    k  " ...Yeah. "
                    scene black with dissolve
                    " You spent the rest of the break copying Temero's notes. "
                    " Her notes actually looked pretty nice... "
                    " It's got full explanations but the important parts are highlighted with pink highlighter. "
                    " Also got some stickers here and there in her notebook. "
                    " ...And her notebook smelt like failed experiments. Not sure how you could tell, "
                    " Just it was just a strong feeling or something. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump thealthclass1
                " I dunno ":
                    $ temerolv += 5
                    k " ... "
                    tm " Oh riiiight, Orchid was talking with Spark. "
                    tm " Spark told me about this game he wanted to show them. "
                    tm " Since Orchid was big into horror, he thought they'd be real into it. "
                    k " Huh...Orchid IS into horror. "
                    k " It's good that Orchid's interacting with Spark now though. "
                    k " But, if it turns out that Orchid isn't comfortable with him... "
                    tm " Yeah, yeah I know. "
                    tm " You wanna protect 'em cause they're like family to you. "
                    tm " No need to throw paragraphs at me. "
                    k " ... "
                    tm " Anywayyy, I'm pretty sure [name] would like to hang out with us. "
                    tm " Would be good for [them] since they could also take notes from MY notes. "
                    tm " Cmere, [name]!! "
                    " You couldn't even say anything and you were pulled down onto the ground with Temero and Koa. "
                    " It was basically one of those awkward group hugs that you and Koa don't want to be in. "
                    " But Temero was holding on pretty tight, so... "
                    tm " This is gonna be the best note taking session ever! "
                    k  " ...Yeah. "
                    scene black with dissolve
                    " You spent the rest of the break copying Temero's notes. "
                    " Her notes actually looked pretty nice... "
                    " It's got full explanations but the important parts are highlighted with pink highlighter. "
                    " Also got some stickers here and there in her notebook. "
                    " ...And her notebook smelt like failed experiments. Not sure how you could tell, "
                    " Just it was just a strong feeling or something. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump thealthclass1
        elif koaknow == True and temeroknow == False:
            x " - And that's why we need to use different needles instead of the same ones! "
            x " Write that down into your notes. "
            k " ... "
            " You greeted them politely before asking them what they're doing. "
            x " Oh heeey, [name]! "
            $ temeroknow = True
            tm " It's me, the great Temero NEO - and I was...uh... "
            tm " (what wasI gonna say again.) "
            tm " (oh right.) "
            tm " I was just letting Koa over here copy my notes. "
            tm " Turns out he got a little distracted in class. "
            tm " Mister Clio would kill you for that, Koa. "
            k " ...I know. "
            k " Orchid was just sending me some notes. "
            tm " Ohooo...now you're blaming it on your friend? "
            tm " That's pretty rudeof you, Koa. "
            hide koaneutral at bottom
            show koaangry at right
            k " I'm not... blaming Orchid. "
            k " I was just simply giving you a reason on why I wasn't paying attention... "
            k " I didn't mean it in that way. "
            tm " Yeah, alright. "
            hide koaangry at bottom
            show koaneutral at right
            tm " How's Orchid anyway? "
            tm " They been actually making friends, or...? "
            k " I'm pretty sure that he has. "
            k " [name] - has Orchid been making more friends...? "
            menu:
                " Saw them talking with someone at the front of the school ":
                    $ koalv += 5
                    $ temerolv += 5
                    k " Really..? "
                    k " That's wonderful to hear, then. "
                    k " Unless if that person is someone who isn't from this school of course. "
                    k " I'm going to get really concerned if that's the case. "
                    tm " Oh riiiight, Orchid was talking with Spark. "
                    tm " Spark told me about this game he wanted to show them. "
                    tm " Since Orchid was big into horror, he thought they'd be real into it. "
                    k " Huh...Orchid IS into horror. "
                    k " It's good that Orchid's interacting with Spark now though. "
                    k " But, if it turns out that Orchid isn't comfortable with him... "
                    tm " Yeah, yeah I know. "
                    tm " You wanna protect 'em cause they're like family to you. "
                    tm " No need to throw paragraphs at me. "
                    k " ... "
                    tm " Anywayyy, I'm pretty sure [name] would like to hang out with us. "
                    tm " Would be good for [them] since they could also take notes from MY notes. "
                    tm " Cmere, [name]!! "
                    " You couldn't even say anything and you were pulled down onto the ground with Temero and Koa. "
                    " It was basically one of those awkward group hugs that you and Koa don't want to be in. "
                    " But Temero was holding on pretty tight, so... "
                    tm " This is gonna be the best note taking session ever! "
                    k  " ...Yeah. "
                    scene black with dissolve
                    " You spent the rest of the break copying Temero's notes. "
                    " Her notes actually looked pretty nice... "
                    " It's got full explanations but the important parts are highlighted with pink highlighter. "
                    " Also got some stickers here and there in her notebook. "
                    " ...And her notebook smelt like failed experiments. Not sure how you could tell, "
                    " Just it was just a strong feeling or something. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump thealthclass1
                " I dunno ":
                    $ temerolv += 5
                    k " ... "
                    tm " Oh riiiight, Orchid was talking with Spark. "
                    tm " Spark told me about this game he wanted to show them. "
                    tm " Since Orchid was big into horror, he thought they'd be real into it. "
                    k " Huh...Orchid IS into horror. "
                    k " It's good that Orchid's interacting with Spark now though. "
                    k " But, if it turns out that Orchid isn't comfortable with him... "
                    tm " Yeah, yeah I know. "
                    tm " You wanna protect 'em cause they're like family to you. "
                    tm " No need to throw paragraphs at me. "
                    k " ... "
                    tm " Anywayyy, I'm pretty sure [name] would like to hang out with us. "
                    tm " Would be good for [them] since they could also take notes from MY notes. "
                    tm " Cmere, [name]!! "
                    " You couldn't even say anything and you were pulled down onto the ground with Temero and Koa. "
                    " It was basically one of those awkward group hugs that you and Koa don't want to be in. "
                    " But Temero was holding on pretty tight, so... "
                    tm " This is gonna be the best note taking session ever! "
                    k  " ...Yeah. "
                    scene black with dissolve
                    " You spent the rest of the break copying Temero's notes. "
                    " Her notes actually looked pretty nice... "
                    " It's got full explanations but the important parts are highlighted with pink highlighter. "
                    " Also got some stickers here and there in her notebook. "
                    " ...And her notebook smelt like failed experiments. Not sure how you could tell, "
                    " Just it was just a strong feeling or something. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump thealthclass1
        elif koaknow == False and temeroknow == True:
            tm " - And that's why we need to use different needles instead of the same ones! "
            tm " Write that down into your notes. "
            x " ... "
            " You greeted them politely before asking them what they're doing. "
            tm " Oh heeey, [name]! "
            $ koaknow = True
            tm " I was just letting Koa over here copy my notes. "
            tm " Turns out he got a little distracted in class. "
            tm " Mister Clio would kill you for that, Koa. "
            k " ...I know. "
            k " Orchid was just sending me some notes. "
            tm " Ohooo...now you're blaming it on your friend? "
            tm " That's pretty rudeof you, Koa. "
            hide koaneutral at bottom
            show koaangry at right
            k " I'm not... blaming Orchid. "
            k " I was just simply giving you a reason on why I wasn't paying attention... "
            k " I didn't mean it in that way. "
            tm " Yeah, alright. "
            hide koaangry at bottom
            show koaneutral at right
            tm " How's Orchid anyway? "
            tm " They been actually making friends, or...? "
            k " I'm pretty sure that he has. "
            k " [name] - has Orchid been making more friends...? "
            menu:
                " Saw them talking with someone at the front of the school ":
                    $ koalv += 5
                    $ temerolv += 5
                    k " Really..? "
                    k " That's wonderful to hear, then. "
                    k " Unless if that person is someone who isn't from this school of course. "
                    k " I'm going to get really concerned if that's the case. "
                    tm " Oh riiiight, Orchid was talking with Spark. "
                    tm " Spark told me about this game he wanted to show them. "
                    tm " Since Orchid was big into horror, he thought they'd be real into it. "
                    k " Huh...Orchid IS into horror. "
                    k " It's good that Orchid's interacting with Spark now though. "
                    k " But, if it turns out that Orchid isn't comfortable with him... "
                    tm " Yeah, yeah I know. "
                    tm " You wanna protect 'em cause they're like family to you. "
                    tm " No need to throw paragraphs at me. "
                    k " ... "
                    tm " Anywayyy, I'm pretty sure [name] would like to hang out with us. "
                    tm " Would be good for [them] since they could also take notes from MY notes. "
                    tm " Cmere, [name]!! "
                    " You couldn't even say anything and you were pulled down onto the ground with Temero and Koa. "
                    " It was basically one of those awkward group hugs that you and Koa don't want to be in. "
                    " But Temero was holding on pretty tight, so... "
                    tm " This is gonna be the best note taking session ever! "
                    k  " ...Yeah. "
                    scene black with dissolve
                    " You spent the rest of the break copying Temero's notes. "
                    " Her notes actually looked pretty nice... "
                    " It's got full explanations but the important parts are highlighted with pink highlighter. "
                    " Also got some stickers here and there in her notebook. "
                    " ...And her notebook smelt like failed experiments. Not sure how you could tell, "
                    " Just it was just a strong feeling or something. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump thealthclass1
                " I dunno ":
                    $ temerolv += 5
                    k " ... "
                    tm " Oh riiiight, Orchid was talking with Spark. "
                    tm " Spark told me about this game he wanted to show them. "
                    tm " Since Orchid was big into horror, he thought they'd be real into it. "
                    k " Huh...Orchid IS into horror. "
                    k " It's good that Orchid's interacting with Spark now though. "
                    k " But, if it turns out that Orchid isn't comfortable with him... "
                    tm " Yeah, yeah I know. "
                    tm " You wanna protect 'em cause they're like family to you. "
                    tm " No need to throw paragraphs at me. "
                    k " ... "
                    tm " Anywayyy, I'm pretty sure [name] would like to hang out with us. "
                    tm " Would be good for [them] since they could also take notes from MY notes. "
                    tm " Cmere, [name]!! "
                    " You couldn't even say anything and you were pulled down onto the ground with Temero and Koa. "
                    " It was basically one of those awkward group hugs that you and Koa don't want to be in. "
                    " But Temero was holding on pretty tight, so... "
                    tm " This is gonna be the best note taking session ever! "
                    k  " ...Yeah. "
                    scene black with dissolve
                    " You spent the rest of the break copying Temero's notes. "
                    " Her notes actually looked pretty nice... "
                    " It's got full explanations but the important parts are highlighted with pink highlighter. "
                    " Also got some stickers here and there in her notebook. "
                    " ...And her notebook smelt like failed experiments. Not sure how you could tell, "
                    " Just it was just a strong feeling or something. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump thealthclass1
        else:
            x " - And that's why we need to use different needles instead of the same ones! "
            x " Write that down into your notes. "
            x " ... "
            " You greeted them politely before asking them what they're doing. "
            x " Oh heeey, [name]! "
            $ temeroknow = True
            tm " It's me, the great Temero NEO - and I was...uh... "
            tm " (what wasI gonna say again.) "
            tm " (oh right.) "
            $ koaknow = True
            tm " I was just letting Koa over here copy my notes. "
            tm " Turns out he got a little distracted in class. "
            tm " Mister Clio would kill you for that, Koa. "
            k " ...I know. "
            k " Orchid was just sending me some notes. "
            tm " Ohooo...now you're blaming it on your friend? "
            tm " That's pretty rudeof you, Koa. "
            hide koaneutral at bottom
            show koaangry at right
            k " I'm not... blaming Orchid. "
            k " I was just simply giving you a reason on why I wasn't paying attention... "
            k " I didn't mean it in that way. "
            tm " Yeah, alright. "
            hide koaangry at bottom
            show koaneutral at right
            tm " How's Orchid anyway? "
            tm " They been actually making friends, or...? "
            k " I'm pretty sure that he has. "
            k " [name] - has Orchid been making more friends...? "
            menu:
                " Saw them talking with someone at the front of the school ":
                    $ koalv += 5
                    $ temerolv += 5
                    k " Really..? "
                    k " That's wonderful to hear, then. "
                    k " Unless if that person is someone who isn't from this school of course. "
                    k " I'm going to get really concerned if that's the case. "
                    tm " Oh riiiight, Orchid was talking with Spark. "
                    tm " Spark told me about this game he wanted to show them. "
                    tm " Since Orchid was big into horror, he thought they'd be real into it. "
                    k " Huh...Orchid IS into horror. "
                    k " It's good that Orchid's interacting with Spark now though. "
                    k " But, if it turns out that Orchid isn't comfortable with him... "
                    tm " Yeah, yeah I know. "
                    tm " You wanna protect 'em cause they're like family to you. "
                    tm " No need to throw paragraphs at me. "
                    k " ... "
                    tm " Anywayyy, I'm pretty sure [name] would like to hang out with us. "
                    tm " Would be good for [them] since they could also take notes from MY notes. "
                    tm " Cmere, [name]!! "
                    " You couldn't even say anything and you were pulled down onto the ground with Temero and Koa. "
                    " It was basically one of those awkward group hugs that you and Koa don't want to be in. "
                    " But Temero was holding on pretty tight, so... "
                    tm " This is gonna be the best note taking session ever! "
                    k  " ...Yeah. "
                    scene black with dissolve
                    " You spent the rest of the break copying Temero's notes. "
                    " Her notes actually looked pretty nice... "
                    " It's got full explanations but the important parts are highlighted with pink highlighter. "
                    " Also got some stickers here and there in her notebook. "
                    " ...And her notebook smelt like failed experiments. Not sure how you could tell, "
                    " Just it was just a strong feeling or something. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump thealthclass1
                " I dunno ":
                    $ temerolv += 5
                    k " ... "
                    tm " Oh riiiight, Orchid was talking with Spark. "
                    tm " Spark told me about this game he wanted to show them. "
                    tm " Since Orchid was big into horror, he thought they'd be real into it. "
                    k " Huh...Orchid IS into horror. "
                    k " It's good that Orchid's interacting with Spark now though. "
                    k " But, if it turns out that Orchid isn't comfortable with him... "
                    tm " Yeah, yeah I know. "
                    tm " You wanna protect 'em cause they're like family to you. "
                    tm " No need to throw paragraphs at me. "
                    k " ... "
                    tm " Anywayyy, I'm pretty sure [name] would like to hang out with us. "
                    tm " Would be good for [them] since they could also take notes from MY notes. "
                    tm " Cmere, [name]!! "
                    " You couldn't even say anything and you were pulled down onto the ground with Temero and Koa. "
                    " It was basically one of those awkward group hugs that you and Koa don't want to be in. "
                    " But Temero was holding on pretty tight, so... "
                    tm " This is gonna be the best note taking session ever! "
                    k  " ...Yeah. "
                    scene black with dissolve
                    " You spent the rest of the break copying Temero's notes. "
                    " Her notes actually looked pretty nice... "
                    " It's got full explanations but the important parts are highlighted with pink highlighter. "
                    " Also got some stickers here and there in her notebook. "
                    " ...And her notebook smelt like failed experiments. Not sure how you could tell, "
                    " Just it was just a strong feeling or something. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump thealthclass1
    label octhursgym1:
        # jacob and matte
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked into the gym and found two of your classmates doing their own things. "
        " You wanted to talk to them...but who do you talk to? "
        if matteknow == True and jacobknow == True:
            menu:
                " {image=matteicon} Matte {image=matteicon} ":
                    jump sixhundredmenlol
                " {image=jacobicon} Jacob {image=jacobicon} ":
                    jump sixhundredstrikelol
        elif matteknow == True and jacobknow == False:
            menu:
                " {image=matteicon} Matte {image=matteicon} ":
                    jump sixhundredmenlol
                " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                    jump sixhundredstrikelol
        elif matteknow == False and jacobknow == True:
            menu:
                " {image=matteicon} An artsy looking girl {image=matteicon} ":
                    jump sixhundredmenlol
                " {image=jacobicon} Jacob {image=jacobicon} ":
                    jump sixhundredstrikelol
        else:
            menu:
                " {image=matteicon} An artsy looking girl {image=matteicon} ":
                    jump sixhundredmenlol
                " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                    jump sixhundredstrikelol
        label sixhundredmenlol:
            show matteneutral at center with easeinleft
            if matteknow == True:
                " You walked over to her and asked what she was doing. "
                ma " Hm? oh, [name]! "
                ma " Sorry...just like... "
                hide matteneutral at bottom
                show mattesad at center
                ma " Do you ever take a good look at a room and decide it needs redesigning? "
                ma " Because I've thought of that more than once in this school! "
                ma " I've thought of it for certain club rooms... "
                ma " Classrooms here and there... "
                ma " Even the god dang rooftop for crying out loud! "
                ma " It just feels like something's missing, you know? "
                ma " Even if it's supposed to look simplistic, "
                ma " I can't help but think that a poster would be good right there... "
                ma " Or a vase with plants in it would be good over there! "
                ma " Sighhh... I know that the school probably won't accept ideas, but... "
                ma " I still think that a little more decorating would be good! "
                hide mattesad at bottom
                show matteneutral at center
                ma " Aaaah, the life of an artist... "
                ma " A nice one, but a painful one. "
                ma " By painful I mean...um... "
                ma " Let me put it to you in this way. "
                ma " You're painting out your day - "
                ma " Everything's good, the canvas is good... "
                hide matteneutral at bottom
                show matteangry at center
                ma " Until you fuck up and the line you're making is slightly wonky. "
                ma " Or whenever you're coloring something and you accidentally color outside of the lines. "
                ma " That really pisses me off. "
                ma " A bad day is basically like fucking up a masterpiece to me, in a way. "
                ma " I know some days just can't be perfect, but... "
                ma " I just want it to be that way so that I don't have to worry about anything. "
                ma " A bad day just gets me more stressed and I can't really think clearly. "
                hide matteangry at bottom
                show matteneutral at center
                ma " Thanks for listening me talking about random shit though. "
                ma " Just needed to tell you about some stuff I'm feeling about. "
                ma " Now we could actually get to a topic you might wanna hear... "
                ma " Hm...I heard something's going on with Spark and Temero. "
                ma " Not sure what, but they're acting a little off. "
                ma " I don't wanna get too into what they're doing though. "
                scene black with dissolve
                " You spent the rest of the break talking with Matte. "
                " That situation with Spark and Temero got you pretty interested... "
                " Best not to look too much into it though. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom after a good bit. "
                pause 2.0
                jump thealthclass1
            else:
                " You walked over to her and asked what she was doing. "
                x " Hm? oh, [name]! "
                $ matteknow = True
                ma " Don't think I ever got to introduce myself before, so... I'm Matte! "
                ma " We're classmates, and uh...hrm. "
                ma " Sorry...just like... "
                hide matteneutral at bottom
                show mattesad at center
                ma " Do you ever take a good look at a room and decide it needs redesigning? "
                ma " Because I've thought of that more than once in this school! "
                ma " I've thought of it for certain club rooms... "
                ma " Classrooms here and there... "
                ma " Even the god dang rooftop for crying out loud! "
                ma " It just feels like something's missing, you know? "
                ma " Even if it's supposed to look simplistic, "
                ma " I can't help but think that a poster would be good right there... "
                ma " Or a vase with plants in it would be good over there! "
                ma " Sighhh... I know that the school probably won't accept ideas, but... "
                ma " I still think that a little more decorating would be good! "
                hide mattesad at bottom
                show matteneutral at center
                ma " Aaaah, the life of an artist... "
                ma " A nice one, but a painful one. "
                ma " By painful I mean...um... "
                ma " Let me put it to you in this way. "
                ma " You're painting out your day - "
                ma " Everything's good, the canvas is good... "
                hide matteneutral at bottom
                show matteangry at center
                ma " Until you fuck up and the line you're making is slightly wonky. "
                ma " Or whenever you're coloring something and you accidentally color outside of the lines. "
                ma " That really pisses me off. "
                ma " A bad day is basically like fucking up a masterpiece to me, in a way. "
                ma " I know some days just can't be perfect, but... "
                ma " I just want it to be that way so that I don't have to worry about anything. "
                ma " A bad day just gets me more stressed and I can't really think clearly. "
                hide matteangry at bottom
                show matteneutral at center
                ma " Thanks for listening me talking about random shit though. "
                ma " Just needed to tell you about some stuff I'm feeling about. "
                ma " Now we could actually get to a topic you might wanna hear... "
                ma " Hm...I heard something's going on with Spark and Temero. "
                ma " Not sure what, but they're acting a little off. "
                ma " I don't wanna get too into what they're doing though. "
                scene black with dissolve
                " You spent the rest of the break talking with Matte. "
                " That situation with Spark and Temero got you pretty interested... "
                " Best not to look too much into it though. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your classroom after a good bit. "
                pause 2.0
                jump thealthclass1
        label sixhundredstrikelol:
            show jacobneutral at center with easeinright
            if jacobknow == True:
                " You walked over to him and asked what he was doing. "
                jac " Huh?- oh, you. "
                jac " Was just thinking about a few things... "
                jac " Have you noticed that two of our classmates is acting weird? "
                jac " I dunno, they're acting more friendly and energetic today. "
                jac " Gets me feeling weird and all that. "
                jac " They're usually not that talkative... "
                " You asked him who he was talking about. "
                " Must be someone you're close with...or not. "
                jac " Spark and Temero - you know them, right? "
                jac " Spark is the guy with antennas. Temero is the one with a butterfly bow. "
                jac " They've been weirding me out for awhile now... "
                jac " I dunno - they just get my guts feeling weird. "
                " You told him that they're probably just in a good mood. "
                " Something good must've happened for them to be acting so cheery. "
                " That's probably the reason why. "
                jac " Even if they're happy - Spark would NOT be that talkative. "
                jac " I know he's a chill guy, but he mostly speaks whenever he's spoken to. "
                jac " Or whenever there's something that he needs to talk about. "
                jac " And Temero? that girl was weird in the first place. "
                jac " But her acting overly energetic? that's even weirder. "
                jac " It takes awhile for you to actually notice that they're acting weird. "
                jac " And I've been here awhile AWHILE. "
                jac " That's how I've noticed. "
                jac " I know it might seem weird that I take a good look at people and how they act... "
                jac " But people who know them well can tell easily that they're acting weird. "
                jac " Sorry if I sound real...off to you. "
                jac " This is just ticking me off a whole lot. "
                jac " Just felt like talking about this to you. "
                jac " Hope I didn't annoy you. "
                jac " Or, something. "
                menu:
                    " You didn't annoy me at all ":
                        $ jacoblv += 10
                        jac " Oh, uh.. "
                        jac " Really? "
                        jac " Wasn't expecting for you to say that, actually. "
                        jac " But thanks for saying that. "
                        jac " Glad to hear I'm not annoying you or whatever. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Jacob. "
                        " Just talking about whatever with him. "
                        " You're thinking about the whole Spark and Temero thing though... "
                        " Wonder what's up with them. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You got out of the gym and you walked back to your classroom. "
                        pause 2.0
                        jump thealthclass1
                    " You're fine ":
                        $ jacoblv += 5
                        jac " Wasn't expecting for you to say that, actually. "
                        jac " But thanks for saying that. "
                        jac " Glad to hear I'm not annoying you or whatever. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Jacob. "
                        " Just talking about whatever with him. "
                        " You're thinking about the whole Spark and Temero thing though... "
                        " Wonder what's up with them. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You got out of the gym and you walked back to your classroom. "
                        pause 2.0
                        jump thealthclass1
            else:
                " You walked over to him and asked what he was doing. "
                x " Huh?- oh, you. "
                x " I don't think I've introduced myself to you or something before. "
                x " Guess I should do that right now... "
                $ jacobknow = True
                jac " I'm Jacob. Your clasmate. And I was just, uh... "
                jac " Was just thinking about a few things... "
                jac " Have you noticed that two of our classmates is acting weird? "
                jac " I dunno, they're acting more friendly and energetic today. "
                jac " Gets me feeling weird and all that. "
                jac " They're usually not that talkative... "
                " You asked him who he was talking about. "
                " Must be someone you're close with...or not. "
                jac " Spark and Temero - you know them, right? "
                jac " Spark is the guy with antennas. Temero is the one with a butterfly bow. "
                jac " They've been weirding me out for awhile now... "
                jac " I dunno - they just get my guts feeling weird. "
                " You told him that they're probably just in a good mood. "
                " Something good must've happened for them to be acting so cheery. "
                " That's probably the reason why. "
                jac " Even if they're happy - Spark would NOT be that talkative. "
                jac " I know he's a chill guy, but he mostly speaks whenever he's spoken to. "
                jac " Or whenever there's something that he needs to talk about. "
                jac " And Temero? that girl was weird in the first place. "
                jac " But her acting overly energetic? that's even weirder. "
                jac " It takes awhile for you to actually notice that they're acting weird. "
                jac " And I've been here awhile AWHILE. "
                jac " That's how I've noticed. "
                jac " I know it might seem weird that I take a good look at people and how they act... "
                jac " But people who know them well can tell easily that they're acting weird. "
                jac " Sorry if I sound real...off to you. "
                jac " This is just ticking me off a whole lot. "
                jac " Just felt like talking about this to you. "
                jac " Hope I didn't annoy you. "
                jac " Or, something. "
                menu:
                    " You didn't annoy me at all ":
                        $ jacoblv += 10
                        jac " Oh, uh.. "
                        jac " Really? "
                        jac " Wasn't expecting for you to say that, actually. "
                        jac " But thanks for saying that. "
                        jac " Glad to hear I'm not annoying you or whatever. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Jacob. "
                        " Just talking about whatever with him. "
                        " You're thinking about the whole Spark and Temero thing though... "
                        " Wonder what's up with them. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You got out of the gym and you walked back to your classroom. "
                        pause 2.0
                        jump thealthclass1
                    " You're fine ":
                        $ jacoblv += 5
                        jac " Wasn't expecting for you to say that, actually. "
                        jac " But thanks for saying that. "
                        jac " Glad to hear I'm not annoying you or whatever. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Jacob. "
                        " Just talking about whatever with him. "
                        " You're thinking about the whole Spark and Temero thing though... "
                        " Wonder what's up with them. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You got out of the gym and you walked back to your classroom. "
                        pause 2.0
                        jump thealthclass1
    label octhurscafeteria1:
        # nox and carmen
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked into the cafeteria and found two of your classmates doing their own things. "
        " You wanted to talk to them...but who do you talk to? "
        if noxknow == True and carmenknow == True:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump magicpuppies
                " {image=carmenicon} Carmen {image=carmenicon} ":
                    jump magiccats
        elif noxknow == True and carmenknow == False:
            menu:
                " {image=noxicon} A sleepy guy {image=noxicon} ":
                    jump magicpuppies
                " {image=carmenicon} Carmen {image=carmenicon} ":
                    jump magiccats
        elif noxknow == False and carmenknow == True:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump magicpuppies
                " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                    jump magiccats
        else:
            menu:
                " {image=noxicon} A sleepy guy {image=noxicon} ":
                    jump magicpuppies
                " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                    jump magiccats
        label magicpuppies:
            show noxneutral at center with easeinright
            if noxknow == True:
                " You walked up to him and asked him if he was feeling alright. "
                n " Huh...? "
                n " Oh, it's you... "
                n " I'm feeling alright, yes... "
                n " Someone actually managed to remind me to take my meds... "
                n " I think I'll be able to last for the entire day now... "
                n " Without sleeping in class, of course. "
                n " I just need to remember when I need to take meds again... "
                n " If I forget, then I'd most likely just pass out... "
                n " And I don't want that to be happening... "
                n " What if I fall asleep in the middle of a presentation...? "
                n " That would be too embarrassing... "
                n " I don't want to embarrass myself... "
                n " ...Well, I'm pretty sure everyone else doesn't... "
                n " But more importantly, I don't want anyone to worry over me... "
                n " People worrying about me makes me feel...sad... "
                n " ...Sad that I couldn't take care of myself better so that they don't have to worry... "
                n " I try to be better, but really.. "
                n " I keep on forgetting and forgetting... "
                hide noxneutral at bottom
                show noxsad at center
                n " And the more I forget... "
                n " The more worried everyone gets... "
                n " I don't want to keep worrying everyone like this... "
                menu:
                    " It's not your fault that you can't remember ":
                        $ noxlv += 10
                        n " Is it really...? "
                        n " I don't think so, but... "
                        n " Thanks for your words. "
                        hide noxsad at bottom
                        show noxneutral at center
                        " You comforted Nox for a little bit longer. "
                        " He really looked like he needed your company. "
                        " Despite not knowing eachother for that long, he looked comfortable. "
                        " That's a nice thing to know. "
                        " You then told him that he could set up a reminder on his phone to take his meds. "
                        " If he didn't know how to do that, then you could help him set it up. "
                        n " O...kay... "
                        n " I'll lend you my phone, since I don't know how to do that stuff... "
                        n " Here... "
                        " Nox gave you his phone and you started setting everything up. "
                        " You noticed that he had a picture of himself and someone else that you don't recognize as his keyboard... "
                        " Must be an old classmate of his. "
                        " You eventually finish setting everything up and you gave him back his phone. "
                        n " Thanks, [name]... "
                        n " I appreciate you doing this stuff for me... "
                        n " (I don't know why I haven't thought of putting up a reminder yet, until now...) "
                        n " (Hm...) "
                        scene black with dissolve
                        " You spent the rest of the break talking with Nox. "
                        " Just talking about stuff... "
                        " You asked about the guy in the keyboard photo, and you were right. "
                        " It was an old friend, but Nox wouldn't want to get deeper into the topic. "
                        " You respected that he didn't want to though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, looks like it's time for your next class. "
                        " You walked out of the cafeteria and went to your classroom after a bit. "
                        pause 2.0
                        jump thealthclass1
                    " It's okay ":
                        n " Is it really...? "
                        n " I don't think so, but... "
                        n " Thanks for your words. "
                        hide noxsad at bottom
                        show noxneutral at center
                        " You comforted Nox for a little bit longer. "
                        " He really looked like he needed your company. "
                        " Despite not knowing eachother for that long, he looked comfortable. "
                        " That's a nice thing to know. "
                        " You then told him that he could set up a reminder on his phone to take his meds. "
                        " If he didn't know how to do that, then you could help him set it up. "
                        n " O...kay... "
                        n " I'll lend you my phone, since I don't know how to do that stuff... "
                        n " Here... "
                        " Nox gave you his phone and you started setting everything up. "
                        " You noticed that he had a picture of himself and someone else that you don't recognize as his keyboard... "
                        " Must be an old classmate of his. "
                        " You eventually finish setting everything up and you gave him back his phone. "
                        n " Thanks, [name]... "
                        n " I appreciate you doing this stuff for me... "
                        n " (I don't know why I haven't thought of putting up a reminder yet, until now...) "
                        n " (Hm...) "
                        scene black with dissolve
                        " You spent the rest of the break talking with Nox. "
                        " Just talking about stuff... "
                        " You asked about the guy in the keyboard photo, and you were right. "
                        " It was an old friend, but Nox wouldn't want to get deeper into the topic. "
                        " You respected that he didn't want to though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, looks like it's time for your next class. "
                        " You walked out of the cafeteria and went to your classroom after a bit. "
                        pause 2.0
                        jump thealthclass1
            else:
                " You walked up to him and asked him if he was feeling alright. "
                x " Huh...? "
                x " Oh, it's you... "
                $ noxknow = True
                n " I'm Nox...Nox Cesso...and, um... "
                n " I'm feeling alright, yes... "
                n " Someone actually managed to remind me to take my meds... "
                n " I think I'll be able to last for the entire day now... "
                n " Without sleeping in class, of course. "
                n " I just need to remember when I need to take meds again... "
                n " If I forget, then I'd most likely just pass out... "
                n " And I don't want that to be happening... "
                n " What if I fall asleep in the middle of a presentation...? "
                n " That would be too embarrassing... "
                n " I don't want to embarrass myself... "
                n " ...Well, I'm pretty sure everyone else doesn't... "
                n " But more importantly, I don't want anyone to worry over me... "
                n " People worrying about me makes me feel...sad... "
                n " ...Sad that I couldn't take care of myself better so that they don't have to worry... "
                n " I try to be better, but really.. "
                n " I keep on forgetting and forgetting... "
                hide noxneutral at bottom
                show noxsad at center
                n " And the more I forget... "
                n " The more worried everyone gets... "
                n " I don't want to keep worrying everyone like this... "
                menu:
                    " It's not your fault that you can't remember ":
                        $ noxlv += 10
                        n " Is it really...? "
                        n " I don't think so, but... "
                        n " Thanks for your words. "
                        hide noxsad at bottom
                        show noxneutral at center
                        " You comforted Nox for a little bit longer. "
                        " He really looked like he needed your company. "
                        " Despite not knowing eachother for that long, he looked comfortable. "
                        " That's a nice thing to know. "
                        " You then told him that he could set up a reminder on his phone to take his meds. "
                        " If he didn't know how to do that, then you could help him set it up. "
                        n " O...kay... "
                        n " I'll lend you my phone, since I don't know how to do that stuff... "
                        n " Here... "
                        " Nox gave you his phone and you started setting everything up. "
                        " You noticed that he had a picture of himself and someone else that you don't recognize as his keyboard... "
                        " Must be an old classmate of his. "
                        " You eventually finish setting everything up and you gave him back his phone. "
                        n " Thanks, [name]... "
                        n " I appreciate you doing this stuff for me... "
                        n " (I don't know why I haven't thought of putting up a reminder yet, until now...) "
                        n " (Hm...) "
                        scene black with dissolve
                        " You spent the rest of the break talking with Nox. "
                        " Just talking about stuff... "
                        " You asked about the guy in the keyboard photo, and you were right. "
                        " It was an old friend, but Nox wouldn't want to get deeper into the topic. "
                        " You respected that he didn't want to though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, looks like it's time for your next class. "
                        " You walked out of the cafeteria and went to your classroom after a bit. "
                        pause 2.0
                        jump thealthclass1
                    " It's okay ":
                        n " Is it really...? "
                        n " I don't think so, but... "
                        n " Thanks for your words. "
                        hide noxsad at bottom
                        show noxneutral at center
                        " You comforted Nox for a little bit longer. "
                        " He really looked like he needed your company. "
                        " Despite not knowing eachother for that long, he looked comfortable. "
                        " That's a nice thing to know. "
                        " You then told him that he could set up a reminder on his phone to take his meds. "
                        " If he didn't know how to do that, then you could help him set it up. "
                        n " O...kay... "
                        n " I'll lend you my phone, since I don't know how to do that stuff... "
                        n " Here... "
                        " Nox gave you his phone and you started setting everything up. "
                        " You noticed that he had a picture of himself and someone else that you don't recognize as his keyboard... "
                        " Must be an old classmate of his. "
                        " You eventually finish setting everything up and you gave him back his phone. "
                        n " Thanks, [name]... "
                        n " I appreciate you doing this stuff for me... "
                        n " (I don't know why I haven't thought of putting up a reminder yet, until now...) "
                        n " (Hm...) "
                        scene black with dissolve
                        " You spent the rest of the break talking with Nox. "
                        " Just talking about stuff... "
                        " You asked about the guy in the keyboard photo, and you were right. "
                        " It was an old friend, but Nox wouldn't want to get deeper into the topic. "
                        " You respected that he didn't want to though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, looks like it's time for your next class. "
                        " You walked out of the cafeteria and went to your classroom after a bit. "
                        pause 2.0
                        jump thealthclass1
        label magiccats:
            show carmenneutral at center with easeinleft
            if carmenknow == True:
                " You walked up to him and asked him what he was doing. "
                hide carmenneutral at bottom
                show carmenhappy at center
                ca " ...?...!! "
                " He waves at you energetically. "
                " Looks like someone's happy today... "
                " You ask him: what's up? "
                ca " ...!! "
                " He starts getting even more excited. "
                " He couldn't really put his excitement into words, so... "
                " He showed you a photo on his phone. "
                " It was a photo about a band coming in this town for a performance. "
                " Looks like Carmen is a huge fan of this band... "
                " And it looks like he already got tickets too. "
                " You look at when they're coming, annd...it's on saturday next week. "
                " Interesting. Maybe you could get yourself tickets too... "
                " But you haven't even heard of their music before - {nw} "
                " Carmen started rapidly shaking you out of pure joy. "
                ca " !!! "
                " Wow, looks like he's really happy. "
                " Eventually, you calmed him down and stopped him from shaking you further. "
                " You feel like your brain and your eyes just rearranged from the shaking. "
                " Not literally, but it sure did feel like it. "
                hide carmenhappy at bottom
                show carmenneutral at center
                ca " ... "
                " Carmen signs 'sorry' and scratches the back of his head. "
                " Looks like he's a little embarrassed for getting too excited now... "
                " You reassure him that it was alright though. "
                " After all, you'd get excited too if your favorite band came over. "
                " If you even had one, that is. "
                ca " ... "
                " Carmen felt a little better, but he still felt a little bit bad. "
                " Now he's thinking about something else... "
                " You ask him if he's doing alright. "
                hide carmenneutral at bottom
                show carmensad at center
                ca " ... "
                " He knows this is gonna sound a little off since you two just met a few days ago, but... "
                " He needed to let out some emotions he's feeling right now. "
                " He tells you in sign language that he desperately wants to be able to speak. "
                " But, you know...he can't because that's just the way he is. "
                " He wanted to talk with you normally. "
                " To show you his excitement. To talk to you about his anger. To be able to feel like someone normal. "
                " But he can't, and all he can do is let out signs and songs that showcase his feelings. "
                " It frustrates him that he can't be like everyone else. "
                " Always having to do complicated things just to talk. "
                " Just to make others understand him. "
                " He got used to the feeling of not talking, but it's still frustrating. "
                menu:
                    " I'll always stay your friend, without your voice or with it ":
                        $ carmenlv += 10
                        ca " ... "
                        " Carmen said he felt better, but also still felt a little bad. "
                        " Not knowing what to do, you suggested talking about something else. "
                        " Just to get everything off of his mind. "
                        hide carmensad at bottom
                        show carmenneutral at center
                        ca " ... "
                        " Looks like he liked that idea. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Carmen. "
                        " Just talking about random stuff... "
                        " Like about the band Carmen mentioned earlier. "
                        " The band sounded pretty interesting. "
                        " And also had a badass name. "
                        " Maybe you should check them out sometime... "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You walked out of the cafeteria and then went to your classroom after a good bit. "
                        pause 2.0
                        jump thealthclass1
                    " *Stay silent* ":
                        ca " ... "
                        " You and Carmen just stay still there. "
                        " Now Carmen kinda felt bad for letting all of that out on you. "
                        " Well this is getting awkwrd. "
                        " You decided to talk to him about something else instead. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Carmen. "
                        " Just talking about random stuff... "
                        " Like about the band Carmen mentioned earlier. "
                        " The band sounded pretty interesting. "
                        " And also had a badass name. "
                        " Maybe you should check them out sometime... "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You walked out of the cafeteria and then went to your classroom after a good bit. "
                        pause 2.0
                        jump thealthclass1
            else:
                " Oh hey, you've heard of this kid before. "
                $ carmenknow = True
                " His name is Carmen - and he's a mute guy who likes the guitar. "
                " He can somehow speak in guitar - no one knows how, but they don't question it. "
                " And he can also speak in sign language, of course. "
                " You walked up to him and asked him what he was doing. "
                hide carmenneutral at bottom
                show carmenhappy at center
                ca " ...?...!! "
                " He waves at you energetically. "
                " Looks like someone's happy today... "
                " You ask him: what's up? "
                ca " ...!! "
                " He starts getting even more excited. "
                " He couldn't really put his excitement into words, so... "
                " He showed you a photo on his phone. "
                " It was a photo about a band coming in this town for a performance. "
                " Looks like Carmen is a huge fan of this band... "
                " And it looks like he already got tickets too. "
                " You look at when they're coming, annd...it's on saturday next week. "
                " Interesting. Maybe you could get yourself tickets too... "
                " But you haven't even heard of their music before - {nw} "
                " Carmen started rapidly shaking you out of pure joy. "
                ca " !!! "
                " Wow, looks like he's really happy. "
                " Eventually, you calmed him down and stopped him from shaking you further. "
                " You feel like your brain and your eyes just rearranged from the shaking. "
                " Not literally, but it sure did feel like it. "
                hide carmenhappy at bottom
                show carmenneutral at center
                ca " ... "
                " Carmen signs 'sorry' and scratches the back of his head. "
                " Looks like he's a little embarrassed for getting too excited now... "
                " You reassure him that it was alright though. "
                " After all, you'd get excited too if your favorite band came over. "
                " If you even had one, that is. "
                ca " ... "
                " Carmen felt a little better, but he still felt a little bit bad. "
                " Now he's thinking about something else... "
                " You ask him if he's doing alright. "
                hide carmenneutral at bottom
                show carmensad at center
                ca " ... "
                " He knows this is gonna sound a little off since you two just met a few days ago, but... "
                " He needed to let out some emotions he's feeling right now. "
                " He tells you in sign language that he desperately wants to be able to speak. "
                " But, you know...he can't because that's just the way he is. "
                " He wanted to talk with you normally. "
                " To show you his excitement. To talk to you about his anger. To be able to feel like someone normal. "
                " But he can't, and all he can do is let out signs and songs that showcase his feelings. "
                " It frustrates him that he can't be like everyone else. "
                " Always having to do complicated things just to talk. "
                " Just to make others understand him. "
                " He got used to the feeling of not talking, but it's still frustrating. "
                menu:
                    " I'll always stay your friend, without your voice or with it ":
                        $ carmenlv += 10
                        ca " ... "
                        " Carmen said he felt better, but also still felt a little bad. "
                        " Not knowing what to do, you suggested talking about something else. "
                        " Just to get everything off of his mind. "
                        hide carmensad at bottom
                        show carmenneutral at center
                        ca " ... "
                        " Looks like he liked that idea. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Carmen. "
                        " Just talking about random stuff... "
                        " Like about the band Carmen mentioned earlier. "
                        " The band sounded pretty interesting. "
                        " And also had a badass name. "
                        " Maybe you should check them out sometime... "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You walked out of the cafeteria and then went to your classroom after a good bit. "
                        pause 2.0
                        jump thealthclass1
                    " *Stay silent* ":
                        ca " ... "
                        " You and Carmen just stay still there. "
                        " Now Carmen kinda felt bad for letting all of that out on you. "
                        " Well this is getting awkwrd. "
                        " You decided to talk to him about something else instead. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Carmen. "
                        " Just talking about random stuff... "
                        " Like about the band Carmen mentioned earlier. "
                        " The band sounded pretty interesting. "
                        " And also had a badass name. "
                        " Maybe you should check them out sometime... "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You walked out of the cafeteria and then went to your classroom after a good bit. "
                        pause 2.0
                        jump thealthclass1
    label octhursrooftop1:
        # disk and jam
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked to the rooftop and spotted two of your classmates talking. "
        " Wondering what they were talking about, you walked over to them. "
        " Let's go ahead and join their wonderful conversation they're having. "
        show diskneutral at left with easeinright
        show jamneutral at right with easeinright
        if diskknow == True and jamknow == True:
            hide diskneutral at bottom
            show diskhappy at left
            d " Hiya there, [name]!! "
            ja " Oh - uh...hey there. "
            " You greeted the both of them politely. "
            " Being ever-so curious, you asked them what they were talkin about. "
            hide diskhappy at bottom
            show diskneutral at left
            d " Oh, we were just talking about random stuff! "
            d " Like, did you know Mister Sol got a little flabbergasted when Jam arrived? "
            ja " ...Why was that, again? "
            d " He told me that you looked like my long lost sibling! "
            ja " I mean, I can see why, I guess. "
            ja " It's just that I'm a little bit lighter than you. "
            d " Oh - and same goes for that one guy... "
            d " What's his name again? the grumpy twin? "
            ja " Yinhui? "
            ja " Dude, he looks way different. "
            ja " How come your uncle got flabbergasted at that? "
            d " Hehe - don't know, he's just like that, really!! "
            d " He thinks of the weirdest things, actually... "
            d " While he was visiting the mansion, he asked for hotdogs from the chefs... "
            d " But to make it not hot and without the dogs. "
            ja " ...Sounds like your average uncle activity... "
            d " RIGHT?? the chefs just gave him icecream though. "
            d " And turns out, that's exactly what he wanted?? "
            d " I mean, if you wanted icecream - you could totally just say that instead of...you know... "
            ja " Uh huh. "
            ja " Oh yeah, I just remembered something... "
            ja " When are you gonna give those flowers to that one guy that you like? "
            d " Huh? Oh, Abbie? "
            hide diskneutral at bottom
            show diskjoyous at left
            d " I dunnooooo... "
            d " I mean, I gotta find the perfect time to give him the flowers! "
            d " I can't do it right now, obviously... "
            d " Me and Abbie still have class! "
            menu:
                " Give it to him on sunday ":
                    $ disklv += 10
                    ja " Yeah. Why not just...give it to him on sunday? "
                    ja " I'm pretty sure that's the time when both of you are free. "
                    ja " There's no way you haven't thought of going over to him on sunday. "
                    d " ...I actually hadn't thought of that yet! "
                    ja " Oooh my god. "
                    d " But, thanks for the idea, guys!! "
                    d " I'll definitely give the flowers to him on sunday! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Jam. "
                    " Well, mostly listening to Disk talking about Abbie. "
                    " Jesus christ, this guy was madly inlove and he was down BAD. "
                    " You could never relate to this though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You got down from the rooftop and went to your classroom after a bit. "
                    pause 2.0
                    jump thealthclass1
                " *Say nothing* ":
                    d " And I wouldn't want to interrupt his class... "
                    d " Even though I keep on texting him whenever I'm bored in class, hehe... "
                    d " I know I have to pay attention, but why not give Abbie all of my attention instead...? "
                    ja " Oh god, here we go again. "
                    ja " Yes Disk, we know you love Abbie very much. "
                    d " Heheee...he's so cuteeee!! "
                    d " How could I not? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Jam. "
                    " Well, mostly listening to Disk talking about Abbie. "
                    " Jesus christ, this guy was madly inlove and he was down BAD. "
                    " You could never relate to this though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You got down from the rooftop and went to your classroom after a bit. "
                    pause 2.0
                    jump thealthclass1
        elif diskknow == True and jamknow == False:
            hide diskneutral at bottom
            show diskhappy at left
            d " Hiya there, [name]!! "
            $ jamknow = True
            d " I'm Disk! and this is my friend, Jam! "
            ja " Oh - uh...hey there. "
            " You greeted the both of them politely. "
            " Being ever-so curious, you asked them what they were talkin about. "
            hide diskhappy at bottom
            show diskneutral at left
            d " Oh, we were just talking about random stuff! "
            d " Like, did you know Mister Sol got a little flabbergasted when Jam arrived? "
            ja " ...Why was that, again? "
            d " He told me that you looked like my long lost sibling! "
            ja " I mean, I can see why, I guess. "
            ja " It's just that I'm a little bit lighter than you. "
            d " Oh - and same goes for that one guy... "
            d " What's his name again? the grumpy twin? "
            ja " Yinhui? "
            ja " Dude, he looks way different. "
            ja " How come your uncle got flabbergasted at that? "
            d " Hehe - don't know, he's just like that, really!! "
            d " He thinks of the weirdest things, actually... "
            d " While he was visiting the mansion, he asked for hotdogs from the chefs... "
            d " But to make it not hot and without the dogs. "
            ja " ...Sounds like your average uncle activity... "
            d " RIGHT?? the chefs just gave him icecream though. "
            d " And turns out, that's exactly what he wanted?? "
            d " I mean, if you wanted icecream - you could totally just say that instead of...you know... "
            ja " Uh huh. "
            ja " Oh yeah, I just remembered something... "
            ja " When are you gonna give those flowers to that one guy that you like? "
            d " Huh? Oh, Abbie? "
            hide diskneutral at bottom
            show diskjoyous at left
            d " I dunnooooo... "
            d " I mean, I gotta find the perfect time to give him the flowers! "
            d " I can't do it right now, obviously... "
            d " Me and Abbie still have class! "
            menu:
                " Give it to him on sunday ":
                    $ disklv += 10
                    ja " Yeah. Why not just...give it to him on sunday? "
                    ja " I'm pretty sure that's the time when both of you are free. "
                    ja " There's no way you haven't thought of going over to him on sunday. "
                    d " ...I actually hadn't thought of that yet! "
                    ja " Oooh my god. "
                    d " But, thanks for the idea, guys!! "
                    d " I'll definitely give the flowers to him on sunday! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Jam. "
                    " Well, mostly listening to Disk talking about Abbie. "
                    " Jesus christ, this guy was madly inlove and he was down BAD. "
                    " You could never relate to this though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You got down from the rooftop and went to your classroom after a bit. "
                    pause 2.0
                    jump thealthclass1
                " *Say nothing* ":
                    d " And I wouldn't want to interrupt his class... "
                    d " Even though I keep on texting him whenever I'm bored in class, hehe... "
                    d " I know I have to pay attention, but why not give Abbie all of my attention instead...? "
                    ja " Oh god, here we go again. "
                    ja " Yes Disk, we know you love Abbie very much. "
                    d " Heheee...he's so cuteeee!! "
                    d " How could I not? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Jam. "
                    " Well, mostly listening to Disk talking about Abbie. "
                    " Jesus christ, this guy was madly inlove and he was down BAD. "
                    " You could never relate to this though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You got down from the rooftop and went to your classroom after a bit. "
                    pause 2.0
                    jump thealthclass1
        elif diskknow == False and jamknow == True:
            hide diskneutral at bottom
            show diskhappy at left
            x " Hiya there, [name]!! "
            $ diskknow = True
            d " I'm Disk! and this is my friend, Jam! "
            ja " Oh - uh...hey there. "
            " You greeted the both of them politely. "
            " Being ever-so curious, you asked them what they were talkin about. "
            hide diskhappy at bottom
            show diskneutral at left
            d " Oh, we were just talking about random stuff! "
            d " Like, did you know Mister Sol got a little flabbergasted when Jam arrived? "
            ja " ...Why was that, again? "
            d " He told me that you looked like my long lost sibling! "
            ja " I mean, I can see why, I guess. "
            ja " It's just that I'm a little bit lighter than you. "
            d " Oh - and same goes for that one guy... "
            d " What's his name again? the grumpy twin? "
            ja " Yinhui? "
            ja " Dude, he looks way different. "
            ja " How come your uncle got flabbergasted at that? "
            d " Hehe - don't know, he's just like that, really!! "
            d " He thinks of the weirdest things, actually... "
            d " While he was visiting the mansion, he asked for hotdogs from the chefs... "
            d " But to make it not hot and without the dogs. "
            ja " ...Sounds like your average uncle activity... "
            d " RIGHT?? the chefs just gave him icecream though. "
            d " And turns out, that's exactly what he wanted?? "
            d " I mean, if you wanted icecream - you could totally just say that instead of...you know... "
            ja " Uh huh. "
            ja " Oh yeah, I just remembered something... "
            ja " When are you gonna give those flowers to that one guy that you like? "
            d " Huh? Oh, Abbie? "
            hide diskneutral at bottom
            show diskjoyous at left
            d " I dunnooooo... "
            d " I mean, I gotta find the perfect time to give him the flowers! "
            d " I can't do it right now, obviously... "
            d " Me and Abbie still have class! "
            menu:
                " Give it to him on sunday ":
                    $ disklv += 10
                    ja " Yeah. Why not just...give it to him on sunday? "
                    ja " I'm pretty sure that's the time when both of you are free. "
                    ja " There's no way you haven't thought of going over to him on sunday. "
                    d " ...I actually hadn't thought of that yet! "
                    ja " Oooh my god. "
                    d " But, thanks for the idea, guys!! "
                    d " I'll definitely give the flowers to him on sunday! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Jam. "
                    " Well, mostly listening to Disk talking about Abbie. "
                    " Jesus christ, this guy was madly inlove and he was down BAD. "
                    " You could never relate to this though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You got down from the rooftop and went to your classroom after a bit. "
                    pause 2.0
                    jump thealthclass1
                " *Say nothing* ":
                    d " And I wouldn't want to interrupt his class... "
                    d " Even though I keep on texting him whenever I'm bored in class, hehe... "
                    d " I know I have to pay attention, but why not give Abbie all of my attention instead...? "
                    ja " Oh god, here we go again. "
                    ja " Yes Disk, we know you love Abbie very much. "
                    d " Heheee...he's so cuteeee!! "
                    d " How could I not? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Jam. "
                    " Well, mostly listening to Disk talking about Abbie. "
                    " Jesus christ, this guy was madly inlove and he was down BAD. "
                    " You could never relate to this though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You got down from the rooftop and went to your classroom after a bit. "
                    pause 2.0
                    jump thealthclass1
        else:
            hide diskneutral at bottom
            show diskhappy at left
            x " Hiya there, [name]!! "
            $ diskknow = True
            $ jamknow = True
            d " I'm Disk! and this is my friend, Jam! "
            ja " Oh - uh...hey there. "
            " You greeted the both of them politely. "
            " Being ever-so curious, you asked them what they were talkin about. "
            hide diskhappy at bottom
            show diskneutral at left
            d " Oh, we were just talking about random stuff! "
            d " Like, did you know Mister Sol got a little flabbergasted when Jam arrived? "
            ja " ...Why was that, again? "
            d " He told me that you looked like my long lost sibling! "
            ja " I mean, I can see why, I guess. "
            ja " It's just that I'm a little bit lighter than you. "
            d " Oh - and same goes for that one guy... "
            d " What's his name again? the grumpy twin? "
            ja " Yinhui? "
            ja " Dude, he looks way different. "
            ja " How come your uncle got flabbergasted at that? "
            d " Hehe - don't know, he's just like that, really!! "
            d " He thinks of the weirdest things, actually... "
            d " While he was visiting the mansion, he asked for hotdogs from the chefs... "
            d " But to make it not hot and without the dogs. "
            ja " ...Sounds like your average uncle activity... "
            d " RIGHT?? the chefs just gave him icecream though. "
            d " And turns out, that's exactly what he wanted?? "
            d " I mean, if you wanted icecream - you could totally just say that instead of...you know... "
            ja " Uh huh. "
            ja " Oh yeah, I just remembered something... "
            ja " When are you gonna give those flowers to that one guy that you like? "
            d " Huh? Oh, Abbie? "
            hide diskneutral at bottom
            show diskjoyous at left
            d " I dunnooooo... "
            d " I mean, I gotta find the perfect time to give him the flowers! "
            d " I can't do it right now, obviously... "
            d " Me and Abbie still have class! "
            menu:
                " Give it to him on sunday ":
                    $ disklv += 10
                    ja " Yeah. Why not just...give it to him on sunday? "
                    ja " I'm pretty sure that's the time when both of you are free. "
                    ja " There's no way you haven't thought of going over to him on sunday. "
                    d " ...I actually hadn't thought of that yet! "
                    ja " Oooh my god. "
                    d " But, thanks for the idea, guys!! "
                    d " I'll definitely give the flowers to him on sunday! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Jam. "
                    " Well, mostly listening to Disk talking about Abbie. "
                    " Jesus christ, this guy was madly inlove and he was down BAD. "
                    " You could never relate to this though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You got down from the rooftop and went to your classroom after a bit. "
                    pause 2.0
                    jump thealthclass1
                " *Say nothing* ":
                    d " And I wouldn't want to interrupt his class... "
                    d " Even though I keep on texting him whenever I'm bored in class, hehe... "
                    d " I know I have to pay attention, but why not give Abbie all of my attention instead...? "
                    ja " Oh god, here we go again. "
                    ja " Yes Disk, we know you love Abbie very much. "
                    d " Heheee...he's so cuteeee!! "
                    d " How could I not? "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Jam. "
                    " Well, mostly listening to Disk talking about Abbie. "
                    " Jesus christ, this guy was madly inlove and he was down BAD. "
                    " You could never relate to this though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You got down from the rooftop and went to your classroom after a bit. "
                    pause 2.0
                    jump thealthclass1
    label octhurslibrary1:
        # yanyi and quinn
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked into the library and spotted two of your classmates talking. "
        " Wondering what they were talking about, you walked over to them. "
        show yangyineutral at right with easeinleft
        show quinnneutral at left with easeinleft
        if yangyiknow == True and quinnknow == True:
            q " Hey there, [name]. "
            ya " Hiya, [name]! "
            q " I was just talking to Yangyi about some of my ideas for my play. "
            q " Like adding in more scenes for more context... "
            ya " Wait, Quinn.. "
            ya " Wouldn't that just mean more praciticing and acting? "
            q " ...Well, yes! "
            q " But it's also to make the story more clearer! "
            q " To...you know. "
            q " To not confuse the audience? "
            ya " But adding it in last minute wouldn't be a good thing... "
            ya " It could confuse your club members! "
            ya " Like they would forget which scene comes first... "
            ya " And it would be more easier for them to forget their lines! "
            q " Hm...that is true... "
            q " What do you suggest that I do though? "
            q " I most certainly don't want my club members to fail. "
            q " You know very well that I don't want to make a fool out of myself, Yangyi. "
            ya " Maybe you could give them an explanation on what happens? "
            ya " A short one, of course. "
            ya " Just to give them a quick thing on what happened in that scene. "
            ya " No acting, just you narrating on what happened... "
            ya " ...As your club members get ready for the next scene! "
            ya " A good idea, right? "
            q " Hmm.. "
            q " Yes, that doesn't sound too bad... "
            q " And it's not that major of a change, too. "
            q " I'll do that, then. "
            q " I'm gonna have to tell my club members soon after the next class.. "
            q " Thank you for this idea, Yangyi. "
            ya " You're welcome, Quinn! "
            ya " I'll help you anytime! "
            scene black with dissolve
            " You spent the rest of the break talking with Quinn and Yangyi. "
            " Huh...you wonder what Quinn's play is gonna be about. "
            " You sure hope it's something interesting. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom for the next class. "
            pause 2.0
            jump thealthclass1
        elif yangyiknow == True and quinnknow == False:
            x " Hey there, [name]. "
            ya " Hiya, [name]! "
            $ quinnknow = True
            q " I'm Quinn. Part of the drama club. "
            q " I was just talking to Yangyi about some of my ideas for my play. "
            q " Like adding in more scenes for more context... "
            ya " Wait, Quinn.. "
            ya " Wouldn't that just mean more praciticing and acting? "
            q " ...Well, yes! "
            q " But it's also to make the story more clearer! "
            q " To...you know. "
            q " To not confuse the audience? "
            ya " But adding it in last minute wouldn't be a good thing... "
            ya " It could confuse your club members! "
            ya " Like they would forget which scene comes first... "
            ya " And it would be more easier for them to forget their lines! "
            q " Hm...that is true... "
            q " What do you suggest that I do though? "
            q " I most certainly don't want my club members to fail. "
            q " You know very well that I don't want to make a fool out of myself, Yangyi. "
            ya " Maybe you could give them an explanation on what happens? "
            ya " A short one, of course. "
            ya " Just to give them a quick thing on what happened in that scene. "
            ya " No acting, just you narrating on what happened... "
            ya " ...As your club members get ready for the next scene! "
            ya " A good idea, right? "
            q " Hmm.. "
            q " Yes, that doesn't sound too bad... "
            q " And it's not that major of a change, too. "
            q " I'll do that, then. "
            q " I'm gonna have to tell my club members soon after the next class.. "
            q " Thank you for this idea, Yangyi. "
            ya " You're welcome, Quinn! "
            ya " I'll help you anytime! "
            scene black with dissolve
            " You spent the rest of the break talking with Quinn and Yangyi. "
            " Huh...you wonder what Quinn's play is gonna be about. "
            " You sure hope it's something interesting. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom for the next class. "
            pause 2.0
            jump thealthclass1
        elif yangyiknow == False and quinnknow == True:
            q " Hey there, [name]. "
            x " Hiya, [name]! "
            $ yangyiknow = True
            q " I was just talking to Yangyi about some of my ideas for my play. "
            q " Like adding in more scenes for more context... "
            ya " Wait, Quinn.. "
            ya " Wouldn't that just mean more praciticing and acting? "
            q " ...Well, yes! "
            q " But it's also to make the story more clearer! "
            q " To...you know. "
            q " To not confuse the audience? "
            ya " But adding it in last minute wouldn't be a good thing... "
            ya " It could confuse your club members! "
            ya " Like they would forget which scene comes first... "
            ya " And it would be more easier for them to forget their lines! "
            q " Hm...that is true... "
            q " What do you suggest that I do though? "
            q " I most certainly don't want my club members to fail. "
            q " You know very well that I don't want to make a fool out of myself, Yangyi. "
            ya " Maybe you could give them an explanation on what happens? "
            ya " A short one, of course. "
            ya " Just to give them a quick thing on what happened in that scene. "
            ya " No acting, just you narrating on what happened... "
            ya " ...As your club members get ready for the next scene! "
            ya " A good idea, right? "
            q " Hmm.. "
            q " Yes, that doesn't sound too bad... "
            q " And it's not that major of a change, too. "
            q " I'll do that, then. "
            q " I'm gonna have to tell my club members soon after the next class.. "
            q " Thank you for this idea, Yangyi. "
            ya " You're welcome, Quinn! "
            ya " I'll help you anytime! "
            scene black with dissolve
            " You spent the rest of the break talking with Quinn and Yangyi. "
            " Huh...you wonder what Quinn's play is gonna be about. "
            " You sure hope it's something interesting. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom for the next class. "
            pause 2.0
            jump thealthclass1
        else:
            x " Hey there, [name]. "
            x " Hiya, [name]! "
            $ quinnknow = True
            q " I'm Quinn. Part of the drama club. "
            $ yangyiknow = True
            q " I was just talking to Yangyi about some of my ideas for my play. "
            q " Like adding in more scenes for more context... "
            ya " Wait, Quinn.. "
            ya " Wouldn't that just mean more praciticing and acting? "
            q " ...Well, yes! "
            q " But it's also to make the story more clearer! "
            q " To...you know. "
            q " To not confuse the audience? "
            ya " But adding it in last minute wouldn't be a good thing... "
            ya " It could confuse your club members! "
            ya " Like they would forget which scene comes first... "
            ya " And it would be more easier for them to forget their lines! "
            q " Hm...that is true... "
            q " What do you suggest that I do though? "
            q " I most certainly don't want my club members to fail. "
            q " You know very well that I don't want to make a fool out of myself, Yangyi. "
            ya " Maybe you could give them an explanation on what happens? "
            ya " A short one, of course. "
            ya " Just to give them a quick thing on what happened in that scene. "
            ya " No acting, just you narrating on what happened... "
            ya " ...As your club members get ready for the next scene! "
            ya " A good idea, right? "
            q " Hmm.. "
            q " Yes, that doesn't sound too bad... "
            q " And it's not that major of a change, too. "
            q " I'll do that, then. "
            q " I'm gonna have to tell my club members soon after the next class.. "
            q " Thank you for this idea, Yangyi. "
            ya " You're welcome, Quinn! "
            ya " I'll help you anytime! "
            scene black with dissolve
            " You spent the rest of the break talking with Quinn and Yangyi. "
            " Huh...you wonder what Quinn's play is gonna be about. "
            " You sure hope it's something interesting. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the library and went to your classroom for the next class. "
            pause 2.0
            jump thealthclass1
label thealthclass1:
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    " You walked into the classroom and saw that the health teacher was already there. "
    " Huh, either you're a little late or the teacher was already there. "
    " You looked at the clock in the wall and knew that the teacher was faster than you. "
    " ...That means the teacher was here before you. "
    " Without any further questions, you walked over to your table and took a seat. "
    " Time to pay attention to health... "
    " You should probably start paying attention on your own health too. "
    " Physical, mental, spiritual... "
    " Don't know who needs this message but someone probably does. "
    show altrixneutral at center with easeinleft
    msa " Good morning class! "
    msa " I hope all of you are doing well today... "
    msa " And uh...not sure if any one of you noticed, buuuut... "
    msa " Mister Clio isn't really feeling well today. "
    msa " Make sure to not accidentally tick him off, alright? "
    msa " Otherwise you'd get an earful of greek words... "
    msa " I would know. I've seen him do that before. "
    msa " Miss Sol was messing around with him, and uh...yeah. "
    msa " Before we go completely out of topic though... "
    msa " Let's get right into our lesson! "
    msa " Grab your notebooks so that you could take notes!...obviously... "
    scene black with dissolve
    " You spent the rest of the class hours taking down notes. "
    " Nothing interesting really happened while you were taking down notes. "
    " Looks like everyone was too busy copying, like you were... "
    play sound "audio/bellring.mp3"
    " The bell rings after a little bit, looks like it's time for a break. "
    " You walked out of the classroom after a good bit. "
    pause 2.0
    jump octhursbreak2
label octhursbreak2:
    scene hallway with dissolve
    if sparklv >= 20 or sparklv == 20:
        # spark demon event
        stop music fadeout 1.5
        $ sparkformseen = True
        " As you were about to walk down the hallway to look for somewhere to hangout... "
        " You looked around a little bit and saw a hallway you've never really seen before. "
        " You were kinda quick to know which hallways lead to which in this school, but you haven't seen this. "
        " It looked pretty odd, too. "
        " You wanted to go ahead and walk over to it to see what's there... "
        " It also looked like the lights weren't working in that hallway. "
        " And from the looks of it, no one really took a look in that hallway. "
        " You wonder why that is... "
        " Well, time for some questions to be answered. "
        scene black with dissolve
        " As you walked over to the hallway, the air felt much colder as you took your steps. "
        " It feels like all noise from the main hallway has been drowned out... "
        " ...With nothing but silence. "
        " As you looked around, the hallways walls had scratch marks on them. "
        " You could also see some wires here and there...not sure what those were for. "
        " And you could also see some broken potion bottles on the floor... "
        " Just as you were walking around, you heard noises...crunching noises. "
        " Looking to where the sound was, you found...hey, isn't that...? "
        play music "audio/concern.mp3" fadein 1.5
        " ...There's no way you were seeing this right. "
        scene sparkform with dissolve
        " You saw Spark in some monsterous TV form he had...eating another student. "
        " You didn't know how to feel about this. "
        " What were you supposed to do? "
        " Your body wouldn't move. You couldn't move. "
        " You desperately tried to, but your body just wouldn't let you. "
        " What's wrong with your body? "
        " You should just go ahead and tell a teacher right away. "
        " After staring there for a bit, he eventually noticed you. "
        sp " ...! [name]...!! "
        sp " You weren't supposed to see me like this...!! "
        sp " You - {nw} "
        scene black with dissolve
        stop music
        " Before you could hear anything else, you collapsed. "
        " The last thing you saw was bright lights. "
        pause 1.0
        " You woke up in the school's clinic. "
        " Turns out you had skipped a class. "
        " The nurse said that you were knocked out real good... "
        " ...And that Spark was the one that took you here. "
        " You were still shaken up by what you just saw... "
        " But you quickly distracted yourself to stop yourself from thinking about it anymore. "
        " You're gonna have to ask him about this at some point. "
        " You waited a bit in the clinic before going out. "
        " It's breaktime, anyway. "
        pause 2.0
        play music "audio/paperhigh.mp3" fadein 1.5
        jump octhursbreak3
    elif temerolv >= 20 or temerolv == 20:
        # temero demon event
        $ temeroformseen = True
        " As you were about to walk down the hallway to look for somewhere to hangout... "
        " You looked around a little bit and saw a hallway you've never really seen before. "
        " You were kinda quick to know which hallways lead to which in this school, but you haven't seen this. "
        " It looked pretty odd, too. "
        " You wanted to go ahead and walk over to it to see what's there... "
        " It also looked like the lights weren't working in that hallway. "
        " And from the looks of it, no one really took a look in that hallway. "
        " You wonder why that is... "
        " Well, time for some questions to be answered. "
        scene black with dissolve
        " As you walked over to the hallway, the air felt much colder as you took your steps. "
        " It feels like all noise from the main hallway has been drowned out... "
        " ...With nothing but silence. "
        " As you looked around, the hallways walls had scratch marks on them. "
        " You could also see some wires here and there...not sure what those were for. "
        " And you could also see some broken potion bottles on the floor... "
        " Just as you were walking around, you heard noises...crunching noises. "
        " Looking to where the sound was, you found...hey, isn't that...? "
        play music "audio/concern.mp3" fadein 1.5
        " ...There's no way you were seeing this right. "
        scene temeroform with dissolve
        " You saw Temero in this butterfly form, eating another student... "
        " You didn't know how to feel about this. "
        " What were you supposed to do? "
        " Your body wouldn't move. You couldn't move. "
        " You desperately tried to, but your body just wouldn't let you. "
        " What's wrong with your body? "
        " You should just go ahead and tell a teacher right away. "
        " After staring there for a bit, she eventually noticed you. "
        tm " ...! [name]...!? "
        tm " THE HELL ARE YOU DOING HERE?! "
        tm " You idio - {nw} "
        scene black with dissolve
        stop music
        " Before you could hear anything else, you collapsed. "
        " The last thing you saw were pink butterflies around you. "
        pause 1.0
        " You woke up in the school's clinic. "
        " Turns out you had skipped a class. "
        " The nurse said that you were knocked out real good... "
        " ...And that Temero was the one that took you here. "
        " You were still shaken up by what you just saw... "
        " But you quickly distracted yourself to stop yourself from thinking about it anymore. "
        " You're gonna have to ask him about this at some point. "
        " You waited a bit in the clinic before going out. "
        " It's breaktime, anyway. "
        pause 2.0
        play music "audio/paperhigh.mp3" fadein 1.5
        jump octhursbreak3
    else:
        pass
    " Where would you like to hangout for this break? "
    menu:
        " {image=koaicon} The front of the school {image=orchidicon} ":
            jump octhursfront2
        " {image=sparkicon} The back of the school {image=quinnicon} ":
            jump octhursback2
        " {image=diskicon} The gym {image=jacobicon} ":
            jump octhursgym2
        " {image=yinyangicon} The cafeteria {image=jamicon} ":
            jump octhurscafeteria2
        " {image=carmenicon} The rooftop {image=matteicon} ":
            jump octhursrooftop2
        " {image=temeroicon} The library {image=noxicon} ":
            jump octhurslibrary2
    label octhursfront2:
        # koa and orchid
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked to the front of your school and spotted two of your classmates talking to eachother. "
        " Wondering what they're talking about, you decided to walk over to them. "
        show koaneutral at right with easeinleft
        show orchidneutral at left with easeinleft
        if koaknow == True and orchidknow == True:
            oc " Hiya there, [name]!! "
            k " ...Hi, [name]. "
            hide orchidneutral at bottom
            show orchidhappy at left
            oc " So! so so! "
            oc " Guess what I got last break! "
            oc " And I mean it - guess. "
            k " Hm... "
            k " You made...a new bracelet? "
            oc " Ooooh, I would love to!! "
            oc " But that's not really what I did. "
            oc " I actually got a new friend! "
            k " Really...? "
            k " Oh, right... "
            k " Temero told me that you were talking with Spark, correct...? "
            hide orchidhappy at bottom
            show orchidneutral at left
            oc " Yup yup! "
            oc " Me and Spark are gonna play a horror game tonight!! "
            oc " You wanna join us? "
            hide koaneutral at bottom
            show koasad at right
            k " Hmmm... "
            k " ...Maybe I could join sometime, when I have the time... "
            hide orchidneutral at bottom
            show orchidsad at left
            oc " Aw, so not right now? "
            k " Unfortunately, no... "
            k " You know how things are at my house. "
            oc " ... "
            hide orchidsad at bottom
            show orchidangry at left
            oc " This is the second time I've considered adopting you. "
            hide koasad at bottom
            show koasurprised at right
            k " That would mean you would adopt my 3 ther siblings. "
            k " And also you'd have to feed all of us. "
            k " Well - your family would have to. "
            oc " Don't care, you're getting to live in luxury with me. "
            k " I don't think your parents will agree. "
            oc " I'll get them to agree one day, come on...!!! "
            hide koasurprised at bottom
            show koalol at right
            k " Suuure, Orchid... sure. "
            oc " WHAT'S THAT FACE FOR?! "
            scene black with dissolve
            " You spent the rest of the break talking with Orchid and Koa. "
            " ...Okay but genuinely what was that face Koa just made. "
            " I mean, it's funny, yes... "
            " But it was pretty silly. It somehow got a giggle out of me. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to the gym for PE. "
            pause 2.0
            jump tpeclass1
        elif koaknow == True and orchidknow == False:
            x " Hiya there, [name]!! "
            k " ...Hi, [name]. "
            k " Oh - uh...[name]. "
            $ orchidknow = True
            k " This is my friend...Orchid. "
            oc " Heeeyy!! I like to hang out with Koa a lottt!! "
            k " ...Mhm. "
            hide orchidneutral at bottom
            show orchidhappy at left
            oc " So! so so! "
            oc " Guess what I got last break! "
            oc " And I mean it - guess. "
            k " Hm... "
            k " You made...a new bracelet? "
            oc " Ooooh, I would love to!! "
            oc " But that's not really what I did. "
            oc " I actually got a new friend! "
            k " Really...? "
            k " Oh, right... "
            k " Temero told me that you were talking with Spark, correct...? "
            hide orchidhappy at bottom
            show orchidneutral at left
            oc " Yup yup! "
            oc " Me and Spark are gonna play a horror game tonight!! "
            oc " You wanna join us? "
            hide koaneutral at bottom
            show koasad at right
            k " Hmmm... "
            k " ...Maybe I could join sometime, when I have the time... "
            hide orchidneutral at bottom
            show orchidsad at left
            oc " Aw, so not right now? "
            k " Unfortunately, no... "
            k " You know how things are at my house. "
            oc " ... "
            hide orchidsad at bottom
            show orchidangry at left
            oc " This is the second time I've considered adopting you. "
            hide koasad at bottom
            show koasurprised at right
            k " That would mean you would adopt my 3 ther siblings. "
            k " And also you'd have to feed all of us. "
            k " Well - your family would have to. "
            oc " Don't care, you're getting to live in luxury with me. "
            k " I don't think your parents will agree. "
            oc " I'll get them to agree one day, come on...!!! "
            hide koasurprised at bottom
            show koalol at right
            k " Suuure, Orchid... sure. "
            oc " WHAT'S THAT FACE FOR?! "
            scene black with dissolve
            " You spent the rest of the break talking with Orchid and Koa. "
            " ...Okay but genuinely what was that face Koa just made. "
            " I mean, it's funny, yes... "
            " But it was pretty silly. It somehow got a giggle out of me. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to the gym for PE. "
            pause 2.0
            jump tpeclass1
        elif koaknow == False and orchidknow == True:
            oc " Hiya there, [name]!! "
            x " ...Hi, [name]. "
            oc " Oh, waiiiittt! [name]!! "
            $ koaknow = True
            oc " This is my good friend, Koa!! "
            oc " I know you've heard of 'em before! "
            oc " I like to hang out with him LOTS!! "
            k " ... "
            hide orchidneutral at bottom
            show orchidhappy at left
            oc " So! so so! "
            oc " Guess what I got last break! "
            oc " And I mean it - guess. "
            k " Hm... "
            k " You made...a new bracelet? "
            oc " Ooooh, I would love to!! "
            oc " But that's not really what I did. "
            oc " I actually got a new friend! "
            k " Really...? "
            k " Oh, right... "
            k " Temero told me that you were talking with Spark, correct...? "
            hide orchidhappy at bottom
            show orchidneutral at left
            oc " Yup yup! "
            oc " Me and Spark are gonna play a horror game tonight!! "
            oc " You wanna join us? "
            hide koaneutral at bottom
            show koasad at right
            k " Hmmm... "
            k " ...Maybe I could join sometime, when I have the time... "
            hide orchidneutral at bottom
            show orchidsad at left
            oc " Aw, so not right now? "
            k " Unfortunately, no... "
            k " You know how things are at my house. "
            oc " ... "
            hide orchidsad at bottom
            show orchidangry at left
            oc " This is the second time I've considered adopting you. "
            hide koasad at bottom
            show koasurprised at right
            k " That would mean you would adopt my 3 ther siblings. "
            k " And also you'd have to feed all of us. "
            k " Well - your family would have to. "
            oc " Don't care, you're getting to live in luxury with me. "
            k " I don't think your parents will agree. "
            oc " I'll get them to agree one day, come on...!!! "
            hide koasurprised at bottom
            show koalol at right
            k " Suuure, Orchid... sure. "
            oc " WHAT'S THAT FACE FOR?! "
            scene black with dissolve
            " You spent the rest of the break talking with Orchid and Koa. "
            " ...Okay but genuinely what was that face Koa just made. "
            " I mean, it's funny, yes... "
            " But it was pretty silly. It somehow got a giggle out of me. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to the gym for PE. "
            pause 2.0
            jump tpeclass1
        else:
            x " Hiya there, [name]!! "
            x " ...Hi, [name]. "
            x " Oh hold on, I don't think we've introduced ourselves yet! "
            $ orchidknow = True
            oc " I'm Orchid!! and... "
            $ koaknow = True
            oc " This is my good friend, Koa!! "
            oc " I know you've heard of 'em before! "
            oc " I like to hang out with him LOTS!! "
            k " ... "
            hide orchidneutral at bottom
            show orchidhappy at left
            oc " So! so so! "
            oc " Guess what I got last break! "
            oc " And I mean it - guess. "
            k " Hm... "
            k " You made...a new bracelet? "
            oc " Ooooh, I would love to!! "
            oc " But that's not really what I did. "
            oc " I actually got a new friend! "
            k " Really...? "
            k " Oh, right... "
            k " Temero told me that you were talking with Spark, correct...? "
            hide orchidhappy at bottom
            show orchidneutral at left
            oc " Yup yup! "
            oc " Me and Spark are gonna play a horror game tonight!! "
            oc " You wanna join us? "
            hide koaneutral at bottom
            show koasad at right
            k " Hmmm... "
            k " ...Maybe I could join sometime, when I have the time... "
            hide orchidneutral at bottom
            show orchidsad at left
            oc " Aw, so not right now? "
            k " Unfortunately, no... "
            k " You know how things are at my house. "
            oc " ... "
            hide orchidsad at bottom
            show orchidangry at left
            oc " This is the second time I've considered adopting you. "
            hide koasad at bottom
            show koasurprised at right
            k " That would mean you would adopt my 3 ther siblings. "
            k " And also you'd have to feed all of us. "
            k " Well - your family would have to. "
            oc " Don't care, you're getting to live in luxury with me. "
            k " I don't think your parents will agree. "
            oc " I'll get them to agree one day, come on...!!! "
            hide koasurprised at bottom
            show koalol at right
            k " Suuure, Orchid... sure. "
            oc " WHAT'S THAT FACE FOR?! "
            scene black with dissolve
            " You spent the rest of the break talking with Orchid and Koa. "
            " ...Okay but genuinely what was that face Koa just made. "
            " I mean, it's funny, yes... "
            " But it was pretty silly. It somehow got a giggle out of me. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked back into the school and went to the gym for PE. "
            pause 2.0
            jump tpeclass1
    label octhursback2:
        # spark and quinn
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of the school and spotted two of your classmates doing their own things. "
        " You'd like to talk to one of them...but who do you choose to talk to? "
        if sparkknow == True and quinnknow == True:
            menu:
                " {image=sparkicon} Spark {image=sparkicon} ":
                    jump huhwhatyougay
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump huhwhatyoubi
        elif sparkknow == True and quinnknow == False:
            menu:
                " {image=sparkicon} Spark {image=sparkicon} ":
                    jump huhwhatyougay
                " {imag=equinnicon} A guy that's acting {image=quinnicon} ":
                    jump huhwhatyoubi
        elif sparkknow == False and quinnknow == True:
            menu:
                " {image=sparkicon} A guy with antennas and a tail {image=sparkicon} ":
                    jump huhwhatyougay
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump huhwhatyoubi
        else:
            menu:
                " {image=sparkicon} A guy with antennas and a tail {image=sparkicon} ":
                    jump huhwhatyougay
                " {image=quinnicon} A guy that's acting {image=quinnicon} ":
                    jump huhwhatyoubi
        label huhwhatyougay:
            # spark worrying about his demon form
            show sparksad at center with easeinleft
            if sparkknow == True:
                " Huh. Looks like he's doing something important. "
                " We're gonna have to eavesdrop for this one. "
                " His tail was causing some sparks of electricity going around. "
                " Including his antennas, too. "
                " That was honestly a little concerning... "
                " You hid behind a tree and started listening into what he was saying... "
                sp " Shit, shit - this shouldn't be happening. "
                sp " Not here, not right now... "
                sp " How am I supposed to hold this back...? "
                sp " All of the meds Clio gave me have run out... "
                sp " It's gonna take me awhile to get another pack... "
                sp " Goddd, this sucks... "
                sp " Keep everything together, Spark... "
                sp " Someone might be listening in, and you don't want them to freak out now, do you...? "
                sp " Geez...I don't think I could hold this back any longer... "
                sp " ...I need to go to the teacher's office. Fast. "
                sp " I don't want to cause a scene here... "
                sp " I need to get there, fast. "
                hide sparksad at right with easeoutright
                " ...And he left. "
                " Looks like he didn't notice you being there. "
                " Wonder what that was all about... "
                scene black with dissolve
                " You spent the rest of the break hanging out at the back of the school. "
                " As you were hanging out back there... "
                " You couldn't help but think about what you just saw. "
                " You wonder if he was gonna be alright... "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You get up and went back into the school so that you could go to the gym for PE. "
                pause 2.0
                jump tpeclass1
            else:
                " Huh. Looks like he's doing something important. "
                " We're gonna have to eavesdrop for this one. "
                " His tail was causing some sparks of electricity going around. "
                " Including his antennas, too. "
                " That was honestly a little concerning... "
                " You hid behind a tree and started listening into what he was saying... "
                x " Shit, shit - this shouldn't be happening. "
                x " Not here, not right now... "
                x " How am I supposed to hold this back...? "
                x " All of the meds Clio gave me have run out... "
                x " It's gonna take me awhile to get another pack... "
                x " Goddd, this sucks... "
                $ sparkknow = True
                sp " Keep everything together, Spark... "
                sp " Someone might be listening in, and you don't want them to freak out now, do you...? "
                sp " Geez...I don't think I could hold this back any longer... "
                sp " ...I need to go to the teacher's office. Fast. "
                sp " I don't want to cause a scene here... "
                sp " I need to get there, fast. "
                hide sparksad at right with easeoutright
                " ...And he left. "
                " Looks like he didn't notice you being there. "
                " Wonder what that was all about... "
                scene black with dissolve
                " You spent the rest of the break hanging out at the back of the school. "
                " As you were hanging out back there... "
                " You couldn't help but think about what you just saw. "
                " You wonder if he was gonna be alright... "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You get up and went back into the school so that you could go to the gym for PE. "
                pause 2.0
                jump tpeclass1
        label huhwhatyoubi:
            show quinnneutral at center with easeinright
            if quinnknow == True:
                hide quinnneutral at bottom
                show quinnhappy at center
                q " Hmhmmm... "
                q " My club members are actually taking the news well... "
                q " It's not big of a change anyway, "
                q " Of course they'd be fine... "
                q " Still I can't help but be happy that they understood... "
                q " Maybe I should take them all out to a pizza place after the play? "
                q " I'm sure they'd love that... "
                q " I mean, who could say no to good food? "
                " You greeted him politely and asked him what he was doing. "
                hide quinnhappy at bottom
                show quinnneutral at center
                q " Oh!! hey there, [name]. "
                q " I was just talking to...uh...myself...about my play! "
                q " I made this little change in the play to give more context in what happens between scenes. "
                q " Instead of acting everything out though, I just narrate what happens! "
                q " Just saying what happens, right? and my club members get ready in the back for the next scene! "
                q " Sounds pretty good, doesn't it? "
                q " This way, my club members wouldn't have to worry about an extra scene added in for them! "
                q " That would mean an extra scene for me, but honestly, I don't mind! "
                q " Besides, I have some good memory. In fact, I've memorized all of my lines in one day! "
                q " That's cool, right? "
                q " And I was just thinking - after the play, I'd take them to a pizza place! "
                q " Who could resist good food, am I right? "
                " ...You're starting to get hungry at the mention of pizza. "
                q " ...You got hungry after I said that, didn't you? "
                " It's as if he read you like a book. "
                " You nodded. "
                q " How about I buy you some food at the cafeteria then? "
                q " If you don't mind, that is. "
                menu:
                    " I don't mind ":
                        $ quinnlv += 10
                        hide quinnneutral at bottom
                        show quinnhappy at center
                        q " Let's go, then! "
                        q " I don't want to be rude and let you starve, haha. "
                        q " You deserve all the good food, [name]! "
                        q " Now, follow me... "
                        scene black with dissolve
                        " You and Quinn went to the cafeteria to get food. "
                        " Quinn bought all of your food for you, by the way. "
                        " You got a lot of good food and he only had a drink. "
                        " You offered him a bit of his food but he told you that he already ate. "
                        " You two talked a bit while you two were there. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after you finished your food. "
                        " You and Quinn got out of the cafeteria to go to the gym for PE class. "
                        pause 2.0
                        jump tpeclass1
                    " I can get my own food ":
                        q " Alright, if you say so... "
                        q " Let's chat while we're here then! "
                        q " I don't want this to just be awkward silence, hmhm. "
                        q " Let's see what I can talk about... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Just talking about his play and random things... "
                        " You were still a bit hungry at the mention of pizza though. "
                        " Maybe you should buy yourself some pizza later... "
                        " Well, if you had enough money for that. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You got back into the school and went to the gym for PE. "
                        pause 2.0
                        jump tpeclass1
            else:
                hide quinnneutral at bottom
                show quinnhappy at center
                x " Hmhmmm... "
                x " My club members are actually taking the news well... "
                x " It's not big of a change anyway, "
                x " Of course they'd be fine... "
                x " Still I can't help but be happy that they understood... "
                x " Maybe I should take them all out to a pizza place after the play? "
                x " I'm sure they'd love that... "
                x " I mean, who could say no to good food? "
                " You greeted him politely and asked him what he was doing. "
                hide quinnhappy at bottom
                show quinnneutral at center
                x " Oh!! hey there, [name]. "
                $ quinnknow = True
                q " I'm Quinn - apart of the drama club AND your classmate. "
                q " I was just talking to...uh...myself...about my play! "
                q " I made this little change in the play to give more context in what happens between scenes. "
                q " Instead of acting everything out though, I just narrate what happens! "
                q " Just saying what happens, right? and my club members get ready in the back for the next scene! "
                q " Sounds pretty good, doesn't it? "
                q " This way, my club members wouldn't have to worry about an extra scene added in for them! "
                q " That would mean an extra scene for me, but honestly, I don't mind! "
                q " Besides, I have some good memory. In fact, I've memorized all of my lines in one day! "
                q " That's cool, right? "
                q " And I was just thinking - after the play, I'd take them to a pizza place! "
                q " Who could resist good food, am I right? "
                " ...You're starting to get hungry at the mention of pizza. "
                q " ...You got hungry after I said that, didn't you? "
                " It's as if he read you like a book. "
                " You nodded. "
                q " How about I buy you some food at the cafeteria then? "
                q " If you don't mind, that is. "
                menu:
                    " I don't mind ":
                        $ quinnlv += 10
                        hide quinnneutral at bottom
                        show quinnhappy at center
                        q " Let's go, then! "
                        q " I don't want to be rude and let you starve, haha. "
                        q " You deserve all the good food, [name]! "
                        q " Now, follow me... "
                        scene black with dissolve
                        " You and Quinn went to the cafeteria to get food. "
                        " Quinn bought all of your food for you, by the way. "
                        " You got a lot of good food and he only had a drink. "
                        " You offered him a bit of his food but he told you that he already ate. "
                        " You two talked a bit while you two were there. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after you finished your food. "
                        " You and Quinn got out of the cafeteria to go to the gym for PE class. "
                        pause 2.0
                        jump tpeclass1
                    " I can get my own food ":
                        q " Alright, if you say so... "
                        q " Let's chat while we're here then! "
                        q " I don't want this to just be awkward silence, hmhm. "
                        q " Let's see what I can talk about... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Just talking about his play and random things... "
                        " You were still a bit hungry at the mention of pizza though. "
                        " Maybe you should buy yourself some pizza later... "
                        " Well, if you had enough money for that. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You got back into the school and went to the gym for PE. "
                        pause 2.0
                        jump tpeclass1
    label octhursgym2:
        # disk and jacob
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked into the gym and spotted two of your classmates talking with eachother. "
        " Wondering what they're talking about, you walked over to them. "
        show diskneutral at left with easeinright
        show jacobneutral at right with easeinright
        if diskknow == True and jacobknow == True:
            d " Heey, [name]!! "
            jac " (Oh god, not another one...) "
            jac " ...Hey, [name]. "
            d " I was just talking to Jacob over here! "
            d " I have to admit, I got a little curious... "
            hide diskneutral at bottom
            show diskhappy at left
            d " Curious on why he wears a bandana and goggles! "
            d " I'm sure your face doesn't look that bad, Jacob! "
            d " [name] - you agree, right? "
            " You don't really know what to think about this. "
            " You just agreed so that you don't start anything. "
            d " Seeee? "
            jac " ...You two haven't even seen my face yet. "
            jac " I bet both of you would freak out. "
            hide diskhappy at bottom
            show diskneutral at left
            d " No we won't! "
            d " It would be totally fine if you showed us your face! "
            d " Well...uh, only if you want to! "
            jac " ... "
            jac " ...I'm not gonna do that anytime soon. "
            hide diskneutral at bottom
            show disksad at left
            d " Oh! uh, if you say so, then! "
            d " I don't want to make you uncomfortable, after all! "
            d " Sorry for um...bothering you about your bandana and goggles though. "
            jac " It's fine, you were just curious about it. "
            jac " Not like you were trying to pull them off my face, anyway. "
            jac " You're all good. "
            hide disksad at bottom
            show diskneutral at left
            d " Really? phew! I was worried that I made you mad... "
            jac " Not at all. "
            jac " Questions like those don't really bother me. "
            jac " Unless if you keep asking me about my goggles and bandana. "
            jac " I'd probably shove my saw up your ass. "
            d " Got it, got it... "
            d " I won't ask you about it again! "
            jac " Great. "
            jac " Glad you understand, Disk. "
            d " Hehe - of course I'd understand! "
            d " I understand not wanting to show your face... "
            d " If you ever got anything to talk about - you can always talk to me! "
            d " And you can talk to [name], too! "
            d " Don't be afraid to share your feelings, alright? "
            d " We're classmates - and classmates should treat eachother like family! "
            jac " ...Yeah, family. "
            jac " I'll be sure to talk with you. "
            d " Yay! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Jacob. "
            " Now that you thought about it... "
            " You were just a little bit curious of what Jacob looked like. "
            " But then again, you didn't want to make him uncomfortable. "
            " Best for him to show his face when he's really comfortable. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " Though, you were already in the place where PE takes place in, so... "
            " You just waited patiently for the teacher to arrive. "
            pause 2.0
            jump tpeclass1
        elif diskknow == True and jacobknow == False:
            d " Heey, [name]!! "
            x " (Oh god, not another one...) "
            x " ...Hey, [name]. "
            $ jacobknow = True
            d " I was just talking to Jacob over here! "
            d " I have to admit, I got a little curious... "
            hide diskneutral at bottom
            show diskhappy at left
            d " Curious on why he wears a bandana and goggles! "
            d " I'm sure your face doesn't look that bad, Jacob! "
            d " [name] - you agree, right? "
            " You don't really know what to think about this. "
            " You just agreed so that you don't start anything. "
            d " Seeee? "
            jac " ...You two haven't even seen my face yet. "
            jac " I bet both of you would freak out. "
            hide diskhappy at bottom
            show diskneutral at left
            d " No we won't! "
            d " It would be totally fine if you showed us your face! "
            d " Well...uh, only if you want to! "
            jac " ... "
            jac " ...I'm not gonna do that anytime soon. "
            hide diskneutral at bottom
            show disksad at left
            d " Oh! uh, if you say so, then! "
            d " I don't want to make you uncomfortable, after all! "
            d " Sorry for um...bothering you about your bandana and goggles though. "
            jac " It's fine, you were just curious about it. "
            jac " Not like you were trying to pull them off my face, anyway. "
            jac " You're all good. "
            hide disksad at bottom
            show diskneutral at left
            d " Really? phew! I was worried that I made you mad... "
            jac " Not at all. "
            jac " Questions like those don't really bother me. "
            jac " Unless if you keep asking me about my goggles and bandana. "
            jac " I'd probably shove my saw up your ass. "
            d " Got it, got it... "
            d " I won't ask you about it again! "
            jac " Great. "
            jac " Glad you understand, Disk. "
            d " Hehe - of course I'd understand! "
            d " I understand not wanting to show your face... "
            d " If you ever got anything to talk about - you can always talk to me! "
            d " And you can talk to [name], too! "
            d " Don't be afraid to share your feelings, alright? "
            d " We're classmates - and classmates should treat eachother like family! "
            jac " ...Yeah, family. "
            jac " I'll be sure to talk with you. "
            d " Yay! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Jacob. "
            " Now that you thought about it... "
            " You were just a little bit curious of what Jacob looked like. "
            " But then again, you didn't want to make him uncomfortable. "
            " Best for him to show his face when he's really comfortable. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " Though, you were already in the place where PE takes place in, so... "
            " You just waited patiently for the teacher to arrive. "
            pause 2.0
            jump tpeclass1
        elif diskknow == False and jacobknow == True:
            x " Heey, [name]!! "
            jac " (Oh god, not another one...) "
            jac " ...Hey, [name]. "
            $ diskknow = True
            d " I'm Disk! Your classmate! and... "
            d " I was just talking to Jacob over here! "
            d " I have to admit, I got a little curious... "
            hide diskneutral at bottom
            show diskhappy at left
            d " Curious on why he wears a bandana and goggles! "
            d " I'm sure your face doesn't look that bad, Jacob! "
            d " [name] - you agree, right? "
            " You don't really know what to think about this. "
            " You just agreed so that you don't start anything. "
            d " Seeee? "
            jac " ...You two haven't even seen my face yet. "
            jac " I bet both of you would freak out. "
            hide diskhappy at bottom
            show diskneutral at left
            d " No we won't! "
            d " It would be totally fine if you showed us your face! "
            d " Well...uh, only if you want to! "
            jac " ... "
            jac " ...I'm not gonna do that anytime soon. "
            hide diskneutral at bottom
            show disksad at left
            d " Oh! uh, if you say so, then! "
            d " I don't want to make you uncomfortable, after all! "
            d " Sorry for um...bothering you about your bandana and goggles though. "
            jac " It's fine, you were just curious about it. "
            jac " Not like you were trying to pull them off my face, anyway. "
            jac " You're all good. "
            hide disksad at bottom
            show diskneutral at left
            d " Really? phew! I was worried that I made you mad... "
            jac " Not at all. "
            jac " Questions like those don't really bother me. "
            jac " Unless if you keep asking me about my goggles and bandana. "
            jac " I'd probably shove my saw up your ass. "
            d " Got it, got it... "
            d " I won't ask you about it again! "
            jac " Great. "
            jac " Glad you understand, Disk. "
            d " Hehe - of course I'd understand! "
            d " I understand not wanting to show your face... "
            d " If you ever got anything to talk about - you can always talk to me! "
            d " And you can talk to [name], too! "
            d " Don't be afraid to share your feelings, alright? "
            d " We're classmates - and classmates should treat eachother like family! "
            jac " ...Yeah, family. "
            jac " I'll be sure to talk with you. "
            d " Yay! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Jacob. "
            " Now that you thought about it... "
            " You were just a little bit curious of what Jacob looked like. "
            " But then again, you didn't want to make him uncomfortable. "
            " Best for him to show his face when he's really comfortable. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " Though, you were already in the place where PE takes place in, so... "
            " You just waited patiently for the teacher to arrive. "
            pause 2.0
            jump tpeclass1
        else:
            x " Heey, [name]!! "
            x " (Oh god, not another one...) "
            x " ...Hey, [name]. "
            $ diskknow = True
            $ jacobknow = True
            d " I'm Disk! Your classmate! and... "
            d " I was just talking to Jacob over here! "
            d " I have to admit, I got a little curious... "
            hide diskneutral at bottom
            show diskhappy at left
            d " Curious on why he wears a bandana and goggles! "
            d " I'm sure your face doesn't look that bad, Jacob! "
            d " [name] - you agree, right? "
            " You don't really know what to think about this. "
            " You just agreed so that you don't start anything. "
            d " Seeee? "
            jac " ...You two haven't even seen my face yet. "
            jac " I bet both of you would freak out. "
            hide diskhappy at bottom
            show diskneutral at left
            d " No we won't! "
            d " It would be totally fine if you showed us your face! "
            d " Well...uh, only if you want to! "
            jac " ... "
            jac " ...I'm not gonna do that anytime soon. "
            hide diskneutral at bottom
            show disksad at left
            d " Oh! uh, if you say so, then! "
            d " I don't want to make you uncomfortable, after all! "
            d " Sorry for um...bothering you about your bandana and goggles though. "
            jac " It's fine, you were just curious about it. "
            jac " Not like you were trying to pull them off my face, anyway. "
            jac " You're all good. "
            hide disksad at bottom
            show diskneutral at left
            d " Really? phew! I was worried that I made you mad... "
            jac " Not at all. "
            jac " Questions like those don't really bother me. "
            jac " Unless if you keep asking me about my goggles and bandana. "
            jac " I'd probably shove my saw up your ass. "
            d " Got it, got it... "
            d " I won't ask you about it again! "
            jac " Great. "
            jac " Glad you understand, Disk. "
            d " Hehe - of course I'd understand! "
            d " I understand not wanting to show your face... "
            d " If you ever got anything to talk about - you can always talk to me! "
            d " And you can talk to [name], too! "
            d " Don't be afraid to share your feelings, alright? "
            d " We're classmates - and classmates should treat eachother like family! "
            jac " ...Yeah, family. "
            jac " I'll be sure to talk with you. "
            d " Yay! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Jacob. "
            " Now that you thought about it... "
            " You were just a little bit curious of what Jacob looked like. "
            " But then again, you didn't want to make him uncomfortable. "
            " Best for him to show his face when he's really comfortable. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " Though, you were already in the place where PE takes place in, so... "
            " You just waited patiently for the teacher to arrive. "
            pause 2.0
            jump tpeclass1
    label octhurscafeteria2:
        # the twins and jam
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked into the cafeteria and spotted three of your classmates doing their own things. "
        " You wanted to talk to one of them...but who do you talk to? "
        if yinhuiknow,yangyiknow == True and jamknow == True:
            menu:
                " {image=yinyangicon} The twins {image=yinyangicon} ":
                    jump preciouslittleguy
                " {image=jamicon} Jam {image=jamicon} ":
                    jump preciouslittlegirl
        elif yinhuiknow,yangyiknow == True and jamknow == False:
            menu:
                " {image=yinyangicon} The twins {image=yinyangicon} ":
                    jump preciouslittleguy
                " {image=jamicon} A mean looking girl {image=jamicon} ":
                    jump preciouslittlegirl
        elif yinhuiknow,yangyiknow == False and jamknow == True:
            menu:
                " {image=yinyangicon} People who look like twins {image=yinyangicon} ":
                    jump preciouslittleguy
                " {image=jamicon} Jam {image=jamicon} ":
                    jump preciouslittlegirl
        else:
            menu:
                " {image=yinyangicon} People who look like twins {image=yinyangicon} ":
                    jump preciouslittleguy
                " {image=jamicon} A mean looking girl {image=jamicon} ":
                    jump preciouslittlegirl
        label preciouslittleguy:
            show yinhuineutral at right with easeinleft
            show yangyineutral at left with easeinleft
            if yinhuiknow == True and yangyiknow == True:
                ya " Hey there, [name]!! "
                yi " Huh? oh, it's you. "
                ya " Yinhui, be nice! greet them properly! "
                yi " ...Hello, [name]. "
                ya " There, that's better - isn't it? "
                yi " ...Yeah, sure. "
                ya " Anyway! we've been thinking... "
                yi " Thinking about what we should make for our mom for dinner. "
                ya " Yup yup! she always makes the best food! "
                yi " So we thought that cooking her something nice in return. "
                ya " It's just that we don't know what to cook for her, you know? "
                yi " Yeah, there's a lot of things that she likes. "
                ya " The only thing she doesn't like is undercooked food... "
                yi " And burnt food, add that to the list. "
                ya " There IS this one dish that we remember... "
                yi " But we can't really remember the ingredients, so we scratched that out. "
                ya " We've been struggling really hard, as you can see. "
                yi " We need ideas. "
                ya " And a whole lot of them! "
                yi " Any idea will do. "
                ya " As long as it's good ones! "
                yi " So, you got any ideas in that small brain of yours? "
                ya " Yinhui. "
                yi " Sorry, sorry. "
                menu:
                    " Cook up her favorite food ":
                        $ yinhuilv += 10
                        $ yangyilv += 10
                        hide yinhuineutral at bottom
                        show yinhuisurprised at right
                        hide yangyineutral at bottom
                        show yangyisurprised at left
                        yi " ... "
                        ya " ... "
                        yi " Yangyi, I believe we're stupid. "
                        yi " How come we haven't thought of that? "
                        ya " I don't know, I thought it would be too obvious! "
                        yi " It would be too obvious, but that doesn't mean it's not a good idea! "
                        ya " Sorryyyy... "
                        yi " ...Hm. "
                        hide yinhuisurprised at bottom
                        show yinhuineutral at right
                        hide yangyisurprised at bottom
                        show yangyineutral at left
                        yi " Whatever, thank you for the idea, [name]. "
                        ya " Yeah, thanks anyway... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Yinhui and Yangyi. "
                        " You kind of found it funny that they haven't really thought of the favorite food thing in the first place. "
                        " I mean, technically they did, but they just chose not to do it. "
                        " Still pretty funny though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for PE class. "
                        " You got out of the cafeteria and went to the gym for the class. "
                        pause 2.0
                        jump tpeclass1
                    " I don't know, sorry ":
                        yi " Hmhmmm... "
                        ya " Thank you, anyway. "
                        hide yinhuineutral at bottom
                        show yinhuisurprised at right
                        yi " Yeah - wait... "
                        yi " Yang, I fear we may be stupid. "
                        ya " Hm? what is it, brother? "
                        yi " We could've just cooked our mom her favorite food. "
                        ya " Wait...really? "
                        yi " OF COURSE!! How come we haven't thought of that yet!! "
                        ya " Well, uh... "
                        ya " Actually, I did, but I thought it would be too obvious... "
                        yi " It would be too obvious, but that doesn't mean it's not a good idea! "
                        ya " Sorryyyy... "
                        yi " ...Hm. "
                        hide yinhuisurprised at bottom
                        show yinhuineutral at right
                        hide yangyisurprised at bottom
                        show yangyineutral at left
                        yi " ...Whatever, atleast we have an idea now. "
                        ya " Yeah, atleast... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Yinhui and Yangyi. "
                        " You kind of found it funny that they haven't really thought of the favorite food thing in the first place. "
                        " I mean, technically they did, but they just chose not to do it. "
                        " Still pretty funny though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for PE class. "
                        " You got out of the cafeteria and went to the gym for the class. "
                        pause 2.0
                        jump tpeclass1
            else:
                x " Hey there, [name]!! "
                x " Huh? oh, it's you. "
                x " Yinhui, be nice! greet them properly! "
                x " ...Hello, [name]. "
                x " There, that's better - isn't it? "
                x " ...Yeah, sure. "
                ya " I'm Yangyi, the twin on the left! "
                yi " And I'm Yinhui, the twin on the right. "
                if yinhuiknow == False and yangyiknow == False:
                    $ yinhuiknow = True
                    $ yangyiknow = True
                elif yinhuiknow == True and yangyiknow == False:
                    $ yangyiknow = True
                elif yinhuiknow == False and yangyiknow == True:
                    $ yinhuiknow = True
                else:
                    pass
                ya " Anyway! we've been thinking... "
                yi " Thinking about what we should make for our mom for dinner. "
                ya " Yup yup! she always makes the best food! "
                yi " So we thought that cooking her something nice in return. "
                ya " It's just that we don't know what to cook for her, you know? "
                yi " Yeah, there's a lot of things that she likes. "
                ya " The only thing she doesn't like is undercooked food... "
                yi " And burnt food, add that to the list. "
                ya " There IS this one dish that we remember... "
                yi " But we can't really remember the ingredients, so we scratched that out. "
                ya " We've been struggling really hard, as you can see. "
                yi " We need ideas. "
                ya " And a whole lot of them! "
                yi " Any idea will do. "
                ya " As long as it's good ones! "
                yi " So, you got any ideas in that small brain of yours? "
                ya " Yinhui. "
                yi " Sorry, sorry. "
                menu:
                    " Cook up her favorite food ":
                        $ yinhuilv += 10
                        $ yangyilv += 10
                        hide yinhuineutral at bottom
                        show yinhuisurprised at right
                        hide yangyineutral at bottom
                        show yangyisurprised at left
                        yi " ... "
                        ya " ... "
                        yi " Yangyi, I believe we're stupid. "
                        yi " How come we haven't thought of that? "
                        ya " I don't know, I thought it would be too obvious! "
                        yi " It would be too obvious, but that doesn't mean it's not a good idea! "
                        ya " Sorryyyy... "
                        yi " ...Hm. "
                        hide yinhuisurprised at bottom
                        show yinhuineutral at right
                        hide yangyisurprised at bottom
                        show yangyineutral at left
                        yi " Whatever, thank you for the idea, [name]. "
                        ya " Yeah, thanks anyway... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Yinhui and Yangyi. "
                        " You kind of found it funny that they haven't really thought of the favorite food thing in the first place. "
                        " I mean, technically they did, but they just chose not to do it. "
                        " Still pretty funny though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for PE class. "
                        " You got out of the cafeteria and went to the gym for the class. "
                        pause 2.0
                        jump tpeclass1
                    " I don't know, sorry ":
                        yi " Hmhmmm... "
                        ya " Thank you, anyway. "
                        hide yinhuineutral at bottom
                        show yinhuisurprised at right
                        yi " Yeah - wait... "
                        yi " Yang, I fear we may be stupid. "
                        ya " Hm? what is it, brother? "
                        yi " We could've just cooked our mom her favorite food. "
                        ya " Wait...really? "
                        yi " OF COURSE!! How come we haven't thought of that yet!! "
                        ya " Well, uh... "
                        ya " Actually, I did, but I thought it would be too obvious... "
                        yi " It would be too obvious, but that doesn't mean it's not a good idea! "
                        ya " Sorryyyy... "
                        yi " ...Hm. "
                        hide yinhuisurprised at bottom
                        show yinhuineutral at right
                        hide yangyisurprised at bottom
                        show yangyineutral at left
                        yi " ...Whatever, atleast we have an idea now. "
                        ya " Yeah, atleast... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Yinhui and Yangyi. "
                        " You kind of found it funny that they haven't really thought of the favorite food thing in the first place. "
                        " I mean, technically they did, but they just chose not to do it. "
                        " Still pretty funny though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for PE class. "
                        " You got out of the cafeteria and went to the gym for the class. "
                        pause 2.0
                        jump tpeclass1
        label preciouslittlegirl:
            show jamgame at center with easeinright
            if jamknow == True:
                " Looks like she's playing a game. "
                " You sat down next to her and looked at the game she was playing... "
                " It was a confusing looking rhythm game. "
                " You're not actually sure how to play it. "
                " It had sky notes and such... "
                " It had four lanes, yes, but sky notes??? that's what's confusing you. "
                " The sky notes could also go down which confuses you even more. "
                ja " ...? "
                ja " Oh, hey there [name]. "
                ja " Uh... "
                ja " Since I don't want this to be really awkward, I'm gonna explain to you how the game works. "
                ja " I just found this neat new rhythm game on the playstore last night. "
                ja " It's a bit confusing at first, but that's 'cause you haven't looked at the tutorial. "
                ja " You get used to it after a bit of playing. "
                ja " It's also got really good art and stuff. "
                ja " And also pretty goot stroyline, too. "
                ja " Peak game - it's a shame that only so few know about it though. "
                ja " And most of those people are foreigners. "
                ja " I don't understand japanese or chinese, so I can't really add anyone on here... "
                ja " So rare to find english players in this game, I swear... "
                ja " Not that I mind, anyway. "
                ja " I like to play alone every now and then. "
                ja " I don't even know what the friend mechanic does in this game... "
                ja " It's a little odd, in all honesty. "
                ja " And also {nw} "
                " Before Jam could finish her sentence, she heard the game finishing. "
                ja " Huh? I didn't realize that I finished the song already. "
                ja " I probably missed a lot while talking to you... "
                hide jamneutral at bottom
                show jamsurprised at center
                ja " Holy moly. "
                ja " There's absolutely no way. "
                ja " This game has to be trolling on me. "
                " You looked at her screen and turns out... "
                " ...She got an all perfect while she was talking to you. "
                " Huh, you'd think that she'd get a lot of misses considering she was distracted, but I guess not. "
                ja " No fucking way. "
                ja " I'm gonna screenshot this and send this to my online friends later. "
                ja " They're gonna absolutely freak out over this. "
                " You were freaking out about it too, in all honesty. "
                " Was Jam really just this good at rhythm games? "
                " Good heavens...you feel so weak after seeing the all perfect dude. "
                scene black with dissolve
                " You spent the rest of the break talking with Jam. "
                " She was still going insane over the fact that she got an all perfect... "
                " And she also looked pretty proud of herself. "
                " You would be proud too if you got something like that, too. "
                " If only you had her skill, man... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You got out of the cafeteria and went to the gym for PE. "
                pause 2.0
                jump tpeclass1
            else:
                " Looks like she's playing a game. "
                " You sat down next to her and looked at the game she was playing... "
                " It was a confusing looking rhythm game. "
                " You're not actually sure how to play it. "
                " It had sky notes and such... "
                " It had four lanes, yes, but sky notes??? that's what's confusing you. "
                " The sky notes could also go down which confuses you even more. "
                x " ...? "
                x " Oh, hey there [name]. "
                $ jamknow = True
                ja " I'm Jam, by the way. "
                ja " Uh... "
                ja " Since I don't want this to be really awkward, I'm gonna explain to you how the game works. "
                ja " I just found this neat new rhythm game on the playstore last night. "
                ja " It's a bit confusing at first, but that's 'cause you haven't looked at the tutorial. "
                ja " You get used to it after a bit of playing. "
                ja " It's also got really good art and stuff. "
                ja " And also pretty goot stroyline, too. "
                ja " Peak game - it's a shame that only so few know about it though. "
                ja " And most of those people are foreigners. "
                ja " I don't understand japanese or chinese, so I can't really add anyone on here... "
                ja " So rare to find english players in this game, I swear... "
                ja " Not that I mind, anyway. "
                ja " I like to play alone every now and then. "
                ja " I don't even know what the friend mechanic does in this game... "
                ja " It's a little odd, in all honesty. "
                ja " And also {nw} "
                " Before Jam could finish her sentence, she heard the game finishing. "
                ja " Huh? I didn't realize that I finished the song already. "
                ja " I probably missed a lot while talking to you... "
                hide jamneutral at bottom
                show jamsurprised at center
                ja " Holy moly. "
                ja " There's absolutely no way. "
                ja " This game has to be trolling on me. "
                " You looked at her screen and turns out... "
                " ...She got an all perfect while she was talking to you. "
                " Huh, you'd think that she'd get a lot of misses considering she was distracted, but I guess not. "
                ja " No fucking way. "
                ja " I'm gonna screenshot this and send this to my online friends later. "
                ja " They're gonna absolutely freak out over this. "
                " You were freaking out about it too, in all honesty. "
                " Was Jam really just this good at rhythm games? "
                " Good heavens...you feel so weak after seeing the all perfect dude. "
                scene black with dissolve
                " You spent the rest of the break talking with Jam. "
                " She was still going insane over the fact that she got an all perfect... "
                " And she also looked pretty proud of herself. "
                " You would be proud too if you got something like that, too. "
                " If only you had her skill, man... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You got out of the cafeteria and went to the gym for PE. "
                pause 2.0
                jump tpeclass1
    label octhursrooftop2:
        # carmen and matte
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked up to the rooftop and spotted two of your classmates talking to eachother. "
        " Wondering what they're doing, you decided to walk over to them and join their conversation. "
        show carmenneutral at right with easeinleft
        show matteneutral at left with easeinleft
        if carmenknow == True and matteknow == True:
            ma " Just pose right there, Carmen. "
            ca " ...? "
            ma " Yeah, like that! "
            ma " And hold your guitar like this... "
            " She does a pose that the other guy can imitate... "
            " The other guy imitates it very well. "
            ma " Wonderful! "
            ma " I'll just sketch out the pose you're in so that you won't have to stand for 4 hours straight. "
            ma " Sound good to you? "
            ca " ...! "
            " He nodded. "
            ma " Great, let me just do that... "
            ma " And let me just get all the details... "
            ma " ...Annnnd perfect! "
            ma " I'll send you the final product when I'm done, alright? "
            ma " I'm planning on working on this at home. "
            ca " ... "
            " The other guy did a nod of agreement and got out of the pose he was in. "
            " You greeted the both of them and asked what they were doing. "
            ma " Oooh, hey there, [name]! "
            ca " ...! "
            " The guy with the guitar greets you by waving at you. "
            ma " I was just planning on drawing Carmen over here later! "
            ma " I got a little bored and decided to draw him, hehe. "
            ma " He's one of the people who I haven't drawn yet! "
            ca " ... "
            ma " What's that? you're planning on making it your profile picture later? "
            ma " Aww, that's nice of you, Carmen! "
            ma " It'd be and honor for my art to be your profile picture! "
            ca " ...:D! "
            ma " Heheh..I sure do love making art for my classmates! "
            ma " Even though it kind of tires me out. "
            " You told Matte to take breaks every now and then. "
            ma " Oh, [name]!! "
            ma " It's nice of you to say that. "
            ma " But don't worry, I actually do take breaks. "
            ma " Unlike some artists around the world... "
            ma " Seriously, people should take more breaks often! "
            ma " Working constantly isn't good for your health! "
            ca " ... "
            " Carmen nodded his head in agreement. "
            " You also agreed. "
            " Working yourself to exhaustion isn't good at all. "
            " SOME people should take notes about that. "
            scene black with dissolve
            " You spent the rest of the break talking with Carmen and Matte. "
            " Just talking about art and whatnot... "
            " Talking about a lot of stuff, actually. "
            " Just random stuff and nothing important. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and went to the gym for PE. "
            pause 2.0
            jump tpeclass1
        elif carmenknow == True and matteknow == False:
            x " Just pose right there, Carmen. "
            ca " ...? "
            x " Yeah, like that! "
            x " And hold your guitar like this... "
            " She does a pose that the other guy can imitate... "
            " The other guy imitates it very well. "
            x " Wonderful! "
            x " I'll just sketch out the pose you're in so that you won't have to stand for 4 hours straight. "
            x " Sound good to you? "
            ca " ...! "
            " He nodded. "
            x " Great, let me just do that... "
            x " And let me just get all the details... "
            x " ...Annnnd perfect! "
            x " I'll send you the final product when I'm done, alright? "
            x " I'm planning on working on this at home. "
            ca " ... "
            " The other guy did a nod of agreement and got out of the pose he was in. "
            " You greeted the both of them and asked what they were doing. "
            x " Oooh, hey there, [name]! "
            ca " ...! "
            " The guy with the guitar greets you by waving at you. "
            $ matteknow = True
            ma " I'm Matte, by the way. Disk's and Quinn's cousin. "
            ma " I was just planning on drawing Carmen over here later! "
            ma " I got a little bored and decided to draw him, hehe. "
            ma " He's one of the people who I haven't drawn yet! "
            ca " ... "
            ma " What's that? you're planning on making it your profile picture later? "
            ma " Aww, that's nice of you, Carmen! "
            ma " It'd be and honor for my art to be your profile picture! "
            ca " ...:D! "
            ma " Heheh..I sure do love making art for my classmates! "
            ma " Even though it kind of tires me out. "
            " You told Matte to take breaks every now and then. "
            ma " Oh, [name]!! "
            ma " It's nice of you to say that. "
            ma " But don't worry, I actually do take breaks. "
            ma " Unlike some artists around the world... "
            ma " Seriously, people should take more breaks often! "
            ma " Working constantly isn't good for your health! "
            ca " ... "
            " Carmen nodded his head in agreement. "
            " You also agreed. "
            " Working yourself to exhaustion isn't good at all. "
            " SOME people should take notes about that. "
            scene black with dissolve
            " You spent the rest of the break talking with Carmen and Matte. "
            " Just talking about art and whatnot... "
            " Talking about a lot of stuff, actually. "
            " Just random stuff and nothing important. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and went to the gym for PE. "
            pause 2.0
            jump tpeclass1
        elif carmenknow == False and matteknow == True:
            ma " Just pose right there, Carmen. "
            x " ...? "
            ma " Yeah, like that! "
            ma " And hold your guitar like this... "
            " She does a pose that the other guy can imitate... "
            " The other guy imitates it very well. "
            ma " Wonderful! "
            ma " I'll just sketch out the pose you're in so that you won't have to stand for 4 hours straight. "
            ma " Sound good to you? "
            x " ...! "
            " He nodded. "
            ma " Great, let me just do that... "
            ma " And let me just get all the details... "
            ma " ...Annnnd perfect! "
            ma " I'll send you the final product when I'm done, alright? "
            ma " I'm planning on working on this at home. "
            x " ... "
            " The other guy did a nod of agreement and got out of the pose he was in. "
            " You greeted the both of them and asked what they were doing. "
            ma " Oooh, hey there, [name]! "
            x " ...! "
            " The guy with the guitar greets you by waving at you. "
            $ carmenknow = True
            ma " I was just planning on drawing Carmen over here later! "
            ma " I got a little bored and decided to draw him, hehe. "
            ma " He's one of the people who I haven't drawn yet! "
            ca " ... "
            ma " What's that? you're planning on making it your profile picture later? "
            ma " Aww, that's nice of you, Carmen! "
            ma " It'd be and honor for my art to be your profile picture! "
            ca " ...:D! "
            ma " Heheh..I sure do love making art for my classmates! "
            ma " Even though it kind of tires me out. "
            " You told Matte to take breaks every now and then. "
            ma " Oh, [name]!! "
            ma " It's nice of you to say that. "
            ma " But don't worry, I actually do take breaks. "
            ma " Unlike some artists around the world... "
            ma " Seriously, people should take more breaks often! "
            ma " Working constantly isn't good for your health! "
            ca " ... "
            " Carmen nodded his head in agreement. "
            " You also agreed. "
            " Working yourself to exhaustion isn't good at all. "
            " SOME people should take notes about that. "
            scene black with dissolve
            " You spent the rest of the break talking with Carmen and Matte. "
            " Just talking about art and whatnot... "
            " Talking about a lot of stuff, actually. "
            " Just random stuff and nothing important. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and went to the gym for PE. "
            pause 2.0
            jump tpeclass1
        else:
            x " Just pose right there, Carmen. "
            x " ...? "
            x " Yeah, like that! "
            x " And hold your guitar like this... "
            " She does a pose that the other guy can imitate... "
            " The other guy imitates it very well. "
            x " Wonderful! "
            x " I'll just sketch out the pose you're in so that you won't have to stand for 4 hours straight. "
            x " Sound good to you? "
            x " ...! "
            " He nodded. "
            x " Great, let me just do that... "
            x " And let me just get all the details... "
            x " ...Annnnd perfect! "
            x " I'll send you the final product when I'm done, alright? "
            x " I'm planning on working on this at home. "
            x " ... "
            " The other guy did a nod of agreement and got out of the pose he was in. "
            " You greeted the both of them and asked what they were doing. "
            x " Oooh, hey there, [name]! "
            ca " ...! "
            " The guy with the guitar greets you by waving at you. "
            $ matteknow = True
            ma " I'm Matte, by the way. Disk's and Quinn's cousin. "
            $ carmenknow = True
            ma " I was just planning on drawing Carmen over here later! "
            ma " I got a little bored and decided to draw him, hehe. "
            ma " He's one of the people who I haven't drawn yet! "
            ca " ... "
            ma " What's that? you're planning on making it your profile picture later? "
            ma " Aww, that's nice of you, Carmen! "
            ma " It'd be and honor for my art to be your profile picture! "
            ca " ...:D! "
            ma " Heheh..I sure do love making art for my classmates! "
            ma " Even though it kind of tires me out. "
            " You told Matte to take breaks every now and then. "
            ma " Oh, [name]!! "
            ma " It's nice of you to say that. "
            ma " But don't worry, I actually do take breaks. "
            ma " Unlike some artists around the world... "
            ma " Seriously, people should take more breaks often! "
            ma " Working constantly isn't good for your health! "
            ca " ... "
            " Carmen nodded his head in agreement. "
            " You also agreed. "
            " Working yourself to exhaustion isn't good at all. "
            " SOME people should take notes about that. "
            scene black with dissolve
            " You spent the rest of the break talking with Carmen and Matte. "
            " Just talking about art and whatnot... "
            " Talking about a lot of stuff, actually. "
            " Just random stuff and nothing important. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down from the rooftop and went to the gym for PE. "
            pause 2.0
            jump tpeclass1
    label octhurslibrary2:
        # temero and nox
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked to the library and found two of your classmates doing their own things. "
        " You wanted to talk to one of them...but who do you talk to? "
        if temeroknow == True and noxknow == True:
            menu:
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump kfcyeah
                " {image=noxicon} Nox {image=noxicon} ":
                    jump kfcnah
        elif temeroknow == True and noxknow == False:
            menu:
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump kfcyeah
                " {image=noxicon} A sleepy guy {image=noxicon} ":
                    jump kfcnah
        elif temeroknow == False and noxknow == True:
            menu:
                " {image=temeroicon} A worried scientist girl {image=temeroicon} ":
                    jump kfcyeah
                " {image=noxicon} Nox {image=noxicon} ":
                    jump kfcnah
        else:
            menu:
                " {image=temeroicon} A worried scientist girl {image=temeroicon} ":
                    jump kfcyeah
                " {image=noxicon} A sleepy guy {image=noxicon} ":
                    jump kfcnah
        label kfcyeah:
            # worrying about her powers
            show temerosad at center with easeinleft
            if temeroknow == True:
                " Huh, looks like she's doing something important right now. "
                " We're gonna have to eavesdrop for this conversation... "
                " As you were looking at her, "
                " She had these odd pink butterflies circling around her... "
                " But there was this one odd butterfly just staring right at her. "
                " You hid behind a bookshelf and started listening in. "
                tm " Shit, shit shit. "
                tm " This isn't good, not good at all... "
                tm " God damn it - why do my powers have to be acting up?! "
                tm " This is horrible timing. "
                tm " Clio's meds have run out, too... "
                tm " Jesus christ, why now of all times?! "
                tm " I've still got a shit ton to do, come on now... "
                tm " You've just got to keep everything together, Temero. "
                tm " I can't just pray that this shit is gonna go away! "
                tm " ...I've gotta go somewhere else. "
                tm " I don't wanna cause a scene here. "
                tm " It's too unsafe for that. "
                tm " I've gotta go to the teacher's office. "
                tm " As soon as possible. "
                tm " ...While not making myself look suspicious, of course. "
                hide temerosad at right with easeoutright
                " The butterflies disappeared as soon as she ran away... "
                " But the same one that stared at her kept on following her. "
                " That's odd... "
                " Hopefully she's doing alright. "
                scene black with dissolve
                " You spent the rest of the break hanging out at the library. "
                " Just reading random books and stuff... "
                " As you were reading, you couldn't help but think about the girl from earlier... "
                " Kept on wondering what was happening to her. "
                " It's none of your business, but you can't help but feel worried. "
                " Just hope that she feels better soon. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like  it's time for the next class. "
                " You put the book down and you got out of the library to go to the gym for PE. "
                pause 2.0
                jump tpeclass1
            else:
                " Huh, looks like she's doing something important right now. "
                " We're gonna have to eavesdrop for this conversation... "
                " As you were looking at her, "
                " She had these odd pink butterflies circling around her... "
                " But there was this one odd butterfly just staring right at her. "
                " You hid behind a bookshelf and started listening in. "
                x " Shit, shit shit. "
                x " This isn't good, not good at all... "
                x " God damn it - why do my powers have to be acting up?! "
                x " This is horrible timing. "
                x " Clio's meds have run out, too... "
                x " Jesus christ, why now of all times?! "
                x " I've still got a shit ton to do, come on now... "
                $ temeroknow = True
                tm " You've just got to keep everything together, Temero. "
                tm " I can't just pray that this shit is gonna go away! "
                tm " ...I've gotta go somewhere else. "
                tm " I don't wanna cause a scene here. "
                tm " It's too unsafe for that. "
                tm " I've gotta go to the teacher's office. "
                tm " As soon as possible. "
                tm " ...While not making myself look suspicious, of course. "
                hide temerosad at right with easeoutright
                " The butterflies disappeared as soon as she ran away... "
                " But the same one that stared at her kept on following her. "
                " That's odd... "
                " Hopefully she's doing alright. "
                scene black with dissolve
                " You spent the rest of the break hanging out at the library. "
                " Just reading random books and stuff... "
                " As you were reading, you couldn't help but think about the girl from earlier... "
                " Kept on wondering what was happening to her. "
                " It's none of your business, but you can't help but feel worried. "
                " Just hope that she feels better soon. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like  it's time for the next class. "
                " You put the book down and you got out of the library to go to the gym for PE. "
                pause 2.0
                jump tpeclass1
        label kfcnah:
            show noxneutral at center with easeinright
            if noxknow == True:
                " You walked over to him and asked what he was doing. "
                n " Hm...? oh, [name]... "
                n " Come and sit... "
                n " I don't want you to be standing there while we talk.. "
                " You sit down next to him. "
                " Turns out he was playing a game on his phone. "
                " A game where you take care of an egg. "
                " The egg was honestly really well decorated and nice. "
                " Looks like Nox was the one who decorated it. "
                " It looked pretty cute, too. "
                n " I was, um...playing this game, you see... "
                n " You take care of eggs in this game... "
                n " And once they grow old enough, they'll turn into a random animal... "
                n " It depends on how you've treated it... "
                n " If you raised it to be sporty, then it would end up as a different animal... "
                n " If you raise it to be cute, then it would end up as a cute animal... "
                n " There's 7 different animals for each type of egg... "
                n " There's a lot of eggs you can get... "
                n " Oh, and uh... "
                n " This game isn't exactly in the playstore anymore.. "
                n " I don't know why, but the creator kind of just... "
                n " ...Left, and so the game got deleted off of the platform... "
                n " I got this from a friend's file, and they told me it was safe, so... "
                n " I trust them, since they've done stuff like this before for me... "
                n " And I'm happy that they gave me this game... "
                n " It's one of my childhood favorites, actually... "
                n " Hmmhmm... "
                n " Since I have another egg here... "
                n " How about I let you decorate it...? "
                n " It can be in any way you want... "
                menu:
                    " lemme decorate that thang like it's easter time ":
                        $ noxlv += 10
                        hide noxneutral at bottom
                        show noxhappy at center
                        n " Okayyy... "
                        n " Here, take my phone... "
                        " You took Nox's phone so that you could decorate the egg. "
                        " Time for some good decorating... "
                        scene black with dissolve
                        " You spent the rest of the break hanging out with Nox. "
                        " And also decorating his egg he had on his game. "
                        if kind == True:
                            " You made the egg look all nice and cute. "
                        elif calm == True:
                            " You made the egg look pretty chill. "
                        elif mean == True:
                            " You made the egg look emo. "
                        else:
                            pass
                        " After you were done, it actually looked pretty decent. "
                        " Nox also let you rename the egg because he didn't like the name he picked for it. "
                        " You named it: '[name] jr.' "
                        " Very original, you know. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You walked out of the library and went to the gym for PE. "
                        pause 2.0
                        jump tpeclass1
                    " nah it would look like shit ":
                        n " Okaay, if you say so... "
                        n " I'll go ahead and decorate it myself, then... "
                        n " I'm gonna try and make it cutesy... "
                        scene black with dissolve
                        " You spent the rest of the break watching Nox play the game. "
                        " Just watching him play the game... "
                        " After he was done decorating the egg, you thought it actually looked pretty cute. "
                        " He named it 'nox jr.' "
                        " Veeery original, I know. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You walked out of the library and went to the gym for PE. "
                        pause 2.0
                        jump tpeclass1
            else:
                " You walked over to him and asked what he was doing. "
                x " Hm...? oh, [name]... "
                x " Come and sit... "
                x " I don't want you to be standing there while we talk.. "
                " You sit down next to him. "
                " Turns out he was playing a game on his phone. "
                " A game where you take care of an egg. "
                " The egg was honestly really well decorated and nice. "
                " Looks like Nox was the one who decorated it. "
                " It looked pretty cute, too. "
                $ noxknow = True
                n " I'm Nox by the way...Nox Cesso... "
                n " I was, um...playing this game, you see... "
                n " You take care of eggs in this game... "
                n " And once they grow old enough, they'll turn into a random animal... "
                n " It depends on how you've treated it... "
                n " If you raised it to be sporty, then it would end up as a different animal... "
                n " If you raise it to be cute, then it would end up as a cute animal... "
                n " There's 7 different animals for each type of egg... "
                n " There's a lot of eggs you can get... "
                n " Oh, and uh... "
                n " This game isn't exactly in the playstore anymore.. "
                n " I don't know why, but the creator kind of just... "
                n " ...Left, and so the game got deleted off of the platform... "
                n " I got this from a friend's file, and they told me it was safe, so... "
                n " I trust them, since they've done stuff like this before for me... "
                n " And I'm happy that they gave me this game... "
                n " It's one of my childhood favorites, actually... "
                n " Hmmhmm... "
                n " Since I have another egg here... "
                n " How about I let you decorate it...? "
                n " It can be in any way you want... "
                menu:
                    " lemme decorate that thang like it's easter time ":
                        $ noxlv += 10
                        hide noxneutral at bottom
                        show noxhappy at center
                        n " Okayyy... "
                        n " Here, take my phone... "
                        " You took Nox's phone so that you could decorate the egg. "
                        " Time for some good decorating... "
                        scene black with dissolve
                        " You spent the rest of the break hanging out with Nox. "
                        " And also decorating his egg he had on his game. "
                        if kind == True:
                            " You made the egg look all nice and cute. "
                        elif calm == True:
                            " You made the egg look pretty chill. "
                        elif mean == True:
                            " You made the egg look emo. "
                        else:
                            pass
                        " After you were done, it actually looked pretty decent. "
                        " Nox also let you rename the egg because he didn't like the name he picked for it. "
                        " You named it: '[name] jr.' "
                        " Very original, you know. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You walked out of the library and went to the gym for PE. "
                        pause 2.0
                        jump tpeclass1
                    " nah it would look like shit ":
                        n " Okaay, if you say so... "
                        n " I'll go ahead and decorate it myself, then... "
                        n " I'm gonna try and make it cutesy... "
                        scene black with dissolve
                        " You spent the rest of the break watching Nox play the game. "
                        " Just watching him play the game... "
                        " After he was done decorating the egg, you thought it actually looked pretty cute. "
                        " He named it 'nox jr.' "
                        " Veeery original, I know. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You walked out of the library and went to the gym for PE. "
                        pause 2.0
                        jump tpeclass1
label tpeclass1:
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You looked around the gym and waited for the teacher to arrive. "
    " You should hear the door slamming open in 3...2...1... "
    " KA-BOOM! There it is. " with vpunch
    " The teacher's there - and on time. "
    " Time for a painful yet fun lesson in PE. "
    show solneutral at center with easeinright
    msso " HEYA FAM!! "
    msso " Hopefully all of y'all is doing great today!! "
    hide solneutral at bottom
    show solangry at center
    msso " (Well, I know someone who isn't...well...) "
    msso " (Yeah no I shouldn't talk about that.) "
    msso " (I should focus on letting the vibes be nice and easy!) "
    msso " (I don't wanna bring down the mood, after all!) "
    hide solangry at bottom
    show solneutral at center
    msso " Ahem... "
    hide solneutral at bottom
    show solhappy at center
    msso " Because we need all that HAPPINESS AND ENERGY FOR THIS CLASS!! "
    msso " It can't be a Sol class if everyone's all gloomy! "
    msso " If all of you were feeling down, I probably would've made you all do a dance to make everyone feel better! "
    msso " And if that doesn't work... "
    hide solhappy at bottom
    show solneutral at center
    msso " Then maybe we could have a talk? I dunno, really. "
    msso " REMEMBER! It's always fine to talk to me! "
    msso " I'm just one message away, dudes - and I'm not judgemental, "
    msso " Don't worry yer overworked braincells over that! "
    msso " You can always talk to me about whatever you want, and I'll lend you an ear! "
    msso " I need some good gossip every now and then after all. "
    msso " And also to make sure that everyone's feeling better! "
    msso " Anyway...let's get to our lesson for todayyyy!! "
    scene black with dissolve
    " You spent the rest of class hours imitating Mister Sol doing a certain PE related thing. "
    " It was a pose that you all had to do to work out a bit... "
    " And by god, SOL WAS SO FLEXIBLE. "
    " No wonder he got chosen as the PE teacher or something - "
    " That man could fold his whole body like paper. "
    " Technically this world IS paper but uh...yeah, you get my idea. "
    play sound "audio/bellring.mp3"
    " The bell rings after a little bit, looks like it's time for a break. "
    " You walked out of the gym after a good bit. "
    pause 2.0
    jump octhursbreak3
label octhursbreak3:
    scene hallway with dissolve
    " Where would you like to hangout for this break? "
    menu:
        " {image=jamicon} The front of the school {image=koaicon} ":
            jump octhursfront3
        " {image=noxicon} The back of the school {image=yinyangicon} ":
            jump octhursback3
        " {image=matteicon} Back into the gym {image=temeroicon} ":
            jump octhursgym3
        " {image=diskicon} The cafeteria {image=orchidicon} ":
            jump octhurscafeteria3
        " {image=quinnicon} The rooftop {image=jacobicon} ":
            jump octhursrooftop3
        " {image=sparkicon} The library {image=carmenicon} ":
            jump octhurslibrary3
    label octhursfront3:
        # jam and koa
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked into the front of the school and spotted two of your classmates doing their own things. "
        " You wanted to talk to one of them...but who do you talk to? "
        if jamknow == True and koaknow == True:
            menu:
                " {image=jamicon} Jam {image=jamicon} ":
                    jump jamandbutter
                " {image=koaicon} Koa {image=koaicon} ":
                    jump koathecouchlmao
        elif jamknow == True and koaknow == False:
            menu:
                " {image=jamicon} Jam {image=jamicon} ":
                    jump jamandbutter
                " {image=koaicon} An emo looking guy {image=koaicon} ":
                    jump koathecouchlmao
        elif jamknow == False and koaknow == True:
            menu:
                " {image=jamicon} A mean looking girl {image=jamicon} ":
                    jump jamandbutter
                " {image=koaicon} Koa {image=koaicon} ":
                    jump koathecouchlmao
        else:
            menu:
                " {image=jamicon} A mean looking girl {image=jamicon} ":
                    jump jamandbutter
                " {image=koaicon} An emo looking guy {image=koaicon} ":
                    jump koathecouchlmao
        label jamandbutter:
            show jamneutral at center with easeinleft
            if jamknow == True:
                ja " ... "
                " Well, looks like she's thinking about something. "
                " Of course I wouldn't know what she's thinking about. "
                " But, if I had to guess... "
                " She's probably thinking about that one girl she's been thinking about. "
                " You probably don't know her, but it's that one artsy girl in your class. "
                " Geez, I feel like a gossipy uncle talking to you like this, lmao. "
                " But I know you probably want to know what she's thinking about, so... "
                hide jamneutral at bottom
                show jamsurprised at center
                ja " Oh, uh...? [name]? "
                ja " I'm sorry I didn't notice you at first. "
                ja " I just zoned out for a bit. "
                hide jamsurprised at bottom
                show jamneutral at center
                ja " Was just thinking about...a few things. "
                ja " Things that I don't want to talk about too much. "
                ja " Best not to think too much about that. "
                ja " Ahem... "
                ja " Uh... "
                hide jamneutral at bottom
                show jamsad at center
                ja " (Okayyy...now I don't know what to talk about.) "
                ja " (I don't want to make [them] uncomfortable or anything.) "
                ja " (Ueehh...I hate awkward silence.) "
                ja " (Let's see...what can I talk about right now...?) "
                ja " (Hmhmmm...) "
                hide jamsad at bottom
                show jamneutral at center
                ja " ...Have you seen that new painting Matte is working on? "
                ja " She's been posting progress on it on her account. "
                ja " It's been looking great, in my opinion. "
                ja " (Well, all of her paintings are good, in my opinion...) "
                ja " (I don't want to go too off topic though.) "
                ja " Hmhmmm... "
                ja " Sometimes I ask Matte for help on drawing. "
                ja " I showed her one of my drawings once... "
                ja " It was really embarrassing. A drawing of myself. "
                ja " And the thing is? she said it looked fine. "
                hide jamneutral at bottom
                show jamconfused at center
                ja " I literally looked like I chicken scratched that thing. "
                ja " Don't you hate chicken scratching??? "
                ja " Atleast that's what I heard about her... "
                ja " But if she says it looks fine, then uh... "
                hide jamconfused at bottom
                show jamneutral at center
                ja " I guess it is, then. "
                ja " Can't really argue with her, really. "
                ja " I just agree to whatever she says, in all honesty. "
                ja " (There's some times where I don't, but...) "
                ja " (It's easy to forgive her for things like that.) "
                ja " (Like that one disagreement I had with her that one day...) "
                ja " (I think I was just really jealous that time.) "
                ja " Ahem... "
                ja " How about we talk about how your day's been going, [name]? "
                scene black with dissolve
                " You spent the rest of the break talking with Jam. "
                " Just talking about random things... "
                " And talking about Matte every now and then. "
                " Jam and Matte most definitely have something to do with eachother. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump tgardeningclass1
            else:
                x " ... "
                " Well, looks like she's thinking about something. "
                " Of course I wouldn't know what she's thinking about. "
                " But, if I had to guess... "
                " She's probably thinking about that one girl she's been thinking about. "
                " You probably don't know her, but it's that one artsy girl in your class. "
                " Geez, I feel like a gossipy uncle talking to you like this, lmao. "
                " But I know you probably want to know what she's thinking about, so... "
                hide jamneutral at bottom
                show jamsurprised at center
                x " Oh, uh...? [name]? "
                x " I'm sorry I didn't notice you at first. "
                x " I just zoned out for a bit. "
                $ jamknow = True
                ja " I'm uh...Jam, by the way. "
                hide jamsurprised at bottom
                show jamneutral at center
                ja " Was just thinking about...a few things. "
                ja " Things that I don't want to talk about too much. "
                ja " Best not to think too much about that. "
                ja " Ahem... "
                ja " Uh... "
                hide jamneutral at bottom
                show jamsad at center
                ja " (Okayyy...now I don't know what to talk about.) "
                ja " (I don't want to make [them] uncomfortable or anything.) "
                ja " (Ueehh...I hate awkward silence.) "
                ja " (Let's see...what can I talk about right now...?) "
                ja " (Hmhmmm...) "
                hide jamsad at bottom
                show jamneutral at center
                ja " ...Have you seen that new painting Matte is working on? "
                ja " She's been posting progress on it on her account. "
                ja " It's been looking great, in my opinion. "
                ja " (Well, all of her paintings are good, in my opinion...) "
                ja " (I don't want to go too off topic though.) "
                ja " Hmhmmm... "
                ja " Sometimes I ask Matte for help on drawing. "
                ja " I showed her one of my drawings once... "
                ja " It was really embarrassing. A drawing of myself. "
                ja " And the thing is? she said it looked fine. "
                hide jamneutral at bottom
                show jamconfused at center
                ja " I literally looked like I chicken scratched that thing. "
                ja " Don't you hate chicken scratching??? "
                ja " Atleast that's what I heard about her... "
                ja " But if she says it looks fine, then uh... "
                hide jamconfused at bottom
                show jamneutral at center
                ja " I guess it is, then. "
                ja " Can't really argue with her, really. "
                ja " I just agree to whatever she says, in all honesty. "
                ja " (There's some times where I don't, but...) "
                ja " (It's easy to forgive her for things like that.) "
                ja " (Like that one disagreement I had with her that one day...) "
                ja " (I think I was just really jealous that time.) "
                ja " Ahem... "
                ja " How about we talk about how your day's been going, [name]? "
                scene black with dissolve
                " You spent the rest of the break talking with Jam. "
                " Just talking about random things... "
                " And talking about Matte every now and then. "
                " Jam and Matte most definitely have something to do with eachother. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump tgardeningclass1
        label koathecouchlmao:
            show koaneutral at center with easeinright
            if koaknow == True:
                " You walked over to him and asked him what he was doing. "
                " ...Actually, you could already tell what he was doing. "
                " Reading a book underneath a tree, duh. "
                " You already asked him though, so...yeah. "
                k " ...? oh, [name]. Sorry, I didn't see you. "
                k " I was just reading a book to pass the time... "
                k " Orchid didn't come up to me, so I figure'd they're out making friends again. "
                k " And honestly? I'm happy for them. "
                k " Back then they were really quiet...only speaks when spoken to. "
                k " But they started getting real energetic the moment I became friends with them. "
                k " They've really grown a lot, huh? "
                k " Hmhmm... "
                " He seems to be going back to his reading. "
                " You don't really know what else to talk to him about... "
                " You sat down next to him on the ground and thought about what you should talk about to him... "
                " You then asked him if he had music that he liked. "
                k " Oh, music? "
                k " Surprisingly... "
                k " I don't listen to music too much. "
                k " I mean, there's times that I do... "
                k " But I doubt it be anything interesting to you. "
                k " ...I like classical music. "
                k " I don't listen to it all the time, but it still sounds nice and relaxing. "
                k " Orchid is...the opposite of me. Music-wise and personality-wise. "
                k " They REALLY like energetic songs. "
                k " And...very interesting songs with interesting lyrics in them. "
                k " Sometimes I get concerned for them liking that stuff, buuut... "
                k " I don't really judge - they're my friend, after all. "
                k " And friends don't judge...right? "
                k " ...Now that I think about it, Orchid might be one of my closest friends at this school. "
                k " Or, they're really the closest friend that I have. I guess. "
                k " I'm glad I got to make a little bit of an impact in their life though. "
                k " I think I've already told you how earlier - they were shy, and now they feel more confident. "
                k " They've been taking a lot of my advice lately... "
                k " To not worry about the little things in life too much...you get the idea. "
                k " I'm happy for them. "
                scene black with dissolve
                " You spent the rest of the break talking with Koa. "
                " And also reading with Koa. "
                " You actually went and read some of the parts of the book that Koa was reading. "
                " It was a nice book, that's all you could say. "
                " What genre was about the book?{p} uh {nw} "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump tgardeningclass1
            else:
                " You walked over to him and asked him what he was doing. "
                " ...Actually, you could already tell what he was doing. "
                " Reading a book underneath a tree, duh. "
                " You already asked him though, so...yeah. "
                x " ...? oh, [name]. Sorry, I didn't see you. "
                $ koaknow = True
                k " ...'m Koa, by the way. "
                k " I was just reading a book to pass the time... "
                k " Orchid didn't come up to me, so I figure'd they're out making friends again. "
                k " And honestly? I'm happy for them. "
                k " Back then they were really quiet...only speaks when spoken to. "
                k " But they started getting real energetic the moment I became friends with them. "
                k " They've really grown a lot, huh? "
                k " Hmhmm... "
                " He seems to be going back to his reading. "
                " You don't really know what else to talk to him about... "
                " You sat down next to him on the ground and thought about what you should talk about to him... "
                " You then asked him if he had music that he liked. "
                k " Oh, music? "
                k " Surprisingly... "
                k " I don't listen to music too much. "
                k " I mean, there's times that I do... "
                k " But I doubt it be anything interesting to you. "
                k " ...I like classical music. "
                k " I don't listen to it all the time, but it still sounds nice and relaxing. "
                k " Orchid is...the opposite of me. Music-wise and personality-wise. "
                k " They REALLY like energetic songs. "
                k " And...very interesting songs with interesting lyrics in them. "
                k " Sometimes I get concerned for them liking that stuff, buuut... "
                k " I don't really judge - they're my friend, after all. "
                k " And friends don't judge...right? "
                k " ...Now that I think about it, Orchid might be one of my closest friends at this school. "
                k " Or, they're really the closest friend that I have. I guess. "
                k " I'm glad I got to make a little bit of an impact in their life though. "
                k " I think I've already told you how earlier - they were shy, and now they feel more confident. "
                k " They've been taking a lot of my advice lately... "
                k " To not worry about the little things in life too much...you get the idea. "
                k " I'm happy for them. "
                scene black with dissolve
                " You spent the rest of the break talking with Koa. "
                " And also reading with Koa. "
                " You actually went and read some of the parts of the book that Koa was reading. "
                " It was a nice book, that's all you could say. "
                " What genre was about the book?{p} uh {nw} "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump tgardeningclass1
    label octhursback3:
        # nox and yinhui
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of the school and spotted two of your classmates talking to eachother. "
        " Curious on what they were talking about, you decided to walk over to them. "
        show noxneutral at left with easeinright
        show yinhuineutral at right with easeinright
        if noxknow == True and yinhuiknow == True:
            n " Look...[name]'s here... "
            yi " Huh? oh, you. "
            yi " Help me deal with this idiot over here. "
            " You asked him what happened. "
            yi " ...I'll just let the guy explain to you. "
            hide noxneutral at bottom
            show noxsad at left
            n " So... "
            n " I {i}may{/i} or may not have lost my bottle of meds around the school... "
            n " And the thing is I don't remember where I last put it... "
            n " I'm sure it was just in my bag, though... "
            hide noxsad at bottom
            show noxneutral at center
            yi " How could you lose something that was in your bag?? "
            n " I dunno... "
            n " I might've taken it out and placed it somewhere... "
            n " Most likely right before Sol's class... "
            yi " Did you put it in the gym, or outside of the gym? "
            n " I'm pretty sure it was outside... "
            yi " Okay...that just made things a lot harder now. "
            yi " Where do you last remember going? "
            hide noxneutral at bottom
            show noxneutralb2 at left
            n " Um... "
            hide yinhuineutral at bottom
            show yinhuiangry at right
            yi " (God, I'm trying not to lose my patience right now.) "
            yi " (Calm down, Yinhui...calm.) "
            yi " (You've got to help Nox here, after all.) "
            yi " (You don't accidentally want to scare someone away, right?) "
            hide yinhuiangry at bottom
            show yinhuineutral at right
            n " I remember... "
            hide noxneutralb2 at bottom
            show noxneutral at left
            n " I think I went to the library, last break... "
            yi " God we're going to have to look at all of the corners of the library for this. "
            yi " Siiighh... "
            yi " Okay - AT LEAST you remember where you last went. "
            yi " We would've looked through the entire school if you didn't. "
            yi " ...And might've asked one of the teachers for help. "
            n " If I didn't though...who would we ask...? "
            yi " Probably Mister Sol - wait, we're getting off track. "
            yi " Okay, uh... "
            yi " [name] - I'm gonna ask this to make sure you're gonna be a part of this. "
            yi " You wanna help us look for this thing or not? "
            yi " I wouldn't want to help, but then again I don't want to carry around this idiot 'cause he fainted randomly in class all day. "
            yi " So? what's your choice? we don't got all day for this. "
            menu:
                " I'm gonna help ":
                    $ noxlv += 10
                    $ yinhuilv += 5
                    hide yinhuineutral at bottom
                    show yinhuiheh at right
                    yi " Good, cause I would've broken your bones if you didn't. "
                    yi " Would be much faster if there were three of us working on this. "
                    yi " And I don't want to spend all day looking around in the library for some meds. "
                    n " ...Erh, I'm glad you're helping, [name]. "
                    n " How about we...go and look at the library now...? "
                    n " I don't want to waste more time... "
                    hide yinhuiheh at bottom
                    show yinhuineutral at right
                    yi " Good thinking, Nox. "
                    yi " Come on, let's go. "
                    yi " Like they said: no more time to waste. "
                    scene black with dissolve
                    " You spent the rest of the break at the library trying to find Nox's meds. "
                    " After a bit of looking, turns out the meds were at the librarian's desk. "
                    " And all of you SWORE that it wasn't even there before. "
                    " Someone must've found it while you all were looking around. "
                    " There was absolutely no way that it was just right there. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked into your classroom after a bit of walking around. "
                    pause 2.0
                    jump tgardeningclass1
                " I got other things to do ":
                    hide yinhuineutral at bottom
                    show yinhuiangry at right
                    yi " ... "
                    " He looks like he's holding in a lot of words right now. "
                    " Ruh roh. "
                    n " ...Yinhui, it's okay... "
                    n " I'll help you look around, of course... "
                    n " And if we can't find anything - we'll just ask for help... "
                    n " Okay...? "
                    " That looked like it didn't help at all. "
                    " Before you could get your ass beat, you decided to skedaddle the hell away. "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the halls. "
                    " Though you avoided looking in the library to prevent your ass being beat. "
                    " You did NOT want to risk your bones being broken for not helping. "
                    " Wonder why that guy looked so mad though... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked into your classroom after a bit of walking around. "
                    pause 2.0
                    jump tgardeningclass1
        elif noxknow == True and yinhuiknow == False:
            n " Look...[name]'s here... "
            x " Huh? oh, you. "
            x " Help me deal with this idiot over here. "
            " You asked him what happened. "
            x " ...I'll just let the guy explain to you. "
            hide noxneutral at bottom
            show noxsad at left
            n " So... "
            n " I {i}may{/i} or may not have lost my bottle of meds around the school... "
            n " And the thing is I don't remember where I last put it... "
            n " I'm sure it was just in my bag, though... "
            hide noxsad at bottom
            show noxneutral at center
            x " How could you lose something that was in your bag?? "
            n " I dunno... "
            n " I might've taken it out and placed it somewhere... "
            n " Most likely right before Sol's class... "
            x " Did you put it in the gym, or outside of the gym? "
            n " I'm pretty sure it was outside... "
            x " Okay...that just made things a lot harder now. "
            x " Where do you last remember going? "
            hide noxneutral at bottom
            show noxneutralb2 at left
            n " Um... "
            hide yinhuineutral at bottom
            show yinhuiangry at right
            x " (God, I'm trying not to lose my patience right now.) "
            $ yinhuiknow = True
            yi " (Calm down, Yinhui...calm.) "
            yi " (You've got to help Nox here, after all.) "
            yi " (You don't accidentally want to scare someone away, right?) "
            hide yinhuiangry at bottom
            show yinhuineutral at right
            n " I remember... "
            hide noxneutralb2 at bottom
            show noxneutral at left
            n " I think I went to the library, last break... "
            yi " God we're going to have to look at all of the corners of the library for this. "
            yi " Siiighh... "
            yi " Okay - AT LEAST you remember where you last went. "
            yi " We would've looked through the entire school if you didn't. "
            yi " ...And might've asked one of the teachers for help. "
            n " If I didn't though...who would we ask...? "
            yi " Probably Mister Sol - wait, we're getting off track. "
            yi " Okay, uh... "
            yi " [name] - I'm gonna ask this to make sure you're gonna be a part of this. "
            yi " You wanna help us look for this thing or not? "
            yi " I wouldn't want to help, but then again I don't want to carry around this idiot 'cause he fainted randomly in class all day. "
            yi " So? what's your choice? we don't got all day for this. "
            menu:
                " I'm gonna help ":
                    $ noxlv += 10
                    $ yinhuilv += 5
                    hide yinhuineutral at bottom
                    show yinhuiheh at right
                    yi " Good, cause I would've broken your bones if you didn't. "
                    yi " Would be much faster if there were three of us working on this. "
                    yi " And I don't want to spend all day looking around in the library for some meds. "
                    n " ...Erh, I'm glad you're helping, [name]. "
                    n " How about we...go and look at the library now...? "
                    n " I don't want to waste more time... "
                    hide yinhuiheh at bottom
                    show yinhuineutral at right
                    yi " Good thinking, Nox. "
                    yi " Come on, let's go. "
                    yi " Like they said: no more time to waste. "
                    scene black with dissolve
                    " You spent the rest of the break at the library trying to find Nox's meds. "
                    " After a bit of looking, turns out the meds were at the librarian's desk. "
                    " And all of you SWORE that it wasn't even there before. "
                    " Someone must've found it while you all were looking around. "
                    " There was absolutely no way that it was just right there. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked into your classroom after a bit of walking around. "
                    pause 2.0
                    jump tgardeningclass1
                " I got other things to do ":
                    hide yinhuineutral at bottom
                    show yinhuiangry at right
                    yi " ... "
                    " He looks like he's holding in a lot of words right now. "
                    " Ruh roh. "
                    n " ...Yinhui, it's okay... "
                    n " I'll help you look around, of course... "
                    n " And if we can't find anything - we'll just ask for help... "
                    n " Okay...? "
                    " That looked like it didn't help at all. "
                    " Before you could get your ass beat, you decided to skedaddle the hell away. "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the halls. "
                    " Though you avoided looking in the library to prevent your ass being beat. "
                    " You did NOT want to risk your bones being broken for not helping. "
                    " Wonder why that guy looked so mad though... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked into your classroom after a bit of walking around. "
                    pause 2.0
                    jump tgardeningclass1
        elif noxknow == False and yinhuiknow == True:
            x " Look...[name]'s here... "
            yi " Huh? oh, you. "
            yi " Help me deal with this idiot over here. "
            " You asked him what happened. "
            yi " ...I'll just let the guy explain to you. "
            hide noxneutral at bottom
            show noxsad at left
            x " So... "
            x " I {i}may{/i} or may not have lost my bottle of meds around the school... "
            x " And the thing is I don't remember where I last put it... "
            x " I'm sure it was just in my bag, though... "
            hide noxsad at bottom
            show noxneutral at center
            yi " How could you lose something that was in your bag?? "
            x " I dunno... "
            x " I might've taken it out and placed it somewhere... "
            x " Most likely right before Sol's class... "
            yi " Did you put it in the gym, or outside of the gym? "
            x " I'm pretty sure it was outside... "
            yi " Okay...that just made things a lot harder now. "
            yi " Where do you last remember going? "
            hide noxneutral at bottom
            show noxneutralb2 at left
            x " Um... "
            hide yinhuineutral at bottom
            show yinhuiangry at right
            yi " (God, I'm trying not to lose my patience right now.) "
            yi " (Calm down, Yinhui...calm.) "
            $ noxknow = True
            yi " (You've got to help Nox here, after all.) "
            yi " (You don't accidentally want to scare someone away, right?) "
            hide yinhuiangry at bottom
            show yinhuineutral at right
            n " I remember... "
            hide noxneutralb2 at bottom
            show noxneutral at left
            n " I think I went to the library, last break... "
            yi " God we're going to have to look at all of the corners of the library for this. "
            yi " Siiighh... "
            yi " Okay - AT LEAST you remember where you last went. "
            yi " We would've looked through the entire school if you didn't. "
            yi " ...And might've asked one of the teachers for help. "
            n " If I didn't though...who would we ask...? "
            yi " Probably Mister Sol - wait, we're getting off track. "
            yi " Okay, uh... "
            yi " [name] - I'm gonna ask this to make sure you're gonna be a part of this. "
            yi " You wanna help us look for this thing or not? "
            yi " I wouldn't want to help, but then again I don't want to carry around this idiot 'cause he fainted randomly in class all day. "
            yi " So? what's your choice? we don't got all day for this. "
            menu:
                " I'm gonna help ":
                    $ noxlv += 10
                    $ yinhuilv += 5
                    hide yinhuineutral at bottom
                    show yinhuiheh at right
                    yi " Good, cause I would've broken your bones if you didn't. "
                    yi " Would be much faster if there were three of us working on this. "
                    yi " And I don't want to spend all day looking around in the library for some meds. "
                    n " ...Erh, I'm glad you're helping, [name]. "
                    n " How about we...go and look at the library now...? "
                    n " I don't want to waste more time... "
                    hide yinhuiheh at bottom
                    show yinhuineutral at right
                    yi " Good thinking, Nox. "
                    yi " Come on, let's go. "
                    yi " Like they said: no more time to waste. "
                    scene black with dissolve
                    " You spent the rest of the break at the library trying to find Nox's meds. "
                    " After a bit of looking, turns out the meds were at the librarian's desk. "
                    " And all of you SWORE that it wasn't even there before. "
                    " Someone must've found it while you all were looking around. "
                    " There was absolutely no way that it was just right there. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked into your classroom after a bit of walking around. "
                    pause 2.0
                    jump tgardeningclass1
                " I got other things to do ":
                    hide yinhuineutral at bottom
                    show yinhuiangry at right
                    yi " ... "
                    " He looks like he's holding in a lot of words right now. "
                    " Ruh roh. "
                    n " ...Yinhui, it's okay... "
                    n " I'll help you look around, of course... "
                    n " And if we can't find anything - we'll just ask for help... "
                    n " Okay...? "
                    " That looked like it didn't help at all. "
                    " Before you could get your ass beat, you decided to skedaddle the hell away. "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the halls. "
                    " Though you avoided looking in the library to prevent your ass being beat. "
                    " You did NOT want to risk your bones being broken for not helping. "
                    " Wonder why that guy looked so mad though... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked into your classroom after a bit of walking around. "
                    pause 2.0
                    jump tgardeningclass1
        else:
            x " Look...[name]'s here... "
            x " Huh? oh, you. "
            x " Help me deal with this idiot over here. "
            " You asked him what happened. "
            x " ...I'll just let the guy explain to you. "
            hide noxneutral at bottom
            show noxsad at left
            x " So... "
            x " I {i}may{/i} or may not have lost my bottle of meds around the school... "
            x " And the thing is I don't remember where I last put it... "
            x " I'm sure it was just in my bag, though... "
            hide noxsad at bottom
            show noxneutral at center
            x " How could you lose something that was in your bag?? "
            x " I dunno... "
            x " I might've taken it out and placed it somewhere... "
            x " Most likely right before Sol's class... "
            x " Did you put it in the gym, or outside of the gym? "
            x " I'm pretty sure it was outside... "
            x " Okay...that just made things a lot harder now. "
            x " Where do you last remember going? "
            hide noxneutral at bottom
            show noxneutralb2 at left
            x " Um... "
            hide yinhuineutral at bottom
            show yinhuiangry at right
            x " (God, I'm trying not to lose my patience right now.) "
            $ yinhuiknow = True
            $ noxknow = True
            yi " (Calm down, Yinhui...calm.) "
            yi " (You've got to help Nox here, after all.) "
            yi " (You don't accidentally want to scare someone away, right?) "
            hide yinhuiangry at bottom
            show yinhuineutral at right
            n " I remember... "
            hide noxneutralb2 at bottom
            show noxneutral at left
            n " I think I went to the library, last break... "
            yi " God we're going to have to look at all of the corners of the library for this. "
            yi " Siiighh... "
            yi " Okay - AT LEAST you remember where you last went. "
            yi " We would've looked through the entire school if you didn't. "
            yi " ...And might've asked one of the teachers for help. "
            n " If I didn't though...who would we ask...? "
            yi " Probably Mister Sol - wait, we're getting off track. "
            yi " Okay, uh... "
            yi " [name] - I'm gonna ask this to make sure you're gonna be a part of this. "
            yi " You wanna help us look for this thing or not? "
            yi " I wouldn't want to help, but then again I don't want to carry around this idiot 'cause he fainted randomly in class all day. "
            yi " So? what's your choice? we don't got all day for this. "
            menu:
                " I'm gonna help ":
                    $ noxlv += 10
                    $ yinhuilv += 5
                    hide yinhuineutral at bottom
                    show yinhuiheh at right
                    yi " Good, cause I would've broken your bones if you didn't. "
                    yi " Would be much faster if there were three of us working on this. "
                    yi " And I don't want to spend all day looking around in the library for some meds. "
                    n " ...Erh, I'm glad you're helping, [name]. "
                    n " How about we...go and look at the library now...? "
                    n " I don't want to waste more time... "
                    hide yinhuiheh at bottom
                    show yinhuineutral at right
                    yi " Good thinking, Nox. "
                    yi " Come on, let's go. "
                    yi " Like they said: no more time to waste. "
                    scene black with dissolve
                    " You spent the rest of the break at the library trying to find Nox's meds. "
                    " After a bit of looking, turns out the meds were at the librarian's desk. "
                    " And all of you SWORE that it wasn't even there before. "
                    " Someone must've found it while you all were looking around. "
                    " There was absolutely no way that it was just right there. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked into your classroom after a bit of walking around. "
                    pause 2.0
                    jump tgardeningclass1
                " I got other things to do ":
                    hide yinhuineutral at bottom
                    show yinhuiangry at right
                    yi " ... "
                    " He looks like he's holding in a lot of words right now. "
                    " Ruh roh. "
                    n " ...Yinhui, it's okay... "
                    n " I'll help you look around, of course... "
                    n " And if we can't find anything - we'll just ask for help... "
                    n " Okay...? "
                    " That looked like it didn't help at all. "
                    " Before you could get your ass beat, you decided to skedaddle the hell away. "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the halls. "
                    " Though you avoided looking in the library to prevent your ass being beat. "
                    " You did NOT want to risk your bones being broken for not helping. "
                    " Wonder why that guy looked so mad though... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked into your classroom after a bit of walking around. "
                    pause 2.0
                    jump tgardeningclass1
    label octhursgym3:
        # matte and temero
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked to the gym and spotted your classmates doing their own things. "
        " You wanted to talk to one of them...but who do you talk to? "
        if matteknow == True and temeroknow == True:
            menu:
                " {image=matteicon} Matte {image=matteicon} ":
                    jump takokopi
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump tatakopi
        elif matteknow == True and temeroknow == False:
            menu:
                " {image=matteicon} Matte {image=matteicon} ":
                    jump takokopi
                " {image=temeroicon} The science-y girl {image=temeroicon} ":
                    jump tatakopi
        elif matteknow == False and temeroknow == True:
            menu:
                " {image=matteicon} The artsy girl {image=matteicon} ":
                    jump takokopi
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump tatakopi
        else:
            menu:
                " {image=matteicon} The artsy girl {image=matteicon} ":
                    jump takokopi
                " {image=temeroicon} The science-y girl {image=temeroicon} ":
                    jump tatakopi
        label takokopi:
            show matteneutral at center with easeinright
            if matteknow == True:
                " You walked over to her and asked what she was doing. "
                hide matteneutral at bottom
                show mattehappy at center
                ma " Hiyaaa, [name]!! "
                ma " Lovely to see you're doing great here! "
                ma " I was just looking around and trying to get some art inspo, you know? "
                hide mattehappy at bottom
                show matteneutral at center
                ma " Inspo as in inspiration, of course. "
                ma " You can take a whole lot of things for inspiration! "
                ma " That can be other peoples art... "
                ma " The things around you... "
                ma " Oh hey, that just gave me an idea, actually! "
                ma " I could make a gjinka of something in here... "
                ma " Hmmhmmm... "
                ma " Maybe I could make a humanization of the bleachers? "
                ma " I think I already have an idea for that! "
                ma " I could also make an idea for gjinkas of sports balls... "
                ma " And even more ideas... "
                ma " Hmhmmm!! I have motivation to draw now!! "
                hide matteneutral at bottom
                show mattesad at center
                ma " Wish it was always this easy to get motivation, hehe... "
                ma " Getting art motivation like this isn't all that easy, you know! "
                ma " Sometimes you feel like drawing, but then other times... "
                ma " Other times, you just feel too much like shit, you get me? "
                ma " You just look at your canvas and decide that you're gonna do it tomorrow... "
                ma " ...Even though you're probably not gonna finish it. "
                ma " That happens to me a lot, by the way. "
                ma " Siiigh... "
                hide mattesad at bottom
                show matteneutral at center
                ma " Anywho - you can watch me while I'm drawing, [name]!! "
                ma " I don't mind, really. "
                ma " You can actually tell me if there's anything I should change in the drawing! "
                ma " I really need some opinions, after all. "
                ma " Gotta make sure it looks perfect! "
                scene black with dissolve
                " You spent the rest of the break looking at Matte's drawing. "
                " As she was drawing, you were also giving her some of your opinions. "
                " Some stuff like changing a few things here and there... "
                " And also some stuff like adding things onto the character she was drawing. "
                " The end result looked pretty good, in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another break. "
                " You walked out of the gym and went to your classroom for the next class. "
                pause 2.0
                jump tgardeningclass1
            else:
                " You walked over to her and asked what she was doing. "
                hide matteneutral at bottom
                show mattehappy at center
                x " Hiyaaa, [name]!! "
                x " Lovely to see you're doing great here! "
                $ matteknow = True
                ma " Oh - uh...I'm Matte, by the way! "
                ma " I was just looking around and trying to get some art inspo, you know? "
                hide mattehappy at bottom
                show matteneutral at center
                ma " Inspo as in inspiration, of course. "
                ma " You can take a whole lot of things for inspiration! "
                ma " That can be other peoples art... "
                ma " The things around you... "
                ma " Oh hey, that just gave me an idea, actually! "
                ma " I could make a gjinka of something in here... "
                ma " Hmmhmmm... "
                ma " Maybe I could make a humanization of the bleachers? "
                ma " I think I already have an idea for that! "
                ma " I could also make an idea for gjinkas of sports balls... "
                ma " And even more ideas... "
                ma " Hmhmmm!! I have motivation to draw now!! "
                hide matteneutral at bottom
                show mattesad at center
                ma " Wish it was always this easy to get motivation, hehe... "
                ma " Getting art motivation like this isn't all that easy, you know! "
                ma " Sometimes you feel like drawing, but then other times... "
                ma " Other times, you just feel too much like shit, you get me? "
                ma " You just look at your canvas and decide that you're gonna do it tomorrow... "
                ma " ...Even though you're probably not gonna finish it. "
                ma " That happens to me a lot, by the way. "
                ma " Siiigh... "
                hide mattesad at bottom
                show matteneutral at center
                ma " Anywho - you can watch me while I'm drawing, [name]!! "
                ma " I don't mind, really. "
                ma " You can actually tell me if there's anything I should change in the drawing! "
                ma " I really need some opinions, after all. "
                ma " Gotta make sure it looks perfect! "
                scene black with dissolve
                " You spent the rest of the break looking at Matte's drawing. "
                " As she was drawing, you were also giving her some of your opinions. "
                " Some stuff like changing a few things here and there... "
                " And also some stuff like adding things onto the character she was drawing. "
                " The end result looked pretty good, in your opinion. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another break. "
                " You walked out of the gym and went to your classroom for the next class. "
                pause 2.0
                jump tgardeningclass1
        label tatakopi:
            show temeroneutral at center with easeinleft
            if temeroknow == True:
                " You walked over to her and asked what she was doing. "
                hide temeroneutral at bottom
                show temeroangry at center
                tm " Huh? whozzat talkin' to me? "
                tm " Better be important - "
                " She looks around for a bit before looking behind her. "
                hide temeroangry at bottom
                show temeroneutral at center
                tm " Oh! it's, a...uhh...you! "
                tm " [name], right? "
                tm " Cool cool - I was just doing one of my experiments over here! "
                tm " 'But Temero - isn't that unsafe?' "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " It sure as hell is! "
                tm " But we don't care about safety around here. "
                tm " (Well, we actually do.) "
                tm " (I mean, at least the teachers do...) "
                tm " (But they kinda give me a pass.) "
                tm " (Sooo...that means more fun for us, hooray!) "
                tm " (Me and this other guy have a pass, so we're all good.) "
                tm " (Don't worry about it too much!) "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " A-HEM! Now, I'll be telling you what I'm doing for today! "
                tm " I'll be experimenting on this cool pink butterfly!! "
                tm " ...Lemme let you in on a secret here. "
                tm " I actually made this butterfly. "
                tm " This butterfly is a clone of another butterfly that's from the wild... "
                tm " Don't worry - I didn't do anything dangerous to that specific butterfly. "
                tm " I just used to clone it, alright? "
                tm " This butterfly over here has special things to it - "
                tm " I made it so that this one is more able to survive during experiments... "
                tm " And I also made it to have special cool powers in case if it's actually in danger ouside of experiments. "
                tm " Pretty neaaat, right? "
                tm " Now, watch this cool thing I can do... "
                " She pours some sparkling water onto it...well, what looks like sparkling water. "
                " You waited for something to happen, but nothing did. "
                tm " Just give it a few moments now. "
                tm " You've gotta be patient for these things, after all! "
                " You waited...and it happened. The butterfly started to tweak out for a bit... "
                " Before it basically caused a disco effect around the room. "
                " It's basically how your normal disco would look around the room, but instead it's butterflies. "
                tm " Cool, right? "
                menu:
                    " VERY COOL ":
                        $ temerolv += 10
                        hide temeroneutral at bottom
                        show temerohappy at center
                        tm " Riiight? "
                        tm " You can come over to me whenever I'm doing some cool experiments! "
                        tm " Though, uh... "
                        tm " Just make sure that I'm actually doing some experiments. "
                        tm " I don't want you to walk in whenever I'm having a call, you know. "
                        tm " That would be awkward for both me and the person I'm on the phone with, haha! "
                        scene black with dissolve
                        " You spent the rest of the break hanging out with Temero. "
                        " Just giving her some ideas for some new experiments... "
                        " Like making the butterflies wings way bigger. "
                        " You wonder if she's going to do this onto humans like you, too. "
                        " Probably not, but there's always a chance. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the gym and went to your classroom for gardening class. "
                        pause 2.0
                        jump tgardeningclass1
                    " it's alright ":
                        tm " Riiight? "
                        tm " You can come over to me whenever I'm doing some cool experiments! "
                        tm " Though, uh... "
                        tm " Just make sure that I'm actually doing some experiments. "
                        tm " I don't want you to walk in whenever I'm having a call, you know. "
                        tm " That would be awkward for both me and the person I'm on the phone with, haha! "
                        scene black with dissolve
                        " You spent the rest of the break hanging out with Temero. "
                        " Just giving her some ideas for some new experiments... "
                        " Like making the butterflies wings way bigger. "
                        " You wonder if she's going to do this onto humans like you, too. "
                        " Probably not, but there's always a chance. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the gym and went to your classroom for gardening class. "
                        pause 2.0
                        jump tgardeningclass1
            else:
                " You walked over to her and asked what she was doing. "
                hide temeroneutral at bottom
                show temeroangry at center
                x " Huh? whozzat talkin' to me? "
                x " Better be important - "
                " She looks around for a bit before looking behind her. "
                hide temeroangry at bottom
                show temeroneutral at center
                x " Oh! it's, a...uhh...you! "
                x " [name], right? "
                $ temeroknow = True
                x " Hopefully I didn't get that wrong, heheh. "
                x " I should probably introduce myself to you, so... "
                tm " I'm the GREAT Temero NEO! Just call me Temero or Neo, I don't mind either. "
                tm " Annyyywayyy - I was just doing one of my experiments over here! "
                tm " 'But Temero - isn't that unsafe?' "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " It sure as hell is! "
                tm " But we don't care about safety around here. "
                tm " (Well, we actually do.) "
                tm " (I mean, at least the teachers do...) "
                tm " (But they kinda give me a pass.) "
                tm " (Sooo...that means more fun for us, hooray!) "
                tm " (Me and this other guy have a pass, so we're all good.) "
                tm " (Don't worry about it too much!) "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " A-HEM! Now, I'll be telling you what I'm doing for today! "
                tm " I'll be experimenting on this cool pink butterfly!! "
                tm " ...Lemme let you in on a secret here. "
                tm " I actually made this butterfly. "
                tm " This butterfly is a clone of another butterfly that's from the wild... "
                tm " Don't worry - I didn't do anything dangerous to that specific butterfly. "
                tm " I just used to clone it, alright? "
                tm " This butterfly over here has special things to it - "
                tm " I made it so that this one is more able to survive during experiments... "
                tm " And I also made it to have special cool powers in case if it's actually in danger ouside of experiments. "
                tm " Pretty neaaat, right? "
                tm " Now, watch this cool thing I can do... "
                " She pours some sparkling water onto it...well, what looks like sparkling water. "
                " You waited for something to happen, but nothing did. "
                tm " Just give it a few moments now. "
                tm " You've gotta be patient for these things, after all! "
                " You waited...and it happened. The butterfly started to tweak out for a bit... "
                " Before it basically caused a disco effect around the room. "
                " It's basically how your normal disco would look around the room, but instead it's butterflies. "
                tm " Cool, right? "
                menu:
                    " VERY COOL ":
                        $ temerolv += 10
                        hide temeroneutral at bottom
                        show temerohappy at center
                        tm " Riiight? "
                        tm " You can come over to me whenever I'm doing some cool experiments! "
                        tm " Though, uh... "
                        tm " Just make sure that I'm actually doing some experiments. "
                        tm " I don't want you to walk in whenever I'm having a call, you know. "
                        tm " That would be awkward for both me and the person I'm on the phone with, haha! "
                        scene black with dissolve
                        " You spent the rest of the break hanging out with Temero. "
                        " Just giving her some ideas for some new experiments... "
                        " Like making the butterflies wings way bigger. "
                        " You wonder if she's going to do this onto humans like you, too. "
                        " Probably not, but there's always a chance. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the gym and went to your classroom for gardening class. "
                        pause 2.0
                        jump tgardeningclass1
                    " it's alright ":
                        tm " Riiight? "
                        tm " You can come over to me whenever I'm doing some cool experiments! "
                        tm " Though, uh... "
                        tm " Just make sure that I'm actually doing some experiments. "
                        tm " I don't want you to walk in whenever I'm having a call, you know. "
                        tm " That would be awkward for both me and the person I'm on the phone with, haha! "
                        scene black with dissolve
                        " You spent the rest of the break hanging out with Temero. "
                        " Just giving her some ideas for some new experiments... "
                        " Like making the butterflies wings way bigger. "
                        " You wonder if she's going to do this onto humans like you, too. "
                        " Probably not, but there's always a chance. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the gym and went to your classroom for gardening class. "
                        pause 2.0
                        jump tgardeningclass1
    label octhurscafeteria3:
        # disk and orchid
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked into the cafeteria and found two of your classmates talking with eachother. "
        " Wondering what they're talking about, you walked over to them. "
        show diskneutral at right with easeinleft
        show orchidneutral at left with easeinleft
        if diskknow == True and orchidknow == True:
            oc " Hey there, [name]!! "
            d " Heyyyy!! "
            oc " I was just talking to Disk over here!! "
            d " Yeah, yeah!! "
            d " I'm actually kind of surprised that you're talking to people more, Orchid! "
            d " I'm really proud of you! "
            hide orchidneutral at bottom
            show orchidhappy at left
            d " Have you been listening to Koa's advice? "
            oc " Heheh - yeah! "
            oc " I actually thought they weren't going to help in the past... "
            oc " Like it was just meaningless words, you know? "
            oc " Believed I wasn't going to change, believed I was going to stay the same... "
            oc " But take a good look at what happened! "
            oc " I'm feeling more lively than ever! "
            oc " I'm smiling more, laughing more... "
            d " I'm really happy that you're feeling way better now!! "
            d " I knew you just need a little motivating... "
            d " What made you listen to Koa's advice, anyway? "
            hide orchidhappy at bottom
            show orchidneutral at left
            oc " Well... "
            oc " Let's just say I was having a tough time. "
            oc " Koa gave me some more advice, and... "
            oc " Instead of ignoring it like I always do, "
            oc " I decided to listen to what he had to say. "
            oc " I'm starting to eat more than I usually do... "
            oc " And I started to appreciate the little things in life more! "
            oc " I'm even starting to feel proud of myself, hehe... "
            d " That's great to hear, Orchid! "
            d " Hey...you free to hang out anytime? "
            d " Only if you want to, of course! "
            d " No forcing at all. "
            oc " Mmmm...I'll see if I have enough social energy for that on that day then. "
            oc " Don't want to tire myself out, you know? "
            d " Aaah, I totally get that, don't worry! "
            d " And hey - maybe we could even invite [name] over, too? "
            d " Only if [they] [are] up to it! "
            d " Don't wanna force [them] too!! "
            oc " Oh, of course! "
            oc " [name] - would you like to join us some time? "
            menu:
                " yeah sure ":
                    $ orchidlv += 5
                    $ disklv += 5
                    hide diskneutral at bottom
                    show diskhappy at right
                    d " That's awesome to hear! "
                    d " Though, it would have to be somewhere NOT on friday... "
                    d " Cause...you know...my party. "
                    oc " Of course, of course! "
                    oc " Maybe this sunday if you're available? "
                    d " Yeah, sure!! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Orchid. "
                    " Just talking about the things you were going to do on the hangout on sunday. "
                    " Too bad there isn't a sunday in this game. "
                    play sound "audio/bellring.mp3"
                    " Looks like the bell rang. Time for another class. "
                    " You walked out of the cafeteria eventually, and went to your classroom. "
                    pause 2.0
                    jump tgardeningclass1
                " i'm busy, sorry ":
                    d " Ooouu...alright! "
                    oc " We understand, don't worry! "
                    d " Anyway, Orchid... "
                    d " It would have to be somewhere NOT on friday... "
                    d " Cause...you know...my party. "
                    oc " Of course, of course! "
                    oc " Maybe this sunday if you're available? "
                    d " Yeah, sure!! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Orchid. "
                    " Just talking about the things they were going to do on the hangout on sunday. "
                    " Too bad there isn't a sunday in this game. "
                    play sound "audio/bellring.mp3"
                    " Looks like the bell rang. Time for another class. "
                    " You walked out of the cafeteria eventually, and went to your classroom. "
                    pause 2.0
                    jump tgardeningclass1
        elif diskknow == True and orchidknow == False:
            x " Hey there, [name]!! "
            d " Heyyyy!! "
            x " I was just talking to Disk over here!! "
            d " Yeah, yeah!! "
            $ orchidknow = True
            d " I'm actually kind of surprised that you're talking to people more, Orchid! "
            d " I'm really proud of you! "
            hide orchidneutral at bottom
            show orchidhappy at left
            d " Have you been listening to Koa's advice? "
            oc " Heheh - yeah! "
            oc " I actually thought they weren't going to help in the past... "
            oc " Like it was just meaningless words, you know? "
            oc " Believed I wasn't going to change, believed I was going to stay the same... "
            oc " But take a good look at what happened! "
            oc " I'm feeling more lively than ever! "
            oc " I'm smiling more, laughing more... "
            d " I'm really happy that you're feeling way better now!! "
            d " I knew you just need a little motivating... "
            d " What made you listen to Koa's advice, anyway? "
            hide orchidhappy at bottom
            show orchidneutral at left
            oc " Well... "
            oc " Let's just say I was having a tough time. "
            oc " Koa gave me some more advice, and... "
            oc " Instead of ignoring it like I always do, "
            oc " I decided to listen to what he had to say. "
            oc " I'm starting to eat more than I usually do... "
            oc " And I started to appreciate the little things in life more! "
            oc " I'm even starting to feel proud of myself, hehe... "
            d " That's great to hear, Orchid! "
            d " Hey...you free to hang out anytime? "
            d " Only if you want to, of course! "
            d " No forcing at all. "
            oc " Mmmm...I'll see if I have enough social energy for that on that day then. "
            oc " Don't want to tire myself out, you know? "
            d " Aaah, I totally get that, don't worry! "
            d " And hey - maybe we could even invite [name] over, too? "
            d " Only if [they] [are] up to it! "
            d " Don't wanna force [them] too!! "
            oc " Oh, of course! "
            oc " [name] - would you like to join us some time? "
            menu:
                " yeah sure ":
                    $ orchidlv += 5
                    $ disklv += 5
                    hide diskneutral at bottom
                    show diskhappy at right
                    d " That's awesome to hear! "
                    d " Though, it would have to be somewhere NOT on friday... "
                    d " Cause...you know...my party. "
                    oc " Of course, of course! "
                    oc " Maybe this sunday if you're available? "
                    d " Yeah, sure!! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Orchid. "
                    " Just talking about the things you were going to do on the hangout on sunday. "
                    " Too bad there isn't a sunday in this game. "
                    play sound "audio/bellring.mp3"
                    " Looks like the bell rang. Time for another class. "
                    " You walked out of the cafeteria eventually, and went to your classroom. "
                    pause 2.0
                    jump tgardeningclass1
                " i'm busy, sorry ":
                    d " Ooouu...alright! "
                    oc " We understand, don't worry! "
                    d " Anyway, Orchid... "
                    d " It would have to be somewhere NOT on friday... "
                    d " Cause...you know...my party. "
                    oc " Of course, of course! "
                    oc " Maybe this sunday if you're available? "
                    d " Yeah, sure!! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Orchid. "
                    " Just talking about the things they were going to do on the hangout on sunday. "
                    " Too bad there isn't a sunday in this game. "
                    play sound "audio/bellring.mp3"
                    " Looks like the bell rang. Time for another class. "
                    " You walked out of the cafeteria eventually, and went to your classroom. "
                    pause 2.0
                    jump tgardeningclass1
        elif diskknow == False and orchidknow == True:
            oc " Hey there, [name]!! "
            x " Heyyyy!! "
            $ diskknow = True
            oc " I was just talking to Disk over here!! "
            d " Yeah, yeah!! "
            d " I'm actually kind of surprised that you're talking to people more, Orchid! "
            d " I'm really proud of you! "
            hide orchidneutral at bottom
            show orchidhappy at left
            d " Have you been listening to Koa's advice? "
            oc " Heheh - yeah! "
            oc " I actually thought they weren't going to help in the past... "
            oc " Like it was just meaningless words, you know? "
            oc " Believed I wasn't going to change, believed I was going to stay the same... "
            oc " But take a good look at what happened! "
            oc " I'm feeling more lively than ever! "
            oc " I'm smiling more, laughing more... "
            d " I'm really happy that you're feeling way better now!! "
            d " I knew you just need a little motivating... "
            d " What made you listen to Koa's advice, anyway? "
            hide orchidhappy at bottom
            show orchidneutral at left
            oc " Well... "
            oc " Let's just say I was having a tough time. "
            oc " Koa gave me some more advice, and... "
            oc " Instead of ignoring it like I always do, "
            oc " I decided to listen to what he had to say. "
            oc " I'm starting to eat more than I usually do... "
            oc " And I started to appreciate the little things in life more! "
            oc " I'm even starting to feel proud of myself, hehe... "
            d " That's great to hear, Orchid! "
            d " Hey...you free to hang out anytime? "
            d " Only if you want to, of course! "
            d " No forcing at all. "
            oc " Mmmm...I'll see if I have enough social energy for that on that day then. "
            oc " Don't want to tire myself out, you know? "
            d " Aaah, I totally get that, don't worry! "
            d " And hey - maybe we could even invite [name] over, too? "
            d " Only if [they] [are] up to it! "
            d " Don't wanna force [them] too!! "
            oc " Oh, of course! "
            oc " [name] - would you like to join us some time? "
            menu:
                " yeah sure ":
                    $ orchidlv += 5
                    $ disklv += 5
                    hide diskneutral at bottom
                    show diskhappy at right
                    d " That's awesome to hear! "
                    d " Though, it would have to be somewhere NOT on friday... "
                    d " Cause...you know...my party. "
                    oc " Of course, of course! "
                    oc " Maybe this sunday if you're available? "
                    d " Yeah, sure!! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Orchid. "
                    " Just talking about the things you were going to do on the hangout on sunday. "
                    " Too bad there isn't a sunday in this game. "
                    play sound "audio/bellring.mp3"
                    " Looks like the bell rang. Time for another class. "
                    " You walked out of the cafeteria eventually, and went to your classroom. "
                    pause 2.0
                    jump tgardeningclass1
                " i'm busy, sorry ":
                    d " Ooouu...alright! "
                    oc " We understand, don't worry! "
                    d " Anyway, Orchid... "
                    d " It would have to be somewhere NOT on friday... "
                    d " Cause...you know...my party. "
                    oc " Of course, of course! "
                    oc " Maybe this sunday if you're available? "
                    d " Yeah, sure!! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Orchid. "
                    " Just talking about the things they were going to do on the hangout on sunday. "
                    " Too bad there isn't a sunday in this game. "
                    play sound "audio/bellring.mp3"
                    " Looks like the bell rang. Time for another class. "
                    " You walked out of the cafeteria eventually, and went to your classroom. "
                    pause 2.0
                    jump tgardeningclass1
        else:
            x " Hey there, [name]!! "
            x " Heyyyy!! "
            $ diskknow = True
            x " I was just talking to Disk over here!! "
            d " Yeah, yeah!! "
            $ orchidknow = True
            d " I'm actually kind of surprised that you're talking to people more, Orchid! "
            d " I'm really proud of you! "
            hide orchidneutral at bottom
            show orchidhappy at left
            d " Have you been listening to Koa's advice? "
            oc " Heheh - yeah! "
            oc " I actually thought they weren't going to help in the past... "
            oc " Like it was just meaningless words, you know? "
            oc " Believed I wasn't going to change, believed I was going to stay the same... "
            oc " But take a good look at what happened! "
            oc " I'm feeling more lively than ever! "
            oc " I'm smiling more, laughing more... "
            d " I'm really happy that you're feeling way better now!! "
            d " I knew you just need a little motivating... "
            d " What made you listen to Koa's advice, anyway? "
            hide orchidhappy at bottom
            show orchidneutral at left
            oc " Well... "
            oc " Let's just say I was having a tough time. "
            oc " Koa gave me some more advice, and... "
            oc " Instead of ignoring it like I always do, "
            oc " I decided to listen to what he had to say. "
            oc " I'm starting to eat more than I usually do... "
            oc " And I started to appreciate the little things in life more! "
            oc " I'm even starting to feel proud of myself, hehe... "
            d " That's great to hear, Orchid! "
            d " Hey...you free to hang out anytime? "
            d " Only if you want to, of course! "
            d " No forcing at all. "
            oc " Mmmm...I'll see if I have enough social energy for that on that day then. "
            oc " Don't want to tire myself out, you know? "
            d " Aaah, I totally get that, don't worry! "
            d " And hey - maybe we could even invite [name] over, too? "
            d " Only if [they] [are] up to it! "
            d " Don't wanna force [them] too!! "
            oc " Oh, of course! "
            oc " [name] - would you like to join us some time? "
            menu:
                " yeah sure ":
                    $ orchidlv += 5
                    $ disklv += 5
                    hide diskneutral at bottom
                    show diskhappy at right
                    d " That's awesome to hear! "
                    d " Though, it would have to be somewhere NOT on friday... "
                    d " Cause...you know...my party. "
                    oc " Of course, of course! "
                    oc " Maybe this sunday if you're available? "
                    d " Yeah, sure!! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Orchid. "
                    " Just talking about the things you were going to do on the hangout on sunday. "
                    " Too bad there isn't a sunday in this game. "
                    play sound "audio/bellring.mp3"
                    " Looks like the bell rang. Time for another class. "
                    " You walked out of the cafeteria eventually, and went to your classroom. "
                    pause 2.0
                    jump tgardeningclass1
                " i'm busy, sorry ":
                    d " Ooouu...alright! "
                    oc " We understand, don't worry! "
                    d " Anyway, Orchid... "
                    d " It would have to be somewhere NOT on friday... "
                    d " Cause...you know...my party. "
                    oc " Of course, of course! "
                    oc " Maybe this sunday if you're available? "
                    d " Yeah, sure!! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Disk and Orchid. "
                    " Just talking about the things they were going to do on the hangout on sunday. "
                    " Too bad there isn't a sunday in this game. "
                    play sound "audio/bellring.mp3"
                    " Looks like the bell rang. Time for another class. "
                    " You walked out of the cafeteria eventually, and went to your classroom. "
                    pause 2.0
                    jump tgardeningclass1
    label octhursrooftop3:
        # quinn jacob
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked to the rooftop and found two of your classmates doing their own things. "
        " You wanted to talk to them...but who do you talk to? "
        if quinnknow == True and jacobknow == True:
            menu:
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump rottingbrain
                " {image=jacobicon} Jacob {image=jacobicon} ":
                    jump cloudforrotting
        elif quinnknow == True and jacobknow == False:
            menu:
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump rottingbrain
                " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                    jump cloudforrotting
        elif quinnknow == False and jacobknow == True:
            menu:
                " {image=quinnicon} An acting guy {image=quinnicon} ":
                    jump rottingbrain
                " {image=jacobicon} Jacob {image=jacobicon} ":
                    jump cloudforrotting
        else:
            menu:
                " {image=quinnicon} An acting guy {image=quinnicon} ":
                    jump rottingbrain
                " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                    jump cloudforrotting
        label rottingbrain:
            show quinnneutral at center with easeinleft
            if quinnknow == True:
                q " Hm...does this line sound right to me? "
                q " No, no...I should probably change that. "
                q " Lemme just rewrite that... "
                q " Things have to be perfect for this, after all... "
                " You asked him politely on what he was doing. "
                q " Oh!! hey there, [name]!! "
                q " Nice to see you up here. "
                q " I don't know if I've ever mentioned it to you before, buuut... "
                q " I'm having this play, right? "
                q " And I decided to add this one extra scene to it... "
                q " It's just for me, though! "
                q " Just so that my club members won't have to worry about anything new. "
                q " This also gives them more time to get ready for the next scene! "
                q " Pretty neat, right? "
                q " And I don't really have a problem with making a new scene for myself... "
                q " I can pretty much memorize anything I want with perfect memory. "
                q " Sooo...I'm fine with all of this! "
                q " The only thing I'm worrying about right now is what I should say. "
                q " Like - I don't know how to make it poetic-sounding! "
                q " And I don't want to use AI for that stuff. "
                q " Using AI would just be really weird, in all honesty. "
                q " It needs to sound genuine! "
                q " Do you have any ideas, [name]? "
                q " Any kind of idea will do.... "
                q " ...I'll just have to make it work, somehow. "
                menu:
                    " *insert great idea here lmao* ":
                        $ quinnlv += 10
                        " You gave Quinn an amazing idea that you had... "
                        " It was so great, that I couldn't say what it was. "
                        " You're just that great, gang. "
                        hide quinnneutral at bottom
                        show quinnhappy at center
                        q " Woah, [name]...! "
                        q " That's really good, actually! "
                        q " Say that again? I need to copy that down... "
                        q " Just to make sure I can REALLY get that into my head! "
                        " You repeat your words to Quinn so that he could type it into his phone. "
                        " Seemed like he was really happy with the idea you gave him. "
                        " I told you gang, you were just so good. "
                        q " Hehe, thanks [name]! "
                        q " I'll make sure to credit you as a special mention, hehe... "
                        q " This helped a lot - since the play is tomorrow. "
                        q " Hope you can see it tomorrow, [name]! "
                        hide quinnhappy at bottom
                        show quinnneutral at center
                        q " Anyway - while you're here, we can talk about something else, if you'd like. "
                        q " I don't want you to be standing there all day, after all. "
                        q " Your legs would be crying if that happened. "
                        q " Hah - just kidding, but it sure would feel like it. "
                        q " Anyway, what should we talk about? "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Talking about random things like... "
                        " Which songs you guys like, for example. "
                        " You both have very different tastes. "
                        " It's kinda obvious, but this guy is really into musicals. "
                        " Like he has a lot of songs from musicals in his playlist. "
                        " Kind of expected, but still holy moly he's got all the bangers in there. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked down from the rooftop and went to your classroom. "
                        pause 2.0
                        jump tgardeningclass1
                    " sorry man i dont got any ":
                        hide quinnneutral at bottom
                        show quinnsad at center
                        q " Oh...well that's fine then. "
                        q " I can come up with something later, I'm sure of it. "
                        q " Thanks anyway, [name]. "
                        hide quinnsad at bottom
                        show quinnneutral at center
                        q " While you're here though, we can talk about something else, if you'd like. "
                        q " I don't want you to be standing there all day, after all. "
                        q " Your legs would be crying if that happened. "
                        q " Hah - just kidding, but it sure would feel like it. "
                        q " Anyway, what should we talk about? "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Talking about random things like... "
                        " Which songs you guys like, for example. "
                        " You both have very different tastes. "
                        " It's kinda obvious, but this guy is really into musicals. "
                        " Like he has a lot of songs from musicals in his playlist. "
                        " Kind of expected, but still holy moly he's got all the bangers in there. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked down from the rooftop and went to your classroom. "
                        pause 2.0
                        jump tgardeningclass1
            else:
                x " Hm...does this line sound right to me? "
                x " No, no...I should probably change that. "
                x " Lemme just rewrite that... "
                x " Things have to be perfect for this, after all... "
                " You asked him politely on what he was doing. "
                x " Oh!! hey there, [name]!! "
                x " Nice to see you up here. "
                $ quinnknow = True
                q " Oh - uh...Quinn, by the way. Part of the drama club and your classmate. "
                q " I don't know if I've ever mentioned it to you before, buuut... "
                q " I'm having this play, right? "
                q " And I decided to add this one extra scene to it... "
                q " It's just for me, though! "
                q " Just so that my club members won't have to worry about anything new. "
                q " This also gives them more time to get ready for the next scene! "
                q " Pretty neat, right? "
                q " And I don't really have a problem with making a new scene for myself... "
                q " I can pretty much memorize anything I want with perfect memory. "
                q " Sooo...I'm fine with all of this! "
                q " The only thing I'm worrying about right now is what I should say. "
                q " Like - I don't know how to make it poetic-sounding! "
                q " And I don't want to use AI for that stuff. "
                q " Using AI would just be really weird, in all honesty. "
                q " It needs to sound genuine! "
                q " Do you have any ideas, [name]? "
                q " Any kind of idea will do.... "
                q " ...I'll just have to make it work, somehow. "
                menu:
                    " *insert great idea here lmao* ":
                        $ quinnlv += 10
                        " You gave Quinn an amazing idea that you had... "
                        " It was so great, that I couldn't say what it was. "
                        " You're just that great, gang. "
                        hide quinnneutral at bottom
                        show quinnhappy at center
                        q " Woah, [name]...! "
                        q " That's really good, actually! "
                        q " Say that again? I need to copy that down... "
                        q " Just to make sure I can REALLY get that into my head! "
                        " You repeat your words to Quinn so that he could type it into his phone. "
                        " Seemed like he was really happy with the idea you gave him. "
                        " I told you gang, you were just so good. "
                        q " Hehe, thanks [name]! "
                        q " I'll make sure to credit you as a special mention, hehe... "
                        q " This helped a lot - since the play is tomorrow. "
                        q " Hope you can see it tomorrow, [name]! "
                        hide quinnhappy at bottom
                        show quinnneutral at center
                        q " Anyway - while you're here, we can talk about something else, if you'd like. "
                        q " I don't want you to be standing there all day, after all. "
                        q " Your legs would be crying if that happened. "
                        q " Hah - just kidding, but it sure would feel like it. "
                        q " Anyway, what should we talk about? "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Talking about random things like... "
                        " Which songs you guys like, for example. "
                        " You both have very different tastes. "
                        " It's kinda obvious, but this guy is really into musicals. "
                        " Like he has a lot of songs from musicals in his playlist. "
                        " Kind of expected, but still holy moly he's got all the bangers in there. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked down from the rooftop and went to your classroom. "
                        pause 2.0
                        jump tgardeningclass1
                    " sorry man i dont got any ":
                        hide quinnneutral at bottom
                        show quinnsad at center
                        q " Oh...well that's fine then. "
                        q " I can come up with something later, I'm sure of it. "
                        q " Thanks anyway, [name]. "
                        hide quinnsad at bottom
                        show quinnneutral at center
                        q " While you're here though, we can talk about something else, if you'd like. "
                        q " I don't want you to be standing there all day, after all. "
                        q " Your legs would be crying if that happened. "
                        q " Hah - just kidding, but it sure would feel like it. "
                        q " Anyway, what should we talk about? "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Talking about random things like... "
                        " Which songs you guys like, for example. "
                        " You both have very different tastes. "
                        " It's kinda obvious, but this guy is really into musicals. "
                        " Like he has a lot of songs from musicals in his playlist. "
                        " Kind of expected, but still holy moly he's got all the bangers in there. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked down from the rooftop and went to your classroom. "
                        pause 2.0
                        jump tgardeningclass1
        label cloudforrotting:
            show jacobneutral at center with easeinright
            if jacobknow == True:
                " You walked over to him and asked him what he was doing. "
                jac " Huh? oh, didn't notice you were coming up to me. "
                jac " Sorry, sorry...was just looking at the clouds and all that. "
                jac " Needed some time to cool myself off. "
                jac " The people in this school can be a little too much... "
                jac " I like to come up here sometimes... "
                jac " Or I just come over to the back of the school to cool off. "
                jac " The noise can be real annoying after a bit of being here. "
                jac " Like, I'm talking a BIT. "
                jac " Or that's probably just me... "
                jac " The first day I got here, I was pretty fine... "
                jac " But then all the energy kinda got to me and I kinda grew out of it quick. "
                jac " I didn't want to do a crash out infront of everyone, so... "
                jac " I usually come up here or the back of the school to calm myself. "
                jac " It works, sometimes. "
                jac " Saying sometimes because there can be some loud people up here and down there too. "
                jac " Really disturbs my peace - "
                jac " But that's kinda what a school is supposed to be.. "
                jac " Loud, annoying, and sometimes fun. "
                jac " The fun part is only if you ever got a lot of friends. "
                jac " I don't have much friends, actually... "
                jac " Most people think I'm too scary to talk to. "
                jac " Like I'm a bad guy or something... "
                jac " Do I really look that bad? be honest with me. "
                menu:
                    " Yeah dude ":
                        $ jacoblv += 10
                        jac " You're actually being honest... "
                        jac " I appreciate that. "
                        jac " I like people who are honest. "
                        jac " Thanks for telling me the truth. "
                        jac " I don't actually mind people avoiding me... "
                        jac " If they're going to avoid me, then I'm fine with it. "
                        jac " I kind of like being alone anyway. "
                        jac " At least they're not bothering me with their stupid questions... "
                        jac " If they're not bothering me with a simple question, then I'm fine. "
                        jac " Hmhmmm... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Jacob. "
                        " Just chilling there on the rooftop... "
                        " You and him didn't really talk much, you kinda just stayed silent... "
                        " To, you know...give him that peace that he wants. "
                        " You wanted to be a good classmate and respect his stuff. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked down the rooftop and went to your classroom after a bit. "
                        pause 2.0
                        jump tgardeningclass1
                    " Nah dude ":
                        $ jacoblv += 5
                        jac " Either you're lying or you actually mean that. "
                        jac " But, uh... "
                        jac " Thanks for sharing your opinion, anyway. "
                        jac " I don't actually mind people avoiding me... "
                        jac " If they're going to avoid me, then I'm fine with it. "
                        jac " I kind of like being alone anyway. "
                        jac " At least they're not bothering me with their stupid questions... "
                        jac " If they're not bothering me with a simple question, then I'm fine. "
                        jac " Hmhmmm... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Jacob. "
                        " Just chilling there on the rooftop... "
                        " You and him didn't really talk much, you kinda just stayed silent... "
                        " To, you know...give him that peace that he wants. "
                        " You wanted to be a good classmate and respect his stuff. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked down the rooftop and went to your classroom after a bit. "
                        pause 2.0
                        jump tgardeningclass1
            else:
                " You walked over to him and asked him what he was doing. "
                x " Huh? oh, didn't notice you were coming up to me. "
                x " Sorry, sorry...was just looking at the clouds and all that. "
                $ jacobknow = True
                jac " I'm Jacob - by the way. And I just, uh... "
                jac " ...Needed some time to cool myself off. "
                jac " The people in this school can be a little too much... "
                jac " I like to come up here sometimes... "
                jac " Or I just come over to the back of the school to cool off. "
                jac " The noise can be real annoying after a bit of being here. "
                jac " Like, I'm talking a BIT. "
                jac " Or that's probably just me... "
                jac " The first day I got here, I was pretty fine... "
                jac " But then all the energy kinda got to me and I kinda grew out of it quick. "
                jac " I didn't want to do a crash out infront of everyone, so... "
                jac " I usually come up here or the back of the school to calm myself. "
                jac " It works, sometimes. "
                jac " Saying sometimes because there can be some loud people up here and down there too. "
                jac " Really disturbs my peace - "
                jac " But that's kinda what a school is supposed to be.. "
                jac " Loud, annoying, and sometimes fun. "
                jac " The fun part is only if you ever got a lot of friends. "
                jac " I don't have much friends, actually... "
                jac " Most people think I'm too scary to talk to. "
                jac " Like I'm a bad guy or something... "
                jac " Do I really look that bad? be honest with me. "
                menu:
                    " Yeah dude ":
                        $ jacoblv += 10
                        jac " You're actually being honest... "
                        jac " I appreciate that. "
                        jac " I like people who are honest. "
                        jac " Thanks for telling me the truth. "
                        jac " I don't actually mind people avoiding me... "
                        jac " If they're going to avoid me, then I'm fine with it. "
                        jac " I kind of like being alone anyway. "
                        jac " At least they're not bothering me with their stupid questions... "
                        jac " If they're not bothering me with a simple question, then I'm fine. "
                        jac " Hmhmmm... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Jacob. "
                        " Just chilling there on the rooftop... "
                        " You and him didn't really talk much, you kinda just stayed silent... "
                        " To, you know...give him that peace that he wants. "
                        " You wanted to be a good classmate and respect his stuff. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked down the rooftop and went to your classroom after a bit. "
                        pause 2.0
                        jump tgardeningclass1
                    " Nah dude ":
                        $ jacoblv += 5
                        jac " Either you're lying or you actually mean that. "
                        jac " But, uh... "
                        jac " Thanks for sharing your opinion, anyway. "
                        jac " I don't actually mind people avoiding me... "
                        jac " If they're going to avoid me, then I'm fine with it. "
                        jac " I kind of like being alone anyway. "
                        jac " At least they're not bothering me with their stupid questions... "
                        jac " If they're not bothering me with a simple question, then I'm fine. "
                        jac " Hmhmmm... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Jacob. "
                        " Just chilling there on the rooftop... "
                        " You and him didn't really talk much, you kinda just stayed silent... "
                        " To, you know...give him that peace that he wants. "
                        " You wanted to be a good classmate and respect his stuff. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked down the rooftop and went to your classroom after a bit. "
                        pause 2.0
                        jump tgardeningclass1
    label octhurslibrary3:
        # spark carmen
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked to the library and spotted two of your classmates talking with eachother, "
        " Wondering what they're talking about, you decided to join their conversation. "
        show sparkneutral at left with easeinright
        show carmenneutral at right with easeinright
        if sparkknow == True and carmenknow == True:
            " You walked over to them and asked what they were doing. "
            sp " Oh hey, [name]. "
            ca " ... "
            " The other guy waves at you. "
            sp " Just lending Carmen my notes. "
            sp " Some notes in gardening, to be specific. "
            sp " He had to skip gardening class one day because one of his family members had a problem.. "
            sp " So he kind of needed notes to get his, you know, notebook complete. "
            sp " Would be kinda bad if you missed something. "
            sp " To get a good grade, you also had to have good notes. "
            sp " Which means your notebook needs to have full notes... "
            sp " Orrr you can just miss one note taking and it would be fine. "
            sp " Only one though. No other chances than that. "
            sp " After the teachers check your notebooks if you've got enough notes... "
            sp " They give you extra points and all of that. "
            sp " That's why we've got to take all the notes we can. "
            sp " Otherwise we would be failing pretty badly. "
            ca " ...(nod of agreement) "
            sp " Yeah, look - even Carmen agrees on that. "
            sp " Yknow, earlier he was crying about not wanting to fail... "
            " Carmen pulls down Spark's tail. "
            " Looks like he wasn't supposed to say that... "
            hide sparkneutral at bottom
            show sparkshit at left
            sp " OW - okay, geez! " with vpunch
            sp " Sorry, sorry! "
            sp " I just meant that to mess with you, come on!! "
            ca " ... "
            hide sparkshit at bottom
            show sparkneutral at center
            sp " ...Ahem...anyway, "
            sp " You wanna take a good look at my notes too, [name]? "
            sp " It could help you out. To, you know.. "
            sp " Remember things? "
            " You nodded in approval. You wanted to take a good look at those notes. "
            " Otherwise the teachers would beat your ass. "
            sp " Alright, come here. Closer, to my side. "
            scene black with dissolve
            " You spent the rest of the break looking at Spark's notes. "
            " Carmen looked like he had a very strong urge to pull Spark's tail again... "
            " But he knew that it would be pretty painful if he did it again, so he decided not to. "
            " Huh...now you wonder what it would feel like if you did what Carmen did. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You got out of the library, and then went to your classroom. "
            pause 2.0
            jump tgardeningclass1
        elif sparkknow == True and carmenknow == False:
            " You walked over to them and asked what they were doing. "
            sp " Oh hey, [name]. "
            x " ... "
            " The other guy waves at you. "
            $ carmenknow = True
            sp " Just lending Carmen my notes. "
            sp " Some notes in gardening, to be specific. "
            sp " He had to skip gardening class one day because one of his family members had a problem.. "
            sp " So he kind of needed notes to get his, you know, notebook complete. "
            sp " Would be kinda bad if you missed something. "
            sp " To get a good grade, you also had to have good notes. "
            sp " Which means your notebook needs to have full notes... "
            sp " Orrr you can just miss one note taking and it would be fine. "
            sp " Only one though. No other chances than that. "
            sp " After the teachers check your notebooks if you've got enough notes... "
            sp " They give you extra points and all of that. "
            sp " That's why we've got to take all the notes we can. "
            sp " Otherwise we would be failing pretty badly. "
            ca " ...(nod of agreement) "
            sp " Yeah, look - even Carmen agrees on that. "
            sp " Yknow, earlier he was crying about not wanting to fail... "
            " Carmen pulls down Spark's tail. "
            " Looks like he wasn't supposed to say that... "
            hide sparkneutral at bottom
            show sparkshit at left
            sp " OW - okay, geez! " with vpunch
            sp " Sorry, sorry! "
            sp " I just meant that to mess with you, come on!! "
            ca " ... "
            hide sparkshit at bottom
            show sparkneutral at center
            sp " ...Ahem...anyway, "
            sp " You wanna take a good look at my notes too, [name]? "
            sp " It could help you out. To, you know.. "
            sp " Remember things? "
            " You nodded in approval. You wanted to take a good look at those notes. "
            " Otherwise the teachers would beat your ass. "
            sp " Alright, come here. Closer, to my side. "
            scene black with dissolve
            " You spent the rest of the break looking at Spark's notes. "
            " Carmen looked like he had a very strong urge to pull Spark's tail again... "
            " But he knew that it would be pretty painful if he did it again, so he decided not to. "
            " Huh...now you wonder what it would feel like if you did what Carmen did. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You got out of the library, and then went to your classroom. "
            pause 2.0
            jump tgardeningclass1
        elif sparkknow == False and carmenknow == True:
            " You walked over to them and asked what they were doing. "
            x " Oh hey, [name]. "
            ca " ... "
            " The other guy waves at you. "
            $ sparkknow = True
            sp " Uh - I'm Spark, by the way. And uh...I was just... "
            sp " Just lending Carmen my notes. "
            sp " Some notes in gardening, to be specific. "
            sp " He had to skip gardening class one day because one of his family members had a problem.. "
            sp " So he kind of needed notes to get his, you know, notebook complete. "
            sp " Would be kinda bad if you missed something. "
            sp " To get a good grade, you also had to have good notes. "
            sp " Which means your notebook needs to have full notes... "
            sp " Orrr you can just miss one note taking and it would be fine. "
            sp " Only one though. No other chances than that. "
            sp " After the teachers check your notebooks if you've got enough notes... "
            sp " They give you extra points and all of that. "
            sp " That's why we've got to take all the notes we can. "
            sp " Otherwise we would be failing pretty badly. "
            ca " ...(nod of agreement) "
            sp " Yeah, look - even Carmen agrees on that. "
            sp " Yknow, earlier he was crying about not wanting to fail... "
            " Carmen pulls down Spark's tail. "
            " Looks like he wasn't supposed to say that... "
            hide sparkneutral at bottom
            show sparkshit at left
            sp " OW - okay, geez! " with vpunch
            sp " Sorry, sorry! "
            sp " I just meant that to mess with you, come on!! "
            ca " ... "
            hide sparkshit at bottom
            show sparkneutral at center
            sp " ...Ahem...anyway, "
            sp " You wanna take a good look at my notes too, [name]? "
            sp " It could help you out. To, you know.. "
            sp " Remember things? "
            " You nodded in approval. You wanted to take a good look at those notes. "
            " Otherwise the teachers would beat your ass. "
            sp " Alright, come here. Closer, to my side. "
            scene black with dissolve
            " You spent the rest of the break looking at Spark's notes. "
            " Carmen looked like he had a very strong urge to pull Spark's tail again... "
            " But he knew that it would be pretty painful if he did it again, so he decided not to. "
            " Huh...now you wonder what it would feel like if you did what Carmen did. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You got out of the library, and then went to your classroom. "
            pause 2.0
            jump tgardeningclass1
        else:
            " You walked over to them and asked what they were doing. "
            x " Oh hey, [name]. "
            x " ... "
            " The other guy waves at you. "
            $ sparkknow = True
            sp " Uh - I'm Spark, by the way. And uh...I was just... "
            $ carmenknow = True
            sp " Just lending Carmen my notes. "
            sp " Some notes in gardening, to be specific. "
            sp " He had to skip gardening class one day because one of his family members had a problem.. "
            sp " So he kind of needed notes to get his, you know, notebook complete. "
            sp " Would be kinda bad if you missed something. "
            sp " To get a good grade, you also had to have good notes. "
            sp " Which means your notebook needs to have full notes... "
            sp " Orrr you can just miss one note taking and it would be fine. "
            sp " Only one though. No other chances than that. "
            sp " After the teachers check your notebooks if you've got enough notes... "
            sp " They give you extra points and all of that. "
            sp " That's why we've got to take all the notes we can. "
            sp " Otherwise we would be failing pretty badly. "
            ca " ...(nod of agreement) "
            sp " Yeah, look - even Carmen agrees on that. "
            sp " Yknow, earlier he was crying about not wanting to fail... "
            " Carmen pulls down Spark's tail. "
            " Looks like he wasn't supposed to say that... "
            hide sparkneutral at bottom
            show sparkshit at left
            sp " OW - okay, geez! " with vpunch
            sp " Sorry, sorry! "
            sp " I just meant that to mess with you, come on!! "
            ca " ... "
            hide sparkshit at bottom
            show sparkneutral at center
            sp " ...Ahem...anyway, "
            sp " You wanna take a good look at my notes too, [name]? "
            sp " It could help you out. To, you know.. "
            sp " Remember things? "
            " You nodded in approval. You wanted to take a good look at those notes. "
            " Otherwise the teachers would beat your ass. "
            sp " Alright, come here. Closer, to my side. "
            scene black with dissolve
            " You spent the rest of the break looking at Spark's notes. "
            " Carmen looked like he had a very strong urge to pull Spark's tail again... "
            " But he knew that it would be pretty painful if he did it again, so he decided not to. "
            " Huh...now you wonder what it would feel like if you did what Carmen did. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You got out of the library, and then went to your classroom. "
            pause 2.0
            jump tgardeningclass1
label tgardeningclass1:
    scene black with dissolve
    pause 2.0
    scene gardenroom with dissolve
    " You walked into the classroom and waited patiently for the gardening teacher to arrive. "
    " As you were waiting, you looked at the pretty flowers in the room. "
    " You wanted to touch some of them, but you knew you weren't allowed to. "
    " Huh. Wonder what flowers taste like. "
    " Probably bad realistically, but you still wanna try. "
    " Even though you're probably going to vomit about three times while eating it. "
    " The gardening teacher arrives as you were staring at a flower. "
    " You didn't notice her being there until you heard her speaking. "
    show wisterianeutral at center with easeinleft
    msw " Hello there, class... "
    msw " I'm sure everyone's all excited after Sol's class.. "
    msw " We're going to have to be calm for this class though... "
    msw " I can't have anyone ruining all of the flowers... "
    hide wisterianeutral at bottom
    show wisteriaangry at center
    msw " (That...actually happened to me once before.) "
    msw " (I don't want that to happen again.) "
    msw " (All of these flowers and plants took so long to grow...) "
    msw " (Only for it to be erased just like that.) "
    msw " (People who destroy things for their own entertainment are disgusting.) "
    msw " (Hopefully none of my students turn out like that...) "
    msw " (I don't want to teach someone who's like that anyway.) "
    hide wisteriaangry at bottom
    show wisterianeutral at center
    msw " Anywho...let's get started for our lesson today... "
    msw " This isn't really anything important, so... "
    msw " You can go ahead and just watch and not take notes... "
    scene black with dissolve
    " Since the teacher said that this class wasn't really anything important, "
    " You kind of just zoned out for the entire class. "
    " You were playing ping pong in your mind, alright? "
    play sound "audio/bellring.mp3"
    " The bell rings after a little bit, looks like it's time for a break. "
    " You walked out of the classroom after a good bit. "
    pause 2.0
    jump octhursbreak4
label octhursbreak4:
    scene hallway with dissolve
    " Where would you like to hangout for this break? "
    menu:
        " {image=sparkicon} The front of the school {image=jacobicon} ":
            jump octhursfront4
        " {image=carmenicon} The back of the school {image=temeroicon} ":
            jump octhursback4
        " {image=orchidicon} The gym {image=yinyangicon} ":
            jump octhursgym4
        " {image=quinnicon} The cafeteria {image=jamicon} ":
            jump octhurscafeteria4
        " {image=diskicon} The rooftop {image=noxicon} ":
            jump octhursrooftop4
        " {image=koaicon} The library {image=matteicon} ":
            jump octhurslibrary4
    label octhursfront4:
        # spark and jacob
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked to the front of the school and noticed that two of your classmates were talking with eachother. "
        " Wondering what they're talking about, you decided to walk over to them. "
        show sparkneutral at left with easeinright
        show jacobneutral at right with easeinright
        if sparkknow == True and jacobknow == True:
            sp " Heya [name]. "
            jac " Oh god - [name]'s here?! "
            jac " Great, atleast [they] can help us in finding this thing faster. "
            " You asked them what they were looking for. "
            " Whatever it is, you might've seen it before. "
            jac " You see, uh... "
            jac " Spark over here kind of has this weird computer pet. "
            jac " And it kinda just ran away during class earlier. "
            jac " So we're kind of just walking around and trying to find it. "
            " You asked them what it looked like. "
            sp " It's basically like this tiny screen thing with four sharp legs... "
            sp " And it's also got antennas like mine. "
            sp " It usually doesn't run off from me unless if it's planning something. "
            sp " And I don't want the entire school to blow up because of it. "
            sp " It usually just does something stupid, but it can also do that too. "
            jac " Aaaand that's why we need to find it. "
            jac " I don't wanna go back to looking for another school to go in. "
            sp " Oh yeah, 'cause most schools are shit around here. "
            sp " And also because I don't want to pay for the damages. "
            sp " You wanna help us look for it, or are you busy doing stuff? "
            sp " We don't mind if you don't wanna help though. "
            jac " Yeah, we won't bother you if you're busy. "
            menu:
                " I want to help ":
                    $ sparklv += 5
                    $ jacoblv == 5
                    hide sparkneutral at bottom
                    show sparkhappy at left
                    sp " Awesome. The more, the better. "
                    sp " Now that we have three people looking around, this would be much faster. "
                    jac " Alright, alright... "
                    jac " Let's get to looking now. "
                    jac " Who knows where it could be right now? "
                    hide sparkhappy at bottom
                    show sparkneutral at left
                    sp " Oh, uh...right. "
                    sp " I'll go and check the left side of the school. "
                    jac " I'll go check out the right. "
                    jac " [name] can go whereever [they] want. "
                    " You gave them a thumbs up before you went back into the school and went to looking. "
                    scene black with dissolve
                    " You spent the rest of the break finding stuff with Spark and Jacob. "
                    " You weren't really finding anything, though - ...what the hell. "
                    " How did it get here??? "
                    " Uh. You know what, I'm just going to teleport this thing to you. "
                    " Return it back to Spark. Pretty sure this thing is named Scrap? "
                    " Atleast that's what I remember. "
                    " Just tell them that you found it near the vents. "
                    " Ahem.... "
                    " You eventually found the thing Spark was looking for and gave it to him. "
                    " Told him that you found it trying to get into the vents. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You talked with Spark and Jacob for a bit, before going to your classroom. "
                    pause 2.0
                    jump tphysicsclass1
                " I'm busy this break, sorry guys ":
                    sp " Alrighty. "
                    sp " Still - if you see anything, just give it to me. "
                    jac " We've got no more time to lose, Spark. "
                    jac " Let's start looking around right now. "
                    sp " Okay - see you later, [name]. "
                    hide jacobneutral at right with easeoutright
                    hide sparkneutral at right with easeoutright
                    scene black with dissolve
                    " You spent the rest of the break just wandering around the school. "
                    " Nothing really interesting caught your attention...hey, wait... "
                    " What's that trying to get into the vents? "
                    " You reached up and got it down, and it looked like that thing Spark was looking for. "
                    " You looked around to find Spark and eventually spotted him at the library. "
                    " You gave him the thing you found before you went back to wanderng around the school. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after you wander around for a good bit. "
                    " You continue wandering around for a bit before you went to your classroom. "
                    pause 2.0
                    jump tphysicsclass1
        elif sparkknow == True and jacobknow == False:
            sp " Heya [name]. "
            x " Oh god - [name]'s here?! "
            x " Great, atleast [they] can help us in finding this thing faster. "
            " You asked them what they were looking for. "
            " Whatever it is, you might've seen it before. "
            x " You see, uh... "
            $ jacobknow = True
            jac " Okay, before I say antyhing else - I'm Jacob, and uh... "
            jac " Spark over here kind of has this weird computer pet. "
            jac " And it kinda just ran away during class earlier. "
            jac " So we're kind of just walking around and trying to find it. "
            " You asked them what it looked like. "
            sp " It's basically like this tiny screen thing with four sharp legs... "
            sp " And it's also got antennas like mine. "
            sp " It usually doesn't run off from me unless if it's planning something. "
            sp " And I don't want the entire school to blow up because of it. "
            sp " It usually just does something stupid, but it can also do that too. "
            jac " Aaaand that's why we need to find it. "
            jac " I don't wanna go back to looking for another school to go in. "
            sp " Oh yeah, 'cause most schools are shit around here. "
            sp " And also because I don't want to pay for the damages. "
            sp " You wanna help us look for it, or are you busy doing stuff? "
            sp " We don't mind if you don't wanna help though. "
            jac " Yeah, we won't bother you if you're busy. "
            menu:
                " I want to help ":
                    $ sparklv += 5
                    $ jacoblv == 5
                    hide sparkneutral at bottom
                    show sparkhappy at left
                    sp " Awesome. The more, the better. "
                    sp " Now that we have three people looking around, this would be much faster. "
                    jac " Alright, alright... "
                    jac " Let's get to looking now. "
                    jac " Who knows where it could be right now? "
                    hide sparkhappy at bottom
                    show sparkneutral at left
                    sp " Oh, uh...right. "
                    sp " I'll go and check the left side of the school. "
                    jac " I'll go check out the right. "
                    jac " [name] can go whereever [they] want. "
                    " You gave them a thumbs up before you went back into the school and went to looking. "
                    scene black with dissolve
                    " You spent the rest of the break finding stuff with Spark and Jacob. "
                    " You weren't really finding anything, though - ...what the hell. "
                    " How did it get here??? "
                    " Uh. You know what, I'm just going to teleport this thing to you. "
                    " Return it back to Spark. Pretty sure this thing is named Scrap? "
                    " Atleast that's what I remember. "
                    " Just tell them that you found it near the vents. "
                    " Ahem.... "
                    " You eventually found the thing Spark was looking for and gave it to him. "
                    " Told him that you found it trying to get into the vents. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You talked with Spark and Jacob for a bit, before going to your classroom. "
                    pause 2.0
                    jump tphysicsclass1
                " I'm busy this break, sorry guys ":
                    sp " Alrighty. "
                    sp " Still - if you see anything, just give it to me. "
                    jac " We've got no more time to lose, Spark. "
                    jac " Let's start looking around right now. "
                    sp " Okay - see you later, [name]. "
                    hide jacobneutral at right with easeoutright
                    hide sparkneutral at right with easeoutright
                    scene black with dissolve
                    " You spent the rest of the break just wandering around the school. "
                    " Nothing really interesting caught your attention...hey, wait... "
                    " What's that trying to get into the vents? "
                    " You reached up and got it down, and it looked like that thing Spark was looking for. "
                    " You looked around to find Spark and eventually spotted him at the library. "
                    " You gave him the thing you found before you went back to wanderng around the school. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after you wander around for a good bit. "
                    " You continue wandering around for a bit before you went to your classroom. "
                    pause 2.0
                    jump tphysicsclass1
        elif sparkknow == False and jacobknow == True:
            x " Heya [name]. "
            jac " Oh god - [name]'s here?! "
            jac " Great, atleast [they] can help us in finding this thing faster. "
            " You asked them what they were looking for. "
            " Whatever it is, you might've seen it before. "
            jac " You see, uh... "
            $ sparkknow = True
            jac " Spark over here kind of has this weird computer pet. "
            jac " And it kinda just ran away during class earlier. "
            jac " So we're kind of just walking around and trying to find it. "
            " You asked them what it looked like. "
            sp " It's basically like this tiny screen thing with four sharp legs... "
            sp " And it's also got antennas like mine. "
            sp " It usually doesn't run off from me unless if it's planning something. "
            sp " And I don't want the entire school to blow up because of it. "
            sp " It usually just does something stupid, but it can also do that too. "
            jac " Aaaand that's why we need to find it. "
            jac " I don't wanna go back to looking for another school to go in. "
            sp " Oh yeah, 'cause most schools are shit around here. "
            sp " And also because I don't want to pay for the damages. "
            sp " You wanna help us look for it, or are you busy doing stuff? "
            sp " We don't mind if you don't wanna help though. "
            jac " Yeah, we won't bother you if you're busy. "
            menu:
                " I want to help ":
                    $ sparklv += 5
                    $ jacoblv == 5
                    hide sparkneutral at bottom
                    show sparkhappy at left
                    sp " Awesome. The more, the better. "
                    sp " Now that we have three people looking around, this would be much faster. "
                    jac " Alright, alright... "
                    jac " Let's get to looking now. "
                    jac " Who knows where it could be right now? "
                    hide sparkhappy at bottom
                    show sparkneutral at left
                    sp " Oh, uh...right. "
                    sp " I'll go and check the left side of the school. "
                    jac " I'll go check out the right. "
                    jac " [name] can go whereever [they] want. "
                    " You gave them a thumbs up before you went back into the school and went to looking. "
                    scene black with dissolve
                    " You spent the rest of the break finding stuff with Spark and Jacob. "
                    " You weren't really finding anything, though - ...what the hell. "
                    " How did it get here??? "
                    " Uh. You know what, I'm just going to teleport this thing to you. "
                    " Return it back to Spark. Pretty sure this thing is named Scrap? "
                    " Atleast that's what I remember. "
                    " Just tell them that you found it near the vents. "
                    " Ahem.... "
                    " You eventually found the thing Spark was looking for and gave it to him. "
                    " Told him that you found it trying to get into the vents. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You talked with Spark and Jacob for a bit, before going to your classroom. "
                    pause 2.0
                    jump tphysicsclass1
                " I'm busy this break, sorry guys ":
                    sp " Alrighty. "
                    sp " Still - if you see anything, just give it to me. "
                    jac " We've got no more time to lose, Spark. "
                    jac " Let's start looking around right now. "
                    sp " Okay - see you later, [name]. "
                    hide jacobneutral at right with easeoutright
                    hide sparkneutral at right with easeoutright
                    scene black with dissolve
                    " You spent the rest of the break just wandering around the school. "
                    " Nothing really interesting caught your attention...hey, wait... "
                    " What's that trying to get into the vents? "
                    " You reached up and got it down, and it looked like that thing Spark was looking for. "
                    " You looked around to find Spark and eventually spotted him at the library. "
                    " You gave him the thing you found before you went back to wanderng around the school. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after you wander around for a good bit. "
                    " You continue wandering around for a bit before you went to your classroom. "
                    pause 2.0
                    jump tphysicsclass1
        else:
            x " Heya [name]. "
            x " Oh god - [name]'s here?! "
            x " Great, atleast [they] can help us in finding this thing faster. "
            " You asked them what they were looking for. "
            " Whatever it is, you might've seen it before. "
            x " You see, uh... "
            $ jacobknow = True
            $ sparkknow = True
            jac " Okay, before I say antyhing else - I'm Jacob, and uh... "
            jac " Spark over here kind of has this weird computer pet. "
            jac " And it kinda just ran away during class earlier. "
            jac " So we're kind of just walking around and trying to find it. "
            " You asked them what it looked like. "
            sp " It's basically like this tiny screen thing with four sharp legs... "
            sp " And it's also got antennas like mine. "
            sp " It usually doesn't run off from me unless if it's planning something. "
            sp " And I don't want the entire school to blow up because of it. "
            sp " It usually just does something stupid, but it can also do that too. "
            jac " Aaaand that's why we need to find it. "
            jac " I don't wanna go back to looking for another school to go in. "
            sp " Oh yeah, 'cause most schools are shit around here. "
            sp " And also because I don't want to pay for the damages. "
            sp " You wanna help us look for it, or are you busy doing stuff? "
            sp " We don't mind if you don't wanna help though. "
            jac " Yeah, we won't bother you if you're busy. "
            menu:
                " I want to help ":
                    $ sparklv += 5
                    $ jacoblv == 5
                    hide sparkneutral at bottom
                    show sparkhappy at left
                    sp " Awesome. The more, the better. "
                    sp " Now that we have three people looking around, this would be much faster. "
                    jac " Alright, alright... "
                    jac " Let's get to looking now. "
                    jac " Who knows where it could be right now? "
                    hide sparkhappy at bottom
                    show sparkneutral at left
                    sp " Oh, uh...right. "
                    sp " I'll go and check the left side of the school. "
                    jac " I'll go check out the right. "
                    jac " [name] can go whereever [they] want. "
                    " You gave them a thumbs up before you went back into the school and went to looking. "
                    scene black with dissolve
                    " You spent the rest of the break finding stuff with Spark and Jacob. "
                    " You weren't really finding anything, though - ...what the hell. "
                    " How did it get here??? "
                    " Uh. You know what, I'm just going to teleport this thing to you. "
                    " Return it back to Spark. Pretty sure this thing is named Scrap? "
                    " Atleast that's what I remember. "
                    " Just tell them that you found it near the vents. "
                    " Ahem.... "
                    " You eventually found the thing Spark was looking for and gave it to him. "
                    " Told him that you found it trying to get into the vents. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You talked with Spark and Jacob for a bit, before going to your classroom. "
                    pause 2.0
                    jump tphysicsclass1
                " I'm busy this break, sorry guys ":
                    sp " Alrighty. "
                    sp " Still - if you see anything, just give it to me. "
                    jac " We've got no more time to lose, Spark. "
                    jac " Let's start looking around right now. "
                    sp " Okay - see you later, [name]. "
                    hide jacobneutral at right with easeoutright
                    hide sparkneutral at right with easeoutright
                    scene black with dissolve
                    " You spent the rest of the break just wandering around the school. "
                    " Nothing really interesting caught your attention...hey, wait... "
                    " What's that trying to get into the vents? "
                    " You reached up and got it down, and it looked like that thing Spark was looking for. "
                    " You looked around to find Spark and eventually spotted him at the library. "
                    " You gave him the thing you found before you went back to wanderng around the school. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after you wander around for a good bit. "
                    " You continue wandering around for a bit before you went to your classroom. "
                    pause 2.0
                    jump tphysicsclass1
    label octhursback4:
        # carmen and temero
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of the school and found your two classmates doing their own things. "
        " Who should you talk to? "
        if carmenknow == True and temeroknow == True:
            menu:
                " {image=carmenicon} Carmen {image=carmenicon} ":
                    jump rawdog
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump wardromance
        elif carmenknow == True and temeroknow == False:
            menu:
                " {image=carmenicon} Carmen {image=carmenicon} ":
                    jump rawdog
                " {image=temeroicon} A evil scientist girl {image=temeroicon} ":
                    jump wardromance
        elif carmenknow == False and temeroknow == True:
            menu:
                " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                    jump rawdog
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump wardromance
        else:
            menu:
                " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                    jump rawdog
                " {image=temeroicon} A evil scientist girl {image=temeroicon} ":
                    jump wardromance
        label rawdog:
            show carmenneutral at center with easeinright
            if carmenknow == True:
                " You walked over to him and asked what he was doing. "
                " ...He didn't respond for some reason. "
                " I mean - he can't really do that verbally due to being mute. "
                " But you thought he would atleast wave at you. "
                " You looked at him a bit more closer and turns out he was listening to music. "
                " Just some music on his phone... "
                " After a bit, he started playing some tunes on his guitar... "
                " Most likely replicating how the music sounds. "
                " It sounded pretty nice... "
                " You could probably listen to this for hours. "
                ca " ... "
                " Aaaand looks like he noticed you. "
                " He seems as if he was inviting you to listen to his guitar playing. "
                " It's alright if you don't, it was just an offer. "
                " Your choice. Should you listen to him playing the guitar? "
                " Or do you think you have something better to do? "
                menu:
                    " Let's listen to him play ":
                        $ carmenlv += 10
                        hide carmenneutral at bottom
                        show carmenhappy at center
                        ca " ...! "
                        " He seems quite happy that you wanted to listen to him play. "
                        " He gestures for you to sit down on the ground next to him. "
                        " I mean, it would be pretty awkward if you just stood there while he played. "
                        " And being awkward is no good, right? "
                        hide carmenhappy at bottom
                        show carmenneutral at center
                        " You sat down next to him, ready to hear some good tunes. "
                        " He seemed to replay the song so you could get the full experience...or something. "
                        " He didn't really want to ruin it for you. "
                        " He took a deep breath in, before he started playing. "
                        scene black with dissolve
                        " You spent the rest of the break hearing Carmen play some nice tunes. "
                        " You swore that you almost fell asleep by hearing them... "
                        " In a good way, of course. "
                        " Beats so fire, you fall asleep to them. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit though, signalling that it's time for another class. "
                        " You wanted to listen to Carmen's playing a little longer, but...oh well. "
                        " You walked back into the school and went to your classroom after a good bit. "
                        pause 2.0
                        jump tphysicsclass1
                    " I'm kind of busy, sorry ":
                        ca " ... "
                        " He looked like he understood. "
                        " He also looked like he didn't want to bother you anymore. "
                        " Time for you to go out... "
                        scene black with dissolve
                        " You spent the rest of the break wandering around the school. "
                        " You didn't really see anything interesting that caught your eye. "
                        " Other than a little computer thing trying to get into the vents. "
                        " You didn't want to disturb it though. "
                        " It looked like it was on a mission for something. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, looks like it's time for your next class. "
                        " You continued wandering for a bit before you went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
            else:
                " Oh hey, you've heard of this guy before. "
                $ carmenknow = True
                " This guy is Carmen. He likes to play the guitar. "
                " He's also mute. "
                " You walked over to him and asked what he was doing. "
                " ...He didn't respond for some reason. "
                " I mean - he can't really do that verbally due to being mute. "
                " But you thought he would atleast wave at you. "
                " You looked at him a bit more closer and turns out he was listening to music. "
                " Just some music on his phone... "
                " After a bit, he started playing some tunes on his guitar... "
                " Most likely replicating how the music sounds. "
                " It sounded pretty nice... "
                " You could probably listen to this for hours. "
                ca " ... "
                " Aaaand looks like he noticed you. "
                " He seems as if he was inviting you to listen to his guitar playing. "
                " It's alright if you don't, it was just an offer. "
                " Your choice. Should you listen to him playing the guitar? "
                " Or do you think you have something better to do? "
                menu:
                    " Let's listen to him play ":
                        $ carmenlv += 10
                        hide carmenneutral at bottom
                        show carmenhappy at center
                        ca " ...! "
                        " He seems quite happy that you wanted to listen to him play. "
                        " He gestures for you to sit down on the ground next to him. "
                        " I mean, it would be pretty awkward if you just stood there while he played. "
                        " And being awkward is no good, right? "
                        hide carmenhappy at bottom
                        show carmenneutral at center
                        " You sat down next to him, ready to hear some good tunes. "
                        " He seemed to replay the song so you could get the full experience...or something. "
                        " He didn't really want to ruin it for you. "
                        " He took a deep breath in, before he started playing. "
                        scene black with dissolve
                        " You spent the rest of the break hearing Carmen play some nice tunes. "
                        " You swore that you almost fell asleep by hearing them... "
                        " In a good way, of course. "
                        " Beats so fire, you fall asleep to them. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit though, signalling that it's time for another class. "
                        " You wanted to listen to Carmen's playing a little longer, but...oh well. "
                        " You walked back into the school and went to your classroom after a good bit. "
                        pause 2.0
                        jump tphysicsclass1
                    " I'm kind of busy, sorry ":
                        ca " ... "
                        " He looked like he understood. "
                        " He also looked like he didn't want to bother you anymore. "
                        " Time for you to go out... "
                        scene black with dissolve
                        " You spent the rest of the break wandering around the school. "
                        " You didn't really see anything interesting that caught your eye. "
                        " Other than a little computer thing trying to get into the vents. "
                        " You didn't want to disturb it though. "
                        " It looked like it was on a mission for something. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, looks like it's time for your next class. "
                        " You continued wandering for a bit before you went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
        label wardromance:
            show temeroneutral at center with easeinleft
            if temeroknow == True:
                " You walked over to her and asked what she was doing. "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " Huh? oh, you!! "
                tm " I was just in the middle of doing one of my experiments. "
                tm " Though, this time! "
                tm " It's a LITTLE bit different. "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " You see...I usually make these to test how far I can go with these. "
                tm " But, this time! "
                tm " I'm doing it to impress someone, ooo. "
                tm " 'But oh great Temero Neo! who are you trying to impress?' "
                tm " You'll have to guess. "
                tm " It's not a student at this school! "
                tm " It's not a teacher! "
                tm " It's no one in this school, actually! "
                tm " I would say it's to impress myself, but that's also not really the case here. "
                tm " I'm doing it to impress someone from another school! "
                tm " Not sure if you've heard of this news before buuut... "
                tm " We've had to move to another school temporarily due to some issues. "
                tm " Annnd, that school was where I met this girl! "
                tm " That's who I'm trying to impress right now! "
                tm " We only got to be there for a week, so of course I got really sad when we left. "
                tm " People saw her as the mean girl, but personally? "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " I thought that whole personality was HOT. "
                tm " Like oooh mama, I'd let you make fun of me anytime you want! "
                tm " ...Eheh. Okay, I may be going too far over here. "
                tm " But still - she's really pretty and I want to impress her! "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " Hmm...you think you got any ideas? "
                tm " I could try making the butterfly explode in confetti... "
                tm " But I doubt that would be cool for her. "
                tm " I need something impressive! "
                menu:
                    " Make it butterfly explode into roses as you ask her to hangout with you ":
                        $ temerolv += 10
                        hide temeroneutral at bottom
                        show temerohappy at center
                        tm " Oho! pretty good idea! "
                        tm " Knowing her, she'd think it would be funny and agree. "
                        tm " You see - we actually talked for a good bit. "
                        tm " Got to know eachother well... "
                        tm " And we became really close in the matter of minutes! "
                        tm " She says she loves how chaotic I am. "
                        tm " I sometimes even partake in their pranks while I was at their school! "
                        tm " Trust me, it was all fun. "
                        hide temerohappy at bottom
                        show temeroneutral at center
                        tm " Now! "
                        tm " It's time to work on that idea you just gave me. "
                        tm " Thanks for helping me out! "
                        tm " As a reward - you get the privilege to see me make your idea come to life! "
                        tm " Just watch and learn... "
                        scene black with dissolve
                        " You spent the rest of the break watching Temero make her experiment. "
                        " It was pretty cool, getting to see how things were made. "
                        " Not sure if this was actually going to impress that girl she's into, but it's cool in your eyes. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked back into the school and then went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
                    " that idea above this one is concerning so this one is the one where you have no idea what to do ":
                        tm " You don't got an idea? that's fine. "
                        tm " I could come up with my own! "
                        tm " Anyway, about that girl... "
                        tm " You see - we actually talked for a good bit. "
                        tm " Got to know eachother well... "
                        tm " And we became really close in the matter of minutes! "
                        tm " She says she loves how chaotic I am. "
                        tm " I sometimes even partake in their pranks while I was at their school! "
                        tm " Trust me, it was all fun. "
                        hide temerohappy at bottom
                        show temeroneutral at center
                        tm " Now! "
                        tm " It's time to work on an idea I just got. "
                        tm " Thanks for helping me out, even though you didn't give me an idea. "
                        tm " You also get the special privilege to see me make my idea come to life! "
                        tm " Just watch and learn... "
                        scene black with dissolve
                        " You spent the rest of the break watching Temero make her experiment. "
                        " It was pretty cool, getting to see how things were made. "
                        " Not sure if this was actually going to impress that girl she's into, but it's cool in your eyes. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked back into the school and then went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
            else:
                " You walked over to her and asked what she was doing. "
                hide temeroneutral at bottom
                show temerohappy at center
                x " Huh? oh, you!! "
                $ temeroknow = True
                tm " I don't think we've met before, so my name is the great Temero NEO! "
                tm " I was just in the middle of doing one of my experiments. "
                tm " Though, this time! "
                tm " It's a LITTLE bit different. "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " You see...I usually make these to test how far I can go with these. "
                tm " But, this time! "
                tm " I'm doing it to impress someone, ooo. "
                tm " 'But oh great Temero Neo! who are you trying to impress?' "
                tm " You'll have to guess. "
                tm " It's not a student at this school! "
                tm " It's not a teacher! "
                tm " It's no one in this school, actually! "
                tm " I would say it's to impress myself, but that's also not really the case here. "
                tm " I'm doing it to impress someone from another school! "
                tm " Not sure if you've heard of this news before buuut... "
                tm " We've had to move to another school temporarily due to some issues. "
                tm " Annnd, that school was where I met this girl! "
                tm " That's who I'm trying to impress right now! "
                tm " We only got to be there for a week, so of course I got really sad when we left. "
                tm " People saw her as the mean girl, but personally? "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " I thought that whole personality was HOT. "
                tm " Like oooh mama, I'd let you make fun of me anytime you want! "
                tm " ...Eheh. Okay, I may be going too far over here. "
                tm " But still - she's really pretty and I want to impress her! "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " Hmm...you think you got any ideas? "
                tm " I could try making the butterfly explode in confetti... "
                tm " But I doubt that would be cool for her. "
                tm " I need something impressive! "
                menu:
                    " Make it butterfly explode into roses as you ask her to hangout with you ":
                        $ temerolv += 10
                        hide temeroneutral at bottom
                        show temerohappy at center
                        tm " Oho! pretty good idea! "
                        tm " Knowing her, she'd think it would be funny and agree. "
                        tm " You see - we actually talked for a good bit. "
                        tm " Got to know eachother well... "
                        tm " And we became really close in the matter of minutes! "
                        tm " She says she loves how chaotic I am. "
                        tm " I sometimes even partake in their pranks while I was at their school! "
                        tm " Trust me, it was all fun. "
                        hide temerohappy at bottom
                        show temeroneutral at center
                        tm " Now! "
                        tm " It's time to work on that idea you just gave me. "
                        tm " Thanks for helping me out! "
                        tm " As a reward - you get the privilege to see me make your idea come to life! "
                        tm " Just watch and learn... "
                        scene black with dissolve
                        " You spent the rest of the break watching Temero make her experiment. "
                        " It was pretty cool, getting to see how things were made. "
                        " Not sure if this was actually going to impress that girl she's into, but it's cool in your eyes. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked back into the school and then went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
                    " that idea above this one is concerning so this one is the one where you have no idea what to do ":
                        tm " You don't got an idea? that's fine. "
                        tm " I could come up with my own! "
                        tm " Anyway, about that girl... "
                        tm " You see - we actually talked for a good bit. "
                        tm " Got to know eachother well... "
                        tm " And we became really close in the matter of minutes! "
                        tm " She says she loves how chaotic I am. "
                        tm " I sometimes even partake in their pranks while I was at their school! "
                        tm " Trust me, it was all fun. "
                        hide temerohappy at bottom
                        show temeroneutral at center
                        tm " Now! "
                        tm " It's time to work on an idea I just got. "
                        tm " Thanks for helping me out, even though you didn't give me an idea. "
                        tm " You also get the special privilege to see me make my idea come to life! "
                        tm " Just watch and learn... "
                        scene black with dissolve
                        " You spent the rest of the break watching Temero make her experiment. "
                        " It was pretty cool, getting to see how things were made. "
                        " Not sure if this was actually going to impress that girl she's into, but it's cool in your eyes. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked back into the school and then went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
    label octhursgym4:
        # orchid and yangyi
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked into the gym and spotted two of your classmates talking to eachother. "
        " Wondering what they were talking about, you decided to walk over to them. "
        show orchidneutral at right with easeinleft
        show yangyineutral at left with easeinleft
        if orchidknow == True and yangyiknow == True:
            oc " Hey there, [name]! "
            ya " Oh, [name]'s here? "
            ya " Hello!! "
            ya " Me and Orchid were just talking about a few things... "
            oc " Like me making bracelets for everyone! "
            ya " Yeah!! it's a good idea, right? "
            ya " I mean, I don't think Yinhui would trust it very much... "
            oc " Eh? why? it's just a bracelet. "
            ya " You see... he's pretty protective, you know that, right? "
            hide orchidneutral at bottom
            show orchidsad at right
            oc " Yeah...? "
            oc " Don't tell me he doesn't trust bracelets. "
            oc " Come on, dude... "
            hide yangyineutral at bottom
            show yangyisurprised at left
            ya " It's not that he doesn't like them!! "
            ya " It's just that... "
            ya " It's a little bit difficult to trust things, you know? "
            ya " I mean...he kind of overthinks things a bit. "
            ya " If my brother got one of your bracelets, for example... "
            ya " He'd kind of think that there's a bomb in it. "
            ya " That's why he looks at things so thoroughly! "
            oc " ...You've gotta be joking. "
            oc " I mean, I get being overprotective... "
            oc " But looking at a bracelet for bombs?? really?? "
            oc " Hmmm... "
            oc " Have you tried convincing him that everything's not dangerous? "
            hide yangyisurprised at bottom
            show yangyineutral at left
            ya " Well... "
            ya " He'll stop thinking it's dangerous if I keep on telling him that it's not. "
            ya " Or if he's examined it for a long time. "
            oc " Geez... "
            oc " You've gotta tell your brother to cool off sometimes! "
            ya " I mean, he does try to... "
            ya " But he cares a whole lot about my safety, so he just keeps on checking things. "
            ya " So...he can't exactly cool off so easily. "
            oc " Hm... "
            scene black with dissolve
            " You spent the rest of the break talking with Orchid and Yangyi. "
            " You never knew Yinhui would be that protective... "
            " I guess we sometimes just have that protective sibling, huh? "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the gym and then went to your classroom. "
            pause 2.0
            jump tphysicsclass1
        elif orchidknow == True and yangyiknow == False:
            oc " Hey there, [name]! "
            x " Oh, [name]'s here? "
            $ yangyiknow = True
            ya " Hello, I'm Yangyi!!! "
            ya " Me and Orchid were just talking about a few things... "
            oc " Like me making bracelets for everyone! "
            ya " Yeah!! it's a good idea, right? "
            ya " I mean, I don't think Yinhui would trust it very much... "
            oc " Eh? why? it's just a bracelet. "
            ya " You see... he's pretty protective, you know that, right? "
            hide orchidneutral at bottom
            show orchidsad at right
            oc " Yeah...? "
            oc " Don't tell me he doesn't trust bracelets. "
            oc " Come on, dude... "
            hide yangyineutral at bottom
            show yangyisurprised at left
            ya " It's not that he doesn't like them!! "
            ya " It's just that... "
            ya " It's a little bit difficult to trust things, you know? "
            ya " I mean...he kind of overthinks things a bit. "
            ya " If my brother got one of your bracelets, for example... "
            ya " He'd kind of think that there's a bomb in it. "
            ya " That's why he looks at things so thoroughly! "
            oc " ...You've gotta be joking. "
            oc " I mean, I get being overprotective... "
            oc " But looking at a bracelet for bombs?? really?? "
            oc " Hmmm... "
            oc " Have you tried convincing him that everything's not dangerous? "
            hide yangyisurprised at bottom
            show yangyineutral at left
            ya " Well... "
            ya " He'll stop thinking it's dangerous if I keep on telling him that it's not. "
            ya " Or if he's examined it for a long time. "
            oc " Geez... "
            oc " You've gotta tell your brother to cool off sometimes! "
            ya " I mean, he does try to... "
            ya " But he cares a whole lot about my safety, so he just keeps on checking things. "
            ya " So...he can't exactly cool off so easily. "
            oc " Hm... "
            scene black with dissolve
            " You spent the rest of the break talking with Orchid and Yangyi. "
            " You never knew Yinhui would be that protective... "
            " I guess we sometimes just have that protective sibling, huh? "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the gym and then went to your classroom. "
            pause 2.0
            jump tphysicsclass1
        elif orchidknow == False and yangyiknow == True:
            x " Hey there, [name]! "
            ya " Oh, [name]'s here? "
            ya " Hello!! "
            $ orchidknow = True
            ya " Me and Orchid were just talking about a few things... "
            oc " Like me making bracelets for everyone! "
            ya " Yeah!! it's a good idea, right? "
            ya " I mean, I don't think Yinhui would trust it very much... "
            oc " Eh? why? it's just a bracelet. "
            ya " You see... he's pretty protective, you know that, right? "
            hide orchidneutral at bottom
            show orchidsad at right
            oc " Yeah...? "
            oc " Don't tell me he doesn't trust bracelets. "
            oc " Come on, dude... "
            hide yangyineutral at bottom
            show yangyisurprised at left
            ya " It's not that he doesn't like them!! "
            ya " It's just that... "
            ya " It's a little bit difficult to trust things, you know? "
            ya " I mean...he kind of overthinks things a bit. "
            ya " If my brother got one of your bracelets, for example... "
            ya " He'd kind of think that there's a bomb in it. "
            ya " That's why he looks at things so thoroughly! "
            oc " ...You've gotta be joking. "
            oc " I mean, I get being overprotective... "
            oc " But looking at a bracelet for bombs?? really?? "
            oc " Hmmm... "
            oc " Have you tried convincing him that everything's not dangerous? "
            hide yangyisurprised at bottom
            show yangyineutral at left
            ya " Well... "
            ya " He'll stop thinking it's dangerous if I keep on telling him that it's not. "
            ya " Or if he's examined it for a long time. "
            oc " Geez... "
            oc " You've gotta tell your brother to cool off sometimes! "
            ya " I mean, he does try to... "
            ya " But he cares a whole lot about my safety, so he just keeps on checking things. "
            ya " So...he can't exactly cool off so easily. "
            oc " Hm... "
            scene black with dissolve
            " You spent the rest of the break talking with Orchid and Yangyi. "
            " You never knew Yinhui would be that protective... "
            " I guess we sometimes just have that protective sibling, huh? "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the gym and then went to your classroom. "
            pause 2.0
            jump tphysicsclass1
        else:
            x " Hey there, [name]! "
            x " Oh, [name]'s here? "
            $ yangyiknow = True
            ya " Hello, I'm Yangyi!!! "
            $ orchidknow = True
            ya " Me and Orchid were just talking about a few things... "
            oc " Like me making bracelets for everyone! "
            ya " Yeah!! it's a good idea, right? "
            ya " I mean, I don't think Yinhui would trust it very much... "
            oc " Eh? why? it's just a bracelet. "
            ya " You see... he's pretty protective, you know that, right? "
            hide orchidneutral at bottom
            show orchidsad at right
            oc " Yeah...? "
            oc " Don't tell me he doesn't trust bracelets. "
            oc " Come on, dude... "
            hide yangyineutral at bottom
            show yangyisurprised at left
            ya " It's not that he doesn't like them!! "
            ya " It's just that... "
            ya " It's a little bit difficult to trust things, you know? "
            ya " I mean...he kind of overthinks things a bit. "
            ya " If my brother got one of your bracelets, for example... "
            ya " He'd kind of think that there's a bomb in it. "
            ya " That's why he looks at things so thoroughly! "
            oc " ...You've gotta be joking. "
            oc " I mean, I get being overprotective... "
            oc " But looking at a bracelet for bombs?? really?? "
            oc " Hmmm... "
            oc " Have you tried convincing him that everything's not dangerous? "
            hide yangyisurprised at bottom
            show yangyineutral at left
            ya " Well... "
            ya " He'll stop thinking it's dangerous if I keep on telling him that it's not. "
            ya " Or if he's examined it for a long time. "
            oc " Geez... "
            oc " You've gotta tell your brother to cool off sometimes! "
            ya " I mean, he does try to... "
            ya " But he cares a whole lot about my safety, so he just keeps on checking things. "
            ya " So...he can't exactly cool off so easily. "
            oc " Hm... "
            scene black with dissolve
            " You spent the rest of the break talking with Orchid and Yangyi. "
            " You never knew Yinhui would be that protective... "
            " I guess we sometimes just have that protective sibling, huh? "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the gym and then went to your classroom. "
            pause 2.0
            jump tphysicsclass1
    label octhurscafeteria4:
        # quinn and jam
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked into the cafeteria and found two of your classmates doing their own things. "
        " Who do you talk to? "
        if quinnknow == True and jamknow == True:
            menu:
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump urminminmin
                " {image=jamicon} Jam {image=jamicon} ":
                    jump hoeisdundundun
        elif quinnknow == True and jamknow == False:
            menu:
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump urminminmin
                " {image=jamicon} A mean looking girl {image=jamicon} ":
                    jump hoeisdundundun
        elif quinnknow == False and jamknow == True:
            menu:
                " {image=quinnicon} A theater guy {image=quinnicon} ":
                    jump urminminmin
                " {image=jamicon} Jam {image=jamicon} ":
                    jump hoeisdundundun
        else:
            menu:
                " {image=quinnicon} A theater guy {image=quinnicon} ":
                    jump urminminmin
                " {image=jamicon} A mean looking girl {image=jamicon} ":
                    jump hoeisdundundun
        label urminminmin:
            show quinnneutral at center with easeinleft
            if quinnknow == True:
                q " Hmmmhmm... "
                q " The food here is always so good... "
                q " Though nothing beats the food at home. "
                q " The chefs back there always manage to cook up delicious stuff back there! "
                q " I think I might need to order more of these... "
                " You sat down next to him and asked him if he was enjoying his food. "
                hide quinnneutral at bottom
                show quinnhappy at center
                q " Hey there, [name]! "
                q " And yes, I'm enjoying my food very much. "
                q " I just decided to eat something before I start practicing with my club members. "
                q " I always kind of thought school food would taste bad due to movies, actually. "
                q " Always saw they were mush and that's why I kind of avoided getting food at canteens... "
                q " But, since this is a prestigious school - I guess the food isn't so bad. "
                q " It's quite good, actually! "
                q " The cooks must be getting paid well if they're cooking like this, hehe. "
                hide quinnhappy at bottom
                show quinnneutral at center
                q " I should probably leave a tip for them... "
                q " ...Hey, [name]. "
                q " I need to go get some more food, alright? "
                q " Would you want some? "
                menu:
                    " yeah im hungry vrah ":
                        $ quinnlv += 5
                        q " Oh, you're hungry? "
                        q " I'll make sure to get a little bit more food for you, then! "
                        q " I don't want you to feel hungry after all, hehe. "
                        q " I'll buy everything for you, don't worry. "
                        q " I'm not going to be hearing any complaints from you. "
                        q " You say you're hungry - I'm going to feed you an entire 5 star meal. "
                        " Thank you Quinn, we say in unison. "
                        scene black with dissolve
                        " You spent the rest of the break talking and eating with Quinn. "
                        " Just talking about how Quinn's play is going... "
                        " And looks like everything's been going well. "
                        " He told you that he won't be in the next class though. "
                        " He had to go work on his play, after all. "
                        " He also already asked every teacher for permission for this. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for the next class. "
                        " You watched Quinn leave before you went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
                    " nah im not hungry ":
                        q " Okay, if you say so. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Just talking about how Quinn's play is going... "
                        " And looks like everything's been going well. "
                        " He told you that he won't be in the next class though. "
                        " He had to go work on his play, after all. "
                        " He also already asked every teacher for permission for this. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for the next class. "
                        " You watched Quinn leave before you went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
            else:
                x " Hmmmhmm... "
                x " The food here is always so good... "
                x " Though nothing beats the food at home. "
                x " The chefs back there always manage to cook up delicious stuff back there! "
                x " I think I might need to order more of these... "
                " You sat down next to him and asked him if he was enjoying his food. "
                hide quinnneutral at bottom
                show quinnhappy at center
                x " Hey there, [name]! "
                x " And yes, I'm enjoying my food very much. "
                $ quinnknow = True
                q " Oh - I'm Quinn, by the way. Part of the drama club. "
                q " I just decided to eat something before I start practicing with my club members. "
                q " I always kind of thought school food would taste bad due to movies, actually. "
                q " Always saw they were mush and that's why I kind of avoided getting food at canteens... "
                q " But, since this is a prestigious school - I guess the food isn't so bad. "
                q " It's quite good, actually! "
                q " The cooks must be getting paid well if they're cooking like this, hehe. "
                hide quinnhappy at bottom
                show quinnneutral at center
                q " I should probably leave a tip for them... "
                q " ...Hey, [name]. "
                q " I need to go get some more food, alright? "
                q " Would you want some? "
                menu:
                    " yeah im hungry vrah ":
                        $ quinnlv += 5
                        q " Oh, you're hungry? "
                        q " I'll make sure to get a little bit more food for you, then! "
                        q " I don't want you to feel hungry after all, hehe. "
                        q " I'll buy everything for you, don't worry. "
                        q " I'm not going to be hearing any complaints from you. "
                        q " You say you're hungry - I'm going to feed you an entire 5 star meal. "
                        " Thank you Quinn, we say in unison. "
                        scene black with dissolve
                        " You spent the rest of the break talking and eating with Quinn. "
                        " Just talking about how Quinn's play is going... "
                        " And looks like everything's been going well. "
                        " He told you that he won't be in the next class though. "
                        " He had to go work on his play, after all. "
                        " He also already asked every teacher for permission for this. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for the next class. "
                        " You watched Quinn leave before you went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
                    " nah im not hungry ":
                        q " Okay, if you say so. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Just talking about how Quinn's play is going... "
                        " And looks like everything's been going well. "
                        " He told you that he won't be in the next class though. "
                        " He had to go work on his play, after all. "
                        " He also already asked every teacher for permission for this. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for the next class. "
                        " You watched Quinn leave before you went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
        label hoeisdundundun:
            show jamneutral at center with easeinright
            if jamknow == True:
                " You walked over to her and then sat next to her. "
                " Politely, you asked her what she was doing. "
                ja " ..? Oh - [name]. "
                ja " Was just thinking about...things. "
                ja " There's this song that's been stuck in my head for a bit now. "
                ja " I listened to it one night, thinking it was alright... "
                ja " I thought I wouldn't get too addicted to it. "
                ja " But guess what? I keep on listening to it now. "
                ja " It's a nice song about a breakup. "
                ja " It's got a pretty nice beat to it... "
                ja " It's always the sad songs that sound so nice. "
                hide jamneutral at bottom
                show jamsad at center
                ja " Except for those wanna be 'emo-sad-crying' songs. "
                ja " God, those are just...cringy, in all honesty. "
                ja " Anyway, about the song I talked about... "
                hide jamsad at bottom
                show jamneutral at center
                ja " The person in the song talks about how they still love the person they broke up with. "
                ja " They're trying to get over them, but they just struggle to. "
                ja " It's sad, but break ups happen. "
                ja " Like - uh...how do I word this. "
                ja " Like what the old people say: "
                ja " If you really love them, you've got to let them go. "
                ja " Letting them go means that you respect their decision and hope that they're happy. "
                ja " Hope that they're going to be happy on their next relationship, "
                ja " Or hope that they're going to be happy all alone. "
                ja " However their life goes, you just have to hope they're doing well. "
                ja " You can still care for them, yes, but that care you showed them when you two were together... "
                ja " You probably can't care for them that way again. "
                ja " But, what you can do is just care for them as a friend. "
                ja " Not a lover - because that's all in the past now. "
                hide jamneutral at bottom
                show jamsad at center
                ja " Jeez, what am I doing? "
                ja " I'm talking about relationships like I'm a professional even though I know nothing. "
                ja " It's...insane. "
                ja " I didn't mean to ramble like that, I'm sorry. "
                menu:
                    " You're all good ":
                        $ jamlv += 5
                        hide jamsad at bottom
                        show jamneutral at center
                        ja " Really? alright... "
                        ja " If you said I did alright, then uh... "
                        ja " I'll believe you on that one. "
                        ja " (...Okay, now what do I talk about.) "
                        ja " (Uh...how about how [their] day went?) "
                        ja " Uh...so. "
                        ja " Moving on from that topic... "
                        ja " How was your day today? "
                        scene black with dissolve
                        " You spent the rest of the break talking with Jam. "
                        " Just talking to her about how your day went... "
                        " Which was a little bit boring, but there were some interesting parts. "
                        " Only some, though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the cafeteria and went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
                    " *say nothing* ":
                        ja " ... "
                        ja " (Okay, great...) "
                        ja " (I just made thins more awkward.) "
                        ja " (Great going, Jam.) "
                        ja " (Quick, uh...talk about something else.) "
                        hide jamsad at bottom
                        show jamneutral at center
                        ja " Uh...so. "
                        ja " Moving on from that topic... "
                        ja " How was your day today? "
                        scene black with dissolve
                        " You spent the rest of the break talking with Jam. "
                        " Just talking to her about how your day went... "
                        " Which was a little bit boring, but there were some interesting parts. "
                        " Only some, though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the cafeteria and went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
            else:
                " You walked over to her and then sat next to her. "
                " Politely, you asked her what she was doing. "
                x " ..? Oh - [name]. "
                x " Was just thinking about...things. "
                $ jamknow = True
                ja " I'm uh... Jam, by the way. "
                ja " There's this song that's been stuck in my head for a bit now. "
                ja " I listened to it one night, thinking it was alright... "
                ja " I thought I wouldn't get too addicted to it. "
                ja " But guess what? I keep on listening to it now. "
                ja " It's a nice song about a breakup. "
                ja " It's got a pretty nice beat to it... "
                ja " It's always the sad songs that sound so nice. "
                hide jamneutral at bottom
                show jamsad at center
                ja " Except for those wanna be 'emo-sad-crying' songs. "
                ja " God, those are just...cringy, in all honesty. "
                ja " Anyway, about the song I talked about... "
                hide jamsad at bottom
                show jamneutral at center
                ja " The person in the song talks about how they still love the person they broke up with. "
                ja " They're trying to get over them, but they just struggle to. "
                ja " It's sad, but break ups happen. "
                ja " Like - uh...how do I word this. "
                ja " Like what the old people say: "
                ja " If you really love them, you've got to let them go. "
                ja " Letting them go means that you respect their decision and hope that they're happy. "
                ja " Hope that they're going to be happy on their next relationship, "
                ja " Or hope that they're going to be happy all alone. "
                ja " However their life goes, you just have to hope they're doing well. "
                ja " You can still care for them, yes, but that care you showed them when you two were together... "
                ja " You probably can't care for them that way again. "
                ja " But, what you can do is just care for them as a friend. "
                ja " Not a lover - because that's all in the past now. "
                hide jamneutral at bottom
                show jamsad at center
                ja " Jeez, what am I doing? "
                ja " I'm talking about relationships like I'm a professional even though I know nothing. "
                ja " It's...insane. "
                ja " I didn't mean to ramble like that, I'm sorry. "
                menu:
                    " You're all good ":
                        $ jamlv += 5
                        hide jamsad at bottom
                        show jamneutral at center
                        ja " Really? alright... "
                        ja " If you said I did alright, then uh... "
                        ja " I'll believe you on that one. "
                        ja " (...Okay, now what do I talk about.) "
                        ja " (Uh...how about how [their] day went?) "
                        ja " Uh...so. "
                        ja " Moving on from that topic... "
                        ja " How was your day today? "
                        scene black with dissolve
                        " You spent the rest of the break talking with Jam. "
                        " Just talking to her about how your day went... "
                        " Which was a little bit boring, but there were some interesting parts. "
                        " Only some, though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the cafeteria and went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
                    " *say nothing* ":
                        ja " ... "
                        ja " (Okay, great...) "
                        ja " (I just made thins more awkward.) "
                        ja " (Great going, Jam.) "
                        ja " (Quick, uh...talk about something else.) "
                        hide jamsad at bottom
                        show jamneutral at center
                        ja " Uh...so. "
                        ja " Moving on from that topic... "
                        ja " How was your day today? "
                        scene black with dissolve
                        " You spent the rest of the break talking with Jam. "
                        " Just talking to her about how your day went... "
                        " Which was a little bit boring, but there were some interesting parts. "
                        " Only some, though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the cafeteria and went to your classroom. "
                        pause 2.0
                        jump tphysicsclass1
    label octhursrooftop4:
        # disk and nox
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked over to the rooftop and spotted two of your classmates talking to eachother. "
        " Wondering what they're talking about, you decided to walk over to them. "
        show diskneutral at left with easeinright
        show noxneutral at right with easeinright
        if diskknow == True and noxknow == True:
            d " Hey there, [name]!! "
            n " Mmm..? oh, [name]'s here...? "
            d " Yup yup! "
            d " I was just talking to Nox over here to see if he was alright! "
            d " Didn't want my classmate to faint, you know? "
            n " Mmm...it's nice that you're checking up on me... "
            n " But I'm sure I'm fine... "
            hide diskneutral at bottom
            show diskangry at left
            d " Oh come on, Noxxy! "
            d " The last time you said that... "
            d " You fainted in the middle of PE! "
            d " You don't know how worried we were for you! "
            n " Sorry... "
            n " I just forgot to take my meds that time... "
            hide diskangry at bottom
            show disksad at left
            d " It's okay...but... "
            d " You should probably get someone to remind you to take your meds. "
            d " It's not good to keep forgetting. "
            d " If you keep on forgetting, you kow what'll happen... "
            n " Yeah... "
            n " Sorry again... "
            n " I'll try to remember... "
            n " I don't want to keep worrying you... "
            hide disksad at bottom
            show diskneutral at left
            d " You better try! "
            d " Otherwise I'm gonna shove meds in your mouth everytime you go to school! "
            n " Noooo...don't do thaaaat... "
            d " I will, if you keep forgetting! "
            n " Okay, okayyy... "
            n " I'll try my absolute best to remember, then... "
            d " Good! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Nox. "
            " Huh...now you're wondering how often Nox forgets about his meds. "
            " It's honestly pretty concerning. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down off of the rooftop, and then went to your classroom. "
            pause 2.0
            jump tphysicsclass1
        elif diskknow == True and noxknow == False:
            d " Hey there, [name]!! "
            x " Mmm..? oh, [name]'s here...? "
            d " Yup yup! "
            $ noxknow = True
            d " I was just talking to Nox over here to see if he was alright! "
            d " Didn't want my classmate to faint, you know? "
            n " Mmm...it's nice that you're checking up on me... "
            n " But I'm sure I'm fine... "
            hide diskneutral at bottom
            show diskangry at left
            d " Oh come on, Noxxy! "
            d " The last time you said that... "
            d " You fainted in the middle of PE! "
            d " You don't know how worried we were for you! "
            n " Sorry... "
            n " I just forgot to take my meds that time... "
            hide diskangry at bottom
            show disksad at left
            d " It's okay...but... "
            d " You should probably get someone to remind you to take your meds. "
            d " It's not good to keep forgetting. "
            d " If you keep on forgetting, you kow what'll happen... "
            n " Yeah... "
            n " Sorry again... "
            n " I'll try to remember... "
            n " I don't want to keep worrying you... "
            hide disksad at bottom
            show diskneutral at left
            d " You better try! "
            d " Otherwise I'm gonna shove meds in your mouth everytime you go to school! "
            n " Noooo...don't do thaaaat... "
            d " I will, if you keep forgetting! "
            n " Okay, okayyy... "
            n " I'll try my absolute best to remember, then... "
            d " Good! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Nox. "
            " Huh...now you're wondering how often Nox forgets about his meds. "
            " It's honestly pretty concerning. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down off of the rooftop, and then went to your classroom. "
            pause 2.0
            jump tphysicsclass1
        elif diskknow == False and noxknow == True:
            x " Hey there, [name]!! "
            n " Mmm..? oh, [name]'s here...? "
            x " Yup yup! "
            $ diskknow = True
            d " I'm Disk, by the way! "
            d " I was just talking to Nox over here to see if he was alright! "
            d " Didn't want my classmate to faint, you know? "
            n " Mmm...it's nice that you're checking up on me... "
            n " But I'm sure I'm fine... "
            hide diskneutral at bottom
            show diskangry at left
            d " Oh come on, Noxxy! "
            d " The last time you said that... "
            d " You fainted in the middle of PE! "
            d " You don't know how worried we were for you! "
            n " Sorry... "
            n " I just forgot to take my meds that time... "
            hide diskangry at bottom
            show disksad at left
            d " It's okay...but... "
            d " You should probably get someone to remind you to take your meds. "
            d " It's not good to keep forgetting. "
            d " If you keep on forgetting, you kow what'll happen... "
            n " Yeah... "
            n " Sorry again... "
            n " I'll try to remember... "
            n " I don't want to keep worrying you... "
            hide disksad at bottom
            show diskneutral at left
            d " You better try! "
            d " Otherwise I'm gonna shove meds in your mouth everytime you go to school! "
            n " Noooo...don't do thaaaat... "
            d " I will, if you keep forgetting! "
            n " Okay, okayyy... "
            n " I'll try my absolute best to remember, then... "
            d " Good! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Nox. "
            " Huh...now you're wondering how often Nox forgets about his meds. "
            " It's honestly pretty concerning. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down off of the rooftop, and then went to your classroom. "
            pause 2.0
            jump tphysicsclass1
        else:
            x " Hey there, [name]!! "
            x " Mmm..? oh, [name]'s here...? "
            x " Yup yup! "
            $ diskknow = True
            d " I'm Disk, by the way! "
            $ noxknow = True
            d " I was just talking to Nox over here to see if he was alright! "
            d " Didn't want my classmate to faint, you know? "
            n " Mmm...it's nice that you're checking up on me... "
            n " But I'm sure I'm fine... "
            hide diskneutral at bottom
            show diskangry at left
            d " Oh come on, Noxxy! "
            d " The last time you said that... "
            d " You fainted in the middle of PE! "
            d " You don't know how worried we were for you! "
            n " Sorry... "
            n " I just forgot to take my meds that time... "
            hide diskangry at bottom
            show disksad at left
            d " It's okay...but... "
            d " You should probably get someone to remind you to take your meds. "
            d " It's not good to keep forgetting. "
            d " If you keep on forgetting, you kow what'll happen... "
            n " Yeah... "
            n " Sorry again... "
            n " I'll try to remember... "
            n " I don't want to keep worrying you... "
            hide disksad at bottom
            show diskneutral at left
            d " You better try! "
            d " Otherwise I'm gonna shove meds in your mouth everytime you go to school! "
            n " Noooo...don't do thaaaat... "
            d " I will, if you keep forgetting! "
            n " Okay, okayyy... "
            n " I'll try my absolute best to remember, then... "
            d " Good! "
            scene black with dissolve
            " You spent the rest of the break talking with Disk and Nox. "
            " Huh...now you're wondering how often Nox forgets about his meds. "
            " It's honestly pretty concerning. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked down off of the rooftop, and then went to your classroom. "
            pause 2.0
            jump tphysicsclass1
    label octhurslibrary4:
        # koa and matte
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked into the library and spotted two of your classmates doing their own things. "
        " Who do you want to talk to? "
        if koaknow == True and matteknow == True:
            menu:
                " {image=koaicon} Koa {image=koaicon} ":
                    jump helnalblad
                " {image=matteicon} Matte {image=matteicon} ":
                    jump macara
        elif koaknow == True and matteknow == False:
            menu:
                " {image=koaicon} Koa {image=koaicon} ":
                    jump helnalblad
                " {image=matteicon} An artsy girl {image=matteicon} ":
                    jump macara
        elif koaknow == False and matteknow == True:
            menu:
                " {image=koaicon} An emo looking guy {image=koaicon} ":
                    jump helnalblad
                " {image=matteicon} Matte {image=matteicon} ":
                    jump macara
        else:
            menu:
                " {image=koaicon} An emo looking guy {image=koaicon} ":
                    jump helnalblad
                " {image=matteicon} An artsy girl {image=matteicon} ":
                    jump macara
        label helnalblad:
            show koaneutral at center with easeinright
            if koaknow == True:
                " You walked over to him and asked him what he was reading. "
                " You took a bit of a closer look, and noticed that he was reading... "
                " ...A romance book? "
                " This guy most certainly doesn't look like the type to read romance. "
                " But, guess you can't judge a book by it's cover now, can we? "
                k " ...Just reading one of those popular romance books. "
                k " Orchid showed me a video about it, and I decided to give it a read. "
                k " I can kind of see why it's going popular... "
                k " It's got a good plot, good characters... "
                k " Pretty solid for me, in all honesty. "
                k " I'm even starting to get a tad bit invested in this. "
                k " You'd think this would kind of be a 'read then never read again' type of thing, but... "
                k " ...It's just really good, alright? "
                k " I wonder if Orchid is also into the story... "
                k " I could talk about the characters for hours. "
                k " I don't usually get this interested in stories like these, but... "
                k " This one's an exception. "
                k " Hmmm... "
                k " Hey, while you're here... "
                k " You perhaps want to read with me? "
                k " It's always fine if you don't want to, of course. "
                k " I can't just force you to read something with me. "
                k " I'm...not the type of person who would do that. "
                " Would you like to read a book with Koa? "
                menu:
                    " GIMME THAT SWEET JUICY DRAMA ":
                        $ koalv += 10
                        k " ...Heh... "
                        k " There {i}is{/i} some drama here and there. "
                        k " I mean, it's a romance book... "
                        k " Of course there's gonna be some drama. "
                        k " ...Actually, now that I think about it... "
                        k " Every book contains some sort of drama. "
                        k " Even just a little bit. "
                        k " Now, I'll go ahead and start at the first page of the book for you. "
                        scene black with dissolve
                        " You spent the rest of the break reading the book with Koa. "
                        " And oh boy, that drama? it was GOOD. "
                        " Best thing I've ever seen, in all honesty. "
                        " No wonder why this thing is so popular. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the library and went to your classroom after a bit. "
                        pause 2.0
                        jump tphysicsclass1
                    " nah romance isn't really my thing ":
                        k " Oh? that's fine. "
                        k " You can go ahead and read this other book I picked out. "
                        k " I picked this one out incase if I didn't like this one. "
                        k " It's horror - something you probably...or not...like. "
                        " Let's just say you were fine with horror and immediately started reading it. "
                        k " ...Huh. "
                        k " Guess you do like horror... "
                        scene black with dissolve
                        " You spent the rest of the break reading books with Koa. "
                        " You read the book you had, Koa read the book he had. "
                        " You and Koa would talk every noe and then, but other than that, it was pretty quiet. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the library and went to your classroom after a bit. "
                        pause 2.0
                        jump tphysicsclass1
            else:
                " You walked over to him and asked him what he was reading. "
                " You took a bit of a closer look, and noticed that he was reading... "
                " ...A romance book? "
                " This guy most certainly doesn't look like the type to read romance. "
                " But, guess you can't judge a book by it's cover now, can we? "
                x " ...Just reading one of those popular romance books. "
                $ koaknow = True
                k " Uh...I'm Koa, by the way. "
                k " My friend Orchid showed me a video about the book I'm reading, and I decided to check it out. "
                k " I can kind of see why it's going popular... "
                k " It's got a good plot, good characters... "
                k " Pretty solid for me, in all honesty. "
                k " I'm even starting to get a tad bit invested in this. "
                k " You'd think this would kind of be a 'read then never read again' type of thing, but... "
                k " ...It's just really good, alright? "
                k " I wonder if Orchid is also into the story... "
                k " I could talk about the characters for hours. "
                k " I don't usually get this interested in stories like these, but... "
                k " This one's an exception. "
                k " Hmmm... "
                k " Hey, while you're here... "
                k " You perhaps want to read with me? "
                k " It's always fine if you don't want to, of course. "
                k " I can't just force you to read something with me. "
                k " I'm...not the type of person who would do that. "
                " Would you like to read a book with Koa? "
                menu:
                    " GIMME THAT SWEET JUICY DRAMA ":
                        $ koalv += 10
                        k " ...Heh... "
                        k " There {i}is{/i} some drama here and there. "
                        k " I mean, it's a romance book... "
                        k " Of course there's gonna be some drama. "
                        k " ...Actually, now that I think about it... "
                        k " Every book contains some sort of drama. "
                        k " Even just a little bit. "
                        k " Now, I'll go ahead and start at the first page of the book for you. "
                        scene black with dissolve
                        " You spent the rest of the break reading the book with Koa. "
                        " And oh boy, that drama? it was GOOD. "
                        " Best thing I've ever seen, in all honesty. "
                        " No wonder why this thing is so popular. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the library and went to your classroom after a bit. "
                        pause 2.0
                        jump tphysicsclass1
                    " nah romance isn't really my thing ":
                        k " Oh? that's fine. "
                        k " You can go ahead and read this other book I picked out. "
                        k " I picked this one out incase if I didn't like this one. "
                        k " It's horror - something you probably...or not...like. "
                        " Let's just say you were fine with horror and immediately started reading it. "
                        k " ...Huh. "
                        k " Guess you do like horror... "
                        scene black with dissolve
                        " You spent the rest of the break reading books with Koa. "
                        " You read the book you had, Koa read the book he had. "
                        " You and Koa would talk every noe and then, but other than that, it was pretty quiet. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the library and went to your classroom after a bit. "
                        pause 2.0
                        jump tphysicsclass1
        label macara:
            show matteneutral at center with easeinleft
            if matteknow == True:
                ma " Hello there, [name]! "
                ma " So I kind of had this really great idea... "
                hide matteneutral at bottom
                show mattehappy at center
                ma " You know, there's been this book that's been going trending lately, right? "
                ma " I decided to check it out yesterday and oh my heavens. "
                ma " It was REALLY good! "
                ma " I can tell why a lot of people loved it! "
                ma " Great characters, great storyline...! "
                ma " Aaaah...I could reread this book for days...!! "
                hide mattehappy at bottom
                show matteneutral at center
                ma " I decided that I wanted to show some appreciation for the book... "
                ma " And you know how I loooove art? "
                ma " I think you know what I might be getting at! "
                ma " I really wanna make art for the book! "
                ma " But the only problem is that I don't know how the characters look... "
                ma " Hmmm... "
                ma " I could just maybe look at some of the designs on TikTok? "
                ma " They've got a whole lot of those! "
                ma " I just need to credit the designers for the designs! "
                ma " Of course we've gotta credit them... "
                ma " Otherwise I'm gonna get jumped by the comments. "
                ma " I don't want to be a design stealer, after all! "
                ma " Hmmm...since my data ran out... "
                ma " Could you go and help me for a bit? "
                ma " I need you to search up some designs for me... "
                ma " And I'll tell you if one is good or not! "
                " Well, you don't really have a choice here. "
                " You grabbed your phone and started looking for inspirations for Matte... "
                scene black with dissolve
                " You spent the rest of the break helping Matte with her artwork. "
                " The good thing about this is that you saw Matte's amazing art coming together. "
                " She told you she was just gonna paint it at home though. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the library and went to your classroom after a bit. "
                pause 2.0
                jump tphysicsclass1
            else:
                x " Hello there, [name]! "
                $ matteknow = True
                ma " Oh ! uh... I'm Matte, by the way. Nice to meet you! "
                ma " So I kind of had this really great idea... "
                hide matteneutral at bottom
                show mattehappy at center
                ma " You know, there's been this book that's been going trending lately, right? "
                ma " I decided to check it out yesterday and oh my heavens. "
                ma " It was REALLY good! "
                ma " I can tell why a lot of people loved it! "
                ma " Great characters, great storyline...! "
                ma " Aaaah...I could reread this book for days...!! "
                hide mattehappy at bottom
                show matteneutral at center
                ma " I decided that I wanted to show some appreciation for the book... "
                ma " And you know how I loooove art? "
                ma " I think you know what I might be getting at! "
                ma " I really wanna make art for the book! "
                ma " But the only problem is that I don't know how the characters look... "
                ma " Hmmm... "
                ma " I could just maybe look at some of the designs on TikTok? "
                ma " They've got a whole lot of those! "
                ma " I just need to credit the designers for the designs! "
                ma " Of course we've gotta credit them... "
                ma " Otherwise I'm gonna get jumped by the comments. "
                ma " I don't want to be a design stealer, after all! "
                ma " Hmmm...since my data ran out... "
                ma " Could you go and help me for a bit? "
                ma " I need you to search up some designs for me... "
                ma " And I'll tell you if one is good or not! "
                " Well, you don't really have a choice here. "
                " You grabbed your phone and started looking for inspirations for Matte... "
                scene black with dissolve
                " You spent the rest of the break helping Matte with her artwork. "
                " The good thing about this is that you saw Matte's amazing art coming together. "
                " She told you she was just gonna paint it at home though. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the library and went to your classroom after a bit. "
                pause 2.0
                jump tphysicsclass1
label tphysicsclass1:
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    " You looked around the classroom and saw some writing on the board. "
    " Reading it, it looks like the physics teacher left a note there. "
    " Let's see what it says... "
    " Looks like the teacher isn't really here due to some issues. "
    " The teacher wants everyone to make a marble roller coaster. "
    " You need to make a video of yourself doing the activity... "
    " Then, after you're done, you send it to the physics teacher herself. "
    " Sounds easy enough. "
    " You could just get the materials you need from the cafeteria. "
    " This school IS an advanced school, after all. "
    " You could just buy stuff from there anytime. "
    " You should probably do the activity now though, so that you won't have to worry tomorrow. "
    " You walked over to the cafeteria to get your materials... "
    scene black with dissolve
    " You spent the rest of class hours making the activity for physics class. "
    " After you were done setting things up, you recorded the video... "
    " And with your mobile data, you sent the video to Miss Lua. "
    " You basically had the entire period to play games on your phone, so that's what you did. "
    play sound "audio/bellring.mp3"
    " The bell rings after a little bit, looks like it's time for a break. "
    " You walked out of the classroom after a good bit. "
    pause 2.0
    jump octhursbreak5
label octhursbreak5:
    scene hallway with dissolve
    " Where would you like to hangout for this break? "
    menu:
        " {image=noxicon} The front of the school {image=quinnicon} ":
            jump octhursfront5
        " {image=diskicon} The back of the school {image=koaicon} ":
            jump octhursback5
        " {image=orchidicon} The gym {image=temeroicon} ":
            jump octhursgym5
        " {image=matteicon} The cafeteria {image=jamicon} ":
            jump octhurscafeteria5
        " {image=sparkicon} The rooftop {image=yinyangicon} ":
            jump octhursrooftop5
        " {image=jacobicon} The library {image=carmenicon} ":
            jump octhurslibrary5
    label octhursfront5:
        # nox and quinn
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked to the front of the school and found two of your classmates doing their own thing. "
        " Who would you like to talk to? "
        if noxknow == True and quinnknow == True:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump overurhead
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump underyonose
        elif noxknow == True and quinnknow == False:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump overurhead
                " {image=quinnicon} A guy that looks like hes into theater {image=quinnicon} ":
                    jump underyonose
        elif noxknow == False and quinnknow == True:
            menu:
                " {image=noxicon} A sleepy guy {image=noxicon} ":
                    jump overurhead
                " {image=quinnicon} Quinn {image=quinnicon} ":
                    jump underyonose
        else:
            menu:
                " {image=noxicon} A sleepy guy {image=noxicon} ":
                    jump overurhead
                " {image=quinnicon} A guy that looks like hes into theater {image=quinnicon} ":
                    jump underyonose
        label overurhead:
            show noxneutral at center with easeinleft
            if noxknow == True:
                " You walked over to him and asked what he was doing. "
                n " Mmm...? "
                n " Oh, [name]... "
                n " I was just looking at the clouds... "
                n " I can't wait to go back to my bed, honestly... "
                n " Um... "
                n " ...Do you ever just... "
                n " ...Wake up for school so early, but you go back to sleep...? "
                n " Then when you wake up again, turns out you're almost late... "
                n " So you have to go and put everything on quickly... "
                n " ...That has happened to me multiple times, actually.. "
                n " I don't like it whenever it happens... "
                n " I just want to go to sleep for a long time, not go to school... "
                n " Infact, the first day I got here... "
                n " I slept in classes a lot... "
                n " They thought that it would just go away after a week, but... "
                n " That's when they actually started getting concerned - after I kept doing it... "
                n " I told them my parents wouldn't really give me meds... "
                n " My parents thought that I was kind of overreacting... "
                n " And the teachers, specifically Mister Altrix convinced them to get me meds... "
                n " I started taking the meds, buuut... "
                n " Most of the time, I would forget to take them... "
                n " Sooo...Mister Altrix kind of reminds me every now and then... "
                n " He's kind of like... "
                n " My...personal alarm clock...? no, that's not right... "
                n " I think you get the idea of what I'm trying to say.. "
                n " He's not annoying though...he's really nice... "
                n " A nice alarm clock... "
                n " Hmhmm... "
                " Nox looks like he's daydreaming a bit. "
                " Wonder what he's daydreaming about... "
                " You can't help but daydream about things, too. "
                scene black with dissolve
                " You spent the rest of the break daydreaming with Nox. "
                " Just...thinking about random things. Like sleeping. "
                " Nox told you he was just thinking of getting some desserts right before going to sleep. "
                " Damn...that honestly sounds pretty nice. "
                " Wish you could get some desserts before sleep. "
                " Though that would probably make you stay up more. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your final class. "
                " You stopped daydreaming, and walked back into the school and went to your classroom. "
                pause 2.0
                jump tcookingclass1
            else:
                " You walked over to him and asked what he was doing. "
                x " Mmm...? "
                x " Oh, [name]... "
                x " I was just looking at the clouds... "
                $ noxknow = True
                n " ...'m Nox, by the way...Nox Cesso... "
                n " I can't wait to go back to my bed, honestly... "
                n " Um... "
                n " ...Do you ever just... "
                n " ...Wake up for school so early, but you go back to sleep...? "
                n " Then when you wake up again, turns out you're almost late... "
                n " So you have to go and put everything on quickly... "
                n " ...That has happened to me multiple times, actually.. "
                n " I don't like it whenever it happens... "
                n " I just want to go to sleep for a long time, not go to school... "
                n " Infact, the first day I got here... "
                n " I slept in classes a lot... "
                n " They thought that it would just go away after a week, but... "
                n " That's when they actually started getting concerned - after I kept doing it... "
                n " I told them my parents wouldn't really give me meds... "
                n " My parents thought that I was kind of overreacting... "
                n " And the teachers, specifically Mister Altrix convinced them to get me meds... "
                n " I started taking the meds, buuut... "
                n " Most of the time, I would forget to take them... "
                n " Sooo...Mister Altrix kind of reminds me every now and then... "
                n " He's kind of like... "
                n " My...personal alarm clock...? no, that's not right... "
                n " I think you get the idea of what I'm trying to say.. "
                n " He's not annoying though...he's really nice... "
                n " A nice alarm clock... "
                n " Hmhmm... "
                " Nox looks like he's daydreaming a bit. "
                " Wonder what he's daydreaming about... "
                " You can't help but daydream about things, too. "
                scene black with dissolve
                " You spent the rest of the break daydreaming with Nox. "
                " Just...thinking about random things. Like sleeping. "
                " Nox told you he was just thinking of getting some desserts right before going to sleep. "
                " Damn...that honestly sounds pretty nice. "
                " Wish you could get some desserts before sleep. "
                " Though that would probably make you stay up more. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for your final class. "
                " You stopped daydreaming, and walked back into the school and went to your classroom. "
                pause 2.0
                jump tcookingclass1
        label underyonose:
            show quinnneutral at center with easeinright
            if quinnknow == True:
                " You walked over to him and asked him what he was doing. "
                q " Oh, [name]!! "
                q " It's quite lovely to see you at this hour. "
                q " I was just thinking about stuff I could do for my play... "
                q " Like extra props, since things are looking a little too bland. "
                q " But then again... "
                q " Even the blandest of things can make everything feel fully decorated. "
                q " Hmhmmm... "
                q " I was also just getting a break before I get back to practice. "
                q " The teachers said I can stay for practice, until 6 pm - 7 pm only though. "
                q " They don't want me to stay for too long, after all. "
                q " And I completely understand that! "
                q " Though I kind of feel like I need to practice a little more... "
                q " Due to the fact that the play is going to be tomorrow. "
                q " But - I also feel like I'm going to do great! "
                q " I've managed to practice enough, and I think that's fine! "
                q " I don't really need to overwork myself too much. "
                q " Otherwise...everything would just start crashing down. "
                hide quinnneutral at bottom
                show quinnsad at center
                q " I remember overworking myself for a play too much once. "
                q " This was way before you came here, of course. "
                q " I wanted everything to be so perfectly so badly... "
                q " I started practicing even when I'm at home - not letting myself rest. "
                q " Even Disk was starting to get concerned over me. "
                q " Always telling me to rest...but I never listened. "
                q " I just wanted everything to be so good that it can impress the entire town. "
                q " Maybe even the entire country - with the mindset that I had back then. "
                q " So when the day of the play came... "
                q " Everything was fine for the most part. "
                q " But, when I came up to do my part... "
                q " In the middle of doing my lines, I fainted. "
                q " I tried going on before that - but...I collapsed. "
                q " God - that has to be the most embarrassing thing that's ever happened to me. "
                q " I woke up in the clinic of the school and I tried going back to the theater club room, but of course... "
                q " They wouldn't let me. "
                q " I felt really horrible that day, you know? "
                q " All that hard work, just went down the drain. "
                q " So much for making everything perfect. "
                menu:
                    " You don't have to be perfect around me ":
                        $ quinnlv += 10
                        hide quinnsad at bottom
                        show quinnneutral at center
                        q " ...You're way too kind to be saying that. "
                        q " Thanks, but... "
                        q " I've got to be perfect for the audience, no? "
                        q " An audience won't like a bad show. "
                        q " I don't want tomatoes being thrown at me after all, haha. "
                        q " But, uh... "
                        q " Very sorry for ruining the mood, [name]. "
                        q " I'm sure you wanted to talk about something happier. "
                        q " Let's talk about something else, alright? "
                        q " Hm...like... "
                        q " How your day is going so far? "
                        q " It's bland, but it's a classic. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Whilst you were talking with him, you could'nt help but be concerned for him. "
                        " Concerned about the fact that he wanted everything to be perfect. "
                        " It looked like he didn't want to talk more about it though, so... "
                        " You just kept the conversation going without mentioning anything like that. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked back into the school and went into your classroom. "
                        pause 2.0
                        jump tcookingclass1
                    " *dont say anything* ":
                        hide quinnsad at bottom
                        show quinnneutral at center
                        q " Ah, but I'm just rambling again. "
                        q " Very sorry for ruining the mood, [name]. "
                        q " I'm sure you wanted to talk about something happier. "
                        q " Let's talk about something else, alright? "
                        q " Hm...like... "
                        q " How your day is going so far? "
                        q " It's bland, but it's a classic. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Whilst you were talking with him, you could'nt help but be concerned for him. "
                        " Concerned about the fact that he wanted everything to be perfect. "
                        " It looked like he didn't want to talk more about it though, so... "
                        " You just kept the conversation going without mentioning anything like that. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked back into the school and went into your classroom. "
                        pause 2.0
                        jump tcookingclass1
            else:
                " You walked over to him and asked him what he was doing. "
                x " Oh, [name]!! "
                x " It's quite lovely to see you at this hour. "
                $ quinnknow = True
                q " I'm Quinn, by the way! part of the drama club. "
                q " I was just thinking about stuff I could do for my play... "
                q " Like extra props, since things are looking a little too bland. "
                q " But then again... "
                q " Even the blandest of things can make everything feel fully decorated. "
                q " Hmhmmm... "
                q " I was also just getting a break before I get back to practice. "
                q " The teachers said I can stay for practice, until 6 pm - 7 pm only though. "
                q " They don't want me to stay for too long, after all. "
                q " And I completely understand that! "
                q " Though I kind of feel like I need to practice a little more... "
                q " Due to the fact that the play is going to be tomorrow. "
                q " But - I also feel like I'm going to do great! "
                q " I've managed to practice enough, and I think that's fine! "
                q " I don't really need to overwork myself too much. "
                q " Otherwise...everything would just start crashing down. "
                hide quinnneutral at bottom
                show quinnsad at center
                q " I remember overworking myself for a play too much once. "
                q " This was way before you came here, of course. "
                q " I wanted everything to be so perfectly so badly... "
                q " I started practicing even when I'm at home - not letting myself rest. "
                q " Even Disk was starting to get concerned over me. "
                q " Always telling me to rest...but I never listened. "
                q " I just wanted everything to be so good that it can impress the entire town. "
                q " Maybe even the entire country - with the mindset that I had back then. "
                q " So when the day of the play came... "
                q " Everything was fine for the most part. "
                q " But, when I came up to do my part... "
                q " In the middle of doing my lines, I fainted. "
                q " I tried going on before that - but...I collapsed. "
                q " God - that has to be the most embarrassing thing that's ever happened to me. "
                q " I woke up in the clinic of the school and I tried going back to the theater club room, but of course... "
                q " They wouldn't let me. "
                q " I felt really horrible that day, you know? "
                q " All that hard work, just went down the drain. "
                q " So much for making everything perfect. "
                menu:
                    " You don't have to be perfect around me ":
                        $ quinnlv += 10
                        hide quinnsad at bottom
                        show quinnneutral at center
                        q " ...You're way too kind to be saying that. "
                        q " Thanks, but... "
                        q " I've got to be perfect for the audience, no? "
                        q " An audience won't like a bad show. "
                        q " I don't want tomatoes being thrown at me after all, haha. "
                        q " But, uh... "
                        q " Very sorry for ruining the mood, [name]. "
                        q " I'm sure you wanted to talk about something happier. "
                        q " Let's talk about something else, alright? "
                        q " Hm...like... "
                        q " How your day is going so far? "
                        q " It's bland, but it's a classic. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Whilst you were talking with him, you could'nt help but be concerned for him. "
                        " Concerned about the fact that he wanted everything to be perfect. "
                        " It looked like he didn't want to talk more about it though, so... "
                        " You just kept the conversation going without mentioning anything like that. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked back into the school and went into your classroom. "
                        pause 2.0
                        jump tcookingclass1
                    " *dont say anything* ":
                        hide quinnsad at bottom
                        show quinnneutral at center
                        q " Ah, but I'm just rambling again. "
                        q " Very sorry for ruining the mood, [name]. "
                        q " I'm sure you wanted to talk about something happier. "
                        q " Let's talk about something else, alright? "
                        q " Hm...like... "
                        q " How your day is going so far? "
                        q " It's bland, but it's a classic. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Quinn. "
                        " Whilst you were talking with him, you could'nt help but be concerned for him. "
                        " Concerned about the fact that he wanted everything to be perfect. "
                        " It looked like he didn't want to talk more about it though, so... "
                        " You just kept the conversation going without mentioning anything like that. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked back into the school and went into your classroom. "
                        pause 2.0
                        jump tcookingclass1
    label octhursback5:
        # disk and koa
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walked to the back of the school and saw two of your classmates talking to eachother. "
        " Wondering what they're talking about, you decided to join in their conversation. "
        show diskneutral at right with easeinleft
        show koaneutral at left with easeinleft
        if diskknow == True and koaknow == True:
            k " ...Look, [name]'s here. "
            d " Oh! [they] [are]? "
            hide diskneutral at bottom
            show diskhappy at right
            d " Hi there [name]!! "
            d " It's so, so nice to see you! "
            d " Can you guys believe it's going to be friday tomorrow? "
            hide diskhappy at bottom
            show diskneutral at center
            k " Yeah, I sure can believe it. "
            k " ...And that also means that's going to be the day of your party, if I remember correctly...? "
            d " Yup yup! "
            d " Geez, time flies by so fast... "
            d " Like - one day it's a monday, and then the next it's a friday! "
            d " Makes me think that we should atleast slow down a little. "
            k " ...That's true, but we can't exactly change that. "
            hide diskneutral at bottom
            show disksad at right
            d " I knooooww... "
            d " The only times where the days feel long is classes, in all honesty. "
            d " And whenever we have something fun to do... "
            d " It always ends so quickly!! "
            d " I don't really like things happening so fast like that... "
            hide koaneutral at bottom
            show koaneutralb2 at left
            k " Well...that's why we've got to learn to savor the small moments. "
            k " Have fun, be at your best... "
            k " Because in the next second - all of that fun is gone. "
            k " Make the small moments count in your life. "
            k " Even if it's a tiny moment, just make sure you're enjoying yourself. "
            k " Enjoying yourself before the moment passes. "
            k " Then, you can look back at your life and think of that one moment... "
            k " Remembering how fun it was fondly, instead of it being a sad thought. "
            hide disksad at bottom
            show diskjoyous at right
            d " ...I think I know the reason why Orchid keeps coming up to your for advice now! "
            hide koaneutralb2 at bottom
            show koasurprised at left
            k " ...Am I really that good at advice? "
            k " I mean, I'm just saying what I think in my head. "
            k " It's really nothing special. "
            d " Oh, come on!! "
            d " You're really good at advice! "
            d " In fact, you're so good - "
            hide koasurprised at bottom
            show koaneutral at left
            k " (Annnnd he's rambling again.) "
            k " (I'm going to have to sit here for a long time, aren't I?) "
            k " (Not that I mind though.) "
            k " (Being complimented like this...feels nice.) "
            k " (Hopefully [name] can handle the rambling though.) "
            " Yeah, you sure can. "
            " If you can handle watching long gameplay videos, then you can handle this. "
            " No big deal, really. "
            " Unless if you're someone with a short attention span. "
            scene black with dissolve
            " You spent the rest of the break listening to Disk yap. "
            " It was just a barrage of compliments towards Koa... "
            " Honestly you wished you could get complimented like that sometime. "
            " Koa eventually told Disk to stop, politely. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for your final class of the day. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump tcookingclass1
        elif diskknow == True and koaknow == False:
            x " ...Look, [name]'s here. "
            d " Oh! [they] [are]? "
            hide diskneutral at bottom
            show diskhappy at right
            d " Hi there [name]!! "
            d " It's so, so nice to see you! "
            $ koaknow = True
            d " This is my buddy Koa, by the way! "
            k " ...Hi. "
            d " Can you guys believe it's going to be friday tomorrow? "
            hide diskhappy at bottom
            show diskneutral at center
            k " Yeah, I sure can believe it. "
            k " ...And that also means that's going to be the day of your party, if I remember correctly...? "
            d " Yup yup! "
            d " Geez, time flies by so fast... "
            d " Like - one day it's a monday, and then the next it's a friday! "
            d " Makes me think that we should atleast slow down a little. "
            k " ...That's true, but we can't exactly change that. "
            hide diskneutral at bottom
            show disksad at right
            d " I knooooww... "
            d " The only times where the days feel long is classes, in all honesty. "
            d " And whenever we have something fun to do... "
            d " It always ends so quickly!! "
            d " I don't really like things happening so fast like that... "
            hide koaneutral at bottom
            show koaneutralb2 at left
            k " Well...that's why we've got to learn to savor the small moments. "
            k " Have fun, be at your best... "
            k " Because in the next second - all of that fun is gone. "
            k " Make the small moments count in your life. "
            k " Even if it's a tiny moment, just make sure you're enjoying yourself. "
            k " Enjoying yourself before the moment passes. "
            k " Then, you can look back at your life and think of that one moment... "
            k " Remembering how fun it was fondly, instead of it being a sad thought. "
            hide disksad at bottom
            show diskjoyous at right
            d " ...I think I know the reason why Orchid keeps coming up to your for advice now! "
            hide koaneutralb2 at bottom
            show koasurprised at left
            k " ...Am I really that good at advice? "
            k " I mean, I'm just saying what I think in my head. "
            k " It's really nothing special. "
            d " Oh, come on!! "
            d " You're really good at advice! "
            d " In fact, you're so good - "
            hide koasurprised at bottom
            show koaneutral at left
            k " (Annnnd he's rambling again.) "
            k " (I'm going to have to sit here for a long time, aren't I?) "
            k " (Not that I mind though.) "
            k " (Being complimented like this...feels nice.) "
            k " (Hopefully [name] can handle the rambling though.) "
            " Yeah, you sure can. "
            " If you can handle watching long gameplay videos, then you can handle this. "
            " No big deal, really. "
            " Unless if you're someone with a short attention span. "
            scene black with dissolve
            " You spent the rest of the break listening to Disk yap. "
            " It was just a barrage of compliments towards Koa... "
            " Honestly you wished you could get complimented like that sometime. "
            " Koa eventually told Disk to stop, politely. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for your final class of the day. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump tcookingclass1
        elif diskknow == False and koaknow == True:
            k " ...Look, [name]'s here. "
            x " Oh! [they] [are]? "
            hide diskneutral at bottom
            show diskhappy at right
            x " Hi there [name]!! "
            x " It's so, so nice to see you! "
            x " Wait, I don't think I've introduced myself to you before! "
            $ diskknow = True
            d " I'm Disk! It's really nice to meet you! "
            d " Can you guys believe it's going to be friday tomorrow? "
            hide diskhappy at bottom
            show diskneutral at center
            k " Yeah, I sure can believe it. "
            k " ...And that also means that's going to be the day of your party, if I remember correctly...? "
            d " Yup yup! "
            d " Geez, time flies by so fast... "
            d " Like - one day it's a monday, and then the next it's a friday! "
            d " Makes me think that we should atleast slow down a little. "
            k " ...That's true, but we can't exactly change that. "
            hide diskneutral at bottom
            show disksad at right
            d " I knooooww... "
            d " The only times where the days feel long is classes, in all honesty. "
            d " And whenever we have something fun to do... "
            d " It always ends so quickly!! "
            d " I don't really like things happening so fast like that... "
            hide koaneutral at bottom
            show koaneutralb2 at left
            k " Well...that's why we've got to learn to savor the small moments. "
            k " Have fun, be at your best... "
            k " Because in the next second - all of that fun is gone. "
            k " Make the small moments count in your life. "
            k " Even if it's a tiny moment, just make sure you're enjoying yourself. "
            k " Enjoying yourself before the moment passes. "
            k " Then, you can look back at your life and think of that one moment... "
            k " Remembering how fun it was fondly, instead of it being a sad thought. "
            hide disksad at bottom
            show diskjoyous at right
            d " ...I think I know the reason why Orchid keeps coming up to your for advice now! "
            hide koaneutralb2 at bottom
            show koasurprised at left
            k " ...Am I really that good at advice? "
            k " I mean, I'm just saying what I think in my head. "
            k " It's really nothing special. "
            d " Oh, come on!! "
            d " You're really good at advice! "
            d " In fact, you're so good - "
            hide koasurprised at bottom
            show koaneutral at left
            k " (Annnnd he's rambling again.) "
            k " (I'm going to have to sit here for a long time, aren't I?) "
            k " (Not that I mind though.) "
            k " (Being complimented like this...feels nice.) "
            k " (Hopefully [name] can handle the rambling though.) "
            " Yeah, you sure can. "
            " If you can handle watching long gameplay videos, then you can handle this. "
            " No big deal, really. "
            " Unless if you're someone with a short attention span. "
            scene black with dissolve
            " You spent the rest of the break listening to Disk yap. "
            " It was just a barrage of compliments towards Koa... "
            " Honestly you wished you could get complimented like that sometime. "
            " Koa eventually told Disk to stop, politely. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for your final class of the day. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump tcookingclass1
        else:
            x " ...Look, [name]'s here. "
            x " Oh! [they] [are]? "
            hide diskneutral at bottom
            show diskhappy at right
            x " Hi there [name]!! "
            x " It's so, so nice to see you! "
            x " Wait, I don't think I've introduced myself to you before! "
            $ diskknow = True
            d " I'm Disk! It's really nice to meet you! "
            $ koaknow = True
            d " This is my buddy Koa, by the way! "
            k " ...Hi. "
            d " Can you guys believe it's going to be friday tomorrow? "
            hide diskhappy at bottom
            show diskneutral at center
            k " Yeah, I sure can believe it. "
            k " ...And that also means that's going to be the day of your party, if I remember correctly...? "
            d " Yup yup! "
            d " Geez, time flies by so fast... "
            d " Like - one day it's a monday, and then the next it's a friday! "
            d " Makes me think that we should atleast slow down a little. "
            k " ...That's true, but we can't exactly change that. "
            hide diskneutral at bottom
            show disksad at right
            d " I knooooww... "
            d " The only times where the days feel long is classes, in all honesty. "
            d " And whenever we have something fun to do... "
            d " It always ends so quickly!! "
            d " I don't really like things happening so fast like that... "
            hide koaneutral at bottom
            show koaneutralb2 at left
            k " Well...that's why we've got to learn to savor the small moments. "
            k " Have fun, be at your best... "
            k " Because in the next second - all of that fun is gone. "
            k " Make the small moments count in your life. "
            k " Even if it's a tiny moment, just make sure you're enjoying yourself. "
            k " Enjoying yourself before the moment passes. "
            k " Then, you can look back at your life and think of that one moment... "
            k " Remembering how fun it was fondly, instead of it being a sad thought. "
            hide disksad at bottom
            show diskjoyous at right
            d " ...I think I know the reason why Orchid keeps coming up to your for advice now! "
            hide koaneutralb2 at bottom
            show koasurprised at left
            k " ...Am I really that good at advice? "
            k " I mean, I'm just saying what I think in my head. "
            k " It's really nothing special. "
            d " Oh, come on!! "
            d " You're really good at advice! "
            d " In fact, you're so good - "
            hide koasurprised at bottom
            show koaneutral at left
            k " (Annnnd he's rambling again.) "
            k " (I'm going to have to sit here for a long time, aren't I?) "
            k " (Not that I mind though.) "
            k " (Being complimented like this...feels nice.) "
            k " (Hopefully [name] can handle the rambling though.) "
            " Yeah, you sure can. "
            " If you can handle watching long gameplay videos, then you can handle this. "
            " No big deal, really. "
            " Unless if you're someone with a short attention span. "
            scene black with dissolve
            " You spent the rest of the break listening to Disk yap. "
            " It was just a barrage of compliments towards Koa... "
            " Honestly you wished you could get complimented like that sometime. "
            " Koa eventually told Disk to stop, politely. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for your final class of the day. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump tcookingclass1
    label octhursgym5:
        # orchid and temero
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You walked to the gym and spotted two of your classmates doing their own things. "
        " Who should you talk to for this break? "
        if orchidknow == True and temeroknow == True:
            menu:
                " {image=orchidicon} Orchid {image=orchidicon} ":
                    jump whattheflippitygiggity
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump whatthefloppitygoggity
        elif orchidknow == True and temeroknow == False:
            menu:
                " {image=orchidicon} Orchid {image=orchidicon} ":
                    jump whattheflippitygiggity
                " {image=temeroicon} A scientist looking girl {image=temeroicon} ":
                    jump whatthefloppitygoggity
        elif orchidknow == False and temeroknow == True:
            menu:
                " {image=orchidicon} A scene kid {image=orchidicon} ":
                    jump whattheflippitygiggity
                " {image=temeroicon} Temero {image=temeroicon} ":
                    jump whatthefloppitygoggity
        else:
            menu:
                " {image=orchidicon} A scene kid {image=orchidicon} ":
                    jump whattheflippitygiggity
                " {image=temeroicon} A scientist looking girl {image=temeroicon} ":
                    jump whatthefloppitygoggity
        label whattheflippitygiggity:
            show orchidneutral at center with easeinleft
            if orchidknow == True:
                " You walked over to him and asked him what he was doing. "
                oc " Huh? oh, hey there [name]! "
                oc " Sorry if I seem a litttleeee bit too energetic... "
                hide orchidneutral at bottom
                show orchidhappy at center
                oc " But it's because I'm planning on doing something for my new friends! "
                oc " Have you noticed I've been talking to a lot of people now? "
                hide orchidhappy at bottom
                show orchidsad at center
                oc " Well...it's not really a big thing that you should notice, but... "
                oc " I think you know how I kind of look like the shy kid in class. "
                oc " I never really talked to anyone, you know? "
                oc " But, after a bit... "
                oc " After Koa started giving me more and more advice... "
                oc " I actually started to listen to them... "
                hide orchidsad at bottom
                show orchidneutral at center
                oc " And look at where I am now! "
                oc " I'm starting to become happier... "
                oc " Becoming more talkative... "
                oc " Eating more.. "
                hide orchidneutral at bottom
                show orchidhappy at center
                oc " Hell - even the negative thoughts I usually get aren't as bad than before! "
                oc " I don't know how to thank Koa for all of this... "
                oc " I don't know how to thank everyone for actually hanging out with me now. "
                oc " That's why I'm planning on taking them to a pool party next week! "
                hide orchidhappy at bottom
                show orchidneutral at center
                oc " Next week saturday, of course. "
                oc " I'm gonna have to invite the entire class - and yes, that means you! "
                oc " I know Koa probably wouldn't agree, but I'm just going to drag him to the pool. "
                oc " Like - come on man, you helped a lot with me! "
                if orchidlv >= 25 or orchidlv == 25:
                    oc " And I'm not going to leave you out either. "
                    oc " You mean a lot to me, you know? "
                    oc " You were there for me and listened to me. "
                    oc " I don't think I can ever say that you never helped me. "
                    oc " You listened to me when I was at my lowest, and I... "
                    oc " I thank you for listening. "
                    oc " People who listen to me actually make me feel better - believe it or not. "
                    oc " I'm DEFINITELY spoiling you on saturday! "
                    oc " Whether you like it or not! "
                else:
                    oc " That guy never learns to treat himself, really... "
                    oc " I think it's because of the situation he's in. "
                    oc " That doesn't mean that I won't help him though! "
                    oc " If he's helped me, then I'll help him! "
                    oc " That's what friends are for, right? "
                    oc " I'm not leaving him behind like that. "
                    oc " Even if he thinks he doesn't deserve all the nice things. "
                oc " Heheh...sorry if I rambled too much there, [name]. "
                oc " I just feel really happy nowadays, you know? "
                oc " Can't help but be proud of myself. "
                menu:
                    " I'm glad that you're feeling better ":
                        $ orchidlv += 10
                        hide orchidneutral at bottom
                        show orchidhappy at center
                        oc " I'm glad that I'm feeling better now, too! "
                        oc " The days used to be so dull and boring... "
                        oc " But honestly? nowadays... "
                        hide orchidhappy at bottom
                        show orchidneutral at center
                        oc " It feels like I'm back to being a kid again. "
                        oc " Everything's bright - everything's fun... "
                        oc " I know that everything isn't sunshine and rainbows, but... "
                        oc " I have to hold on and enjoy the moments where it feels like everything's going to be okay. "
                        oc " I know that everything's going to be okay in the end. "
                        oc " Even though things might not look like it sometimes. "
                        oc " It's just another day that's going to pass. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Orchid. "
                        " It was nice seeing him being happy like this... "
                        " This was probably the happiest he's ever been. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " Well, your final one for the day. "
                        " You walked out of the gym and went to your classroom. "
                        pause 2.0
                        jump tcookingclass1
                    " yeah!! ":
                        hide orchidneutral at bottom
                        show orchidhappy at center
                        oc " Yeah!! "
                        oc " The days used to be so dull and boring... "
                        oc " But honestly? nowadays... "
                        hide orchidhappy at bottom
                        show orchidneutral at center
                        oc " It feels like I'm back to being a kid again. "
                        oc " Everything's bright - everything's fun... "
                        oc " I know that everything isn't sunshine and rainbows, but... "
                        oc " I have to hold on and enjoy the moments where it feels like everything's going to be okay. "
                        oc " I know that everything's going to be okay in the end. "
                        oc " Even though things might not look like it sometimes. "
                        oc " It's just another day that's going to pass. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Orchid. "
                        " It was nice seeing him being happy like this... "
                        " This was probably the happiest he's ever been. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " Well, your final one for the day. "
                        " You walked out of the gym and went to your classroom. "
                        pause 2.0
                        jump tcookingclass1
            else:
                " You walked over to him and asked him what he was doing. "
                x " Huh? oh, hey there [name]! "
                x " I don't think I've introduced myself to you before, actually... "
                $ orchidknow = True
                oc " I'm Orchid! It's really nice to meet you!! "
                oc " Oh, uh...we're classmates, by the way. "
                oc " Sorry if I seem a litttleeee bit too energetic... "
                hide orchidneutral at bottom
                show orchidhappy at center
                oc " But it's because I'm planning on doing something for my new friends! "
                oc " Have you noticed I've been talking to a lot of people now? "
                hide orchidhappy at bottom
                show orchidsad at center
                oc " Well...it's not really a big thing that you should notice, but... "
                oc " I think you know how I kind of look like the shy kid in class. "
                oc " I never really talked to anyone, you know? "
                oc " But, after a bit... "
                oc " After Koa started giving me more and more advice... "
                oc " I actually started to listen to them... "
                hide orchidsad at bottom
                show orchidneutral at center
                oc " And look at where I am now! "
                oc " I'm starting to become happier... "
                oc " Becoming more talkative... "
                oc " Eating more.. "
                hide orchidneutral at bottom
                show orchidhappy at center
                oc " Hell - even the negative thoughts I usually get aren't as bad than before! "
                oc " I don't know how to thank Koa for all of this... "
                oc " I don't know how to thank everyone for actually hanging out with me now. "
                oc " That's why I'm planning on taking them to a pool party next week! "
                hide orchidhappy at bottom
                show orchidneutral at center
                oc " Next week saturday, of course. "
                oc " I'm gonna have to invite the entire class - and yes, that means you! "
                oc " I know Koa probably wouldn't agree, but I'm just going to drag him to the pool. "
                oc " Like - come on man, you helped a lot with me! "
                if orchidlv >= 25 or orchidlv == 25:
                    oc " And I'm not going to leave you out either. "
                    oc " You mean a lot to me, you know? "
                    oc " You were there for me and listened to me. "
                    oc " I don't think I can ever say that you never helped me. "
                    oc " You listened to me when I was at my lowest, and I... "
                    oc " I thank you for listening. "
                    oc " People who listen to me actually make me feel better - believe it or not. "
                    oc " I'm DEFINITELY spoiling you on saturday! "
                    oc " Whether you like it or not! "
                else:
                    oc " That guy never learns to treat himself, really... "
                    oc " I think it's because of the situation he's in. "
                    oc " That doesn't mean that I won't help him though! "
                    oc " If he's helped me, then I'll help him! "
                    oc " That's what friends are for, right? "
                    oc " I'm not leaving him behind like that. "
                    oc " Even if he thinks he doesn't deserve all the nice things. "
                oc " Heheh...sorry if I rambled too much there, [name]. "
                oc " I just feel really happy nowadays, you know? "
                oc " Can't help but be proud of myself. "
                menu:
                    " I'm glad that you're feeling better ":
                        $ orchidlv += 10
                        hide orchidneutral at bottom
                        show orchidhappy at center
                        oc " I'm glad that I'm feeling better now, too! "
                        oc " The days used to be so dull and boring... "
                        oc " But honestly? nowadays... "
                        hide orchidhappy at bottom
                        show orchidneutral at center
                        oc " It feels like I'm back to being a kid again. "
                        oc " Everything's bright - everything's fun... "
                        oc " I know that everything isn't sunshine and rainbows, but... "
                        oc " I have to hold on and enjoy the moments where it feels like everything's going to be okay. "
                        oc " I know that everything's going to be okay in the end. "
                        oc " Even though things might not look like it sometimes. "
                        oc " It's just another day that's going to pass. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Orchid. "
                        " It was nice seeing him being happy like this... "
                        " This was probably the happiest he's ever been. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " Well, your final one for the day. "
                        " You walked out of the gym and went to your classroom. "
                        pause 2.0
                        jump tcookingclass1
                    " yeah!! ":
                        hide orchidneutral at bottom
                        show orchidhappy at center
                        oc " Yeah!! "
                        oc " The days used to be so dull and boring... "
                        oc " But honestly? nowadays... "
                        hide orchidhappy at bottom
                        show orchidneutral at center
                        oc " It feels like I'm back to being a kid again. "
                        oc " Everything's bright - everything's fun... "
                        oc " I know that everything isn't sunshine and rainbows, but... "
                        oc " I have to hold on and enjoy the moments where it feels like everything's going to be okay. "
                        oc " I know that everything's going to be okay in the end. "
                        oc " Even though things might not look like it sometimes. "
                        oc " It's just another day that's going to pass. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Orchid. "
                        " It was nice seeing him being happy like this... "
                        " This was probably the happiest he's ever been. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " Well, your final one for the day. "
                        " You walked out of the gym and went to your classroom. "
                        pause 2.0
                        jump tcookingclass1
        label whatthefloppitygoggity:
            show temeroneutral at center with easeinright
            if temeroknow == True:
                " You walked over to her and asked what she was doing. "
                tm " Uh? someone's talking to me? "
                tm " Hold on, I just gotta... "
                tm " Finish this up... "
                " She finishes something up that you couldn't see. "
                " Looks like she didn't want you to see whatever she was doing. "
                " Most likely just keeping it as a surprise. "
                tm " Heelllooo - oh! "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " It's you! "
                tm " You came to watch another one of my experiments, huh? "
                tm " I know you've been eyeing my doing my experiments. "
                tm " Don't lie to me, now! "
                tm " I always saw you take a glance at what I'm doing. "
                tm " And I KNOW you must be really impressed! "
                tm " Sooo...you actually came to watch me do another one of them! "
                tm " I'll gladly show you what I'm working with this time. "
                hide temerohappy at bottom
                show temeroneutral at center
                " She pulls something from behind her, and it looked like a normal pink butterfly. "
                tm " Looks like a normal butterfly, right? "
                tm " Well you're about to be amazed! "
                tm " Just give it a moment for it to work, alright? "
                tm " This needs just a little bit of time. "
                " You wait for something to happen... "
                " ...Strangely, the butterfly converts into a burger. "
                " Huh. Okay now you're actually confused on how that works. "
                " I'm even confused myself. "
                hide temeroneutral at bottom
                show temerowhenzip at center
                tm " Tadaaa!! "
                tm " It looks like a burger, and it also tastes like one! "
                tm " I actually don't know how I managed to do this. "
                tm " I just mixed random things and...this happened. "
                tm " I've actually tried the burger and it tasted good! "
                hide temerowhenzip at bottom
                show temeroneutral at center
                tm " You want a bite? "
                menu:
                    " yeah even though ts is probably poisonous ":
                        $ temerolv += 10
                        tm " Alright, here you go! "
                        tm " Tell me if it tastes good, alright? "
                        tm " I'm gonna have to do something if it doesn't, haha. "
                        " You took the burger from Temero's hands... "
                        " You stare at it a bit before reluctantly taking a bite into it. "
                        " And honestly? it tastes REALLY good! "
                        " You just hoped this wasn't drugged or something. "
                        " You gave her the thumbs up of approval and continued eating the burger. "
                        hide temeroneutral at bottom
                        show temerohappy at center
                        tm " Woah, so it DOES taste good! "
                        tm " Hmm...if it does taste that good, then... "
                        tm " Maybe I could make a business out of this? "
                        tm " Hmhmmm...money. "
                        tm " Thanks for giving me your opinion, [name]! "
                        tm " I can make more if you want - anytime. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Temero. "
                        " Okay, now I want a burger. "
                        " I can't exactly just go down there and ask for one, though... "
                        " I might just have to steal one while she isn't looking. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, looks like it's time for another class. "
                        " Your final one for the day, actually. "
                        " You walked out of the gym and then went to your classroom. "
                        pause 2.0
                        jump tcookingclass1
                    " nah im not hungry ":
                        tm " More for me, then! "
                        tm " Though...this is technically eating one of my butterflies. "
                        tm " Atleast I can just clone more, right? "
                        tm " Hehe...if you didn't know - I clone my butterflies. "
                        tm " Basically taking a real one and cloning them to be experiment material... "
                        tm " Then letting the real butterfly go. "
                        tm " Pretty easy process, if you ask me. "
                        " She then takes a bite of the butterfly burger. "
                        " Great, now you're hungry for burgers. "
                        " But you don't wanna eat that one. "
                        " It kinda irks you that this thing used to be a butterfly. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Temero. "
                        " You were still hungry, but you'd rather not eat a butterfly. "
                        " You wanted some real food. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, looks like it's time for another class. "
                        " Your final one for the day, actually. "
                        " You walked out of the gym and then went to your classroom. "
                        pause 2.0
                        jump tcookingclass1
            else:
                " You walked over to her and asked what she was doing. "
                x " Uh? someone's talking to me? "
                x " Hold on, I just gotta... "
                x " Finish this up... "
                " She finishes something up that you couldn't see. "
                " Looks like she didn't want you to see whatever she was doing. "
                " Most likely just keeping it as a surprise. "
                x " Heelllooo - oh! "
                hide temeroneutral at bottom
                show temerohappy at center
                x " It's you! "
                x " Hold on, you've probably never met me before. "
                x " It would be rude if I didn't introduce myself! "
                $ temeroknow = True
                tm " I'm the GREAT Temero NEO! (call me Temero, or Neo. I don't mind either.) "
                tm " I'm your classmate - annnnnd... "
                tm " You came to watch another one of my experiments, huh? "
                tm " I know you've been eyeing my doing my experiments. "
                tm " Don't lie to me, now! "
                tm " I always saw you take a glance at what I'm doing. "
                tm " And I KNOW you must be really impressed! "
                tm " Sooo...you actually came to watch me do another one of them! "
                tm " I'll gladly show you what I'm working with this time. "
                hide temerohappy at bottom
                show temeroneutral at center
                " She pulls something from behind her, and it looked like a normal pink butterfly. "
                tm " Looks like a normal butterfly, right? "
                tm " Well you're about to be amazed! "
                tm " Just give it a moment for it to work, alright? "
                tm " This needs just a little bit of time. "
                " You wait for something to happen... "
                " ...Strangely, the butterfly converts into a burger. "
                " Huh. Okay now you're actually confused on how that works. "
                " I'm even confused myself. "
                hide temeroneutral at bottom
                show temerowhenzip at center
                tm " Tadaaa!! "
                tm " It looks like a burger, and it also tastes like one! "
                tm " I actually don't know how I managed to do this. "
                tm " I just mixed random things and...this happened. "
                tm " I've actually tried the burger and it tasted good! "
                hide temerowhenzip at bottom
                show temeroneutral at center
                tm " You want a bite? "
                menu:
                    " yeah even though ts is probably poisonous ":
                        $ temerolv += 10
                        tm " Alright, here you go! "
                        tm " Tell me if it tastes good, alright? "
                        tm " I'm gonna have to do something if it doesn't, haha. "
                        " You took the burger from Temero's hands... "
                        " You stare at it a bit before reluctantly taking a bite into it. "
                        " And honestly? it tastes REALLY good! "
                        " You just hoped this wasn't drugged or something. "
                        " You gave her the thumbs up of approval and continued eating the burger. "
                        hide temeroneutral at bottom
                        show temerohappy at center
                        tm " Woah, so it DOES taste good! "
                        tm " Hmm...if it does taste that good, then... "
                        tm " Maybe I could make a business out of this? "
                        tm " Hmhmmm...money. "
                        tm " Thanks for giving me your opinion, [name]! "
                        tm " I can make more if you want - anytime. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Temero. "
                        " Okay, now I want a burger. "
                        " I can't exactly just go down there and ask for one, though... "
                        " I might just have to steal one while she isn't looking. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, looks like it's time for another class. "
                        " Your final one for the day, actually. "
                        " You walked out of the gym and then went to your classroom. "
                        pause 2.0
                        jump tcookingclass1
                    " nah im not hungry ":
                        tm " More for me, then! "
                        tm " Though...this is technically eating one of my butterflies. "
                        tm " Atleast I can just clone more, right? "
                        tm " Hehe...if you didn't know - I clone my butterflies. "
                        tm " Basically taking a real one and cloning them to be experiment material... "
                        tm " Then letting the real butterfly go. "
                        tm " Pretty easy process, if you ask me. "
                        " She then takes a bite of the butterfly burger. "
                        " Great, now you're hungry for burgers. "
                        " But you don't wanna eat that one. "
                        " It kinda irks you that this thing used to be a butterfly. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Temero. "
                        " You were still hungry, but you'd rather not eat a butterfly. "
                        " You wanted some real food. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, looks like it's time for another class. "
                        " Your final one for the day, actually. "
                        " You walked out of the gym and then went to your classroom. "
                        pause 2.0
                        jump tcookingclass1
    label octhurscafeteria5:
        # jam and matte
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walked into the cafeteria and spotted two of your classmates talking with eachother. "
        " Wondering what they're talking about, you decided to walk over to them. "
        show matteneutral at right with easeinleft
        show jamneutral at left with easeinleft
        if matteknow == True and jamknow == True:
            " You walked over to them and asked them what they were doing. "
            ma " Oh, [name]! come and sit with us! "
            ja " ...Yeah, just sit next to me. "
            " You sat down next to her politely. "
            ma " Me and my friend Jam over here were just talking about a few things... "
            ma " Talking about my next masterpiece, of course! "
            ma " Since me and Jam are so close - I wanted to make a painting about us! "
            ma " A painting that shows our friendship... "
            hide jamneutral at bottom
            show jamsad at left
            ja " ...Yeah. Friendship. "
            hide matteneutral at bottom
            show mattesad at right
            ma " You okay there, Jam? "
            ma " You sound a little...sad. "
            ma " Or you sound like you're lost in your thoughts. "
            ja " Uh...yeah - I was just thinking about a few things. "
            ja " Don't worry about it too much. "
            hide jamsad at bottom
            show jamneutral at center
            ma " Okay, if you say so... "
            hide mattesad at bottom
            show matteneutral at right
            ma " Anyway! as I was saying...new painting, right? "
            ma " I'm planning on making it my biggest one yet! "
            ma " Though...not sure if I'm gonna have enough motivation to do that. "
            ma " I'm sure I can do it though! "
            ma " I've done big paintings before - I can do it again! "
            ma " I just gotta make sure I don't accidentally burn myself out. "
            ma " I remember doing that once... "
            ma " Whew. That did NOT go well. "
            ja " ... "
            ja " Hey, Matte? "
            ma " Hm? what is it, Jam? "
            ja " Just... "
            ja " Remember not to overwork yourself too much, okay? "
            ja " You know that it gets me worried. "
            ja " Only do things and continue projects if you really want to. "
            ja " You don't have to force yourself to finish it if you're tired. "
            ja " You need to remember you need rest sometimes. "
            hide matteneutral at bottom
            show mattehappy at right
            ma " Awww, Jam...!! "
            ma " Of course I'll remember to take breaks. "
            ma " Rest is important for an artist, after all! "
            ma " You care about me so much, hmmhmm... "
            hide jamneutral at bottom
            show jamhappy at left
            ja " ...I'm just making sure you're going to be okay. "
            ma " Hehe, you're cute. "
            ja " ... "
            scene black with dissolve
            " You spent the rest of the break talking with Jam and Matte. "
            " They kind of gave the vibe of those school couples... "
            " Except I know that they're going to be more doomed. "
            " You'd know that if you talked to Jam more. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for your final class of the day. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump tcookingclass1
        elif matteknow == True and jamknow == False:
            " You walked over to them and asked them what they were doing. "
            ma " Oh, [name]! come and sit with us! "
            x " ...Yeah, just sit next to me. "
            " You sat down next to her politely. "
            $ jamknow = True
            ma " Me and my friend Jam over here were just talking about a few things... "
            ma " Talking about my next masterpiece, of course! "
            ma " Since me and Jam are so close - I wanted to make a painting about us! "
            ma " A painting that shows our friendship... "
            hide jamneutral at bottom
            show jamsad at left
            ja " ...Yeah. Friendship. "
            hide matteneutral at bottom
            show mattesad at right
            ma " You okay there, Jam? "
            ma " You sound a little...sad. "
            ma " Or you sound like you're lost in your thoughts. "
            ja " Uh...yeah - I was just thinking about a few things. "
            ja " Don't worry about it too much. "
            hide jamsad at bottom
            show jamneutral at center
            ma " Okay, if you say so... "
            hide mattesad at bottom
            show matteneutral at right
            ma " Anyway! as I was saying...new painting, right? "
            ma " I'm planning on making it my biggest one yet! "
            ma " Though...not sure if I'm gonna have enough motivation to do that. "
            ma " I'm sure I can do it though! "
            ma " I've done big paintings before - I can do it again! "
            ma " I just gotta make sure I don't accidentally burn myself out. "
            ma " I remember doing that once... "
            ma " Whew. That did NOT go well. "
            ja " ... "
            ja " Hey, Matte? "
            ma " Hm? what is it, Jam? "
            ja " Just... "
            ja " Remember not to overwork yourself too much, okay? "
            ja " You know that it gets me worried. "
            ja " Only do things and continue projects if you really want to. "
            ja " You don't have to force yourself to finish it if you're tired. "
            ja " You need to remember you need rest sometimes. "
            hide matteneutral at bottom
            show mattehappy at right
            ma " Awww, Jam...!! "
            ma " Of course I'll remember to take breaks. "
            ma " Rest is important for an artist, after all! "
            ma " You care about me so much, hmmhmm... "
            hide jamneutral at bottom
            show jamhappy at left
            ja " ...I'm just making sure you're going to be okay. "
            ma " Hehe, you're cute. "
            ja " ... "
            scene black with dissolve
            " You spent the rest of the break talking with Jam and Matte. "
            " They kind of gave the vibe of those school couples... "
            " Except I know that they're going to be more doomed. "
            " You'd know that if you talked to Jam more. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for your final class of the day. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump tcookingclass1
        elif matteknow == False and jamknow == True:
            " You walked over to them and asked them what they were doing. "
            x " Oh, [name]! come and sit with us! "
            ja " ...Yeah, just sit next to me. "
            " You sat down next to her politely. "
            x " I don't think we've met before, so... "
            $ matteknow = True
            ma " I'm Matte! It's really nice to meet you! "
            ma " Me and my friend Jam over here were just talking about a few things... "
            ma " Talking about my next masterpiece, of course! "
            ma " Since me and Jam are so close - I wanted to make a painting about us! "
            ma " A painting that shows our friendship... "
            hide jamneutral at bottom
            show jamsad at left
            ja " ...Yeah. Friendship. "
            hide matteneutral at bottom
            show mattesad at right
            ma " You okay there, Jam? "
            ma " You sound a little...sad. "
            ma " Or you sound like you're lost in your thoughts. "
            ja " Uh...yeah - I was just thinking about a few things. "
            ja " Don't worry about it too much. "
            hide jamsad at bottom
            show jamneutral at center
            ma " Okay, if you say so... "
            hide mattesad at bottom
            show matteneutral at right
            ma " Anyway! as I was saying...new painting, right? "
            ma " I'm planning on making it my biggest one yet! "
            ma " Though...not sure if I'm gonna have enough motivation to do that. "
            ma " I'm sure I can do it though! "
            ma " I've done big paintings before - I can do it again! "
            ma " I just gotta make sure I don't accidentally burn myself out. "
            ma " I remember doing that once... "
            ma " Whew. That did NOT go well. "
            ja " ... "
            ja " Hey, Matte? "
            ma " Hm? what is it, Jam? "
            ja " Just... "
            ja " Remember not to overwork yourself too much, okay? "
            ja " You know that it gets me worried. "
            ja " Only do things and continue projects if you really want to. "
            ja " You don't have to force yourself to finish it if you're tired. "
            ja " You need to remember you need rest sometimes. "
            hide matteneutral at bottom
            show mattehappy at right
            ma " Awww, Jam...!! "
            ma " Of course I'll remember to take breaks. "
            ma " Rest is important for an artist, after all! "
            ma " You care about me so much, hmmhmm... "
            hide jamneutral at bottom
            show jamhappy at left
            ja " ...I'm just making sure you're going to be okay. "
            ma " Hehe, you're cute. "
            ja " ... "
            scene black with dissolve
            " You spent the rest of the break talking with Jam and Matte. "
            " They kind of gave the vibe of those school couples... "
            " Except I know that they're going to be more doomed. "
            " You'd know that if you talked to Jam more. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for your final class of the day. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump tcookingclass1
        else:
            " You walked over to them and asked them what they were doing. "
            x " Oh, [name]! come and sit with us! "
            x " ...Yeah, just sit next to me. "
            " You sat down next to her politely. "
            x " I don't think we've met before, so... "
            $ matteknow = True
            $ jamknow = True
            ma " I'm Matte! It's really nice to meet you! "
            ma " Me and my friend Jam over here were just talking about a few things... "
            ma " Talking about my next masterpiece, of course! "
            ma " Since me and Jam are so close - I wanted to make a painting about us! "
            ma " A painting that shows our friendship... "
            hide jamneutral at bottom
            show jamsad at left
            ja " ...Yeah. Friendship. "
            hide matteneutral at bottom
            show mattesad at right
            ma " You okay there, Jam? "
            ma " You sound a little...sad. "
            ma " Or you sound like you're lost in your thoughts. "
            ja " Uh...yeah - I was just thinking about a few things. "
            ja " Don't worry about it too much. "
            hide jamsad at bottom
            show jamneutral at center
            ma " Okay, if you say so... "
            hide mattesad at bottom
            show matteneutral at right
            ma " Anyway! as I was saying...new painting, right? "
            ma " I'm planning on making it my biggest one yet! "
            ma " Though...not sure if I'm gonna have enough motivation to do that. "
            ma " I'm sure I can do it though! "
            ma " I've done big paintings before - I can do it again! "
            ma " I just gotta make sure I don't accidentally burn myself out. "
            ma " I remember doing that once... "
            ma " Whew. That did NOT go well. "
            ja " ... "
            ja " Hey, Matte? "
            ma " Hm? what is it, Jam? "
            ja " Just... "
            ja " Remember not to overwork yourself too much, okay? "
            ja " You know that it gets me worried. "
            ja " Only do things and continue projects if you really want to. "
            ja " You don't have to force yourself to finish it if you're tired. "
            ja " You need to remember you need rest sometimes. "
            hide matteneutral at bottom
            show mattehappy at right
            ma " Awww, Jam...!! "
            ma " Of course I'll remember to take breaks. "
            ma " Rest is important for an artist, after all! "
            ma " You care about me so much, hmmhmm... "
            hide jamneutral at bottom
            show jamhappy at left
            ja " ...I'm just making sure you're going to be okay. "
            ma " Hehe, you're cute. "
            ja " ... "
            scene black with dissolve
            " You spent the rest of the break talking with Jam and Matte. "
            " They kind of gave the vibe of those school couples... "
            " Except I know that they're going to be more doomed. "
            " You'd know that if you talked to Jam more. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for your final class of the day. "
            " You walked out of the cafeteria and went to your classroom. "
            pause 2.0
            jump tcookingclass1
    label octhursrooftop5:
        # spark and yinhui
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked over to the rooftop and spotted two of your classmates doing their own things. "
        " Who do you talk to for this break? "
        if sparkknow == True and yinhuiknow == True:
            menu:
                " {image=sparkicon} Spark {image=sparkicon} ":
                    jump yonaem
                " {image=yinyangicon} Yinhui {image=yinyangicon} ":
                    jump yoaeg
        elif sparkknow == True and yinhuiknow == False:
            menu:
                " {image=sparkicon} Spark {image=sparkicon} ":
                    jump yonaem
                " {image=yinyangicon} A mean looking guy {image=yinyangicon} ":
                    jump yoaeg
        elif sparkknow == False and yinhuiknow == True:
            menu:
                " {image=sparkicon} A guy with antennas and a tail {image=sparkicon} ":
                    jump yonaem
                " {image=yinyangicon} Yinhui {image=yinyangicon} ":
                    jump yoaeg
        else:
            menu:
                " {image=sparkicon} A guy with antennas and a tail {image=sparkicon} ":
                    jump yonaem
                " {image=yinyangicon} A mean looking guy {image=yinyangicon} ":
                    jump yoaeg
        label yonaem:
            show sparkneutral at center with easeinright
            if sparkknow == True:
                " You walked over to him and asked him what he was doing. "
                " He didn't respond though... "
                " You took a closer look and turns out he had his earphones on. "
                " You felt like messing with him just a bit... "
                " So you pulled on his tail just a little bit. "
                hide sparkneutral at bottom
                show sparkshit at center
                sp " Ow! what the - hey?! "
                sp " Why'd you do that...?? "
                hide sparkshit at bottom
                show sparkneutral at center
                sp " ...Sigh. Okay... "
                sp " I know that you probably want to talk to me. "
                sp " But, you can't pull on my tail to get my attention. "
                sp " That hurts a little, you know? "
                sp " I know that you probably didn't mean it, but still... "
                sp " Hoping that you remember to not touch my tail in the future. "
                sp " (Eugh, I sound like those cringy people from 2018...) "
                sp " (Those roleplayers, specifically.) "
                sp " (But I have to say it so that [they] won't do it again.) "
                sp " (It also reminds me of what {i}he{/i} did to me back then...) "
                sp " (God those days at that school was fun.) "
                sp " (Wish I could visit him sometime...) "
                sp " ...Ahem. "
                sp " I heard Temero's been working on something new. "
                sp " Said she started making these things called...butterfly burgers. "
                sp " Told me that she could somehow turn a butterfly into a burger. "
                sp " I didn't believe it because I didn't see it yet, of course. "
                sp " But...when she showed me - holy moly. "
                sp " She basically just turned one of her butterflies into burgers... hence the name. "
                sp " And the thing is??? "
                sp " It actually tastes like a burger. "
                sp " I don't even know how she manages to do this stuff. "
                sp " I could definitely use some more burgers from her though.. "
                sp " You should check them out sometime. "
                sp " Not sure if you'd like it, but I'm just reccomending. "
                sp " Not gonna force you to eat it or anything. "
                sp " Despite it tasting really good, I don't want to shove it down someones throat. "
                sp " I'm just not that kind of person, you know? "
                scene black with dissolve
                " You spent the rest of thebreak talking with Spark. "
                " At the mention of burgers, you started feeling a bit hungry... "
                " Even I'm starting to get hungry over here, woah. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your final class of the day. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump tcookingclass1
            else:
                " You walked over to him and asked him what he was doing. "
                " He didn't respond though... "
                " You took a closer look and turns out he had his earphones on. "
                " You felt like messing with him just a bit... "
                " So you pulled on his tail just a little bit. "
                hide sparkneutral at bottom
                show sparkshit at center
                x " Ow! what the - hey?! "
                x " Why'd you do that...?? "
                hide sparkshit at bottom
                show sparkneutral at center
                x " ...Sigh. Okay... "
                x " I know that you probably want to talk to me. "
                x " But, you can't pull on my tail to get my attention. "
                x " That hurts a little, you know? "
                x " I know that you probably didn't mean it, but still... "
                x " Hoping that you remember to not touch my tail in the future. "
                x " (Eugh, I sound like those cringy people from 2018...) "
                x " (Those roleplayers, specifically.) "
                x " (But I have to say it so that [they] won't do it again.) "
                x " (It also reminds me of what {i}he{/i} did to me back then...) "
                x " (God those days at that school was fun.) "
                x " (Wish I could visit him sometime...) "
                x " ...Ahem. "
                $ sparkknow = True
                sp " I'm Spark, by the way. And uh... "
                sp " I heard Temero's been working on something new. "
                sp " Said she started making these things called...butterfly burgers. "
                sp " Told me that she could somehow turn a butterfly into a burger. "
                sp " I didn't believe it because I didn't see it yet, of course. "
                sp " But...when she showed me - holy moly. "
                sp " She basically just turned one of her butterflies into burgers... hence the name. "
                sp " And the thing is??? "
                sp " It actually tastes like a burger. "
                sp " I don't even know how she manages to do this stuff. "
                sp " I could definitely use some more burgers from her though.. "
                sp " You should check them out sometime. "
                sp " Not sure if you'd like it, but I'm just reccomending. "
                sp " Not gonna force you to eat it or anything. "
                sp " Despite it tasting really good, I don't want to shove it down someones throat. "
                sp " I'm just not that kind of person, you know? "
                scene black with dissolve
                " You spent the rest of thebreak talking with Spark. "
                " At the mention of burgers, you started feeling a bit hungry... "
                " Even I'm starting to get hungry over here, woah. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your final class of the day. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump tcookingclass1
        label yoaeg:
            show yinhuineutral at center with easeinleft
            if yinhuiknow == True:
                " You walked over to him and asked what he was doing. "
                yi " ...You. "
                yi " I was just thinking about...a few things. "
                yi " Like a few things for cooking class. "
                yi " Wondering what mom has for next class.. "
                yi " I'm sure she talked about having no activities for today. "
                yi " But then again...she could be trolling. "
                yi " She sometimes does that, by the way. "
                yi " That's why we have to prepare all the time. "
                yi " It's a little bit frustrating, yes... "
                yi " But she's my mom. And I can't really complain about that to her. "
                yi " Otherwise, I think she's going to give me the silent treatment for awhile. "
                yi " I don't really want that, in all honesty. "
                yi " Her giving me the silent treatment is basically the equivalent of 'you're going to be tonights dinner'. "
                yi " And I don't want to become like my dad. "
                hide yinhuineutral at bottom
                show yinhuisurprised at center
                yi " ...? "
                yi " (Great, did I really just say that?) "
                yi " (Good going, Yinhui.) "
                yi " (Yangyi and mom told you not to say anything like that.) "
                yi " (Just...gotta play as if I didn't say anything.) "
                yi " (It's a dumb solution, but it's the only thing I can do.) "
                yi " (I don't want [them] to dig too deep into this.) "
                hide yinhuisurprised at bottom
                show yinhuineutral at center
                " You asked him about what he just said. "
                " What did he mean when he said that he didn't want to become like his dad? "
                " That's odd. Really odd. "
                yi " Huh? "
                yi " What do you mean? "
                yi " I didn't say anything. "
                yi " You must be hearing things. "
                hide yinhuineutral at bottom
                show yinhuiheh at center
                yi " Though I wouldn't be surprised if you were hearing things. "
                yi " You're a weirdo, of course you'd be thinking like that. "
                yi " Heheh... "
                yi " Don't take that in the wrong way, by the way. "
                yi " I'm just messing with you, of course. "
                yi " I don't actually mean it. "
                yi " If I did, then I'm pretty sure Yangyi wouldn't be too proud of me. "
                hide yinhuiheh at bottom
                show yinhuineutral at center
                yi " But truly, I didn't say anything. "
                yi " Maybe you need to get your ears checked by Mister Altrix. "
                yi " Not only is he a good teacher - he's a good nurse, too. "
                yi " He can help you with anything. "
                scene black with dissolve
                " You spent the rest of the break talking with Yinhui. "
                " As you were talking, you couldn't help but think about what he said... "
                " What did he mean when he didn't want to be like his dad? "
                " ...Maybe you shouldn't think about this too much. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump tcookingclass1
            else:
                " You walked over to him and asked what he was doing. "
                x " ...You. "
                x " I don't think I've introduced myself before, so... "
                $ yinhuiknow = True
                yi " I'm Yinhui. It's nice to meet you. "
                yi " I was just thinking about...a few things. "
                yi " Like a few things for cooking class. "
                yi " Wondering what mom has for next class.. "
                yi " I'm sure she talked about having no activities for today. "
                yi " But then again...she could be trolling. "
                yi " She sometimes does that, by the way. "
                yi " That's why we have to prepare all the time. "
                yi " It's a little bit frustrating, yes... "
                yi " But she's my mom. And I can't really complain about that to her. "
                yi " Otherwise, I think she's going to give me the silent treatment for awhile. "
                yi " I don't really want that, in all honesty. "
                yi " Her giving me the silent treatment is basically the equivalent of 'you're going to be tonights dinner'. "
                yi " And I don't want to become like my dad. "
                hide yinhuineutral at bottom
                show yinhuisurprised at center
                yi " ...? "
                yi " (Great, did I really just say that?) "
                yi " (Good going, Yinhui.) "
                yi " (Yangyi and mom told you not to say anything like that.) "
                yi " (Just...gotta play as if I didn't say anything.) "
                yi " (It's a dumb solution, but it's the only thing I can do.) "
                yi " (I don't want [them] to dig too deep into this.) "
                hide yinhuisurprised at bottom
                show yinhuineutral at center
                " You asked him about what he just said. "
                " What did he mean when he said that he didn't want to become like his dad? "
                " That's odd. Really odd. "
                yi " Huh? "
                yi " What do you mean? "
                yi " I didn't say anything. "
                yi " You must be hearing things. "
                hide yinhuineutral at bottom
                show yinhuiheh at center
                yi " Though I wouldn't be surprised if you were hearing things. "
                yi " You're a weirdo, of course you'd be thinking like that. "
                yi " Heheh... "
                yi " Don't take that in the wrong way, by the way. "
                yi " I'm just messing with you, of course. "
                yi " I don't actually mean it. "
                yi " If I did, then I'm pretty sure Yangyi wouldn't be too proud of me. "
                hide yinhuiheh at bottom
                show yinhuineutral at center
                yi " But truly, I didn't say anything. "
                yi " Maybe you need to get your ears checked by Mister Altrix. "
                yi " Not only is he a good teacher - he's a good nurse, too. "
                yi " He can help you with anything. "
                scene black with dissolve
                " You spent the rest of the break talking with Yinhui. "
                " As you were talking, you couldn't help but think about what he said... "
                " What did he mean when he didn't want to be like his dad? "
                " ...Maybe you shouldn't think about this too much. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump tcookingclass1
    label octhurslibrary5:
        # jacob and carmen
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked into the library and spotted two of your classmates talking to eachother. "
        " Wondering what they're talking about, you decided to walk over to them. "
        show jacobneutral at left with easeinright
        show carmenneutral at right with easeinright
        if jacobknow == True and carmenknow == True:
            " You walked over to them and asked them what they were doing. "
            jac " Oh, hey there [name]. "
            jac " I'm kind of helping Carmen over here right now. "
            jac " I thought it would be a funny idea to shove some book pages into his guitar... "
            jac " But now we can't really get it out. "
            jac " Oopsies. "
            ca " ... "
            " Carmen just looks really done with Jacob. "
            " Why exactly did he think this was a good idea? "
            jac " Look - I thought it would be funny, okay?! "
            jac " I already apologized to you!! "
            ca " ... "
            " Carmen stares at him before he gives him some signs... "
            " Signs about Jacob being the one to get the pages out. "
            " I mean...it was pretty fair. "
            " He was the one who did the thing in the first place. "
            " You considered helping if Jacob struggled too much. "
            jac " Alright, alright... "
            jac " Fine - I'll get the pages out of your guitar. "
            jac " Just gimme it. "
            " Carmen hands him over the guitar and sits down on a chair. "
            " He looks like he's ready to see him struggle... "
            " And honestly, you were, too. "
            " Let's see how badly he struggles with this. "
            jac " This should be pretty easy. "
            jac " Just let me...do this... "
            " He starts trying to get the paper, but he can't seem to get it. "
            hide jacobneutral at bottom
            show jacobangry at left
            jac " Ugh, come on now... "
            jac " This shouldn't be that hard... "
            jac " This is probably the easiest thing to do... "
            jac " I can't be fumbling this bad. "
            " He keeps trying and trying... "
            " But he kept on failing. "
            " You honestly felt a little bad that he was struggling. "
            " Should you help him? "
            " Carmen looks like he doesn't want you to help him though. "
            menu:
                " Help Jacob ":
                    $ jacoblv += 10
                    hide jacobangry at bottom
                    show jacobneutral at left
                    jac " ...Huh? you're actually helping me? "
                    jac " ...Alright, thanks. "
                    jac " Here, so you can get the pages easier. "
                    " Jacob tilts the guitar a bit so you could get the pages easier. "
                    " And then you started helping him out... "
                    scene black with dissolve
                    " You spent the rest of the break helping Jacob. "
                    " Eventually, he does get the pages out. "
                    " Carmen still gave him a bonk on the head for messing with his guitar though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the library and went to your classroom. "
                    pause 2.0
                    jump tcookingclass1
                " Just watch with Carmen ":
                    $ carmenlv += 10
                    ca " ... "
                    " You sat down next to Carmen and just watched Jacob struggle. "
                    " I mean, he DID cause that mess himself. "
                    " You're not gonna help him with that. "
                    " Nuh uh. "
                    " You're just gonna watch. "
                    scene black with dissolve
                    " You spent the rest of the break watching Jacob suffer with Carmen. "
                    " Eventually, he does get the pages out. "
                    " Carmen still gave him a bonk on the head for messing with his guitar though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the library and went to your classroom. "
                    pause 2.0
                    jump tcookingclass1
        elif jacobknow == True and carmenknow == False:
            " You walked over to them and asked them what they were doing. "
            jac " Oh, hey there [name]. "
            $ carmenknow = True
            jac " I'm kind of helping Carmen over here right now. "
            jac " I thought it would be a funny idea to shove some book pages into his guitar... "
            jac " But now we can't really get it out. "
            jac " Oopsies. "
            ca " ... "
            " Carmen just looks really done with Jacob. "
            " Why exactly did he think this was a good idea? "
            jac " Look - I thought it would be funny, okay?! "
            jac " I already apologized to you!! "
            ca " ... "
            " Carmen stares at him before he gives him some signs... "
            " Signs about Jacob being the one to get the pages out. "
            " I mean...it was pretty fair. "
            " He was the one who did the thing in the first place. "
            " You considered helping if Jacob struggled too much. "
            jac " Alright, alright... "
            jac " Fine - I'll get the pages out of your guitar. "
            jac " Just gimme it. "
            " Carmen hands him over the guitar and sits down on a chair. "
            " He looks like he's ready to see him struggle... "
            " And honestly, you were, too. "
            " Let's see how badly he struggles with this. "
            jac " This should be pretty easy. "
            jac " Just let me...do this... "
            " He starts trying to get the paper, but he can't seem to get it. "
            hide jacobneutral at bottom
            show jacobangry at left
            jac " Ugh, come on now... "
            jac " This shouldn't be that hard... "
            jac " This is probably the easiest thing to do... "
            jac " I can't be fumbling this bad. "
            " He keeps trying and trying... "
            " But he kept on failing. "
            " You honestly felt a little bad that he was struggling. "
            " Should you help him? "
            " Carmen looks like he doesn't want you to help him though. "
            menu:
                " Help Jacob ":
                    $ jacoblv += 10
                    hide jacobangry at bottom
                    show jacobneutral at left
                    jac " ...Huh? you're actually helping me? "
                    jac " ...Alright, thanks. "
                    jac " Here, so you can get the pages easier. "
                    " Jacob tilts the guitar a bit so you could get the pages easier. "
                    " And then you started helping him out... "
                    scene black with dissolve
                    " You spent the rest of the break helping Jacob. "
                    " Eventually, he does get the pages out. "
                    " Carmen still gave him a bonk on the head for messing with his guitar though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the library and went to your classroom. "
                    pause 2.0
                    jump tcookingclass1
                " Just watch with Carmen ":
                    $ carmenlv += 10
                    ca " ... "
                    " You sat down next to Carmen and just watched Jacob struggle. "
                    " I mean, he DID cause that mess himself. "
                    " You're not gonna help him with that. "
                    " Nuh uh. "
                    " You're just gonna watch. "
                    scene black with dissolve
                    " You spent the rest of the break watching Jacob suffer with Carmen. "
                    " Eventually, he does get the pages out. "
                    " Carmen still gave him a bonk on the head for messing with his guitar though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the library and went to your classroom. "
                    pause 2.0
                    jump tcookingclass1
        elif jacobknow == False and carmenknow == True:
            " You walked over to them and asked them what they were doing. "
            x " Oh, hey there [name]. "
            $ jacobknow = True
            jac " I'm Jacob, and uh... "
            jac " I'm kind of helping Carmen over here right now. "
            jac " I thought it would be a funny idea to shove some book pages into his guitar... "
            jac " But now we can't really get it out. "
            jac " Oopsies. "
            ca " ... "
            " Carmen just looks really done with Jacob. "
            " Why exactly did he think this was a good idea? "
            jac " Look - I thought it would be funny, okay?! "
            jac " I already apologized to you!! "
            ca " ... "
            " Carmen stares at him before he gives him some signs... "
            " Signs about Jacob being the one to get the pages out. "
            " I mean...it was pretty fair. "
            " He was the one who did the thing in the first place. "
            " You considered helping if Jacob struggled too much. "
            jac " Alright, alright... "
            jac " Fine - I'll get the pages out of your guitar. "
            jac " Just gimme it. "
            " Carmen hands him over the guitar and sits down on a chair. "
            " He looks like he's ready to see him struggle... "
            " And honestly, you were, too. "
            " Let's see how badly he struggles with this. "
            jac " This should be pretty easy. "
            jac " Just let me...do this... "
            " He starts trying to get the paper, but he can't seem to get it. "
            hide jacobneutral at bottom
            show jacobangry at left
            jac " Ugh, come on now... "
            jac " This shouldn't be that hard... "
            jac " This is probably the easiest thing to do... "
            jac " I can't be fumbling this bad. "
            " He keeps trying and trying... "
            " But he kept on failing. "
            " You honestly felt a little bad that he was struggling. "
            " Should you help him? "
            " Carmen looks like he doesn't want you to help him though. "
            menu:
                " Help Jacob ":
                    $ jacoblv += 10
                    hide jacobangry at bottom
                    show jacobneutral at left
                    jac " ...Huh? you're actually helping me? "
                    jac " ...Alright, thanks. "
                    jac " Here, so you can get the pages easier. "
                    " Jacob tilts the guitar a bit so you could get the pages easier. "
                    " And then you started helping him out... "
                    scene black with dissolve
                    " You spent the rest of the break helping Jacob. "
                    " Eventually, he does get the pages out. "
                    " Carmen still gave him a bonk on the head for messing with his guitar though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the library and went to your classroom. "
                    pause 2.0
                    jump tcookingclass1
                " Just watch with Carmen ":
                    $ carmenlv += 10
                    ca " ... "
                    " You sat down next to Carmen and just watched Jacob struggle. "
                    " I mean, he DID cause that mess himself. "
                    " You're not gonna help him with that. "
                    " Nuh uh. "
                    " You're just gonna watch. "
                    scene black with dissolve
                    " You spent the rest of the break watching Jacob suffer with Carmen. "
                    " Eventually, he does get the pages out. "
                    " Carmen still gave him a bonk on the head for messing with his guitar though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the library and went to your classroom. "
                    pause 2.0
                    jump tcookingclass1
        else:
            " You walked over to them and asked them what they were doing. "
            x " Oh, hey there [name]. "
            $ jacobknow = True
            jac " I'm Jacob, and uh... "
            $ carmenknow = True
            jac " I'm kind of helping Carmen over here right now. "
            jac " I thought it would be a funny idea to shove some book pages into his guitar... "
            jac " But now we can't really get it out. "
            jac " Oopsies. "
            ca " ... "
            " Carmen just looks really done with Jacob. "
            " Why exactly did he think this was a good idea? "
            jac " Look - I thought it would be funny, okay?! "
            jac " I already apologized to you!! "
            ca " ... "
            " Carmen stares at him before he gives him some signs... "
            " Signs about Jacob being the one to get the pages out. "
            " I mean...it was pretty fair. "
            " He was the one who did the thing in the first place. "
            " You considered helping if Jacob struggled too much. "
            jac " Alright, alright... "
            jac " Fine - I'll get the pages out of your guitar. "
            jac " Just gimme it. "
            " Carmen hands him over the guitar and sits down on a chair. "
            " He looks like he's ready to see him struggle... "
            " And honestly, you were, too. "
            " Let's see how badly he struggles with this. "
            jac " This should be pretty easy. "
            jac " Just let me...do this... "
            " He starts trying to get the paper, but he can't seem to get it. "
            hide jacobneutral at bottom
            show jacobangry at left
            jac " Ugh, come on now... "
            jac " This shouldn't be that hard... "
            jac " This is probably the easiest thing to do... "
            jac " I can't be fumbling this bad. "
            " He keeps trying and trying... "
            " But he kept on failing. "
            " You honestly felt a little bad that he was struggling. "
            " Should you help him? "
            " Carmen looks like he doesn't want you to help him though. "
            menu:
                " Help Jacob ":
                    $ jacoblv += 10
                    hide jacobangry at bottom
                    show jacobneutral at left
                    jac " ...Huh? you're actually helping me? "
                    jac " ...Alright, thanks. "
                    jac " Here, so you can get the pages easier. "
                    " Jacob tilts the guitar a bit so you could get the pages easier. "
                    " And then you started helping him out... "
                    scene black with dissolve
                    " You spent the rest of the break helping Jacob. "
                    " Eventually, he does get the pages out. "
                    " Carmen still gave him a bonk on the head for messing with his guitar though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the library and went to your classroom. "
                    pause 2.0
                    jump tcookingclass1
                " Just watch with Carmen ":
                    $ carmenlv += 10
                    ca " ... "
                    " You sat down next to Carmen and just watched Jacob struggle. "
                    " I mean, he DID cause that mess himself. "
                    " You're not gonna help him with that. "
                    " Nuh uh. "
                    " You're just gonna watch. "
                    scene black with dissolve
                    " You spent the rest of the break watching Jacob suffer with Carmen. "
                    " Eventually, he does get the pages out. "
                    " Carmen still gave him a bonk on the head for messing with his guitar though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the library and went to your classroom. "
                    pause 2.0
                    jump tcookingclass1
label tcookingclass1:
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    " You walked into the classroom and the teacher was already there. "
    " You then went over to your desk and waited patiently for the teacher to start her class. "
    show jiayuneutral at center with easeinleft
    msx " Hello, class. "
    msx " Today we will be taking down notes. "
    msx " No activities. "
    msx " Take out notebooks and start copying from my slides. "
    msx " If you do not copy everything in time, "
    msx " Just copy from your classmate. "
    msx " I am in a rush this time. "
    " Well geez, alright. "
    " You took your notebook and you started writing things down... "
    " You need to do this fast this time. "
    scene black with dissolve
    " You spent the rest of class hours quickly doing your notes. "
    " You managed to copy most of the important things in there... "
    " Some you didn't quite get, but you could just ask for notes later. "
    play sound "audio/bellring.mp3"
    " The bell rings after a little bit, looks like it's time for you to go home. "
    " You walked out of the classroom after you packed all of your things. "
    pause 2.0
    jump thursocgohome
label thursocgohome:
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
    " There was mostly nothing new, as per usual. "
    " You checked the goofy classroom GC and found all of your classmates goofing off...per usual. "
    " You decided to do some doomscrolling here and there... "
    " You eventually closed your phone and left it to charge overnight, "
    " Then you laid yourself on your bed, tucking yourself in. "
    " Not long after, you started falling asleep. "
    scene black with dissolve
    " Good night, [name]. "
    stop music fadeout 1.5
    pause 2.0
    jump ocfriday
