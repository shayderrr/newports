label teacherwednesday:
    show text " DAY 3 - WEDNESDAY "
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
    " As you were about to walk into the school, you couldn't help but notice a missing student poster that flew down to your feet. "
    " You picked it up and took a closer look on who it was... "
    " Looks like it was a random student that you don't even know about. "
    " It didn't make you less concerned though, a student is still a human being after all. "
    " Maybe the other teachers know about this...you might have to talk to one of them today. "
    " You walked into the school with the poster crumpled into your pocket. "
    scene black with dissolve
    pause 1.5
    scene hallway with dissolve
    pause 1.5
    scene gardenroom with dissolve
    " You sat down onto your chair and waited for it to be time to start the class. "
    " As you were waiting for it to be time, you played games on your phone. "
    " The thought of the missing student still lingering on your mind as you played... "
    " You REALLY have to talk about this to another teacher. "
    " You could only wait until it's time to start class though... "
    pause 1.0
    play sound "audio/bellring.mp3"
    " Well, would you look at that. It's time to help another teacher! "
    " Let's go and see who needs help. "
    scene black with dissolve
    pause 2.0
    jump twclass1

label twclass1:
    scene hallway with dissolve
    " Who do you want to help today? "
    if circleknow,thavelknow,bloomieknow == True:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump grassgreen
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump cloudwhite
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump bluesky
    elif circleknow,thavelknow == True and bloomieknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump grassgreen
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump cloudwhite
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump bluesky
    elif circleknow,bloomieknow == True and thavelknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump grassgreen
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump cloudwhite
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump bluesky
    elif thavelknow,bloomieknow == True and circleknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump grassgreen
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump cloudwhite
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump bluesky
    elif circleknow == True and thavelknow,bloomieknow == False:
        menu:
            " {image=misscircleicon} Miss Bloomie {image=misscircleicon} ":
                jump grassgreen
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump cloudwhite
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump bluesky
    elif thavelknow == True and circleknow,bloomieknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump grassgreen
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump cloudwhite
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump bluesky
    elif bloomieknow == True and circleknow,thavelknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump grassgreen
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump cloudwhite
            " {image=missbloomieicon} Bloomie {image=missbloomieicon} ":
                jump bluesky
    else:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump grassgreen
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump cloudwhite
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump bluesky
label grassgreen:
    $ askedcircle = True
    # miss circle - asking abuot the missing student
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    " You walked into the math classroom only to find the students doing some work. "
    " You looked around and eventually found the math teacher at her desk. "
    " Hey, let's go and talk to her about the missing student you've heard about. "
    " Maybe she knows something? or not. Let's find out. "
    show misscircleneutral at center with easeinleft
    if circleknow == True:
        msc " Hmhmhm...oh? "
        msc " Hey there, [name]! Did you need something from me? "
        msc " Had a question? If it's about me recovering so quickly, I'm fine. "
        msc " I just had some...very good medicine to help me out. "
        msc " Trust me! I'm fine. "
        " You told her that you were glad to know that she was alright, "
        " But that's not what you're concerned about. "
        msc " ...? Oh, really? Then what did you need? "
        msc " Did you need some advice from me on what to do when your students are out of control? "
        msc " What to do when your students fail one of the most easiest exams in the world and you feel like you're about to crash out? "
        msc " Just tell me - I might have an answer to your questions! "
        " You told her that it was none of what she had just said. "
        " You asked her about what happened to the missing student...if she knew anything about it. "
        " You could swear that you saw just a hint of annoyance in Miss Circle's face for a split moment. "
        " Might just be your eyes tricking you. You've never seen her annoyed like that. Or have you? "
        " Can't really remember, sorry. Being a bad narrator here, woopsies! "
        " Anyway, she takes a moment to take a deep breath in before responding. "
        msc " I'm sorry, but a missing student? "
        msc " I have just now heard about this from you! "
        msc " I'll make sure to contact Miss Grace about it. "
        msc " Can't have a student going missing, after all! "
        msc " We'd get complaints from their parents, heheh. "
        msc " Infact, I'll go ahead and call Miss Grace right now! "
        msc " Take care of my class while I'm gone, alright? "
        hide misscircleneutral at right with easeoutright
        " Before you could say anything else, Miss Circle is gone. "
        " You have a feeling Miss Grace might have something to do with the missing student... "
        " ...But that's only your assumptions. Who knows if she did something or not. "
        " Anywho, you decided to stick in Miss Circle's classroom. She did ask you to stay here and take care of her students, after all. "
        " This class is your responsibility for the time being...how fun. "
        " As you looked around, you could see Miss Circle talking to Miss Grace on the phone outside. "
        " Miss Circle turned around for a bit, showing a side view of her face. "
        " She didn't look happy at all. I mean, of course she wouldn't after what she heard...or maybe it could be for another reason. "
        " She looked almost as if she was worried. Or, annoyed. A mix of both of that. "
        " You wonder why. "
        " Your attention is caught by a student who came up to you to check if they did their work right. "
        " Annnnd you get distracted. "
        scene black with dissolve
        " You spent the rest of the class time checking the student's works. "
        " It was going pretty good, but you couldn't get the thought of the missing student out of your head. "
        " You need answers to what happened. A school should be safe for teachers and students. "
        " A student going missing is just completely worrisome, and it shouldn't go unnoticed. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Time for break. "
        " You're gonna have to see what you can do. "
        pause 2.0
        jump twbreak1
    else:
        x " Hmhmhm...oh? "
        x " Hey there, [name]! Did you need something from me? "
        x " Oh, right! Before you ask me anything, I would like to introduce myself! "
        x " I kind of forgot to introduce myself to you in the first day, sorry about that... "
        $ circleknow = True
        msc " I'm Miss Circle, and I'm the math teacher! Real glad to finally get to talk to you."
        msc " Anyway, you had a question? "
        msc " Oh! I'm pretty sure that you've heard about me being sick yesterday, right? "
        msc " If it's about me recovering so quickly, I'm fine. "
        msc " I just had some...very good medicine to help me out. "
        msc " Trust me! I'm fine. "
        " You told her that you were glad to know that she was alright, "
        " But that's not what you're concerned about. "
        msc " ...? Oh, really? Then what did you need? "
        msc " Did you need some advice from me on what to do when your students are out of control? "
        msc " What to do when your students fail one of the most easiest exams in the world and you feel like you're about to crash out? "
        msc " Just tell me - I might have an answer to your questions! "
        " You told her that it was none of what she had just said. "
        " You asked her about what happened to the missing student...if she knew anything about it. "
        " You could swear that you saw just a hint of annoyance in Miss Circle's face for a split moment. "
        " Might just be your eyes tricking you. You've never seen her annoyed like that. Or have you? "
        " Can't really remember, sorry. Being a bad narrator here, woopsies! "
        " Anyway, she takes a moment to take a deep breath in before responding. "
        msc " I'm sorry, but a missing student? "
        msc " I have just now heard about this from you! "
        msc " I'll make sure to contact Miss Grace about it. "
        msc " Can't have a student going missing, after all! "
        msc " We'd get complaints from their parents, heheh. "
        msc " Infact, I'll go ahead and call Miss Grace right now! "
        msc " Take care of my class while I'm gone, alright? "
        hide misscircleneutral at right with easeoutright
        " Before you could say anything else, Miss Circle is gone. "
        " You have a feeling Miss Grace might have something to do with the missing student... "
        " ...But that's only your assumptions. Who knows if she did something or not. "
        " Anywho, you decided to stick in Miss Circle's classroom. She did ask you to stay here and take care of her students, after all. "
        " This class is your responsibility for the time being...how fun. "
        " As you looked around, you could see Miss Circle talking to Miss Grace on the phone outside. "
        " Miss Circle turned around for a bit, showing a side view of her face. "
        " She didn't look happy at all. I mean, of course she wouldn't after what she heard...or maybe it could be for another reason. "
        " She looked almost as if she was worried. Or, annoyed. A mix of both of that. "
        " You wonder why. "
        " Your attention is caught by a student who came up to you to check if they did their work right. "
        " Annnnd you get distracted. "
        scene black with dissolve
        " You spent the rest of the class time checking the student's works. "
        " It was going pretty good, but you couldn't get the thought of the missing student out of your head. "
        " You need answers to what happened. A school should be safe for teachers and students. "
        " A student going missing is just completely worrisome, and it shouldn't go unnoticed. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Time for break. "
        " You're gonna have to see what you can do. "
        pause 2.0
        jump twbreak1
label cloudwhite:
    $ askedthavel = True
    # miss thavel - asking about the missing student
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    " You walked into the classroom and found that the language teacher was teaching something to her students. "
    " From what you could see, she was teaching her students some sentences in different languages. "
    " You quickly poked her to get her attention, interrupting her class for a bit. "
    " You know that it might be a little rude to do this, but you've just GOT to talk to her about what's going on. "
    " You needed answers, and you needed them now. "
    show msthravelneutral at center with easeinleft
    if thavelknow == True:
        mst " Oh! Hola, [name]! "
        mst " Did you need anything from me? "
        mst " Perhaps you had a question for me? "
        mst " If it's anything about Miss Circle's quick recovery, she's doing fine. "
        mst " Oooor you wanted some advice from me? "
        mst " Though, this kind of has to be important because I don't want my students to start being loud and using their phones. "
        mst " That happening has to be the most annoying thing ever... "
        mst " ...You can really just waste your breath on them by ranting about how annoying they're being. "
        mst " Anyway! What did you want from me? "
        " You told her that it was great knowing that Miss Circle's doing well now... "
        " ...But you were here for a completely different reason. "
        " You then asked her about the recently missing student. You asked if she knew anything about them. "
        " Any information of what happened, anything, really. Where they were last seen... "
        " ...Okay, we should've became detectives instead of teachers. "
        " Miss Thavel kind of just stared at you, and you could SWEAR that she looked just a little mad at you for asking her about this. "
        " She was acting as if this wasn't a serious situation, which is just absurd! "
        " I mean, you're NOT the type of teacher to just wait until things get worse before taking action. "
        " That's just being a horrible teacher in your opinion... "
        " Miss Thavel stares at you a bit more before she responded. "
        mst " ...Oh my, a missing student! "
        mst " I actually didn't know about that until now! "
        " Not with all of the missing student posters around the school? "
        " I mean, those were probably added in a bit early and the teachers thought nothing about it, but still... "
        mst " I'll go and have a talk with Miss Grace about it, alright? "
        mst " You're going to have to take care of my students though. "
        mst " Here's their topic for today! "
        " Miss Thavel gives you some papers of what they were supposed to talk about for the day. "
        hide msthavelneutral at right with easeoutright
        " Before you could say anything, she exits out of the room to go to the principal's office. "
        " And now you have all of the student's eyes on you...how fun. "
        " Well, time to get teaching then. Hopefully you knew a thing or two about language and stuff. "
        scene black with dissolve
        " You spent the rest of the classtime teaching the students about things they can say in different languages. "
        " As you were teaching, you couldn't get the thought of the missing student out of your head. "
        " You need answers to what happened. A school should be safe for teachers and students. "
        " A student going missing is just completely worrisome, and it shouldn't go unnoticed. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Time for break. "
        " You're gonna have to see what you can do. "
        pause 2.0
        jump twbreak1
    else:
        x " Oh! Hola, [name]! "
        x " Wait, sorry, I don't think I've introduced myself to you yet. "
        x " I think I forgot to do that on your first day here, hah... "
        $ thavelknow = True
        mst " I'm Miss Thavel! The language teacher. It's real nice to finally talk to you! "
        mst " Anyway, did you need anything from me? "
        mst " Perhaps you had a question for me? "
        mst " If it's anything about Miss Circle's quick recovery, she's doing fine. "
        mst " Oooor you wanted some advice from me? "
        mst " Though, this kind of has to be important because I don't want my students to start being loud and using their phones. "
        mst " That happening has to be the most annoying thing ever... "
        mst " ...You can really just waste your breath on them by ranting about how annoying they're being. "
        mst " Anyway! What did you want from me? "
        " You told her that it was great knowing that Miss Circle's doing well now... "
        " ...But you were here for a completely different reason. "
        " You then asked her about the recently missing student. You asked if she knew anything about them. "
        " Any information of what happened, anything, really. Where they were last seen... "
        " ...Okay, we should've became detectives instead of teachers. "
        " Miss Thavel kind of just stared at you, and you could SWEAR that she looked just a little mad at you for asking her about this. "
        " She was acting as if this wasn't a serious situation, which is just absurd! "
        " I mean, you're NOT the type of teacher to just wait until things get worse before taking action. "
        " That's just being a horrible teacher in your opinion... "
        " Miss Thavel stares at you a bit more before she responded. "
        mst " ...Oh my, a missing student! "
        mst " I actually didn't know about that until now! "
        " Not with all of the missing student posters around the school? "
        " I mean, those were probably added in a bit early and the teachers thought nothing about it, but still... "
        mst " I'll go and have a talk with Miss Grace about it, alright? "
        mst " You're going to have to take care of my students though. "
        mst " Here's their topic for today! "
        " Miss Thavel gives you some papers of what they were supposed to talk about for the day. "
        hide msthavelneutral at right with easeoutright
        " Before you could say anything, she exits out of the room to go to the principal's office. "
        " And now you have all of the student's eyes on you...how fun. "
        " Well, time to get teaching then. Hopefully you knew a thing or two about language and stuff. "
        scene black with dissolve
        " You spent the rest of the classtime teaching the students about things they can say in different languages. "
        " As you were teaching, you couldn't get the thought of the missing student out of your head. "
        " You need answers to what happened. A school should be safe for teachers and students. "
        " A student going missing is just completely worrisome, and it shouldn't go unnoticed. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Time for break. "
        " You're gonna have to see what you can do. "
        pause 2.0
        jump twbreak1
