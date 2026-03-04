label teachertuesday:
    show text " DAY 2 - TUESDAY "
    pause 2.0
    play music "audio/home.mp3" fadein 0.5
    scene mcroom with dissolve
    " Morning, sleepy head. "
    " Hope you had a good dream. Or nightmare. I don't really care. "
    " I also took away your privileges to just roam the halls. "
    " Why? for funny. You need to interact more, idiot. "
    " Anyways, you cook your breakfast, get ready for the day... "
    " ...You look at the teacher's gc you were added in and found out Miss Circle is absent today. "
    " She asked you to take over for a bit in your dms. "
    " What should you respond with? "
    menu:
        " actually text her ":
            $ circlelv += 10
            " Alright, screw it. Let's text her. "
            " Uhhh...what should you even say? "
            " Of course you gotta say that you want her to feel better. "
            " Otherwise it'll look like you don't care. "
            " Hmmm...{p} Okay, hear me out. "
            " 'Hey Circle, of course I could take over for you...' "
            " '...I do hope that you feel better soon though.' "
            " 'This school wouldn't be the same without you!' "
            " ...Okay, that one kind of sucked, but it's what I got. "
            " Now send that, and wait for her to respond... "
            " ...She responded with a heart emoji and she's typing. "
            msc " Thank you for taking over for me, [name]!! "
            msc " And also, I'll get better tomorrow, trust me. "
            msc " Don't ask how that works, hehe...it just does! "
            msc " Anyway, the students will only have to do an activity for today. "
            msc " The activity sheets should be on my desk. "
            msc " Make sure that my students behave! "
            " She then went offline. "
            " Alright, let's go to work now. "
            scene black with dissolve
            stop music fadeout 0.5
            pause 2.0
            jump teacherclass1
        " Just put a thumbs up emoji ":
            $ circlelv += 1
            " You reacted to her message with a thumbs up emoji. "
            " She then texted you after a bit. "
            msc " The students will only have to do an activity for today. "
            msc " The activity sheets should be on my desk. "
            msc " Make sure that my students behave! "
            " She then went offline. "
            " Alright, let's go to work now. "
            scene black with dissolve
            stop music fadeout 0.5
            pause 2.0
            jump teacherclass1
label teacherclass1:
    play music "audio/paperhigh.mp3" fadein 0.5
    scene paperschoolfront with dissolve
    pause 1.0
    scene hallway with dissolve
    pause 1.0
    scene classroom with dissolve
    " You sat down in Miss Circle's chair and waited for the students to come in. "
    " While you were waiting, you decided to take a look at what the activity was for the students. "
    " Looks like it's just some normal math questions. Looks pretty easy to you. "
    " You look around her desk and found a picture of Miss circle and...someone that looks oddly like her. "
    " You're thinking that this could be her lover, or just a sibling. "
    " They kind of looked too similar for you to tell if they're siblings or dating. "
    " Oh well, you probably shouldn't think about it too much. "
    " Besides, you could just ask Miss Circle once she gets back. "
    " You didn't really have anything to do, so you just scrolled on your phone to pass time... "
    pause 1.0
    play sound "audio/bellring.mp3"
    " The bell eventually rings, meaning that class was about to start. "
    " You put your phone away and you look at all of the students who had just entered the class. "
    " They seemed to be a tad bit confused that you were here. "
    " Once everyone was seated, you got up from your seat and stood still as you made sure everyone was paying attention to you. "
    " You explained that you're here because Miss Circle is sick, and that you'll be taking over. "
    " Then you explained to them that Miss Circle had left them an activity to do while she's gone. "
    " You went over to the pile of activity sheets and you started giving the papers to the students. "
    " You reminded them that just because you're taking over, doesn't mean that you'll be nice and give them candy. "
    " They still gotta behave and that's final. "
    " You told them that their worksheets should be done once the class is over. "
    " After all of that yapping, you sat back down on your seat. "
    " Though, you weren't playing any games or anything, no. "
    " You're making sure they don't do anything stupid and don't misbehave. "
    scene black with dissolve
    " You spent the rest of the class making sure the students don't misbehave. "
    " There were a few, but you managed to make them focus on their work. "
    " Wow! You're such a great teacher! You totally get paid well for this! "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, and you had all of the students pass their papers to you. "
    " A kid named Engel politely asked you if he could have the papers. "
    " Apparently, he was usually the one who delivered papers to Miss Circle whenever she was sick. "
    " Interesting...you gave him the papers though. "
    " You then went outside Miss Circle's classroom to see what's going on in the hallways. "
    pause 2.0
    jump ttbreak1

