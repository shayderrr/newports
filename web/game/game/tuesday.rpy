label tuesday:
    # now tuesday is being worked on
    play music "audio/home.mp3" fadein 0.5
    show text " DAY 2 - TUESDAY "
    pause 1.5
    scene mcroom with dissolve
    pause 0.5
    scene black with dissolve
    pause 0.5
    scene mcroom with dissolve
    " Good morning, sunshine. "
    " Time for another day of school that you have to endure. "
    " You get yourself dressed, eat breakfast, and you hop out of your house to go to school. "
    scene black with dissolve
    stop music fadeout 0.5
    pause 2.0
    play music "audio/paperhigh.mp3" fadein 0.5
    scene paperschoolfront with dissolve
    pause 1.0
    scene hallway with dissolve
    pause 1.0
    scene classroom with dissolve
    " You sat down on your seat, seeing that only a few students are here. "
    " You {i}did{/i} arrive a little too early... "
    " But, you know what they say. Being early is better than being late. "
    if claengbub,abblana == True:
        " You were about to pull out your notebook and study, until one of your seatmates started talking to you. "
        if claengbub == True:
            show engelneutral at center with easeinleft
            e " My, you're quite early today, [name]... "
            e " It's better to be early than, late, right? "
            hide engelneutral at bottom
            show engelhappy at center
            e " Heheh...Bubble and Claire usually come in a bit late. "
            e " They don't know that we get additional points for coming in early, hmhm... "
            e " I actually keep track of who comes in early and who comes in late. "
            e " When it's time for class to start, I tell Miss Circle who came early...and she gives them +15 points. "
            e " That includes me. And now, you get +15 points too. "
            e " Sweet, right? Well, if you want to keep getting those additional points, you gotta keep coming in early. "
            " Well, damn. Let's keep coming in early, then! "
            " You want those sweet juicy points, otherwise you're basically gonna fail this school year. "
            hide engelhappy at bottom
            show engelneutral at center
            e " Anywho, Miss Circle is going to be absent today. She told me that she's sick... "
            e " She'll be back tomorrow though, don't worry! "
            " ...How can she recover that fast? "
            hide engelneutral at bottom
            show engelhappy at center
            e " Don't worry, she's just built different. That's how she can recover quick! "
            " Oh. Well that explains it. "
            hide engelhappy at bottom
            show engelneutral at center
            e " Another thing, by the way. Miss Circle left something for us to work on... "
            e " Here, I have a photo of it. Let's work on this together - you only need a one whole sheet of paper... "
            scene black with dissolve
            " You answered the worksheet Miss Circle gave to you with Engel. "
            " It was pretty easy, surprisingly. "
            " Or you're just lying and it was really hard. "
            " Well, who cares if it was easy or not? It's just a worksheet anyway. "
            " Eventually, you and Engel got done with the worksheet. "
            " Engel told you that he'll just get everyone else's worksheet and pass it to Miss Circle. "
            " ...He told you that he's usually the one who passes things to Miss Circle whenever she's absent. "
            " Totally makes sense. Totally. I don't know how to word things, man. "
            play sound "audio/bellring.mp3"
            " The bell rings after a few minutes of chilling in your seat. "
            " It's time for a break now. You get up off of your seat and you go into the hallway. "
            pause 2.0
            jump tuesdaybreak1
        elif abblana == True:
            show lananeutral at center with easeinright
            l " Hey there, [name]! "
            l " You're pretty early, hmmm? "
            l " Abbie usually comes in late, since he's such a deep sleeper. "
            l " I did hear about this rumor about you getting additional points if you come in early, buuutt... "
            l " I'm not really sure. I mean, it's just a rumor after all! "
            l " I don't really believe in the rumor, because I don't think Miss Circle would be nice enough to do that... "
            l " Another thing I'd like to talk about! "
            l " Apparently, Miss Circle's gonna be absent for today because she's sick... "
            l " I hope she recovers soon! Oh, right...! "
            l " We've got a worksheet sent by Miss Circle that we had to do! "
            l " Engel sent a photo of it last night, I'm pretty sure you were already asleep at that time, hehe... "
            l " Since you probably don't have a photo of it, I saved it! "
            l " I think we only need a one whole sheet of paper to answer this thing... "
            " Lana goes to check in her bag, and she has a whole lot of paper. "
            hide lananeutral at bottom
            show lanahappy at center
            l " I have a lot of paper, [name]! Here, take one, take one! "
            " You take one sheet of paper from Lana, look at the photo that Lana had, and you started answering. "
            scene black with dissolve
            " You answered the worksheet with Lana. "
            " Abbie comes into the classroom 20 minutes later. "
            " You had to explain to Abbie and Lana about what to do on the worksheet. "
            " They didn't really understand math as much as you did, so you explained it to them the best you could. "
            " Eventually, all of you got done answering. "
            " You three passed your papers to Engel once you all were done. "
            " Apparently, Engel was the guy who would pass things to teachers whenever they're absent. "
            " Interesting fact... "
            " You decided to talk to Lana and Abbie now that all of you were done with the worksheet. "
            play sound "audio/bellring.mp3"
            pause 1.0
            " The bell rings after a few minutes of talking with Lana and Abbie. "
            " You get up from your seat, and you walk into the hallway to take a break. "
            pause 2.0
            jump tuesdaybreak1
        else:
            " You sat in your seat, and pulled out your phone to see if there's anything new.. "
            " You look into your school GC and found that there was a worksheet that Miss Circle left for you and your classmates to do. "
            " Apparently, she's going to be absent today because she's sick. "
            " Hopefully she'll recover soon. "
            " Anywho, you pulled out one whole sheet of paper, and you started answering the worksheet. "
            scene black with dissolve
            " You spent the entire class answering the worksheet that Miss Circle left. "
            " It was honestly pretty easy. "
            " Or you're just lying and it was really hard. "
            " Well, who cares if it was easy or not? It's just a worksheet anyway. "
            " Eventually, you got done with the worksheet. "
            " You passed your paper to Engel once you all were done. "
            " Apparently, Engel was the guy who would pass things to teachers whenever they're absent. "
            " Interesting fact... "
            " You decided to just chill around and listen to some music until break starts. "
            pause 1.0
            play sound "audio/bellring.mp3"
            " The bell rings a few mintues later, meaning that it's time for a break. "
            " You get up from your seat, and you walk out into the hallways so that you could find somewhere to hangout. "
            pause 2.0
            jump tuesdaybreak1
    elif alone == True:
        " You sat in your seat, and pulled out your phone to see if there's anything new.. "
        " You look into your school GC and found that there was a worksheet that Miss Circle left for you and your classmates to do. "
        " Apparently, she's going to be absent today because she's sick. "
        " Hopefully she'll recover soon. "
        " Anywho, you pulled out one whole sheet of paper, and you started answering the worksheet. "
        scene black with dissolve
        " You spent the entire class answering the worksheet that Miss Circle left. "
        " It was honestly pretty easy. "
        " Or you're just lying and it was really hard. "
        " Well, who cares if it was easy or not? It's just a worksheet anyway. "
        " Eventually, you got done with the worksheet. "
        " You passed your paper to Engel once you all were done. "
        " Apparently, Engel was the guy who would pass things to teachers whenever they're absent. "
        " Interesting fact... "
        " You decided to just chill around and listen to some music until break starts. "
        pause 1.0
        play sound "audio/bellring.mp3"
        " The bell rings a few mintues later, meaning that it's time for a break. "
        " You get up from your seat, and you walk out into the hallways so that you could find somewhere to hangout. "
        pause 2.0
        jump tuesdaybreak1
label tuesdaybreak1:
    scene hallway with dissolve
    " It's breaktime, and you're thinking about hanging out somewhere. "
    " Where do you go? "
    if populartiktok == True:
        " Psst, seems like Lizzy and Petunia have something to talk about to you in the front of the school. "
        " Best to go there. "
    else:
        pass
    menu:
        " {image=popularicon} The front of the school {image=popularicon} ":
            jump tuesdayfront1
        " {image=abbieicon} The back of the school {image=skellicon} ":
            jump tuesdayback1
        " {image=claireicon} The gym {image=bubbleicon} ":
            jump tuesdaygym1
        " The cafeteria ":
            jump tuesdaycafe1
        " {image=rileyicon} Rooftop {image=robbyicon} ":
            jump tuesdayrooftop1
        " {image=kevinicon} The library {image=cubbieicon} ":
            jump tuesdaylibrary1
label tuesdayfront1:
    # lizzy + petunia
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walk outside of the school, and immediately spot two of your classmates hanging out. "
    " Curious on what they're doing, you walk up to them. "
    show petunianeutral at left with easeinright
    show lizzyneutral at right with easeinright
    if popularknow == True and populartiktok == True:
        lz " Hey there, [name]. "
        hide petunianeutral at bottom
        show petuniahappy at left
        p " Heyyyy girlie!!! "
        if they == "he","they":
            " You're not exactly a 'girlie', but you didn't mind. "
            " Petunia and Lizzy would probably call anyone girlie regardless of gender. "
            " Like those kinds of girls you see on tiktok. "
        elif they == "she":
            " Heeyyy!!! ^_^ "
        hide petuniahappy at bottom
        show petunianeutral at left
        p " So, I was thinking... "
        p " How about we move that tiktok thing and we do it right now? "
        lz " Since we've pretty much got enough time for a quick QNA. "
        p " Yeah! what do you think, [name]? "
        menu:
            " Let's do it ":
                hide petunianeutral at bottom
                show petuniahappy at left
                p " Woohoo, alright! "
                hide petuniahappy at bottom
                show petunianeutral at left
                p " Pretty sure you know what to do, right? "
                lz " Just answer the questions Petunia throws at you. "
                lz " I'll be the one recording. "
                p " Okay, here we go! "
                lz " Three, two, one... go. "
                p " Hiii everyone, today we have a special guest: [name]!! "
                if kind == True:
                    " You wave energetically at the camera. "
                elif calm == True:
                    " You do a peace sign at the camera. "
                elif mean == True:
                    " You do a simple wave at the camera. "
                p " Today, we'll be asking a bunch of questions to [name]!! "
                p " Here's our first one - [name], what's your favorite food? "
                " You told them what your favorite food was. "
                " No, you can't say that you ate people for breakfast today. "
                " That'd make them lose their followers! "
                p " Ooo, sounds delicious! "
                p " Now, onto our next question... "
                scene black with dissolve
                " You spent the rest of the break doing a tiktok video with Lizzy and Petunia. "
                " You're going to have to check how that video's going to do later after school. "
                play sound "audio/bellring.mp3"
                " The bell rings not too long after you guys were done with recording the video. "
                " You all then went back into the school and walked to the classroom. "
                pause 2.0
                jump languageclass2
            " Maybe later, after school ":
                $ populartiktoklater = True
                p " Mmm... alright, whatever you say. "
                lz " Let's just hang out for the rest of the break, then. "
                hide petunianeutral at bottom
                show petuniahappy at left
                p " Yup! This is a good time for us to take quick photos together! "
                lz " It sure is... "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Lizzy. "
                " You also got to take photos of you three hanging out. "
                " Being friends with the popular girls... it's pretty neat. "
                " You might just become popular yourself, too. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes of talking with Petunia and Lizzy. "
                " You all then went back into the school and walked to the classroom. "
                pause 2.0
                jump languageclass2
    elif popularknow == True and populartiktok == False:
        lz " Hey there, [name]. "
        hide petunianeutral at bottom
        show petuniahappy at left
        p " Heyyyy girlie!!! "
        if they == "he","they":
            " You're not exactly a 'girlie', but you didn't mind. "
            " Petunia and Lizzy would probably call anyone girlie regardless of gender. "
            " Like those kinds of girls you see on tiktok. "
        elif they == "she":
            " Heeyyy!!! ^_^ "
        hide petuniahappy at bottom
        show petunianeutral at left
        p " Me and Liz were just discussing on where we would film our video. "
        lz " Been having a bit of trouble on deciding. "
        p " Could you help us out a bit? We know you don't really have much to do. "
        " Well, they're not wrong. "
        " You thought about where they could film the video... "
        menu:
            " The park ":
                p " The park...? "
                lz " I told you that would be a good place to film. "
                lz " Even [name] agrees, don't [they]? "
                p " Well, alright! since [name] said so, I suppose. "
                lz " Let's just hang out for the rest of the break, since we'redone deciding. "
                hide petunianeutral at bottom
                show petuniahappy at left
                p " Yup! This is a good time for us to take quick photos together! "
                lz " It sure is... "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Lizzy. "
                " You also got to take photos of you three hanging out. "
                " Being friends with the popular girls... it's pretty neat. "
                " You might just become popular yourself, too. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes of talking with Petunia and Lizzy. "
                " You all then went back into the school and walked to the classroom. "
                pause 2.0
                jump languageclass2
            " The back of the school ":
                lz " The back of the school? "
                p " Told you it'd be a good recording place! "
                lz " Yeah, I guess so. "
                lz " But, Skell always hangs out there. We gotta make sure that he doesn't get in camera. "
                lz " ...Otherwise he'd throw a fit. "
                p " Wonder why he doesn't like being in camera... "
                lz " Anyway, let's just hang out for the rest of the break, since we'redone deciding. "
                hide petunianeutral at bottom
                show petuniahappy at left
                p " Yup! This is a good time for us to take quick photos together! "
                lz " It sure is... "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Lizzy. "
                " You also got to take photos of you three hanging out. "
                " Being friends with the popular girls... it's pretty neat. "
                " You might just become popular yourself, too. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes of talking with Petunia and Lizzy. "
                " You all then went back into the school and walked to the classroom. "
                pause 2.0
                jump languageclass2
            " At their house ":
                $ popularlv += 20
                hide petunianeutral at bottom
                show petuniasurprised at left
                " ...Petunia looks at you as if she just told herself that she's an idiot. "
                " You feel as if choosing this option just granted you a lot of points. "
                hide petuniasurprised at bottom
                show petuniahappy at left
                p " Of course, my house! "
                p " How come I didn't think of that sooner? "
                p " Thanks, [name]! "
                hide petuniahappy at bottom
                show petunianeutral at left
                lz " Now that that's settled... "
                lz " Let's just hang out for the rest of the break, since we'redone deciding. "
                hide petunianeutral at bottom
                show petuniahappy at left
                p " Yup! This is a good time for us to take quick photos together! "
                lz " It sure is... "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Lizzy. "
                " You also got to take photos of you three hanging out. "
                " Being friends with the popular girls... it's pretty neat. "
                " You might just become popular yourself, too. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes of talking with Petunia and Lizzy. "
                " You all then went back into the school and walked to the classroom. "
                pause 2.0
                jump languageclass2
    else:
        x " So I was thinking... "
        x " Oh, hey there, new kid. "
        hide petunianeutral at bottom
        show petuniahappy at left
        x " Heyyyy !! "
        hide petuniahappy at bottom
        show petunianeutral at left
        $ popularknow = True
        p " I'm Petunia! This is Lizzy! "
        lz " We're pretty famous. "
        p " Uh huh! Anyway... "
        p " Me and Liz were just discussing on where we would film our video. "
        lz " Been having a bit of trouble on deciding. "
        p " Could you help us out a bit? We know you don't really have much to do. "
        " Well, they're not wrong. "
        " You thought about where they could film the video... "
        menu:
            " The park ":
                p " The park...? "
                lz " I told you that would be a good place to film. "
                lz " Even [name] agrees, don't [they]? "
                p " Well, alright! since [name] said so, I suppose. "
                lz " Let's just hang out for the rest of the break, since we'redone deciding. "
                hide petunianeutral at bottom
                show petuniahappy at left
                p " Yup! This is a good time for us to take quick photos together! "
                lz " It sure is... "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Lizzy. "
                " You also got to take photos of you three hanging out. "
                " Being friends with the popular girls... it's pretty neat. "
                " You might just become popular yourself, too. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes of talking with Petunia and Lizzy. "
                " You all then went back into the school and walked to the classroom. "
                pause 2.0
                jump languageclass2
            " The back of the school ":
                lz " The back of the school? "
                p " Told you it'd be a good recording place! "
                lz " Yeah, I guess so. "
                lz " But, Skell always hangs out there. We gotta make sure that he doesn't get in camera. "
                lz " ...Otherwise he'd throw a fit. "
                p " Wonder why he doesn't like being in camera... "
                lz " Anyway, let's just hang out for the rest of the break, since we'redone deciding. "
                hide petunianeutral at bottom
                show petuniahappy at left
                p " Yup! This is a good time for us to take quick photos together! "
                lz " It sure is... "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Lizzy. "
                " You also got to take photos of you three hanging out. "
                " Being friends with the popular girls... it's pretty neat. "
                " You might just become popular yourself, too. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes of talking with Petunia and Lizzy. "
                " You all then went back into the school and walked to the classroom. "
                pause 2.0
                jump languageclass2
            " At their house ":
                $ popularlv += 20
                hide petunianeutral at bottom
                show petuniasurprised at left
                " ...Petunia looks at you as if she just told herself that she's an idiot. "
                " You feel as if choosing this option just granted you a lot of points. "
                hide petuniasurprised at bottom
                show petuniahappy at left
                p " Of course, my house! "
                p " How come I didn't think of that sooner? "
                p " Thanks, [name]! "
                hide petuniahappy at bottom
                show petunianeutral at left
                lz " Now that that's settled... "
                lz " Let's just hang out for the rest of the break, since we'redone deciding. "
                hide petunianeutral at bottom
                show petuniahappy at left
                p " Yup! This is a good time for us to take quick photos together! "
                lz " It sure is... "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Lizzy. "
                " You also got to take photos of you three hanging out. "
                " Being friends with the popular girls... it's pretty neat. "
                " You might just become popular yourself, too. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes of talking with Petunia and Lizzy. "
                " You all then went back into the school and walked to the classroom. "
                pause 2.0
                jump languageclass2
label tuesdayback1:
    # abbie + skell
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and noticed that two of your classmates are hanging out here. "
    " You thought of talking to one of them, but who do you talk to? "
    if abbieknow == True and skellknow == True:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump abbieint
            " {image=skellicon} Skell {image=skellicon} ":
                jump skellint
    elif abbieknow == True and skellknow == False:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump abbieint
            " {image=skellicon} An emo guy {image=skellicon} ":
                jump skellint
    elif abbieknow == False and skellknow == True:
        menu:
            " {image=abbieicon} A sad guy {image=abbieicon} ":
                jump abbieint
            " {image=skellicon} Skell {image=skellicon} ":
                jump skellint
    else:
        menu:
            " {image=abbieicon} A sad guy {image=abbieicon} ":
                jump abbieint
            " {image=skellicon} An emo guy {image=skellicon} ":
                jump skellint
    label abbieint:
        " You see him curled up into a ball, sitting on the ground. "
        " You decided to sit next to him. "
        show abbieneutral at center with easeinbottom
        if abbieknow == True:
            a " ... "
            " He seems quite comfortable in this position... "
            " You ask him if he's doing alright. "
            a " ...? "
            a " Oh, it's you... "
            a " I'm doing fine...it's just... "
            a " I like to visit here sometimes... "
            a " It makes me calm down a whole lot. "
            hide abbieneutral at bottom
            show abbiehappy at center
            a " Just looking around at nature and listening to background noise... "
            a " ...It's nice... to get a break from all of the yelling... "
            a " That I usually hear in here... "
            a " ... "
            a " Um... "
            a " Would you like to...relax with me for a bit...? "
            a " It's okay if you don't want to... "
            a " I don't want to be a bother to you... "
            " You need a little break for yourself, so... "
            " You decided to relax a little with Abbie for a bit. "
            scene black with dissolve
            " You spent the rest of the break relaxing with Abbie. "
            " It was honestly real nice getting to catch a break like this.. "
            " You wish that you could just rest for the entire day. "
            play sound "audio/bellring.mp3"
            " But, that won't happen. You have school, of course it won't! "
            " You get yourself up from the ground, and you walk your ass back to your classroom. "
            pause 2.0
            jump languageclass2
        else:
            x " ... "
            " He seems quite comfortable in this position... "
            " You ask him if he's doing alright. "
            x " ...? "
            x " Oh, it's you... "
            x " I'm doing fine...it's just... "
            x " I like to visit here sometimes... "
            x " It makes me calm down a whole lot. "
            $ abbieknow = True
            a " I'm Abbie, by the way... "
            a " It's...nice to meet you... "
            hide abbieneutral at bottom
            show abbiehappy at center
            a " ...looking around at nature and listening to background noise... "
            a " ...It's nice... to get a break from all of the yelling... "
            a " That I usually hear in here... "
            a " ... "
            a " Um... "
            a " Would you like to...relax with me for a bit...? "
            a " It's okay if you don't want to... "
            a " I don't want to be a bother to you... "
            " You need a little break for yourself, so... "
            " You decided to relax a little with Abbie for a bit. "
            scene black with dissolve
            " You spent the rest of the break relaxing with Abbie. "
            " It was honestly real nice getting to catch a break like this.. "
            " You wish that you could just rest for the entire day. "
            play sound "audio/bellring.mp3"
            " But, that won't happen. You have school, of course it won't! "
            " You get yourself up from the ground, and you walk your ass back to your classroom. "
            pause 2.0
            jump languageclass2
    label skellint:
        $ skelllv += 20
        " You saw him staring into space while having his earphones on. "
        " You sat down next to him curiously. "
        show skellneutral at center with easeinbottom
        if skellknow == True:
            sk " ... "
            " Looks like he's in deep thought. "
            " You gently poke him on the shoulder to see if he's doing alright. "
            sk " ...Huh? "
            sk " Oh. You. "
            sk " I'm doing alright, just... thinking about a few things, is all. "
            sk " You ever get that feeling where life just doesn't feel real sometimes? "
            sk " Like, something good happens to you on a week where everything's awful. "
            sk " It should be a good thing, but it just feels...weird. "
            sk " Weird as in 'should this be happening?' weird. "
            sk " This week has been pretty horrible for be so far. "
            sk " Mostly due to family issues and personal issues. "
            sk " But, uh... "
            sk " ...Nevermind. You're going to think that I'm weird. "
            " Before you could tell him that it was okay, he pulled out his phone and showed you a picture. "
            " A picture of his pet cat. "
            sk " Her name is Catrina. "
            sk " See why I named her that? She's adorable... "
            " You've got to admit, that's one cute cat. "
            scene black with dissolve
            " You spent the rest of the break looking at cat pictures Skell has on his phone. "
            " It was worth it, getting to see fat cute cats... "
            " Even though you knew that it was probably just to distract you from asking about what Skell was gonna say. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that breaktime was over and thatyou should go to class. "
            " And go to class you did. "
            pause 2.0
            jump languageclass2
        else:
            x " ... "
            " Looks like he's in deep thought. "
            " You gently poke him on the shoulder to see if he's doing alright. "
            x " ...Huh? "
            x " Oh. You. "
            x " I'm doing alright, just... thinking about a few things, is all. "
            $ skellknow = True
            sk " I'm Skell, by the way. Nice to meet you, I guess. "
            sk " ... "
            sk " You ever get that feeling where life just doesn't feel real sometimes? "
            sk " Like, something good happens to you on a week where everything's awful. "
            sk " It should be a good thing, but it just feels...weird. "
            sk " Weird as in 'should this be happening?' weird. "
            sk " This week has been pretty horrible for be so far. "
            sk " Mostly due to family issues and personal issues. "
            sk " But, uh... "
            sk " ...Nevermind. You're going to think that I'm weird. "
            " Before you could tell him that it was okay, he pulled out his phone and showed you a picture. "
            " A picture of his pet cat. "
            sk " Her name is Catrina. "
            sk " See why I named her that? She's adorable... "
            " You've got to admit, that's one cute cat. "
            scene black with dissolve
            " You spent the rest of the break looking at cat pictures Skell has on his phone. "
            " It was worth it, getting to see fat cute cats... "
            " Even though you knew that it was probably just to distract you from asking about what Skell was gonna say. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that breaktime was over and thatyou should go to class. "
            " And go to class you did. "
            pause 2.0
            jump languageclass2
label tuesdaygym1:
    # Claire + Bubble
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked around the gym for a bit. "
    " And of course, you spotted two of your classmates talking to eachother. "
    " Curious on what they're talking about, you walk up to them. "
    if mean == True and clairesorry == False:
        " ...Wait, that's Claire. "
        " Oh hell no, you're not talking to her. "
        " Let's just go to class early or whatever. "
        scene black with dissolve
        " You went to class early this time, and you waited for your classmates to arrive. "
        " And your teacher. "
        pause 2.0
        jump languageclass2
    else:
        pass
    show claireneutral at right with easeinleft
    show bubbleneutral at left with easeinleft
    if claireknow == True and bubbleknow == True:
        c " Did you hear? "
        b " Hear about what, Claire? "
        c " A series that I really like is getting another season! "
        hide bubbleneutral at bottom
        show bubblehappy at left
        b " Really?! that's great! "
        hide claireneutral at bottom
        show clairehappy at right
        c " I know right!! "
        c " Hopefully, I'll get more content of my favorite character. "
        c " Since he's just a side character and all... "
        hide bubblehappy at bottom
        show bubbleneutral at left
        b " Heh, yes... it's sort of a struggle whenever your favorite character is a side character. "
        b " They either get little to no content, or they get a whole bunch of content. "
        " You greeted them hello and asked them which series they were talking about. "
        hide clairehappy at bottom
        show claireneutral at right
        c " Oh, hey [name]! "
        b " Hiya, [name]!! "
        c " About the series we were talking about...? "
        b " We're not exactly sure if it's your type of thing, [name]... "
        if kind == True:
            " I mean, you did look a bit innocent. "
            " I can see why Bubble said that. "
        elif mean == True:
            " ...No? judging from your appearance, you're the type to watch anything princess related{nw} "
            " I mean huh. "
        elif calm == True:
            " No, you're probably the type to watch anything. "
            " You're just a chill guy, after all. "
        c " Yeah, since it's got a lot of...interesting scenes. "
        b " Not in the way that you're thinking right now, of course. "
        c " I wouldn't watch anything like that! "
        play sound "audio/bellring.mp3"
        c " Oh, well would you look at that. "
        b " It's time to go to class! "
        b " We'll see you in the classroom, [name]! "
        b " See you! "
        hide claireneutral at right with easeoutright
        hide bubbleneutral at right with easeoutright
        "...Well, that was odd. "
        " You should probably go to class too. "
        " You don't want your ass to get beat. "
        scene black with dissolve
        pause 2.0
        jump languageclass2
    elif claireknow == True and bubbleknow == False:
        c " Did you hear? "
        x " Hear about what, Claire? "
        c " A series that I really like is getting another season! "
        hide bubbleneutral at bottom
        show bubblehappy at left
        x " Really?! that's great! "
        hide claireneutral at bottom
        show clairehappy at right
        c " I know right!! "
        c " Hopefully, I'll get more content of my favorite character. "
        c " Since he's just a side character and all... "
        hide bubblehappy at bottom
        show bubbleneutral at left
        x " Heh, yes... it's sort of a struggle whenever your favorite character is a side character. "
        x " They either get little to no content, or they get a whole bunch of content. "
        " You greeted them hello and asked them which series they were talking about. "
        hide clairehappy at bottom
        show claireneutral at right
        c " Oh, hey [name]! "
        x " Hiya, [name]!! "
        x " I don't think I got to introduce myself, erm... "
        c " Oh, right! "
        $ bubbleknow = True
        c " [name], this is one of my dear friends - Bubble! She's really nice! "
        b " It's good to meet you! "
        c " Now, about the series we were talking about...? "
        b " We're not exactly sure if it's your type of thing, [name]... "
        if kind == True:
            " I mean, you did look a bit innocent. "
            " I can see why Bubble said that. "
        elif mean == True:
            " ...No? judging from your appearance, you're the type to watch anything princess related{nw} "
            " I mean huh. "
        elif calm == True:
            " No, you're probably the type to watch anything. "
            " You're just a chill guy, after all. "
        c " Yeah, since it's got a lot of...interesting scenes. "
        b " Not in the way that you're thinking right now, of course. "
        c " I wouldn't watch anything like that! "
        play sound "audio/bellring.mp3"
        c " Oh, well would you look at that. "
        b " It's time to go to class! "
        b " We'll see you in the classroom, [name]! "
        b " See you! "
        hide claireneutral at right with easeoutright
        hide bubbleneutral at right with easeoutright
        "...Well, that was odd. "
        " You should probably go to class too. "
        " You don't want your ass to get beat. "
        scene black with dissolve
        pause 2.0
        jump languageclass2
    elif claireknow == False and bubbleknow == True:
        x " Did you hear? "
        b " Hear about what, Claire? "
        x " A series that I really like is getting another season! "
        hide bubbleneutral at bottom
        show bubblehappy at left
        b " Really?! that's great! "
        hide claireneutral at bottom
        show clairehappy at right
        x " I know right!! "
        x " Hopefully, I'll get more content of my favorite character. "
        x " Since he's just a side character and all... "
        hide bubblehappy at bottom
        show bubbleneutral at left
        b " Heh, yes... it's sort of a struggle whenever your favorite character is a side character. "
        b " They either get little to no content, or they get a whole bunch of content. "
        " You greeted them hello and asked them which series they were talking about. "
        hide clairehappy at bottom
        show claireneutral at right
        x " Oh, hey [name]! "
        b " Hiya, [name]!! "
        x " I don't think I got to introduce myself to you... "
        x " I think I recognize you, though! You're that new kid from yesterday, yes? "
        " You nodded your head. "
        b " That's right, Claire! "
        $ claireknow = True
        b " [name], this is one of my dear friends, Claire! "
        c " It's nice to meet you! "
        c " Now, about the series we were talking about...? "
        b " We're not exactly sure if it's your type of thing, [name]... "
        if kind == True:
            " I mean, you did look a bit innocent. "
            " I can see why Bubble said that. "
        elif mean == True:
            " ...No? judging from your appearance, you're the type to watch anything princess related{nw} "
            " I mean huh. "
        elif calm == True:
            " No, you're probably the type to watch anything. "
            " You're just a chill guy, after all. "
        c " Yeah, since it's got a lot of...interesting scenes. "
        b " Not in the way that you're thinking right now, of course. "
        c " I wouldn't watch anything like that! "
        play sound "audio/bellring.mp3"
        c " Oh, well would you look at that. "
        b " It's time to go to class! "
        b " We'll see you in the classroom, [name]! "
        b " See you! "
        hide claireneutral at right with easeoutright
        hide bubbleneutral at right with easeoutright
        "...Well, that was odd. "
        " You should probably go to class too. "
        " You don't want your ass to get beat. "
        scene black with dissolve
        pause 2.0
        jump languageclass2
    else:
        x " Did you hear? "
        x " Hear about what, Claire? "
        x " A series that I really like is getting another season! "
        hide bubbleneutral at bottom
        show bubblehappy at left
        x " Really?! that's great! "
        hide claireneutral at bottom
        show clairehappy at right
        x " I know right!! "
        x " Hopefully, I'll get more content of my favorite character. "
        x " Since he's just a side character and all... "
        hide bubblehappy at bottom
        show bubbleneutral at left
        x " Heh, yes... it's sort of a struggle whenever your favorite character is a side character. "
        x " They either get little to no content, or they get a whole bunch of content. "
        " You greeted them hello and asked them which series they were talking about. "
        hide clairehappy at bottom
        show claireneutral at right
        x " Oh, hey [name]! "
        x " Hiya, [name]!! "
        x " I don't think I got to introduce myself to you... "
        x " Me neither... "
        x " I think I recognize you, though! You're that new kid from yesterday, yes? "
        " You nodded your head. "
        x " That's right, Claire! "
        $ claireknow = True
        $ bubbleknow = True
        x " [name], this is one of my dear friends, Claire! "
        b " And I'm Bubble!! "
        c " It's nice to meet you!! "
        c " Now, about the series we were talking about...? "
        b " We're not exactly sure if it's your type of thing, [name]... "
        if kind == True:
            " I mean, you did look a bit innocent. "
            " I can see why Bubble said that. "
        elif mean == True:
            " ...No? judging from your appearance, you're the type to watch anything princess related{nw} "
            " I mean huh. "
        elif calm == True:
            " No, you're probably the type to watch anything. "
            " You're just a chill guy, after all. "
        c " Yeah, since it's got a lot of...interesting scenes. "
        b " Not in the way that you're thinking right now, of course. "
        c " I wouldn't watch anything like that! "
        play sound "audio/bellring.mp3"
        c " Oh, well would you look at that. "
        b " It's time to go to class! "
        b " We'll see you in the classroom, [name]! "
        b " See you! "
        hide claireneutral at right with easeoutright
        hide bubbleneutral at right with easeoutright
        "...Well, that was odd. "
        " You should probably go to class too. "
        " You don't want your ass to get beat. "
        scene black with dissolve
        pause 2.0
        jump languageclass2
label tuesdaycafe1:
    # Ruby, Lana, Zip
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You enter the cafeteria and spotted some of your classmates just vibing. "
    " You're thinking about talking to them... but who do you talk to? "
    if rubyknow,lanaknow,oligangknow == True:
        menu:
            " {image=rubyicon} Ruby {image=rubyicon} ":
                jump rubycafeint
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump lanacafeint
            " {image=oligangicon} Zip {image=oligangicon} ":
                jump zipcafeint
    elif rubyknow,lanaknow == True and oligangknow == False:
        menu:
            " {image=rubyicon} Ruby {image=rubyicon} ":
                jump rubycafeint
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump lanacafeint
            " {image=oligangicon} A mean looking girl {image=oligangicon} ":
                jump zipcafeint
    elif rubyknow,oligangknow == True and lanaknow == False:
        menu:
            " {image=rubyicon} Ruby {image=rubyicon} ":
                jump rubycafeint
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump lanacafeint
            " {image=oligangicon} Zip {image=oligangicon} ":
                jump zipcafeint
    elif lanaknow,oligangknow == True and rubyknow == False:
        menu:
            " {image=rubyicon} A girl with a TV for her head {image=rubyicon} ":
                jump rubycafeint
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump lanacafeint
            " {image=oligangicon} Zip {image=oligangicon} ":
                jump zipcafeint
    elif rubyknow == True and lanaknow,oligangknow == False:
        menu:
            " {image=rubyicon} Ruby {image=rubyicon} ":
                jump rubycafeint
            " {image=lanaicon} A girl with sock puppets for hands {image=lanaicon} ":
                jump lanacafeint
            " {image=oligangicon} A mean looking girl {image=oligangicon} ":
                jump zipcafeint
    elif lanaknow == True and rubyknow,oligangknow == False:
        menu:
            " {image=rubyicon} A girl with a TV for her head {image=rubyicon} ":
                jump rubycafeint
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump lanacafeint
            " {image=oligangicon} A mean looking girl {image=oligangicon} ":
                jump zipcafeint
    elif oligangknow == True and rubyknow,lanaknow == False:
        menu:
            " {image=rubyicon} A girl with a TV for her head {image=rubyicon} ":
                jump rubycafeint
            " {image=lanaicon} A girl with sock puppets for hands {image=lanaicon} ":
                jump lanacafeint
            " {image=oligangicon} Zip {image=oligangicon} ":
                jump zipcafeint
    else:
        menu:
            " {image=rubyicon} A girl with a TV for her head {image=rubyicon} ":
                jump rubycafeint
            " {image=lanaicon} A girl with sock puppets for hands {image=lanaicon} ":
                jump lanacafeint
            " {image=oligangicon} A mean looking girl {image=oligangicon} ":
                jump zipcafeint
    label rubycafeint:
        # talking about games
        if rubyknow == True:
            " You decided to go and sit next to Ruby. "
        else:
            " You decided to go and sit with the TV girl. "
        show rubyneutral at center with easeinleft
        if rubyknow == True:
            ru " ...Loading... "
            hide rubyneutral at bottom
            show rubyhappy at center
            ru " Oh, hi there [name]!! "
            ru " I hope you're doing well today, hehe... "
            hide rubyhappy at bottom
            show rubyneutral at center
            ru " Was there something that you wanted to talk to me about? "
            " You shrugged. You were kinda expecting Ruby to start talking about something interesting instead of you finding a topic to talk about. "
            hide rubyneutral at bottom
            show rubysurprised at center
            ru " Oh...? "
            hide rubysurprised at bottom
            show rubyneutral at center
            ru " Alright, I'll find some topics that we can talk about! "
            ru " Finding things to talk about... "
            ru " ...Have you heard of a game called CraftMine? "
            ru " I probably said it wrong, but I'm sure it's familiar to you! "
            ru " You basically just...craft and mine. "
            ru " It's in the name, heheh! "
            ru " I've also heard that they've got a movie of it out recently... "
            ru " I haven't seen it yet, but there's a bunch of people saying odd things related to the movie. "
            ru " Like...what is a 'chicken jockey'...? "
            ru " What are you going to do with a 'Flint and Steel'? "
            ru " 'Release' what??? "
            ru " But, anyway... I really want to try that 'Alex's lava chicken' thing! "
            ru " Everyone's been talking about it on social media, and I want to give it a try! "
            ru " But, I did hear about another thing in the CraftMine movie. "
            ru " They added a reference to a big minecraft content creator who died a few years ago... "
            hide rubyneutral at bottom
            show rubyhappy at center
            ru " That's quite sweet of them to do so, in my opinion! "
            ru " A little reference to a legend... it just goes to show how much big of an impact that creator made on the community. "
            ru " May they rest in peace. They would've been happy to see the things the community has done for them. "
            ru " Hmmhm... "
            hide rubyhappy at bottom
            show rubyneutral at center
            play sound "audio/bellring.mp3"
            ru " ...The bell has rung? "
            ru " I swore that the breaks here were much longer... "
            ru " Had I been on sleep mode for far too long? "
            ru " ...Well, anyway... "
            ru " I'll see you in class, [name]! "
            hide rubyneutral at right with easeoutright
            "...You'd better get to class aswell. "
            scene black with dissolve
            pause 2.0
            jump languageclass2
        else:
            x " ...Loading... "
            hide rubyneutral at bottom
            show rubyhappy at center
            x " Oh, hi there [name]!! "
            x " I hope you're doing well today, hehe... "
            hide rubyhappy at bottom
            show rubyneutral at center
            x " Oh, wait! I'm afraid that I haven't introduced myself yet to you, as far as I can remember... "
            x " Sincerest of apologies... "
            $ rubyknow = True
            ru " I'm Ruby! We're in the same class. "
            ru " I hope we can become the best of friends! "
            ru " Anywho, was there something that you wanted to talk to me about? "
            " You shrugged. You were kinda expecting Ruby to start talking about something interesting instead of you finding a topic to talk about. "
            hide rubyneutral at bottom
            show rubysurprised at center
            ru " Oh...? "
            hide rubysurprised at bottom
            show rubyneutral at center
            ru " Alright, I'll find some topics that we can talk about! "
            ru " Finding things to talk about... "
            ru " ...Have you heard of a game called CraftMine? "
            ru " I probably said it wrong, but I'm sure it's familiar to you! "
            ru " You basically just...craft and mine. "
            ru " It's in the name, heheh! "
            ru " I've also heard that they've got a movie of it out recently... "
            ru " I haven't seen it yet, but there's a bunch of people saying odd things related to the movie. "
            ru " Like...what is a 'chicken jockey'...? "
            ru " What are you going to do with a 'Flint and Steel'? "
            ru " 'Release' what??? "
            ru " But, anyway... I really want to try that 'Alex's lava chicken' thing! "
            ru " Everyone's been talking about it on social media, and I want to give it a try! "
            ru " But, I did hear about another thing in the CraftMine movie. "
            ru " They added a reference to a big minecraft content creator who died a few years ago... "
            hide rubyneutral at bottom
            show rubyhappy at center
            ru " That's quite sweet of them to do so, in my opinion! "
            ru " A little reference to a legend... it just goes to show how much big of an impact that creator made on the community. "
            ru " May they rest in peace. They would've been happy to see the things the community has done for them. "
            ru " Hmmhm... "
            hide rubyhappy at bottom
            show rubyneutral at center
            play sound "audio/bellring.mp3"
            ru " ...The bell has rung? "
            ru " I swore that the breaks here were much longer... "
            ru " Had I been on sleep mode for far too long? "
            ru " ...Well, anyway... "
            ru " I'll see you in class, [name]! "
            hide rubyneutral at right with easeoutright
            "...You'd better get to class aswell. "
            scene black with dissolve
            pause 2.0
            jump languageclass2
    label lanacafeint:
        # talking about school stuff
        if lanaknow == True:
            " You decided to go and sit next to Lana. "
        else:
            " You decided to go and sit next to the girl with sock puppets. "
        show lananeutral at center with easeinright
        if lanaknow == True:
            l " [name]!! HII HI HI!! " with vpunch
            " Geezes, does her voice usually get this loud when she's excited? "
            l " It's nice to see you here! "
            l " I was kinda just thinking about a few things, mainly school stuff... "
            hide lananeutral at bottom
            show lanaangry at center
            l " Like, we've got a lot of things to do! A lot of homework... "
            l " You're lucky you don't get to do those kinds of stuff, [name]... "
            l " Since you're new and all... "
            hide lanaangry at bottom
            show lananeutral at center
            l " But then again, this IS school... "
            l " We just gotta keep handling the pain of dealing with a lot of homework. "
            l " ...And a lot of activities and stuff. "
            l " And we gotta sometimes pray that there's going to be no class and all. "
            l " But, I have a secret! "
            l " You see, I go to this secret website and see what days there's going to be no class! "
            l " Don't tell anyone that, or else I'm gonna get in big trouble, eheh. "
            l " Apparently, the next time there's going to be no class is... "
            l " Next monday and tuesday! Which means, we're gonna be having a long weekend! "
            l " That's pretty great, isn't it? "
            " Well, yeah. If only this game had more than one week. "
            l " Too bad! "
            " Wait, did she just speak to me? "
            l " I mean, whaaat? I didn't say anything, not at all... "
            " ...Right. "
            play sound "audio/bellring.mp3"
            l " Oh! The bell has rang! "
            l " I swore these breaks were much longer... "
            l " But, whatever! I'll see you in class, [name]! "
            hide lananeutral at left with easeoutleft
            " ...You should probably go to class too. "
            scene black with dissolve
            pause 2.0
            jump languageclass2
        else:
            x " [name]!! HII HI HI!! " with vpunch
            " Geezes, does her voice usually get this loud when she's excited? "
            x " It's nice to see you here! "
            x " Wait wait, I just realized! I haven't introduced myself! "
            x " I'm so sorry! "
            $ lanaknow = True
            l " I'm Lana! It's nice to meet you! "
            l " Anyway... "
            l " I was kinda just thinking about a few things, mainly school stuff... "
            hide lananeutral at bottom
            show lanaangry at center
            l " Like, we've got a lot of things to do! A lot of homework... "
            l " You're lucky you don't get to do those kinds of stuff, [name]... "
            l " Since you're new and all... "
            hide lanaangry at bottom
            show lananeutral at center
            l " But then again, this IS school... "
            l " We just gotta keep handling the pain of dealing with a lot of homework. "
            l " ...And a lot of activities and stuff. "
            l " And we gotta sometimes pray that there's going to be no class and all. "
            l " But, I have a secret! "
            l " You see, I go to this secret website and see what days there's going to be no class! "
            l " Don't tell anyone that, or else I'm gonna get in big trouble, eheh. "
            l " Apparently, the next time there's going to be no class is... "
            l " Next monday and tuesday! Which means, we're gonna be having a long weekend! "
            l " That's pretty great, isn't it? "
            " Well, yeah. If only this game had more than one week. "
            l " Too bad! "
            " Wait, did she just speak to me? "
            l " I mean, whaaat? I didn't say anything, not at all... "
            " ...Right. "
            play sound "audio/bellring.mp3"
            l " Oh! The bell has rang! "
            l " I swore these breaks were much longer... "
            l " But, whatever! I'll see you in class, [name]! "
            hide lananeutral at left with easeoutleft
            " ...You should probably go to class too. "
            scene black with dissolve
            pause 2.0
            jump languageclass2
    label zipcafeint:
        # zip recognizes you
        if oligangknow == True:
            " You decided to sit next to Zip. "
        else:
            " You decided to sit next to the mean looking girl. "
        show zipneutral at center with dissolve
        if oligangknow == True:
            z " ... "
            hide zipneutral at bottom
            show zipangry at center
            z " Oh geez, is a loser really sitting next to me - "
            hide zipangry at bottom
            show zipconfused at center
            z " Wait, hey... I recognize yer ass! "
            hide zipconfused at bottom
            show zipangry at center
            z " You're the one that got Oliver suspended! "
            z " You little fucking prick... "
            z " ... "
            z " ...You know, you could've done something else than beat Oliver up. "
            z " Like, I don't know, call a teacher? "
            z " You just HAD to decide that you were gonna go up and beat him. "
            z " We were just having fun! It's not like we were hurting that kid's feelings... "
            z " I'm sure he was probably enjoying us doing all that to him, like the sick freak that he is. "
            " ... "
            stop music
            hide zipangry at bottom
            show zipconfused at center
            mc " How about you shut up before I rip your body to pieces, cook you, and then feed you to your family. " with vpunch
            z " ...! "
            " ...That has to be the first time you've ever actually spoken. "
            z " ... "
            z " ..Jeez, alright, I'll leave you alone, god damn... "
            scene black with dissolve
            " Zip left you alone for the rest of the break. "
            " You just sort of sat there and looked at your phone, but, everynow and then... "
            " You could see that Zip, from the corner of your eye... "
            " ...She kept glancing at you, but everytime you noticed, she would look away nervously. "
            " Guess your words really just scared her, huh? "
            " ...Wait, how are you even gonna cook paper? "
            play music "audio/paperhigh.mp3" fadein 0.5
            " ...Well, whatever. Game logic, I suppose. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, and you get up from your seat. "
            " It's time to go to class. "
            pause 2.0
            jump languageclass2
        else:
            x " ... "
            hide zipneutral at bottom
            show zipangry at center
            x " Oh geez, is a loser really sitting next to me - "
            x " Hey, you're not really supposed to sit next to me, you know. "
            x " Someone else is supposed to sit where you're sitting right now. "
            x " Shoo! Go away! Shoo! "
            x " I don't want your loser germs to get on me, you know. "
            x " Go away! I'm not in the mood to deal with this! "
            hide zipangry at left with easeoutleft
            " You got up and decided to sit on an empty table. "
            " Time to scroll on tiktok to pass time... "
            scene black with dissolve
            " You decided to scroll on tiktok to pass time. "
            " You sort of wondered for a bit, what was that girls problem? "
            " You never really did anything, so why was she so upset? "
            " ...Eh, you probably shouldn't think too much about it. "
            " You just gotta relax for a bit. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, and you get up from your seat. "
            " You then go back to your classroom for your next class. "
            pause 2.0
            jump languageclass2
label tuesdayrooftop1:
    # Riley + Robby
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walk up to the rooftop so that you could get some fresh air. "
    " After a bit of walking around the rooftop, youspotted two of your classmates just hanging out with eachother. "
    " Wanting to talk to them, you decided to walk up to them to see what they're talking about. "
    show rileyneutral at left with easeinright
    show robbyneutral at right with easeinright
    if rileyknow == True and robbyknow == True:
        ri " Oooh Robbyyyyyy!!! "
        rb " What do you want now, Riley.. "
        ri " Noothing...I just have this small question. "
        rb " ...You better make it quick, I'm trying to study over here. "
        ri " Pff, you nerd! "
        ri " Anyway... "
        ri " What do you think are the chances offffff... "
        hide rileyneutral at bottom
        show rileyhappy at left
        ri " ...Oliver falling inlove with me?? "
        rb " ... "
        rb " Really...? That's your question...? "
        rb " Riley, I don't have time to answer these stupid questions... "
        rb " How about you ask [name] over there instead? "
        hide rileyhappy at bottom
        show rileyneutral at left
        ri " Okeyyy!! "
        show rileyneutral at center with move
        ri " [name], what do you think are the chances of Oliver falling in love with me? "
        " You think about the question given to you for a bit... "
        if kind == True:
            " You honestly didn't want to hurt her feelings, so... "
            " You just told her that the chances were very high. "
            " You also wished Riley good luck into confessing her feelings to Oliver. "
            hide rileyneutral at bottom
            show rileyhappy at center
            ri " Wow!! Thanks, [name]!! "
            ri "I hope you can find someone to love too! "
            " Well, too bad. This game is about friendship. "
            " This isn't a dating sim, gang! "
        elif calm == True:
            " Well, you didn't really want to hurt her feelings, but... "
            " You also got to tell her the truth. "
            " You just decided to tell her that there's a 50% he will, but also a 50% chance he wont. "
            "That way, you're both lying and telling the truth. "
            ri " Hm... Okay! "
            ri "I hope I'll get the 50% where he'll love me! "
        elif mean == True:
            " You just decided to tell her bluntly that there's absolutely no chance that Oliver would fall in love with her. "
            "I mean, you're just telling her the truth right? "
            hide rileyneutral at bottom
            show rileysad at center
            ri " ...Oh. "
            " ...Well shucks she's upset! "
        scene black with dissolve
        " You spent the entire break talking to Robby and Riley. "
        " Well, mainly talking to Riley since you didn't want to disturb Robby's studying. "
        " You were just vibing. "
        if kind == True:
            " ...And listening to Riley yap about Oliver. "
            " You didn't mind, though. "
        elif calm == True:
            " ...And listening to Riley yap about Oliver. "
            " You didn't mind, though. "
        elif mean == True:
            " ...And trying to teach Riley that not everyone will fall in love with her. "
            " Sometimes, telling someone the truth isthe best option. "
        play sound "audio/bellring.mp3"
        " The bell rings a few minutes later, meaning that it was time for the next class. "
        " You walked down from the rooftop so that you can go back to your classroom for the next class. "
        pause 2.0
        jump languageclass2
    elif rileyknow == True and robbyknow == False:
        ri " Oooh Robbyyyyyy!!! "
        x " What do you want now, Riley.. "
        ri " Noothing...I just have this small question. "
        x " ...You better make it quick, I'm trying to study over here. "
        ri " Pff, you nerd! "
        ri " Anyway... "
        ri " What do you think are the chances offffff... "
        hide rileyneutral at bottom
        show rileyhappy at left
        ri " ...Oliver falling inlove with me?? "
        x " ... "
        x " Really...? That's your question...? "
        x " Riley, I don't have time to answer these stupid questions... "
        x " How about you ask [name] over there instead? "
        hide rileyhappy at bottom
        show rileyneutral at left
        ri " Okeyyy!! "
        show rileyneutral at center with move
        ri " [name], what do you think are the chances of Oliver falling in love with me? "
        " You think about the question given to you for a bit... "
        if kind == True:
            " You honestly didn't want to hurt her feelings, so... "
            " You just told her that the chances were very high. "
            " You also wished Riley good luck into confessing her feelings to Oliver. "
            hide rileyneutral at bottom
            show rileyhappy at center
            ri " Wow!! Thanks, [name]!! "
            ri "I hope you can find someone to love too! "
            " Well, too bad. This game is about friendship. "
            " This isn't a dating sim, gang! "
        elif calm == True:
            " Well, you didn't really want to hurt her feelings, but... "
            " You also got to tell her the truth. "
            " You just decided to tell her that there's a 50% he will, but also a 50% chance he wont. "
            "That way, you're both lying and telling the truth. "
            ri " Hm... Okay! "
            ri "I hope I'll get the 50% where he'll love me! "
        elif mean == True:
            " You just decided to tell her bluntly that there's absolutely no chance that Oliver would fall in love with her. "
            "I mean, you're just telling her the truth right? "
            hide rileyneutral at bottom
            show rileysad at center
            ri " ...Oh. "
            " ...Well shucks she's upset! "
        scene black with dissolve
        " You spent the entire break talking to the boy and Riley. "
        $ robbyknow = True
        " You learnt that the boys name was Robby. "
        " You were mainly talking to Riley since you didn't want to disturb Robby's studying. "
        " You were just vibing. "
        if kind == True:
            " ...And listening to Riley yap about Oliver. "
            " You didn't mind, though. "
        elif calm == True:
            " ...And listening to Riley yap about Oliver. "
            " You didn't mind, though. "
        elif mean == True:
            " ...And trying to teach Riley that not everyone will fall in love with her. "
            " Sometimes, telling someone the truth isthe best option. "
        play sound "audio/bellring.mp3"
        " The bell rings a few minutes later, meaning that it was time for the next class. "
        " You walked down from the rooftop so that you can go back to your classroom for the next class. "
        pause 2.0
        jump languageclass2
    elif rileyknow == True and robbyknow == False:
        x " Oooh Robbyyyyyy!!! "
        rb " What do you want now, Riley.. "
        x " Noothing...I just have this small question. "
        rb " ...You better make it quick, I'm trying to study over here. "
        x " Pff, you nerd! "
        x " Anyway... "
        x " What do you think are the chances offffff... "
        hide rileyneutral at bottom
        show rileyhappy at left
        x " ...Oliver falling inlove with me?? "
        rb " ... "
        rb " Really...? That's your question...? "
        rb " Riley, I don't have time to answer these stupid questions... "
        rb " How about you ask [name] over there instead? "
        hide rileyhappy at bottom
        show rileyneutral at left
        x " Okeyyy!! "
        show rileyneutral at center with move
        x " [name], what do you think are the chances of Oliver falling in love with me? "
        " You think about the question given to you for a bit... "
        if kind == True:
            " You honestly didn't want to hurt her feelings, so... "
            " You just told her that the chances were very high. "
            " You also wished Riley good luck into confessing her feelings to Oliver. "
            hide rileyneutral at bottom
            show rileyhappy at center
            x " Wow!! Thanks, [name]!! "
            x "I hope you can find someone to love too! "
            " Well, too bad. This game is about friendship. "
            " This isn't a dating sim, gang! "
        elif calm == True:
            " Well, you didn't really want to hurt her feelings, but... "
            " You also got to tell her the truth. "
            " You just decided to tell her that there's a 50% he will, but also a 50% chance he wont. "
            "That way, you're both lying and telling the truth. "
            x " Hm... Okay! "
            x "I hope I'll get the 50% where he'll love me! "
        elif mean == True:
            " You just decided to tell her bluntly that there's absolutely no chance that Oliver would fall in love with her. "
            "I mean, you're just telling her the truth right? "
            hide rileyneutral at bottom
            show rileysad at center
            x " ...Oh. "
            " ...Well shucks she's upset! "
        scene black with dissolve
        " You spent the entire break talking to Robby and the girl. "
        $ rileyknow = True
        " You learnt that the girls name was Riley. "
        " You were mainly talking to Riley since you didn't want to disturb Robby's studying. "
        " You were just vibing. "
        if kind == True:
            " ...And listening to Riley yap about Oliver. "
            " You didn't mind, though. "
        elif calm == True:
            " ...And listening to Riley yap about Oliver. "
            " You didn't mind, though. "
        elif mean == True:
            " ...And trying to teach Riley that not everyone will fall in love with her. "
            " Sometimes, telling someone the truth isthe best option. "
        play sound "audio/bellring.mp3"
        " The bell rings a few minutes later, meaning that it was time for the next class. "
        " You walked down from the rooftop so that you can go back to your classroom for the next class. "
        pause 2.0
        jump languageclass2
    else:
        x " Oooh Robbyyyyyy!!! "
        x " What do you want now, Riley.. "
        x " Noothing...I just have this small question. "
        x " ...You better make it quick, I'm trying to study over here. "
        x " Pff, you nerd! "
        x " Anyway... "
        x " What do you think are the chances offffff... "
        hide rileyneutral at bottom
        show rileyhappy at left
        x " ...Oliver falling inlove with me?? "
        x " ... "
        x " Really...? That's your question...? "
        x " Riley, I don't have time to answer these stupid questions... "
        x " How about you ask [name] over there instead? "
        hide rileyhappy at bottom
        show rileyneutral at left
        x " Okeyyy!! "
        show rileyneutral at center with move
        x " [name], what do you think are the chances of Oliver falling in love with me? "
        " You think about the question given to you for a bit... "
        if kind == True:
            " You honestly didn't want to hurt her feelings, so... "
            " You just told her that the chances were very high. "
            " You also wished Riley good luck into confessing her feelings to Oliver. "
            hide rileyneutral at bottom
            show rileyhappy at center
            x " Wow!! Thanks, [name]!! "
            x "I hope you can find someone to love too! "
            " Well, too bad. This game is about friendship. "
            " This isn't a dating sim, gang! "
        elif calm == True:
            " Well, you didn't really want to hurt her feelings, but... "
            " You also got to tell her the truth. "
            " You just decided to tell her that there's a 50% he will, but also a 50% chance he wont. "
            "That way, you're both lying and telling the truth. "
            x " Hm... Okay! "
            x "I hope I'll get the 50% where he'll love me! "
        elif mean == True:
            " You just decided to tell her bluntly that there's absolutely no chance that Oliver would fall in love with her. "
            "I mean, you're just telling her the truth right? "
            hide rileyneutral at bottom
            show rileysad at center
            x " ...Oh. "
            " ...Well shucks she's upset! "
        scene black with dissolve
        " You spent the entire break talking to the boy and the girl. "
        $ robbyknow = True
        $ rileyknow = True
        " You learnt that the boys name was Robby, and that the girls name was Riley. "
        " You were mainly talking to Riley since you didn't want to disturb Robby's studying. "
        " You were just vibing. "
        if kind == True:
            " ...And listening to Riley yap about Oliver. "
            " You didn't mind, though. "
        elif calm == True:
            " ...And listening to Riley yap about Oliver. "
            " You didn't mind, though. "
        elif mean == True:
            " ...And trying to teach Riley that not everyone will fall in love with her. "
            " Sometimes, telling someone the truth isthe best option. "
        play sound "audio/bellring.mp3"
        " The bell rings a few minutes later, meaning that it was time for the next class. "
        " You walked down from the rooftop so that you can go back to your classroom for the next class. "
        pause 2.0
        jump languageclass2
label tuesdaylibrary1:
    # kevin + cubbie
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library just to get some nice peace and quiet. "
    " You walked around for a bit and found two of your classmates just hanging out. "
    " Curious on what they're doing, you walked up to them. "
    show kevinneutral at left with easeinright
    show cubbieneutral at right with easeinright
    if kevinknow == True and cubbieknow == True:
        kv " Cubbie, your body is a pencil sharpener, yes? "
        cb " ...? "
        kv " ...  What if someone were to grab a pencil and - {nw}"
        hide cubbieneutral at bottom
        show cubbieangry at right
        cb " !!! " with vpunch
        hide kevinneutral at bottom
        show kevinsurprised at left
        kv " I apologize, I was only curious. "
        hide kevinsurprised at bottom
        show kevinneutral at left
        kv " Has anyone tried to ...you know, do that to you before though? "
        kv " Just asking out of curiousity. "
        hide cubbieangry at bottom
        show cubbieneutral at right
        cb " ... "
        kv " No one? well, that's good. "
        kv " I can imagine that it wouldn't be a pleasant feeling, considering how sharp pencils can get. "
        kv " I hope no one tries to do that to you in the future as well... "
        kv " If anyone ever does, you should tell a teacher immediately. Alright? "
        cb " ... "
        scene black with dissolve
        " ...Well that was quite the interesting conversation you just heard. "
        " You actually want to try doing that to Cubbie, but that would be too evil. "
        " Plus, you didn't want to get in trouble. This is literally your second day here. "
        " You've gotta keep the good act going. "
        " You just decided to walk around the library, since they didn't really notice that you were there. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit of checking other books inside the library. "
        " You put the books you checked out back into their original places (as if you remember where they even were in the first place)... "
        " ...And you then walked back to your classroom. "
        pause 2.0
        jump languageclass2
    elif kevinknow == True and cubbieknow == False:
        kv " Cubbie, your body is a pencil sharpener, yes? "
        x " ...? "
        kv " ...  What if someone were to grab a pencil and - {nw}"
        hide cubbieneutral at bottom
        show cubbieangry at right
        x " !!! " with vpunch
        hide kevinneutral at bottom
        show kevinsurprised at left
        kv " I apologize, I was only curious. "
        hide kevinsurprised at bottom
        show kevinneutral at left
        kv " Has anyone tried to ...you know, do that to you before though? "
        kv " Just asking out of curiousity. "
        hide cubbieangry at bottom
        show cubbieneutral at right
        x " ... "
        kv " No one? well, that's good. "
        kv " I can imagine that it wouldn't be a pleasant feeling, considering how sharp pencils can get. "
        kv " I hope no one tries to do that to you in the future as well... "
        kv " If anyone ever does, you should tell a teacher immediately. Alright? "
        x " ... "
        scene black with dissolve
        " ...Well that was quite the interesting conversation you just heard. "
        " You actually want to try doing that to that cat guy, but that would be too evil. "
        " Plus, you didn't want to get in trouble. This is literally your second day here. "
        " You've gotta keep the good act going. "
        " You just decided to walk around the library, since they didn't really notice that you were there. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit of checking other books inside the library. "
        " You put the books you checked out back into their original places (as if you remember where they even were in the first place)... "
        " ...And you then walked back to your classroom. "
        pause 2.0
        jump languageclass2
    elif kevinknow == False and cubbieknow == True:
        x " Cubbie, your body is a pencil sharpener, yes? "
        cb " ...? "
        x " ...  What if someone were to grab a pencil and - {nw}"
        hide cubbieneutral at bottom
        show cubbieangry at right
        cb " !!! " with vpunch
        hide kevinneutral at bottom
        show kevinsurprised at left
        x " I apologize, I was only curious. "
        hide kevinsurprised at bottom
        show kevinneutral at left
        x " Has anyone tried to ...you know, do that to you before though? "
        x " Just asking out of curiousity. "
        hide cubbieangry at bottom
        show cubbieneutral at right
        cb " ... "
        x " No one? well, that's good. "
        x " I can imagine that it wouldn't be a pleasant feeling, considering how sharp pencils can get. "
        x " I hope no one tries to do that to you in the future as well... "
        x " If anyone ever does, you should tell a teacher immediately. Alright? "
        cb " ... "
        scene black with dissolve
        " ...Well that was quite the interesting conversation you just heard. "
        " You actually want to try doing that to Cubbie, but that would be too evil. "
        " Plus, you didn't want to get in trouble. This is literally your second day here. "
        " You've gotta keep the good act going. "
        " You just decided to walk around the library, since they didn't really notice that you were there. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit of checking other books inside the library. "
        " You put the books you checked out back into their original places (as if you remember where they even were in the first place)... "
        " ...And you then walked back to your classroom. "
        pause 2.0
        jump languageclass2
    else:
        x " Cubbie, your body is a pencil sharpener, yes? "
        x " ...? "
        x " ...  What if someone were to grab a pencil and - {nw}"
        hide cubbieneutral at bottom
        show cubbieangry at right
        x " !!! " with vpunch
        hide kevinneutral at bottom
        show kevinsurprised at left
        x " I apologize, I was only curious. "
        hide kevinsurprised at bottom
        show kevinneutral at left
        x " Has anyone tried to ...you know, do that to you before though? "
        x " Just asking out of curiousity. "
        hide cubbieangry at bottom
        show cubbieneutral at right
        x " ... "
        x " No one? well, that's good. "
        x " I can imagine that it wouldn't be a pleasant feeling, considering how sharp pencils can get. "
        x " I hope no one tries to do that to you in the future as well... "
        x " If anyone ever does, you should tell a teacher immediately. Alright? "
        x " ... "
        scene black with dissolve
        " ...Well that was quite the interesting conversation you just heard. "
        " You actually want to try doing that to that cat guy, but that would be too evil. "
        " Plus, you didn't want to get in trouble. This is literally your second day here. "
        " You've gotta keep the good act going. "
        " You just decided to walk around the library, since they didn't really notice that you were there. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit of checking other books inside the library. "
        " You put the books you checked out back into their original places (as if you remember where they even were in the first place)... "
        " ...And you then walked back to your classroom. "
        pause 2.0
        jump languageclass2
label languageclass2:
    scene classroom with dissolve
    " You sat down on your seat and waited for the language teacher to arrive. "
    " ...Taking her a bit more longer than usual. "
    " Eventually, she comes in with a lot of papers in her hands. "
    show msthravelneutral at center with easeinright
    mst " Hello, class! I apologize for being a bit late. "
    mst " But, instead of having a lesson, I decided that we're all going to have a fun activity! "
    mst " Just answer these papers and then you'll be done. "
    mst " It's nothing too hard, don't worry! "
    mst " Now I HOPE that you all have been taking your duolingo spanish classes! "
    mst " This will all be about spanish words and stuff!!! "
    " ...We were supposed to download duolingo??????? "
    " Well, you most certainly haven't done your spanish lessons. "
    " Spanish or vanish, as they say... and you're pretty much ready to vanish. "
    " Sorry duolingo bird. "
    " Anywho, Miss Thavel starts giving out papers to you and your classmates. "
    mst " All of you better be done once this class is over! "
    mst " Now, I have to go work on other duties... "
    mst " Better stay nice and quiet while I'm out! "
    mst " Your time to start answering those papers starts NOW! "
    hide msthravelneutral at right with easeoutright
    " ...The classroom was not quiet at all once Miss Thavel left. "
    " You should probably start answering instead of talking to your other classmates. "
    " You look at your paper and there's about 15 questions. "
    " Alright, let's do this... Even though you don't know how to answer most of these questions. "
    " Number 1: Conjugate haber in the pluscuamperfecto. "
    " You...didn't even understand what that means. "
    " Atleast there's multiple options. "
    menu:
        " A. Yo he ":
            " You're having second thoughts on this option. "
            " Oh well, you already answered with your pen. Can't erase that now. "
            jump language1
        " B. Yo habia ":
            " Yeah, that seems about right. "
            " Let's keep going. "
            jump language1
        " C. Yo habiera ":
            " You're having second thoughts on this option. "
            " Oh well, you already answered with your pen. Can't erase that now. "
            jump language1
    label language1:
        " Number 2: Correct the sentence; "
        " Mis hermana fue a la tienda y compraron pan. "
        menu:
            " A. Mis hermana fueron a la tienda y compraron pan.  ":
                " You're having second thoughts on this option. "
                " Oh well, you already answered with your pen. Can't erase that now. "
                jump language2
            " B. Mi hermana fue a la tienda y compro pan. ":
                " Yeah, that seems about right. "
                " Let's keep going. "
                jump language2
            " C. Mis hermana fue a la tienda y compro pan. ":
                " You're having second thoughts on this option. "
                " Oh well, you already answered with your pen. Can't erase that now. "
                jump language2
        label language2:
            " Number 3: Translate the sentence; "
            " If I had studied more, I would've passed the exam easily. "
            menu:
                " A. Si estudiara mas, pasare el examen facilmente. ":
                    " You're having second thoughts on this option. "
                    " Oh well, you already answered with your pen. Can't erase that now. "
                    jump language3
                " B. Si estudiare mas, hubiera pasado el examen facilmente. ":
                    " You're having second thoughts on this option. "
                    " Oh well, you already answered with your pen. Can't erase that now. "
                    jump language3
                " C. Si hubiera estudiado mas, habria pasado el examen facilmente. ":
                    " Yeah, that seems about right. "
                    " Let's keep going. "
                    jump language3
            label language3:
                " Number 4: What's an example of 'estar' being used correctly? "
                menu:
                    " El libro esta sobre la mesa. ":
                        " Yeah, that seems about right. "
                        " Let's keep going. "
                        jump language4
                    " Ella esta doctora. ":
                        " You're having second thoughts on this option. "
                        " Oh well, you already answered with your pen. Can't erase that now. "
                        jump language4
                    " El coche es en el goraje. ":
                        " You're having second thoughts on this option. "
                        " Oh well, you already answered with your pen. Can't erase that now. "
                        jump language4
                label language4:
                    " Number 5: Rewrite this sentence using pronouns; "
                    " Juan dio el libro a Maria. "
                    menu:
                        " Juan le dio lo. ":
                            " You're having second thoughts on this option. "
                            " Oh well, you already answered with your pen. Can't erase that now. "
                            jump language5
                        " Juan se lo dio. ":
                            " Yeah, that seems about right. "
                            " Let's keep going. "
                            jump language5
                        " Juan la dio a Maria. ":
                            " You're having second thoughts on this option. "
                            " Oh well, you already answered with your pen. Can't erase that now. "
                            jump language5
                    label language5:
                        " While answering number 9, you were honestly feeling a bit tired of answering. "
                        if abblana == True:
                            " While you were thinking, Abbie gently poked you to ask a question. "
                            show abbieneutral at center with easeinleft
                            a " ...Hey, um...[name]..? "
                            a " ...I'm sorry if I'm bothering you, but... "
                            a " Do you happen to know the answer to number 3...? "
                            menu:
                                " I don't know, A? ":
                                    a " Okay...thank you, [name]... "
                                    hide abbieneutral at left with easeoutleft
                                    " Anyway... "
                                    jump option2
                                " I don't know, B? ":
                                    a " Okay...thank you, [name]... "
                                    hide abbieneutral at left with easeoutleft
                                    " Anyway... "
                                    jump option2
                                " I don't know, C? ":
                                    a " Okay...thank you, [name]... "
                                    hide abbieneutral at left with easeoutleft
                                    " Anyway... "
                                    jump option2
                        else:
                            jump option2
                        label option2:
                            " You were thinking about speedrunning answering or just not answering at all. "
                            " But then again, you should answer so that the teacher doesn't get angry at you. "
                            " What will you do? "
                            menu:
                                " Actually answer ":
                                    " Alright, nerd. "
                                    " Not like you'll get all of them correct, anyway... "
                                    scene black with dissolve
                                    " You spent the rest of the class answering the activity left by Miss Thavel. "
                                    " Once you were done, you placed your paper down onto the teacher's desk and you were allowed to go out. "
                                    pause 2.0
                                    jump tuesdaybreak2
                                " Speedrun answering ":
                                    " Yeah, be like me fr!! "
                                    " Okay so you just put A on some parts, B and C on some other parts... "
                                    scene black with dissolve
                                    " You spent the rest of the class speedrunning answering the activity left by Miss Thavel. "
                                    " Once you were done, you placed your paper down onto the teacher's desk and you were allowed to go out. "
                                    pause 2.0
                                    jump tuesdaybreak2
                                " Don't answer the rest and pass the paper already ":
                                    $ thavelmad1 = True
                                    " Oop. Alright. "
                                    scene black with dissolve
                                    " You decided not to answer the rest of the questions and you put your paper on Miss Thavel's desk. "
                                    " Once you were done, you placed your paper down onto the teacher's desk and you were allowed to go out. "
                                    " But wait, what's this? "
                                    " Looks like you got one 'mad' point. "
                                    " Everytime you do something that makes a teacher mad, that point will increase. "
                                    " Three points and it's over for you! "
                                    " Make sure those points dont increase...or just keep trying to make a specific teacher mad. I don't really care. "
                                    " You're gonna die. "
                                    pause 2.0
                                    jump tuesdaybreak2
label tuesdaybreak2:
    scene hallway with dissolve
    " It's the second break of the day and you're thinking about going somewhere else in the school. "
    " Where do you go? "
    menu:
        " {image=cubbieicon} The front of the school {image=skellicon} ":
            jump tuesdayfront2
        " {image=claireicon} The back of the school {image=claireicon} ":
            jump tuesdayback2
        " {image=rubyicon} The gym {image=kevinicon} ":
            jump tuesdaygym2
        " {image=popularicon} The cafeteria {image=bubbleicon} ":
            jump tuesdaycafeteria2
        " {image=engelicon} The rooftop {image=oligangicon} ":
            jump tuesdayrooftop2
        " {image=abbieicon} The library {image=rileyicon} ":
            jump tuesdaylibrary2

label tuesdayfront2:
    # cubbie and skell
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked out into the front of the school so that you could relax for a bit. "
    " You saw some other students talking and doing their own things... such as taking selfies, studying... "
    " ...Gaming. And of course those types of students who say they're straight and then act gay towards other students. "
    " Yep, this is the normal highschool expirience. "
    " Whilst you were just walking around, trying to find a place to sit, you spot two or your classmates just vibing. "
    " They were hanging out underneath a tree, and they were just...talking. "
    " You wanted to hang out with them since they looked cool, so, you walked up to them and sat next to them. "
    show skellneutral at left with easeinbottom
    show cubbieneutral at right with easeinbottom
    if skellknow == True and cubbieknow == True:
        sk " ...Hi [name]. "
        hide cubbieneutral at bottom
        show cubbiehappy at right
        " Cubbie seems happy to see you. "
        hide cubbiehappy at bottom
        show cubbieneutral at right
        sk " Me and Cubbie were just talking about stuff while listening to music. "
        " You asked Skell what kind of stuff he and Cubbie were talking about. "
        sk " You know, the boring stuff. "
        sk " Life. And our cringe choices in it. "
        sk " Like, what do you mean I used to have a phase where I howled at the moon...? "
        cb " ... "
        sk " Look, I had a wolf phase at the time. We listen and we don't judge here. "
        " We listen and we don't judge! "
        " Challenge: try to act as if you're not one of those people who argue over character pairings! "
        " ...Either you failed or passed that "
        sk " I don't even know why I had a wolf phase... "
        sk " I think it's cause I thought wolves were so cool at the time. But they're not really...that cool anymore. "
        sk " I think I still have my wolf t-shirts in my closet. "
        hide cubbieneutral at bottom
        show cubbiehappy at right
        cb " ... "
        sk " I'm not wearing one to school tomorrow. "
        cb " ...? "
        sk " Are you sure it would even fit on you? "
        cb " !!! "
        sk " ...you're really... "
        sk " ...Sigh, alright. I'll bring it tomorrow so that you can have it. "
        cb " :3!! "
        scene black with dissolve
        " You spent the rest of the break talking with Skell and Cubbie. "
        " They were honestly just pretty chill, joking around and stuff. "
        " Man, they're very much just chill guys. "
        " You keep on talking to them until the break was over. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, and you all get up to go back to the classroom for the next class. "
        pause 2.0
        jump scienceclass2
    elif skellknow == True and cubbieknow == False:
        sk " ...Hi [name]. "
        hide cubbieneutral at bottom
        show cubbiehappy at right
        " The cat looking fella seems happy to see you. "
        hide cubbiehappy at bottom
        show cubbieneutral at right
        sk " Oh, um... Cubbie, have you...introduced yourself to [name] before? "
        x " (*shakes head no*) "
        sk " Alright, I'll introduce you to [them] for you. "
        $ cubbieknow = True
        sk " [name], this is Cubbie. He can speak, but he just prefers not to. "
        " Cubbie does a little wave at you, and you did a little wave at him back. "
        " ...He looks really cute. "
        sk " ...Anyway... "
        sk " Me and Cubbie were just talking about stuff while listening to music. "
        " You asked Skell what kind of stuff he and Cubbie were talking about. "
        sk " You know, the boring stuff. "
        sk " Life. And our cringe choices in it. "
        sk " Like, what do you mean I used to have a phase where I howled at the moon...? "
        cb " ... "
        sk " Look, I had a wolf phase at the time. We listen and we don't judge here. "
        " We listen and we don't judge! "
        " Challenge: try to act as if you're not one of those people who argue over character pairings! "
        " ...Either you failed or passed that "
        sk " I don't even know why I had a wolf phase... "
        sk " I think it's cause I thought wolves were so cool at the time. But they're not really...that cool anymore. "
        sk " I think I still have my wolf t-shirts in my closet. "
        hide cubbieneutral at bottom
        show cubbiehappy at right
        cb " ... "
        sk " I'm not wearing one to school tomorrow. "
        cb " ...? "
        sk " Are you sure it would even fit on you? "
        cb " !!! "
        sk " ...you're really... "
        sk " ...Sigh, alright. I'll bring it tomorrow so that you can have it. "
        cb " :3!! "
        scene black with dissolve
        " You spent the rest of the break talking with Skell and Cubbie. "
        " They were honestly just pretty chill, joking around and stuff. "
        " Man, they're very much just chill guys. "
        " You keep on talking to them until the break was over. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, and you all get up to go back to the classroom for the next class. "
        pause 2.0
        jump scienceclass2
    elif skellknow == False and cubbieknow == True:
        x " ...Hi [name]. "
        hide cubbieneutral at bottom
        show cubbiehappy at right
        " Cubbie seems happy to see you. "
        hide cubbiehappy at bottom
        show cubbieneutral at right
        x " ...Oh, shoot. I forgot to introduce myself to you, I'm sorry. "
        x " Cubbie, have you met [name] before? "
        cb " (*nods*) "
        x " Alright... "
        $ skellknow = True
        sk " The name's Skell. It's nice to meet you. Hope you're having fun in this school...or whatever. "
        sk " Anywho... "
        sk " Me and Cubbie were just talking about stuff while listening to music. "
        " You asked Skell what kind of stuff he and Cubbie were talking about. "
        sk " You know, the boring stuff. "
        sk " Life. And our cringe choices in it. "
        sk " Like, what do you mean I used to have a phase where I howled at the moon...? "
        cb " ... "
        sk " Look, I had a wolf phase at the time. We listen and we don't judge here. "
        " We listen and we don't judge! "
        " Challenge: try to act as if you're not one of those people who argue over character pairings! "
        " ...Either you failed or passed that "
        sk " I don't even know why I had a wolf phase... "
        sk " I think it's cause I thought wolves were so cool at the time. But they're not really...that cool anymore. "
        sk " I think I still have my wolf t-shirts in my closet. "
        hide cubbieneutral at bottom
        show cubbiehappy at right
        cb " ... "
        sk " I'm not wearing one to school tomorrow. "
        cb " ...? "
        sk " Are you sure it would even fit on you? "
        cb " !!! "
        sk " ...you're really... "
        sk " ...Sigh, alright. I'll bring it tomorrow so that you can have it. "
        cb " :3!! "
        scene black with dissolve
        " You spent the rest of the break talking with Skell and Cubbie. "
        " They were honestly just pretty chill, joking around and stuff. "
        " Man, they're very much just chill guys. "
        " You keep on talking to them until the break was over. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, and you all get up to go back to the classroom for the next class. "
        pause 2.0
        jump scienceclass2
    else:
        x " ...Hi [name]. "
        hide cubbieneutral at bottom
        show cubbiehappy at right
        " The cat looking fella seems happy to see you. "
        hide cubbiehappy at bottom
        show cubbieneutral at right
        x " Ah, wait...I haven't introduced myself to you yet - wait... "
        x " Oh, um... Cubbie, have you...introduced yourself to [name] before? "
        x " (*shakes head no*) "
        x " Alright, I'll introduce you to [them] for you. "
        $ cubbieknow = True
        x " [name], this is Cubbie. He can speak, but he just prefers not to. "
        " Cubbie does a little wave at you, and you did a little wave at him back. "
        " ...He looks really cute. "
        $ skellknow = True
        sk " ...And I'm Skell. Hope you're having a good time in this school...or whatever. "
        sk " ...Anyway... "
        sk " Me and Cubbie were just talking about stuff while listening to music. "
        " You asked Skell what kind of stuff he and Cubbie were talking about. "
        sk " You know, the boring stuff. "
        sk " Life. And our cringe choices in it. "
        sk " Like, what do you mean I used to have a phase where I howled at the moon...? "
        cb " ... "
        sk " Look, I had a wolf phase at the time. We listen and we don't judge here. "
        " We listen and we don't judge! "
        " Challenge: try to act as if you're not one of those people who argue over character pairings! "
        " ...Either you failed or passed that "
        sk " I don't even know why I had a wolf phase... "
        sk " I think it's cause I thought wolves were so cool at the time. But they're not really...that cool anymore. "
        sk " I think I still have my wolf t-shirts in my closet. "
        hide cubbieneutral at bottom
        show cubbiehappy at right
        cb " ... "
        sk " I'm not wearing one to school tomorrow. "
        cb " ...? "
        sk " Are you sure it would even fit on you? "
        cb " !!! "
        sk " ...you're really... "
        sk " ...Sigh, alright. I'll bring it tomorrow so that you can have it. "
        cb " :3!! "
        scene black with dissolve
        " You spent the rest of the break talking with Skell and Cubbie. "
        " They were honestly just pretty chill, joking around and stuff. "
        " Man, they're very much just chill guys. "
        " You keep on talking to them until the break was over. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, and you all get up to go back to the classroom for the next class. "
        pause 2.0
        jump scienceclass2
label tuesdayback2:
    # claire- talking about a book she likes
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walk to the back of the school so that you could get some fresh air. "
    " After walking around to try and find a spot to sit down, you spot one of your classmates reading a book. "
    if mean == True and clairesorry == False:
        " Hold on, is that...Claire? "
        " ... "
        " You're sure that she doesn't want to talk to you. "
        " You just sit somewhere far from her. "
        " You're still too afraid to talk to her. "
        " You feel you're not worthy of even talking to her. "
        " ...Let's get your thoughts on something else. "
        " It's hard to think when she's around as you're reminded of your past actions, but... "
        " You try to think of the scenery around you. That calms you a bit. "
        " You listen to the birds chirping every now and then. "
        " Alright, you're starting to get a bit distracted. "
        " Though, a few questions pop up into your mind... "
        " When does a comet become a meteor? "
        " When does a candle become a blaze? "
        " When does a man become a monster? "
        " ...That was totally added in with no reason whatsoever. "
        " It's totally not a reference to a musical. "
        scene black with dissolve
        " You spent the rest of the break just vibing underneath a tree. "
        " While not paying attention to Claire. "
        " It's honestly pretty calming, being outside and listening to the birds chirping... "
        " Maybe you should go touch grass more often. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, meaning that your breaktime is over. "
        " You get up from where you were sitting and you walk back to your classroom for the next class. "
        pause 2.0
        jump scienceclass2
    else:
        " Curiousity got to you and you decided to sit next to them to see what they were reading about. "
        show claireneutral at center with easeinbottom
        if claireknow == True:
            c " hmhm... "
            c " Hey [name]! "
            c " I'm just reading this new book I got! "
            " You ask her what it's called and what it's about. "
            c " It's called {color=#4169e1}{a=https://www.webtoons.com/en/canvas/ghost-eyes/list?title_no=147330}Ghost Eyes{/a}{/color}! "
            c " It's kind of controversial from what I've heard, so I decided to check it out if it really was... "
            c " It's about this boy called Tobias who has, well...ghost eyes! "
            c " And, um... It's kind of hard for me to explain the lore of it right now... "
            c " ...Because some parts are not really understandable. "
            c " If you wanna read with me, you can! But uh... "
            c " Just a warning, this does have some sensitive topics in it. "
            c " Just tell me when you're uncomfortable and we can skip to the next page, alright? "
            " You nod your head. "
            c " Okay! Let's go back to the beginning so that you can get an idea of what the story's like.. "
            scene black with dissolve
            " You spent the rest of the break reading a book with Claire. "
            " She was right, there were some concerning parts in the book...there even was a warning at the very start. "
            " But, you didn't mind. You've read far worse that this. "
            " Like that one 'Boyfriends' comic you've seen. Eeeyuck. That one was horribly written. "
            " Plus everything was just stereotypes. You're never reading that thing again. "
            play sound "audio/bellring.mp3"
            " The bell rings, stopping you and Claire from reading at an...interesting page. "
            " Claire closes her book, you both then get up to go to your next class. "
            pause 2.0
            jump scienceclass2
        else:
            x " hmhm... "
            x " Oh, hey! You're that new kid, right? "
            x " I don't think I ever got to introduce myself to you, hehe. Sorry... "
            $ claireknow = True
            hide claireneutral at bottom
            show clairehappy at center
            c " I'm Claire! It's nice to meet you! "
            " You tell her that it was nice to meet her, and then you asked her what she was doing. "
            hide clairehappy at bottom
            show claireneutral at center
            c " I'm just reading this new book I got! "
            " You ask her what it's called and what it's about. "
            c " It's called {color=#4169e1}{a=https://www.webtoons.com/en/canvas/ghost-eyes/list?title_no=147330}Ghost Eyes{/a}{/color}! "
            c " It's kind of controversial from what I've heard, so I decided to check it out if it really was... "
            c " It's about this boy called Tobias who has, well...ghost eyes! "
            c " And, um... It's kind of hard for me to explain the lore of it right now... "
            c " ...Because some parts are not really understandable. "
            c " If you wanna read with me, you can! But uh... "
            c " Just a warning, this does have some sensitive topics in it. "
            c " Just tell me when you're uncomfortable and we can skip to the next page, alright? "
            " You nod your head. "
            c " Okay! Let's go back to the beginning so that you can get an idea of what the story's like.. "
            scene black with dissolve
            " You spent the rest of the break reading a book with Claire. "
            " She was right, there were some concerning parts in the book...there even was a warning at the very start. "
            " But, you didn't mind. You've read far worse that this. "
            " Like that one 'Boyfriends' comic you've seen. Eeeyuck. That one was horribly written. "
            " Plus everything was just stereotypes. You're never reading that thing again. "
            play sound "audio/bellring.mp3"
            " The bell rings, stopping you and Claire from reading at an...interesting page. "
            " Claire closes her book, you both then get up to go to your next class. "
            pause 2.0
            jump scienceclass2
label tuesdaygym2:
    # Ruby and Kevin - talking about errors
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walk into the gym and started trying to find a place for you to sit. "
    " Whilst looking around, you find two of your classmates talking with eachother. "
    " You decided to walk up to them and sit next to them just because you wanna know what they're talking about. "
    show rubyneutral at left with easeinright
    show kevinneutral at right with easeinright
    if rubyknow == True and kevinknow == True:
        ru " Hello, [name]! - "
        hide rubyneutral at bottom
        show rubysad at left
        ru " Agh, there I go again... " with vpunch
        " You ask her what's wrong. "
        ru " I'm sorry, I'm overheating quite a bit right now... "
        ru " I've been overheating a lot today, and I don't know why! "
        kv " Hmm... you really don't know why? "
        ru " Yes! It all started this morning... "
        kv " ...Then I can get you to Robby and see if he can fix you. "
        kv " I do know how you robots work, but I don't know how to fix you like Robby does. "
        kv " How about you have a talk with him once school's done? "
        ru " Mmm... I don't know if I can last that long, but alright... "
        ru " I just hope my overheating doesn't get too bad to the point I start crashing... "
        kv " Mhm. Hopefully. "
        hide rubysad at bottom
        show rubyneutral at left
        ru " ...How about we change the topic to lighten the mood? "
        kv " Uh, alright...let me think. "
        scene black with dissolve
        " You spent the rest of the break talking about errors with Ruby and Kevin. "
        " It was pretty interesting to hear about the amount of errors Ruby had... "
        " ...She really needs to get more fixing, you don't even know how she's functioning right now. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, indicating that the break was over and it was time for class. "
        " You all get up from where you all were sitting and went back to the classroom. "
        " ...While making sure Ruby was alright. "
        pause 2.0
        jump scienceclass2
    elif rubyknow == True and kevinknow == False:
        ru " Hello, [name]! - "
        hide rubyneutral at bottom
        show rubysad at left
        ru " Agh, there I go again... " with vpunch
        " You ask her what's wrong. "
        ru " I'm sorry, I'm overheating quite a bit right now... "
        ru " I've been overheating a lot today, and I don't know why! "
        x " Hmm... you really don't know why? "
        ru " Yes! It all started this morning... "
        x " ...Then I can get you to Robby and see if he can fix you. "
        x " I do know how you robots work, but I don't know how to fix you like Robby does. "
        x " How about you have a talk with him once school's done? "
        ru " Mmm... I don't know if I can last that long, but alright... "
        ru " I just hope my overheating doesn't get too bad to the point I start crashing... "
        x " Mhm. Hopefully. "
        hide rubysad at bottom
        show rubyneutral at left
        ru " ...How about we change the topic to lighten the mood? "
        x " Uh, alright...let me think. "
        scene black with dissolve
        " You spent the rest of the break talking about errors with Ruby and the other guy. "
        " It was pretty interesting to hear about the amount of errors Ruby had... "
        " ...She really needs to get more fixing, you don't even know how she's functioning right now. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, indicating that the break was over and it was time for class. "
        " You all get up from where you all were sitting and went back to the classroom. "
        " ...While making sure Ruby was alright. "
        pause 2.0
        jump scienceclass2
    elif rubyknow == False and kevinknow == True:
        x " Hello, [name]! - "
        hide rubyneutral at bottom
        show rubysad at left
        x " Agh, there I go again... " with vpunch
        " You ask her what's wrong. "
        x " I'm sorry, I'm overheating quite a bit right now... "
        x " I've been overheating a lot today, and I don't know why! "
        kv " Hmm... you really don't know why? "
        x " Yes! It all started this morning... "
        kv " ...Then I can get you to Robby and see if he can fix you. "
        kv " I do know how you robots work, but I don't know how to fix you like Robby does. "
        kv " How about you have a talk with him once school's done? "
        x " Mmm... I don't know if I can last that long, but alright... "
        x " I just hope my overheating doesn't get too bad to the point I start crashing... "
        kv " Mhm. Hopefully. "
        hide rubysad at bottom
        show rubyneutral at left
        x " ...How about we change the topic to lighten the mood? "
        kv " Uh, alright...let me think. "
        scene black with dissolve
        " You spent the rest of the break talking about errors with the girl and Kevin. "
        " It was pretty interesting to hear about the amount of errors the girl had... "
        " ...She really needs to get more fixing, you don't even know how she's functioning right now. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, indicating that the break was over and it was time for class. "
        " You all get up from where you all were sitting and went back to the classroom. "
        " ...While making sure the girl was alright. "
        pause 2.0
        jump scienceclass2
    else:
        x " Hello, [name]! - "
        hide rubyneutral at bottom
        show rubysad at left
        x " Agh, there I go again... " with vpunch
        " You ask her what's wrong. "
        x " I'm sorry, I'm overheating quite a bit right now... "
        x " I've been overheating a lot today, and I don't know why! "
        x " Hmm... you really don't know why? "
        x " Yes! It all started this morning... "
        x " ...Then I can get you to Robby and see if he can fix you. "
        x " I do know how you robots work, but I don't know how to fix you like Robby does. "
        x " How about you have a talk with him once school's done? "
        x " Mmm... I don't know if I can last that long, but alright... "
        x " I just hope my overheating doesn't get too bad to the point I start crashing... "
        x " Mhm. Hopefully. "
        hide rubysad at bottom
        show rubyneutral at left
        x " ...How about we change the topic to lighten the mood? "
        x " Uh, alright...let me think. "
        scene black with dissolve
        " You spent the rest of the break talking about errors with the girl and the other guy. "
        " It was pretty interesting to hear about the amount of errors the girl had... "
        " ...She really needs to get more fixing, you don't even know how she's functioning right now. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, indicating that the break was over and it was time for class. "
        " You all get up from where you all were sitting and went back to the classroom. "
        " ...While making sure the girl was alright. "
        pause 2.0
        jump scienceclass2
label tuesdaycafeteria2:
    # petunia lizzy and bubble
    # petunia and lizzy talking about gaining followers
    # bubble talking about favorite kinds of ducks
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walk into the cafeteria and spotted a few of your classmates talking with eachother or just vibing. "
    " You're thinking of talking to them, but who do you talk to? "
    if popularknow == True and bubbleknow == True:
        menu:
            " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                jump populartalkyeah
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump bubbletalkyeah
    elif popularknow == True and bubbleknow == False:
        menu:
            " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                jump populartalkyeah
            " {image=bubbleicon} A girl with a duck on her head {image=bubbleicon} ":
                jump bubbletalkyeah
    elif popularknow == False and bubbleknow == True:
        menu:
            " {image=popularicon} Some popular looking girls {image=popularicon} ":
                jump populartalkyeah
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump bubbletalkyeah
    else:
        menu:
            " {image=popularicon} Some popular looking girls {image=popularicon} ":
                jump populartalkyeah
            " {image=bubbleicon} A girl with a duck on her head {image=bubbleicon} ":
                jump bubbletalkyeah
    label populartalkyeah:
        show petunianeutral at left with easeinright
        show lizzyneutral at right with easeinright
        if popularknow == True:
            p " Heeey girlie!! "
            " Heeey!! ^_^ "
            lz " Hi, [name]. "
            p " So, we've actually got some news for you! "
            " Well this is interesting. "
            p " We've been getting more followers recently! "
            lz " Isn't that great? "
            " You nodded your head, then you asked them how much followers they have now. "
            p " We've got 30 new followers! It's not a lot, but it's something, right? "
            lz " Mhm. We should post more frequently to gain more followers. "
            " You ask them what type of content they make. "
            p " What type of content we make? Oh, you know... "
            hide petunianeutral at bottom
            show petuniahappy at left
            p " I like to make videos of myself dancing to trending songs! "
            lz " And I like to make videos of myself singing. "
            hide petuniahappy at bottom
            show petuniaconfused at left
            p " ...Weren't you just lipsync-ing to random emotional audios? "
            lz " It's still considered singing. "
            p " I'm pretty sure it isn't, girlie... "
            " ...Oh jeez, they were THOSE types of tiktok girls. "
            " Both of their content stuff is just...really bad. "
            " You thought about how you could help them for a bit... "
            " But, before you could, they started talking about new trends that they should do. "
            " Well, there's no stopping them, then... let's just let them do whatever they want for now. "
            " Even though their ideas suck. "
            scene black with dissolve
            " You spent the entire break listening to Petunia and Lizzy's content ideas. "
            " You really wanted to help them on how to become better content creators, but they wouldn't really listen and continued yapping your ears off. "
            " Sigh...You probably should message them about it later. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit of Petunia and Lizzy yapping. Finally, you're free. "
            " You get up from your seat, and walked back to your classroom for the next class. "
            pause 2.0
            jump scienceclass2
        else:
            x " Oh, heyy! "
            " Heeey!! ^_^ "
            x " Hi there. "
            x " I don't think we've got to introduce ourselves to you before! "
            x " Don't you think they know us with how popular we are? "
            x " Come on, Liz! We're not that popular just yet! "
            x " Hmm, okay. "
            $ popularknow = True
            p " I'm Petunia! And this is my best friend lizzy! "
            lz " We're inseperable. "
            p " That's right! And we're gonna be famous in just a few months! "
            lz " ...You mean this month, right? "
            p " Er...yeah! "
            p " Actually, we've actually got some news for you! "
            " Well this is interesting. "
            p " We've been getting more followers recently! "
            lz " Isn't that great? "
            " You nodded your head, then you asked them how much followers they have now. "
            p " We've got 30 new followers! It's not a lot, but it's something, right? "
            lz " Mhm. We should post more frequently to gain more followers. "
            " You ask them what type of content they make. "
            p " What type of content we make? Oh, you know... "
            hide petunianeutral at bottom
            show petuniahappy at left
            p " I like to make videos of myself dancing to trending songs! "
            lz " And I like to make videos of myself singing. "
            hide petuniahappy at bottom
            show petuniaconfused at left
            p " ...Weren't you just lipsync-ing to random emotional audios? "
            lz " It's still considered singing. "
            p " I'm pretty sure it isn't, girlie... "
            " ...Oh jeez, they were THOSE types of tiktok girls. "
            " Both of their content stuff is just...really bad. "
            " You thought about how you could help them for a bit... "
            " But, before you could, they started talking about new trends that they should do. "
            " Well, there's no stopping them, then... let's just let them do whatever they want for now. "
            " Even though their ideas suck. "
            scene black with dissolve
            " You spent the entire break listening to Petunia and Lizzy's content ideas. "
            " You really wanted to help them on how to become better content creators, but they wouldn't really listen and continued yapping your ears off. "
            " Sigh...You probably should message them about it later. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit of Petunia and Lizzy yapping. Finally, you're free. "
            " You get up from your seat, and walked back to your classroom for the next class. "
            pause 2.0
            jump scienceclass2
    label bubbletalkyeah:
        show bubbleneutral at center with easeinleft
        if bubbleknow == True:
            b " Hi [name]!! I hope you're feeling well today! "
            b " You know... I'm kinda glad that those bullies aren't bothering anyone recently! "
            b " From what I remember, Oliver got suspended for a bit... "
            hide bubbleneutral at bottom
            show bubblesad at center
            b " I think he's coming back tomorrow though, so that's not good... "
            b " I just know Abbie will be the victim for all of his pranks again! "
            b " Why do the teachers allow them to do all of this... "
            b " It's just horrible! "
            hide bubblesad at bottom
            show bubbleneutral at center
            b " Wait, now that I think about it... "
            b " ...Oliver never really got suspended before. This has the be the first time he's ever gotten suspended... "
            b " The worst Miss Grace could do was just leave him off with a warning, but... "
            hide bubbleneutral at bottom
            show bubbleconfuse at center
            b " ...Hold on. Oliver isn't even from this school! "
            b " I remember someone mentioning that he's a university student before, so...how the hell did he even get here? "
            b " And also, since he's a university student...Did Miss Grace completely forget that he isn't even from here in the first place? "
            b " This is all so confusing... "
            hide bubbleconfuse at bottom
            show bubbleneutral at center
            b " I could just ask Miss Grace about it, but I doubt that she'll even give me a proper answer. "
            b " She's always been so mysterious about things...like that one freaky door in the hallway. "
            b " You know that one door that says to not enter Alice's room? "
            b " I asked her about it once, and she just told me to not enter it. No explanation why whatsoever... "
            b " Guess I'll never know.. "
            play sound "audio/bellring.mp3"
            b " The bell's ringing already...? I thought the breaks were longer than this... "
            b " Maybe I got too distracted in talking with you, [name]. Hehe. "
            b " I'll see you in class, [name]!! "
            hide bubbleneutral at left with easeoutleft
            " ...You should head over to class now. "
            scene black with dissolve
            pause 2.0
            jump scienceclass2
        else:
            x " Hi [name]!! I hope you're feeling well today! "
            x " Hmmm, wait... Oh, that's right! I never got to introduce myself to you yet! Sorry, heheh... "
            $ bubbleknow = True
            b " I'm Bubble! I'm Claire's friend - if you know her...If you don't, she's pretty cool! "
            if mean == True and clairesorry == False:
                " ...That girl. "
            else:
                pass
            b " You know... I'm kinda glad that those bullies aren't bothering anyone recently! "
            b " From what I remember, Oliver got suspended for a bit... "
            hide bubbleneutral at bottom
            show bubblesad at center
            b " I think he's coming back tomorrow though, so that's not good... "
            b " I just know Abbie will be the victim for all of his pranks again! "
            b " Why do the teachers allow them to do all of this... "
            b " It's just horrible! "
            hide bubblesad at bottom
            show bubbleneutral at center
            b " Wait, now that I think about it... "
            b " ...Oliver never really got suspended before. This has the be the first time he's ever gotten suspended... "
            b " The worst Miss Grace could do was just leave him off with a warning, but... "
            hide bubbleneutral at bottom
            show bubbleconfuse at center
            b " ...Hold on. Oliver isn't even from this school! "
            b " I remember someone mentioning that he's a university student before, so...how the hell did he even get here? "
            b " And also, since he's a university student...Did Miss Grace completely forget that he isn't even from here in the first place? "
            b " This is all so confusing... "
            hide bubbleconfuse at bottom
            show bubbleneutral at center
            b " I could just ask Miss Grace about it, but I doubt that she'll even give me a proper answer. "
            b " She's always been so mysterious about things...like that one freaky door in the hallway. "
            b " You know that one door that says to not enter Alice's room? "
            b " I asked her about it once, and she just told me to not enter it. No explanation why whatsoever... "
            b " Guess I'll never know.. "
            play sound "audio/bellring.mp3"
            b " The bell's ringing already...? I thought the breaks were longer than this... "
            b " Maybe I got too distracted in talking with you, [name]. Hehe. "
            b " I'll see you in class, [name]!! "
            hide bubbleneutral at left with easeoutleft
            " ...You should head over to class now. "
            scene black with dissolve
            pause 2.0
            jump scienceclass2
label tuesdayrooftop2:
    # Engel and edward - getting bullied in the middle of a calm conversation
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walk up onto the rooftop, and see one of your classmates that's just vibing. "
    " They seem to notice you. They motioned for you to come over to them - and you did. "
    show engelhappy at center with easeinright
    if engelknow == True:
        e " Hello, [name]. It's nice to see you. "
        e " Did you want to come up here to get some fresh air? Me too. "
        e " Being up here gives me a nice break from all of the noise back down in the school... "
        e " The silence here is comforting... "
        hide engelhappy at bottom
        show engelneutral at center
        e " ... "
        " There's silence for a bit. "
        " Looks like Engel is thinking about what to say. "
        hide engelneutral at bottom
        show engelhappy at center
        e " Hey, [name]? "
        e " If anyone ever brings you trouble, just know that I'm here for you, alright? "
        e " Don't listen to whatever they say. You're an amazing [person]. "
        hide engelhappy at bottom
        show engelneutral at center
        x " Nah, don't listen to him! You're horrible! "
        e " Oh geez, not this guy... "
        show engelneutral at left with move
        show edwardneutral at right with easeinright
        if oligangknow == True:
            ed " Heya, {i}angle{/i}. "
            e " Edward, could you not do anything...idiotic? I'm just having a fun and normal chat with [name] over here. "
            " This must be that one guy that's in Oliver's gang... "
            " ...He seems interesting. "
            hide edwardneutral at bottom
            show edwardhappy at right
            ed " Oh, but I wanna do something idiotic! "
            ed " It's simply impossible to not do something idiotic whenever I'm arround you, angle. "
            if clairebeatup == True and abbiemeandefend == True:
                hide edwardhappy at bottom
                show edwardconfused at right
                ed " Hey, holdon. I recognize this kid! "
                hide engelneutral at bottom
                show engelangry at left
                show engelangry at center with move
                e " Edward, please don't do something stupid to them. "
                hide edwardconfused at bottom
                show edwardneutral at right
                ed " Oh, don't cha worry! I'm just gonna take a look at them... "
                show engelangry at left with move
                show edwardneutral at center with move
                " Edward rudely shoves Engel to the side. "
                ed " Hmmm...You're [name], right? "
                ed " ...AHA! I knew it! "
                ed " This kid's the one that Oliver's been talking about! The one that beat up Claire! "
                e " ...I'm sorry, what...? "
                ed " Oh, right. Yer the one that got Oliver suspended in the first place! "
                ed " Now, honestly. I don't know whether to think if you're cool or not! "
                ed " I mean, you did kick Claire's ass, but you also got Oliver suspended... "
                ed " ...Eh! I'm not gonna think about it too much. "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardneutral at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Was what Edward said...true? "
                e " I don't want to believe that you're the one that made her upset. Tell me the truth. "
                e " Did you hurt Claire...? "
                " ...You can't afford to tell him the truth. "
                " You lied and said that you didn't, and that Edward was just making up lies. "
                e " ...He {i}is{/i} the type of guy to lie about things like that... "
                hide engelneutral at bottom
                show engelhappy at center
                e " Alright, I believe you, [name]. "
                e " But if you lied...I won't hesitate to report you to the principal. "
                e " You don't seem like the type of person to beat someone up, anyway. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
            elif clairebeatup == True and abbiemeandefend == False:
                hide edwardhappy at bottom
                show edwardconfused at right
                ed " Hey, holdon. I recognize this kid! "
                hide engelneutral at bottom
                show engelangry at left
                show engelangry at center with move
                e " Edward, please don't do something stupid to them. "
                hide edwardconfused at bottom
                show edwardneutral at right
                ed " Oh, don't cha worry! I'm just gonna take a look at them... "
                show engelangry at left with move
                show edwardneutral at center with move
                " Edward rudely shoves Engel to the side. "
                ed " Hmmm...You're [name], right? "
                ed " ...AHA! I knew it! "
                ed " This kid's the one that Oliver's been talking about! The one that beat up Claire! "
                e " ...I'm sorry, what...? "
                ed " Yeah, you're mega cool dude! "
                ed " I might have to ask Oliver to get you in our little gang once he's out of suspension. "
                ed " He did seem to like you a lot! "
                ed " Anyyywayyy, time for me to hop out! "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardneutral at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Was what Edward said...true? "
                e " I don't want to believe that you're the one that made her upset. Tell me the truth. "
                e " Did you hurt Claire...? "
                " ...You can't afford to tell him the truth. "
                " You lied and said that you didn't, and that Edward was just making up lies. "
                e " ...He {i}is{/i} the type of guy to lie about things like that... "
                hide engelneutral at bottom
                show engelhappy at center
                e " Alright, I believe you, [name]. "
                e " But if you lied...I won't hesitate to report you to the principal. "
                e " You don't seem like the type of person to beat someone up, anyway. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
            elif clairebeatup == False and abbiemeandefend == True:
                hide edwardhappy at bottom
                show edwardconfused at right
                ed " Hey, holdon. I recognize this kid! "
                hide engelneutral at bottom
                show engelangry at left
                show engelangry at center with move
                e " Edward, please don't do something stupid to them. "
                hide edwardconfused at bottom
                show edwardneutral at right
                ed " Oh, don't cha worry! I'm just gonna take a look at them... "
                show engelangry at left with move
                show edwardneutral at center with move
                " Edward rudely shoves Engel to the side. "
                ed " Hmmm...You're [name], right? "
                ed " ...AHA! I knew it! "
                ed " So, yer the one that got Oliver into suspension, eh...? "
                e " ...I'm sorry, what...? "
                hide edwardneutral at bottom
                show edwardangry at center
                ed " Not really cool, dude. "
                ed " We were just playing and messing around with Abbie, you see! "
                ed " It's not like we were killing him or anythin'. "
                ed " Ya didn't have to beat Oliver up, you know. "
                ed " Eugh, I don't want to spend too much time with losers like you guys. I'm heading out. "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardangry at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Was what Edward said...true? "
                e " I don't want to believe that you're the one that made her upset. Tell me the truth. "
                e " Did you hurt Claire...? "
                " ...You can't afford to tell him the truth. "
                " You lied and said that you didn't, and that Edward was just making up lies. "
                e " ...He {i}is{/i} the type of guy to lie about things like that... "
                hide engelneutral at bottom
                show engelhappy at center
                e " Alright, I believe you, [name]. "
                e " But if you lied...I won't hesitate to report you to the principal. "
                e " You don't seem like the type of person to beat someone up, anyway. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
            else:
                ed " Hmm... that kid next to you looks really stupid. "
                ed " This your friend? "
                hide engelneutral at bottom
                show engelangry at left
                e " ...Yes, [they] [are] my friend. "
                e " No, [they] [are] not stupid. [name] [are] really cool, you know! "
                ed " Uh huh, yeah, right. "
                ed " Anyyywayyy, time for me to hop out! "
                ed " I don't wanna spend too much time with losers like you guys. "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardneutral at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Whenever he comes over again...just ignore him, alright? "
                e " He's just a big pain to deal with. "
                e " ...How about we talk about something else to get our minds off of him? "
                " You nodded your head, agreeing to what Engel said. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
        else:
            x " Heya, {i}angle{/i}. "
            e " Edward, could you not do anything...idiotic? I'm just having a fun and normal chat with [name] over here. "
            " This must be that one guy that's in Oliver's gang... You've heard of him before. "
            " ...He seems interesting. "
            $ oligangknow = True
            hide edwardneutral at bottom
            show edwardhappy at right
            ed " Oh, but I wanna do something idiotic! "
            ed " It's simply impossible to not do something idiotic whenever I'm arround you, angle. "
            if clairebeatup == True and abbiemeandefend == True:
                hide edwardhappy at bottom
                show edwardconfused at right
                ed " Hey, holdon. I recognize this kid! "
                hide engelneutral at bottom
                show engelangry at left
                show engelangry at center with move
                e " Edward, please don't do something stupid to them. "
                hide edwardconfused at bottom
                show edwardneutral at right
                ed " Oh, don't cha worry! I'm just gonna take a look at them... "
                show engelangry at left with move
                show edwardneutral at center with move
                " Edward rudely shoves Engel to the side. "
                ed " Hmmm...You're [name], right? "
                ed " ...AHA! I knew it! "
                ed " This kid's the one that Oliver's been talking about! The one that beat up Claire! "
                e " ...I'm sorry, what...? "
                ed " Oh, right. Yer the one that got Oliver suspended in the first place! "
                ed " Now, honestly. I don't know whether to think if you're cool or not! "
                ed " I mean, you did kick Claire's ass, but you also got Oliver suspended... "
                ed " ...Eh! I'm not gonna think about it too much. "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardneutral at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Was what Edward said...true? "
                e " I don't want to believe that you're the one that made her upset. Tell me the truth. "
                e " Did you hurt Claire...? "
                " ...You can't afford to tell him the truth. "
                " You lied and said that you didn't, and that Edward was just making up lies. "
                e " ...He {i}is{/i} the type of guy to lie about things like that... "
                hide engelneutral at bottom
                show engelhappy at center
                e " Alright, I believe you, [name]. "
                e " But if you lied...I won't hesitate to report you to the principal. "
                e " You don't seem like the type of person to beat someone up, anyway. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
            elif clairebeatup == True and abbiemeandefend == False:
                hide edwardhappy at bottom
                show edwardconfused at right
                ed " Hey, holdon. I recognize this kid! "
                hide engelneutral at bottom
                show engelangry at left
                show engelangry at center with move
                e " Edward, please don't do something stupid to them. "
                hide edwardconfused at bottom
                show edwardneutral at right
                ed " Oh, don't cha worry! I'm just gonna take a look at them... "
                show engelangry at left with move
                show edwardneutral at center with move
                " Edward rudely shoves Engel to the side. "
                ed " Hmmm...You're [name], right? "
                ed " ...AHA! I knew it! "
                ed " This kid's the one that Oliver's been talking about! The one that beat up Claire! "
                e " ...I'm sorry, what...? "
                ed " Yeah, you're mega cool dude! "
                ed " I might have to ask Oliver to get you in our little gang once he's out of suspension. "
                ed " He did seem to like you a lot! "
                ed " Anyyywayyy, time for me to hop out! "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardneutral at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Was what Edward said...true? "
                e " I don't want to believe that you're the one that made her upset. Tell me the truth. "
                e " Did you hurt Claire...? "
                " ...You can't afford to tell him the truth. "
                " You lied and said that you didn't, and that Edward was just making up lies. "
                e " ...He {i}is{/i} the type of guy to lie about things like that... "
                hide engelneutral at bottom
                show engelhappy at center
                e " Alright, I believe you, [name]. "
                e " But if you lied...I won't hesitate to report you to the principal. "
                e " You don't seem like the type of person to beat someone up, anyway. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
            elif clairebeatup == False and abbiemeandefend == True:
                hide edwardhappy at bottom
                show edwardconfused at right
                ed " Hey, holdon. I recognize this kid! "
                hide engelneutral at bottom
                show engelangry at left
                show engelangry at center with move
                e " Edward, please don't do something stupid to them. "
                hide edwardconfused at bottom
                show edwardneutral at right
                ed " Oh, don't cha worry! I'm just gonna take a look at them... "
                show engelangry at left with move
                show edwardneutral at center with move
                " Edward rudely shoves Engel to the side. "
                ed " Hmmm...You're [name], right? "
                ed " ...AHA! I knew it! "
                ed " So, yer the one that got Oliver into suspension, eh...? "
                e " ...I'm sorry, what...? "
                hide edwardneutral at bottom
                show edwardangry at center
                ed " Not really cool, dude. "
                ed " We were just playing and messing around with Abbie, you see! "
                ed " It's not like we were killing him or anythin'. "
                ed " Ya didn't have to beat Oliver up, you know. "
                ed " Eugh, I don't want to spend too much time with losers like you guys. I'm heading out. "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardangry at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Was what Edward said...true? "
                e " I don't want to believe that you're the one that made her upset. Tell me the truth. "
                e " Did you hurt Claire...? "
                " ...You can't afford to tell him the truth. "
                " You lied and said that you didn't, and that Edward was just making up lies. "
                e " ...He {i}is{/i} the type of guy to lie about things like that... "
                hide engelneutral at bottom
                show engelhappy at center
                e " Alright, I believe you, [name]. "
                e " But if you lied...I won't hesitate to report you to the principal. "
                e " You don't seem like the type of person to beat someone up, anyway. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
            else:
                ed " Hmm... that kid next to you looks really stupid. "
                ed " This your friend? "
                hide engelneutral at bottom
                show engelangry at left
                e " ...Yes, [they] [are] my friend. "
                e " No, [they] [are] not stupid. [name] [are] really cool, you know! "
                ed " Uh huh, yeah, right. "
                ed " Anyyywayyy, time for me to hop out! "
                ed " I don't wanna spend too much time with losers like you guys. "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardneutral at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Whenever he comes over again...just ignore him, alright? "
                e " He's just a big pain to deal with. "
                e " ...How about we talk about something else to get our minds off of him? "
                " You nodded your head, agreeing to what Engel said. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
    else:
        x " Hello, [name]. It's nice to see you. "
        $ engelknow = True
        e " I'm Engel, by the way. I don't think I've introduced myself to you before, hehe. "
        e " Did you want to come up here to get some fresh air? Me too. "
        e " Being up here gives me a nice break from all of the noise back down in the school... "
        e " The silence here is comforting... "
        hide engelhappy at bottom
        show engelneutral at center
        e " ... "
        " There's silence for a bit. "
        " Looks like Engel is thinking about what to say. "
        hide engelneutral at bottom
        show engelhappy at center
        e " Hey, [name]? "
        e " If anyone ever brings you trouble, just know that I'm here for you, alright? "
        e " Don't listen to whatever they say. You're an amazing [person]. "
        hide engelhappy at bottom
        show engelneutral at center
        x " Nah, don't listen to him! You're horrible! "
        e " Oh geez, not this guy... "
        show engelneutral at left with move
        show edwardneutral at right with easeinright
        if oligangknow == True:
            ed " Heya, {i}angle{/i}. "
            e " Edward, could you not do anything...idiotic? I'm just having a fun and normal chat with [name] over here. "
            " This must be that one guy that's in Oliver's gang... "
            " ...He seems interesting. "
            hide edwardneutral at bottom
            show edwardhappy at right
            ed " Oh, but I wanna do something idiotic! "
            ed " It's simply impossible to not do something idiotic whenever I'm arround you, angle. "
            if clairebeatup == True and abbiemeandefend == True:
                hide edwardhappy at bottom
                show edwardconfused at right
                ed " Hey, holdon. I recognize this kid! "
                hide engelneutral at bottom
                show engelangry at left
                show engelangry at center with move
                e " Edward, please don't do something stupid to [them]. "
                hide edwardconfused at bottom
                show edwardneutral at right
                ed " Oh, don't cha worry! I'm just gonna take a look at [them]... "
                show engelangry at left with move
                show edwardneutral at center with move
                " Edward rudely shoves Engel to the side. "
                ed " Hmmm...You're [name], right? "
                ed " ...AHA! I knew it! "
                ed " This kid's the one that Oliver's been talking about! The one that beat up Claire! "
                e " ...I'm sorry, what...? "
                ed " Oh, right. Yer the one that got Oliver suspended in the first place! "
                ed " Now, honestly. I don't know whether to think if you're cool or not! "
                ed " I mean, you did kick Claire's ass, but you also got Oliver suspended... "
                ed " ...Eh! I'm not gonna think about it too much. "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardneutral at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Was what Edward said...true? "
                e " I don't want to believe that you're the one that made her upset. Tell me the truth. "
                e " Did you hurt Claire...? "
                " ...You can't afford to tell him the truth. "
                " You lied and said that you didn't, and that Edward was just making up lies. "
                e " ...He {i}is{/i} the type of guy to lie about things like that... "
                hide engelneutral at bottom
                show engelhappy at center
                e " Alright, I believe you, [name]. "
                e " But if you lied...I won't hesitate to report you to the principal. "
                e " You don't seem like the type of person to beat someone up, anyway. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
            elif clairebeatup == True and abbiemeandefend == False:
                hide edwardhappy at bottom
                show edwardconfused at right
                ed " Hey, holdon. I recognize this kid! "
                hide engelneutral at bottom
                show engelangry at left
                show engelangry at center with move
                e " Edward, please don't do something stupid to [them]. "
                hide edwardconfused at bottom
                show edwardneutral at right
                ed " Oh, don't cha worry! I'm just gonna take a look at [them]... "
                show engelangry at left with move
                show edwardneutral at center with move
                " Edward rudely shoves Engel to the side. "
                ed " Hmmm...You're [name], right? "
                ed " ...AHA! I knew it! "
                ed " This kid's the one that Oliver's been talking about! The one that beat up Claire! "
                e " ...I'm sorry, what...? "
                ed " Yeah, you're mega cool dude! "
                ed " I might have to ask Oliver to get you in our little gang once he's out of suspension. "
                ed " He did seem to like you a lot! "
                ed " Anyyywayyy, time for me to hop out! "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardneutral at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Was what Edward said...true? "
                e " I don't want to believe that you're the one that made her upset. Tell me the truth. "
                e " Did you hurt Claire...? "
                " ...You can't afford to tell him the truth. "
                " You lied and said that you didn't, and that Edward was just making up lies. "
                e " ...He {i}is{/i} the type of guy to lie about things like that... "
                hide engelneutral at bottom
                show engelhappy at center
                e " Alright, I believe you, [name]. "
                e " But if you lied...I won't hesitate to report you to the principal. "
                e " You don't seem like the type of person to beat someone up, anyway. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
            elif clairebeatup == False and abbiemeandefend == True:
                hide edwardhappy at bottom
                show edwardconfused at right
                ed " Hey, holdon. I recognize this kid! "
                hide engelneutral at bottom
                show engelangry at left
                show engelangry at center with move
                e " Edward, please don't do something stupid to [them]. "
                hide edwardconfused at bottom
                show edwardneutral at right
                ed " Oh, don't cha worry! I'm just gonna take a look at [them]... "
                show engelangry at left with move
                show edwardneutral at center with move
                " Edward rudely shoves Engel to the side. "
                ed " Hmmm...You're [name], right? "
                ed " ...AHA! I knew it! "
                ed " So, yer the one that got Oliver into suspension, eh...? "
                e " ...I'm sorry, what...? "
                hide edwardneutral at bottom
                show edwardangry at center
                ed " Not really cool, dude. "
                ed " We were just playing and messing around with Abbie, you see! "
                ed " It's not like we were killing him or anythin'. "
                ed " Ya didn't have to beat Oliver up, you know. "
                ed " Eugh, I don't want to spend too much time with losers like you guys. I'm heading out. "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardangry at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Was what Edward said...true? "
                e " I don't want to believe that you're the one that made her upset. Tell me the truth. "
                e " Did you hurt Claire...? "
                " ...You can't afford to tell him the truth. "
                " You lied and said that you didn't, and that Edward was just making up lies. "
                e " ...He {i}is{/i} the type of guy to lie about things like that... "
                hide engelneutral at bottom
                show engelhappy at center
                e " Alright, I believe you, [name]. "
                e " But if you lied...I won't hesitate to report you to the principal. "
                e " You don't seem like the type of person to beat someone up, anyway. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
            else:
                hide edwardhappy at bottom
                show edwardneutral at right
                ed " Hmm... that kid next to you looks really stupid. "
                ed " This your friend? "
                hide engelneutral at bottom
                show engelangry at left
                e " ...Yes, [they] [are] my friend. "
                e " No, [they] [are] not stupid. [name] [are] really cool, you know! "
                ed " Uh huh, yeah, right. "
                ed " Anyyywayyy, time for me to hop out! "
                ed " I don't wanna spend too much time with losers like you guys. "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardneutral at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Whenever he comes over again...just ignore him, alright? "
                e " He's just a big pain to deal with. "
                e " ...How about we talk about something else to get our minds off of him? "
                " You nodded your head, agreeing to what Engel said. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
        else:
            x " Heya, {i}angle{/i}. "
            e " Edward, could you not do anything...idiotic? I'm just having a fun and normal chat with [name] over here. "
            " This must be that one guy that's in Oliver's gang... You've heard of him before. "
            " ...He seems interesting. "
            $ oligangknow = True
            hide edwardneutral at bottom
            show edwardhappy at right
            ed " Oh, but I wanna do something idiotic! "
            ed " It's simply impossible to not do something idiotic whenever I'm arround you, angle. "
            if clairebeatup == True and abbiemeandefend == True:
                hide edwardhappy at bottom
                show edwardconfused at right
                ed " Hey, holdon. I recognize this kid! "
                hide engelneutral at bottom
                show engelangry at left
                show engelangry at center with move
                e " Edward, please don't do something stupid to [them]. "
                hide edwardconfused at bottom
                show edwardneutral at right
                ed " Oh, don't cha worry! I'm just gonna take a look at [them]... "
                show engelangry at left with move
                show edwardneutral at center with move
                " Edward rudely shoves Engel to the side. "
                ed " Hmmm...You're [name], right? "
                ed " ...AHA! I knew it! "
                ed " This kid's the one that Oliver's been talking about! The one that beat up Claire! "
                e " ...I'm sorry, what...? "
                ed " Oh, right. Yer the one that got Oliver suspended in the first place! "
                ed " Now, honestly. I don't know whether to think if you're cool or not! "
                ed " I mean, you did kick Claire's ass, but you also got Oliver suspended... "
                ed " ...Eh! I'm not gonna think about it too much. "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardneutral at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Was what Edward said...true? "
                e " I don't want to believe that you're the one that made her upset. Tell me the truth. "
                e " Did you hurt Claire...? "
                " ...You can't afford to tell him the truth. "
                " You lied and said that you didn't, and that Edward was just making up lies. "
                e " ...He {i}is{/i} the type of guy to lie about things like that... "
                hide engelneutral at bottom
                show engelhappy at center
                e " Alright, I believe you, [name]. "
                e " But if you lied...I won't hesitate to report you to the principal. "
                e " You don't seem like the type of person to beat someone up, anyway. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
            elif clairebeatup == True and abbiemeandefend == False:
                hide edwardhappy at bottom
                show edwardconfused at right
                ed " Hey, holdon. I recognize this kid! "
                hide engelneutral at bottom
                show engelangry at left
                show engelangry at center with move
                e " Edward, please don't do something stupid to [them]. "
                hide edwardconfused at bottom
                show edwardneutral at right
                ed " Oh, don't cha worry! I'm just gonna take a look at [them]... "
                show engelangry at left with move
                show edwardneutral at center with move
                " Edward rudely shoves Engel to the side. "
                ed " Hmmm...You're [name], right? "
                ed " ...AHA! I knew it! "
                ed " This kid's the one that Oliver's been talking about! The one that beat up Claire! "
                e " ...I'm sorry, what...? "
                ed " Yeah, you're mega cool dude! "
                ed " I might have to ask Oliver to get you in our little gang once he's out of suspension. "
                ed " He did seem to like you a lot! "
                ed " Anyyywayyy, time for me to hop out! "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardneutral at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Was what Edward said...true? "
                e " I don't want to believe that you're the one that made her upset. Tell me the truth. "
                e " Did you hurt Claire...? "
                " ...You can't afford to tell him the truth. "
                " You lied and said that you didn't, and that Edward was just making up lies. "
                e " ...He {i}is{/i} the type of guy to lie about things like that... "
                hide engelneutral at bottom
                show engelhappy at center
                e " Alright, I believe you, [name]. "
                e " But if you lied...I won't hesitate to report you to the principal. "
                e " You don't seem like the type of person to beat someone up, anyway. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
            elif clairebeatup == False and abbiemeandefend == True:
                hide edwardhappy at bottom
                show edwardconfused at right
                ed " Hey, holdon. I recognize this kid! "
                hide engelneutral at bottom
                show engelangry at left
                show engelangry at center with move
                e " Edward, please don't do something stupid to [them]. "
                hide edwardconfused at bottom
                show edwardneutral at right
                ed " Oh, don't cha worry! I'm just gonna take a look at [them]... "
                show engelangry at left with move
                show edwardneutral at center with move
                " Edward rudely shoves Engel to the side. "
                ed " Hmmm...You're [name], right? "
                ed " ...AHA! I knew it! "
                ed " So, yer the one that got Oliver into suspension, eh...? "
                e " ...I'm sorry, what...? "
                hide edwardneutral at bottom
                show edwardangry at center
                ed " Not really cool, dude. "
                ed " We were just playing and messing around with Abbie, you see! "
                ed " It's not like we were killing him or anythin'. "
                ed " Ya didn't have to beat Oliver up, you know. "
                ed " Eugh, I don't want to spend too much time with losers like you guys. I'm heading out. "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardangry at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Was what Edward said...true? "
                e " I don't want to believe that you're the one that made her upset. Tell me the truth. "
                e " Did you hurt Claire...? "
                " ...You can't afford to tell him the truth. "
                " You lied and said that you didn't, and that Edward was just making up lies. "
                e " ...He {i}is{/i} the type of guy to lie about things like that... "
                hide engelneutral at bottom
                show engelhappy at center
                e " Alright, I believe you, [name]. "
                e " But if you lied...I won't hesitate to report you to the principal. "
                e " You don't seem like the type of person to beat someone up, anyway. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
            else:
                ed " Hmm... that kid next to you looks really stupid. "
                ed " This your friend? "
                hide engelneutral at bottom
                show engelangry at left
                e " ...Yes, [they] [are] my friend. "
                e " No, [they] [are] not stupid. [name] [are] really cool, you know! "
                ed " Uh huh, yeah, right. "
                ed " Anyyywayyy, time for me to hop out! "
                ed " I don't wanna spend too much time with losers like you guys. "
                ed " Later, losers. I'm wasting my time being here! "
                hide edwardneutral at right with easeoutright
                show engelangry at center with move
                " ...Then Edward left. "
                e " Sigh... he gives me such a headache... "
                hide engelangry at bottom
                show engelneutral at center
                e " ...[name]. "
                e " Whenever he comes over again...just ignore him, alright? "
                e " He's just a big pain to deal with. "
                e " ...How about we talk about something else to get our minds off of him? "
                " You nodded your head, agreeing to what Engel said. "
                scene black with dissolve
                " You spent the rest of the break talking to Engel. "
                " You both weren't talking about anything interesting, just talking about random topics. "
                " Just vibing on the rooftop, nothing else. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, meaning that it was time for the next class. "
                " You walked back down into the school, and went to your classroom. "
                pause 2.0
                jump scienceclass2
label tuesdaylibrary2:
    # abbie and riley - opinions in this school
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and spotted two of your classmates just vibing. "
    " You wanted to talk to one of them, but didn't know which one to talk to. "
    " Who do you talk to? "
    if abbieknow == True and rileyknow == True:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump abbielibint
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump rileylibint
    elif abbieknow == True and rileyknow == False:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump abbielibint
            " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                jump rileylibint
    elif abbieknow == False and rileyknow == True:
        menu:
            " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                jump abbielibint
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump rileylibint
    else:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump abbielibint
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump rileylibint
    label abbielibint:
        if abbieknow == True:
            " You walked over to Abbie, and sat next to him. "
        else:
            " You walked over to the shy looking boy, and sat next to him. "
        show abbieneutral at center with easeinright
        if abbieknow == True:
            a " ... "
            a " ...Oh, uh...hi [name]... "
            a " Sorry, I got a little distracted by my thoughts... "
            a " Um...did you want to talk about something...? "
            " Abbie looks like the type of guy who can't decided a topic for conversation, so you try to think of something... "
            " ...You then come up with a topic. "
            " You ask Abbie what he thinks of this school and it's teachers. "
            a " What I think of this school...? "
            a " Well, um... I think this school's pretty neat...aside from the bullies... "
            a " Sometimes I could see trash on the ground...wait, actually... "
            a " That reminds me of one situation we had before you came here... "
            a " One time, Oliver, Zip, and Edward thought it would be funny if they filled the halls with paper... "
            a " ...And everyone had to clean for the entire day...Including the three of them and the teachers... "
            a " It kind of sucked...I don't know why they thought that it was a good idea... "
            a " They were complaining about it the entire day...but...atleast we had no class...I guess? "
            a " And uh...I guess the teachers are nice... "
            hide abbieneutral at bottom
            show abbiesad at center
            a " But, the math, language, and science teachers scare me the most... "
            a " I remember seeing Miss Circle yell at someone just for failing... "
            a " Now that I think about it...I haven't seen that student in awhile now... "
            a " ...I think they might've dropped out of school...or... "
            a " ... "
            hide abbiesad at bottom
            show abbieneutral at center
            a " ...Yeah, they might've just dropped out of school... "
            a " It would be horrible if something bad happed to them... "
            a " I hope they're okay... "
            scene black with dissolve
            " You spent the entire break talking with Abbie in the library. "
            " It was actually pretty fun to talk to him, he would throw jokes every now and then that weren't funny, but you knew he was trying his best. "
            if abbiehelp == True:
                " You then remembered something...you wanted to help this dude out. "
                " You should talk to him in the next break. "
            else:
                pass
            play sound "audio/bellring.mp3"
            " The bell eventually rings. You and Abbie get up your seats and go back to class. "
            pause 2.0
            jump scienceclass2
        else:
            x " ... "
            x " ...Oh, uh...hi [name]... "
            x " Sorry, I got a little distracted by my thoughts... "
            x " Um...I haven't introduced myself to you yet, have I...? Sorry, my memory isn't great... "
            $ abbieknow = True
            a " I'm Abbie...it's nice to meet you... "
            a " Um...did you want to talk about something...? "
            " Abbie looks like the type of guy who can't decided a topic for conversation, so you try to think of something... "
            " ...You then come up with a topic. "
            " You ask Abbie what he thinks of this school and it's teachers. "
            a " What I think of this school...? "
            a " Well, um... I think this school's pretty neat...aside from the bullies... "
            a " Sometimes I could see trash on the ground...wait, actually... "
            a " That reminds me of one situation we had before you came here... "
            a " One time, Oliver, Zip, and Edward thought it would be funny if they filled the halls with paper... "
            a " ...And everyone had to clean for the entire day...Including the three of them and the teachers... "
            a " It kind of sucked...I don't know why they thought that it was a good idea... "
            a " They were complaining about it the entire day...but...atleast we had no class...I guess? "
            a " And uh...I guess the teachers are nice... "
            hide abbieneutral at bottom
            show abbiesad at center
            a " But, the math, language, and science teachers scare me the most... "
            a " I remember seeing Miss Circle yell at someone just for failing... "
            a " Now that I think about it...I haven't seen that student in awhile now... "
            a " ...I think they might've dropped out of school...or... "
            a " ... "
            hide abbiesad at bottom
            show abbieneutral at center
            a " ...Yeah, they might've just dropped out of school... "
            a " It would be horrible if something bad happed to them... "
            a " I hope they're okay... "
            scene black with dissolve
            " You spent the entire break talking with Abbie in the library. "
            " It was actually pretty fun to talk to him, he would throw jokes every now and then that weren't funny, but you knew he was trying his best. "
            if abbiehelp == True:
                " You then remembered something...you wanted to help this dude out. "
                " You should talk to him in the next break. "
            else:
                pass
            play sound "audio/bellring.mp3"
            " The bell eventually rings. You and Abbie get up your seats and go back to class. "
            pause 2.0
            jump scienceclass2
    label rileylibint:
        if rileyknow == True:
            " You decided to walk up to Riley, even though you know that she'll probably talk about Oliver. "
        else:
            " You decided to walk up to the insane looking girl, surely you'll have a normal and sane conversation with her... "
        show rileyneutral at center with easeinleft
        if rileyknow == True:
            ri " Heheh...hiya, [name]! "
            ri " I'm just standing around the library...thinking about my beloved Oliver! "
            ri " He's so pretty right? Well, I know he is! You can't have him though. "
            ri " He's alllllllll mine!! "
            ri " ...Wait, you probably wanted to talk to me about something non-Oliver related. "
            ri " HehehhhhAHAHAH!! Sorry about that. I can't help but talk about my sweet Oliver a lot!! "
            ri " What did you want to talk about, [name]? "
            " You're gonna have to try and think about a topic that isn't relating to Oliver. "
            " You think long and hard, before you found a topic that you could talk about to Riley. "
            " You asked her what she thought about this school. "
            ri " Hm...what I think about this school? "
            ri " WELL! Before, I thought it was gloomy and boring...your average school, basically! "
            ri " BUT THEN! Oliver came!! The day Oliver came, it was like love at first sight for me! "
            " Yeah, you knew she was gonna be able to drag in Oliver somehow. "
            ri " He was just so dreamy, I couldn't help but fall in love with him!! "
            ri " Zip and Edward...? Eh, they're alright. But Oliver is the real deal! "
            ri " I honestly don't know what I'd be like if I never met Oliver at all! "
            ri " I hope he falls in love with me and we can start dating soon... "
            " You kind of tuned out her yapping session, but then you realized something... "
            " ...You've heard something about Oliver being a college student. We're in highschool right now. "
            " Oliver was most likely way older than Riley, so you remind her about that. "
            ri " ... "
            ri " I just LOVE my Oliver so much!! "
            " Aaaaand it seems like she completely ignored you. "
            " Someone should really check up on her...obsessive-ness. "
            " You wonder how her parents aren't going insane with how much she's talking about Oliver. "
            " Then again, they might just think that it's just young normal love. "
            " Sigh... You could've been doing something else right now, but here we are. "
            scene black with dissolve
            " You spent the rest of break talking with Riley. "
            " Well, it was more like Riley talking to you about Oliver, and you just tuning out the entire conversation... "
            " Oh well. You were the one that chose this option anyway. "
            play sound "audio/bellring.mp3"
            " The bell rings, saving your ears from the yapping session. "
            " You IMMEDIATELY skedaddle to the exit and went straight to your classroom for the next class. "
            pause 2.0
            jump scienceclass2
        else:
            x " Heheh...hiya, [name]! "
            $ rileyknow = True
            ri " I'm Riley, by the way! What am I doing here? well... "
            ri " I'm just standing around the library...thinking about my beloved Oliver! "
            ri " He's so pretty right? Well, I know he is! You can't have him though. "
            ri " He's alllllllll mine!! "
            ri " ...Wait, you probably wanted to talk to me about something non-Oliver related. "
            ri " HehehhhhAHAHAH!! Sorry about that. I can't help but talk about my sweet Oliver a lot!! "
            ri " What did you want to talk about, [name]? "
            " You're gonna have to try and think about a topic that isn't relating to Oliver. "
            " You think long and hard, before you found a topic that you could talk about to Riley. "
            " You asked her what she thought about this school. "
            ri " Hm...what I think about this school? "
            ri " WELL! Before, I thought it was gloomy and boring...your average school, basically! "
            ri " BUT THEN! Oliver came!! The day Oliver came, it was like love at first sight for me! "
            " Yeah, you knew she was gonna be able to drag in Oliver somehow. "
            ri " He was just so dreamy, I couldn't help but fall in love with him!! "
            ri " Zip and Edward...? Eh, they're alright. But Oliver is the real deal! "
            ri " I honestly don't know what I'd be like if I never met Oliver at all! "
            ri " I hope he falls in love with me and we can start dating soon... "
            " You kind of tuned out her yapping session, but then you realized something... "
            " ...You've heard something about Oliver being a college student. We're in highschool right now. "
            " Oliver was most likely way older than Riley, so you remind her about that. "
            ri " ... "
            ri " I just LOVE my Oliver so much!! "
            " Aaaaand it seems like she completely ignored you. "
            " Someone should really check up on her...obsessive-ness. "
            " You wonder how her parents aren't going insane with how much she's talking about Oliver. "
            " Then again, they might just think that it's just young normal love. "
            " Sigh... You could've been doing something else right now, but here we are. "
            scene black with dissolve
            " You spent the rest of break talking with Riley. "
            " Well, it was more like Riley talking to you about Oliver, and you just tuning out the entire conversation... "
            " Oh well. You were the one that chose this option anyway. "
            play sound "audio/bellring.mp3"
            " The bell rings, saving your ears from the yapping session. "
            " You IMMEDIATELY skedaddle to the exit and went straight to your classroom for the next class. "
            pause 2.0
            jump scienceclass2
label scienceclass2:
    # questions
    scene classroom with dissolve
    " You arrived to your classroom and you sat in your seat. "
    " Not too long after you sat down, the science teacher arrives and stands infront of the class. "
    show missbloomieneutral at center with easeinright
    msb " Good morning, class. "
    msb " Let's start with our lesson for today... "
    msb " So, last we left off was about the periodic table. "
    msb " Can anyone tell me what the symbol for Berylium was? "
    " You're thinking about answering. Should you? "
    menu:
        " Answer":
            " You answered the question with 'Be'. "
            msb " Yes, that's correct, [name]. "
            msb " It is infact, 'Be'. Good job. "
            msb " All of you should be like [name], and memorize the periodic table. "
            msb " I'll be asking all of you the symbol for each element next monday. "
            msb " No, I won't let you read from your phones or anything about the entire periodic table. "
            msb " Pure memorization. "
            " Thank god this game only has 1 week so that you don't have to deal with all of that. "
            msb " Anyway... "
            scene black with dissolve
            " You just had to take down some notes for science class for today. "
            " Atleast you have something in your notebook now. "
            play sound "audio/bellring.mp3"
            " The bell rings after a few minutes, meaning that it was time for another break. "
            " You get up from your seat and walked to the hallways. "
            pause 2.0
            jump tuesdaybreak3
        " Let someone else answer ":
            " You let someone else answer. You weren't feeling it today. "
            show engelneutral at left with easeinleft
            if engelknow == True:
                e " Is it 'Be'? "
            else:
                x " Is it 'Be'? "
            hide engelneutral at left with easeoutleft
            msb " Yes, that's correct, Engel. "
            msb " It is infact, 'Be'. Good job. "
            msb " All of you should be like Engel, and memorize the periodic table. "
            msb " I'll be asking all of you the symbol for each element next monday. "
            msb " No, I won't let you read from your phones or anything about the entire periodic table. "
            msb " Pure memorization. "
            " Thank god this game only has 1 week so that you don't have to deal with all of that. "
            msb " Anyway... "
            scene black with dissolve
            " You just had to take down some notes for science class for today. "
            " Atleast you have something in your notebook now. "
            play sound "audio/bellring.mp3"
            " The bell rings after a few minutes, meaning that it was time for another break. "
            " You get up from your seat and walked to the hallways. "
            pause 2.0
            jump tuesdaybreak3
label tuesdaybreak3:
    scene hallway with dissolve
    " It's the third break of the day, and you're thinking about going somewhere in the school. "
    " Where do you go? "
    if abbiehelp == True:
        " Psst, you've got to help Abbie in the gym. "
        " He's got something to deal with in there. "
        pass
    else:
        pass
    menu:
        " {image=cubbieicon} The front of the school {image=robbyicon} ":
            jump tuesdayfront3
        " {image=popularicon} The back of the school {image=kevinicon} ":
            jump tuesdayback3
        " {image=abbieicon} The gym {image=oligangicon} ":
            jump tuesdaygym3
        " The cafeteria ":
            jump tuesdaycafe3
        " {image=skellicon} The rooftop {image=bubbleicon} ":
            jump tuesdayrooftop3
        " {image=claireicon} The library {image=claireicon} ":
            jump tuesdaylibrary3
label tuesdayfront3:
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walk outside to take a break from all of the noise inside the school. "
    " Whilst you were walking around outside, you spotted two of your classmates just vibing. "
    " I'm pretty sure you know the deal already. Who do you talk to? "
    if cubbieknow == True and robbyknow == True:
        menu:
            " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                jump cubcubs
            " {image=robbyicon} Robby {image=robbyicon} ":
                jump robrobs
    elif cubbieknow == True and robbyknow == False:
        menu:
            " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                jump cubcubs
            " {image=robbyicon} A guy with a silly looking hat. {image=robbyicon} ":
                jump robrobs
    elif cubbieknow == False and robbyknow == True:
        menu:
            " {image=cubbieicon} A cute cat guy! {image=cubbieicon} ":
                jump cubcubs
            " {image=robbyicon} Robby {image=robbyicon} ":
                jump robrobs
    else:
        menu:
            " {image=cubbieicon} A cute cat guy! {image=cubbieicon} ":
                jump cubcubs
            " {image=robbyicon} A guy with a silly looking hat. {image=robbyicon} ":
                jump robrobs
    label cubcubs:
        show cubbieneutral at center with easeinright
        if cubbieknow == True:
            " You walked up to Cubbie and saw that he was messing with a few sticks. "
            " You asked him what he was doing. "
            cb " ... "
            " ...You then remembered that he wasn't exactly comfortable with talking, uh... "
            " You had to figure out a way for you to understand Cubbie. "
            cb " ... "
            " Cubbie pointed towards a pile of sticks...was he collecting sticks? "
            " You asked him if he was collecting sticks. "
            cb " (nod)... "
            " You then asked him why he was collecting sticks. "
            " He just shrugged in response...maybe because he was bored? "
            " He probably had nothing to do... "
            " You asked him if you could join him in collecting sticks. "
            " He nodded. Great! You're gonna become a stick collector now! "
            " You started to collect sticks with Cubbie. "
            scene black with dissolve
            " You spent the entire break collecting sticks with Cubbie to cure your boredom. "
            " It was actually kind of fun because you two got to make random things with the sticks once you both were done. "
            " You made a little stickman with the sticks. Now it's literally just a STICKman. "
            play sound "audio/bellring.mp3"
            " The bell rings, meaning that it was time for another class. "
            " You and Cubbie get up and start walking back to the classroom for the next class. "
            pause 2.0
            jump historyclass2
        else:
            " You walked up to the cat guy and saw that he was messing with a few sticks. "
            $ cubbieknow = True
            " You've heard that this guy's name was Cubbie... how cute!! "
            " You then asked him what he was doing. "
            cb " ... "
            " ...You then remembered that he wasn't exactly comfortable with talking, uh... "
            " You had to figure out a way for you to understand Cubbie. "
            cb " ... "
            " Cubbie pointed towards a pile of sticks...was he collecting sticks? "
            " You asked him if he was collecting sticks. "
            cb " (nod)... "
            " You then asked him why he was collecting sticks. "
            " He just shrugged in response...maybe because he was bored? "
            " He probably had nothing to do... "
            " You asked him if you could join him in collecting sticks. "
            " He nodded. Great! You're gonna become a stick collector now! "
            " You started to collect sticks with Cubbie. "
            scene black with dissolve
            " You spent the entire break collecting sticks with Cubbie to cure your boredom. "
            " It was actually kind of fun because you two got to make random things with the sticks once you both were done. "
            " You made a little stickman with the sticks. Now it's literally just a STICKman. "
            play sound "audio/bellring.mp3"
            " The bell rings, meaning that it was time for another class. "
            " You and Cubbie get up and start walking back to the classroom for the next class. "
            pause 2.0
            jump historyclass2
    label robrobs:
        show robbyneutral at center with easeinleft
        if robbyknow == True:
            " Robby seemed to look bored, poking at a rock with his wrench. "
            " You sat down next to him, poking his shoulder to get his attention. "
            rb " Oh, uh... hey [name]. "
            rb " Kinda bored because I don't have much to do. "
            rb " And my friends are busy talking with other students, so... "
            rb " ...Yeah. "
            " You tried to think of what you could talk about with Robby... "
            " ...You came up with a lttle conversation topic after a few minutes. "
            if rubyknow == True:
                " You asked about Ruby. "
                rb " Oh, Ruby? she's doing fine. "
                rb " But I did hear that she's been overheating a lot today... "
                rb " I may need to check her out, but these breaks are too short for me to do so. "
                rb " Just gonna have to pray that she can last a bit longer without crashing. "
                rb " ...Yes, she has crashed a lot before. "
                rb " Due to multiple things, actually. "
                rb " One time, Zip decided it would be a really funny idea to mess with her. "
                rb " ...So, she dumped a bucket of water on her. "
                rb " Causing Ruby to completely glitch out, and I had to fix her for the entire day. "
                rb " It was really annoying, but atleast I had an excuse to skip school for the day... I guess. "
                rb " Sometimes I wish that Zip and the other guys would stop being so annoying. "
                rb " Sometimes, they're slightly tolerable. And other times... they piss me off real bad. "
                rb " If you ever see Ruby, just tell her that I'll fix her when school is over. "
            else:
                " You asked about a girl with a TV for a head, asking if Robby knew her. "
                rb " Oh, Ruby? yeah, I know her. She's my friend, and she's doing fine. "
                rb " But I did hear that she's been overheating a lot today... "
                rb " I may need to check her out, but these breaks are too short for me to do so. "
                rb " Just gonna have to pray that she can last a bit longer without crashing. "
                rb " ...Yes, she has crashed a lot before. "
                rb " Due to multiple things, actually. "
                rb " One time, Zip decided it would be a really funny idea to mess with her. "
                rb " ...So, she dumped a bucket of water on her. "
                rb " Causing Ruby to completely glitch out, and I had to fix her for the entire day. "
                rb " It was really annoying, but atleast I had an excuse to skip school for the day... I guess. "
                rb " Sometimes I wish that Zip and the other guys would stop being so annoying. "
                rb " Sometimes, they're slightly tolerable. And other times... they piss me off real bad. "
                rb " If you ever see Ruby, just tell her that I'll fix her when school is over. "
            scene black with dissolve
            " You spent the rest of the break talking about things with Robby. "
            " He was pretty much just a chill guy. He would often mess with other rocks around him with his wrench out of boredom. "
            " ...You wonder how wrenches taste like now for some reason. "
            " Probably good. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that it was time for another class. "
            " You get up from where you were sitting, and you walked back into the school to go to your classroom. "
            pause 2.0
            jump historyclass2
        else:
            " He seemed to look bored, poking at a rock with his wrench. "
            " You sat down next to him, poking his shoulder to get his attention. "
            x " Oh, uh... hey [name]. "
            $ robbyknow = True
            rb " I'm Robby, by the way. Um... we're in the same class. "
            rb " I'm kinda bored because I don't have much to do. "
            rb " And my friends are busy talking with other students, so... "
            rb " ...Yeah. "
            " You tried to think of what you could talk about with Robby... "
            " ...You came up with a lttle conversation topic after a few minutes. "
            if rubyknow == True:
                " You asked about Ruby. "
                rb " Oh, Ruby? she's doing fine. "
                rb " But I did hear that she's been overheating a lot today... "
                rb " I may need to check her out, but these breaks are too short for me to do so. "
                rb " Just gonna have to pray that she can last a bit longer without crashing. "
                rb " ...Yes, she has crashed a lot before. "
                rb " Due to multiple things, actually. "
                rb " One time, Zip decided it would be a really funny idea to mess with her. "
                rb " ...So, she dumped a bucket of water on her. "
                rb " Causing Ruby to completely glitch out, and I had to fix her for the entire day. "
                rb " It was really annoying, but atleast I had an excuse to skip school for the day... I guess. "
                rb " Sometimes I wish that Zip and the other guys would stop being so annoying. "
                rb " Sometimes, they're slightly tolerable. And other times... they piss me off real bad. "
                rb " If you ever see Ruby, just tell her that I'll fix her when school is over. "
            else:
                " You asked about a girl with a TV for a head, asking if Robby knew her. "
                rb " Oh, Ruby? yeah, I know her. She's my friend, and she's doing fine. "
                rb " But I did hear that she's been overheating a lot today... "
                rb " I may need to check her out, but these breaks are too short for me to do so. "
                rb " Just gonna have to pray that she can last a bit longer without crashing. "
                rb " ...Yes, she has crashed a lot before. "
                rb " Due to multiple things, actually. "
                rb " One time, Zip decided it would be a really funny idea to mess with her. "
                rb " ...So, she dumped a bucket of water on her. "
                rb " Causing Ruby to completely glitch out, and I had to fix her for the entire day. "
                rb " It was really annoying, but atleast I had an excuse to skip school for the day... I guess. "
                rb " Sometimes I wish that Zip and the other guys would stop being so annoying. "
                rb " Sometimes, they're slightly tolerable. And other times... they piss me off real bad. "
                rb " If you ever see Ruby, just tell her that I'll fix her when school is over. "
            scene black with dissolve
            " You spent the rest of the break talking about things with Robby. "
            " He was pretty much just a chill guy. He would often mess with other rocks around him with his wrench out of boredom. "
            " ...You wonder how wrenches taste like now for some reason. "
            " Probably good. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that it was time for another class. "
            " You get up from where you were sitting, and you walked back into the school to go to your classroom. "
            pause 2.0
            jump historyclass2
label tuesdayback3:
    # petunia lizzy and kevin
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and saw three of your classmates there. "
    " You're thinking of talking to one of them...who do you talk to? "
    if popularknow == True and kevinknow == True:
        menu:
            " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                jump lesbians
            " {image=kevinicon} Kevin {image=kevinicon} ":
                jump nerdynerd
    elif popularknow == True and kevinknow == False:
        menu:
            " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                jump lesbians
            " {image=kevinicon} A nerd {image=kevinicon} ":
                jump nerdynerd
    elif popularknow == False and kevinknow == True:
        menu:
            " {image=popularicon} Popular looking girls {image=popularicon} ":
                jump lesbians
            " {image=kevinicon} Kevin {image=kevinicon} ":
                jump nerdynerd
    else:
        menu:
            " {image=popularicon} Popular looking girls {image=popularicon} ":
                jump lesbians
            " {image=kevinicon} Popular looking girls {image=kevinicon} ":
                jump nerdynerd
    label lesbians:
        show petuniaangry at left with easeinright
        show lizzyneutral at right with easeinright
        if popularknow == True:
            p " This little prick...! "
            lz " Calm down, Petunia. It's just a hater, they're not gonna do anything to you. "
            " You asked them what was going on. "
            p " Oh, uh. Hi [name]. Nothing, just an annoying bitch commenting on my video. "
            lz " Erhh... for context, someone said that her dancing was bad. "
            p " My dancing is AMAZING, thank you! "
            p " Look at this! "
            " Petunia shoves her phone into your face, showing you her video of her dancing. "
            " ...Her dancing skills were alright, actually. It wasn't that bad. "
            " Atleast she wasn't those types of girls who are trying to make themselves look hot. "
            " And only putting all of the effort on some parts of the song. "
            p " My dancing skills aren't THAT bad, right, [name]?! "
            " You reassure her that her dancing skills were fine. "
            p " SEE?! Even [name] agrees that it's fine! "
            p " I don't know why they wasted their time to comment on my video like that, when all they could've done was just scroll away if they didn't like it! "
            p " Geez, people are idiots... "
            " You tell Petunia that she could just delete the comment... "
            " ...So that she could'nt see it again. "
            hide petuniaangry at bottom
            show petuniasurprised at left
            p " ... "
            p " Okay, I honestly don't know why I haven't thought of doing that. "
            hide lizzyneutral at bottom
            show lizzyconfused at right
            lz " I literally told you to do it about...5 times before [name] got here.. "
            hide petuniasurprised at bottom
            show petunianeutral at left
            p " Oh, uh. Sorry, Liz...guess I got too distracted on that one person. "
            hide lizzyconfused at bottom
            show lizzyneutral at right
            lz " It's alright. Just remember that you shouldn't let haters get to you. "
            lz " Haters are gonna hate, but remember that you're great and all that. "
            hide petunianeutral at bottom
            show petuniahappy at left
            p " Yeah! Thanks, Liz! "
            hide lizzyneutral at bottom
            show lizzyhappy at right
            lz " No problem. "
            " Honestly, it's a bit stupid that she got a little mad at a comment. "
            " She could've just...you know...ignored it... "
            " And not pay attention to it at all... "
            " But, eh... atleast she's gonna delete it and ignore it now. "
            scene black with dissolve
            " You spent the entire break talking to Petunia and Lizzy. "
            " Petunia was just telling you and Lizzy about recent drama she's heard on tiktok. "
            " Interesting... "
            play sound "audio/bellring.mp3"
            " ...Though, in the middle of the yapping session, the bell rings. "
            " Petunia says that she'll say more later. "
            " You all then went back to the classroom for the next class. "
            pause 2.0
            jump historyclass2
        else:
            x " This little prick...! "
            x " Calm down, Petunia. It's just a hater, they're not gonna do anything to you. "
            " You asked them what was going on. "
            x " Oh, uh. Hi [name]. Nothing, just an annoying bitch commenting on my video. "
            x " Erhh... for context, someone said that her dancing was bad. "
            x " My dancing is AMAZING, thank you! "
            x " Look at this! "
            " She shoves her phone into your face, showing you her video of her dancing. "
            " ...Her dancing skills were alright, actually. It wasn't that bad. "
            " Atleast she wasn't those types of girls who are trying to make themselves look hot. "
            " And only putting all of the effort on some parts of the song. "
            x " My dancing skills aren't THAT bad, right, [name]?! "
            " You reassure her that her dancing skills were fine. "
            x " SEE?! Even [name] agrees that it's fine! "
            x " I don't know why they wasted their time to comment on my video like that, when all they could've done was just scroll away if they didn't like it! "
            x " Geez, people are idiots... "
            " You tell her that she could just delete the comment... "
            " ...So that she could'nt see it again. "
            hide petuniaangry at bottom
            show petuniasurprised at left
            x " ... "
            x " Okay, I honestly don't know why I haven't thought of doing that. "
            hide lizzyneutral at bottom
            show lizzyconfused at right
            x " I literally told you to do it about...5 times before [name] got here.. "
            hide petuniasurprised at bottom
            show petunianeutral at left
            x " Oh, uh. Sorry, Liz...guess I got too distracted on that one person. "
            hide lizzyconfused at bottom
            show lizzyneutral at right
            x " It's alright. Just remember that you shouldn't let haters get to you. "
            x " Haters are gonna hate, but remember that you're great and all that. "
            hide petunianeutral at bottom
            show petuniahappy at left
            x " Yeah! Thanks, Liz! "
            hide lizzyneutral at bottom
            show lizzyhappy at right
            x " No problem. "
            " Honestly, it's a bit stupid that she got a little mad at a comment. "
            " She could've just...you know...ignored it... "
            " And not pay attention to it at all... "
            " But, eh... atleast she's gonna delete it and ignore it now. "
            hide petuniahappy at bottom
            show petunianeutral at left
            hide lizzyhappy at bottom
            show lizzyneutral at right
            x " Ooooh, right! I forgot we were supposed to introduce ourselves to [name]! "
            x " Heh, sorry buddy. Looks like I got too distracted! "
            $ popularknow = True
            p " I'm Petunia! "
            lz " And I'm Lizzy. We're best friends. "
            hide petunianeutral at bottom
            show petuniahappy at left
            p " And we're inseperable! "
            hide petuniahappy at bottom
            show petunianeutral at left
            p " Now that we got that over with... "
            p " You guys wanna hear some drama I've heard of? "
            lz " Sure, why not. I love me some tea. "
            " You nodded, wanting to hear drama. "
            p " O-kay! so, basically... "
            scene black with dissolve
            " You spent the entire break talking to Petunia and Lizzy. "
            " Petunia was just telling you and Lizzy about recent drama she's heard on tiktok. "
            " Interesting... "
            play sound "audio/bellring.mp3"
            " ...Though, in the middle of the yapping session, the bell rings. "
            " Petunia says that she'll say more later. "
            " You all then went back to the classroom for the next class. "
            pause 2.0
            jump historyclass2
    label nerdynerd:
        show kevinneutral at center with easeinleft
        if kevinknow == True:
            " You asked Kevin what he was doing. "
            kv " Greetings, [name]. "
            kv " I'm playing chess on my phone. Please stay quiet so that I could concentrate... "
            " ...He plays chess? Well, it isn't that surprising that he does. "
            " He's a nerd, after all. "
            " You stayed silent and sat down next to him. Waiting for him to win, or not. "
            " Eventually, after a few minutes, he manages to win the match. "
            hide kevinneutral at bottom
            show kevinhappy at center
            kv " Nice, I knew I would win that one! "
            hide kevinhappy at bottom
            show kevinneutral at center
            kv " Ahem... did you want to talk to me about something? "
            " ...You honestly didn't know what to talk about with him. "
            " You looked around and saw that some girl was raging at her phone. "
            " You asked Kevin if he knew anything about what was going on over there. "
            kv " Oh? Petunia? "
            kv " Yes, she's just raging over a comment she got on her video... "
            kv " I overheard about it while I was playing chess to cure my boredom. "
            kv " Doesn't she know that she can just...delete the comment? "
            kv " Though, I could agree on one thing I heard her say... "
            kv " ...That the commenter could've just scrolled away instead of causing trouble if they didn't like the video. "
            kv " It's really just that simple, and it's not a hard thing to do... "
            kv " People really are just looking for trouble these days. "
            kv " But, what can we do? not like we can stop them or anything. "
            kv " We also can't change what they think about a certain something. "
            kv " It's only best for us to just ignore them for now. "
            scene black with dissolve
            " You spent the rest of the break talking about things with Kevin. "
            " He made some pretty good points that you could agree with, even though he's a nerd. "
            " Pretty nice. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that the break was over. "
            " You get up from you were sitting, and you went back into the school to go to the next class. "
            pause 2.0
            jump historyclass2
        else:
            " You asked the nerd what he was doing. "
            x " Greetings, [name]. "
            x " I'm playing chess on my phone. Please stay quiet so that I could concentrate... "
            " ...He plays chess? Well, it isn't that surprising that he does. "
            " He's a nerd, after all. "
            " You stayed silent and sat down next to him. Waiting for him to win, or not. "
            " Eventually, after a few minutes, he manages to win the match. "
            hide kevinneutral at bottom
            show kevinhappy at center
            x " Nice, I knew I would win that one! "
            hide kevinhappy at bottom
            show kevinneutral at center
            x " Oh, uh. Apologies, I haven't introduced myself to you yet. "
            $ kevinknow = True
            kv " I'm Kevin. It's nice to meet you. "
            kv " Ahem... did you want to talk to me about something? "
            " ...You honestly didn't know what to talk about with him. "
            " You looked around and saw that some girl was raging at her phone. "
            " You asked Kevin if he knew anything about what was going on over there. "
            kv " Oh? Petunia? "
            kv " Yes, she's just raging over a comment she got on her video... "
            kv " I overheard about it while I was playing chess to cure my boredom. "
            kv " Doesn't she know that she can just...delete the comment? "
            kv " Though, I could agree on one thing I heard her say... "
            kv " ...That the commenter could've just scrolled away instead of causing trouble if they didn't like the video. "
            kv " It's really just that simple, and it's not a hard thing to do... "
            kv " People really are just looking for trouble these days. "
            kv " But, what can we do? not like we can stop them or anything. "
            kv " We also can't change what they think about a certain something. "
            kv " It's only best for us to just ignore them for now. "
            scene black with dissolve
            " You spent the rest of the break talking about things with Kevin. "
            " He made some pretty good points that you could agree with, even though he's a nerd. "
            " Pretty nice. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that the break was over. "
            " You get up from you were sitting, and you went back into the school to go to the next class. "
            pause 2.0
            jump historyclass2
label tuesdaygym3:
    # abbie and edward - edward bullies abbie
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walk into the gym and spot someone causing trouble to another student. "
    " Let's go see what's going on. "
    show abbiesad at left with easeinright
    show edwardbully at right with easeinright
    if abbieknow == True and oligangknow == True:
        a " ...Please stop... "
        ed " Come on, I'm just having some fun with you! "
        ed " Jeez, you really are a weak loser, eh? "
        ed " I'm lucky that no teachers have seen me hitting you yet. "
        ed " Time for me to use the walking punching bag! "
        " Abbie makes a weak attempt at punching Edward, but he fails. "
        hide edwardbully at bottom
        show edwardneutral at right
        " Edward manages to dodge and catch Abbie's fist. "
        ed " Oho, you're trying to fight back now, huh? "
        ed " You'll need a lot more skill and strength if you wanna fight me, idiot! "
        hide edwardneutral at bottom
        show edwardbully at right
        show edwardbully at center with move
        ed " Now, let me show you how to punch for REALS! "
        hide edwardbully at bottom
        show edwardangry at center
        show edwardangry at right with move
        " Before Edward could land a punch on Abbie, you managed to hit him first. "
        if kind == True:
            " ...Huh? what's happened to you? you've never even hurt a fly, and you... "
            " You hit someone? well that's surprising. "
        elif calm == True:
            " Woah. You've always been a chill guy, but you actually... "
            " You actually hit him. That's surprising. "
        elif mean == True:
            " ...Well that felt good to do. "
        ed " Ow! good heavens... "
        if kind == True:
            ed " Well, looks like little [mr] goody two-shoes has changed up. "
            ed " Jeez, that hurt... "
        elif calm == True:
            ed " Looks like little [mr] chill [person] has changed up. "
            ed " God, that hurt. "
        elif mean == True:
            ed " Oh jeez. You little prick... "
        elif clairebeatup == True and clairesorry,abbiemeandefend == False:
            ed " Not cool dude. Not cool. "
        elif clairebeatup,clairesorry == True and abbiemeandefend == True:
            ed " ...You. "
            " He seems to recognize you. "
        ed " I wasn't even doing anything bad to him! God. "
        ed " You know what, I'm leaving. Screw this place. "
        hide edwardangry at right with easeoutright
        show abbiesad at center with move
        " ...He left. "
        hide abbiesad at bottom
        show abbieneutral at center
        a " ... "
        a " ...Thank you for...defending me, [name]... "
        a " I really wish I could hit him like that...But I can't, I'm too weak... "
        if abbielv >= 10:
            $ abbielv += 10
            $ abbieteach = True
            " You told him that you could help him with that. "
            a " Wh...wait, really? You could? "
            a " You mean...you're gonna teach me how to fight...? "
            " You nodded your head. You probably didn't know how to fight, but you're gonna try. "
            " You can literally just watch tutorials on how to fight people and teach those methods to Abbie. "
            hide abbieneutral at bottom
            show abbiehappy at center
            a " ...Wow...[name]... "
            a " Um...when do we start then...? I don't wanna deal with these bullies for much longer... "
            " You thought about it for a bit, before you told him that they were gonna start tomorrow, after school was over. "
            a " Tomorrow...okay...! "
            hide abbiehappy at bottom
            show abbieneutral at center
            a " Though, um... "
            a " If I do anything wrong, you can tell me... "
            " You patted his head. "
        elif abbielv == 10:
            $ abbielv += 10
            $ abbieteach = True
            " You told him that you could help him with that. "
            a " Wh...wait, really? You could? "
            a " You mean...you're gonna teach me how to fight...? "
            " You nodded your head. You probably didn't know how to fight, but you're gonna try. "
            " You can literally just watch tutorials on how to fight people and teach those methods to Abbie. "
            hide abbieneutral at bottom
            show abbiehappy at center
            a " ...Wow...[name]... "
            a " Um...when do we start then...? I don't wanna deal with these bullies for much longer... "
            " You thought about it for a bit, before you told him that they were gonna start tomorrow, after school was over. "
            a " Tomorrow...okay...! "
            hide abbiehappy at bottom
            show abbieneutral at center
            a " Though, um... "
            a " If I do anything wrong, you can tell me... "
            " You patted his head. "
        else:
            $ abbieteach = False
            " You wished you could help him, but you don't know how. "
            " You just patted his head and told him that everything will be okay. "
            a " ...I hope so... "
        scene black with dissolve
        " You spent the rest of the break comforting Abbie. "
        " Telling him that he was gonna be alright... "
        " ...And his pain was gonna be over soon when he graduates. "
        " Well, you're not sure about that, but you just want him to feel better. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, the break now over. "
        " You and Abbie walk to the classroom for the next class. "
        pause 2.0
        jump historyclass2
    elif abbieknow == True and oligangknow == False:
        a " ...Please stop... "
        x " Come on, I'm just having some fun with you! "
        x " Jeez, you really are a weak loser, eh? "
        x " I'm lucky that no teachers have seen me hitting you yet. "
        x " Time for me to use the walking punching bag! "
        " Abbie makes a weak attempt at punching the other guy, but he fails. "
        hide edwardbully at bottom
        show edwardneutral at right
        " The mean boy manages to dodge and catch Abbie's fist. "
        x " Oho, you're trying to fight back now, huh? "
        x " You'll need a lot more skill and strength if you wanna fight me, idiot! "
        hide edwardneutral at bottom
        show edwardbully at right
        show edwardbully at center with move
        x " Now, let me show you how to punch for REALS! "
        hide edwardbully at bottom
        show edwardangry at center
        show edwardangry at right with move
        " Before the guy could land a punch on Abbie, you managed to hit him first. "
        if kind == True:
            " ...Huh? what's happened to you? you've never even hurt a fly, and you... "
            " You hit someone? well that's surprising. "
        elif calm == True:
            " Woah. You've always been a chill guy, but you actually... "
            " You actually hit him. That's surprising. "
        elif mean == True:
            " ...Well that felt good to do. "
        x " Ow! good heavens... "
        if kind == True:
            x " Well, looks like little [mr] goody two-shoes has changed up. "
            x " Jeez, that hurt... "
        elif calm == True:
            x " Looks like little [mr] chill [person] has changed up. "
            x " God, that hurt. "
        elif mean == True:
            x " Oh jeez. You little prick... "
        elif clairebeatup == True and clairesorry,abbiemeandefend == False:
            x " Not cool dude. Not cool. "
        elif clairebeatup,clairesorry == True and abbiemeandefend == True:
            x " ...You. "
            " He seems to recognize you. "
        x " I wasn't even doing anything bad to him! God. "
        x " You know what, I'm leaving. Screw this place. "
        hide edwardangry at right with easeoutright
        show abbiesad at center with move
        " ...He left. "
        hide abbiesad at bottom
        show abbieneutral at center
        a " ... "
        a " ...Thank you for...defending me, [name]... "
        a " I really wish I could hit him like that...But I can't, I'm too weak... "
        if abbielv >= 10:
            $ abbielv += 10
            $ abbieteach = True
            " You told him that you could help him with that. "
            a " Wh...wait, really? You could? "
            a " You mean...you're gonna teach me how to fight...? "
            " You nodded your head. You probably didn't know how to fight, but you're gonna try. "
            " You can literally just watch tutorials on how to fight people and teach those methods to Abbie. "
            hide abbieneutral at bottom
            show abbiehappy at center
            a " ...Wow...[name]... "
            a " Um...when do we start then...? I don't wanna deal with these bullies for much longer... "
            " You thought about it for a bit, before you told him that they were gonna start tomorrow, after school was over. "
            a " Tomorrow...okay...! "
            hide abbiehappy at bottom
            show abbieneutral at center
            a " Though, um... "
            a " If I do anything wrong, you can tell me... "
            " You patted his head. "
        elif abbielv == 10:
            $ abbielv += 10
            $ abbieteach = True
            " You told him that you could help him with that. "
            a " Wh...wait, really? You could? "
            a " You mean...you're gonna teach me how to fight...? "
            " You nodded your head. You probably didn't know how to fight, but you're gonna try. "
            " You can literally just watch tutorials on how to fight people and teach those methods to Abbie. "
            hide abbieneutral at bottom
            show abbiehappy at center
            a " ...Wow...[name]... "
            a " Um...when do we start then...? I don't wanna deal with these bullies for much longer... "
            " You thought about it for a bit, before you told him that they were gonna start tomorrow, after school was over. "
            a " Tomorrow...okay...! "
            hide abbiehappy at bottom
            show abbieneutral at center
            a " Though, um... "
            a " If I do anything wrong, you can tell me... "
            " You patted his head. "
        else:
            $ abbieteach = False
            " You wished you could help him, but you don't know how. "
            " You just patted his head and told him that everything will be okay. "
            a " ...I hope so... "
        scene black with dissolve
        " You spent the rest of the break comforting Abbie. "
        " Telling him that he was gonna be alright... "
        " ...And his pain was gonna be over soon when he graduates. "
        " Well, you're not sure about that, but you just want him to feel better. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, the break now over. "
        " You and Abbie walk to the classroom for the next class. "
        pause 2.0
        jump historyclass2
    elif abbieknow == False and oligangknow == True:
        x " ...Please stop... "
        ed " Come on, I'm just having some fun with you! "
        ed " Jeez, you really are a weak loser, eh? "
        ed " I'm lucky that no teachers have seen me hitting you yet. "
        ed " Time for me to use the walking punching bag! "
        " The shy looking makes a weak attempt at punching Edward, but he fails. "
        hide edwardbully at bottom
        show edwardneutral at right
        " Edward manages to dodge and catch his fist. "
        ed " Oho, you're trying to fight back now, huh? "
        ed " You'll need a lot more skill and strength if you wanna fight me, idiot! "
        hide edwardneutral at bottom
        show edwardbully at right
        show edwardbully at center with move
        ed " Now, let me show you how to punch for REALS! "
        hide edwardbully at bottom
        show edwardangry at center
        show edwardangry at right with move
        " Before Edward could land a punch on the poor guy, you managed to hit him first. "
        if kind == True:
            " ...Huh? what's happened to you? you've never even hurt a fly, and you... "
            " You hit someone? well that's surprising. "
        elif calm == True:
            " Woah. You've always been a chill guy, but you actually... "
            " You actually hit him. That's surprising. "
        elif mean == True:
            " ...Well that felt good to do. "
        ed " Ow! good heavens... "
        if kind == True:
            ed " Well, looks like little [mr] goody two-shoes has changed up. "
            ed " Jeez, that hurt... "
        elif calm == True:
            ed " Looks like little [mr] chill [person] has changed up. "
            ed " God, that hurt. "
        elif mean == True:
            ed " Oh jeez. You little prick... "
        elif clairebeatup == True and clairesorry,abbiemeandefend == False:
            ed " Not cool dude. Not cool. "
        elif clairebeatup,clairesorry == True and abbiemeandefend == True:
            ed " ...You. "
            " He seems to recognize you. "
        ed " I wasn't even doing anything bad to him! God. "
        ed " You know what, I'm leaving. Screw this place. "
        hide edwardangry at right with easeoutright
        show abbiesad at center with move
        " ...He left. "
        hide abbiesad at bottom
        show abbieneutral at center
        x " ... "
        x " ...Thank you for...defending me, [name]... "
        $ abbieknow = True
        a " I'm Abbie, by the way...it's nice to meet you... "
        a " I really wish I could hit him like that...But I can't, I'm too weak... "
        if abbielv >= 10:
            $ abbielv += 10
            $ abbieteach = True
            " You told him that you could help him with that. "
            a " Wh...wait, really? You could? "
            a " You mean...you're gonna teach me how to fight...? "
            " You nodded your head. You probably didn't know how to fight, but you're gonna try. "
            " You can literally just watch tutorials on how to fight people and teach those methods to Abbie. "
            hide abbieneutral at bottom
            show abbiehappy at center
            a " ...Wow...[name]... "
            a " Um...when do we start then...? I don't wanna deal with these bullies for much longer... "
            " You thought about it for a bit, before you told him that they were gonna start tomorrow, after school was over. "
            a " Tomorrow...okay...! "
            hide abbiehappy at bottom
            show abbieneutral at center
            a " Though, um... "
            a " If I do anything wrong, you can tell me... "
            " You patted his head. "
        elif abbielv == 10:
            $ abbielv += 10
            $ abbieteach = True
            " You told him that you could help him with that. "
            a " Wh...wait, really? You could? "
            a " You mean...you're gonna teach me how to fight...? "
            " You nodded your head. You probably didn't know how to fight, but you're gonna try. "
            " You can literally just watch tutorials on how to fight people and teach those methods to Abbie. "
            hide abbieneutral at bottom
            show abbiehappy at center
            a " ...Wow...[name]... "
            a " Um...when do we start then...? I don't wanna deal with these bullies for much longer... "
            " You thought about it for a bit, before you told him that they were gonna start tomorrow, after school was over. "
            a " Tomorrow...okay...! "
            hide abbiehappy at bottom
            show abbieneutral at center
            a " Though, um... "
            a " If I do anything wrong, you can tell me... "
            " You patted his head. "
        else:
            $ abbieteach = False
            " You wished you could help him, but you don't know how. "
            " You just patted his head and told him that everything will be okay. "
            a " ...I hope so... "
        scene black with dissolve
        " You spent the rest of the break comforting Abbie. "
        " Telling him that he was gonna be alright... "
        " ...And his pain was gonna be over soon when he graduates. "
        " Well, you're not sure about that, but you just want him to feel better. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, the break now over. "
        " You and Abbie walk to the classroom for the next class. "
        pause 2.0
        jump historyclass2
    else:
        x " ...Please stop... "
        x " Come on, I'm just having some fun with you! "
        x " Jeez, you really are a weak loser, eh? "
        x " I'm lucky that no teachers have seen me hitting you yet. "
        x " Time for me to use the walking punching bag! "
        " The shy looking makes a weak attempt at punching the other guy, but he fails. "
        hide edwardbully at bottom
        show edwardneutral at right
        " The other guy manages to dodge and catch his fist. "
        x " Oho, you're trying to fight back now, huh? "
        x " You'll need a lot more skill and strength if you wanna fight me, idiot! "
        hide edwardneutral at bottom
        show edwardbully at right
        show edwardbully at center with move
        x " Now, let me show you how to punch for REALS! "
        hide edwardbully at bottom
        show edwardangry at center
        show edwardangry at right with move
        " Before the other guy could land a punch on the poor guy, you managed to hit him first. "
        if kind == True:
            " ...Huh? what's happened to you? you've never even hurt a fly, and you... "
            " You hit someone? well that's surprising. "
        elif calm == True:
            " Woah. You've always been a chill guy, but you actually... "
            " You actually hit him. That's surprising. "
        elif mean == True:
            " ...Well that felt good to do. "
        x " Ow! good heavens... "
        if kind == True:
            x " Well, looks like little [mr] goody two-shoes has changed up. "
            x " Jeez, that hurt... "
        elif calm == True:
            x " Looks like little [mr] chill [person] has changed up. "
            x " God, that hurt. "
        elif mean == True:
            x " Oh jeez. You little prick... "
        elif clairebeatup == True and clairesorry,abbiemeandefend == False:
            x " Not cool dude. Not cool. "
        elif clairebeatup,clairesorry == True and abbiemeandefend == True:
            x " ...You. "
            " He seems to recognize you. "
        x " I wasn't even doing anything bad to him! God. "
        x " You know what, I'm leaving. Screw this place. "
        hide edwardangry at right with easeoutright
        show abbiesad at center with move
        " ...He left. "
        hide abbiesad at bottom
        show abbieneutral at center
        x " ... "
        x " ...Thank you for...defending me, [name]... "
        $ abbieknow = True
        a " I'm Abbie, by the way...it's nice to meet you... "
        a " I really wish I could hit him like that...But I can't, I'm too weak... "
        if abbielv >= 10:
            $ abbielv += 10
            $ abbieteach = True
            " You told him that you could help him with that. "
            a " Wh...wait, really? You could? "
            a " You mean...you're gonna teach me how to fight...? "
            " You nodded your head. You probably didn't know how to fight, but you're gonna try. "
            " You can literally just watch tutorials on how to fight people and teach those methods to Abbie. "
            hide abbieneutral at bottom
            show abbiehappy at center
            a " ...Wow...[name]... "
            a " Um...when do we start then...? I don't wanna deal with these bullies for much longer... "
            " You thought about it for a bit, before you told him that they were gonna start tomorrow, after school was over. "
            a " Tomorrow...okay...! "
            hide abbiehappy at bottom
            show abbieneutral at center
            a " Though, um... "
            a " If I do anything wrong, you can tell me... "
            " You patted his head. "
        elif abbielv == 10:
            $ abbielv += 10
            $ abbieteach = True
            " You told him that you could help him with that. "
            a " Wh...wait, really? You could? "
            a " You mean...you're gonna teach me how to fight...? "
            " You nodded your head. You probably didn't know how to fight, but you're gonna try. "
            " You can literally just watch tutorials on how to fight people and teach those methods to Abbie. "
            hide abbieneutral at bottom
            show abbiehappy at center
            a " ...Wow...[name]... "
            a " Um...when do we start then...? I don't wanna deal with these bullies for much longer... "
            " You thought about it for a bit, before you told him that they were gonna start tomorrow, after school was over. "
            a " Tomorrow...okay...! "
            hide abbiehappy at bottom
            show abbieneutral at center
            a " Though, um... "
            a " If I do anything wrong, you can tell me... "
            " You patted his head. "
        else:
            $ abbieteach = False
            " You wished you could help him, but you don't know how. "
            " You just patted his head and told him that everything will be okay. "
            a " ...I hope so... "
        scene black with dissolve
        " You spent the rest of the break comforting Abbie. "
        " Telling him that he was gonna be alright... "
        " ...And his pain was gonna be over soon when he graduates. "
        " Well, you're not sure about that, but you just want him to feel better. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, the break now over. "
        " You and Abbie walk to the classroom for the next class. "
        pause 2.0
        jump historyclass2
label tuesdaycafe3:
    # engel, riley, lana
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted three of your classmates vibing. "
    " You're thinking about talking to one of them...who do you talk to? "
    if engelknow,rileyknow,lanaknow == True:
        menu:
            " {image=engelicon} Engel {image=engelicon} ":
                jump angel
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump devil
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump idontknowlol
    elif engelknow,rileyknow == True and lanaknow == False:
        menu:
            " {image=engelicon} Engel {image=engelicon} ":
                jump angel
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump devil
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump idontknowlol
    elif engelknow,lanaknow == True and rileyknow == False:
        menu:
            " {image=engelicon} Engel {image=engelicon} ":
                jump angel
            " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                jump devil
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump idontknowlol
    elif rileyknow,lanaknow == True and engelknow == False:
        menu:
            " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                jump angel
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump devil
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump idontknowlol
    elif engelknow == True and rileyknow,lanaknow == False:
        menu:
            " {image=engelicon} Engel {image=engelicon} ":
                jump angel
            " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                jump devil
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump idontknowlol
    elif rileyknow == True and engelknow,lanaknow == False:
        menu:
            " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                jump angel
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump devil
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump idontknowlol
    elif lanaknow == True and engelknow,rileyknow == False:
        menu:
            " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                jump angel
            " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                jump devil
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump idontknowlol
    else:
        menu:
            " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                jump angel
            " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                jump devil
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump idontknowlol
    label angel:
        show engelneutral at center with easeinright
        if engelknow == True:
            " You sit down next to Engel and saw that he was just zoning out. "
            e " ... "
            " You poke him a few times to snap him out of it. "
            e " ...Huh? Oh, sorry, [name]... "
            e " I've just been thinking about a few things, is all. "
            e " You know how I'm the star student? "
            e " It kind of pressures me a bit into being great and all. "
            e " But, I remind myself that I don't always have to be great. "
            e " I can just take life at my own pace and not rush anything, and that not I don't have to be perfect... "
            e " ...Because all of us aren't perfect. We will always have impurities. "
            e " It's just something we can't avoid, you know? "
            hide engelneutral at bottom
            show engelhappy at center
            e " So, if you ever feel down, and that you're not enough... "
            e " ...Just remember that you are. There's people that care about you... "
            e " And you probably know that they wouldn't like it if you're thinking like that, hehe. "
            e " You don't have to be perfect. Just do the best that you can. "
            e " Even if that best is getting a low score... "
            e " ...Okay, I might have to help you if you get a low score, but still. "
            e " Don't push yourself too hard, okay? "
            " You wish that Engel wouldn't push himself too much too. "
            hide engelhappy at bottom
            show engelcontent at center
            e " Heh, aww... "
            e " That's nice of you to say, [name]. "
            scene black with dissolve
            " You spent the rest of the break talking to Engel. "
            " You were mostly getting comforted randomly by Engel though. "
            " Not like you minded it. You thought it was nice to hear such reassuring words. "
            " Your parents could learn a thing or two before they... "
            " ...Yeah, let's not do a lore drop right now. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit. Time for another class. "
            " You get up from where you were sitting, and you walked back to your classroom. "
            pause 2.0
            jump historyclass2
        else:
            " You sit down next to the boy and saw that he was just zoning out. "
            x " ... "
            " You poke him a few times to snap him out of it. "
            x " ...Huh? Oh, sorry, [name]... "
            x " I've just been thinking about a few things, is all. "
            $ engelknow = True
            e " I'm Engel, by the way. It's nice to meet you... "
            e " ...I don't think I've mentioned it to you before, but I'm the star student here.. "
            e " I don't mean to say this as a 'bragging' way, it's just that... "
            e " It kind of pressures me a bit into being great and all. "
            e " But, I remind myself that I don't always have to be great. "
            e " I can just take life at my own pace and not rush anything, and that not I don't have to be perfect... "
            e " ...Because all of us aren't perfect. We will always have impurities. "
            e " It's just something we can't avoid, you know? "
            hide engelneutral at bottom
            show engelhappy at center
            e " So, if you ever feel down, and that you're not enough... "
            e " ...Just remember that you are. There's people that care about you... "
            e " And you probably know that they wouldn't like it if you're thinking like that, hehe. "
            e " You don't have to be perfect. Just do the best that you can. "
            e " Even if that best is getting a low score... "
            e " ...Okay, I might have to help you if you get a low score, but still. "
            e " Don't push yourself too hard, okay? "
            " You wish that Engel wouldn't push himself too much too. "
            hide engelhappy at bottom
            show engelcontent at center
            e " Heh, aww... "
            e " That's nice of you to say, [name]. "
            scene black with dissolve
            " You spent the rest of the break talking to Engel. "
            " You were mostly getting comforted randomly by Engel though. "
            " Not like you minded it. You thought it was nice to hear such reassuring words. "
            " Your parents could learn a thing or two before they... "
            " ...Yeah, let's not do a lore drop right now. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit. Time for another class. "
            " You get up from where you were sitting, and you walked back to your classroom. "
            pause 2.0
            jump historyclass2
    label devil:
        show rileyneutral at center with easeinleft
        if rileyknow == True:
            ri " EhhhhehHHAHAHHheheh. Hi [name]! "
            ri " What's up? You got something to talk about to me? "
            " You're kind of surprised that she wasn't talking about Oliver for once. "
            " And also a bit proud of her that she wasn't talking about him. "
            " You thought about something to ask Riley... "
            " You then asked her what was her favorite memory in this school. "
            ri " .mmmMMy favorite memory? WELL!! "
            ri " I know you're probably looking for me to say something not Oliver related, sooo..!! "
            ri " There was this one time where Miss Emily told us if we could knock down a stack of books on her desk, we would have no homework for a week!! "
            ri " ...We couldn't use our hands to do it. We could use items only. "
            ri " I had an idea, but I wasn't sure if it would work! "
            ri " But, I did it anyways and I threw my knife at the books! and guess what? it knocked down the books! "
            ri " ...I honestly don't know how I did it, since technically it wouldn't be possible for me to do that. "
            ri " But atleast I saved everyone from having history homework for a week! "
            ri " That feeling was great! Everyone was cheering for me! "
            hide rileyneutral at bottom
            show rileyhappy at center
            ri " Even my sweet, sweet Oliver! "
            " You were proud of her not talking about Oliver only for a few minutes. "
            " That has to be her new record of not talking about Oliver for a bit... "
            " Oh well, back to the Oliver yapping session... "
            scene black with dissolve
            " You spent the entire break listening to Riley talk about Oliver. "
            " Atleast you got to hear a few minutes of her yapping of something non-Oliver related. "
            " Sigh...you're assuming she has a lot of Oliver pictures in her room. "
            " But then again, she might not be that obsessed. But who knows? "
            " Definitely not me. "
            play sound "audio/bellring.mp3"
            " The bell rings. Looks like it's time for another class. "
            " You get up from your seat, and you walk over back to your classroom. "
            pause 2.0
            jump historyclass2
        else:
            x " EhhhhehHHAHAHHheheh. Hi [name]! "
            $ rileyknow = True
            ri " I'm Riley by the way!! Oliver's wife and girlfriend!! "
            " ...You can't really be...someone's wife and girlfriend at the smae time, can you? "
            ri " Anyway... What's up? You got something to talk about to me? "
            " You're kind of surprised that she wasn't talking about Oliver for once. Since you've heard that she keeps talking about Oliver."
            " And also a bit proud of her that she wasn't talking about him. "
            " You thought about something to ask Riley... "
            " You then asked her what was her favorite memory in this school. "
            ri " .mmmMMy favorite memory? WELL!! "
            ri " I know you're probably looking for me to say something not Oliver related, sooo..!! "
            ri " There was this one time where Miss Emily told us if we could knock down a stack of books on her desk, we would have no homework for a week!! "
            ri " ...We couldn't use our hands to do it. We could use items only. "
            ri " I had an idea, but I wasn't sure if it would work! "
            ri " But, I did it anyways and I threw my knife at the books! and guess what? it knocked down the books! "
            ri " ...I honestly don't know how I did it, since technically it wouldn't be possible for me to do that. "
            ri " But atleast I saved everyone from having history homework for a week! "
            ri " That feeling was great! Everyone was cheering for me! "
            hide rileyneutral at bottom
            show rileyhappy at center
            ri " Even my sweet, sweet Oliver! "
            " You were proud of her not talking about Oliver only for a few minutes. "
            " That has to be her new record of not talking about Oliver for a bit... "
            " Oh well, back to the Oliver yapping session... "
            scene black with dissolve
            " You spent the entire break listening to Riley talk about Oliver. "
            " Atleast you got to hear a few minutes of her yapping of something non-Oliver related. "
            " Sigh...you're assuming she has a lot of Oliver pictures in her room. "
            " But then again, she might not be that obsessed. But who knows? "
            " Definitely not me. "
            play sound "audio/bellring.mp3"
            " The bell rings. Looks like it's time for another class. "
            " You get up from your seat, and you walk over back to your classroom. "
            pause 2.0
            jump historyclass2
    label idontknowlol:
        show lananeutral at center with easeinright
        if lanaknow == True:
            " You sat down next to Lana, checking out what she was doing. "
            l " Hmhmh... your eyes look a little goofy... "
            " Looks like she's busy fixing her sock puppet. "
            " You poked her shoulder to get her attention. "
            l " Oh! Hi, [name]! "
            l " You see... I'm just fixing the eyes of my sock puppets! "
            l " They usually get like this, so I have to fix them every now and then... "
            l " And before you ask if it's annoying, it isn't that annoying! "
            l " I mean, sure, at times it is, but I can just get it fixed in a jiffy! "
            l " It's not too hard to fix it anyway. "
            l " After all, it's just a simple sock puppet! "
            l " Not like it's anything valuable, right? "
            " You nodded. You had a question pop up in your mind though... "
            " ...You asked Lana if she was ever asked to take those off. "
            l " Well, aside from taking them off for eating... "
            l " I {i}did{/i} have this one incident happen to me when I was way younger... "
            l " I was making my very first sock puppets, and I was really proud of what I had made!! "
            l " But, when it was time for class, the teacher asked me to take it off. "
            l " I actually got so upset, and I cried a bit... "
            hide lananeutral at bottom
            show lanahappy at center
            l " But! Of course, the teacher reassured little me that I can put it back on once class was over! "
            l " That teacher was the one that was really nice to me, too! "
            hide lanahappy at bottom
            show lananeutral at center
            l " So...yeah! "
            " Very interesting story time. "
            " She's been making sock puppets ever since she was a little kid, huh...? "
            " Cool funfact. "
            scene black with dissolve
            " You spent the rest of the break having a conversation with Lana about sock puppets. "
            " Maybe you should make yur own sock puppet too... "
            " And make it all cute and everything. You're gonna call it twinkletoes. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit. Looks like its time for another class. "
            " You get up from where you were sitting, and you walked back to your classroom for the next class. "
            pause 2.0
            jump historyclass2
        else:
            " You sat down next to the girl, checking out what she was doing. "
            x " Hmhmh... your eyes look a little goofy... "
            " Looks like she's busy fixing her sock puppet. "
            " You poked her shoulder to get her attention. "
            x " Oh! Hi, [name]! "
            $ lanaknow = True
            x " I don't think I got to tell you my name, sooo... "
            l " I'm Lana! I hope we can become the bestest of friends! "
            " You told her that it was nice to meet her, then asked her what she was doing. "
            l " You see... I'm just fixing the eyes of my sock puppets! "
            l " They usually get like this, so I have to fix them every now and then... "
            l " And before you ask if it's annoying, it isn't that annoying! "
            l " I mean, sure, at times it is, but I can just get it fixed in a jiffy! "
            l " It's not too hard to fix it anyway. "
            l " After all, it's just a simple sock puppet! "
            l " Not like it's anything valuable, right? "
            " You nodded. You had a question pop up in your mind though... "
            " ...You asked Lana if she was ever asked to take those off. "
            l " Well, aside from taking them off for eating... "
            l " I {i}did{/i} have this one incident happen to me when I was way younger... "
            l " I was making my very first sock puppets, and I was really proud of what I had made!! "
            l " But, when it was time for class, the teacher asked me to take it off. "
            l " I actually got so upset, and I cried a bit... "
            hide lananeutral at bottom
            show lanahappy at center
            l " But! Of course, the teacher reassured little me that I can put it back on once class was over! "
            l " That teacher was the one that was really nice to me, too! "
            hide lanahappy at bottom
            show lananeutral at center
            l " So...yeah! "
            " Very interesting story time. "
            " She's been making sock puppets ever since she was a little kid, huh...? "
            " Cool funfact. "
            scene black with dissolve
            " You spent the rest of the break having a conversation with Lana about sock puppets. "
            " Maybe you should make yur own sock puppet too... "
            " And make it all cute and everything. You're gonna call it twinkletoes. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit. Looks like its time for another class. "
            " You get up from where you were sitting, and you walked back to your classroom for the next class. "
            pause 2.0
            jump historyclass2
label tuesdayrooftop3:
    # skell and bubble
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked up onto the rooftop to get some fresh air. "
    " As you were looking around, you spotted two of your classmates vibing. "
    " You thought of talking to one of them... who do you talk to? "
    if skellknow == True and bubbleknow == True:
        menu:
            " {image=skellicon} Skell {image=skellicon} ":
                jump bruh
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump dude
    elif skellknow == True and bubbleknow == False:
        menu:
            " {image=skellicon} Skell {image=skellicon} ":
                jump bruh
            " {image=bubbleicon} A girl with a rubber duck on her head {image=bubbleicon} ":
                jump dude
    elif skellknow == False and bubbleknow == True:
        menu:
            " {image=skellicon} An emo looking guy {image=skellicon} ":
                jump bruh
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump dude
    else:
        menu:
            " {image=skellicon} An emo looking guy {image=skellicon} ":
                jump bruh
            " {image=bubbleicon} A girl with a rubber duck on her head {image=bubbleicon} ":
                jump dude
    label bruh:
        show skellneutral at center with easeinright
        if skellknow == True:
            " You walked up to him and asked him what he was doing. "
            sk " Hi, [name]. "
            sk " Just came here to chill... "
            sk " ...You're surprised that I'm not at the back of the school, huh? "
            sk " I mean, that's kind of reasonable. I do usually hang out there... "
            sk " Felt doing something a little different though. "
            sk " Plus, it's nice to hang out up here too. "
            sk " I like the view... "
            sk " ... "
            sk " ...Do you, uh... "
            sk " Just wanna hang out with me here...? "
            sk " Or do you wanna go somewhere else. "
            " You feel like you want some peace for a bit. "
            " So, you decided to stay with Skell for now. "
            sk " ...Okay. "
            sk " I needed someone to talk to anyway... "
            scene black with dissolve
            " You spent the rest of the break hanging out with Skell. "
            " It was pretty nice, you and him would occassionally talk about random things. "
            " ...While looking at the very pretty view. "
            " The world may not look great and all, but atleast you got some time to relax from it's obstacles in this moment. "
            play sound "audio/bellring.mp3"
            " Too bad you have to go to your next class now. "
            " You walk down from the rooftop and you go back to your classroom for the next class. "
            pause 2.0
            jump historyclass2
        else:
            " You walked up to him and asked him what he was doing. "
            x " Hi, [name]. "
            x " Just came here to chill... "
            $ skellknow = True
            sk " I'm Skell, by the way. It's um...nice to meet you. "
            sk " ...Most people would be kind of surprised that I'm not at the back of the school right now... "
            sk " I mean, that's kind of reasonable. I do usually hang out there... "
            sk " Felt doing something a little different though. "
            sk " Plus, it's nice to hang out up here too. "
            sk " I like the view... "
            sk " ... "
            sk " ...Do you, uh... "
            sk " Just wanna hang out with me here...? "
            sk " Or do you wanna go somewhere else. "
            " You feel like you want some peace for a bit. "
            " So, you decided to stay with Skell for now. "
            sk " ...Okay. "
            sk " I needed someone to talk to anyway... "
            scene black with dissolve
            " You spent the rest of the break hanging out with Skell. "
            " It was pretty nice, you and him would occassionally talk about random things. "
            " ...While looking at the very pretty view. "
            " The world may not look great and all, but atleast you got some time to relax from it's obstacles in this moment. "
            play sound "audio/bellring.mp3"
            " Too bad you have to go to your next class now. "
            " You walk down from the rooftop and you go back to your classroom for the next class. "
            pause 2.0
            jump historyclass2
    label dude:
        show bubbleneutral at center with easeinleft
        if bubbleknow == True:
            " You walked up to her and asked her what she was doing. "
            b " Hiya [name]!! "
            b " Just studying for history in case if Miss Emily throws another surprise quiz at us... "
            b " She sometimes does that to keep us studying. And it works pretty well! "
            b " ...Well, it works good on the students who want to have good grades. "
            b " Some of our classmates don't even study for history sometimes, causing them to fail at the history quizzes... "
            b " Atleast Miss Emily isn't like those teachers who would get mad at you and yell if you got a single question wrong. "
            b " Everyone would be pretty afraid of her, if she was like that. "
            b " But, from what I heard... Miss Emily really doesn't want to be like that kind of teacher at all. "
            b " She just wants to make sure her students can learn properly and be happy at the same time. "
            b " That's why she also throws in fun activities from time to time! "
            b " From what I heard... "
            hide bubbleneutral at bottom
            show bubblehappy at center
            b " She's planning to throw another fun activity this wednesday! "
            b " Isn't that exciting? "
            b " I know that history might not be everyone's thing, but Miss Emily's activities are really fun! "
            b " You'll just have to see it for yourself when wednesday hits! "
            hide bubblehappy at bottom
            show bubbleneutral at center
            b " Anywho... you can talk to me whilst I'm studying! "
            b " It can get a bit lonely for me without someone to talk to, heh... "
            b " Besides, I don't mind it whenever someone talks to me while I'm studying! "
            b " Cmere! "
            " Bubble motions for you to sit down with her on the ground of the rooftop. "
            " You sat down next to her and started having a nice conversation with her whilst she studies. "
            scene black with dissolve
            " You spent the rest of the break talking with Bubble on the rooftop as she studied. "
            " You're kind of wondering how she can focus on both studying and talking at the same time... "
            " It's probably a talent of hers to not get too distracted in talking. "
            " Nice. "
            play sound "audio/bellring.mp3"
            " The bell rings after a few minutes of studying. Time for history class. "
            " You get up from where you were sitting, and you walked down back into the school to go into your classroom for the next class. "
            pause 2.0
            jump historyclass2
        else:
            " You walked up to her and asked her what she was doing. "
            x " Hiya [name]!! "
            b " Oh, right!! I haven't introduced myself to you yet, silly me! "
            hide bubbleneutral at bottom
            show bubblehappy at center
            $ bubbleknow = True
            b " I'm Bubble! We're in the same class! "
            " You told her that it was nice to meet her, then asked what she was doing. "
            b " Just studying for history in case if Miss Emily throws another surprise quiz at us... "
            b " She sometimes does that to keep us studying. And it works pretty well! "
            b " ...Well, it works good on the students who want to have good grades. "
            b " Some of our classmates don't even study for history sometimes, causing them to fail at the history quizzes... "
            b " Atleast Miss Emily isn't like those teachers who would get mad at you and yell if you got a single question wrong. "
            b " Everyone would be pretty afraid of her, if she was like that. "
            b " But, from what I heard... Miss Emily really doesn't want to be like that kind of teacher at all. "
            b " She just wants to make sure her students can learn properly and be happy at the same time. "
            b " That's why she also throws in fun activities from time to time! "
            b " From what I heard... "
            hide bubbleneutral at bottom
            show bubblehappy at center
            b " She's planning to throw another fun activity this wednesday! "
            b " Isn't that exciting? "
            b " I know that history might not be everyone's thing, but Miss Emily's activities are really fun! "
            b " You'll just have to see it for yourself when wednesday hits! "
            hide bubblehappy at bottom
            show bubbleneutral at center
            b " Anywho... you can talk to me whilst I'm studying! "
            b " It can get a bit lonely for me without someone to talk to, heh... "
            b " Besides, I don't mind it whenever someone talks to me while I'm studying! "
            b " Cmere! "
            " Bubble motions for you to sit down with her on the ground of the rooftop. "
            " You sat down next to her and started having a nice conversation with her whilst she studies. "
            scene black with dissolve
            " You spent the rest of the break talking with Bubble on the rooftop as she studied. "
            " You're kind of wondering how she can focus on both studying and talking at the same time... "
            " It's probably a talent of hers to not get too distracted in talking. "
            " Nice. "
            play sound "audio/bellring.mp3"
            " The bell rings after a few minutes of studying. Time for history class. "
            " You get up from where you were sitting, and you walked down back into the school to go into your classroom for the next class. "
            pause 2.0
            jump historyclass2
label tuesdaylibrary3:
    # claire
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and spotted one of your classmates. "
    " They look like they're studying... you should go bother them. "
    if clairebeatup == True and clairesorry == False:
        " Hold on, that's Claire. "
        " ...No. Not right now. "
        " You'll apologize some other day. "
        scene black
        pause 2.0
        jump historyclass2
    else:
        pass
    show claireneutral at center with easeinright
    if claireknow == True:
        " You walked behind her, and gave her a little jumpscare. "
        hide claireneutral at bottom
        show clairescared at center
        " Gotta hit them with a quick 'BOO!!' " with vpunch
        c " Eeek!! "
        " Claire seemed to have only let out a quiet 'eek'. Boring. "
        " Though, you could understand, since this was a library. "
        c " Oh, it's just you, [name]... "
        hide clairescared at bottom
        show claireneutral at center
        c " Jeez, don't scare me like that next time! "
        c " Remember, this is a library...you know... where we're supposed to be quiet? "
        c " But then again, the librarian isn't here... "
        c " BUT still! we gotta follow the rules. I don't wanna get in trouble. "
        c " Cmere, sit with me... "
        " You sat down next to Claire. Once you were seated, you asked her what she was reading. "
        c " Just a book about history. It's for history class! "
        c " Gotta study because Miss Emily might throw a surprise quiz at us again... "
        c " While I'm praying that she won't, I know that she probably will.. "
        hide claireneutral at bottom
        show clairehappy at center
        c " You should study too, [name]! Just so that your butt wouldn't get beat. "
        " Well, you had nothing to do, so... "
        " You decided to study with Claire for history class. "
        scene black with dissolve
        " You spent the rest of the break studying with Claire. "
        " She would read a few things to you before asking you a question. "
        " She would not give you a hint if you got it wrong, and she continued doing this until you got everything right. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, stopping your study session with Claire. "
        " You get up from your seat, and you walked back to your classroom for the next class. "
        pause 2.0
        jump historyclass2
    else:
        " You walked behind her, and gave her a little jumpscare. "
        hide claireneutral at bottom
        show clairescared at center
        " Gotta hit them with a quick 'BOO!!' " with vpunch
        x " Eeek!! "
        " She seemed to have only let out a quiet 'eek'. Boring. "
        " Though, you could understand, since this was a library. "
        x " Oh, it's just you, [name]... "
        hide clairescared at bottom
        show claireneutral at center
        x " Jeez, don't scare me like that next time! "
        x " Remember, this is a library...you know... where we're supposed to be quiet? "
        x " But then again, the librarian isn't here... "
        x " BUT still! we gotta follow the rules. I don't wanna get in trouble. "
        x " Oh, right! I almost forgot to introduce myself to you! "
        $ claireknow = True
        c " I'm Claire! It's nice to meet you, [name]! "
        c " Cmere, sit with me... I don't want you to stand behind me for too long! "
        " You sat down next to Claire. Once you were seated, you asked her what she was reading. "
        c " Just a book about history. It's for history class! "
        c " Gotta study because Miss Emily might throw a surprise quiz at us again... "
        c " While I'm praying that she won't, I know that she probably will.. "
        hide claireneutral at bottom
        show clairehappy at center
        c " You should study too, [name]! Just so that your butt wouldn't get beat. "
        " Well, you had nothing to do, so... "
        " You decided to study with Claire for history class. "
        scene black with dissolve
        " You spent the rest of the break studying with Claire. "
        " She would read a few things to you before asking you a question. "
        " She would not give you a hint if you got it wrong, and she continued doing this until you got everything right. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, stopping your study session with Claire. "
        " You get up from your seat, and you walked back to your classroom for the next class. "
        pause 2.0
        jump historyclass2
label historyclass2:
    scene classroom with dissolve
    " You sat down on your seat and waited for the history teacher to arrive. "
    " After a few minutes, she enters the classroom. "
    show msemilyneutral at center with easeinright
    mse " Hello, class! "
    mse " Now, before we start our class for today, I have something to say! "
    mse " We'll be having an art-related activity on wednesday... "
    mse " ...So I'm saying this just so that you guys can prepare in advance! "
    mse " It's going to be a group project, since I know you guys like doing those. "
    mse " Anywho, let's get started with our lesson! "
    scene black with dissolve
    " Class was pretty boring. You had nothing to do other than copy a few things. "
    " You could hear a few students messing around in the back of the classroom ... "
    " Which ended up in them getting whacked on the head by Miss Emily's ruler. "
    " Yikes. You better be paying to class, you don't want to end up like them over there. "
    play sound "audio/bellring.mp3"
    " The bell rings, meaning that class was over. "
    " You got up from your seat and you walked back into the hallways. "
    pause 2.0
    jump tuesdaybreak4
label tuesdaybreak4:
    scene hallway with dissolve
    " You know the drill, you want to go somewhere. "
    " Where do you go, though? "
    menu:
        " {image=rileyicon} The front of the school {image=popularicon} ":
            jump tuesdayfront4
        " {image=rubyicon} The back of the school {image=robbyicon} ":
            jump tuesdayback4
        " {image=lanaicon} The Gym {image=engelicon} ":
            jump tuesdaygym4
        " The cafeteria ":
            jump tuesdaycafe4
        " {image=cubbieicon} The rooftop {image=abbieicon} ":
            jump tuesdayrooftop4
        " {image=bubbleicon} The library {image=bubbleicon} ":
            jump tuesdaylibrary4
label tuesdayfront4:
    # riley bothering petunia
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked outside of the school, and immediately you could hear someone bothering someone. "
    " What a normal day in school...let's go check out what's happening. "
    show petuniaconfused at right with easeinleft
    show rileyhappy at left with easeinleft
    if popularknow == True and rileyknow == True:
        p " Look girl, whoever told you that is lying -{nw}"
        ri " No, I know it's true! " with vpunch
        ri " Someone told me that Oliver's going to give me a big hug once he gets back to school tomorrow! "
        ri " I just know it's real! "
        ri " He's finally showing his feelings for me!! "
        p " Eeeh... "
        " Petunia looks at you as if she's asking for help. "
        " Help her? "
        menu:
            " Help Petunia ":
                $ popularlv += 10
                hide rileyhappy at bottom
                show rileyneutral at left
                if kind == True:
                    " You walked up to Riley and kindly told her to stop bothering Petunia. "
                    " You said that it was kind of making the other uncomfortable. "
                elif calm == True:
                    " You walked up to Riley and told her to stop bothering Petunia. "
                    " You calmly told her that it was making the girl uncomfortable. "
                elif mean == True:
                    " You just told Riley that Petunia doesn't want to deal with her right now. "
                ri " Oh, uh...! Sorry, then! "
                ri " I'll go get going... "
                hide rileyneutral at right with easeoutright
                hide petuniaconfused at bottom
                show petunianeutral at left
                show petunianeutral at center with move
                p " Thanks, [name]. "
                p " I don't really wanna say it, but she was starting to get real annoying. "
                p " She's gotta learn to not believe what anyone says... "
                p " Especially if it's Oliver related. "
                p " Anyway! I gotta go see Lizzy in the cafeteria. "
                p " See you later! "
                hide petunianeutral at right with easeoutright
                " ...Seems like you're just gonna have to stay here for a bit. "
                scene black with dissolve
                " You spent the rest of the break just chilling on a bench. "
                " While you were waiting for the break to be over, you were just playing blockblast. "
                " ...you suddenly get flashbacks to those utterly insane blockblast stories you kept seeing on your fyp. "
                " Eeeyikes. Let's not think about that right now."
                play sound "audio/bellring.mp3"
                " The bell eventually rings, pulling you out of your gaming session. "
                " You get up from the bench you were sitting on and you walk back to your classroom for the next class. "
                pause 2.0
                jump musicclass2
            " Nope, not my problem ":
                " You decided to not help Petunia. "
                hide rileyhappy at left with easeoutleft
                hide petuniaconfused at left with easeoutleft
                " You, instead sat on a nearby bench and watched Riley cause trouble to Petunia. "
                " Besides, it's not like it's your problem. "
                " Atleast you now get some free entertainment now. "
                scene black with dissolve
                " You spent the rest of the break watching Riley yap to Petunia. "
                " Petunia can't exactly move, because if she did, Riley would just follow her. "
                " ...And if she said anything, Riley wouldn't really listen to her. "
                " Now that you're thinking more about it, you kind of feel bad for Petunia having to deal with this. "
                " But, oh well. You can't really do anything about it now. "
                " Unless if you press the back button. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, stopping Riley from her yapping session and freeing Petunia. "
                " You get up from the bench you were sitting on and you walked to your classroom for the next class. "
                pause 2.0
                jump musicclass2
    elif popularknow == True and rileyknow == False:
        p " Look girl, whoever told you that is lying -{nw}"
        x " No, I know it's true! " with vpunch
        x " Someone told me that Oliver's going to give me a big hug once he gets back to school tomorrow! "
        x " I just know it's real! "
        x " He's finally showing his feelings for me!! "
        p " Eeeh... "
        " Petunia looks at you as if she's asking for help. "
        " Help her? "
        menu:
            " Help Petunia ":
                $ popularlv += 10
                hide rileyhappy at bottom
                show rileyneutral at left
                if kind == True:
                    " You walked up to the insane looking girl and kindly told her to stop bothering Petunia. "
                    " You said that it was kind of making the other uncomfortable. "
                elif calm == True:
                    " You walked up to the insane looking girl and told her to stop bothering Petunia. "
                    " You calmly told her that it was making the girl uncomfortable. "
                elif mean == True:
                    " You just told the insane looking girl that Petunia doesn't want to deal with her right now. "
                x " Oh, uh...! Sorry, then! "
                x " I'll go get going... "
                hide rileyneutral at right with easeoutright
                hide petuniaconfused at bottom
                show petunianeutral at left
                show petunianeutral at center with move
                p " Thanks, [name]. "
                p " I don't really wanna say it, but she was starting to get real annoying. "
                p " She's gotta learn to not believe what anyone says... "
                p " Especially if it's Oliver related. "
                p " Anyway! I gotta go see Lizzy in the cafeteria. "
                p " See you later! "
                hide petunianeutral at right with easeoutright
                " ...Seems like you're just gonna have to stay here for a bit. "
                scene black with dissolve
                " You spent the rest of the break just chilling on a bench. "
                " While you were waiting for the break to be over, you were just playing blockblast. "
                " ...you suddenly get flashbacks to those utterly insane blockblast stories you kept seeing on your fyp. "
                " Eeeyikes. Let's not think about that right now."
                play sound "audio/bellring.mp3"
                " The bell eventually rings, pulling you out of your gaming session. "
                " You get up from the bench you were sitting on and you walk back to your classroom for the next class. "
                pause 2.0
                jump musicclass2
            " Nope, not my problem ":
                " You decided to not help Petunia. "
                hide rileyhappy at left with easeoutleft
                hide petuniaconfused at left with easeoutleft
                " You, instead sat on a nearby bench and watched the insane looking girl cause trouble to Petunia. "
                " Besides, it's not like it's your problem. "
                " Atleast you now get some free entertainment now. "
                scene black with dissolve
                " You spent the rest of the break watching the other girl yap to Petunia. "
                " Petunia can't exactly move, because if she did, the girl would just follow her. "
                " ...And if she said anything, the girl wouldn't really listen to her. "
                " Now that you're thinking more about it, you kind of feel bad for Petunia having to deal with this. "
                " But, oh well. You can't really do anything about it now. "
                " Unless if you press the back button. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, stopping the girl from her yapping session and freeing Petunia. "
                " You get up from the bench you were sitting on and you walked to your classroom for the next class. "
                pause 2.0
                jump musicclass2
    elif popularknow == False and rileyknow == True:
        x " Look girl, whoever told you that is lying -{nw}"
        ri " No, I know it's true! " with vpunch
        ri " Someone told me that Oliver's going to give me a big hug once he gets back to school tomorrow! "
        ri " I just know it's real! "
        ri " He's finally showing his feelings for me!! "
        x " Eeeh... "
        " The popular looking girl looks at you as if she's asking for help. "
        " Help her? "
        menu:
            " Help the popular girl ":
                $ popularlv += 10
                hide rileyhappy at bottom
                show rileyneutral at left
                if kind == True:
                    " You walked up to Riley and kindly told her to stop bothering the popular girl. "
                    " You said that it was kind of making the other uncomfortable. "
                elif calm == True:
                    " You walked up to Riley and told her to stop bothering the popular girl. "
                    " You calmly told her that it was making the girl uncomfortable. "
                elif mean == True:
                    " You just told Riley that the popular girl doesn't want to deal with her right now. "
                ri " Oh, uh...! Sorry, then! "
                ri " I'll go get going... "
                hide rileyneutral at right with easeoutright
                hide petuniaconfused at bottom
                show petunianeutral at left
                show petunianeutral at center with move
                x " Thanks, [name]. "
                x " I don't really wanna say it, but she was starting to get real annoying. "
                x " She's gotta learn to not believe what anyone says... "
                x " Especially if it's Oliver related. "
                x " Anyway! I gotta go see my bestie in the cafeteria. "
                x " See you later! "
                hide petunianeutral at right with easeoutright
                " ...Seems like you're just gonna have to stay here for a bit. "
                scene black with dissolve
                " You spent the rest of the break just chilling on a bench. "
                " While you were waiting for the break to be over, you were just playing blockblast. "
                " ...you suddenly get flashbacks to those utterly insane blockblast stories you kept seeing on your fyp. "
                " Eeeyikes. Let's not think about that right now."
                play sound "audio/bellring.mp3"
                " The bell eventually rings, pulling you out of your gaming session. "
                " You get up from the bench you were sitting on and you walk back to your classroom for the next class. "
                pause 2.0
                jump musicclass2
            " Nope, not my problem ":
                " You decided to not help the popular girl. "
                hide rileyhappy at left with easeoutleft
                hide petuniaconfused at left with easeoutleft
                " You, instead sat on a nearby bench and watched Riley cause trouble to the popular girl. "
                " Besides, it's not like it's your problem. "
                " Atleast you now get some free entertainment now. "
                scene black with dissolve
                " You spent the rest of the break watching Riley yap to the popular girl. "
                " The popular girl can't exactly move, because if she did, Riley would just follow her. "
                " ...And if she said anything, Riley wouldn't really listen to her. "
                " Now that you're thinking more about it, you kind of feel bad for the popular girl having to deal with this. "
                " But, oh well. You can't really do anything about it now. "
                " Unless if you press the back button. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, stopping Riley from her yapping session and freeing the popular girl. "
                " You get up from the bench you were sitting on and you walked to your classroom for the next class. "
                pause 2.0
                jump musicclass2
    else:
        x " Look girl, whoever told you that is lying -{nw}"
        x " No, I know it's true! " with vpunch
        x " Someone told me that Oliver's going to give me a big hug once he gets back to school tomorrow! "
        x " I just know it's real! "
        x " He's finally showing his feelings for me!! "
        x " Eeeh... "
        " The popular looking girl looks at you as if she's asking for help. "
        " Help her? "
        menu:
            " Help the popular girl ":
                $ popularlv += 10
                hide rileyhappy at bottom
                show rileyneutral at left
                if kind == True:
                    " You walked up to the insane looking girl and kindly told her to stop bothering the popular girl. "
                    " You said that it was kind of making the other uncomfortable. "
                elif calm == True:
                    " You walked up to the insane looking girl and told her to stop bothering the popular girl. "
                    " You calmly told her that it was making the girl uncomfortable. "
                elif mean == True:
                    " You just told the insane looking girl that the popular girl doesn't want to deal with her right now. "
                x " Oh, uh...! Sorry, then! "
                x " I'll go get going... "
                hide rileyneutral at right with easeoutright
                hide petuniaconfused at bottom
                show petunianeutral at left
                show petunianeutral at center with move
                x " Thanks, [name]. "
                x " I don't really wanna say it, but she was starting to get real annoying. "
                x " She's gotta learn to not believe what anyone says... "
                x " Especially if it's Oliver related. "
                x " Anyway! I gotta go see my bestie in the cafeteria. "
                x " See you later! "
                hide petunianeutral at right with easeoutright
                " ...Seems like you're just gonna have to stay here for a bit. "
                scene black with dissolve
                " You spent the rest of the break just chilling on a bench. "
                " While you were waiting for the break to be over, you were just playing blockblast. "
                " ...you suddenly get flashbacks to those utterly insane blockblast stories you kept seeing on your fyp. "
                " Eeeyikes. Let's not think about that right now."
                play sound "audio/bellring.mp3"
                " The bell eventually rings, pulling you out of your gaming session. "
                " You get up from the bench you were sitting on and you walk back to your classroom for the next class. "
                pause 2.0
                jump musicclass2
            " Nope, not my problem ":
                " You decided to not help the popular girl. "
                hide rileyhappy at left with easeoutleft
                hide petuniaconfused at left with easeoutleft
                " You, instead sat on a nearby bench and watched the insane girl cause trouble to the popular girl. "
                " Besides, it's not like it's your problem. "
                " Atleast you now get some free entertainment now. "
                scene black with dissolve
                " You spent the rest of the break watching the insane girl yap to the popular girl. "
                " The popular girl can't exactly move, because if she did, the insane girl would just follow her. "
                " ...And if she said anything, the other girl wouldn't really listen to her. "
                " Now that you're thinking more about it, you kind of feel bad for the popular girl having to deal with this. "
                " But, oh well. You can't really do anything about it now. "
                " Unless if you press the back button. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, stopping the insane girl from her yapping session and freeing the popular girl. "
                " You get up from the bench you were sitting on and you walked to your classroom for the next class. "
                pause 2.0
                jump musicclass2
label tuesdayback4:
    # Ruby and robby
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked over to the back of the school, and spotted your two classmates doing something. "
    " You wanted to make sure that they weren't doing anything suspicious, so you checked on what was going on. "
    show rubyneutral at left with easeinright
    show robbyneutral at right with easeinright
    if rubyknow == True and robbyknow == True:
        rb " ...Aaaand that should fix you, just until school's over. "
        rb " Are you sure you could hold up that long? "
        rb " I mean, I'm not too great at these things, so there might've been an error and you might overheat again. "
        ru " I'm sure I'll be fine! And don't say that about yourself, you're great! "
        ru " If it wasn't for you, I probably would've exploded. You know, that one time in class? "
        rb " Ooooh, right. That incident. "
        hide robbyneutral at bottom
        show robbyhappy at right
        rb " Yeah, don't want you to be exploding all around class. "
        rb " Just tell me when you need fixing again, alright? I don't want you to overheat yourself too much. "
        hide rubyneutral at bottom
        show rubyhappy at left
        ru " Will do! You're the best, Robby! "
        rb " Hah, you say that to almost everyone you know. "
        hide rubyhappy at bottom
        show rubyneutral at left
        ru " Well, yes... but that still doesn't change the fact that you're great! "
        rb " ...You're too nice sometimes, Ruby. "
        hide robbyhappy at bottom
        show robbyneutral at right
        rb " Oh. [name]'s here. "
        ru " [they] are? I didn't even notice! so sorry, [name]! "
        " You told her that it was fine, and you asked if she was feeling better now. "
        " With her being fixed and all that... "
        ru " I feel better than ever! "
        ru " And it's all thanks to this little guy right here! "
        rb " ...Little? "
        ru " Sorry, this big strong man! "
        rb " Wh- Ooookay Ruby, I might need to change your code a little. "
        ru " All cause of some compliments? Come on! "
        scene black with dissolve
        " You spent the rest of the break with Ruby and Robby. "
        " They were pretty chill, but most of the conversation was just Ruby complimenting either you or Robby. "
        " Saying how cool you guys were... "
        " ...Yeah, you think Robby was right. She's complimenting you guys a lot. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Looks like it's time for another class. "
        " You walked back into the school, and made your way to the classroom. "
        pause 2.0
        jump musicclass2
    elif rubyknow == True and robbyknow == False:
        rb " ...Aaaand that should fix you, just until school's over. "
        rb " Are you sure you could hold up that long? "
        rb " I mean, I'm not too great at these things, so there might've been an error and you might overheat again. "
        ru " I'm sure I'll be fine! And don't say that about yourself, you're great! "
        ru " If it wasn't for you, I probably would've exploded. You know, that one time in class? "
        rb " Ooooh, right. That incident. "
        hide robbyneutral at bottom
        show robbyhappy at right
        rb " Yeah, don't want you to be exploding all around class. "
        rb " Just tell me when you need fixing again, alright? I don't want you to overheat yourself too much. "
        hide rubyneutral at bottom
        show rubyhappy at left
        ru " Will do! You're the best, Robby! "
        rb " Hah, you say that to almost everyone you know. "
        hide rubyhappy at bottom
        show rubyneutral at left
        ru " Well, yes... but that still doesn't change the fact that you're great! "
        rb " ...You're too nice sometimes, Ruby. "
        hide robbyhappy at bottom
        show robbyneutral at right
        x " Oh. [name]'s here. "
        ru " [they] are? I didn't even notice! so sorry, [name]! "
        " You told her that it was fine, and you asked if she was feeling better now. "
        " With her being fixed and all that... "
        ru " I feel better than ever! "
        ru " And it's all thanks to this little guy right here! "
        ru " Wait, I don't think you've met him before! "
        $ robbyknow = True
        ru " This little guy over here is Robby! He's really cool! "
        rb " ...Little? "
        ru " Sorry, this big strong man! "
        rb " Wh- Ooookay Ruby, I might need to change your code a little. "
        ru " All cause of some compliments? Come on! "
        scene black with dissolve
        " You spent the rest of the break with Ruby and Robby. "
        " They were pretty chill, but most of the conversation was just Ruby complimenting either you or Robby. "
        " Saying how cool you guys were... "
        " ...Yeah, you think Robby was right. She's complimenting you guys a lot. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Looks like it's time for another class. "
        " You walked back into the school, and made your way to the classroom. "
        pause 2.0
        jump musicclass2
    elif rubyknow == False and robbyknow == True:
        rb " ...Aaaand that should fix you, just until school's over. "
        rb " Are you sure you could hold up that long? "
        rb " I mean, I'm not too great at these things, so there might've been an error and you might overheat again. "
        x " I'm sure I'll be fine! And don't say that about yourself, you're great! "
        x " If it wasn't for you, I probably would've exploded. You know, that one time in class? "
        rb " Ooooh, right. That incident. "
        hide robbyneutral at bottom
        show robbyhappy at right
        rb " Yeah, don't want you to be exploding all around class. "
        rb " Just tell me when you need fixing again, alright? I don't want you to overheat yourself too much. "
        hide rubyneutral at bottom
        show rubyhappy at left
        x " Will do! You're the best, Robby! "
        rb " Hah, you say that to almost everyone you know. "
        hide rubyhappy at bottom
        show rubyneutral at left
        x " Well, yes... but that still doesn't change the fact that you're great! "
        rb " ...You're too nice sometimes, Ruby. "
        hide robbyhappy at bottom
        show robbyneutral at right
        rb " Oh. [name]'s here. "
        x " [they] are? I didn't even notice! so sorry, [name]! "
        " You told her that it was fine, and you asked if she was feeling better now. "
        " With her being fixed and all that... "
        x " I feel better than ever! "
        x " And it's all thanks to this little guy right here! "
        hide rubyneutral at bottom
        show rubysurprised at left
        x " Waaait, I almost forgot to introduce myself! Silly me... "
        $ rubyknow = True
        hide rubysurprised at bottom
        show rubyneutral at left
        ru " I'm Ruby! It's nice to meet you! This little guy fixed me from overheating too much!"
        rb " ...Little? "
        ru " Sorry, this big strong man! "
        rb " Wh- Ooookay Ruby, I might need to change your code a little. "
        ru " All cause of some compliments? Come on! "
        scene black with dissolve
        " You spent the rest of the break with Ruby and Robby. "
        " They were pretty chill, but most of the conversation was just Ruby complimenting either you or Robby. "
        " Saying how cool you guys were... "
        " ...Yeah, you think Robby was right. She's complimenting you guys a lot. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Looks like it's time for another class. "
        " You walked back into the school, and made your way to the classroom. "
        pause 2.0
        jump musicclass2
    else:
        x " ...Aaaand that should fix you, just until school's over. "
        x " Are you sure you could hold up that long? "
        x " I mean, I'm not too great at these things, so there might've been an error and you might overheat again. "
        x " I'm sure I'll be fine! And don't say that about yourself, you're great! "
        x " If it wasn't for you, I probably would've exploded. You know, that one time in class? "
        x " Ooooh, right. That incident. "
        hide robbyneutral at bottom
        show robbyhappy at right
        x " Yeah, don't want you to be exploding all around class. "
        x " Just tell me when you need fixing again, alright? I don't want you to overheat yourself too much. "
        hide rubyneutral at bottom
        show rubyhappy at left
        x " Will do! You're the best, Robby! "
        x " Hah, you say that to almost everyone you know. "
        hide rubyhappy at bottom
        show rubyneutral at left
        x " Well, yes... but that still doesn't change the fact that you're great! "
        x " ...You're too nice sometimes, Ruby. "
        hide robbyhappy at bottom
        show robbyneutral at right
        x " Oh. [name]'s here. "
        x " [they] are? I didn't even notice! so sorry, [name]! "
        " You told her that it was fine, and you asked if she was feeling better now. "
        " With her being fixed and all that... "
        x " I feel better than ever! "
        x " And it's all thanks to this little guy right here! "
        x " ...Little? "
        x " Sorry, this big strong man! "
        x " Wh- Ooookay Ruby, I might need to change your code a little. "
        x " All cause of some compliments? Come on! "
        x " Wait, I don't think we've introduced ourselves to [name] yet. "
        x " Have we..? Oh, we're so sorry! "
        $ rubyknow = True
        $ robbyknow = True
        ru " I'm Ruby! It's nice to meet you! "
        rb " And I'm Robby. "
        ru " ...The coolest guy ever! "
        rb " Hey... "
        scene black with dissolve
        " You spent the rest of the break with Ruby and Robby. "
        " They were pretty chill, but most of the conversation was just Ruby complimenting either you or Robby. "
        " Saying how cool you guys were... "
        " ...Yeah, you think Robby was right. She's complimenting you guys a lot. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Looks like it's time for another class. "
        " You walked back into the school, and made your way to the classroom. "
        pause 2.0
        jump musicclass2
label tuesdaygym4:
    # lana and Engel
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym, and spotted two of your classmates doing their own things. "
    " You're thinking about talking to one of them, but who do you talk to? "
    if lanaknow == True and engelknow == True:
        menu:
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump lulz
            " {image=engelicon} Engel {image=engelicon} ":
                jump ihasaface
    elif lanaknow == True and engelknow == False:
        menu:
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump lulz
            " {image=engelicon} A boy with feathers on his head {image=engelicon} ":
                jump ihasaface
    elif lanaknow == False and engelknow == True:
        menu:
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump lulz
            " {image=engelicon} Engel {image=engelicon} ":
                jump ihasaface
    else:
        menu:
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump lulz
            " {image=engelicon} A boy with feathers on his head {image=engelicon} ":
                jump ihasaface
    label lulz:
        show lananeutral at center with easeinright
        if lanaknow == True:
            " You walked up to Lana and sat next to her. "
            " You greeted her before asking what she was doing. "
            l " Hiya, [name]! "
            l " I'm not really doing anything right now... "
            l " ...Just staring into space and thinking about things. "
            l " Like school stuff. "
            l " Boring, right? "
            l " ...Yeah, I don't know why my mind's thinking about school stuff. "
            l " I'm glad that you're here though, now I have someone to talk to! "
            l " Erm... what do we talk about, though? "
            " You thought about a conversation topic...what could you possibly talk about with Lana? "
            " ...Oh, now you have an idea. "
            if abblana == True:
                " You asked what Lana thought about Abbie. "
                l " Oh, Abbie? "
                hide lananeutral at bottom
                show lanahappy at center
                l " He's a really good friend! "
                hide lanahappy at bottom
                show lananeutral at center
                l " There are times where he doubts himself, like... "
                l " He keeps asking me if he's really good enough. "
                l " And I always have to reassure him that he's doing just fine! "
                l " I don't find it annoying or anything, I know he needs comfort! "
                l " And good friends are always there for their friends! "
                hide lananeutral at bottom
                show lanasad at center
                l " Though...there are sometimes where his thoughts get too dark. "
                l " No matter what I say or do, he just wouldn't feel better. "
                hide lanasad at bottom
                show lananeutral at center
                l " But he does feel better whenever we play his favorite game... "
                l " What's his favorite game, you ask? "
                l " Well it's none other than {color=#4169e1}{a=https://www.roblox.com/games/70630463876810/Gubby}Gubby{/a}{/color}!"
                l " It's basically a game where there's little cute bunnies! "
                l " The little buns comfort Abbie a whole lot...since they're so cute looking! "
                l " You should play with us sometime, [name]! "
                " Yeah, you should. Gubby is peak. "
                " Gubby. "
                scene black with dissolve
                " You spent the rest of the break talking to Lana. "
                " You can't stop thinking about that one game she mentioned now... "
                " Gubby is love. Gubby is life. "
                play sound "audio/bellring.mp3"
                " Gubby. "
                pause 2.0
                jump musicclass2
            else:
                if abbieknow == True:
                    " You asked what Lana thought about Abbie. "
                    l " Oh, Abbie? "
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " He's a really good friend! "
                    hide lanahappy at bottom
                    show lananeutral at center
                    l " There are times where he doubts himself, like... "
                    l " He keeps asking me if he's really good enough. "
                    l " And I always have to reassure him that he's doing just fine! "
                    l " I don't find it annoying or anything, I know he needs comfort! "
                    l " And good friends are always there for their friends! "
                    hide lananeutral at bottom
                    show lanasad at center
                    l " Though...there are sometimes where his thoughts get too dark. "
                    l " No matter what I say or do, he just wouldn't feel better. "
                    hide lanasad at bottom
                    show lananeutral at center
                    l " But he does feel better whenever we play his favorite game... "
                    l " What's his favorite game, you ask? "
                    l " Well it's none other than {color=#4169e1}{a=https://www.roblox.com/games/70630463876810/Gubby}Gubby{/a}{/color}!"
                    l " It's basically a game where there's little cute bunnies! "
                    l " The little buns comfort Abbie a whole lot...since they're so cute looking! "
                    l " You should play with us sometime, [name]! "
                    " Yeah, you should. Gubby is peak. "
                    " Gubby. "
                    scene black with dissolve
                    " You spent the rest of the break talking to Lana. "
                    " You can't stop thinking about that one game she mentioned now... "
                    " Gubby is love. Gubby is life. "
                    play sound "audio/bellring.mp3"
                    " Gubby. "
                    pause 2.0
                    jump musicclass2
                else:
                    " You asked what Lana thought about a black haired boy with a leaf on his head. "
                    l " Oh, Abbie? "
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " Yeah, I know him! He's a really good friend! "
                    hide lanahappy at bottom
                    show lananeutral at center
                    l " There are times where he doubts himself, like... "
                    l " He keeps asking me if he's really good enough. "
                    l " And I always have to reassure him that he's doing just fine! "
                    l " I don't find it annoying or anything, I know he needs comfort! "
                    l " And good friends are always there for their friends! "
                    hide lananeutral at bottom
                    show lanasad at center
                    l " Though...there are sometimes where his thoughts get too dark. "
                    l " No matter what I say or do, he just wouldn't feel better. "
                    hide lanasad at bottom
                    show lananeutral at center
                    l " But he does feel better whenever we play his favorite game... "
                    l " What's his favorite game, you ask? "
                    l " Well it's none other than {color=#4169e1}{a=https://www.roblox.com/games/70630463876810/Gubby}Gubby{/a}{/color}!"
                    l " It's basically a game where there's little cute bunnies! "
                    l " The little buns comfort Abbie a whole lot...since they're so cute looking! "
                    l " You should play with us sometime, [name]! "
                    " Yeah, you should. Gubby is peak. "
                    " Gubby. "
                    scene black with dissolve
                    " You spent the rest of the break talking to Lana. "
                    " You can't stop thinking about that one game she mentioned now... "
                    " Gubby is love. Gubby is life. "
                    play sound "audio/bellring.mp3"
                    " Gubby. "
                    pause 2.0
                    jump musicclass2
        else:
            " You walked up to the girl and sat next to her. "
            " You greeted her before asking what she was doing. "
            x " Hiya, [name]! "
            x " I'm not really doing anything right now... "
            x " ...Just staring into space and thinking about things. "
            x " Like school stuff. "
            x " Boring, right? "
            x " ...Yeah, I don't know why my mind's thinking about school stuff. "
            x " Wait, I forgot to introduce myself to you! "
            $ lanaknow = True
            l " I'm Lana! It's so nice to meet you! You know, I was feeling a bit lonely here... "
            l " I'm glad that you're here though, now I have someone to talk to! "
            l " Erm... what do we talk about, though? "
            " You thought about a conversation topic...what could you possibly talk about with Lana? "
            " ...Oh, now you have an idea. "
            if abblana == True:
                " You asked what Lana thought about Abbie. "
                l " Oh, Abbie? "
                hide lananeutral at bottom
                show lanahappy at center
                l " He's a really good friend! "
                hide lanahappy at bottom
                show lananeutral at center
                l " There are times where he doubts himself, like... "
                l " He keeps asking me if he's really good enough. "
                l " And I always have to reassure him that he's doing just fine! "
                l " I don't find it annoying or anything, I know he needs comfort! "
                l " And good friends are always there for their friends! "
                hide lananeutral at bottom
                show lanasad at center
                l " Though...there are sometimes where his thoughts get too dark. "
                l " No matter what I say or do, he just wouldn't feel better. "
                hide lanasad at bottom
                show lananeutral at center
                l " But he does feel better whenever we play his favorite game... "
                l " What's his favorite game, you ask? "
                l " Well it's none other than {color=#4169e1}{a=https://www.roblox.com/games/70630463876810/Gubby}Gubby{/a}{/color}!"
                l " It's basically a game where there's little cute bunnies! "
                l " The little buns comfort Abbie a whole lot...since they're so cute looking! "
                l " You should play with us sometime, [name]! "
                " Yeah, you should. Gubby is peak. "
                " Gubby. "
                scene black with dissolve
                " You spent the rest of the break talking to Lana. "
                " You can't stop thinking about that one game she mentioned now... "
                " Gubby is love. Gubby is life. "
                play sound "audio/bellring.mp3"
                " Gubby. "
                pause 2.0
                jump musicclass2
            else:
                if abbieknow == True:
                    " You asked what Lana thought about Abbie. "
                    l " Oh, Abbie? "
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " He's a really good friend! "
                    hide lanahappy at bottom
                    show lananeutral at center
                    l " There are times where he doubts himself, like... "
                    l " He keeps asking me if he's really good enough. "
                    l " And I always have to reassure him that he's doing just fine! "
                    l " I don't find it annoying or anything, I know he needs comfort! "
                    l " And good friends are always there for their friends! "
                    hide lananeutral at bottom
                    show lanasad at center
                    l " Though...there are sometimes where his thoughts get too dark. "
                    l " No matter what I say or do, he just wouldn't feel better. "
                    hide lanasad at bottom
                    show lananeutral at center
                    l " But he does feel better whenever we play his favorite game... "
                    l " What's his favorite game, you ask? "
                    l " Well it's none other than {color=#4169e1}{a=https://www.roblox.com/games/70630463876810/Gubby}Gubby{/a}{/color}!"
                    l " It's basically a game where there's little cute bunnies! "
                    l " The little buns comfort Abbie a whole lot...since they're so cute looking! "
                    l " You should play with us sometime, [name]! "
                    " Yeah, you should. Gubby is peak. "
                    " Gubby. "
                    scene black with dissolve
                    " You spent the rest of the break talking to Lana. "
                    " You can't stop thinking about that one game she mentioned now... "
                    " Gubby is love. Gubby is life. "
                    play sound "audio/bellring.mp3"
                    " Gubby. "
                    pause 2.0
                    jump musicclass2
                else:
                    " You asked what Lana thought about a black haired boy with a leaf on his head. "
                    l " Oh, Abbie? "
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " Yeah, I know him! He's a really good friend! "
                    hide lanahappy at bottom
                    show lananeutral at center
                    l " There are times where he doubts himself, like... "
                    l " He keeps asking me if he's really good enough. "
                    l " And I always have to reassure him that he's doing just fine! "
                    l " I don't find it annoying or anything, I know he needs comfort! "
                    l " And good friends are always there for their friends! "
                    hide lananeutral at bottom
                    show lanasad at center
                    l " Though...there are sometimes where his thoughts get too dark. "
                    l " No matter what I say or do, he just wouldn't feel better. "
                    hide lanasad at bottom
                    show lananeutral at center
                    l " But he does feel better whenever we play his favorite game... "
                    l " What's his favorite game, you ask? "
                    l " Well it's none other than {color=#4169e1}{a=https://www.roblox.com/games/70630463876810/Gubby}Gubby{/a}{/color}!"
                    l " It's basically a game where there's little cute bunnies! "
                    l " The little buns comfort Abbie a whole lot...since they're so cute looking! "
                    l " You should play with us sometime, [name]! "
                    " Yeah, you should. Gubby is peak. "
                    " Gubby. "
                    scene black with dissolve
                    " You spent the rest of the break talking to Lana. "
                    " You can't stop thinking about that one game she mentioned now... "
                    " Gubby is love. Gubby is life. "
                    play sound "audio/bellring.mp3"
                    " Gubby. "
                    pause 2.0
                    jump musicclass2
    label ihasaface:
        show engelneutral at center with easeinleft
        if engelknow == True:
            " You walked over to him and sat next to him. "
            " You greeted him before you asked him what he was doing. "
            hide engelneutral at bottom
            show engelhappy at center
            e " Hello there, [name]... "
            e " I'm thinking of giving a gift to my friend, Claire, but I don't know what to give her. "
            " You asked him why he would want to give her a gift. "
            e " Well, of course, it's not her birthday or anything... "
            e " I just wanted to giveher something nice. "
            e " I've given her many gifts in the past, some just for jokes... "
            e " ...And the others being actual gifts because I looked at the item and thought; "
            e " 'Claire would definitely like this'. "
            e " Sometimes, Claire tells me that I give her too many gifts. "
            e " But, you could never have too many gifts, right? "
            " ...You ask Engel how much money he has. Since he buys so much for Claire. "
            e " You don't wanna know that. "
            e " Just kidding! I still have a lot of money, you know? "
            e " It's not like I buy anything expensive for her, I make sure the price is just about right for me to buy! "
            e " Now, back to my question...what should I get her? "
            " You're thinking about something simple... "
            " ...It shouldn't be anything like money. That's too basic. "
            " Something that's basic, but shouldn't be too basic. You know? "
            " ...You then came up with a gift idea. Roses. You don't know if Claire would like roses, but it's something. "
            e " mmm...roses, you say? "
            e " Pretty simple, but that's what makes it good. "
            e " I'll go get those for her then. Thank you, [name]. "
            scene black with dissolve
            " You spent the entire break talking to Engel about the gifts that he bought for Claire. "
            " This guy...really likes getting gifts for his friends, the more you think about it. "
            " What a nice dude, but he probably shouldn't always spend money on his friends. How about spend money on yourself? "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit of talking. "
            " Time to go to another class... You get up from where you were sitting, and you walked back to your classroom. "
            pause 2.0
            jump musicclass2
        else:
            " You walked over to him and sat next to him. "
            " You greeted him before you asked him what he was doing. "
            hide engelneutral at bottom
            show engelhappy at center
            x " Hello there, [name]... "
            x " I don't think I've introduced myself to you yet, actually. Sorry about that. "
            $ engelknow = True
            e " I'm Engel, it's nice to meet you. Anyway... "
            e " I'm thinking of giving a gift to my friend, Claire, but I don't know what to give her. "
            " You asked him why he would want to give her a gift. "
            e " Well, of course, it's not her birthday or anything... "
            e " I just wanted to giveher something nice. "
            e " I've given her many gifts in the past, some just for jokes... "
            e " ...And the others being actual gifts because I looked at the item and thought; "
            e " 'Claire would definitely like this'. "
            e " Sometimes, Claire tells me that I give her too many gifts. "
            e " But, you could never have too many gifts, right? "
            " ...You ask Engel how much money he has. Since he buys so much for Claire. "
            e " You don't wanna know that. "
            e " Just kidding! I still have a lot of money, you know? "
            e " It's not like I buy anything expensive for her, I make sure the price is just about right for me to buy! "
            e " Now, back to my question...what should I get her? "
            " You're thinking about something simple... "
            " ...It shouldn't be anything like money. That's too basic. "
            " Something that's basic, but shouldn't be too basic. You know? "
            " ...You then came up with a gift idea. Roses. You don't know if Claire would like roses, but it's something. "
            e " mmm...roses, you say? "
            e " Pretty simple, but that's what makes it good. "
            e " I'll go get those for her then. Thank you, [name]. "
            scene black with dissolve
            " You spent the entire break talking to Engel about the gifts that he bought for Claire. "
            " This guy...really likes getting gifts for his friends, the more you think about it. "
            " What a nice dude, but he probably shouldn't always spend money on his friends. How about spend money on yourself? "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit of talking. "
            " Time to go to another class... You get up from where you were sitting, and you walked back to your classroom. "
            pause 2.0
            jump musicclass2
label tuesdaycafe4:
    # claire, lizzy, and kevin
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walk into the cafeteria and spotted three of your classmates vibing. "
    " You're thinking of walking up to one of them...But who should you talk to? "
    if claireknow,popularknow,kevinknow == True:
        menu:
            " {image=claireicon} Claire {image=claireicon} ":
                jump luckyisshe
            " {image=popularicon} Lizzy {image=popularicon} ":
                jump wholivesunaware
            " {image=kevinicon} Kevin {image=kevinicon}":
                jump doesntgiveacare
    elif claireknow,popularknow == True and kevinknow == False:
        menu:
            " {image=claireicon} Claire {image=claireicon} ":
                jump luckyisshe
            " {image=popularicon} Lizzy {image=popularicon} ":
                jump wholivesunaware
            " {image=kevinicon} A guy that looks like a nerd {image=kevinicon}":
                jump doesntgiveacare
    elif claireknow,kevinknow == True and popularknow == False:
        menu:
            " {image=claireicon} Claire {image=claireicon} ":
                jump luckyisshe
            " {image=popularicon} A popular looking girl {image=popularicon} ":
                jump wholivesunaware
            " {image=kevinicon} Kevin {image=kevinicon}":
                jump doesntgiveacare
    elif popularknow,kevinknow == True and claireknow == False:
        menu:
            " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                jump luckyisshe
            " {image=popularicon} Lizzy {image=popularicon} ":
                jump wholivesunaware
            " {image=kevinicon} Kevin {image=kevinicon}":
                jump doesntgiveacare
    elif claireknow == True and popularknow,kevinknow == False:
        menu:
            " {image=claireicon} Claire {image=claireicon} ":
                jump luckyisshe
            " {image=popularicon} A popular looking girl {image=popularicon} ":
                jump wholivesunaware
            " {image=kevinicon} A guy that looks like a nerd {image=kevinicon}":
                jump doesntgiveacare
    elif popularknow == True and claireknow,kevinknow == False:
        menu:
            " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                jump luckyisshe
            " {image=popularicon} Lizzy {image=popularicon} ":
                jump wholivesunaware
            " {image=kevinicon} A guy that looks like a nerd {image=kevinicon}":
                jump doesntgiveacare
    elif kevinknow == True and claireknow,popularknow == False:
        menu:
            " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                jump luckyisshe
            " {image=popularicon} A popular looking girl {image=popularicon} ":
                jump wholivesunaware
            " {image=kevinicon} Kevin {image=kevinicon}":
                jump doesntgiveacare
    else:
        menu:
            " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                jump luckyisshe
            " {image=popularicon} A popular looking girl {image=popularicon} ":
                jump wholivesunaware
            " {image=kevinicon} A guy that looks like a nerd {image=kevinicon}":
                jump doesntgiveacare
    label luckyisshe:
        if clairebeatup == True and clairesorry == False:
            " Not yet. "
            scene black
            pause 2.0
            jump musicclass2
        else:
            " You walked up to her and sat next to her. "
        show claireneutral at center with easeinright
        if claireknow == True:
            " You greeted her and asked what she was doing. "
            hide claireneutral at bottom
            show clairehappy at center
            c " Oh hello, [name]! "
            hide clairehappy at bottom
            show claireneutral at center
            c " Just looking at my old notes on my phone... "
            c " Nothing interesting, really. "
            c " Besides some cringy stories that I wrote, hehe. "
            c " ...You know, [name]... "
            c " There's been a student that's been having low grades recently. "
            c " Lower grades than Abbie, if you know who that is.. "
            c " They don't really pay attention to class, and Miss Circle... "
            hide claireneutral at bottom
            show clairesad at center
            c " ...She doesn't look too happy with them. "
            c " I'm worried for them, you know? She's been eyeing them for awhile now... "
            c " Let's just pray that they will pay attention to class just this once... "
            hide clairesad at bottom
            show claireneutral at center
            c " Anyway, um...away from the negative-ish topic... "
            c " Let's take a look at my old notes, yeah? "
            c " Warning though, they're quite...cringe worthy. "
            c " Even cringier than those fangirls I kept seeing back then on Youtube... "
            c " We might die of cringe because of these, haha. "
            scene black with dissolve
            " You spent the entire break looking at Claire's cringy notes. "
            " ...Some of them looked like an old gacha life story, actually. "
            " She even had: 'The bullied kid turns out to be the lost hybrid princess'... "
            " Absolute cinema. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that it's time for another class. "
            " You get up from where you were sitting, and you walked back to your classroom for the next class. "
            pause 2.0
            jump musicclass2
        else:
            " You greeted her and asked what she was doing. "
            hide claireneutral at bottom
            show clairehappy at center
            x " Oh hello, [name]! "
            hide clairehappy at bottom
            show claireneutral at center
            x " Actually, I don't think I've introduced myself to you yet... "
            x " Sorry, ehe! "
            $ claireknow = True
            c " I'm Claire! It's nice to meet you... We're classmates! "
            c " As for what I'm doing? well.. "
            c " Just looking at my old notes on my phone... "
            c " Nothing interesting, really. "
            c " Besides some cringy stories that I wrote, hehe. "
            c " ...You know, [name]... "
            c " There's been a student that's been having low grades recently. "
            c " Lower grades than Abbie, if you know who that is.. "
            c " They don't really pay attention to class, and Miss Circle... "
            hide claireneutral at bottom
            show clairesad at center
            c " ...She doesn't look too happy with them. "
            c " I'm worried for them, you know? She's been eyeing them for awhile now... "
            c " Let's just pray that they will pay attention to class just this once... "
            hide clairesad at bottom
            show claireneutral at center
            c " Anyway, um...away from the negative-ish topic... "
            c " Let's take a look at my old notes, yeah? "
            c " Warning though, they're quite...cringe worthy. "
            c " Even cringier than those fangirls I kept seeing back then on Youtube... "
            c " We might die of cringe because of these, haha. "
            scene black with dissolve
            " You spent the entire break looking at Claire's cringy notes. "
            " ...Some of them looked like an old gacha life story, actually. "
            " She even had: 'The bullied kid turns out to be the lost hybrid princess'... "
            " Absolute cinema. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that it's time for another class. "
            " You get up from where you were sitting, and you walked back to your classroom for the next class. "
            pause 2.0
            jump musicclass2
    label wholivesunaware:
        # looking for Petunia
        show lizzyneutral at center with easeinleft
        if popularknow == True:
            " You walked up to Lizzy and noticed that Petunia wasn't there. "
            " You asked her where Petunia was, since you usually saw her with her. "
            hide lizzyneutral at bottom
            show lizzyconfused at center
            lz " ...I have no idea either. "
            lz " I told her to meet up over here, but she's... "
            hide lizzyconfused at bottom
            show lizzyneutral at center
            " Lizzy's phone that was on the table buzzes. "
            " Looks like it was a message from Petunia. "
            lz " Oh, Petunia messaged me. One moment. "
            lz " ...'sry, i had to deal w an annoying bitch, omw'? "
            lz " Ah, she must be talking about Riley. "
            if rileyknow == True:
                " Understandable, since... "
                " ...You knew how she was. "
            else:
                " You asked her what's wrong with Riley. "
                hide lizzyneutral at bottom
                show lizzyconfused at center
                lz " I'm very surprised that you don't know about her. "
                lz " You're telling me that you haven't heard of the girl that's been saying: "
                lz " 'OLIVER'S MINE!!!' everywhere...? "
                lz " That's...shocking. But she does that a LOT. "
                hide lizzyconfused at bottom
                show lizzyneutral at center
                lz " You see, we have this boy in our class called Oliver. "
                lz " He's about... a few years older than us. He doesn't even go to this school. "
                lz " How did he manage to get in? No clue. "
                lz " But, Riley really likes him. And by that, I mean that she likes him A LOT. "
                lz " Talks about him practically every day, nonstop. "
                lz " Though, I have been noticing that she's been talking about him less, which is a shocker. "
                lz " Maybe she's finally learning that Oliver doesn't like her back? "
            show lizzyneutral at left with move
            show petunianeutral at right with easeinright
            p " Hey, girlies! Sorry I was late. Liz, you got my message right? "
            lz " Yeah, 'course I did. "
            p " Sweet! Anywho, lemme rant about that girl for a bit... "
            scene black with dissolve
            " You spent the entire break listening to Petunia talk about Riley. "
            " Geez, Riley was that bad, eh? "
            " ...You know, you should probably go ahead and tell them that it's probably best to just...ignore her. "
            " Instead of speaking badly about her. Like mean people. "
            " But what can you do? You literally cant speak unless I say so. "
            play sound "audio/bellring.mp3"
            " The bell rings, meaning that the break is over and it's time for another class..but you already knew that. "
            " You get up from where you were sitting and you walked over to your classroom. "
            pause 2.0
            jump musicclass2
        else:
            " You walked up to the popular girl and noticed something off... "
            " You always saw this girl with another one, and asked her where she was. "
            hide lizzyneutral at bottom
            show lizzyconfused at center
            x " ...I have no idea either. "
            x " I told her to meet up over here, but she's... "
            hide lizzyconfused at bottom
            show lizzyneutral at center
            " Her phone that was on the table buzzes. "
            " Looks like it was a message from the other girl. "
            x " Oh, Petunia messaged me. One moment. "
            x " ...'sry, i had to deal w an annoying bitch, omw'? "
            x " Ah, she must be talking about Riley. "
            if rileyknow == True:
                " Understandable, since... "
                " ...You knew how she was. "
            else:
                " You asked her what's wrong with Riley. "
                hide lizzyneutral at bottom
                show lizzyconfused at center
                x " I'm very surprised that you don't know about her. "
                x " You're telling me that you haven't heard of the girl that's been saying: "
                x " 'OLIVER'S MINE!!!' everywhere...? "
                x " That's...shocking. But she does that a LOT. "
                hide lizzyconfused at bottom
                show lizzyneutral at center
                x " You see, we have this boy in our class called Oliver. "
                x " He's about... a few years older than us. He doesn't even go to this school. "
                x " How did he manage to get in? No clue. "
                x " But, Riley really likes him. And by that, I mean that she likes him A LOT. "
                x " Talks about him practically every day, nonstop. "
                x " Though, I have been noticing that she's been talking about him less, which is a shocker. "
                x " Maybe she's finally learning that Oliver doesn't like her back? "
            show lizzyneutral at left with move
            show petunianeutral at right with easeinright
            x " Hey, girlies! Sorry I was late. Liz, you got my message right? "
            x " Yeah, 'course I did. "
            x " Sweet! Anywho, lemme rant about that girl for a bit... "
            scene black with dissolve
            " You spent the entire break listening to the popular girl ranting about Riley. "
            " Geez, Riley was that bad, eh? "
            " ...You know, you should probably go ahead and tell them that it's probably best to just...ignore her. "
            " Instead of speaking badly about her. Like mean people. "
            " But what can you do? You literally cant speak unless I say so. "
            play sound "audio/bellring.mp3"
            " The bell rings, meaning that the break is over and it's time for another class..but you already knew that. "
            " You get up from where you were sitting and you walked over to your classroom. "
            pause 2.0
            jump musicclass2
    label doesntgiveacare:
        show kevinneutral at center with easeinright
        if kevinknow == True:
            " You walked up to him and asked him what he was doing. "
            kv " Greetings, [name]. "
            kv " I'm playing quite the classic game of, you know... "
            kv " Snake.io. You know, that one game where a snake eats apples? "
            kv " Classic, isn't it? Some may find it boring, but I'm one of the very few enjoyers of this game. "
            kv " You might not know this, but this is what our parents and grandparents used to play in the days. "
            " ...You...most definitely knew that. "
            " I was one of those kids who played those kids of games, actually. "
            " Who's talking? Just the narrator, no one important, really. "
            " How could someone not know this game? Aside from the kids who were born from the later years. "
            kv " Would you want to watch me play? "
            kv " I'll give you a turn after I'm done trying to give myself a new highscore. "
            " ...You don't really have anything to do, so you agreed. "
            " You have a feeling Kevin probably won't give you a turn, but you trust him. "
            hide kevinneutral at bottom
            show kevinhappy at center
            kv " Splendid! "
            scene black with dissolve
            " You spent the entire break watching Kevin play. "
            " You were right, Kevin kept failing and therefore didn't let you play on his phone. "
            " Though, he did let you play Snake.io in your mind while he was at it. "
            " You did way better than him, obviously. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You get up from where you were seated, and you walked back to your classroom. "
            pause 2.0
            jump musicclass2
        else:
            " You walked up to him and asked him what he was doing. "
            x " Greetings, [name]. "
            $ kevinknow = True
            kv " It seems I haven't introduced myself before...I am Kevin. "
            kv " And as for what I'm doing? "
            kv " I'm playing quite the classic game of, you know... "
            kv " Snake.io. You know, that one game where a snake eats apples? "
            kv " Classic, isn't it? Some may find it boring, but I'm one of the very few enjoyers of this game. "
            kv " You might not know this, but this is what our parents and grandparents used to play in the days. "
            " ...You...most definitely knew that. "
            " I was one of those kids who played those kids of games, actually. "
            " Who's talking? Just the narrator, no one important, really. "
            " How could someone not know this game? Aside from the kids who were born from the later years. "
            kv " Would you want to watch me play? "
            kv " I'll give you a turn after I'm done trying to give myself a new highscore. "
            " ...You don't really have anything to do, so you agreed. "
            " You have a feeling Kevin probably won't give you a turn, but you trust him. "
            hide kevinneutral at bottom
            show kevinhappy at center
            kv " Splendid! "
            scene black with dissolve
            " You spent the entire break watching Kevin play. "
            " You were right, Kevin kept failing and therefore didn't let you play on his phone. "
            " Though, he did let you play Snake.io in your mind while he was at it. "
            " You did way better than him, obviously. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You get up from where you were seated, and you walked back to your classroom. "
            pause 2.0
            jump musicclass2
label tuesdayrooftop4:
    # cubbie, abbie
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walk up to the rooftop and spotted two of your classmates chilling. "
    " You wanted to talk to one of them...but who do you talk to? "
    if abbieknow == True and cubbieknow == True:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump thebass
            " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                jump therock
    elif abbieknow == True and cubbieknow == False:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump thebass
            " {image=cubbieicon} A cute kitty! {image=cubbieicon} ":
                jump therock
    elif abbieknow == False and cubbieknow == True:
        menu:
            " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                jump thebass
            " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                jump therock
    else:
        menu:
            " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                jump thebass
            " {image=cubbieicon} A cute kitty! {image=cubbieicon} ":
                jump therock
    label thebass:
        show abbieneutral at center with easeinright
        if abbieknow == True:
            " You walked up to him and asked him what he was doing. "
            x " Oh, um...hey, [name]... "
            $ abbieknow = True
            a " I'm Abbie, by the way... "
            a " I'm just...taking a look at the sky... "
            a " ...This scene...kind of reminds me of a game I've seen before... "
            a " A game where you sleep and walk into different kinds of dreams... "
            a " Not Nikki Yume, no...I don't actually remember that the game's name was. "
            a " All I know was that this game had a main character called Nessie... "
            a " ...And that the scene I'm talking about was... "
            a " ... "
            a " It...took palce in a dream where there were a lot of sunflowers... "
            hide abbieneutral at bottom
            show abbiehappy at center
            a " And there was this girl that was painting something... "
            a " Just a field of sunflowers...near a bus stop... "
            a " I can remember how the music sounded very clearly, and it sounded so relaxing... "
            a " A guitar being played nicely in the background with a beautiful scenery.. "
            a " ...It sounds perfect, doesn't it...? "
            " ...It does. "
            scene black with dissolve
            " You spent the rest of the break talking to Abbie about the game he mentioned. "
            " You found it to be pretty interesting, and you wanted to help him find it. "
            " Maybe later once you got home. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You get up from where you were seated, and you walked back to your classroom. "
            pause 2.0
            jump musicclass2
        else:
            " You walked up to him and asked him what he was doing. "
            a " Oh, um...hey, [name]... "
            a " I'm just...taking a look at the sky... "
            a " ...This scene...kind of reminds me of a game I've seen before... "
            a " A game where you sleep and walk into different kinds of dreams... "
            a " Not Nikki Yume, no...I don't actually remember that the game's name was. "
            a " All I know was that this game had a main character called Nessie... "
            a " ...And that the scene I'm talking about was... "
            a " ... "
            a " It...took palce in a dream where there were a lot of sunflowers... "
            hide abbieneutral at bottom
            show abbiehappy at center
            a " And there was this girl that was painting something... "
            a " Just a field of sunflowers...near a bus stop... "
            a " I can remember how the music sounded very clearly, and it sounded so relaxing... "
            a " A guitar being played nicely in the background with a beautiful scenery.. "
            a " ...It sounds perfect, doesn't it...? "
            " ...It does. "
            scene black with dissolve
            " You spent the rest of the break talking to Abbie about the game he mentioned. "
            " You found it to be pretty interesting, and you wanted to help him find it. "
            " Maybe later once you got home. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You get up from where you were seated, and you walked back to your classroom. "
            pause 2.0
            jump musicclass2
    label therock:
        show cubbieneutral at center with easeinleft
        if cubbieknow == True:
            " You walked up to him and asked him what he was doing. "
            cb " ... "
            " ... You kind of forgot that he doesn't exactly speak. "
            " Hm...looks like he's just taking a look at the sky... "
            cb " ...? "
            " He looks as if he's asking if you could...what? "
            cb " ... "
            " He patted the ground next to him and pointed at his phone. "
            " Seems like he wants you to keep him company while he's playing on his phone. "
            " You don't have much to do, so you sat down next to him on the rooftops ground... "
            " And started watching him play games on his phone. "
            hide cubbieneutral at bottom
            show cubbiehappy at center
            " He seems pleased with your actions. "
            scene black with dissolve
            " You spent the rest of the break watching Cubbie play something on his phone. "
            " It was actually quite interesting, seeing how he made cute expressions every time he messed up... "
            " ...He's adorable, don't you think? "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You get up from where you were seated, and you walked back to your classroom. "
            pause 2.0
            jump musicclass2
        else:
            $ cubbieknow = True
            " Hmm...you've heard of this kid before. "
            " His name was Cubbie, wasn't it? What a cute name for a cute kitty... "
            " You walked up to him and asked him what he was doing. "
            cb " ... "
            " ... You kind of forgot that he doesn't exactly speak. "
            " Hm...looks like he's just taking a look at the sky... "
            cb " ...? "
            " He looks as if he's asking if you could...what? "
            cb " ... "
            " He patted the ground next to him and pointed at his phone. "
            " Seems like he wants you to keep him company while he's playing on his phone. "
            " You don't have much to do, so you sat down next to him on the rooftops ground... "
            " And started watching him play games on his phone. "
            hide cubbieneutral at bottom
            show cubbiehappy at center
            " He seems pleased with your actions. "
            scene black with dissolve
            " You spent the rest of the break watching Cubbie play something on his phone. "
            " It was actually quite interesting, seeing how he made cute expressions every time he messed up... "
            " ...He's adorable, don't you think? "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for another class. "
            " You get up from where you were seated, and you walked back to your classroom. "
            pause 2.0
            jump musicclass2
label tuesdaylibrary4:
    # bubble
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and spotted one of your classmates vibing. "
    " You didn't want them to feel lonely, so you walked up to them and decided to have a conversation with them. "
    show bubbleneutral at center with easeinright
    if bubbleknow == True:
        " Seems like she's reading a book...about what? "
        " You poke her shoulder to get her attention. "
        b " Oh! Hello, [name]! "
        " You greeted her back. You then asked her what kind of book she's reading. "
        b " What kind of book am I reading...? "
        b " Well, you should come down and sit next to me! I don't want you standing still for our entire conversation, ehhe... "
        " You sat down next to her and got a closer look at what she was reading. "
        " Sounds like she was reading a horror themed book. "
        b " It's about this book of a father who one day woke up with a little child at their doorstep! "
        b " Though...the more you read...the more depressing it gets. "
        b " You see, the father loses his child after a bit and turns out... "
        b " This child of his turned into a monster, killing people...thinking it was all a game of tag... "
        b " The father, upset about how he lost his child in this way, he... "
        b " ...Hah! I'm not spoiling you on that part. "
        b " If you're really interested, you should start reading the book yourself! "
        b " Oooor, you know...we could read together! "
        b " Though I'd have to read all the way from the start so that you could get a gist of what's going on. "
        b " Not that I mind, hehe! Here, let's start reading..."
        scene black with dissolve
        " You spent the rest of the break reading a book with Bubble. "
        " This seems...oddly familiar to Claire's interaction. "
        " Look, the programmer of this game has bad memory so shut it. "
        play sound "audio/bellring.mp3"
        " The bell rings, looks like it's time for another class. "
        " You get up from where you were seated, and you walked back to your classroom. "
        pause 2.0
        jump musicclass2
    else:
        " Seems like she's reading a book...about what? "
        " You poke her shoulder to get her attention. "
        x " Oh! Hello, [name]! "
        $ bubbleknow = True
        b " I'm Bubble, by the way. "
        " You greeted her back. You then asked her what kind of book she's reading. "
        b " What kind of book am I reading...? "
        b " Well, you should come down and sit next to me! I don't want you standing still for our entire conversation, ehhe... "
        " You sat down next to her and got a closer look at what she was reading. "
        " Sounds like she was reading a horror themed book. "
        b " It's about this book of a father who one day woke up with a little child at their doorstep! "
        b " Though...the more you read...the more depressing it gets. "
        b " You see, the father loses his child after a bit and turns out... "
        b " This child of his turned into a monster, killing people...thinking it was all a game of tag... "
        b " The father, upset about how he lost his child in this way, he... "
        b " ...Hah! I'm not spoiling you on that part. "
        b " If you're really interested, you should start reading the book yourself! "
        b " Oooor, you know...we could read together! "
        b " Though I'd have to read all the way from the start so that you could get a gist of what's going on. "
        b " Not that I mind, hehe! Here, let's start reading..."
        scene black with dissolve
        " You spent the rest of the break reading a book with Bubble. "
        " This seems...oddly familiar to Claire's interaction. "
        " Look, the programmer of this game has bad memory so shut it. "
        play sound "audio/bellring.mp3"
        " The bell rings, looks like it's time for another class. "
        " You get up from where you were seated, and you walked back to your classroom. "
        pause 2.0
        jump musicclass2
label musicclass2:
    scene classroom with dissolve
    " You walked into the classroom and waited for the music teacher to arrive. "
    " After a few minutes, the teacher arrives. "
    show mrdemineutral at center with easeinright
    msd " Hello, my students... "
    msd " Before we'd...um. Start our class... "
    msd " Just a reminder that we're going to have an activity tomorrow. "
    " ...Looks like we somewhat have a lot of activities. "
    " Wonder what this is gonna be... "
    msd " A-anywho...Let's get started with our lesson today... "
    scene black with dissolve
    " Music class was boring. Nothing much, really. "
    " You could hear some students yapping in the back. That's how boring it was. "
    " They got a bit scolded by Mister Demi though. And the star student. "
    " Lame. You wanted to hear what they were talking about... "
    play sound "audio/bellring.mp3"
    " The bell rings, looks like class is over. "
    " You head out to the hallways to find somewhere to chill for a bit. "
    pause 2.0
    jump tuesdaybreak5
label tuesdaybreak5:
    scene hallway with dissolve
    " It's the last break of the day, and you're thinking about going somewhere to hangout. "
    " Where do you go, though? "
    menu:
        " {image=lanaicon} The front of the school {image=skellicon} ":
            jump tuesdayfront5
        " {image=cubbieicon} The back of the school {image=engelicon} ":
            jump tuesdayback5
        " {image=claireicon} The gym {image=oligangicon} ":
            jump tuesdaygym5
        " The cafeteria ":
            jump tuesdaycafe5
        " {image=popularicon} The rooftop {image=popularicon} ":
            jump tuesdayrooftop5
        " {image=abbieicon} The library {image=abbieicon} ":
            jump tuesdaylibrary5
label tuesdayfront5:
    # lana, Skell
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked out to the front of the school, and spotted two of your classmates. "
    " They were just doing their own things...you should talk to one of them and bother them. "
    " Who do you talk to, though? "
    if lanaknow == True and skellknow == True:
        menu:
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump odysseus
            " {image=skellicon} Skell {image=skellicon} ":
                jump penelope
    elif lanaknow == True and skellknow == False:
        menu:
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump odysseus
            " {image=skellicon} An emo looking kid {image=skellicon} ":
                jump penelope
    elif lanaknow == False and skellknow == True:
        menu:
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump odysseus
            " {image=skellicon} Skell {image=skellicon} ":
                jump penelope
    else:
        menu:
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump odysseus
            " {image=skellicon} An emo looking kid {image=skellicon} ":
                jump penelope
    label odysseus:
        show lananeutral at center with easeinright
        if lanaknow == True:
            " You walked up to her and asked what she was doing. "
            l " Hey, [name]! "
            l " I was just doing a roleplay between my sock puppets! "
            l " You wanna watch? It's interesting, I swear! "
            menu:
                " Watch Lana's roleplay ":
                    $ lanalv += 10
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " Yayy! I've been waiting for an audience! "
                    hide lanahappy at bottom
                    show lananeutral at center
                    l " Alright, lemme start! "
                    pe " Juliana, my love... "
                    ju " Ah, my dear! You've finally come back! "
                    ju " Come here, dinner's gonna get cold. "
                    pe " Yes, but...I have something to tell you. "
                    ju " Hm? What is it, my love? You can tell me anything! "
                    pe " I... "
                    hide lananeutral at bottom
                    show lanasad at center
                    pe " I'm sorry, mi amor, but I've fallen in love with another. "
                    ju " WHAT?! " with vpunch
                    " How shocking! "
                    pe " Yes, it is unfortunate... I love you, Juliana, but...I don't think we can work this out anymore. "
                    ju " No, Pedro! I love you so! Please don't leave me! "
                    pe " Juliana... "
                    pe " ...I know it is tough for you, but... "
                    pe " Please, find another man to love you. As they say...there are many fish in the sea. "
                    ju " NOOO!!! PEDRO!!!! " with vpunch
                    " Pedro then leaves...leaving Juliana heartbroken... "
                    hide lanasad at bottom
                    show lananeutral at center
                    l " ...Well, that's all for now! "
                    l " I say for now, because I have another thing planned for these two characters!! "
                    l " So...how'd you think? "
                    menu:
                        " WAAAAHHH SO EMOTIONAL 1000/10 ":
                            $ lanalv += 5
                            hide lananeutral at bottom
                            show lanahappy at center
                            l " I'm glad that you liked it!! "
                            l " I should probably make another one of these, since you liked it so much! "
                            hide lanahappy at bottom
                            show lananeutral at center
                            l " Hmmm...maybe tomorrow. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Lana. "
                            " She told you she was gonna continue the story of Juliana and Pedro... "
                            " ...But of course, didn't spoil anything for you. "
                            " Damn it, I wanted spoilers. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for your final class. "
                            " You went back inside the school and went into your classroom. "
                            pause 2.0
                            jump artclass2
                        " It was fine ":
                            l " Nice! "
                            l " I should probably make another one of these... "
                            l " Hmmm...maybe tomorrow. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Lana. "
                            " She told you she was gonna continue the story of Juliana and Pedro... "
                            " ...But of course, didn't spoil anything for you. "
                            " Damn it, I wanted spoilers. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for your final class. "
                            " You went back inside the school and went into your classroom. "
                            pause 2.0
                            jump artclass2
                " On second thought, I have to go somewhere. ":
                    l " Ooo, okay! If yo need anything, I'll be here! "
                    hide lananeutral at left with easeoutleft
                    scene black with dissolve
                    " You left Lana alone and sort of just... "
                    " ...Walked around on the front of the school out of boredom. "
                    " You kind of just lied to Lana since you didn't have anywhere to go. "
                    " But, you weren't in the mood to deal with her sock pupet stories, so... "
                    " Kind of good choice??? I'm not sure. "
                    " You eventually find a place to sit on and you just... "
                    " Stared into space for a good long while. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, snapping you out of your thinking session. "
                    " You get up from where you were seated, and you went back inside the school and went into your classroom. "
                    pause 2.0
                    jump artclass2
        else:
            " You walked up to her and asked what she was doing. "
            x " Hey, [name]! "
            x " I was just doing a roleplay between my sock puppets! "
            $ lanaknow = True
            l " I'm Lana by the way, hehe. "
            l " Anyway, you wanna watch? It's interesting, I swear! "
            menu:
                " Watch Lana's roleplay ":
                    $ lanalv += 10
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " Yayy! I've been waiting for an audience! "
                    hide lanahappy at bottom
                    show lananeutral at center
                    l " Alright, lemme start! "
                    pe " Juliana, my love... "
                    ju " Ah, my dear! You've finally come back! "
                    ju " Come here, dinner's gonna get cold. "
                    pe " Yes, but...I have something to tell you. "
                    ju " Hm? What is it, my love? You can tell me anything! "
                    pe " I... "
                    hide lananeutral at bottom
                    show lanasad at center
                    pe " I'm sorry, mi amor, but I've fallen in love with another. "
                    ju " WHAT?! " with vpunch
                    " How shocking! "
                    pe " Yes, it is unfortunate... I love you, Juliana, but...I don't think we can work this out anymore. "
                    ju " No, Pedro! I love you so! Please don't leave me! "
                    pe " Juliana... "
                    pe " ...I know it is tough for you, but... "
                    pe " Please, find another man to love you. As they say...there are many fish in the sea. "
                    ju " NOOO!!! PEDRO!!!! " with vpunch
                    " Pedro then leaves...leaving Juliana heartbroken... "
                    hide lanasad at bottom
                    show lananeutral at center
                    l " ...Well, that's all for now! "
                    l " I say for now, because I have another thing planned for these two characters!! "
                    l " So...how'd you think? "
                    menu:
                        " WAAAAHHH SO EMOTIONAL 1000/10 ":
                            $ lanalv += 5
                            hide lananeutral at bottom
                            show lanahappy at center
                            l " I'm glad that you liked it!! "
                            l " I should probably make another one of these, since you liked it so much! "
                            hide lanahappy at bottom
                            show lananeutral at center
                            l " Hmmm...maybe tomorrow. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Lana. "
                            " She told you she was gonna continue the story of Juliana and Pedro... "
                            " ...But of course, didn't spoil anything for you. "
                            " Damn it, I wanted spoilers. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for your final class. "
                            " You went back inside the school and went into your classroom. "
                            pause 2.0
                            jump artclass2
                        " It was fine ":
                            l " Nice! "
                            l " I should probably make another one of these... "
                            l " Hmmm...maybe tomorrow. "
                            scene black with dissolve
                            " You spent the rest of the break talking with Lana. "
                            " She told you she was gonna continue the story of Juliana and Pedro... "
                            " ...But of course, didn't spoil anything for you. "
                            " Damn it, I wanted spoilers. "
                            play sound "audio/bellring.mp3"
                            " The bell rings after a bit, looks like it's time for your final class. "
                            " You went back inside the school and went into your classroom. "
                            pause 2.0
                            jump artclass2
                " On second thought, I have to go somewhere. ":
                    l " Ooo, okay! If yo need anything, I'll be here! "
                    hide lananeutral at left with easeoutleft
                    scene black with dissolve
                    " You left Lana alone and sort of just... "
                    " ...Walked around on the front of the school out of boredom. "
                    " You kind of just lied to Lana since you didn't have anywhere to go. "
                    " But, you weren't in the mood to deal with her sock pupet stories, so... "
                    " Kind of good choice??? I'm not sure. "
                    " You eventually find a place to sit on and you just... "
                    " Stared into space for a good long while. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, snapping you out of your thinking session. "
                    " You get up from where you were seated, and you went back inside the school and went into your classroom. "
                    pause 2.0
                    jump artclass2
    label penelope:
        show skellneutral at center with easeinleft
        if skellknow == True:
            " You walked up to him and asked what he was doing. "
            sk " Hey there, [name]. "
            sk " You know, I heard.. "
            sk " Someone's throwing a party on friday. "
            sk " That someone is like...this one kid at a very prestigious school. "
            sk " Too bad we can't join it, right? "
            sk " Eh. Not like I would do anything there anyway. "
            sk " I would just come for the food and drinks, honestly. "
            sk " And not interact with anyone at all. "
            sk " Unless if I had a few people I knew there, then I would talk to them. "
            sk " Buuut, we're not from that school. And therefore we can't go. "
            sk " If only I had the money to go to that school... "
            sk " ...My parents probably wouldn't take me there though. "
            sk " I mean, yes, I've heard the teachers were nicer than the ones here, "
            sk " But...I've kinda gotten used to how everything works here. "
            sk " So uh, safe to say I'm not gonna move to that school anytime soon. "
            sk " ...I don't even know what I'm talking about right now. "
            " Stuff. You're talking about stuff, Skell. "
            scene black with dissolve
            " You spent the rest of the break talking with Skell. "
            " You're starting to wonder what that prestigious school's name is... "
            " ...Not like you're planning to move there or anything. "
            " Besides, I wouldn't even let you. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for your final class. "
            " You walked back into the school and you went back to your classroom. "
            pause 2.0
            jump artclass2
        else:
            " You walked up to him and asked what he was doing. "
            x " Hey there, [name]. "
            $ skellknow = True
            sk " I'm, uh...Skell, by the way. "
            sk " ...You know, I heard.. "
            sk " Someone's throwing a party on friday. "
            sk " That someone is like...this one kid at a very prestigious school. "
            sk " Too bad we can't join it, right? "
            sk " Eh. Not like I would do anything there anyway. "
            sk " I would just come for the food and drinks, honestly. "
            sk " And not interact with anyone at all. "
            sk " Unless if I had a few people I knew there, then I would talk to them. "
            sk " Buuut, we're not from that school. And therefore we can't go. "
            sk " If only I had the money to go to that school... "
            sk " ...My parents probably wouldn't take me there though. "
            sk " I mean, yes, I've heard the teachers were nicer than the ones here, "
            sk " But...I've kinda gotten used to how everything works here. "
            sk " So uh, safe to say I'm not gonna move to that school anytime soon. "
            sk " ...I don't even know what I'm talking about right now. "
            " Stuff. You're talking about stuff, Skell. "
            scene black with dissolve
            " You spent the rest of the break talking with Skell. "
            " You're starting to wonder what that prestigious school's name is... "
            " ...Not like you're planning to move there or anything. "
            " Besides, I wouldn't even let you. "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for your final class. "
            " You walked back into the school and you went back to your classroom. "
            pause 2.0
            jump artclass2
label tuesdayback5:
    # cubbie and engel getting art inspiration
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school, and spotted two of your classmates vibing. "
    " Curious on what they're talking about, you decide to walk up to them. "
    show engelhappy at right with easeinleft
    show cubbieneutral at left with easeinleft
    if engelknow == True and cubbieknow == True:
        e " You know, Cubbie... "
        e " Since we're having art class next, this scene right here infront of us would be some good art inspiration... "
        e " ...Don't you think? "
        cb " ...! "
        " Cubbie nods, agreeing with Engel on what he said. "
        " Engel was about to say something else, but he stops once he notices you standing where you were. "
        " Looks like he wasn't expecting you... I mean, to them you're kinda just... "
        " Teleporting into their conversations for some odd reasons. "
        " Blame the programmer for that, not me. I'm just reading out a script. "
        " Back to the actual game... "
        e " Oh hey there, [name]. Apologies that we didn't notice you. "
        e " Come here for a moment... "
        " You came closer towards Engel, wondering why he wanted you to do what you did. "
        e " See this? "
        " He's literally just looking at the sky and the trees. "
        " Now that you think about it, it looks pretty nice. "
        e " It's very pretty, correct? "
        e " Would be perfect to take a picture of it so that I could paint it later. "
        cb " ...!! "
        e " See? Cubbie agrees that it looks pretty nice. "
        e " I know just what colors to mix for my upcoming painting of this... "
        scene black with dissolve
        " ..Yeah, I'm not gonna let you see Engel yap about painting. "
        " Let's just pretend that you, Engel, and Cubbie talked about painting. "
        " Sorry I'm lazy, programmer. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for the next class. "
        " You walked back into the school and you went back to your classroom. "
        pause 2.0
        jump artclass2
    elif engelknow == True and cubbieknow == False:
        e " You know, Cubbie... "
        " So thats the little cat's name, huh? "
        e " Since we're having art class next, this scene right here infront of us would be some good art inspiration... "
        e " ...Don't you think? "
        $ cubbieknow = True
        cb " ...! "
        " Cubbie nods, agreeing with Engel on what he said. "
        " Engel was about to say something else, but he stops once he notices you standing where you were. "
        " Looks like he wasn't expecting you... I mean, to them you're kinda just... "
        " Teleporting into their conversations for some odd reasons. "
        " Blame the programmer for that, not me. I'm just reading out a script. "
        " Back to the actual game... "
        e " Oh hey there, [name]. Apologies that we didn't notice you. "
        e " Come here for a moment... "
        " You came closer towards Engel, wondering why he wanted you to do what you did. "
        e " See this? "
        " He's literally just looking at the sky and the trees. "
        " Now that you think about it, it looks pretty nice. "
        e " It's very pretty, correct? "
        e " Would be perfect to take a picture of it so that I could paint it later. "
        cb " ...!! "
        e " See? Cubbie agrees that it looks pretty nice. "
        e " I know just what colors to mix for my upcoming painting of this... "
        scene black with dissolve
        " ..Yeah, I'm not gonna let you see Engel yap about painting. "
        " Let's just pretend that you, Engel, and Cubbie talked about painting. "
        " Sorry I'm lazy, programmer. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for the next class. "
        " You walked back into the school and you went back to your classroom. "
        pause 2.0
        jump artclass2
    elif engelknow == False and cubbieknow == True:
        x " You know, Cubbie... "
        x " Since we're having art class next, this scene right here infront of us would be some good art inspiration... "
        x " ...Don't you think? "
        cb " ...! "
        " Cubbie nods, agreeing with the other boy on what he said. "
        " The other boy was about to say something else, but he stops once he notices you standing where you were. "
        " Looks like he wasn't expecting you... I mean, to them you're kinda just... "
        " Teleporting into their conversations for some odd reasons. "
        " Blame the programmer for that, not me. I'm just reading out a script. "
        " Back to the actual game... "
        x " Oh hey there, [name]. Apologies that we didn't notice you. "
        $ engelknow = True
        e " I'm Engel, by the way. We're classmates. "
        e " ...Could you come here for a moment...? "
        " You came closer towards Engel, wondering why he wanted you to do what you did. "
        e " See this? "
        " He's literally just looking at the sky and the trees. "
        " Now that you think about it, it looks pretty nice. "
        e " It's very pretty, correct? "
        e " Would be perfect to take a picture of it so that I could paint it later. "
        cb " ...!! "
        e " See? Cubbie agrees that it looks pretty nice. "
        e " I know just what colors to mix for my upcoming painting of this... "
        scene black with dissolve
        " ..Yeah, I'm not gonna let you see Engel yap about painting. "
        " Let's just pretend that you, Engel, and Cubbie talked about painting. "
        " Sorry I'm lazy, programmer. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for the next class. "
        " You walked back into the school and you went back to your classroom. "
        pause 2.0
        jump artclass2
    else:
        x " You know, Cubbie... "
        $ cubbieknow = True
        " So that's the name of the little cat guy... "
        x " Since we're having art class next, this scene right here infront of us would be some good art inspiration... "
        x " ...Don't you think? "
        cb " ...! "
        " Cubbie nods, agreeing with the other boy on what he said. "
        " The other boy was about to say something else, but he stops once he notices you standing where you were. "
        " Looks like he wasn't expecting you... I mean, to them you're kinda just... "
        " Teleporting into their conversations for some odd reasons. "
        " Blame the programmer for that, not me. I'm just reading out a script. "
        " Back to the actual game... "
        x " Oh hey there, [name]. Apologies that we didn't notice you. "
        $ engelknow = True
        e " I'm Engel, by the way. We're classmates. "
        e " ...Could you come here for a moment...? "
        " You came closer towards Engel, wondering why he wanted you to do what you did. "
        e " See this? "
        " He's literally just looking at the sky and the trees. "
        " Now that you think about it, it looks pretty nice. "
        e " It's very pretty, correct? "
        e " Would be perfect to take a picture of it so that I could paint it later. "
        cb " ...!! "
        e " See? Cubbie agrees that it looks pretty nice. "
        e " I know just what colors to mix for my upcoming painting of this... "
        scene black with dissolve
        " ..Yeah, I'm not gonna let you see Engel yap about painting. "
        " Let's just pretend that you, Engel, and Cubbie talked about painting. "
        " Sorry I'm lazy, programmer. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for the next class. "
        " You walked back into the school and you went back to your classroom. "
        pause 2.0
        jump artclass2
label tuesdaygym5:
    # claire and zip - zip bullying claire
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym, and you could hear someone yelling at someone. "
    " Being curious on what's going on, you decided to walk over to the noise. "
    show claireangry at left with easeinright
    show zipangry at right with easeinright
    if claireknow == True and oligangknow == True:
        c " Jesus christ Zip, I told you that I didn't do it! "
        c " No, I didn't take away your little brother's drawings, why would I?! "
        z " Number one, you're the type of person to do that. "
        z " Number two, I know you have them, just admit it, god damn it! "
        c " No I don't? And I'm not the type of person to take away a child's drawings! "
        c " How about you go ask someone else, I really can't deal with this right now... "
        " Seems like she's in a bit of trouble. "
        " ...Do you want to help her? "
        menu:
            " Why not ":
                $ clairelv += 10
                " You walked up to the two and thought about what you should do to calm them down. "
                if clairebeatup == True:
                    $ clairedefend = True
                    " ...Hold on, you're actually helping Claire? "
                    " ...Maybe you might be ready. "
                    z " Stop bullshitting me! I know you have my little brother's drawings! "
                    z " Stop lying and just -  "
                    stop music
                    hide zipangry at bottom
                    show zipconfused at right
                    hide claireangry at bottom
                    show clairescared at left
                    " You slapped Zip. " with vpunch
                    c " ...What- "
                    z " ... "
                    hide zipconfused at bottom
                    show zipsad at right
                    z " ... "
                    hide zipsad at left with easeoutleft
                    z " WAAAAHH!! "
                    " ...She ran away. "
                    " For someone who looked so tough...she started crying like a child. "
                    " It's insane, now that you think about it. But not really. "
                    hide clairescared at bottom
                    show claireneutral at left
                    show claireneutral at center with move
                    play music "audio/paperhigh.mp3" fadein 0.5
                    c " ... "
                    c " ...Um...Thank you. "
                    hide claireneutral at left with easeoutleft
                    " You gave her a thumbs up as a you're welcome and you went to sit on the bleachers and do your own thing. "
                    " Which is just scrolling on your phone. "
                    scene black with dissolve
                    " You spent the rest of the break scrolling on your phone... "
                    " ...And thinking about what happened and what you did. "
                    " It's surprising to me thatyou actually decided to help. "
                    " I think you might be ready...but not right now. Maybe on thursday. "
                    pause 2.0
                    play sound "audio/bellring.mp3"
                    " The bell rings after a few minutes, snapping you out of your thinking session. "
                    " You get up from where you were sitting and you walked back to your classroom for your final class. "
                    pause 2.0
                    jump artclass2
                else:
                    pass
                " You should probably just lie to Zip so that she won't be bothering Claire anymore. "
                " Yeah, that's the best you got. Besides, if you tried convincing her that Claire didn't have the drawings, she probably wouldn't believe you. "
                " You tap Zip's shoulder and told her that you found someone in the hallways who had her brother's drawings. "
                z " Oh, what? Really...? "
                hide claireangry at bottom
                show claireneutral at left
                hide zipangry at bottom
                show zipneutral at right
                z " Fine then. I'll go check it out... "
                z " Which direction did they go in? "
                " You pointed to a random direction. "
                z " ...Okay. "
                hide zipneutral at left with easeoutleft
                show claireneutral at center with move
                " ..She skedaddled away. "
                c " ...Thanks for that, [name]. "
                c " For a fact, I didn't steal her brother's drawings. "
                c " I don't know why she would think that way... "
                c " It's kind of idiotic, if you ask me. To just assume someone did something bad... "
                c " You agree with me, right? "
                " You nodded. "
                scene black with dissolve
                " You spent the rest of the break having a talk with Claire. "
                " Just talking about random things...and talking about what happened with her and Zip. "
                " Making jokes about her here and there... "
                " She's a pretty nice person to talk with. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, disrupting your conversation. "
                " You walked back to your classroom for your final class of the day. "
                pause 2.0
                jump artclass2
            " Nah, I'd rather just watch what's going on ":
                " Yeah, this isn't your problem. "
                " You took a seat on one of the bleachers and just watched. "
                " You pulled out your earphones and pretended you were listening to music... "
                " When in reality, you're just listening into their conversation. "
                " They won't even suspect a thing. "
                " Trust me. "
                scene black with dissolve
                if claireknow == True and oligangknow == True:
                    " You spent the rest of the break watching Claire and Zip argue. "
                elif claireknow == True and oligangknow == False:
                    " You spent the rest of the break watching Claire and the other girl argue. "
                elif claireknow == False and oligangknow == True:
                    " You spent the rest of the break watching the other girl and Zip argue. "
                else:
                    " You spent the rest of the break watching the two girls argue. "
                " It was pretty interesting, actually. "
                " They argued for a long time, you're surprised that they could argue for that long without getting tired. "
                play sound "audio/bellring.mp3"
                " For a fact, they argued until the bell rang. "
                " You got up from where you were sitting and you walked back toyour classroom for the final class. "
                pause 2.0
                jump artclass2
    elif claireknow == True and oligangknow == False:
        c " Jesus christ Zip, I told you that I didn't do it! "
        c " No, I didn't take away your little brother's drawings, why would I?! "
        x " Number one, you're the type of person to do that. "
        x " Number two, I know you have them, just admit it, god damn it! "
        c " No I don't? And I'm not the type of person to take away a child's drawings! "
        c " How about you go ask someone else, I really can't deal with this right now... "
        " Seems like she's in a bit of trouble. "
        " ...Do you want to help her? "
        menu:
            " Why not ":
                $ clairelv += 10
                " You walked up to the two and thought about what you should do to calm them down. "
                if clairebeatup == True:
                    $ clairedefend = True
                    " ...Hold on, you're actually helping Claire? "
                    " ...Maybe you might be ready. "
                    x " Stop bullshitting me! I know you have my little brother's drawings! "
                    x " Stop lying and just -  "
                    stop music
                    hide zipangry at bottom
                    show zipconfused at right
                    hide claireangry at bottom
                    show clairescared at left
                    " You slapped the other girl. " with vpunch
                    c " ...What- "
                    x " ... "
                    hide zipconfused at bottom
                    show zipsad at right
                    x " ... "
                    hide zipsad at left with easeoutleft
                    x " WAAAAHH!! "
                    " ...She ran away. "
                    " For someone who looked so tough...she started crying like a child. "
                    " It's insane, now that you think about it. But not really. "
                    hide clairescared at bottom
                    show claireneutral at left
                    show claireneutral at center with move
                    play music "audio/paperhigh.mp3" fadein 0.5
                    c " ... "
                    c " ...Um...Thank you. "
                    hide claireneutral at left with easeoutleft
                    " You gave her a thumbs up as a you're welcome and you went to sit on the bleachers and do your own thing. "
                    " Which is just scrolling on your phone. "
                    scene black with dissolve
                    " You spent the rest of the break scrolling on your phone... "
                    " ...And thinking about what happened and what you did. "
                    " It's surprising to me thatyou actually decided to help. "
                    " I think you might be ready...but not right now. Maybe on thursday. "
                    pause 2.0
                    play sound "audio/bellring.mp3"
                    " The bell rings after a few minutes, snapping you out of your thinking session. "
                    " You get up from where you were sitting and you walked back to your classroom for your final class. "
                    pause 2.0
                    jump artclass2
                else:
                    pass
                " You should probably just lie to the other girl so that she won't be bothering Claire anymore. "
                " Yeah, that's the best you got. Besides, if you tried convincing her that Claire didn't have the drawings, she probably wouldn't believe you. "
                " You tap the mean looking girl's shoulder and told her that you found someone in the hallways who had her brother's drawings. "
                x " Oh, what? Really...? "
                hide claireangry at bottom
                show claireneutral at left
                hide zipangry at bottom
                show zipneutral at right
                x " Fine then. I'll go check it out... "
                x " Which direction did they go in? "
                " You pointed to a random direction. "
                x " ...Okay. "
                hide zipneutral at left with easeoutleft
                show claireneutral at center with move
                " ..She skedaddled away. "
                c " ...Thanks for that, [name]. "
                c " For a fact, I didn't steal her brother's drawings. "
                c " I don't know why she would think that way... "
                c " It's kind of idiotic, if you ask me. To just assume someone did something bad... "
                c " You agree with me, right? "
                " You nodded. "
                scene black with dissolve
                " You spent the rest of the break having a talk with Claire. "
                " Just talking about random things...and talking about what happened with her and that other girl. "
                " Making jokes about her here and there... "
                " She's a pretty nice person to talk with. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, disrupting your conversation. "
                " You walked back to your classroom for your final class of the day. "
                pause 2.0
                jump artclass2
            " Nah, I'd rather just watch what's going on ":
                " Yeah, this isn't your problem. "
                " You took a seat on one of the bleachers and just watched. "
                " You pulled out your earphones and pretended you were listening to music... "
                " When in reality, you're just listening into their conversation. "
                " They won't even suspect a thing. "
                " Trust me. "
                scene black with dissolve
                if claireknow == True and oligangknow == True:
                    " You spent the rest of the break watching Claire and Zip argue. "
                elif claireknow == True and oligangknow == False:
                    " You spent the rest of the break watching Claire and the other girl argue. "
                elif claireknow == False and oligangknow == True:
                    " You spent the rest of the break watching the other girl and Zip argue. "
                else:
                    " You spent the rest of the break watching the two girls argue. "
                " It was pretty interesting, actually. "
                " They argued for a long time, you're surprised that they could argue for that long without getting tired. "
                play sound "audio/bellring.mp3"
                " For a fact, they argued until the bell rang. "
                " You got up from where you were sitting and you walked back toyour classroom for the final class. "
                pause 2.0
                jump artclass2
    elif claireknow == False and oligangknow == True:
        x " Jesus christ Zip, I told you that I didn't do it! "
        x " No, I didn't take away your little brother's drawings, why would I?! "
        z " Number one, you're the type of person to do that. "
        z " Number two, I know you have them, just admit it, god damn it! "
        x " No I don't? And I'm not the type of person to take away a child's drawings! "
        x " How about you go ask someone else, I really can't deal with this right now... "
        " Seems like she's in a bit of trouble. "
        " ...Do you want to help her? "
        menu:
            " Why not ":
                $ clairelv += 10
                " You walked up to the two and thought about what you should do to calm them down. "
                if clairebeatup == True:
                    $ clairedefend = True
                    " ...Hold on, you're actually helping her out? "
                    " ...Maybe you might be ready. "
                    z " Stop bullshitting me! I know you have my little brother's drawings! "
                    z " Stop lying and just -  "
                    stop music
                    hide zipangry at bottom
                    show zipconfused at right
                    hide claireangry at bottom
                    show clairescared at left
                    " You slapped Zip. " with vpunch
                    x " ...What- "
                    z " ... "
                    hide zipconfused at bottom
                    show zipsad at right
                    z " ... "
                    hide zipsad at left with easeoutleft
                    z " WAAAAHH!! "
                    " ...She ran away. "
                    " For someone who looked so tough...she started crying like a child. "
                    " It's insane, now that you think about it. But not really. "
                    hide clairescared at bottom
                    show claireneutral at left
                    show claireneutral at center with move
                    play music "audio/paperhigh.mp3" fadein 0.5
                    x " ... "
                    x " ...Um...Thank you. "
                    hide claireneutral at left with easeoutleft
                    " You gave her a thumbs up as a you're welcome and you went to sit on the bleachers and do your own thing. "
                    " Which is just scrolling on your phone. "
                    scene black with dissolve
                    " You spent the rest of the break scrolling on your phone... "
                    " ...And thinking about what happened and what you did. "
                    " It's surprising to me thatyou actually decided to help. "
                    " I think you might be ready...but not right now. Maybe on thursday. "
                    pause 2.0
                    play sound "audio/bellring.mp3"
                    " The bell rings after a few minutes, snapping you out of your thinking session. "
                    " You get up from where you were sitting and you walked back to your classroom for your final class. "
                    pause 2.0
                    jump artclass2
                else:
                    pass
                " You should probably just lie to Zip so that she won't be bothering this girl anymore. "
                " Yeah, that's the best you got. Besides, if you tried convincing her that the girl with the bow didn't have the drawings, she probably wouldn't believe you. "
                " You tap Zip's shoulder and told her that you found someone in the hallways who had her brother's drawings. "
                z " Oh, what? Really...? "
                hide claireangry at bottom
                show claireneutral at left
                hide zipangry at bottom
                show zipneutral at right
                z " Fine then. I'll go check it out... "
                z " Which direction did they go in? "
                " You pointed to a random direction. "
                z " ...Okay. "
                hide zipneutral at left with easeoutleft
                show claireneutral at center with move
                " ..She skedaddled away. "
                x " ...Thanks for that, [name]. "
                $ claireknow = True
                c " I'm Claire, by the way. We're classmates! "
                c " For a fact, I didn't steal her brother's drawings. "
                c " I don't know why she would think that way... "
                c " It's kind of idiotic, if you ask me. To just assume someone did something bad... "
                c " You agree with me, right? "
                " You nodded. "
                scene black with dissolve
                " You spent the rest of the break having a talk with Claire. "
                " Just talking about random things...and talking about what happened with her and Zip. "
                " Making jokes about her here and there... "
                " She's a pretty nice person to talk with. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, disrupting your conversation. "
                " You walked back to your classroom for your final class of the day. "
                pause 2.0
                jump artclass2
            " Nah, I'd rather just watch what's going on ":
                " Yeah, this isn't your problem. "
                " You took a seat on one of the bleachers and just watched. "
                " You pulled out your earphones and pretended you were listening to music... "
                " When in reality, you're just listening into their conversation. "
                " They won't even suspect a thing. "
                " Trust me. "
                scene black with dissolve
                if claireknow == True and oligangknow == True:
                    " You spent the rest of the break watching Claire and Zip argue. "
                elif claireknow == True and oligangknow == False:
                    " You spent the rest of the break watching Claire and the other girl argue. "
                elif claireknow == False and oligangknow == True:
                    " You spent the rest of the break watching the other girl and Zip argue. "
                else:
                    " You spent the rest of the break watching the two girls argue. "
                " It was pretty interesting, actually. "
                " They argued for a long time, you're surprised that they could argue for that long without getting tired. "
                play sound "audio/bellring.mp3"
                " For a fact, they argued until the bell rang. "
                " You got up from where you were sitting and you walked back toyour classroom for the final class. "
                pause 2.0
                jump artclass2
    else:
        x " Jesus christ Zip, I told you that I didn't do it! "
        x " No, I didn't take away your little brother's drawings, why would I?! "
        x " Number one, you're the type of person to do that. "
        x " Number two, I know you have them, just admit it, god damn it! "
        x " No I don't? And I'm not the type of person to take away a child's drawings! "
        x " How about you go ask someone else, I really can't deal with this right now... "
        " Seems like she's in a bit of trouble. "
        " ...Do you want to help her? "
        menu:
            " Why not ":
                $ clairelv += 10
                " You walked up to the two and thought about what you should do to calm them down. "
                if clairebeatup == True:
                    $ clairedefend = True
                    " ...Hold on, you're actually helping her out? "
                    " ...Maybe you might be ready. "
                    x " Stop bullshitting me! I know you have my little brother's drawings! "
                    x " Stop lying and just -  "
                    stop music
                    hide zipangry at bottom
                    show zipconfused at right
                    hide claireangry at bottom
                    show clairescared at left
                    " You slapped the other girl. " with vpunch
                    x " ...What- "
                    x " ... "
                    hide zipconfused at bottom
                    show zipsad at right
                    x " ... "
                    hide zipsad at left with easeoutleft
                    x " WAAAAHH!! "
                    " ...She ran away. "
                    " For someone who looked so tough...she started crying like a child. "
                    " It's insane, now that you think about it. But not really. "
                    hide clairescared at bottom
                    show claireneutral at left
                    show claireneutral at center with move
                    play music "audio/paperhigh.mp3" fadein 0.5
                    x " ... "
                    x " ...Um...Thank you. "
                    hide claireneutral at left with easeoutleft
                    " You gave her a thumbs up as a you're welcome and you went to sit on the bleachers and do your own thing. "
                    " Which is just scrolling on your phone. "
                    scene black with dissolve
                    " You spent the rest of the break scrolling on your phone... "
                    " ...And thinking about what happened and what you did. "
                    " It's surprising to me thatyou actually decided to help. "
                    " I think you might be ready...but not right now. Maybe on thursday. "
                    pause 2.0
                    play sound "audio/bellring.mp3"
                    " The bell rings after a few minutes, snapping you out of your thinking session. "
                    " You get up from where you were sitting and you walked back to your classroom for your final class. "
                    pause 2.0
                    jump artclass2
                else:
                    pass
                " You should probably just lie to the mean girl so that she won't be bothering this girl anymore. "
                " Yeah, that's the best you got. Besides, if you tried convincing her that the girl with the bow didn't have the drawings, she probably wouldn't believe you. "
                " You tap the mean girl's shoulder and told her that you found someone in the hallways who had her brother's drawings. "
                x " Oh, what? Really...? "
                hide claireangry at bottom
                show claireneutral at left
                hide zipangry at bottom
                show zipneutral at right
                x " Fine then. I'll go check it out... "
                x " Which direction did they go in? "
                " You pointed to a random direction. "
                x " ...Okay. "
                hide zipneutral at left with easeoutleft
                show claireneutral at center with move
                " ..She skedaddled away. "
                x " ...Thanks for that, [name]. "
                $ claireknow = True
                c " I'm Claire, by the way. We're classmates! "
                c " For a fact, I didn't steal her brother's drawings. "
                c " I don't know why she would think that way... "
                c " It's kind of idiotic, if you ask me. To just assume someone did something bad... "
                c " You agree with me, right? "
                " You nodded. "
                scene black with dissolve
                " You spent the rest of the break having a talk with Claire. "
                " Just talking about random things...and talking about what happened with her and Zip. "
                " Making jokes about her here and there... "
                " She's a pretty nice person to talk with. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, disrupting your conversation. "
                " You walked back to your classroom for your final class of the day. "
                pause 2.0
                jump artclass2
            " Nah, I'd rather just watch what's going on ":
                " Yeah, this isn't your problem. "
                " You took a seat on one of the bleachers and just watched. "
                " You pulled out your earphones and pretended you were listening to music... "
                " When in reality, you're just listening into their conversation. "
                " They won't even suspect a thing. "
                " Trust me. "
                scene black with dissolve
                if claireknow == True and oligangknow == True:
                    " You spent the rest of the break watching Claire and Zip argue. "
                elif claireknow == True and oligangknow == False:
                    " You spent the rest of the break watching Claire and the other girl argue. "
                elif claireknow == False and oligangknow == True:
                    " You spent the rest of the break watching the other girl and Zip argue. "
                else:
                    " You spent the rest of the break watching the two girls argue. "
                " It was pretty interesting, actually. "
                " They argued for a long time, you're surprised that they could argue for that long without getting tired. "
                play sound "audio/bellring.mp3"
                " For a fact, they argued until the bell rang. "
                " You got up from where you were sitting and you walked back toyour classroom for the final class. "
                pause 2.0
                jump artclass2
label tuesdaycafe5:
    # Kevin, Ruby, and Bubble
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and you spotted three of your classmates just chilling. "
    " You're thinking about talking to one of them...but who do you talk to? "
    if kevinknow,rubyknow,bubbleknow == True:
        menu:
            " {image=rubyicon} Ruby and Bubble {image=bubbleicon} ":
                jump ash
            " {image=kevinicon} Kevin {image=kevinicon} ":
                jump again
    elif rubyknow,bubbleknow == True and kevinknow == False:
        menu:
            " {image=rubyicon} Ruby and Bubble {image=bubbleicon} ":
                jump ash
            " {image=kevinicon} A guy that looks like a nerd {image=kevinicon} ":
                jump again
    elif rubyknow,kevinknow == True and bubbleknow == False:
        menu:
            " {image=rubyicon} Ruby and a girl with a duck on her head {image=bubbleicon} ":
                jump ash
            " {image=kevinicon} Kevin {image=kevinicon} ":
                jump again
    elif kevinknow,bubbleknow == True and rubyknow == False:
        menu:
            " {image=rubyicon} A girl that has a TV for a head and Bubble {image=bubbleicon} ":
                jump ash
            " {image=kevinicon} Kevin {image=kevinicon} ":
                jump again
    elif rubyknow == True and bubbleknow,kevinknow == False:
        menu:
            " {image=rubyicon} Ruby and a girl with a rubber duck on her head {image=bubbleicon} ":
                jump ash
            " {image=kevinicon} A guy that looks like a nerd {image=kevinicon} ":
                jump again
    elif bubbleknow == True and rubyknow,kevinknow == False:
        menu:
            " {image=rubyicon} A girl with a TV for a head and Bubble {image=bubbleicon} ":
                jump ash
            " {image=kevinicon} A guy that looks like a nerd {image=kevinicon} ":
                jump again
    elif kevinknow == True and rubyknow,bubbleknow == False:
        menu:
            " {image=rubyicon} A girl with a TV for a head and a girl with a rubber duck on her head {image=bubbleicon} ":
                jump ash
            " {image=kevinicon} Kevin {image=kevinicon} ":
                jump again
    else:
        menu:
            " {image=rubyicon} A girl with a TV for a head and a girl with a rubber duck on her head {image=bubbleicon} ":
                jump ash
            " {image=kevinicon} A guy that looks like a nerd {image=kevinicon} ":
                jump again
    label ash:
        show rubyneutral at left with easeinright
        show bubbleneutral at right with easeinright
        if rubyknow == True and bubbleknow == True:
            ru " Hello, [name]! "
            b " Hi [name]!! Glad to have you here with us!! "
            ru " Yeah, [name]!! I hope you're doing well!! "
            ru " Actually, now that I think about it... "
            ru " Bubble, you're quite literally made of bubble's...right? "
            b " Yes, that's right. "
            ru " ...And bubbles are made of soapy water, right...? "
            hide bubbleneutral at bottom
            show bubbleconfuse at right
            b " Yess?????????????? "
            ru " ... "
            ru " As long as you don't touch my wires I think I should be fine. "
            hide bubbleconfuse at bottom
            show bubbleneutral at right
            b " Ooooh, right!! "
            b " Electricity and stuff like water doesn't really go well... "
            ru " Yup! My wires are safe, so there's a low chance I'll even get electrocuted! "
            b " Hopefully that doesn't happen... "
            " ...You're kind of tempted to pour a bucket of water on Ruby. "
            " Now that you think about it, some people must've already thought about doing that to Ruby. "
            " So, she might be seeing it coming and has to be careful. "
            scene black with dissolve
            " You spent the rest of the break having a nice talk with Ruby and Bubble. "
            " And totally not thinking about pouring a bucket of water on Ruby. "
            " Totally. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, disrupting your conversation with Ruby and Bubble. "
            " You get up from where you were sitting and you walked back to your classroom for your final class of the day. "
            pause 2.0
            jump artclass2
        elif rubyknow == True and bubbleknow == False:
            ru " Hello, [name]! "
            x " Hi [name]!! Glad to have you here with us!! "
            ru " Yeah, [name]!! I hope you're doing well!! "
            x " Oh, waitwait! I haven't introduced myself to you yet!! I'm so sorry! "
            $ bubbleknow = True
            b " I'm Bubble, it's nice to meet you!! We're classmates!! "
            ru " Hmhm...I just had a thought. "
            ru " Bubble, you're quite literally made of bubble's...right? "
            b " Yes, that's right. "
            ru " ...And bubbles are made of soapy water, right...? "
            hide bubbleneutral at bottom
            show bubbleconfuse at right
            b " Yess?????????????? "
            ru " ... "
            ru " As long as you don't touch my wires I think I should be fine. "
            hide bubbleconfuse at bottom
            show bubbleneutral at right
            b " Ooooh, right!! "
            b " Electricity and stuff like water doesn't really go well... "
            ru " Yup! My wires are safe, so there's a low chance I'll even get electrocuted! "
            b " Hopefully that doesn't happen... "
            " ...You're kind of tempted to pour a bucket of water on Ruby. "
            " Now that you think about it, some people must've already thought about doing that to Ruby. "
            " So, she might be seeing it coming and has to be careful. "
            scene black with dissolve
            " You spent the rest of the break having a nice talk with Ruby and Bubble. "
            " And totally not thinking about pouring a bucket of water on Ruby. "
            " Totally. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, disrupting your conversation with Ruby and Bubble. "
            " You get up from where you were sitting and you walked back to your classroom for your final class of the day. "
            pause 2.0
            jump artclass2
        elif rubyknow == False and bubbleknow == True:
            x " Hello, [name]! "
            b " Hi [name]!! Glad to have you here with us!! "
            x " Yeah, [name]!! I hope you're doing well!! "
            x " Actually, now that I think about it... "
            x " I haven't introduced myself to you yet! I apologize... "
            $ rubyknow = True
            ru " I'm Ruby! We're classmates!! "
            ru " Oh, I just had another thought! "
            ru " Bubble, you're quite literally made of bubble's...right? "
            b " Yes, that's right. "
            ru " ...And bubbles are made of soapy water, right...? "
            hide bubbleneutral at bottom
            show bubbleconfuse at right
            b " Yess?????????????? "
            ru " ... "
            ru " As long as you don't touch my wires I think I should be fine. "
            hide bubbleconfuse at bottom
            show bubbleneutral at right
            b " Ooooh, right!! "
            b " Electricity and stuff like water doesn't really go well... "
            ru " Yup! My wires are safe, so there's a low chance I'll even get electrocuted! "
            b " Hopefully that doesn't happen... "
            " ...You're kind of tempted to pour a bucket of water on Ruby. "
            " Now that you think about it, some people must've already thought about doing that to Ruby. "
            " So, she might be seeing it coming and has to be careful. "
            scene black with dissolve
            " You spent the rest of the break having a nice talk with Ruby and Bubble. "
            " And totally not thinking about pouring a bucket of water on Ruby. "
            " Totally. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, disrupting your conversation with Ruby and Bubble. "
            " You get up from where you were sitting and you walked back to your classroom for your final class of the day. "
            pause 2.0
            jump artclass2
        else:
            x " Hello, [name]! "
            x " Hi [name]!! Glad to have you here with us!! "
            x " Yeah, [name]!! I hope you're doing well!! "
            x " Waitwait! I forgot to introduce myself to you, [name]! I'm so sorry! "
            $ bubbleknow = True
            b " I'm Bubble! It's nice to meet you! We're classmates! "
            x " Actually, now that I think about it... "
            x " I haven't introduced myself to you yet! I apologize... "
            $ rubyknow = True
            ru " I'm Ruby! We're also classmates!! "
            ru " Oh, I just had another thought! "
            ru " Bubble, you're quite literally made of bubble's...right? "
            b " Yes, that's right. "
            ru " ...And bubbles are made of soapy water, right...? "
            hide bubbleneutral at bottom
            show bubbleconfuse at right
            b " Yess?????????????? "
            ru " ... "
            ru " As long as you don't touch my wires I think I should be fine. "
            hide bubbleconfuse at bottom
            show bubbleneutral at right
            b " Ooooh, right!! "
            b " Electricity and stuff like water doesn't really go well... "
            ru " Yup! My wires are safe, so there's a low chance I'll even get electrocuted! "
            b " Hopefully that doesn't happen... "
            " ...You're kind of tempted to pour a bucket of water on Ruby. "
            " Now that you think about it, some people must've already thought about doing that to Ruby. "
            " So, she might be seeing it coming and has to be careful. "
            scene black with dissolve
            " You spent the rest of the break having a nice talk with Ruby and Bubble. "
            " And totally not thinking about pouring a bucket of water on Ruby. "
            " Totally. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, disrupting your conversation with Ruby and Bubble. "
            " You get up from where you were sitting and you walked back to your classroom for your final class of the day. "
            pause 2.0
            jump artclass2
    label again:
        show kevinneutral at center with easeinleft
        if kevinknow == True:
            " You walked up to him and sat next to him, greeting him before you asked him what he was doing. "
            kv " Greetings, [name]. "
            kv " Is it not obvious as to what I'm doing? "
            kv " I'm studying for art class, our next class, by the way. "
            " You thought art class was just all about painting. "
            kv " Of course not! The teacher has to teach us everything about all kinds of things about art. "
            kv " And also throw in art related quizzes, of course. "
            kv " That's why I took down all the notes I could in art class! "
            kv " ...It's a lot, I'll admit, but only because I want to fully understand and memorize everything! "
            kv " ...So far I could only memorize atleast 5 things written in here. "
            hide kevinneutral at bottom
            show kevinangry at center
            kv " That doesn't satisfy me! I want to memorize better! "
            hide kevinangry at bottom
            show kevinneutral at center
            kv " [name], could you try to help me memorize a few things before art class starts? "
            menu:
                " sure why not ":
                    $ kevinlv += 10
                    hide kevinneutral at bottom
                    show kevinhappy at center
                    kv " Splendid! "
                    kv " I appreciate your help, [name]! "
                    scene black with dissolve
                    " You spent the rest of the break helping Kevin memorize. "
                    " You didn't really know what to do, so you just repeated the questions until he got it right. "
                    " Suprisingly, he managed to memorize atleast 10 things due to what you did. "
                    " Not a lot, but it's an improvement atleast. "
                    " You can't even memorize anything yourself. One second you're like; 'okay I have to do that'.. "
                    " ...And the next, you'd probably forget what you were supposed to do. "
                    " Most normal MC thoughts ever. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, interrupting your memorizing session. "
                    " You get up from where you were sitting and walked back to your classroom for art class. "
                    pause 2.0
                    jump artclass2
                " nah no thanks ":
                    kv " ...I'll ask someone else next time then. "
                    kv " You can stay with me as I study, I don't mind. "
                    kv " Just don't bother me. "
                    scene black with dissolve
                    " You spent the rest of the break just chilling with Kevin. "
                    " You didn't want to disturb him, so you just played some games on your phone. "
                    " Atleast you had something to do otherthan just stare into the abyss. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, interrupting your gaming session. "
                    " You get up from where you were sitting, and you walked back to your classroom for art class. "
                    pause 2.0
                    jump artclass2
        else:
            " You walked up to him and sat next to him, greeting him before you asked him what he was doing. "
            x " Greetings, [name]. "
            $ kevinknow = True
            kv " I'm Kevin, one of your classmates, and... "
            kv " Is it not obvious as to what I'm doing? "
            kv " I'm studying for art class, our next class, by the way. "
            " You thought art class was just all about painting. "
            kv " Of course not! The teacher has to teach us everything about all kinds of things about art. "
            kv " And also throw in art related quizzes, of course. "
            kv " That's why I took down all the notes I could in art class! "
            kv " ...It's a lot, I'll admit, but only because I want to fully understand and memorize everything! "
            kv " ...So far I could only memorize atleast 5 things written in here. "
            hide kevinneutral at bottom
            show kevinangry at center
            kv " That doesn't satisfy me! I want to memorize better! "
            hide kevinangry at bottom
            show kevinneutral at center
            kv " [name], could you try to help me memorize a few things before art class starts? "
            menu:
                " sure why not ":
                    $ kevinlv += 10
                    hide kevinneutral at bottom
                    show kevinhappy at center
                    kv " Splendid! "
                    kv " I appreciate your help, [name]! "
                    scene black with dissolve
                    " You spent the rest of the break helping Kevin memorize. "
                    " You didn't really know what to do, so you just repeated the questions until he got it right. "
                    " Suprisingly, he managed to memorize atleast 10 things due to what you did. "
                    " Not a lot, but it's an improvement atleast. "
                    " You can't even memorize anything yourself. One second you're like; 'okay I have to do that'.. "
                    " ...And the next, you'd probably forget what you were supposed to do. "
                    " Most normal MC thoughts ever. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, interrupting your memorizing session. "
                    " You get up from where you were sitting and walked back to your classroom for art class. "
                    pause 2.0
                    jump artclass2
                " nah no thanks ":
                    kv " ...I'll ask someone else next time then. "
                    kv " You can stay with me as I study, I don't mind. "
                    kv " Just don't bother me. "
                    scene black with dissolve
                    " You spent the rest of the break just chilling with Kevin. "
                    " You didn't want to disturb him, so you just played some games on your phone. "
                    " Atleast you had something to do otherthan just stare into the abyss. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, interrupting your gaming session. "
                    " You get up from where you were sitting, and you walked back to your classroom for art class. "
                    pause 2.0
                    jump artclass2
label tuesdayrooftop5:
    # lizzy and petunia
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked up onto the rooftop and spotted two of your classmates talking about something. "
    " Curious on what they're talking about, you walk over to them and see what they're doing. "
    show petunianeutral at left with easeinright
    show lizzyneutral at right with easeinright
    if popularknow == True:
        p " Heya, [name]! "
        lz " Hi, [name]. "
        p " Me and Lizzy have been thinking about what games we should play on Boblox! "
        lz " We can't just play HavenBrook for all of our videos. "
        lz " We need something new, something popular... "
        p " Do you have any ideas, [name]? "
        " You thought about games you've played on Boblox before... "
        " ..And then you remembered a game that everyone's been playing recently. "
        " You told them to hear you out for just a moment. "
        p " We're listening... "
        " ...And then you told them that you wanted them to play Dress to Impress. "
        " A nice dressing up game where you compete with other people to have the best outfit ever and reach number one. "
        hide petunianeutral at bottom
        show petuniahappy at left
        p " Oh, hey! I've heard of that game before! "
        lz " Yeah, it's quite popular, actually. "
        p " Maybe we should give it a try later, Lizzy? "
        lz " Mhm. "
        p " Thanks for your help, [name]! "
        scene black with dissolve
        " You spent the rest of the break talking with Petunia and Lizzy. "
        " You were basically just talking about what you can do in Dress to Impress. "
        " You haven't even played the game yourself, you were just basing off your explanation off of what you've seen in videos. "
        " You also added in about how the game has lore. Somewhat. "
        " Now that you think about it, it {i}is{/i} kind of insane that a game about dressing up has lore. "
        " You haven't seen anything like it, but that's what makes it unique. "
        " Shoutout to all of the baddies who play dress to impress. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, disrupting your conversation with Petunia and Lizzy. "
        " You walked down from the rooftop and you walked back down to your classroom. "
        pause 2.0
        jump artclass2
    else:
        x " Heya, [name]! "
        x " Hi, [name]. "
        x " I don't think we've introduced ourselves to you yet, have we? "
        x " Do they really need our introduction? I'm sure they know us already. "
        x " Come on, Liz! we're not that popular yet! "
        x " Hm...you're right. Let's do it then. "
        $ popularknow = True
        p " I'm Petunia! "
        lz " And I'm Lizzy. Me and Petunia are the bestest of friends. "
        p " We're inseperable! "
        p " Anyway...me and Lizzy have been thinking about what games we should play on Boblox! "
        lz " We can't just play HavenBrook for all of our videos. "
        lz " We need something new, something popular... "
        p " Do you have any ideas, [name]? "
        " You thought about games you've played on Boblox before... "
        " ..And then you remembered a game that everyone's been playing recently. "
        " You told them to hear you out for just a moment. "
        p " We're listening... "
        " ...And then you told them that you wanted them to play Dress to Impress. "
        " A nice dressing up game where you compete with other people to have the best outfit ever and reach number one. "
        hide petunianeutral at bottom
        show petuniahappy at left
        p " Oh, hey! I've heard of that game before! "
        lz " Yeah, it's quite popular, actually. "
        p " Maybe we should give it a try later, Lizzy? "
        lz " Mhm. "
        p " Thanks for your help, [name]! "
        scene black with dissolve
        " You spent the rest of the break talking with Petunia and Lizzy. "
        " You were basically just talking about what you can do in Dress to Impress. "
        " You haven't even played the game yourself, you were just basing off your explanation off of what you've seen in videos. "
        " You also added in about how the game has lore. Somewhat. "
        " Now that you think about it, it {i}is{/i} kind of insane that a game about dressing up has lore. "
        " You haven't seen anything like it, but that's what makes it unique. "
        " Shoutout to all of the baddies who play dress to impress. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, disrupting your conversation with Petunia and Lizzy. "
        " You walked down from the rooftop and you walked back down to your classroom. "
        pause 2.0
        jump artclass2
label tuesdaylibrary5:
    # abbie needing help on art skills
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and spotted one of your classmates drawing something in their notebook. "
    " Curious on what they're drawing, you decided to walk up to them and check it out. "
    show abbieneutral at center with easeinright
    if abbieknow == True:
        " He doesn't seem to notice that you sat next to him. "
        " He did once you moved a bit though, and he immediately closed his notebookin embarrasment. "
        a " ...You...shouldn't see that... "
        a " I know my art skills are horrible... "
        " You try to remember what Abbie drew, and you thought it looked pretty nice. "
        " You told him that it looked really nice and that you can literally only draw a stickman. "
        " Making him look better than you so that he could feel better. "
        " You could probably only draw a stickman though. Or not, if you're an artist or something. "
        a " ...Really...? You think my drawing looked nice? "
        a " Thanks, but... I don't think that way... "
        a " I want to improve my drawing skills...Everyone elses paintings looked so nice yesterday... "
        a " And mine just looked...boring and unoriginal... "
        " You told him that he was very creative and that his painting looked nice. "
        " You understood the struggle of thinking that what you're doing is not good enough. "
        " But, you just gotta remind yourself that you're doing okay, and improvement takes time. "
        " That's what you told Abbie. "
        a " ...You're...right... "
        hide abbieneutral at bottom
        show abbiehappy at center
        a " ...Well, um...would you like to draw with me...? "
        menu:
            " Sure!! You're going to be better at drawing than me though ":
                $ abbielv += 10
                a " Yahoo!! "
                a " Hmm...You don't have anything to drawon though... "
                a " ...Oh, I know!! I have extra paper...here... and also an extra pencil for you to draw with.. "
                " Abbie gives you the extra paper and the extra pencil he grabbed out. "
                " He honestly looks so adorable being happy like this... "
                " ...You couldn't help but reach out and pat his head. "
                " He seemed surprised by the action, but he seemed happy about it nonetheless. "
                " You then started drawing with Abbie. "
                scene black with dissolve
                " You drew with Abbie in the library for the rest of the break. "
                " You drew a nice picture of you and Abbie just hanging out. Abbie on the other hand... "
                " He drew a REALLY nice portrait of you. "
                " He said it was because you were being so nice to him...aww... "
                " You asked if you could keep it somewhere in your room and he said yes. "
                " God he's adorable. Onceyou two were done drawing, you both just kinda talked with eachother for a bit. "
                play sound "audio/bellring.mp3"
                " The bell rings, disrupting your conversation with Abbie. "
                " You get up from where you were seated, and you walked back to the classroom. "
                pause 2.0
                jump artclass2
            " Nah my drawing skills suck, you're better though ":
                $ abbielv += 5
                a " Ah...I'm sure your drawings skills are just as good, [name]... "
                a " Since you don't want to draw, then maybe you could just... "
                a " ...Watch me draw, right...? "
                " You nodded your head. You wanted to see what kinds of things Abbie's going to draw. "
                " He seemed to look really happy when he saw that you wanted to watch him draw... "
                " ...Adorable. "
                " He started to draw after a bit. "
                scene black with dissolve
                " You spent the rest of the break watching Abbie draw and talking with him. "
                " You weren't going to lie, he was actually a really good artist. "
                " He might just be a really nice artist in the future... "
                " But who knows? Only time will tell. And also his decisions if he really wants to be an artist. "
                play sound "audio/bellring.mp3"
                " The bell rings, disrupting your drawing session with Abbie. "
                " You get up from where you were sitting and you walked back to your classroom. "
                pause 2.0
                jump artclass2
    else:
        " He doesn't seem to notice that you sat next to him. "
        " He did once you moved a bit though, and he immediately closed his notebookin embarrasment. "
        x " ...You...shouldn't see that... "
        x " I know my art skills are horrible... "
        " You try to remember what he drew, and you thought it looked pretty nice. "
        " You told him that it looked really nice and that you can literally only draw a stickman. "
        " Making him look better than you so that he could feel better. "
        " You could probably only draw a stickman though. Or not, if you're an artist or something. "
        x " ...Really...? You think my drawing looked nice? "
        x " Thanks, but... I don't think that way... "
        x " I want to improve my drawing skills...Everyone elses paintings looked so nice yesterday... "
        x " And mine just looked...boring and unoriginal... "
        " You told him that he was very creative and that his painting looked nice. "
        " You understood the struggle of thinking that what you're doing is not good enough. "
        " But, you just gotta remind yourself that you're doing okay, and improvement takes time. "
        " That's what you told him. "
        x " ...You're...right... "
        hide abbieneutral at bottom
        show abbiehappy at center
        x " ...Well, um...would you like to draw with me...? "
        $ abbieknow = True
        a " I'm Abbie, by the way... "
        " You told him that it was nice to meet him, and you thought about his question for a bit... "
        menu:
            " Sure!! You're going to be better at drawing than me though ":
                $ abbielv += 10
                a " Yahoo!! "
                a " Hmm...You don't have anything to drawon though... "
                a " ...Oh, I know!! I have extra paper...here... and also an extra pencil for you to draw with.. "
                " Abbie gives you the extra paper and the extra pencil he grabbed out. "
                " He honestly looks so adorable being happy like this... "
                " ...You couldn't help but reach out and pat his head. "
                " He seemed surprised by the action, but he seemed happy about it nonetheless. "
                " You then started drawing with Abbie. "
                scene black with dissolve
                " You drew with Abbie in the library for the rest of the break. "
                " You drew a nice picture of you and Abbie just hanging out. Abbie on the other hand... "
                " He drew a REALLY nice portrait of you. "
                " He said it was because you were being so nice to him...aww... "
                " You asked if you could keep it somewhere in your room and he said yes. "
                " God he's adorable. Onceyou two were done drawing, you both just kinda talked with eachother for a bit. "
                play sound "audio/bellring.mp3"
                " The bell rings, disrupting your conversation with Abbie. "
                " You get up from where you were seated, and you walked back to the classroom. "
                pause 2.0
                jump artclass2
            " Nah my drawing skills suck, you're better though ":
                $ abbielv += 5
                a " Ah...I'm sure your drawings skills are just as good, [name]... "
                a " Since you don't want to draw, then maybe you could just... "
                a " ...Watch me draw, right...? "
                " You nodded your head. You wanted to see what kinds of things Abbie's going to draw. "
                " He seemed to look really happy when he saw that you wanted to watch him draw... "
                " ...Adorable. "
                " He started to draw after a bit. "
                scene black with dissolve
                " You spent the rest of the break watching Abbie draw and talking with him. "
                " You weren't going to lie, he was actually a really good artist. "
                " He might just be a really nice artist in the future... "
                " But who knows? Only time will tell. And also his decisions if he really wants to be an artist. "
                play sound "audio/bellring.mp3"
                " The bell rings, disrupting your drawing session with Abbie. "
                " You get up from where you were sitting and you walked back to your classroom. "
                pause 2.0
                jump artclass2
label artclass2:
    scene classroom with dissolve
    " You walked into the classroom and waited for the class to start. "
    show sashaneutral at center with easeinright
    mss " Hellooo, class! "
    mss " No activities today, unfortunately, buuuut!! "
    hide sashaneutral at bottom
    show sashahappy at center
    mss " We're only gonna be copying a few things from our lesson last week!! "
    mss " No yapping session, woohoo! "
    mss " Get out your notebooks, let me prepare the slides real quick... "
    scene black with dissolve
    " You spent the rest of class writing things down on your notebook. "
    " It was pretty boring, but atleast you don't have to listen to a yapping session... "
    " ...Like what Miss Sasha said. "
    " Now that you think about it, she just said some gen alpha slang. "
    " Kind of embarrassing to hear from a teacher, but also funny. "
    " Probably just them trying to look cool. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, meaning that the school day is over. "
    " You grab your things together, and you walked out of the school to go home. "
    pause 2.0
    jump endday2
label endday2:
    scene paperschoolfront with dissolve
    if populartiktoklater == True:
        show petunieneutral at left with easeinright
        show lizzyneutral at right with easeinright
        p " Heeey, [name]!! Looks like it's time for our video!! "
        lz " Mhm. We know you just want to get home, soo... "
        p " Let's get right into it! "
        p " Pretty sure you know what to do, right? "
        lz " Just answer the questions Petunia throws at you. "
        lz " I'll be the one recording. "
        p " Okay, here we go! "
        lz " Three, two, one... go. "
        p " Hiii everyone, today we have a special guest: [name]!! "
        if kind == True:
            " You wave energetically at the camera. "
        elif calm == True:
            " You do a peace sign at the camera. "
        elif mean == True:
            " You do a simple wave at the camera. "
        p " Today, we'll be asking a bunch of questions to [name]!! "
        p " Here's our first one - [name], what's your favorite food? "
        " You told them what your favorite food was. "
        " No, you can't say that you ate people for breakfast today. "
        " That'd make them lose their followers! "
        p " Ooo, sounds delicious! "
        " Petunia and Lizzy continue to throw questions at you until all of them were answered. "
        " They stopped recording. "
        p " That was great, [name]! "
        lz " Mhm. Let's just see if our video goes well tomorrow. "
        p " We'll see you tomorrow, [name]!! "
        lz " See you. "
        hide petunianeutral at left with easeoutleft
        hide lizzyneutral at left with easeoutleft
        " And with that, you went back home. "
        scene black with dissolve
        jump homelala
    else:
        pass
    " What a tiring day of school...You're glad that you're going back home now though. "
    " You can't wait to just go back and lay on your comfy bed... "
    if abbielv >= 10:
        " You were about to walk home, but someone walked up to you and tapped your shoulder. "
        " You turned around to see who it was... "
        show abbieneutral at center with easeinleft
        a " Um...hey, [name]... "
        a " You see...I need help with homework... "
        a " Miss Bloomie gave us homework last week and tomorrow is the deadline... "
        a " You could do the assignment given to us at my house, if you want... "
        a " I'm not forcing you to help me out...but...do you want to...? "
        a " It's okay if not... "
        menu:
            " Help Abbie with his homework ":
                $ abbiehomework = True
                $ abbielv += 10
                hide abbieneutral at bottom
                show abbiehappy at center
                a " ...Really...? "
                a " Okay, um...my house isn't that far...just follow me... "
                hide abbiehappy at right with easeoutright
                scene black with dissolve
                " You followed Abbie all the way to his house. "
                " It took a bit, but you guys eventually got there. "
                " You followed him all the way to his room. "
                scene abbieroom with dissolve
                show abbiehappy at center with easeinleft
                a " Here's my room...sorry if it looks like a mess... "
                " You told him that it looked just fine. "
                " You then asked him what kind of homework that he had to do. "
                hide abbiehappy at bottom
                show abbieneutral at center
                a " ...Wellll...we only have to answer a few questions... "
                a " Only 3, and we have to give an explanation... "
                a " ...It should be pretty easy, but...the problem is, two questions are kind of... "
                a " Confusing me... "
                " You told him not to worry and that you'll help. "
                hide abbieneutral at bottom
                show abbiehappy at center
                a " Hehe...thank you, [name]...you're the best... "
                scene black with dissolve
                " You helped Abbie do his homework while you did yours. "
                " You also came up with different explanations for you and Abbie... "
                " ...With ChatGPT. Miss Bloomie's not gonna know, anyway. "
                " After you were done helping him, you told him that you had a great time hanging out with him. "
                " You then politely left to go to your own house. "
                pause 2.0
                jump homelala
            " No thanks, I'm busy ":
                a " ..I understand.. "
                a " I'll go ahead and ask Lana if she's available then... "
                a " I'll seeyou tomorrow, [name]... "
                hide abbieneutral at right with easeoutright
                " You waved him goodbye before you started walking to your own home. "
                scene black with dissolve
                jump homelala
    elif abbielv == 10:
        " You were about to walk home, but someone walked up to you and tapped your shoulder. "
        " You turned around to see who it was... "
        show abbieneutral at center with easeinleft
        a " Um...hey, [name]... "
        a " You see...I need help with homework... "
        a " Miss Bloomie gave us homework last week and tomorrow is the deadline... "
        a " You could do the assignment given to us at my house, if you want... "
        a " I'm not forcing you to help me out...but...do you want to...? "
        a " It's okay if not... "
        menu:
            " Help Abbie with his homework ":
                $ abbiehomework = True
                $ abbielv += 10
                hide abbieneutral at bottom
                show abbiehappy at center
                a " ...Really...? "
                a " Okay, um...my house isn't that far...just follow me... "
                hide abbiehappy at right with easeoutright
                scene black with dissolve
                " You followed Abbie all the way to his house. "
                " It took a bit, but you guys eventually got there. "
                " You followed him all the way to his room. "
                scene abbieroom with dissolve
                show abbiehappy at center with easeinleft
                a " Here's my room...sorry if it looks like a mess... "
                " You told him that it looked just fine. "
                " You then asked him what kind of homework that he had to do. "
                hide abbiehappy at bottom
                show abbieneutral at center
                a " ...Wellll...we only have to answer a few questions... "
                a " Only 3, and we have to give an explanation... "
                a " ...It should be pretty easy, but...the problem is, two questions are kind of... "
                a " Confusing me... "
                " You told him not to worry and that you'll help. "
                hide abbieneutral at bottom
                show abbiehappy at center
                a " Hehe...thank you, [name]...you're the best... "
                scene black with dissolve
                " You helped Abbie do his homework while you did yours. "
                " You also came up with different explanations for you and Abbie... "
                " ...With ChatGPT. Miss Bloomie's not gonna know, anyway. "
                " After you were done helping him, you told him that you had a great time hanging out with him. "
                " You then politely left to go to your own house. "
                pause 2.0
                jump homelala
            " No thanks, I'm busy ":
                a " ..I understand.. "
                a " I'll go ahead and ask Lana if she's available then... "
                a " I'll seeyou tomorrow, [name]... "
                hide abbieneutral at right with easeoutright
                " You waved him goodbye before you started walking to your own home. "
                scene black with dissolve
                jump homelala
    else:
        pass
    " You then started to walk back to your nice and comfy home. "
    scene black with dissolve
    stop music fadeout 0.5
    pause 2.0
    jump homelala
label homelala:
    play music "audio/home.mp3" fadein 0.5
    scene mcroom with dissolve
    " Once you get home, you get changed and immediately lay on your bed. "
    " How you've missed the warm comforts of your bed... "
    " ...Even though it's only been a few hours. "
    if abbiehomework == True:
        " With your homework done, you immediately fell asleep. "
        " You just felt really exhausted. "
        scene black with dissolve
        stop music fadeout 1.5
        " Good night, [name]. "
        pause 2.0
        jump wednesday
    else:
        " You checked your phone and turns out there's homework thats due tomorrow that had been sent by Miss Bloomie. "
        " You quickly spedran all of that, and once you were done, you went to sleep. "
        " You were just that exhausted, huh? "
        scene black with dissolve
        stop music fadeout 1.5
        " Well, good night, [name] "
        pause 2.0
        jump wednesday