label bluesky:
    $ askedbloomie = True
    # miss bloomie - asking aboutthe missing student
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    " You walked into the classroom and spotted the science teacher demonstrating an experiment. "
    " Before she could do anything, she noticed you standing by the door and looking as if you wanted to ask her a question. "
    " She puts her things on her desks before excusing herself from her class, before going to you. "
    " She looked like she was hoping this is going to be important...to which is was going to be. "
    show missbloomieneutral at center with easeinleft
    if bloomieknow == True:
        msb " Hello there, [name]. "
        msb " Did you need something from me? "
        msb " If it's anything about Circle's health, then she's doing fine. "
        msb " Recored quickly and all that, somehow. "
        msb " If it's anything else, then you're free to ask. "
        " You take a deep breath in, and you asked Miss Bloomie about the student that went missing. "
        " You told her that you felt worried about them and asked her if she knew anything about it. "
        " ...She just stares at you for a bit when you mentioned that to her. "
        " Though, for a moment, you could see her eye twitching. Don't know what that means. "
        " Probably meant that she was just a little mad at you. Though, for what reason? "
        " You don't know. Though if you asked her, she probably wouldn't tell you. "
        " After a few moments of staring at you, she responds to your question. "
        msb " ...I actually didn't know about the missing student. "
        msb " Thank you for telling me about this though. "
        msb " A student going missing is something to take seriously. "
        msb " I'll go ahead and have a talk with Miss Grace right now. "
        msb " That DOES mean that you have to take over my class though. "
        msb " Hopefully you're okay with that... "
        msb " I'll get going now though. See you later. "
        hide missbloomieneutral at right with easeoutright
        " Before you could say anything else, Miss Bloomie gets out of the classroom. "
        " And now you've got the students looking at you, confused on what happened. "
        " Well...you're sure Miss Bloomie has something that says what they're talking about. "
        " Time to get teaching then. "
        scene black with dissolve
        " You spent the rest of the class time taking over Miss Bloomie's class. "
        " You were just following a recipe book you found on Bloomie's desk and found what they were talking about. "
        " Hopefully you were doing all of that right though. Otherwise it would be a disaster. "
        " As you were teaching, you couldn't get the thought of the missing student out of your head. "
        " You need answers to what happened. A school should be safe for teachers and students. "
        " A student going missing is just completely worrisome, and it shouldn't go unnoticed. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Time for break. "
        " You're gonna have to see what you can do. "
        pause 2.0
        jump twbreak1
    else:
        x " Hello there, [name]. "
        x " I forgot that I haven't introduced myself to you, I apologize. "
        $ bloomieknow = True
        msb " I am Miss Bloomie. The science teacher. It is a pleasure to finally talk to you. "
        msb " Did you need something from me? "
        msb " If it's anything about Circle's health, then she's doing fine. "
        msb " Recored quickly and all that, somehow. "
        msb " If it's anything else, then you're free to ask. "
        " You take a deep breath in, and you asked Miss Bloomie about the student that went missing. "
        " You told her that you felt worried about them and asked her if she knew anything about it. "
        " ...She just stares at you for a bit when you mentioned that to her. "
        " Though, for a moment, you could see her eye twitching. Don't know what that means. "
        " Probably meant that she was just a little mad at you. Though, for what reason? "
        " You don't know. Though if you asked her, she probably wouldn't tell you. "
        " After a few moments of staring at you, she responds to your question. "
        msb " ...I actually didn't know about the missing student. "
        msb " Thank you for telling me about this though. "
        msb " A student going missing is something to take seriously. "
        msb " I'll go ahead and have a talk with Miss Grace right now. "
        msb " That DOES mean that you have to take over my class though. "
        msb " Hopefully you're okay with that... "
        msb " I'll get going now though. See you later. "
        hide missbloomieneutral at right with easeoutright
        " Before you could say anything else, Miss Bloomie gets out of the classroom. "
        " And now you've got the students looking at you, confused on what happened. "
        " Well...you're sure Miss Bloomie has something that says what they're talking about. "
        " Time to get teaching then. "
        scene black with dissolve
        " You spent the rest of the class time taking over Miss Bloomie's class. "
        " You were just following a recipe book you found on Bloomie's desk and found what they were talking about. "
        " Hopefully you were doing all of that right though. Otherwise it would be a disaster. "
        " As you were teaching, you couldn't get the thought of the missing student out of your head. "
        " You need answers to what happened. A school should be safe for teachers and students. "
        " A student going missing is just completely worrisome, and it shouldn't go unnoticed. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit. Time for break. "
        " You're gonna have to see what you can do. "
        pause 2.0
        jump twbreak1