label ttbreak1:
    scene hallway with dissolve
    " As you walked out of Miss Circle's classroom, you spotted three of your teacher friends. "
    " You also had to make sure that you didn't bump into the students on accident. "
    " You wanted to talk to one of the teachers too, of course. Who do you talk to though? "
    if thavelknow,bloomieknow,emilyknow == True:
        menu:
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump monitoring
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump mesmerizer
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump candycookiechocolate
    elif thavelknow,bloomieknow == True and emilyknow == False:
        menu:
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump monitoring
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump mesmerizer
            " {image=missemilyicon} A woman that looks rather panicked {image=missemilyicon} ":
                jump candycookiechocolate
    elif thavelknow,emilyknow == True and bloomieknow == False:
        menu:
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump monitoring
            " {image=missbloomieicon} A woman cleaning up her...hand? {image=missbloomieicon} ":
                jump mesmerizer
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump candycookiechocolate
    elif bloomieknow,emilyknow == True and thavelknow == False:
        menu:
            " {image=missthavelicon} A woman with deer horns {image=missthavelicon} ":
                jump monitoring
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump mesmerizer
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump candycookiechocolate
    elif thavelknow == True and bloomieknow,emilyknow == False:
        menu:
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump monitoring
            " {image=missbloomieicon} A woman cleaning up her...hand? {image=missbloomieicon} ":
                jump mesmerizer
            " {image=missemilyicon} A woman that looks rather panicked {image=missemilyicon} ":
                jump candycookiechocolate
    elif bloomieknow == True and thavelknow,emilyknow == False:
        menu:
            " {image=missthavelicon} A woman with deer horns {image=missthavelicon} ":
                jump monitoring
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump mesmerizer
            " {image=missemilyicon} A woman that looks rather panicked {image=missemilyicon} ":
                jump candycookiechocolate
    elif emilyknow == True and thavelknow,bloomieknow == False:
        menu:
            " {image=missthavelicon} A woman with deer horns {image=missthavelicon} ":
                jump monitoring
            " {image=missbloomieicon} A woman cleaning up her...hand? {image=missbloomieicon} ":
                jump mesmerizer
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump candycookiechocolate
    else:
        menu:
            " {image=missthavelicon} A woman with deer horns {image=missthavelicon} ":
                jump monitoring
            " {image=missbloomieicon} A woman cleaning up her...hand? {image=missbloomieicon} ":
                jump mesmerizer
            " {image=missemilyicon} A woman that looks rather panicked {image=missemilyicon} ":
                jump candycookiechocolate
    label monitoring:
        show msthravelneutral at center with easeinleft
        if thavelknow == True:
            " Looks like she's doing her own thing... "
            " ...Like arrange her papers or something. Looks like she's checking something out. "
            " Interesting...she must've had given her students some homework to do. "
            " You waited patiently for her to notice you. "
            mst " ...Oh! [name]! "
            mst " It's nice to see you. You must've replaced Miss Circle for a bit, yeah? "
            mst " Well that's neat! What's not neat though, is her being sick. "
            mst " Don't worry about it too much though! Somehow, whenever she gets sick, she always... "
            mst " Recovers a day after. Don't ask me how it works, no one knows how she works. "
            mst " So! It's best not to worry about her. "
            mst " I do think that I need help on organizing my papers in my office... "
            mst " Everyone else is busy, so... "
            mst " Could you help me arrange a few things? It's alright if not. "
            menu:
                " Help Miss Thavel ":
                    $ thavellv += 10
                    hide msthravelneutral at bottom
                    show msthravelhappy at center
                    mst " Nice! I appreciate your assistance, [name]! "
                    mst " I'd doubt the other teachers would even help me out on this... "
                    mst " ...Considering how busy they are. And how much they have to deal with such nuisances of students. "
                    mst " Thank you again, [name]! "
                    mst " My office is this way, follow me. "
                    scene black with dissolve
                    " You spent the rest of the break helping Miss Thavel arrange her papers. "
                    " It was honestly nice, having to do something instead of doing nothing and scrolling on your phone. "
                    " You also talked with her a bit while you were arranging her stuff. "
                    " You also had to admit... "
                    " Her office was messy, that was for sure. "
                    " You could also see some scratch marks on the walls??? "
                    " When you asked her about it, she just said that those were from her, herself... "
                    " ...Interesting. So she goes feral every now and then. "
                    " New fun fact acquired. Miss Thavel goes feral. "
                    play sound "audio/bellring.mp3"
                    " The bell rang the moment you two were done arranging the paperworks. "
                    " You left her office, and started looking around for who you could help. "
                    pause 2.0
                    jump helpclass1
                " No thanks, I'm busy ":
                    mst " That's alright. "
                    mst " I'll just try to manage organaizing all of my papers.. "
                    mst " I just know it's gonna be a pain, but I can handle it! "
                    mst " ... "
                    mst " Now that I think about it... "
                    mst " I also have to memorize where everything is. "
                    mst " My memory isn't the best for this. "
                    mst " I'm going to suffer, aren't I? "
                    scene black with dissolve
                    " You spent the rest of the break talking to Miss Thavel. "
                    " You didn't really know that she had memory issues... "
                    " She just like me fr!! "
                    " Of course Miss Thavel having memory issues isn't canon. "
                    " I just had to add something to make it more interesting. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, interrupting your conversation with the other teacher. "
                    " Looks like it's time to help someone again. "
                    " You look at all of the students go into their classrooms, before you started looking around for teachers who need your help. "
                    pause 2.0
                    jump helpclass1
        else:
            " Looks like she's doing her own thing... "
            " ...Like arrange her papers or something. Looks like she's checking something out. "
            " Interesting...she must've had given her students some homework to do. "
            " You waited patiently for her to notice you. "
            x " ...Oh! [name]! "
            x " It's nice to see you. You must've replaced Miss Circle for a bit, yeah? "
            x " Well that's neat! What's not neat though, is her being sick. "
            x " Don't worry about it too much though! Somehow, whenever she gets sick, she always... "
            x " Recovers a day after. Don't ask me how it works, no one knows how she works. "
            x " So! It's best not to worry about her. "
            $ thavelknow = True
            mst " I'm Miss Thavel, by the way. The Language teacher. "
            " You told her that it was nice to meet her, then asked her if she needed help with anything. "
            mst " I do think that I need help on organizing my papers in my office... "
            mst " Everyone else is busy, so... "
            mst " Could you help me arrange a few things? It's alright if not. "
            menu:
                " Help Miss Thavel ":
                    $ thavellv += 10
                    hide msthravelneutral at bottom
                    show msthravelhappy at center
                    mst " Nice! I appreciate your assistance, [name]! "
                    mst " I'd doubt the other teachers would even help me out on this... "
                    mst " ...Considering how busy they are. And how much they have to deal with such nuisances of students. "
                    mst " Thank you again, [name]! "
                    mst " My office is this way, follow me. "
                    scene black with dissolve
                    " You spent the rest of the break helping Miss Thavel arrange her papers. "
                    " It was honestly nice, having to do something instead of doing nothing and scrolling on your phone. "
                    " You also talked with her a bit while you were arranging her stuff. "
                    " You also had to admit... "
                    " Her office was messy, that was for sure. "
                    " You could also see some scratch marks on the walls??? "
                    " When you asked her about it, she just said that those were from her, herself... "
                    " ...Interesting. So she goes feral every now and then. "
                    " New fun fact acquired. Miss Thavel goes feral. "
                    play sound "audio/bellring.mp3"
                    " The bell rang the moment you two were done arranging the paperworks. "
                    " You left her office, and started looking around for who you could help. "
                    pause 2.0
                    jump helpclass1
                " No thanks, I'm busy ":
                    mst " That's alright. "
                    mst " I'll just try to manage organaizing all of my papers.. "
                    mst " I just know it's gonna be a pain, but I can handle it! "
                    mst " ... "
                    mst " Now that I think about it... "
                    mst " I also have to memorize where everything is. "
                    mst " My memory isn't the best for this. "
                    mst " I'm going to suffer, aren't I? "
                    scene black with dissolve
                    " You spent the rest of the break talking to Miss Thavel. "
                    " You didn't really know that she had memory issues... "
                    " She just like me fr!! "
                    " Of course Miss Thavel having memory issues isn't canon. "
                    " I just had to add something to make it more interesting. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, interrupting your conversation with the other teacher. "
                    " Looks like it's time to help someone again. "
                    " You look at all of the students go into their classrooms, before you started looking around for teachers who need your help. "
                    pause 2.0
                    jump helpclass1
    label mesmerizer:
        show missbloomieneutral at center with easeinright
        if bloomieknow == True:
            " You walked up to her. Looks like she's busy cleaning up her blade of an arm... "
            " It must've gotten a bit dirty if she was cleaning it. "
            " Totally didn't murder someone. She looks like a nice person, she probably wouldn't do that. "
            " You waited for her to notice you. "
            msb " ... "
            msb " Oh, hey [name]. Sorry that I didn't notice you a bit sooner. "
            msb " Just cleaning up my blade since some chemicals got onto it while I was teaching. "
            msb " Not really fun, since it's not gonna have the most pleasant smell for a bit. "
            msb " It'll eventually go back to normal though. "
            msb " ...So, you replaced Miss Circle for a bit, right? "
            msb " You know how she's sick? And how she can recover quickly? "
            msb " I may or may not have figured out her secret. Don't tell anyone that I told you though. "
            msb " Don't tell her either, or she'll get upset. Anyway, her secret is... "
            msb " ...She eats oreos to heal herself. Yes, that's really it. "
            msb " She keeps a whole load of oreos stashed in her closet. "
            msb " How I know about this? Well, one time I've been to her house before. "
            msb " She accidentally got a cut while cutting some ingredients up, and she proceeded to go to her oreo closet... "
            msb " ...Eat about 5 oreos, and she was all better. I did NOT see that cut on her finger anymore. "
            msb " Now, I don't know how many oreos she has to exactly eat for her to become better tomorrow, but I'm sure it's a lot. "
            msb " ...Now that I think of it, she couldn't possibly just eat oreos for an entire day. "
            msb " She has to eat proper food!... "
            msb " ...But, knowing her, she probably would. "
            msb " She's a unique one, I'll give you that. "
            " ...Interesting. "
            " You nodded at what Miss Bloomie said, and then asked her if she needed help with anything. "
            msb " Hmm...let's see... "
            msb " I do need to clean up some test bottles for my next class. "
            msb " Could you help me with that? "
            menu:
                " Sure ":
                    $ bloomielv += 10
                    msb " ... "
                    hide missbloomieneutral
                    show missbloomiehappy at center
                    msb " ...Okay. "
                    " ...Oh wow, she looks pretty happy. "
                    msb " You know where my classroom is, right? "
                    msb " Just follow me. "
                    hide missbloomiehappy at left with easeoutleft
                    scene black with dissolve
                    " You spent the rest of the break helping out Miss Bloomie. "
                    " You cleaned half of her test bottles, and she took the other half. "
                    " You two didn't really talk much, but when you two did, you were the one who was starting the conversation. "
                    " She doesn't really seem like the talkative type, eh? "
                    " She's just like me fr !! - okay I gotta stop with these jokes soon. "
                    " Eventually, you two were done. You didn't really know what to say so you just politely and awkwardly left her classroom. "
                    " Since you still had some freetime on your hands, you decided to walk around the school for a bit. "
                    " ...And make sure that the students aren't doing anything bad, of course. "
                    " Miss Grace did say not to slack off. You wouldn't want to be fired now, would you? "
                    " If you're curious, no, there's no secret ending where you get fired. "
                    " Check the achievements list, loser. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like you have to help someone again. "
                    " You wait for every student to get into their respective classrooms before you started looking for anyone who might need help. "
                    pause 2.0
                    jump helpclass1
                " Actually, I think I'm busy ":
                    msb " I see... "
                    msb " I'll go ahead and clean up the bottles myself then. "
                    msb " See you later, [name]. "
                    hide missbloomieneutral at left with easeoutleft
                    " ...Let's just make sure no students are doing anything bad for the rest of the break. "
                    " You didn't have anything else to do anyway. "
                    scene black with dissolve
                    " You spent the rest of the break monitoring the halls. "
                    " Thankfully, you didn't see any students breaking the rules or anything. "
                    " Otherwise, you're going to have to deal with your second headache for the day. "
                    " The first headache was from Miss Bloomie's explanation of how Miss Circle heals. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for you to go help someone again. "
                    " You wait for every student to get into their respective classrooms before you started looking for anyone who might need help. "
                    pause 2.0
                    jump helpclass1
        else:
            " You walked up to her. Looks like she's busy cleaning up her blade of an arm... "
            " It must've gotten a bit dirty if she was cleaning it. "
            " Totally didn't murder someone. She looks like a nice person, she probably wouldn't do that. "
            " You waited for her to notice you. "
            x " ... "
            x " Oh, hey [name]. Sorry that I didn't notice you a bit sooner. "
            x " Just cleaning up my blade since some chemicals got onto it while I was teaching. "
            x " Not really fun, since it's not gonna have the most pleasant smell for a bit. "
            x " It'll eventually go back to normal though. "
            $ bloomieknow = True
            msb " I'm Miss Bloomie, by the way. The science teacher. "
            msb " ...So, you replaced Miss Circle for a bit, right? "
            msb " You know how she's sick? And how she can recover quickly? "
            msb " I may or may not have figured out her secret. Don't tell anyone that I told you though. "
            msb " Don't tell her either, or she'll get upset. Anyway, her secret is... "
            msb " ...She eats oreos to heal herself. Yes, that's really it. "
            msb " She keeps a whole load of oreos stashed in her closet. "
            msb " How I know about this? Well, one time I've been to her house before. "
            msb " She accidentally got a cut while cutting some ingredients up, and she proceeded to go to her oreo closet... "
            msb " ...Eat about 5 oreos, and she was all better. I did NOT see that cut on her finger anymore. "
            msb " Now, I don't know how many oreos she has to exactly eat for her to become better tomorrow, but I'm sure it's a lot. "
            msb " ...Now that I think of it, she couldn't possibly just eat oreos for an entire day. "
            msb " She has to eat proper food!... "
            msb " ...But, knowing her, she probably would. "
            msb " She's a unique one, I'll give you that. "
            " ...Interesting. "
            " You nodded at what Miss Bloomie said, and then asked her if she needed help with anything. "
            msb " Hmm...let's see... "
            msb " I do need to clean up some test bottles for my next class. "
            msb " Could you help me with that? "
            menu:
                " Sure ":
                    $ bloomielv += 10
                    msb " ... "
                    hide missbloomieneutral
                    show missbloomiehappy at center
                    msb " ...Okay. "
                    " ...Oh wow, she looks pretty happy. "
                    msb " You know where my classroom is, right? "
                    msb " Just follow me. "
                    hide missbloomiehappy at left with easeoutleft
                    scene black with dissolve
                    " You spent the rest of the break helping out Miss Bloomie. "
                    " You cleaned half of her test bottles, and she took the other half. "
                    " You two didn't really talk much, but when you two did, you were the one who was starting the conversation. "
                    " She doesn't really seem like the talkative type, eh? "
                    " She's just like me fr !! - okay I gotta stop with these jokes soon. "
                    " Eventually, you two were done. You didn't really know what to say so you just politely and awkwardly left her classroom. "
                    " Since you still had some freetime on your hands, you decided to walk around the school for a bit. "
                    " ...And make sure that the students aren't doing anything bad, of course. "
                    " Miss Grace did say not to slack off. You wouldn't want to be fired now, would you? "
                    " If you're curious, no, there's no secret ending where you get fired. "
                    " Check the achievements list, loser. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like you have to help someone again. "
                    " You wait for every student to get into their respective classrooms before you started looking for anyone who might need help. "
                    pause 2.0
                    jump helpclass1
                " Actually, I think I'm busy ":
                    msb " I see... "
                    msb " I'll go ahead and clean up the bottles myself then. "
                    msb " See you later, [name]. "
                    hide missbloomieneutral at left with easeoutleft
                    " ...Let's just make sure no students are doing anything bad for the rest of the break. "
                    " You didn't have anything else to do anyway. "
                    scene black with dissolve
                    " You spent the rest of the break monitoring the halls. "
                    " Thankfully, you didn't see any students breaking the rules or anything. "
                    " Otherwise, you're going to have to deal with your second headache for the day. "
                    " The first headache was from Miss Bloomie's explanation of how Miss Circle heals. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for you to go help someone again. "
                    " You wait for every student to get into their respective classrooms before you started looking for anyone who might need help. "
                    pause 2.0
                    jump helpclass1
    label candycookiechocolate:
        show msemilyshock at center with easeinleft
        if emilyknow == True:
            " You walk over to her, and she seems a little panicked. "
            " Wondering why she's so worried, you tapped her shoulder to get her attention and asked her what was wrong. "
            mse " O-oh, [name]! Thank goodness you're here! "
            mse " You see, one of our younger students apparently lost their bracelet. "
            mse " Apparently it was with them before they went to class, and now it's just...gone! "
            mse " That bracelet was very special to them since it was from their older sibling! "
            mse " Uh, if it doesn't bother you... "
            mse " Could you help out a bit? Go and look around the school? "
            mse " It's okay if not though! I'll go and ask someone else, if that's the case... "
            " ...Should you help her look? "
            menu:
                " Of course ":
                    $ emilylv += 10
                    hide msemilyshock at bottom
                    show msemilyneutral at center
                    mse " Whew, thanks [name]... "
                    mse " Things would've been a bit harder for me if I looked around alone. "
                    mse " How about I ask the students, and you look around? "
                    mse " I've already got Mister Demi searching around the school, so with you helping along it's going to be way faster! "
                    mse " Thanks again for your help, [name]... "
                    mse " Before I go, the bracelet is blue. Different shades of blue. "
                    hide msemilyneutral at right with easeoutright
                    " Well, time to get searching. "
                    " You looked at the area around you, and didn't see any bracelets. Unfortunately. "
                    " This is gonna take awhile, isn't it? "
                    " Well, too bad. You're dealing with this now. "
                    scene black with dissolve
                    " You spent the rest of the break helping a kid find their bracelet. "
                    " Eventually, you found it. It was in a trash can. "
                    " Miss Emily asked around for why it was in the trash can, and turns out, another student had borrowed it... "
                    " ...And had thrown it there. Let's just say you, Miss Emily, and the other teacher scolded them. "
                    " Just a little scolding, nothing too serious. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for you to go help someone again. "
                    " You wait for every student to get into their respective classrooms before you started looking for anyone who might need help. "
                    pause 2.0
                    jump helpclass1
                " I'm busy, sorry ":
                    hide msemilyshock at bottom
                    show msemilysad at center
                    mse " Ah, okay... "
                    mse " I'll go and find others to help then! "
                    mse " I'll talk with you later, [name]! "
                    hide msemilysad at right with easeoutright
                    " ...Let's just make sure no students are doing anything bad for the rest of the break. "
                    " You didn't have anything else to do anyway. "
                    scene black with dissolve
                    " You spent the rest of the break monitoring the halls. "
                    " Thankfully, you didn't see any students breaking the rules or anything. "
                    " You do hope that Miss Emily finds that kids bracelet soon... "
                    " It's not nice to have something important lost. "
                    " While you were monitoring the halls, you also secretly looked around to look for the bracelet. "
                    " ...You couldn't find anything though, unfortunately. "
                    " Looks like Miss Emily's gonna have to go through the entire school... "
                    " And students to ask them where they last saw a bracelet. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for you to go help someone again. "
                    " You wait for every student to get into their respective classrooms before you started looking for anyone who might need help. "
                    pause 2.0
                    jump helpclass1
        else:
            " You walk over to her, and she seems a little panicked. "
            " Wondering why she's so worried, you tapped her shoulder to get her attention and asked her what was wrong. "
            x " O-oh, [name]! Thank goodness you're here! "
            $ emilyknow = True
            mse " I'm Miss Emily - history teacher - and I uh... "
            mse " You see, one of our younger students apparently lost their bracelet. "
            mse " Apparently it was with them before they went to class, and now it's just...gone! "
            mse " That bracelet was very special to them since it was from their older sibling! "
            mse " Uh, if it doesn't bother you... "
            mse " Could you help out a bit? Go and look around the school? "
            mse " It's okay if not though! I'll go and ask someone else, if that's the case... "
            " ...Should you help her look? "
            menu:
                " Of course ":
                    $ emilylv += 10
                    hide msemilyshock at bottom
                    show msemilyneutral at center
                    mse " Whew, thanks [name]... "
                    mse " Things would've been a bit harder for me if I looked around alone. "
                    mse " How about I ask the students, and you look around? "
                    mse " I've already got Mister Demi searching around the school, so with you helping along it's going to be way faster! "
                    mse " Thanks again for your help, [name]... "
                    mse " Before I go, the bracelet is blue. Different shades of blue. "
                    hide msemilyneutral at right with easeoutright
                    " Well, time to get searching. "
                    " You looked at the area around you, and didn't see any bracelets. Unfortunately. "
                    " This is gonna take awhile, isn't it? "
                    " Well, too bad. You're dealing with this now. "
                    scene black with dissolve
                    " You spent the rest of the break helping a kid find their bracelet. "
                    " Eventually, you found it. It was in a trash can. "
                    " Miss Emily asked around for why it was in the trash can, and turns out, another student had borrowed it... "
                    " ...And had thrown it there. Let's just say you, Miss Emily, and the other teacher scolded them. "
                    " Just a little scolding, nothing too serious. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for you to go help someone again. "
                    " You wait for every student to get into their respective classrooms before you started looking for anyone who might need help. "
                    pause 2.0
                    jump helpclass1
                " I'm busy, sorry ":
                    hide msemilyshock at bottom
                    show msemilysad at center
                    mse " Ah, okay... "
                    mse " I'll go and find others to help then! "
                    mse " I'll talk with you later, [name]! "
                    hide msemilysad at right with easeoutright
                    " ...Let's just make sure no students are doing anything bad for the rest of the break. "
                    " You didn't have anything else to do anyway. "
                    scene black with dissolve
                    " You spent the rest of the break monitoring the halls. "
                    " Thankfully, you didn't see any students breaking the rules or anything. "
                    " You do hope that Miss Emily finds that kids bracelet soon... "
                    " It's not nice to have something important lost. "
                    " While you were monitoring the halls, you also secretly looked around to look for the bracelet. "
                    " ...You couldn't find anything though, unfortunately. "
                    " Looks like Miss Emily's gonna have to go through the entire school... "
                    " And students to ask them where they last saw a bracelet. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for you to go help someone again. "
                    " You wait for every student to get into their respective classrooms before you started looking for anyone who might need help. "
                    pause 2.0
                    jump helpclass1
