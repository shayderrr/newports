label wednesday:
    play music "audio/home.mp3" fadein 1.5
    show text " DAY 3 - WEDNESDAY "
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
    pause 2.0
    scene black with dissolve
    pause 2.0
    scene hallway with dissolve
    " You were just entering the hallways, already on the way to go to your classroom... "
    " When suddenly, someone bumps into you. "
    " You turned around to see who bumped into you, and... "
    if oligangknow == True:
        pass
    else:
        $ oligangknow = True
        pass
    if abbiemeandefend == True:
        " Oh god, it's this guy. "
    else:
        " Huh...you feel like you've seen this guy before. "
        " Oh wait, it's that one bully. Oliver. "
    show oliverhappy at center with easeinleft
    o " Guess who's back! "
    if abbiemeandefend == True:
        hide oliverhappy at bottom
        show oliverneutral at center
        o " Oh hey, it's {i}you{/i}. "
        o " Haven't seen yer ass in a mighty long time. "
        o " You know. I didn't really appreciate what you did to me last time. "
        o " Didn't know you had the balls to wreck me like that. "
        o " But, I'll have to say... "
        o " ...You were pretty good at doing all of that. "
        o " Not that I enjoyed it or anything, ew. "
        o " But, with your skills...you'd be good enough to join my little gang. "
        o " Of course, it's not going to be as easy as you think. "
        o " You'd have to IMPRESS me first. "
        o " I know it's gonne be weird for you to join me since you beat me up after all, but hear me out. "
        o " You'd be a good addition for me. And I want someone as good as you. "
        o " I've done some thinking, and thought that you'd help me a LOT in my antics in this school. "
        o " What do you think? "
        menu:
            " I'll try to join ":
                $ oliganglv += 5
                $ oligangtry = True
                hide oliverneutral at bottom
                show oliverhappy at center
                o " Good, good... "
                o " I knew that you'd try to join me. I'm just that good, after all. "
                o " I'll see you later then...~ "
                o " Good luck trying to impress me, though. "
                hide oliverhappy at right with easeoutright
                " ...Why would you join him? I have no idea. "
                " You're the one who decided to choose this option anyway. "
                " You walk to your classroom for the first class of the day. "
                scene black with dissolve
                pause 2.0
                jump mathclass3
            " As if I would join you ":
                hide oliverneutral at bottom
                show oliverhappy at center
                o " Hah, are you sure? "
                o " If you're really sure that you're not joing to join me, well... "
                o " Soon you'll realized that deep down, you wanted to be with me and my crew. "
                o " It's inevitable, [name]. You'll realize it soon enough. "
                o " Bye for now...~ "
                hide oliverhappy at right with easeoutright
                " ...This guy makes no sense whatsoever. "
                " You ignored all of what he said, and you walked to your classroom for the first class of the day. "
                scene black with dissolve
                pause 2.0
                jump mathclass3
    elif clairebeatup == True:
        hide oliverhappy at bottom
        show oliverneutral at center
        o " Oh hey, it's {i}you{/i}. "
        o " Haven't seen yer ass in a mighty long time. "
        o " You know. I didn't really appreciate what you did to me last time. "
        o " Didn't know you had the balls to wreck me like that. "
        o " But, I'll have to say... "
        o " ...You were pretty good at doing all of that. "
        o " Not that I enjoyed it or anything, ew. "
        o " But, with your skills...you'd be good enough to join my little gang. "
        o " Of course, it's not going to be as easy as you think. "
        o " You'd have to IMPRESS me first. "
        o " I know it's gonne be weird for you to join me since you beat me up after all, but hear me out. "
        o " You'd be a good addition for me. And I want someone as good as you. "
        o " I've done some thinking, and thought that you'd help me a LOT in my antics in this school. "
        o " What do you think? "
        menu:
            " I'll try to join ":
                $ oliganglv += 5
                $ oligangtry = True
                hide oliverneutral at bottom
                show oliverhappy at center
                o " Good, good... "
                o " I knew that you'd try to join me. I'm just that good, after all. "
                o " I'll see you later then...~ "
                o " Good luck trying to impress me, though. "
                hide oliverhappy at right with easeoutright
                " ...Why would you join him? I have no idea. "
                " You're the one who decided to choose this option anyway. "
                " You walk to your classroom for the first class of the day. "
                scene black with dissolve
                pause 2.0
                jump mathclass3
            " As if I would join you ":
                hide oliverneutral at bottom
                show oliverhappy at center
                o " Hah, are you sure? "
                o " If you're really sure that you're not joing to join me, well... "
                o " Soon you'll realized that deep down, you wanted to be with me and my crew. "
                o " It's inevitable, [name]. You'll realize it soon enough. "
                o " Bye for now...~ "
                hide oliverhappy at right with easeoutright
                " ...This guy makes no sense whatsoever. "
                " You ignored all of what he said, and you walked to your classroom for the first class of the day. "
                scene black with dissolve
                pause 2.0
                jump mathclass3
    else:
        hide oliverhappy at bottom
        show oliverneutral at center
        o " Out of my way, loser. "
        o " I'm gonna have to get myself some soap once I get my hands on it... "
        hide oliverneutral at right with easeoutright
        " ...What a weird guy. "
        " You ignored all of what he said, and you walked to your classroom for the first class of the day. "
        scene black with dissolve
        pause 2.0
        jump mathclass3

label mathclass3:
    scene classroom with dissolve
    " You arrive at your classroom, already hearing whispers about the Oliver guy you saw earlier. "
    " You at down at your seat and could already hear your seatmates talking about him while the teacher's not here. "
    if claengbub == True:
        show claireconfused at left with easeinright
        show engelneutral at center with easeinright
        show bubblesad at right with easeinright
        c " Oh geez, you're telling me Oliver came back? "
        e " Mhm. "
        c " Wait, didn't Miss Grace state that he's coming back on thursday? "
        c " Did he just decide to come back early? "
        e " Apparently she made an error, and she only suspended him for 2 days. "
        b " This isn't good...not good at all!! "
        b " I don't want him to steal my rubber ducky again!! "
        hide claireconfused at bottom
        show claireneutral at left
        c " Don't worry, Bubble! "
        c " We won't let him steal your rubber ducky! "
        hide engelneutral at bottom
        show engelhappy at center
        e " Mhm, not on our watch. "
        hide bubbleneutral at bottom
        show bubbleamazed at right
        b " Wowza, thanks guys!! "
        if clairebeatup == True:
            " You stayed silent as they talked. "
            " You honestly felt kinda left out, but... "
            " ...Maybe you can apologize tommorrow. "
            " Maybe. "
        else:
            " You just chilled out as they talked. "
            " You didn't really know Oliver's bullying could get this bad. "
            " You're sure that you can probably handle him though. "
            " Probably. "
    elif abblana == True:
        show abbiesad at right with easeinleft
        show lanasad at left with easeinleft
        l " Oh geez, Oliver's back? "
        a " Oh god, I can already feel the bullying... "
        a " I was getting absolutely tormented by Zip and Edward yesterday, but... "
        a " Now that he's back, I know everything's gonna get worse from now on.. "
        hide lanasad at bottom
        show lananeutral at left
        l " Don't worry, me and [name] will protect you! "
        l " Right, [name]? "
        " You nodded your head, you were infact gonna protect Abbie from any dangers. "
        hide abbiesad at bottom
        show abbiehappy at right
        a " Oh, um... "
        a " Thanks, guys... "
    elif alone == True:
        x " Oh my god, Oliver's back? "
        x " This isn't good...he's gonna steal and hide away my rubber ducky again! "
        x " Zip and Edward were tormenting me yesterday... now I know things are just getting worse for me! "
        x " God, this is gonna be horrible... "
        " ...You're pretty sure that you can handle this. Probably. "
        " Or probably not. Whatever happens just happens."
    else:
        pass
    " After a bit, the teacher walks in. "
    " Looks like Miss Circle really recovered quick. "
    msc " Alright, class! Quiet down! "
    msc " Yes Oliver's back, yadda yadda... "
    msc " I've graded all of your activities from yesterday, so now I'll be distributing them all to you guys. "
    " Oh great, you're probably gonna get a low or high score. "
    scene black with dissolve
    " You got your paper and you got a pretty decent score. "
    " Not too bad, but not too good either. "
    " You then got to copy down some things for math class. "
    " Nothing really interesting happened as you were copying, as per usual... "
    " Can't help but feel like someone was staring directly at you though. "
    " You tried your best to just shrug it off for now. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, your first class now over. "
    " You get out of your seat and get into the hallways to take a nice, sweet break. "
    pause 2.0
    jump wedbreak1

label wedbreak1:
    scene hallway with dissolve
    " You walked into the hallway and spotted a little missing person poster... "
    " ...It was a student from this school and they were last seen last night. "
    " Creepy... you should probably be careful from now on. "
    " You don't know whether or not you're going to go missing too. "
    " And you most certainly don't want that happening. "
    " Alright...let's just go hangout somewhere. "
    " Where do you want to hangout for this break? "
    menu:
        " {image=engelicon} The front of the school {image=lanaicon} ":
            jump wedfront1
        " {image=rubyicon} The back of the school {image=bubbleicon} ":
            jump wedback1
        " {image=abbieicon} The gym {image=kevinicon} ":
            jump wedgym1
        " {image=claireicon} The cafeteria {image=skellicon} ":
            jump wedcafe1
        " {image=rileyicon} The rooftop {image=popularicon} ":
            jump wedrooftop1
        " {image=cubbieicon} The library {image=robbyicon} ":
            jump wedlibrary1

label wedfront1:
    # engel and lana talking about claire
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked onto the front of the school and spotted your two classmates talking about something. "
    " You wanted to know what they were talking about... "
    " So, you made your way to them and you listened to what they were talking about. "
    show engelneutral at right with easeinleft
    show lananeutral at left with easeinleft
    if engelknow == True and lanaknow == True:
        e " Hmm...Lana, have you noticed that Claire's been acting...off today? "
        l " Eehh? I dunno, Engel... she looks fine to me... "
        " He noticed that you were there, so he decided to ask you. "
        e " [name], have you noticed? "
        " You shrugged. You didn't really look too closely on how Claire felt. "
        e " Well... "
        e " As I was walking with Claire to school today, we spotted a missing person poster. "
        e " Not just any missing person poster, no. "
        e " But...the person that was missing was someone in this school. "
        hide lananeutral at bottom
        show lanasad at left
        l " ...! Oh... "
        e " Mhm, it's unfortunate. "
        l " I hope they're alright... "
        e " I hope so too. "
        " The both of them look at you before they look at eachother. "
        " They look like they know something that you don't... "
        " ...Wonder what that is. You're hoping they didn't do anything relating to the missing student. "
        " If they did do something horrible like that, it would suck really bad. "
        hide lanasad at bottom
        show lananeutral at left
        l " Mmm...how about we talk about something else? "
        e " Yeah, I don't really want to talk about something like this while [name] is around. "
        " While you were around? what's the problem with you around? "
        " Somethings definitely going on. "
        scene black with dissolve
        " You spent the rest of the break talking with Lana and Engel. "
        " You hoped that missing person was going to be okay and was going to be found... "
        " ...But you were also getting a bit suspicious of Lana and Engel. "
        " You knew they were hiding something, and you're probably going to find out what they're hiding. "
        " Maybe Claire knows something about this... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, it's time to go to your next class. "
        " You walked back into the school and went to your classroom for the next class. "
        pause 2.0
        jump languageclass3
    elif engelknow == True and lanaknow == False:
        e " Hmm...Lana, have you noticed that Claire's been acting...off today? "
        $ lanaknow = True
        " So Lana is that girl's name, huh? interesting. "
        l " Eehh? I dunno, Engel... she looks fine to me... "
        " He noticed that you were there, so he decided to ask you. "
        e " [name], have you noticed? "
        " You shrugged. You didn't really look too closely on how Claire felt. "
        e " Well... "
        e " As I was walking with Claire to school today, we spotted a missing person poster. "
        e " Not just any missing person poster, no. "
        e " But...the person that was missing was someone in this school. "
        hide lananeutral at bottom
        show lanasad at left
        l " ...! Oh... "
        e " Mhm, it's unfortunate. "
        l " I hope they're alright... "
        e " I hope so too. "
        " The both of them look at you before they look at eachother. "
        " They look like they know something that you don't... "
        " ...Wonder what that is. You're hoping they didn't do anything relating to the missing student. "
        " If they did do something horrible like that, it would suck really bad. "
        hide lanasad at bottom
        show lananeutral at left
        l " Mmm...how about we talk about something else? "
        e " Yeah, I don't really want to talk about something like this while [name] is around. "
        " While you were around? what's the problem with you around? "
        " Somethings definitely going on. "
        scene black with dissolve
        " You spent the rest of the break talking with Lana and Engel. "
        " You hoped that missing person was going to be okay and was going to be found... "
        " ...But you were also getting a bit suspicious of Lana and Engel. "
        " You knew they were hiding something, and you're probably going to find out what they're hiding. "
        " Maybe Claire knows something about this... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, it's time to go to your next class. "
        " You walked back into the school and went to your classroom for the next class. "
        pause 2.0
        jump languageclass3
    elif engelknow == False and lanaknow == True:
        x " Hmm...Lana, have you noticed that Claire's been acting...off today? "
        l " Eehh? I dunno, Engel... she looks fine to me... "
        $ engelknow = True
        " So Engel is that guy's name, huh? Interesting... "
        " He noticed that you were there, so he decided to ask you. "
        e " [name], have you noticed? "
        " You shrugged. You didn't really look too closely on how Claire felt. "
        e " Well... "
        e " As I was walking with Claire to school today, we spotted a missing person poster. "
        e " Not just any missing person poster, no. "
        e " But...the person that was missing was someone in this school. "
        hide lananeutral at bottom
        show lanasad at left
        l " ...! Oh... "
        e " Mhm, it's unfortunate. "
        l " I hope they're alright... "
        e " I hope so too. "
        " The both of them look at you before they look at eachother. "
        " They look like they know something that you don't... "
        " ...Wonder what that is. You're hoping they didn't do anything relating to the missing student. "
        " If they did do something horrible like that, it would suck really bad. "
        hide lanasad at bottom
        show lananeutral at left
        l " Mmm...how about we talk about something else? "
        e " Yeah, I don't really want to talk about something like this while [name] is around. "
        " While you were around? what's the problem with you around? "
        " Somethings definitely going on. "
        scene black with dissolve
        " You spent the rest of the break talking with Lana and Engel. "
        " You hoped that missing person was going to be okay and was going to be found... "
        " ...But you were also getting a bit suspicious of Lana and Engel. "
        " You knew they were hiding something, and you're probably going to find out what they're hiding. "
        " Maybe Claire knows something about this... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, it's time to go to your next class. "
        " You walked back into the school and went to your classroom for the next class. "
        pause 2.0
        jump languageclass3
    else:
        $ lanaknow = True
        x " Hmm...Lana, have you noticed that Claire's been acting...off today? "
        " Oh? Lana is that girl's name, got it... "
        l " Eehh? I dunno, Engel... she looks fine to me... "
        $ engelknow = True
        " Annnnd Engel's that guys name. got it. "
        " He noticed that you were there, so he decided to ask you. "
        e " [name], have you noticed? "
        " You shrugged. You didn't really look too closely on how Claire felt. "
        e " Well... "
        e " As I was walking with Claire to school today, we spotted a missing person poster. "
        e " Not just any missing person poster, no. "
        e " But...the person that was missing was someone in this school. "
        hide lananeutral at bottom
        show lanasad at left
        l " ...! Oh... "
        e " Mhm, it's unfortunate. "
        l " I hope they're alright... "
        e " I hope so too. "
        " The both of them look at you before they look at eachother. "
        " They look like they know something that you don't... "
        " ...Wonder what that is. You're hoping they didn't do anything relating to the missing student. "
        " If they did do something horrible like that, it would suck really bad. "
        hide lanasad at bottom
        show lananeutral at left
        l " Mmm...how about we talk about something else? "
        e " Yeah, I don't really want to talk about something like this while [name] is around. "
        " While you were around? what's the problem with you around? "
        " Somethings definitely going on. "
        scene black with dissolve
        " You spent the rest of the break talking with Lana and Engel. "
        " You hoped that missing person was going to be okay and was going to be found... "
        " ...But you were also getting a bit suspicious of Lana and Engel. "
        " You knew they were hiding something, and you're probably going to find out what they're hiding. "
        " Maybe Claire knows something about this... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, it's time to go to your next class. "
        " You walked back into the school and went to your classroom for the next class. "
        pause 2.0
        jump languageclass3

label wedback1:
    # ruby taking data of flowers, bubble trying to save a cat from a tree
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked into the back of the school and spotted two of your classmates chilling out and doing their own things. "
    " You wanted to talk to one of them...who do you talk to, though? "
    if rubyknow == True and bubbleknow == True:
        menu:
            " {image=rubyicon} Ruby {image=rubyicon} ":
                jump helloworlding
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump kitkatkitkat
    elif rubyknow == True and bubbleknow == False:
        menu:
            " {image=rubyicon} Ruby {image=rubyicon} ":
                jump helloworlding
            " {image=bubbleicon} A girl made out of bubbles {image=bubbleicon} ":
                jump kitkatkitkat
    elif rubyknow == False and bubbleknow == True:
        menu:
            " {image=rubyicon} A girl with a TV for a head {image=rubyicon} ":
                jump helloworlding
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump kitkatkitkat
    else:
        menu:
            " {image=rubyicon} A girl with a TV for a head {image=rubyicon} ":
                jump helloworlding
            " {image=bubbleicon} A girl made out of bubbles {image=bubbleicon} ":
                jump kitkatkitkat
    label helloworlding:
        # taking a data out of flowers
        " You walked up to her and checked what she was doing... "
        " ...She's been looking at that specific flower for awhile now. "
        show rubyneutral at center with easeinright
        if rubyknow == True:
            ru " Hmhmhm... "
            hide rubyneutral at bottom
            show rubyhappy at center
            ru " Oh? Hello, [name]! "
            hide rubyhappy at bottom
            show rubyneutral at center
            ru " I'm just taking data about the flowers around here. "
            ru " Been scanning around because I wanna know what kinda of flowers these areee... "
            ru " What? I should have already known these? well... "
            ru " You see! my creator kind of didn't...include SOME information into me. "
            ru " So sometimes I'd have to use my scan feature to identify things! "
            ru " How my scan feature works is that my screen takes a photo of what's infront of me... "
            ru " ...And it asks the internet about what it is! "
            ru " Theeeen...I use that information and put it in my data folder? "
            ru " Isn't that pretty cool? "
            ru " Though, it CAN get a little tiring scanning everything around... "
            " You gave her an idea to just get a whole bunch of flowers and put them up to her face. "
            ru " Oooh, sure!! "
            ru " Though I can't just GRAB the flowers. "
            ru " Rather - I'd have to take a photo of all of them being NEAR into eachother. "
            ru " I don't just wanna pull out someone's hard work! "
            ru " Let me see here... "
            " She tries to find a spot with a lot of different flowers with it... "
            " Took her a few minutes, but she eventually found a spot and scanned it. "
            " ... "
            " ...Her screen's been black for about 5 minutes now. "
            " Seems like you've actually managed to get her to crash. "
            " You're gonna have to wait this one out. You know, waiting for her to be back to normal... "
            " You're starting to wonder if she's gonna take up until the school bell rings... "
            " ...Or it'll take her a few hours. You'll find out though."
            scene black with dissolve
            " You spent the rest of the break waiting for Ruby to wake up from her crashing. "
            " While you were waiting, you took a look at the flowers she was looking at. "
            " They were some pretty flowers, that's for sure. "
            " You wondered who decided to plant these... "
            " Or they could've just been there originally in the first place. "
            " You don't know, no one really knows unless if they asked someone or something. "
            " But flowers are kinda just a really small detail that no one really notices. "
            " Sooo...might be heard to get a proper response from anyone. "
            play sound "audio/bellring.mp3"
            " The bell eventually rings, waking Ruby up, surprisingly. "
            " You eventually walked back inside of the school to go to your next class. "
            " You don't want to be late now, would you? "
            pause 2.0
            jump languageclass3
        else:
            x " Hmhmhm... "
            hide rubyneutral at bottom
            show rubyhappy at center
            x " Oh? Hello, [name]! "
            hide rubyhappy at bottom
            show rubyneutral at center
            $ rubyknow = True
            ru " I don't think I've gotten to introduce myself...I'm Ruby! "
            ru " I'm quite sure that we're classmates, are we not? "
            ru " Anyway... "
            ru " I'm just taking data about the flowers around here. "
            ru " Been scanning around because I wanna know what kinda of flowers these areee... "
            ru " What? I should have already known these? well... "
            ru " You see! my creator kind of didn't...include SOME information into me. "
            ru " So sometimes I'd have to use my scan feature to identify things! "
            ru " How my scan feature works is that my screen takes a photo of what's infront of me... "
            ru " ...And it asks the internet about what it is! "
            ru " Theeeen...I use that information and put it in my data folder? "
            ru " Isn't that pretty cool? "
            ru " Though, it CAN get a little tiring scanning everything around... "
            " You gave her an idea to just get a whole bunch of flowers and put them up to her face. "
            ru " Oooh, sure!! "
            ru " Though I can't just GRAB the flowers. "
            ru " Rather - I'd have to take a photo of all of them being NEAR into eachother. "
            ru " I don't just wanna pull out someone's hard work! "
            ru " Let me see here... "
            " She tries to find a spot with a lot of different flowers with it... "
            " Took her a few minutes, but she eventually found a spot and scanned it. "
            " ... "
            " ...Her screen's been black for about 5 minutes now. "
            " Seems like you've actually managed to get her to crash. "
            " You're gonna have to wait this one out. You know, waiting for her to be back to normal... "
            " You're starting to wonder if she's gonna take up until the school bell rings... "
            " ...Or it'll take her a few hours. You'll find out though."
            scene black with dissolve
            " You spent the rest of the break waiting for Ruby to wake up from her crashing. "
            " While you were waiting, you took a look at the flowers she was looking at. "
            " They were some pretty flowers, that's for sure. "
            " You wondered who decided to plant these... "
            " Or they could've just been there originally in the first place. "
            " You don't know, no one really knows unless if they asked someone or something. "
            " But flowers are kinda just a really small detail that no one really notices. "
            " Sooo...might be heard to get a proper response from anyone. "
            play sound "audio/bellring.mp3"
            " The bell eventually rings, waking Ruby up, surprisingly. "
            " You eventually walked back inside of the school to go to your next class. "
            " You don't want to be late now, would you? "
            pause 2.0
            jump languageclass3
    label kitkatkitkat:
        # trying to help a cat get down from a tree
        " You walked up to her and checked what she was doing - "
        " Wait, is that a cat stuck on a tree branch? "
        show bubblesad at center with easeinleft
        if bubbleknow == True:
            b " Oh no...!! "
            b " Don't worry, kitty! I'll somehow save you... "
            " She tried to reach up to get to the little cat, but she couldn't reach up high. "
            " ...Due to how short she was, of course. Looks like she needed help. "
            b " Dang it! Can't...reach..!! "
            b " Curse my height... "
            b " ...That poor kitty looks so scared... "
            b " Wonder where it's mom went... "
            " You're thinking about helping her...should you? "
            menu:
                " Help her out ":
                    $ bubblelv += 5
                    " You walked near her and then you offered to let her up so that she could reach the kitty. "
                    " You wanted to help her, after all. "
                    hide bubblesad at bottom
                    show bubbleneutral at center
                    b " Oh, [name]!! didn't even notice that you were there, sorry.. "
                    hide bubbleneutral at bottom
                    show bubblehappy at center
                    b " But, you're here to help, right? "
                    b " Thanks for deciding to come by!! I noticed this little cat on this branch not too long ago... "
                    b " It looked like it wanted to get down, but I don't think it can... "
                    hide bubblehappy at bottom
                    show bubbleneutral at center
                    b " Uh - enough of the rambling, you wanted to help me up, right? "
                    b " Lifting me up...? so, uh...like... "
                    " She was waiting for you to do something to help her get the cat. "
                    " You got into a position where you could safely lift her up and get that cat down. "
                    b " Alright, let me just... "
                    b " Cmere kitty...I'm safe, don't worry... "
                    " As she was trying to convince the cat to go to her, you looked away from where she was... "
                    " ...So that you couldn't see something that you didn't want to, of course. "
                    " It would also be really rude for you. "
                    if they == "he":
                        " Especially since you're a guy and all. "
                    else:
                        pass
                    b " Alright, [name]! "
                    b " I got the cat, you can put me down now!! "
                    " You slowly and safely put her down and looked at the cat that was now in her arms. "
                    hide bubbleneutral at bottom
                    show bubblehappy at center
                    b " Awww...look at it! "
                    b " Isn't it so cute, [name] - "
                    hide bubblehappy at bottom
                    show bubbleneutral at center
                    " ...The cat jumped out of her arms after being in there for a few moments. "
                    " The little guy really just said: 'thanks, bye'... "
                    b " ...Hm...guess it's got places to be, then! "
                    b " Though I do wish that I could've held it for a bit longer, hah... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Bubble. "
                    " She kept talking about how cute that cat was and how she found it up there. "
                    " ...Now you want to grab the kitty back and pet it too. "
                    " Too bad it's probably ran off to somewhere faraway now. "
                    " Oh well...things happen. Let's just let it be free. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You eventually walked back inside of the school to go to your next class. "
                    " You don't want to be late now, would you? "
                    pause 2.0
                    jump languageclass3
                    pause 2.0
                    jump languageclass3
                " Nah, not my problem ":
                    " You decided to just let her ask someone else. "
                    " Not helping at all...wow, you're such a good classmate! "
                    " Totally. For sure. "
                    scene black with dissolve
                    " You sat down somewhere and watched her try to get someone to help. "
                    " She didn't really find anyone though, and left sadly. "
                    " ...The cat just casually jumped off and left the tree the moment she went back into the school. "
                    " Looks like that thing wasn't scared after all. "
                    " Sometimes, some people don't really need help even though they don't think they need it. "
                    " Excluding if they're going through mental problems of course. "
                    " Try to get them some help. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You eventually walked back inside of the school to go to your next class. "
                    " You don't want to be late now, would you? "
                    pause 2.0
                    jump languageclass3
        else:
            x " Oh no...!! "
            x " Don't worry, kitty! I'll somehow save you... "
            " She tried to reach up to get to the little cat, but she couldn't reach up high. "
            " ...Due to how short she was, of course. Looks like she needed help. "
            x " Dang it! Can't...reach..!! "
            x " Curse my height... "
            x " ...That poor kitty looks so scared... "
            x " Wonder where it's mom went... "
            " You're thinking about helping her...should you? "
            menu:
                " Help her out ":
                    $ bubblelv += 5
                    " You walked near her and then you offered to let her up so that she could reach the kitty. "
                    " You wanted to help her, after all. "
                    hide bubblesad at bottom
                    show bubbleneutral at center
                    x " Oh, [name]!! didn't even notice that you were there, sorry.. "
                    hide bubbleneutral at bottom
                    show bubblehappy at center
                    $ bubbleknow = True
                    b " I'm Bubble, by the way! we're classmates, if I recall correctly. "
                    b " But, you're here to help, right? "
                    b " Thanks for deciding to come by!! I noticed this little cat on this branch not too long ago... "
                    b " It looked like it wanted to get down, but I don't think it can... "
                    hide bubblehappy at bottom
                    show bubbleneutral at center
                    b " Uh - enough of the rambling, you wanted to help me up, right? "
                    b " Lifting me up...? so, uh...like... "
                    " She was waiting for you to do something to help her get the cat. "
                    " You got into a position where you could safely lift her up and get that cat down. "
                    b " Alright, let me just... "
                    b " Cmere kitty...I'm safe, don't worry... "
                    " As she was trying to convince the cat to go to her, you looked away from where she was... "
                    " ...So that you couldn't see something that you didn't want to, of course. "
                    " It would also be really rude for you. "
                    if they == "he":
                        " Especially since you're a guy and all. "
                    else:
                        pass
                    b " Alright, [name]! "
                    b " I got the cat, you can put me down now!! "
                    " You slowly and safely put her down and looked at the cat that was now in her arms. "
                    hide bubbleneutral at bottom
                    show bubblehappy at center
                    b " Awww...look at it! "
                    b " Isn't it so cute, [name] - "
                    hide bubblehappy at bottom
                    show bubbleneutral at center
                    " ...The cat jumped out of her arms after being in there for a few moments. "
                    " The little guy really just said: 'thanks, bye'... "
                    b " ...Hm...guess it's got places to be, then! "
                    b " Though I do wish that I could've held it for a bit longer, hah... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Bubble. "
                    " She kept talking about how cute that cat was and how she found it up there. "
                    " ...Now you want to grab the kitty back and pet it too. "
                    " Too bad it's probably ran off to somewhere faraway now. "
                    " Oh well...things happen. Let's just let it be free. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You eventually walked back inside of the school to go to your next class. "
                    " You don't want to be late now, would you? "
                    pause 2.0
                    jump languageclass3
                    pause 2.0
                    jump languageclass3
                " Nah, not my problem ":
                    " You decided to just let her ask someone else. "
                    " Not helping at all...wow, you're such a good classmate! "
                    " Totally. For sure. "
                    scene black with dissolve
                    " You sat down somewhere and watched her try to get someone to help. "
                    " She didn't really find anyone though, and left sadly. "
                    " ...The cat just casually jumped off and left the tree the moment she went back into the school. "
                    " Looks like that thing wasn't scared after all. "
                    " Sometimes, some people don't really need help even though they don't think they need it. "
                    " Excluding if they're going through mental problems of course. "
                    " Try to get them some help. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You eventually walked back inside of the school to go to your next class. "
                    " You don't want to be late now, would you? "
                    pause 2.0
                    jump languageclass3

label wedgym1:
    # abbie dreading oliver's return // kevin having trouble with oliver misplacing his things
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym and spotted two of your classmates seemingly struggling with things. "
    " You wanted to talk to one of them and help them out... "
    " Who do you want to help for today's break? "
    if abbieknow == True and kevinknow == True:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump shyboyshyboy
            " {image=kevinicon} Kevin {image=kevinicon} ":
                jump nerdboynerdboy
    elif abbieknow == True and kevinknow == False:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump shyboyshyboy
            " {image=kevinicon} A nerd looking boy {image=kevinicon} ":
                jump nerdboynerdboy
    elif abbieknow == False and kevinknow == True:
        menu:
            " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                jump shyboyshyboy
            " {image=kevinicon} Kevin {image=kevinicon} ":
                jump nerdboynerdboy
    else:
        menu:
            " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                jump shyboyshyboy
            " {image=kevinicon} A nerd looking boy {image=kevinicon} ":
                jump nerdboynerdboy
    label shyboyshyboy:
        " You walked up to him and find himself curled up into a ball... "
        " Poor guy...let's see how you can help him. "
        " You sat down next to him and put a hand on his shoulder before you asked if he was alright. "
        show abbiesad at center with easeinbottom
        if abbieknow == True:
            a " Ehhh..? "
            a " I'm fine, [name]... "
            a " Just... "
            a " Worried about what Oliver's going to do to me... "
            a " Look at how Kevin's struggling... "
            a " I saw Oliver come in here and he stole Kevin's glasses and put it in the trash can... "
            a " He didn't do anything to {i}me{/i}, but he looked AT me... "
            a " I know that he'll do something to me and I'm very scared of what he's planning... "
            a " I don't wanna get hurt... "
            if abbieteach == True:
                " You reminded him that you were gonna teach him how to fight back later. "
                " Once school was over, of course. "
                " Somehow you managed to not forget. Your memoryis being good on you for once. "
                hide abbiesad at bottom
                show abbiehappy at center
                a " O-oh...right, sorry... "
                a " I'm excited to start learning from you, though...! "
                a " I'm just really tired of them picking on me so much... "
                a " ...Feels like I have to...change for the better...or whatever they say...and just... "
                a " ...Show them that I'm strong. "
                " You seemed very happy that Abbie said all of those words. "
                hide abbiehappy at bottom
                show abbieneutral at center
                " Though, looks like you stared too much and he got embarrassed of what he said. "
                " Maybe you shouldn't do that??? or uh...yeah, I don't know. "
                a " Uh...anyway... "
                a " Oliver stealing Kevin's glasses and misplacing them isn't the worst he's done... "
                a " Would you, uh... "
                a " ...Like to hear about a few things that he did...? "
                " Well, you had nothing else to do. "
                " You could try helping that Kevin guy, but you didn't really feel like it. "
                " Besides, he's just gonna find it in the end. "
                a " Alright... "
                scene black with dissolve
                " You spent the rest of the break listening to Abbie talking about things that Oliver did. "
                " And jeez, he was right. "
                " Compared to Kevin losing his glasses and all, the other stuff he did was way worse. "
                " You feel like this is just the start of something horrible bound to happen. "
                play sound "audio/bellring.mp3"
                " The bell rings. Time for another class. "
                " You walked all the way back to your classroom for the next class. "
                pause 2.0
                jump languageclass3
            else:
                " You told him that it was okay to be scared... "
                " ...You were just gonna beat the hell out of Oliver and his gang. "
                hide abbieneutral at bottom
                show abbiehappy at center
                a " ...Thanks, [name]... "
                a " That actually makes me feel a lot better, haha... "
                a " I'm just really tired of them picking on me so much... "
                a " ...Feels like I have to...change for the better...or whatever they say...and just... "
                a " ...Show them that I'm strong. "
                " You kind of just stared at Abbie for a bit. "
                " You didn't know why, you just did...??? "
                " Not like you were making fun of him or anything. "
                " You would never make fun of someone like him. "
                hide abbiehappy at bottom
                show abbieneutral at center
                " Though, looks like you stared too much and he got embarrassed of what he said. "
                " Maybe you shouldn't do that??? or uh...yeah, I don't know. "
                a " Uh...anyway... "
                a " Oliver stealing Kevin's glasses and misplacing them isn't the worst he's done... "
                a " Would you, uh... "
                a " ...Like to hear about a few things that he did...? "
                " Well, you had nothing else to do. "
                " You could try helping that Kevin guy, but you didn't really feel like it. "
                " Besides, he's just gonna find it in the end. "
                a " Alright... "
                scene black with dissolve
                " You spent the rest of the break listening to Abbie talking about things that Oliver did. "
                " And jeez, he was right. "
                " Compared to Kevin losing his glasses and all, the other stuff he did was way worse. "
                " You feel like this is just the start of something horrible bound to happen. "
                play sound "audio/bellring.mp3"
                " The bell rings. Time for another class. "
                " You walked all the way back to your classroom for the next class. "
                pause 2.0
                jump languageclass3
        else:
            x " Ehhh..? "
            x " Oh...it's you... "
            x " Um...I don't think I got to introduce myself to you before... "
            $ abbieknow = True
            a " I'm Abbie...we're classmates, and...You shouldn't worry about me too much... "
            a " I'm fine, [name]... "
            a " Just... "
            a " Worried about what Oliver's going to do to me... "
            a " Look at how Kevin's struggling... "
            a " I saw Oliver come in here and he stole Kevin's glasses and put it in the trash can... "
            a " He didn't do anything to {i}me{/i}, but he looked AT me... "
            a " I know that he'll do something to me and I'm very scared of what he's planning... "
            a " I don't wanna get hurt... "
            if abbieteach == True:
                " You reminded him that you were gonna teach him how to fight back later. "
                " Once school was over, of course. "
                " Somehow you managed to not forget. Your memoryis being good on you for once. "
                hide abbiesad at bottom
                show abbiehappy at center
                a " O-oh...right, sorry... "
                a " I'm excited to start learning from you, though...! "
                a " I'm just really tired of them picking on me so much... "
                a " ...Feels like I have to...change for the better...or whatever they say...and just... "
                a " ...Show them that I'm strong. "
                " You seemed very happy that Abbie said all of those words. "
                hide abbiehappy at bottom
                show abbieneutral at center
                " Though, looks like you stared too much and he got embarrassed of what he said. "
                " Maybe you shouldn't do that??? or uh...yeah, I don't know. "
                a " Uh...anyway... "
                a " Oliver stealing Kevin's glasses and misplacing them isn't the worst he's done... "
                a " Would you, uh... "
                a " ...Like to hear about a few things that he did...? "
                " Well, you had nothing else to do. "
                " You could try helping that Kevin guy, but you didn't really feel like it. "
                " Besides, he's just gonna find it in the end. "
                a " Alright... "
                scene black with dissolve
                " You spent the rest of the break listening to Abbie talking about things that Oliver did. "
                " And jeez, he was right. "
                " Compared to Kevin losing his glasses and all, the other stuff he did was way worse. "
                " You feel like this is just the start of something horrible bound to happen. "
                play sound "audio/bellring.mp3"
                " The bell rings. Time for another class. "
                " You walked all the way back to your classroom for the next class. "
                pause 2.0
                jump languageclass3
            else:
                " You told him that it was okay to be scared... "
                " ...You were just gonna beat the hell out of Oliver and his gang. "
                hide abbieneutral at bottom
                show abbiehappy at center
                a " ...Thanks, [name]... "
                a " That actually makes me feel a lot better, haha... "
                a " I'm just really tired of them picking on me so much... "
                a " ...Feels like I have to...change for the better...or whatever they say...and just... "
                a " ...Show them that I'm strong. "
                " You kind of just stared at Abbie for a bit. "
                " You didn't know why, you just did...??? "
                " Not like you were making fun of him or anything. "
                " You would never make fun of someone like him. "
                hide abbiehappy at bottom
                show abbieneutral at center
                " Though, looks like you stared too much and he got embarrassed of what he said. "
                " Maybe you shouldn't do that??? or uh...yeah, I don't know. "
                a " Uh...anyway... "
                a " Oliver stealing Kevin's glasses and misplacing them isn't the worst he's done... "
                a " Would you, uh... "
                a " ...Like to hear about a few things that he did...? "
                " Well, you had nothing else to do. "
                " You could try helping that Kevin guy, but you didn't really feel like it. "
                " Besides, he's just gonna find it in the end. "
                a " Alright... "
                scene black with dissolve
                " You spent the rest of the break listening to Abbie talking about things that Oliver did. "
                " And jeez, he was right. "
                " Compared to Kevin losing his glasses and all, the other stuff he did was way worse. "
                " You feel like this is just the start of something horrible bound to happen. "
                play sound "audio/bellring.mp3"
                " The bell rings. Time for another class. "
                " You walked all the way back to your classroom for the next class. "
                pause 2.0
                jump languageclass3
    label nerdboynerdboy:
        " You walked up to him and it looks like he's trying to find something... "
        " Perhaps he has glasses? "
        " Maybe you could look around for his glasses to try and help him out... "
        " Then again, you don't know what's actually wrong, so you're gonna have to ask him what he's missing. "
        " You poked his shoulder to get his attention and asked him what he was looking for. "
        show kevinneutral at center with easeinbottom
        " ...I know his glasses are right there on his face, but for this conversation, just pretend that it's not there. "
        " For the sake of this game's logic. And for the sake of my sprite artist. "
        if kevinknow == True:
            " You walked over and asked him what's wrong. "
            kv " Ah, [name]. Glad to have you here. "
            kv " You see, I was reading my book as per usual... "
            kv " Nothing out of the ordinary, right? "
            hide kevinneutral at bottom
            show kevinangry at center
            kv " Well, as I was reading, Oliver snuck up behind me and threw my glasses away. "
            kv " Obviously I tried to take them back, but I was too late and I heard him throw the glasses away somewhere else. "
            hide kevinangry at bottom
            show kevinneutral at center
            kv " Then I heard him leave... "
            kv " I honestly thought that finding my glasses would be easy, but... "
            kv " I've been at this for a few minutes now. "
            kv " And I hate to say this, but I require your assistance, [name]. "
            " Hmmm...should you help him out? "
            menu:
                " Help him out ":
                    $ kevinlv += 5
                    " You told him that you wanted to help him out. "
                    hide kevinneutral at bottom
                    show kevinhappy at center
                    kv " Thank you, [name]! "
                    kv " I appreciate your help! "
                    scene black with dissolve
                    " You spent the rest of the break helping Kevin find his glasses. "
                    " Eventually, you found it in one of the trash cans. "
                    " You cleaned it up a bit before giving it to Kevin, who seemed to be really grateful. "
                    " He gave you 69$ as a reward! Nice! "
                    " Though you can't really do anything with this. "
                    " Atleast you get free useless money though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for another class. "
                    " You walked all the way back to your classroom for the next class. "
                    pause 2.0
                    jump languageclass3
                " Actually I'm busy ":
                    kv " Ah...it's fine. "
                    kv " I could probably find my glasses on my own anyway. "
                    scene black with dissolve
                    " You sat back and watched Kevin attempt to find his glasses. "
                    " He just looked around...occasionally tripping here and there... "
                    " Don't worry, he'll probably find his glasses once the bell rings. "
                    play sound "audio/bellring.mp3"
                    " ...The bell rnag after a few mintues of watching Kevin. "
                    " He still hasn't found his glasses... "
                    " You looked around and spotted his glasses in the trash can. "
                    if kind == True:
                        " You gave him back his glasses because you felt pretty bad. "
                    elif calm == True:
                        " You gave him back his glasses because you felt pretty bad. "
                    elif mean == True:
                        " You didn't give him back his glasses because you didn't really care about him. "
                    else:
                        " You gave him back his glasses because you felt pretty bad. "
                    " You then walked all the way back to your classroom for the next class. "
                    pause 2.0
                    jump languageclass3
        else:
            " You walked over and asked him what's wrong. "
            x " Hm? I haven't heard of this voice before... "
            x " You must be... "
            x " Ah, [name]. Glad to have you here. "
            $ kevinknow = True
            kv " I'm Kevin. We're classmates. You see...I'm in a bit of trouble. "
            kv " You see, I was reading my book as per usual... "
            kv " Nothing out of the ordinary, right? "
            hide kevinneutral at bottom
            show kevinangry at center
            kv " Well, as I was reading, Oliver snuck up behind me and threw my glasses away. "
            kv " Obviously I tried to take them back, but I was too late and I heard him throw the glasses away somewhere else. "
            hide kevinangry at bottom
            show kevinneutral at center
            kv " Then I heard him leave... "
            kv " I honestly thought that finding my glasses would be easy, but... "
            kv " I've been at this for a few minutes now. "
            kv " And I hate to say this, but I require your assistance, [name]. "
            " Hmmm...should you help him out? "
            menu:
                " Help him out ":
                    $ kevinlv += 5
                    " You told him that you wanted to help him out. "
                    hide kevinneutral at bottom
                    show kevinhappy at center
                    kv " Thank you, [name]! "
                    kv " I appreciate your help! "
                    scene black with dissolve
                    " You spent the rest of the break helping Kevin find his glasses. "
                    " Eventually, you found it in one of the trash cans. "
                    " You cleaned it up a bit before giving it to Kevin, who seemed to be really grateful. "
                    " He gave you 69$ as a reward! Nice! "
                    " Though you can't really do anything with this. "
                    " Atleast you get free useless money though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Time for another class. "
                    " You walked all the way back to your classroom for the next class. "
                    pause 2.0
                    jump languageclass3
                " Actually I'm busy ":
                    kv " Ah...it's fine. "
                    kv " I could probably find my glasses on my own anyway. "
                    scene black with dissolve
                    " You sat back and watched Kevin attempt to find his glasses. "
                    " He just looked around...occasionally tripping here and there... "
                    " Don't worry, he'll probably find his glasses once the bell rings. "
                    play sound "audio/bellring.mp3"
                    " ...The bell rnag after a few mintues of watching Kevin. "
                    " He still hasn't found his glasses... "
                    " You looked around and spotted his glasses in the trash can. "
                    if kind == True:
                        " You gave him back his glasses because you felt pretty bad. "
                    elif calm == True:
                        " You gave him back his glasses because you felt pretty bad. "
                    elif mean == True:
                        " You didn't give him back his glasses because you didn't really care about him. "
                    else:
                        " You gave him back his glasses because you felt pretty bad. "
                    " You then walked all the way back to your classroom for the next class. "
                    pause 2.0
                    jump languageclass3

label wedcafe1:
    # claire isn't doing okay // skell worrying about Riley since Oliver's back
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria spotted two of your classmates... "
    " ...Let's just say that they're not doing too okay. "
    " You wanted to talk to one of them and make them feel better though... "
    " Who do you talk to? "
    if claireknow == True and skellknow == True:
        menu:
            " {image=claireicon} Claire {image=claireicon} ":
                jump claclaclacla
            " {image=skellicon} Skell {image=skellicon} ":
                jump skeskeskeske
    elif claireknow == True and skellknow == False:
        menu:
            " {image=claireicon} Claire {image=claireicon} ":
                jump claclaclacla
            " {image=skellicon} A emo guy {image=skellicon} ":
                jump skeskeskeske
    elif claireknow == False and skellknow == True:
        menu:
            " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                jump claclaclacla
            " {image=skellicon} Skell {image=skellicon} ":
                jump skeskeskeske
    else:
        menu:
            " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                jump claclaclacla
            " {image=skellicon} A emo guy {image=skellicon} ":
                jump skeskeskeske
    label claclaclacla:
        if clairebeatup == True:
            " ... "
            " ...She doesn't seem alright. "
            " Maybe you could comfort her, but... "
            " Now's not the right time, sorry. "
            " Have to send you to somewhere else... "
            stop music
            scene black
            play music "audio/paperhigh.mp3"
            jump languageclass3
        else:
            pass
        " You walked up to her and sat down next to her. "
        " You wonder what's wrong... "
        show clairesad at center with easeinleft
        if claireknow == True:
            " You poke her shoulder to get her attention. "
            hide clairesad at bottom
            show clairescared at center
            " She seemed to not notice that you sat down next to her and got spooked. "
            c " eek! "
            " Though, when she noticed that it was just you, she calmed down. "
            hide clairescared at bottom
            show claireneutral at center
            c " Oh, [name]... "
            c " You scared me there for a bit, haha! "
            c " Did you have something to say to me? "
            " You asked her if she was doing alright. "
            " You told her that you noticed that she looked a little worried... "
            " ...And that's why you decided to come up here and check on her. "
            " You just wanted to know if she was okay or not. "
            c " ... "
            " She stares at you for a bit. "
            " ...Actually, she's staring at you for more than a bit. "
            " Seems like she has a lot on her mind. "
            " She eventually responds to you though. "
            c " Eeh, how I'm feeling? "
            hide claireneutral at bottom
            show clairehappy at center
            c " Hahah, don't worry about me, [name]! "
            c " I'm doing just fine, see? "
            c " Gosh...do I really look that stressed? "
            c " Maybe I've been thinking too much about my assignments, hehah! "
            hide clairehappy at bottom
            show claireneutral at center
            c " But...yeah. I'm doing fine, [name]. "
            c " You shouldn't be worrying about me anytime soon. "
            c " You should instead just... "
            c " Look after yourself, okay? Your safety matters more than mine. "
            " ...The way she said that was kind of off. "
            " But, she looked like she didn't want to talk about a certain something right now... "
            " ...You just decided to leave her be and talked about something different. "
            scene black with dissolve
            " You spent the rest of the break talking to Claire. "
            " As you were talking to her, you can't help but feel like she was hiding something. "
            " Of course, you didn't want to ask her since she probably didn't feel like talking about what she was hiding... "
            " ...Maybe you could ask her later, if she feels better by that time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get up from where you were sitting and you walked back to your classroom for the next class. "
            pause 2.0
            jump languageclass3
        else:
            " You poke her shoulder to get her attention. "
            hide clairesad at bottom
            show clairescared at center
            " She seemed to not notice that you sat down next to her and got spooked. "
            x " eek! "
            " Though, when she noticed that it was just you, she calmed down. "
            hide clairescared at bottom
            show claireneutral at center
            x " Oh, [name]... "
            x " You scared me there for a bit, haha! "
            x " Mmm...wait, I don't think I've introduced myself to you before! "
            x " Sorry...let me do that now. "
            $ claireknow = True
            c " I'm Claire! It's nice to meet you! "
            c " Did you have something to say to me? "
            " You asked her if she was doing alright. "
            " You told her that you noticed that she looked a little worried... "
            " ...And that's why you decided to come up here and check on her. "
            " You just wanted to know if she was okay or not. "
            c " ... "
            " She stares at you for a bit. "
            " ...Actually, she's staring at you for more than a bit. "
            " Seems like she has a lot on her mind. "
            " She eventually responds to you though. "
            c " Eeh, how I'm feeling? "
            hide claireneutral at bottom
            show clairehappy at center
            c " Hahah, don't worry about me, [name]! "
            c " I'm doing just fine, see? "
            c " Gosh...do I really look that stressed? "
            c " Maybe I've been thinking too much about my assignments, hehah! "
            hide clairehappy at bottom
            show claireneutral at center
            c " But...yeah. I'm doing fine, [name]. "
            c " You shouldn't be worrying about me anytime soon. "
            c " You should instead just... "
            c " Look after yourself, okay? Your safety matters more than mine. "
            " ...The way she said that was kind of off. "
            " But, she looked like she didn't want to talk about a certain something right now... "
            " ...You just decided to leave her be and talked about something different. "
            scene black with dissolve
            " You spent the rest of the break talking to Claire. "
            " As you were talking to her, you can't help but feel like she was hiding something. "
            " Of course, you didn't want to ask her since she probably didn't feel like talking about what she was hiding... "
            " ...Maybe you could ask her later, if she feels better by that time. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get up from where you were sitting and you walked back to your classroom for the next class. "
            pause 2.0
            jump languageclass3
    label skeskeskeske:
        " You walked up to him and sat down next to him, wondering what's on his mind. "
        show skellsad at center with easeinright
        if skellknow == True:
            " You asked him why he looked so down today. "
            sk " Hi [name]. "
            sk " Erh...you know how Oliver's back? "
            sk " I'm sort of starting to get worried about how Riley would react. "
            sk " There are times where Oliver would go absent for a bit... "
            sk " ...Then he would suddenly come back, and Riley would freak out. "
            sk " Hell, she's probably freaking out right now for all I know. "
            sk " And when she's freaking out, she kind of... "
            sk " ...Does things whenever she's like that. "
            sk " Things that are very much concerning to the point I question why I'm here. "
            sk " I honestly hope she doesn't have too much of a bad reaction. "
            sk " And hopefully she doesn't do anything with that knife of hers that she always has. "
            " You reassure him that she's probably going to fine. "
            " She's also probably going to calm down back to her normal self later. "
            " Well, you're not exactly sure about that, but you hope. "
            sk " Hmhmhm... "
            hide skellsad at bottom
            show skellneutral at center
            sk " Yeah...you're probably right. "
            sk " You know, while we're here... "
            sk " You want me to tell you a few situations where she got out of hand? "
            sk " Out of hand as in she went absolutely and utterly feral. "
            sk " More feral than she usually is, you get what I'm saying? Just...feral. "
            sk " I know you probably don't have much to do, so that's why I'm asking you this. "
            sk " And also because I want to pass time to get my mind off of the situation. "
            " He was right, you had nothing to do. "
            " You told him that you wanted to hear some stories, since you were curious. "
            sk " Alright, so... "
            scene black with dissolve
            " You spent the rest of the break talking with Skell. "
            " You honestly couldn't BELIEVE some of the things Riley did for Oliver. "
            " You've seen obsessed people, but not people who were THAT obsessed to do things like that. "
            " Sometimes humans are interesting creatures. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get up from where you were sitting and you walked back to your classroom for the next class. "
            pause 2.0
            jump languageclass3
        else:
            " You asked him why he looked so down today. "
            x " Hi [name]. "
            $ skellknow = True
            sk " Before I tell you, uh...I'm Skell. Your classmate. "
            sk " Erh...you know how Oliver's back? "
            sk " I'm sort of starting to get worried about how Riley would react. "
            sk " There are times where Oliver would go absent for a bit... "
            sk " ...Then he would suddenly come back, and Riley would freak out. "
            sk " Hell, she's probably freaking out right now for all I know. "
            sk " And when she's freaking out, she kind of... "
            sk " ...Does things whenever she's like that. "
            sk " Things that are very much concerning to the point I question why I'm here. "
            sk " I honestly hope she doesn't have too much of a bad reaction. "
            sk " And hopefully she doesn't do anything with that knife of hers that she always has. "
            " You reassure him that she's probably going to fine. "
            " She's also probably going to calm down back to her normal self later. "
            " Well, you're not exactly sure about that, but you hope. "
            sk " Hmhmhm... "
            hide skellsad at bottom
            show skellneutral at center
            sk " Yeah...you're probably right. "
            sk " You know, while we're here... "
            sk " You want me to tell you a few situations where she got out of hand? "
            sk " Out of hand as in she went absolutely and utterly feral. "
            sk " More feral than she usually is, you get what I'm saying? Just...feral. "
            sk " I know you probably don't have much to do, so that's why I'm asking you this. "
            sk " And also because I want to pass time to get my mind off of the situation. "
            " He was right, you had nothing to do. "
            " You told him that you wanted to hear some stories, since you were curious. "
            sk " Alright, so... "
            scene black with dissolve
            " You spent the rest of the break talking with Skell. "
            " You honestly couldn't BELIEVE some of the things Riley did for Oliver. "
            " You've seen obsessed people, but not people who were THAT obsessed to do things like that. "
            " Sometimes humans are interesting creatures. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get up from where you were sitting and you walked back to your classroom for the next class. "
            pause 2.0
            jump languageclass3

label wedrooftop1:
    # riley freaking out about Oliver's return // popular girls being concerned about riley
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked up onto the rooftop and spotted three of your classmates just chilling and doing their own things."
    " You're thinking about talking to one of them...but who do you talk to? "
    if rileyknow == True and popularknow == True:
        menu:
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump nowworkgo
            " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                jump getajob
    elif rileyknow == True and popularknow == False:
        menu:
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump nowworkgo
            " {image=popularicon} Two worried popular girls {image=popularicon} ":
                jump getajob
    elif rileyknow == False and popularknow == True:
        menu:
            " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                jump nowworkgo
            " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                jump getajob
    else:
        menu:
            " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                jump nowworkgo
            " {image=popularicon} Two worried popular girls {image=popularicon} ":
                jump getajob
    label nowworkgo:
        $ robbrileylv += 10
        " ...Are you really sure you want to talk to this girl? "
        " Well, you made the choice to do this, so I guess so. "
        " You walked up to the insane looking girl, regretting your choices as you went up... "
        show rileyneutral at center with easeinleft
        if rileyknow == True:
            ri " Hehehh... HE'S BACK!! HE'S BACK!! "
            " She continued laughing and laughing in absolute and utter joy. "
            " ...Yeah, no. She's way too excited over this. "
            " I mean, who would be THIS excited to see a school bully come back to school? "
            " Probably those girls from those stereotypical highschool shows. "
            " She stopped laughing the moment she noticed you. "
            ri " Ohoho. OHo. Hi [name]!! "
            ri " Didja want to talk to me about something? "
            ri " Well I WANNA TALK TO YOU ABOUT MY BELOVED OLIVER NOW!! "
            " Okay, maybe you shouldn't have talked to her. "
            " You're going to have to deal with a whole lot of yapping now. "
            ri " Hehh. Did you know that he came back today? "
            ri " I heard that he would be suspended for two whole days... "
            ri " ...But he came back!! JUST FOR ME!! "
            ri " This just shows how much he LOVES me, [name]!! "
            ri " CAN'T YOU SEE?! we're going to be the most popular and cutest couple in this school! "
            ri " All of the girls will be JEALOUS that I got to be with someone like him!! "
            ri " Even Petunia and Lizzy themselves!! "
            hide rileyneutral at bottom
            show rileyangry at center
            ri " I know those spoiled whores wanted him so bad... "
            ri " Of COURSE they do! Oliver's just the best, isn't he?! "
            hide rileyangry at bottom
            show rileyhappy at center
            ri " Well, too bad I got to HIM first! "
            ri " Suck on that, idiots!! "
            ri " I don't care what anyone says about me anymore.. "
            ri " I'm insane? I could be, but all that matters is my sweet, sweet Oliver! "
            ri " I would be NOTHING without him! NOTHING!!! "
            hide rileyhappy at bottom
            show rileyneutral at center
            ri " Hhehhahahh. "
            ri " Tell me, [name]!! "
            ri " How long do you think me and Oliver would last as a couple?!! "
            menu:
                " Forever (lie) ":
                    $ robbrileylv += 10
                    hide rileyneutral at bottom
                    show rileyhappy at center
                    ri " Yess...that's right!!! "
                    ri " You really DO get me, [name]!! "
                    " Even though you lied... "
                    " ..Seems like she didn't really care that you did. "
                    " What mattered was that she heard that you told her that they were going to last forever. "
                    " Even though you knew that she wouldn't even have a chance with him. "
                    ri " Hehhehahh...we should talk more!! "
                    " Please god no. "
                    scene black with dissolve
                    " You spent the rest of the break talking to Riley. "
                    " I think it was pretty obvious on what she talked about, so I'm not gonna describe everything out for you. "
                    " I mean, you can just imagine what she's talking about right now. "
                    " Like...sniffing Oliver's clothes at night or something. "
                    " You know that Riley would do much weirder things though. "
                    play sound "audio/bellring.mp3"
                    " The bell finally rang, saving you from this hell. "
                    " You walked down from the rooftop, and went to your classroom for the next class. "
                    pause 2.0
                    jump languageclass3
                " About 2 months ":
                    $ robbrileylv += 5
                    ri " No,no!! "
                    ri " You're WRONG!! "
                    ri " We're going to last FOREVER, you HEAR ME?!?! "
                    " You just sighed and lied to her that they were going to last forever. "
                    hide rileyneutral at bottom
                    show rileyhappy at center
                    ri " Yess...that's right!!! "
                    ri " You really DO get me, [name]!! "
                    " Even though you lied... "
                    " ..Seems like she didn't really care that you did. "
                    " What mattered was that she heard that you told her that they were going to last forever. "
                    " Even though you knew that she wouldn't even have a chance with him. "
                    ri " Hehhehahh...we should talk more!! "
                    " Please god no. "
                    scene black with dissolve
                    " You spent the rest of the break talking to Riley. "
                    " I think it was pretty obvious on what she talked about, so I'm not gonna describe everything out for you. "
                    " I mean, you can just imagine what she's talking about right now. "
                    " Like...sniffing Oliver's clothes at night or something. "
                    " You know that Riley would do much weirder things though. "
                    play sound "audio/bellring.mp3"
                    " The bell finally rang, saving you from this hell. "
                    " You walked down from the rooftop, and went to your classroom for the next class. "
                    pause 2.0
                    jump languageclass3
        else:
            x " Hehehh... HE'S BACK!! HE'S BACK!! "
            " She continued laughing and laughing in absolute and utter joy. "
            " ...Yeah, no. She's way too excited over this. "
            " I mean, who would be THIS excited to see a school bully come back to school? "
            " Probably those girls from those stereotypical highschool shows. "
            " She stopped laughing the moment she noticed you. "
            x " Ohoho. OHo. Hi [name]!! "
            $ rileyknow = True
            ri " I'm Riley!! Oliver's wife and girlfriend!! "
            " ...Wait what. "
            ri " Didja want to talk to me about something? "
            ri " Well I WANNA TALK TO YOU ABOUT MY BELOVED OLIVER NOW!! "
            " Okay, maybe you shouldn't have talked to her. "
            " You're going to have to deal with a whole lot of yapping now. "
            ri " Hehh. Did you know that he came back today? "
            ri " I heard that he would be suspended for two whole days... "
            ri " ...But he came back!! JUST FOR ME!! "
            ri " This just shows how much he LOVES me, [name]!! "
            ri " CAN'T YOU SEE?! we're going to be the most popular and cutest couple in this school! "
            ri " All of the girls will be JEALOUS that I got to be with someone like him!! "
            ri " Even Petunia and Lizzy themselves!! "
            hide rileyneutral at bottom
            show rileyangry at center
            ri " I know those spoiled whores wanted him so bad... "
            ri " Of COURSE they do! Oliver's just the best, isn't he?! "
            hide rileyangry at bottom
            show rileyhappy at center
            ri " Well, too bad I got to HIM first! "
            ri " Suck on that, idiots!! "
            ri " I don't care what anyone says about me anymore.. "
            ri " I'm insane? I could be, but all that matters is my sweet, sweet Oliver! "
            ri " I would be NOTHING without him! NOTHING!!! "
            hide rileyhappy at bottom
            show rileyneutral at center
            ri " Hhehhahahh. "
            ri " Tell me, [name]!! "
            ri " How long do you think me and Oliver would last as a couple?!! "
            menu:
                " Forever (lie) ":
                    $ robbrileylv += 10
                    hide rileyneutral at bottom
                    show rileyhappy at center
                    ri " Yess...that's right!!! "
                    ri " You really DO get me, [name]!! "
                    " Even though you lied... "
                    " ..Seems like she didn't really care that you did. "
                    " What mattered was that she heard that you told her that they were going to last forever. "
                    " Even though you knew that she wouldn't even have a chance with him. "
                    ri " Hehhehahh...we should talk more!! "
                    " Please god no. "
                    scene black with dissolve
                    " You spent the rest of the break talking to Riley. "
                    " I think it was pretty obvious on what she talked about, so I'm not gonna describe everything out for you. "
                    " I mean, you can just imagine what she's talking about right now. "
                    " Like...sniffing Oliver's clothes at night or something. "
                    " You know that Riley would do much weirder things though. "
                    play sound "audio/bellring.mp3"
                    " The bell finally rang, saving you from this hell. "
                    " You walked down from the rooftop, and went to your classroom for the next class. "
                    pause 2.0
                    jump languageclass3
                " About 2 months ":
                    $ robbrileylv += 5
                    ri " No,no!! "
                    ri " You're WRONG!! "
                    ri " We're going to last FOREVER, you HEAR ME?!?! "
                    " You just sighed and lied to her that they were going to last forever. "
                    hide rileyneutral at bottom
                    show rileyhappy at center
                    ri " Yess...that's right!!! "
                    ri " You really DO get me, [name]!! "
                    " Even though you lied... "
                    " ..Seems like she didn't really care that you did. "
                    " What mattered was that she heard that you told her that they were going to last forever. "
                    " Even though you knew that she wouldn't even have a chance with him. "
                    ri " Hehhehahh...we should talk more!! "
                    " Please god no. "
                    scene black with dissolve
                    " You spent the rest of the break talking to Riley. "
                    " I think it was pretty obvious on what she talked about, so I'm not gonna describe everything out for you. "
                    " I mean, you can just imagine what she's talking about right now. "
                    " Like...sniffing Oliver's clothes at night or something. "
                    " You know that Riley would do much weirder things though. "
                    play sound "audio/bellring.mp3"
                    " The bell finally rang, saving you from this hell. "
                    " You walked down from the rooftop, and went to your classroom for the next class. "
                    pause 2.0
                    jump languageclass3
    label getajob:
        " You walked up to them to see what was wrong. "
        show petuniaconfused at left with easeinright
        show lizzyconfused at right with easeinright
        if popularknow == True:
            p " ...Is that girl seriously talking to herself? "
            if rileyknow == True:
                " Looks like they were talking about Riley. "
            else:
                " Looks like they were talking about the other girl in the area. "
            lz " Mhmm...what's this about us wanting Oliver or something? "
            p " Hey, since when did we say that we want that jerk? "
            p " Doesn't the guy have a boyfriend or something? "
            hide lizzyconfused at bottom
            show lizzyneutral at right
            lz " Well, we shouldn't think about this too much. She's just weird. "
            hide petuniaconfused at bottom
            show petunianeutral at left
            p " Yeah, she's weird. Real weird. "
            " They finally noticed that you were there. "
            p " Oooh, heya [name]!! "
            lz " Hi, [name]. "
            p " You doing alright? No one hurting you or anything? "
            p " Well...me and Lizzy were just talking about that...girl over there. "
            lz " You see her? Yeah, she's always like that, weird and all. "
            lz " Would always fuss about Oliver whenever she got the chance to... "
            p " Mhm. "
            p " Though, how about we just..you know... "
            lz " Ignore her? "
            hide petunianeutral at bottom
            show petuniahappy at left
            p " Exactly what I'm thinking, Liz! "
            lz " I knew you'd say that. "
            hide petuniahappy at bottom
            show petunianeutral at left
            p " Let's just talk about...um... "
            p " Let's talk about random things!! "
            lz " That's the best you could do? "
            p " Shut up, Liz. "
            lz " Wow, alright. "
            scene black with dissolve
            " You spent the rest of the break talking with Petunia and Lizzy. "
            " ...And ignoring that girl talking to herself. "
            " Humans really are interesting creatures. Especially that one. "
            play sound "audio/bellring.mp3"
            " The bell finally rang, saving you from this hell. "
            " You walked down from the rooftop, and went to your classroom for the next class. "
            pause 2.0
            jump languageclass3
        else:
            x " ...Is that girl seriously talking to herself? "
            if rileyknow == True:
                " Looks like they were talking about Riley. "
            else:
                " Looks like they were talking about the other girl in the area. "
            x " Mhmm...what's this about us wanting Oliver or something? "
            x " Hey, since when did we say that we want that jerk? "
            x " Doesn't the guy have a boyfriend or something? "
            hide lizzyconfused at bottom
            show lizzyneutral at right
            x " Well, we shouldn't think about this too much. She's just weird. "
            hide petuniaconfused at bottom
            show petunianeutral at left
            x " Yeah, she's weird. Real weird. "
            " They finally noticed that you were there. "
            x " Oooh, heya [name]!! "
            x " Hi, [name]. "
            x " Hey, wait! We haven't introduced ourselves, right? "
            x " Yup. We probably should. "
            x " Yeahhh!! "
            $ popularknow = True
            p " I'm Petunia! And this is my best friend, Lizzy! "
            lz " We're inseperable. "
            p " Mhm! Anyway... "
            p " You doing alright? No one hurting you or anything? "
            p " Well...me and Lizzy were just talking about that...girl over there. "
            lz " You see her? Yeah, she's always like that, weird and all. "
            lz " Would always fuss about Oliver whenever she got the chance to... "
            p " Mhm. "
            p " Though, how about we just..you know... "
            lz " Ignore her? "
            hide petunianeutral at bottom
            show petuniahappy at left
            p " Exactly what I'm thinking, Liz! "
            lz " I knew you'd say that. "
            hide petuniahappy at bottom
            show petunianeutral at left
            p " Let's just talk about...um... "
            p " Let's talk about random things!! "
            lz " That's the best you could do? "
            p " Shut up, Liz. "
            lz " Wow, alright. "
            scene black with dissolve
            " You spent the rest of the break talking with Petunia and Lizzy. "
            " ...And ignoring that girl talking to herself. "
            " Humans really are interesting creatures. Especially that one. "
            play sound "audio/bellring.mp3"
            " The bell finally rang, saving you from this hell. "
            " You walked down from the rooftop, and went to your classroom for the next class. "
            pause 2.0
            jump languageclass3

label wedlibrary1:
    # cubbie getting war flashbacks // robby struggling with fixing something Oliver broke
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and spotted two of your classmates doing their things. "
    " They seemed a little tense...you wanted to know what was wrong. "
    " Who do you want to talk to for this break? "
    if cubbieknow == True and robbyknow == True:
        menu:
            " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                jump catfancat
            " {image=robbyicon} Robby {image=robbyicon} ":
                jump wrenchboywrench
    elif cubbieknow == True and robbyknow == False:
        menu:
            " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                jump catfancat
            " {image=robbyicon} A guy struggling to fix something {image=robbyicon} ":
                jump wrenchboywrench
    elif cubbieknow == False and robbyknow == True:
        menu:
            " {image=cubbieicon} A traumatized looking cat {image=cubbieicon} ":
                jump catfancat
            " {image=robbyicon} Robby {image=robbyicon} ":
                jump wrenchboywrench
    else:
        menu:
            " {image=cubbieicon} A traumatized looking cat {image=cubbieicon} ":
                jump catfancat
            " {image=robbyicon} A guy struggling to fix something {image=robbyicon} ":
                jump wrenchboywrench

    label catfancat:
        $ cubbielv += 5
        " You walked up to him and checked if he was doing alright. "
        show cubbiesad at center with easeinright
        if cubbieknow == True:
            cb " ... "
            " You asked him what was wrong. "
            cb " ... "
            " You watched him picked up a piece of paper... "
            " ...And watched him write what he wanted to say. "
            " He then eventually showed his paper to you. "
            " Apparently he just got flashbacks from what Oliver told him in the past. "
            " You asked him if he could tell you what happened... "
            " ...If he was comfortable with that, of course. "
            " It took him a bit before he started to work on another note... "
            " He showed you what he wrote after a bit and - oh. "
            " No way he actually tried doing THAT to him. "
            " You didn't like what Cubbie wrote and wanted to do something so that he could feel better. "
            " You then had an idea, and offered to get Cubbie some icecream. "
            hide cubbiesad at bottom
            show cubbieamazed at center
            cb " ...!! "
            " Cubbie seemed really excited at the mention of icecream. "
            " You should probably get him some icecream. "
            " And also one icecream for yourself. "
            " Hey, I want some icecream too...I need a break being a narrator. "
            scene black with dissolve
            " You skedaddled out of the school to go get some icecream. "
            " Then came back with two icecream cones in both of your hands. "
            " One for you, and one for Cubbie. "
            " You spent the rest of the break eating icecream with Cubbie and distracting him from the memories. "
            " You felt bad that Oliver had told him those things. "
            " What did he tell Cubbie, you wonder? "
            " I don't think you'd want to know. "
            " ...He was told that Oliver was going to be in his walls. "
            " Yep, that's literally it. He's got nightmares of it ever since he heard sounds coming from his walls... "
            " ...Even though those were probably just cats. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit. Looks like it's time for another class. "
            " You finished up your icecream, then you walked to your classroom for your next class. "
            pause 2.0
            jump languageclass3
        else:
            $ cubbieknow = True
            " You've heard of this boy beofre, now that you look at him closer... "
            " His name was Cubbie. "
            cb " ... "
            " You asked him what was wrong. "
            cb " ... "
            " You watched him picked up a piece of paper... "
            " ...And watched him write what he wanted to say. "
            " He then eventually showed his paper to you. "
            " Apparently he just got flashbacks from what Oliver told him in the past. "
            " You asked him if he could tell you what happened... "
            " ...If he was comfortable with that, of course. "
            " It took him a bit before he started to work on another note... "
            " He showed you what he wrote after a bit and - oh. "
            " No way he actually tried doing THAT to him. "
            " You didn't like what Cubbie wrote and wanted to do something so that he could feel better. "
            " You then had an idea, and offered to get Cubbie some icecream. "
            hide cubbiesad at bottom
            show cubbieamazed at center
            cb " ...!! "
            " Cubbie seemed really excited at the mention of icecream. "
            " You should probably get him some icecream. "
            " And also one icecream for yourself. "
            " Hey, I want some icecream too...I need a break being a narrator. "
            scene black with dissolve
            " You skedaddled out of the school to go get some icecream. "
            " Then came back with two icecream cones in both of your hands. "
            " One for you, and one for Cubbie. "
            " You spent the rest of the break eating icecream with Cubbie and distracting him from the memories. "
            " You felt bad that Oliver had told him those things. "
            " What did he tell Cubbie, you wonder? "
            " I don't think you'd want to know. "
            " ...He was told that Oliver was going to be in his walls. "
            " Yep, that's literally it. He's got nightmares of it ever since he heard sounds coming from his walls... "
            " ...Even though those were probably just cats. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit. Looks like it's time for another class. "
            " You finished up your icecream, then you walked to your classroom for your next class. "
            pause 2.0
            jump languageclass3
    label wrenchboywrench:
        $ robbrileylv += 5
        " You walked up to him and took a look at what he was doing... "
        " Looks like he was struggling to fix something broken. "
        " Maybe you could help in fixing, somehow? "
        show robbyangry at center with easeinleft
        if robbyknow == True:
            rb " Goddammit...he just had to break this, huh? "
            rb " Comes back for a single day and he does this shit. Just great. "
            rb " Now I have to fix all of this, and... "
            hide robbyangry at bottom
            show robbyneutral at center
            rb " Oh, uh. Hey [name]. "
            rb " I'm kind of working on something right now. "
            rb " Something that a certain someone broke. "
            hide robbyneutral at bottom
            show robbyangry at center
            rb " Take a WIIIILLDDD guess on who broke this. "
            rb " That's right, Oliver. "
            rb " You see -  this is an item that the librarian really likes. "
            rb " I know, shocker that the librarian actually exists and isn't just some fake character. "
            hide robbyangry at bottom
            show robbyneutral at center
            rb " Oliver just decided to come here...acting like he just wanted to chill for once. "
            rb " Now, if you knew Oliver then you would know that he was about to cause trouble. "
            rb " I was minding my own business, reading a book to study and all.. "
            hide robbyneutral at bottom
            show robbyangry at center
            rb " When suddenly I heard a SHATTERING sound. "
            rb " I looked around and - turns out - Oliver had AcCiDeNtAlLy broken something! "
            rb " Once I saw what it was, I immediately got mad at him! who wouldn't?! "
            rb " I started scolding him - and then he had the nerve to just... "
            rb " TO JUST EAT SOAP RIGHT IN FRONT OF ME AND SPIT ON ME AFTERWARDS!! " with vpunch
            rb " LIKE, GROSS??!?!? "
            rb " And then the librarian walked in and saw what happened. "
            rb " Right before they could get to him, he fucking ran away! "
            rb " Now I have to deal with fixing this shit! "
            rb " All I wanted was to just study, I didn't even feel like fixing anything today but this just HAD to happen. "
            rb " Goddammit...screw my life. "
            hide robbyangry at bottom
            show robbyneutral at center
            " He takes a deep breath before he starts to try and fix the item again. "
            rb " I've been at this for minutes and things just keep falling back apart. "
            rb " Don't know what I'm doing wrong, at this point... "
            " You offered to help him. "
            rb " Eh? what? "
            rb " You wanna help? "
            rb " Uh...sure, just follow what I say. "
            scene black with dissolve
            " You spent the rest of the break fixing an item with Robby. "
            " You would talk to him here and there, trying to distract him from his angry thoughts. "
            " It seemed to work pretty well as he was working much faster than before. "
            " And eventually...you two were done! "
            " Of course it wasn't perfect, but atleast it was something. "
            " You then carefully put it back on the desk where it rightfully belonged. "
            play sound "audio/bellring.mp3"
            " The bell rings. Looks like it's time for another class. "
            " You walked back to your classroom, making sure that you weren't late. "
            pause 2.0
            jump languageclass3
        else:
            x " Goddammit...he just had to break this, huh? "
            x " Comes back for a single day and he does this shit. Just great. "
            x " Now I have to fix all of this, and... "
            hide robbyangry at bottom
            show robbyneutral at center
            x " Oh, uh. Hey [name]. "
            $ robbyknow = True
            rb " I'm Robby by the way, uh... "
            rb " Sorry - just feeling really pissed off today because of what's been happening. "
            rb " I'm kind of working on something right now. "
            rb " Something that a certain someone broke. "
            hide robbyneutral at bottom
            show robbyangry at center
            rb " Take a WIIIILLDDD guess on who broke this. "
            rb " That's right, Oliver. "
            rb " You see -  this is an item that the librarian really likes. "
            rb " I know, shocker that the librarian actually exists and isn't just some fake character. "
            hide robbyangry at bottom
            show robbyneutral at center
            rb " Oliver just decided to come here...acting like he just wanted to chill for once. "
            rb " Now, if you knew Oliver then you would know that he was about to cause trouble. "
            rb " I was minding my own business, reading a book to study and all.. "
            hide robbyneutral at bottom
            show robbyangry at center
            rb " When suddenly I heard a SHATTERING sound. "
            rb " I looked around and - turns out - Oliver had AcCiDeNtAlLy broken something! "
            rb " Once I saw what it was, I immediately got mad at him! who wouldn't?! "
            rb " I started scolding him - and then he had the nerve to just... "
            rb " TO JUST EAT SOAP RIGHT IN FRONT OF ME AND SPIT ON ME AFTERWARDS!! " with vpunch
            rb " LIKE, GROSS??!?!? "
            rb " And then the librarian walked in and saw what happened. "
            rb " Right before they could get to him, he fucking ran away! "
            rb " Now I have to deal with fixing this shit! "
            rb " All I wanted was to just study, I didn't even feel like fixing anything today but this just HAD to happen. "
            rb " Goddammit...screw my life. "
            hide robbyangry at bottom
            show robbyneutral at center
            " He takes a deep breath before he starts to try and fix the item again. "
            rb " I've been at this for minutes and things just keep falling back apart. "
            rb " Don't know what I'm doing wrong, at this point... "
            " You offered to help him. "
            rb " Eh? what? "
            rb " You wanna help? "
            rb " Uh...sure, just follow what I say. "
            scene black with dissolve
            " You spent the rest of the break fixing an item with Robby. "
            " You would talk to him here and there, trying to distract him from his angry thoughts. "
            " It seemed to work pretty well as he was working much faster than before. "
            " And eventually...you two were done! "
            " Of course it wasn't perfect, but atleast it was something. "
            " You then carefully put it back on the desk where it rightfully belonged. "
            play sound "audio/bellring.mp3"
            " The bell rings. Looks like it's time for another class. "
            " You walked back to your classroom, making sure that you weren't late. "
            pause 2.0
            jump languageclass3

label languageclass3:
    scene classroom with dissolve
    " You walked into the classroom and waited for the teacher to arrive. "
    " As you sat down onto your seat, you could still feel as if someone was staring at you. "
    " It made you uncomfortable of course, but you tried your best ignoring it. "
    " God...wonder who's staring at you this intensely. "
    " Eventually the teacher comes in and the staring stops. "
    " You get ready your notebook and your pen. "
    show msthravelneutral at center with easeinright
    mst " Alright, class! "
    mst " I've got all of your grades from the test yesterday! "
    mst " All of you did great, but some of you did better. "
    hide msthravelneutral at bottom
    show msthravelhappy at center
    mst " Oliver and Engel got the highest scores in the test! "
    " Wait, what? "
    " That guy didn't even take the test...Oliver, I mean. "
    " This is honestly pretty rigged, not even going to lie here. "
    mst " All of you should've been like those two, honestly. "
    hide msthravelhappy at bottom
    show msthravelneutral at center
    mst " Anyway! Let's start our lesson for today! "
    scene black with dissolve
    " You zoned out as Miss Thavel was teaching you things about language. "
    " You could honestly care less about the lesson, something else was bugging you in your mind. "
    " How come Oliver got a high score when he wasn't even there? "
    " And why did no one even seem surprised about it? "
    " Was this something that happened often? This is really odd. "
    " You thought about it too much to the point you didn't really know what to feel. "
    play sound "audio/bellring.mp3"
    " You didn't even notice that the bell rang for a bit. "
    " You eventually realized that your classmates were leaving, and you got out of your seat... "
    " ...Going into the hallway. You just want some place to chill out your thoughts for a bit. "
    pause 2.0
    jump wedbreak2

label wedbreak2:
    scene hallway with dissolve
    " You walked into the hallway and thought of going some place in the school to calm yourself down. "
    " Where do you go? "
    if oligangtry == True:
        " Pstt, you wanna try getting into Oliver's crew, right? "
        " I'd reccomend checking the gym. He's doing some...business there. "
        " Good luck. "
        pass
    else:
        pass
    menu:
        " {image=abbieicon} The front of the school {image=rubyicon} ":
            jump wedfrontschool2
        " {image=skellicon} The back of the school {image=claireicon} ":
            jump wedbackschool2
        " {image=kevinicon} The gym {image=oligangicon} ":
            jump wedgym2
        " {image=popularicon} The cafeteria {image=engelicon} ":
            jump wedcafe2
        " {image=bubbleicon} The rooftop {image=lanaicon} ":
            jump wedrooftop2
        " {image=rileyicon} The library {image=cubbieicon} ":
            jump wedlibrary2
label wedfrontschool2:
    # abbie and ruby, both bumped into eachother and dont know whose fault it was
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school and spotted two of your classmates talking to eachother. "
    " Curious as always, you walked up to them to see what they were talking about. "
    " Even if you didn't feel like being social, I'm making you do social stuff right now. Why? I'm the narrator, duh. "
    show abbiesad at left with easeinright
    show rubysad at right with easeinright
    if abbieknow == True and rubyknow == True:
        a " I'm sorry - I didn't mean to... "
        ru " No, I'm sorry! I wasn't looking! "
        a " No, no...I was the one blocking your way... "
        ru " Nuh uh! This was completely my fault! "
        a " Noooo...don't blame yourself, it's me who didn't move out of the way... "
        " Huh...looks like they're blaming themselves into eachother. "
        " It was clearly none of their faults, though. "
        " You stopped them from worrying and told them that it was none of their faults for bumping into eachother. "
        " I mean, Abbie didn't know Ruby was behind him or in front of him, probably. "
        " Same for Ruby but opposite, or something. "
        " You then told them that you both were fine and things like these happen. "
        " It's all good, gang! "
        hide abbiesad at bottom
        show abbieneutral at left
        hide rubysad at bottom
        show rubyneutral at right
        ru " Processing... "
        ru " ...Yeah, [name] is right! "
        ru " Let's not worry about it too much since, like [they] said, stuff happens like this - okay? "
        a " Mmmm...okay... "
        a " Now I feel bad for overreacting a bit... "
        ru " Oh, no! You're all good! "
        ru " You were worried that you did something wrong and everything's okay - that doesn't mean that you have to NOT be worried or anything... "
        ru " ...But you cared enough to be worried!! So that's a good thing!! "
        a " Well, when you put it that way... "
        a " It does sound a little better... "
        a " I did panick a bit when I almost saw you fall... "
        a " I didn't want to break your screen or anything, since... "
        a " Screens like yours must've cost a lot, right...? "
        ru " Oooh, yeah...that could've been bad... "
        ru " But thankfully I'm fine, and my screen isn't cracked at all! "
        ru " Not even a bit, since I didn't fall! "
        a " Hmmm...yeah, that's good... "
        scene black with dissolve
        " You spent the rest of the break talking with Abbie and Ruby. "
        " They were actually pretty fun to talk to, though... "
        " Abbie would start worrying about things the moment Ruby mentions something surprising to him. "
        " Now that you think about it more, he was stuttering a whole lot in the conversation. "
        " You asked about it and turns out that Abbie just doesn't know how to talk to people, not just Ruby. "
        " Huh...this is probably going to be relatable to some people out there. "
        " Including me, actually. "
        play sound "audio/bellring.mp3"
        " The bell rings, looks like it's time for another class. "
        " You walked back into the school and you went to your classroom for the next class. "
        pause 2.0
        jump scienceclass3
    elif abbieknow == True and rubyknow == False:
        a " I'm sorry - I didn't mean to... "
        x " No, I'm sorry! I wasn't looking! "
        a " No, no...I was the one blocking your way... "
        x " Nuh uh! This was completely my fault! "
        a " Noooo...don't blame yourself, it's me who didn't move out of the way... "
        " Huh...looks like they're blaming themselves into eachother. "
        " It was clearly none of their faults, though. "
        " You stopped them from worrying and told them that it was none of their faults for bumping into eachother. "
        " I mean, Abbie didn't know that the girl was behind him or in front of him, probably. "
        " Same for the girl but opposite, or something. "
        " You then told them that you both were fine and things like these happen. "
        " It's all good, gang! "
        hide abbiesad at bottom
        show abbieneutral at left
        hide rubysad at bottom
        show rubyneutral at right
        x " Processing... "
        x " ...Yeah, [name] is right! "
        x " Let's not worry about it too much since, like [they] said, stuff happens like this - okay? "
        a " Mmmm...okay... "
        a " Now I feel bad for overreacting a bit... "
        x " Oh, no! You're all good! "
        x " You were worried that you did something wrong and everything's okay - that doesn't mean that you have to NOT be worried or anything... "
        x " ...But you cared enough to be worried!! So that's a good thing!! "
        a " Well, when you put it that way... "
        a " It does sound a little better... "
        a " I did panick a bit when I almost saw you fall... "
        a " I didn't want to break your screen or anything, since... "
        a " Screens like yours must've cost a lot, right...? "
        x " Oooh, yeah...that could've been bad... "
        x " But thankfully I'm fine, and my screen isn't cracked at all! "
        x " Not even a bit, since I didn't fall! "
        a " Hmmm...yeah, that's good... "
        scene black with dissolve
        " You spent the rest of the break talking with Abbie and and the TV girl. "
        " I...didn't intend to make a reference once I mentioned TV girl, but whatever, it's there now. "
        $ rubyknow = True
        " You've also learnt that the TV girl's name was Ruby, as you three talked. "
        " They were actually pretty fun to talk to, though... "
        " Abbie would start worrying about things the moment Ruby mentions something surprising to him. "
        " Now that you think about it more, he was stuttering a whole lot in the conversation. "
        " You asked about it and turns out that Abbie just doesn't know how to talk to people, not just Ruby. "
        " Huh...this is probably going to be relatable to some people out there. "
        " Including me, actually. "
        play sound "audio/bellring.mp3"
        " The bell rings, looks like it's time for another class. "
        " You walked back into the school and you went to your classroom for the next class. "
        pause 2.0
        jump scienceclass3
    elif abbieknow == False and rubyknow == True:
        x " I'm sorry - I didn't mean to... "
        ru " No, I'm sorry! I wasn't looking! "
        x " No, no...I was the one blocking your way... "
        ru " Nuh uh! This was completely my fault! "
        x " Noooo...don't blame yourself, it's me who didn't move out of the way... "
        " Huh...looks like they're blaming themselves into eachother. "
        " It was clearly none of their faults, though. "
        " You stopped them from worrying and told them that it was none of their faults for bumping into eachother. "
        " I mean, the boy didn't know Ruby was behind him or in front of him, probably. "
        " Same for Ruby but opposite, or something. "
        " You then told them that you both were fine and things like these happen. "
        " It's all good, gang! "
        hide abbiesad at bottom
        show abbieneutral at left
        hide rubysad at bottom
        show rubyneutral at right
        ru " Processing... "
        ru " ...Yeah, [name] is right! "
        ru " Let's not worry about it too much since, like [they] said, stuff happens like this - okay? "
        x " Mmmm...okay... "
        x " Now I feel bad for overreacting a bit... "
        ru " Oh, no! You're all good! "
        ru " You were worried that you did something wrong and everything's okay - that doesn't mean that you have to NOT be worried or anything... "
        ru " ...But you cared enough to be worried!! So that's a good thing!! "
        x " Well, when you put it that way... "
        x " It does sound a little better... "
        x " I did panick a bit when I almost saw you fall... "
        x " I didn't want to break your screen or anything, since... "
        x " Screens like yours must've cost a lot, right...? "
        ru " Oooh, yeah...that could've been bad... "
        ru " But thankfully I'm fine, and my screen isn't cracked at all! "
        ru " Not even a bit, since I didn't fall! "
        x " Hmmm...yeah, that's good... "
        scene black with dissolve
        " You spent the rest of the break talking with the boy and Ruby. "
        $ abbieknow = True
        " You've also learned that the boy's name was Abbie, as you three talked. "
        " They were actually pretty fun to talk to, though... "
        " Abbie would start worrying about things the moment Ruby mentions something surprising to him. "
        " Now that you think about it more, he was stuttering a whole lot in the conversation. "
        " You asked about it and turns out that Abbie just doesn't know how to talk to people, not just Ruby. "
        " Huh...this is probably going to be relatable to some people out there. "
        " Including me, actually. "
        play sound "audio/bellring.mp3"
        " The bell rings, looks like it's time for another class. "
        " You walked back into the school and you went to your classroom for the next class. "
        pause 2.0
        jump scienceclass3
    else:
        x " I'm sorry - I didn't mean to... "
        x " No, I'm sorry! I wasn't looking! "
        x " No, no...I was the one blocking your way... "
        x " Nuh uh! This was completely my fault! "
        x " Noooo...don't blame yourself, it's me who didn't move out of the way... "
        " Huh...looks like they're blaming themselves into eachother. "
        " It was clearly none of their faults, though. "
        " You stopped them from worrying and told them that it was none of their faults for bumping into eachother. "
        " I mean, The boy didn't know that the girl was behind him or in front of him, probably. "
        " Same for the girl but opposite, or something. "
        " You then told them that you both were fine and things like these happen. "
        " It's all good, gang! "
        hide abbiesad at bottom
        show abbieneutral at left
        hide rubysad at bottom
        show rubyneutral at right
        x " Processing... "
        x " ...Yeah, [name] is right! "
        x " Let's not worry about it too much since, like [they] said, stuff happens like this - okay? "
        x " Mmmm...okay... "
        x " Now I feel bad for overreacting a bit... "
        x " Oh, no! You're all good! "
        x " You were worried that you did something wrong and everything's okay - that doesn't mean that you have to NOT be worried or anything... "
        x " ...But you cared enough to be worried!! So that's a good thing!! "
        x " Well, when you put it that way... "
        x " It does sound a little better... "
        x " I did panick a bit when I almost saw you fall... "
        x " I didn't want to break your screen or anything, since... "
        x " Screens like yours must've cost a lot, right...? "
        x " Oooh, yeah...that could've been bad... "
        x " But thankfully I'm fine, and my screen isn't cracked at all! "
        x " Not even a bit, since I didn't fall! "
        x " Hmmm...yeah, that's good... "
        scene black with dissolve
        " You spent the rest of the break talking with Abbie and and the TV girl. "
        " I...didn't intend to make a reference once I mentioned TV girl, but whatever, it's there now. "
        $ rubyknow = True
        " You've also learnt that the TV girl's name was Ruby, as you three talked. "
        $ abbieknow = True
        " Oh yeah, and that the boy's name was Abbie. Pretty sweet. "
        " They were actually pretty fun to talk to, though... "
        " Abbie would start worrying about things the moment Ruby mentions something surprising to him. "
        " Now that you think about it more, he was stuttering a whole lot in the conversation. "
        " You asked about it and turns out that Abbie just doesn't know how to talk to people, not just Ruby. "
        " Huh...this is probably going to be relatable to some people out there. "
        " Including me, actually. "
        play sound "audio/bellring.mp3"
        " The bell rings, looks like it's time for another class. "
        " You walked back into the school and you went to your classroom for the next class. "
        pause 2.0
        jump scienceclass3
label wedbackschool2:
    # skell and claire - claire acting off again and skell worrying a little about claire
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and spotted your two classmates vibing. "
    " You wanted to talk to one of them, of course. But who do you talk to? "
    if skellknow == True and claireknow == True:
        menu:
            " {image=skellicon} Skell {image=skellicon} ":
                jump evilpomni
            " {image=claireicon} Claire {image=claireicon} ":
                jump evilragatha
    elif skellknow == True and claireknow == False:
        menu:
            " {image=skellicon} Skell {image=skellicon} ":
                jump evilpomni
            " {image=claireicon} A worried looking girl with a bow on her head {image=claireicon} ":
                jump evilragatha
    elif skellknow == False and claireknow == True:
        menu:
            " {image=skellicon} A emo guy {image=skellicon} ":
                jump evilpomni
            " {image=claireicon} Claire {image=claireicon} ":
                jump evilragatha
    else:
        menu:
            " {image=skellicon} A emo guy {image=skellicon} ":
                jump evilpomni
            " {image=claireicon} A worried looking girl with a bow on her head {image=claireicon} ":
                jump evilragatha
    label evilpomni:
        " You walked up to him and sat down next to him on the ground. "
        " ...He seemed a little worried. "
        show skellneutral at center with dissolve
        if skellknow == True:
            " You asked him if he was doing alright. "
            " You've always seen him in the corners of class, just hanging out and chilling...doing alright... "
            " He's always had that stoic face on as if he's not bothered by anything. "
            " So, seeing something like worry on his face is something that you should probably be concerned about. "
            sk " Eh...? Me, worried? "
            sk " Nope, not worried about anything right now. "
            sk " If I were worried about something, it would be passing my assignments last minute. "
            sk " I've had that happened to be multiple times, still freaks me out every now and then. "
            " You just stared at him, looking as if you didn't believe every single word that he said. "
            " Well, you really didn't believe him - since he looked a bit funny when you approached him. "
            " It looks like he knows that his lies won't get to you though. "
            sk " ... "
            sk " ...Alright, alright. You don't have to keep looking at me like that. "
            sk " You see...this is going to be embarrassing for me - but I've had a lot happen to me thats more embarrassing than this. "
            sk " I never really saw myself as the type to worry about others, but... "
            sk " ...You see that girl over there? the one with the bow? "
            " Skell points to the girl who seems to be a bit distressed. Wonder if she's alright... "
            " Though, you didn't really just want to...go up to her and ask if everything's fine. That would be awkward. "
            " Like, imagine a stranger walking up to you on a bad day and just asking if you're fine. "
            " That would be weird. Most of those scenarios come from animes or movies though. "
            sk " ...She's our classmate. "
            sk " Usually she'd be so happy and cheerful, but now she's just... "
            sk " ...I've honestly never seen her this worried before. "
            sk " It's concerning, since most of the time she's worried is when she forgets to do assignments or activities. "
            sk " I couldn't help but get myself just a bit worried about her. "
            sk " I wonder... "
            sk " ...What cuased her to be like this? "
            sk " Is it the fact that a student has gone missing, or.. - "
            hide skellneutral at bottom
            show skellsurprised at center
            sk " ...! "
            " He looked like he just realized something. "
            " Most likely the reason why the girl was panicking in the first place. "
            " You were about to ask him if there was something on your face, but he cuts you off. "
            hide skellsurprised at bottom
            show skellneutral at center
            sk " No, no... "
            sk " I may or may not have just figured out why she was freaking out. "
            sk " I don't think you'll like my answer, though. "
            sk " Maybe you'll figure it out later, you're smart, right? "
            " Maybe you could, with that singular braincell of yours working hard to process this. "
            " He seems like he doesn't want to talk about this right now... "
            " For now, you nodded your head and decided to talk about a different topic with him. "
            scene black with dissolve
            " You spent the rest of the break having a talk with Skell. "
            " As you were talking with him, you couldn't help but wonder why that girl over there looked so worried... "
            " ...You knew that it was probably none of your business though. "
            " Must've been some personal issues. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for class. "
            " You get up from where you were sitting, and you walked back into the school to go to your classroom. "
            pause 2.0
            jump scienceclass3
        else:
            " You asked him if he was doing alright. "
            " You've always seen him in the corners of class, just hanging out and chilling...doing alright... "
            " He's always had that stoic face on as if he's not bothered by anything. "
            " So, seeing something like worry on his face is something that you should probably be concerned about. "
            x " Eh...? Me, worried? "
            x " Nope, not worried about anything right now. "
            $ skellknow = True
            sk " I'm Skell, by the way. We're classmates, and all of that...anyway... "
            sk " If I were worried about something, it would be passing my assignments last minute. "
            sk " I've had that happened to be multiple times, still freaks me out every now and then. "
            " You just stared at him, looking as if you didn't believe every single word that he said. "
            " Well, you really didn't believe him - since he looked a bit funny when you approached him. "
            " It looks like he knows that his lies won't get to you though. "
            sk " ... "
            sk " ...Alright, alright. You don't have to keep looking at me like that. "
            sk " You see...this is going to be embarrassing for me - but I've had a lot happen to me thats more embarrassing than this. "
            sk " I never really saw myself as the type to worry about others, but... "
            sk " ...You see that girl over there? the one with the bow? "
            " Skell points to the girl who seems to be a bit distressed. Wonder if she's alright... "
            " Though, you didn't really just want to...go up to her and ask if everything's fine. That would be awkward. "
            " Like, imagine a stranger walking up to you on a bad day and just asking if you're fine. "
            " That would be weird. Most of those scenarios come from animes or movies though. "
            sk " ...She's our classmate. "
            sk " Usually she'd be so happy and cheerful, but now she's just... "
            sk " ...I've honestly never seen her this worried before. "
            sk " It's concerning, since most of the time she's worried is when she forgets to do assignments or activities. "
            sk " I couldn't help but get myself just a bit worried about her. "
            sk " I wonder... "
            sk " ...What cuased her to be like this? "
            sk " Is it the fact that a student has gone missing, or.. - "
            hide skellneutral at bottom
            show skellsurprised at center
            sk " ...! "
            " He looked like he just realized something. "
            " Most likely the reason why the girl was panicking in the first place. "
            " You were about to ask him if there was something on your face, but he cuts you off. "
            hide skellsurprised at bottom
            show skellneutral at center
            sk " No, no... "
            sk " I may or may not have just figured out why she was freaking out. "
            sk " I don't think you'll like my answer, though. "
            sk " Maybe you'll figure it out later, you're smart, right? "
            " Maybe you could, with that singular braincell of yours working hard to process this. "
            " He seems like he doesn't want to talk about this right now... "
            " For now, you nodded your head and decided to talk about a different topic with him. "
            scene black with dissolve
            " You spent the rest of the break having a talk with Skell. "
            " As you were talking with him, you couldn't help but wonder why that girl over there looked so worried... "
            " ...You knew that it was probably none of your business though. "
            " Must've been some personal issues. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for class. "
            " You get up from where you were sitting, and you walked back into the school to go to your classroom. "
            pause 2.0
            jump scienceclass3
    label evilragatha:
        " You walked up to her and sat down next to her on the ground. "
        " ...She seemed stressed out. "
        if clairebeatup == True:
            " ...Too bad you can't help with that. "
            " Sorry! script says you can't. Onto the next class! "
            scene black
            pause 1.5
            jump scienceclass3
        else:
            pass
        show clairesad at center with dissolve
        if claireknow == True:
            c " Oh geez, what am I supposed to do...? "
            c " If [they] found out, this could be really bad... "
            c " I want [them] to have a good impression on this school, but with how things are recently... "
            c " I don't think [they] [are] gonna like this a lot... "
            c " I mean, what if [they] find out and they want to leave this school already - "
            c " It's only [their] third day here, [they] could easily just - "
            hide clairesad at bottom
            show claireneutral at center
            " She stops her rambling the moment she sees you. "
            c " Oh, hey there [name]! "
            c " What I was rambling about...? "
            hide claireneutral at bottom
            show clairehappy at center
            c " Well, it's nothing you should worry about, really! "
            c " Was just worrying about a certain someone. "
            c " You know, that one missing kid? "
            hide clairehappy at bottom
            show claireneutral at center
            c " Yeah...I really hope they're alright, you know? "
            c " They said that they're still looking around for them... "
            c " Let's just pray that they're safe, okay? "
            " ... "
            " ...She sounded like she was lying about what she really felt. "
            " But, it also looked like she didn't want to talk about it. "
            " You just decided to play along for now, and talk about something else. "
            scene black with dissolve
            " You spent the rest of the break talking to Claire. "
            " You wondered what was on her mind earlier to make her so worried... "
            " ...It's probably something personal, something you shouldn't think about too much. "
            " You couldn't help but feel worried about her, though... "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for class. "
            " You walked back into the school and walked back to your classroom for the next class. "
            pause 2.0
            jump scienceclass3
        else:
            x " Oh geez, what am I supposed to do...? "
            x " If [they] found out, this could be really bad... "
            x " I want [them] to have a good impression on this school, but with how things are recently... "
            x " I don't think [they] [are] gonna like this a lot... "
            x " I mean, what if [they] find out and they want to leave this school already - "
            x " It's only [their] third day here, [they] could easily just - "
            hide clairesad at bottom
            show claireneutral at center
            " She stops her rambling the moment she sees you. "
            x " Oh, hey there [name]! "
            x " I don't think I got to introduce myself to you, no? "
            $ claireknow = True
            hide claireneutral at bottom
            show clairehappy at center
            c " I'm Claire! We're classmates! It's nice to meet you! "
            hide clairehappy at bottom
            show claireneutral at cneter
            " You told her that it was nice to meet her, but you told her that you were more interested in what she was talking about. "
            c " What I was rambling about...? "
            hide claireneutral at bottom
            show clairehappy at center
            c " Well, it's nothing you should worry about, really! "
            c " Was just worrying about a certain someone. "
            c " You know, that one missing kid? "
            hide clairehappy at bottom
            show claireneutral at center
            c " Yeah...I really hope they're alright, you know? "
            c " They said that they're still looking around for them... "
            c " Let's just pray that they're safe, okay? "
            " ... "
            " ...She sounded like she was lying about what she really felt. "
            " But, it also looked like she didn't want to talk about it. "
            " You just decided to play along for now, and talk about something else. "
            scene black with dissolve
            " You spent the rest of the break talking to Claire. "
            " You wondered what was on her mind earlier to make her so worried... "
            " ...It's probably something personal, something you shouldn't think about too much. "
            " You couldn't help but feel worried about her, though... "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for class. "
            " You walked back into the school and walked back to your classroom for the next class. "
            pause 2.0
            jump scienceclass3
label wedgym2:
    # kevin and oliver - your chance to prove yourself
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym and spotted your two classmates. "
    " Looks like that bully is here, and...wait, isn't that...? That one nerdy kid?? "
    " Huh, wonder what he's doing with him. "
    " Let's go check. "
    show kevinangry at right with easeinleft
    show oliverhappy at left with easeinleft
    if kevinknow == True and oligangknow == True:
        kv " Eheh, look, Oliver. "
        o " I'm already looking, though? "
        kv " ... "
        o " Heh. What, got you mad? "
        kv " Whatever - I don't have time for this. "
        o " Awww, you're leaving already, Kevs? "
        o " Come on, I'm just getting started! "
        kv " Getting started on what? doing your job of annoying me? "
        o " Yuuup!! "
        o " Come on, Kevs - can't you stay a little longer? "
        kv " I have work to do, Oliver. "
        o " Whaaaat? Homework? How boring, Kevin. I thought you were better than this! "
        kv " Geez, could you just get off of me?! "
        o " Nuh uh!! "
        o " Not when I'm having fun with you!! "
        kv " Good lord, have mercy... "
        " Looks like Oliver's bothering him. "
        " You feel like you should help him... "
        " Should you? "
        if oligangtry == True:
            menu:
                " Help Kevin ":
                    $ kevinlv += 10
                    hide kevinangry at bottom
                    show kevinneutral at right
                    " You walked infront of Oliver and told him to stop. "
                    " You told him that it was making the other guy uncomfortable, and that it wasn't okay. "
                    hide oliverhappy at bottom
                    show oliverneutral at left
                    o " Oooh, what's this? "
                    o " Are you really defending this nerd, [name]? "
                    o " Come on, it's completely alright for me to be bothering him! "
                    if oligangtry == True:
                        o " Besides, didn't you say that you wanted to join my crew earlier? "
                        o " What a shame...looks like you don't want to join after all! "
                        o " You would've been a great addition to my team...but if you don't want to join, then... "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " Your loss, hah! "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                    else:
                        o " You just don't know how to have fun, [name]. "
                        o " I don't really care if I get in trouble or not... "
                        o " ...Doing this stuff is what 'fun' is to me! "
                        o " You've got to live a little, [name], jeez. "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " You probably don't know how to do that, though. Considering how you are! "
                        o " All flesh and bones, with thoughts and all of that... only to end up being used as a puppet for some sick game! "
                        " ...Okay, what nonsense was he on about? "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                        o " All of your actions are being controlled by someone, silly. "
                        o " You just can't bring yourself to believe that fact! "
                    o " Anyway, I'm outta here. "
                    o " Later, losers! "
                    hide oliverneutral at right with easeoutright
                    show kevinneutral at center with move
                    " ...Well, guess that worked. "
                    if oligangtry == True:
                        " You could probably care less about what he said to you. "
                        " His gang stinks, anyway. "
                    else:
                        " Wonder what he was on about, though... "
                    kv " ...Ahem. "
                    kv " I'd like to thank you, [name]. "
                    kv " For helping Oliver get off of my business, to be specific. "
                    kv " I don't know how long I'd last without your help... "
                    if oligangtry == True:
                        hide kevinneutral at bottom
                        show kevinconfused at center
                        kv " I'm gonna have to ask about your questionable choice of... "
                        kv " ...Wanting to be in his group, was it? "
                        kv " Why?????????? "
                        " Oh boy, this is going to be a somewhat long explanation. "
                        " You brace yourself for the very long explanation you're about to give to Kevin... "
                    else:
                        kv " I don't know what he was going on about the whole puppet thing, though. "
                        kv " Must've been him just trying to make himself look cool... "
                        kv " ...Or for me to stir up some very wild and wacky theories. "
                        kv " I'm not that type of person, though. "
                    scene black with dissolve
                    if oligangtry == True:
                        " You spent the rest of the break explaining to Kevin on why you wanted to join Oliver in the first place. "
                        " Actually, it was more of you just saying that you were lying to Oliver about all of that... "
                        " ...Though Kevin didn't believe you with the tone you were using, apparently. "
                        " You had to tell him what happened on the very first day and everything...yada yada... "
                        " Let's just say he was flabbergasted. "
                    else:
                        " You spent the rest of the break talking with Kevin. "
                        " You two were just talking about what happened... "
                        " Kevin was explaining how he even got into that situation with Oliver. "
                        " According to him, he was just minding his business, and Oliver was just trying to find some soap. "
                        " ...In the gym?? - Anyway, There just so happened to be a bar of soap right next to Kevin, andddd...you know what happened. "
                        " Is there always some soap in the gym? "
                        " Do they have, like...a special stock of soap just for Oliver? "
                        " So many questions, but no answers. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for class. "
                    " You walked all the way to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
                " Help Oliver ":
                    $ oliganglv += 10
                    $ oligangjoin = True
                    " You sure you wanna do this? Damn, alright. "
                    " You do you, I guess. "
                    hide oliverhappy at bottom
                    show oliverneutral at left
                    " You walked infront of Kevin and stared at him for a bit. "
                    kv " ...Oh, now what do you want - {nw} "
                    hide kevinangry at bottom
                    show kevinsurprised at right
                    " You then proceeded to snatch his glasses away from him and threw it to the trash can. "
                    " Fyi the trash can was pretty far from you guys, so...pretty impressive. "
                    hide kevinsurprised at bottom
                    show kevinangry at right
                    kv " MY GLASSES!! " with vpunch
                    hide kevinangry at bottom with easeoutbottom
                    " Before he could say anything, you kicked him down onto the ground. "
                    " You then proceeded to kick him in the stomach a few times before you stopped. "
                    " You looked at the other guy that was near you and he seemed impressed with what you did. "
                    if abbiemeandefend == True:
                        " Though it did remind you of what you did to him in the past.. "
                    else:
                        pass
                    hide oliverneutral at bottom
                    show oliverhappy at left
                    show oliverhappy at center with move
                    o " Oooh, nice one, [name]! "
                    o " I like your style there...how about we force feed him some soap? "
                    o " Hah, good idea, right? "
                    hide oliverhappy at bottom
                    show oliverneutral at center
                    o " ...Unfortunately there's a security camera here, so we can't do anything too bad. "
                    o " Miss Grace would've killed us if we went too far. "
                    o " For now, let's leave Kevin alone, yeah? Looks like we've done enough for now! "
                    o " Hope he's gonna have a fun time finding his glasses, hehe. "
                    o " Let's go into the hallways, alright? "
                    o " Don't want someone to tell the teachers now, would we? "
                    o " I'd rather NOT get caught after having fun like this. "
                    o " Come on, let's go, [name]. "
                    hide oliverneutral at right with easeoutright
                    scene black with dissolve
                    " You followed Oliver into the hallway. "
                    pause 1.0
                    scene hallway with dissolve
                    show oliverneutral at center with easeinleft
                    o " Ahhh, it's surprisingly quiet here. Good. "
                    hide oliverneutral at bottom
                    show oliverhappy at center
                    o " Though, someone might be listening in. We wouldn't really want that now, would we? "
                    hide oliverhappy at bottom
                    show oliverneutral at center
                    o " Let's just talk really, really quietly then. "
                    o " So... "
                    o " I know that I've said that it's going to take a LOT to impress me, but... "
                    o " With what you did to Kevin, it kind of just...I dunno... "
                    o " Let's say: made me think that you're going to be a perfect member in my team. "
                    o " Now, I know what you're thinking - 'What do I get in being in your team?' "
                    o " Well, for example...I'll give you 30$ daily. "
                    o " Sounds good enough, no? I already give Zip and Edward that amount everytime they did something good. "
                    hide oliverneutral at bottom
                    show oliverhappy at center
                    o " Well, anyway...you can't back out now, dear! You're with me from now on. "
                    o " No taking anything back, you hear? "
                    play sound "audio/bellring.mp3"
                    " The bell rings right before Oliver gets to say anything. "
                    hide oliverhappy at bottom
                    show oliverneutral at center
                    o " Hmm, that sucks. "
                    o " I was hoping I could talk to you more, [name]. "
                    o " Oh, well! we could always talk in our hangout room! "
                    o " Where that is? well... "
                    o " It's at the veeeerry back of the school. It's just an abandoned classroom, so it'll be easy to find. "
                    o " Thankfully Miss Grace allowed me and the others to hang out there, hah. "
                    o " AAAANYWAY!! I'll see you later, goodbye!! "
                    hide oliverneutral at right with easeoutright
                    " ...You walked your way to your classroom. "
                    scene black with dissolve
                    " From now on, every single break, you're only going to be hanging out in the abandoned classroom. "
                    " Why? cause you made this decision, of course. "
                    " Now, let's get to class. "
                    pause 2.0
                    jump scienceclass3
                " Nah, let's just watch ":
                    " You looked around and sat down on the bleachers. "
                    " You watched Kevin and Oliver argue...hey, wait... "
                    " You could record this. It would be funny. "
                    " It could also serve as a memory in the future... "
                    " Not like they'd notice that you're recording, right? "
                    " You pulled out your phone and you started recording them. "
                    scene black with dissolve
                    " You spent the rest of the break watching and recording Kevin and Oliver arguing. "
                    " The argument stopped a little early, but atleast you got something to remind yourself in the future of what this school was like. "
                    " So if anyone asked you how your time here was, you could just show them this video that you recorded. "
                    " No long explanation needed at all! "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You get up from the bleachers and you walked all the way back to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
        else:
            menu:
                " Help Kevin ":
                    $ kevinlv += 10
                    hide kevinangry at bottom
                    show kevinneutral at right
                    " You walked infront of Oliver and told him to stop. "
                    " You told him that it was making the other guy uncomfortable, and that it wasn't okay. "
                    hide oliverhappy at bottom
                    show oliverneutral at left
                    o " Oooh, what's this? "
                    o " Are you really defending this nerd, [name]? "
                    o " Come on, it's completely alright for me to be bothering him! "
                    if oligangtry == True:
                        o " Besides, didn't you say that you wanted to join my crew earlier? "
                        o " What a shame...looks like you don't want to join after all! "
                        o " You would've been a great addition to my team...but if you don't want to join, then... "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " Your loss, hah! "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                    else:
                        o " You just don't know how to have fun, [name]. "
                        o " I don't really care if I get in trouble or not... "
                        o " ...Doing this stuff is what 'fun' is to me! "
                        o " You've got to live a little, [name], jeez. "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " You probably don't know how to do that, though. Considering how you are! "
                        o " All flesh and bones, with thoughts and all of that... only to end up being used as a puppet for some sick game! "
                        " ...Okay, what nonsense was he on about? "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                        o " All of your actions are being controlled by someone, silly. "
                        o " You just can't bring yourself to believe that fact! "
                    o " Anyway, I'm outta here. "
                    o " Later, losers! "
                    hide oliverneutral at right with easeoutright
                    show kevinneutral at center with move
                    " ...Well, guess that worked. "
                    if oligangtry == True:
                        " You could probably care less about what he said to you. "
                        " His gang stinks, anyway. "
                    else:
                        " Wonder what he was on about, though... "
                    kv " ...Ahem. "
                    kv " I'd like to thank you, [name]. "
                    kv " For helping Oliver get off of my business, to be specific. "
                    kv " I don't know how long I'd last without your help... "
                    if oligangtry == True:
                        hide kevinneutral at bottom
                        show kevinconfused at center
                        kv " I'm gonna have to ask about your questionable choice of... "
                        kv " ...Wanting to be in his group, was it? "
                        kv " Why?????????? "
                        " Oh boy, this is going to be a somewhat long explanation. "
                        " You brace yourself for the very long explanation you're about to give to Kevin... "
                    else:
                        kv " I don't know what he was going on about the whole puppet thing, though. "
                        kv " Must've been him just trying to make himself look cool... "
                        kv " ...Or for me to stir up some very wild and wacky theories. "
                        kv " I'm not that type of person, though. "
                    scene black with dissolve
                    if oligangtry == True:
                        " You spent the rest of the break explaining to Kevin on why you wanted to join Oliver in the first place. "
                        " Actually, it was more of you just saying that you were lying to Oliver about all of that... "
                        " ...Though Kevin didn't believe you with the tone you were using, apparently. "
                        " You had to tell him what happened on the very first day and everything...yada yada... "
                        " Let's just say he was flabbergasted. "
                    else:
                        " You spent the rest of the break talking with Kevin. "
                        " You two were just talking about what happened... "
                        " Kevin was explaining how he even got into that situation with Oliver. "
                        " According to him, he was just minding his business, and Oliver was just trying to find some soap. "
                        " ...In the gym?? - Anyway, There just so happened to be a bar of soap right next to Kevin, andddd...you know what happened. "
                        " Is there always some soap in the gym? "
                        " Do they have, like...a special stock of soap just for Oliver? "
                        " So many questions, but no answers. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for class. "
                    " You walked all the way to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
                " Nah, let's just watch ":
                    " You looked around and sat down on the bleachers. "
                    " You watched Kevin and Oliver argue...hey, wait... "
                    " You could record this. It would be funny. "
                    " It could also serve as a memory in the future... "
                    " Not like they'd notice that you're recording, right? "
                    " You pulled out your phone and you started recording them. "
                    scene black with dissolve
                    " You spent the rest of the break watching and recording Kevin and Oliver arguing. "
                    " The argument stopped a little early, but atleast you got something to remind yourself in the future of what this school was like. "
                    " So if anyone asked you how your time here was, you could just show them this video that you recorded. "
                    " No long explanation needed at all! "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You get up from the bleachers and you walked all the way back to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
    elif kevinknow == True and oligangknow == False:
        kv " Eheh, look, Oliver. "
        o " I'm already looking, though? "
        kv " ... "
        o " Heh. What, got you mad? "
        kv " Whatever - I don't have time for this. "
        o " Awww, you're leaving already, Kevs? "
        o " Come on, I'm just getting started! "
        kv " Getting started on what? doing your job of annoying me? "
        o " Yuuup!! "
        o " Come on, Kevs - can't you stay a little longer? "
        kv " I have work to do, Oliver. "
        o " Whaaaat? Homework? How boring, Kevin. I thought you were better than this! "
        kv " Geez, could you just get off of me?! "
        o " Nuh uh!! "
        o " Not when I'm having fun with you!! "
        kv " Good lord, have mercy... "
        " Looks like Oliver's bothering him. "
        " You feel like you should help him... "
        " Should you? "
        if oligangtry == True:
            menu:
                " Help Kevin ":
                    $ kevinlv += 10
                    hide kevinangry at bottom
                    show kevinneutral at right
                    " You walked infront of Oliver and told him to stop. "
                    " You told him that it was making the other guy uncomfortable, and that it wasn't okay. "
                    hide oliverhappy at bottom
                    show oliverneutral at left
                    o " Oooh, what's this? "
                    o " Are you really defending this nerd, [name]? "
                    o " Come on, it's completely alright for me to be bothering him! "
                    if oligangtry == True:
                        o " Besides, didn't you say that you wanted to join my crew earlier? "
                        o " What a shame...looks like you don't want to join after all! "
                        o " You would've been a great addition to my team...but if you don't want to join, then... "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " Your loss, hah! "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                    else:
                        o " You just don't know how to have fun, [name]. "
                        o " I don't really care if I get in trouble or not... "
                        o " ...Doing this stuff is what 'fun' is to me! "
                        o " You've got to live a little, [name], jeez. "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " You probably don't know how to do that, though. Considering how you are! "
                        o " All flesh and bones, with thoughts and all of that... only to end up being used as a puppet for some sick game! "
                        " ...Okay, what nonsense was he on about? "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                        o " All of your actions are being controlled by someone, silly. "
                        o " You just can't bring yourself to believe that fact! "
                    o " Anyway, I'm outta here. "
                    o " Later, losers! "
                    hide oliverneutral at right with easeoutright
                    show kevinneutral at center with move
                    " ...Well, guess that worked. "
                    if oligangtry == True:
                        " You could probably care less about what he said to you. "
                        " His gang stinks, anyway. "
                    else:
                        " Wonder what he was on about, though... "
                    kv " ...Ahem. "
                    kv " I'd like to thank you, [name]. "
                    kv " For helping Oliver get off of my business, to be specific. "
                    kv " I don't know how long I'd last without your help... "
                    if oligangtry == True:
                        hide kevinneutral at bottom
                        show kevinconfused at center
                        kv " I'm gonna have to ask about your questionable choice of... "
                        kv " ...Wanting to be in his group, was it? "
                        kv " Why?????????? "
                        " Oh boy, this is going to be a somewhat long explanation. "
                        " You brace yourself for the very long explanation you're about to give to Kevin... "
                    else:
                        kv " I don't know what he was going on about the whole puppet thing, though. "
                        kv " Must've been him just trying to make himself look cool... "
                        kv " ...Or for me to stir up some very wild and wacky theories. "
                        kv " I'm not that type of person, though. "
                    scene black with dissolve
                    if oligangtry == True:
                        " You spent the rest of the break explaining to Kevin on why you wanted to join Oliver in the first place. "
                        " Actually, it was more of you just saying that you were lying to Oliver about all of that... "
                        " ...Though Kevin didn't believe you with the tone you were using, apparently. "
                        " You had to tell him what happened on the very first day and everything...yada yada... "
                        " Let's just say he was flabbergasted. "
                    else:
                        " You spent the rest of the break talking with Kevin. "
                        " You two were just talking about what happened... "
                        " Kevin was explaining how he even got into that situation with Oliver. "
                        " According to him, he was just minding his business, and Oliver was just trying to find some soap. "
                        " ...In the gym?? - Anyway, There just so happened to be a bar of soap right next to Kevin, andddd...you know what happened. "
                        " Is there always some soap in the gym? "
                        " Do they have, like...a special stock of soap just for Oliver? "
                        " So many questions, but no answers. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for class. "
                    " You walked all the way to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
                " Help Oliver ":
                    $ oliganglv += 10
                    $ oligangjoin = True
                    " You sure you wanna do this? Damn, alright. "
                    " You do you, I guess. "
                    hide oliverhappy at bottom
                    show oliverneutral at left
                    " You walked infront of Kevin and stared at him for a bit. "
                    kv " ...Oh, now what do you want - {nw} "
                    hide kevinangry at bottom
                    show kevinsurprised at right
                    " You then proceeded to snatch his glasses away from him and threw it to the trash can. "
                    " Fyi the trash can was pretty far from you guys, so...pretty impressive. "
                    hide kevinsurprised at bottom
                    show kevinangry at right
                    kv " MY GLASSES!! " with vpunch
                    hide kevinangry at bottom with easeoutbottom
                    " Before he could say anything, you kicked him down onto the ground. "
                    " You then proceeded to kick him in the stomach a few times before you stopped. "
                    " You looked at the other guy that was near you and he seemed impressed with what you did. "
                    if abbiemeandefend == True:
                        " Though it did remind you of what you did to him in the past.. "
                    else:
                        pass
                    hide oliverneutral at bottom
                    show oliverhappy at left
                    show oliverhappy at center with move
                    o " Oooh, nice one, [name]! "
                    o " I like your style there...how about we force feed him some soap? "
                    o " Hah, good idea, right? "
                    hide oliverhappy at bottom
                    show oliverneutral at center
                    o " ...Unfortunately there's a security camera here, so we can't do anything too bad. "
                    o " Miss Grace would've killed us if we went too far. "
                    o " For now, let's leave Kevin alone, yeah? Looks like we've done enough for now! "
                    o " Hope he's gonna have a fun time finding his glasses, hehe. "
                    o " Let's go into the hallways, alright? "
                    o " Don't want someone to tell the teachers now, would we? "
                    o " I'd rather NOT get caught after having fun like this. "
                    o " Come on, let's go, [name]. "
                    hide oliverneutral at right with easeoutright
                    scene black with dissolve
                    " You followed Oliver into the hallway. "
                    pause 1.0
                    scene hallway with dissolve
                    show oliverneutral at center with easeinleft
                    o " Ahhh, it's surprisingly quiet here. Good. "
                    hide oliverneutral at bottom
                    show oliverhappy at center
                    o " Though, someone might be listening in. We wouldn't really want that now, would we? "
                    hide oliverhappy at bottom
                    show oliverneutral at center
                    o " Let's just talk really, really quietly then. "
                    o " So... "
                    o " I know that I've said that it's going to take a LOT to impress me, but... "
                    o " With what you did to Kevin, it kind of just...I dunno... "
                    o " Let's say: made me think that you're going to be a perfect member in my team. "
                    o " Now, I know what you're thinking - 'What do I get in being in your team?' "
                    o " Well, for example...I'll give you 30$ daily. "
                    o " Sounds good enough, no? I already give Zip and Edward that amount everytime they did something good. "
                    hide oliverneutral at bottom
                    show oliverhappy at center
                    o " Well, anyway...you can't back out now, dear! You're with me from now on. "
                    o " No taking anything back, you hear? "
                    play sound "audio/bellring.mp3"
                    " The bell rings right before Oliver gets to say anything. "
                    hide oliverhappy at bottom
                    show oliverneutral at center
                    o " Hmm, that sucks. "
                    o " I was hoping I could talk to you more, [name]. "
                    o " Oh, well! we could always talk in our hangout room! "
                    o " Where that is? well... "
                    o " It's at the veeeerry back of the school. It's just an abandoned classroom, so it'll be easy to find. "
                    o " Thankfully Miss Grace allowed me and the others to hang out there, hah. "
                    o " AAAANYWAY!! I'll see you later, goodbye!! "
                    hide oliverneutral at right with easeoutright
                    " ...You walked your way to your classroom. "
                    scene black with dissolve
                    " From now on, every single break, you're only going to be hanging out in the abandoned classroom. "
                    " Why? cause you made this decision, of course. "
                    " Now, let's get to class. "
                    pause 2.0
                    jump scienceclass3
                " Nah, let's just watch ":
                    " You looked around and sat down on the bleachers. "
                    " You watched Kevin and Oliver argue...hey, wait... "
                    " You could record this. It would be funny. "
                    " It could also serve as a memory in the future... "
                    " Not like they'd notice that you're recording, right? "
                    " You pulled out your phone and you started recording them. "
                    scene black with dissolve
                    " You spent the rest of the break watching and recording Kevin and Oliver arguing. "
                    " The argument stopped a little early, but atleast you got something to remind yourself in the future of what this school was like. "
                    " So if anyone asked you how your time here was, you could just show them this video that you recorded. "
                    " No long explanation needed at all! "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You get up from the bleachers and you walked all the way back to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
        else:
            menu:
                " Help Kevin ":
                    $ kevinlv += 10
                    hide kevinangry at bottom
                    show kevinneutral at right
                    " You walked infront of Oliver and told him to stop. "
                    " You told him that it was making the other guy uncomfortable, and that it wasn't okay. "
                    hide oliverhappy at bottom
                    show oliverneutral at left
                    o " Oooh, what's this? "
                    o " Are you really defending this nerd, [name]? "
                    o " Come on, it's completely alright for me to be bothering him! "
                    if oligangtry == True:
                        o " Besides, didn't you say that you wanted to join my crew earlier? "
                        o " What a shame...looks like you don't want to join after all! "
                        o " You would've been a great addition to my team...but if you don't want to join, then... "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " Your loss, hah! "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                    else:
                        o " You just don't know how to have fun, [name]. "
                        o " I don't really care if I get in trouble or not... "
                        o " ...Doing this stuff is what 'fun' is to me! "
                        o " You've got to live a little, [name], jeez. "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " You probably don't know how to do that, though. Considering how you are! "
                        o " All flesh and bones, with thoughts and all of that... only to end up being used as a puppet for some sick game! "
                        " ...Okay, what nonsense was he on about? "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                        o " All of your actions are being controlled by someone, silly. "
                        o " You just can't bring yourself to believe that fact! "
                    o " Anyway, I'm outta here. "
                    o " Later, losers! "
                    hide oliverneutral at right with easeoutright
                    show kevinneutral at center with move
                    " ...Well, guess that worked. "
                    if oligangtry == True:
                        " You could probably care less about what he said to you. "
                        " His gang stinks, anyway. "
                    else:
                        " Wonder what he was on about, though... "
                    kv " ...Ahem. "
                    kv " I'd like to thank you, [name]. "
                    kv " For helping Oliver get off of my business, to be specific. "
                    kv " I don't know how long I'd last without your help... "
                    if oligangtry == True:
                        hide kevinneutral at bottom
                        show kevinconfused at center
                        kv " I'm gonna have to ask about your questionable choice of... "
                        kv " ...Wanting to be in his group, was it? "
                        kv " Why?????????? "
                        " Oh boy, this is going to be a somewhat long explanation. "
                        " You brace yourself for the very long explanation you're about to give to Kevin... "
                    else:
                        kv " I don't know what he was going on about the whole puppet thing, though. "
                        kv " Must've been him just trying to make himself look cool... "
                        kv " ...Or for me to stir up some very wild and wacky theories. "
                        kv " I'm not that type of person, though. "
                    scene black with dissolve
                    if oligangtry == True:
                        " You spent the rest of the break explaining to Kevin on why you wanted to join Oliver in the first place. "
                        " Actually, it was more of you just saying that you were lying to Oliver about all of that... "
                        " ...Though Kevin didn't believe you with the tone you were using, apparently. "
                        " You had to tell him what happened on the very first day and everything...yada yada... "
                        " Let's just say he was flabbergasted. "
                    else:
                        " You spent the rest of the break talking with Kevin. "
                        " You two were just talking about what happened... "
                        " Kevin was explaining how he even got into that situation with Oliver. "
                        " According to him, he was just minding his business, and Oliver was just trying to find some soap. "
                        " ...In the gym?? - Anyway, There just so happened to be a bar of soap right next to Kevin, andddd...you know what happened. "
                        " Is there always some soap in the gym? "
                        " Do they have, like...a special stock of soap just for Oliver? "
                        " So many questions, but no answers. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for class. "
                    " You walked all the way to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
                " Nah, let's just watch ":
                    " You looked around and sat down on the bleachers. "
                    " You watched Kevin and Oliver argue...hey, wait... "
                    " You could record this. It would be funny. "
                    " It could also serve as a memory in the future... "
                    " Not like they'd notice that you're recording, right? "
                    " You pulled out your phone and you started recording them. "
                    scene black with dissolve
                    " You spent the rest of the break watching and recording Kevin and Oliver arguing. "
                    " The argument stopped a little early, but atleast you got something to remind yourself in the future of what this school was like. "
                    " So if anyone asked you how your time here was, you could just show them this video that you recorded. "
                    " No long explanation needed at all! "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You get up from the bleachers and you walked all the way back to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
    elif kevinknow == False and oligangknow == True:
        x " Eheh, look, Oliver. "
        o " I'm already looking, though? "
        x " ... "
        o " Heh. What, got you mad? "
        x " Whatever - I don't have time for this. "
        o " Awww, you're leaving already, Kevs? "
        o " Come on, I'm just getting started! "
        x " Getting started on what? doing your job of annoying me? "
        o " Yuuup!! "
        o " Come on, Kevs - can't you stay a little longer? "
        x " I have work to do, Oliver. "
        o " Whaaaat? Homework? How boring, Kevin. I thought you were better than this! "
        x " Geez, could you just get off of me?! "
        o " Nuh uh!! "
        o " Not when I'm having fun with you!! "
        x " Good lord, have mercy... "
        " Looks like Oliver's bothering him. "
        " You feel like you should help him... "
        " Should you? "
        if oligangtry == True:
            menu:
                " Help the nerd ":
                    $ kevinlv += 10
                    hide kevinangry at bottom
                    show kevinneutral at right
                    " You walked infront of Oliver and told him to stop. "
                    " You told him that it was making the other guy uncomfortable, and that it wasn't okay. "
                    hide oliverhappy at bottom
                    show oliverneutral at left
                    o " Oooh, what's this? "
                    o " Are you really defending this nerd, [name]? "
                    o " Come on, it's completely alright for me to be bothering him! "
                    if oligangtry == True:
                        o " Besides, didn't you say that you wanted to join my crew earlier? "
                        o " What a shame...looks like you don't want to join after all! "
                        o " You would've been a great addition to my team...but if you don't want to join, then... "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " Your loss, hah! "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                    else:
                        o " You just don't know how to have fun, [name]. "
                        o " I don't really care if I get in trouble or not... "
                        o " ...Doing this stuff is what 'fun' is to me! "
                        o " You've got to live a little, [name], jeez. "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " You probably don't know how to do that, though. Considering how you are! "
                        o " All flesh and bones, with thoughts and all of that... only to end up being used as a puppet for some sick game! "
                        " ...Okay, what nonsense was he on about? "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                        o " All of your actions are being controlled by someone, silly. "
                        o " You just can't bring yourself to believe that fact! "
                    o " Anyway, I'm outta here. "
                    o " Later, losers! "
                    hide oliverneutral at right with easeoutright
                    show kevinneutral at center with move
                    " ...Well, guess that worked. "
                    if oligangtry == True:
                        " You could probably care less about what he said to you. "
                        " His gang stinks, anyway. "
                    else:
                        " Wonder what he was on about, though... "
                    x " ...Ahem. "
                    x " I'd like to thank you, [name]. "
                    x " For helping Oliver get off of my business, to be specific. "
                    x " I don't know how long I'd last without your help... "
                    $ kevinknow = True
                    kv " I'm Kevin, by the way. We're classmates. "
                    if oligangtry == True:
                        hide kevinneutral at bottom
                        show kevinconfused at center
                        kv " I'm gonna have to ask about your questionable choice of... "
                        kv " ...Wanting to be in his group, was it? "
                        kv " Why?????????? "
                        " Oh boy, this is going to be a somewhat long explanation. "
                        " You brace yourself for the very long explanation you're about to give to Kevin... "
                    else:
                        kv " I don't know what he was going on about the whole puppet thing, though. "
                        kv " Must've been him just trying to make himself look cool... "
                        kv " ...Or for me to stir up some very wild and wacky theories. "
                        kv " I'm not that type of person, though. "
                    scene black with dissolve
                    if oligangtry == True:
                        " You spent the rest of the break explaining to Kevin on why you wanted to join Oliver in the first place. "
                        " Actually, it was more of you just saying that you were lying to Oliver about all of that... "
                        " ...Though Kevin didn't believe you with the tone you were using, apparently. "
                        " You had to tell him what happened on the very first day and everything...yada yada... "
                        " Let's just say he was flabbergasted. "
                    else:
                        " You spent the rest of the break talking with Kevin. "
                        " You two were just talking about what happened... "
                        " Kevin was explaining how he even got into that situation with Oliver. "
                        " According to him, he was just minding his business, and Oliver was just trying to find some soap. "
                        " ...In the gym?? - Anyway, There just so happened to be a bar of soap right next to Kevin, andddd...you know what happened. "
                        " Is there always some soap in the gym? "
                        " Do they have, like...a special stock of soap just for Oliver? "
                        " So many questions, but no answers. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for class. "
                    " You walked all the way to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
                " Help Oliver ":
                    $ oliganglv += 10
                    $ oligangjoin = True
                    " You sure you wanna do this? Damn, alright. "
                    " You do you, I guess. "
                    hide oliverhappy at bottom
                    show oliverneutral at left
                    " You walked infront of Kevin and stared at him for a bit. "
                    x " ...Oh, now what do you want - {nw} "
                    hide kevinangry at bottom
                    show kevinsurprised at right
                    " You then proceeded to snatch his glasses away from him and threw it to the trash can. "
                    " Fyi the trash can was pretty far from you guys, so...pretty impressive. "
                    hide kevinsurprised at bottom
                    show kevinangry at right
                    x " MY GLASSES!! " with vpunch
                    hide kevinangry at bottom with easeoutbottom
                    " Before he could say anything, you kicked him down onto the ground. "
                    " You then proceeded to kick him in the stomach a few times before you stopped. "
                    " You looked at the other guy that was near you and he seemed impressed with what you did. "
                    if abbiemeandefend == True:
                        " Though it did remind you of what you did to him in the past.. "
                    else:
                        pass
                    hide oliverneutral at bottom
                    show oliverhappy at left
                    show oliverhappy at center with move
                    o " Oooh, nice one, [name]! "
                    o " I like your style there...how about we force feed him some soap? "
                    o " Hah, good idea, right? "
                    hide oliverhappy at bottom
                    show oliverneutral at center
                    o " ...Unfortunately there's a security camera here, so we can't do anything too bad. "
                    o " Miss Grace would've killed us if we went too far. "
                    o " For now, let's leave Kevin alone, yeah? Looks like we've done enough for now! "
                    o " Hope he's gonna have a fun time finding his glasses, hehe. "
                    o " Let's go into the hallways, alright? "
                    o " Don't want someone to tell the teachers now, would we? "
                    o " I'd rather NOT get caught after having fun like this. "
                    o " Come on, let's go, [name]. "
                    hide oliverneutral at right with easeoutright
                    scene black with dissolve
                    " You followed Oliver into the hallway. "
                    pause 1.0
                    scene hallway with dissolve
                    show oliverneutral at center with easeinleft
                    o " Ahhh, it's surprisingly quiet here. Good. "
                    hide oliverneutral at bottom
                    show oliverhappy at center
                    o " Though, someone might be listening in. We wouldn't really want that now, would we? "
                    hide oliverhappy at bottom
                    show oliverneutral at center
                    o " Let's just talk really, really quietly then. "
                    o " So... "
                    o " I know that I've said that it's going to take a LOT to impress me, but... "
                    o " With what you did to Kevin, it kind of just...I dunno... "
                    o " Let's say: made me think that you're going to be a perfect member in my team. "
                    o " Now, I know what you're thinking - 'What do I get in being in your team?' "
                    o " Well, for example...I'll give you 30$ daily. "
                    o " Sounds good enough, no? I already give Zip and Edward that amount everytime they did something good. "
                    hide oliverneutral at bottom
                    show oliverhappy at center
                    o " Well, anyway...you can't back out now, dear! You're with me from now on. "
                    o " No taking anything back, you hear? "
                    play sound "audio/bellring.mp3"
                    " The bell rings right before Oliver gets to say anything. "
                    hide oliverhappy at bottom
                    show oliverneutral at center
                    o " Hmm, that sucks. "
                    o " I was hoping I could talk to you more, [name]. "
                    o " Oh, well! we could always talk in our hangout room! "
                    o " Where that is? well... "
                    o " It's at the veeeerry back of the school. It's just an abandoned classroom, so it'll be easy to find. "
                    o " Thankfully Miss Grace allowed me and the others to hang out there, hah. "
                    o " AAAANYWAY!! I'll see you later, goodbye!! "
                    hide oliverneutral at right with easeoutright
                    " ...You walked your way to your classroom. "
                    scene black with dissolve
                    " From now on, every single break, you're only going to be hanging out in the abandoned classroom. "
                    " Why? cause you made this decision, of course. "
                    " Now, let's get to class. "
                    pause 2.0
                    jump scienceclass3
                " Nah, let's just watch ":
                    " You looked around and sat down on the bleachers. "
                    " You watched the nerd and Oliver argue...hey, wait... "
                    " You could record this. It would be funny. "
                    " It could also serve as a memory in the future... "
                    " Not like they'd notice that you're recording, right? "
                    " You pulled out your phone and you started recording them. "
                    scene black with dissolve
                    " You spent the rest of the break watching and recording the nerd and Oliver arguing. "
                    " The argument stopped a little early, but atleast you got something to remind yourself in the future of what this school was like. "
                    " So if anyone asked you how your time here was, you could just show them this video that you recorded. "
                    " No long explanation needed at all! "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You get up from the bleachers and you walked all the way back to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
        else:
            menu:
                " Help the nerd ":
                    $ kevinlv += 10
                    hide kevinangry at bottom
                    show kevinneutral at right
                    " You walked infront of Oliver and told him to stop. "
                    " You told him that it was making the other guy uncomfortable, and that it wasn't okay. "
                    hide oliverhappy at bottom
                    show oliverneutral at left
                    o " Oooh, what's this? "
                    o " Are you really defending this nerd, [name]? "
                    o " Come on, it's completely alright for me to be bothering him! "
                    if oligangtry == True:
                        o " Besides, didn't you say that you wanted to join my crew earlier? "
                        o " What a shame...looks like you don't want to join after all! "
                        o " You would've been a great addition to my team...but if you don't want to join, then... "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " Your loss, hah! "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                    else:
                        o " You just don't know how to have fun, [name]. "
                        o " I don't really care if I get in trouble or not... "
                        o " ...Doing this stuff is what 'fun' is to me! "
                        o " You've got to live a little, [name], jeez. "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " You probably don't know how to do that, though. Considering how you are! "
                        o " All flesh and bones, with thoughts and all of that... only to end up being used as a puppet for some sick game! "
                        " ...Okay, what nonsense was he on about? "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                        o " All of your actions are being controlled by someone, silly. "
                        o " You just can't bring yourself to believe that fact! "
                    o " Anyway, I'm outta here. "
                    o " Later, losers! "
                    hide oliverneutral at right with easeoutright
                    show kevinneutral at center with move
                    " ...Well, guess that worked. "
                    if oligangtry == True:
                        " You could probably care less about what he said to you. "
                        " His gang stinks, anyway. "
                    else:
                        " Wonder what he was on about, though... "
                    x " ...Ahem. "
                    x " I'd like to thank you, [name]. "
                    x " For helping Oliver get off of my business, to be specific. "
                    x " I don't know how long I'd last without your help... "
                    $ kevinknow = True
                    kv " I'm Kevin, by the way. We're classmates. "
                    if oligangtry == True:
                        hide kevinneutral at bottom
                        show kevinconfused at center
                        kv " I'm gonna have to ask about your questionable choice of... "
                        kv " ...Wanting to be in his group, was it? "
                        kv " Why?????????? "
                        " Oh boy, this is going to be a somewhat long explanation. "
                        " You brace yourself for the very long explanation you're about to give to Kevin... "
                    else:
                        kv " I don't know what he was going on about the whole puppet thing, though. "
                        kv " Must've been him just trying to make himself look cool... "
                        kv " ...Or for me to stir up some very wild and wacky theories. "
                        kv " I'm not that type of person, though. "
                    scene black with dissolve
                    if oligangtry == True:
                        " You spent the rest of the break explaining to Kevin on why you wanted to join Oliver in the first place. "
                        " Actually, it was more of you just saying that you were lying to Oliver about all of that... "
                        " ...Though Kevin didn't believe you with the tone you were using, apparently. "
                        " You had to tell him what happened on the very first day and everything...yada yada... "
                        " Let's just say he was flabbergasted. "
                    else:
                        " You spent the rest of the break talking with Kevin. "
                        " You two were just talking about what happened... "
                        " Kevin was explaining how he even got into that situation with Oliver. "
                        " According to him, he was just minding his business, and Oliver was just trying to find some soap. "
                        " ...In the gym?? - Anyway, There just so happened to be a bar of soap right next to Kevin, andddd...you know what happened. "
                        " Is there always some soap in the gym? "
                        " Do they have, like...a special stock of soap just for Oliver? "
                        " So many questions, but no answers. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for class. "
                    " You walked all the way to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
                " Nah, let's just watch ":
                    " You looked around and sat down on the bleachers. "
                    " You watched the nerd and Oliver argue...hey, wait... "
                    " You could record this. It would be funny. "
                    " It could also serve as a memory in the future... "
                    " Not like they'd notice that you're recording, right? "
                    " You pulled out your phone and you started recording them. "
                    scene black with dissolve
                    " You spent the rest of the break watching and recording the nerd and Oliver arguing. "
                    " The argument stopped a little early, but atleast you got something to remind yourself in the future of what this school was like. "
                    " So if anyone asked you how your time here was, you could just show them this video that you recorded. "
                    " No long explanation needed at all! "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You get up from the bleachers and you walked all the way back to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
    else:
        x " Eheh, look, Oliver. "
        o " I'm already looking, though? "
        x " ... "
        o " Heh. What, got you mad? "
        x " Whatever - I don't have time for this. "
        o " Awww, you're leaving already, Kevs? "
        o " Come on, I'm just getting started! "
        x " Getting started on what? doing your job of annoying me? "
        o " Yuuup!! "
        o " Come on, Kevs - can't you stay a little longer? "
        x " I have work to do, Oliver. "
        o " Whaaaat? Homework? How boring, Kevin. I thought you were better than this! "
        x " Geez, could you just get off of me?! "
        o " Nuh uh!! "
        o " Not when I'm having fun with you!! "
        x " Good lord, have mercy... "
        " Looks like Oliver's bothering him. "
        " You feel like you should help him... "
        " Should you? "
        if oligangtry == True:
            menu:
                " Help the nerd ":
                    $ kevinlv += 10
                    hide kevinangry at bottom
                    show kevinneutral at right
                    " You walked infront of Oliver and told him to stop. "
                    " You told him that it was making the other guy uncomfortable, and that it wasn't okay. "
                    hide oliverhappy at bottom
                    show oliverneutral at left
                    o " Oooh, what's this? "
                    o " Are you really defending this nerd, [name]? "
                    o " Come on, it's completely alright for me to be bothering him! "
                    if oligangtry == True:
                        o " Besides, didn't you say that you wanted to join my crew earlier? "
                        o " What a shame...looks like you don't want to join after all! "
                        o " You would've been a great addition to my team...but if you don't want to join, then... "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " Your loss, hah! "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                    else:
                        o " You just don't know how to have fun, [name]. "
                        o " I don't really care if I get in trouble or not... "
                        o " ...Doing this stuff is what 'fun' is to me! "
                        o " You've got to live a little, [name], jeez. "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " You probably don't know how to do that, though. Considering how you are! "
                        o " All flesh and bones, with thoughts and all of that... only to end up being used as a puppet for some sick game! "
                        " ...Okay, what nonsense was he on about? "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                        o " All of your actions are being controlled by someone, silly. "
                        o " You just can't bring yourself to believe that fact! "
                    o " Anyway, I'm outta here. "
                    o " Later, losers! "
                    hide oliverneutral at right with easeoutright
                    show kevinneutral at center with move
                    " ...Well, guess that worked. "
                    if oligangtry == True:
                        " You could probably care less about what he said to you. "
                        " His gang stinks, anyway. "
                    else:
                        " Wonder what he was on about, though... "
                    x " ...Ahem. "
                    x " I'd like to thank you, [name]. "
                    x " For helping Oliver get off of my business, to be specific. "
                    x " I don't know how long I'd last without your help... "
                    $ kevinknow = True
                    kv " I'm Kevin, by the way. We're classmates. "
                    if oligangtry == True:
                        hide kevinneutral at bottom
                        show kevinconfused at center
                        kv " I'm gonna have to ask about your questionable choice of... "
                        kv " ...Wanting to be in his group, was it? "
                        kv " Why?????????? "
                        " Oh boy, this is going to be a somewhat long explanation. "
                        " You brace yourself for the very long explanation you're about to give to Kevin... "
                    else:
                        kv " I don't know what he was going on about the whole puppet thing, though. "
                        kv " Must've been him just trying to make himself look cool... "
                        kv " ...Or for me to stir up some very wild and wacky theories. "
                        kv " I'm not that type of person, though. "
                    scene black with dissolve
                    if oligangtry == True:
                        " You spent the rest of the break explaining to Kevin on why you wanted to join Oliver in the first place. "
                        " Actually, it was more of you just saying that you were lying to Oliver about all of that... "
                        " ...Though Kevin didn't believe you with the tone you were using, apparently. "
                        " You had to tell him what happened on the very first day and everything...yada yada... "
                        " Let's just say he was flabbergasted. "
                    else:
                        " You spent the rest of the break talking with Kevin. "
                        " You two were just talking about what happened... "
                        " Kevin was explaining how he even got into that situation with Oliver. "
                        " According to him, he was just minding his business, and Oliver was just trying to find some soap. "
                        " ...In the gym?? - Anyway, There just so happened to be a bar of soap right next to Kevin, andddd...you know what happened. "
                        " Is there always some soap in the gym? "
                        " Do they have, like...a special stock of soap just for Oliver? "
                        " So many questions, but no answers. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for class. "
                    " You walked all the way to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
                " Help Oliver ":
                    $ oliganglv += 10
                    $ oligangjoin = True
                    " You sure you wanna do this? Damn, alright. "
                    " You do you, I guess. "
                    hide oliverhappy at bottom
                    show oliverneutral at left
                    " You walked infront of Kevin and stared at him for a bit. "
                    x " ...Oh, now what do you want - {nw} "
                    hide kevinangry at bottom
                    show kevinsurprised at right
                    " You then proceeded to snatch his glasses away from him and threw it to the trash can. "
                    " Fyi the trash can was pretty far from you guys, so...pretty impressive. "
                    hide kevinsurprised at bottom
                    show kevinangry at right
                    x " MY GLASSES!! " with vpunch
                    hide kevinangry at bottom with easeoutbottom
                    " Before he could say anything, you kicked him down onto the ground. "
                    " You then proceeded to kick him in the stomach a few times before you stopped. "
                    " You looked at the other guy that was near you and he seemed impressed with what you did. "
                    if abbiemeandefend == True:
                        " Though it did remind you of what you did to him in the past.. "
                    else:
                        pass
                    hide oliverneutral at bottom
                    show oliverhappy at left
                    show oliverhappy at center with move
                    o " Oooh, nice one, [name]! "
                    o " I like your style there...how about we force feed him some soap? "
                    o " Hah, good idea, right? "
                    hide oliverhappy at bottom
                    show oliverneutral at center
                    o " ...Unfortunately there's a security camera here, so we can't do anything too bad. "
                    o " Miss Grace would've killed us if we went too far. "
                    o " For now, let's leave Kevin alone, yeah? Looks like we've done enough for now! "
                    o " Hope he's gonna have a fun time finding his glasses, hehe. "
                    o " Let's go into the hallways, alright? "
                    o " Don't want someone to tell the teachers now, would we? "
                    o " I'd rather NOT get caught after having fun like this. "
                    o " Come on, let's go, [name]. "
                    hide oliverneutral at right with easeoutright
                    scene black with dissolve
                    " You followed Oliver into the hallway. "
                    pause 1.0
                    scene hallway with dissolve
                    show oliverneutral at center with easeinleft
                    o " Ahhh, it's surprisingly quiet here. Good. "
                    hide oliverneutral at bottom
                    show oliverhappy at center
                    o " Though, someone might be listening in. We wouldn't really want that now, would we? "
                    hide oliverhappy at bottom
                    show oliverneutral at center
                    o " Let's just talk really, really quietly then. "
                    o " So... "
                    o " I know that I've said that it's going to take a LOT to impress me, but... "
                    o " With what you did to Kevin, it kind of just...I dunno... "
                    o " Let's say: made me think that you're going to be a perfect member in my team. "
                    o " Now, I know what you're thinking - 'What do I get in being in your team?' "
                    o " Well, for example...I'll give you 30$ daily. "
                    o " Sounds good enough, no? I already give Zip and Edward that amount everytime they did something good. "
                    hide oliverneutral at bottom
                    show oliverhappy at center
                    o " Well, anyway...you can't back out now, dear! You're with me from now on. "
                    o " No taking anything back, you hear? "
                    play sound "audio/bellring.mp3"
                    " The bell rings right before Oliver gets to say anything. "
                    hide oliverhappy at bottom
                    show oliverneutral at center
                    o " Hmm, that sucks. "
                    o " I was hoping I could talk to you more, [name]. "
                    o " Oh, well! we could always talk in our hangout room! "
                    o " Where that is? well... "
                    o " It's at the veeeerry back of the school. It's just an abandoned classroom, so it'll be easy to find. "
                    o " Thankfully Miss Grace allowed me and the others to hang out there, hah. "
                    o " AAAANYWAY!! I'll see you later, goodbye!! "
                    hide oliverneutral at right with easeoutright
                    " ...You walked your way to your classroom. "
                    scene black with dissolve
                    " From now on, every single break, you're only going to be hanging out in the abandoned classroom. "
                    " Why? cause you made this decision, of course. "
                    " Now, let's get to class. "
                    pause 2.0
                    jump scienceclass3
                " Nah, let's just watch ":
                    " You looked around and sat down on the bleachers. "
                    " You watched the nerd and Oliver argue...hey, wait... "
                    " You could record this. It would be funny. "
                    " It could also serve as a memory in the future... "
                    " Not like they'd notice that you're recording, right? "
                    " You pulled out your phone and you started recording them. "
                    scene black with dissolve
                    " You spent the rest of the break watching and recording the nerd and Oliver arguing. "
                    " The argument stopped a little early, but atleast you got something to remind yourself in the future of what this school was like. "
                    " So if anyone asked you how your time here was, you could just show them this video that you recorded. "
                    " No long explanation needed at all! "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You get up from the bleachers and you walked all the way back to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
        else:
            menu:
                " Help the nerd ":
                    $ kevinlv += 10
                    hide kevinangry at bottom
                    show kevinneutral at right
                    " You walked infront of Oliver and told him to stop. "
                    " You told him that it was making the other guy uncomfortable, and that it wasn't okay. "
                    hide oliverhappy at bottom
                    show oliverneutral at left
                    o " Oooh, what's this? "
                    o " Are you really defending this nerd, [name]? "
                    o " Come on, it's completely alright for me to be bothering him! "
                    if oligangtry == True:
                        o " Besides, didn't you say that you wanted to join my crew earlier? "
                        o " What a shame...looks like you don't want to join after all! "
                        o " You would've been a great addition to my team...but if you don't want to join, then... "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " Your loss, hah! "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                    else:
                        o " You just don't know how to have fun, [name]. "
                        o " I don't really care if I get in trouble or not... "
                        o " ...Doing this stuff is what 'fun' is to me! "
                        o " You've got to live a little, [name], jeez. "
                        hide oliverneutral at bottom
                        show oliverhappy at left
                        o " You probably don't know how to do that, though. Considering how you are! "
                        o " All flesh and bones, with thoughts and all of that... only to end up being used as a puppet for some sick game! "
                        " ...Okay, what nonsense was he on about? "
                        hide oliverhappy at bottom
                        show oliverneutral at left
                        o " All of your actions are being controlled by someone, silly. "
                        o " You just can't bring yourself to believe that fact! "
                    o " Anyway, I'm outta here. "
                    o " Later, losers! "
                    hide oliverneutral at right with easeoutright
                    show kevinneutral at center with move
                    " ...Well, guess that worked. "
                    if oligangtry == True:
                        " You could probably care less about what he said to you. "
                        " His gang stinks, anyway. "
                    else:
                        " Wonder what he was on about, though... "
                    x " ...Ahem. "
                    x " I'd like to thank you, [name]. "
                    x " For helping Oliver get off of my business, to be specific. "
                    x " I don't know how long I'd last without your help... "
                    $ kevinknow = True
                    kv " I'm Kevin, by the way. We're classmates. "
                    if oligangtry == True:
                        hide kevinneutral at bottom
                        show kevinconfused at center
                        kv " I'm gonna have to ask about your questionable choice of... "
                        kv " ...Wanting to be in his group, was it? "
                        kv " Why?????????? "
                        " Oh boy, this is going to be a somewhat long explanation. "
                        " You brace yourself for the very long explanation you're about to give to Kevin... "
                    else:
                        kv " I don't know what he was going on about the whole puppet thing, though. "
                        kv " Must've been him just trying to make himself look cool... "
                        kv " ...Or for me to stir up some very wild and wacky theories. "
                        kv " I'm not that type of person, though. "
                    scene black with dissolve
                    if oligangtry == True:
                        " You spent the rest of the break explaining to Kevin on why you wanted to join Oliver in the first place. "
                        " Actually, it was more of you just saying that you were lying to Oliver about all of that... "
                        " ...Though Kevin didn't believe you with the tone you were using, apparently. "
                        " You had to tell him what happened on the very first day and everything...yada yada... "
                        " Let's just say he was flabbergasted. "
                    else:
                        " You spent the rest of the break talking with Kevin. "
                        " You two were just talking about what happened... "
                        " Kevin was explaining how he even got into that situation with Oliver. "
                        " According to him, he was just minding his business, and Oliver was just trying to find some soap. "
                        " ...In the gym?? - Anyway, There just so happened to be a bar of soap right next to Kevin, andddd...you know what happened. "
                        " Is there always some soap in the gym? "
                        " Do they have, like...a special stock of soap just for Oliver? "
                        " So many questions, but no answers. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for class. "
                    " You walked all the way to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
                " Nah, let's just watch ":
                    " You looked around and sat down on the bleachers. "
                    " You watched the nerd and Oliver argue...hey, wait... "
                    " You could record this. It would be funny. "
                    " It could also serve as a memory in the future... "
                    " Not like they'd notice that you're recording, right? "
                    " You pulled out your phone and you started recording them. "
                    scene black with dissolve
                    " You spent the rest of the break watching and recording the nerd and Oliver arguing. "
                    " The argument stopped a little early, but atleast you got something to remind yourself in the future of what this school was like. "
                    " So if anyone asked you how your time here was, you could just show them this video that you recorded. "
                    " No long explanation needed at all! "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You get up from the bleachers and you walked all the way back to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
label wedcafe2:
    # popular girls, engel - petunia n liz gossiping - engel worrying about claire
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted three of your classmates hanging out. "
    " You wanted to talk to them...but who do you talk to? "
    if popularknow == True and engelknow == True:
        menu:
            " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                jump thatsa
            " {image=engelicon} Engel {image=engelicon} ":
                jump wrap
    elif popularknow == True and engelknow == False:
        menu:
            " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                jump thatsa
            " {image=engelicon} A boy with feathers on his head {image=engelicon} ":
                jump wrap
    elif popularknow == False and engelknow == True:
        menu:
            " {image=popularicon} Popular looking girls {image=popularicon} ":
                jump thatsa
            " {image=engelicon} Engel {image=engelicon} ":
                jump wrap
    else:
        menu:
            " {image=popularicon} Popular looking girls {image=popularicon} ":
                jump thatsa
            " {image=engelicon} A boy with feathers on his head {image=engelicon} ":
                jump wrap
    label thatsa:
        " You walked up to them and sat down next to them... "
        " Sounds like they're gossiping about something. Let's take a listen. "
        show petunianeutral at left with easeinleft
        show lizzyneutral at right with easeinright
        if popularknow == True:
            p " Hiya, [name]! "
            lz " Hello there, [name]. "
            p " Me and Lizzy were just gossiping, as per usual. "
            hide lizzyneutral at bottom
            show lizzyconfused at right
            lz " Yeahuh...wait, what is that smell? "
            hide petunianeutral at bottom
            show petuniaconfused at left
            p " Huh? what do you mean? "
            p " I don't smell anything... "
            hide lizzyconfused at bottom
            show lizzyneutral at right
            lz " Well, you know what they say. "
            lz " If you can't smell anything, then it must've been coming from you. "
            p " What?! "
            p " I'm pretty sure I've only heard my grandmama say that... "
            p " I mean, I know I forgot to take a shower today, but It can't smell that bad, right? "
            p " It's just a day after all.. It can't be that bad. "
            lz " ...For a day? how does that even happen? "
            p " ...Let's just say that I forgot. "
            p " Of course I wouldn't want to go to school without taking a bath! "
            p " I just forgot today, alright?! "
            p " And that smell is most DEFINITELY not coming from me. "
            lz " ...Okay, sure. "
            scene black with dissolve
            " You spent the rest of the break talking with Petunia and Lizzy. "
            " As you talked with them, you can't help but feel the very obvious tension in the air. "
            " Wonder what happened between them... "
            play sound "audio/bellring.mp3"
            " The bell has rang. Time for another class. "
            " You get up from where you were sitting and you walked back to your classroom. "
            pause 2.0
            jump scienceclass3
        else:
            x " Hiya, [name]! "
            x " Hello there, [name]. "
            x " I think we haven't introduced ourselves to [them], no? "
            x " Mmmm...yeah, I don't think so. "
            x " Let's introduce ourselves then! "
            $ popularknow = True
            p " I'm Petunia - The very cute bunny. And this is my friend, Lizzy! She's also cute!"
            lz " And ... wait, aren't I {i}VERY{/i} cute too? "
            p " Uh...yeah...very cute. Anyway!"
            p " Me and Lizzy were just gossiping, as per usual. "
            hide lizzyneutral at bottom
            show lizzyconfused at right
            lz " Yeahuh...wait, what is that smell? "
            hide petunianeutral at bottom
            show petuniaconfused at left
            p " Huh? what do you mean? "
            p " I don't smell anything... "
            hide lizzyconfused at bottom
            show lizzyneutral at right
            lz " Well, you know what they say. "
            lz " If you can't smell anything, then it must've been coming from you. "
            p " What?! "
            p " I'm pretty sure I've only heard my grandmama say that... "
            p " I mean, I know I forgot to take a shower today, but It can't smell that bad, right? "
            p " It's just a day after all.. It can't be that bad. "
            lz " ...For a day? how does that even happen? "
            p " ...Let's just say that I forgot. "
            p " Of course I wouldn't want to go to school without taking a bath! "
            p " I just forgot today, alright?! "
            p " And that smell is most DEFINITELY not coming from me. "
            lz " ...Okay, sure. "
            scene black with dissolve
            " You spent the rest of the break talking with Petunia and Lizzy. "
            " As you talked with them, you can't help but feel the very obvious tension in the air. "
            " Wonder what happened between them... "
            play sound "audio/bellring.mp3"
            " The bell has rang. Time for another class. "
            " You get up from where you were sitting and you walked back to your classroom. "
            pause 2.0
            jump scienceclass3
    label wrap:
        " You walked up to him and sat down next to him... "
        " Looks like he's a bit worried about something. Let's see what he's worrying over. "
        show engelsad at center with easeinright
        if engelknow == True:
            " You looked over to him and asked him what was wrong. "
            " Let's see if you could help him out... "
            e " Hm? oh, uh...[name], hello. "
            e " Sorry, it's just that I've been deep in my thoughts recently... "
            e " The reason why? well.. "
            e " You know my friend Claire, right? "
            e " Well...you seee... "
            e " She's been feeling down recently. "
            e " I've never seen her this upset over anything. "
            e " Sure, I've seen her being upset over getting a low score on tests before, but... "
            e " Those times, she could just...I don't know how to describe it. "
            e " She could just cheer herself up about it after a few minutes. But this...? "
            e " I don't think she can cheer herself up with how things are going... "
            e " I think I understand the reason why she's so upset, but... "
            e " I don't think that you'll like the reason why. "
            e " I'll just say... "
            e " It has something to do with the missing student. "
            hide engelsad at bottom
            show engelneutral at center
            e " ...But, um... "
            e " I'm wondering what I can do to cheer her up... "
            e " I don't like seeing that frown on her face. "
            e " I've tried everything I could to get her to smile - "
            e " Buying her icecream... tickling her... telling her some jokes... "
            e " None of it worked. I'm honestly starting to lose a bit of hope here... "
            " You wonder what the reason could be on why Claire's been feeling so down lately... "
            " Maybe it's something you should check out later. "
            " For now, you've got to give Engel some cheering up advice. "
            scene black with dissolve
            " You spent the rest of the break talking to Engel. "
            " As you were talking with him, you couldn't help but be curious on what his idea was... "
            " Again, it's probably something you should look into later. Or not. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get up from where you were sitting and you walked back to your classroom. "
            pause 2.0
            jump scienceclass3
        else:
            " You looked over to him and asked him what was wrong. "
            " Let's see if you could help him out... "
            x " Hm? oh, uh...[name], hello. "
            x " Sorry, it's just that I've been deep in my thoughts recently... "
            $ engelknow = True
            e " I'm Engel, by the way. We're classmates. "
            " You told him that it was nice to meet him, then asked what he was thinking about. "
            e " What I was thinking about? Well... "
            e " You know my friend Claire, right? "
            e " She's the girl with a bow...and she has short hair. "
            e " Well...you seee... "
            e " She's been feeling down recently. "
            e " I've never seen her this upset over anything. "
            e " Sure, I've seen her being upset over getting a low score on tests before, but... "
            e " Those times, she could just...I don't know how to describe it. "
            e " She could just cheer herself up about it after a few minutes. But this...? "
            e " I don't think she can cheer herself up with how things are going... "
            e " I think I understand the reason why she's so upset, but... "
            e " I don't think that you'll like the reason why. "
            e " I'll just say... "
            e " It has something to do with the missing student. "
            hide engelsad at bottom
            show engelneutral at center
            e " ...But, um... "
            e " I'm wondering what I can do to cheer her up... "
            e " I don't like seeing that frown on her face. "
            e " I've tried everything I could to get her to smile - "
            e " Buying her icecream... tickling her... telling her some jokes... "
            e " None of it worked. I'm honestly starting to lose a bit of hope here... "
            " You wonder what the reason could be on why Claire's been feeling so down lately... "
            " Maybe it's something you should check out later. "
            " For now, you've got to give Engel some cheering up advice. "
            scene black with dissolve
            " You spent the rest of the break talking to Engel. "
            " As you were talking with him, you couldn't help but be curious on what his idea was... "
            " Again, it's probably something you should look into later. Or not. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You get up from where you were sitting and you walked back to your classroom. "
            pause 2.0
            jump scienceclass3
label wedrooftop2:
    # bubble and lana
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked up to the rooftop and saw two of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if bubbleknow == True and lanaknow == True:
        menu:
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump arming
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump warmering
    elif bubbleknow == True and lanaknow == False:
        menu:
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump arming
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump warmering
    elif bubbleknow == False and lanaknow == True:
        menu:
            " {image=bubbleicon} A girl made out of bubbles {image=bubbleicon} ":
                jump arming
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump warmering
    else:
        menu:
            " {image=bubbleicon} A girl made out of bubbles {image=bubbleicon} ":
                jump arming
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump warmering
    label arming:
        " You walked up to her to see what she was doing. "
        show bubbleneutral at center with easeinright
        if bubbleknow == True:
            b " Oh, heya [name]!! "
            b " Sorry, was just trying to distract myself from the whole Oliver situation. "
            b " Have you heard about this game? It's called...forsakened. "
            b " Basically, to sum it up to you - It's a game where each round there's a killer, right? "
            hide bubbleneutral at bottom
            show bubbleamazed at center
            b " And the rest of the players are survivors who do generators to lessen the timer! "
            hide bubbleamazed at bottom
            show bubbleneutral at center
            b " If the timer goes to zero, then the survivors win, of course. "
            b " Buuut, if the killer kills everyone, then the killer wins! "
            b " Of course they're not gonna win if they don't manage to kill everyone, you know. "
            b " There's going to be this new update adding a bunch of stuff... "
            hide bubbleneutral at bottom
            show bubblehappy at center
            b " Like a new killer named LiNo! and a bunch of emotes and skins, and of course, a whole new map! "
            b " Of course they're adding in some more lore to the characters, too. "
            b " It's such a good game...and it's all made on Boblox!! "
            hide bubblehappy at bottom
            show bubbleneutral at center
            b " You should really go ahead and check everything out, [name]. "
            b " You could join me and play with me tonight! "
            b " ...Though, that's only if ever my parents would let me stay up tonight. "
            b " Still though! Go check it out on your own!! "
            scene black with dissolve
            " You spent the rest of the break having a talk with Bubble about this game she's interested in. "
            " Honestly, maybe you should check it out in a bit, it sounds cool. "
            " All you gotta do is just hop on Roblox and search up Forsaken. Wait, wrong game, sorry. "
            " Totally not a reference to anything cool. "
            " Totally. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit of talking. "
            " You get down from the rooftop, and then you start walking back to your classroom for the next class. "
            pause 2.0
            jump scienceclass3
        else:
            x " Oh, heya [name]!! "
            x " Sorry, was just trying to distract myself from the whole Oliver situation. "
            $ bubbleknow = True
            b " I'm Bubble, by the way! We're classmates, heheh. "
            b " Have you heard about this game? It's called...forsakened. "
            b " Basically, to sum it up to you - It's a game where each round there's a killer, right? "
            hide bubbleneutral at bottom
            show bubbleamazed at center
            b " And the rest of the players are survivors who do generators to lessen the timer! "
            hide bubbleamazed at bottom
            show bubbleneutral at center
            b " If the timer goes to zero, then the survivors win, of course. "
            b " Buuut, if the killer kills everyone, then the killer wins! "
            b " Of course they're not gonna win if they don't manage to kill everyone, you know. "
            b " There's going to be this new update adding a bunch of stuff... "
            hide bubbleneutral at bottom
            show bubblehappy at center
            b " Like a new killer named LiNo! and a bunch of emotes and skins, and of course, a whole new map! "
            b " Of course they're adding in some more lore to the characters, too. "
            b " It's such a good game...and it's all made on Boblox!! "
            hide bubblehappy at bottom
            show bubbleneutral at center
            b " You should really go ahead and check everything out, [name]. "
            b " You could join me and play with me tonight! "
            b " ...Though, that's only if ever my parents would let me stay up tonight. "
            b " Still though! Go check it out on your own!! "
            scene black with dissolve
            " You spent the rest of the break having a talk with Bubble about this game she's interested in. "
            " Honestly, maybe you should check it out in a bit, it sounds cool. "
            " All you gotta do is just hop on Roblox and search up Forsaken. Wait, wrong game, sorry. "
            " Totally not a reference to anything cool. "
            " Totally. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit of talking. "
            " You get down from the rooftop, and then you start walking back to your classroom for the next class. "
            pause 2.0
            jump scienceclass3
    label warmering:
        " You walked up to her to see what she was doing. "
        show lananeutral at center with easeinleft
        if lanaknow == True:
            l " Hello, hellooooo [name]!! "
            l " You know, going away from the whole Oliver situation... "
            hide lananeutral at bottom
            show lanahappy at center
            l " Claire gave me this really cool dating sim she found! "
            l " It's basically a sim where you date everything in your house, isn't that cool? "
            hide lanahappy at bottom
            show lananeutral at center
            l " Well, uh... "
            l " First of all, you get these very cool glasses, right? "
            l " They just sorta came from this hacker that texted you one day...don't ask why. "
            hide lananeutral at bottom
            show lanahappy at center
            l " You put them on and - WOW! everything you see in your house is humans now! "
            l " My personal favorite has to be Lucinda Lustrous. "
            hide lanahappy at bottom
            show lananeutral at center
            l " And uh, not to get anyone mad, but she's honestly the best character in the game. "
            l " I mean, she tells us that herself in-game, you know? "
            l " So OBVIOUSLY she just has to be the greatest character there! "
            l " Plus, I love her style and her outfit! "
            l " If you wanna check the game out, you can! I mean...their demo is free. "
            l " If you wanna get the full thing though AND see Lucinda Lasviscious, you've gotta pay for the DLC to see her. "
            l " For the normal game though, just pay for that normally. "
            l " Though I gotta warn you - the game DOES get a little frisky at times, if you know what I mean. "
            l " Make sure to get your headsets ready just incase if anything goes on! "
            l " Don't want you to accidentally get in trouble, heheh. "
            " Well, good thing you live alone. "
            " You can do whatever you want without someone judging you! "
            " Well, as long as you're not being loud. "
            " Otherwise your neighbors are gonna judge you. "
            scene black with dissolve
            " You spent the rest of the break talking to Lana about a game that she likes. "
            " You're feeling a little lonely, maybe you should check that out sometime... "
            " Though, you're also playing this game right now which means you're being lonely right now and are in need of friends. "
            " Wow dude. I mean, why have real people when you could just have fictional bros, right? "
            " ...Never mind, that's gotta be a bad mindset to have. "
            " Fictional bros are okay, but getting realistic bros are A-okay too. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for class. "
            " You get down from the rooftop, and then you start walking back to your classroom for the next class. "
            pause 2.0
            jump scienceclass3
        else:
            x " Hello, hellooooo [name]!! "
            $ lanaknow = True
            x " I don't think I've ever met you before, soooo... "
            l " I'm Lana! We're classmates! And, uh... "
            l " Going away from the whole Oliver situation... "
            hide lananeutral at bottom
            show lanahappy at center
            l " Claire gave me this really cool dating sim she found! "
            l " It's basically a sim where you date everything in your house, isn't that cool? "
            hide lanahappy at bottom
            show lananeutral at center
            l " Well, uh... "
            l " First of all, you get these very cool glasses, right? "
            l " They just sorta came from this hacker that texted you one day...don't ask why. "
            hide lananeutral at bottom
            show lanahappy at center
            l " You put them on and - WOW! everything you see in your house is humans now! "
            l " My personal favorite has to be Lucinda Lustrous. "
            hide lanahappy at bottom
            show lananeutral at center
            l " And uh, not to get anyone mad, but she's honestly the best character in the game. "
            l " I mean, she tells us that herself in-game, you know? "
            l " So OBVIOUSLY she just has to be the greatest character there! "
            l " Plus, I love her style and her outfit! "
            l " If you wanna check the game out, you can! I mean...their demo is free. "
            l " If you wanna get the full thing though AND see Lucinda Lasviscious, you've gotta pay for the DLC to see her. "
            l " For the normal game though, just pay for that normally. "
            l " Though I gotta warn you - the game DOES get a little frisky at times, if you know what I mean. "
            l " Make sure to get your headsets ready just incase if anything goes on! "
            l " Don't want you to accidentally get in trouble, heheh. "
            " Well, good thing you live alone. "
            " You can do whatever you want without someone judging you! "
            " Well, as long as you're not being loud. "
            " Otherwise your neighbors are gonna judge you. "
            scene black with dissolve
            " You spent the rest of the break talking to Lana about a game that she likes. "
            " You're feeling a little lonely, maybe you should check that out sometime... "
            " Though, you're also playing this game right now which means you're being lonely right now and are in need of friends. "
            " Wow dude. I mean, why have real people when you could just have fictional bros, right? "
            " ...Never mind, that's gotta be a bad mindset to have. "
            " Fictional bros are okay, but getting realistic bros are A-okay too. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for class. "
            " You get down from the rooftop, and then you start walking back to your classroom for the next class. "
            pause 2.0
            jump scienceclass3
label wedlibrary2:
    # riley and cubbie
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and spotted two of your classmates hanging out. "
    " You wanted to talk to one of them...who do you talk to? "
    if rileyknow == True and cubbieknow == True:
        menu:
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump robloxjumpscare
            " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                jump discordjumpscare
    elif rileyknow == True and cubbieknow == False:
        menu:
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump robloxjumpscare
            " {image=cubbieicon} A little cat guy! {image=cubbieicon} ":
                jump discordjumpscare
    elif rileyknow == False and cubbieknow == True:
        menu:
            " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                jump robloxjumpscare
            " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                jump discordjumpscare
    else:
        menu:
            " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                jump robloxjumpscare
            " {image=cubbieicon} A little cat guy! {image=cubbieicon} ":
                jump discordjumpscare
    label robloxjumpscare:
        # riley freaking out over oliver
        " You walked up to her and uh... "
        " ...Looks like she's admiring her crush. "
        " Very loudly. Hopefully your ears can last for a bit. "
        show rileyneutral at center with easeinright
        if rileyknow == True:
            ri " Hehehehe... "
            ri " Finally, some new photos to add to my collection! "
            ri " Some of these even seem like he knows that I'm there to take some pictures of him, heheh... "
            ri " I'm gonna have to put these up my wall later, all nice where I can see them...~ "
            ri " Oh, hey [name]! "
            ri " You should know what I'm doing at this point, right? ehhe... "
            ri " It's no surprise that I'm taking more photos of my dearest Oliver right now... "
            ri " I mean, he's just so handsome and smart, how could you not fall for him? "
            hide rileyneutral at bottom
            show rileymurder at center
            ri " Though if you do fall for him, I'm gonna have to put my knife up your ass. "
            hide rileymurder at bottom
            show rileyneutral at center
            ri " That ass is MINE alright? I'm not sharing him with anyone. "
            " Yeah, you kinda made that very clear from the start... "
            " ...And also she's being pretty loud, don't you think? "
            " You take a lot at the other people in the room and they just look as if... "
            " ...As if they're trying their best to ignore what Riley's saying right now. "
            " Though if you look more closer, it looks as if they've gotten used to this. "
            " Does she really talk about him this much to the point others are used to it? "
            " That should probably be very concerning. "
            ri " Anyywayyyy... "
            ri " I'm planning to make myself and Oliver some pins! "
            ri " I'm thinking that one should say: I <3 Oliver! "
            ri " That's obviously mine, of course. "
            ri " And the other one should be: I <3 Riley! "
            ri " Then me and Oliver can match!! "
            hide rileyneutral at bottom
            show rileyhappy at center
            ri " Ahhh... it's going to be so perfect!! "
            ri " Me and Oliver are going to match... "
            ri " ...And everyone in this school is going to know that me and Oliver are dating!! "
            ri " Isn't it just the sweetest idea, [name]? "
            " ...Yeah, that's great, Rileyyy... "
            scene black with dissolve
            " Well, looks like you had to deal with an earful of what Riley had to say about Oliver. "
            " The matching pins idea was actually pretty good, if only Riley and Oliver were actually dating. "
            " You're also pretty sure that Oliver would just reject her idea the moment she comes up to him. "
            " You've heard that that guy already has a girlfriend, anyhow. "
            " Of course he's going to reject her. But of course... she's not going to listen. "
            " She's far too deep into her fantasies. "
            " You're sure if Oliver went absent for a long time, then she'd probably forget about him. "
            " Too bad he had to come back so early. "
            play sound "audio/bellring.mp3"
            " The bell rings, interrupting you from your thoughts as Riley yapped to you. "
            " Before she continued on saying anything else, you walked out of the library and walked back to your classroom for the next class. "
            pause 2.0
            jump scienceclass3
        else:
            x " Hehehehe... "
            x " Finally, some new photos to add to my collection! "
            x " Some of these even seem like he knows that I'm there to take some pictures of him, heheh... "
            x " I'm gonna have to put these up my wall later, all nice where I can see them...~ "
            x " Oh, hey [name]! Not sure if we've met before or not, but erh... "
            x " Still would be good to introduce myself, no? "
            $ rileyknow = True
            ri " I'm Riley! Your very cool classmate, ANNNDDD Oliver's wife and girlfriend! "
            " How can one be someone's wife and girlfriend at the same time...? You're not sure. "
            ri " You should know what I'm doing at this point, right? ehhe... "
            ri " I mean, almost everyone here talks about what I do with my sweet Oliver! "
            ri " Some may call it weird, but I call my devotion to him impressive! "
            ri " I've loved him for about...awhile now. ANYWAY! "
            ri " It's no surprise that I'm taking more photos of my dearest Oliver right now... "
            ri " I mean, he's just so handsome and smart, how could you not fall for him? "
            hide rileyneutral at bottom
            show rileymurder at center
            ri " Though if you do fall for him, I'm gonna have to put my knife up your ass. "
            hide rileymurder at bottom
            show rileyneutral at center
            ri " That ass is MINE alright? I'm not sharing him with anyone. "
            " Yeah, you kinda made that very clear from the start... "
            " ...And also she's being pretty loud, don't you think? "
            " You take a lot at the other people in the room and they just look as if... "
            " ...As if they're trying their best to ignore what Riley's saying right now. "
            " Though if you look more closer, it looks as if they've gotten used to this. "
            " Does she really talk about him this much to the point others are used to it? "
            " That should probably be very concerning. "
            ri " Anyywayyyy... "
            ri " I'm planning to make myself and Oliver some pins! "
            ri " I'm thinking that one should say: I <3 Oliver! "
            ri " That's obviously mine, of course. "
            ri " And the other one should be: I <3 Riley! "
            ri " Then me and Oliver can match!! "
            hide rileyneutral at bottom
            show rileyhappy at center
            ri " Ahhh... it's going to be so perfect!! "
            ri " Me and Oliver are going to match... "
            ri " ...And everyone in this school is going to know that me and Oliver are dating!! "
            ri " Isn't it just the sweetest idea, [name]? "
            " ...Yeah, that's great, Rileyyy... "
            scene black with dissolve
            " Well, looks like you had to deal with an earful of what Riley had to say about Oliver. "
            " The matching pins idea was actually pretty good, if only Riley and Oliver were actually dating. "
            " You're also pretty sure that Oliver would just reject her idea the moment she comes up to him. "
            " You've heard that that guy already has a girlfriend, anyhow. "
            " Of course he's going to reject her. But of course... she's not going to listen. "
            " She's far too deep into her fantasies. "
            " You're sure if Oliver went absent for a long time, then she'd probably forget about him. "
            " Too bad he had to come back so early. "
            play sound "audio/bellring.mp3"
            " The bell rings, interrupting you from your thoughts as Riley yapped to you. "
            " Before she continued on saying anything else, you walked out of the library and walked back to your classroom for the next class. "
            pause 2.0
            jump scienceclass3
    label discordjumpscare:
        # cubbie concerned about riley since she's freaking out so loud
        " You walked up to him, and he looked as if he were cringing. "
        " Wonder why that is... "
        show cubbieneutral at center with easeinleft
        if cubbieknow == True:
            " You walked up to him and asked what was wrong. "
            cb " ... "
            hide cubbieneutral at bottom
            show cubbiesad at center
            cb " ... "
            " You were about to ask him again, before he pointed at a girl in the corner... "
            " It looked as if she had photos of something, no, someone. "
            " You were about to ask what was wrong about her, but then you hear her speak very loudly for everyone to hear in the library. "
            " At this point, you were very much wondering where the librarian was for this. "
            if rileyknow == True:
                ri " Ooooh, my sweet, sweet Oliver! "
                ri " With these sweet pins that I'm going to make for you and I... "
                ri " ...Everyone will know that we're going to be together forever! "
                ri " Oh, won't it be so wonderful? Hehehh... "
            else:
                x " Ooooh, my sweet, sweet Oliver! "
                x " With these sweet pins that I'm going to make for you and I... "
                x " ...Everyone will know that we're going to be together forever! "
                x " Oh, won't it be so wonderful? Hehehh... "
            " ...She's acting as if no one in this library can hear her right now. "
            " Honestly, you're even starting to cringe yourself. "
            " You have no idea how to ignore all of this though... "
            " And you have no idea how to spare Cubbie from hearing all of this. "
            " You have an idea form into your mind after a bit of thinking. "
            " Maybe you should just...I don't know... "
            " Leave with Cubbie and get a snack with him distract both you and him? "
            " How about it? "
            menu:
                " Let's do that ":
                    $ cubbielv += 10
                    " You nudge Cubbie on the shoulder and then pointed at the exit of the library... "
                    " ..Then asked him if he wanted to get some food. "
                    hide cubbiesad at bottom
                    show cubbieneutral at center
                    cb " ... "
                    hide cubbieneutral at bottom
                    show cubbiehappy at center
                    cb " ...!! "
                    " Looks like Cubbie agreed to that little idea of yours! "
                    " You take his hand...well, paw? I don't know how to describe it. "
                    " And you both get out of the library to get a nice snack. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Cubbie as you two shared a nice snack. "
                    " Now you both don't have to deal with all of the simping going on in the library. "
                    " You both also talked about a few things while the two of you were there. Like things such as... "
                    " What it would be like to have someone simp on you daily. "
                    " Probably a bad thing, considering how obsessive they could get. "
                    " Yeesh, you wouldn't want someone to have a room with pictures and notes all about you. "
                    " Very creepy. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for class. "
                    " You get up from where you were sitting and you walked back to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
                " Nah, I'll go to get my own snack ":
                    " You decided to leave Cubbie there to deal with the simping... "
                    " ...Just so that you yourself could get a nice snack. "
                    " Yup, you're definitely not dealing with this. "
                    " Guess Cubbie's just gonna have to figure out how to block out all of this noise by himself. "
                    scene black with dissolve
                    " You walked out of the library and you went to the cafeteria to get yourself a snack. "
                    " As you were chowing down on whatever you were eating, you decided to spend the time doomscrolling. "
                    " Amazing! Atleast now you don't have to deal with all of the simping going on the library. "
                    " ...You wonder how it's like to have someone simp on you daily. "
                    " Probably a bad thing, considering how obsessive they could get. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for class. "
                    " You get up from where you were sitting and you walked back to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
        else:
            $ cubbieknow = True
            " From what you've heard, this little guy's name was Cubbie. "
            " He also didn't prefer to speak a lot. Interesting... "
            " You walked up to him and asked what was wrong. "
            cb " ... "
            hide cubbieneutral at bottom
            show cubbiesad at center
            cb " ... "
            " You were about to ask him again, before he pointed at a girl in the corner... "
            " It looked as if she had photos of something, no, someone. "
            " You were about to ask what was wrong about her, but then you hear her speak very loudly for everyone to hear in the library. "
            " At this point, you were very much wondering where the librarian was for this. "
            if rileyknow == True:
                ri " Ooooh, my sweet, sweet Oliver! "
                ri " With these sweet pins that I'm going to make for you and I... "
                ri " ...Everyone will know that we're going to be together forever! "
                ri " Oh, won't it be so wonderful? Hehehh... "
            else:
                x " Ooooh, my sweet, sweet Oliver! "
                x " With these sweet pins that I'm going to make for you and I... "
                x " ...Everyone will know that we're going to be together forever! "
                x " Oh, won't it be so wonderful? Hehehh... "
            " ...She's acting as if no one in this library can hear her right now. "
            " Honestly, you're even starting to cringe yourself. "
            " You have no idea how to ignore all of this though... "
            " And you have no idea how to spare Cubbie from hearing all of this. "
            " You have an idea form into your mind after a bit of thinking. "
            " Maybe you should just...I don't know... "
            " Leave with Cubbie and get a snack with him distract both you and him? "
            " How about it? "
            menu:
                " Let's do that ":
                    $ cubbielv += 10
                    " You nudge Cubbie on the shoulder and then pointed at the exit of the library... "
                    " ..Then asked him if he wanted to get some food. "
                    hide cubbiesad at bottom
                    show cubbieneutral at center
                    cb " ... "
                    hide cubbieneutral at bottom
                    show cubbiehappy at center
                    cb " ...!! "
                    " Looks like Cubbie agreed to that little idea of yours! "
                    " You take his hand...well, paw? I don't know how to describe it. "
                    " And you both get out of the library to get a nice snack. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Cubbie as you two shared a nice snack. "
                    " Now you both don't have to deal with all of the simping going on in the library. "
                    " You both also talked about a few things while the two of you were there. Like things such as... "
                    " What it would be like to have someone simp on you daily. "
                    " Probably a bad thing, considering how obsessive they could get. "
                    " Yeesh, you wouldn't want someone to have a room with pictures and notes all about you. "
                    " Very creepy. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for class. "
                    " You get up from where you were sitting and you walked back to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
                " Nah, I'll go to get my own snack ":
                    " You decided to leave Cubbie there to deal with the simping... "
                    " ...Just so that you yourself could get a nice snack. "
                    " Yup, you're definitely not dealing with this. "
                    " Guess Cubbie's just gonna have to figure out how to block out all of this noise by himself. "
                    scene black with dissolve
                    " You walked out of the library and you went to the cafeteria to get yourself a snack. "
                    " As you were chowing down on whatever you were eating, you decided to spend the time doomscrolling. "
                    " Amazing! Atleast now you don't have to deal with all of the simping going on the library. "
                    " ...You wonder how it's like to have someone simp on you daily. "
                    " Probably a bad thing, considering how obsessive they could get. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for class. "
                    " You get up from where you were sitting and you walked back to your classroom for the next class. "
                    pause 2.0
                    jump scienceclass3
label scienceclass3:
    scene classroom with dissolve
    " You walked into the classroom and waited patiently for the teacher to arrive. "
    " Well, you actually didn't even have to wait. "
    " The teacher came in right after you entered the classroom and took your seat. "
    " You get out your notebook and pen, ready to take a few notes down. "
    " ...Or to just pretend that you were, and just doze off in the middle of class. "
    show missbloomieneutral at center
    msb " Alright, class. "
    msb " Get your notebooks and your pens. "
    msb " Let's start with a new lesson for today's lecture. "
    msb " If I catch you sleeping in my class, I will not hesitate to throw something at you. "
    msb " I want all of you to pay attention. "
    msb " School {i}is{/i} very important, after all. "
    msb " Let's begin our new lesson for today. "
    scene black with dissolve
    " You spent the rest of class taking down notes. "
    " Nothing too interesting happened while in class...oh wait. "
    " Wasn't there supposed to be an activity for history and music today? "
    " Well, shit. Gotta be prepared for those, then. "
    play sound "audio/bellring.mp3"
    " The bell rings, time for another break. "
    " You put your stuff back into your bag and you walk out of the classroom to go back into the hallways once more. "
    pause 2.0
    jump wedbreak3

label wedbreak3:
    scene hallway with dissolve
    " You're thinking about hanging out somewhere again. "
    " Where do you go? "
    if clairelv == 20:
        " Hey, you're close to Claire, right? "
        " Why don't you check the front of the school? seems like she's not feeling well today. "
        " Good friends check up on their homies, you know. "
        " Only if you want to check up on her though, you can go where-ever the hell you want. "
        " Your choices, dude. "
        pass
    elif clairelv >= 20:
        " Hey, you're close to Claire, right? "
        " Why don't you check the front of the school? seems like she's not feeling well today. "
        " Good friends check up on their homies, you know. "
        " Only if you want to check up on her though, you can go where-ever the hell you want. "
        " Your choices, dude. "
        pass
    else:
        pass
    if oligangjoin == True:
        " Oh wait, right. You're supposed to be with Oliver and his crew right now. "
        " Let's go there, then. "
        " He said that the spot should be at the very back of the school... "
        " Shouldn't be that far...let's go. "
        scene black with dissolve
        jump wedoligang1
    else:
        pass
    menu:
        " {image=claireicon} The front of the school {image=claireicon} ":
            jump wedfrontschool3
        " {image=engelicon} The back of the school {image=skellicon} ":
            jump wedbackschool3
        " {image=lanaicon}The gym {image=popularicon} ":
            jump wedgym3
        " {image=abbieicon} The cafeteria {image=bubbleicon} ":
            jump wedcafeteria3
        " {image=kevinicon} The rooftop {image=robbyicon} ":
            jump wedrooftop3
        " {image=rileyicon} The library {image=popularicon} ":
            jump wedlibrary3

label wedfrontschool3:
    # claire vents
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school and spotted one of your classmates. "
    " A girl with a bow, looking quite down... "
    " You're thinking about walking over to her to see what's wrong. "
    if clairebeatup == True:
        " But, like I told you, it's something that I won't allow to happen. "
        " Not until tomorrow, at least. "
        " Look forward to that, I'm gonna send you back now. "
        scene black
        pause 1.5
        jump historyclass3
    else:
        pass
    " Should you talk to her? "
    if claireknow == True:
        menu:
            " {image=claireicon} Talk to Claire {image=claireicon} ":
                jump claireventing
            " Nah, she looks like she needs space. ":
                jump claireignoring
    else:
        menu:
            " {image=claireicon} Talk to the girl {image=claireicon} ":
                jump claireventing
            " Nah, she looks like she needs space. ":
                jump claireignoring
    label claireventing:
        " Let's go and help her, then. "
        " She looks like she needs someone to talk to. "
        show clairesad at center with easeinleft
        if claireknow == True:
            c " Oh...what am I gonna do... "
            " You tap her shoulder to get your attention. "
            c " Oh, uh...? "
            hide clairesad at bottom
            show claireneutral at center
            " The moment she sees you, it's like a switch was flipped. "
            " She looked like she was worrying about nothing whatsoever... "
            " ...Seems like she's trying to make you believe that she's fine. Even though she's really not. "
            " Let's see how we can work with this. "
            c " Hey there, [name]! "
            c " Sorry, sorry...was just thinking about school stuff. "
            c " Man, everything's been so stressful now, huh? "
            c " Like, we've had tests...assignments here and there... "
            hide claireneutral at bottom
            show clairehappy at center
            c " I mean, of course we have assignments! Silly me. "
            c " I keep on forgetting nowadays, haha... "
            c " Forgetting about assignments really are a bad thing, right [name]? "
            " ...This isn't really convincing you that she's fine. "
            " You breathe in and tell her... "
            if kind == True:
                " Look, Claire... "
                " ...You can tell me if anything's wrong. "
                " We're friends, right? "
            elif calm == True:
                " Look, dudettee... "
                " You don't have to keep pushing yerself and keep telling yersef that everything's fine. "
                " You can tell me if anything's wrong. "
            elif mean == True:
                " Claire. You can tell me if anything's wrong. "
            else:
                ""
            c " Eeh...? what're you saying, [name]? "
            c " I'm a hundred percent fine! "
            c " You don't need to worry about me, trust me on that. "
            if clairelv >= 20 or clairelv == 20:
                " Claire stares at you, as if she was expecting for you to believe her. "
                " Though, it looks as if she knew that she can't just keep this lie going on forever.. "
                hide claireneutral at bottom
                show clairesad at center
                stop music fadeout 1.5
                " ...The lie that she was doing fine, and that everything was fine. "
                " Her smile crumbles back into a frown, something that you usually don't see on her, if you knew her well. "
                " And honestly, a frown doesn't really suit her looks. "
                " You've gotta find a way to make her feel better, but first... "
                " You have to listen to what she has to say. "
                play music "audio/emotionalmoment.mp3" fadein 1.5
                c " ...I knew you wouldn't believe my lies, [name]... "
                c " You're too smart to fall for anything like a simple lie of: 'Im doing fine'. "
                c " I was still hoping that you would just... "
                c " Fall for them at one point and believe that I'm doing okay. "
                c " So that you wouldn't have to worry about me. "
                c " ...I know you're wondering why I've been so upset lately, so... "
                c " ...I'll tell you. Even if I don't like what I'm gonna say to you myself. "
                c " The truth is... "
                c " Ah, I don't know how to start this, um... "
                c " ...You know that student that has recently gone missing...? "
                c " ...I'm worried a lot about them. "
                c " But that's not the only thing that I've been worrying about. "
                c " I've been also worrying about...you. "
                c " You've been a really great classmate here, [name], and... "
                c " I don't know what you're going to think of this school after I tell you what I'm about to say, but... "
                c " I know the reason why that student went missing. "
                c " You see... "
                c " This school isn't like other schools. You get a failing grade... "
                c " ...And you get hunted down by one of the teachers. "
                c " That's what happened to that student. They've always got low grades on every single subject. "
                c " We've tried to warn them, but they wouldn't listen. "
                c " And...it eventually lead to their demise, cutting their life short. "
                c " Of course I'm upset about them but...I'm also upset at the thought of you leaving because of the fact that I just told you what happens when you fail. "
                c " You've been a very great classmate, like I said. "
                c " And...I wouldn't want you to leave anytime soon. You always manage to bring a smile to my face... "
                c " You make me laugh sometimes...you're wonderful to have. "
                c " And I know that it's only your third day of being here, so you could just easily make up a decision and..leave. "
                c " I've been trying to avoid telling you the real reason why that one student went missing.. "
                c " ...Just so that you could stay a little longer, until you eventually find out. "
                c " But now that you know... "
                stop music fadeout 1.5
                c " Are you...gonna still be in this school, despite it's dangers? "
                menu:
                    " I'll stay with you, no matter what ":
                        $ clairelv += 10
                        " Claire seemed to be a little surprised by your decision. "
                        " I mean, it's understandable since any sane person would want to leave this school due to what you just heard. "
                        play music "audio/paperhigh.mp3" fadein 1.5
                        hide clairesad at bottom
                        show claireneutral at center
                        " But, after a few moments, that sweet smile of hers comes back onto her face. "
                        c " Eh...are you serious? "
                        c " I mean, if you get low grades, you're gonna be killed - "
                        c " - I most certainly don't want that to happen - "
                        " Claire starts to ramble to herself about a few things that could happen. "
                        " Though eventually, she comes back to her senses and takes a deep breath. "
                        c " ...Ooookay... "
                        c " Well, if you really want to stay, I could help you out on your homework if you ever forget to do one of them! "
                        c " Just, eh...don't tell the teachers that I'm helping you, alright? "
                        c " You have no idea how mad they're going to be, hah... "
                        c " You're safe with me and my friends on your side, though! "
                        scene black with dissolve
                        " Seems like you've done a pretty good job at making Claire feel better. "
                        " You spent the rest of the day talking with a nice and happy Claire... "
                        " A happy Claire is better than a sad one. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, time for class. "
                        " You walked back into the school with Claire to go to your next class. "
                        pause 2.0
                        jump historyclass3
            else:
                # if does not meet requirements, then claire ignores you
                c " Ooooh, you know I found this really cool book in the library! "
                c " It's about these three kpop stars fighting demons and stuff... "
                c " Some people think that it's boring, but I think the writing is great! "
                c " There's also this rival boy band and they turn out to be demons and stuff... "
                " Claire starts to ramble on and on about this book, not giving you a chance to speak. "
                " She's really putting in effort just so that you could forget about what you were going to say to her... "
                " Wait, what were you gonna tell her? You forgot already. "
                " You decided to just talk with Claire about the book for now, maybe you can rememberwhat you were going to say to her later... "
                scene black with dissolve
                " You spent the rest of the day talking with a nice and happy Claire... "
                " ...Even though you knew that she wasn't feeling happy on the inside. "
                " Someone should really talk to her so that she could feel better. "
                " Like that one gy she always hangs out with, for example. "
                play sound "audio/bellring.mp3"
                " The bell rings, time for class. "
                " You walked back into the school with Claire to go to your next class. "
                pause 2.0
                jump historyclass3
        else:
            x " Oh...what am I gonna do... "
            " You tap her shoulder to get your attention. "
            x " Oh, uh...? "
            hide clairesad at bottom
            show claireneutral at center
            " The moment she sees you, it's like a switch was flipped. "
            " She looked like she was worrying about nothing whatsoever... "
            " ...Seems like she's trying to make you believe that she's fine. Even though she's really not. "
            " Let's see how we can work with this. "
            x " Hey there, [name]! "
            x " Sorry, sorry...was just thinking about school stuff. "
            $ claireknow = True
            c " Oh dear, I forgot to introduce myself! I'm Claire, haha. "
            c " I'm your classmate! Sorry, my mind's just been so cluttered to the point that it's hard to remember certain things, hehe... "
            c " Man, everything's been so stressful now, huh? "
            c " Like, we've had tests...assignments here and there... "
            hide claireneutral at bottom
            show clairehappy at center
            c " I mean, of course we have assignments! Silly me. "
            c " I keep on forgetting nowadays, haha... "
            c " Forgetting about assignments really are a bad thing, right [name]? "
            " ...This isn't really convincing you that she's fine. "
            " You breathe in and tell her... "
            if kind == True:
                " Look, Claire... "
                " ...You can tell me if anything's wrong. "
                " We're friends, right? "
            elif calm == True:
                " Look, dudettee... "
                " You don't have to keep pushing yerself and keep telling yersef that everything's fine. "
                " You can tell me if anything's wrong. "
            elif mean == True:
                " Claire. You can tell me if anything's wrong. "
            else:
                ""
            c " Eeh...? what're you saying, [name]? "
            c " I'm a hundred percent fine! "
            c " You don't need to worry about me, trust me on that. "
            if clairelv >= 20 or clairelv == 20:
                " Claire stares at you, as if she was expecting for you to believe her. "
                " Though, it looks as if she knew that she can't just keep this lie going on forever.. "
                hide claireneutral at bottom
                show clairesad at center
                stop music fadeout 1.5
                " ...The lie that she was doing fine, and that everything was fine. "
                " Her smile crumbles back into a frown, something that you usually don't see on her, if you knew her well. "
                " And honestly, a frown doesn't really suit her looks. "
                " You've gotta find a way to make her feel better, but first... "
                " You have to listen to what she has to say. "
                play music "audio/emotionalmoment.mp3" fadein 1.5
                c " ...I knew you wouldn't believe my lies, [name]... "
                c " You're too smart to fall for anything like a simple lie of: 'Im doing fine'. "
                c " I was still hoping that you would just... "
                c " Fall for them at one point and believe that I'm doing okay. "
                c " So that you wouldn't have to worry about me. "
                c " ...I know you're wondering why I've been so upset lately, so... "
                c " ...I'll tell you. Even if I don't like what I'm gonna say to you myself. "
                c " The truth is... "
                c " Ah, I don't know how to start this, um... "
                c " ...You know that student that has recently gone missing...? "
                c " ...I'm worried a lot about them. "
                c " But that's not the only thing that I've been worrying about. "
                c " I've been also worrying about...you. "
                c " You've been a really great classmate here, [name], and... "
                c " I don't know what you're going to think of this school after I tell you what I'm about to say, but... "
                c " I know the reason why that student went missing. "
                c " You see... "
                c " This school isn't like other schools. You get a failing grade... "
                c " ...And you get hunted down by one of the teachers. "
                c " That's what happened to that student. They've always got low grades on every single subject. "
                c " We've tried to warn them, but they wouldn't listen. "
                c " And...it eventually lead to their demise, cutting their life short. "
                c " Of course I'm upset about them but...I'm also upset at the thought of you leaving because of the fact that I just told you what happens when you fail. "
                c " You've been a very great classmate, like I said. "
                c " And...I wouldn't want you to leave anytime soon. You always manage to bring a smile to my face... "
                c " You make me laugh sometimes...you're wonderful to have. "
                c " And I know that it's only your third day of being here, so you could just easily make up a decision and..leave. "
                c " I've been trying to avoid telling you the real reason why that one student went missing.. "
                c " ...Just so that you could stay a little longer, until you eventually find out. "
                c " But now that you know... "
                stop music fadeout 1.5
                c " Are you...gonna still be in this school, despite it's dangers? "
                menu:
                    " I'll stay with you, no matter what ":
                        $ clairelv += 10
                        " Claire seemed to be a little surprised by your decision. "
                        " I mean, it's understandable since any sane person would want to leave this school due to what you just heard. "
                        play music "audio/paperhigh.mp3" fadein 1.5
                        hide clairesad at bottom
                        show claireneutral at center
                        " But, after a few moments, that sweet smile of hers comes back onto her face. "
                        c " Eh...are you serious? "
                        c " I mean, if you get low grades, you're gonna be killed - "
                        c " - I most certainly don't want that to happen - "
                        " Claire starts to ramble to herself about a few things that could happen. "
                        " Though eventually, she comes back to her senses and takes a deep breath. "
                        c " ...Ooookay... "
                        c " Well, if you really want to stay, I could help you out on your homework if you ever forget to do one of them! "
                        c " Just, eh...don't tell the teachers that I'm helping you, alright? "
                        c " You have no idea how mad they're going to be, hah... "
                        c " You're safe with me and my friends on your side, though! "
                        scene black with dissolve
                        " Seems like you've done a pretty good job at making Claire feel better. "
                        " You spent the rest of the day talking with a nice and happy Claire... "
                        " A happy Claire is better than a sad one. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, time for class. "
                        " You walked back into the school with Claire to go to your next class. "
                        pause 2.0
                        jump historyclass3
            else:
                # if does not meet requirements, then claire ignores you
                c " Ooooh, you know I found this really cool book in the library! "
                c " It's about these three kpop stars fighting demons and stuff... "
                c " Some people think that it's boring, but I think the writing is great! "
                c " There's also this rival boy band and they turn out to be demons and stuff... "
                " Claire starts to ramble on and on about this book, not giving you a chance to speak. "
                " She's really putting in effort just so that you could forget about what you were going to say to her... "
                " Wait, what were you gonna tell her? You forgot already. "
                " You decided to just talk with Claire about the book for now, maybe you can rememberwhat you were going to say to her later... "
                scene black with dissolve
                " You spent the rest of the day talking with a nice and happy Claire... "
                " ...Even though you knew that she wasn't feeling happy on the inside. "
                " Someone should really talk to her so that she could feel better. "
                " Like that one gy she always hangs out with, for example. "
                play sound "audio/bellring.mp3"
                " The bell rings, time for class. "
                " You walked back into the school with Claire to go to your next class. "
                pause 2.0
                jump historyclass3
    label claireignoring:
        " Yeah, she {i}does{/i} look like she needs space... "
        " Let's leave her alone, for now. "
        " You sit on a nearby bench and get yourself distracted on your phone. "
        " Time to go on another session of doomscrolling... "
        scene black with dissolve
        " You spent the rest of the break doomscrolling on your phone. "
        " Though, as you were, you could hear the girl talking about something. "
        " Not sure what it's about, but you heard your name being mentioned at one point. "
        " How odd... "
        " It's best not to think too hard about it though. "
        " Can't go around making assumptions of what people think of you, you know. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You get up from the bench you were sitting on and you walked back to your classroom. "
        pause 2.0
        jump historyclass3

label wedbackschool3:
    # engel, skell - engel wants to know more about skell
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of your school and you found your two classmates hanging out with eachother. "
    " Curious, you decided to hang out with them aswell. Well, uh...if they let you hang out with them, that is. "
    " Hopefully they do. "
    show engelhappy at left with easeinright
    show skellneutral at right with easeinright
    if engelknow == True and skellknow == True:
        e " Hey there, [name]. "
        sk " Oh, uh...[name]'s here? Hi. "
        " You said hello to the both of them, and asked them what they were doing. "
        e " I was just asking Skell a few things about himself! "
        e " I want to be a good student and learn a lot about my classmates, you know. "
        e " Who knows - they might be good at something unexpected! "
        sk " Ehh...though, it's been kind of...more like you're annoying me a bit. "
        hide engelhappy at bottom
        show engelneutral at left
        e " Oh...annoying you? "
        e " I'm sorry if I'm asking too much questions, Skell. "
        sk " It's alright, I know you mean no harm. "
        sk " It's just... "
        hide skellneutral at bottom
        show skellsad at right
        sk " Why would you want to know stuff about me? "
        e " I mean...why would I not want to? "
        e " You've got an interesting character, Skell. "
        sk " ...Interesting? I don't really see that in myself. "
        sk " I'm just your average emo teenager, you know. "
        sk " There's nothing special about me whatsoever... "
        e " Come on, Skell! Don't talk bad about yourself like that... "
        hide engelneutral at bottom
        show engelhappy at left
        e " I think everyone's special in their own way! "
        e " I mean, look at you! "
        e " Does anyone have a tail and wings at the same time? "
        e " I mean...birds do, but still! "
        e " You've got your own style and personality that others like me, well...like! "
        e " So don't put yourself down like that, okay? "
        e " There will be always others who don't like you, ands that's fine because that's jsut how life works! "
        sk " I, uh...really appreciate all of your words, but... "
        sk " All of those things you just said about me kinda seems unnecessary. "
        sk " You could just be saying that to someone else instead of someone like me. "
        e " ... (Psst, [name]!) "
        e " (Say something here!) "
        menu:
            " (Say something) ":
                $ skelllv += 10
                " You actually managed to say something so flattering to Skell. "
                hide skellsad at bottom
                show skellsurprised at right
                " So flattering, that it causes his mind to get all confused with your words. "
                " Seems like he hasn't had anyone tell him something as flattering as THAT in a good while. "
                sk " ...Huh? What? "
                sk " I- ???????????????? "
                hide engelhappy at bottom
                show engelcontent at left
                e " Oh, heheh... [name], I think you overdid that a bit. "
                e " But there's nothing wrongwith a little flattery here and there, right? "
                e " Now uh, let's just figure out how to get Skell to become normal again. "
                scene black with dissolve
                " You spent the rest of the break trying to get Skell's brain to function properly. "
                " Geez, is this really how powerful your words are? "
                " Words are powerful, but actions are, too. "
                play sound "audio/bellring.mp3"
                " The bell rings after you get Skell to work properly. "
                " You then went back into your school so that you could go to your next class. "
                pause 2.0
                jump historyclass3
            " (Say nothing) ":
                " You chose not to say anything. "
                " Looks like Engel's gonna have to do all the talking for now... "
                scene black with dissolve
                " You spent the rest of the break hearing Engel try to convince Skell to say something positive about himself. "
                " It did work, but only just a bit. "
                " Huh...you wonder how low Skell's self esteem was or something. "
                " Annnnd once again, I have no words to say here. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You went back into the school so that you could go to your next class. "
                pause 2.0
                jump historyclass3
    elif engelknow == True and skellknow == False:
        e " Hey there, [name]. "
        x " Oh, uh...[name]'s here? Hi. "
        " You said hello to the both of them, and asked them what they were doing. "
        $ skellknow = True
        e " I was just asking Skell a few things about himself! "
        e " I want to be a good student and learn a lot about my classmates, you know. "
        e " Who knows - they might be good at something unexpected! "
        sk " Ehh...though, it's been kind of...more like you're annoying me a bit. "
        hide engelhappy at bottom
        show engelneutral at left
        e " Oh...annoying you? "
        e " I'm sorry if I'm asking too much questions, Skell. "
        sk " It's alright, I know you mean no harm. "
        sk " It's just... "
        hide skellneutral at bottom
        show skellsad at right
        sk " Why would you want to know stuff about me? "
        e " I mean...why would I not want to? "
        e " You've got an interesting character, Skell. "
        sk " ...Interesting? I don't really see that in myself. "
        sk " I'm just your average emo teenager, you know. "
        sk " There's nothing special about me whatsoever... "
        e " Come on, Skell! Don't talk bad about yourself like that... "
        hide engelneutral at bottom
        show engelhappy at left
        e " I think everyone's special in their own way! "
        e " I mean, look at you! "
        e " Does anyone have a tail and wings at the same time? "
        e " I mean...birds do, but still! "
        e " You've got your own style and personality that others like me, well...like! "
        e " So don't put yourself down like that, okay? "
        e " There will be always others who don't like you, ands that's fine because that's jsut how life works! "
        sk " I, uh...really appreciate all of your words, but... "
        sk " All of those things you just said about me kinda seems unnecessary. "
        sk " You could just be saying that to someone else instead of someone like me. "
        e " ... (Psst, [name]!) "
        e " (Say something here!) "
        menu:
            " (Say something) ":
                $ skelllv += 10
                " You actually managed to say something so flattering to Skell. "
                hide skellsad at bottom
                show skellsurprised at right
                " So flattering, that it causes his mind to get all confused with your words. "
                " Seems like he hasn't had anyone tell him something as flattering as THAT in a good while. "
                sk " ...Huh? What? "
                sk " I- ???????????????? "
                hide engelhappy at bottom
                show engelcontent at left
                e " Oh, heheh... [name], I think you overdid that a bit. "
                e " But there's nothing wrongwith a little flattery here and there, right? "
                e " Now uh, let's just figure out how to get Skell to become normal again. "
                scene black with dissolve
                " You spent the rest of the break trying to get Skell's brain to function properly. "
                " Geez, is this really how powerful your words are? "
                " Words are powerful, but actions are, too. "
                play sound "audio/bellring.mp3"
                " The bell rings after you get Skell to work properly. "
                " You then went back into your school so that you could go to your next class. "
                pause 2.0
                jump historyclass3
            " (Say nothing) ":
                " You chose not to say anything. "
                " Looks like Engel's gonna have to do all the talking for now... "
                scene black with dissolve
                " You spent the rest of the break hearing Engel try to convince Skell to say something positive about himself. "
                " It did work, but only just a bit. "
                " Huh...you wonder how low Skell's self esteem was or something. "
                " Annnnd once again, I have no words to say here. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You went back into the school so that you could go to your next class. "
                pause 2.0
                jump historyclass3
    elif engelknow == False and skellknow == True:
        x " Hey there, [name]. "
        sk " Oh, uh...[name]'s here? Hi. "
        " You said hello to the both of them, and asked them what they were doing. "
        x " I was just asking Skell a few things about himself! "
        x " I want to be a good student and learn a lot about my classmates, you know. "
        x " Who knows - they might be good at something unexpected! "
        $ engelknow = True
        sk " Ehh...though, it's been kind of...more like you're annoying me a bit, Engel. "
        hide engelhappy at bottom
        show engelneutral at left
        e " Oh...annoying you? "
        e " I'm sorry if I'm asking too much questions, Skell. "
        sk " It's alright, I know you mean no harm. "
        sk " It's just... "
        hide skellneutral at bottom
        show skellsad at right
        sk " Why would you want to know stuff about me? "
        e " I mean...why would I not want to? "
        e " You've got an interesting character, Skell. "
        sk " ...Interesting? I don't really see that in myself. "
        sk " I'm just your average emo teenager, you know. "
        sk " There's nothing special about me whatsoever... "
        e " Come on, Skell! Don't talk bad about yourself like that... "
        hide engelneutral at bottom
        show engelhappy at left
        e " I think everyone's special in their own way! "
        e " I mean, look at you! "
        e " Does anyone have a tail and wings at the same time? "
        e " I mean...birds do, but still! "
        e " You've got your own style and personality that others like me, well...like! "
        e " So don't put yourself down like that, okay? "
        e " There will be always others who don't like you, ands that's fine because that's jsut how life works! "
        sk " I, uh...really appreciate all of your words, but... "
        sk " All of those things you just said about me kinda seems unnecessary. "
        sk " You could just be saying that to someone else instead of someone like me. "
        e " ... (Psst, [name]!) "
        e " (Say something here!) "
        menu:
            " (Say something) ":
                $ skelllv += 10
                " You actually managed to say something so flattering to Skell. "
                hide skellsad at bottom
                show skellsurprised at right
                " So flattering, that it causes his mind to get all confused with your words. "
                " Seems like he hasn't had anyone tell him something as flattering as THAT in a good while. "
                sk " ...Huh? What? "
                sk " I- ???????????????? "
                hide engelhappy at bottom
                show engelcontent at left
                e " Oh, heheh... [name], I think you overdid that a bit. "
                e " But there's nothing wrongwith a little flattery here and there, right? "
                e " Now uh, let's just figure out how to get Skell to become normal again. "
                scene black with dissolve
                " You spent the rest of the break trying to get Skell's brain to function properly. "
                " Geez, is this really how powerful your words are? "
                " Words are powerful, but actions are, too. "
                play sound "audio/bellring.mp3"
                " The bell rings after you get Skell to work properly. "
                " You then went back into your school so that you could go to your next class. "
                pause 2.0
                jump historyclass3
            " (Say nothing) ":
                " You chose not to say anything. "
                " Looks like Engel's gonna have to do all the talking for now... "
                scene black with dissolve
                " You spent the rest of the break hearing Engel try to convince Skell to say something positive about himself. "
                " It did work, but only just a bit. "
                " Huh...you wonder how low Skell's self esteem was or something. "
                " Annnnd once again, I have no words to say here. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You went back into the school so that you could go to your next class. "
                pause 2.0
                jump historyclass3
    else:
        x " Hey there, [name]. "
        x " Oh, uh...[name]'s here? Hi. "
        " You said hello to the both of them, and asked them what they were doing. "
        $ skellknow = True
        x " I was just asking Skell a few things about himself! "
        x " I want to be a good student and learn a lot about my classmates, you know. "
        x " Who knows - they might be good at something unexpected! "
        $ engelknow = True
        sk " Ehh...though, it's been kind of...more like you're annoying me a bit, Engel. "
        hide engelhappy at bottom
        show engelneutral at left
        e " Oh...annoying you? "
        e " I'm sorry if I'm asking too much questions, Skell. "
        sk " It's alright, I know you mean no harm. "
        sk " It's just... "
        hide skellneutral at bottom
        show skellsad at right
        sk " Why would you want to know stuff about me? "
        e " I mean...why would I not want to? "
        e " You've got an interesting character, Skell. "
        sk " ...Interesting? I don't really see that in myself. "
        sk " I'm just your average emo teenager, you know. "
        sk " There's nothing special about me whatsoever... "
        e " Come on, Skell! Don't talk bad about yourself like that... "
        hide engelneutral at bottom
        show engelhappy at left
        e " I think everyone's special in their own way! "
        e " I mean, look at you! "
        e " Does anyone have a tail and wings at the same time? "
        e " I mean...birds do, but still! "
        e " You've got your own style and personality that others like me, well...like! "
        e " So don't put yourself down like that, okay? "
        e " There will be always others who don't like you, ands that's fine because that's jsut how life works! "
        sk " I, uh...really appreciate all of your words, but... "
        sk " All of those things you just said about me kinda seems unnecessary. "
        sk " You could just be saying that to someone else instead of someone like me. "
        e " ... (Psst, [name]!) "
        e " (Say something here!) "
        menu:
            " (Say something) ":
                $ skelllv += 10
                " You actually managed to say something so flattering to Skell. "
                hide skellsad at bottom
                show skellsurprised at right
                " So flattering, that it causes his mind to get all confused with your words. "
                " Seems like he hasn't had anyone tell him something as flattering as THAT in a good while. "
                sk " ...Huh? What? "
                sk " I- ???????????????? "
                hide engelhappy at bottom
                show engelcontent at left
                e " Oh, heheh... [name], I think you overdid that a bit. "
                e " But there's nothing wrongwith a little flattery here and there, right? "
                e " Now uh, let's just figure out how to get Skell to become normal again. "
                scene black with dissolve
                " You spent the rest of the break trying to get Skell's brain to function properly. "
                " Geez, is this really how powerful your words are? "
                " Words are powerful, but actions are, too. "
                play sound "audio/bellring.mp3"
                " The bell rings after you get Skell to work properly. "
                " You then went back into your school so that you could go to your next class. "
                pause 2.0
                jump historyclass3
            " (Say nothing) ":
                " You chose not to say anything. "
                " Looks like Engel's gonna have to do all the talking for now... "
                scene black with dissolve
                " You spent the rest of the break hearing Engel try to convince Skell to say something positive about himself. "
                " It did work, but only just a bit. "
                " Huh...you wonder how low Skell's self esteem was or something. "
                " Annnnd once again, I have no words to say here. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You went back into the school so that you could go to your next class. "
                pause 2.0
                jump historyclass3

label wedgym3:
    # lana, petunia - petunia tries to hang out with lana
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym and spotted two of your classmates hanging out with eachother. "
    " You wanted to talk to them, so you walked over to them and sat next to them on the bleachers. "
    " Hey, wait...isn't that bunny girl supposed to be with her best friend or something right now? "
    " Odd. Let's ask about that in a bit. "
    show petunianeutral at right with easeinleft
    show lananeutral at left with easeinleft
    if popularknow == True and lanaknow == True:
        hide petunianeutral at bottom
        show petuniasurprised at right
        p " Oh? and what happened next? "
        p " What happened to Juliana and Pedro? "
        hide lananeutral at bottom
        show lanahappy at left
        l " Well, you see! You'll see what happens tomorrow! "
        hide lanahappy at bottom
        show lananeutral at left
        l " Gotta figure out a script, after all. "
        hide petuniasurprised at bottom
        show petunianeutral at right
        p " Ah, right...gotta figure out a perfect script, hm? "
        l " Yuuuup! "
        l " I always have to bring in the best for my perfect little audience! "
        hide petunianeutral at bottom
        show petuniahappy at right
        p " Of course, so that you won't dissappoint! "
        hide petuniahappy at bottom
        show petunianeutral at right
        " You coughed so that you could get their attention. "
        " You do wonder what they were talking about earlier though... "
        p " Oh, heya [name]! "
        l " Oooo, hihi!! "
        p " Just talking to Lana over here, she's real fun! "
        p " Never really got to talk to her before, it's sweet talking to someone else other than Lizzy. "
        p " Sometimes besties need their breaks too, you know? "
        l " Mmm, yeah, I get that... "
        l " ...Not everything in friendship is fine and dandy! "
        l " Ya just don't know what might be going on underneath. "
        p " Mhmmmm... "
        " Huh. You wondered what happened with Petunia and Lizzy... "
        " You would usually see them hanging out togehter. "
        " You look to your left and they're always there, you look to right right, they're there too. "
        " Seeing Petunia talking with someone else is an odd sight. "
        " But you think that they're probably going to come back to eachother later. "
        " Besties have fights every now and then, and they come back, eventually. "
        p " Oh, right! "
        p " Lana, could we have a recap of what happened in the recent episode? "
        p " 'M sure [name] hasn't heard of it yet. "
        l " Oop! Pretty sure [they] haven't, no... "
        l " I'll get ready for a recap, then! Here we go... "
        p " Sweet! Better have some snacks on ya, [name]! This is gonna be good! "
        scene black with dissolve
        " You spent the rest of the break watching Lana's puppet show with Petunia. "
        " Petunia wasn't lying - it really was good. "
        " You're going to have to need 8 seasons, 3 spinoffs, and... "
        " I'm not even going to list down all of that. "
        " If I did, the game would have a 59 hours of playtime. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You get up from your seat and you walked over to your next class. "
        pause 2.0
        jump historyclass3
    elif popularknow == True and lanaknow == False:
        hide petunianeutral at bottom
        show petuniasurprised at right
        p " Oh? and what happened next? "
        p " What happened to Juliana and Pedro? "
        hide lananeutral at bottom
        show lanahappy at left
        x " Well, you see! You'll see what happens tomorrow! "
        hide lanahappy at bottom
        show lananeutral at left
        x " Gotta figure out a script, after all. "
        hide petuniasurprised at bottom
        show petunianeutral at right
        p " Ah, right...gotta figure out a perfect script, hm? "
        x " Yuuuup! "
        x " I always have to bring in the best for my perfect little audience! "
        hide petunianeutral at bottom
        show petuniahappy at right
        p " Of course, so that you won't dissappoint! "
        hide petuniahappy at bottom
        show petunianeutral at right
        " You coughed so that you could get their attention. "
        " You do wonder what they were talking about earlier though... "
        p " Oh, heya [name]! "
        x " Oooo, hihi!! "
        p " Just talking to Lana over here, she's real fun! "
        p " Oh wait, I don't think you've met her before! "
        $ lanaknow = True
        p " A real sweetheart, and a good storyteller. Someone would be lucky to have her as their partner! "
        l " Haha - Petunia? You're surprisingly being kind today... "
        p " I decided to be nice and give out compliments as a change of pace. "
        p " Anyway, never really got to talk to her before, it's sweet talking to someone else other than Lizzy. "
        p " Sometimes besties need their breaks too, you know? "
        l " Mmm, yeah, I get that... "
        l " ...Not everything in friendship is fine and dandy! "
        l " Ya just don't know what might be going on underneath. "
        p " Mhmmmm... "
        " Huh. You wondered what happened with Petunia and Lizzy... "
        " You would usually see them hanging out togehter. "
        " You look to your left and they're always there, you look to right right, they're there too. "
        " Seeing Petunia talking with someone else is an odd sight. "
        " But you think that they're probably going to come back to eachother later. "
        " Besties have fights every now and then, and they come back, eventually. "
        p " Oh, right! "
        p " Lana, could we have a recap of what happened in the recent episode? "
        p " 'M sure [name] hasn't heard of it yet. "
        l " Oop! Pretty sure [they] haven't, no... "
        l " I'll get ready for a recap, then! Here we go... "
        p " Sweet! Better have some snacks on ya, [name]! This is gonna be good! "
        scene black with dissolve
        " You spent the rest of the break watching Lana's puppet show with Petunia. "
        " Petunia wasn't lying - it really was good. "
        " You're going to have to need 8 seasons, 3 spinoffs, and... "
        " I'm not even going to list down all of that. "
        " If I did, the game would have a 59 hours of playtime. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You get up from your seat and you walked over to your next class. "
        pause 2.0
        jump historyclass3
    elif popularknow == False and lanaknow == True:
        hide petunianeutral at bottom
        show petuniasurprised at right
        x " Oh? and what happened next? "
        x " What happened to Juliana and Pedro? "
        hide lananeutral at bottom
        show lanahappy at left
        l " Well, you see! You'll see what happens tomorrow! "
        hide lanahappy at bottom
        show lananeutral at left
        l " Gotta figure out a script, after all. "
        hide petuniasurprised at bottom
        show petunianeutral at right
        x " Ah, right...gotta figure out a perfect script, hm? "
        l " Yuuuup! "
        l " I always have to bring in the best for my perfect little audience! "
        hide petunianeutral at bottom
        show petuniahappy at right
        x " Of course, so that you won't dissappoint! "
        hide petuniahappy at bottom
        show petunianeutral at right
        " You coughed so that you could get their attention. "
        " You do wonder what they were talking about earlier though... "
        x " Oh, heya [name]! "
        l " Oooo, hihi!! "
        x " Just talking to Lana over here, she's real fun! "
        l " Ooo, wait! Petunia, I don't think You've introduced yourself! "
        $ popularknow = True
        p " Well...you just said my name, so I think that's enough for [them]. "
        l " Ah....okay??? "
        p " Anyway, I've never really got to talk to Lana before, it's sweet talking to someone else other than Lizzy. "
        p " Sometimes besties need their breaks too, you know? "
        l " Mmm, yeah, I get that... "
        l " ...Not everything in friendship is fine and dandy! "
        l " Ya just don't know what might be going on underneath. "
        p " Mhmmmm... "
        " Huh. You wondered what happened with Petunia and Lizzy... "
        " You would usually see them hanging out togehter. "
        " You look to your left and they're always there, you look to right right, they're there too. "
        " Seeing Petunia talking with someone else is an odd sight. "
        " But you think that they're probably going to come back to eachother later. "
        " Besties have fights every now and then, and they come back, eventually. "
        p " Oh, right! "
        p " Lana, could we have a recap of what happened in the recent episode? "
        p " 'M sure [name] hasn't heard of it yet. "
        l " Oop! Pretty sure [they] haven't, no... "
        l " I'll get ready for a recap, then! Here we go... "
        p " Sweet! Better have some snacks on ya, [name]! This is gonna be good! "
        scene black with dissolve
        " You spent the rest of the break watching Lana's puppet show with Petunia. "
        " Petunia wasn't lying - it really was good. "
        " You're going to have to need 8 seasons, 3 spinoffs, and... "
        " I'm not even going to list down all of that. "
        " If I did, the game would have a 59 hours of playtime. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You get up from your seat and you walked over to your next class. "
        pause 2.0
        jump historyclass3
    else:
        hide petunianeutral at bottom
        show petuniasurprised at right
        x " Oh? and what happened next? "
        x " What happened to Juliana and Pedro? "
        hide lananeutral at bottom
        show lanahappy at left
        x " Well, you see! You'll see what happens tomorrow! "
        hide lanahappy at bottom
        show lananeutral at left
        x " Gotta figure out a script, after all. "
        hide petuniasurprised at bottom
        show petunianeutral at right
        x " Ah, right...gotta figure out a perfect script, hm? "
        x " Yuuuup! "
        x " I always have to bring in the best for my perfect little audience! "
        hide petunianeutral at bottom
        show petuniahappy at right
        x " Of course, so that you won't dissappoint! "
        hide petuniahappy at bottom
        show petunianeutral at right
        " You coughed so that you could get their attention. "
        " You do wonder what they were talking about earlier though... "
        x " Oh, heya [name]! "
        x " Oooo, hihi!! "
        x " Just talking to Lana over here, she's real fun! "
        x " Oh wait, I don't think you've met her before! "
        $ lanaknow = True
        x " A real sweetheart, and a good storyteller. Someone would be lucky to have her as their partner! "
        $ popularknow = True
        l " Haha - Petunia? You're surprisingly being kind today... "
        p " I decided to be nice and give out compliments as a change of pace. "
        p " Anyway, never really got to talk to her before, it's sweet talking to someone else other than Lizzy. "
        p " Sometimes besties need their breaks too, you know? "
        l " Mmm, yeah, I get that... "
        l " ...Not everything in friendship is fine and dandy! "
        l " Ya just don't know what might be going on underneath. "
        p " Mhmmmm... "
        " Huh. You wondered what happened with Petunia and Lizzy... "
        " You would usually see them hanging out togehter. "
        " You look to your left and they're always there, you look to right right, they're there too. "
        " Seeing Petunia talking with someone else is an odd sight. "
        " But you think that they're probably going to come back to eachother later. "
        " Besties have fights every now and then, and they come back, eventually. "
        p " Oh, right! "
        p " Lana, could we have a recap of what happened in the recent episode? "
        p " 'M sure [name] hasn't heard of it yet. "
        l " Oop! Pretty sure [they] haven't, no... "
        l " I'll get ready for a recap, then! Here we go... "
        p " Sweet! Better have some snacks on ya, [name]! This is gonna be good! "
        scene black with dissolve
        " You spent the rest of the break watching Lana's puppet show with Petunia. "
        " Petunia wasn't lying - it really was good. "
        " You're going to have to need 8 seasons, 3 spinoffs, and... "
        " I'm not even going to list down all of that. "
        " If I did, the game would have a 59 hours of playtime. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You get up from your seat and you walked over to your next class. "
        pause 2.0
        jump historyclass3
label wedcafeteria3:
    # abbie, bubble - bubble makes abbie see a cool trick she can do
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted two of your classmates hanging out. "
    " Curious on what they're doing, you decided to sit with them and have a nice talk with them. "
    " Maybe you could get some good drama out of this. "
    show abbieneutral at left with easeinright
    show bubbleneutral at right with easeinright
    if abbieknow == True and bubbleknow == True:
        b " Heya, [name]! "
        a " Ah, um...Hi there... "
        " You greeted them both a nice 'hello', before you asked them what they were doing. "
        b " I was actually about to show Abbie this cool trick I can do! "
        b " You wanna see it? "
        " Well, you can't really say no to a face like Bubble's... "
        " Or, technically eyes, since she doesn't really have a face. "
        " Just eyes so that you could tell what she's feeling. "
        " And eyebrows too, I guess. "
        hide bubbleneutral at bottom
        show bubbleamazed at right
        b " Cool, Cool! "
        b " Knew you'd say yes, [name]! "
        b " Just gimme a sec, alright? "
        hide bubbleamazed at bottom
        show bubbleneutral at right
        " You and Abbie wait for Bubble to finish preparing. "
        " Abbie seems to be a bit nervous...you're gonna have to guess he doesn't talk to Bubble much. "
        " He does seem like the closed-off type... "
        if abbieteach == True:
            " Maybe you should teach him to work on his social skills next. "
            " You've gotta work on his fighting skills first though. "
        else:
            pass
        b " Alright! Ready to see this cool trick? "
        " You and Abbie give Bubble a thumbs up as she takes a deep breath... "
        " Before her hair starts producing a whole lot of bubbles around the room. "
        hide bubbleneutral at bottom
        show bubblehappy at right
        b " Cool, isn't it?! "
        hide abbieneutral at bottom
        show abbiehappy at left
        " By the time Bubble spoke, you and Abbie have already started popping all of the bubbles that were pouring out of Bubble's hair. "
        " You couldn't really help your urges. "
        " Though, not sure how to feel about water and soap going into people's foods because of this. "
        scene black with dissolve
        " You spent the rest of the break popping Bubble's little... "
        " ...Bubbles. Kind of weird since she's a bubble herself and you're kinda popping little things of her... "
        " But, she looks like she's fine with it, soooooo...yeah. "
        " Couldn't really hold yourself back from playing with the bubbles anyway. "
        " Awakened something deep in your memory or something. "
        play sound "audio/bellring.mp3"
        " Aww, no more bubble popping session. "
        " You get up from your seat and you walked over to your next class. "
        pause 2.0
        jump historyclass3
    elif abbieknow == True and bubbleknow == False:
        x " Heya, [name]! "
        a " Ah, um...Hi there... "
        " You greeted them both a nice 'hello', before you asked them what they were doing. "
        x " Ah, uh...before you I tell you what I'm gonna be doing! "
        $ bubbleknow = True
        b " I'm Bubble. Sorry, it's just that I don't think that I've introduced myself to you, you know? "
        b " Would've been rude if I didn't, hahaa... "
        b " I was actually about to show Abbie this cool trick I can do! "
        b " You wanna see it? "
        " Well, you can't really say no to a face like Bubble's... "
        " Or, technically eyes, since she doesn't really have a face. "
        " Just eyes so that you could tell what she's feeling. "
        " And eyebrows too, I guess. "
        hide bubbleneutral at bottom
        show bubbleamazed at right
        b " Cool, Cool! "
        b " Knew you'd say yes, [name]! "
        b " Just gimme a sec, alright? "
        hide bubbleamazed at bottom
        show bubbleneutral at right
        " You and Abbie wait for Bubble to finish preparing. "
        " Abbie seems to be a bit nervous...you're gonna have to guess he doesn't talk to Bubble much. "
        " He does seem like the closed-off type... "
        if abbieteach == True:
            " Maybe you should teach him to work on his social skills next. "
            " You've gotta work on his fighting skills first though. "
        else:
            pass
        b " Alright! Ready to see this cool trick? "
        " You and Abbie give Bubble a thumbs up as she takes a deep breath... "
        " Before her hair starts producing a whole lot of bubbles around the room. "
        hide bubbleneutral at bottom
        show bubblehappy at right
        b " Cool, isn't it?! "
        hide abbieneutral at bottom
        show abbiehappy at left
        " By the time Bubble spoke, you and Abbie have already started popping all of the bubbles that were pouring out of Bubble's hair. "
        " You couldn't really help your urges. "
        " Though, not sure how to feel about water and soap going into people's foods because of this. "
        scene black with dissolve
        " You spent the rest of the break popping Bubble's little... "
        " ...Bubbles. Kind of weird since she's a bubble herself and you're kinda popping little things of her... "
        " But, she looks like she's fine with it, soooooo...yeah. "
        " Couldn't really hold yourself back from playing with the bubbles anyway. "
        " Awakened something deep in your memory or something. "
        play sound "audio/bellring.mp3"
        " Aww, no more bubble popping session. "
        " You get up from your seat and you walked over to your next class. "
        pause 2.0
        jump historyclass3
    elif abbieknow == False and bubbleknow == True:
        b " Heya, [name]! "
        x " Ah, um...Hi there... "
        " You greeted them both a nice 'hello', before you asked them what they were doing. "
        $ abbieknow = True
        b " I was actually about to show Abbie this cool trick I can do! "
        b " You wanna see it? "
        " Well, you can't really say no to a face like Bubble's... "
        " Or, technically eyes, since she doesn't really have a face. "
        " Just eyes so that you could tell what she's feeling. "
        " And eyebrows too, I guess. "
        hide bubbleneutral at bottom
        show bubbleamazed at right
        b " Cool, Cool! "
        b " Knew you'd say yes, [name]! "
        b " Just gimme a sec, alright? "
        hide bubbleamazed at bottom
        show bubbleneutral at right
        " You and Abbie wait for Bubble to finish preparing. "
        " Abbie seems to be a bit nervous...you're gonna have to guess he doesn't talk to Bubble much. "
        " He does seem like the closed-off type... "
        if abbieteach == True:
            " Maybe you should teach him to work on his social skills next. "
            " You've gotta work on his fighting skills first though. "
        else:
            pass
        b " Alright! Ready to see this cool trick? "
        " You and Abbie give Bubble a thumbs up as she takes a deep breath... "
        " Before her hair starts producing a whole lot of bubbles around the room. "
        hide bubbleneutral at bottom
        show bubblehappy at right
        b " Cool, isn't it?! "
        hide abbieneutral at bottom
        show abbiehappy at left
        " By the time Bubble spoke, you and Abbie have already started popping all of the bubbles that were pouring out of Bubble's hair. "
        " You couldn't really help your urges. "
        " Though, not sure how to feel about water and soap going into people's foods because of this. "
        scene black with dissolve
        " You spent the rest of the break popping Bubble's little... "
        " ...Bubbles. Kind of weird since she's a bubble herself and you're kinda popping little things of her... "
        " But, she looks like she's fine with it, soooooo...yeah. "
        " Couldn't really hold yourself back from playing with the bubbles anyway. "
        " Awakened something deep in your memory or something. "
        play sound "audio/bellring.mp3"
        " Aww, no more bubble popping session. "
        " You get up from your seat and you walked over to your next class. "
        pause 2.0
        jump historyclass3
    else:
        x " Heya, [name]! "
        x " Ah, um...Hi there... "
        " You greeted them both a nice 'hello', before you asked them what they were doing. "
        x " Ah, uh...before you I tell you what I'm gonna be doing! "
        $ bubbleknow = True
        b " I'm Bubble. Sorry, it's just that I don't think that I've introduced myself to you, you know? "
        b " Would've been rude if I didn't, hahaa... "
        $ abbieknow = True
        b " I was actually about to show Abbie this cool trick I can do! "
        b " You wanna see it? "
        " Well, you can't really say no to a face like Bubble's... "
        " Or, technically eyes, since she doesn't really have a face. "
        " Just eyes so that you could tell what she's feeling. "
        " And eyebrows too, I guess. "
        hide bubbleneutral at bottom
        show bubbleamazed at right
        b " Cool, Cool! "
        b " Knew you'd say yes, [name]! "
        b " Just gimme a sec, alright? "
        hide bubbleamazed at bottom
        show bubbleneutral at right
        " You and Abbie wait for Bubble to finish preparing. "
        " Abbie seems to be a bit nervous...you're gonna have to guess he doesn't talk to Bubble much. "
        " He does seem like the closed-off type... "
        if abbieteach == True:
            " Maybe you should teach him to work on his social skills next. "
            " You've gotta work on his fighting skills first though. "
        else:
            pass
        b " Alright! Ready to see this cool trick? "
        " You and Abbie give Bubble a thumbs up as she takes a deep breath... "
        " Before her hair starts producing a whole lot of bubbles around the room. "
        hide bubbleneutral at bottom
        show bubblehappy at right
        b " Cool, isn't it?! "
        hide abbieneutral at bottom
        show abbiehappy at left
        " By the time Bubble spoke, you and Abbie have already started popping all of the bubbles that were pouring out of Bubble's hair. "
        " You couldn't really help your urges. "
        " Though, not sure how to feel about water and soap going into people's foods because of this. "
        scene black with dissolve
        " You spent the rest of the break popping Bubble's little... "
        " ...Bubbles. Kind of weird since she's a bubble herself and you're kinda popping little things of her... "
        " But, she looks like she's fine with it, soooooo...yeah. "
        " Couldn't really hold yourself back from playing with the bubbles anyway. "
        " Awakened something deep in your memory or something. "
        play sound "audio/bellring.mp3"
        " Aww, no more bubble popping session. "
        " You get up from your seat and you walked over to your next class. "
        pause 2.0
        jump historyclass3
label wedrooftop3:
    # kevin, robby - kevin and robby discussing about math
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked up to the rooftop and spotted your two classmates talking about something. "
    " Probably talking about something nerdy, but you want to talk to them nonetheless. "
    " You walked up to them to hear what they're talking about. "
    show kevinneutral at right with easeinleft
    show robbyneutral at left with easeinleft
    if kevinknow == True and robbyknow == True:
        kv " No, no. I think there's 307 marbles in this jar, Robby. "
        rb " Nope. That's 306. I think you should get new glasses, Kevin... "
        kv " How EXACTLY can you prove that there's 306 marbles in this jar? "
        rb " By using the basic method of solving anything in a jar, of course. "
        kv " And that method iiiiiiis? "
        rb " If you're smart, then you would know it. "
        hide robbyneutral at bottom
        show robbyhappy at left
        rb " And you're really smart, aren't you, Kevs? "
        kv " I am...! "
        rb " Then you would know what my answer would be. "
        rb " IF you were smart enough. "
        kv " You know what, how about we'll just ask [name]?! "
        " You don't even know what's going on. "
        " Why are they talking about marbles in a jar? "
        " Where'd they even get that thing? "
        kv " If [name] is that smart, [they] would know that there's 307 marbles in this jar! "
        rb " We'll see... "
        hide robbyhappy at bottom
        show robbyneutral at left
        rb " Yo, [name]! How much marbles do you think are in this jar? "
        " For funny purposes, I'm going to make you make a choice. "
        " Also because you might be in need of points for one of these characters. "
        " If you don't want any, just click the lowest option! "
        menu:
            " 307 marbles ":
                $ kevinlv += 10
                hide kevinneutral at bottom
                show kevinhappy at right
                kv " Aha, you see! "
                kv " I knew I was right! "
                rb " Hm, either [they] actually think that there's 307 marbles... "
                rb " ...Or [they] just felt bad for you, kevs. "
                kv " Come on, you're just salty because I won, Robby. "
                rb " Not at all, and I would never be. "
                rb  " For something as stupid as this, to be honest. "
                kv " Mhm, suuure...keep lying to yourself, Rob. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin and Robby. "
                " Turns out the jar filled with marbles came from Miss Circle's office... "
                " ...And Kevin and Robby got bored in the middle of class and thought about the jar. "
                " Soooo they kind of took it to do tomfoolery. "
                " ...They should probably return that to it's original place after a bit before Miss Circle notices. "
                play sound "audio/bellring.mp3"
                " And that they did, right after the bell rang. "
                " Luckily Miss circle didn't see anything. "
                " You then went to your classroom for the next class. "
                pause 2.0
                jump historyclass3
            " 306 marbles ":
                $ robbrileylv += 10
                hide robbyneutral at bottom
                show robbyhappy at left
                rb " See, Kevin? "
                rb " You should really just get some new glasses. "
                hide kevinneutral at bottom
                show kevinangry at right
                kv " C-come on, [they] probably just guessed that! "
                kv " [they] didn't actually count or anything! "
                rb " Kevin, dude... "
                rb " There's a sticker that shows how many marbles are in this jar at the back of it. "
                hide kevinangry at bottom
                show kevinsurprised at right
                kv " ... "
                " Kevin seems shocked at this. "
                " Maybe he didn't check the jar's back before? "
                " He stays silent for a bit more until he speaks up again. "
                hide kevinsurprised at bottom
                show kevinangry at right
                kv " Well, that's because you didn't show me the back! "
                kv " Of course I would've thought that it would be 306! "
                rb " But where's the fun in that? "
                rb " Guessing is just better, you know. "
                kv " At this point I'm starting to think that you're doing this to piss me off... "
                rb " Hah...how I love annoying you. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin and Robby. "
                " Turns out the jar filled with marbles came from Miss Circle's office... "
                " ...And Kevin and Robby got bored in the middle of class and thought about the jar. "
                " Soooo they kind of took it to do tomfoolery. "
                " ...They should probably return that to it's original place after a bit before Miss Circle notices. "
                play sound "audio/bellring.mp3"
                " And that they did, right after the bell rang. "
                " Luckily Miss circle didn't see anything. "
                " You then went to your classroom for the next class. "
                pause 2.0
                jump historyclass3
            " I CANT FUCKING COUNT ":
                rb " Huh...so if [they] can't count, does this mean that this is a ... "
                kv " A DRAW??? I don't accept that. "
                rb " Come on, Kevs...let's just accept that there's 306 marbles in this jar. "
                kv " Nope. Actually, gimme all of the marbles! "
                kv " I'm going to count all of them just to prove that there's 307. "
                rb " ...Whatever you say, mister genius. "
                " And turns out, there was 306 marbles. "
                " Kevin and Robby managed to speedrun counting all of the marbles together. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin and Robby. "
                " Turns out the jar filled with marbles came from Miss Circle's office... "
                " ...And Kevin and Robby got bored in the middle of class and thought about the jar. "
                " Soooo they kind of took it to do tomfoolery. "
                " ...They should probably return that to it's original place after a bit before Miss Circle notices. "
                play sound "audio/bellring.mp3"
                " And that they did, right after the bell rang. "
                " Luckily Miss circle didn't see anything. "
                " You then went to your classroom for the next class. "
                pause 2.0
                jump historyclass3
    elif kevinknow == True and robbyknow == False:
        $ robbyknow = True
        kv " No, no. I think there's 307 marbles in this jar, Robby. "
        rb " Nope. That's 306. I think you should get new glasses, Kevin... "
        kv " How EXACTLY can you prove that there's 306 marbles in this jar? "
        rb " By using the basic method of solving anything in a jar, of course. "
        kv " And that method iiiiiiis? "
        rb " If you're smart, then you would know it. "
        hide robbyneutral at bottom
        show robbyhappy at left
        rb " And you're really smart, aren't you, Kevs? "
        kv " I am...! "
        rb " Then you would know what my answer would be. "
        rb " IF you were smart enough. "
        kv " You know what, how about we'll just ask [name]?! "
        " You don't even know what's going on. "
        " Why are they talking about marbles in a jar? "
        " Where'd they even get that thing? "
        kv " If [name] is that smart, [they] would know that there's 307 marbles in this jar! "
        rb " We'll see... "
        hide robbyhappy at bottom
        show robbyneutral at left
        rb " Yo, [name]! How much marbles do you think are in this jar? "
        " For funny purposes, I'm going to make you make a choice. "
        " Also because you might be in need of points for one of these characters. "
        " If you don't want any, just click the lowest option! "
        menu:
            " 307 marbles ":
                $ kevinlv += 10
                hide kevinneutral at bottom
                show kevinhappy at right
                kv " Aha, you see! "
                kv " I knew I was right! "
                rb " Hm, either [they] actually think that there's 307 marbles... "
                rb " ...Or [they] just felt bad for you, kevs. "
                kv " Come on, you're just salty because I won, Robby. "
                rb " Not at all, and I would never be. "
                rb  " For something as stupid as this, to be honest. "
                kv " Mhm, suuure...keep lying to yourself, Rob. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin and Robby. "
                " Turns out the jar filled with marbles came from Miss Circle's office... "
                " ...And Kevin and Robby got bored in the middle of class and thought about the jar. "
                " Soooo they kind of took it to do tomfoolery. "
                " ...They should probably return that to it's original place after a bit before Miss Circle notices. "
                play sound "audio/bellring.mp3"
                " And that they did, right after the bell rang. "
                " Luckily Miss circle didn't see anything. "
                " You then went to your classroom for the next class. "
                pause 2.0
                jump historyclass3
            " 306 marbles ":
                $ robbrileylv += 10
                hide robbyneutral at bottom
                show robbyhappy at left
                rb " See, Kevin? "
                rb " You should really just get some new glasses. "
                hide kevinneutral at bottom
                show kevinangry at right
                kv " C-come on, [they] probably just guessed that! "
                kv " [they] didn't actually count or anything! "
                rb " Kevin, dude... "
                rb " There's a sticker that shows how many marbles are in this jar at the back of it. "
                hide kevinangry at bottom
                show kevinsurprised at right
                kv " ... "
                " Kevin seems shocked at this. "
                " Maybe he didn't check the jar's back before? "
                " He stays silent for a bit more until he speaks up again. "
                hide kevinsurprised at bottom
                show kevinangry at right
                kv " Well, that's because you didn't show me the back! "
                kv " Of course I would've thought that it would be 306! "
                rb " But where's the fun in that? "
                rb " Guessing is just better, you know. "
                kv " At this point I'm starting to think that you're doing this to piss me off... "
                rb " Hah...how I love annoying you. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin and Robby. "
                " Turns out the jar filled with marbles came from Miss Circle's office... "
                " ...And Kevin and Robby got bored in the middle of class and thought about the jar. "
                " Soooo they kind of took it to do tomfoolery. "
                " ...They should probably return that to it's original place after a bit before Miss Circle notices. "
                play sound "audio/bellring.mp3"
                " And that they did, right after the bell rang. "
                " Luckily Miss circle didn't see anything. "
                " You then went to your classroom for the next class. "
                pause 2.0
                jump historyclass3
            " I CANT FUCKING COUNT ":
                rb " Huh...so if [they] can't count, does this mean that this is a ... "
                kv " A DRAW??? I don't accept that. "
                rb " Come on, Kevs...let's just accept that there's 306 marbles in this jar. "
                kv " Nope. Actually, gimme all of the marbles! "
                kv " I'm going to count all of them just to prove that there's 307. "
                rb " ...Whatever you say, mister genius. "
                " And turns out, there was 306 marbles. "
                " Kevin and Robby managed to speedrun counting all of the marbles together. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin and Robby. "
                " Turns out the jar filled with marbles came from Miss Circle's office... "
                " ...And Kevin and Robby got bored in the middle of class and thought about the jar. "
                " Soooo they kind of took it to do tomfoolery. "
                " ...They should probably return that to it's original place after a bit before Miss Circle notices. "
                play sound "audio/bellring.mp3"
                " And that they did, right after the bell rang. "
                " Luckily Miss circle didn't see anything. "
                " You then went to your classroom for the next class. "
                pause 2.0
                jump historyclass3
    elif kevinknow == False and robbyknow == True:
        x " No, no. I think there's 307 marbles in this jar, Robby. "
        $ kevinknow = True
        rb " Nope. That's 306. I think you should get new glasses, Kevin... "
        kv " How EXACTLY can you prove that there's 306 marbles in this jar? "
        rb " By using the basic method of solving anything in a jar, of course. "
        kv " And that method iiiiiiis? "
        rb " If you're smart, then you would know it. "
        hide robbyneutral at bottom
        show robbyhappy at left
        rb " And you're really smart, aren't you, Kevs? "
        kv " I am...! "
        rb " Then you would know what my answer would be. "
        rb " IF you were smart enough. "
        kv " You know what, how about we'll just ask [name]?! "
        " You don't even know what's going on. "
        " Why are they talking about marbles in a jar? "
        " Where'd they even get that thing? "
        kv " If [name] is that smart, [they] would know that there's 307 marbles in this jar! "
        rb " We'll see... "
        hide robbyhappy at bottom
        show robbyneutral at left
        rb " Yo, [name]! How much marbles do you think are in this jar? "
        " For funny purposes, I'm going to make you make a choice. "
        " Also because you might be in need of points for one of these characters. "
        " If you don't want any, just click the lowest option! "
        menu:
            " 307 marbles ":
                $ kevinlv += 10
                hide kevinneutral at bottom
                show kevinhappy at right
                kv " Aha, you see! "
                kv " I knew I was right! "
                rb " Hm, either [they] actually think that there's 307 marbles... "
                rb " ...Or [they] just felt bad for you, kevs. "
                kv " Come on, you're just salty because I won, Robby. "
                rb " Not at all, and I would never be. "
                rb  " For something as stupid as this, to be honest. "
                kv " Mhm, suuure...keep lying to yourself, Rob. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin and Robby. "
                " Turns out the jar filled with marbles came from Miss Circle's office... "
                " ...And Kevin and Robby got bored in the middle of class and thought about the jar. "
                " Soooo they kind of took it to do tomfoolery. "
                " ...They should probably return that to it's original place after a bit before Miss Circle notices. "
                play sound "audio/bellring.mp3"
                " And that they did, right after the bell rang. "
                " Luckily Miss circle didn't see anything. "
                " You then went to your classroom for the next class. "
                pause 2.0
                jump historyclass3
            " 306 marbles ":
                $ robbrileylv += 10
                hide robbyneutral at bottom
                show robbyhappy at left
                rb " See, Kevin? "
                rb " You should really just get some new glasses. "
                hide kevinneutral at bottom
                show kevinangry at right
                kv " C-come on, [they] probably just guessed that! "
                kv " [they] didn't actually count or anything! "
                rb " Kevin, dude... "
                rb " There's a sticker that shows how many marbles are in this jar at the back of it. "
                hide kevinangry at bottom
                show kevinsurprised at right
                kv " ... "
                " Kevin seems shocked at this. "
                " Maybe he didn't check the jar's back before? "
                " He stays silent for a bit more until he speaks up again. "
                hide kevinsurprised at bottom
                show kevinangry at right
                kv " Well, that's because you didn't show me the back! "
                kv " Of course I would've thought that it would be 306! "
                rb " But where's the fun in that? "
                rb " Guessing is just better, you know. "
                kv " At this point I'm starting to think that you're doing this to piss me off... "
                rb " Hah...how I love annoying you. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin and Robby. "
                " Turns out the jar filled with marbles came from Miss Circle's office... "
                " ...And Kevin and Robby got bored in the middle of class and thought about the jar. "
                " Soooo they kind of took it to do tomfoolery. "
                " ...They should probably return that to it's original place after a bit before Miss Circle notices. "
                play sound "audio/bellring.mp3"
                " And that they did, right after the bell rang. "
                " Luckily Miss circle didn't see anything. "
                " You then went to your classroom for the next class. "
                pause 2.0
                jump historyclass3
            " I CANT FUCKING COUNT ":
                rb " Huh...so if [they] can't count, does this mean that this is a ... "
                kv " A DRAW??? I don't accept that. "
                rb " Come on, Kevs...let's just accept that there's 306 marbles in this jar. "
                kv " Nope. Actually, gimme all of the marbles! "
                kv " I'm going to count all of them just to prove that there's 307. "
                rb " ...Whatever you say, mister genius. "
                " And turns out, there was 306 marbles. "
                " Kevin and Robby managed to speedrun counting all of the marbles together. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin and Robby. "
                " Turns out the jar filled with marbles came from Miss Circle's office... "
                " ...And Kevin and Robby got bored in the middle of class and thought about the jar. "
                " Soooo they kind of took it to do tomfoolery. "
                " ...They should probably return that to it's original place after a bit before Miss Circle notices. "
                play sound "audio/bellring.mp3"
                " And that they did, right after the bell rang. "
                " Luckily Miss circle didn't see anything. "
                " You then went to your classroom for the next class. "
                pause 2.0
                jump historyclass3
    else:
        $ robbyknow = True
        x " No, no. I think there's 307 marbles in this jar, Robby. "
        $ kevinknow = True
        rb " Nope. That's 306. I think you should get new glasses, Kevin... "
        kv " How EXACTLY can you prove that there's 306 marbles in this jar? "
        rb " By using the basic method of solving anything in a jar, of course. "
        kv " And that method iiiiiiis? "
        rb " If you're smart, then you would know it. "
        hide robbyneutral at bottom
        show robbyhappy at left
        rb " And you're really smart, aren't you, Kevs? "
        kv " I am...! "
        rb " Then you would know what my answer would be. "
        rb " IF you were smart enough. "
        kv " You know what, how about we'll just ask [name]?! "
        " You don't even know what's going on. "
        " Why are they talking about marbles in a jar? "
        " Where'd they even get that thing? "
        kv " If [name] is that smart, [they] would know that there's 307 marbles in this jar! "
        rb " We'll see... "
        hide robbyhappy at bottom
        show robbyneutral at left
        rb " Yo, [name]! How much marbles do you think are in this jar? "
        " For funny purposes, I'm going to make you make a choice. "
        " Also because you might be in need of points for one of these characters. "
        " If you don't want any, just click the lowest option! "
        menu:
            " 307 marbles ":
                $ kevinlv += 10
                hide kevinneutral at bottom
                show kevinhappy at right
                kv " Aha, you see! "
                kv " I knew I was right! "
                rb " Hm, either [they] actually think that there's 307 marbles... "
                rb " ...Or [they] just felt bad for you, kevs. "
                kv " Come on, you're just salty because I won, Robby. "
                rb " Not at all, and I would never be. "
                rb  " For something as stupid as this, to be honest. "
                kv " Mhm, suuure...keep lying to yourself, Rob. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin and Robby. "
                " Turns out the jar filled with marbles came from Miss Circle's office... "
                " ...And Kevin and Robby got bored in the middle of class and thought about the jar. "
                " Soooo they kind of took it to do tomfoolery. "
                " ...They should probably return that to it's original place after a bit before Miss Circle notices. "
                play sound "audio/bellring.mp3"
                " And that they did, right after the bell rang. "
                " Luckily Miss circle didn't see anything. "
                " You then went to your classroom for the next class. "
                pause 2.0
                jump historyclass3
            " 306 marbles ":
                $ robbrileylv += 10
                hide robbyneutral at bottom
                show robbyhappy at left
                rb " See, Kevin? "
                rb " You should really just get some new glasses. "
                hide kevinneutral at bottom
                show kevinangry at right
                kv " C-come on, [they] probably just guessed that! "
                kv " [they] didn't actually count or anything! "
                rb " Kevin, dude... "
                rb " There's a sticker that shows how many marbles are in this jar at the back of it. "
                hide kevinangry at bottom
                show kevinsurprised at right
                kv " ... "
                " Kevin seems shocked at this. "
                " Maybe he didn't check the jar's back before? "
                " He stays silent for a bit more until he speaks up again. "
                hide kevinsurprised at bottom
                show kevinangry at right
                kv " Well, that's because you didn't show me the back! "
                kv " Of course I would've thought that it would be 306! "
                rb " But where's the fun in that? "
                rb " Guessing is just better, you know. "
                kv " At this point I'm starting to think that you're doing this to piss me off... "
                rb " Hah...how I love annoying you. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin and Robby. "
                " Turns out the jar filled with marbles came from Miss Circle's office... "
                " ...And Kevin and Robby got bored in the middle of class and thought about the jar. "
                " Soooo they kind of took it to do tomfoolery. "
                " ...They should probably return that to it's original place after a bit before Miss Circle notices. "
                play sound "audio/bellring.mp3"
                " And that they did, right after the bell rang. "
                " Luckily Miss circle didn't see anything. "
                " You then went to your classroom for the next class. "
                pause 2.0
                jump historyclass3
            " I CANT FUCKING COUNT ":
                rb " Huh...so if [they] can't count, does this mean that this is a ... "
                kv " A DRAW??? I don't accept that. "
                rb " Come on, Kevs...let's just accept that there's 306 marbles in this jar. "
                kv " Nope. Actually, gimme all of the marbles! "
                kv " I'm going to count all of them just to prove that there's 307. "
                rb " ...Whatever you say, mister genius. "
                " And turns out, there was 306 marbles. "
                " Kevin and Robby managed to speedrun counting all of the marbles together. "
                scene black with dissolve
                " You spent the rest of the break talking with Kevin and Robby. "
                " Turns out the jar filled with marbles came from Miss Circle's office... "
                " ...And Kevin and Robby got bored in the middle of class and thought about the jar. "
                " Soooo they kind of took it to do tomfoolery. "
                " ...They should probably return that to it's original place after a bit before Miss Circle notices. "
                play sound "audio/bellring.mp3"
                " And that they did, right after the bell rang. "
                " Luckily Miss circle didn't see anything. "
                " You then went to your classroom for the next class. "
                pause 2.0
                jump historyclass3
label wedlibrary3:
    # riley, lizzy - lizzy tries to understand riley
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and spotted two of your classmates hanging out with eachother. "
    " Wondering what they were talking about, you walked over to them and sat down next to them. "
    " Oh hey, it's one of those popular girls. Maybe you could get some good gossip from this. "
    show lizzyneutral at left with easeinright
    show rileyneutral at right with easeinright
    if popularknow == True and rileyknow == True:
        ri " And then I told him - Oh, Oliver! I love you so much! "
        ri " And guess what, he said the same thing to me! "
        lz " Wow, that's...nice, Riley. "
        lz " Glad that you and Oliver have a nice and healthy relationship. "
        lz " I wish I had something like that. "
        ri " Oh, don't worry, Lizzy! "
        ri " You'll find someone as sweet as my Oliver soon! "
        ri " Just not my sweet Oliver himself. "
        lz " Mmmm...Yeah, with how popular I am. "
        lz " But, I kinda prefer getting school done first. "
        lz " Sure, I'll have crushes here and there... "
        lz " But will I actually fulfill a relationship with them? nope. "
        lz " Gotta find the right person in adulthood. "
        lz " Don't want to end up like Petunia, after all... "
        ri " Wait, what happened with you and Petunia? "
        lz " ...We just had a little disagreement. "
        " Oooh, drama. "
        " Looks like they haven't noticed that you're there yet... "
        " You pretend to be reading some sort of book as you listen into their conversation. "
        if kind == True:
            " Of course you're kind enough to not spread this around the school, "
            " But some little drama won't hurt your life. "
            " In fact, it would make your life more interesting. "
        elif calm == True:
            " Of course you're calm enough to not spread this around the school, "
            " But some little drama won't hurt your life. "
            " In fact, it would make your life more interesting. "
        elif mean == True:
            " You're 100% gonna spread this around the school. "
            " You've gotta listen to the whole thing first though. "
            " Some drama could never hurt anyone's life. "
        else:
            pass
        scene black with dissolve
        " You spent the rest of the break listening into the conversation fo the two girls next to you. "
        " You've got some pretty juicy information all about this... "
        " ...Their secret is safe with you, or is it? "
        " Their secrets are definitely not safe from me, the narrator. "
        " I could just spit out what they were talking about, but I don't feel like it. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, time for another class. "
        " You get up from your seat and you walked to your classroom for the next class. "
        pause 2.0
        jump historyclass3
    elif popularknow == True and rileyknow == False:
        x " And then I told him - Oh, Oliver! I love you so much! "
        x " And guess what, he said the same thing to me! "
        lz " Wow, that's...nice, Riley. "
        lz " Glad that you and Oliver have a nice and healthy relationship. "
        lz " I wish I had something like that. "
        x " Oh, don't worry, Lizzy! "
        x " You'll find someone as sweet as my Oliver soon! "
        x " Just not my sweet Oliver himself. "
        lz " Mmmm...Yeah, with how popular I am. "
        lz " But, I kinda prefer getting school done first. "
        lz " Sure, I'll have crushes here and there... "
        lz " But will I actually fulfill a relationship with them? nope. "
        lz " Gotta find the right person in adulthood. "
        lz " Don't want to end up like Petunia, after all... "
        x " Wait, what happened with you and Petunia? "
        lz " ...We just had a little disagreement. "
        " Oooh, drama. "
        " Looks like they haven't noticed that you're there yet... "
        " You pretend to be reading some sort of book as you listen into their conversation. "
        if kind == True:
            " Of course you're kind enough to not spread this around the school, "
            " But some little drama won't hurt your life. "
            " In fact, it would make your life more interesting. "
        elif calm == True:
            " Of course you're calm enough to not spread this around the school, "
            " But some little drama won't hurt your life. "
            " In fact, it would make your life more interesting. "
        elif mean == True:
            " You're 100% gonna spread this around the school. "
            " You've gotta listen to the whole thing first though. "
            " Some drama could never hurt anyone's life. "
        else:
            pass
        scene black with dissolve
        " You spent the rest of the break listening into the conversation fo the two girls next to you. "
        " You've got some pretty juicy information all about this... "
        " ...Their secret is safe with you, or is it? "
        " Their secrets are definitely not safe from me, the narrator. "
        " I could just spit out what they were talking about, but I don't feel like it. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, time for another class. "
        " You get up from your seat and you walked to your classroom for the next class. "
        pause 2.0
        jump historyclass3
    elif popularknow == False and rileyknow == True:
        ri " And then I told him - Oh, Oliver! I love you so much! "
        ri " And guess what, he said the same thing to me! "
        x " Wow, that's...nice, Riley. "
        x " Glad that you and Oliver have a nice and healthy relationship. "
        x " I wish I had something like that. "
        ri " Oh, don't worry, Lizzy! "
        ri " You'll find someone as sweet as my Oliver soon! "
        ri " Just not my sweet Oliver himself. "
        x " Mmmm...Yeah, with how popular I am. "
        x " But, I kinda prefer getting school done first. "
        x " Sure, I'll have crushes here and there... "
        x " But will I actually fulfill a relationship with them? nope. "
        x " Gotta find the right person in adulthood. "
        x " Don't want to end up like Petunia, after all... "
        ri " Wait, what happened with you and Petunia? "
        x " ...We just had a little disagreement. "
        " Oooh, drama. "
        " Looks like they haven't noticed that you're there yet... "
        " You pretend to be reading some sort of book as you listen into their conversation. "
        if kind == True:
            " Of course you're kind enough to not spread this around the school, "
            " But some little drama won't hurt your life. "
            " In fact, it would make your life more interesting. "
        elif calm == True:
            " Of course you're calm enough to not spread this around the school, "
            " But some little drama won't hurt your life. "
            " In fact, it would make your life more interesting. "
        elif mean == True:
            " You're 100% gonna spread this around the school. "
            " You've gotta listen to the whole thing first though. "
            " Some drama could never hurt anyone's life. "
        else:
            pass
        scene black with dissolve
        " You spent the rest of the break listening into the conversation fo the two girls next to you. "
        " You've got some pretty juicy information all about this... "
        " ...Their secret is safe with you, or is it? "
        " Their secrets are definitely not safe from me, the narrator. "
        " I could just spit out what they were talking about, but I don't feel like it. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, time for another class. "
        " You get up from your seat and you walked to your classroom for the next class. "
        pause 2.0
        jump historyclass3
    else:
        x " And then I told him - Oh, Oliver! I love you so much! "
        x " And guess what, he said the same thing to me! "
        x " Wow, that's...nice, Riley. "
        x " Glad that you and Oliver have a nice and healthy relationship. "
        x " I wish I had something like that. "
        x " Oh, don't worry, Lizzy! "
        x " You'll find someone as sweet as my Oliver soon! "
        x " Just not my sweet Oliver himself. "
        x " Mmmm...Yeah, with how popular I am. "
        x " But, I kinda prefer getting school done first. "
        x " Sure, I'll have crushes here and there... "
        x " But will I actually fulfill a relationship with them? nope. "
        x " Gotta find the right person in adulthood. "
        x " Don't want to end up like Petunia, after all... "
        x " Wait, what happened with you and Petunia? "
        x " ...We just had a little disagreement. "
        " Oooh, drama. "
        " Looks like they haven't noticed that you're there yet... "
        " You pretend to be reading some sort of book as you listen into their conversation. "
        if kind == True:
            " Of course you're kind enough to not spread this around the school, "
            " But some little drama won't hurt your life. "
            " In fact, it would make your life more interesting. "
        elif calm == True:
            " Of course you're calm enough to not spread this around the school, "
            " But some little drama won't hurt your life. "
            " In fact, it would make your life more interesting. "
        elif mean == True:
            " You're 100% gonna spread this around the school. "
            " You've gotta listen to the whole thing first though. "
            " Some drama could never hurt anyone's life. "
        else:
            pass
        scene black with dissolve
        " You spent the rest of the break listening into the conversation fo the two girls next to you. "
        " You've got some pretty juicy information all about this... "
        " ...Their secret is safe with you, or is it? "
        " Their secrets are definitely not safe from me, the narrator. "
        " I could just spit out what they were talking about, but I don't feel like it. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, time for another class. "
        " You get up from your seat and you walked to your classroom for the next class. "
        pause 2.0
        jump historyclass3
label wedoligang1:
    # new member!
    scene black with dissolve
    pause 2.0
    scene oligangclub with dissolve
    " You walked into the club and found that all the members were already there. "
    " Great...let's see how all of this goes. "
    show edwardneutral at left with easeinright
    show oliverneutral at center with easeinright
    show zipneutral at right with easeinright
    o " So as I was saying, soap is the best topping to add to your pizza! "
    o " Pepperoni, sausage, pineapple? OVERRATED! "
    o " Try something new for a chance and eat some good ol' soap. "
    o " Not only tastes good but it also makes your mouth feel all clean afterwards! "
    z " Oliver, I don't think that's really healthy dude. "
    o " Who cares about health? In this gang? All we care about is danger. "
    z " Eh, guess you're right. By the way, is that the new member you were talking about? "
    o " Oh, [name]? yep! Ya really came. "
    ed " So! You're the new members, eh? "
    hide edwardneutral at bottom
    show edwardconfused at left
    ed " Wait, hold on...isn't this the [person] who... "
    if clairebeatup,clairedefend,abbiemeandefend == True:
        o " Did too many things that I can't name? Yes. "
        o " Thought [they] would be a good addition to the team with how great [they] were! "
    elif clairebeatup,clairedefend == True and abbiemeandefend == False:
        o " Proceeded to beat up Claire and then defend her? yes. "
        o " Thought [they] would be a good addition to the team with how great [they] were! "
    elif clairebeatup,abbiemeandefend == True and clairedefend == False:
        o " Proceeded to beat up Claire and then defend Abbie? yes. "
        o " Thought [they] would be a good addition to the team with how great [they] were! "
    elif abbiemeandefend,clairedefend == True and clairebeatup == False:
        o " Proceeded to defend Abbie and defend Claire? Yes. "
        o " Thought [they] would be a good addition to the team with how great [they] were! "
    elif clairebeatup == True and abbiemeandefend,clairedefend == False:
        o " Beat up Claire? Yes. "
        o " Thought [they] would be a good addition to the team with how great [they] were! "
    elif clairedefend == True and abbiemeandefend,clairebeatup == False:
        o " Defend Claire? Yes. "
        o " Thought [they] would be a good addition to the team with how great [they] were! "
    elif abbiemeandefend == True and clairedefend,clairebeatup == False:
        o " Defend Abbie and absolutely wreck my ass? Yes. "
        o " Thought [they] would be a good addition to the team with how great [they] were! "
    else:
        o " Is a dumbass? yes. "
    ed " Wh - doesn't that make them a loser, though? "
    hide zipneutral at bottom
    show zipangry at right
    z " Yeah, dude. Don't you remember, Oliver? "
    z " You said it yourself that we don't take in losers. "
    hide zipangry at bottom
    show zipneutral at right
    z " You guys got something going on together? "
    hide edwardconfused at bottom
    show edwardneutral at left
    ed " Ooooh, shiiit! "
    ed " Don't think Alice would be too happy about that one, Oliver? "
    hide oliverneutral at bottom
    show oliverangry at center
    o " Ew, of course not, idiots. "
    o " Besides, [name] isn't even my type. "
    hide oliverangry at bottom
    show oliverneutral at center
    o " [they] may be badass, but not Alice's level of badass. "
    ed " Eh, whatever ya say, boss... "
    z " As much as I don't like you being here, welcome to the team, [name]! "
    ed " Yeah, welcome or whatever. "
    ed " We don't usually do things like these. "
    o " Your ass should feel lucky, hmhm. "
    scene black with dissolve
    " You spent the rest of the break hanging out with Oliver and the gang. "
    " You couldn't help but feel a strange sensation of peace as you were hanging out with them... "
    " ...When all of them are nowhere close to being peaceful. "
    " You choose to ignore that feeling though as you discuss some new pranks you'd like to do with the gang. "
    " Oh yeah, right. For every activity, you're going to be seated with Oliver and the gang now. "
    if claengbub == True:
        " Goodbye, Claire, Engel, and Bubble. "
        " Those three were nerds anyway. "
        $ claengbub = False
        $ oligang = True
        pass
    elif abblana == True:
        " Goodbye, Abbie and Lana. "
        " You two were wimps anyway. "
        $ abblana = False
        $ oligang = True
        pass
    elif alone == True:
        " Oh, you're already sitting alone. "
        " Perfect! Now you have three people who can make you lose your sanity! "
        $ alone = False
        $ oligang = True
        pass
    play sound "audio/bellring.mp3"
    " The bell rings, looks like it's time for class. "
    " You and the gang chatted for a bit more before all of you went to class. "
    " When you got there, the teacher seemed a little surprised that you would hang out with Oliver... "
    " ...Infact, everyone was. "
    " You chose to ignore their looks though. "
    pause 2.0
    jump historyclass3

label historyclass3:
    scene classroom with dissolve
    " You walked into the classroom and looks like the teacher's already there. "
    " Oh right, it's activity time. Woohoo. "
    " Wonder what you're gonna have to do for this activity... "
    show msemilyneutral at center with easeinleft
    mse " Good day, class! "
    mse " As all of you know, today's the day where we're going to have an activity! "
    mse " Let me explain to you all how this is gonna work... "
    mse " This is going to be a group activity! Make sure everyone in your group cooperates. "
    mse " This is also going to be worth {b}80{b} points. "
    " Oooh, delicious points. Now this is making you want to actually participate in this. "
    mse " Oh right, and you can pick anyone to be in your team! There's no limit, really! "
    mse " All of you will explore a specific historical era by creating an art-inspired poster that reflects the culture, major events, and values of the time. "
    mse " I'll give each of you a historical time period in just a moment! "
    mse " For now, find your groups! "
    hide msemilyneutral at right with easeoutright
    if oligang == True:
        " Well, you're already with Oliver and the gang. "
        " This is gonna be your group. "
        jump oliganghistoryrah
    else:
        pass
    " Who should you partner with? I mean, she did say that you can partner with anybody. "
    if claengbub == True:
        menu:
            " I wanna partner with who I'm sitting with (Claire, Engel, Bubble) ":
                jump claengbubhistory
            " Let's see who else I can partner with... ":
                jump historyotheroptions
    elif abblana == True:
        menu:
            " I wanna partner with who I'm sitting with (Abbie, Lana) ":
                jump abblanahistory
            " Let's see who else I can partner with... ":
                jump historyotheroptions
    elif alone == True:
        menu:
            " Screw this, I can do it all myself ":
                jump alonehistory
            " Let's see who else I can partner with... ":
                jump historyotheroptions
    else:
        menu:
            " Screw this, I can do it all myself ":
                jump alonehistory
            " Let's see who else I can partner with... ":
                jump historyotheroptions
    label historyotheroptions:
        " Here are the other people who you can group with... "
        menu:
            " The popular girls ":
                jump popularhistory
            " A cat and a nerd ":
                jump cubkevhistory
            " A girl with a TV head, an insane looking girl, a concerned guy with a propeller hat, and an emo guy. ":
                jump ruriroskhistory
            " Actually, I'd rather just do this with the people I'm sitting with. ":
                if claengbub == True:
                    jump claengbubhistory
                elif abblana == True:
                    jump abblanahistory
                elif alone == True:
                    " Wait, but you aren't even sitting with anyone. "
                    " Oh well, looks like you're doing this alone! "
                    jump alonehistory
                else:
                    " Wait, but you aren't even sitting with anyone. "
                    " Oh well, looks like you're doing this alone! "
                    jump alonehistory
            " Screw this, I'm doing this by myself! ":
                jump alonehistory
    label claengbubhistory:
        $ engellv += 5
        $ clairelv += 5
        $ bubblelv += 5
        show engelneutral at left with easeinright
        show claireneutral at center with easeinright
        show bubbleneutral at right with easeinright
        c " Alright guys! Miss Emily just gave us our materials and our topic... "
        b " Let's hope it's something easy! "
        e " Bubble, nothing is easy...but, sure. "
        c " Shhh! Alright, we got... "
        c " Ancient Egypt! We've got to explore tomb paintings, hieroglyphics... "
        c " You guys get the idea, right? "
        hide bubbleneutral at bottom
        show bubbleamazed at right
        b " Oooh, ancient egypt! Isn't that a trend or something? "
        hide engelneutral at bottom
        show engelhappy at left
        e " Pretty sure that's just a time period, Bubble. "
        hide bubbleamazed at bottom
        show bubbleneutral at right
        b " Nah, I meant that one trend where people show off their characters in Egyptian outfits... "
        b " ...But I did hear some people say that it was a bad trend, soo... best not to talk about that then. "
        c " Alright, everyone! I'll get a reference picture for us online in a bit... "
        c " Just wait, alright? "
        e " Sure thing, Claire. "
        " You and your group made the activity with a reference picture online. "
        if clairebeatup == True:
            " Things were a little awkward with Claire as your partner but... "
            " You tried to ignore what happened for now. You just wanted to have some fun. "
        else:
            " You had a lot of fun working with your groupmates. "
            " They were really nice to talk to! "
        scene black with dissolve
        " You spent the rest of class doing the activity. "
        " Once your group was done, you all passed it to the teacher. "
        " You guys were actually the first ones to pass, so you had a LOT of free time. "
        " ...And you spent all of that free time looking at your phone. "
        " What? you didn't want to disturb your classmates while they're working. "
        " Plus, your groupmates were already doing their own thing the moment you guys were done, and you didn't want to disturb them either. "
        " Sooo...more phone time, less complaining. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another break. "
        " You get out of your seat and you walk into the hallways... "
        pause 2.0
        jump wedbreak4
    label abblanahistory:
        # ancient greece and rome
        $ abbielv += 5
        $ lanalv += 5
        show abbieneutral at left with easeinright
        show lananeutral at right with easeinright
        " You wonder what your topic for this group is gonna be... "
        l " Oh! Hiya there, [name]! It's good to see you! "
        a " Mmm...Hi, [name]... "
        l " Miss Emily's giving out all of the topics and stuff, and ours should be right abouuutt... "
        " Miss Emily walks by to give Lana the topic for your group. "
        hide lananeutral at bottom
        show lanahappy at right
        l " Thanks, Miss Emily! "
        mse " You're welcome, dear! "
        mse " If you need any help with the topic, you can ask me to give examples. "
        l " Sure thing! "
        hide lanahappy at bottom
        show lananeutral at right
        a " ...So...what did we get...? "
        l " We got 'Ancient greece and rome!' "
        l " Hmmm...isn't ancient greece about gods and stuff? "
        l " Not really sure about rome though... "
        a " ...Well...I heard that there was a musical about greek gods and stuff... "
        l " Maybe we could listen to that then! Just for a bit though. "
        l " Oh, oh! and also look at examples on google. "
        l " You {i}do{i} have some date, right? "
        a " Hhhmm...yeah, I do... "
        l " Sweet! Let's get to working, then!! "
        l " This is going to be fun! "
        " You and your group made the activity by listening to a musical and looking at examples online. "
        " Wonder how that musical is gonna help, but you're not gonna question the choices of your groupmates. "
        " Plus, the songs were pretty much bangers. "
        " You had a lot of fun working with your groupmates. "
        " They were really nice to talk to! "
        scene black with dissolve
        " You spent the rest of class doing the activity. "
        " Once your group was done, you all passed it to the teacher. "
        " You guys were actually the third ones to pass, so you had a LOT of free time. "
        " ...And you spent all of that free time looking at your phone. "
        " What? you didn't want to disturb your classmates while they're working. "
        " Plus, your groupmates were already doing their own thing the moment you guys were done, and you didn't want to disturb them either. "
        " Sooo...more phone time, less complaining. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another break. "
        " You get out of your seat and you walk into the hallways... "
        pause 2.0
        jump wedbreak4
    label popularhistory:
        # the renaissance
        $ popularlv += 5
        " Let's see what the popular girls have in store for you today. "
        show petunianeutral at right with easeinleft
        show lizzyneutral at left with easeinleft
        if popularknow == True:
            " You walked over to them only to see that they were whispering to eachother about something. "
            " You could see a slight hint of annoyance on each of their faces, but for the most part, they look calm. "
            " Well, that's the front they're putting up. Making it seem like they're all fine and that... "
            " Wonder what happened. "
            " The moment that they noticed that you were there though, they immediately switched up and put their attention on you. "
            p " Heya there, [name]! "
            lz " Hi there. "
            " You greeted them both and then asked what they were talking about. "
            " Hopefully this won't cause a lot of drama. "
            p " Me and Liz were just talking about some things... "
            lz " Things about the project, of course. "
            p " You mean activity? "
            lz " ...The activity, yes. "
            p " You know, I was gonna say that we were TOTALLY talking about the activity and stuff but you beat me to it! "
            p " You're SOOOO good at predicting what I was gonna say, Liz! "
            hide petunianeutral at bottom
            show petuniaangry at right
            p " How fucking great you are. "
            lz " Yeah, thanks Petunia. Totally needed you to say that. "
            hide lizzyneutral at bottom
            show lizzyangry at left
            lz " Bitch.. "
            " Ooohh boy. "
            hide petuniaangry at bottom
            hide lizzyangry at bottom
            show petunianeutral at right
            show lizzyneutral at left
            p " Anyway! enough of the talking. "
            p " Let's get started with the ACTUAL project before the teacher starts killing us. "
            lz " The topic we got was renaissance. "
            lz " Pretty sure that Petunia doesn't even know what that is, with all of that air in her head. "
            p " Ha ha. Very funny, Liz. "
            p " Let's just copy something from the internet. "
            " While I would say that you had fun working with them... "
            " ...You couldn't help but feel the thick tension in the air. "
            " Wonder what happened for them to have such a bad disagreement. "
            " Probably not your business though. "
            scene black with dissolve
            " You spent the rest of class doing the activity. "
            " Once your group was done, you all passed it to the teacher. "
            " You guys were actually the fifth ones to pass, so you had some freetime on your hands. "
            " ...And you spent all of that free time looking at your phone. "
            " What? you didn't want to disturb your classmates while they're working. "
            " Plus, your groupmates were already doing their own thing the moment you guys were done, and you didn't want to disturb them either. "
            " Sooo...more phone time, less complaining. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You get out of your seat and you walk into the hallways... "
            pause 2.0
            jump wedbreak4
        else:
            " You walked over to them only to see that they were whispering to eachother about something. "
            " You could see a slight hint of annoyance on each of their faces, but for the most part, they look calm. "
            " Well, that's the front they're putting up. Making it seem like they're all fine and that... "
            " Wonder what happened. "
            " The moment that they noticed that you were there though, they immediately switched up and put their attention on you. "
            x " Heya there, [name]! "
            x " Hi there. "
            " You greeted them both and then asked what they were talking about. "
            " Hopefully this won't cause a lot of drama. "
            $ popularknow = True
            x " Me and Liz were just talking about some things... "
            lz " Things about the project, of course. "
            x " You mean activity? "
            lz " ...The activity, yes. "
            x " You know, I was gonna say that we were TOTALLY talking about the activity and stuff but you beat me to it! "
            x " You're SOOOO good at predicting what I was gonna say, Liz! "
            hide petunianeutral at bottom
            show petuniaangry at right
            x " How fucking great you are. "
            lz " Yeah, thanks Petunia. Totally needed you to say that. "
            hide lizzyneutral at bottom
            show lizzyangry at left
            lz " Bitch.. "
            " Ooohh boy. "
            hide petuniaangry at bottom
            hide lizzyangry at bottom
            show petunianeutral at right
            show lizzyneutral at left
            p " Anyway! enough of the talking. "
            p " Let's get started with the ACTUAL project before the teacher starts killing us. "
            lz " The topic we got was renaissance. "
            lz " Pretty sure that Petunia doesn't even know what that is, with all of that air in her head. "
            p " Ha ha. Very funny, Liz. "
            p " Let's just copy something from the internet. "
            " While I would say that you had fun working with them... "
            " ...You couldn't help but feel the thick tension in the air. "
            " Wonder what happened for them to have such a bad disagreement. "
            " Probably not your business though. "
            scene black with dissolve
            " You spent the rest of class doing the activity. "
            " Once your group was done, you all passed it to the teacher. "
            " You guys were actually the fifth ones to pass, so you had some freetime on your hands. "
            " ...And you spent all of that free time looking at your phone. "
            " What? you didn't want to disturb your classmates while they're working. "
            " Plus, your groupmates were already doing their own thing the moment you guys were done, and you didn't want to disturb them either. "
            " Sooo...more phone time, less complaining. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You get out of your seat and you walk into the hallways... "
            pause 2.0
            jump wedbreak4
    label cubkevhistory:
        $ cubbielv += 5
        $ kevinlv += 5
        # the french revolution
        " These nerds are for SURE gonna carry you for this activity. "
        " Smart people always know what they're talking about. Just follow their lead, and you should be fine. "
        show cubbieneutral at left with easeinright
        show kevinneutral at right with easeinright
        if cubbieknow == True and kevinknow == True:
            hide cubbieneutral at bottom
            show cubbiehappy at left
            cb " !!! "
            hide kevinneutral at bottom
            show kevinhappy at right
            kv " Oh, [name]. "
            kv " Lovely for you to join us for this project! "
            hide kevinhappy at bottom
            show kevinneutral at right
            kv " Anyway, our topic for this activity is gonna be... "
            kv " ... "
            kv " I was hoping that this would be a topic that I'd know about. "
            cb " ...? "
            kv " We have 'the french revolution'. "
            kv " Look - I was absent the day when we talked about that, and I had forgotten to ask for notes. "
            kv " Completely my fault, I know that. "
            cb " ... "
            hide kevinneutral at bottom
            show kevinangry at right
            kv " But I don't want to look at pictures online! "
            kv " I don't need no examples, I need knowledge! "
            kv " I need to actually learn from it from the teacher so that I know it's true! "
            kv " The teacher's are always right! "
            cb " (...Sigh.) "
            " You ended up asking the teacher for help since Kevin was being stubborn. "
            " A little embarrassing that you had to deal with this, but you can deal with worse. "
            " Maybe you should've picked another group though, if you were looking for something serious. "
            scene black with dissolve
            " You spent the rest of class doing the activity. "
            " Once your group was done, you all passed it to the teacher. "
            " You guys were actually the second ones to pass, so you had some freetime on your hands. "
            " ...And you spent all of that free time looking at your phone. "
            " What? you didn't want to disturb your classmates while they're working. "
            " Plus, your groupmates were already doing their own thing the moment you guys were done, and you didn't want to disturb them either. "
            " Sooo...more phone time, less complaining. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You get out of your seat and you walk into the hallways... "
            pause 2.0
            jump wedbreak4
        elif cubbieknow == True and kevinknow == False:
            hide cubbieneutral at bottom
            show cubbiehappy at left
            cb " !!! "
            hide kevinneutral at bottom
            show kevinhappy at right
            x " Oh, [name]. "
            x " Lovely for you to join us for this project! "
            $ kevinknow = True
            kv " I'm Kevin by the way, a pleasure meet you. "
            kv " If I can recall correctly, I don't think I introduced myself to you. So...there you go. "
            hide kevinhappy at bottom
            show kevinneutral at right
            kv " Anyway, our topic for this activity is gonna be... "
            kv " ... "
            kv " I was hoping that this would be a topic that I'd know about. "
            cb " ...? "
            kv " We have 'the french revolution'. "
            kv " Look - I was absent the day when we talked about that, and I had forgotten to ask for notes. "
            kv " Completely my fault, I know that. "
            cb " ... "
            hide kevinneutral at bottom
            show kevinangry at right
            kv " But I don't want to look at pictures online! "
            kv " I don't need no examples, I need knowledge! "
            kv " I need to actually learn from it from the teacher so that I know it's true! "
            kv " The teacher's are always right! "
            cb " (...Sigh.) "
            " You ended up asking the teacher for help since Kevin was being stubborn. "
            " A little embarrassing that you had to deal with this, but you can deal with worse. "
            " Maybe you should've picked another group though, if you were looking for something serious. "
            scene black with dissolve
            " You spent the rest of class doing the activity. "
            " Once your group was done, you all passed it to the teacher. "
            " You guys were actually the second ones to pass, so you had some freetime on your hands. "
            " ...And you spent all of that free time looking at your phone. "
            " What? you didn't want to disturb your classmates while they're working. "
            " Plus, your groupmates were already doing their own thing the moment you guys were done, and you didn't want to disturb them either. "
            " Sooo...more phone time, less complaining. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You get out of your seat and you walk into the hallways... "
            pause 2.0
            jump wedbreak4
        elif cubbieknow == False and kevinknow == True:
            hide cubbieneutral at bottom
            show cubbiehappy at left
            x " !!! "
            hide kevinneutral at bottom
            show kevinhappy at right
            kv " Oh, [name]. "
            kv " Lovely for you to join us for this project! "
            $ cubbieknow = True
            kv " This is my friend, Cubbie, by the way. "
            kv " I believe you two haven't met before...He also doesn't like to talk much. "
            hide kevinhappy at bottom
            show kevinneutral at right
            kv " Anyway, our topic for this activity is gonna be... "
            kv " ... "
            kv " I was hoping that this would be a topic that I'd know about. "
            cb " ...? "
            kv " We have 'the french revolution'. "
            kv " Look - I was absent the day when we talked about that, and I had forgotten to ask for notes. "
            kv " Completely my fault, I know that. "
            cb " ... "
            hide kevinneutral at bottom
            show kevinangry at right
            kv " But I don't want to look at pictures online! "
            kv " I don't need no examples, I need knowledge! "
            kv " I need to actually learn from it from the teacher so that I know it's true! "
            kv " The teacher's are always right! "
            cb " (...Sigh.) "
            " You ended up asking the teacher for help since Kevin was being stubborn. "
            " A little embarrassing that you had to deal with this, but you can deal with worse. "
            " Maybe you should've picked another group though, if you were looking for something serious. "
            scene black with dissolve
            " You spent the rest of class doing the activity. "
            " Once your group was done, you all passed it to the teacher. "
            " You guys were actually the second ones to pass, so you had some freetime on your hands. "
            " ...And you spent all of that free time looking at your phone. "
            " What? you didn't want to disturb your classmates while they're working. "
            " Plus, your groupmates were already doing their own thing the moment you guys were done, and you didn't want to disturb them either. "
            " Sooo...more phone time, less complaining. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You get out of your seat and you walk into the hallways... "
            pause 2.0
            jump wedbreak4
        else:
            hide cubbieneutral at bottom
            show cubbiehappy at left
            cb " !!! "
            hide kevinneutral at bottom
            show kevinhappy at right
            x " Oh, [name]. "
            x " Lovely for you to join us for this project! "
            $ kevinknow = True
            kv " I'm Kevin by the way, a pleasure meet you. "
            kv " If I can recall correctly, I don't think I introduced myself to you. So...there you go. "
            $ cubbieknow = True
            kv " This is my friend, Cubbie, by the way. "
            kv " I believe you two haven't met before...He also doesn't like to talk much. "
            hide kevinhappy at bottom
            show kevinneutral at right
            kv " Anyway, our topic for this activity is gonna be... "
            kv " ... "
            kv " I was hoping that this would be a topic that I'd know about. "
            cb " ...? "
            kv " We have 'the french revolution'. "
            kv " Look - I was absent the day when we talked about that, and I had forgotten to ask for notes. "
            kv " Completely my fault, I know that. "
            cb " ... "
            hide kevinneutral at bottom
            show kevinangry at right
            kv " But I don't want to look at pictures online! "
            kv " I don't need no examples, I need knowledge! "
            kv " I need to actually learn from it from the teacher so that I know it's true! "
            kv " The teacher's are always right! "
            cb " (...Sigh.) "
            " You ended up asking the teacher for help since Kevin was being stubborn. "
            " A little embarrassing that you had to deal with this, but you can deal with worse. "
            " Maybe you should've picked another group though, if you were looking for something serious. "
            scene black with dissolve
            " You spent the rest of class doing the activity. "
            " Once your group was done, you all passed it to the teacher. "
            " You guys were actually the second ones to pass, so you had some freetime on your hands. "
            " ...And you spent all of that free time looking at your phone. "
            " What? you didn't want to disturb your classmates while they're working. "
            " Plus, your groupmates were already doing their own thing the moment you guys were done, and you didn't want to disturb them either. "
            " Sooo...more phone time, less complaining. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another break. "
            " You get out of your seat and you walk into the hallways... "
            pause 2.0
            jump wedbreak4
    label ruriroskhistory:
        $ rubylv += 5
        $ skelllv += 5
        $ robbrileylv += 5
        # the harlem renaissance
        " Surely the more members you have, the faster you're gonna finish this... "
        " Riiighhhtt?? "
        " Well, let me give you a summary instead of making you having to go through pain. "
        " First of all, Riley wasn't even paying attention to what the topic was... "
        " ...Which was the harlem renaissance. "
        " She was just staring and absolutely drooling at Oliver. "
        " She wouldn't budge until you promised that you'd give her a drawing signed by Oliver himself. "
        " Ruby kept on crashing every now and then, having Skell reboot her taking some more time if she had an idea but then got cut off or something. "
        " Really, the only people in your group that was locked in was you, Skell, and Robby. "
        if rubyknow,robbyknow,rileyknow,skellknow == True:
            pass
        else:
            " You probably don't know who some of the people were (the people I just mentioned), but I don't really care. "
            pass
        " Well, Ruby was kind of locked in. She was trying her best, really... "
        " ...But she was crashing too much. "
        scene black with dissolve
        " You guys ended up being the last to pass your work. "
        " Atleast you had some time to yourself after you all were done... "
        " ...And you spent your time scrolling on your phone. "
        " Wow, you're so productive or something. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another break. "
        " You get out of your seat and you walk into the hallways... "
        pause 2.0
        jump wedbreak4
    label alonehistory:
        " You decided to do this project alone. "
        " You got your project and started working... "
        scene black with dissolve
        " ...And then eventually, you finished your work. "
        " You were the fourth one to pass. That didn't bother you though. "
        " You still had a lot of freetime because you passed a bit early. "
        " ...And you spent all of that free time looking at your phone. "
        " What? you didn't want to disturb your classmates while they're working. "
        " Plus, your groupmates were already doing their own thing the moment you guys were done, and you didn't want to disturb them either. "
        " Sooo...more phone time, less complaining. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another break. "
        " You get out of your seat and you walk into the hallways... "
        pause 2.0
        jump wedbreak4
    label oliganghistoryrah:
        $ oliganglv += 5
        # protest art in the 1960s
        " You walked over to your gang and saw how they were doing. "
        " Just lowkey vibing... "
        " ...Not doing the work at all. "
        show zipneutral at left with easeinright
        show oliverneutral at center with easeinright
        show edwardneutral at right with easeinright
        o " Sup [name]. "
        ed " Yoooo, it's you! "
        z " We've already done the project thing, so no worries. "
        o " It's right over here... "
        " Oliver points and the center of the table, and at the center, you saw... "
        " ...A very poorly made drawing of protest art. "
        " It just says 'in 1960s' in the corner and theres angry stickmen. "
        " This was just 'protest art in the 1960s'. But..not really done well. "
        " I mean, what were you expecting from these three? "
        " Art like the Mona Lisa? "
        o " Amazing, right? "
        ed " We know, we have good art skills. "
        o " You see, [name]... "
        o " The teachers here just let us do everything we want. "
        o " First it was Miss Circle...then Miss Thavel...Then Miss Bloomie. "
        o " It was just them for awhile, but they somehow managed to convince the other teachers to give us good scores too. "
        hide oliverneutral at bottom
        show oliverhappy at center
        o " Pretty neat, aint it? "
        o " You can just spend the time on your phone and hanging out with us, no sweat. "
        o " You're gonna start realizing that this was a good decision to be with us. "
        hide oliverhappy at bottom
        show oliverneutral at center
        o " Or you already did, I dunno what I'm tryin' to say but you get the idea. "
        scene black with dissolve
        " You spent the rest of the break just chilling out. "
        " You didn't really do anything since Oliver just said that you could relax. "
        " Zip was drawing something...Edward was tinkering with a bot that he made... "
        " And he was also flexing it all to you because he thought it was really cool when it was just a simple bot. "
        " All it could do was wave its hand, but Edward said that he's gonna upgrade it in a bit. "
        play sound "audio/bellring.mp3"
        " The bell rings for a bit, time for another break. "
        " Another break with these three. "
        pause 2.0
        jump wedbreak4

label wedbreak4:
    scene hallway with dissolve
    if oligangjoin == True:
        jump wedoligang4
    else:
        pass
    " Where are we going for this break? "
    menu:
        " {image=skellicon} The front of the school {image=robbyicon} ":
            jump wedfrontschool4
        " {image=popularicon} The back of the school {image=kevinicon} ":
            jump wedbackschool4
        " {image=claireicon} The gym {image=rileyicon} ":
            jump wedgym4
        " The cafeteria ":
            jump wedcafeteria4
        " {image=rubyicon} The rooftop {image=bubbleicon} ":
            jump wedrooftop4
        " {image=cubbieicon} The library {image=lanaicon} ":
            jump wedlibrary4

label wedfrontschool4:
    # Skell + robby //  Skell and robby nerding out on a princess game.
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school and spotted your two classmates hanging out. "
    " Wondering what they're talking about as always, you decided to talk with them. "
    show skellneutral at left with easeinright
    show robbyneutral at right with easeinright
    if skellknow == True and robbyknow == True:
        sk " - Oh dude, and the outfits? they're great. "
        hide robbyneutral at bottom
        show robbyhappy at right
        rb " Of course they are! They've got some of the best outfit designers on the team! "
        rb " Why wouldn't they be in such high quality? "
        rb " God, I love this game so much. "
        sk " Hmmm...maybe after school, we could play together? "
        sk " See if anyone's doing a roleplay? "
        hide robbyhappy at bottom
        show robbyneutral at right
        rb " Well, people rarely do roleplays nowadays... "
        rb " But sure, if I have time tonight. "
        " You cough so that you could get their attention. "
        sk " Oh, hey there [name]. Didn't notice you. "
        rb " Guess we got too distracted on talking about this one game that we like... "
        rb " Should I tell [them] what game it is? "
        sk " I mean...sure. "
        rb " You sure? I mean, it's gonna be kind of surprising for [them] because you look like you're not the type to play these kinds of games. "
        rb " And honestly, neither do I... "
        sk " Come on, Robby. I'll be fine. "
        rb " ...The game we're talking about is Princess Tycoon. "
        hide skellneutral at bottom
        show skellangry at left
        sk " Ooookay, now the embarrassment's kicking in. "
        rb " Told you that you'd feel embarrassed. "
        menu:
            " NO WAY I PLAY THAT GAME TOO ":
                $ robbrileylv += 5
                $ skelllv += 10
                hide skellangry at bottom
                show skellsurprised at left
                rb " Wait, seriously? "
                sk " You're not pulling my leg, are you? "
                rb " ... "
                sk " ... "
                scene black with dissolve
                " For the rest of the break, you had to deal with Skell and Robby yapping to you about princess tycoon. "
                " Not that you minded though, since you did say that you played it too. "
                " While some of your opinions got Robby to almost go feral to you...it was all in good fun. "
                " You should probably talk with them more. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and you walked into your classroom for the next class. "
                pause 2.0
                jump musicclass3
            " interesting choice ig ":
                sk " Yeeeaaahhh... "
                hide robbyneutral at bottom
                show robbyhappy at right
                hide skellangry at bottom
                show skellneutral at left
                rb " It's a good game though! "
                rb " Especially with the outfits and stuff. "
                sk " Personally I like the weapons. "
                sk " The weapons are really sick. "
                sk " Whoever designed them, I'm gonna have to give them 60 bobux. "
                rb " Come on, Skell! They deserve more than that! "
                sk " I would've given them more if I wasn't so poor. "
                scene black with dissolve
                " You spent the rest of the break talking with Skell and Robby. "
                " Honestly, Robby was right. He and Skell really didn't look like people who would play Princess Tycoon. "
                " Though, you're not gonna judge them since they look like they really enjoy the game. "
                " Don't want to be a jerk now... "
                " ...Actually, you kind of want to check out princess tycoon now to see if it's really that good. "
                " Maybe if you have time tonight. Or maybe if you remember. "
                " Which is probably impossible. "
                " You literally have the memory of a gold fish. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and you walked into your classroom for the next class. "
                pause 2.0
                jump musicclass3
    elif skellknow == True and robbyknow == False:
        sk " - Oh dude, and the outfits? they're great. "
        hide robbyneutral at bottom
        show robbyhappy at right
        x " Of course they are! They've got some of the best outfit designers on the team! "
        x " Why wouldn't they be in such high quality? "
        x " God, I love this game so much. "
        sk " Hmmm...maybe after school, we could play together? "
        sk " See if anyone's doing a roleplay? "
        hide robbyhappy at bottom
        show robbyneutral at right
        x " Well, people rarely do roleplays nowadays... "
        x " But sure, if I have time tonight. "
        " You cough so that you could get their attention. "
        sk " Oh, hey there [name]. Didn't notice you. "
        x " Guess we got too distracted on talking about this one game that we like... "
        x " Hold on, I don't think I've introduced myself to [them] yet. One moment... "
        $ robbyknow = True
        rb " I'm Robby; Skell's good friend. It's nice to meet you. "
        rb " Anyway, should I tell [them] what game we were talking about? "
        sk " I mean...sure. "
        rb " You sure? I mean, it's gonna be kind of surprising for [them] because you look like you're not the type to play these kinds of games. "
        rb " And honestly, neither do I... "
        sk " Come on, Robby. I'll be fine. "
        rb " ...The game we're talking about is Princess Tycoon. "
        hide skellneutral at bottom
        show skellangry at left
        sk " Ooookay, now the embarrassment's kicking in. "
        rb " Told you that you'd feel embarrassed. "
        menu:
            " NO WAY I PLAY THAT GAME TOO ":
                $ robbrileylv += 5
                $ skelllv += 10
                hide skellangry at bottom
                show skellsurprised at left
                rb " Wait, seriously? "
                sk " You're not pulling my leg, are you? "
                rb " ... "
                sk " ... "
                scene black with dissolve
                " For the rest of the break, you had to deal with Skell and Robby yapping to you about princess tycoon. "
                " Not that you minded though, since you did say that you played it too. "
                " While some of your opinions got Robby to almost go feral to you...it was all in good fun. "
                " You should probably talk with them more. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and you walked into your classroom for the next class. "
                pause 2.0
                jump musicclass3
            " interesting choice ig ":
                sk " Yeeeaaahhh... "
                hide robbyneutral at bottom
                show robbyhappy at right
                hide skellangry at bottom
                show skellneutral at left
                rb " It's a good game though! "
                rb " Especially with the outfits and stuff. "
                sk " Personally I like the weapons. "
                sk " The weapons are really sick. "
                sk " Whoever designed them, I'm gonna have to give them 60 bobux. "
                rb " Come on, Skell! They deserve more than that! "
                sk " I would've given them more if I wasn't so poor. "
                scene black with dissolve
                " You spent the rest of the break talking with Skell and Robby. "
                " Honestly, Robby was right. He and Skell really didn't look like people who would play Princess Tycoon. "
                " Though, you're not gonna judge them since they look like they really enjoy the game. "
                " Don't want to be a jerk now... "
                " ...Actually, you kind of want to check out princess tycoon now to see if it's really that good. "
                " Maybe if you have time tonight. Or maybe if you remember. "
                " Which is probably impossible. "
                " You literally have the memory of a gold fish. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and you walked into your classroom for the next class. "
                pause 2.0
                jump musicclass3
    elif skellknow == False and robbyknow == True:
        x " - Oh dude, and the outfits? they're great. "
        hide robbyneutral at bottom
        show robbyhappy at right
        rb " Of course they are! They've got some of the best outfit designers on the team! "
        rb " Why wouldn't they be in such high quality? "
        rb " God, I love this game so much. "
        x " Hmmm...maybe after school, we could play together? "
        x " See if anyone's doing a roleplay? "
        hide robbyhappy at bottom
        show robbyneutral at right
        rb " Well, people rarely do roleplays nowadays... "
        rb " But sure, if I have time tonight. "
        " You cough so that you could get their attention. "
        x " Oh, hey there [name]. Didn't notice you. "
        rb " Guess we got too distracted on talking about this one game that we like... "
        rb " Wait, hey. I don't think You got to introduce yourself to [name] yet, Skell. "
        x " Mmmm...yeah, I forgot to do that, sorry. "
        $ skellknow = True
        sk " I'm Skell. It's nice to meet you. "
        rb " Lovely...now, should I tell [them] what game we were talking about? "
        sk " I mean...sure. "
        rb " You sure? I mean, it's gonna be kind of surprising for [them] because you look like you're not the type to play these kinds of games. "
        rb " And honestly, neither do I... "
        sk " Come on, Robby. I'll be fine. "
        rb " ...The game we're talking about is Princess Tycoon. "
        hide skellneutral at bottom
        show skellangry at left
        sk " Ooookay, now the embarrassment's kicking in. "
        rb " Told you that you'd feel embarrassed. "
        menu:
            " NO WAY I PLAY THAT GAME TOO ":
                $ robbrileylv += 5
                $ skelllv += 10
                hide skellangry at bottom
                show skellsurprised at left
                rb " Wait, seriously? "
                sk " You're not pulling my leg, are you? "
                rb " ... "
                sk " ... "
                scene black with dissolve
                " For the rest of the break, you had to deal with Skell and Robby yapping to you about princess tycoon. "
                " Not that you minded though, since you did say that you played it too. "
                " While some of your opinions got Robby to almost go feral to you...it was all in good fun. "
                " You should probably talk with them more. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and you walked into your classroom for the next class. "
                pause 2.0
                jump musicclass3
            " interesting choice ig ":
                sk " Yeeeaaahhh... "
                hide robbyneutral at bottom
                show robbyhappy at right
                hide skellangry at bottom
                show skellneutral at left
                rb " It's a good game though! "
                rb " Especially with the outfits and stuff. "
                sk " Personally I like the weapons. "
                sk " The weapons are really sick. "
                sk " Whoever designed them, I'm gonna have to give them 60 bobux. "
                rb " Come on, Skell! They deserve more than that! "
                sk " I would've given them more if I wasn't so poor. "
                scene black with dissolve
                " You spent the rest of the break talking with Skell and Robby. "
                " Honestly, Robby was right. He and Skell really didn't look like people who would play Princess Tycoon. "
                " Though, you're not gonna judge them since they look like they really enjoy the game. "
                " Don't want to be a jerk now... "
                " ...Actually, you kind of want to check out princess tycoon now to see if it's really that good. "
                " Maybe if you have time tonight. Or maybe if you remember. "
                " Which is probably impossible. "
                " You literally have the memory of a gold fish. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and you walked into your classroom for the next class. "
                pause 2.0
                jump musicclass3
    else:
        x " - Oh dude, and the outfits? they're great. "
        hide robbyneutral at bottom
        show robbyhappy at right
        x " Of course they are! They've got some of the best outfit designers on the team! "
        x " Why wouldn't they be in such high quality? "
        x " God, I love this game so much. "
        x " Hmmm...maybe after school, we could play together? "
        x " See if anyone's doing a roleplay? "
        hide robbyhappy at bottom
        show robbyneutral at right
        x " Well, people rarely do roleplays nowadays... "
        x " But sure, if I have time tonight. "
        " You cough so that you could get their attention. "
        x " Oh, hey there [name]. Didn't notice you. "
        x " Guess we got too distracted on talking about this one game that we like... "
        x " Wait, hey. I don't think You got to introduce yourself to [name] yet, Skell. "
        x " Mmmm...yeah, I forgot to do that, sorry. "
        $ skellknow = True
        sk " I'm Skell. It's nice to meet you. "
        x " Lovely. "
        x " Hold on, I don't think I've introduced myself to [them] yet. One moment... "
        $ robbyknow = True
        rb " I'm Robby; Skell's good friend. It's nice to meet you. "
        rb " Anyway, should I tell [them] what game we were talking about? "
        sk " I mean...sure. "
        rb " You sure? I mean, it's gonna be kind of surprising for [them] because you look like you're not the type to play these kinds of games. "
        rb " And honestly, neither do I... "
        sk " Come on, Robby. I'll be fine. "
        rb " ...The game we're talking about is Princess Tycoon. "
        hide skellneutral at bottom
        show skellangry at left
        sk " Ooookay, now the embarrassment's kicking in. "
        rb " Told you that you'd feel embarrassed. "
        menu:
            " NO WAY I PLAY THAT GAME TOO ":
                $ robbrileylv += 5
                $ skelllv += 10
                hide skellangry at bottom
                show skellsurprised at left
                rb " Wait, seriously? "
                sk " You're not pulling my leg, are you? "
                rb " ... "
                sk " ... "
                scene black with dissolve
                " For the rest of the break, you had to deal with Skell and Robby yapping to you about princess tycoon. "
                " Not that you minded though, since you did say that you played it too. "
                " While some of your opinions got Robby to almost go feral to you...it was all in good fun. "
                " You should probably talk with them more. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and you walked into your classroom for the next class. "
                pause 2.0
                jump musicclass3
            " interesting choice ig ":
                sk " Yeeeaaahhh... "
                hide robbyneutral at bottom
                show robbyhappy at right
                hide skellangry at bottom
                show skellneutral at left
                rb " It's a good game though! "
                rb " Especially with the outfits and stuff. "
                sk " Personally I like the weapons. "
                sk " The weapons are really sick. "
                sk " Whoever designed them, I'm gonna have to give them 60 bobux. "
                rb " Come on, Skell! They deserve more than that! "
                sk " I would've given them more if I wasn't so poor. "
                scene black with dissolve
                " You spent the rest of the break talking with Skell and Robby. "
                " Honestly, Robby was right. He and Skell really didn't look like people who would play Princess Tycoon. "
                " Though, you're not gonna judge them since they look like they really enjoy the game. "
                " Don't want to be a jerk now... "
                " ...Actually, you kind of want to check out princess tycoon now to see if it's really that good. "
                " Maybe if you have time tonight. Or maybe if you remember. "
                " Which is probably impossible. "
                " You literally have the memory of a gold fish. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and you walked into your classroom for the next class. "
                pause 2.0
                jump musicclass3

label wedbackschool4:
    # Kevin + petunia // petunia wants advice
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and spotted two of your classmates having a conversation. "
    " Wondering what they're talking about, you walk up to them and see what they talk about. "
    show petunianeutral at right with easeinright
    show kevinneutral at left with easeinleft
    if popularknow == True and kevinknow == True:
        p " Hi [name]! Just asking Kevin a few questions here... "
        kv " Questions that are probably irrelevant to my studies. "
        p " Come on, Kev! "
        p " I just need you to answer these questions, and I'll leave you alone. "
        kv " As long as you'd leave me alone afterwards... "
        kv " Alright, what do you want, Petunia? "
        p " Well, me and Lizzy recently have been having more...disagreements. "
        p " I wonder if it's something that I did or something I said. "
        kv " Depends on what you did or said then. "
        kv " If you want to know what you did wrong, then you've got to talk to Lizzy. "
        kv " Can't just ask me since I don't even know what happened. "
        hide petunianeutral at bottom
        show petuniasurprised at right
        p " But I can't talk to her! I'm pretty sure she hates me... "
        kv " Even if she hates you or something, you've still got to try and talk. "
        kv " If she doesn't respond to you, just leave her alone for a bit. "
        kv " Give her space, you know? "
        kv " Now anyway, I'll get on with my studies. "
        hide petuniasurprised at bottom
        show petuniaangry at center with move
        hide kevinneutral at right with easeoutright
        " Kevin goes to another spot in the back of the school, leaving Petunia standing there and looking annoyed. "
        p " Dammit, knew he was gonna be of no help... "
        " Well this is awkward. "
        " Who do you want to stay with? "
        menu:
            " Stay with Petunia ":
                $ popularlv += 10
                " You asked Petunia if she was alright. "
                hide petuniaangry at bottom
                show petuniasad at center
                p " ...Yeah. I'm fine. "
                p " I just wanted to know why me and Lizzy are having drama with eachother. "
                p " Having drama with a bestie is NOT hot, I tell you. "
                p " I wanted to know what was up, but Lizzy...Lizzy didn't really tell me anything. "
                p " That's why it's so confusing! Why won't she talk to me?? I just want to work things out... "
                p " ...*Sigh*. "
                p " This is kind of tiring me out. "
                " You asked if it would be alright for you to just hang out with her a bit to distract her. "
                " She probably needed to talk about something different for now so that she feels better. "
                p " ...That would be great. Thank you. "
                " You and Petunia sat down somewhere on a bench at the back of the school. "
                " And you began listening to her talk about other dramas and stuff... "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia. "
                " She looked like she felt better as she continued talking to you. "
                " You were glad that she was atleast feeling a bit better. "
                play sound "audio/bellring.mp3"
                " The bell ringsafter a bit, stopping your conversation with Petunia. "
                " You get up from the bench you were sitting on, and you walked back into your classroom for the next class. "
                pause 2.0
                jump musicclass3
            " Walk over to Kevin ":
                $ kevinlv += 10
                hide petuniaangry at left with easeoutleft
                " You decided to go and hangout with Kevin for a bit. "
                " You didn't really want to deal with an angry popular girl for now. "
                " Plus, you might get attacked for talking to her with how angry she looks. "
                " Yikes. Definitely don't want that to happen for you. "
                " Otherwise this game would be much shorter, like the demo. "
                show kevinneutral at center with easeinright
                " You find Kevin sitting near a batch of flowers on the ground. "
                " You sat down next to him and it looked like he was studying. "
                " Hoping you weren't bothering him, you asked him what he was studying about. "
                kv " ...? Oh, it's you. "
                kv " I didn't think you'd come with me, honestly... "
                kv " But I guess it's kind of understandable since Petunia's a bit scary when she's mad. "
                kv " I'm studying for our music class, which is right after this break. "
                hide kevinneutral at bottom
                show kevinhappy at center
                kv " Who knows? maybe there might be a quiz that Mister Demi might throw at us! "
                kv " I always love me a good quiz about music, hmhm... "
                hide kevinhappy at bottom
                show kevinneutral at center
                " Kevin goes silent for a bit, his eyes darting around his notebook, taking in the notes he wrote. "
                " Honestly, his writing looked like the writing of a doctor's. "
                " How does one even understand this? Maybe it's best for you to not ask him for notes if you missed out on anything. "
                " After a bit, he eventually speaks up. "
                kv " ...You know, I actually know the reason why Petunia and Lizzy have been beefing with eachother for a bit now. "
                kv " It all started last night. "
                if populartiktok == True or populartiktoklater == True:
                    kv " You know how you joined in on making a video with them? "
                    kv " Well, that video blew up by a LOT, I'll tell you that. "
                    kv " People really liked you. "
                    kv " Infact, liked you so much that they wanted more content of you. "
                    kv " Lizzy was mostly the hot topic for their little channel, but now that you were there... "
                    kv " ...Things kind of started to turn a bit. "
                    kv " People have been commenting about things like you and Petunia being a pair... "
                    kv " Completely forgetting about Lizzy. "
                    kv " Literally, every video I check on their account, there's only about 5 people who ever comment about her. "
                    kv " And the others? It's just about either you or Petunia. Or both of you. "
                    kv " And naturally, Lizzy got jealous. "
                    kv " Lizzy started attacking Petunia for it...with words of course. "
                    kv " Calling her multiple insults... "
                    kv " All of that. "
                    kv " She hasn't even explained why she's mad at Petunia yet. "
                    kv " Since you're close with them, maybe you could try fixing their relationship? "
                    kv " Just a suggestion, of course. "
                    kv " You don't gotta do it if you don't want to. "
                    pass
                else:
                    kv " Let's just say that Lizzy got jealous over Petunia's friend. "
                    kv " Petunia's friend was kind of hanging out with Petunia way too much... "
                    kv " ...Annnd naturally, Lizzy got jealous. "
                    kv " A little stupid to get jealous at that, but I'm not gonna judge. "
                    pass
                kv " But yeah, that's the story. "
                kv " Looks like Petunia left before she could even hear me explaining stuff to you... "
                kv " Maybe looking for some other people to talk to. "
                kv " To fill Lizzy's spot for now... "
                kv " ...Moving on with the topic, how about we study? "
                " You don't really have a choice in this. "
                hide kevinneutral at bottom
                show kevinhappy at center
                kv " Great! I always love a good study buddy! "
                scene black with dissolve
                " You spent the rest of the break studying with Kevin. "
                " As you were studying with him, you couldn't help but feel worried for Petunia and Lizzy... "
                " Hopefully they're gonna be alright. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for music class. "
                " You get up from where you were sitting, and you walked back to your classroom for music class. "
                pause 2.0
                jump musicclass3
            " Nah, this is too much drama for me ":
                hide petuniaangry at right with easeoutright
                " You decided that this was just too much drama for you and left. "
                scene black with dissolve
                " You spent the rest of the break wandering the halls, looking for some good gossip... "
                " Unfortunately nothing good though. "
                " Man, you could've asked for some gossip from Petunia and Lizzy... "
                " ...Only if they weren't so torn apart right now. "
                " You can only hope that they'll get better soon. "
                play sound "audio/bellring.mp3"
                " After a bit of walking around, the bell rings. Time for music class. "
                " You walked into your classroom and you sat in your seat. "
                pause 2.0
                jump musicclass3
    elif popularknow == True and kevinknow == False:
        p " Hi [name]! Just asking Kevin a few questions here... "
        $ kevinknow = True
        kv " Questions that are probably irrelevant to my studies. "
        p " Come on, Kev! "
        p " I just need you to answer these questions, and I'll leave you alone. "
        kv " As long as you'd leave me alone afterwards... "
        kv " Alright, what do you want, Petunia? "
        p " Well, me and Lizzy recently have been having more...disagreements. "
        p " I wonder if it's something that I did or something I said. "
        kv " Depends on what you did or said then. "
        kv " If you want to know what you did wrong, then you've got to talk to Lizzy. "
        kv " Can't just ask me since I don't even know what happened. "
        hide petunianeutral at bottom
        show petuniasurprised at right
        p " But I can't talk to her! I'm pretty sure she hates me... "
        kv " Even if she hates you or something, you've still got to try and talk. "
        kv " If she doesn't respond to you, just leave her alone for a bit. "
        kv " Give her space, you know? "
        kv " Now anyway, I'll get on with my studies. "
        hide petuniasurprised at bottom
        show petuniaangry at center with move
        hide kevinneutral at right with easeoutright
        " Kevin goes to another spot in the back of the school, leaving Petunia standing there and looking annoyed. "
        p " Dammit, knew he was gonna be of no help... "
        " Well this is awkward. "
        " Who do you want to stay with? "
        menu:
            " Stay with Petunia ":
                $ popularlv += 10
                " You asked Petunia if she was alright. "
                hide petuniaangry at bottom
                show petuniasad at center
                p " ...Yeah. I'm fine. "
                p " I just wanted to know why me and Lizzy are having drama with eachother. "
                p " Having drama with a bestie is NOT hot, I tell you. "
                p " I wanted to know what was up, but Lizzy...Lizzy didn't really tell me anything. "
                p " That's why it's so confusing! Why won't she talk to me?? I just want to work things out... "
                p " ...*Sigh*. "
                p " This is kind of tiring me out. "
                " You asked if it would be alright for you to just hang out with her a bit to distract her. "
                " She probably needed to talk about something different for now so that she feels better. "
                p " ...That would be great. Thank you. "
                " You and Petunia sat down somewhere on a bench at the back of the school. "
                " And you began listening to her talk about other dramas and stuff... "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia. "
                " She looked like she felt better as she continued talking to you. "
                " You were glad that she was atleast feeling a bit better. "
                play sound "audio/bellring.mp3"
                " The bell ringsafter a bit, stopping your conversation with Petunia. "
                " You get up from the bench you were sitting on, and you walked back into your classroom for the next class. "
                pause 2.0
                jump musicclass3
            " Walk over to Kevin ":
                $ kevinlv += 10
                hide petuniaangry at left with easeoutleft
                " You decided to go and hangout with Kevin for a bit. "
                " You didn't really want to deal with an angry popular girl for now. "
                " Plus, you might get attacked for talking to her with how angry she looks. "
                " Yikes. Definitely don't want that to happen for you. "
                " Otherwise this game would be much shorter, like the demo. "
                show kevinneutral at center with easeinright
                " You find Kevin sitting near a batch of flowers on the ground. "
                " You sat down next to him and it looked like he was studying. "
                " Hoping you weren't bothering him, you asked him what he was studying about. "
                kv " ...? Oh, it's you. "
                kv " I didn't think you'd come with me, honestly... "
                kv " But I guess it's kind of understandable since Petunia's a bit scary when she's mad. "
                kv " I'm studying for our music class, which is right after this break. "
                hide kevinneutral at bottom
                show kevinhappy at center
                kv " Who knows? maybe there might be a quiz that Mister Demi might throw at us! "
                kv " I always love me a good quiz about music, hmhm... "
                hide kevinhappy at bottom
                show kevinneutral at center
                " Kevin goes silent for a bit, his eyes darting around his notebook, taking in the notes he wrote. "
                " Honestly, his writing looked like the writing of a doctor's. "
                " How does one even understand this? Maybe it's best for you to not ask him for notes if you missed out on anything. "
                " After a bit, he eventually speaks up. "
                kv " ...You know, I actually know the reason why Petunia and Lizzy have been beefing with eachother for a bit now. "
                kv " It all started last night. "
                if populartiktok == True or populartiktoklater == True:
                    kv " You know how you joined in on making a video with them? "
                    kv " Well, that video blew up by a LOT, I'll tell you that. "
                    kv " People really liked you. "
                    kv " Infact, liked you so much that they wanted more content of you. "
                    kv " Lizzy was mostly the hot topic for their little channel, but now that you were there... "
                    kv " ...Things kind of started to turn a bit. "
                    kv " People have been commenting about things like you and Petunia being a pair... "
                    kv " Completely forgetting about Lizzy. "
                    kv " Literally, every video I check on their account, there's only about 5 people who ever comment about her. "
                    kv " And the others? It's just about either you or Petunia. Or both of you. "
                    kv " And naturally, Lizzy got jealous. "
                    kv " Lizzy started attacking Petunia for it...with words of course. "
                    kv " Calling her multiple insults... "
                    kv " All of that. "
                    kv " She hasn't even explained why she's mad at Petunia yet. "
                    kv " Since you're close with them, maybe you could try fixing their relationship? "
                    kv " Just a suggestion, of course. "
                    kv " You don't gotta do it if you don't want to. "
                    pass
                else:
                    kv " Let's just say that Lizzy got jealous over Petunia's friend. "
                    kv " Petunia's friend was kind of hanging out with Petunia way too much... "
                    kv " ...Annnd naturally, Lizzy got jealous. "
                    kv " A little stupid to get jealous at that, but I'm not gonna judge. "
                    pass
                kv " But yeah, that's the story. "
                kv " Looks like Petunia left before she could even hear me explaining stuff to you... "
                kv " Maybe looking for some other people to talk to. "
                kv " To fill Lizzy's spot for now... "
                kv " ...Moving on with the topic, how about we study? "
                " You don't really have a choice in this. "
                hide kevinneutral at bottom
                show kevinhappy at center
                kv " Great! I always love a good study buddy! "
                scene black with dissolve
                " You spent the rest of the break studying with Kevin. "
                " As you were studying with him, you couldn't help but feel worried for Petunia and Lizzy... "
                " Hopefully they're gonna be alright. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for music class. "
                " You get up from where you were sitting, and you walked back to your classroom for music class. "
                pause 2.0
                jump musicclass3
            " Nah, this is too much drama for me ":
                hide petuniaangry at right with easeoutright
                " You decided that this was just too much drama for you and left. "
                scene black with dissolve
                " You spent the rest of the break wandering the halls, looking for some good gossip... "
                " Unfortunately nothing good though. "
                " Man, you could've asked for some gossip from Petunia and Lizzy... "
                " ...Only if they weren't so torn apart right now. "
                " You can only hope that they'll get better soon. "
                play sound "audio/bellring.mp3"
                " After a bit of walking around, the bell rings. Time for music class. "
                " You walked into your classroom and you sat in your seat. "
                pause 2.0
                jump musicclass3
    elif popularknow == False and kevinknow == True:
        x " Hi [name]! Just asking Kevin a few questions here... "
        kv " Questions that are probably irrelevant to my studies. "
        x " Come on, Kev! "
        x " I just need you to answer these questions, and I'll leave you alone. "
        kv " As long as you'd leave me alone afterwards... "
        $ popularknow = True
        kv " Alright, what do you want, Petunia? "
        p " Well, me and Lizzy recently have been having more...disagreements. "
        p " I wonder if it's something that I did or something I said. "
        kv " Depends on what you did or said then. "
        kv " If you want to know what you did wrong, then you've got to talk to Lizzy. "
        kv " Can't just ask me since I don't even know what happened. "
        hide petunianeutral at bottom
        show petuniasurprised at right
        p " But I can't talk to her! I'm pretty sure she hates me... "
        kv " Even if she hates you or something, you've still got to try and talk. "
        kv " If she doesn't respond to you, just leave her alone for a bit. "
        kv " Give her space, you know? "
        kv " Now anyway, I'll get on with my studies. "
        hide petuniasurprised at bottom
        show petuniaangry at center with move
        hide kevinneutral at right with easeoutright
        " Kevin goes to another spot in the back of the school, leaving Petunia standing there and looking annoyed. "
        p " Dammit, knew he was gonna be of no help... "
        " Well this is awkward. "
        " Who do you want to stay with? "
        menu:
            " Stay with Petunia ":
                $ popularlv += 10
                " You asked Petunia if she was alright. "
                hide petuniaangry at bottom
                show petuniasad at center
                p " ...Yeah. I'm fine. "
                p " I just wanted to know why me and Lizzy are having drama with eachother. "
                p " Having drama with a bestie is NOT hot, I tell you. "
                p " I wanted to know what was up, but Lizzy...Lizzy didn't really tell me anything. "
                p " That's why it's so confusing! Why won't she talk to me?? I just want to work things out... "
                p " ...*Sigh*. "
                p " This is kind of tiring me out. "
                " You asked if it would be alright for you to just hang out with her a bit to distract her. "
                " She probably needed to talk about something different for now so that she feels better. "
                p " ...That would be great. Thank you. "
                " You and Petunia sat down somewhere on a bench at the back of the school. "
                " And you began listening to her talk about other dramas and stuff... "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia. "
                " She looked like she felt better as she continued talking to you. "
                " You were glad that she was atleast feeling a bit better. "
                play sound "audio/bellring.mp3"
                " The bell ringsafter a bit, stopping your conversation with Petunia. "
                " You get up from the bench you were sitting on, and you walked back into your classroom for the next class. "
                pause 2.0
                jump musicclass3
            " Walk over to Kevin ":
                $ kevinlv += 10
                hide petuniaangry at left with easeoutleft
                " You decided to go and hangout with Kevin for a bit. "
                " You didn't really want to deal with an angry popular girl for now. "
                " Plus, you might get attacked for talking to her with how angry she looks. "
                " Yikes. Definitely don't want that to happen for you. "
                " Otherwise this game would be much shorter, like the demo. "
                show kevinneutral at center with easeinright
                " You find Kevin sitting near a batch of flowers on the ground. "
                " You sat down next to him and it looked like he was studying. "
                " Hoping you weren't bothering him, you asked him what he was studying about. "
                kv " ...? Oh, it's you. "
                kv " I didn't think you'd come with me, honestly... "
                kv " But I guess it's kind of understandable since Petunia's a bit scary when she's mad. "
                kv " I'm studying for our music class, which is right after this break. "
                hide kevinneutral at bottom
                show kevinhappy at center
                kv " Who knows? maybe there might be a quiz that Mister Demi might throw at us! "
                kv " I always love me a good quiz about music, hmhm... "
                hide kevinhappy at bottom
                show kevinneutral at center
                " Kevin goes silent for a bit, his eyes darting around his notebook, taking in the notes he wrote. "
                " Honestly, his writing looked like the writing of a doctor's. "
                " How does one even understand this? Maybe it's best for you to not ask him for notes if you missed out on anything. "
                " After a bit, he eventually speaks up. "
                kv " ...You know, I actually know the reason why Petunia and Lizzy have been beefing with eachother for a bit now. "
                kv " It all started last night. "
                if populartiktok == True or populartiktoklater == True:
                    kv " You know how you joined in on making a video with them? "
                    kv " Well, that video blew up by a LOT, I'll tell you that. "
                    kv " People really liked you. "
                    kv " Infact, liked you so much that they wanted more content of you. "
                    kv " Lizzy was mostly the hot topic for their little channel, but now that you were there... "
                    kv " ...Things kind of started to turn a bit. "
                    kv " People have been commenting about things like you and Petunia being a pair... "
                    kv " Completely forgetting about Lizzy. "
                    kv " Literally, every video I check on their account, there's only about 5 people who ever comment about her. "
                    kv " And the others? It's just about either you or Petunia. Or both of you. "
                    kv " And naturally, Lizzy got jealous. "
                    kv " Lizzy started attacking Petunia for it...with words of course. "
                    kv " Calling her multiple insults... "
                    kv " All of that. "
                    kv " She hasn't even explained why she's mad at Petunia yet. "
                    kv " Since you're close with them, maybe you could try fixing their relationship? "
                    kv " Just a suggestion, of course. "
                    kv " You don't gotta do it if you don't want to. "
                    pass
                else:
                    kv " Let's just say that Lizzy got jealous over Petunia's friend. "
                    kv " Petunia's friend was kind of hanging out with Petunia way too much... "
                    kv " ...Annnd naturally, Lizzy got jealous. "
                    kv " A little stupid to get jealous at that, but I'm not gonna judge. "
                    pass
                kv " But yeah, that's the story. "
                kv " Looks like Petunia left before she could even hear me explaining stuff to you... "
                kv " Maybe looking for some other people to talk to. "
                kv " To fill Lizzy's spot for now... "
                kv " ...Moving on with the topic, how about we study? "
                " You don't really have a choice in this. "
                hide kevinneutral at bottom
                show kevinhappy at center
                kv " Great! I always love a good study buddy! "
                scene black with dissolve
                " You spent the rest of the break studying with Kevin. "
                " As you were studying with him, you couldn't help but feel worried for Petunia and Lizzy... "
                " Hopefully they're gonna be alright. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for music class. "
                " You get up from where you were sitting, and you walked back to your classroom for music class. "
                pause 2.0
                jump musicclass3
            " Nah, this is too much drama for me ":
                hide petuniaangry at right with easeoutright
                " You decided that this was just too much drama for you and left. "
                scene black with dissolve
                " You spent the rest of the break wandering the halls, looking for some good gossip... "
                " Unfortunately nothing good though. "
                " Man, you could've asked for some gossip from Petunia and Lizzy... "
                " ...Only if they weren't so torn apart right now. "
                " You can only hope that they'll get better soon. "
                play sound "audio/bellring.mp3"
                " After a bit of walking around, the bell rings. Time for music class. "
                " You walked into your classroom and you sat in your seat. "
                pause 2.0
                jump musicclass3
    else:
        x " Hi [name]! Just asking Kevin a few questions here... "
        $ kevinknow = True
        kv " Questions that are probably irrelevant to my studies. "
        x " Come on, Kev! "
        x " I just need you to answer these questions, and I'll leave you alone. "
        kv " As long as you'd leave me alone afterwards... "
        $ popularknow = True
        kv " Alright, what do you want, Petunia? "
        p " Well, me and Lizzy recently have been having more...disagreements. "
        p " I wonder if it's something that I did or something I said. "
        kv " Depends on what you did or said then. "
        kv " If you want to know what you did wrong, then you've got to talk to Lizzy. "
        kv " Can't just ask me since I don't even know what happened. "
        hide petunianeutral at bottom
        show petuniasurprised at right
        p " But I can't talk to her! I'm pretty sure she hates me... "
        kv " Even if she hates you or something, you've still got to try and talk. "
        kv " If she doesn't respond to you, just leave her alone for a bit. "
        kv " Give her space, you know? "
        kv " Now anyway, I'll get on with my studies. "
        hide petuniasurprised at bottom
        show petuniaangry at center with move
        hide kevinneutral at right with easeoutright
        " Kevin goes to another spot in the back of the school, leaving Petunia standing there and looking annoyed. "
        p " Dammit, knew he was gonna be of no help... "
        " Well this is awkward. "
        " Who do you want to stay with? "
        menu:
            " Stay with Petunia ":
                $ popularlv += 10
                " You asked Petunia if she was alright. "
                hide petuniaangry at bottom
                show petuniasad at center
                p " ...Yeah. I'm fine. "
                p " I just wanted to know why me and Lizzy are having drama with eachother. "
                p " Having drama with a bestie is NOT hot, I tell you. "
                p " I wanted to know what was up, but Lizzy...Lizzy didn't really tell me anything. "
                p " That's why it's so confusing! Why won't she talk to me?? I just want to work things out... "
                p " ...*Sigh*. "
                p " This is kind of tiring me out. "
                " You asked if it would be alright for you to just hang out with her a bit to distract her. "
                " She probably needed to talk about something different for now so that she feels better. "
                p " ...That would be great. Thank you. "
                " You and Petunia sat down somewhere on a bench at the back of the school. "
                " And you began listening to her talk about other dramas and stuff... "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia. "
                " She looked like she felt better as she continued talking to you. "
                " You were glad that she was atleast feeling a bit better. "
                play sound "audio/bellring.mp3"
                " The bell ringsafter a bit, stopping your conversation with Petunia. "
                " You get up from the bench you were sitting on, and you walked back into your classroom for the next class. "
                pause 2.0
                jump musicclass3
            " Walk over to Kevin ":
                $ kevinlv += 10
                hide petuniaangry at left with easeoutleft
                " You decided to go and hangout with Kevin for a bit. "
                " You didn't really want to deal with an angry popular girl for now. "
                " Plus, you might get attacked for talking to her with how angry she looks. "
                " Yikes. Definitely don't want that to happen for you. "
                " Otherwise this game would be much shorter, like the demo. "
                show kevinneutral at center with easeinright
                " You find Kevin sitting near a batch of flowers on the ground. "
                " You sat down next to him and it looked like he was studying. "
                " Hoping you weren't bothering him, you asked him what he was studying about. "
                kv " ...? Oh, it's you. "
                kv " I didn't think you'd come with me, honestly... "
                kv " But I guess it's kind of understandable since Petunia's a bit scary when she's mad. "
                kv " I'm studying for our music class, which is right after this break. "
                hide kevinneutral at bottom
                show kevinhappy at center
                kv " Who knows? maybe there might be a quiz that Mister Demi might throw at us! "
                kv " I always love me a good quiz about music, hmhm... "
                hide kevinhappy at bottom
                show kevinneutral at center
                " Kevin goes silent for a bit, his eyes darting around his notebook, taking in the notes he wrote. "
                " Honestly, his writing looked like the writing of a doctor's. "
                " How does one even understand this? Maybe it's best for you to not ask him for notes if you missed out on anything. "
                " After a bit, he eventually speaks up. "
                kv " ...You know, I actually know the reason why Petunia and Lizzy have been beefing with eachother for a bit now. "
                kv " It all started last night. "
                if populartiktok == True or populartiktoklater == True:
                    kv " You know how you joined in on making a video with them? "
                    kv " Well, that video blew up by a LOT, I'll tell you that. "
                    kv " People really liked you. "
                    kv " Infact, liked you so much that they wanted more content of you. "
                    kv " Lizzy was mostly the hot topic for their little channel, but now that you were there... "
                    kv " ...Things kind of started to turn a bit. "
                    kv " People have been commenting about things like you and Petunia being a pair... "
                    kv " Completely forgetting about Lizzy. "
                    kv " Literally, every video I check on their account, there's only about 5 people who ever comment about her. "
                    kv " And the others? It's just about either you or Petunia. Or both of you. "
                    kv " And naturally, Lizzy got jealous. "
                    kv " Lizzy started attacking Petunia for it...with words of course. "
                    kv " Calling her multiple insults... "
                    kv " All of that. "
                    kv " She hasn't even explained why she's mad at Petunia yet. "
                    kv " Since you're close with them, maybe you could try fixing their relationship? "
                    kv " Just a suggestion, of course. "
                    kv " You don't gotta do it if you don't want to. "
                    pass
                else:
                    kv " Let's just say that Lizzy got jealous over Petunia's friend. "
                    kv " Petunia's friend was kind of hanging out with Petunia way too much... "
                    kv " ...Annnd naturally, Lizzy got jealous. "
                    kv " A little stupid to get jealous at that, but I'm not gonna judge. "
                    pass
                kv " But yeah, that's the story. "
                kv " Looks like Petunia left before she could even hear me explaining stuff to you... "
                kv " Maybe looking for some other people to talk to. "
                kv " To fill Lizzy's spot for now... "
                kv " ...Moving on with the topic, how about we study? "
                " You don't really have a choice in this. "
                hide kevinneutral at bottom
                show kevinhappy at center
                kv " Great! I always love a good study buddy! "
                scene black with dissolve
                " You spent the rest of the break studying with Kevin. "
                " As you were studying with him, you couldn't help but feel worried for Petunia and Lizzy... "
                " Hopefully they're gonna be alright. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for music class. "
                " You get up from where you were sitting, and you walked back to your classroom for music class. "
                pause 2.0
                jump musicclass3
            " Nah, this is too much drama for me ":
                hide petuniaangry at right with easeoutright
                " You decided that this was just too much drama for you and left. "
                scene black with dissolve
                " You spent the rest of the break wandering the halls, looking for some good gossip... "
                " Unfortunately nothing good though. "
                " Man, you could've asked for some gossip from Petunia and Lizzy... "
                " ...Only if they weren't so torn apart right now. "
                " You can only hope that they'll get better soon. "
                play sound "audio/bellring.mp3"
                " After a bit of walking around, the bell rings. Time for music class. "
                " You walked into your classroom and you sat in your seat. "
                pause 2.0
                jump musicclass3

label wedgym4:
    # claire, riley // checking on claire, looking to see if Riley's doing alright
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked to the back of the gym and spotted two of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if claireknow == True and rileyknow == True:
        menu:
            " {image=claireicon} Claire {image=claireicon} ":
                jump whatthehelly
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump whatthefucky
    elif claireknow == True and rileyknow == False:
        menu:
            " {image=claireicon} Claire {image=claireicon} ":
                jump whatthehelly
            " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                jump whatthefucky
    elif claireknow == False and rileyknow == True:
        menu:
            " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                jump whatthehelly
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump whatthefucky
    else:
        menu:
            " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                jump whatthehelly
            " {image=rileyicon} An insane looking girl {image=rileyicon} ":
                jump whatthefucky
    label whatthehelly:
        " You decided to go and check if she was doing okay. "
        if clairebeatup == True:
            " ...Is what I would say if it's time. "
            " But right now, it's not. "
            " Off to the next class! "
            scene black
            pause 2.0
            jump musicclass3
        else:
            pass
        $ clairelv += 5
        show claireneutral at center with easeinleft
        if claireknow == True:
            " You greeted her and asked if she was doing alright now. "
            c " Oh, heya there [name]! "
            c " It's always a pleasure seeing you, hehe... "
            c " Anyway, about your question! "
            c " I'm doing alright now, thanks for asking. "
            hide claireneutral at bottom
            show clairehappy at center
            c " Engel actually gave me a really nice looking bracelet to cheer me up! "
            c " He also gave one to Bubble, so that we'd all be matching! "
            c " Now isn't that adorable? he's just the sweetest, ehhe.. "
            if clairelv >= 25 or clairelv == 25:
                hide clairehappy at bottom
                show claireneutral at center
                c " When I first looked at the bracelet and heard that he had made some for me and Bubble... "
                c " I couldn't help but ask if he made one for you. But, he didn't... "
                hide claireneutral at bottom
                show clairesad at center
                c " Which kind of bummed me out, since you're such a good friend... "
                hide clairesad at bottom
                show claireneutral at center
                c " So, I took some matters into my own hands, aaaannnd... "
                hide claireneutral at bottom
                show clairehappy at center
                " Claire opens up her hands, and turns out she had made a nice little bracelet just for you. "
                " This has to be the nicest thing someone's ever done for you in your entire life. "
                c " Weeell... what do you think? "
                c " This took me a bit of time to make, but I hope that you like it! "
                c " ... "
                " Claire waits for your opinion on her bracelet. "
                " What do you say? "
                menu:
                    " Thank you so muchhh!! it's really nice i love it :3 ":
                        $ clairelv += 10
                        hide clairehappy at bottom
                        show claireamazed at center
                        c " Wait, you really do? "
                        hide claireamazed at bottom
                        show clairehappy at center
                        c " I'm glad that you love it then! "
                        c " (It's so nice hearing someone appreciate my work...) "
                        c " Here, let me put it on for you... "
                        hide clairehappy at bottom
                        show claireneutral at center
                        " Claire gently takes your hand and she puts the bracelet nice on your wrist. "
                        " Pretty cool looking, in my opinion. "
                        " Probably would've freaked out about it positively if I was in your situation. "
                        c " It looks very good on you! "
                        c " I'm glad I picked the right clors, hehehe... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Claire. "
                        " You were definitely going to wear this bracelet every day now. "
                        " Not only that it looked good, but now you're also matching with Claire's friend group! And Claire herself. "
                        " Very sweet! "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for music class. "
                        " You get up and off of where you were sitting, and you walked back to your classroom. "
                        pause 2.0
                        jump musicclass3
                    " it's okay I guess ":
                        c " Glad that you like it, then! "
                        c " Here, let me put it on for you... "
                        hide clairehappy at bottom
                        show claireneutral at center
                        " Claire gently takes your hand and she puts the bracelet nice on your wrist. "
                        " Pretty cool looking, in my opinion. "
                        " Probably would've freaked out about it positively if I was in your situation. "
                        c " It looks very good on you! "
                        c " I'm glad I picked the right clors, hehehe... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Claire. "
                        " You were definitely going to wear this bracelet every day now. "
                        " Not only that it looked good, but now you're also matching with Claire's friend group! And Claire herself. "
                        " Very sweet! "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for music class. "
                        " You get up and off of where you were sitting, and you walked back to your classroom. "
                        pause 2.0
                        jump musicclass3
            elif clairelv <= 25:
                " Looks like Claire was supposed to say something here, but you don't have the right amount of affection points. "
                " Unfortunate, really... "
                pass
            else:
                " Looks like Claire was supposed to say something here, but you don't have the right amount of affection points. "
                " Unfortunate, really... "
                pass
            " Let's timeskip this thing then. "
            scene black with dissolve
            " You spent the rest of the break talking with Claire. "
            " You heard that one of her friends, Engel, was planning on making you a bracelet... "
            " But he didn't have enough materials to make you one. "
            " Not to worry, he said that he'll try to get some as soon as he can. "
            " What a nice guy... "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for music class. "
            " You get up and off of where you were sitting, and you walked back to your classroom. "
            pause 2.0
            jump musicclass3
        else:
            " You greeted her and asked if she was doing alright. "
            " You did hear about some whispers about how she looked like she was stressed out... "
            " A good classmate would want to know if the other was alright. "
            x " Oh, heya there [name]! "
            x " It's always a pleasure seeing you, hehe... "
            x " Wait, huh? I haven't even introduced myself to you, I'm so sorry... "
            $ claireknow = True
            c " I'm Claire! It's really nice to meet you!! "
            c " Anyway, about your question! "
            c " I'm doing alright, thanks for asking. "
            hide claireneutral at bottom
            show clairehappy at center
            c " Engel actually gave me a really nice looking bracelet to cheer me up! "
            c " He also gave one to Bubble, so that we'd all be matching! "
            c " Now isn't that adorable? he's just the sweetest, ehhe.. "
            if clairelv >= 25 or clairelv == 25:
                hide clairehappy at bottom
                show claireneutral at center
                c " When I first looked at the bracelet and heard that he had made some for me and Bubble... "
                c " I couldn't help but ask if he made one for you. But, he didn't... "
                hide claireneutral at bottom
                show clairesad at center
                c " Which kind of bummed me out, since you're such a good friend... "
                hide clairesad at bottom
                show claireneutral at center
                c " So, I took some matters into my own hands, aaaannnd... "
                hide claireneutral at bottom
                show clairehappy at center
                " Claire opens up her hands, and turns out she had made a nice little bracelet just for you. "
                " This has to be the nicest thing someone's ever done for you in your entire life. "
                c " Weeell... what do you think? "
                c " This took me a bit of time to make, but I hope that you like it! "
                c " ... "
                " Claire waits for your opinion on her bracelet. "
                " What do you say? "
                menu:
                    " Thank you so muchhh!! it's really nice i love it :3 ":
                        $ clairelv += 10
                        hide clairehappy at bottom
                        show claireamazed at center
                        c " Wait, you really do? "
                        hide claireamazed at bottom
                        show clairehappy at center
                        c " I'm glad that you love it then! "
                        c " (It's so nice hearing someone appreciate my work...) "
                        c " Here, let me put it on for you... "
                        hide clairehappy at bottom
                        show claireneutral at center
                        " Claire gently takes your hand and she puts the bracelet nice on your wrist. "
                        " Pretty cool looking, in my opinion. "
                        " Probably would've freaked out about it positively if I was in your situation. "
                        c " It looks very good on you! "
                        c " I'm glad I picked the right clors, hehehe... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Claire. "
                        " You were definitely going to wear this bracelet every day now. "
                        " Not only that it looked good, but now you're also matching with Claire's friend group! And Claire herself. "
                        " Very sweet! "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for music class. "
                        " You get up and off of where you were sitting, and you walked back to your classroom. "
                        pause 2.0
                        jump musicclass3
                    " it's okay I guess ":
                        c " Glad that you like it, then! "
                        c " Here, let me put it on for you... "
                        hide clairehappy at bottom
                        show claireneutral at center
                        " Claire gently takes your hand and she puts the bracelet nice on your wrist. "
                        " Pretty cool looking, in my opinion. "
                        " Probably would've freaked out about it positively if I was in your situation. "
                        c " It looks very good on you! "
                        c " I'm glad I picked the right clors, hehehe... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Claire. "
                        " You were definitely going to wear this bracelet every day now. "
                        " Not only that it looked good, but now you're also matching with Claire's friend group! And Claire herself. "
                        " Very sweet! "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for music class. "
                        " You get up and off of where you were sitting, and you walked back to your classroom. "
                        pause 2.0
                        jump musicclass3
            elif clairelv <= 25:
                " Looks like Claire was supposed to say something here, but you don't have the right amount of affection points. "
                " Unfortunate, really... "
                pass
            else:
                " Looks like Claire was supposed to say something here, but you don't have the right amount of affection points. "
                " Unfortunate, really... "
                pass
            " Let's timeskip this thing then. "
            scene black with dissolve
            " You spent the rest of the break talking with Claire. "
            " You heard that one of her friends, Engel, was planning on making you a bracelet... "
            " But he didn't have enough materials to make you one. "
            " Not to worry, he said that he'll try to get some as soon as he can. "
            " What a nice guy... "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for music class. "
            " You get up and off of where you were sitting, and you walked back to your classroom. "
            pause 2.0
            jump musicclass3
    label whatthefucky:
        " Let's see if her mental health is going good... "
        show rileyneutral at center with easeinright
        if rileyknow == True:
            hide rileyneutral at bottom
            show rileyhappy at center
            ri " Hihihiiii!! "
            ri " Sooooo... "
            hide rileyhappy at bottom
            show rileyneutral at center
            ri " I tried to make me and Oliver some pins so that we could match, right? "
            ri " He took them, and I like, freaked out about it!! "
            ri " Still freaking out about it, by the way. He never accepts anything I give him! "
            ri " He's so cute, aaaa!! "
            ri " But anyway, after a bit of walking around... "
            ri " I saw the pin that I gave him in the trash can. "
            ri " Of course I'm not sad about that or anything! "
            ri " That just means that I'm gonna have to try harder in finding something that he likes! "
            ri " I know that he's gonna accept me one day...One dayyy... "
            ri " And that day is coming SOON, BABY!! "
            ri " Like, hear me out on this idea that I just got in my head! "
            ri " What if I make a plushie of myself and give it to him? "
            ri " He's probably gonna rip it to shreds, but that's just gonna make it all the more better! "
            ri " He really likes ripping things, mind you, ahah. "
            ri " I mean, he did do something with a heart one day... "
            ri " Just showing it off to this random creepy girl. "
            ri " Surely nothing between those two! "
            ri " Besides, I did make it clear that he's mine and mine only, soooo... "
            ri " That girl better know to not try anything stupid! "
            hide rileyneutral at bottom
            show rileymurder at center
            ri " Otherwise I'm gonna have to do something about it, hehe. "
            ri " But I don't really have anything to worry about! "
            hide rileymurder at bottom
            show rileyneutral at center
            ri " I know Oliver's type! And I know that he's not into her! "
            ri " Becuase his type is ME!! "
            " ...Insane? Okay girl, whatever you say... "
            scene black with dissolve
            " Yep, her mental health still isn't the best. "
            " You've heard many things about Riley, but never knew that she would be this obssessed. "
            " Good heavens... reminds me of my younger days. "
            " Most definitely don't want to go back to that. Eugh. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, finally, a break from the yapping. "
            " You walked back to your classroom fore the next class. "
            pause 2.0
            jump musicclass3
        else:
            hide rileyneutral at bottom
            show rileyhappy at center
            ri " Hihihiiii!! "
            ri " Sooooo... "
            hide rileyhappy at bottom
            show rileyneutral at center
            ri " I tried to make me and Oliver some pins so that we could match, right? "
            ri " He took them, and I like, freaked out about it!! "
            ri " Still freaking out about it, by the way. He never accepts anything I give him! "
            ri " He's so cute, aaaa!! "
            ri " But anyway, after a bit of walking around... "
            ri " I saw the pin that I gave him in the trash can. "
            ri " Of course I'm not sad about that or anything! "
            ri " That just means that I'm gonna have to try harder in finding something that he likes! "
            ri " I know that he's gonna accept me one day...One dayyy... "
            ri " And that day is coming SOON, BABY!! "
            ri " Like, hear me out on this idea that I just got in my head! "
            ri " What if I make a plushie of myself and give it to him? "
            ri " He's probably gonna rip it to shreds, but that's just gonna make it all the more better! "
            ri " He really likes ripping things, mind you, ahah. "
            ri " I mean, he did do something with a heart one day... "
            ri " Just showing it off to this random creepy girl. "
            ri " Surely nothing between those two! "
            ri " Besides, I did make it clear that he's mine and mine only, soooo... "
            ri " That girl better know to not try anything stupid! "
            hide rileyneutral at bottom
            show rileymurder at center
            ri " Otherwise I'm gonna have to do something about it, hehe. "
            ri " But I don't really have anything to worry about! "
            hide rileymurder at bottom
            show rileyneutral at center
            ri " I know Oliver's type! And I know that he's not into her! "
            ri " Becuase his type is ME!! "
            " ...Insane? Okay girl, whatever you say... "
            scene black with dissolve
            " Yep, her mental health still isn't the best. "
            " You've heard many things about Riley, but never knew that she would be this obssessed. "
            " Good heavens... reminds me of my younger days. "
            " Most definitely don't want to go back to that. Eugh. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, finally, a break from the yapping. "
            " You walked back to your classroom fore the next class. "
            pause 2.0
            jump musicclass3

label wedcafeteria4:
    # lizzy, engel, abbie
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted three of your classmates doing their own things. "
    " Who should you talk to? "
    if popularknow,engelknow,abbieknow == True:
        menu:
            " {image=popularicon} Lizzy {image=popularicon} ":
                jump lizlizliz
            " {image=engelicon} Engel {image=engelicon} ":
                jump engengeng
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump ababab
    elif popularknow,engelknow == True and abbieknow == False:
        menu:
            " {image=popularicon} Lizzy {image=popularicon} ":
                jump lizlizliz
            " {image=engelicon} Engel {image=engelicon} ":
                jump engengeng
            " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                jump ababab
    elif popularknow,abbieknow == True and engelknow == False:
        menu:
            " {image=popularicon} Lizzy {image=popularicon} ":
                jump lizlizliz
            " {image=engelicon} A boy with feathers on his head {image=engelicon} ":
                jump engengeng
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump ababab
    elif engelknow,abbieknow == True and popularknow == False:
        menu:
            " {image=popularicon} A surprisingly lonely looking popular girl {image=popularicon} ":
                jump lizlizliz
            " {image=engelicon} Engel {image=engelicon} ":
                jump engengeng
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump ababab
    elif popularknow == True and engelknow,abbieknow == False:
        menu:
            " {image=popularicon} Lizzy {image=popularicon} ":
                jump lizlizliz
            " {image=engelicon} A boy with feathers on his head {image=engelicon} ":
                jump engengeng
            " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                jump ababab
    elif engelknow == True and popularknow,abbieknow == False:
        menu:
            " {image=popularicon} A surprisingly lonely looking girl {image=popularicon} ":
                jump lizlizliz
            " {image=engelicon} Engel {image=engelicon} ":
                jump engengeng
            " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                jump ababab
    elif abbieknow == True and popularknow,engelknow == False:
        menu:
            " {image=popularicon} A surprisingly lonely looking popular girl {image=popularicon} ":
                jump lizlizliz
            " {image=engelicon} A boy with feathers on his head {image=engelicon} ":
                jump engengeng
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump ababab
    else:
        menu:
            " {image=popularicon} A surprisingly lonely looking popular girl {image=popularicon} ":
                jump lizlizliz
            " {image=engelicon} A boy with feathers on his head {image=engelicon} ":
                jump engengeng
            " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                jump ababab
    label lizlizliz:
        # lizzy feels a bit lonely without petunia
        show lizzyneutral at center with easeinright
        if popularknow == True:
            lz " Ah, uh...hey [name]. "
            " You asked her if she's doing alright, since she looked so down. "
            " Wondering what happened for her to look this upset... "
            hide lizzyneutral at bottom
            show lizzysad at center
            lz " ...Well. "
            lz " It's something that I don't really want to tell you, but you're here, and I have no one else to talk to, so... "
            lz " ...I'll just tell you, at this point. "
            lz " It's Petunia. I don't feel too comfortable being with her right now, but... "
            lz " Without her being by my side, it kind of feels... "
            lz " Empty. Lonely, in a way. "
            lz " I guess I got too used to her loudness. "
            lz " I thought for sure that this could make me feel less bad, but... "
            lz " This is kind of making it worse. "
            lz " I mean, I did call her a lot of mean things last night... "
            lz " ...Not sure if she'd want to be around me right now. "
            lz " Maybe she's finding new people to talk to at this moment. "
            lz " Well, it's very likely at this point. "
            lz " I just hope that she comes back to talk with me soon. "
            lz " So that I can explain to her...about everything. "
            menu:
                " Let me hang out with you for a bit ":
                    $ popularlv += 10
                    hide lizzysad at bottom
                    show lizzyneutral at center
                    lz " ...Is this your attempt at making me feel less lonely? "
                    lz " Well, I can't really say no to you now, can I? "
                    lz " It's...nice to have someone to talk to. "
                    lz " Go ahead, talk to me about whatever you'd like. "
                    lz " I won't make fun of you for any embarrassing things you say. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Lizzy. "
                    " It was actually pretty nice to talk to her like this... "
                    " ...Though it did feel a little empty withot Petunia by her side. "
                    " You could always hear Petunia being loud whenever they were talking. "
                    " But, let's not focus on Petunia right now. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for the next class. "
                    " You get up from your seat and you walked back to the classroom for the next class. "
                    pause 2.0
                    jump musicclass3
                " Sorry I gotta do important stuff rn ":
                    hide lizzysad at bottom
                    show lizzyneutral at center
                    lz " That's fine. "
                    lz " Good luck on...whatever you're gonna do. "
                    " You then left Lizzy alone. "
                    " For some reason, she looked a little sad about you leaving... "
                    " Probably just your thoughts messing with you. "
                    scene black with dissolve
                    " You, for a fact, had nothing important to do whatsoever. "
                    " You just probably left because you had no idea how to deal with situations like Lizzy's having right now. "
                    " Or you really just didn't care. "
                    " Probably because you didn't care since you picked this option. "
                    " Anyway, you spent your time in the library to do some doomscrolling. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit of scrolling, time for music class then. "
                    " You get up from the chair you were sitting on in the library, and you walked to your classroom for the next class. "
                    pause 2.0
                    jump musicclass3
        else:
            lz " Ah, uh...hey [name]. "
            " You asked her if she's doing alright, since she looked so down. "
            " Wondering what happened for her to look this upset... "
            hide lizzyneutral at bottom
            show lizzysad at center
            lz " ...Well. "
            lz " It's something that I don't really want to tell you, but you're here, and I have no one else to talk to, so... "
            lz " ...I'll just tell you, at this point. "
            lz " It's Petunia. I don't feel too comfortable being with her right now, but... "
            lz " Without her being by my side, it kind of feels... "
            lz " Empty. Lonely, in a way. "
            lz " I guess I got too used to her loudness. "
            lz " I thought for sure that this could make me feel less bad, but... "
            lz " This is kind of making it worse. "
            lz " I mean, I did call her a lot of mean things last night... "
            lz " ...Not sure if she'd want to be around me right now. "
            lz " Maybe she's finding new people to talk to at this moment. "
            lz " Well, it's very likely at this point. "
            lz " I just hope that she comes back to talk with me soon. "
            lz " So that I can explain to her...about everything. "
            menu:
                " Let me hang out with you for a bit ":
                    $ popularlv += 10
                    hide lizzysad at bottom
                    show lizzyneutral at center
                    lz " ...Is this your attempt at making me feel less lonely? "
                    lz " Well, I can't really say no to you now, can I? "
                    lz " It's...nice to have someone to talk to. "
                    lz " Go ahead, talk to me about whatever you'd like. "
                    lz " I won't make fun of you for any embarrassing things you say. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Lizzy. "
                    " It was actually pretty nice to talk to her like this... "
                    " ...Though it did feel a little empty withot Petunia by her side. "
                    " You could always hear Petunia being loud whenever they were talking in the halls. Or anywhere, really. "
                    " But, let's not focus on Petunia right now. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for the next class. "
                    " You get up from your seat and you walked back to the classroom for the next class. "
                    pause 2.0
                    jump musicclass3
                " Sorry I gotta do important stuff rn ":
                    hide lizzysad at bottom
                    show lizzyneutral at center
                    lz " That's fine. "
                    lz " Good luck on...whatever you're gonna do. "
                    " You then left Lizzy alone. "
                    " For some reason, she looked a little sad about you leaving... "
                    " Probably just your thoughts messing with you. "
                    scene black with dissolve
                    " You, for a fact, had nothing important to do whatsoever. "
                    " You just probably left because you had no idea how to deal with situations like Lizzy's having right now. "
                    " Or you really just didn't care. "
                    " Probably because you didn't care since you picked this option. "
                    " Anyway, you spent your time in the library to do some doomscrolling. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit of scrolling, time for music class then. "
                    " You get up from the chair you were sitting on in the library, and you walked to your classroom for the next class. "
                    pause 2.0
                    jump musicclass3
    label engengeng:
        $ engellv += 5
        # engel talks about how claire's feeling better
        show engelneutral at center with easeinleft
        if engelknow == True:
            " You greeted him before asking him how he's doing. "
            hide engelneutral at bottom
            show engelhappy at center
            e " Hello, [name]! "
            e " I'm doing a lot better now that Claire's feeling happier. "
            e " You know, I made a bracelet for her. "
            e " Told her some comforting things, like how everything's gonna be alright... "
            e " And eventually, she felt better...! "
            e " I'm glad that I could cheer her up, I don't like it whenever I see her frown. "
            e " Oh, and I also made a bracelet for Bubble too! "
            e " Now me, Claire, and Bubble are matching! "
            if engellv >= 25 or engellv == 25:
                hide engelhappy at bottom
                show engelcontent at center
                e " And of course I didn't forget you, hehe... "
                e " How could I ever? You've been a really good friend, after all. "
                e " Here, let me just pull it out of my pocket... "
                " Engel pulls out a well made and cute bracelet from his pocket and gives it to you. "
                hide engelcontent at bottom
                show engelhappy at center
                e " Here, try it on. "
                e " I know that it's gonna look amazing on you! "
                e " Well, it's a small detail, but still. "
                " You put the well made bracelet on... "
                " It feels really nice! Also love the little details Engel put. "
                " There were also some dangling things that look like they were reflecting your personality. "
                if kind == True:
                    " Clovers! makes you feel lucky, and also makes you feel really nice, just like how you are. "
                elif calm == True:
                    " The moon - chill as the cold air in the night. Nice! "
                elif mean == True:
                    " Some fire emojis - either it means that Engel thinks you're hot or it's for your fiery personality. "
                    " Most likely the personality one though. "
                " Engel waits expectantly for your thoughts on the bracelet. "
                menu:
                    " It's great!! I love it so much!! ":
                        $ engellv += 10
                        hide engelhappy at bottom
                        show engelcontent at center
                        e " I'm really glad that you love it, then! "
                        e " Hehehe...I should start giving you gifts more often. "
                        " Is he really gonna spoil you with gifts? "
                        " Nice one. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Engel. "
                        " It was really nice talking with him...he was also thinking about stuff he could give you. "
                        " No matter how many times you said that you're fine without anything, he kept on insiting. "
                        " Nice fella, but you think he gives a lot too much. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit. Looks like it's time for music class. "
                        " You get up from where you were sitting, and you walked to your classroom for the next class. "
                        pause 2.0
                        jump musicclass3
                    " It's alright I guess ":
                        e " I'm glad you like it, then! "
                        scene black with dissolve
                        " You spent the rest of the break talking with Engel. "
                        " It was really nice talking with him...he was also thinking about stuff he could give you. "
                        " No matter how many times you said that you're fine without anything, he kept on insiting. "
                        " Nice fella, but you think he gives a lot too much. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit. Looks like it's time for music class. "
                        " You get up from where you were sitting, and you walked to your classroom for the next class. "
                        pause 2.0
                        jump musicclass3
            else:
                " Engel was supposed to be saying something here, but turns out you don't have enough affection points. "
                " Unfortunate... "
                " Well, let's skip this whole thing then. "
                scene black with dissolve
                " You spent the rest of the break talking with Engel. "
                " He told you that he WAS gonna make a bracelet for you, but he didn't have enough materials. "
                " He did reassure you that he was gonna get them as soon as he can, so...yippee! "
                " Wonder what the bracelet's gonna look like... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for music class. "
                " You get up from where you were sitting, and you walked to your classroom for the next class. "
                pause 2.0
                jump musicclass3
        else:
            " You greeted him before asking him how he's doing. "
            hide engelneutral at bottom
            show engelhappy at center
            x " Hello, [name]! "
            $ engelknow = True
            e " First things first - I'm Engel. I didn't get to introduce myself earlier cause I was busy... "
            e " And second, about your question... I'm doing a lot better now that Claire's feeling happier. "
            e " You know, I made a bracelet for her. "
            e " Told her some comforting things, like how everything's gonna be alright... "
            e " And eventually, she felt better...! "
            e " I'm glad that I could cheer her up, I don't like it whenever I see her frown. "
            e " Oh, and I also made a bracelet for Bubble too! "
            e " Now me, Claire, and Bubble are matching! "
            if engellv >= 25 or engellv == 25:
                hide engelhappy at bottom
                show engelcontent at center
                e " And of course I didn't forget you, hehe... "
                e " How could I ever? You've been a really good friend, after all. "
                e " Here, let me just pull it out of my pocket... "
                " Engel pulls out a well made and cute bracelet from his pocket and gives it to you. "
                hide engelcontent at bottom
                show engelhappy at center
                e " Here, try it on. "
                e " I know that it's gonna look amazing on you! "
                e " Well, it's a small detail, but still. "
                " You put the well made bracelet on... "
                " It feels really nice! Also love the little details Engel put. "
                " There were also some dangling things that look like they were reflecting your personality. "
                if kind == True:
                    " Clovers! makes you feel lucky, and also makes you feel really nice, just like how you are. "
                elif calm == True:
                    " The moon - chill as the cold air in the night. Nice! "
                elif mean == True:
                    " Some fire emojis - either it means that Engel thinks you're hot or it's for your fiery personality. "
                    " Most likely the personality one though. "
                " Engel waits expectantly for your thoughts on the bracelet. "
                menu:
                    " It's great!! I love it so much!! ":
                        $ engellv += 10
                        hide engelhappy at bottom
                        show engelcontent at center
                        e " I'm really glad that you love it, then! "
                        e " Hehehe...I should start giving you gifts more often. "
                        " Is he really gonna spoil you with gifts? "
                        " Nice one. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Engel. "
                        " It was really nice talking with him...he was also thinking about stuff he could give you. "
                        " No matter how many times you said that you're fine without anything, he kept on insiting. "
                        " Nice fella, but you think he gives a lot too much. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit. Looks like it's time for music class. "
                        " You get up from where you were sitting, and you walked to your classroom for the next class. "
                        pause 2.0
                        jump musicclass3
                    " It's alright I guess ":
                        e " I'm glad you like it, then! "
                        scene black with dissolve
                        " You spent the rest of the break talking with Engel. "
                        " It was really nice talking with him...he was also thinking about stuff he could give you. "
                        " No matter how many times you said that you're fine without anything, he kept on insiting. "
                        " Nice fella, but you think he gives a lot too much. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit. Looks like it's time for music class. "
                        " You get up from where you were sitting, and you walked to your classroom for the next class. "
                        pause 2.0
                        jump musicclass3
            else:
                " Engel was supposed to be saying something here, but turns out you don't have enough affection points. "
                " Unfortunate... "
                " Well, let's skip this whole thing then. "
                scene black with dissolve
                " You spent the rest of the break talking with Engel. "
                " He told you that he WAS gonna make a bracelet for you, but he didn't have enough materials. "
                " He did reassure you that he was gonna get them as soon as he can, so...yippee! "
                " Wonder what the bracelet's gonna look like... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Looks like it's time for music class. "
                " You get up from where you were sitting, and you walked to your classroom for the next class. "
                pause 2.0
                jump musicclass3
    label ababab:
        # abbie talks about this new movie he likes.
        show abbieneutral at center with easeinright
        if abbieknow == True:
            " You walked up to him and saw that he was watching some sort of movie on his phone. "
            " Making sure not to startle him, you asked him what he was watching. "
            a " Hmmm...? "
            hide abbieneutral at bottom
            show abbiehappy at center
            a " Oh, hi [name]... "
            a " I'm just watching this new movie that came out... "
            a " It's...about this girl band going up against...a boy band... "
            a " ...Seems normal, right...? "
            a " Well turns out...the boys in the boy band are demons... "
            a " ...And the girls have to slay them... "
            a " It's pretty good, in my opinion... "
            hide abbiehappy at bottom
            show abbieneutral at center
            a " Um, I hope I'm not gonna bother you, but... "
            a " Would you...maybe like to join me in watching...? "
            a " Ah - It's okay if you don't want to, though... "
            a " I'm not gonna force you or anything... "
            menu:
                " Let's watch!! ":
                    $ abbielv += 10
                    hide abbieneutral at bottom
                    show abbiehappy at center
                    a " Come sit next to me then... "
                    " You sat down next to him and he offered you one of his earphones so that you could hear properly. "
                    " The cafeteria WAS loud, so if you didn't have them on, then you'd probably hear nothing. "
                    " You put it on, and started watching with Abbie. "
                    " You recognized the movie from all of those youtube shorts you've seen about it. "
                    " You're feeling pretty glad that you're seeing the actual thing now. "
                    if abbielv >= 25 or abbielv == 25:
                        a " ...You know... "
                        a " It's really nice spending time with you like this... "
                        a " ...You make me feel safer in this school, in a way... "
                        hide abbiehappy at bottom
                        show abbieneutral at center
                        a " God, s-sorry...saying that was embarrassing... "
                        a " I should just be quiet now... "
                        menu:
                            " I like spending time with you too ":
                                $ abbielv += 10
                                a " ...R..really...? "
                                hide abbieneutral at bottom
                                show abbiehappy at center
                                a " I'm glad that you think that way, then... "
                                a " It makes me feel happy that you think that... "
                                scene black with dissolve
                                " You spent the rest of the break watching the movie with Abbie on his phone. "
                                " Abbie's phone screen looked a bit broken... "
                                " You're considering on getting him a new protection screen. "
                                " Maybe not right now since you're broke. "
                                play sound "audio/bellring.mp3"
                                " The bell rings after a bit, stopping your watch session with Abbie. "
                                " You get up from where you were sitting, and you walked to your classroom for the next class. "
                                pause 2.0
                                jump musicclass3
                            " *stay silent* ":
                                hide abbieneutral at bottom
                                show abbiesad at center
                                a " ... "
                                scene black with dissolve
                                " You spent the rest of the break watching the movie with Abbie on his phone. "
                                " Abbie's phone screen looked a bit broken... "
                                " You're considering on getting him a new protection screen. "
                                " Maybe not right now since you're broke. "
                                play sound "audio/bellring.mp3"
                                " The bell rings after a bit, stopping your watch session with Abbie. "
                                " You get up from where you were sitting, and you walked to your classroom for the next class. "
                                pause 2.0
                                jump musicclass3
                    else:
                        " Abbie was supposed to say something here, but you don't have enough affection points for that. "
                        " Unfortunate... "
                        scene black with dissolve
                        " You spent the rest of the break watching the movie with Abbie on his phone. "
                        " Abbie's phone screen looked a bit broken... "
                        " You're considering on getting him a new protection screen. "
                        " Maybe not right now since you're broke. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, stopping your watch session with Abbie. "
                        " You get up from where you were sitting, and you walked to your classroom for the next class. "
                        pause 2.0
                        jump musicclass3
                " Sorry I gotta go somewhere ":
                    a " Okayyy... "
                    a " Stay safeeee... "
                    scene black with dissolve
                    " You, for a fact, didn't have to go anywhere. "
                    " You just wanted an excuse to leave. "
                    " Let me just time skip because nothing interesting happened while you were out... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, and you walked to your classroom for your next class. "
                    pause 2.0
                    jump musicclass3
        else:
            " You walked up to him and saw that he was watching some sort of movie on his phone. "
            " Making sure not to startle him, you asked him what he was watching. "
            x " Hmmm...? "
            hide abbieneutral at bottom
            show abbiehappy at center
            x " Oh, hi [name]... "
            $ abbieknow = True
            a " I'm Abbie, by the way...it's nice to meet you... "
            a " I'm just watching this new movie that came out... "
            a " It's...about this girl band going up against...a boy band... "
            a " ...Seems normal, right...? "
            a " Well turns out...the boys in the boy band are demons... "
            a " ...And the girls have to slay them... "
            a " It's pretty good, in my opinion... "
            hide abbiehappy at bottom
            show abbieneutral at center
            a " Um, I hope I'm not gonna bother you, but... "
            a " Would you...maybe like to join me in watching...? "
            a " Ah - It's okay if you don't want to, though... "
            a " I'm not gonna force you or anything... "
            menu:
                " Let's watch!! ":
                    $ abbielv += 10
                    hide abbieneutral at bottom
                    show abbiehappy at center
                    a " Come sit next to me then... "
                    " You sat down next to him and he offered you one of his earphones so that you could hear properly. "
                    " The cafeteria WAS loud, so if you didn't have them on, then you'd probably hear nothing. "
                    " You put it on, and started watching with Abbie. "
                    " You recognized the movie from all of those youtube shorts you've seen about it. "
                    " You're feeling pretty glad that you're seeing the actual thing now. "
                    if abbielv >= 25 or abbielv == 25:
                        a " ...You know... "
                        a " It's really nice spending time with you like this... "
                        a " ...You make me feel safer in this school, in a way... "
                        hide abbiehappy at bottom
                        show abbieneutral at center
                        a " God, s-sorry...saying that was embarrassing... "
                        a " I should just be quiet now... "
                        menu:
                            " I like spending time with you too ":
                                $ abbielv += 10
                                a " ...R..really...? "
                                hide abbieneutral at bottom
                                show abbiehappy at center
                                a " I'm glad that you think that way, then... "
                                a " It makes me feel happy that you think that... "
                                scene black with dissolve
                                " You spent the rest of the break watching the movie with Abbie on his phone. "
                                " Abbie's phone screen looked a bit broken... "
                                " You're considering on getting him a new protection screen. "
                                " Maybe not right now since you're broke. "
                                play sound "audio/bellring.mp3"
                                " The bell rings after a bit, stopping your watch session with Abbie. "
                                " You get up from where you were sitting, and you walked to your classroom for the next class. "
                                pause 2.0
                                jump musicclass3
                            " *stay silent* ":
                                hide abbieneutral at bottom
                                show abbiesad at center
                                a " ... "
                                scene black with dissolve
                                " You spent the rest of the break watching the movie with Abbie on his phone. "
                                " Abbie's phone screen looked a bit broken... "
                                " You're considering on getting him a new protection screen. "
                                " Maybe not right now since you're broke. "
                                play sound "audio/bellring.mp3"
                                " The bell rings after a bit, stopping your watch session with Abbie. "
                                " You get up from where you were sitting, and you walked to your classroom for the next class. "
                                pause 2.0
                                jump musicclass3
                    else:
                        " Abbie was supposed to say something here, but you don't have enough affection points for that. "
                        " Unfortunate... "
                        scene black with dissolve
                        " You spent the rest of the break watching the movie with Abbie on his phone. "
                        " Abbie's phone screen looked a bit broken... "
                        " You're considering on getting him a new protection screen. "
                        " Maybe not right now since you're broke. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, stopping your watch session with Abbie. "
                        " You get up from where you were sitting, and you walked to your classroom for the next class. "
                        pause 2.0
                        jump musicclass3
                " Sorry I gotta go somewhere ":
                    a " Okayyy... "
                    a " Stay safeeee... "
                    scene black with dissolve
                    " You, for a fact, didn't have to go anywhere. "
                    " You just wanted an excuse to leave. "
                    " Let me just time skip because nothing interesting happened while you were out... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, and you walked to your classroom for your next class. "
                    pause 2.0
                    jump musicclass3

label wedrooftop4:
    # ruby, bubble
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked to the rooftop and spotted two of your classmates doing their own things. "
    " Who do you talk to for this break? "
    if rubyknow == True and bubbleknow == True:
        menu:
            " {image=rubyicon} Ruby {image=rubyicon} ":
                jump rubyrubyqueen
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump bubblebubblequeen
    elif rubyknow == True and bubbleknow == False:
        menu:
            " {image=rubyicon} Ruby {image=rubyicon} ":
                jump rubyrubyqueen
            " {image=bubbleicon} A girl made out of bubbles {image=bubbleicon} ":
                jump bubblebubblequeen
    elif rubyknow == False and bubbleknow == True:
        menu:
            " {image=rubyicon} A girl with a TV for a head {image=rubyicon} ":
                jump rubyrubyqueen
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump bubblebubblequeen
    else:
        menu:
            " {image=rubyicon} A girl with a TV for a head {image=rubyicon} ":
                jump rubyrubyqueen
            " {image=bubbleicon} A girl made out of bubbles {image=bubbleicon} ":
                jump bubblebubblequeen
    label rubyrubyqueen:
        " You walked up to her to see what she was up to. "
        show rubyneutral at center with easeinright
        if rubyknow == True:
            ru " Hi, [name]! "
            ru " You know, that one song from that new movie has been stuck in my head... "
            ru " I don't know if you've heard about the new movie, but it's pretty good! "
            ru " If you'd want to see it sometime, then you could watch it on my screen! "
            ru " We can't do it right now though, since this IS school. "
            ru " Anyway, about that song... "
            ru " It's been EVERYWHERE on my fyp! Literally cannot escape it! "
            ru " At first, I thought that the movie was kinda bad... "
            ru " ...But now I think it's pretty good! What a way to change my opinion! "
            ru " And that song...I still remember the popular lyrics... "
            hide rubyneutral at bottom
            show rubyhappy at center
            ru " You're all I can think of, every drop I drink up... "
            ru " ...You're my soda pop, my little soda pop! "
            ru " Hmhmhmhm...that song is way too catchy to be real! "
            hide rubyhappy at bottom
            show rubyneutral at center
            ru " What do you think, [name]? "
            menu:
                " It's really catchy! ":
                    $ rubylv += 10
                    hide rubyneutral at bottom
                    show rubyhappy at center
                    ru " I'm glad you think the same way! "
                    ru " I could listen to this song for hours, really... "
                    ru " And I have! Should that be concerning? "
                    ru " Well, while I was on sleep mode, I kind of forgot to pause the song... "
                    ru " And it played all throughout the night... "
                    hide rubyhappy at bottom
                    show rubyneutral at center
                    ru " Let's just say that this song is going to be on my 'most listened to' playlist for awhile. "
                    ru " Like, for awhile, awhile...I listened to that for 8 hours straight... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Ruby. "
                    " You have to admit, the song she mentioned DID sound a bit catchy... "
                    " You're gonna have to check it out later. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for music class. "
                    " You walked down from the rooftop and went to your classroom for the next class. "
                    pause 2.0
                    jump musicclass3
                " It's okay I guess ":
                    hide rubyneutral at bottom
                    show rubyhappy at center
                    ru " I'm glad you think that way! "
                    ru " I could listen to this song for hours, really... "
                    ru " And I have! Should that be concerning? "
                    ru " Well, while I was on sleep mode, I kind of forgot to pause the song... "
                    ru " And it played all throughout the night... "
                    hide rubyhappy at bottom
                    show rubyneutral at center
                    ru " Let's just say that this song is going to be on my 'most listened to' playlist for awhile. "
                    ru " Like, for awhile, awhile...I listened to that for 8 hours straight... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Ruby. "
                    " You have to admit, the song she mentioned DID sound a bit catchy... "
                    " You're gonna have to check it out later. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for music class. "
                    " You walked down from the rooftop and went to your classroom for the next class. "
                    pause 2.0
                    jump musicclass3
        else:
            x " Hi, [name]! "
            $ rubyknow = True
            ru " Oh right, ahem... "
            ru " I'm Ruby! I don't think I've got to introduce myself to you before, hehe... "
            ru " Anyway! "
            ru " You know, that one song from that new movie has been stuck in my head... "
            ru " I don't know if you've heard about the new movie, but it's pretty good! "
            ru " If you'd want to see it sometime, then you could watch it on my screen! "
            ru " We can't do it right now though, since this IS school. "
            ru " Anyway, about that song... "
            ru " It's been EVERYWHERE on my fyp! Literally cannot escape it! "
            ru " At first, I thought that the movie was kinda bad... "
            ru " ...But now I think it's pretty good! What a way to change my opinion! "
            ru " And that song...I still remember the popular lyrics... "
            hide rubyneutral at bottom
            show rubyhappy at center
            ru " You're all I can think of, every drop I drink up... "
            ru " ...You're my soda pop, my little soda pop! "
            ru " Hmhmhmhm...that song is way too catchy to be real! "
            hide rubyhappy at bottom
            show rubyneutral at center
            ru " What do you think, [name]? "
            menu:
                " It's really catchy! ":
                    $ rubylv += 10
                    hide rubyneutral at bottom
                    show rubyhappy at center
                    ru " I'm glad you think the same way! "
                    ru " I could listen to this song for hours, really... "
                    ru " And I have! Should that be concerning? "
                    ru " Well, while I was on sleep mode, I kind of forgot to pause the song... "
                    ru " And it played all throughout the night... "
                    hide rubyhappy at bottom
                    show rubyneutral at center
                    ru " Let's just say that this song is going to be on my 'most listened to' playlist for awhile. "
                    ru " Like, for awhile, awhile...I listened to that for 8 hours straight... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Ruby. "
                    " You have to admit, the song she mentioned DID sound a bit catchy... "
                    " You're gonna have to check it out later. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for music class. "
                    " You walked down from the rooftop and went to your classroom for the next class. "
                    pause 2.0
                    jump musicclass3
                " It's okay I guess ":
                    hide rubyneutral at bottom
                    show rubyhappy at center
                    ru " I'm glad you think that way! "
                    ru " I could listen to this song for hours, really... "
                    ru " And I have! Should that be concerning? "
                    ru " Well, while I was on sleep mode, I kind of forgot to pause the song... "
                    ru " And it played all throughout the night... "
                    hide rubyhappy at bottom
                    show rubyneutral at center
                    ru " Let's just say that this song is going to be on my 'most listened to' playlist for awhile. "
                    ru " Like, for awhile, awhile...I listened to that for 8 hours straight... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Ruby. "
                    " You have to admit, the song she mentioned DID sound a bit catchy... "
                    " You're gonna have to check it out later. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for music class. "
                    " You walked down from the rooftop and went to your classroom for the next class. "
                    pause 2.0
                    jump musicclass3
    label bubblebubblequeen:
        " You walked up to her to see what she was up to. "
        show bubbleneutral at center with easeinleft
        if bubbleknow == True:
            b " Hi [name]!! "
            b " How're you doing today? Doing fine? "
            b " Hope so! "
            b " You know, I did hear that Claire was feeling down today... "
            hide bubbleneutral at bottom
            show bubblehappy at center
            b " But now she's all better!! "
            b " Engel also made us these really pretty bracelets! "
            b " Look, mine even has a rubber duck on it! "
            b " Soooo cute... "
            if bubblelv >= 25 or bubblelv == 25:
                b " Oh, look!! "
                b " Engel also made one for you!! "
                b " He didn't know where you were, so he gave it to me incase he couldn't find you! "
                b " Let me put it on for you... "
                " Bubble gently grabs your hand and puts on the bracelet for you. "
                " The bracelet is well made, looks very nice on you. "
                " Even if it's a small detail, it looks very, very cool. "
                " You're definitely going to be keeping this one. "
                " This has to be the nicest thing someone has done for you in awhile. "
                hide bubblehappy at bottom
                show bubbleneutral at center
                b " Sooo, what do you think? "
                b " Engel wanted to know what you thought, of course! "
                b " Incase you didn't like it, he could make another one!...is what he said. "
                b " Gosh, he's too nice for his own good... "
                menu:
                    " I love it! ":
                        $ bubblelv += 10
                        hide bubblehappy at bottom
                        show bubbleamazed at center
                        b " Really?? You like it?? "
                        hide bubbleamazed at bottom
                        show bubblehappy at center
                        b " Yayyy!! I'm really glad that you liike it!! "
                        b " Now we're all matching bracelets!! "
                        b " Isn't that great?? "
                        b " Yipeee!! "
                        scene black with dissolve
                        " You spent the rest of the break talking with Bubble. "
                        " Nothing much to say here, really. "
                        " Sorry but I've run out of cool text to give you. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit of talking, looks like it's time for music class. "
                        " You walked down from the rooftop and then went to your classroom. "
                        pause 2.0
                        jump musicclass3
                    " I think it's alright ":
                        hide bubbleneutral at bottom
                        show bubblehappy at center
                        b " Yayyy!! I'm really glad that you liike it!! "
                        b " Now we're all matching bracelets!! "
                        b " Isn't that great?? "
                        b " Yipeee!! "
                        scene black with dissolve
                        " You spent the rest of the break talking with Bubble. "
                        " Nothing much to say here, really. "
                        " Sorry but I've run out of cool text to give you. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit of talking, looks like it's time for music class. "
                        " You walked down from the rooftop and then went to your classroom. "
                        pause 2.0
                        jump musicclass3
            else:
                " Looks like Bubble was supposed to say something here, but you don't have enough affection points. "
                " Unfortunate... "
                " Time for a timeskip! "
                scene black with dissolve
                " You spent the rest of the break talking with Bubble. "
                " Nothing much to say here, really. "
                " Sorry but I've run out of cool text to give you. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit of talking, looks like it's time for music class. "
                " You walked down from the rooftop and then went to your classroom. "
                pause 2.0
                jump musicclass3
        else:
            x " Hi [name]!! "
            $ bubbleknow = True
            b " I'm Bubble! It's super nice to meet you!! "
            b " How're you doing today? Doing fine? "
            b " Hope so! "
            b " You know, I did hear that Claire was feeling down today... "
            hide bubbleneutral at bottom
            show bubblehappy at center
            b " But now she's all better!! "
            b " Engel also made us these really pretty bracelets! "
            b " Look, mine even has a rubber duck on it! "
            b " Soooo cute... "
            if bubblelv >= 25 or bubblelv == 25:
                b " Oh, look!! "
                b " Engel also made one for you!! "
                b " He didn't know where you were, so he gave it to me incase he couldn't find you! "
                b " Let me put it on for you... "
                " Bubble gently grabs your hand and puts on the bracelet for you. "
                " The bracelet is well made, looks very nice on you. "
                " Even if it's a small detail, it looks very, very cool. "
                " You're definitely going to be keeping this one. "
                " This has to be the nicest thing someone has done for you in awhile. "
                hide bubblehappy at bottom
                show bubbleneutral at center
                b " Sooo, what do you think? "
                b " Engel wanted to know what you thought, of course! "
                b " Incase you didn't like it, he could make another one!...is what he said. "
                b " Gosh, he's too nice for his own good... "
                menu:
                    " I love it! ":
                        $ bubblelv += 10
                        hide bubblehappy at bottom
                        show bubbleamazed at center
                        b " Really?? You like it?? "
                        hide bubbleamazed at bottom
                        show bubblehappy at center
                        b " Yayyy!! I'm really glad that you liike it!! "
                        b " Now we're all matching bracelets!! "
                        b " Isn't that great?? "
                        b " Yipeee!! "
                        scene black with dissolve
                        " You spent the rest of the break talking with Bubble. "
                        " Nothing much to say here, really. "
                        " Sorry but I've run out of cool text to give you. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit of talking, looks like it's time for music class. "
                        " You walked down from the rooftop and then went to your classroom. "
                        pause 2.0
                        jump musicclass3
                    " I think it's alright ":
                        hide bubbleneutral at bottom
                        show bubblehappy at center
                        b " Yayyy!! I'm really glad that you liike it!! "
                        b " Now we're all matching bracelets!! "
                        b " Isn't that great?? "
                        b " Yipeee!! "
                        scene black with dissolve
                        " You spent the rest of the break talking with Bubble. "
                        " Nothing much to say here, really. "
                        " Sorry but I've run out of cool text to give you. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit of talking, looks like it's time for music class. "
                        " You walked down from the rooftop and then went to your classroom. "
                        pause 2.0
                        jump musicclass3
            else:
                " Looks like Bubble was supposed to say something here, but you don't have enough affection points. "
                " Unfortunate... "
                " Time for a timeskip! "
                scene black with dissolve
                " You spent the rest of the break talking with Bubble. "
                " Nothing much to say here, really. "
                " Sorry but I've run out of cool text to give you. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit of talking, looks like it's time for music class. "
                " You walked down from the rooftop and then went to your classroom. "
                pause 2.0
                jump musicclass3
label wedlibrary4:
    # cubbie + lana
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and spotted two of your classmates hanging out with eachother. "
    " Wondering what they're talking about, you walked over to them to see what's up. "
    show cubbieneutral at left with easeinright
    show lananeutral at right with easeinright
    if cubbieknow == True and lanaknow == True:
        cb " ..!! "
        l " Huh? What's that Cubbie? "
        l " [name]'s here? Oh yeah, hi [name]!! "
        " Cubbie is pleased to see you. "
        l " I'm just teaching Cubbie over here how to make sock puppets! "
        l " You wanna join? It's completely fine if you don't want to! "
        " Wow this interaction is shorter than most interactions. "
        " Bet the teacher route interactions are shorter though. "
        " Anyway, do you want to join Lana and Cubbie? "
        menu:
            " Of course!! ":
                $ lanalv += 10
                $ cubbielv += 10
                hide lananeutral at bottom
                hide cubbieneutral at bottom
                show lanahappy at right
                show cubbiehappy at left
                cb " ...!! "
                l " Yay!! Let's get to it then! "
                scene black with dissolve
                " You spent the rest of the break making sock puppets with Cubbie and Lana. "
                " It was actually pretty fun... "
                " You should probably do stuff like this sometime. "
                " If only you didn't have to deal with homework a lot. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You get up from where you were sitting with Lana and Cubbie, and you walked back to class. "
                pause 2.0
                jump musicclass3
            " I'd rather watch ":
                l " Oh, alright! "
                cb " ... "
                scene black with dissolve
                " You spent the rest of the break watching Lana and Cubbie make sock puppets. "
                " It did look pretty fun... "
                " You should probably try to do stuff like that sometime. "
                " If only you didn't have to deal with homework a lot. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You get up from where you were sitting with Lana and Cubbie, and you walked back to class. "
                pause 2.0
                jump musicclass3
    elif cubbieknow == True and lanaknow == False:
        cb " ..!! "
        x " Huh? What's that Cubbie? "
        x " [name]'s here? Oh yeah, hi [name]!! "
        " Cubbie is pleased to see you. "
        $ lanaknow = True
        l " Oh, I'm Lana by the way! "
        l " I'm just teaching Cubbie over here how to make sock puppets! "
        l " You wanna join? It's completely fine if you don't want to! "
        " Wow this interaction is shorter than most interactions. "
        " Bet the teacher route interactions are shorter though. "
        " Anyway, do you want to join Lana and Cubbie? "
        menu:
            " Of course!! ":
                $ lanalv += 10
                $ cubbielv += 10
                hide lananeutral at bottom
                hide cubbieneutral at bottom
                show lanahappy at right
                show cubbiehappy at left
                cb " ...!! "
                l " Yay!! Let's get to it then! "
                scene black with dissolve
                " You spent the rest of the break making sock puppets with Cubbie and Lana. "
                " It was actually pretty fun... "
                " You should probably do stuff like this sometime. "
                " If only you didn't have to deal with homework a lot. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You get up from where you were sitting with Lana and Cubbie, and you walked back to class. "
                pause 2.0
                jump musicclass3
            " I'd rather watch ":
                l " Oh, alright! "
                cb " ... "
                scene black with dissolve
                " You spent the rest of the break watching Lana and Cubbie make sock puppets. "
                " It did look pretty fun... "
                " You should probably try to do stuff like that sometime. "
                " If only you didn't have to deal with homework a lot. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You get up from where you were sitting with Lana and Cubbie, and you walked back to class. "
                pause 2.0
                jump musicclass3
    elif cubbieknow == False and lanaknow == True:
        x " ..!! "
        $ cubbieknow = True
        l " Huh? What's that Cubbie? "
        l " [name]'s here? Oh yeah, hi [name]!! "
        " Cubbie is pleased to see you. "
        l " I'm just teaching Cubbie over here how to make sock puppets! "
        l " You wanna join? It's completely fine if you don't want to! "
        " Wow this interaction is shorter than most interactions. "
        " Bet the teacher route interactions are shorter though. "
        " Anyway, do you want to join Lana and Cubbie? "
        menu:
            " Of course!! ":
                $ lanalv += 10
                $ cubbielv += 10
                hide lananeutral at bottom
                hide cubbieneutral at bottom
                show lanahappy at right
                show cubbiehappy at left
                cb " ...!! "
                l " Yay!! Let's get to it then! "
                scene black with dissolve
                " You spent the rest of the break making sock puppets with Cubbie and Lana. "
                " It was actually pretty fun... "
                " You should probably do stuff like this sometime. "
                " If only you didn't have to deal with homework a lot. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You get up from where you were sitting with Lana and Cubbie, and you walked back to class. "
                pause 2.0
                jump musicclass3
            " I'd rather watch ":
                l " Oh, alright! "
                cb " ... "
                scene black with dissolve
                " You spent the rest of the break watching Lana and Cubbie make sock puppets. "
                " It did look pretty fun... "
                " You should probably try to do stuff like that sometime. "
                " If only you didn't have to deal with homework a lot. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You get up from where you were sitting with Lana and Cubbie, and you walked back to class. "
                pause 2.0
                jump musicclass3
    else:
        x " ..!! "
        $ cubbieknow = True
        x " Huh? What's that Cubbie? "
        x " [name]'s here? Oh yeah, hi [name]!! "
        " Cubbie is pleased to see you. "
        $ lanaknow = True
        l " Oh, I'm Lana by the way! "
        l " I'm just teaching Cubbie over here how to make sock puppets! "
        l " You wanna join? It's completely fine if you don't want to! "
        " Wow this interaction is shorter than most interactions. "
        " Bet the teacher route interactions are shorter though. "
        " Anyway, do you want to join Lana and Cubbie? "
        menu:
            " Of course!! ":
                $ lanalv += 10
                $ cubbielv += 10
                hide lananeutral at bottom
                hide cubbieneutral at bottom
                show lanahappy at right
                show cubbiehappy at left
                cb " ...!! "
                l " Yay!! Let's get to it then! "
                scene black with dissolve
                " You spent the rest of the break making sock puppets with Cubbie and Lana. "
                " It was actually pretty fun... "
                " You should probably do stuff like this sometime. "
                " If only you didn't have to deal with homework a lot. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You get up from where you were sitting with Lana and Cubbie, and you walked back to class. "
                pause 2.0
                jump musicclass3
            " I'd rather watch ":
                l " Oh, alright! "
                cb " ... "
                scene black with dissolve
                " You spent the rest of the break watching Lana and Cubbie make sock puppets. "
                " It did look pretty fun... "
                " You should probably try to do stuff like that sometime. "
                " If only you didn't have to deal with homework a lot. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You get up from where you were sitting with Lana and Cubbie, and you walked back to class. "
                pause 2.0
                jump musicclass3

label wedoligang4:
    scene black with dissolve
    pause 2.0
    scene oligangclub with dissolve
    " You walked into the classroom to find that no one's there. "
    " You looked around and spotted a note on one of the tables... "
    " You picked it up and read it. It said: "
    " 'Hi there [name]!! you must be wondering where we are right now...' "
    " 'We just went out to get some icecream. Don't worry, we'll get ya some.' "
    " 'Though we don't really know what yur favorite flavor is, so we just guessed.' "
    " 'Wait for us to come back so we can all hang out!' - Oliver. "
    " ...And wait you shall. "
    " You sat down on one of the chairs, ready to start a few minutes of scrolling on your phone. "
    scene black with dissolve
    " You scrolled on your phone until Oliver and the gang arrived. "
    " They got you chocolate icecream... "
    " I mean, they didn't know what your favorite icecream flavor was so it's fine. "
    " Plus, nothing is wrong with a little chocolate. "
    " You then spent the rest of the break eating icecream and hanging out with the gang. "
    " For some ungodly reason Oliver decided to throw in a bar of soap in his icecream. "
    " Zip got strawberry icecream...Edward got chocolate mint icecream...and Oliver got cookies and cream icecream, with a dash of soap. "
    " Wait...is that a reference I smell? "
    " Oh god, not that song again. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for class to start. "
    " You guys talk with eachother for a bit, then eventually went off to go to class. "
    pause 2.0
    jump musicclass3

label musicclass3:
    scene classroom with dissolve
    " You walked into the classroom and got ready for the lesson today. "
    " Well, you heard that there was gonna be and activity today so you're gonna have to get prepared for that. "
    " You don't know what to expect for an activity in music... "
    " Probably some singing, which is kinda easy if you don't suck ass at it. "
    " The teacher eventually arrives and you prepare for anything he's going to say. "
    show mrdemineutral at center with easeinright
    msd " Alright class, we're going to be having an activity today, as you all know... "
    msd " ...We're going to be doing some singing. You can sing anything you want, just make sure that it isn't inappropriate. "
    msd " I'll be judging you guys and giving you points for how well you do...and, um...the max points should be 100...? "
    msd " (Is Miss Grace really sure about this?) "
    msd " (Can't really complain though, since she is the principal and everything...) "
    msd " Alright, I'll start with the guys at the back... "
    " ...Oh, singing. "
    " Honestly didn't really think it would be singing out of everything. The teachers probably ran out of ideas on what to do. "
    " You wait for it to be your turn patiently. "
    " You're probably gonna suck ass at this activity since you probably don't sing. "
    " Eventually, it's your turn to sing, so you stand up from your seat. "
    " You clear your throat and get ready to sing... "
    if kind == True:
        " You sang a happy and nice song. "
        " Your singing wasn't that bad, it was a bit good, actually. "
        hide mrdemineutral at bottom
        show mrdemihappy at center
        msd " ...Good job, [name]...! "
        msd " You'll be getting a good 78 points for that... "
        " Nice one! Atleast you didn't get a low grade. "
    elif calm == True:
        " You sang a chill song. "
        " Your voice wasn't the best, but atleast you were trying. "
        msd " Alrighty... "
        msd " You'll be getting a...55 for that one. "
    elif mean == True:
        " You were honestly embarrassed about this, but you sang a cutesy song. "
        hide mrdemineutral at bottom
        show mrdemisurprised at center
        " And HOLY SHIT your voice was good. "
        " Mister Demi looked so stunned, you hadto wait for 20 minutes before he gave you your grade. "
        msd " ...O-okay...this might be a little unfair but... "
        msd " ..100 points. The whole class can agree, that was good - right?????? "
        " You weren't expecting for your classmates to actually agree. "
        " Wow... "
    else:
        pass
    " As the teacher moved onto the other students, you fell asleep on your desk.. "
    scene black with dissolve
    " Take a nice nap, [name]. "
    pause 1.0
    play sound "audio/bellring.mp3"
    " Too bad naps only last for a bit. "
    " You got woken up to the loud sound of the bell ringing. "
    " You get off of your seat and you walked back into the hallways. "
    " Time for the final break of the day... "
    pause 2.0
    jump wedbreak5

label wedbreak5:
    scene hallway with dissolve
    if oligangjoin == True:
        jump wedoligang5
    else:
        pass
    " You're thinking about going somewhere for the last break of the day. "
    " Where do you go? "
    menu:
        " {image=rubyicon} The front of the school {image=abbieicon} ":
            jump wedfrontschool5
        " {image=cubbieicon} The back of the school {image=kevinicon} ":
            jump wedbackschool5
        " {image=robbyicon} The gym {image=bubbleicon} ":
            jump wedgym5
        " {image=rileyicon} The cafeteria {image=claireicon} ":
            jump wedcafeteria5
        " {image=engelicon} The rooftop {image=popularicon} ":
            jump wedrooftop5
        " {image=skellicon} The library {image=lanaicon} ":
            jump wedlibrary5

label wedfrontschool5:
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school and spotted your two classmates talking with eachother. "
    " Wondering what they're talking about, you decided to walk up to them and see how they're doing... "
    show abbieneutral at right with easeinleft
    show rubyneutral at left with easeinleft
    if abbieknow == True and rubyknow == True:
        ru " Hiya there, [name]! Hiya, Abbie! "
        ru " So, you guys know that one new movie that's been released? "
        a " mmm...yeah...? "
        a " Wait, you know about that movie? "
        ru " Yep! Loved it! "
        hide abbieneutral at bottom
        show abbiehappy at right
        a " No wayyy...same...!! "
        ru " I'm actually a bit surprised that you're into that movie, Abbie. "
        ru " But I guess that the movie's popularity really gets to everyone, eh? "
        a " Mhmmm... "
        ru " Actually, do you wanna listen to a song from that movie? "
        ru " I've got all music videos downloaded! "
        a " Oooh, can we do Silver...? "
        hide rubyneutral at bottom
        show rubyhappy at left
        ru " You like silver? Me too!! "
        ru " Of course we can!! "
        ru " Hey [name], do you wanna listen to the song with us? "
        ru " Completely fine if you don't want to! "
        ru " I don't want to force you or anything... "
        menu:
            " PLEASE PLEASE PLEASE PLEASE PLEA ":
                jump silverlmao
            " NONONONONONONONONONONONONONON ":
                jump silverlmao
        label silverlmao:
            $ rubylv += 5
            $ abbielv += 5
            " Whatever option you picked, I made you say yes just for the funny. "
            " What? You didn't want to listen? Well too bad, you're listening to it now. "
            ru " Alriiight then! I'll put on the song... "
            a " ...Yay...! "
            scene black with dissolve
            " You spent the rest of the break hanging out with Ruby and Abbie, "
            " Singing Silver and looking at the music video Ruby had on her screen... "
            " Infact, you got a little too into singing to the point that a few people were looking. "
            " A bit embarrassing. "
            " Abbie sang with you, and you've gotta admit, his singing voice is actually pretty cute. "
            " You need him to sing a whole cover of this. "
            play sound "audio/bellring.mp3"
            " The bell rings right after the song ends. "
            " You all then went back into the school and went to your final class. "
            pause 2.0
            jump artclass3
    elif abbieknow == True and rubyknow == False:
        x " Hiya there, [name]! Hiya, Abbie! "
        $ rubyknow = True
        x " Hey, wait...I don't think I've introduced myself to you before! "
        ru " I'm Ruby, it's really nice to meet you, [name]! "
        ru " So, you guys know that one new movie that's been released? "
        a " mmm...yeah...? "
        a " Wait, you know about that movie? "
        ru " Yep! Loved it! "
        hide abbieneutral at bottom
        show abbiehappy at right
        a " No wayyy...same...!! "
        ru " I'm actually a bit surprised that you're into that movie, Abbie. "
        ru " But I guess that the movie's popularity really gets to everyone, eh? "
        a " Mhmmm... "
        ru " Actually, do you wanna listen to a song from that movie? "
        ru " I've got all music videos downloaded! "
        a " Oooh, can we do Silver...? "
        hide rubyneutral at bottom
        show rubyhappy at left
        ru " You like silver? Me too!! "
        ru " Of course we can!! "
        ru " Hey [name], do you wanna listen to the song with us? "
        ru " Completely fine if you don't want to! "
        ru " I don't want to force you or anything... "
        menu:
            " PLEASE PLEASE PLEASE PLEASE PLEA ":
                jump silverlmao1
            " NONONONONONONONONONONONONONON ":
                jump silverlmao1
        label silverlmao1:
            $ rubylv += 5
            $ abbielv += 5
            " Whatever option you picked, I made you say yes just for the funny. "
            " What? You didn't want to listen? Well too bad, you're listening to it now. "
            ru " Alriiight then! I'll put on the song... "
            a " ...Yay...! "
            scene black with dissolve
            " You spent the rest of the break hanging out with Ruby and Abbie, "
            " Singing Silver and looking at the music video Ruby had on her screen... "
            " Infact, you got a little too into singing to the point that a few people were looking. "
            " A bit embarrassing. "
            " Abbie sang with you, and you've gotta admit, his singing voice is actually pretty cute. "
            " You need him to sing a whole cover of this. "
            play sound "audio/bellring.mp3"
            " The bell rings right after the song ends. "
            " You all then went back into the school and went to your final class. "
            pause 2.0
            jump artclass3
    elif abbieknow == False and rubyknow == True:
        $ abbieknow = True
        ru " Hiya there, [name]! Hiya, Abbie! "
        ru " So, you guys know that one new movie that's been released? "
        a " mmm...yeah...? "
        a " Wait, you know about that movie? "
        ru " Yep! Loved it! "
        hide abbieneutral at bottom
        show abbiehappy at right
        a " No wayyy...same...!! "
        ru " I'm actually a bit surprised that you're into that movie, Abbie. "
        ru " But I guess that the movie's popularity really gets to everyone, eh? "
        a " Mhmmm... "
        ru " Actually, do you wanna listen to a song from that movie? "
        ru " I've got all music videos downloaded! "
        a " Oooh, can we do Silver...? "
        hide rubyneutral at bottom
        show rubyhappy at left
        ru " You like silver? Me too!! "
        ru " Of course we can!! "
        ru " Hey [name], do you wanna listen to the song with us? "
        ru " Completely fine if you don't want to! "
        ru " I don't want to force you or anything... "
        menu:
            " PLEASE PLEASE PLEASE PLEASE PLEA ":
                jump silverlmao2
            " NONONONONONONONONONONONONONON ":
                jump silverlmao2
        label silverlmao2:
            $ rubylv += 5
            $ abbielv += 5
            " Whatever option you picked, I made you say yes just for the funny. "
            " What? You didn't want to listen? Well too bad, you're listening to it now. "
            ru " Alriiight then! I'll put on the song... "
            a " ...Yay...! "
            scene black with dissolve
            " You spent the rest of the break hanging out with Ruby and Abbie, "
            " Singing Silver and looking at the music video Ruby had on her screen... "
            " Infact, you got a little too into singing to the point that a few people were looking. "
            " A bit embarrassing. "
            " Abbie sang with you, and you've gotta admit, his singing voice is actually pretty cute. "
            " You need him to sing a whole cover of this. "
            play sound "audio/bellring.mp3"
            " The bell rings right after the song ends. "
            " You all then went back into the school and went to your final class. "
            pause 2.0
            jump artclass3
    else:
        $ abbieknow = True
        x " Hiya there, [name]! Hiya, Abbie! "
        $ rubyknow = True
        x " Hey, wait...I don't think I've introduced myself to you before! "
        ru " I'm Ruby, it's really nice to meet you, [name]! "
        ru " So, you guys know that one new movie that's been released? "
        a " mmm...yeah...? "
        a " Wait, you know about that movie? "
        ru " Yep! Loved it! "
        hide abbieneutral at bottom
        show abbiehappy at right
        a " No wayyy...same...!! "
        ru " I'm actually a bit surprised that you're into that movie, Abbie. "
        ru " But I guess that the movie's popularity really gets to everyone, eh? "
        a " Mhmmm... "
        ru " Actually, do you wanna listen to a song from that movie? "
        ru " I've got all music videos downloaded! "
        a " Oooh, can we do Silver...? "
        hide rubyneutral at bottom
        show rubyhappy at left
        ru " You like silver? Me too!! "
        ru " Of course we can!! "
        ru " Hey [name], do you wanna listen to the song with us? "
        ru " Completely fine if you don't want to! "
        ru " I don't want to force you or anything... "
        menu:
            " PLEASE PLEASE PLEASE PLEASE PLEA ":
                jump silverlmao3
            " NONONONONONONONONONONONONONON ":
                jump silverlmao3
        label silverlmao3:
            $ rubylv += 5
            $ abbielv += 5
            " Whatever option you picked, I made you say yes just for the funny. "
            " What? You didn't want to listen? Well too bad, you're listening to it now. "
            ru " Alriiight then! I'll put on the song... "
            a " ...Yay...! "
            scene black with dissolve
            " You spent the rest of the break hanging out with Ruby and Abbie, "
            " Singing Silver and looking at the music video Ruby had on her screen... "
            " Infact, you got a little too into singing to the point that a few people were looking. "
            " A bit embarrassing. "
            " Abbie sang with you, and you've gotta admit, his singing voice is actually pretty cute. "
            " You need him to sing a whole cover of this. "
            play sound "audio/bellring.mp3"
            " The bell rings right after the song ends. "
            " You all then went back into the school and went to your final class. "
            pause 2.0
            jump artclass3
label wedbackschool5:
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school, and spotted two of your classmates talking about something. "
    " Wondering what they were talking about, you decided to sit next to them on the ground and see what they were up to. "
    show kevinneutral at left with easeinright
    show cubbieneutral at right with easeinright
    if kevinknow == True and cubbieknow == True:
        kv " Hello there, [name]. "
        cb " ..!! "
        kv " Me and Cubbie here were just talking about who's the better vocaloid. "
        cb " ... "
        " Cubbie shows Kevin a picture of a woman with yellow hair. "
        " She has a yellow phone...wait, you recognize this girl. "
        " Isn't this Okito Nero? "
        kv " Cubbie, Nero isn't even a vocaloid. "
        kv " She's just a fanloid or something like that... "
        kv " ...Personally, I prefer Kosona Teta. "
        cb " ...??? "
        " Oh, that red haired girl. "
        " Isn't she owned by another company right now? "
        " Also techinically not a vocaloid. "
        hide kevinneutral at bottom
        show kevinconfused at left
        kv " She {i}is{/i} a vocaloid though! "
        kv " She got mentioned in one of the concerts with Zatsune Ziku! "
        kv " And she even got to step up on stage with her! "
        kv " Tell me that's NOT confirmation that she's a vocaloid. "
        cb " ... "
        hide kevinconfused at bottom
        show kevinneutral at left
        kv " Sigh...this is going nowhere. "
        kv " [name], who do YOU think is the better vocaloid? "
        menu:
            " Okito Nero ":
                $ cubbielv += 10
                hide cubbieneutral at bottom
                show cubbiehappy at right
                cb " !! "
                " Cubbie seems pleased that you picked her. "
                " How joyous! "
                kv " ...Alright, whatever floats your boat then. "
                kv " I still prefer Kosona Teta though. "
                kv " Now that I think about it though...Nero IS quite underrated. "
                kv " You have a valid choice there, Cubbie. And [name]. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Cubbie and Kevin. "
                " Talking about Okito Nero... "
                " She's pretty chill. You like that about her. "
                " Not only that, but she's the most underrated out of her trio with Kosona Teta and Zatsune Ziku. "
                " The other two may have good voices, yes, but you'll always like Okito Nero. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You walked back inside the school and you walked to your classroom for the next class. "
                pause 2.0
                jump artclass3
            " Kosona Teta ":
                $ kevinlv += 10
                hide kevinneutral at bottom
                show kevinhappy at left
                kv " Aha, see! "
                kv " Kosona Teta really IS superior. "
                kv " Though, I don't really mind you liking Okito Nero. "
                kv " People have their own opinions, of course! "
                hide cubbieneutral at bottom
                show cubbiehappy at right
                cb " ...!! "
                scene black with dissolve
                " You spent the rest of the break talking with Cubbie and Kevin about Kosona Teta. "
                " Did you know? she was actually supposed to be an april fools character but ended up becoming famous. "
                " Now isn't that interesting... "
                " You always liked something about her personality. And her love for bread. "
                " You thought it was pretty cute. "
                " For a fact, she's kind of now rising in popularity, getting a tad bit more popular than Zatsune. "
                " But in the end, we all know Zatsune's popularity can't be topped. "
                " You're forever loving Kosona Teta though. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You walked back inside the school and you walked to your classroom for the next class. "
                pause 2.0
                jump artclass3
            " Defoko ":
                " I'm surprised that you remember this one. "
                hide kevinneutral at bottom
                show kevinconfused at left
                " Looks like they're surprised as well. "
                kv " Defoko...? Jeez, I haven't heard of that name in a long time. "
                kv " I'm honestly surprised that you even remember her. "
                cb " ...??? "
                hide kevinconfused at bottom
                show kevinneutral at left
                kv " Cubbie, Defoko is the default voice for the software Kosona Teta was made in. "
                kv " People don't really recognize her nowadays and it's honestly..quite sad. "
                kv " I can honestly see why you'd like her, [name]. "
                kv " From what I remember, her design was...pretty cute. "
                kv " She also doesn't get that much talk online compared to the others. "
                kv " I mean, sure, there's other neglected vocaloids, but what about her? "
                kv " Hrm... "
                scene black with dissolve
                " You spent the rest of the break talking to Kevin and Cubbie about Defoko. "
                " I'm REALLY surprised that you remembered this one. "
                " Or, you actually had a different favorite voicebank/vocaloid but didn't have another option. "
                " If the creator added more, then this conversation would be way longer. "
                " And that would've added more suffering for the creator. "
                " Wouldn't want that to happen, jeez... "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You walked back inside the school and you walked to your classroom for the next class. "
                pause 2.0
                jump artclass3
    elif kevinknow == True and cubbieknow == False:
        kv " Hello there, [name]. "
        x " ..!! "
        $ cubbieknow = True
        kv " Me and Cubbie here were just talking about who's the better vocaloid. "
        " ...Huh, so that's that kid's name. "
        cb " ... "
        " Cubbie shows Kevin a picture of a woman with yellow hair. "
        " She has a yellow phone...wait, you recognize this girl. "
        " Isn't this Okito Nero? "
        kv " Cubbie, Nero isn't even a vocaloid. "
        kv " She's just a fanloid or something like that... "
        kv " ...Personally, I prefer Kosona Teta. "
        cb " ...??? "
        " Oh, that red haired girl. "
        " Isn't she owned by another company right now? "
        " Also techinically not a vocaloid. "
        hide kevinneutral at bottom
        show kevinconfused at left
        kv " She {i}is{/i} a vocaloid though! "
        kv " She got mentioned in one of the concerts with Zatsune Ziku! "
        kv " And she even got to step up on stage with her! "
        kv " Tell me that's NOT confirmation that she's a vocaloid. "
        cb " ... "
        hide kevinconfused at bottom
        show kevinneutral at left
        kv " Sigh...this is going nowhere. "
        kv " [name], who do YOU think is the better vocaloid? "
        menu:
            " Okito Nero ":
                $ cubbielv += 10
                hide cubbieneutral at bottom
                show cubbiehappy at right
                cb " !! "
                " Cubbie seems pleased that you picked her. "
                " How joyous! "
                kv " ...Alright, whatever floats your boat then. "
                kv " I still prefer Kosona Teta though. "
                kv " Now that I think about it though...Nero IS quite underrated. "
                kv " You have a valid choice there, Cubbie. And [name]. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Cubbie and Kevin. "
                " Talking about Okito Nero... "
                " She's pretty chill. You like that about her. "
                " Not only that, but she's the most underrated out of her trio with Kosona Teta and Zatsune Ziku. "
                " The other two may have good voices, yes, but you'll always like Okito Nero. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You walked back inside the school and you walked to your classroom for the next class. "
                pause 2.0
                jump artclass3
            " Kosona Teta ":
                $ kevinlv += 10
                hide kevinneutral at bottom
                show kevinhappy at left
                kv " Aha, see! "
                kv " Kosona Teta really IS superior. "
                kv " Though, I don't really mind you liking Okito Nero. "
                kv " People have their own opinions, of course! "
                hide cubbieneutral at bottom
                show cubbiehappy at right
                cb " ...!! "
                scene black with dissolve
                " You spent the rest of the break talking with Cubbie and Kevin about Kosona Teta. "
                " Did you know? she was actually supposed to be an april fools character but ended up becoming famous. "
                " Now isn't that interesting... "
                " You always liked something about her personality. And her love for bread. "
                " You thought it was pretty cute. "
                " For a fact, she's kind of now rising in popularity, getting a tad bit more popular than Zatsune. "
                " But in the end, we all know Zatsune's popularity can't be topped. "
                " You're forever loving Kosona Teta though. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You walked back inside the school and you walked to your classroom for the next class. "
                pause 2.0
                jump artclass3
            " Defoko ":
                " I'm surprised that you remember this one. "
                hide kevinneutral at bottom
                show kevinconfused at left
                " Looks like they're surprised as well. "
                kv " Defoko...? Jeez, I haven't heard of that name in a long time. "
                kv " I'm honestly surprised that you even remember her. "
                cb " ...??? "
                hide kevinconfused at bottom
                show kevinneutral at left
                kv " Cubbie, Defoko is the default voice for the software Kosona Teta was made in. "
                kv " People don't really recognize her nowadays and it's honestly..quite sad. "
                kv " I can honestly see why you'd like her, [name]. "
                kv " From what I remember, her design was...pretty cute. "
                kv " She also doesn't get that much talk online compared to the others. "
                kv " I mean, sure, there's other neglected vocaloids, but what about her? "
                kv " Hrm... "
                scene black with dissolve
                " You spent the rest of the break talking to Kevin and Cubbie about Defoko. "
                " I'm REALLY surprised that you remembered this one. "
                " Or, you actually had a different favorite voicebank/vocaloid but didn't have another option. "
                " If the creator added more, then this conversation would be way longer. "
                " And that would've added more suffering for the creator. "
                " Wouldn't want that to happen, jeez... "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You walked back inside the school and you walked to your classroom for the next class. "
                pause 2.0
                jump artclass3
    elif kevinknow == False and cubbieknow == True:
        x " Hello there, [name]. "
        cb " ..!! "
        x " Oh wait, I'm afraid I haven't introduced myself to you yet. "
        $ kevinknow = True
        kv " I'm Kevin, it's really nice to finally speak with you. "
        kv " Me and my friend Cubbie here were just talking about who's the better vocaloid. "
        cb " ... "
        " Cubbie shows Kevin a picture of a woman with yellow hair. "
        " She has a yellow phone...wait, you recognize this girl. "
        " Isn't this Okito Nero? "
        kv " Cubbie, Nero isn't even a vocaloid. "
        kv " She's just a fanloid or something like that... "
        kv " ...Personally, I prefer Kosona Teta. "
        cb " ...??? "
        " Oh, that red haired girl. "
        " Isn't she owned by another company right now? "
        " Also techinically not a vocaloid. "
        hide kevinneutral at bottom
        show kevinconfused at left
        kv " She {i}is{/i} a vocaloid though! "
        kv " She got mentioned in one of the concerts with Zatsune Ziku! "
        kv " And she even got to step up on stage with her! "
        kv " Tell me that's NOT confirmation that she's a vocaloid. "
        cb " ... "
        hide kevinconfused at bottom
        show kevinneutral at left
        kv " Sigh...this is going nowhere. "
        kv " [name], who do YOU think is the better vocaloid? "
        menu:
            " Okito Nero ":
                $ cubbielv += 10
                hide cubbieneutral at bottom
                show cubbiehappy at right
                cb " !! "
                " Cubbie seems pleased that you picked her. "
                " How joyous! "
                kv " ...Alright, whatever floats your boat then. "
                kv " I still prefer Kosona Teta though. "
                kv " Now that I think about it though...Nero IS quite underrated. "
                kv " You have a valid choice there, Cubbie. And [name]. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Cubbie and Kevin. "
                " Talking about Okito Nero... "
                " She's pretty chill. You like that about her. "
                " Not only that, but she's the most underrated out of her trio with Kosona Teta and Zatsune Ziku. "
                " The other two may have good voices, yes, but you'll always like Okito Nero. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You walked back inside the school and you walked to your classroom for the next class. "
                pause 2.0
                jump artclass3
            " Kosona Teta ":
                $ kevinlv += 10
                hide kevinneutral at bottom
                show kevinhappy at left
                kv " Aha, see! "
                kv " Kosona Teta really IS superior. "
                kv " Though, I don't really mind you liking Okito Nero. "
                kv " People have their own opinions, of course! "
                hide cubbieneutral at bottom
                show cubbiehappy at right
                cb " ...!! "
                scene black with dissolve
                " You spent the rest of the break talking with Cubbie and Kevin about Kosona Teta. "
                " Did you know? she was actually supposed to be an april fools character but ended up becoming famous. "
                " Now isn't that interesting... "
                " You always liked something about her personality. And her love for bread. "
                " You thought it was pretty cute. "
                " For a fact, she's kind of now rising in popularity, getting a tad bit more popular than Zatsune. "
                " But in the end, we all know Zatsune's popularity can't be topped. "
                " You're forever loving Kosona Teta though. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You walked back inside the school and you walked to your classroom for the next class. "
                pause 2.0
                jump artclass3
            " Defoko ":
                " I'm surprised that you remember this one. "
                hide kevinneutral at bottom
                show kevinconfused at left
                " Looks like they're surprised as well. "
                kv " Defoko...? Jeez, I haven't heard of that name in a long time. "
                kv " I'm honestly surprised that you even remember her. "
                cb " ...??? "
                hide kevinconfused at bottom
                show kevinneutral at left
                kv " Cubbie, Defoko is the default voice for the software Kosona Teta was made in. "
                kv " People don't really recognize her nowadays and it's honestly..quite sad. "
                kv " I can honestly see why you'd like her, [name]. "
                kv " From what I remember, her design was...pretty cute. "
                kv " She also doesn't get that much talk online compared to the others. "
                kv " I mean, sure, there's other neglected vocaloids, but what about her? "
                kv " Hrm... "
                scene black with dissolve
                " You spent the rest of the break talking to Kevin and Cubbie about Defoko. "
                " I'm REALLY surprised that you remembered this one. "
                " Or, you actually had a different favorite voicebank/vocaloid but didn't have another option. "
                " If the creator added more, then this conversation would be way longer. "
                " And that would've added more suffering for the creator. "
                " Wouldn't want that to happen, jeez... "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You walked back inside the school and you walked to your classroom for the next class. "
                pause 2.0
                jump artclass3
    else:
        x " Hello there, [name]. "
        x " ..!! "
        x " Oh wait, I'm afraid I haven't introduced myself to you yet. "
        $ kevinknow = True
        kv " I'm Kevin, it's really nice to finally speak with you. "
        $ cubbieknow = True
        kv " Me and my friend Cubbie here were just talking about who's the better vocaloid. "
        cb " ... "
        " Cubbie shows Kevin a picture of a woman with yellow hair. "
        " She has a yellow phone...wait, you recognize this girl. "
        " Isn't this Okito Nero? "
        kv " Cubbie, Nero isn't even a vocaloid. "
        kv " She's just a fanloid or something like that... "
        kv " ...Personally, I prefer Kosona Teta. "
        cb " ...??? "
        " Oh, that red haired girl. "
        " Isn't she owned by another company right now? "
        " Also techinically not a vocaloid. "
        hide kevinneutral at bottom
        show kevinconfused at left
        kv " She {i}is{/i} a vocaloid though! "
        kv " She got mentioned in one of the concerts with Zatsune Ziku! "
        kv " And she even got to step up on stage with her! "
        kv " Tell me that's NOT confirmation that she's a vocaloid. "
        cb " ... "
        hide kevinconfused at bottom
        show kevinneutral at left
        kv " Sigh...this is going nowhere. "
        kv " [name], who do YOU think is the better vocaloid? "
        menu:
            " Okito Nero ":
                $ cubbielv += 10
                hide cubbieneutral at bottom
                show cubbiehappy at right
                cb " !! "
                " Cubbie seems pleased that you picked her. "
                " How joyous! "
                kv " ...Alright, whatever floats your boat then. "
                kv " I still prefer Kosona Teta though. "
                kv " Now that I think about it though...Nero IS quite underrated. "
                kv " You have a valid choice there, Cubbie. And [name]. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Cubbie and Kevin. "
                " Talking about Okito Nero... "
                " She's pretty chill. You like that about her. "
                " Not only that, but she's the most underrated out of her trio with Kosona Teta and Zatsune Ziku. "
                " The other two may have good voices, yes, but you'll always like Okito Nero. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You walked back inside the school and you walked to your classroom for the next class. "
                pause 2.0
                jump artclass3
            " Kosona Teta ":
                $ kevinlv += 10
                hide kevinneutral at bottom
                show kevinhappy at left
                kv " Aha, see! "
                kv " Kosona Teta really IS superior. "
                kv " Though, I don't really mind you liking Okito Nero. "
                kv " People have their own opinions, of course! "
                hide cubbieneutral at bottom
                show cubbiehappy at right
                cb " ...!! "
                scene black with dissolve
                " You spent the rest of the break talking with Cubbie and Kevin about Kosona Teta. "
                " Did you know? she was actually supposed to be an april fools character but ended up becoming famous. "
                " Now isn't that interesting... "
                " You always liked something about her personality. And her love for bread. "
                " You thought it was pretty cute. "
                " For a fact, she's kind of now rising in popularity, getting a tad bit more popular than Zatsune. "
                " But in the end, we all know Zatsune's popularity can't be topped. "
                " You're forever loving Kosona Teta though. "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You walked back inside the school and you walked to your classroom for the next class. "
                pause 2.0
                jump artclass3
            " Defoko ":
                " I'm surprised that you remember this one. "
                hide kevinneutral at bottom
                show kevinconfused at left
                " Looks like they're surprised as well. "
                kv " Defoko...? Jeez, I haven't heard of that name in a long time. "
                kv " I'm honestly surprised that you even remember her. "
                cb " ...??? "
                hide kevinconfused at bottom
                show kevinneutral at left
                kv " Cubbie, Defoko is the default voice for the software Kosona Teta was made in. "
                kv " People don't really recognize her nowadays and it's honestly..quite sad. "
                kv " I can honestly see why you'd like her, [name]. "
                kv " From what I remember, her design was...pretty cute. "
                kv " She also doesn't get that much talk online compared to the others. "
                kv " I mean, sure, there's other neglected vocaloids, but what about her? "
                kv " Hrm... "
                scene black with dissolve
                " You spent the rest of the break talking to Kevin and Cubbie about Defoko. "
                " I'm REALLY surprised that you remembered this one. "
                " Or, you actually had a different favorite voicebank/vocaloid but didn't have another option. "
                " If the creator added more, then this conversation would be way longer. "
                " And that would've added more suffering for the creator. "
                " Wouldn't want that to happen, jeez... "
                play sound "audio/bellring.mp3"
                " The bell rings. Looks like it's time for your final class of the day. "
                " You walked back inside the school and you walked to your classroom for the next class. "
                pause 2.0
                jump artclass3
label wedgym5:
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym and spotted two of your classmates doing their own things. "
    " Who do you talk to? "
    if robbyknow == True and bubbleknow == True:
        menu:
            " {image=robbyicon} Robby {image=robbyicon} ":
                jump takedown
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump sodapopsaja
    elif robbyknow == True and bubbleknow == False:
        menu:
            " {image=robbyicon} Robby {image=robbyicon} ":
                jump takedown
            " {image=bubbleicon} A girl made up of bubbles {image=bubbleicon} ":
                jump sodapopsaja
    elif robbyknow == False and bubbleknow == True:
        menu:
            " {image=robbyicon} A guy with a propeller hat {image=robbyicon} ":
                jump takedown
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump sodapopsaja
    else:
        menu:
            " {image=robbyicon} A guy with a propeller hat {image=robbyicon} ":
                jump takedown
            " {image=bubbleicon} A girl made up of bubbles {image=bubbleicon} ":
                jump sodapopsaja
    label takedown:
        show robbyneutral at center with easeinright
        if robbyknow == True:
            " You walked over only to see him fixing something on the bleachers. "
            " Well, not something ON the bleachers, but the bleachers itself. "
            " You hope you're not bothering him as you ask him what he was fixing over there. "
            rb " Huh? Oh, it's you. "
            rb " As for what I'm fixing? I don't think you'd want to know. "
            rb " It's gonna be like those long ranting sessions Riley would throw at everyone in this school... "
            hide robbyneutral at bottom
            show robbyhappy at center
            rb " Except mine is just about how absurd some things are built in this school. "
            rb " Trust me, you wouldn't believe how many things I've had to fix in this school. "
            rb " You'd be pretty surprised at how many there are... "
            hide robbyhappy at bottom
            show robbyneutral at center
            rb " ...But really, if you don't want to hear me ranting about things like these, it's best to just go. "
            rb " Not gonna force you to stay here or whatever, but... "
            rb " ...If you actually want to hear me talk, then I don't mind. "
            rb " Most people don't want to hear me talk since I look like a nerd to most. "
            rb " Probably gonna think that I'm gonna yap about something like math... "
            rb " I'll probably do that though. "
            rb " But, uh...yeah. Don't want to hear me talk? You can leave. "
            " Do you want to listen to Robby talk? "
            menu:
                " Yap to me, boy ":
                    $ robbrileylv += 10
                    rb " ...Hold on, what? "
                    rb " You jest, surely???? "
                    rb " There's no way you'd want to listen to someone like me. "
                    rb " Talking about screws, scraps, bolts and what not... "
                    rb " ...But, if ya really want to, then... "
                    rb " Here, take a good look at this. "
                    " Robby moves a little bit so that you could see what he was trying to fix. "
                    " You look closer and it seems like he was fixing a screw that wasn't put in properly. "
                    " Huh. You wonder who got hired to do this. "
                    " No, wondering how they got even HIRED to have a job like this and fumble it. "
                    rb " This irritates me a whole lot. "
                    rb " You see, I kinda noticed this because I happened to sit down and it just felt...weird. "
                    rb " Looked around, checked the screws and eventually found this. "
                    rb " Is it okay for me to do this? probably not, since this is school property. "
                    rb " Am I going to do it again if this breaks again? yes. "
                    rb " Us students deserve the best, after all. And also the teachers if they ever sit on these things. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Robby about the bleachers. "
                    " Surpisingly you actually managed to get yourself interested in what he was talking about. "
                    " Didn't think that you'd be the type to listen to HIM out of all people, but you do you. "
                    " I won't judge or anything. "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Robby reassures you that he can speedrun fixing this. "
                    " You DID spend the time talking with him instead of letting him fix it. "
                    " You walked to your classroom for the final class of the day. "
                    pause 2.0
                    jump artclass3
                " I'd rather have my ears closed ":
                    rb " Good choice, or whatever. "
                    rb " I'll see you in class then. "
                    scene black with dissolve
                    " You walked out of the gym and walked around in the hallways for the rest of the break. "
                    " That's right, your legs are finally getting some exercise in them. "
                    " Well, this is what basically happens whenever you skip something like this. "
                    " You get work to do because the programmer doesn't know what to put here. "
                    " How fun and exciting, right? "
                    play sound "audio/bellring.mp3"
                    " You stop walking when the bell rang. Time for art class. "
                    " You then continued walking so that you could get to your last class of the day. "
                    pause 2.0
                    jump artclass3
        else:
            " You walked over only to see him fixing something on the bleachers. "
            " Well, not something ON the bleachers, but the bleachers itself. "
            " You hope you're not bothering him as you ask him what he was fixing over there. "
            x " Huh? Oh, it's you. "
            $ robbyknow = True
            rb " Don't think I introduced myself before, but uh...I'm Robby. "
            rb " As for what I'm fixing? I don't think you'd want to know. "
            rb " It's gonna be like those long ranting sessions Riley would throw at everyone in this school... "
            hide robbyneutral at bottom
            show robbyhappy at center
            rb " Except mine is just about how absurd some things are built in this school. "
            rb " Trust me, you wouldn't believe how many things I've had to fix in this school. "
            rb " You'd be pretty surprised at how many there are... "
            hide robbyhappy at bottom
            show robbyneutral at center
            rb " ...But really, if you don't want to hear me ranting about things like these, it's best to just go. "
            rb " Not gonna force you to stay here or whatever, but... "
            rb " ...If you actually want to hear me talk, then I don't mind. "
            rb " Most people don't want to hear me talk since I look like a nerd to most. "
            rb " Probably gonna think that I'm gonna yap about something like math... "
            rb " I'll probably do that though. "
            rb " But, uh...yeah. Don't want to hear me talk? You can leave. "
            " Do you want to listen to Robby talk? "
            menu:
                " Yap to me, boy ":
                    $ robbrileylv += 10
                    rb " ...Hold on, what? "
                    rb " You jest, surely???? "
                    rb " There's no way you'd want to listen to someone like me. "
                    rb " Talking about screws, scraps, bolts and what not... "
                    rb " ...But, if ya really want to, then... "
                    rb " Here, take a good look at this. "
                    " Robby moves a little bit so that you could see what he was trying to fix. "
                    " You look closer and it seems like he was fixing a screw that wasn't put in properly. "
                    " Huh. You wonder who got hired to do this. "
                    " No, wondering how they got even HIRED to have a job like this and fumble it. "
                    rb " This irritates me a whole lot. "
                    rb " You see, I kinda noticed this because I happened to sit down and it just felt...weird. "
                    rb " Looked around, checked the screws and eventually found this. "
                    rb " Is it okay for me to do this? probably not, since this is school property. "
                    rb " Am I going to do it again if this breaks again? yes. "
                    rb " Us students deserve the best, after all. And also the teachers if they ever sit on these things. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Robby about the bleachers. "
                    " Surpisingly you actually managed to get yourself interested in what he was talking about. "
                    " Didn't think that you'd be the type to listen to HIM out of all people, but you do you. "
                    " I won't judge or anything. "
                    play sound "audio/bellring.mp3"
                    " The bell rings. Robby reassures you that he can speedrun fixing this. "
                    " You DID spend the time talking with him instead of letting him fix it. "
                    " You walked to your classroom for the final class of the day. "
                    pause 2.0
                    jump artclass3
                " I'd rather have my ears closed ":
                    rb " Good choice, or whatever. "
                    rb " I'll see you in class then. "
                    scene black with dissolve
                    " You walked out of the gym and walked around in the hallways for the rest of the break. "
                    " That's right, your legs are finally getting some exercise in them. "
                    " Well, this is what basically happens whenever you skip something like this. "
                    " You get work to do because the programmer doesn't know what to put here. "
                    " How fun and exciting, right? "
                    play sound "audio/bellring.mp3"
                    " You stop walking when the bell rang. Time for art class. "
                    " You then continued walking so that you could get to your last class of the day. "
                    pause 2.0
                    jump artclass3
    label sodapopsaja:
        show bubbleneutral at center with easeinleft
        if bubbleknow == True:
            b " Hi there, [name]! "
            b " Hope you're feeling good as always today. "
            b " You know, I heard that Petunia and Lizzy aren't doing so well with eachother... "
            b " They haven't been talking to eachother for the past few hours or so! "
            hide bubbleneutral at bottom
            show bubblesad at center
            b " That's really concerning, considering the fact that they're always together... "
            b " I wonder what happened to them... "
            hide bubblesad at bottom
            show bubbleneutral at center
            b " ...But then again, it's not my thing to just go up to them and ask what's up. "
            b " I mean - how would YOU feel if someone you don't know just walks up to you and ask if you're alright? "
            b " To be honest, I'd be a little weirded out. "
            b " I'm pretty sure Lizzy and Petunia don't pay attention to who's in their class. "
            b " That's why I think they'd be weirded out if I just asked them! "
            b " I know that I should be a good student and ask them if they're doing alright buuuut...you knooow... "
            b " Just wanna give them some space for now. "
            hide bubbleneutral at bottom
            show bubblehappy at center
            b " Besides, I'm sure they're probably gonna be friends again tomorrow! "
            b " They're kind of the type to argue and then be friends again. Trust me! "
            hide bubblehappy at bottom
            show bubbleneutral at center
            b " I'd know....I've seen their arguments before. "
            b " One time Petunia argued with Lizzy all because she didn't defend her on a tiktok post. "
            b " Insane, right? "
            b " That's just how they are, hehe! "
            scene black with dissolve
            " You spent the rest of the break hanging out with Bubble. "
            " Huh...you wonder what happened to Lizzy and Petunia. "
            " They're probably going to be fine though, like Bubble said. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your final class. "
            " You walked out of the gym and went to your classroom a few moments after the bell rang. "
            pause 2.0
            jump artclass3
        else:
            x " Hi there, [name]! "
            x " Hope you're feeling good as always today. "
            x " Wait, I don't think I've introduced myself to you before! Silly me! "
            $ bubbleknow = True
            b " I'm Bubble! It's really nice to meet you! "
            b " You know, I heard that Petunia and Lizzy aren't doing so well with eachother... "
            b " They haven't been talking to eachother for the past few hours or so! "
            hide bubbleneutral at bottom
            show bubblesad at center
            b " That's really concerning, considering the fact that they're always together... "
            b " I wonder what happened to them... "
            hide bubblesad at bottom
            show bubbleneutral at center
            b " ...But then again, it's not my thing to just go up to them and ask what's up. "
            b " I mean - how would YOU feel if someone you don't know just walks up to you and ask if you're alright? "
            b " To be honest, I'd be a little weirded out. "
            b " I'm pretty sure Lizzy and Petunia don't pay attention to who's in their class. "
            b " That's why I think they'd be weirded out if I just asked them! "
            b " I know that I should be a good student and ask them if they're doing alright buuuut...you knooow... "
            b " Just wanna give them some space for now. "
            hide bubbleneutral at bottom
            show bubblehappy at center
            b " Besides, I'm sure they're probably gonna be friends again tomorrow! "
            b " They're kind of the type to argue and then be friends again. Trust me! "
            hide bubblehappy at bottom
            show bubbleneutral at center
            b " I'd know....I've seen their arguments before. "
            b " One time Petunia argued with Lizzy all because she didn't defend her on a tiktok post. "
            b " Insane, right? "
            b " That's just how they are, hehe! "
            scene black with dissolve
            " You spent the rest of the break hanging out with Bubble. "
            " Huh...you wonder what happened to Lizzy and Petunia. "
            " They're probably going to be fine though, like Bubble said. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your final class. "
            " You walked out of the gym and went to your classroom a few moments after the bell rang. "
            pause 2.0
            jump artclass3
label wedcafeteria5:
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted two of your classmates talking to eachother. "
    " Wondering what they were talking about, you decided to sit next to them and listen into their conversation. "
    " And also be apart of the conversation, of course. "
    show claireneutral at right with easeinleft
    show rileyneutral at left with easeinleft
    if clairebeatup == True:
        " Oh, hold on there. It's her. "
        " Try again tomorrow. "
        " Why can't you talk to Claire? well... "
        " Let's just say HE won't allow it. "
        " I know I'm being mysterious here but it's for your own good. "
        scene black
        pause 2.0
        jump artclass3
    else:
        pass
    if claireknow == True and rileyknow == True:
        c " You know, this is really great, Riley... "
        c " ...But I really should get back to studying! "
        c " Don't want to get some low grades in class now... "
        ri " Huuuh? study about what? "
        ri " Oh, right! I need to study too! "
        c " Hold on, really? "
        c " What subject are you studying for then, Riley?{nw} "
        hide rileyneutral at bottom
        show rileyhappy at left
        ri " Need to study about how perfect Oliver is! "
        c " ...Ah. Of course you'd say that... "
        c " I think you already know a lot about him being perfect, no? "
        c " I mean, you quite literally know every single detail about him. "
        c " What else is there to study? "
        hide rileyhappy at bottom
        show rileyneutral at left
        ri " Well, for example! "
        ri " I need to study what Oliver did for today! "
        ri " Then that's going to lead to what I'm gonna give him to get his attention on me! "
        ri " A gift, in short. "
        ri " Soooo, he got a cold shower today, as per usual... "
        hide claireneutral at bottom
        show claireconfused at right
        c " ...How do you know that he had a cold shower? "
        ri " A girl has her secrets! "
        ri " He also ate eggs and bacon for today... "
        c " ...Okay now this is just getting weird. "
        " She continues to talk to the other girl about Oliver. "
        " Looks like it's bothering the other girl that's trying to study... "
        " You should probably do something. "
        " But then again, you didn't feel like doing something. "
        " The other girl eventually whispers to you the moment the girl yapping is distracted. "
        hide claireconfused at bottom
        show claireneutral at right
        c " (Psst, [name]!) "
        c " (I don't wanna be rude, but I really don't want to listen to Riley talking...) "
        c " (I need to keep studying, you know?) "
        c " (Could you listen to her talking? Please?) "
        " You had nothing else to do, so you agreed. "
        hide claireneutral at bottom
        show clairehappy at right
        c " (Thanks!) "
        c " (I'll get you something next time!) "
        hide clairehappy at bottom
        show claireneutral at right
        ri " ...Anyway! What was I talking about? "
        ri " Oh hey [name]! Didn't know that you were here! "
        ri " I was just talking to Claire about how perfect my dear Oliver is! "
        ri " He's so cute, I just love him so much! "
        scene black with dissolve
        " You spent the rest of the break listening to Riley yap for Claire. "
        " You can see why Claire wouldn't want to listen to Riley. "
        " But, you couldn't really back out now, you DID agree with this... "
        " What good choices you make! "
        play sound "audio/bellring.mp3"
        " The bell rings, saving your ears from all of the talking. "
        " You got up from where you were sitting, and you walked to your classroom for your last class. "
        pause 2.0
        jump artclass3
    elif claireknow == True and rileyknow == False:
        c " You know, this is really great, Riley... "
        c " ...But I really should get back to studying! "
        c " Don't want to get some low grades in class now... "
        x " Huuuh? study about what? "
        x " Oh, right! I need to study too! "
        c " Hold on, really? "
        c " What subject are you studying for then, Riley?{nw} "
        hide rileyneutral at bottom
        show rileyhappy at left
        x " Need to study about how perfect Oliver is! "
        c " ...Ah. Of course you'd say that... "
        c " I think you already know a lot about him being perfect, no? "
        c " I mean, you quite literally know every single detail about him. "
        c " What else is there to study? "
        hide rileyhappy at bottom
        show rileyneutral at left
        x " Well, for example! "
        x " I need to study what Oliver did for today! "
        x " Then that's going to lead to what I'm gonna give him to get his attention on me! "
        x " A gift, in short. "
        x " Soooo, he got a cold shower today, as per usual... "
        hide claireneutral at bottom
        show claireconfused at right
        c " ...How do you know that he had a cold shower? "
        x " A girl has her secrets! "
        x " He also ate eggs and bacon for today... "
        c " ...Okay now this is just getting weird. "
        " She continues to talk to the other girl about Oliver. "
        " Looks like it's bothering the other girl that's trying to study... "
        " You should probably do something. "
        " But then again, you didn't feel like doing something. "
        " The other girl eventually whispers to you the moment the girl yapping is distracted. "
        hide claireconfused at bottom
        show claireneutral at right
        c " (Psst, [name]!) "
        $ rileyknow = True
        c " (I'm sure you haven't met her before, but her name's Riley!) "
        c " (And I don't wanna be rude, but I really don't want to listen to Riley talking...) "
        c " (I need to keep studying, you know?) "
        c " (Could you listen to her talking? Please?) "
        " You had nothing else to do, so you agreed. "
        hide claireneutral at bottom
        show clairehappy at right
        c " (Thanks!) "
        c " (I'll get you something next time!) "
        hide clairehappy at bottom
        show claireneutral at right
        ri " ...Anyway! What was I talking about? "
        ri " Oh hey [name]! Didn't know that you were here! "
        ri " I was just talking to Claire about how perfect my dear Oliver is! "
        ri " He's so cute, I just love him so much! "
        scene black with dissolve
        " You spent the rest of the break listening to Riley yap for Claire. "
        " You can see why Claire wouldn't want to listen to Riley. "
        " But, you couldn't really back out now, you DID agree with this... "
        " What good choices you make! "
        play sound "audio/bellring.mp3"
        " The bell rings, saving your ears from all of the talking. "
        " You got up from where you were sitting, and you walked to your classroom for your last class. "
        pause 2.0
        jump artclass3
    elif claireknow == False and rileyknow == True:
        x " You know, this is really great, Riley... "
        x " ...But I really should get back to studying! "
        x " Don't want to get some low grades in class now... "
        ri " Huuuh? study about what? "
        ri " Oh, right! I need to study too! "
        x " Hold on, really? "
        x " What subject are you studying for then, Riley?{nw} "
        hide rileyneutral at bottom
        show rileyhappy at left
        ri " Need to study about how perfect Oliver is! "
        x " ...Ah. Of course you'd say that... "
        x " I think you already know a lot about him being perfect, no? "
        x " I mean, you quite literally know every single detail about him. "
        x " What else is there to study? "
        hide rileyhappy at bottom
        show rileyneutral at left
        ri " Well, for example! "
        ri " I need to study what Oliver did for today! "
        ri " Then that's going to lead to what I'm gonna give him to get his attention on me! "
        ri " A gift, in short. "
        ri " Soooo, he got a cold shower today, as per usual... "
        hide claireneutral at bottom
        show claireconfused at right
        x " ...How do you know that he had a cold shower? "
        ri " A girl has her secrets! "
        ri " He also ate eggs and bacon for today... "
        x " ...Okay now this is just getting weird. "
        " She continues to talk to the other girl about Oliver. "
        " Looks like it's bothering the other girl that's trying to study... "
        " You should probably do something. "
        " But then again, you didn't feel like doing something. "
        " The other girl eventually whispers to you the moment the girl yapping is distracted. "
        hide claireconfused at bottom
        show claireneutral at right
        x " (Psst, [name]!) "
        $ claireknow = True
        x " (Ah, I haven't introduced myself yet...I'm Claire! Real nice to meet you.) "
        c " (I don't wanna be rude, but I really don't want to listen to Riley talking...) "
        c " (I need to keep studying, you know?) "
        c " (Could you listen to her talking? Please?) "
        " You had nothing else to do, so you agreed. "
        hide claireneutral at bottom
        show clairehappy at right
        c " (Thanks!) "
        c " (I'll get you something next time!) "
        hide clairehappy at bottom
        show claireneutral at right
        ri " ...Anyway! What was I talking about? "
        ri " Oh hey [name]! Didn't know that you were here! "
        ri " I was just talking to Claire about how perfect my dear Oliver is! "
        ri " He's so cute, I just love him so much! "
        scene black with dissolve
        " You spent the rest of the break listening to Riley yap for Claire. "
        " You can see why Claire wouldn't want to listen to Riley. "
        " But, you couldn't really back out now, you DID agree with this... "
        " What good choices you make! "
        play sound "audio/bellring.mp3"
        " The bell rings, saving your ears from all of the talking. "
        " You got up from where you were sitting, and you walked to your classroom for your last class. "
        pause 2.0
        jump artclass3
    else:
        x " You know, this is really great, Riley... "
        x " ...But I really should get back to studying! "
        x " Don't want to get some low grades in class now... "
        x " Huuuh? study about what? "
        x " Oh, right! I need to study too! "
        x " Hold on, really? "
        x " What subject are you studying for then, Riley?{nw} "
        hide rileyneutral at bottom
        show rileyhappy at left
        x " Need to study about how perfect Oliver is! "
        x " ...Ah. Of course you'd say that... "
        x " I think you already know a lot about him being perfect, no? "
        x " I mean, you quite literally know every single detail about him. "
        x " What else is there to study? "
        hide rileyhappy at bottom
        show rileyneutral at left
        x " Well, for example! "
        x " I need to study what Oliver did for today! "
        x " Then that's going to lead to what I'm gonna give him to get his attention on me! "
        x " A gift, in short. "
        x " Soooo, he got a cold shower today, as per usual... "
        hide claireneutral at bottom
        show claireconfused at right
        x " ...How do you know that he had a cold shower? "
        x " A girl has her secrets! "
        x " He also ate eggs and bacon for today... "
        x " ...Okay now this is just getting weird. "
        " She continues to talk to the other girl about Oliver. "
        " Looks like it's bothering the other girl that's trying to study... "
        " You should probably do something. "
        " But then again, you didn't feel like doing something. "
        " The other girl eventually whispers to you the moment the girl yapping is distracted. "
        hide claireconfused at bottom
        show claireneutral at right
        x " (Psst, [name]!) "
        $ claireknow = True
        x " (Ah, I haven't introduced myself yet...I'm Claire! Real nice to meet you.) "
        $ rileyknow = True
        c " (I'm sure you haven't met her before, but her name's Riley!) "
        c " (And I don't wanna be rude, but I really don't want to listen to Riley talking...) "
        c " (I need to keep studying, you know?) "
        c " (Could you listen to her talking? Please?) "
        " You had nothing else to do, so you agreed. "
        hide claireneutral at bottom
        show clairehappy at right
        c " (Thanks!) "
        c " (I'll get you something next time!) "
        hide clairehappy at bottom
        show claireneutral at right
        ri " ...Anyway! What was I talking about? "
        ri " Oh hey [name]! Didn't know that you were here! "
        ri " I was just talking to Claire about how perfect my dear Oliver is! "
        ri " He's so cute, I just love him so much! "
        scene black with dissolve
        " You spent the rest of the break listening to Riley yap for Claire. "
        " You can see why Claire wouldn't want to listen to Riley. "
        " But, you couldn't really back out now, you DID agree with this... "
        " What good choices you make! "
        play sound "audio/bellring.mp3"
        " The bell rings, saving your ears from all of the talking. "
        " You got up from where you were sitting, and you walked to your classroom for your last class. "
        pause 2.0
        jump artclass3
label wedrooftop5:
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked to the rooftop and spotted two of your classmates talking to eachother. "
    " Hey wait, isn't that one of the popular girls? let's see what's going on. "
    show engelneutral at left with easeinright
    show petunianeutral at right with easeinright
    if engelknow == True and popularknow == True:
        p " Come on, Engel! I know you're smart! "
        p " Just tell me what I have to do, and you're all good! "
        p " You want anything? Money? Just tell me! "
        e " Petunia, I don't want anything... "
        e " And I'm sorry to tell you this, but you should really just talk it out. "
        e " If you want the best, then that's the best advice I could give. "
        e " If you'll excuse me now... I'd like to get studying. "
        hide petunianeutral at bottom
        show petuniasad at right
        hide engelneutral at left with easeoutright
        show petuniasad at center with move
        " Who do you stay with? "
        menu:
            " Petunia ":
                $ popularlv += 5
                " You were about to ask her if she was alright, but she stopped you. "
                p " Don't bother worrying about me. "
                p " I'm gonna be fine without her by my side, anyway. "
                hide petuniasad at bottom
                show petuniahappy at center
                p " Just needa her to get outta my account, haha!... "
                hide petuniahappy at bottom
                show petuniasad at center
                p " Ha...ha. "
                p " ... "
                p " I'm going home early. "
                p " If they look for me, just tell them my parents had something important to do with me. "
                p " Okay? I trust you. "
                " Petunia gets on her phone and calls her parents. "
                " You didn't stay for long, and walked down stairs... "
                " You didn't want to disturb Petunia anymore anyway. "
                scene black with dissolve
                " You spent the rest of the break walking around in the hallways. "
                " You were wondering if Petunia really was gonna be okay... "
                " You could only hope that she was gonna be. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your final class. "
                " You walked to your classroom after a bit. "
                pause 2.0
                jump artclass3
            " Engel ":
                $ engellv += 5
                hide petuniasad at right with easeoutright
                show engelneutral at center with easeinleft
                e " Oh, uh...hey there [name]. "
                e " I wasn't actually expecting you to be here... "
                e " ...You were listening to the conversation me and Petunia had, didn't you? "
                e " She's been...asking what to do with her and Lizzy's situation to a lot of people. "
                e " including me. She was staring at me a lot last class... "
                e " I can really hope that they're gonna be okay in the end... "
                e " Seeing friendships break kinda make me sad a little. "
                e " ...But, getting away from that topic... "
                e " Want to study with me for now? "
                " You had nothing else to do, so you agreed. "
                hide engelneutral at bottom
                show engelhappy at center
                e " Excellent. I'll hand you my notes. "
                scene black with dissolve
                " You spent the rest of the break studying with Engel. "
                " As you were studying, you were praying that Petunia and Lizzy were going to be okay. "
                " Just hoping and praying... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Time for art class. "
                " You get down from the rooftop and walked to your classroom. "
                pause 2.0
                jump artclass3
            " I'd rather stay with myself ":
                hide petuniasad at right with easeoutright
                " You decided to leave the both of them alone. "
                " This was not your business anyway. "
                " You sat down at the corner of the rooftop, pulled out your phone... "
                " ...And started listening to some music you had. "
                " Making up some imaginary scenarios in your head as you chillaxed there. "
                scene black with dissolve
                " You spent the rest of the break chilling out on the rooftop. "
                " As you chillaxed, you saw Petunia on a call with someone. "
                " Of course she was still sad, and you highly doubt that she's talking to Lizzy or whoever the hell she was talking about. "
                " She DOES refuse to talk to her and all that... "
                " You focused more on your imaginary scenarios in your head though. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Time for art class. "
                " You get down from the rooftop and walked to your classroom. "
                pause 2.0
                jump artclass3
    elif engelknow == True and popularknow == False:
        x " Come on, Engel! I know you're smart! "
        x " Just tell me what I have to do, and you're all good! "
        x " You want anything? Money? Just tell me! "
        $ popularknow = True
        e " Petunia, I don't want anything... "
        e " And I'm sorry to tell you this, but you should really just talk it out. "
        e " If you want the best, then that's the best advice I could give. "
        e " If you'll excuse me now... I'd like to get studying. "
        hide petunianeutral at bottom
        show petuniasad at right
        hide engelneutral at left with easeoutright
        show petuniasad at center with move
        " Who do you stay with? "
        menu:
            " Petunia ":
                $ popularlv += 5
                " You were about to ask her if she was alright, but she stopped you. "
                p " Don't bother worrying about me. "
                p " I'm gonna be fine without her by my side, anyway. "
                hide petuniasad at bottom
                show petuniahappy at center
                p " Just needa her to get outta my account, haha!... "
                hide petuniahappy at bottom
                show petuniasad at center
                p " Ha...ha. "
                p " ... "
                p " I'm going home early. "
                p " If they look for me, just tell them my parents had something important to do with me. "
                p " Okay? I trust you. "
                " Petunia gets on her phone and calls her parents. "
                " You didn't stay for long, and walked down stairs... "
                " You didn't want to disturb Petunia anymore anyway. "
                scene black with dissolve
                " You spent the rest of the break walking around in the hallways. "
                " You were wondering if Petunia really was gonna be okay... "
                " You could only hope that she was gonna be. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your final class. "
                " You walked to your classroom after a bit. "
                pause 2.0
                jump artclass3
            " Engel ":
                $ engellv += 5
                hide petuniasad at right with easeoutright
                show engelneutral at center with easeinleft
                e " Oh, uh...hey there [name]. "
                e " I wasn't actually expecting you to be here... "
                e " ...You were listening to the conversation me and Petunia had, didn't you? "
                e " She's been...asking what to do with her and Lizzy's situation to a lot of people. "
                e " including me. She was staring at me a lot last class... "
                e " I can really hope that they're gonna be okay in the end... "
                e " Seeing friendships break kinda make me sad a little. "
                e " ...But, getting away from that topic... "
                e " Want to study with me for now? "
                " You had nothing else to do, so you agreed. "
                hide engelneutral at bottom
                show engelhappy at center
                e " Excellent. I'll hand you my notes. "
                scene black with dissolve
                " You spent the rest of the break studying with Engel. "
                " As you were studying, you were praying that Petunia and Lizzy were going to be okay. "
                " Just hoping and praying... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Time for art class. "
                " You get down from the rooftop and walked to your classroom. "
                pause 2.0
                jump artclass3
            " I'd rather stay with myself ":
                hide petuniasad at right with easeoutright
                " You decided to leave the both of them alone. "
                " This was not your business anyway. "
                " You sat down at the corner of the rooftop, pulled out your phone... "
                " ...And started listening to some music you had. "
                " Making up some imaginary scenarios in your head as you chillaxed there. "
                scene black with dissolve
                " You spent the rest of the break chilling out on the rooftop. "
                " As you chillaxed, you saw Petunia on a call with someone. "
                " Of course she was still sad, and you highly doubt that she's talking to Lizzy or whoever the hell she was talking about. "
                " She DOES refuse to talk to her and all that... "
                " You focused more on your imaginary scenarios in your head though. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Time for art class. "
                " You get down from the rooftop and walked to your classroom. "
                pause 2.0
                jump artclass3
    elif engelknow == False and popularknow == True:
        $ engelknow = True
        p " Come on, Engel! I know you're smart! "
        p " Just tell me what I have to do, and you're all good! "
        p " You want anything? Money? Just tell me! "
        e " Petunia, I don't want anything... "
        e " And I'm sorry to tell you this, but you should really just talk it out. "
        e " If you want the best, then that's the best advice I could give. "
        e " If you'll excuse me now... I'd like to get studying. "
        hide petunianeutral at bottom
        show petuniasad at right
        hide engelneutral at left with easeoutright
        show petuniasad at center with move
        " Who do you stay with? "
        menu:
            " Petunia ":
                $ popularlv += 5
                " You were about to ask her if she was alright, but she stopped you. "
                p " Don't bother worrying about me. "
                p " I'm gonna be fine without her by my side, anyway. "
                hide petuniasad at bottom
                show petuniahappy at center
                p " Just needa her to get outta my account, haha!... "
                hide petuniahappy at bottom
                show petuniasad at center
                p " Ha...ha. "
                p " ... "
                p " I'm going home early. "
                p " If they look for me, just tell them my parents had something important to do with me. "
                p " Okay? I trust you. "
                " Petunia gets on her phone and calls her parents. "
                " You didn't stay for long, and walked down stairs... "
                " You didn't want to disturb Petunia anymore anyway. "
                scene black with dissolve
                " You spent the rest of the break walking around in the hallways. "
                " You were wondering if Petunia really was gonna be okay... "
                " You could only hope that she was gonna be. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your final class. "
                " You walked to your classroom after a bit. "
                pause 2.0
                jump artclass3
            " Engel ":
                $ engellv += 5
                hide petuniasad at right with easeoutright
                show engelneutral at center with easeinleft
                e " Oh, uh...hey there [name]. "
                e " I wasn't actually expecting you to be here... "
                e " ...You were listening to the conversation me and Petunia had, didn't you? "
                e " She's been...asking what to do with her and Lizzy's situation to a lot of people. "
                e " including me. She was staring at me a lot last class... "
                e " I can really hope that they're gonna be okay in the end... "
                e " Seeing friendships break kinda make me sad a little. "
                e " ...But, getting away from that topic... "
                e " Want to study with me for now? "
                " You had nothing else to do, so you agreed. "
                hide engelneutral at bottom
                show engelhappy at center
                e " Excellent. I'll hand you my notes. "
                scene black with dissolve
                " You spent the rest of the break studying with Engel. "
                " As you were studying, you were praying that Petunia and Lizzy were going to be okay. "
                " Just hoping and praying... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Time for art class. "
                " You get down from the rooftop and walked to your classroom. "
                pause 2.0
                jump artclass3
            " I'd rather stay with myself ":
                hide petuniasad at right with easeoutright
                " You decided to leave the both of them alone. "
                " This was not your business anyway. "
                " You sat down at the corner of the rooftop, pulled out your phone... "
                " ...And started listening to some music you had. "
                " Making up some imaginary scenarios in your head as you chillaxed there. "
                scene black with dissolve
                " You spent the rest of the break chilling out on the rooftop. "
                " As you chillaxed, you saw Petunia on a call with someone. "
                " Of course she was still sad, and you highly doubt that she's talking to Lizzy or whoever the hell she was talking about. "
                " She DOES refuse to talk to her and all that... "
                " You focused more on your imaginary scenarios in your head though. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Time for art class. "
                " You get down from the rooftop and walked to your classroom. "
                pause 2.0
                jump artclass3
    else:
        x " Come on, Engel! I know you're smart! "
        $ engelknow = True
        x " Just tell me what I have to do, and you're all good! "
        x " You want anything? Money? Just tell me! "
        $ popularknow = True
        e " Petunia, I don't want anything... "
        e " And I'm sorry to tell you this, but you should really just talk it out. "
        e " If you want the best, then that's the best advice I could give. "
        e " If you'll excuse me now... I'd like to get studying. "
        hide petunianeutral at bottom
        show petuniasad at right
        hide engelneutral at left with easeoutright
        show petuniasad at center with move
        " Who do you stay with? "
        menu:
            " Petunia ":
                $ popularlv += 5
                " You were about to ask her if she was alright, but she stopped you. "
                p " Don't bother worrying about me. "
                p " I'm gonna be fine without her by my side, anyway. "
                hide petuniasad at bottom
                show petuniahappy at center
                p " Just needa her to get outta my account, haha!... "
                hide petuniahappy at bottom
                show petuniasad at center
                p " Ha...ha. "
                p " ... "
                p " I'm going home early. "
                p " If they look for me, just tell them my parents had something important to do with me. "
                p " Okay? I trust you. "
                " Petunia gets on her phone and calls her parents. "
                " You didn't stay for long, and walked down stairs... "
                " You didn't want to disturb Petunia anymore anyway. "
                scene black with dissolve
                " You spent the rest of the break walking around in the hallways. "
                " You were wondering if Petunia really was gonna be okay... "
                " You could only hope that she was gonna be. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your final class. "
                " You walked to your classroom after a bit. "
                pause 2.0
                jump artclass3
            " Engel ":
                $ engellv += 5
                hide petuniasad at right with easeoutright
                show engelneutral at center with easeinleft
                e " Oh, uh...hey there [name]. "
                e " I wasn't actually expecting you to be here... "
                e " ...You were listening to the conversation me and Petunia had, didn't you? "
                e " She's been...asking what to do with her and Lizzy's situation to a lot of people. "
                e " including me. She was staring at me a lot last class... "
                e " I can really hope that they're gonna be okay in the end... "
                e " Seeing friendships break kinda make me sad a little. "
                e " ...But, getting away from that topic... "
                e " Want to study with me for now? "
                " You had nothing else to do, so you agreed. "
                hide engelneutral at bottom
                show engelhappy at center
                e " Excellent. I'll hand you my notes. "
                scene black with dissolve
                " You spent the rest of the break studying with Engel. "
                " As you were studying, you were praying that Petunia and Lizzy were going to be okay. "
                " Just hoping and praying... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Time for art class. "
                " You get down from the rooftop and walked to your classroom. "
                pause 2.0
                jump artclass3
            " I'd rather stay with myself ":
                hide petuniasad at right with easeoutright
                " You decided to leave the both of them alone. "
                " This was not your business anyway. "
                " You sat down at the corner of the rooftop, pulled out your phone... "
                " ...And started listening to some music you had. "
                " Making up some imaginary scenarios in your head as you chillaxed there. "
                scene black with dissolve
                " You spent the rest of the break chilling out on the rooftop. "
                " As you chillaxed, you saw Petunia on a call with someone. "
                " Of course she was still sad, and you highly doubt that she's talking to Lizzy or whoever the hell she was talking about. "
                " She DOES refuse to talk to her and all that... "
                " You focused more on your imaginary scenarios in your head though. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit. Time for art class. "
                " You get down from the rooftop and walked to your classroom. "
                pause 2.0
                jump artclass3

label wedlibrary5:
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and found two of your classmates doing their own things. "
    " Who do you want to talk to? "
    if skellknow == True and lanaknow == True:
        menu:
            " {image=skellicon} Skell {image=skellicon} ":
                jump hplala
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump asuslala
    elif skellknow == True and lanaknow == False:
        menu:
            " {image=skellicon} Skell {image=skellicon} ":
                jump hplala
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump asuslala
    elif skellknow == False and lanaknow == True:
        menu:
            " {image=skellicon} An emo kid {image=skellicon} ":
                jump hplala
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump asuslala
    else:
        menu:
            " {image=skellicon} An emo kid {image=skellicon} ":
                jump hplala
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump asuslala
    label hplala:
        show skellneutral at center with easeinleft
        if skellknow == True:
            sk " Hey there. "
            sk " I was just thinking of what I should do after class. "
            sk " I mean, I know I should do assignments, buuuuut... "
            sk " Thing is, all of our assignments are due next week. "
            sk " They're being more generous after you arrived, wow. "
            sk " Usually they're due the next day, but here we are now. "
            sk " You've got some special powers to make the teachers change the homework due date or something. "
            sk " Not that I'm complaining. It's real nice to get a break like this. "
            sk " Anyway... "
            sk " I should probably do some mad gaming sessions. "
            hide skellneutral at bottom
            show skellhappy at center
            sk " Like playing on boblox all night...and some CraftMine here and there... "
            sk " Drinking a lot of soda to keep me up...that sounds really nice. "
            sk " I need to have some gaming sessions and ignore all of the homework for once. "
            sk " I'm just going to worry about all of that on Sunday. "
            sk " Should be fineee, right? "
            hide skellhappy at bottom
            show skellneutral at center
            sk " Anyway, wanna do some hangman with me? "
            sk " I'm kind of bored, and I need something to entertain me. "
            " Hey, you're also bored and need to do something. "
            " Youagreed to play some hangman with Skell. "
            sk " Sweet. I'll get us some paper... "
            sk " I'll have you know that I'm pretty good at hangman, so, good luck. "
            scene black with dissolve
            " You spent the rest of the break playing hangman with Skell. "
            " He really wasn't lying when he said that he was good at hangman... "
            " Your game went pretty good though. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your final class. "
            " You get up from where you were sitting and you walked back to your classroom. "
            pause 2.0
            jump artclass3
        else:
            x " Hey there. "
            x " Don't believe we've met before... "
            x " ...I just know that you're that new kid from days ago. "
            x " Let me introduce myself or whatever. "
            $ skellknow = True
            sk " I'm Skell, it's nice to meet you. "
            sk " Anyway, I was just thinking of what I should do after class. "
            sk " I mean, I know I should do assignments, buuuuut... "
            sk " Thing is, all of our assignments are due next week. "
            sk " They're being more generous after you arrived, wow. "
            sk " Usually they're due the next day, but here we are now. "
            sk " You've got some special powers to make the teachers change the homework due date or something. "
            sk " Not that I'm complaining. It's real nice to get a break like this. "
            sk " Anyway... "
            sk " I should probably do some mad gaming sessions. "
            hide skellneutral at bottom
            show skellhappy at center
            sk " Like playing on boblox all night...and some CraftMine here and there... "
            sk " Drinking a lot of soda to keep me up...that sounds really nice. "
            sk " I need to have some gaming sessions and ignore all of the homework for once. "
            sk " I'm just going to worry about all of that on Sunday. "
            sk " Should be fineee, right? "
            hide skellhappy at bottom
            show skellneutral at center
            sk " Anyway, wanna do some hangman with me? "
            sk " I'm kind of bored, and I need something to entertain me. "
            " Hey, you're also bored and need to do something. "
            " Youagreed to play some hangman with Skell. "
            sk " Sweet. I'll get us some paper... "
            sk " I'll have you know that I'm pretty good at hangman, so, good luck. "
            scene black with dissolve
            " You spent the rest of the break playing hangman with Skell. "
            " He really wasn't lying when he said that he was good at hangman... "
            " Your game went pretty good though. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your final class. "
            " You get up from where you were sitting and you walked back to your classroom. "
            pause 2.0
            jump artclass3

    label asuslala:
        show lananeutral at center with easeinright
        if lanaknow == True:
            l " Hi there [name]!! "
            l " You know that situation Petunia and Lizzy are having right now? "
            l " I know I should be worried about them, buuut... "
            hide lananeutral at bottom
            show lanahappy at center
            l " The way they're acting right now is giving me some MAD ideas for a story! "
            l " Yes, yes - I should be hoping them the best, but I just managed to be in need for some ideas with Juliana and Pedro! "
            hide lanahappy at bottom
            show lananeutral at center
            l " I {i}am{/i} hoping them the best though. "
            l " So I was thinking this storyline for Juliana and Pedro - "
            l " I'm sure you weren't really there for the last few episodes, so let's say Juliana moved to a new city to see better people. "
            l " Juliana walked around the city and found a guy at a restaurant named Rainier! "
            l " Rainier's this...bisexual dude, by the way. He goes both ways and he's also a waiter! "
            l " Anyway, he and Juliana get well together, right? "
            l " He invited Juliana over at his place since he had a break day... "
            l " ...He and Juliana have a good time... and guess what? "
            hide lananeutral at bottom
            show lanahappy at center
            l " BAM! Juliana finds a picture of Rainier and Pedro together! " with vpunch
            l " She gasps in utter horror. So this was the person who took her dearest love away?! "
            l " She couldn't handle it, and she lashes out at Rainier! "
            hide lanahappy at bottom
            show lanaangry at center
            l " ...Actually, I can't remember if I said that Pedro got with a man or a woman...shucks. "
            hide lanaangry at bottom
            show lananeutral at center
            l " Well, if I DID say that he got with a woman, let's just sayyyy... "
            l " ...That he lied to Juliana, yeah! "
            l " Anyway, Juliana storms out of his house, and Rainier wanted to make things okay with her- "
            l " But, Juliana doesn't listen - too angry to even think about anything - and leaves. "
            l " Sooo...they hate eachother now! Well, more likely Juliana hates Rainier. "
            l " Rainier's just trying to make things okay with her and trying to get them to be friends again. "
            l " Juliana's still being a bit stubborn though. "
            hide lananeutral at bottom
            show lanahappy at center
            l " What will happen next? Find out on the next episode of Juliana and Pedro! "
            hide lanahappy at bottom
            show lananeutral at center
            l " Soooo...what did you think? "
            menu:
                " TS SO PEAK I LOVE IT ":
                    $ lanalv += 5
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " Yayyy! I'm glad that you think that it's good! "
                    l " I need to tweak out a few things though, since I didn't really like some things that I wrote in the script. "
                    hide lanahappy at bottom
                    show lananeutral at center
                    l " Actually, could you help me with writing a few things for the script? "
                    l " I'll even credit you if you do! It'll be fun, I promise! "
                    " Well, you do need to let your creativity out for once... "
                    " You agreed to help Lana with writing her script for her story. "
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " Yayyy!! I'm so glad you agreed! "
                    l " Let's get started right away! "
                    scene black with dissolve
                    " You spent the rest of the break writing a script for Lana's story. "
                    " You gave her some pretty good ideas here and there, making sure things made sense... "
                    " And in the end, you guys came up with a pretty good story. "
                    " A lot of drama here and there, following the outline Lana gave you earlier... "
                    " Very nice. This would go pretty hard if it was an actual movie. "
                    " Maybe Lana should be a movie director or something one day... "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for your final class of the day. "
                    " You get out of the library and walked back to your classroom for your art class. "
                    pause 2.0
                    jump artclass3
                " It's okay ":
                    l " You think it's okay? that's alright! "
                    l " But the fact that you said it was okay means that it needs some improvements. "
                    l " And I can TOTALLY agree with that because I don't like the script I wrote for it too! "
                    l " The audience needs the best, after all! "
                    l " Actually, could you help me with writing a few things for the script? "
                    l " I'll even credit you if you do! It'll be fun, I promise! "
                    " Well, you do need to let your creativity out for once... "
                    " You agreed to help Lana with writing her script for her story. "
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " Yayyy!! I'm so glad you agreed! "
                    l " Let's get started right away! "
                    scene black with dissolve
                    " You spent the rest of the break writing a script for Lana's story. "
                    " You gave her some pretty good ideas here and there, making sure things made sense... "
                    " And in the end, you guys came up with a pretty good story. "
                    " A lot of drama here and there, following the outline Lana gave you earlier... "
                    " Very nice. This would go pretty hard if it was an actual movie. "
                    " Maybe Lana should be a movie director or something one day... "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for your final class of the day. "
                    " You get out of the library and walked back to your classroom for your art class. "
                    pause 2.0
                    jump artclass3
        else:
            x " Hi there [name]!! "
            x " Oh wait, I don't think I've introduced myself to you yet! Sorry! "
            $ lanaknow = True
            l " I'm Lana! It's so, so nice to meet you! "
            l " Anyway, you know that situation Petunia and Lizzy are having right now? "
            l " I know I should be worried about them, buuut... "
            hide lananeutral at bottom
            show lanahappy at center
            l " The way they're acting right now is giving me some MAD ideas for a story! "
            l " Yes, yes - I should be hoping them the best, but I just managed to be in need for some ideas with Juliana and Pedro! "
            hide lanahappy at bottom
            show lananeutral at center
            l " I {i}am{/i} hoping them the best though. "
            l " So I was thinking this storyline for Juliana and Pedro - "
            l " I'm sure you weren't really there for the last few episodes, so let's say... "
            l " Juliana is this woman who's love, Pedro, had just broken up with her! "
            l " And then, after that, juliana moved to a new city to see better people. "
            l " Juliana walked around the city and found a guy at a restaurant named Rainier! "
            l " Rainier's this...bisexual dude, by the way. He goes both ways and he's also a waiter! "
            l " Anyway, he and Juliana get well together, right? "
            l " He invited Juliana over at his place since he had a break day... "
            l " ...He and Juliana have a good time... and guess what? "
            hide lananeutral at bottom
            show lanahappy at center
            l " BAM! Juliana finds a picture of Rainier and Pedro together! " with vpunch
            l " She gasps in utter horror. So this was the person who took her dearest love away?! "
            l " She couldn't handle it, and she lashes out at Rainier! "
            hide lanahappy at bottom
            show lanaangry at center
            l " ...Actually, I can't remember if I said that Pedro got with a man or a woman...shucks. "
            hide lanaangry at bottom
            show lananeutral at center
            l " Well, if I DID say that he got with a woman, let's just sayyyy... "
            l " ...That he lied to Juliana, yeah! "
            l " Anyway, Juliana storms out of his house, and Rainier wanted to make things okay with her- "
            l " But, Juliana doesn't listen - too angry to even think about anything - and leaves. "
            l " Sooo...they hate eachother now! Well, more likely Juliana hates Rainier. "
            l " Rainier's just trying to make things okay with her and trying to get them to be friends again. "
            l " Juliana's still being a bit stubborn though. "
            hide lananeutral at bottom
            show lanahappy at center
            l " What will happen next? Find out on the next episode of Juliana and Pedro! "
            hide lanahappy at bottom
            show lananeutral at center
            l " Soooo...what did you think? "
            menu:
                " TS SO PEAK I LOVE IT ":
                    $ lanalv += 5
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " Yayyy! I'm glad that you think that it's good! "
                    l " I need to tweak out a few things though, since I didn't really like some things that I wrote in the script. "
                    hide lanahappy at bottom
                    show lananeutral at center
                    l " Actually, could you help me with writing a few things for the script? "
                    l " I'll even credit you if you do! It'll be fun, I promise! "
                    " Well, you do need to let your creativity out for once... "
                    " You agreed to help Lana with writing her script for her story. "
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " Yayyy!! I'm so glad you agreed! "
                    l " Let's get started right away! "
                    scene black with dissolve
                    " You spent the rest of the break writing a script for Lana's story. "
                    " You gave her some pretty good ideas here and there, making sure things made sense... "
                    " And in the end, you guys came up with a pretty good story. "
                    " A lot of drama here and there, following the outline Lana gave you earlier... "
                    " Very nice. This would go pretty hard if it was an actual movie. "
                    " Maybe Lana should be a movie director or something one day... "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for your final class of the day. "
                    " You get out of the library and walked back to your classroom for your art class. "
                    pause 2.0
                    jump artclass3
                " It's okay ":
                    l " You think it's okay? that's alright! "
                    l " But the fact that you said it was okay means that it needs some improvements. "
                    l " And I can TOTALLY agree with that because I don't like the script I wrote for it too! "
                    l " The audience needs the best, after all! "
                    l " Actually, could you help me with writing a few things for the script? "
                    l " I'll even credit you if you do! It'll be fun, I promise! "
                    " Well, you do need to let your creativity out for once... "
                    " You agreed to help Lana with writing her script for her story. "
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " Yayyy!! I'm so glad you agreed! "
                    l " Let's get started right away! "
                    scene black with dissolve
                    " You spent the rest of the break writing a script for Lana's story. "
                    " You gave her some pretty good ideas here and there, making sure things made sense... "
                    " And in the end, you guys came up with a pretty good story. "
                    " A lot of drama here and there, following the outline Lana gave you earlier... "
                    " Very nice. This would go pretty hard if it was an actual movie. "
                    " Maybe Lana should be a movie director or something one day... "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for your final class of the day. "
                    " You get out of the library and walked back to your classroom for your art class. "
                    pause 2.0
                    jump artclass3

label wedoligang5:
    scene black with dissolve
    pause 2.0
    scene oligangclub with dissolve
    " You walked into the club and spotted Oliver and Edward talking about something. "
    " Wondering what they're up to, you walked up to them. "
    show edwardneutral at left with easeinright
    show oliverneutral at right with easeinright
    ed " Yoyoyoooo, it's the new [person]! "
    o " Hey there, [name]! "
    o " Me and Eddie over here were just talking about the situation Petunia's having with Lizzy right now. "
    ed " Interesting, yeah? "
    ed " It's not really anything new for me, since I've seen them argue a couple of times. "
    ed " The whole school has seen them fight sometimes, and it's never NOT entertaining. "
    ed " Peak drama, I tell you! "
    o " Agreed, agreed...anyway, I heard that Petunia's just going to get out of school early. "
    o " Already called her parents and everything. "
    " You look around and spotted Zip was missing. "
    " Confused, you asked where Zip was. "
    o " Her? she's spying on what Petunia's doing right now. "
    ed " Ya see, Zip's kinda like our little security camera thing. "
    ed " With the perks of being a dragon and all, she has wings. "
    ed " And having wings, means that she can fly up in the air and spy whoever the hell she wants! "
    ed " See what I'm getting at here? "
    o " Well, Zip only every flies whenever she checks out the rooftop. "
    o " How she hears the conversations? Super good hearing, duh. "
    ed " She's just that amazing, really! "
    ed " Before I actually used to think she was a lame loser but she's MEGA cool now. "
    o " Oop, just got a message from Zip. Let's see what this is about... "
    hide oliverneutral at bottom
    show oliverhappy at right
    o " oHO. Looks like she just figured out the reason why they were beefin in the first place! "
    o " Let's see... "
    o " Apparently it was because the fact that Lizzy felt jealous of Petunia! "
    o " She's been getting a lot of comments about Petunia and rarely about her herself... "
    hide oliverhappy at bottom
    show oliverbully at right
    o  " ...Pretty FUCKING funny if you ask me! "
    hide edwardneutral at bottom
    show edwardbully at left
    ed " Hah! Is that really the reason?! god, this has to be the most stupidest thing they've ever argued about! "
    ed " Looks like we've got a new topic to bully Petunia and Lizzy about! "
    hide edwardbully at bottom
    show edwardneutral at left
    ed " Though, I would like to see Petunia and Lizzy argue a bit more. "
    hide oliverbully at bottom
    show oliverhappy at right
    o " Yeah, same. "
    o " I'm getting a bit tired of their short arguments. "
    o " I want them to argue for an entire week! "
    scene black with dissolve
    " You spent the rest of the break talking with Oliver and Edward. "
    " Talking about that one situation Petunia and Lizzy are having... "
    " You're starting to think that thing is pretty interesting now and starting to think that they should argue a bit more. "
    " DAMN they're already starting to influence you hard, huh? "
    " Guess that's just the oligang effect. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for the last class of the day. "
    " You and the gang hang out for a bit, and then enter the next class after a few moments. "
    pause 2.0
    jump artclass3

label artclass3:
    scene classroom with dissolve
    " You sat down in your seat and waited for the teacher to arrive. "
    " As you were waiting, you decided to draw on the desk you were on. "
    " There were some other students drawings on them, all from different times... "
    " Woah, you just ended up on an ancient relic. a note from the 2000's. "
    " It's a really nice drawing of probably the person who drew it. "
    " Wonder where that guy is at now... "
    " ...You leave a cool drawing of an S right next to it. "
    " The teacher arrives a few moments after you were done with drawing. Time to lock in. "
    show sashaneutral at center with easeinright
    mss " Hello, everyone! "
    mss " I hope you've had a good day today! "
    mss " You're all going to be taking down a few notes for today, yaayy! Nothing much to do!! "
    mss " Hold on... "
    hide sashaneutral at bottom
    show sashaconfused at center
    mss " Where's Petunia? "
    mss " Hmm... "
    hide sashaconfused at bottom
    show sashaneutral at center
    mss " As long as she shows up with an excuse later tomorrrow! "
    mss " I'm sure that'll explain where she's been! "
    mss " Anyway...get your notebooks and pens, it's time to get writing! "
    scene black with dissolve
    " You spent the rest of the class writing down notes for art class. "
    " Nothing interesting happened in class, of course. "
    " You were pretty happy that class was ending soon though, and couldn't wait. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit of copying, time for you to go back home!! "
    " You close your notebook and get your things ready, and then headed out of school. "
    pause 2.0
    jump wedendday

label wedendday:
    scene paperschoolfront with dissolve
    " Ah yes, finally time for the end of school. "
    " You look around at your classmates, seeing all of them smiling, laughing... "
    " Some of them looking down and having beef with eachother. "
    " The average school expirience. "
    if oligangjoin == True:
        " As you were about to go home, you were stopped by Oliver. "
        " He looked like he needed a word with you... "
        show oliverneutral at center with easeinright
        o " Heya there, [name]! "
        o " Just wanted to say that having you in our gang is really fun. "
        hide oliverneutral at bottom
        show oliverhappy at center
        o " Hopefully you can cause some mischief with us tomorrow, hehe! "
        o " Gotta go now before a certain someone chases after me. See ya~! "
        hide oliverhappy at left with easeoutleft
        " Well, time for you to go home then. "
        scene black with dissolve
        pause 2.0
        jump mcgohomewed
    elif abbieteach == True:
        " As you were about to go home, you were stopped by Abbie. "
        " He looked like he needed a word with you... "
        show abbiehappy at center with easeinleft
        a " H..hey there [name]...! "
        a " I'm thinking that I should probably train on my own, since you taught me everything I needed to... "
        a " I'll...I'll send you some updates later, okay...? "
        a " Have a good night...! "
        hide abbiehappy at right with easeoutright
        " Wow. He looks more happy than when you first met him. "
        " You're glad that you could help him. "
        " Well, time for you to go home then. "
        scene black with dissolve
        pause 2.0
        jump mcgohomewed
    elif popularknow == True:
        " Before you went home, you checked your GC to see if anything's up... "
        " ...Only to find that you were kicked out of the GC that you were in with Petunia and Lizzy. "
        " You're starting to think that this whole thing was because of you. "
        " But, you shouldn't overthink it. You closed your phone and put it back into your pocket. "
        " Well, time for you to go home then. "
        scene black with dissolve
        pause 2.0
        jump mcgohomewed
    elif clairebeatup == True:
        " ...You're gonna be able to do a good choice tomorrow. "
        " Make sure you don't choose the wrong option. "
        " Well, time for you to go home then. "
        scene black with dissolve
        pause 2.0
        jump mcgohomewed
    else:
        " Well, time for you to go home then. "
        scene black with dissolve
        pause 2.0
        jump mcgohomewed
label mcgohomewed:
    stop music fadeout 1.5
    pause 1.0
    play music "audio/home.mp3" fadein 2.0
    scene mcroom with dissolve
    " You got into your room and got out of your clothes, putting your bag to the side. "
    " Changing into your bedwear, you checked the GC to see if there's anything up. "
    " No assignmetns since everything is due next week...nice. "
    " You laid down on your bed and left your phone to charge over night. "
    " You then started to close your eyes, falling into a deep slumber... "
    scene black with dissolve
    " Good night, [name]. "
    " Sweet dreams. "
    pause 2.0
    jump thursday