label twbreak1:
    scene hallway with dissolve
    " You walked into the hallway and thankfully spotted three of your other teacher friends outside. "
    " Who should you talk to for this break? "
    if emilyknow,demiknow,sashaknow == True:
        menu:
            " {image=missemilyicon} Emily {image=missemilyicon} ":
                jump eminems
            " {image=misterdemiicon} Demi {image=misterdemiicon} ":
                jump demiboy
            " {image=sashaicon} Sasha {image=sashaicon} ":
                jump ilysasha
    elif emilyknow,demiknow == True and sashaknow == False:
        menu:
            " {image=missemilyicon} Emily {image=missemilyicon} ":
                jump eminems
            " {image=misterdemiicon} Demi {image=misterdemiicon} ":
                jump demiboy
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump ilysasha
    elif emilyknow,sashaknow == True and demiknow == False:
        menu:
            " {image=missemilyicon} Emily {image=missemilyicon} ":
                jump eminems
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump demiboy
            " {image=sashaicon} Sasha {image=sashaicon} ":
                jump ilysasha
    elif sashaknow,demiknow == True and emilyknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump eminems
            " {image=misterdemiicon} Demi {image=misterdemiicon} ":
                jump demiboy
            " {image=sashaicon} Sasha {image=sashaicon} ":
                jump ilysasha
    elif emilyknow == True and demiknow,sashaknow == False:
        menu:
            " {image=missemilyicon} Emily {image=missemilyicon} ":
                jump eminems
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump demiboy
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump ilysasha
    elif demiknow == True and emilyknow,sashaknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump eminems
            " {image=misterdemiicon} Demi {image=misterdemiicon} ":
                jump demiboy
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump ilysasha
    elif sashaknow == True and emilyknow,demiknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump eminems
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump demiboy
            " {image=sashaicon} Sasha {image=sashaicon} ":
                jump ilysasha
    else:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump eminems
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump demiboy
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump ilysasha
    label eminems:
        $ emilylv += 10
        " You walked up to the history teacher and saw that she was also putting up posters of the missing student. "
        " You've gotta figure out what's going on here...this isn't normal. "
        show msemilysad at center with easeinleft
        if emilyknow == True:
            mse " Hmm...still no information about them... "
            mse " Come on...where are you...? What happened to you...? "
            mse " I really don't want to give up on them... "
            mse " I know that it's still possible to find them, it has to be... "
            " She doesn't notice you until she turns around to get more posters. "
            hide msemilysad at bottom
            show msemilyneutral at center
            mse " Oh, hello there [name]! "
            mse " I think you've heard about what's been going on recently... "
            mse " The missing student, of course. "
            hide msemilyneutral at bottom
            show msemilysad at center
            mse " Miss Grace has already been informed of the situation by Miss Sasha... "
            mse " I'm trying to do my own work aswell by putting up posters around. "
            mse " And also making posts on facebook. "
            mse " Strangely, their parents aren't responding to me whenever I message them... "
            mse " It's odd, because they're always online! "
            mse " I know that because they contact me often to check on how their kid is doing! "
            mse " God, I'm hoping that this isn't going to be a disaster... "
            mse " I wouldn't want another kid to just... "
            mse " ... "
            hide msemilysad at bottom
            show msemilyneutral at center
            mse " Actually, would you want to help me put some more papers around the school? "
            mse " It would really help a lot. "
            " You wanted to help, so you agreed. "
            hide msemilyneutral at bottom
            show msemilyhappy at center
            mse " That's fantastic, [name]! "
            mse " It's real nice of you to help out! "
            mse " Here, lemme give you some of the posters I have... "
            hide msemilyhappy at bottom
            show msemilyneutral at center
            mse " There's already a few places where I put some posters in, but theres STILL some places that I haven't gone to! "
            mse " Where do ya wanna go? "
            menu:
                " The rooftop ":
                    mse " The rooftop's barely got some walls, but you could put them up somewhere, I know it! "
                    mse " Get going now, we still have a lot to put up! "
                    scene black with dissolve
                    " You went up to the rooftop with some of the posters Miss Emily gave you... "
                    pause 1.0
                    scene rooftop with dissolve
                    " You tried finding a place to put the posters in... "
                    " You ended up sticking them on some of the walls that were there. "
                    " And also put them down on some of the benches. Not sticking them, just putting them down there. "
                    " You also put something to hold them down so that they wouldn't fly away. "
                    " Eventually, you got done with doing the posters for the rooftop. "
                    " Time to help Miss Emily with putting on some more posters. "
                    scene black with dissolve
                    " You spent the rest of the break helping out Emily with the missing person posters. "
                    " While you were doing this, you were thinking where that student could be. "
                    " They could've been taken away...their parents did a stupid decision...or they're just running away to get out of school. "
                    " That last one you could probably see happening, but the parents not responding is just odd. "
                    " Maybe the parents were in on the whole thing? Or something bad happened... "
                    " ...You could only hope that they would be okay. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for you to help someone again. "
                    " You walked back into the hallways with all of the posters posted, and looked around to see who needed help. "
                    pause 2.0
                    jump twclass2
                " The library ":
                    mse " Oooh, the library! "
                    mse " I {i}did{/i} put a few there, but not all of it. "
                    mse " Would be real nice if you put the rest of them! "
                    mse " Get going now, we still have a lot to put up! "
                    scene black with dissolve
                    " You walked over to the library with all of the posters Emily told you to put up... "
                    pause 1.0
                    scene library with dissolve
                    " You were about to ask the librarian if you had permission to post the posters here, buuuut... "
                    " The librarian wasn't exactly there. Huh. Weird... "
                    " You proceeded to post the posters on the walls and everything else though. "
                    " Eventually, you got done with doing the posters for the library. "
                    " Time to help Miss Emily with putting on some more posters. "
                    scene black with dissolve
                    " You spent the rest of the break helping out Emily with the missing person posters. "
                    " While you were doing this, you were thinking where that student could be. "
                    " They could've been taken away...their parents did a stupid decision...or they're just running away to get out of school. "
                    " That last one you could probably see happening, but the parents not responding is just odd. "
                    " Maybe the parents were in on the whole thing? Or something bad happened... "
                    " ...You could only hope that they would be okay. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for you to help someone again. "
                    " You walked back into the hallways with all of the posters posted, and looked around to see who needed help. "
                    pause 2.0
                    jump twclass2
                " The gym ":
                    mse " Ooooh, of course! The gym! "
                    mse " A lot of students usually hang out there to have their lunch... "
                    mse " ...And to have some gossip! Some students might know a thing or two about that kid that went missing! "
                    mse " Get going now, we still have a lot to put up! "
                    scene black with dissolve
                    " You went to the gym, carrying all of the posters Emily asked you to put up there... "
                    pause 1.0
                    scene gym with dissolve
                    " You walked into the gym and found a whole lot of great spots to put the posters in. "
                    " You put the posters in somewhere where it looked noticeable. "
                    " It was VERY much noticeable since the other posters were so colorful and bright...and this one was just so dull. "
                    " A lot of information on just a single poster and while the others are just motivational posters. "
                    " Very eye catching. "
                    " You eventually got done with the posters in the gym. "
                    " Time to help Miss Emily with putting on some more posters. "
                    scene black with dissolve
                    " You spent the rest of the break helping out Emily with the missing person posters. "
                    " While you were doing this, you were thinking where that student could be. "
                    " They could've been taken away...their parents did a stupid decision...or they're just running away to get out of school. "
                    " That last one you could probably see happening, but the parents not responding is just odd. "
                    " Maybe the parents were in on the whole thing? Or something bad happened... "
                    " ...You could only hope that they would be okay. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for you to help someone again. "
                    " You walked back into the hallways with all of the posters posted, and looked around to see who needed help. "
                    pause 2.0
                    jump twclass2
        else:
            x " Hmm...still no information about them... "
            x " Come on...where are you...? What happened to you...? "
            x " I really don't want to give up on them... "
            x " I know that it's still possible to find them, it has to be... "
            " She doesn't notice you until she turns around to get more posters. "
            hide msemilysad at bottom
            show msemilyneutral at center
            x " Oh, hello there [name]! "
            x " Wait, I don't think I've introduced myself to you before...I'm so sorry. "
            $ emilyknow = True
            mse " I'm Miss Emily! I'm the history teacher! It's nice to finally talk to you, hehe... "
            mse " I think you've heard about what's been going on recently... "
            mse " The missing student, of course. "
            hide msemilyneutral at bottom
            show msemilysad at center
            mse " Miss Grace has already been informed of the situation by Miss Sasha... "
            mse " I'm trying to do my own work aswell by putting up posters around. "
            mse " And also making posts on facebook. "
            mse " Strangely, their parents aren't responding to me whenever I message them... "
            mse " It's odd, because they're always online! "
            mse " I know that because they contact me often to check on how their kid is doing! "
            mse " God, I'm hoping that this isn't going to be a disaster... "
            mse " I wouldn't want another kid to just... "
            mse " ... "
            hide msemilysad at bottom
            show msemilyneutral at center
            mse " Actually, would you want to help me put some more papers around the school? "
            mse " It would really help a lot. "
            " You wanted to help, so you agreed. "
            hide msemilyneutral at bottom
            show msemilyhappy at center
            mse " That's fantastic, [name]! "
            mse " It's real nice of you to help out! "
            mse " Here, lemme give you some of the posters I have... "
            hide msemilyhappy at bottom
            show msemilyneutral at center
            mse " There's already a few places where I put some posters in, but theres STILL some places that I haven't gone to! "
            mse " Where do ya wanna go? "
            menu:
                " The rooftop ":
                    mse " The rooftop's barely got some walls, but you could put them up somewhere, I know it! "
                    mse " Get going now, we still have a lot to put up! "
                    scene black with dissolve
                    " You went up to the rooftop with some of the posters Miss Emily gave you... "
                    pause 1.0
                    scene rooftop with dissolve
                    " You tried finding a place to put the posters in... "
                    " You ended up sticking them on some of the walls that were there. "
                    " And also put them down on some of the benches. Not sticking them, just putting them down there. "
                    " You also put something to hold them down so that they wouldn't fly away. "
                    " Eventually, you got done with doing the posters for the rooftop. "
                    " Time to help Miss Emily with putting on some more posters. "
                    scene black with dissolve
                    " You spent the rest of the break helping out Emily with the missing person posters. "
                    " While you were doing this, you were thinking where that student could be. "
                    " They could've been taken away...their parents did a stupid decision...or they're just running away to get out of school. "
                    " That last one you could probably see happening, but the parents not responding is just odd. "
                    " Maybe the parents were in on the whole thing? Or something bad happened... "
                    " ...You could only hope that they would be okay. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for you to help someone again. "
                    " You walked back into the hallways with all of the posters posted, and looked around to see who needed help. "
                    pause 2.0
                    jump twclass2
                " The library ":
                    mse " Oooh, the library! "
                    mse " I {i}did{/i} put a few there, but not all of it. "
                    mse " Would be real nice if you put the rest of them! "
                    mse " Get going now, we still have a lot to put up! "
                    scene black with dissolve
                    " You walked over to the library with all of the posters Emily told you to put up... "
                    pause 1.0
                    scene library with dissolve
                    " You were about to ask the librarian if you had permission to post the posters here, buuuut... "
                    " The librarian wasn't exactly there. Huh. Weird... "
                    " You proceeded to post the posters on the walls and everything else though. "
                    " Eventually, you got done with doing the posters for the library. "
                    " Time to help Miss Emily with putting on some more posters. "
                    scene black with dissolve
                    " You spent the rest of the break helping out Emily with the missing person posters. "
                    " While you were doing this, you were thinking where that student could be. "
                    " They could've been taken away...their parents did a stupid decision...or they're just running away to get out of school. "
                    " That last one you could probably see happening, but the parents not responding is just odd. "
                    " Maybe the parents were in on the whole thing? Or something bad happened... "
                    " ...You could only hope that they would be okay. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for you to help someone again. "
                    " You walked back into the hallways with all of the posters posted, and looked around to see who needed help. "
                    pause 2.0
                    jump twclass2
                " The gym ":
                    mse " Ooooh, of course! The gym! "
                    mse " A lot of students usually hang out there to have their lunch... "
                    mse " ...And to have some gossip! Some students might know a thing or two about that kid that went missing! "
                    mse " Get going now, we still have a lot to put up! "
                    scene black with dissolve
                    " You went to the gym, carrying all of the posters Emily asked you to put up there... "
                    pause 1.0
                    scene gym with dissolve
                    " You walked into the gym and found a whole lot of great spots to put the posters in. "
                    " You put the posters in somewhere where it looked noticeable. "
                    " It was VERY much noticeable since the other posters were so colorful and bright...and this one was just so dull. "
                    " A lot of information on just a single poster and while the others are just motivational posters. "
                    " Very eye catching. "
                    " You eventually got done with the posters in the gym. "
                    " Time to help Miss Emily with putting on some more posters. "
                    scene black with dissolve
                    " You spent the rest of the break helping out Emily with the missing person posters. "
                    " While you were doing this, you were thinking where that student could be. "
                    " They could've been taken away...their parents did a stupid decision...or they're just running away to get out of school. "
                    " That last one you could probably see happening, but the parents not responding is just odd. "
                    " Maybe the parents were in on the whole thing? Or something bad happened... "
                    " ...You could only hope that they would be okay. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for you to help someone again. "
                    " You walked back into the hallways with all of the posters posted, and looked around to see who needed help. "
                    pause 2.0
                    jump twclass2
    label demiboy:
        $ demilv += 10
        " You walked up to the music teacher and he was looking at one of the posters, looking really concerned. "
        " You've gotta figure out what's going on here...this isn't normal. "
        show mrdemineutral at center with easeinright
        if demiknow == True:
            msd " Oh god... I thought the kids were just joking when they said that someone went missing, but... "
            msd " ...This is just horrible...! Who could've done this... "
            msd " Or, maybe the kid ran away...? but what or who would cause that...? "
            msd " Oh god, I hope that I'm not the problem... "
            msd " I've been a good teacher, right...? I haven't been yelling at students at all... "
            msd " I don't want to be the reason why that student is gone... "
            msd " Ouuugh...this is all making my head hurt... "
            " It doesn't take him long for him to realize that you were there after a bit of his rambling session. "
            msd " O-oh! I'm so sorry, [name]... I didn't even notice you... "
            msd " I suppose I was just so caught up in my thoughts that I didn't really catch you there... "
            msd " Sorry if I annoyed you or anything...Hopefully I didn't make you stay there for too long... "
            msd " A-anyway...did you have something to ask me...? "
            " You told him that he was doing fine and that you weren't annoyed... "
            " ...Then you asked if he was doing anything to help spread awareness of the missing kid. "
            msd " That's what I'm trying to figure out right now - what I should do... "
            msd " I mean, Miss Emily's putting on posters...Sasha's already asking around... "
            msd " I don't really know what Circle, Thavel, and Bloomie are doing, actually... "
            msd " They're just walking around and acting as if everything's normal... "
            msd " ...(Hopefully this isn't another one of their cases again)... "
            " ...Maybe he thought that you didn't hear that. "
            " So those three DO have something to do with this. "
            " Looks like it's a reoccuring thing too. The things they do. "
            msd " ...A-anyway, um...do you have any ideas on what I should do...? "
            " You thought for a moment, and then gave your answer. "
            menu:
                " Make posts on facebook if anyone has seen them ":
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " That's actually...pretty great! "
                    msd " I'll just use some of the information that's on the posters... "
                    msd " Uh, do you mind if you read the information outloud for me? "
                    msd " If that's okay with you, of course. "
                    " You gave him a thumbs up before looking at a poster near you and reading the information out loud. "
                    " Hopefully we'll find this kid soon. "
                    scene black with dissolve
                    " You spent the rest of the break telling Demi what to do while making a post to spread awareness. "
                    " You also read outloud the kid's information on the missing person poster of course. "
                    " Just so that people can get an image of what the kid looks like. "
                    " You were really hoping that atleast someone knows where that kid is. "
                    " You thought yesterday was stressful but this is just stressing you out even more now. "
                    " And this is just the start of your day, too... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for you to help someone again. "
                    " You looked around to see who needed help. "
                    pause 2.0
                    jump twclass2
                " Help Emily put up posters ":
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " That...actually doesn't sound too bad! "
                    msd " I'll go help her right away, thanks [name]! "
                    msd " After all, double the help means double thr progress...! Or, uhh... "
                    msd " ...You get what I'm trying to say. "
                    msd " I-I'll see you later! Hey, Ems! Could I help you with that...? "
                    hide mrdemihappy at right with easeoutright
                    " And with that, Mister Demi goes on to Help Miss Emily. "
                    " You could do something while you're here, too... "
                    " ...Probably post something on Facebook about the missing kid. "
                    " Yeah, let's do that. You're gonna have to use the information from the missing person poster though. "
                    " Actually, let's just take a picture of the missing person poster and put in a few words... "
                    " ...About how we're really worried. Hopefully this is gonna catch the attention of parents. "
                    " Facebook IS a place for old people, after all... "
                    scene black with dissolve
                    " You spent the rest of the break making a post for facebook about the missing kid. "
                    " You just hoped this is going to get a lot of views and it'll go a bit viral for the parents. "
                    " And also hoping that someone had last seen the kid. "
                    " You're really hoping that the kid's just going to be fine... "
                    " ...Because the thoughts of what might have happened with the kid are not exactly helping you at this moment. "
                    " Your brain is thinking that something horrible happened to the kid. "
                    " But the kid's going to be fine. You're trusting yourself on this one. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for you to help someone again. "
                    " You looked around to see who needed help. "
                    pause 2.0
                    jump twclass2
                " Help Sasha ask around if anyone's seen the kid ":
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " That...actually doesn't sound too bad! "
                    msd " I'll go help her right away, thanks [name]! "
                    msd " After all, double the help means double thr progress...! Or, uhh... "
                    msd " ...You get what I'm trying to say. "
                    msd " I-I'll see you later! Hey, Sasha! Could I help you with asking around...? "
                    hide mrdemihappy at left with easeoutleft
                    " And with that, Mister Demi goes on to Help Miss Sasha. "
                    " You could do something while you're here, too... "
                    " ...Probably post something on Facebook about the missing kid. "
                    " Yeah, let's do that. You're gonna have to use the information from the missing person poster though. "
                    " Actually, let's just take a picture of the missing person poster and put in a few words... "
                    " ...About how we're really worried. Hopefully this is gonna catch the attention of parents. "
                    " Facebook IS a place for old people, after all... "
                    scene black with dissolve
                    " You spent the rest of the break making a post for facebook about the missing kid. "
                    " You just hoped this is going to get a lot of views and it'll go a bit viral for the parents. "
                    " And also hoping that someone had last seen the kid. "
                    " You're really hoping that the kid's just going to be fine... "
                    " ...Because the thoughts of what might have happened with the kid are not exactly helping you at this moment. "
                    " Your brain is thinking that something horrible happened to the kid. "
                    " But the kid's going to be fine. You're trusting yourself on this one. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for you to help someone again. "
                    " You looked around to see who needed help. "
                    pause 2.0
                    jump twclass2
        else:
            x " Oh god... I thought the kids were just joking when they said that someone went missing, but... "
            x " ...This is just horrible...! Who could've done this... "
            x " Or, maybe the kid ran away...? but what or who would cause that...? "
            x " Oh god, I hope that I'm not the problem... "
            x " I've been a good teacher, right...? I haven't been yelling at students at all... "
            x " I don't want to be the reason why that student is gone... "
            x " Ouuugh...this is all making my head hurt... "
            " It doesn't take him long for him to realize that you were there after a bit of his rambling session. "
            x " O-oh! I'm so sorry, [name]... I didn't even notice you... "
            x " I suppose I was just so caught up in my thoughts that I didn't really catch you there... "
            x " Sorry if I annoyed you or anything...Hopefully I didn't make you stay there for too long... "
            x " Oh, right...! I almost forgot to introduce myself to you...Sorry, again... "
            $ demiknow = True
            msd " I'm Mister Demi...the music teacher...It's really nice to meet you... "
            msd " A-anyway...did you have something to ask me...? "
            " You told him that he was doing fine and that you weren't annoyed... "
            " ...Then you asked if he was doing anything to help spread awareness of the missing kid. "
            msd " That's what I'm trying to figure out right now - what I should do... "
            msd " I mean, Miss Emily's putting on posters...Sasha's already asking around... "
            msd " I don't really know what Circle, Thavel, and Bloomie are doing, actually... "
            msd " They're just walking around and acting as if everything's normal... "
            msd " ...(Hopefully this isn't another one of their cases again)... "
            " ...Maybe he thought that you didn't hear that. "
            " So those three DO have something to do with this. "
            " Looks like it's a reoccuring thing too. The things they do. "
            msd " ...A-anyway, um...do you have any ideas on what I should do...? "
            " You thought for a moment, and then gave your answer. "
            menu:
                " Make posts on facebook if anyone has seen them ":
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " That's actually...pretty great! "
                    msd " I'll just use some of the information that's on the posters... "
                    msd " Uh, do you mind if you read the information outloud for me? "
                    msd " If that's okay with you, of course. "
                    " You gave him a thumbs up before looking at a poster near you and reading the information out loud. "
                    " Hopefully we'll find this kid soon. "
                    scene black with dissolve
                    " You spent the rest of the break telling Demi what to do while making a post to spread awareness. "
                    " You also read outloud the kid's information on the missing person poster of course. "
                    " Just so that people can get an image of what the kid looks like. "
                    " You were really hoping that atleast someone knows where that kid is. "
                    " You thought yesterday was stressful but this is just stressing you out even more now. "
                    " And this is just the start of your day, too... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for you to help someone again. "
                    " You looked around to see who needed help. "
                    pause 2.0
                    jump twclass2
                " Help Emily put up posters ":
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " That...actually doesn't sound too bad! "
                    msd " I'll go help her right away, thanks [name]! "
                    msd " After all, double the help means double thr progress...! Or, uhh... "
                    msd " ...You get what I'm trying to say. "
                    msd " I-I'll see you later! Hey, Ems! Could I help you with that...? "
                    hide mrdemihappy at right with easeoutright
                    " And with that, Mister Demi goes on to Help Miss Emily. "
                    " You could do something while you're here, too... "
                    " ...Probably post something on Facebook about the missing kid. "
                    " Yeah, let's do that. You're gonna have to use the information from the missing person poster though. "
                    " Actually, let's just take a picture of the missing person poster and put in a few words... "
                    " ...About how we're really worried. Hopefully this is gonna catch the attention of parents. "
                    " Facebook IS a place for old people, after all... "
                    scene black with dissolve
                    " You spent the rest of the break making a post for facebook about the missing kid. "
                    " You just hoped this is going to get a lot of views and it'll go a bit viral for the parents. "
                    " And also hoping that someone had last seen the kid. "
                    " You're really hoping that the kid's just going to be fine... "
                    " ...Because the thoughts of what might have happened with the kid are not exactly helping you at this moment. "
                    " Your brain is thinking that something horrible happened to the kid. "
                    " But the kid's going to be fine. You're trusting yourself on this one. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for you to help someone again. "
                    " You looked around to see who needed help. "
                    pause 2.0
                    jump twclass2
                " Help Sasha ask around if anyone's seen the kid ":
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " That...actually doesn't sound too bad! "
                    msd " I'll go help her right away, thanks [name]! "
                    msd " After all, double the help means double thr progress...! Or, uhh... "
                    msd " ...You get what I'm trying to say. "
                    msd " I-I'll see you later! Hey, Sasha! Could I help you with asking around...? "
                    hide mrdemihappy at left with easeoutleft
                    " And with that, Mister Demi goes on to Help Miss Sasha. "
                    " You could do something while you're here, too... "
                    " ...Probably post something on Facebook about the missing kid. "
                    " Yeah, let's do that. You're gonna have to use the information from the missing person poster though. "
                    " Actually, let's just take a picture of the missing person poster and put in a few words... "
                    " ...About how we're really worried. Hopefully this is gonna catch the attention of parents. "
                    " Facebook IS a place for old people, after all... "
                    scene black with dissolve
                    " You spent the rest of the break making a post for facebook about the missing kid. "
                    " You just hoped this is going to get a lot of views and it'll go a bit viral for the parents. "
                    " And also hoping that someone had last seen the kid. "
                    " You're really hoping that the kid's just going to be fine... "
                    " ...Because the thoughts of what might have happened with the kid are not exactly helping you at this moment. "
                    " Your brain is thinking that something horrible happened to the kid. "
                    " But the kid's going to be fine. You're trusting yourself on this one. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for you to help someone again. "
                    " You looked around to see who needed help. "
                    pause 2.0
                    jump twclass2
    label ilysasha:
        $ sashalv += 10
        " You walked up to the art teacher and spotted her asking around with other people if they've seen the student. "
        " You've gotta figure out what's going on here...this isn't normal. "
        show sashasad at center with easeinleft
        if sashaknow == True:
            mss " Good heavens, not even the students know where they're at?! "
            mss " Either they're just that unpopular, or they really don't know! "
            mss " God, this isn't good, isn't good at all! "
            mss " If this is because of Circle, Thavel, or Bloomie, I swear... "
            mss " PLEASE let this be fake...please just tell me that this is all a prank... "
            mss " I'm just a poor teacher who gets underpaid, come onnnn!! " with vpunch
            mss " A kid going missing absolutely breaks my heart, please just tell me this is all some cruel joke!! " with vpunch
            mss " Huuhuuuu... "
            " It took her a bit to notice that you were there, but the moment she noticed... "
            hide sashasad at bottom
            show sashaneutral at center
            " ...It's like her personality had completely changed. "
            mss " Oh, um...hiya, [name]! "
            mss " It's nice to see you here, really... "
            mss " Kind of need a breather after asking everyone where that one student went...! "
            mss " But, I know that I'm gonna have to go back to doing that, soo...hahah... "
            mss " Gotta keep up the grind, you know..! "
            mss " ... "
            hide sashaneutral at bottom
            show sashasad at center
            " And suddenly, she went back to panicking and started shaking you by the shoulders. "
            mss " BUT, REALLY! I'M STRESSING OUT OVER HEREEEE!! " with vpunch
            mss " THE MORE I THINK OF WHAT COULD'VE HAPPENED TO THAT KID, THE MORE I GET WORRIED!! " with vpunch
            mss " AND THE MORE SOMEONE TELLS ME THAT THEY DON'T KNOW WHERE THAT KID IS, THE MORE I GO INSANEEEE!! " with vpunch
            mss " I JUST WANT THAT ONE KID TO BE SAFE AND HAPPY!!! THEY'RE TOO YOUNG TO DIEEEEE!! " with vpunch
            mss " THEY SHOULD'VE ATLEAST FELT HOW HAVING TO PAY TAXES FEELS LIKE!!! " with vpunch
            " She takes a deep breath in, calming herself down. "
            " She let go of your shoulders, though she still looked a little upset over the kid. "
            " It's pretty reasonable, though you did think the whole tax thing was a litte funny. "
            mss " [name]...could you help me ask people where that kid has been...? "
            mss " It would make things way faster and way better... "
            mss " ...Pleeeasseeee.... "
            " You wanted to help, so you agreed. "
            mss " Okay...thank you... "
            mss " I'll go left and you go right...okay? "
            mss " Let's meet up here again when the bell rings... "
            hide sashasad at right with easeoutright
            " Annnd she's gone. "
            " Well, time to get to asking people and stuff. "
            " Let's get to asking! "
            scene black with dissolve
            " You spent the rest of the break asking everyone in the hallway and multiple other places in the school if they've seen the kid. "
            " Though, unfortunately, everyone said that they didn't know where they were. "
            " You could honestly see why Sasha was getting more and more worried about this. "
            " The more you got told that they didn't know where they were, the more you got stressed out. "
            " You had to remind yourself to take a breather every once and awhile cause DAMN you were stressing out. "
            " You were still hoping that atleast someone would say that they knew where they were. "
            " Just keeping that tiny shred of hope in you... "
            play sound "audio/bellring.mp3"
            " The bell rings, and you and Sasha meet up again. "
            " You told her that you found nothing, and Sasha found nothing as well. "
            " This is really just going nowhere... "
            " ...But you weren't gonna give up on them just yet. "
            " You were gonna look into this more after you get done helping someone. "
            " You then looked around if anyone needed help from you... "
            pause 2.0
            jump twclass2
        else:
            x " Good heavens, not even the students know where they're at?! "
            x " Either they're just that unpopular, or they really don't know! "
            x " God, this isn't good, isn't good at all! "
            x " If this is because of Circle, Thavel, or Bloomie, I swear... "
            x " PLEASE let this be fake...please just tell me that this is all a prank... "
            x " I'm just a poor teacher who gets underpaid, come onnnn!! " with vpunch
            x " A kid going missing absolutely breaks my heart, please just tell me this is all some cruel joke!! " with vpunch
            x " Huuhuuuu... "
            " It took her a bit to notice that you were there, but the moment she noticed... "
            hide sashasad at bottom
            show sashaneutral at center
            " ...It's like her personality had completely changed. "
            x " Oh, um...hiya, [name]! "
            x " It's nice to see you here, really... "
            x " Oh, wait! I forgot to introduce myself to you, I'm so sorry! "
            $ sashaknow = True
            mss " I'm Miss Sasha, the art teacher! It's real good to meet ya! "
            mss " Anyway, I kind of need a breather after asking everyone where that one student went...! "
            mss " But, I know that I'm gonna have to go back to doing that, soo...hahah... "
            mss " Gotta keep up the grind, you know..! "
            mss " ... "
            hide sashaneutral at bottom
            show sashasad at center
            " And suddenly, she went back to panicking and started shaking you by the shoulders. "
            mss " BUT, REALLY! I'M STRESSING OUT OVER HEREEEE!! " with vpunch
            mss " THE MORE I THINK OF WHAT COULD'VE HAPPENED TO THAT KID, THE MORE I GET WORRIED!! " with vpunch
            mss " AND THE MORE SOMEONE TELLS ME THAT THEY DON'T KNOW WHERE THAT KID IS, THE MORE I GO INSANEEEE!! " with vpunch
            mss " I JUST WANT THAT ONE KID TO BE SAFE AND HAPPY!!! THEY'RE TOO YOUNG TO DIEEEEE!! " with vpunch
            mss " THEY SHOULD'VE ATLEAST FELT HOW HAVING TO PAY TAXES FEELS LIKE!!! " with vpunch
            " She takes a deep breath in, calming herself down. "
            " She let go of your shoulders, though she still looked a little upset over the kid. "
            " It's pretty reasonable, though you did think the whole tax thing was a litte funny. "
            mss " [name]...could you help me ask people where that kid has been...? "
            mss " It would make things way faster and way better... "
            mss " ...Pleeeasseeee.... "
            " You wanted to help, so you agreed. "
            mss " Okay...thank you... "
            mss " I'll go left and you go right...okay? "
            mss " Let's meet up here again when the bell rings... "
            hide sashasad at right with easeoutright
            " Annnd she's gone. "
            " Well, time to get to asking people and stuff. "
            " Let's get to asking! "
            scene black with dissolve
            " You spent the rest of the break asking everyone in the hallway and multiple other places in the school if they've seen the kid. "
            " Though, unfortunately, everyone said that they didn't know where they were. "
            " You could honestly see why Sasha was getting more and more worried about this. "
            " The more you got told that they didn't know where they were, the more you got stressed out. "
            " You had to remind yourself to take a breather every once and awhile cause DAMN you were stressing out. "
            " You were still hoping that atleast someone would say that they knew where they were. "
            " Just keeping that tiny shred of hope in you... "
            play sound "audio/bellring.mp3"
            " The bell rings, and you and Sasha meet up again. "
            " You told her that you found nothing, and Sasha found nothing as well. "
            " This is really just going nowhere... "
            " ...But you weren't gonna give up on them just yet. "
            " You were gonna look into this more after you get done helping someone. "
            " You then looked around if anyone needed help from you... "
            pause 2.0
            jump twclass2