label helpclass1:
    scene hallway with dissolve
    " You found three classrooms that needed help. "
    " Which teacher should you help? "
    # science, music, history
    if bloomieknow,demiknow,emilyknow == True:
        menu:
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump MY
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump COMPASS
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump ISCURIOUSITY
    elif bloomieknow,demiknow == True and emilyknow == False:
        menu:
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump MY
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump COMPASS
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump ISCURIOUSITY
    elif bloomieknow,emilyknow == True and demiknow == False:
        menu:
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump MY
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump COMPASS
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump ISCURIOUSITY
    elif demiknow,emilyknow == True and bloomieknow == False:
        menu:
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump MY
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump COMPASS
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump ISCURIOUSITY
    elif bloomieknow == True and demiknow,emilyknow == False:
        menu:
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump MY
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump COMPASS
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump ISCURIOUSITY
    elif demiknow == True and bloomieknow,emilyknow == False:
        menu:
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump MY
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump COMPASS
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump ISCURIOUSITY
    elif emilyknow == True and bloomieknow,demiknow == False:
        menu:
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump MY
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump COMPASS
            " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                jump ISCURIOUSITY
    else:
        menu:
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump MY
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump COMPASS
            " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                jump ISCURIOUSITY
label MY:
    $ bloomielv += 10
    # making sure the students were paying attention
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    " You walk into the classroom and saw Miss Bloomie demonstrating how to make a certain potion. "
    " Though, from what you saw...the students weren't exactly paying attention to her. "
    show missbloomieneutral at center with easeinleft
    if bloomieknow == True:
        msb " Okay, so you mix this...and you mix that... "
        " Miss Bloomie pours two funny looking potions into another bottle. "
        " You don't really know what she was doing, science wasn't really your thing. "
        " It did look a little cool when it did a tiny explosion. "
        msb " Aaaand that's how you make this potion. "
        msb " For your activity today, I want all of you to make the same potion I just made with the same exact steps. "
        " ...Yeah, you could tell that none of the students memorized that. "
        " You could see there was a few, but that few was only like...3 students who took that down. "
        msb " ... "
        msb " Start now. "
        " Everyone started working on their projects, though... "
        " ...They REALLY looked like they were struggling. "
        hide missbloomieneutral at bottom
        show missbloomiesad at center
        " You could see the utter disappointment on Miss Bloomie's face. "
        " She was clearly expecting better than this... "
        " ...You wanted to help her out though, so you did. You walked up to her and asked her if she needed help. "
        msb " ...I think my answer is quite obvious. "
        msb " Please, just teach them how to make the potion I just made... "
        msb " My disappointment is immeasurable and my day is ruined. "
        msb " It's gonna be hard if I gave you the scientific names, so I'll just describe them by color. "
        msb " Red potion, then green potion, then purple potion. Got that? "
        msb " Remember all that. "
        " You gave her a thumbs up before you went over to each student to teach them how to make the potion. "
        scene black with dissolve
        " You spent Miss Bloomie's class teaching students how to make a certain potion. "
        " You were kinda baffled on how they didn't memorize, considering it was a three step thing. "
        " But then again, you could see them using their phones...talking to eachother... "
        " Being too distracted overall and not learning anything. Classic students. "
        " They should probably take away their phones everytime they start class. "
        " Probably, but you know that the students wouldn't really like that idea that much. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, and eventually the students were done with their potions. "
        " Some didn't quite get it, but atleast they tried, I guess...? "
        " Wait, how'd they not even understa -...oh right, the classroom was being a bit too loud. "
        " Sigh...the normal day of a teacher. "
        " You waited for the students to get out of the classroom and pass their work to Miss Bloomie before you went out aswell. "
        " You need a break after all of that happening. "
        pause 2.0
        jump ttbreak2
    else:
        x " Okay, so you mix this...and you mix that... "
        " The science teacher pours two funny looking potions into another bottle. "
        " You don't really know what she was doing, science wasn't really your thing. "
        " It did look a little cool when it did a tiny explosion. "
        x " Aaaand that's how you make this potion. "
        x " For your activity today, I want all of you to make the same potion I just made with the same exact steps. "
        " ...Yeah, you could tell that none of the students memorized that. "
        " You could see there was a few, but that few was only like...3 students who took that down. "
        x " ... "
        x " Start now. "
        " Everyone started working on their projects, though... "
        " ...They REALLY looked like they were struggling. "
        hide missbloomieneutral at bottom
        show missbloomiesad at center
        " You could see the utter disappointment on the teachers face. "
        " She was clearly expecting better than this... "
        " ...You wanted to help her out though, so you did. You walked up to her and asked her if she needed help. "
        x " ...I think my answer is quite obvious. "
        $ bloomieknow = True
        msb " I'm Miss Bloomie by the way, science teacher... "
        msb " Please, just teach them how to make the potion I just made... "
        msb " My disappointment is immeasurable and my day is ruined. "
        msb " It's gonna be hard if I gave you the scientific names, so I'll just describe them by color. "
        msb " Red potion, then green potion, then purple potion. Got that? "
        msb " Remember all that. "
        " You gave her a thumbs up before you went over to each student to teach them how to make the potion. "
        scene black with dissolve
        " You spent Miss Bloomie's class teaching students how to make a certain potion. "
        " You were kinda baffled on how they didn't memorize, considering it was a three step thing. "
        " But then again, you could see them using their phones...talking to eachother... "
        " Being too distracted overall and not learning anything. Classic students. "
        " They should probably take away their phones everytime they start class. "
        " Probably, but you know that the students wouldn't really like that idea that much. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, and eventually the students were done with their potions. "
        " Some didn't quite get it, but atleast they tried, I guess...? "
        " Wait, how'd they not even understa -...oh right, the classroom was being a bit too loud. "
        " Sigh...the normal day of a teacher. "
        " You waited for the students to get out of the classroom and pass their work to Miss Bloomie before you went out aswell. "
        " You need a break after all of that happening. "
        pause 2.0
        jump ttbreak2
label COMPASS:
    $ demilv += 10
    # helping with activities (demi needs ideas)
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    " You walked into the classroom and saw that the students were doing a group activity. "
    " You looked around and saw that the music teacher was just chilling in the corner. "
    " You walked up to him and asked him what he was doing. "
    show mrdemineutral at center with easeinright
    if demiknow == True:
        msd " Oh, um...hey, [name]... "
        msd " I'm letting my students do a group activity right now... "
        msd " But...I fear that it's a tad bit unoriginal... "
        msd " And the students aren't having fun... "
        " You look at what the students were doing and it seemed like they were having fun. "
        " You looked back at Mister Demi and reassured him that they were having fun and he was fine. "
        msd " Really...? That's good... "
        msd " But, I've been thinking... "
        msd " I want to do another activity, but I have no clue on what to make them do... "
        msd " I asked Miss Grace about it and she just said to do whatever... "
        hide mrdemineutral at bottom
        show mrdemisurprised at center
        msd " I don't even know 'whatever' means!! "
        msd " Look, I just need a nice new idea so that I can keep my class happy and entertained... "
        msd " ...And also learning, of course... "
        msd " I've tried asking the other teachers on what I should do but... "
        msd " ...Everything they've said, I've already done... "
        msd " This sucks, really.. "
        " Seems like Mister Demi really needs some help, eh? "
        " You tried to think of something original to help Mister Demi out... "
        " ...You them came up with an idea related to singing. "
        hide mrdemisurprised at bottom
        show mrdemineutral at center
        msd " ...Singing...? "
        msd " Actually, I haven't done that yet... "
        msd " I don't know what to do with singing, but I'll try to come up with something...! "
        hide mrdemineutral at bottom
        show mrdemihappy at center
        msd " Thank you for the help, [name]...! "
        scene black with dissolve
        " You spent the rest of the break discussing with Mister Demi on what he could do. "
        " It was a nice conversation, until everyone in his class was done with the activity he gave them. "
        " You helped him on rating and grading what the students did aswell. Why? because why not. "
        " You need to have some sort of help, after all. Not just give Mister Demi advice on what he should do. "
        play sound "audio/bellring.mp3"
        " The bell rings after you and Demi were done rating and grading. "
        " You watched the students leave the classroom, before you left to go out to the hallways. "
        pause 2.0
        jump ttbreak2
    else:
        x " Oh, um...hey, [name]... "
        $ demiknow = True
        msd " I'm Mister Demi, by the way...Music teacher...And what I'm doing..? "
        msd " I'm letting my students do a group activity right now... "
        msd " But...I fear that it's a tad bit unoriginal... "
        msd " And the students aren't having fun... "
        " You look at what the students were doing and it seemed like they were having fun. "
        " You looked back at Mister Demi and reassured him that they were having fun and he was fine. "
        msd " Really...? That's good... "
        msd " But, I've been thinking... "
        msd " I want to do another activity, but I have no clue on what to make them do... "
        msd " I asked Miss Grace about it and she just said to do whatever... "
        hide mrdemineutral at bottom
        show mrdemisurprised at center
        msd " I don't even know 'whatever' means!! "
        msd " Look, I just need a nice new idea so that I can keep my class happy and entertained... "
        msd " ...And also learning, of course... "
        msd " I've tried asking the other teachers on what I should do but... "
        msd " ...Everything they've said, I've already done... "
        msd " This sucks, really.. "
        " Seems like Mister Demi really needs some help, eh? "
        " You tried to think of something original to help Mister Demi out... "
        " ...You them came up with an idea related to singing. "
        hide mrdemisurprised at bottom
        show mrdemineutral at center
        msd " ...Singing...? "
        msd " Actually, I haven't done that yet... "
        msd " I don't know what to do with singing, but I'll try to come up with something...! "
        hide mrdemineutral at bottom
        show mrdemihappy at center
        msd " Thank you for the help, [name]...! "
        scene black with dissolve
        " You spent the rest of the break discussing with Mister Demi on what he could do. "
        " It was a nice conversation, until everyone in his class was done with the activity he gave them. "
        " You helped him on rating and grading what the students did aswell. Why? because why not. "
        " You need to have some sort of help, after all. Not just give Mister Demi advice on what he should do. "
        play sound "audio/bellring.mp3"
        " The bell rings after you and Demi were done rating and grading. "
        " You watched the students leave the classroom, before you left to go out to the hallways. "
        pause 2.0
        jump ttbreak2
label ISCURIOUSITY:
    $ emilylv += 10
    # deciding when to hold a group projecr
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    " You walked into the classroom to find it really quiet. "
    " Wondering why, you look around and turns out the students were doing a few tests. "
    " You also saw that the history teacher was trying to figure something out on her phone. "
    " Curious, you walked over to her and asked her if she needed any help. "
    show msemilyneutral at center with easeinleft
    if emilyknow == True:
        mse " ...Hmmm...what should I do...? "
        mse " Ah, hello [name]. "
        mse " I'm letting my students have a test right now, buuuuut... "
        mse " I'm just trying to figure out when I should do an activity I have planned. "
        mse " You see, Miss grace lets us do absolutely anything with our students... "
        mse " ...Except slacking off and of course being a weirdo with them. "
        mse " We can't just slack off, and it's completely illegal to be like that with a student. "
        mse " I've been thinking...should I make them do the activity tomorrow or on Thursday? "
        " You thought about it for a moment, when would be a good time to do an activity? "
        " ...You came up with an answer, and you told her that she should do it tomorrow. "
        hide msemilyneutral at bottom
        show msemilyhappy at center
        mse " Alrighty! Thank you, [name]. "
        mse " Let's hang out for a bit, yeah? "
        " You were actually about to leave, but you didn't mind wanting to hang out with Miss Emily for a bit. "
        " You grabbed an extra chair next to her and sat down, quietly talking to eachother to not disturb the students. "
        scene black with dissolve
        " You spent the rest of the break talking with Miss Emily. "
        " She would talk about random things, like her pet cat.. and the stupid things her students did. "
        " Honestly the thing that caught your attention was her cat. "
        " She even showed you a picture of it, and it was just so PHAT and adorable. "
        " You honestly want a cat too... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, and the students pass their papers to Miss Emily. "
        " You helped Miss Emily arrange her papers after all of them were done. "
        " And after you were done with that, you walked out of her classroom to chill a bit in the hallways. "
        pause 2.0
        jump ttbreak2
    else:
        x " ...Hmmm...what should I do...? "
        x " Ah, hello [name]. "
        $ emilyknow = True
        mse " I'm Miss Emily by the way, the history teacher. "
        mse " I'm letting my students have a test right now, buuuuut... "
        mse " I'm just trying to figure out when I should do an activity I have planned. "
        mse " You see, Miss grace lets us do absolutely anything with our students... "
        mse " ...Except slacking off and of course being a weirdo with them. "
        mse " We can't just slack off, and it's completely illegal to be like that with a student. "
        mse " I've been thinking...should I make them do the activity tomorrow or on Thursday? "
        " You thought about it for a moment, when would be a good time to do an activity? "
        " ...You came up with an answer, and you told her that she should do it tomorrow. "
        hide msemilyneutral at bottom
        show msemilyhappy at center
        mse " Alrighty! Thank you, [name]. "
        mse " Let's hang out for a bit, yeah? "
        " You were actually about to leave, but you didn't mind wanting to hang out with Miss Emily for a bit. "
        " You grabbed an extra chair next to her and sat down, quietly talking to eachother to not disturb the students. "
        scene black with dissolve
        " You spent the rest of the break talking with Miss Emily. "
        " She would talk about random things, like her pet cat.. and the stupid things her students did. "
        " Honestly the thing that caught your attention was her cat. "
        " She even showed you a picture of it, and it was just so PHAT and adorable. "
        " You honestly want a cat too... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, and the students pass their papers to Miss Emily. "
        " You helped Miss Emily arrange her papers after all of them were done. "
        " And after you were done with that, you walked out of her classroom to chill a bit in the hallways. "
        pause 2.0
        jump ttbreak2
label ttbreak2:
    scene hallway with dissolve
    " You didnt really spot any of your teacher friends out in the hallway... "
    " Maybe they're busy doing something? "
    " Oh well...more free time and alonetime for you, I suppose. "
    " Let's just make you walk around. "
    " Not like you have anything else to do than that, right? "
    scene black with dissolve
    " You spent the rest of the break walking around the hallways... "
    " ...Making sure none of the kids were causing trouble. "
    " You did catch some kids bullying another kid, and you scolded them for doing so. "
    " ...They threw you a bar of soap in the face in response and ran away. "
    " What an interesting group of kids. "
    " You help the bullied kid and made sure they were okay... "
    " Before you went back to what you were doing earlier. "
    " And that was to walk around the school and make sure that no one is causing trouble. "
    " And doing absolutely and utterly nothing. "
    " So hard working! "
    play sound "audio/bellring.mp3"
    " The bell rings, looks like it's time for you to go help someone again. "
    " You wait for every student to get into their respective classrooms before you started looking for anyone who might need help. "
    pause 2.0
    jump helpclass2
label helpclass2:
    # sasha, thavel
    scene hallway with dissolve
    " You found about two classrooms that needed help. "
    " Which teacher should you help? "
    if sashaknow == True and thavelknow == True:
        menu:
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump wouldntyouliketoknow
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump weathergirl
    elif sashaknow == True and thavelknow == False:
        menu:
            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                jump wouldntyouliketoknow
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump weathergirl
    elif sashaknow == False and thavelknow == True:
        menu:
            " {image=sashaicon}The art teacher {image=sashaicon} ":
                jump wouldntyouliketoknow
            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                jump weathergirl
    else:
        menu:
            " {image=sashaicon} The art teacher{image=sashaicon} ":
                jump wouldntyouliketoknow
            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                jump weathergirl
label wouldntyouliketoknow:
    $ sashalv += 10
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    " You walk into the classroom and spotted the art teacher having her students draw for a bit. "
    " Though, she looks a little troubled herself. "
    " Wondering why, you decided to walk up to her and ask what's wrong. "
    show sashasad at center with easeinleft
    if sashaknow == True:
        mss " Oh dear, this isn't good... "
        " You poked her shoulder to get her attention, then asked what was wrong. "
        hide sashasad at bottom
        show sashaneutral at center
        mss " Hi, [name]! I'm kind of...a little bit running low of storage. "
        mss " You see, I accidentally ordered too much paint buckets and art supplies... "
        mss " Annnnd my office is running out of space on where to put them... "
        mss " I kind of need some containers so that I could properly arrange things... "
        mss " And so that my office doesn't look too cluttered. "
        mss " Do you happen to have any containers to put my stuff in? It's alright if not. "
        " You thought for a bit, but then told her that you might need to check your classroom for some. "
        " You told her that you'll be right back. "
        hide sashaneutral at bottom
        show sashahappy at center
        mss " Okay! I'll be waiting, [name]! "
        scene black with dissolve
        " You left Miss Sasha's classroom to check if your classroom has any containers. "
        " You're sure you have some, incase if you bought too much stuff. "
        pause 1.0
        scene gardenroom with dissolve
        " You looked around your classroom... "
        " ...And found four containers! Two big, two small. "
        " This would be good for Miss Sasha...let's head back. "
        scene black with dissolve
        pause 1.0
        scene classroom with dissolve
        show sashaneutral at center with dissolve
        " You walked back into Sasha's classroom and showed her the containers you found. "
        hide sashaneutral at bottom
        show sashahappy at center
        mss " These are actually really perfect, [name]! "
        mss " Hold on...are you really sure that you don't mind me having them? "
        mss " I mean, I could just buy some containers... "
        " You nodded, you're gonna let her keep these. "
        " Cause why not? you're feeling nice today. "
        mss " Wow...thanks, [name]! You're so nice! "
        mss " Hmm...to repay you, how about we have some coffee? "
        mss " I accidentally made two for myself, hehe. "
        " ...You ask her how could she possibly make two for herself. "
        hide sashahappy at bottom
        show sashaneutral at center
        mss " Weeeeell, I was busy painting while letting the students paint themselves, right? "
        mss " I go and make coffee for myself and put it on my counter... "
        mss " ...I continue painting, and after a few minutes I go to make coffee again, thinking I hadn't already made one... "
        mss " And when I came back, I realized I had made two...oopsies. "
        mss " So... you wanna drink some coffee with me and talk? "
        " You don't see why not. You didn't have anything else to do anyway. "
        hide sashaneutral at bottom
        show sashahappy at center
        mss " Yay!! Cmere, I have an extra seat. "
        scene black with dissolve
        " You spent the rest of the class talking with Miss Sasha and drinking coffee with her. "
        " You're still a little flabbergasted that she somehow managed to make two cups of coffee though. "
        " It's a little silly, but also kinda cute that she can forget easily. "
        " SHE'S JUST LIKE ME FOR REA{nw} "
        play sound "audio/bellring.mp3"
        " The bell rings, and the students pass all of their work to Miss Sasha. "
        " Miss Sasha collects all of them, and you watch the students exit out of the classroom before you do. "
        pause 2.0
        jump ttbreak3
    else:
        x " Oh dear, this isn't good... "
        " You poked her shoulder to get her attention, then asked what was wrong. "
        hide sashasad at bottom
        show sashaneutral at center
        x " Hi, [name]! I'm kind of...a little bit running low of storage. "
        $ sashaknow = True
        mss " I'm Miss Sasha by the way - Art teacher... "
        mss " You see, I accidentally ordered too much paint buckets and art supplies... "
        mss " Annnnd my office is running out of space on where to put them... "
        mss " I kind of need some containers so that I could properly arrange things... "
        mss " And so that my office doesn't look too cluttered. "
        mss " Do you happen to have any containers to put my stuff in? It's alright if not. "
        " You thought for a bit, but then told her that you might need to check your classroom for some. "
        " You told her that you'll be right back. "
        hide sashaneutral at bottom
        show sashahappy at center
        mss " Okay! I'll be waiting, [name]! "
        scene black with dissolve
        " You left Miss Sasha's classroom to check if your classroom has any containers. "
        " You're sure you have some, incase if you bought too much stuff. "
        pause 1.0
        scene gardenroom with dissolve
        " You looked around your classroom... "
        " ...And found four containers! Two big, two small. "
        " This would be good for Miss Sasha...let's head back. "
        scene black with dissolve
        pause 1.0
        scene classroom with dissolve
        show sashaneutral at center with dissolve
        " You walked back into Sasha's classroom and showed her the containers you found. "
        hide sashaneutral at bottom
        show sashahappy at center
        mss " These are actually really perfect, [name]! "
        mss " Hold on...are you really sure that you don't mind me having them? "
        mss " I mean, I could just buy some containers... "
        " You nodded, you're gonna let her keep these. "
        " Cause why not? you're feeling nice today. "
        mss " Wow...thanks, [name]! You're so nice! "
        mss " Hmm...to repay you, how about we have some coffee? "
        mss " I accidentally made two for myself, hehe. "
        " ...You ask her how could she possibly make two for herself. "
        hide sashahappy at bottom
        show sashaneutral at center
        mss " Weeeeell, I was busy painting while letting the students paint themselves, right? "
        mss " I go and make coffee for myself and put it on my counter... "
        mss " ...I continue painting, and after a few minutes I go to make coffee again, thinking I hadn't already made one... "
        mss " And when I came back, I realized I had made two...oopsies. "
        mss " So... you wanna drink some coffee with me and talk? "
        " You don't see why not. You didn't have anything else to do anyway. "
        hide sashaneutral at bottom
        show sashahappy at center
        mss " Yay!! Cmere, I have an extra seat. "
        scene black with dissolve
        " You spent the rest of the class talking with Miss Sasha and drinking coffee with her. "
        " You're still a little flabbergasted that she somehow managed to make two cups of coffee though. "
        " It's a little silly, but also kinda cute that she can forget easily. "
        " SHE'S JUST LIKE ME FOR REA{nw} "
        play sound "audio/bellring.mp3"
        " The bell rings, and the students pass all of their work to Miss Sasha. "
        " Miss Sasha collects all of them, and you watch the students exit out of the classroom before you do. "
        pause 2.0
        jump ttbreak3