label twclass2:
    scene hallway with dissolve
    " Who are you gonna help this time? "
    if emilyknow,demiknow,sashaknow == True:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump yellowdiamondlabubu
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump bluediamondlabubu
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump pinkdiamondlabubu
    elif emilyknow,demiknow == True and sashaknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump yellowdiamondlabubu
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump bluediamondlabubu
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump pinkdiamondlabubu
    elif emilyknow,sashaknow == True and demiknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump yellowdiamondlabubu
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump bluediamondlabubu
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump pinkdiamondlabubu
    elif demiknow,sashaknow == True and emilyknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump yellowdiamondlabubu
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump bluediamondlabubu
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump pinkdiamondlabubu
    elif emilyknow == True and demiknow,sashaknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump yellowdiamondlabubu
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump bluediamondlabubu
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump pinkdiamondlabubu
    elif demiknow == True and emilyknow,sashaknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump yellowdiamondlabubu
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump bluediamondlabubu
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump pinkdiamondlabubu
    elif sashaknow == True and emilyknow,demiknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump yellowdiamondlabubu
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump bluediamondlabubu
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump pinkdiamondlabubu
    else:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump yellowdiamondlabubu
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump bluediamondlabubu
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump pinkdiamondlabubu

    label yellowdiamondlabubu:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom and noticed that a bunch of students looked confused. "
        " Looks like the history teacher's a bit confused as well. "
        " Let's see what you can help with here... "
        show msemilyshock at center with easeinright
        if emilyknow == True:
            mse " Okay, now this has to be just a prank. "
            mse " I know you're here right now to help [name], and you have to help us out here... "
            mse " So I told my students to bring in their maps, right? "
            mse " The moment I walk in I see my students being confused. "
            mse " I asked them what was wrong, and they told me that their maps went missing...?? "
            mse " I thought it was a prank at first until one of them called their parents and told them it wasn't at home. "
            mse " This is bamboozling me. Who would want to steal maps? "
            mse " Did they perhaps want to go somewhere??? But even so, why would you need a lot of maps?? "
            mse " I'd get it if they were doing a project, but god... "
            mse " Sigh, could you help me out here, [name]? It would be real nice... "
            mse " ...I don't want to walk around the school after posting so much posters around. "
            mse " We kind of really need those maps for our project for the day. "
            mse " So, if you can, could you help me? "
            " You literally chose this option so that you could help her. "
            " Of course you agreed. "
            hide msemilyshock at bottom
            show msemilyneutral at center
            mse " Thanks, [name]! I really owe you a lot... "
            mse " Maybe try checking in open spaces? "
            mse " Well, there's a lot of open spaces, buuut...uh...You know what, forget what I said! "
            mse " Look anywhere, alright? Come back to me when you find them! "
            mse " Get going, I'm gonna start thinking of what to do to keep my students entertained... "
            scene black with dissolve
            " You spent some of the class hours to find Emily's maps. "
            " You couldn't find any of them anywhere...until you looked in one of the trachcans. "
            " All of them were all ripped up. Huh. Looks like someone didn't want to do an activity. "
            " Understandable. Time to go back to Miss Emily and tell her about what happened... "
            " You know...as a narrator, I feel like this is hinting to something in the story. "
            " What am I talking about? Probably about something that happened earlier. "
            " Anyway, you told Miss Emily about what happened to the maps and she jsut let out a big sigh, "
            " She then told you that she'll come up with a new activity for the kids. "
            " For now, you got to hang out with Emily and the students. "
            " And you also played some cool games with them. "
            " Very nice. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit of hanging out. "
            " You get up from the chair that you were sitting on, and went into the hallways to take a break. "
            pause 2.0
            jump twbreak2
        else:
            x " Okay, now this has to be just a prank. "
            x " I know you're here right now to help [name], and you have to help us out here... "
            x " Oh wait - I didn't introduce myself to you yet, oops. "
            $ emilyknow = True
            mse " I'm Miss Emily, the history teacher. Anyway... "
            mse " So I told my students to bring in their maps, right? "
            mse " The moment I walk in I see my students being confused. "
            mse " I asked them what was wrong, and they told me that their maps went missing...?? "
            mse " I thought it was a prank at first until one of them called their parents and told them it wasn't at home. "
            mse " This is bamboozling me. Who would want to steal maps? "
            mse " Did they perhaps want to go somewhere??? But even so, why would you need a lot of maps?? "
            mse " I'd get it if they were doing a project, but god... "
            mse " Sigh, could you help me out here, [name]? It would be real nice... "
            mse " ...I don't want to walk around the school after posting so much posters around. "
            mse " We kind of really need those maps for our project for the day. "
            mse " So, if you can, could you help me? "
            " You literally chose this option so that you could help her. "
            " Of course you agreed. "
            hide msemilyshock at bottom
            show msemilyneutral at center
            mse " Thanks, [name]! I really owe you a lot... "
            mse " Maybe try checking in open spaces? "
            mse " Well, there's a lot of open spaces, buuut...uh...You know what, forget what I said! "
            mse " Look anywhere, alright? Come back to me when you find them! "
            mse " Get going, I'm gonna start thinking of what to do to keep my students entertained... "
            scene black with dissolve
            " You spent some of the class hours to find Emily's maps. "
            " You couldn't find any of them anywhere...until you looked in one of the trachcans. "
            " All of them were all ripped up. Huh. Looks like someone didn't want to do an activity. "
            " Understandable. Time to go back to Miss Emily and tell her about what happened... "
            " You know...as a narrator, I feel like this is hinting to something in the story. "
            " What am I talking about? Probably about something that happened earlier. "
            " Anyway, you told Miss Emily about what happened to the maps and she jsut let out a big sigh, "
            " She then told you that she'll come up with a new activity for the kids. "
            " For now, you got to hang out with Emily and the students. "
            " And you also played some cool games with them. "
            " Very nice. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit of hanging out. "
            " You get up from the chair that you were sitting on, and went into the hallways to take a break. "
            pause 2.0
            jump twbreak2
    label bluediamondlabubu:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom only to see a rather odd sight. "
        " Students circling around a broken instrument. Specifically a...what's it called again... "
        " A 'Koto'? yeah, that's what it was called. "
        " Looks like someone really didn't like that instrument. "
        " You walked up to the anxious teacher to see if he's doing alright. "
        show mrdemineutral at center with easeinright
        if demiknow == True:
            msd " Oh, um...hey there, [name]... "
            msd " This is...kind of odd, right...? "
            msd " No one really dared to damage the school's instruments like this... "
            msd " ...Well, up until now. "
            msd " I was just teaching my students about music and...instruments, of course... "
            msd " And then suddenly - we heard a loud crash at the back of class! "
            msd " Looked around and checked and saw it was the Koto that got damaged... "
            msd " Luckily, no one got hurt...someone just threw a brick down onto it. "
            msd " Don't know who decided to do that...or why...but it's concerning... "
            msd " I'm gonna have to pay to get this fixed, don't I...? "
            hide mrdemineutral at bottom
            show mrdemisad at center
            msd " Oooough, and I don't have enough moneyyy... "
            msd " I can't exactly just...borrow from my students and other friends... "
            msd " I don't want to bother them like this...not at all... "
            msd " This is going to be a bit tough for me...{nw} "
            hide mrdemisad at bottom
            show mrdemisurprised at center
            " You immediately put your wallet into Mister Demi's hands. "
            msd " ...What?? "
            msd " ...[name]...are you suggesting that I should have your money...? "
            msd " No, no...this isn't right... "
            msd " I really don't want to use your money...that would make me feel bad...! "
            msd " You should use your own money for yourself, not me...! "
            msd " I'm sure I'll be fine anyway... "
            " You did NOT take your wallet out of Mister Demi's hands. "
            " Instead, you kept on insisting that he should have the money. "
            " You're not gonna stop this until he accepts the money. "
            scene black with dissolve
            " You spent the rest of the classtime trying to convince Mister Demi that he should have the money. "
            " This kept on going and going, until he eventually agreed. "
            " Big win, big win! "
            play sound "audio/bellring.mp3"
            " The bell rings, time for another break. "
            " You walked out of Demi's classroom so that you could take a break. "
            pause 2.0
            jump twbreak2
        else:
            x " Oh, um...hey there, [name]... "
            $ demiknow = True
            msd " I'm...I'm Mister Demi, the music teacher... "
            msd " This is...kind of odd, right...? "
            msd " No one really dared to damage the school's instruments like this... "
            msd " ...Well, up until now. "
            msd " I was just teaching my students about music and...instruments, of course... "
            msd " And then suddenly - we heard a loud crash at the back of class! "
            msd " Looked around and checked and saw it was the Koto that got damaged... "
            msd " Luckily, no one got hurt...someone just threw a brick down onto it. "
            msd " Don't know who decided to do that...or why...but it's concerning... "
            msd " I'm gonna have to pay to get this fixed, don't I...? "
            hide mrdemineutral at bottom
            show mrdemisad at center
            msd " Oooough, and I don't have enough moneyyy... "
            msd " I can't exactly just...borrow from my students and other friends... "
            msd " I don't want to bother them like this...not at all... "
            msd " This is going to be a bit tough for me...{nw} "
            hide mrdemisad at bottom
            show mrdemisurprised at center
            " You immediately put your wallet into Mister Demi's hands. "
            msd " ...What?? "
            msd " ...[name]...are you suggesting that I should have your money...? "
            msd " No, no...this isn't right... "
            msd " I really don't want to use your money...that would make me feel bad...! "
            msd " You should use your own money for yourself, not me...! "
            msd " I'm sure I'll be fine anyway... "
            " You did NOT take your wallet out of Mister Demi's hands. "
            " Instead, you kept on insisting that he should have the money. "
            " You're not gonna stop this until he accepts the money. "
            scene black with dissolve
            " You spent the rest of the classtime trying to convince Mister Demi that he should have the money. "
            " This kept on going and going, until he eventually agreed. "
            " Big win, big win! "
            play sound "audio/bellring.mp3"
            " The bell rings, time for another break. "
            " You walked out of Demi's classroom so that you could take a break. "
            pause 2.0
            jump twbreak2
    label pinkdiamondlabubu:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the art teacher's classroom, only to find a very interesting scene. "
        " Looks like the art teacher had just walked in aswell, and she looked as if she was panicking about something... "
        " ...You looked closer, and saw that a bunch of paintings were destroyed. "
        " Jesus, someone must've really not liked art. "
        show sashasad at center with easeinright
        if sashaknow == True:
            mss " Oh goodness - thank god you're here, [name]! "
            mss " I honestly don't know what I should do... "
            mss " You see - I had just walked in to teach my class about paintings... "
            mss " And when I looked at the art corner - all of my students paintings were RIPPED APART!! "
            mss " I know that my students took a lot of time in making those, so I feel HORRIBLE!! "
            mss " I know it's not my fault for this happening but still!! "
            mss " That's a lot of time wasted...!! Huhuuuu... "
            mss " [name], what should I doooo???!! "
            mss " I'm really losing all of my ideas with how I'm being so stressed lately!! "
            mss " First it was that student going missing... "
            mss " Then having to go around and ask people about that kid and trying not to tweak out after they say that they haven't seen them... "
            mss " ...THEN THIS!!! This is just a complete and utter disaster!! "
            mss " WAAAAH, I DIDN'T THINK BEING A TEACHER WOULD SUCK THIS BAD!!! " with vpunch
            mss " I MEAN IT IS FUN BUT NOT WHEN THINGS LIKE THIS ARE HAPPENING!! " with vpunch
            mss " MOM WAS RIGHT, I SHOULD'VE BECOME A DOCTOR!!! " with vpunch
            " ...Sounds like she's stressing out pretty badly. "
            " You told her that everything was going to be fine and you thought about what you could do to fix all of the damage that had been done. "
            " You thought for a long good while...hmmm... "
            " What could fix all of this artwork that had been broken? "
            " You thought for a quick moment before you finally got and idea. "
            " You suggested to her that she should somehow glue everything together to create and abstract painting...thing. "
            " You didn't know if that would help or not, but it was the best you could do. "
            " You just prayed that it would work. "
            hide sashasad at bottom
            show sashaconfused at center
            mss " Hmmm...that... "
            hide sashaconfused at bottom
            show sashahappy at center
            mss " That sounds really good, actually! "
            mss " WHy hadn't I thought about that before?! "
            mss " Thank you so much, [name]! "
            mss " Hey kids - give me some pieces of your artwork and give them to me and [mr] [name]... "
            mss " ...So that we could glue them together and make a whole new painting! "
            mss " Everyone has to participate, this is all worth for 50 points if you do! "
            " Wow, that's an easy 50 points there. "
            " Maybe she doesn't know what she was saying, but that doesn't make her less adorable. "
            " And woah hey, I guess you're gluing stuff together now. "
            " Atleast you've got some work to do for the rest of the class hours. "
            " Time to get gluing! "
            scene black with dissolve
            " You spent the rest of the class hours gluing artwork together with Sasha. "
            " You also got to know a bit more about the students. "
            " Like some of them not really being as good at art as others. "
            " You weren't judging though. You could barely draw a stickman. "
            " We all don't judge you for that. "
            play sound "audio/bellring.mp3"
            " The bell rings right after you finish the entire thing. "
            " You then walked outside of the classroom so that you could take a break. "
            pause 2.0
            jump twbreak2
        else:
            x " Oh goodness - thank god you're here, [name]! "
            $ sashaknow = True
            mss " I'm Miss Sasha, the art teacher, and uh... "
            mss " I honestly don't know what I should do... "
            mss " You see - I had just walked in to teach my class about paintings... "
            mss " And when I looked at the art corner - all of my students paintings were RIPPED APART!! "
            mss " I know that my students took a lot of time in making those, so I feel HORRIBLE!! "
            mss " I know it's not my fault for this happening but still!! "
            mss " That's a lot of time wasted...!! Huhuuuu... "
            mss " [name], what should I doooo???!! "
            mss " I'm really losing all of my ideas with how I'm being so stressed lately!! "
            mss " First it was that student going missing... "
            mss " Then having to go around and ask people about that kid and trying not to tweak out after they say that they haven't seen them... "
            mss " ...THEN THIS!!! This is just a complete and utter disaster!! "
            mss " WAAAAH, I DIDN'T THINK BEING A TEACHER WOULD SUCK THIS BAD!!! " with vpunch
            mss " I MEAN IT IS FUN BUT NOT WHEN THINGS LIKE THIS ARE HAPPENING!! " with vpunch
            mss " MOM WAS RIGHT, I SHOULD'VE BECOME A DOCTOR!!! " with vpunch
            " ...Sounds like she's stressing out pretty badly. "
            " You told her that everything was going to be fine and you thought about what you could do to fix all of the damage that had been done. "
            " You thought for a long good while...hmmm... "
            " What could fix all of this artwork that had been broken? "
            " You thought for a quick moment before you finally got and idea. "
            " You suggested to her that she should somehow glue everything together to create and abstract painting...thing. "
            " You didn't know if that would help or not, but it was the best you could do. "
            " You just prayed that it would work. "
            hide sashasad at bottom
            show sashaconfused at center
            mss " Hmmm...that... "
            hide sashaconfused at bottom
            show sashahappy at center
            mss " That sounds really good, actually! "
            mss " WHy hadn't I thought about that before?! "
            mss " Thank you so much, [name]! "
            mss " Hey kids - give me some pieces of your artwork and give them to me and [mr] [name]... "
            mss " ...So that we could glue them together and make a whole new painting! "
            mss " Everyone has to participate, this is all worth for 50 points if you do! "
            " Wow, that's an easy 50 points there. "
            " Maybe she doesn't know what she was saying, but that doesn't make her less adorable. "
            " And woah hey, I guess you're gluing stuff together now. "
            " Atleast you've got some work to do for the rest of the class hours. "
            " Time to get gluing! "
            scene black with dissolve
            " You spent the rest of the class hours gluing artwork together with Sasha. "
            " You also got to know a bit more about the students. "
            " Like some of them not really being as good at art as others. "
            " You weren't judging though. You could barely draw a stickman. "
            " We all don't judge you for that. "
            play sound "audio/bellring.mp3"
            " The bell rings right after you finish the entire thing. "
            " You then walked outside of the classroom so that you could take a break. "
            pause 2.0
            jump twbreak2
label twbreak2:
    scene hallway with dissolve
    " You walked into the hallway and saw a bizzare sight. "
    " Some of the posters were scratched down... "
    " ...Who could've done this? You swear that no one was allowed to leave the classrooms during class hours... "
    " You're sure it was either a student or a teacher. "
    " The more you're seeing weird stuff happen, the more you feel concerned. "
    " You have a feeling that whoever did this was the one who got the student missing in the first place... "
    " ...But again, this is just your thoughts speaking, not the truth. "
    " We still need to figure out what TRULY happened. "
    " But we can't figure things out if no one's being cooperative. "
    " ... "
    " You're going to have to take a breather for just this break. "
    " Instead of walking around, let's just...hang out in your classroom for a bit. "
    " This is getting pretty stressful, even for you. "
    " God damn it. "
    scene black with dissolve
    " You spent the rest of the break in your classroom all alone, thinking about what you could do. "
    " You very badly wanted to know what happened to the kid. You wanted to know if they were okay or not. "
    " You were very much hoping that they were okay, but the thoughts of them not being alright is haunting you. "
    " Most teachers probably would've ignored it, students probably wouldn't have cared, but... "
    " Doing all of that just doesn't sit right with you. No way. "
    " That kid should've atleast been remembered as a person, not just as a nobody. "
    " Everyone should be remembered. "
    play sound "audio/bellring.mp3"
    " The bell rings, getting you out of your deep thoughts. "
    " Time to help someone else, then... "
    " You get up from your chair and walked back into the hallways to see if someone needed help. "
    pause 2.0
    jump twclass3

label twclass3:
    scene hallway with dissolve
    " Who would you like to help for now? "
    if circleknow,thavelknow,bloomieknow == True:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump adventuretimeyuri
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump stevenuniverseyuri
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump lumityyuri
    elif circleknow,thavelknow == True and bloomieknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump adventuretimeyuri
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump stevenuniverseyuri
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump lumityyuri
    elif circleknow,bloomieknow == True and thavelknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump adventuretimeyuri
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump stevenuniverseyuri
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump lumityyuri
    elif thavelknow,bloomieknow == True and circleknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump adventuretimeyuri
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump stevenuniverseyuri
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump lumityyuri
    elif circleknow == True and thavelknow,bloomieknow == False:
        menu:
            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                jump adventuretimeyuri
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump stevenuniverseyuri
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump lumityyuri
    elif thavelknow == True and circleknow,bloomieknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump adventuretimeyuri
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump stevenuniverseyuri
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump lumityyuri
    elif bloomieknow == True and circleknow,thavelknow == False:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump adventuretimeyuri
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump stevenuniverseyuri
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump lumityyuri
    else:
        menu:
            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                jump adventuretimeyuri
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump stevenuniverseyuri
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump lumityyuri
    label adventuretimeyuri:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom only to realize that it was completely empty. "
        " No students talking, no students writing, no nothing. "
        " You looked around, trying to find the math teacher... "
        " And she eventually pops out of her office. "
        " Wait... "
        " What's that stain on her pants? "
        show misscircleneutral at center with easeinleft
        if circleknow == True:
            msc " Hmhmhmmmm...I should probably make new math equations for my students. "
            msc " That way, their grades would have a boost! "
            msc " They've been doing horribly lately, after all... "
            msc " Hmhmhm...Also gotta arrange stuff here... "
            " It took her a bit to notice you, but she eventually did. "
            msc " Hey there [name]! It's nice to see you. "
            msc " Why my classroom is empty? well... "
            msc " Miss Grace told me that I {i}may{/i} need to pause some of my classes to figure out what's going on. "
            msc " Gives us more time to investigate on what's going on, you get me? "
            msc " I know this just gives the students more time to do stupid things, but don't worry! "
            msc " I made sure to give them a nice little activity before they went out. "
            msc " That activity is worth 100 points, so surely they wouldn't want to miss out on that! "
            msc " Now, I'm sure you needed something if you came in here. "
            msc " What is it? Got a question for me? Or did you need to tell me something? "
            " You told her that you were originally just going to check in with her... "
            " ...But now you have two questions that concern you by a lot. "
            msc " Oooh, so I was right! Let me hear it then! "
            msc " Don't worry - you can ask me any question! If it's about the school, I can give you all the info I need! "
            msc " Where rooms are...what rules there areee... everything! "
            " You told her that you would love to learn all of that sometime. "
            " But first, you asked her what's that one stain she had on her pants. "
            hide misscircleneutral at bottom
            show misscircleangry at center
            msc " ...This thing? "
            " Woah, she looks...pretty mad when you mentioned that. "
            " That was pretty concerning. "
            hide misscircleangry at bottom
            show misscircleneutral at center
            " Though, when she realizes what tone she just used, she switches back. "
            msc " That's just a little stain from the burger that I ate! "
            msc " You see, I bought a hamburger from the cafeteria, right? "
            msc " When I took a bite of it...you know how sometimes when you bite into them the filling kinda just... "
            msc " Gets pushed back, causing some of it to spill out? "
            msc " Pretty annoying when it happens, but it usually means that they added too much filling. "
            msc " In my case, it's ketchup! "
            msc " Hold on. Wait. "
            hide misscircleneutral at bottom
            show misscirclesad at center
            msc " Siiighhh...my white pants...now I see why you're concerned. "
            msc " I'll just clean this thoroughly later... "
            hide misscirclesad at bottom
            show misscircleneutral at center
            msc " Anyway! You said you had another question for me? "
            " You nodded, then asked her about how it's going with Miss Grace and the investigation. "
            " You were praying that there was at least some good news for you. "
            msc " Ooooh, the investigation? "
            msc " Unfortunately nothing good, sorry... "
            msc " I know that you know that we're all trying our best though! "
            scene black with dissolve
            " You spent the rest of the class hours talking with Miss Circle about the situation going on. "
            " The more you talk to her...the more you're starting to think that she's somehow connected to what happened. "
            " It's just a feeling from your gut, but of course, just a feeling - not a fact. "
            " She looks like such a nice person who wouldn't do such a thing to a student... "
            " ... "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for a break. "
            " You got out of Circle's classroom and you walked into the hallways. "
            pause 2.0
            jump twbreak3
        else:
            x " Hmhmhmmmm...I should probably make new math equations for my students. "
            x " That way, their grades would have a boost! "
            x " They've been doing horribly lately, after all... "
            x " Hmhmhm...Also gotta arrange stuff here... "
            " It took her a bit to notice you, but she eventually did. "
            x " Hey there [name]! It's nice to see you. "
            x " Oooh, I haven't introduced myself to you yet! So sorry about that. "
            $ circleknow = True
            msc " I'm Miss Circle, the math teacher! Real nice to finally talk to you! "
            msc " Anyway...What was I gonna say again...? "
            msc " Hmmm...oh! "
            msc " Why my classroom is empty? well... "
            msc " Miss Grace told me that I {i}may{/i} need to pause some of my classes to figure out what's going on. "
            msc " Gives us more time to investigate on what's going on, you get me? "
            msc " I know this just gives the students more time to do stupid things, but don't worry! "
            msc " I made sure to give them a nice little activity before they went out. "
            msc " That activity is worth 100 points, so surely they wouldn't want to miss out on that! "
            msc " Now, I'm sure you needed something if you came in here. "
            msc " What is it? Got a question for me? Or did you need to tell me something? "
            " You told her that you were originally just going to check in with her... "
            " ...But now you have two questions that concern you by a lot. "
            msc " Oooh, so I was right! Let me hear it then! "
            msc " Don't worry - you can ask me any question! If it's about the school, I can give you all the info I need! "
            msc " Where rooms are...what rules there areee... everything! "
            " You told her that you would love to learn all of that sometime. "
            " But first, you asked her what's that one stain she had on her pants. "
            hide misscircleneutral at bottom
            show misscircleangry at center
            msc " ...This thing? "
            " Woah, she looks...pretty mad when you mentioned that. "
            " That was pretty concerning. "
            hide misscircleangry at bottom
            show misscircleneutral at center
            " Though, when she realizes what tone she just used, she switches back. "
            msc " That's just a little stain from the burger that I ate! "
            msc " You see, I bought a hamburger from the cafeteria, right? "
            msc " When I took a bite of it...you know how sometimes when you bite into them the filling kinda just... "
            msc " Gets pushed back, causing some of it to spill out? "
            msc " Pretty annoying when it happens, but it usually means that they added too much filling. "
            msc " In my case, it's ketchup! "
            msc " Hold on. Wait. "
            hide misscircleneutral at bottom
            show misscirclesad at center
            msc " Siiighhh...my white pants...now I see why you're concerned. "
            msc " I'll just clean this thoroughly later... "
            hide misscirclesad at bottom
            show misscircleneutral at center
            msc " Anyway! You said you had another question for me? "
            " You nodded, then asked her about how it's going with Miss Grace and the investigation. "
            " You were praying that there was at least some good news for you. "
            msc " Ooooh, the investigation? "
            msc " Unfortunately nothing good, sorry... "
            msc " I know that you know that we're all trying our best though! "
            scene black with dissolve
            " You spent the rest of the class hours talking with Miss Circle about the situation going on. "
            " The more you talk to her...the more you're starting to think that she's somehow connected to what happened. "
            " It's just a feeling from your gut, but of course, just a feeling - not a fact. "
            " She looks like such a nice person who wouldn't do such a thing to a student... "
            " ... "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for a break. "
            " You got out of Circle's classroom and you walked into the hallways. "
            pause 2.0
            jump twbreak3
    label stevenuniverseyuri:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the language teacher's classroom only to find it to be empty. "
        " You were sure that they would be doing a discussion right now... "
        " Like teaching students how to use duolingo. Oh wait, that app is controversial now, oops. "
        " Like actually teaching students how to actually learn a language is what I meant. "
        " You looked around, trying to find the teacher... "
        " ...And eventually, she pops out from doing stuff underneath her desk. "
        " Wonder what she was doing - wait, hold on. "
        " You swear you just saw her with deer horns on. They quickly disappeared before you could make sure of what you were seeing. "
        " That's really odd... "
        show msthravelneutral at center with easeinbottom
        if thavelknow == True:
            mst " Alright, got that done... "
            mst " Now I just have to move some boxes here and there to make some space for newer things! "
            mst " I should get some more decorations so that things look good in here... "
            mst " And some pictures of what I'm teaching about, of course! "
            mst " Can't forget about all of that...I'm gonna have to write all of that down. "
            mst " Let me just grab some paper, and... "
            " She was about to go and grab some paper, but then she spots you. "
            mst " Oh heya there, [name]! "
            mst " It's real nice to see you here! Was there something that you needed from me? "
            mst " Or maybe a question about something? "
            mst " Oh, were you gonna ask why I'm not having my class at the moment? "
            mst " It's because...Miss Grace is giving me this time to find some stuff about what's going on! "
            mst " Like more information of what happened to that student, you know? "
            mst " And right now, I'm trying to clean things up around my room so that I might find things that's hidden in my room! "
            mst " See what I'm getting at here? "
            mst " Once I'm done checking in my room, I'm going to check outside! "
            mst " Pretty good plan, right? The only problem is if I don't find anything... "
            mst " God, I'm gonna get yelled at later... "
            " You told her that what she was doing was pretty smart, but then you had another question. "
            " What was with those deer horns that she had on just a few seconds. "
            hide msthravelneutral at bottom
            show msthravelangry at center
            mst " ...{b}{i}What.{/i}{/b} "
            " Woah, she's mad. You didn't even say anything wrong, you were just asking about the horns... "
            " Maybe the horns are a sore topic for her? "
            " Yeah, maybe you shouldn't have asked her about that... "
            " ...She looks like she would go driving on her car right after a beer and run over you right now. "
            " You said sorry and only said that you were curious. "
            hide msthravelangry at bottom
            show msthravelneutral at center
            " After you said that, she stares you for a bit longer before going back to normal. "
            " You could've sworn you saw something on her head rustling... "
            " Probably just you seeing things again, or were you? "
            mst " ...Oooooh! You must've thought that I was putting on a costume or something."
            mst " Because I don't have deer horns, silly. "
            mst " It msut've been your imagination tricking you. "
            mst " Your imagination is a wild one, [name]! "
            " ...Huh. "
            " You then asked her about how things are going with Miss Grace. "
            mst " We haven't found anything yet, unfortunately... "
            mst " We're going to find them soon, trust me [name]! "
            mst " Everything's going to be fine. "
            " You hope so. "
            scene black with dissolve
            " You spent the rest of the break talking with Miss Thavel. "
            " The more you talk to her...the more you're starting to think that she's somehow connected to what happened. "
            " It's just a feeling from your gut, but of course, just a feeling - not a fact. "
            " She looks like such a nice person who wouldn't do such a thing to a student... "
            " ... "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for a break. "
            " You got out of Thavel's classroom and you walked into the hallways. "
            pause 2.0
            jump twbreak3
        else:
            x " Alright, got that done... "
            x " Now I just have to move some boxes here and there to make some space for newer things! "
            x " I should get some more decorations so that things look good in here... "
            x " And some pictures of what I'm teaching about, of course! "
            x " Can't forget about all of that...I'm gonna have to write all of that down. "
            x " Let me just grab some paper, and... "
            " She was about to go and grab some paper, but then she spots you. "
            x " Oh heya there, [name]! "
            x " Wait, I haven't even introduced myself to you yet. Geez, how can I be this forgetful? So sorry! "
            $ thavelknow = True
            mst " I'm Miss Thavel - The language teacher! "
            mst " It's real nice to see you here! Was there something that you needed from me? "
            mst " Or maybe a question about something? "
            mst " Oh, were you gonna ask why I'm not having my class at the moment? "
            mst " It's because...Miss Grace is giving me this time to find some stuff about what's going on! "
            mst " Like more information of what happened to that student, you know? "
            mst " And right now, I'm trying to clean things up around my room so that I might find things that's hidden in my room! "
            mst " See what I'm getting at here? "
            mst " Once I'm done checking in my room, I'm going to check outside! "
            mst " Pretty good plan, right? The only problem is if I don't find anything... "
            mst " God, I'm gonna get yelled at later... "
            " You told her that what she was doing was pretty smart, but then you had another question. "
            " What was with those deer horns that she had on just a few seconds. "
            hide msthravelneutral at bottom
            show msthravelangry at center
            mst " ...{b}{i}What.{/i}{/b} "
            " Woah, she's mad. You didn't even say anything wrong, you were just asking about the horns... "
            " Maybe the horns are a sore topic for her? "
            " Yeah, maybe you shouldn't have asked her about that... "
            " ...She looks like she would go driving on her car right after a beer and run over you right now. "
            " You said sorry and only said that you were curious. "
            hide msthravelangry at bottom
            show msthravelneutral at center
            " After you said that, she stares you for a bit longer before going back to normal. "
            " You could've sworn you saw something on her head rustling... "
            " Probably just you seeing things again, or were you? "
            mst " ...Oooooh! You must've thought that I was putting on a costume or something."
            mst " Because I don't have deer horns, silly. "
            mst " It msut've been your imagination tricking you. "
            mst " Your imagination is a wild one, [name]! "
            " ...Huh. "
            " You then asked her about how things are going with Miss Grace. "
            mst " We haven't found anything yet, unfortunately... "
            mst " We're going to find them soon, trust me [name]! "
            mst " Everything's going to be fine. "
            " You hope so. "
            scene black with dissolve
            " You spent the rest of the break talking with Miss Thavel. "
            " The more you talk to her...the more you're starting to think that she's somehow connected to what happened. "
            " It's just a feeling from your gut, but of course, just a feeling - not a fact. "
            " She looks like such a nice person who wouldn't do such a thing to a student... "
            " ... "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for a break. "
            " You got out of Thavel's classroom and you walked into the hallways. "
            pause 2.0
            jump twbreak3
    label lumityyuri:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the science teacher's classroom and...saw nothing. "
        " No students, only silence. Where is teacher? "
        " You looked around for a bit in the classroom and eventually spotted the teacher all the way in the back... "
        " ...Cleaning her box cutter of an arm. Wonder why... "
        " You took a look closer, and...what's that weird red stain on her arm? "
        show missbloomieneutral at center with easeinleft
        if bloomieknow == True:
            msb " ... "
            msb " ...Helping them was a waste of time... "
            msb " Now I've got all this on my arm... "
            msb " ...But then again, no one was choosing to help them, so... "
            msb " ... "
            " She eventually gets done with cleaning her arm, and notices you. "
            " She quickly skedaddles up to you to see what you were up to. "
            msb " ...[name]. Hello there. "
            msb " Did you need something from me? "
            msb " Any questions? "
            msb " ...Perhaps why I don't have my class right now. "
            msb " It's because Miss Grace is giving me this time to figure out some things about the situation that's been going on. "
            msb " I've been checking around the hallways and all of the corners of the school. "
            msb " I'm pretty sure Miss Sasha wasn't checking hard enough earlier when she was looking all over the school. "
            msb " That's why I'm assisting in her looking for some sort of sign of where the student went. "
            msb " Everyone is trying their best to figure out what's been going on. "
            msb " Though things aren't looking good right now, I'm sure that things will look better tomorrow. "
            msb " Trust me. "
            " You told her that you hoped everything will go well and that the kid would be alright. "
            " You then had a question for her... "
            " What was that strange red liquid on her box cutter of an arm? "
            msb " ... "
            " You swore you saw her eye twitch when you mention that. "
            " Actually, yeah. Her eye just twitched again. "
            msb " ...Oh, that? "
            msb " Let me explain something here... "
            msb " I was just walking around during break time, and Miss Circle wanted some help in the cafeteria. "
            msb " Turns out the ketchup bottle wasn't working and she just wanted ketchup on her burger. "
            msb " I tried opening it, but it really didn't open no matter what I did. "
            msb " I eventually got frustrated and used my box cutter hand to open the ketchup bottle. "
            msb " I got some of the ketchup on my hand, and now I had to clean it. "
            " ...Huh. "
            " You then asked her about how it's going with Miss Grace. "
            msb " We haven't found anything yet, unfortunately. "
            msb " I'm sure we can find something, [name]. "
            msb " The fact that you care about this kid so much is...sweet. "
            msb " Hopefully we can find them. It would be better if it was soon."
            " Hopefully. "
            scene black with dissolve
            " You spent the rest of the break talking with Miss Bloomie. "
            " The more you talk to her...the more you're starting to think that she's somehow connected to what happened. "
            " It's just a feeling from your gut, but of course, just a feeling - not a fact. "
            " She looks like such a nice person who wouldn't do such a thing to a student... "
            " ... "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for a break. "
            " You got out of Bloomie's classroom and you walked into the hallways. "
            pause 2.0
            jump twbreak3
        else:
            x " ... "
            x " ...Helping them was a waste of time... "
            x " Now I've got all this on my arm... "
            x " ...But then again, no one was choosing to help them, so... "
            x " ... "
            " She eventually gets done with cleaning her arm, and notices you. "
            " She quickly skedaddles up to you to see what you were up to. "
            x " ...[name]. Hello there. "
            $ bloomieknow = True
            msb " I'm Miss Bloomie. The science teacher. "
            msb " Did you need something from me? "
            msb " Any questions? "
            msb " ...Perhaps why I don't have my class right now. "
            msb " It's because Miss Grace is giving me this time to figure out some things about the situation that's been going on. "
            msb " I've been checking around the hallways and all of the corners of the school. "
            msb " I'm pretty sure Miss Sasha wasn't checking hard enough earlier when she was looking all over the school. "
            msb " That's why I'm assisting in her looking for some sort of sign of where the student went. "
            msb " Everyone is trying their best to figure out what's been going on. "
            msb " Though things aren't looking good right now, I'm sure that things will look better tomorrow. "
            msb " Trust me. "
            " You told her that you hoped everything will go well and that the kid would be alright. "
            " You then had a question for her... "
            " What was that strange red liquid on her box cutter of an arm? "
            msb " ... "
            " You swore you saw her eye twitch when you mention that. "
            " Actually, yeah. Her eye just twitched again. "
            msb " ...Oh, that? "
            msb " Let me explain something here... "
            msb " I was just walking around during break time, and Miss Circle wanted some help in the cafeteria. "
            msb " Turns out the ketchup bottle wasn't working and she just wanted ketchup on her burger. "
            msb " I tried opening it, but it really didn't open no matter what I did. "
            msb " I eventually got frustrated and used my box cutter hand to open the ketchup bottle. "
            msb " I got some of the ketchup on my hand, and now I had to clean it. "
            " ...Huh. "
            " You then asked her about how it's going with Miss Grace. "
            msb " We haven't found anything yet, unfortunately. "
            msb " I'm sure we can find something, [name]. "
            msb " The fact that you care about this kid so much is...sweet. "
            msb " Hopefully we can find them. It would be better if it was soon."
            " Hopefully. "
            scene black with dissolve
            " You spent the rest of the break talking with Miss Bloomie. "
            " The more you talk to her...the more you're starting to think that she's somehow connected to what happened. "
            " It's just a feeling from your gut, but of course, just a feeling - not a fact. "
            " She looks like such a nice person who wouldn't do such a thing to a student... "
            " ... "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for a break. "
            " You got out of Bloomie's classroom and you walked into the hallways. "
            pause 2.0
            jump twbreak3