label weathergirl:
    $ thavellv += 10
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    " You walked into the classroom and saw that the students were doing a worksheet. "
    " Seriously, is everyone just doing worksheets and activities today? "
    " Not like you're complaining, atleast you don't feel like you're interrupting something. "
    " You noticed the language teacher at her desk, seemingly thinking deeply. "
    " You wanted to talk to her for a bit, so you did. Walked up to her and asked what she was thinking about. "
    show msthravelneutral at center with easeinleft
    if thavelknow == True:
        mst " Hola, [name]. "
        mst " I was just thinking about how I could help my students improve in speaking a certain language. "
        mst " I'm very much not going to tell them to use duolingo, after the recent stuff that happened, apparently. "
        mst " I mean, AI to teach people? "
        mst " That's just as pointless as using google translate to lie about where you came from. "
        mst " Like: Oh, I'm from Spain! and then they proceed to tell a person who's actually from Spain some random gibberish. "
        mst " Or just completely broken spanish words. "
        mst " Jesus christ...using AI for everything is getting really boring. "
        mst " And also really annoying. "
        mst " But enough of the AI talk, I need help on how I can improve my students speaking in other languages. "
        mst " Since, clearly they don't have the time to study on their own. "
        mst " Do you perhaps have any ideas? "
        " You thought about it for a few moments... "
        " ...You then came up with an idea. How about Miss Thavel does this extra activity where she teaches a few students on some languages? "
        " The ones that are most likely struggling, of course. "
        " And also this would only include students who actually wanted to learn. "
        " You knew only a few would participate, but atleast it's something. "
        mst " Hm...that doesn't sound too bad. "
        hide msthravelneutral at bottom
        show msthravelhappy at center
        mst " I'll try out your idea later, [name]. Thank you! "
        scene black with dissolve
        " You spent the rest of the class talking about your idea to Miss Thavel. "
        " Whilst you were talking to her, you could see that a few students were listening to your conversation. "
        " You already knew what they were thinking: Oh hell no, I'm definitely not participating in that. "
        " You could understand why...they probably just want to go home already. "
        " Not gonna lie, you wanted to go home too. "
        " But you can't since you know that Miss Grace will kick your ass. "
        " Womp womp. "
        play sound "audio/bellring.mp3"
        " The bell rings, and all of the students pass their worksheets to Miss Thavel. "
        " You wait for the students to get out of the classroom, before you did. "
        pause 2.0
        jump ttbreak3
    else:
        x " Hola, [name]. "
        $ thavelknow = True
        mst " I'm Miss Thavel, the language teacher. "
        mst " I was just thinking about how I could help my students improve in speaking a certain language. "
        mst " I'm very much not going to tell them to use duolingo, after the recent stuff that happened, apparently. "
        mst " I mean, AI to teach people? "
        mst " That's just as pointless as using google translate to lie about where you came from. "
        mst " Like: Oh, I'm from Spain! and then they proceed to tell a person who's actually from Spain some random gibberish. "
        mst " Or just completely broken spanish words. "
        mst " Jesus christ...using AI for everything is getting really boring. "
        mst " And also really annoying. "
        mst " But enough of the AI talk, I need help on how I can improve my students speaking in other languages. "
        mst " Since, clearly they don't have the time to study on their own. "
        mst " Do you perhaps have any ideas? "
        " You thought about it for a few moments... "
        " ...You then came up with an idea. How about Miss Thavel does this extra activity where she teaches a few students on some languages? "
        " The ones that are most likely struggling, of course. "
        " And also this would only include students who actually wanted to learn. "
        " You knew only a few would participate, but atleast it's something. "
        mst " Hm...that doesn't sound too bad. "
        hide msthravelneutral at bottom
        show msthravelhappy at center
        mst " I'll try out your idea later, [name]. Thank you! "
        scene black with dissolve
        " You spent the rest of the class talking about your idea to Miss Thavel. "
        " Whilst you were talking to her, you could see that a few students were listening to your conversation. "
        " You already knew what they were thinking: Oh hell no, I'm definitely not participating in that. "
        " You could understand why...they probably just want to go home already. "
        " Not gonna lie, you wanted to go home too. "
        " But you can't since you know that Miss Grace will kick your ass. "
        " Womp womp. "
        play sound "audio/bellring.mp3"
        " The bell rings, and all of the students pass their worksheets to Miss Thavel. "
        " You wait for the students to get out of the classroom, before you did. "
        pause 2.0
        jump ttbreak3
label ttbreak3:
    scene hallway with dissolve
    " You didn't see any of your teacher friends in the hallway again... "
    " Though, you did think of a few places where you could relax for a bit. "
    " Where should you go? "
    menu:
        " The rooftop ":
            scene black with dissolve
            pause 2.0
            jump flavor
        " The back of the school ":
            scene black with dissolve
            pause 2.0
            jump foley
        " Your classroom ":
            scene black with dissolve
            pause 2.0
            jump mikumikumiku
    label flavor:
        scene rooftop with dissolve
        " You walk up to the rooftop, seeing a few students wandering around and vibing. "
        " You look around for a place to sit and you found an empty bench on one of the corners of the rooftop. "
        " Perfect...though this makes you look like some weird edgy teacher. "
        " You sat down and relaxed a bit, looking at the nice sky. "
        " The sky looks nice today. It always does, but you never really took the time to appreciate it with how busy you are now. "
        " Now you can though. Listening to the students having fun while you just relax... "
        " The birds chirping and flying around in the sky, being free... "
        " It's all very nice, but you still gotta do something productive otherwise miss Grace is gonna kick your ass. "
        " You pull out your phone and try to remember what you're supposed to do for your next class. "
        " ... "
        " All you know is that you're supposed to teach them gardening or some shit. "
        " Then again, from what you've heard...Miss Grace just lets you and the other teachers teach them whatever. "
        " Not whatever as in everything, you can't teach certain topics of course. "
        " But still... Hm... "
        " Maybe you should teach them how to not be a dumbass in gardening. "
        " But then again, you know that your students aren't dumb to the point they are dumbasses. In gardening. "
        " But you also know that there's probably gonna be some who are. "
        " Which kinda flabbergasts you a bit. "
        " You gotta act as a nice and kind teacher though... "
        " A supportive and patient teacher... "
        scene black with dissolve
        " You spent the rest of the break thinking about what you could do for your next class. "
        " And also vibing here and there of course. "
        " You should probably go and have a nice break sometime... "
        " Go to a pool and take care of yourself for a bit... "
        " ...If you even have the money to go there. "
        " Atleast this job doesn't pay you 1$ for finishing a single day here. "
        " You get 10$ an hour! (...this is a joke. Of course you get more than that.) "
        " (Wow, a teacher not being underpaid? surprising.) "
        play sound "audio/bellring.mp3"
        " The bell rings, looks like it's time for you to go help someone again. "
        " You walk down the rooftop and looked at all of the students skedaddling to go on their way to class. "
        " You wait for every student to get into their respective classrooms before you started looking for anyone who might need help. "
        pause 2.0
        jump helpclass3
    label foley:
        scene paperschoolback with dissolve
        " You walked to the back of the school, and sat down on one of the benches that you saw was there. "
        " You looked around and spotted an emo kid listening to some music... "
        " ...Wait, is that monitoring by hatsune miku? "
        " He's listening to absolute peak. You didn't know students here knew peak music. "
        " You decided not to talk about it to him though, you didn't want to look weird. "
        " Like, who just goes up to someone and ask: "
        " Hey! Is that monitoring by hatsune miku? "
        " That just makes you look like you've been watching them for a good while now. "
        " And it also makes it more weird since you're a teacher and that's a kid. "
        " It would make it even more weird since teachers don't usually look like the type of people to listen to hatsune miku. "
        " ...You should probably think about something else. You don't wanna keep on thinking about weird stuff. "
        " You look around the area you're in, looking at the trees and other things... "
        " Then you spot that someone, most likely a student has planted a few flowers near you. "
        " Pretty cool... "
        " You wanted to give them a few gardening tips, being the teacher you are. "
        " You just happened to have a few seeds lying in your pockets. "
        " How'd you get those in there? You're a gardening teacher. Who knows if you need them. "
        " You place about two seed packets near the flowers incase if the person comes back to check on their flowers... "
        " You also take a photo so that you could post this on facebook and act like your average facebook mom. "
        " oh my god a student did a great job at planting these flowers heart emoji heart emoji heart emoj "
        " ...You get the idea. "
        scene black with dissolve
        " You spent the rest of the break just vibing in the back of the school. "
        " Relaxing, and doing your own thing... "
        " Just completely vibing and thinking about stuff. "
        " Just being a silly little creature in a big serious world. "
        " Sometimes, you can be a silly little creature instead of being serious. "
        play sound "audio/bellring.mp3"
        " The bell rings, looks like it's time for you to go help someone again. "
        " You walk back into the hallways and watched the students skedaddle to their classrooms. "
        " You wait for every student to get into their respective classrooms before you started looking for anyone who might need help. "
        pause 2.0
        jump helpclass3
    label mikumikumiku:
        scene gardenroom with dissolve
        " You walked into your own classroom. Pretty empty, but also looks really nice. "
        " You're thinking about what you could do while you're here... "
        " Something to atleast pass your time for just a bit. "
        " Maybe you could arrange a few things? "
        " Your classroom {i}is{/i} getting a tad bit messy... "
        " Especially after your class yesterday. "
        " Yeah, let's just arrange your stuff to make things look nicer. "
        " Let's get to work! "
        scene black with dissolve
        " You spent the rest of your break fixing up your classroom. "
        " Arranging your plants and things... "
        " Cleaning up dust and some cobwebs in the corners... "
        " Jesus, this classroom must've not been used in awhile with how much dirt there is. "
        " How sad... "
        " Atleast everything's clean now though! Nice and clean, just like how you and others like it. "
        " You wouldn't want your students to be sitting in filth after all. "
        " They simply just deserve the best! "
        " What a great teacher you are! "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like you gotta go help someone again. "
        " You finish things up in your classroom, before you go out and saw all the students skedaddling to their classrooms. "
        " You wait for every student to get into their respective classrooms before you started looking for anyone who might need help. "
        pause 2.0
        jump helpclass3
label helpclass3:
    scene hallway with dissolve
    " You walked out of your classroom, and found two teachers who need your help. "
    " Who do you help, though? "
    if demiknow == True and bloomieknow == True:
        menu:
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump shake1
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump shake2
    elif demiknow == True and bloomieknow == False:
        menu:
            " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                jump shake1
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump shake2
    elif demiknow == False and bloomieknow == True:
        menu:
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump shake1
            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                jump shake2
    else:
        menu:
            " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                jump shake1
            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                jump shake2