label twbreak3:
    scene hallway with dissolve
    " You walked into the hallway and overheard more students talking about the situation. "
    " While it's a good thing that they're finally aware of what's been going on, that's not what's concerning you about why they're talking about them. "
    " The thing that's concerning you is the fact that they don't even know who that student was. "
    scene black with dissolve
    " You overheard people asking eachother who that student was and if they were even in this school or not. "
    " It scares you to think that you could be so unknown to the point that no one would know who you were... "
    " Not even remembering you, and only wondering where you were the moment that you're actually gone. "
    " You're just left there in the dark with no one by your side. "
    " Now that you think more about the situation, you wondered if that kid even have any friends. "
    " If not, then that's just...sad. "
    " Surely they could've had someone, right? "
    " There's just no way that someone would have no friends. "
    " ...They really didn't have anyone to care about them, did they? "
    " Sigh...you've gotta find this kid quick. "
    " Another thing what you fear most is that they're just going to act as if everything's normal. "
    " That nothing even happened. That they didn't disappear. "
    " Just a normal tuesday, and nothing else. "
    " The thought of that happening to you yourself is terrifying. "
    " Just left alone to rot. No one looking for you and no one caring for you. "
    " Not even your own parents...okay sorry to break the emotional moment but the creator really put a lot of thought into this part "
    " Anyway...you pulled out your phone and decided to make a facebook post about the missing kid for the break. "
    " Hopefully atleast someone would respond to your post. "
    " Hopefully. You don't want someone to die young and forgotten. "
    " ...But don't we all get forgotten at some point? "
    " No, you can't be thinking about that. We've got to atleast get some hope. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit of you waiting for someone to respond to your post. "
    " Unfortunately, no one replied to your post at all. It did get views, yes, but no one bothered to comment. "
    " This is just so odd... "
    " Time to look around for people you can help, then. "
    pause 2.0
    jump twclass4