label shake1:
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    if demiknow == True:
        " You walk into the classroom and spotted Mister Demi having his normal class. "
    else:
        " You walk into the classroom and spotted the music teacher having his normal class. "
    " Well, this certainly feels like you're interrupting something. "
    " Atleast the students are ignoring you as if this is a normal thing. "
    " Makes you feel less awkward. "
    " You just sit in one of the extra chairs and wait for the teacher to say if he needed help or anything. "
    show mrdemineutral at center with easeinleft
    if demiknow == True:
        msd " And this class, is the - "
        " Mister Demi gets interrupted as he gets a call on his phone. "
        hide mrdemineutral at bottom
        show mrdemisurprised at center
        msd " ... "
        hide mrdemisurprised at bottom
        show mrdemineutral at center
        msd " ...One moment, class. "
        msd " I have to take a call real quick, please don't do anything stupid whilst I'm away... "
        " He looks at you and basically gives you an expression that screams: "
        " PLEASE make sure they don't do anything stupid I beg of you please please please plea "
        hide mrdemineutral at right with easeoutright
        " ...He then left. "
        " The students were being surprisingly silent while Mister Demi was out of the room. "
        " Probably because they noticed that you were there. "
        " Wow! You're already being respected! "
        " Either that or they probably don't know that you're secretly chill. "
        " Probably. "
        " Mister Demi comes back into his classroom after a bit. "
        show mrdemineutral at center with easeinright
        msd " Um...Okay, class... "
        msd " I'll be gone for a bit, due to some issues that popped up... "
        msd " ([fancy] [name], are you fine with taking over for a bit..?) "
        " Well, you're here to help. "
        " Of course you agreed. "
        msd " ...Okay, class - [fancy] [name] will be taking over for now... "
        msd " Please don't make [name] lose [their] sanity... "
        msd " Thank you... "
        " Mister Demi then left again. "
        hide mrdemineutral at right with easeoutright
        " Wonder what the issue was, to cause him to give you control over his class. "
        " Oh well, you'll ask him about it later. "
        " You walked up to the front of the class, and thought about what you should do... "
        " You put your hand in your pocket and found about 10 candies still in your pocket. "
        " Huh. Maybe you could do something with this. "
        " ...{p} WHOEVER ANSWERS RIGHT WINS A PIECE OF CANDY!! "
        scene black with dissolve
        " You spent the rest of the class asking Mister Demi's students questions about music... "
        " ...And whenever they got a question right, you'd give them a piece of candy. "
        " This went on until all of your candy was gone. "
        play sound "audio/bellring.mp3"
        " And also when the bell rang. "
        " Yes, your questions were that difficult to the point the bell rang. "
        " You watched the students leave the classroom before you left the classroom yourself. "
        pause 2.0
        jump ttbreak4
    else:
        $ demiknow = True
        " This must be Mister Demi... You've heard about a few teachers talk about him before. "
        " He seems a little anxious, but you were told that this is how he usually acts. "
        " Interesting. "
        msd " And this class, is the - "
        " Mister Demi gets interrupted as he gets a call on his phone. "
        hide mrdemineutral at bottom
        show mrdemisurprised at center
        msd " ... "
        hide mrdemisurprised at bottom
        show mrdemineutral at center
        msd " ...One moment, class. "
        msd " I have to take a call real quick, please don't do anything stupid whilst I'm away... "
        " He looks at you and basically gives you an expression that screams: "
        " PLEASE make sure they don't do anything stupid I beg of you please please please plea "
        hide mrdemineutral at right with easeoutright
        " ...He then left. "
        " The students were being surprisingly silent while Mister Demi was out of the room. "
        " Probably because they noticed that you were there. "
        " Wow! You're already being respected! "
        " Either that or they probably don't know that you're secretly chill. "
        " Probably. "
        " Mister Demi comes back into his classroom after a bit. "
        show mrdemineutral at center with easeinright
        msd " Um...Okay, class... "
        msd " I'll be gone for a bit, due to some issues that popped up... "
        msd " ([fancy] [name], are you fine with taking over for a bit..?) "
        " Well, you're here to help. "
        " Of course you agreed. "
        msd " ...Okay, class - [fancy] [name] will be taking over for now... "
        msd " Please don't make [name] lose [their] sanity... "
        msd " Thank you... "
        " Mister Demi then left again. "
        hide mrdemineutral at right with easeoutright
        " Wonder what the issue was, to cause him to give you control over his class. "
        " Oh well, you'll ask him about it later. "
        " You walked up to the front of the class, and thought about what you should do... "
        " You put your hand in your pocket and found about 10 candies still in your pocket. "
        " Huh. Maybe you could do something with this. "
        " ...{p} WHOEVER ANSWERS RIGHT WINS A PIECE OF CANDY!! "
        scene black with dissolve
        " You spent the rest of the class asking Mister Demi's students questions about music... "
        " ...And whenever they got a question right, you'd give them a piece of candy. "
        " This went on until all of your candy was gone. "
        play sound "audio/bellring.mp3"
        " And also when the bell rang. "
        " Yes, your questions were that difficult to the point the bell rang. "
        " You watched the students leave the classroom before you left the classroom yourself. "
        pause 2.0
        jump ttbreak4
label shake2:
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    if bloomieknow == True:
        " You walked into the classroom and found Miss Bloomie making students make potions. "
    else:
        " You walked into the classroom and found the science teacher making students make potions. "
    " Even with that serious look on her face... "
    " ...You could tell that she was troubled with something. "
    " You decided to walk up to her to see what's wrong. "
    show missbloomieneutral at center with easeinleft
    if bloomieknow == True:
        msb " ...No, no...this can't be good. "
        msb " This has to be the seventh report this month... "
        msb " I have to get the teachers to do something about this. "
        msb " Our school's reputation wouldn't look good if we don't do something for this. "
        " You ask her what's wrong. "
        msb " [name]. I'm pleased to see you here. "
        msb " Listen... "
        msb " I've had Miss Grace tell me something. "
        msb " Apparently, there's been a student that has been facing constant bullying. "
        msb " The moment they get into school - they get bullied. "
        msb " The moment they leave school - they get bullied. "
        msb " As long as they're breathing, they're getting bullied. "
        msb " It's getting worse and worse to be point the kid is considering... "
        msb " Doing something not good to themself. "
        msb " We've only been informed of this just now because of 3 students reporting of the situation. "
        msb " We also don't know why the kid that's been getting bullied themself hasn't reported the situation earlier. "
        msb " Probably too afraid to even say anything, otherwise they're gonna get into more trouble with those bullies. "
        msb " From what I've heard, Mister Demi and a few more teachers are already on the situation. "
        msb " The good thing is, we've managed to come in contact with the bullies. "
        msb " The only problem is that one of the bullies isn't even from this school. "
        msb " Sure, we could kick him out, but somehow he always manages to come back. "
        msb " Not to mention the fact that he's one of my favorite students. "
        msb " I...really don't know what to do. "
        msb " Another thing that I've heard is that they, the bullies, are planning to... "
        msb " Do something really dangerous to that kid I mentioned from before. "
        msb " ...I don't want that happening. "
        msb " I'm going to have to confront them after your class, [name]. "
        msb " If you ever see a kid that looks beaten up... "
        msb " ...Do your best to seperate them from those bullies. "
        msb " I feel if you even let them be close with them, they'll just bother them more. "
        msb " I trust that you'll do a good job in protecting that kid. "
        scene black with dissolve
        " You spent the rest of the class talking with Miss Bloomie about the situation that's been going on. "
        " This is...quite worrying. "
        " You've heard of bullying where people just...say mean words to someone, "
        " But you haven't seen people take it THIS far. "
        " All you could do is just pray for this kids safety. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, class is over. "
        " The students pass their work to Miss Bloomie and they all walk out of the classroom. "
        " You eventually walk out of the classroom as well, feeling worried over that student that Miss Bloomie mentioned. "
        " ...You do hope that they're doing okay. "
        pause 2.0
        jump ttbreak4
    else:
        x " ...No, no...this can't be good. "
        x " This has to be the seventh report this month... "
        x " I have to get the teachers to do something about this. "
        x " Our school's reputation wouldn't look good if we don't do something for this. "
        " You ask her what's wrong. "
        x " [name]. I'm pleased to see you here. "
        $ bloomieknow = True
        msb " I'm Miss Bloomie. Science teacher. "
        msb " Listen... "
        msb " I've had Miss Grace tell me something. "
        msb " Apparently, there's been a student that has been facing constant bullying. "
        msb " The moment they get into school - they get bullied. "
        msb " The moment they leave school - they get bullied. "
        msb " As long as they're breathing, they're getting bullied. "
        msb " It's getting worse and worse to be point the kid is considering... "
        msb " Doing something not good to themself. "
        msb " We've only been informed of this just now because of 3 students reporting of the situation. "
        msb " We also don't know why the kid that's been getting bullied themself hasn't reported the situation earlier. "
        msb " Probably too afraid to even say anything, otherwise they're gonna get into more trouble with those bullies. "
        msb " From what I've heard, Mister Demi and a few more teachers are already on the situation. "
        msb " The good thing is, we've managed to come in contact with the bullies. "
        msb " The only problem is that one of the bullies isn't even from this school. "
        msb " Sure, we could kick him out, but somehow he always manages to come back. "
        msb " Not to mention the fact that he's one of my favorite students. "
        msb " I...really don't know what to do. "
        msb " Another thing that I've heard is that they, the bullies, are planning to... "
        msb " Do something really dangerous to that kid I mentioned from before. "
        msb " ...I don't want that happening. "
        msb " I'm going to have to confront them after your class, [name]. "
        msb " If you ever see a kid that looks beaten up... "
        msb " ...Do your best to seperate them from those bullies. "
        msb " I feel if you even let them be close with them, they'll just bother them more. "
        msb " I trust that you'll do a good job in protecting that kid. "
        scene black with dissolve
        " You spent the rest of the class talking with Miss Bloomie about the situation that's been going on. "
        " This is...quite worrying. "
        " You've heard of bullying where people just...say mean words to someone, "
        " But you haven't seen people take it THIS far. "
        " All you could do is just pray for this kids safety. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, class is over. "
        " The students pass their work to Miss Bloomie and they all walk out of the classroom. "
        " You eventually walk out of the classroom as well, feeling worried over that student that Miss Bloomie mentioned. "
        " ...You do hope that they're doing okay. "
        pause 2.0
        jump ttbreak4

label ttbreak4:
    scene hallway with dissolve
    " You walked into the hallway. "
    " Nothing interesting was happening, until... "
    " You caught three suspicious students talking about something. "
    " Pretending that you were just standing there and not listening, you eavesdropped on their conversation. "
    " Let's see what they're talking about... "
    show zipneutral at left with easeinright
    show oliverneutral at center with easeinright
    show edwardneutral at right with easeinright
    z " So, Oliver! What will we be doing to Abbie today? "
    ed " Oooh, maybe we could rip all of his notebooks to shreds? "
    z " OOOOR we could throw buckets of paint at him. "
    ed " OR! we could force feed him a lot of soap! "
    z " And make him drink shampoo afterwards! "
    o " Mmmm... that idea doesn't sound too bad, actually! "
    o " Just don't take the soap from my stash. "
    o " Otherwise I'm killing you both. "
    z " Yeah, yeah...whatever! "
    hide edwardneutral at bottom
    show edwardconfused at right
    ed " Uh...guys, you might want to look behind you. "
    z " Huh? "
    o " Is it Abbie?{nw} "
    hide oliverneutral at bottom
    show oliverohshit at center
    hide zipneutral at bottom
    show zipconfused at left
    o " Oh shit. "
    " They all stare at you, knowing that they're cooked. "
    " You didn't really expect them to notice you that fast. "
    " But you kinda find it funny that they were acting so tough from earlier, and now they're just... "
    " Shitting their pants all because you're here. "
    o " ... "
    o " Run. "
    hide zipconfused at left with easeoutleft
    hide oliverohshit at left with easeoutleft
    hide edwardconfused at left with easeoutleft
    " ...They ran away. "
    " You're gonna have to deal with them later. "
    " And you're also going to have to keep an eye on that Abbie kid they mentioned... "
    " ...To make sure that those three kids don't do anything stupid to Abbie. "
    " Back to roaming the halls for now, you guess.. "
    scene black with dissolve
    " Yeah, you get the deal. "
    " You spent the entire break walking around and making sure the students didn't do anything stupid. "
    " And of course, you didn't spot anyone doing anything stupid. "
    " Wait...you just realized your class is next. "
    " Oh boy. Better get prepared then! "
    play sound "audio/bellring.mp3"
    " The bell rings, looks like it's time for your class. "
    " You walked into your classroom and prepared to teach your students some new things. "
    pause 2.0
    jump helpclass4
label helpclass4:
    scene gardenroom with dissolve
    " You entered your classroom and already found your students in your classroom. "
    " Pretty good... "
    " You got up infront and started teaching them about what they should know. "
    " But, as you were teaching... "
    " You spotted the three kids from earlier eyeing this one student. "
    " Perhaps this is the student that they've been talking about? "
    " You need to keep an eye on them. And you also need to talk to that kid. "
    " Upon closer look, they look hurt...really hurt. "
    " That wasn't good at all. "
    " The moment your class ends, you're talking to them. "
    " You also might need to tell another teacher about this. "
    " You just continue teaching...for now. "
    scene black with dissolve
    pause 1.0
    play sound "audio/bellring.mp3"
    scene gardenroom with dissolve
    " Once your class was over, you called the kid over. "
    show abbieneutral at center with easeinright
    a " ...Yes, [fancy]..? "
    " He seems to look really nervous. "
    " You reassure him that you weren't gonna make fun of him or anything. "
    " You just called him over to ask him what happened. "
    a " ... "
    hide abbieneutral at bottom
    show abbiesad at center
    a " ...W...well.. "
    a " Three kids...decided to beat me up... "
    a " At the back of the school... "
    a " Their names were...Oliver, Zip, and Edward... "
    a " They were being very mean...telling me that I should just... "
    a " ...{sc}jump off the building{/sc}... "
    " ...Yeah you're DEFINITELY telling another teacher about this. "
    " You gave him permission to go to the nurses office to heal up... "
    " ...And told him that you're gonna deal with those three kids he mentioned. "
    " You gave him a nice pat on the head before giving him a piece of candy from your drawer on your desk. "
    hide abbiesad at bottom
    show abbiehappy at center
    " He looks pretty happy. "
    a " Okay...thank you... "
    a " You're a really good teacher, [mr] [name]... "
    a " You have to be my favorite teacher... "
    a " Even if you just started out yesterday... "
    a " You're doing great...! "
    hide abbiehappy at left with easeoutleft
    " ...AWWWW!!! "
    " That was adorable. "
    scene black with dissolve
    " You then exitted out of your classroom after that. "
    " Already planning to tell one of your teacher friends about what's going on. "
    pause 2.0
    jump ttbreak5

label ttbreak5:
    scene hallway with dissolve
    " You walked into the hallway and started talking around to try and find another teacher. "
    " It wasn't long until you found the art teacher who was just walking to her classroom. "
    " You rush up to her, and immediately started yapping. "
    show sashaconfused at center with easeinleft
    if sashaknow == True:
        mss " Woah-! [name], slow down! "
        mss " I can't understand a thing you're saying if you're talking this fast! "
        mss " What's the rush? "
        mss " You seem really worried over something... "
        mss " What's wrong? a student picking on you? "
        mss " Orrr are things not really going well for you right now? "
        mss " You can tell me anything, just calm down for a moment! "
        hide sashaconfused at bottom
        show sashaneutral at center
        " You take a deep breath to calm yourself down... "
        " ...And then you started telling her about what happened earlier in your class. "
        " And what Abbie told you. "
        mss " ... "
        hide sashaneutral at bottom
        show sashaangry at center
        mss " I'M SORRY, WHAT DID THOSE KIDS DO TO HIM??? "
        mss " AND WHAT ARE THEY PLANNING??? "
        mss " Ohoho, I'm NOT letting this slide. "
        mss " I'm going to have a nice and friendly talk with them! "
        mss " Thank you for telling me about this, [name]! "
        mss " And just when my day's going well right now... "
        mss " I'll get going now, [name]! "
        mss " I'll see you later!! "
        hide sashaangry at right with easeoutright
        " ... "
        " Yeah, those kids are gonna have a nice and friendly talk alright. "
        " Well...what do you do now? "
        " ...Now that you think about it, the floors is kind of looking a bit dirty. "
        " You didn't want the janitor to have a pain in cleaning all of this mess. "
        " You decided to help out a bit and just start cleaning. "
        scene black with dissolve
        " You spent the rest of the break cleaning up the hallways a bit. "
        " Throwing away crumpled up papers and putting them in the trash cans... "
        " Finding lost things and returning them to their proper owners... "
        " Wow! You probably should've became the janitor at this point. "
        " But, eh...too late. "
        " You've already become a teacher. No going back now. "
        play sound "audio/bellring.mp3"
        " The bell rings. Looks like it's time for you to help someone again. "
        " You wait for all of the students to return to their perspective classrooms before you went around to see if anyone needed help. "
        pause 2.0
        jump helpclass5
    else:
        x " Woah-! [name], slow down! "
        x " I can't understand a thing you're saying if you're talking this fast! "
        x " What's the rush? "
        x " You seem really worried over something... "
        x " What's wrong? a student picking on you? "
        x " Orrr are things not really going well for you right now? "
        x " You can tell me anything, just calm down for a moment! "
        hide sashaconfused at bottom
        show sashaneutral at center
        " You take a deep breath to calm yourself down... "
        " ...And then you started telling her about what happened earlier in your class. "
        " And what Abbie told you. "
        x " ... "
        hide sashaneutral at bottom
        show sashaangry at center
        x " I'M SORRY, WHAT DID THOSE KIDS DO TO HIM??? "
        x " AND WHAT ARE THEY PLANNING??? "
        x " Ohoho, I'm NOT letting this slide. "
        x " I'm going to have a nice and friendly talk with them! "
        x " Thank you for telling me about this, [name]! "
        x " And just when my day's going well right now... "
        x " I'll get going now, [name]! "
        x " I'll see you later!! "
        hide sashaangry at right with easeoutright
        " ... "
        " Yeah, those kids are gonna have a nice and friendly talk alright. "
        " Well...what do you do now? "
        " ...Now that you think about it, the floors is kind of looking a bit dirty. "
        " You didn't want the janitor to have a pain in cleaning all of this mess. "
        " You decided to help out a bit and just start cleaning. "
        scene black with dissolve
        " You spent the rest of the break cleaning up the hallways a bit. "
        " Throwing away crumpled up papers and putting them in the trash cans... "
        " Finding lost things and returning them to their proper owners... "
        " Wow! You probably should've became the janitor at this point. "
        " But, eh...too late. "
        " You've already become a teacher. No going back now. "
        play sound "audio/bellring.mp3"
        " The bell rings. Looks like it's time for you to help someone again. "
        " You wait for all of the students to return to their perspective classrooms before you went around to see if anyone needed help. "
        pause 2.0
        jump helpclass5

label helpclass5:
    scene hallway with dissolve
    " You walked around and found only one teacher that needs help. "
    " Should you help them out? "
    if thavelknow == True:
        menu:
            " {image=missthavelicon} Help Miss Thavel {image=missthavelicon} ":
                jump thenedengame
            " Nah, let's roam around the halls for now ":
                jump tocatchapredator
    else:
        menu:
            " {image=missthavelicon} Help the language teacher {image=missthavelicon} ":
                jump thenedengame
            " Nah, let's roam around the halls for now ":
                jump tocatchapredator

label thenedengame:
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    " You walked into the classroom, and found the students in the middle of a roleplay. "
    " You made sure not to disturb the students, because it would've been awkward if you did. "
    " At the very back, you could see the language teacher taking notes on the roleplay. "
    " Basically just rating how well they're doing right now. "
    " And so far they look like they're doing fine. "
    " A few mistakes here and there, but fine overall. "
    " You didn't wanna stand still for the rest of the class, so you grabbed a chair and sat next to your other teacher friend. "
    " The both of you were silent for a bit. "
    " You didn't wanna disturb her doing her work. "
    " You just...gotta wait until it's the right time. "
    show msthravelneutral at center with easeinleft
    if thavelknow == True:
        mst " ... "
        " ... "
        mst " ...{p} Oh, bonjour, [name]! "
        mst " I'm letting my students do a roleplay... "
        mst " ...Making them using differents languages, of course. "
        mst " Their grammar isn't the best, but atleast it's something, right? "
        mst " Anywho, did you want to talk to me about something? "
        " You shook your head, you kind of just wanted to hang out with her. "
        " In a productive way of course, You know damn well you're gonna get cooked if you don't do anything productive. "
        hide msthravelneutral at bottom
        show msthravelhappy at center
        mst " Heh, right. In a productive way. "
        hide msthravelhappy at bottom
        show msthravelneutral at center
        mst " Anywho, it's your second day here, right? "
        mst " What do you think so far? "
        mst " Kids giving you a headache yet? "
        mst " Or are you having a surprisingly nice time here? "
        " You thought about her question for a bit. "
        " Then responded that you think that you're doing fine, but... "
        " It's also starting to get a little exhausting. "
        " And you're also starting to get worried with some of the students mental health..."
        " Considering what's been happening recently. "
        " You ask Miss Thavel if bullying happens a lot at this school. "
        mst " ...Well.. "
        mst " Thankfully, not a lot. "
        mst " Only a few students - just three - bully some students. "
        mst " I'm thankful that it's just three, otherwise this school would've been more of a nightmare than it already is. "
        mst " You probably would've wanted to quit your job on the first day if that was the case. "
        mst " Then again, now that I think about it... "
        mst " I've been seeing those three students bully this specific student. "
        mst " He doesn't really do well in class, but he tries his best, I guess. "
        mst " I don't really know what to do with him, he can probably deal with the bullying just fine. "
        mst " Probably. He should be strong enough to deal with that. "
        " ... "
        " You don't know whether to say that Miss Thavel is right or wrong. "
        " You probably shouldn't think too much about it though. "
        scene black with dissolve
        " You spent the rest of the class time talking with Miss Thavel while she was looking at the students roleplaying. "
        " You also kind of helped her with grading and rating how well they did. "
        " You also told her to include the grammar mistakes as a minus 1 point. "
        " It only makes sense to do that, I guess? "
        " Okay I have to admit I have absolutely no idea what to say here "
        " Like literally what else can I yap about here "
        " It's like 11 am and I'm listening to weathergirl by flavor foley rn "
        " Okay whatever "
        play sound "audio/bellring.mp3"
        " The bell eventually rings, stopping the students from roleplaying any further. "
        " Miss Thavel finishes giving the students their points, and all the students leave. "
        " You then walk out into the hallway so that you could give yourself a break. "
        pause 2.0
        jump ttbreak6
    else:
        x " ... "
        " ... "
        x " ...{p} Oh, bonjour, [name]! "
        $ thavelknow = True
        mst " I'm Miss Thavel, the language teacher. I believe I haven't got to introduce myself to you yet. "
        mst " I'm letting my students do a roleplay... "
        mst " ...Making them using differents languages, of course. "
        mst " Their grammar isn't the best, but atleast it's something, right? "
        mst " Anywho, did you want to talk to me about something? "
        " You shook your head, you kind of just wanted to hang out with her. "
        " In a productive way of course, You know damn well you're gonna get cooked if you don't do anything productive. "
        hide msthravelneutral at bottom
        show msthravelhappy at center
        mst " Heh, right. In a productive way. "
        hide msthravelhappy at bottom
        show msthravelneutral at center
        mst " Anywho, it's your second day here, right? "
        mst " What do you think so far? "
        mst " Kids giving you a headache yet? "
        mst " Or are you having a surprisingly nice time here? "
        " You thought about her question for a bit. "
        " Then responded that you think that you're doing fine, but... "
        " It's also starting to get a little exhausting. "
        " And you're also starting to get worried with some of the students mental health..."
        " Considering what's been happening recently. "
        " You ask Miss Thavel if bullying happens a lot at this school. "
        mst " ...Well.. "
        mst " Thankfully, not a lot. "
        mst " Only a few students - just three - bully some students. "
        mst " I'm thankful that it's just three, otherwise this school would've been more of a nightmare than it already is. "
        mst " You probably would've wanted to quit your job on the first day if that was the case. "
        mst " Then again, now that I think about it... "
        mst " I've been seeing those three students bully this specific student. "
        mst " He doesn't really do well in class, but he tries his best, I guess. "
        mst " I don't really know what to do with him, he can probably deal with the bullying just fine. "
        mst " Probably. He should be strong enough to deal with that. "
        " ... "
        " You don't know whether to say that Miss Thavel is right or wrong. "
        " You probably shouldn't think too much about it though. "
        scene black with dissolve
        " You spent the rest of the class time talking with Miss Thavel while she was looking at the students roleplaying. "
        " You also kind of helped her with grading and rating how well they did. "
        " You also told her to include the grammar mistakes as a minus 1 point. "
        " It only makes sense to do that, I guess? "
        " Okay I have to admit I have absolutely no idea what to say here "
        " Like literally what else can I yap about here "
        " It's like 11 am and I'm listening to weathergirl by flavor foley rn "
        " Okay whatever "
        play sound "audio/bellring.mp3"
        " The bell eventually rings, stopping the students from roleplaying any further. "
        " Miss Thavel finishes giving the students their points, and all the students leave. "
        " You then walk out into the hallway so that you could give yourself a break. "
        pause 2.0
        jump ttbreak6

label tocatchapredator:
    " Yeah, let's just roam around the halls for now. "
    " You think you just need some alone time after what's been happening today. "
    " Just a quick breather... "
    " ...While making sure that some kids aren't doing anything stupid. "
    " You start roaming around the school's hallways, seeing if there's any kids doing anything stupid. "
    scene black with dissolve
    " You spent the rest of the class hours walking around the hallways. "
    " You actually managed to walk by the principal's office, and heard some talking... "
    " Being the curious little idiot that you are, you listened into the conversation. "
    " From what you could hear... "
    " ...Miss Grace was talking to three kids. "
    " Maybe these were the three kids that were causing trouble to that Abbie kid? "
    " They seemed pretty mad. "
    " ...'We weren't doing anything bad'? I don't think that's a good excuse, buddy. "
    " Atleast put some effort into trying to get yourself out of trouble. "
    " ...Well, it's best not to stick around for too long. "
    " Let's get back to roaming around, otherwise there might be kids skipping class. "
    pause 1.0
    play sound "audio/bellring.mp3"
    " The bell rings after a few minutes of you wandering around. "
    " You managed to catch a few kids skipping class before this, and you returned them to their class. "
    " Time for you to take a break. "
    pause 2.0
    jump ttbreak6