label twclass4:
    scene hallway with dissolve
    " Who would you want to help for now? "
    if emilyknow,demiknow,sashaknow == True:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump hundredgfs
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump hundredbfs
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump hundredpartners
    elif emilyknow,demiknow == True and sashaknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump hundredgfs
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump hundredbfs
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump hundredpartners
    elif emilyknow,sashaknow == True and demiknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump hundredgfs
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump hundredbfs
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump hundredpartners
    elif demiknow,sashaknow == True and emilyknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump hundredgfs
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump hundredbfs
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump hundredpartners
    elif emilyknow == True and demiknow,sashaknow == False:
        menu:
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump hundredgfs
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump hundredbfs
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump hundredpartners
    elif demiknow == True and emilyknow,sashaknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump hundredgfs
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump hundredbfs
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump hundredpartners
    elif sashaknow == True and emilyknow,demiknow == False:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump hundredgfs
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump hundredbfs
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump hundredpartners
    else:
        menu:
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump hundredgfs
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump hundredbfs
            " {image=sashaicon} The art teacher {image=sashaicon} ":
                jump hundredpartners
    label hundredgfs:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom...seems like they're having an activity right now. "
        " You looked around to try and find the history teacher, and found her at the corner on a call with someone. "
        " You slowly and secretly walked over to her to check on what she was talking about. "
        show msemilysad at center with easeinleft
        if emilyknow == True:
            mse " ...Yes, Miss Grace... "
            mse " ...We've found nothing so far... "
            mse " ...Yes, Miss Grace... "
            mse " ...Okay...I'll see you later... "
            " The phone call ends and you could hear Miss Emily sigh deeply. "
            hide msemilysad at bottom
            show msemilyneutral at center
            " She turns around and gets startled by your presence, since she didn't notice you. "
            mse " O-OH! [name], I didn't know that you're here... "
            mse " How long have you been standing there? Hopefully I didn't keep you waiting... "
            " You told her that you just arrived, and asked her what she was talking about with Miss Grace. "
            " You can't tell me that you weren't curious with what she was talking about with Miss Grace. "
            mse " Oh? what I was talking about? "
            hide msemilyneutral at bottom
            show msemilysad at center
            mse " Well, it's about the situation that's been happening recently... "
            mse " Miss Grace has given me some orders to do so that we can find the student faster. "
            mse " Spread word everywhere and ask questions to people... "
            mse " Every teacher's going to be a part of this, and you were supposed to be included, buuut... "
            mse " Miss Grace saw how much you were stressing yourself over this kid. "
            mse " She found it sweet, but you don't have to overstress about what happened. "
            mse " School's going to be cut off for the rest of the day. Me and the other teachers will handle the situation for now. "
            mse " All you can do is ask around online if anyone's seen them... "
            mse " Miss Grace said that school's going to be cut off due to the recent suspicious things that's been happening. "
            mse " I mean, students HAVE gotten missing, but right now...things have been getting way too shady. "
            mse " School ends after your class, alright? I'll tell you if we find anything. "
            scene black with dissolve
            " You spent the rest of the break talking with Miss Emily. "
            " ...Huh. So you basically had the rest of the afternoon to yourself. "
            " You're gonna use that time to spread more awareness of the missing student for sure. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, time for another break. "
            " After this break, it's gonna be your class. "
            " And after your class, you're gonna go home. "
            pause 2.0
            jump twbreak4
        else:
            x " ...Yes, Miss Grace... "
            x " ...We've found nothing so far... "
            x " ...Yes, Miss Grace... "
            x " ...Okay...I'll see you later... "
            " The phone call ends and you could hear Miss Emily sigh deeply. "
            hide msemilysad at bottom
            show msemilyneutral at center
            " She turns around and gets startled by your presence, since she didn't notice you. "
            x " O-OH! [name], I didn't know that you're here... "
            x " How long have you been standing there? Hopefully I didn't keep you waiting... "
            $ emilyknow = True
            mse " Oh - uh...I'm Miss Emily by the way. History teacher. "
            " You told her that you just arrived, and asked her what she was talking about with Miss Grace. "
            " You can't tell me that you weren't curious with what she was talking about with Miss Grace. "
            mse " Oh? what I was talking about? "
            hide msemilyneutral at bottom
            show msemilysad at center
            mse " Well, it's about the situation that's been happening recently... "
            mse " Miss Grace has given me some orders to do so that we can find the student faster. "
            mse " Spread word everywhere and ask questions to people... "
            mse " Every teacher's going to be a part of this, and you were supposed to be included, buuut... "
            mse " Miss Grace saw how much you were stressing yourself over this kid. "
            mse " She found it sweet, but you don't have to overstress about what happened. "
            mse " School's going to be cut off for the rest of the day. Me and the other teachers will handle the situation for now. "
            mse " All you can do is ask around online if anyone's seen them... "
            mse " Miss Grace said that school's going to be cut off due to the recent suspicious things that's been happening. "
            mse " I mean, students HAVE gotten missing, but right now...things have been getting way too shady. "
            mse " School ends after your class, alright? I'll tell you if we find anything. "
            scene black with dissolve
            " You spent the rest of the break talking with Miss Emily. "
            " ...Huh. So you basically had the rest of the afternoon to yourself. "
            " You're gonna use that time to spread more awareness of the missing student for sure. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, time for another break. "
            " After this break, it's gonna be your class. "
            " And after your class, you're gonna go home. "
            pause 2.0
            jump twbreak4
    label hundredbfs:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom and it looked like all the students were doing their activities. "
        " You tried to find where the music teacher was... "
        " ...And found him in the corner, on a call with someone. "
        " Being the nosy person you were, you decided to check out who he was talking to and what he was talking about. "
        show mrdemineutral at center with easeinleft
        if demiknow == True:
            msd " ... "
            msd " ...Okay... "
            msd " ...I'll tell [them] about it once I see [them]... "
            msd " ...See you later, Grace... "
            " He ends the call, and turns around to check on his students... "
            hide mrdemineutral at bottom
            show mrdemisurprised at center
            " Only to get jumpscared by you, who was standing right behind him. "
            " You didn't inform him that you were there, so of course he would get surprised. "
            msd " Eek! " with vpunch
            hide mrdemisurprised at bottom
            show mrdemineutral at center
            msd " Whhh...hooo... It's just you, [name]... "
            msd " I hope I didn't keep you waiting for too long... "
            " You told him that you just arrived, and asked him what he was talking about with Miss Grace. "
            " You can't tell me that you weren't curious with what he was talking about with Miss Grace. "
            msd " What I was talking about with Miss Grace...? Gee, you're that curious... "
            msd " If you really want to know, then... "
            msd " It's about the situation that's been happening recently... "
            msd " Miss Grace has given me some orders to do so that we can find the student faster. "
            msd " Spread word everywhere and ask questions to people... "
            msd " ...Every teacher's going to be a part of this, and you were supposed to be included, buuut... "
            msd " ...Miss Grace saw how much you were stressing yourself over this student... "
            msd " ...S-she found it sweet, but you don't have to overstress about what happened. "
            msd " ...And also... School's going to be cut off for the rest of the day. Me and the other teachers will handle the situation for now. "
            msd " ...All you can do is ask around online if anyone's seen them... "
            msd " ...Miss Grace said that school's going to be cut off due to the recent suspicious things that's been happening. "
            msd "... I-I mean, students HAVE gotten missing, but right now...things have been getting way too shady. "
            msd " ...School ends after your class, alright...? I'll tell you if we find anything... "
            scene black with dissolve
            " You spent the rest of the break talking with Mister Demi. "
            " ...Huh. So you basically had the rest of the afternoon to yourself. "
            " You're gonna use that time to spread more awareness of the missing student for sure. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, time for another break. "
            " After this break, it's gonna be your class. "
            " And after your class, you're gonna go home. "
            pause 2.0
            jump twbreak4
        else:
            x " ... "
            x " ...Okay... "
            x " ...I'll tell [them] about it once I see [them]... "
            x " ...See you later, Grace... "
            " He ends the call, and turns around to check on his students... "
            hide mrdemineutral at bottom
            show mrdemisurprised at center
            " Only to get jumpscared by you, who was standing right behind him. "
            " You didn't inform him that you were there, so of course he would get surprised. "
            x " Eek! " with vpunch
            hide mrdemisurprised at bottom
            show mrdemineutral at center
            x " Whhh...hooo... It's just you, [name]... "
            x " I hope I didn't keep you waiting for too long... "
            $ demiknow = True
            msd " Uhh...Mister Demi, by the way... "
            " You told him that you just arrived, and asked him what he was talking about with Miss Grace. "
            " You can't tell me that you weren't curious with what he was talking about with Miss Grace. "
            msd " What I was talking about with Miss Grace...? Gee, you're that curious... "
            msd " If you really want to know, then... "
            msd " It's about the situation that's been happening recently... "
            msd " Miss Grace has given me some orders to do so that we can find the student faster. "
            msd " Spread word everywhere and ask questions to people... "
            msd " ...Every teacher's going to be a part of this, and you were supposed to be included, buuut... "
            msd " ...Miss Grace saw how much you were stressing yourself over this student... "
            msd " ...S-she found it sweet, but you don't have to overstress about what happened. "
            msd " ...And also... School's going to be cut off for the rest of the day. Me and the other teachers will handle the situation for now. "
            msd " ...All you can do is ask around online if anyone's seen them... "
            msd " ...Miss Grace said that school's going to be cut off due to the recent suspicious things that's been happening. "
            msd "... I-I mean, students HAVE gotten missing, but right now...things have been getting way too shady. "
            msd " ...School ends after your class, alright...? I'll tell you if we find anything... "
            scene black with dissolve
            " You spent the rest of the break talking with Mister Demi. "
            " ...Huh. So you basically had the rest of the afternoon to yourself. "
            " You're gonna use that time to spread more awareness of the missing student for sure. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, time for another break. "
            " After this break, it's gonna be your class. "
            " And after your class, you're gonna go home. "
            pause 2.0
            jump twbreak4

    label hundredpartners:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the art teacher's classroom, and spotted all of the other students doing some painting. "
        " All of them looked pretty good, but you were wondering where the art teacher was. "
        " You looked around and spotted her at the very corner of the room, on a call with someone. "
        " Being the little nosy [person] you were, you decided to check out what she was talking about and who she was talking to. "
        show sashaneutral at center with easeinleft
        if sashaknow == True:
            mss " ...Yes, ma'am... "
            mss " ...On it! You can count on me...! "
            " She ends the call before turning around to check on her student's paintings... "
            " Only to get jumpscared by you being there. She wasn't expecting you there. "
            mss " Oh! Hey there [name]! "
            mss " Hopefully I didn't keep you waiting for long, hehe! Was just on a call with the principal. "
            " You told her that you just arrived, and asked her what she was talking about with Miss Grace. "
            " You can't tell me that you weren't curious with what she was talking about with Miss Grace. "
            hide sashaneutral at bottom
            show sashaconfused at center
            mss " Hmm, what I was talking with Miss Grace? "
            mss " My, you're really a nosy one, [name]... "
            mss " But since you really, really want to know, I'll tell you! "
            hide sashaconfused at bottom
            show sashasad at center
            mss " Miss Grace has given me some orders to do so that we can find the student faster. "
            mss " Spread word everywhere and ask questions to people...!!! "
            mss " Every teacher's going to be a part of this, and you were supposed to be included, buuut... "
            mss " Miss Grace saw how much you were stressing yourself over this kid. "
            mss " She found it sweet, but you don't have to overstress about what happened. "
            mss " School's going to be cut off for the rest of the day. Me and the other teachers will handle the situation for now. "
            mss " All you can do is ask around online if anyone's seen them... "
            mss " Miss Grace said that school's going to be cut off due to the recent suspicious things that's been happening. "
            mss " I mean, students HAVE gotten missing, but right now...things have been getting way too shady!! "
            mss " School ends after your class, alright? I'll tell you if we find anything! "
            scene black with dissolve
            " You spent the rest of the break talking with Miss Sasha. "
            " ...Huh. So you basically had the rest of the afternoon to yourself. "
            " You're gonna use that time to spread more awareness of the missing student for sure. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, time for another break. "
            " After this break, it's gonna be your class. "
            " And after your class, you're gonna go home. "
            pause 2.0
            jump twbreak4
        else:
            x " ...Yes, ma'am... "
            x " ...On it! You can count on me...! "
            " She ends the call before turning around to check on her student's paintings... "
            " Only to get jumpscared by you being there. She wasn't expecting you there. "
            x " Oh! Hey there [name]! "
            x " Hopefully I didn't keep you waiting for long, hehe! Was just on a call with the principal. "
            $ sashaknow = True
            mss " I'm Miss Sasha by the way, art teacher! "
            " You told her that you just arrived, and asked her what she was talking about with Miss Grace. "
            " You can't tell me that you weren't curious with what she was talking about with Miss Grace. "
            hide sashaneutral at bottom
            show sashaconfused at center
            mss " Hmm, what I was talking with Miss Grace? "
            mss " My, you're really a nosy one, [name]... "
            mss " But since you really, really want to know, I'll tell you! "
            hide sashaconfused at bottom
            show sashasad at center
            mss " Miss Grace has given me some orders to do so that we can find the student faster. "
            mss " Spread word everywhere and ask questions to people...!!! "
            mss " Every teacher's going to be a part of this, and you were supposed to be included, buuut... "
            mss " Miss Grace saw how much you were stressing yourself over this kid. "
            mss " She found it sweet, but you don't have to overstress about what happened. "
            mss " School's going to be cut off for the rest of the day. Me and the other teachers will handle the situation for now. "
            mss " All you can do is ask around online if anyone's seen them... "
            mss " Miss Grace said that school's going to be cut off due to the recent suspicious things that's been happening. "
            mss " I mean, students HAVE gotten missing, but right now...things have been getting way too shady!! "
            mss " School ends after your class, alright? I'll tell you if we find anything! "
            scene black with dissolve
            " You spent the rest of the break talking with Miss Sasha. "
            " ...Huh. So you basically had the rest of the afternoon to yourself. "
            " You're gonna use that time to spread more awareness of the missing student for sure. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, time for another break. "
            " After this break, it's gonna be your class. "
            " And after your class, you're gonna go home. "
            pause 2.0
            jump twbreak4
label twbreak4:
    scene hallway with dissolve
    " You were getting a little too stressed thinking about the things that's been happening lately. "
    " You decided to get into your classroom early so that you could think there. "
    " All of the noise wasn't exactly helping you right now. "
    " I mean, how could it? You're literally hearing voices of worried students around you. "
    " You've gotta make sure that these students don't go missing. "
    " They're too young for this. "
    scene black with dissolve
    pause 2.0
    jump twclass5

label twclass5:
    scene gardenroom with dissolve
    " You patiently waited for the students to get into your classroom. "
    " As you were waiting, you spotted a bug on one of the windows in your classroom. "
    " It looked pretty cute...there was also another bug behind it. "
    " It was much bigger, and it was coming up to the bug pretty quickly. "
    " The bigger bug ended up eating the smaller bug. Huh. "
    " Is this considered bug cannibalism? You don't really know. "
    " Is this also hinting towards something? Probably. "
    " After a bit of staring at the sight you were seeing, you heard your classroom doors open. The students are here. "
    " You're going to be giving them a test today. Just a quick one. "
    " You gave them their test papers and watched them answer. "
    " They finished pretty quickly considering the fact it was multiple choice and only 15 numbers. "
    " You were very much expecting for one of them to have spedran your test. "
    play sound "audio/bellring.mp3"
    " The students leave your classroom, leaving you to check their papers before you went home. "
    scene black with dissolve
    " You spent the rest of the time checking your students papers. "
    " Somehow someone got a 1, but you gave them a +5 out of pity. "
    " Eventually you got done with checking everything, and you prepared your things as Miss Grace announced in the speakers that school will end early today. "
    " You put everything you needed in your bag, and got out of the school. "
    pause 2.0
    jump twendday