label ttbreak6:
    scene hallway with dissolve
    " You walked around the hallway and heard a few kids talking things... "
    " Things that have happened recently. "
    " Like, for example: "
    " 'Did you hear?' "
    " 'Oliver, Zip, and Edward got into massive trouble.' "
    " 'They're in the principals office as we speak!' "
    " 'What happened?' "
    " 'Apparently, they were planning to kill Abbie.' "
    " 'Really...?' "
    " 'That's horrible!' "
    " And a lot more things. "
    " You're glad that Miss Grace is talking to those three kids now though. "
    " You don't want that Abbie kid suffering the entire time that he's here. "
    " He seemed like such a sweet guy... "
    " ...Why would they go after him? "
    " From what you've heard, he gets pretty low grades, but that doesn't change your mind on anything about him. "
    " To you, he's just an ordinary student. "
    " You don't know why people go out of their way to bully someone like this. "
    " It's making your head hurt with how much you're thinking about it. "
    " Remember kids! Bullying isn't good! "
    " I say as I proceed to bully kids on roblox "
    " We don't talk about that though. "
    scene black with dissolve
    " You spent the rest of the break wandering around the hallways... "
    " Wondering what Miss Grace is going to do about Oliver, Zip, and Edward. "
    " Probably a warning, but that would be too little. "
    " A suspension for a few days would be good. "
    " Then again, they could just use those days to just... "
    " ...Do whatever the hell they want. "
    " Like drugs. "
    " Nah, they probably wont do that. Anything but drugs. "
    play sound "audio/bellring.mp3"
    " The bell rings, looks like you have to help someone again. "
    " You wait for all of the kids to get into their classrooms before you wandered around and checked to see if anyone else needed help. "
    pause 2.0
    jump helpclass6

label helpclass6:
    scene hallway with dissolve
    " Looks like there's only one teacher that needs some help. "
    " SHould you go help them out? "
    if emilyknow == True:
        menu:
            " {image=missemilyicon} Help Miss Emily {image=missemilyicon} ":
                jump meand
            " Nah, let's go have a talk with Miss Grace instead ":
                jump mrwolf
    else:
        menu:
            " {image=missemilyicon} Help Miss Emily {image=missemilyicon} ":
                jump meand
            " Nah, let's go have a talk with Miss Grace instead ":
                jump mrwolf
label meand:
    scene black with dissolve
    pause 2.0
    scene classroom with dissolve
    " You walked into the classroom, finding it to be empty. "
    " You're a little confused. Shouldn't the history teacher have her class right now? "
    " You look around and spotted the teacher packing up her things. "
    " Maybe she's ending class early? "
    " You walked up to her to ask if she's really ending class this early. "
    show msemilyneutral at center with easeinleft
    if emilyknow == True:
        mse " Hey [name]!! "
        mse " Why I'm ending class early? "
        mse " Well... "
        mse " Just some personal matters, is all. "
        mse " I've already asked Miss Grace if I could end class, don't worry. "
        mse " I'd rather not talk about what personal matters im going through. "
        " Understandable... "
        " You ask her if she's doing alright. "
        mse " I'm fine, don't worry. "
        mse " You should get going since you don't have to help me. "
        mse " I'll just... "
        mse " Pack my things. I'll be fine. "
        " She starts packing all of her things, but... "
        " ...Looks like she's struggling carrying a few things. "
        " You might want to help her. "
        " Or just leave her alone just like she said. "
        menu:
            " Help her carry all of her things ":
                $ emilylv += 5
                " You decided to help her carry a few things. "
                " You just felt a little nice, I guess. "
                scene black with dissolve
                " You spent the rest of the class time helping Miss Emily pack her things. "
                " You even carried her bag for her, and paperworks that she needs to do. "
                " Carried all of them all the way to her car. "
                " You're such a nice teacher! Miss Emily seemed to be thankful for what you did. "
                " You watched her drive away, and then walked back inside the school. "
                " Class hours hasn't exactly ended yet, so you roamed the hallways to cure your boredom for the last few minutes. "
                " As you were walking, you can't help but feel like... "
                " ...Miss Emily wasn't doing okay. "
                " But then again, you're probably overthinking things. "
                " You also can't just force an answer out of her just because she was feeling bad. "
                " Just gotta respect her privacy for now. "
                " You continued to roam the hallways to pass your time. "
                pause 1.0
                play sound "audio/bellring.mp3"
                " The bell rings, meaning that the schoolday is over. "
                " You head over to your classroom so that you could get your things packed up. "
                " This was..an exhausting day. "
                pause 2.0
                jump ttendday2
            " Leave like she told you ":
                scene black with dissolve
                " You decided to leave Miss Emily alone. "
                " Though, you can't help but feel like... "
                " ...She wasn't doing okay. "
                " But then again, you're probably overthinking things. "
                " You also can't just force an answer out of her just because she was feeling bad. "
                " Just gotta respect her privacy for now. "
                " You decided to roam the hallways to pass your time. "
                pause 1.0
                play sound "audio/bellring.mp3"
                " The bell rings, meaning that the schoolday is over. "
                " You head over to your classroom so that you could get your things packed up. "
                " This was..an exhausting day. "
                pause 2.0
                jump ttendday2
    else:
        $ emilyknow = True
        " This is Miss Emily. You've heard about her before your first day. "
        " She's the history teacher, and she's really nice. "
        mse " Hey [name]!! "
        mse " Why I'm ending class early? "
        mse " Well... "
        mse " Just some personal matters, is all. "
        mse " I've already asked Miss Grace if I could end class, don't worry. "
        mse " I'd rather not talk about what personal matters im going through. "
        " Understandable... "
        " You ask her if she's doing alright. "
        mse " I'm fine, don't worry. "
        mse " You should get going since you don't have to help me. "
        mse " I'll just... "
        mse " Pack my things. I'll be fine. "
        " She starts packing all of her things, but... "
        " ...Looks like she's struggling carrying a few things. "
        " You might want to help her. "
        " Or just leave her alone just like she said. "
        menu:
            " Help her carry all of her things ":
                $ emilylv += 5
                " You decided to help her carry a few things. "
                " You just felt a little nice, I guess. "
                scene black with dissolve
                " You spent the rest of the class time helping Miss Emily pack her things. "
                " You even carried her bag for her, and paperworks that she needs to do. "
                " Carried all of them all the way to her car. "
                " You're such a nice teacher! Miss Emily seemed to be thankful for what you did. "
                " You watched her drive away, and then walked back inside the school. "
                " Class hours hasn't exactly ended yet, so you roamed the hallways to cure your boredom for the last few minutes. "
                " As you were walking, you can't help but feel like... "
                " ...Miss Emily wasn't doing okay. "
                " But then again, you're probably overthinking things. "
                " You also can't just force an answer out of her just because she was feeling bad. "
                " Just gotta respect her privacy for now. "
                " You continued to roam the hallways to pass your time. "
                pause 1.0
                play sound "audio/bellring.mp3"
                " The bell rings, meaning that the schoolday is over. "
                " You head over to your classroom so that you could get your things packed up. "
                " This was..an exhausting day. "
                pause 2.0
                jump ttendday2
            " Leave like she told you ":
                scene black with dissolve
                " You decided to leave Miss Emily alone. "
                " Though, you can't help but feel like... "
                " ...She wasn't doing okay. "
                " But then again, you're probably overthinking things. "
                " You also can't just force an answer out of her just because she was feeling bad. "
                " Just gotta respect her privacy for now. "
                " You decided to roam the hallways to pass your time. "
                pause 1.0
                play sound "audio/bellring.mp3"
                " The bell rings, meaning that the schoolday is over. "
                " You head over to your classroom so that you could get your things packed up. "
                " This was..an exhausting day. "
                pause 2.0
                jump ttendday2

label mrwolf:
    scene black with dissolve
    pause 2.0
    scene principalsoffice with dissolve
    " You walked into Miss Grace's office. "
    " Honestly, why did you even go here? "
    " Was it by curiousity or did you just want to see if there's something funny? "
    " Or are you trying to see if there's a secret Miss Grace ending? "
    " Well, Miss Grace doesn't have an ending. "
    " Never will be, unfortunately. "
    " That's just gonna cause more problems actually. "
    " Ahem, anyway... "
    show msgraceneutral at center with dissolve
    msg " Alice, I told you not to exit your room. "
    msg " You know you're not allowed to. "
    msg " If you want to see Oliver, get out of your room in the night... "
    msg " ...And just go visit his house. "
    msg " I've made that clear since the day you two got here. "
    msg " I really don't want to have this conversation with you all over again. "
    msg " ...Alright, have a good rest. "
    " Seems like she was talking to someone... "
    " Then she noticed that you were just standing there. "
    msg " Ah, [name]. Have a seat. "
    msg " Did you have something to report to me? "
    msg " Or did you have something to ask me? "
    " You shrugged. You didn't really know why you came here... "
    " ...Then remembered something you've heard earlier. "
    " You asked her what she did with the three kids who were bullying Abbie. "
    msg " Oh. Oliver, Zip, and Edward? "
    msg " I gave them a lecture, of course... "
    msg " They weren't listening, so I decided to suspend Oliver for a day. "
    msg " Why only Oliver? I know Zip and Edward wouldn't even dare risk being suspended. "
    msg " I know how their parents are. "
    msg " If they even get caught being suspended... "
    msg " Let's just say that they're getting their asses whooped. "
    msg " Really bad. Their asses are getting whooped really bad if that happened. "
    msg " So, if Oliver gets suspended, Zip and Edward won't do anything horrible. "
    msg " ... "
    msg " You know...Zip and Edward never were really like this. "
    msg " They used to be sweet kids. "
    msg " I think it's just Oliver's influence that ruined them. "
    msg " Which is...unfortunate. "
    msg " But, there was no other way of stopping it, no? "
    msg " Oliver would talk to them every day, teaching them new things, like... "
    msg " ...How to eat soap safely. "
    msg " I never understood his love for soap... "
    msg " Oliver would also teach them dangerous pranks... "
    msg " And all of that lead to how they are now. "
    msg " It's a shame they turned rotten like this. "
    msg " But, what can we do if they won't listen? "
    msg " Can't exactly do anything about it. "
    msg " If I can't do anything about it, then I'll just do nothing. "
    msg " Sit in the back and watch for what happens... "
    msg " That's the type of thing I do. "
    scene black with dissolve
    " You spent the rest of the class hours talking with Miss Grace. "
    " She was honestly just a chill person to talk to... "
    " ...Though you shouldn't really talk to her a lot. "
    " She's literally the principal and she can be busy. "
    " Best not to disturb her all the time. "
    play sound "audio/bellring.mp3"
    " The bell rings, meaning that the schoolday is over. "
    " You head over to your classroom so that you could get your things packed up. "
    " This was..an exhausting day. "
    pause 2.0
    jump ttendday2

label ttendday2:
    scene gardenroom with dissolve
    " You walked into your classroom and cleaned up a few things. "
    " Arranged some plants, making sure everything looked good before you left... "
    " Then you started to put your stuff into your bag. "
    " You just wanted to go back to your sweet bed, after this hell of a day... "
    " ...And take a nice long nap... "
    " Even though you know that you're just going to come back to this hell again tomorrow. "
    " Whatever, atleast you get to rest for just a moment. "
    " Just a moment, and you'll be all fine... "
    scene black with dissolve
    " You packed up all of your things, then you went out to go back to your home. "
    stop music fadeout 1.5
    pause 2.0
    play music "audio/home.mp3" fadein 1.5
    scene mcroom with dissolve
    " You put your bag of things near your desk, and you sat down on your bed. "
    " You took a look on your phone to see if anything's going on in the teacher's GC... "
    " ...Looks like they're just talking about what happened earlier. "
    " Nothing important whatsoever...just jokes here and there. "
    " You close your phone and put it on your desk before you tucked yourself into your blankets and fall asleep. "
    " You needed some good rest after what had happened today... "
    " Hopefully tomorrow wouldn't be as much hell as today was. "
    " You could only pray. "
    " You close your eyes... "
    scene black with dissolve
    " ...And fall asleep. Good night, [name]. "
    stop music fadeout 1.5
    pause 2.0
    jump teacherwednesday