label twendday:
    # reminder the interactions
    stop music fadeout 1.5
    pause 1.5
    play music "audio/home.mp3"
    scene mcroom with dissolve
    " You eventually got home and changed out of your teacher uniform and changed into something more comfortable. "
    " Checking your phone as you sat down on your bed, you saw that no one had still replied. "
    " You checked the other teachers posts about the missing kid and there was nothing there either. "
    " You were kind of losing hope with how no one was responding...you expected that someone would've atleast known something about it. "
    " You've just gotta pray that the kid is alright though. No negative thoughts. "
    " You still didn't know what actually happened to the kid so they're going to be fine. "
    " You laid down onto your bed. You need a nap. "
    scene black with dissolve
    pause 2.0
    " Knock knock. Someone's at your door. "
    scene mcroom with dissolve
    " You woke up to someone knocking on your door. "
    " You then looked at the time on your phone and saw that it was 9 PM. "
    " Jesus CHRIST you were that sleepy? damn, that's not even a nap anymore... "
    " Anyway, you get up from your bed and opened your door to see who it was. "
    if circlelv >= 15 or circlelv == 15:
        show misscircleneutral at center with easeinright
        msc " Hey there, [name]! "
        msc " Sorry that I woke you up or anything, haha... "
        msc " I had to ask Miss Grace where you lived cause you weren't responding to my texts. "
        msc " We actually live pretty close by! Isn't that a nice fun fact? "
        msc " Anywho...I know you want to know what happened to that kid. "
        msc " And...I'm pretty sure you're not gonna like it. "
        msc " So, you see... "
        stop music
        msc " The kid you're looking for is {b}dead{/b}. "
        msc " Chopped up into pieces at the very back of the school in the forest. "
        msc " We only found out about it because Miss Emily was looking around and smelt something nasty back there. "
        msc " ...But, that's not the only thing that I'm going to tell you. "
        msc " You see... "
        msc " ...I {b}killed{/b} them. "
        " ...You can't even say anything - you weren't expecting this at all. "
        " You thought she wouldn't do something like this, but now your thoughts were just now proven wrong about her. "
        play music "audio/concern.mp3" fadein 3.0
        hide misscircleneutral at bottom
        show misscirclehappy at center
        msc " Why? because they had low grades! "
        msc " Listen here, I have an explanation for YOU to understand my actions better! "
        msc " So...there's just some students who just wont pay attention no matter what. "
        msc " We've tried warning them in the past, threatening to get them sent out of this school... "
        msc " But they never cared to listen!  "
        msc " So, me, Thavel, and Bloomie decided on something... "
        msc " We were to {b}kill{/b} any student who got a low grade. "
        msc " It was even approved by Miss Grace herself! Interesting, right? "
        msc " She just looks like the person who wouldn't even agree to that stuff, but in reality she's just letting us do ANYTHING we want. "
        msc " At first, no one took us seriously. "
        msc " But after a little {i}incident{/i} that happened in the hallways... "
        msc " Everyone finally took our warnings seriously! "
        msc " Everyone was paying attention...everyone was doing well... "
        msc " But there's still some people who don't believe us, so...!! "
        msc " We had to kill them. "
        msc " Easy to understand why we do that now, isn't it? "
        msc " If they don't pay attention, we're just gonna have to make the expectations higher and higher or else they'll meet their death! "
        msc " Hehe...it's fun, really! murdering students and all..."
        hide misscirclehappy at bottom
        show misscircleneutral at center
        msc " Originally I didn't want to be the one to tell you this, but I had no choice. "
        stop music fadeout 1.5
        msc " You're a good friend, [name]! But do you think you'd bring yourself to be friends with someone like me? A murderer? "
        stop music fadeout 1.5
        menu:
            " ... ":
                $ circlelv += 10
                hide misscircleneutral at bottom
                show misscirclehappy at center
                msc " I'll take your silence as a yes. "
                msc " I knew I could count on you, [name]! "
                msc " Maybe we could also get you in the whole murdering students thing too! "
                scene black with dissolve
                " You talked with Miss Circle for a bit. "
                " You didn't know how to feel about the fact that there were just three murderers in this school and no one really cared about it. "
                " You also can't really back away now since you're basically stuck in this job for a good while. Can't exactly quit. "
                " This is the only way you can get money. Trying to find another job you can do is hard. "
                " Guess you're just going to have to deal with this for now. "
                " Eventually, Miss Circle left your house and you closed n locked the door... "
                " ...Then you went back to sleep. What a wild day. "
                pause 2.0
                jump teacherthursday
            " *Close the door on her* ":
                $ circlelv = 0
                hide misscircleneutral at right with easeoutright
                " You closed and locked the door on her. "
                " Miss Circle's affection points has been resetted to 0. "
                " You're going to need some time to think about this. "
                scene black with dissolve
                " You went back to your room to think for a few minutes. "
                " You didn't know how to feel about the fact that there were just three murderers in this school and no one really cared about it. "
                " You also can't really back away now since you're basically stuck in this job for a good while. Can't exactly quit. "
                " This is the only way you can get money. Trying to find another job you can do is hard. "
                " Guess you're just going to have to deal with this for now. "
                " You then went back to sleep. What a wild day. "
                pause 2.0
                jump teacherthursday
    elif thavellv >= 15 or thavellv == 15:
        show msthravelneutral at center with easeinright
        mst " Hola there, [name]! "
        mst " Sorry for bothering you at this hour, but you weren't replying to my texts. "
        mst " Had to ask Miss Grace on where you lived so that I could tell ya. "
        mst " And we live kinda close!! Isn't that nice? "
        mst " But anyway, time for me to tell you the news of what we found. "
        stop music
        mst " The kid you're looking for is {b}dead{/b}. "
        mst " Chopped up into pieces at the very back of the school in the forest. "
        mst " We only found out about it because Miss Emily was looking around and smelt something nasty back there. "
        mst " ...But, that's not the only thing that I'm going to tell you. "
        mst " You see... "
        mst " ...I {b}killed{/b} them. "
        " ...You can't even say anything - you weren't expecting this at all. "
        " You thought she wouldn't do something like this, but now your thoughts were just now proven wrong about her. "
        play music "audio/concern.mp3" fadein 3.0
        hide msthravelneutral at bottom
        show msthravelhappy at center
        mst " Why? because they had low grades! "
        mst " Listen here, I have an explanation for YOU to understand my actions better! "
        mst " So...there's just some students who just wont pay attention no matter what. "
        mst " We've tried warning them in the past, threatening to get them sent out of this school... "
        mst " But they never cared to listen!  "
        mst " So, me, Thavel, and Bloomie decided on something... "
        mst " We were to {b}kill{/b} any student who got a low grade. "
        mst " It was even approved by Miss Grace herself! Interesting, right? "
        mst " She just looks like the person who wouldn't even agree to that stuff, but in reality she's just letting us do ANYTHING we want. "
        mst " At first, no one took us seriously. "
        mst " But after a little {i}incident{/i} that happened in the hallways... "
        mst " Everyone finally took our warnings seriously! "
        mst " Everyone was paying attention...everyone was doing well... "
        mst " But there's still some people who don't believe us, so...!! "
        mst " We had to kill them. "
        mst " Easy to understand why we do that now, isn't it? "
        mst " If they don't pay attention, we're just gonna have to make the expectations higher and higher or else they'll meet their death! "
        mst " Hehe...it's fun, really! murdering students and all..."
        hide msthravelhappy at bottom
        show msthravelneutral at center
        mst " I didn't want to tell you this and everything, but... "
        mst " No one else was really volunteering to tell you. "
        mst " And plus, we all spammed your name in the group chat but you were faaast asleep. "
        if they == "he":
            mst " Anyway, you've been a really good amigo, [name]! "
        elif they == "she":
            mst " Anyway, you've been a really good amiga, [name]! "
        elif they == "they":
            mst " Anyway, you've been a really good amigo, [name]! "
        else:
            mst " Anyway, you've been a really good amigo, [name]! "
        mst " But I wonder if you'd still be friends with someone like me. "
        mst " Friends with a murderer, imagine that! "
        stop music fadeout 1.5
        mst " ...What do you say, would you still be friends with me even after all I've done? "
        menu:
            " ... ":
                $ thavellv += 10
                hide msthravelneutral at bottom
                show msthravelhappy at center
                mst " I'll take that as a yes, then. "
                mst " Surprised that you'd want to stay with someone like me, but I should be happy. "
                mst " Maybe I could even get you interested in the whole murdering thing too... "
                mst " Just a possibility, not reality if you don't want it. "
                scene black with dissolve
                " You talked with Miss Thravel for a bit. "
                " You didn't know how to feel about the fact that there were just three murderers in this school and no one really cared about it. "
                " You also can't really back away now since you're basically stuck in this job for a good while. Can't exactly quit. "
                " This is the only way you can get money. Trying to find another job you can do is hard. "
                " Guess you're just going to have to deal with this for now. "
                " Eventually, Miss Thavel left your house and you closed n locked the door... "
                " ...Then you went back to sleep. What a wild day. "
                pause 2.0
                jump teacherthursday
            " *Close the door on her* ":
                $ thavellv = 0
                hide msthravel at right with easeoutright
                " You closed and locked the door on her. "
                " Miss Thavel's affection points has been resetted to 0. "
                " You're going to need some time to think about this. "
                scene black with dissolve
                " You went back to your room to think for a few minutes. "
                " You didn't know how to feel about the fact that there were just three murderers in this school and no one really cared about it. "
                " You also can't really back away now since you're basically stuck in this job for a good while. Can't exactly quit. "
                " This is the only way you can get money. Trying to find another job you can do is hard. "
                " Guess you're just going to have to deal with this for now. "
                " You then went back to sleep. What a wild day. "
                pause 2.0
                jump teacherthursday
    elif bloomielv >= 15 or bloomielv == 15:
        show missbloomieneutral at center with easeinright
        msb " Hello there, [name]. "
        msb " You weren't responding to our texts in the group chat. "
        msb " I had to ask Miss Grace for your location so I could tell you the news personally. "
        msb " I'm going to make this short and simple. "
        stop music
        msb " The student you're looking for is {b}dead{/b}. "
        msb " I placed them in the back of the school, all chopped up. "
        play music "audio/concern.mp3" fadein 1.5
        msb " And yes, I killed that student. "
        msb " Me, Thavel, and Circle kill students who are misbehaving. "
        msb " Misbehaving as in getting low grades or acting like fool in classes. "
        msb " We kept warning them awhile back, but eventually came to the conclusion that we needed to take things seriously if we want them to focus. "
        msb " Even if that means hurting them. Even if that means killing them. "
        msb " Anything to get their attention onto learning. "
        msb " It's simple to understand, truly. "
        msb " I didn't want to tell you this, but no other teacher wanted to tell you about it. "
        stop music fadeout 1.5
        msb " You've been a good friend, [name]. "
        msb " But it's honestly hard to believe that you would want to still be friends with someone like me. "
        msb " Would you want to be friends with a murderer? "
        menu:
            " ... (Stay) ":
                $ bloomielv += 10
                hide missbloomieneutral at bottom
                show missbloomiehappy at center
                msb " ...I'm...honestly a little surprised that you chose to stay. "
                msb " Nonetheless, I'm happy that you're staying. "
                msb " I might introduce you to killing students, if you want me to. "
                scene black with dissolve
                " You talked with Miss Bloomie for a bit. "
                " You didn't know how to feel about the fact that there were just three murderers in this school and no one really cared about it. "
                " You also can't really back away now since you're basically stuck in this job for a good while. Can't exactly quit. "
                " This is the only way you can get money. Trying to find another job you can do is hard. "
                " Guess you're just going to have to deal with this for now. "
                " Eventually, Miss Bloomie left your house and you closed n locked the door... "
                " ...Then you went back to sleep. What a wild day. "
                pause 2.0
                jump teacherthursday
            " *Close the door on her* ":
                $ bloomielv = 0
                hide missbloomieneutral at right with easeoutright
                " You closed and locked the door on her. "
                " Miss Bloomie's affection points has been resetted to 0. "
                " You're going to need some time to think about this. "
                scene black with dissolve
                " You went back to your room to think for a few minutes. "
                " You didn't know how to feel about the fact that there were just three murderers in this school and no one really cared about it. "
                " You also can't really back away now since you're basically stuck in this job for a good while. Can't exactly quit. "
                " This is the only way you can get money. Trying to find another job you can do is hard. "
                " Guess you're just going to have to deal with this for now. "
                " You then went back to sleep. What a wild day. "
                pause 2.0
                jump teacherthursday
    elif emilylv >= 15 or emilylv == 15:
        show msemilyneutral at center with easeinright
        mse " Hey there, [name]! Were you fast asleep? "
        mse " Sorry if I woke you up...but you weren't responding to my text messages. "
        mse " I honestly just came here because you needed to know about...you know...the kid."
        mse " I know how badly you want to know about what happened to them, and... "
        hide msemilyneutral at bottom
        show msemilysad at center
        stop music fadeout 1.5
        mse " Things didn't...exactly go well. "
        mse " I'm not sure if you're gonna like what you're going to hear, but you still need to hear this. "
        mse " You see, the kid...well... "
        play music "audio/emotionalmoment.mp3" fadein 2.5
        mse " We found the kid's dead body at the back of the school. "
        mse " It was all chopped up... "
        mse " I was the one who found it because I was looking for clues on where they might be, and smelt something odd, and then... "
        mse " ...You could guess what I found. "
        mse " And there's another thing I would like to admit to you... "
        mse " ...This school isn't safe for the students. If they got a low grade, that is. "
        mse " If they got a low grade, then Miss Circle, Thavel, or Bloomie will go after them... "
        mse " ...And kill them. That's exactly what happened to the kid you were looking for. "
        mse " I'm...very sorry you had to hear about this, [name]. "
        mse " I know that you were hoping for that kid to be alright. "
        mse " Hoping that the kid would atleast live a long life... "
        mse " ...But they didn't even get to say goodbye to the people they care about. "
        mse " ...Would you...want me to stay with you for a bit? I know you're feeling down after hearing this news. "
        mse " It's okay if you want some time for yourself right now. "
        menu:
            " Please stay ":
                $ emilylv += 10
                hide msemilysad at bottom
                show msemilyhappy at center
                mse " ...I gladly will. "
                mse " You can talk to me whenever you want, okay? "
                mse " Don't be afraid to tell me anything. "
                scene black with dissolve
                " You talked with Miss Emily for a bit. "
                " You didn't know how to feel about the fact that there were just three murderers in this school and no one really cared about it. "
                " You also can't really back away now since you're basically stuck in this job for a good while. Can't exactly quit. "
                " This is the only way you can get money. Trying to find another job you can do is hard. "
                " Guess you're just going to have to deal with this for now. "
                " Miss Emily eventually left to go to sleep in her house, and you locked the door after she went away. "
                " You then went back to sleep. What a wild day... "
                pause 2.0
                jump teacherthursday
            " I need some time for myself ":
                hide msemilysad at bottom
                show msemilyneutral at center
                mse " It's alright, I understand. "
                mse " Take care, okay? "
                mse " I'll get going now. Have a good night. "
                scene black with dissolve
                " You went back to your room to think for a few minutes. "
                " You didn't know how to feel about the fact that there were just three murderers in this school and no one really cared about it. "
                " You also can't really back away now since you're basically stuck in this job for a good while. Can't exactly quit. "
                " This is the only way you can get money. Trying to find another job you can do is hard. "
                " Guess you're just going to have to deal with this for now. "
                " You then went back to sleep. What a wild day. "
                pause 2.0
                jump teacherthursday
    elif demilv >= 15 or demilv == 15:
        show mrdemineutral at center with easeinright
        msd " Uhhh...hey there, [name]... "
        msd " L-look, I'm really sorry that I had to wake you up, but you just weren't responding to Miss Grace's texts... "
        msd " She sent me to go here...to your place to inform you what happened... "
        msd " She knows how much you needed to hear about the news personally since...you cared so much about that kid... "
        msd " Even though you didn't know them...it was sweet, really... "
        stop music fadeout 1.5
        msd " ...But now it's time for me to tell you what really happened... "
        msd " I know that you won't really like this...and t-trust me, I almost broke down after I found out what happened... "
        msd " So please...make sure you yourself is alright before hearing about this... "
        msd " ...(Deep breaths, Demi. You can do this.)... "
        play music "audio/emotionalmoment.mp3" fadein 1.5
        msd " So...we found the student dead at the back of the school... "
        msd " M-miss Emily was looking around and...she smelt something funny there... "
        msd " ...And that's how she found the dead body...all chopped up... "
        msd " ...That's not all that I have to tell you... "
        msd " There's three teachers in this school that...'punishes' sutdents for failing... "
        msd " These three are...Circle, Thavel, and Bloomie... "
        msd " Only if you fail in their classes, they would hunt you down until you're dead... "
        msd " ...That's why most students here are so stressed on making themselves pass their works... "
        msd " It's...horrifying really...I don't know why Grace would allow this... "
        msd " It scares me to think that so many children were killed just for a low grade... "
        msd " ... "
        msd " ...Look, I know that you...might want some time to yourself after the news I just told you, but... "
        msd " ...Perhaps...I-I could keep you some company...? "
        msd " I-If you don't mind, of course! I don't want to make you uncomfortable... "
        menu:
            " Please stay ":
                $ demilv += 10
                hide mrdemineutral at bottom
                show mrdemihappy at center
                msd " ...I-I'd...Yeah, I will... "
                msd " You can tell me anything, okay...? "
                msd " You don't have to worry about a thing while I'm here with you... "
                scene black with dissolve
                " You spent a few hours talking with Mister Demi. "
                " You didn't know how to feel about the fact that there were just three murderers in this school and no one really cared about it. "
                " You also can't really back away now since you're basically stuck in this job for a good while. Can't exactly quit. "
                " This is the only way you can get money. Trying to find another job you can do is hard. "
                " Guess you're just going to have to deal with this for now. "
                " Mister Demi then left to go back to his own home, and you locked your door after he left. "
                " You then went back to sleep. What a wild day. "
                pause 2.0
                jump teacherthursday
            " I need some time for myself ":
                msd " Okay... "
                msd " Keep yourself safe...alright...? "
                hide mrdemineutral at right with easeoutright
                scene black with dissolve
                " You went back to your room to think for a few minutes. "
                " You didn't know how to feel about the fact that there were just three murderers in this school and no one really cared about it. "
                " You also can't really back away now since you're basically stuck in this job for a good while. Can't exactly quit. "
                " This is the only way you can get money. Trying to find another job you can do is hard. "
                " Guess you're just going to have to deal with this for now. "
                " You then went back to sleep. What a wild day. "
                pause 2.0
                jump teacherthursday
    elif sashalv >= 15 or sashalv == 15:
        show sashaneutral at center with easeinright
        mss " Haha, hey there, [name]...! "
        mss " Sorry, I probably woke you up from your slumber, haha... "
        mss " It's just that you weren't responding to my texts and I had to tell you something really important...!! "
        " You have a feeling her sad expression is going to be a little unserious for this. "
        mss " It's about the kid that you really cared about from earlier... "
        hide sashaneutral at bottom
        show sashasad at center
        stop music fadeout 1.5
        mss " And it's not exactly good news... "
        mss " I think it's best to prepare your emotions before I tell you...! "
        " She sounds like she's trying to make things sound better even though things aren't. "
        mss " Whooo...okay, time for me to tell you... "
        play music "audio/emotionalmoment.mp3" fadein 1.5
        mss " We found the kid's dead body at the back of the school. "
        mss " It was all chopped up... "
        mss " Miss Emily was the one who found the kid because she was looking around for clues...then she smelt something funny, and... "
        mss " ...You can guess what happened... "
        mss " And there's another thing I would like to admit to you... "
        mss " ...This school isn't safe for the students. If they got a low grade, that is. "
        mss " If they got a low grade, then Miss Circle, Thavel, or Bloomie will go after them... "
        mss " ...And kill them. That's exactly what happened to the kid you were looking for. "
        mss " I'm...very sorry you had to hear about this, [name]. "
        mss " I know that you were hoping for that kid to be alright. "
        mss " Hoping that the kid would atleast live a long life... "
        mss " ...But they didn't even get to say goodbye to the people they care about. "
        mss " ...Would you...want me to stay with you for a bit? I know you're feeling down after hearing this news. "
        mss " It's okay if you want some time for yourself right now...!! "
        menu:
            " Please Stay ":
                $ sashalv += 10
                hide sashasad at bottom
                show sashahappy at center
                mss " ...Well..if that's what you want... "
                mss " ...Then I don't mind! "
                mss " Go ahead and tell me what you feel... "
                scene black with dissolve
                " You spent a few hours talking with Miss Sasha. "
                " You didn't know how to feel about the fact that there were just three murderers in this school and no one really cared about it. "
                " You also can't really back away now since you're basically stuck in this job for a good while. Can't exactly quit. "
                " This is the only way you can get money. Trying to find another job you can do is hard. "
                " Guess you're just going to have to deal with this for now. "
                " Miss Sasha then left to go back to her own home, and you locked your door after she left. "
                " You then went back to sleep. What a wild day. "
                pause 2.0
                jump teacherthursday
            " I need some time for myself ":
                hide sashasad at bottom
                show sashaneutral at center
                mss " Well, alright...If that's what you want. "
                mss " Take care of yourself, alright? "
                hide sashaneutral at right with easeoutright
                scene black with dissolve
                " You went back to your room to think for a few minutes. "
                " You didn't know how to feel about the fact that there were just three murderers in this school and no one really cared about it. "
                " You also can't really back away now since you're basically stuck in this job for a good while. Can't exactly quit. "
                " This is the only way you can get money. Trying to find another job you can do is hard. "
                " Guess you're just going to have to deal with this for now. "
                " You then went back to sleep. What a wild day. "
                pause 2.0
                jump teacherthursday
    else:
        " You opened your door to see that no one was there. Huh. "
        " Must've been some kid ding dong ditching you or whatever it's called... "
        " ...You close and lock your door again before going back to your room. "
        " Then, you went back to sleep. "
        scene black with dissolve
        " What a wild day that you had... "
        " Hopefully tomorrow's way better. "
        pause 2.0
        jump teacherthursday
