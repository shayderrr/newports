label monday:
    pause 0.5
    play music "audio/home.mp3" fadein 0.5
    scene mcroom with dissolve
    pause 0.5
    scene black with dissolve
    pause 0.5
    scene mcroom with dissolve
    " You slowly wake up from your slumber, realizing that it's a monday. oh no. "
    " And it's not just a normal monday, it's the 'first day of your class' monday. "
    " You've just transferred to Paper School, hearing that this school offers amazing opportunities for growth and learning. "
    " ...Other than some of the teachers being a tad bit strict. "
    " You get up and stretch, hearing that lovely back-cracking ASMR everyone loves to hear. "
    if kind == True:
        " You seem to be quite ready for the day, excited to make new friends, excited to learn... "
        " Or you're just thinking like that so that your ancestors wont disown you for being an introverted goof. "
        " Or maybe not. "
    elif mean == True:
        " You weren't exactly ready for the day coming ahead, after all, you think that all schools are the same. "
        " You've got all of those stereotypes in your head...the popular girls...the emos... all sorts. "
        " It's just gonna be the same expirience as your old school, you thought. "
        " And unfortunately, you can't skip your first day in class because I said so. "
    elif calm == True:
        " You honestly just wanted to go back to sleep, but you knew that you had to eventually go to school. "
        " Whether you liked it or not. You didn't really mind it, you were just a chill guy. "
    " You get your breakfast, which were just a few pancakes you managed to cook up in time. "
    " They were a little burnt due to your cooking not being the best, but as long as you're fed it's fine. "
    " You then get into your outfit that you wanted to wear to school, and you headed off. "
    scene black with dissolve
    stop music
    pause 1.5
    show text " DAY 1 - MONDAY "
    pause 1.5
    play music "audio/paperhigh.mp3" fadein 0.5
    scene paperschoolfront with dissolve
    " You've finally arrived at your school. Everything seems oddly peaceful and quiet.... "
    " Except for the fact that you're hearing a lot of screaming from inside of the school. "
    " And also some swear words here and there. Your average school, basically. "
    " What great fun this is! You probably won't get bullied and get passing grades! "
    " That's what your inner self is telling you, but you end up procrastinating on homework until the last second of the deadline. "
    " Very fun! Excellent, splendid! "
    " Without a further a do, you step into your new hell hole that you have to suffer in for the rest of your life...probably. "
    scene black with dissolve
    pause 2.0
    scene hallway with dissolve
    " And here you are, taking your first baby steps into the very big bad scary hallways of the school. "
    " Whilst walking around you could see other people taking pictures, making fun of a poor kid, normal school stuff. "
    " You then saw a girl trip and got all of her books on the floor. "
    show claireconfused at center with dissolve
    x " Ow ... " with vpunch
    " You're feeling like you should maybe help her with her books and stuff. "
    " Should you help her carry her books and help her up? "
    if kind == True:
        menu:
            " Help her up ":
                " You offered her a hand to help her up. "
                hide claireconfused at bottom
                show claireneutral at center
                " She took your hand, and she got up, dusting herself off. "
                " You then kept half of the books to yourself so that you could handle them, and you gave the other half to her. "
                x " Whew, thanks... "
                x " Handling with so much books is a little pain, right? Heheh... "
                x " My locker isn't that far, don't worry. It's just around the corner. "
                " The both of you walked in silence. "
                " Obviously, you wouldn't try to make a conversation with someone you don't know. "
                " You didn't know what they liked, so you didn't really have a topic to talk about with her. "
                " Eventually, you and the girl reach the locker that she was talking about, and she put all of her things in. "
                " Just as you were about to leave to go do your own business, she suddenly spoke up. "
                hide claireneutral at bottom
                show claireconfused at center
                x " Hey... Aren't you that new kid? "
                " You turned around and nodded your head, confirming that you are {i}indeed{/i} the new kid. "
                hide claireconfused at bottom
                show claireneutral at center
                x " Well then, thank you for helping me! And nice to meet you too! "
                $ claireknow = True
                hide claireneutral at bottom
                show clairehappy at center
                c " I'm Claire! "
                hide clairehappy at bottom
                show claireneutral at center
                c " Do you want me to show you around the school? "
                c " I could, if you want me to-!{nw} "
                play sound "audio/bellring.mp3"
                " As if on cue, the bell rings, preventing Claire from showing you around the school. It's class time. "
                hide claireneutral at bottom
                show clairesad at center
                c " Aw dang... I was really hoping I could show you around the school... "
                hide clairesad at bottom
                show claireneutral at center
                c " Well, no problem then! You could still explore the school when it's breaktime! "
                c " I'll see you around, [name]! "
                hide claireneutral at right with easeoutright
                " Then Claire went away to go to class. "
                " You spent the next few minutes trying to figure out where your classroom was. "
                scene black with dissolve
                pause 2.0
                jump class1
            " Ignore her, and let someone else help ":
                " You decided that this wasn't your problem, and so you just turned and walked away. "
                " She could get all of those books all on her own, probably. "
                " You just continued to walk around the school, curiously. "
                " You spotted a door labelled 'Alice's room', but decided not to go near it, nor did you think of opening it. "
                " It looked far too eerie, and you got bad vibes just by looking at it. "
                " As if you're looking at something that you shouldn't be seeing. "
                play sound "audio/bellring.mp3"
                " The bell rings, you should probably start finding where your classroom is. "
                " Luckily, you didn't have much struggle on finding it. "
                " You open the door... "
                scene black with dissolve
                pause 2.0
                jump class1
    elif calm == True:
        menu:
            " Help her up ":
                " You offered her a hand to help her up. "
                hide claireconfused at bottom
                show claireneutral at center
                " She took your hand, and she got up, dusting herself off. "
                " You then kept half of the books to yourself so that you could handle them, and you gave the other half to her. "
                x " Whew, thanks... "
                x " Handling with so much books is a little pain, right? Heheh... "
                x " My locker isn't that far, don't worry. It's just around the corner. "
                " The both of you walked in silence. "
                " Obviously, you wouldn't try to make a conversation with someone you don't know. "
                " You didn't know what they liked, so you didn't really have a topic to talk about with her. "
                " Eventually, you and the girl reach the locker that she was talking about, and she put all of her things in. "
                " Just as you were about to leave to go do your own business, she suddenly spoke up. "
                hide claireneutral at bottom
                show claireconfused at center
                x " Hey... Aren't you that new kid? "
                " You turned around and nodded your head, confirming that you are {i}indeed{/i} the new kid. "
                hide claireconfused at bottom
                show claireneutral at center
                x " Well then, thank you for helping me! And nice to meet you too! "
                $ claireknow = True
                hide claireneutral at bottom
                show clairehappy at center
                c " I'm Claire! "
                hide clairehappy at bottom
                show claireneutral at center
                c " Do you want me to show you around the school? "
                c " I could, if you want me to-!{nw} "
                play sound "audio/bellring.mp3"
                " As if on cue, the bell rings, preventing Claire from showing you around the school. It's class time. "
                hide claireneutral at bottom
                show clairesad at center
                c " Aw dang... I was really hoping I could show you around the school... "
                hide clairesad at bottom
                show claireneutral at center
                c " Well, no problem then! You could still explore the school when it's breaktime! "
                c " I'll see you around, [name]! "
                hide claireneutral at right with easeoutright
                " Then Claire went away to go to class. "
                " You spent the next few minutes trying to figure out where your classroom was. "
                scene black with dissolve
                pause 2.0
                jump class1
            " Ignore her, and let someone else help ":
                " You decided that this wasn't your problem, and so you just turned and walked away. "
                " She could get all of those books all on her own, probably. "
                " You just continued to walk around the school, curiously. "
                " You spotted a door labelled 'Alice's room', but decided not to go near it, nor did you think of opening it. "
                " It looked far too eerie, and you got bad vibes just by looking at it. "
                " As if you're looking at something that you shouldn't be seeing. "
                play sound "audio/bellring.mp3"
                " The bell rings, you should probably start finding where your classroom is. "
                " Luckily, you didn't have much struggle on finding it. "
                " You open the door... "
                scene black with dissolve
                pause 2.0
                jump class1
    elif mean == True:
        menu:
            " Help her up ":
                " You offered her a hand to help her up. "
                hide claireconfused at bottom
                show claireneutral at center
                " She took your hand, and she got up, dusting herself off. "
                " You then kept half of the books to yourself so that you could handle them, and you gave the other half to her. "
                x " Whew, thanks... "
                x " Handling with so much books is a little pain, right? Heheh... "
                x " My locker isn't that far, don't worry. It's just around the corner. "
                " The both of you walked in silence. "
                " Obviously, you wouldn't try to make a conversation with someone you don't know. "
                " You didn't know what they liked, so you didn't really have a topic to talk about with her. "
                " Eventually, you and the girl reach the locker that she was talking about, and she put all of her things in. "
                " Just as you were about to leave to go do your own business, she suddenly spoke up. "
                hide claireneutral at bottom
                show claireconfused at center
                x " Hey... Aren't you that new kid? "
                " You turned around and nodded your head, confirming that you are {i}indeed{/i} the new kid. "
                hide claireconfused at bottom
                show claireneutral at center
                x " Well then, thank you for helping me! And nice to meet you too! "
                $ claireknow = True
                hide claireneutral at bottom
                show clairehappy at center
                c " I'm Claire! "
                hide clairehappy at bottom
                show claireneutral at center
                c " Do you want me to show you around the school? "
                c " I could, if you want me to-!{nw} "
                play sound "audio/bellring.mp3"
                " As if on cue, the bell rings, preventing Claire from showing you around the school. It's class time. "
                hide claireneutral at bottom
                show clairesad at center
                c " Aw dang... I was really hoping I could show you around the school... "
                hide clairesad at bottom
                show claireneutral at center
                c " Well, no problem then! You could still explore the school when it's breaktime! "
                c " I'll see you around, [name]! "
                hide claireneutral at right with easeoutright
                " Then Claire went away to go to class. "
                " You spent the next few minutes trying to figure out where your classroom was. "
                scene black with dissolve
                pause 2.0
                jump class1
            " Ignore her, and let someone else help ":
                " You decided that this wasn't your problem, and so you just turned and walked away. "
                " She could get all of those books all on her own, probably. "
                " You just continued to walk around the school, curiously. "
                " You spotted a door labelled 'Alice's room', but decided not to go near it, nor did you think of opening it. "
                " It looked far too eerie, and you got bad vibes just by looking at it. "
                " As if you're looking at something that you shouldn't be seeing. "
                play sound "audio/bellring.mp3"
                " The bell rings, you should probably start finding where your classroom is. "
                " Luckily, you didn't have much struggle on finding it. "
                " You open the door... "
                scene black with dissolve
                pause 2.0
                jump class1
            " Make the situation worse. ":
                $ clairebeatup = True
                " You know what? you're not being a nice guy today. "
                " Let's go and cause some chaos. "
                " You walk over, pretending that you're about to help her up, extending your hand to her. "
                hide claireconfused at right
                show clairescared at center
                " Before she grabs it, you kick her in the stomach, kicking her a bit away and you stomp on some of her books. " with vpunch
                x " H-hey! Stop that! Those are mine...! "
                " Without even noticing, you notice that an older boy has joined you. "
                show clairescared at right with move
                show oliverbully at left with easeinleft
                x " Finally, some REAL action! "
                x " OHOHO! And it's the new kid that's doing it?! This is PEAK! "
                x " Go get them newbie! Destroy all of her stuff! " with vpunch
                " Due to how this guy was encouraging you to do things, you rip apart one of her books. "
                " Everyone who was near you was now staring. "
                " Looks of anger, looks of fear. All of it was so... {sc}{b}thrilling.{/b}{/sc} "
                play sound "audio/bellring.mp3"
                hide oliverbully at bottom
                show oliverangry at left
                " The bell rings, saving the girl from getting into any more of your trouble. "
                " The boy that was cheering you on seemed to be a little upset, since the chaos ended. "
                hide clairescared at right with easeoutright
                show oliverangry at center with move
                " She doesn't think, and she gets up to skedaddle to her classroom. "
                " Not thinking of getting her books from the ground at all as one of her arms were clutching her stomach. "
                hide oliverangry at bottom
                show oliverneutral at center
                " You were about to leave to go to your classroom as well, but the older boy stopped you, him now being infront of you. "
                x " Hey, new kid. "
                x " Y'know, I respect ya for doing allat. "
                x " Hell, I wasn't expecting you to kick someone's ass the moment you got here! "
                x " I wouldn't even have the balls to do that on my first day, heh. I'd rather start doing it on the second. "
                x " I like your style, kid. "
                x " Hope to see you again. "
                hide oliverneutral at right with easeoutright
                " ...He then left, going into the same room as the girl did. "
                " You assumed that they were classmates. "
                " You then went to find your own classroom. "
                scene black with dissolve
                pause 2.0
                jump class1
    else:
        return
    label class1:
        scene classroom with dissolve
        " You enter your classroom. Why is this place more colorful than the hallways? I have no idea either. "
        " You see people using their phones like earlier, and you see people bullying a few more students. "
        " Basically just what you've seen from the outside. "
        " But this happens in almost every other school, so it should be normal. "
        " You were kinda just chilling around, standing there... not knowing what to do... "
        " You then spot a tall and rather menacing woman walk by, with a large drawing compass for one of her hands. "
        " Everyone goes back in their place and they all go silent. This must be your new teacher. "
        show misscircleneutral at appearright
        x " Good morning, students! "
        x " We'll be having a new student here in our class, as you've heard. "
        x " Go on up here, [name]! Now, don't be shy and introduce yourself. "
        if kind == True:
            " You don't even really seem to be as nervous people usually are when they have to present up to the board. "
            " Or you're just hiding all of that deep inside so that you won't have to be an embarrassment. "
            " Either way, you go up and face everyone and start to introduce yourself. "
            menu:
                " Hello! I'm [name]! ":
                    menu:
                        " I like to do... ":
                            menu:
                                " Arts and Crafts, Drawing traditionally/digitally! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Singing, dancing, listening to music! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Writing poems, short stories, and other stuff! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                        " My hobbies are... ":
                            menu:
                                " Arts and Crafts, Drawing traditionally/digitally! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Singing, dancing, listening to music! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Writing poems, short stories, and other stuff! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                        " The things I like doing are... ":
                            menu:
                                " Arts and Crafts, Drawing traditionally/digitally! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Singing, dancing, listening to music! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Writing poems, short stories, and other stuff! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                " Hello everyone, good morning my new classmates! I'm [name]! ":
                    menu:
                        " I like to do... ":
                            menu:
                                " Arts and Crafts, Drawing traditionally/digitally! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Singing, dancing, listening to music! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Writing poems, short stories, and other stuff! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                        " My hobbies are... ":
                            menu:
                                " Arts and Crafts, Drawing traditionally/digitally! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Singing, dancing, listening to music! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Writing poems, short stories, and other stuff! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                        " The things I like doing are... ":
                            menu:
                                " Arts and Crafts, Drawing traditionally/digitally! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Singing, dancing, listening to music! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Writing poems, short stories, and other stuff! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                " Hiii!! I'm [name]! ":
                    menu:
                        " I like to do... ":
                            menu:
                                " Arts and Crafts, Drawing traditionally/digitally! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Singing, dancing, listening to music! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Writing poems, short stories, and other stuff! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                        " My hobbies are... ":
                            menu:
                                " Arts and Crafts, Drawing traditionally/digitally! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Singing, dancing, listening to music! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Writing poems, short stories, and other stuff! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                        " The things I like doing are... ":
                            menu:
                                " Arts and Crafts, Drawing traditionally/digitally! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Singing, dancing, listening to music! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
                                " Writing poems, short stories, and other stuff! ":
                                    menu:
                                        " I hope we can all be good friends! ":
                                            jump introdone
                                        " I hope we can make some great memories together and become great friends! ":
                                            jump introdone
        elif mean == True:
            " You groaned internally at this. You always hated it whenever you went up to present up to the board infront of everyone. "
            " You honestly find it very annoying and you get nervous whenever you had to go up... "
            " But you just have to suck it up for now. You have to do it, and you most certainly don't want to look like a wimp. "
            " You then start to introduce yourself. "
            menu:
                " Hello, I'm [name]. ":
                    menu:
                        " I like doing... ":
                            menu:
                                " Arts and stuff. ":
                                    jump introdone
                                " Listening to music. ":
                                    jump introdone
                                " Writing sometimes. ":
                                    jump introdone
                        " I like to do... ":
                            menu:
                                " Arts and stuff. ":
                                    jump introdone
                                " Listening to music. ":
                                    jump introdone
                                " Writing sometimes. ":
                                    jump introdone
                        " Some stuff I like to do are... ":
                            menu:
                                " Arts and stuff. ":
                                    jump introdone
                                " Listening to music. ":
                                    jump introdone
                                " Writing sometimes. ":
                                    jump introdone
                " ...Sup. I'm [name]. ":
                    menu:
                        " I like doing... ":
                            menu:
                                " Arts and stuff. ":
                                    jump introdone
                                " Listening to music. ":
                                    jump introdone
                                " Writing sometimes. ":
                                    jump introdone
                        " I like to do... ":
                            menu:
                                " Arts and stuff. ":
                                    jump introdone
                                " Listening to music. ":
                                    jump introdone
                                " Writing sometimes. ":
                                    jump introdone
                        " Some stuff I like to do are... ":
                            menu:
                                " Arts and stuff. ":
                                    jump introdone
                                " Listening to music. ":
                                    jump introdone
                                " Writing sometimes. ":
                                    jump introdone
                " Hi. I'm [name]. ":
                    menu:
                        " I like doing... ":
                            menu:
                                " Arts and stuff. ":
                                    jump introdone
                                " Listening to music. ":
                                    jump introdone
                                " Writing sometimes. ":
                                    jump introdone
                        " I like to do... ":
                            menu:
                                " Arts and stuff. ":
                                    jump introdone
                                " Listening to music. ":
                                    jump introdone
                                " Writing sometimes. ":
                                    jump introdone
                        " Some stuff I like to do are... ":
                            menu:
                                " Arts and stuff. ":
                                    jump introdone
                                " Listening to music. ":
                                    jump introdone
                                " Writing sometimes. ":
                                    jump introdone
        elif calm == True:
            " You started walking up to the board so that you could face your classmates. "
            " You're honestly just a chill guy, so you didn't mind it whenever you had to present at front. "
            " You clear your throat, making sure to grab everyone's attention before you start to introduce yourself. "
            menu:
                " Suuhhhh everyone, the name's [name]. ":
                    menu:
                        " I like to do stuff like... ":
                            menu:
                                " Arts - drawing traditionally/digitally, and other stuff. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Music - singing, dancing, or making music myself. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Writing - writing storis, poetry, and other things. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                        " Stuff I like to do are... ":
                            menu:
                                " Arts - drawing traditionally/digitally, and other stuff. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Music - singing, dancing, or making music myself. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Writing - writing storis, poetry, and other things. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                        " I do... ":
                            menu:
                                " Arts - drawing traditionally/digitally, and other stuff. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Music - singing, dancing, or making music myself. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Writing - writing storis, poetry, and other things. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                " What's good, everyone. I'm [name]. ":
                    menu:
                        " I like to do stuff like... ":
                            menu:
                                " Arts - drawing traditionally/digitally, and other stuff. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Music - singing, dancing, or making music myself. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Writing - writing storis, poetry, and other things. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                        " Stuff I like to do are... ":
                            menu:
                                " Arts - drawing traditionally/digitally, and other stuff. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Music - singing, dancing, or making music myself. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Writing - writing storis, poetry, and other things. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                        " I do... ":
                            menu:
                                " Arts - drawing traditionally/digitally, and other stuff. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Music - singing, dancing, or making music myself. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Writing - writing storis, poetry, and other things. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                " Hey y'all, it's [name]. ":
                    menu:
                        " I like to do stuff like... ":
                            menu:
                                " Arts - drawing traditionally/digitally, and other stuff. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Music - singing, dancing, or making music myself. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Writing - writing storis, poetry, and other things. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                        " Stuff I like to do are... ":
                            menu:
                                " Arts - drawing traditionally/digitally, and other stuff. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Music - singing, dancing, or making music myself. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Writing - writing storis, poetry, and other things. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                        " I do... ":
                            menu:
                                " Arts - drawing traditionally/digitally, and other stuff. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Music - singing, dancing, or making music myself. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
                                " Writing - writing storis, poetry, and other things. ":
                                    menu:
                                        " I hope we can all be good friends. ":
                                            jump introdone
                                        " I hope we can all be chill homies. ":
                                            jump introdone
                                        " I hope we can all be sigma. ":
                                            jump introdone
        label introdone:
            if kind == True:
                " You were finally done with your introduction, andy ou could already see a few people liking you! "
                " Or you're just tweaking out. "
            elif mean == True:
                " You cheered internally after you were done with your introduction. "
                " That was a pain to deal with, but it could've gone worse so it's fine. "
            elif calm == True:
                " You finish up your introduction and you wait for what the teacher would say. "
                " ...Are you seriously doing the chill guy pose rn{nw} "
            x " Thank you, [name]! "
            x " We still have a few seats open, so you can go ahead and sit where-ever you like. "
            msc " I'm Miss Circle, your new teacher, [name]. "
            msc " It's a pleasure to have you a part of our class! "
            hide misscircleneutral at right with easeoutright
            " You nod and then you then start deciding where you should sit. "
            " Where do you sit? (note: where you sit is permanent, you can't change it.) "
            if claireknow == True:
                menu:
                    " Claire, a white haired guy and a girl with a little rubber duckie on her head. ":
                        $ claengbub = True
                        jump claengbub
                    " A girl with sock puppets on her hands, and a shy looking guy with a leaf on his head. ":
                        $ abblana = True
                        jump abblana
                    " I'd like to sit alone. ":
                        $ alone = True
                        jump alone
            else:
                menu:
                    " A girl with a white bow, a white haired guy and a girl with a little rubber duckie on her head. ":
                        $ claengbub = True
                        jump claengbub
                    " A girl with sock puppets on her hands, and a shy looking guy with a leaf on his head. ":
                        $ abblana = True
                        jump abblana
                    " I'd like to sit alone. ":
                        $ alone = True
                        jump alone
            label claengbub:
                $ clairelv += 10
                $ engellv += 10
                $ bubblelv += 10
                show claireneutral at left with easeinright
                show engelneutral at center with easeinright
                show bubbleneutral at right with easeinright
                if claireknow == True:
                    $ engelknow = True
                    $ bubbleknow = True
                    hide claireneutral at bottom
                    show clairehappy at left
                    c " Oh, hey [name]! Glad that you came to sit with us! "
                    x " So, Claire.. this was the person you've been talking about? "
                    if kind == True:
                        c " Yep, [they] [are] pretty nice, actually! "
                    elif calm == True:
                        c " Uh huh, [they] [are] pretty chill, actually! "
                    elif mean == True:
                        c " Uh huh! [they] may look a little scary, but [they] [are] really nice! "
                    hide clairehappy
                    show claireneutral at left
                    c " Anyway, I'd like for you to meet my friends, [name]! "
                    hide engelneutral
                    show engelhappy at center
                    e " Hello there... I'm Engel. It's a pleasure to meet you, [name]! "
                    hide bubbleneutral at bottom
                    show bubblehappy at right
                    b " Hello!!! I'm Bubble!! Great to meet you!! I hope we can become good friends! "
                    msc " Alrighty, class! Now let's begin the lesson! "
                    " Time to pay attention. Or not. "
                    scene black with dissolve
                    pause 2.0
                    jump break1
                else:
                    if mean == True and clairebeatup == True:
                        " It's that same girl you saw from earlier. "
                        " She seemed to be talking normally with her friends, until she saw... you. "
                        hide claireneutral at bottom
                        show clairescared at left
                        " She froze. She looks terrified. "
                        " Her other friends look concerned. "
                        x " Claire...? What's wrong? Is everything alright? "
                        x " ... "
                        " She didn't respond. "
                        hide bubbleneutral at bottom
                        show bubblesad at right
                        x " Claire? You're kind of scaring us... you look like you've just seen a ghost... "
                        x " ... "
                        " She still didn't respond. "
                        " She didn't say anything, as if she was thinking that if she spoke up, you'd do something worse to her than the thing you did to her earlier. "
                        " You just stared at her, just like how she stared at you with those wide and fearful eyes. "
                        " From someone who looks so brave and confident... "
                        " ...She was so easily scared just by what you did. "
                        " Baffling, is it not? "
                        " What could've caused for her to act this way? "
                        $ clairewallbreak = renpy.random.randint = (1, 100)
                        if clairewallbreak == 50:
                            stop music
                            x " ... "
                            x " .-.. --- .-.. / -.-- --- ..- / - .... --- ..- --. .... - / - .... .. ... / .- -.-. - ..- .- .-.. .-.. -.-- / -- . .- -. - / ... --- -- . - .... .. -. --. / -.. .. -.. -. - / -.-- --- ..- "
                            scene black
                            pause 2.0
                            play music "audio/paperhigh.mp3"
                            jump break1
                        else:
                            msc " Alright class, time to start our first lesson for today! "
                            " Time to pay attention then. "
                            scene black with dissolve
                            " You spent the entire class listening to what the teacher has said. "
                            " As the teacher talked, you could notice that the girl near you looked... Uncomfortable. "
                            " As if she wasn't feeling well whilst you were next to her. "
                            " Well, you can't change your seat now. "
                            pause 2.0
                            play sound "audio/bellring.mp3"
                            " You then heard the bell ring, indicating that class was over. "
                            " You get up from your seat, and walked out back into the hallways. "
                            pause 2.0
                            jump break1
                    elif mean, claireknow == True and clairebeatup == False:
                        $ engelknow = True
                        $ bubbleknow = True
                        hide claireneutral at bottom
                        show clairehappy at left
                        c " Oh, hey [name]! Glad that you came to sit with us! "
                        x " So, Claire.. this was the person you've been talking about? "
                        if kind == True:
                            c " Yep, [they] [are] pretty nice, actually! "
                        elif calm == True:
                            c " Uh huh, [they] [are] pretty chill, actually! "
                        elif mean == True:
                            c " Uh huh! [they] may look a little scary, but [they] [are] really nice! "
                        hide clairehappy
                        show claireneutral at left
                        c " Anyway, I'd like for you to meet my friends, [name]! "
                        hide engelneutral
                        show engelhappy at center
                        e " Hello there... I'm Engel. It's a pleasure to meet you, [name]! "
                        hide bubbleneutral at bottom
                        show bubblehappy at right
                        b " Hello!!! I'm Bubble!! Great to meet you!! I hope we can become good friends! "
                        msc " Alrighty, class! Now let's begin the lesson! "
                        " Time to pay attention. Or not. "
                        scene black with dissolve
                        pause 2.0
                        jump break1
                    else:
                        $ claireknow = True
                        $ engelknow = True
                        $ bubbleknow = True
                        " You seemed to recognize that one girl over on the left... "
                        " It seems it was that one girl that tripped and got her books all over the floor. "
                        " They seem to be busy talking to eachother, but it didn't take long for them to notice you. "
                        hide claireneutral at bottom
                        show clairehappy at right
                        x " Oh, hey! It's that new kid! Hello! "
                        hide engelneutral at bottom
                        show engelhappy at center
                        x " Do you think we should introduce ourselves to [them]...? "
                        hide bubbleneutral at bottom
                        show bubblehappy at left
                        x " Of course we should! We wanna make a good impression on [them], don't we? "
                        x " Mhm. "
                        c " I'm Claire! "
                        e " I'm Engel. "
                        b " And I'm Bubble! "
                        c " It's nice to meet you, [name]! "
                        e " It's nice to have a new friend join us... "
                        b " I hope we can be very good friends! Welcome to our friend group! "
                        " Well, they're a nice bunch... "
                        " You can tell it was a good choice choosing to sit with them. "
                        msc " Alrighty class, it's time to start our first lesson of the day! "
                        msc " Pay attention now! "
                        " Let's focus on class so that you won't get beaten up by the teacher. "
                        scene black with dissolve
                        pause 2.0
                        play sound "audio/bellring.mp3"
                        " You then heard the bell ring, indicating that class was over. "
                        " You get up from your seat, and walked out back into the hallways. "
                        pause 2.0
                        jump break1
                        # reminder to change the parts where you explain to bubble and engel what happened
                        # and also the part where claire asks you for forgiveness or something
            label abblana:
                $ abbielv += 10
                $ lanalv += 10
                $ abbieknow = True
                $ lanaknow = True
                show lananeutral at appearleft
                show abbieneutral at appearright
                x " Hmm, hmm... "
                " The girl seems to be busy making some sock puppets... until she noticed you. "
                hide lananeutral at bottom
                show lanahappy at left
                x " Oh, hi there! "
                x " Abbie, lookie, lookie! The new kid sat with us! "
                a " Huh...? Oh, uh... hi there... "
                hide lanahappy at bottom
                show lananeutral at left
                l " I'm Lana! This is my good friend, Abbie! "
                l " It's a pleasure to meet you!! "
                a " ...It's nice to meet you... "
                hide lananeutral
                show lanahappy at left
                l " I hope we'll be good friends! "
                a " ...Y-yeah... "
                msc " Alright, class! Let's get started with today's lesson! "
                " Time to pay attention... or not. "
                scene black with dissolve
                pause 2.0
                jump break1
            label alone:
                " You go and sit alone so that you won't be disturbed by anyone. "
                " Atleast now you don't have to deal with annoying seatmates. "
                msc " Alright, class! Let's get started with today's lesson! "
                " Time to pay attention... or not. "
                scene black with dissolve
                pause 2.0
                jump break1
            label break1:
                " You pretty much just sat around in your seat the entire time you were there. "
                " Eventually, your first break started and you left your seat and went outside to the hallways. "
                scene hallway with dissolve
                " Break has started, and you feel like exploring the school. "
                " Where should you go for the break? "
                menu:
                    " {image=claireicon} The front of the school {image=claireicon} ":
                        " You decide to go to the front of the school to relax a bit. "
                        scene black with dissolve
                        pause 1.0
                        jump frontschool1
                    " {image=skellicon} The back of the school {image=skellicon} ":
                        " You decide to go to the back of the school to relax there for a bit. "
                        scene black with dissolve
                        pause 1.0
                        jump backschool1
                    " {image=bubbleicon} The gym {image=bubbleicon} ":
                        " You decide to go to the gym to chill there. "
                        scene black with dissolve
                        pause 1.0
                        jump gym1
                    " The cafeteria ":
                        " You decide to go to the cafeteria. "
                        scene black with dissolve
                        pause 1.0
                        jump cafe1
                    " {image=lanaicon} The rooftop {image=abbieicon} ":
                        " You decide to go to the rooftop to relax there. "
                        scene black with dissolve
                        pause 1.0
                        jump rooftop1
                    " {image=engelicon} The library {image=engelicon} ":
                        " You decide to go to the library to read some books or chill there. "
                        scene black with dissolve
                        pause 1.0
                        jump library1
                label frontschool1:
                    scene paperschoolfront with dissolve
                    " You go outside of the school, taking in some fresh air. "
                    " It's a lot more quieter here than inside the school, a place where you can take a short break. "
                    " You then spot someone sitting on a bench. They look quite lonely... "
                    " You decide to approach them and sit next to them. "
                    show claireneutral at center with dissolve
                    if claireknow == True:
                        c " Hm... "
                        " She seems to be lost in thought. "
                        " She then notices you after a few minutes. "
                        if claireknow == True and engelknow == True:
                            c " Oh, hello there, [name]! Sorry that I didn't notice you, heh... "
                            c " It's just that I was thinking about a few things. "
                            c " Anyway, what brings you here? just out to get fresh air? "
                            c " Well, same for me, then... "
                            c " Sometimes it gets a little too loud whenever I'm inside the school. "
                            c " It's a bit... uh... how do I say this... "
                            c " School's a bit...overwhelming? is that the right word to describe it? "
                            c " Ehh, whatever...it's just that there's these bullies going around... "
                            hide claireneutral at bottom
                            show claireangry at center
                            c " And they like to mess with me and my friends a lot. "
                            c " They're so annoying, yet most of the teachers let them have a passing grade without them doing anything to actually achieve that! "
                            c " But, then again... I can't really complain. The teachers aren't really gonna change anything about that. "
                            hide claireangry at bottom
                            show claireneutral at center
                            c " Another thing is that sometimes...the teachers can get really strict. "
                            c " There's three teachers that have a rule; if you fail... you get... "
                            hide claireneutral at bottom
                            show clairescared at center
                            c " ... "
                            c " You know, I wouldn't want to talk about it, but... "
                            hide clairescared at bottom
                            show clairesad at center
                            c " Let's just say...you go 'missing'. Forever. "
                            c " And I don't want that to happen to me or my friends, so sometimes I get tutoring lessons from Engel. "
                            c " And I'd help other people who are struggling, too... "
                            c " This school's got a lot of people reported missing in the past, but... "
                            c " For now, there isn't really any of that going on right now. "
                            hide clairesad at bottom
                            show claireneutral at center
                            c " That should be a good thing, right? "
                            c " Atleast there's no one going missing for now, but who knows.. It might just happen again. "
                            play sound "audio/bellring.mp3"
                            pause 1.0
                            c " Oh, it's time for the next class... "
                            hide claireneutral at bottom
                            show clairehappy at center
                            c " I'll see you in class, then, [name]! "
                            hide clairehappy at right with easeoutright
                            scene black with dissolve
                            " You follow Claire to your next class. "
                            jump languageclass1
                        elif claireknow == True and engelknow == False:
                            c " Oh, hello there, [name]! Sorry that I didn't notice you, heh... "
                            c " It's just that I was thinking about a few things. "
                            c " Like, I was thinking of making you meet my other friends! But maybe we could do that later?"
                            c " Anyway, what brings you here? just out to get fresh air? "
                            c " Well, same for me, then... "
                            c " Sometimes it gets a little too loud whenever I'm inside the school. "
                            c " It's a bit... uh... how do I say this... "
                            c " School's a bit...overwhelming? is that the right word to describe it? "
                            c " Ehh, whatever...it's just that there's these bullies going around... "
                            hide claireneutral at bottom
                            show claireangry at center
                            c " And they like to mess with me and my friends a lot. "
                            c " They're so annoying, yet most of the teachers let them have a passing grade without them doing anything to actually achieve that! "
                            c " But, then again... I can't really complain. The teachers aren't really gonna change anything about that. "
                            hide claireangry at bottom
                            show claireneutral at center
                            c " Another thing is that sometimes...the teachers can get really strict. "
                            c " There's three teachers that have a rule; if you fail... you get... "
                            hide claireneutral at bottom
                            show clairescared at center
                            c " ... "
                            c " You know, I wouldn't want to talk about it, but... "
                            hide clairescared at bottom
                            show clairesad at center
                            c " Let's just say...you go 'missing'. Forever. "
                            c " And I don't want that to happen to me or my friends, so sometimes I get tutoring lessons from Engel. "
                            c " And I'd help other people who are struggling, too... "
                            c " This school's got a lot of people reported missing in the past, but... "
                            c " For now, there isn't really any of that going on right now. "
                            hide clairesad at bottom
                            show claireneutral at center
                            c " That should be a good thing, right? "
                            c " Atleast there's no one going missing for now, but who knows.. It might just happen again. "
                            play sound "audio/bellring.mp3"
                            pause 1.0
                            c " Oh, it's time for the next class... "
                            hide claireneutral at bottom
                            show clairehappy at center
                            c " I'll see you in class, then, [name]! "
                            hide clairehappy at right with easeoutright
                            scene black with dissolve
                            " You follow Claire to your next class. "
                            jump languageclass1
                        elif claireknow == True and clairebeatup == False:
                            c " Oh, hello there, [name]! Sorry that I didn't notice you, heh... "
                            c " It's just that I was thinking about a few things. "
                            c " Anyway, what brings you here? just out to get fresh air? "
                            c " Well, same for me, then... "
                            c " Sometimes it gets a little too loud whenever I'm inside the school. "
                            c " It's a bit... uh... how do I say this... "
                            c " School's a bit...overwhelming? is that the right word to describe it? "
                            c " Ehh, whatever...it's just that there's these bullies going around... "
                            hide claireneutral at bottom
                            show claireangry at center
                            c " And they like to mess with me and my friends a lot. "
                            c " They're so annoying, yet most of the teachers let them have a passing grade without them doing anything to actually achieve that! "
                            c " But, then again... I can't really complain. The teachers aren't really gonna change anything about that. "
                            hide claireangry at bottom
                            show claireneutral at center
                            c " Another thing is that sometimes...the teachers can get really strict. "
                            c " There's three teachers that have a rule; if you fail... you get... "
                            hide claireneutral at bottom
                            show clairescared at center
                            c " ... "
                            c " You know, I wouldn't want to talk about it, but... "
                            hide clairescared at bottom
                            show clairesad at center
                            c " Let's just say...you go 'missing'. Forever. "
                            c " And I don't want that to happen to me or my friends, so sometimes I get tutoring lessons from Engel. "
                            c " And I'd help other people who are struggling, too... "
                            c " This school's got a lot of people reported missing in the past, but... "
                            c " For now, there isn't really any of that going on right now. "
                            hide clairesad at bottom
                            show claireneutral at center
                            c " That should be a good thing, right? "
                            c " Atleast there's no one going missing for now, but who knows.. It might just happen again. "
                            play sound "audio/bellring.mp3"
                            pause 1.0
                            c " Oh, it's time for the next class... "
                            hide claireneutral at bottom
                            show clairehappy at center
                            c " I'll see you in class, then, [name]! "
                            hide clairehappy at right with easeoutright
                            scene black with dissolve
                            " You follow Claire to your next class. "
                            jump languageclass1
                        elif claireknow == True and clairebeatup == True:
                            hide claireneutral at bottom
                            show clairescared at center
                            " She stares at you. She looks... horrified. "
                            " She's freezing in her place, as if she's afraid that you might do something to her. "
                            " What's wrong with her? You just came over to do nothing. To just sit there near her. "
                            " She gets up from her seat, before she makes an attempt to run back into the school. "
                            " What should you do? "
                            menu:
                                " Catch up to her and tell her that you're sorry ":
                                    " You catch up to her and grab her wrist, stopping her from running away further. "
                                    " You then tell her that you're sorry for what you did earlier and that you didn't mean it. "
                                    " You explained to her that someone paid you to do that to her. "
                                    " That was a lie, but what else could you say to her to get her to forgive you? "
                                    x " ...Y..you're sorry...? "
                                    " You nod your head, confirming that you were indeed sorry. "
                                    x " ...Well... "
                                    hide clairescared at bottom
                                    show claireneutral at center
                                    $ clairesorry = True
                                    x " Just don't do that again, okay? Even if someone paid you to do it. "
                                    x " I forgive you. "
                                    x " Um, since we're all nice and calm now... How about I introduce myself? "
                                    $ claireknow = True
                                    c " I'm Claire. You're [name], right? "
                                    c " It's nice to meet you. I'll see you later, okay? "
                                    c " I just remembered that I had to help a friend out with their homework. "
                                    c " They forgot to do it last night... "
                                    c " Byebye, for now. "
                                    hide claireneutral at right with easeoutright
                                    " She then left to go help her friend. "
                                    " You went back to sit on the bench you were sitting on earlier to chillax. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rings after awhile, and you get up to go to your next class. "
                                    scene black with dissolve
                                    pause 2.0
                                    jump languageclass1
                                " {sc}Don't run away from me.{/sc} ":
                                    stop music
                                    " You're not letting her get away from you. "
                                    play music "audio/worry.mp3"
                                    " You easily catch up to her and grab her wrist, stopping her from running. "
                                    " She was about to scream for help, but you started choking her and slapping her on the face. "
                                    " Shut up, you brat. "
                                    " No one's going to hear your screams. No one's going to help you. "
                                    " You'll die alone with no one to remember who you even were. "
                                    " You're a nobody, and it would've been better if you just disappeared. "
                                    stop music
                                    play music "audio/concern.mp3"
                                    " Come on, {sc}die already.{/sc} "
                                    " Quit struggling and just die already. "
                                    " How about I break your limbs and tear you to shreds? "
                                    " Or I could cook you alive and feed you to your friends and family. "
                                    " They wouldn't even know that it's you. "
                                    stop music
                                    play sound "audio/bellring.mp3"
                                    " The bell rings before you could actually kill her. "
                                    hide clairescared at bottom with easeoutbottom
                                    " You threw her to the ground harshly. You see her trying to catch her breath. "
                                    scene black with dissolve
                                    " You went back inside the school, going to your classroom. "
                                    " You didn't care that you almost killed your classmate. "
                                    " But, after a few minutes... You can't help but feel a little guilty. "
                                    " She didn't deserve that. She did nothing. "
                                    " The more you thought about it, the more guilty and regretful you felt. "
                                    " How could you do something like that...? "
                                    " ... "
                                    " Whatever. It's too late to fix things. "
                                    " You sit in your seat and wait for the teacher to come. "
                                    pause 2.0
                                    play music "audio/paperhigh.mp3"
                                    jump languageclass1
                        elif claireknow == False and clairebeatup == True:
                            hide claireneutral at bottom
                            show clairescared at center
                            " She stares at you. She looks... horrified. "
                            " She's freezing in her place, as if she's afraid that you might do something to her. "
                            " What's wrong with her? You just came over to do nothing. To just sit there near her. "
                            " She gets up from her seat, before she makes an attempt to run back into the school. "
                            " What should you do? "
                            menu:
                                " Catch up to her and tell her that you're sorry ":
                                    " You catch up to her and grab her wrist, stopping her from running away further. "
                                    " You then tell her that you're sorry for what you did earlier and that you didn't mean it. "
                                    " You explained to her that someone paid you to do that to her. "
                                    " That was a lie, but what else could you say to her to get her to forgive you? "
                                    x " ...Y..you're sorry...? "
                                    " You nod your head, confirming that you were indeed sorry. "
                                    x " ...Well... "
                                    hide clairescared at bottom
                                    show claireneutral at center
                                    $ clairesorry = True
                                    x " Just don't do that again, okay? Even if someone paid you to do it. "
                                    x " I forgive you. "
                                    x " Um, since we're all nice and calm now... How about I introduce myself? "
                                    $ claireknow = True
                                    c " I'm Claire. You're [name], right? "
                                    c " It's nice to meet you. I'll see you later, okay? "
                                    c " I just remembered that I had to help a friend out with their homework. "
                                    c " They forgot to do it last night... "
                                    c " Byebye, for now. "
                                    hide claireneutral at right with easeoutright
                                    " She then left to go help her friend. "
                                    " You went back to sit on the bench you were sitting on earlier to chillax. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rings after awhile, and you get up to go to your next class. "
                                    scene black with dissolve
                                    pause 2.0
                                    jump languageclass1
                                " {sc}Don't run away from me.{/sc} ":
                                    stop music
                                    " You're not letting her get away from you. "
                                    play music "audio/worry.mp3"
                                    " You easily catch up to her and grab her wrist, stopping her from running. "
                                    " She was about to scream for help, but you started choking her and slapping her on the face. "
                                    " Shut up, you brat. "
                                    " No one's going to hear your screams. No one's going to help you. "
                                    " You'll die alone with no one to remember who you even were. "
                                    " You're a nobody, and it would've been better if you just disappeared. "
                                    stop music
                                    play music "audio/concern.mp3"
                                    " Come on, {sc}die already.{/sc} "
                                    " Quit struggling and just die already. "
                                    " How about I break your limbs and tear you to shreds? "
                                    " Or I could cook you alive and feed you to your friends and family. "
                                    " They wouldn't even know that it's you. "
                                    stop music
                                    play sound "audio/bellring.mp3"
                                    " The bell rings before you could actually kill her. "
                                    hide clairescared at bottom with easeoutbottom
                                    " You threw her to the ground harshly. You see her trying to catch her breath. "
                                    scene black with dissolve
                                    " You went back inside the school, going to your classroom. "
                                    " You didn't care that you almost killed your classmate. "
                                    " But, after a few minutes... You can't help but feel a little guilty. "
                                    " She didn't deserve that. She did nothing. "
                                    " The more you thought about it, the more guilty and regretful you felt. "
                                    " How could you do something like that...? "
                                    " ... "
                                    " Whatever. It's too late to fix things. "
                                    " You sit in your seat and wait for the teacher to come. "
                                    pause 2.0
                                    play music "audio/paperhigh.mp3"
                                    jump languageclass1
                    else:
                        if claireknow == False and clairebeatup == True:
                            hide claireneutral at bottom
                            show clairescared at center
                            " She stares at you. She looks... horrified. "
                            " She's freezing in her place, as if she's afraid that you might do something to her. "
                            " What's wrong with her? You just came over to do nothing. To just sit there near her. "
                            " She gets up from her seat, before she makes an attempt to run back into the school. "
                            " What should you do? "
                            menu:
                                " Catch up to her and tell her that you're sorry ":
                                    " You catch up to her and grab her wrist, stopping her from running away further. "
                                    " You then tell her that you're sorry for what you did earlier and that you didn't mean it. "
                                    " You explained to her that someone paid you to do that to her. "
                                    " That was a lie, but what else could you say to her to get her to forgive you? "
                                    x " ...Y..you're sorry...? "
                                    " You nod your head, confirming that you were indeed sorry. "
                                    x " ...Well... "
                                    hide clairescared at bottom
                                    show claireneutral at center
                                    $ clairesorry = True
                                    x " Just don't do that again, okay? Even if someone paid you to do it. "
                                    x " I forgive you. "
                                    x " Um, since we're all nice and calm now... How about I introduce myself? "
                                    $ claireknow = True
                                    c " I'm Claire. You're [name], right? "
                                    c " It's nice to meet you. I'll see you later, okay? "
                                    c " I just remembered that I had to help a friend out with their homework. "
                                    c " They forgot to do it last night... "
                                    c " Byebye, for now. "
                                    hide claireneutral at right with easeoutright
                                    " She then left to go help her friend. "
                                    " You went back to sit on the bench you were sitting on earlier to chillax. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rings after awhile, and you get up to go to your next class. "
                                    scene black with dissolve
                                    pause 2.0
                                    jump languageclass1
                                " {sc}Don't run away from me.{/sc} ":
                                    stop music
                                    " You're not letting her get away from you. "
                                    play music "audio/worry.mp3"
                                    " You easily catch up to her and grab her wrist, stopping her from running. "
                                    " She was about to scream for help, but you started choking her and slapping her on the face. "
                                    " Shut up, you brat. "
                                    " No one's going to hear your screams. No one's going to help you. "
                                    " You'll die alone with no one to remember who you even were. "
                                    " You're a nobody, and it would've been better if you just disappeared. "
                                    stop music
                                    play music "audio/concern.mp3"
                                    " Come on, {sc}die already.{/sc} "
                                    " Quit struggling and just die already. "
                                    " How about I break your limbs and tear you to shreds? "
                                    " Or I could cook you alive and feed you to your friends and family. "
                                    " They wouldn't even know that it's you. "
                                    stop music
                                    play sound "audio/bellring.mp3"
                                    " The bell rings before you could actually kill her. "
                                    hide clairescared at bottom with easeoutbottom
                                    " You threw her to the ground harshly. You see her trying to catch her breath. "
                                    scene black with dissolve
                                    " You went back inside the school, going to your classroom. "
                                    " You didn't care that you almost killed your classmate. "
                                    " But, after a few minutes... You can't help but feel a little guilty. "
                                    " She didn't deserve that. She did nothing. "
                                    " The more you thought about it, the more guilty and regretful you felt. "
                                    " How could you do something like that...? "
                                    " ... "
                                    " Whatever. It's too late to fix things. "
                                    " You sit in your seat and wait for the teacher to come. "
                                    pause 2.0
                                    play music "audio/paperhigh.mp3"
                                    jump languageclass1
                        else:
                            x " Hm... "
                            " She seems to be lost in thought. "
                            " She then notices you after a few minutes. "
                            jump languageclass1
                            x " Oh, hello there, [name]! Sorry that I didn't notice you, heh... "
                            x " It's just that I was thinking about a few things. "
                            x " Wait, I just realized... I haven't introduced myself to you yet! "
                            $ claireknow = True
                            c " I'm Claire! Wego to the same class, eheh... "
                            c " Anyway, what brings you here? just out to get fresh air? "
                            c " Well, same for me, then... "
                            c " Sometimes it gets a little too loud whenever I'm inside the school. "
                            c " It's a bit... uh... how do I say this... "
                            c " School's a bit...overwhelming? is that the right word to describe it? "
                            c " Ehh, whatever...it's just that there's these bullies going around... "
                            hide claireneutral at bottom
                            show claireangry at center
                            c " And they like to mess with me and my friends a lot. "
                            c " They're so annoying, yet most of the teachers let them have a passing grade without them doing anything to actually achieve that! "
                            c " But, then again... I can't really complain. The teachers aren't really gonna change anything about that. "
                            hide claireangry at bottom
                            show claireneutral at center
                            c " Another thing is that sometimes...the teachers can get really strict. "
                            c " There's three teachers that have a rule; if you fail... you get... "
                            hide claireneutral at bottom
                            show clairescared at center
                            c " ... "
                            c " You know, I wouldn't want to talk about it, but... "
                            hide clairescared at bottom
                            show clairesad at center
                            c " Let's just say...you go 'missing'. Forever. "
                            c " And I don't want that to happen to me or my friends, so sometimes I get tutoring lessons from Engel. "
                            c " And I'd help other people who are struggling, too... "
                            c " This school's got a lot of people reported missing in the past, but... "
                            c " For now, there isn't really any of that going on right now. "
                            hide clairesad at bottom
                            show claireneutral at center
                            c " That should be a good thing, right? "
                            c " Atleast there's no one going missing for now, but who knows.. It might just happen again. "
                            play sound "audio/bellring.mp3"
                            pause 1.0
                            c " Oh, it's time for the next class... "
                            hide claireneutral at bottom
                            show clairehappy at center
                            c " I'll see you in class, then, [name]! "
                            hide clairehappy at right with easeoutright
                            scene black with dissolve
                            " You follow Claire to your next class. "
                            jump languageclass1
                label backschool1:
                    scene paperschoolback with dissolve
                    " You walk to the back of the school. It's much more quieter here than the inside of the school. "
                    " You could hear birds chirping. The sun is shining and flowers are blooming. "
                    " This would be the perfect day to just relax and hang out. "
                    " You sit down against a wall, and don't notice that there was someone sitting next to you. "
                    " You eventually turn your head and look at them once they made a noise to let you acknowledge their existence. "
                    show skellneutral at center with dissolve
                    x " Uh... hey there. "
                    " It was a guy that...looked like a cat-ish? Except for the fact that they had wings, too. "
                    " They seem a tad bit awkward, as if they didn't know that someone would come to the back of the school at this hour. "
                    " It was silent until they spoke up again. "
                    x " So... you just gonna hang out here for a bit? "
                    x " Or do you want me to leave? For like, space and stuff so that you can be alone. "
                    menu:
                        " Let him stay ":
                            $ skellknow = True
                            hide skellneutral at bottom
                            show skellsurprised at center
                            x " ...You want me to stay? "
                            hide skellsurprised at bottom
                            show skellneutral at center
                            x " Well... If you say so, then. "
                            sk " The name's Skell. "
                            sk " You must be the new kid, yeah? I kinda was listening to some music while you were introducing yourself. Sorry. "
                            sk " It's nice to meet you though... "
                            menu:
                                " What kind of music do you listen to? ":
                                    sk " Mostly metal music. "
                                    sk " Though, I do listen to other types of music... "
                                    sk " But I can't really tell you what other stuff I listen to. It's embarrassing. "
                                    sk " Maybe I'll tell you sometime, just not right now. "
                                    sk " Do you...wanna...maybe... "
                                    sk " Listen to this playlist that I have...? "
                                    menu:
                                        " Sure ":
                                            sk " Alright. "
                                            " Skell hands you over one of his earphones so that you both can listen to his music. "
                                            " You and Skell listen to music for the rest of the break. "
                                            " It was mostly just metal music, the other ones being sad and depressing songs... "
                                            " For a short bit, you could hear 'world is mine' by Hatsune Miku playing from his playlist, but he quickly skips it. "
                                            " He seems a little embarrassed about that one, but you didn't seem to judge him for it. "
                                            " We listen and we don't judge. "
                                            play sound "audio/bellring.mp3"
                                            " Once the bell rang, you both got up and went to the next class for the day. "
                                            scene black with dissolve
                                            pause 1.0
                                            jump languageclass1
                                        " Nah I'm good ":
                                            sk " If you say so, then. "
                                            " You spent your time watching the sky and other stuff while you and Skell just vibe. "
                                            " You hear 'World is mine' by Hatsune Miku coming from Skell's earphones. "
                                            " But you didn't really have the heart to tell him that his music was THAT loud. "
                                            " ...Now that's just making you wonder how his ears are feeling about the fact his music is so loud to the point someone else can hear them. "
                                            " His poor ears. "
                                            play sound "audio/bellring.mp3"
                                            " Once the bell rang, you both got up and went to the next class for the day. "
                                            scene black with dissolve
                                            pause 1.0
                                            jump languageclass1
                                " What are you doing? ":
                                    sk " Just vibing, mostly. "
                                    sk " It's honestly comforting to be out here most of the time. "
                                    sk " Away from those stupid bullies that keep bullying me for being 'emo'... "
                                    sk " ...Do you think I'm weird for being like this? You probably do, don't you? "
                                    menu:
                                        " I think you're cool. ":
                                            hide skellneutral at bottom
                                            show skellsurprised at center
                                            sk " ...You really do? "
                                            hide skellsurprised at bottom
                                            show skellneutral at center
                                            sk " That's... nice to hear. "
                                            sk " No one's really said something nice about me, other than my friend, Ruby. "
                                            sk " I appreciate that, dude. "
                                            sk " It kinda sucks since I keep getting bullied, but sometimes whenever I'm actually left alone... "
                                            sk " The silence is comforting. The feeling of being alone feel comforting. "
                                            sk " So, whenever I'm alone, I kinda feel comforted because it feels like no one's gonna judge me for what I do in my alone time. "
                                            sk " Because no one's watching what I do. It's nice. "
                                            play sound "audio/bellring.mp3"
                                            " You and Skell talk until the bell rings and it's time to go to class. "
                                            sk " Well, it's time for language class... "
                                            sk " I'll see you there, [name]. Talk to you later. "
                                            hide skellneutral at left with easeoutleft
                                            scene black with dissolve
                                            " You follow Skell to your next class. "
                                            pause 1.0
                                            jump languageclass1
                                        " Yeah you kinda suck ngl ":
                                            sk " I was expecting that. "
                                            sk " No one's really said something nice about me, other than my friend, Ruby. "
                                            sk " It kinda sucks, but you kinda get used to it the more people say that to you. "
                                            sk " But it would be pretty bad for you if you want attention and for people to like you and stuff. "
                                            sk " But, personally, I don't really want to be in the spotlight like most people do. "
                                            sk " I just wanna be alone sometimes, you get me? "
                                            play sound "audio/bellring.mp3"
                                            " You and Skell talk until the bell rings and it's time to go to class. "
                                            sk " Well, it's time for language class... "
                                            sk " I'll see you there, [name]. Talk to you later. "
                                            hide skellneutral at left with easeoutleft
                                            scene black with dissolve
                                            " You follow Skell to your next class. "
                                            pause 1.0
                                            jump languageclass1
                        " Move to another spot. ":
                            $ skellknow = False
                            x " You're gonna move to another spot? "
                            x " That's alright then. "
                            x " Later, dude. "
                            hide skellneutral at left with easeoutleft
                            " You move to another part of the back of the school so that you can have some sweet alone time. "
                            " You sit down again against a wall, enjoying the peave you're having without any disturbances. "
                            " You look up at the sky and you see a funny shaped cloud. "
                            " I would say what it is but it isn't really appropriate. "
                            play sound "audio/bellring.mp3"
                            " You sat there and thought to yourself until the bell eventually rang. "
                            " You got up and you headed off to your next class of the day. "
                            scene black with dissolve
                            pause 2.0
                            jump languageclass1
                label gym1:
                    scene poolroom with dissolve
                    " You decide to go to the gym. Honstly, the dev didn't know what to call this room so he just called it the gym. "
                    " Though it had a big ahh pool in it. He still doesn't know. "
                    " You go ahead and decide to sit on the bleachers and just watch the water for a bit. "
                    " You then look to your side and you see a girl. "
                    if bubbleknow == True:
                        " It was Bubble. She seemed to be playing around with the little ducky on her head. "
                        " Should you go and talk to her, or should you stay still, where you are? "
                        menu:
                            " Talk to her ":
                                show bubbleneutral at center with easeinleft
                                " You move to sit next to her and you tap on her shoulder so that you could get her attention. "
                                b " Oh, [name]! Hi there! "
                                b " I was kinda bored while waiting for break to be over, so I'm glad that you're here to spend some time with me! "
                                b " So... how're you doing today? "
                                menu:
                                    " Doing fine ":
                                        hide bubbleneutral at bottom
                                        show bubblehappy at center
                                        b " That's good, then! "
                                        hide bubblehappy at bottom
                                        show bubbleneutral at center
                                        b " I'm doing fine aswell... "
                                        b " Except for the fact that there's been these bullies targetting our classmates... "
                                        b " You've heard of them, right? Oliver, Zip, and Edward? "
                                        hide bubbleneutral at bottom
                                        show bubbleangry at center
                                        b " Well... once they stole my rubber duckie when I wasn't looking, "
                                        b " And at the end of the day, I found out that it was in one of the school's trash cans! "
                                        hide bubbleangry at bottom
                                        show bubblesad at center
                                        b " I was so worried about my duckie, you know...! I even had Claire and Engel to help me out! "
                                        b " Everytime it was time for us to go to class, I would worry about where my duckie was! "
                                        b " I know I can just get a new one to replace it, but it's really special to me! "
                                        hide bubblesad at bottom
                                        show bubbleneutral at center
                                        b " It's good that we found it, though... Engel was the one that spotted it. "
                                        b " Still, the thought of my duckie being lost forever is horrifying to me...! "
                                        b " Ive got to make sure that doesnt happen again, but how...? "
                                        b " I cant just glue the duck onto my hair, my hair is literally made up of bubbles... "
                                        b " Well, my parents didnt name me Bubble for nothing... "
                                        b " I guess Ill just have to keep a close eye on it... Or ask my friends to keep an eye on it. "
                                        b " Who knows, they might steal my duck again! "
                                        hide bubbleneutral at bottom
                                        show bubblehappy at center
                                        b " You can keep a close eye on it, right? I trust you! "
                                        b " I know you'll do a good job on keeping those bullies away! "
                                        hide bubblehappy at bottom
                                        show bubbleneutral at center
                                        play sound "audio/bellring.mp3"
                                        " The bell rings. It's time for you to go to class. "
                                        b " Oh... language class! Let's get going, [name]! "
                                        b " We don't want to be late! "
                                        hide bubbleneutral at right with easeoutright
                                        scene black with dissolve
                                        pause 2.0
                                        jump languageclass1
                            " Stay where you are ":
                                " You decided to just stay where you were for the rest of the break. "
                                " You mostly just looked at walls, the water, your phone... "
                                " Not gonna lie, you were thinking about some 'what-ifs'...like what if your phone fell in the water. "
                                " Oh great it just fell in there. "
                                " Just trolling. "
                                play sound "audio/bellring.mp3"
                                " Once the bell rang, you went to your next class. "
                                scene black with dissolve
                                pause 2.0
                                jump languageclass1
                    else:
                        " It was a girl whose hair was just... bubbles. she was also playing around with the duck on her head. "
                        " Should you go and talk to her, or should you stay still, where you are? "
                        menu:
                            " Talk to her ":
                                $ bubbleknow = True
                                show bubbleneutral at center with easeinleft
                                " You move to sit next to her and you tap on her shoulder so that you could get her attention. "
                                x " Oh, [name]! Hi there! "
                                x " Wait - I haven't introduced myself before... ehm... "
                                hide bubbleneutral at bottom
                                show bubblehappy at center
                                b " I'm Bubble, nice to meet you! "
                                hide bubblehappy at bottom
                                show bubbleneutral at center
                                b " Anwyay, I was kinda bored while waiting for break to be over, so I'm glad that you're here to spend some time with me! "
                                b " So... how're you doing today? "
                                menu:
                                    " Doing fine ":
                                        hide bubbleneutral at bottom
                                        show bubblehappy at center
                                        b " That's good, then! "
                                        hide bubblehappy at bottom
                                        show bubbleneutral at center
                                        b " I'm doing fine aswell... "
                                        b " Except for the fact that there's been these bullies targetting our classmates... "
                                        b " You've heard of them, right? Oliver, Zip, and Edward? "
                                        hide bubbleneutral at bottom
                                        show bubbleangry at center
                                        b " Well... once they stole my rubber duckie when I wasn't looking, "
                                        b " And at the end of the day, I found out that it was in one of the school's trash cans! "
                                        hide bubbleangry at bottom
                                        show bubblesad at center
                                        b " I was so worried about my duckie, you know...! I even had Claire and Engel to help me out! "
                                        b " Everytime it was time for us to go to class, I would worry about where my duckie was! "
                                        b " I know I can just get a new one to replace it, but it's really special to me! "
                                        hide bubblesad at bottom
                                        show bubbleneutral at center
                                        b " It's good that we found it, though... Engel was the one that spotted it. "
                                        b " Still, the thought of my duckie being lost forever is horrifying to me! "
                                        b " I have got to find a way to keep a close eye on my duckie... "
                                        b " I can't just glue the duck onto my hair, my hair's literally made up of bubbles! "
                                        b " Well, my parents didn't name me Bubble for nothing... "
                                        b " I guess I'll just have to keep a close eye on it... Or ask my friends to keep an eye on it. "
                                        b " Who knows, they might steal my duck again! "
                                        hide bubbleneutral at bottom
                                        show bubblehappy at center
                                        b " You can keep a close eye on it, right? I trust you! "
                                        b " I know you'll do a good job on keeping those bullies away! "
                                        hide bubblehappy at bottom
                                        show bubbleneutral at center
                                        if mean, clairebeatup == True and clairesorry == False:
                                            b " Now that I think about it... "
                                            hide bubbleneutral at bottom
                                            show bubbleconfuse at center
                                            b " What happened with you and Claire? "
                                            if claengbub == True:
                                                b " Claire seemed pretty upset earlier. "
                                            else:
                                                b " Claire was upset earlier, and in class... She didn't look too happy when you entered the classroom. "
                                            b " I don't know If this is a sensitive topic or anything, but... I just want to know. "
                                            menu:
                                                " Nothing. Bubble doesn't need to know what you did. ":
                                                    $ clairesorry = False
                                                    b " Well... If you say so, then. "
                                                    play sound "audio/bellring.mp3"
                                                    hide bubbleconfuse at bottom
                                                    show bubbleneutral at center
                                                    " The bell rings. It's time for you to go to class. "
                                                    b " Oh... language class! Let's get going, [name]! "
                                                    b " We don't want to be late! "
                                                    hide bubbleneutral at right with easeoutright
                                                    scene black with dissolve
                                                    pause 2.0
                                                    jump languageclass1
                                        else:
                                            play sound "audio/bellring.mp3"
                                            " The bell rings. It's time for you to go to class. "
                                            b " Oh... language class! Let's get going, [name]! "
                                            b " We don't want to be late! "
                                            hide bubbleneutral at right with easeoutright
                                            scene black with dissolve
                                            pause 2.0
                                            jump languageclass1
                            " Stay where you are ":
                                " You decided to just stay where you were for the rest of the break. "
                                " You mostly just looked at walls, the water, your phone... "
                                " Not gonna lie, you were thinking about some 'what-ifs'...like what if your phone fell in the water. "
                                " Oh great it just fell in there. "
                                " Just trolling. "
                                play sound "audio/bellring.mp3"
                                " Once the bell rang, you went to your next class. "
                                scene black with dissolve
                                pause 2.0
                                jump languageclass1
                label cafe1:
                    scene cafeteria with dissolve
                    " You enter the cafeteria, and it's filled with people. Just the same as outside. "
                    " Who do you want to sit with? "
                    menu:
                        " {image=popularicon} A bunny girl, and another girl that has a little crown on her head. {image=popularicon} ":
                            $ popularknow = True
                            " You decided to walk up and sit with the popular-looking girls. "
                            " Not that you were trying to become popular, you just thought they looked cool. "
                            show lizzyneutral at left with easeinright
                            show petunianeutral at right with easeinright
                            x " - And then I heard that in Everleaf Highschool, they have a GHOST there! "
                            x " Woah, really?? Where'd you get this info, 'Tunia? "
                            hide petunianeutral at bottom
                            show petuniahappy at right
                            p " Well, I overheard a few people talking about it on the way here! "
                            hide petuniahappy at bottom
                            show petunianeutral at right
                            p " They say he only appears at night, and if you're alone in a room... "
                            p " He asks you to play a game and he'll ask you three riddles. "
                            p " If you get them wrong, apparently he kills you! "
                            x " All three? "
                            p " Well, there's some occasions where he'll let you live if you get 1 or 2 wrong, but it's rare! "
                            x " Oooh, interesting... "
                            p " Oh, hey! We've got that one kid in sitting next to us...whats [their] name? "
                            x " It was [name]. How could you forget [their] name, [they] literally did an introduction and everything. "
                            hide petunianeutral at bottom
                            show petuniahappy at right
                            p " That's my bad, Liz... I was looking at my phone. "
                            hide petuniahappy at bottom
                            show petunianeutral at right
                            p " Anyway! I'm Petunia, and this is my BEST FRIEND Lizzy! "
                            p " You've probably seen us a lot on TikTok, we're kinda famous! "
                            " ...You, for a fact haven't seen them. "
                            lz " Mhm. We share an account that has 190 followers. "
                            " No wonder why you haven't seen them before... They're not really too famous. "
                            p " Anyway, you wanna hear some drama? or are you just like...here to sit with us? "
                            menu:
                                " spill the tea ":
                                    hide petunianeutral
                                    show petuniahappy at right
                                    p " Now that's the spirit! "
                                    hide petuniahappy at bottom
                                    show petunianeutral at right
                                    p " Okay, so like did you hear about the time where... "
                                    scene black with dissolve
                                    " You, Petunia and Lizzy talk about some good ol' drama. "
                                    if claireknow == True:
                                        " It was actually pretty interesting, apparently Claire read a book about gay witches once...huh. "
                                    else:
                                        " It was actually pretty interesting, apparently a girl named Claire read a book about gay witches once...huh. "
                                    " Wonder where they got that information from. "
                                    " Probably because they snoop around a lot. Maybe. "
                                    play sound "audio/bellring.mp3"
                                    " Eventually, the bell rings and you all leave to go to the next class. "
                                    jump languageclass1
                                " nah im js here to chill ":
                                    p " Alrighty then... "
                                    p " Okay, so like did you hear about the time where... "
                                    scene black with dissolve
                                    " You just sort of chilled around with Petunia and Lizzy. "
                                    " You could hear some of the drama they were talking about, but you were too busy to actually listen to them. "
                                    " Busy looking at twitter on your phone about goofy pictures of people getting exposed. "
                                    play sound "audio/bellring.mp3"
                                    " Eventually, the bell rings and you all leave to go to the next class. "
                                    jump languageclass1
                        " {image=rubyicon} A girl with a robot head, and a guy with a goofy looking hat. {image=robbyicon} ":
                            $ rubyknow = True
                            $ robbyknow = True
                            " You decided to hang out with the weird looking group, because honestly you were considered a weird kid back then too. "
                            show rubyneutral at left with easeinright
                            show robbyneutral at right with easeinright
                            x " Robby! Did you study for the science test we're having later? "
                            x " 'Course I did. The topic wasn't really that hard, in all honesty. "
                            hide rubyneutral at bottom
                            show rubyhappy at left
                            x " Ooh, alright! "
                            hide rubyhappy at bottom
                            show rubyneutral at left
                            x " Oh, heyy! It's the new kid! "
                            hide rubyneutral at bottom
                            show rubyhappy at left
                            ru " Heyy! I'm Ruby, so glad to meet you! "
                            rb " I'm Robby. "
                            hide rubyhappy at bottom
                            show rubyneutral at left
                            ru " Sooo, [name]! Do you wanna study with us for the science class test? "
                            menu:
                                " Sure ":
                                    ru " Alrighty! Hold on... "
                                    hide rubyneutral at bottom
                                    show rubyconfused at left
                                    ru " Where's Riley? She was just here a few moments ago... "
                                    rb " Most likely stalking Oliver again. Geez, when will she stop doing that... "
                                    hide robbyneutral at bottom
                                    show robbyconfused at right
                                    rb " Sometimes I even wonder what she sees in that guy. "
                                    rb " Doesn't Oliver have a girlfriend or something...? "
                                    hide robbyconfused at bottom
                                    hide rubyconfused at bottom
                                    show rubyneutral at left
                                    show robbyneutral at right
                                    rb " Anyway, let's get studying. We're getitng a tad bit distracted here. "
                                    ru " Hmmm...alright! "
                                    scene black with dissolve
                                    " You study with Ruby and Robby for the upcoming science quiz. "
                                    " You've gained the answers for the science quiz! All in order: "
                                    " Gravitational Force, NaCl, Mitochondria, Milky way, Mantle. "
                                    " ...Yeah pretty simple answers I know. "
                                    play sound "audio/bellring.mp3"
                                    " After you're done studying with Ruby and Robby, the bell rings. "
                                    " You all then go to your next class, which is language class. "
                                    pause 2.0
                                    jump languageclass1
                                " Nah ":
                                    ru " You just wanna hang out with us? That's fine! "
                                    ru " ...One moment... "
                                    hide rubyneutral at bottom
                                    show rubyconfused at left
                                    ru " Where's Riley? She was just here a few moments ago... "
                                    rb " Most likely stalking Oliver again. Geez, when will she stop doing that... "
                                    hide robbyneutral at bottom
                                    show robbyconfused at right
                                    rb " Sometimes I even wonder what she sees in that guy. "
                                    rb " Doesn't Oliver have a girlfriend or something...? "
                                    hide robbyconfused at bottom
                                    hide rubyconfused at bottom
                                    show rubyneutral at left
                                    show robbyneutral at right
                                    rb " Anyway, let's get studying. We're getitng a tad bit distracted here. "
                                    ru " Hmmm...alright! "
                                    scene black with dissolve
                                    " You just hung around with Ruby and Robby whilst they studied. "
                                    " Meanwhile, you were on TikTok and looking at interesting slideshows you found. "
                                    " ...One slideshow just called you gay. "
                                    play sound "audio/bellring.mp3"
                                    " Eventually, the bell rang and you all went to the next class; which is English. "
                                    pause 2.0
                                    jump languageclass1
                        " {image=kevinicon} A guy that looks like a nerd, and a cute cat. {image=cubbieicon} ":
                            $ kevinknow = True
                            $ cubbieknow = True
                            " You walk up to them, but they seem pretty busy.. "
                            " You decide to sit next to the cute cat looking thing and you listened on into their conversation. "
                            show kevinconfused at left with easeinleft
                            show cubbieneutral at right with easeinleft
                            x " I believe that you're incorrect, Cubbie. 9 + 10 = 21, not 19. "
                            cb " ...?? (The little cat seems confused. 9 + 10 IS 19 though...) "
                            cb " ... (Seems like he's questioning the other boy's intelligence now.) "
                            x " Oh, why hello there, [name]. "
                            x " I am just teaching Cubbie how to do proper math, since he can't do 1 + 1. "
                            cb " ... (Cubbie can in fact, do 1 + 1.) "
                            x " Oh, right... I forgot that I haven't introduced myself to you. "
                            kv " My name is Kevin. Kevin nerdington the 3rd. Odd name, I know. "
                            kv " I keep being bullied for my name, but I'm rather proud of it. "
                            " ...Oh yeah at least your last name isn't something inappropriate. "
                            kv " I don't see what's wrong with being named 'Kevin Nerdington' though... "
                            kv " But anyway, would you like to help me teach Cubbie how to do proper math? "
                            menu:
                                " yeah ":
                                    kv " Alrighty! Cubbie, what's 10 + 10? "
                                    cb " ... (Cubbie writes down on a piece of paper that it's 20.) "
                                    hide kevinneutral at bottom
                                    show kevinconfused at left
                                    kv " ...It's 1010, you absolute idiot. "
                                    cb " ?????? (Cubbie seems more confused than ever. He doesn't understand.) "
                                    " You're wondering how Kevin gets somewhat good grades, according to something you've overheard. "
                                    " Should you tell him that it isn't 1010? or should you let him be stupid? "
                                    menu:
                                        " Tell him the truth. ":
                                            " You tell Kevin that it is in fact, 20, and you even pulled out a calculator to prove it. "
                                            kv " ... "
                                            hide kevinconfused at bottom
                                            show kevinsad at left
                                            kv " ...Oh. "
                                            kv " I {i}MAY{/i} be an idiot. "
                                            kv " You two might have to teach me a thing or two about proper math. "
                                            scene black with dissolve
                                            " You spent the rest of the break teaching Kevin how to do actual math. "
                                            " It was a little hard to explain it to him, but eventually he started understanding. "
                                            play sound "audio/bellring.mp3"
                                            " Eventually, in the middle of you and Cubbie teaching him, the bell rang. "
                                            " You all got up from your seats and you all went to the next class: Language. "
                                            pause 2.0
                                            jump languageclass1
                                        " Nah let him suffer. ":
                                            " You just watch Kevin teach Cubbie the wrong ways of doing math. "
                                            " You could see Cubbie asking you silently what was wrong with Kevin, and you shrug in response. "
                                            scene black with dissolve
                                            " You just sat with them and watched as Cubbie continued to struggle with Kevin. "
                                            " Both you and Cubbie know that Kevin's math is wrong, but you both didn't have the heart to tell him. "
                                            play sound "audio/bellring.mp3"
                                            " Thankfully, the bell rang before Cubbie could lose more braincells. "
                                            " You all then get up from your seats and you all went to the next class: Language. "
                                            pause 2.0
                                            jump languageclass1
                                " nah i wanna see you suffer ":
                                    kv " Alrighty, if you say so, then. "
                                    kv " Cubbie, what's 10 + 10? "
                                    cb " ... (Cubbie writes down on a piece of paper that it's 20.) "
                                    hide kevinneutral at bottom
                                    show kevinconfused at left
                                    kv " ...It's 1010, you absolute idiot. "
                                    cb " ?????? (Cubbie seems more confused than ever. He doesn't understand.) "
                                    " You're wondering how Kevin gets somewhat good grades, according to something you've overheard. "
                                    " Should you tell him that it isn't 1010? or should you let him be stupid? "
                                    menu:
                                        " Tell him the truth. ":
                                            " You tell Kevin that it is in fact, 20, and you even pulled out a calculator to prove it. "
                                            kv " ... "
                                            hide kevinconfused at bottom
                                            show kevinsad at left
                                            kv " ...Oh. "
                                            kv " I {i}MAY{/i} be an idiot. "
                                            kv " You two might have to teach me a thing or two about proper math. "
                                            scene black with dissolve
                                            " You spent the rest of the break teaching Kevin how to do actual math. "
                                            " It was a little hard to explain it to him, but eventually he started understanding. "
                                            play sound "audio/bellring.mp3"
                                            " Eventually, in the middle of you and Cubbie teaching him, the bell rang. "
                                            " You all got up from your seats and you all went to the next class: Language. "
                                            pause 2.0
                                            jump languageclass1
                                        " Nah let him suffer. ":
                                            " You just watch Kevin teach Cubbie the wrong ways of doing math. "
                                            " You could see Cubbie asking you silently what was wrong with Kevin, and you shrug in response. "
                                            scene black with dissolve
                                            " You just sat with them and watched as Cubbie continued to struggle with Kevin. "
                                            " Both you and Cubbie know that Kevin's math is wrong, but you both didn't have the heart to tell him. "
                                            play sound "audio/bellring.mp3"
                                            " Thankfully, the bell rang before Cubbie could lose more braincells. "
                                            " You all then get up from your seats and you all went to the next class: Language. "
                                            pause 2.0
                                            jump languageclass1
                        " I'll sit alone for now. ":
                            " You went over to one of the empty seats, and you just decided to sit there... "
                            " Like the loner you are. "
                            " You probably just decided to choose this option because talking to other people isn't really your thing. "
                            " You don't even talk that much, in general. "
                            " You opened up your phone and decided to scroll on tiktok for a bit. "
                            " Nothing interesting really pops up, other than a whole load of drama. "
                            play sound "audio/bellring.mp3"
                            " You continued to mindlessly scroll on tiktok, until you heard the bell ring."
                            " You put your phone back into your pocket and you got up from your seat. "
                            " You then went out of the cafeteria like the other students and you went to your next class: Language. "
                            scene black with dissolve
                            pause 2.0
                            jump languageclass1
                label library1:
                    scene library with dissolve
                    " You enter the library. Finally, some peace and quiet. "
                    " Though you have to make sure that you're quiet enough so that you won't disturb other people's reading. "
                    " You walk around, finding some interesting books that caught your attention. "
                    " Apparently there was a book that was a tutorial on how to bully someone... "
                    " You pick it out and it was just some random image taped onto a random book about science and stuff. "
                    " Don't know who did this, but they taped a drawing of very detailed male genitalia on the back of the book. "
                    " ...How come no one else noticed this? "
                    " You put the book back into its place, now removing the crude drawing and the 'bullying' image from it and throwing them into the trash. "
                    if engelknow == True:
                        " After a bit of walking, you spot Engel reading a book, all alone. "
                        " Should you sit next to him to see what he's reading? or do you leave him alone? "
                        menu:
                            " Sit next to him ":
                                show engelneutral at center with easeinright
                                " You walk over and you sat next to Engel, looking at what he was reading. "
                                " Engel eventually notices that you were there, and he spoke to you in a hushed tone. "
                                e " Oh, hello there, [name]... "
                                e " I'm just reading a book about birds, is all. "
                                e " I find birds to be quite interesting... Did you know? The Sword-billed Hummingbird is the only bird with a bill longer than its body. "
                                hide engelneutral at bottom
                                show engelhappy at center
                                e " Well, it isn't called the Sword-billed hummingbird for nothing, am I right? "
                                hide engelhappy at bottom
                                show engelneutral at center
                                e " I wonder how it would be like to live as a bird like that, having bill longer than its own body... "
                                e " Anywho, what're you doing here, [name]? wanted some peace and quiet? "
                                e " Me too. It's honestly nice without people screaming in here... "
                                hide engelneutral at bottom
                                show engelangry at center
                                e " The only problem is if Oliver and his gang come in here. "
                                e " They're quite..the nuisance. "
                                hide engelangry at bottom
                                show engelneutral at center
                                e " But, it's lucky that they don't come in here as often. "
                                e " They've only ever came here five times, just to mess with the books. "
                                e " It's probably because they find the library boring, and they can't do anything worse due to the librarian being...a bit strict. "
                                e " They've only messed with the book titles before, so it isn't that bad. "
                                e " Infact, I saw them come in here a while ago to mess with another book. "
                                e " It's really idiotic, in all honesty... "
                                e " Anywho...since you're here... would you like to read with me? "
                                menu:
                                    " Sure ":
                                        hide engelneutral at bottom
                                        show engelhappy at center
                                        e " Very well, then.. "
                                        if mean == True and clairebeatup == True:
                                            hide engelhappy at bottom
                                            show engelneutral at center
                                            e " Though, before we do start reading, I'd like to ask.. "
                                            e " If it doesn't bother you...could you tell me what happened with you and Claire...? "
                                            if claengbub == True:
                                                e " She was...looking upset earlier in class. "
                                            else:
                                                e " She talked about you, and she looked upset... "
                                            e " You don't have to if you don't want to. "
                                            menu:
                                                " He doesn't need to know. ":
                                                    e " If you say so, then... "
                                                    scene black with dissolve
                                                    " You and Engel read a book about bird facts for the rest of the break. "
                                                    " It was pretty fun, actually. You saw a whole lot of cute birds in the photos. "
                                                    play sound "audio/bellring.mp3"
                                                    " The bell rings eventually, you and Engel then got off of your seats, returned the book and went to the next class: Language. "
                                                    pause 2.0
                                                    jump languageclass1
                                        elif mean == True and clairebeatup == False:
                                            hide engelhappy at bottom
                                            show engelneutral at center
                                            e " Though, before we do start reading, I'd like to ask.. "
                                            e " If it doesn't bother you...could you tell me what happened with you and Claire...? "
                                            if claengbub == True:
                                                e " She was...looking upset earlier in class. "
                                            else:
                                                e " She talked about you, and she looked upset... "
                                            e " You don't have to if you don't want to. "
                                            menu:
                                                " He doesn't need to know. ":
                                                    e " If you say so, then... "
                                                    scene black with dissolve
                                                    " You and Engel read a book about bird facts for the rest of the break. "
                                                    " It was pretty fun, actually. You saw a whole lot of cute birds in the photos. "
                                                    play sound "audio/bellring.mp3"
                                                    " The bell rings eventually, you and Engel then got off of your seats, returned the book and went to the next class: Language. "
                                                    pause 2.0
                                                    jump languageclass1
                                        else:
                                            scene black with dissolve
                                            " You and Engel read a book about bird facts for the rest of the break. "
                                            " It was pretty fun, actually. You saw a whole lot of cute birds in the photos. "
                                            play sound "audio/bellring.mp3"
                                            " The bell rings eventually, you and Engel then got off of your seats, returned the book and went to the next class: Language. "
                                            pause 2.0
                                            jump languageclass1
                            " I don't want to disturb him ":
                                " You decide not to disturb Engel from his reading. "
                                " You took a walk in the library trying to find something interesting to read... "
                                play sound "audio/bellring.mp3"
                                " Until the bell rings. You then went out of the library to go to your next class: Language. "
                                scene black with dissolve
                                pause 2.0
                                jump languageclass1
                    else:
                        " After a bit of walking, you spot a white-haired boy reading a book, all alone. "
                        " Should you sit next to him to see what he's reading? or do you leave him alone? "
                        menu:
                            " Sit next to him ":
                                $ engelknow = True
                                show engelneutral at center with easeinright
                                " You walk over and you sat next to Engel, looking at what he was reading. "
                                " he eventually notices that you were there, and he spoke to you in a hushed tone. "
                                x " Oh, hello there, [name]... "
                                e " I believe we haven't met before, so... My name's Engel. It's a pleasure to meet you."
                                e " I'm just reading a book about birds. "
                                e " I find birds to be quite interesting... Did you know? The Sword-billed Hummingbird is the only bird with a bill longer than its body. "
                                hide engelneutral at bottom
                                show engelhappy at center
                                e " Well, it isn't called the Sword-billed hummingbird for nothing, am I right? "
                                hide engelhappy at bottom
                                show engelneutral at center
                                e " I wonder how it would be like to live as a bird like that, having bill longer than its own body... "
                                e " Anywho, what're you doing here, [name]? wanted some peace and quiet? "
                                e " Me too. It's honestly nice without people screaming in here... "
                                hide engelneutral at bottom
                                show engelangry at center
                                e " The only problem is if Oliver and his gang come in here. "
                                e " They're quite..the nuisance. "
                                hide engelangry at bottom
                                show engelneutral at center
                                e " But, it's lucky that they don't come in here as often. "
                                e " They've only ever came here five times, just to mess with the books. "
                                e " It's probably because they find the library boring, and they can't do anything worse due to the librarian being...a bit strict. "
                                e " They've only messed with the book titles before, so it isn't that bad. "
                                e " Infact, I saw them come in here a while ago to mess with another book. "
                                e " It's really idiotic, in all honesty... "
                                e " Anywho...since you're here... would you like to read with me? "
                                menu:
                                    " Sure ":
                                        hide engelneutral at bottom
                                        show engelhappy at center
                                        e " Very well, then.. "
                                        if mean == True and clairebeatup == True:
                                            hide engelhappy at bottom
                                            show engelneutral at center
                                            e " Though, before we do start reading, I'd like to ask.. "
                                            e " If it doesn't bother you...could you tell me what happened with you and Claire...? "
                                            if claengbub == True:
                                                e " She was...looking upset earlier in class. "
                                            else:
                                                e " She talked about you, and she looked upset... "
                                            e " You don't have to if you don't want to. "
                                            menu:
                                                " He doesn't need to know. ":
                                                    e " If you say so, then... "
                                                    scene black with dissolve
                                                    " You and Engel read a book about bird facts for the rest of the break. "
                                                    " It was pretty fun, actually. You saw a whole lot of cute birds in the photos. "
                                                    play sound "audio/bellring.mp3"
                                                    " The bell rings eventually, you and Engel then got off of your seats, returned the book and went to the next class: Language. "
                                                    pause 2.0
                                                    jump languageclass1
                                        elif mean == True and clairebeatup == False:
                                            hide engelhappy at bottom
                                            show engelneutral at center
                                            e " Though, before we do start reading, I'd like to ask.. "
                                            e " If it doesn't bother you...could you tell me what happened with you and Claire...? "
                                            if claengbub == True:
                                                e " She was...looking upset earlier in class. "
                                            else:
                                                e " She talked about you, and she looked upset... "
                                            e " You don't have to if you don't want to. "
                                            menu:
                                                " He doesn't need to know. ":
                                                    e " If you say so, then... "
                                                    scene black with dissolve
                                                    " You and Engel read a book about bird facts for the rest of the break. "
                                                    " It was pretty fun, actually. You saw a whole lot of cute birds in the photos. "
                                                    play sound "audio/bellring.mp3"
                                                    " The bell rings eventually, you and Engel then got off of your seats, returned the book and went to the next class: Language. "
                                                    pause 2.0
                                                    jump languageclass1
                                        else:
                                            scene black with dissolve
                                            " You and Engel read a book about bird facts for the rest of the break. "
                                            " It was pretty fun, actually. You saw a whole lot of cute birds in the photos. "
                                            play sound "audio/bellring.mp3"
                                            " The bell rings eventually, you and Engel then got off of your seats, returned the book and went to the next class: Language. "
                                            pause 2.0
                                            jump languageclass1
                            " I don't want to disturb him ":
                                " You decide not to disturb the boy from his reading. "
                                " You took a walk in the library trying to find something interesting to read... "
                                play sound "audio/bellring.mp3"
                                " Until the bell rings. You then went out of the library to go to your next class: Language. "
                                scene black with dissolve
                                pause 2.0
                                jump languageclass1
                label rooftop1:
                    scene rooftop with dissolve
                    " After a bit of walking on the stairs, you manage to finally get up to the rooftop. "
                    " The air feels nice up here... You decide to sit near a wall and watch the sky for a bit. "
                    " You then notice someone next to you... "
                    " Well, not really someone. Two people, actually. "
                    if lanaknow == True and abbieknow == True:
                        " It was Lana and Abbie. Seems like they're busy talking and making something... "
                        " Would you like to join them? "
                        menu:
                            " Move over to them ":
                                show lananeutral at left with easeinright
                                show abbieneutral at right with easeinright
                                " You move closer to them and they're drawing little characters based off of themselves. "
                                " How cute! "
                                " You tap Lana's shoulder to get hers and Abbie's attention. "
                                hide lananeutral at bottom
                                show lanahappy at left
                                l " Oh, hey there [name]! "
                                hide lanahappy at bottom
                                show lananeutral at left
                                a " Hi, [name]... "
                                l " We're just making some cool ocs for a game we really like! "
                                a " It's kinda cringe, I know... "
                                l " Nah, it isn't really cringe! People make ocs for a game they like all the time! "
                                l " It's normal! Sure, some people may find it weird but atleast it's not the whole world shaming you for it! "
                                l " Just... as long as your oc isn't too problematic then it's fine. "
                                l " Anywho! [name]! Would you like to make some ocs with us? It's okay if you just wanna watch! "
                                menu:
                                    " Make ocs with them ":
                                        l " Alrighty then! We're making ocs for this one game where you basically team up with other people, "
                                        l " And you basically have to avoid these things called 'twisteds' because they'll kill you! "
                                        l " There's like, a lot of characters in the game! "
                                        hide abbieneutral at bottom
                                        show abbiehappy at right
                                        a " ...My favorite is Aster... "
                                        hide lananeutral at bottom
                                        show lanahappy at left
                                        l " And I really like Shelly! "
                                        hide lanahappy at bottom
                                        show lananeutral at left
                                        l " My oc is gonna be based off of a sock puppet! "
                                        a " I don't really know for mine... Maybe an apple? "
                                        l " Sure, If you want it to be one! "
                                        a " What about yours, [name]? "
                                        menu:
                                            " A school book ":
                                                l " Ooh! I think they'd be great friends with Britney! "
                                                l " Britney's this really smart lamp that likes books! "
                                                scene black with dissolve
                                                " You spent the rest of your break designing OC's with Lana and Abbie... "
                                                " Maybe you should try out this game they were talking about later. "
                                                " It actually sounds quite interesting... What's it called? "
                                                " Andy's World? Maybe, that's what it was. "
                                                " You'll check it out later when you get home. "
                                                play sound "audio/bellring.mp3"
                                                " Whilst you were making oc's with Abbie and Lana, the bell rings. "
                                                " You all got up and went to the next class: Language. "
                                                pause 2.0
                                                jump languageclass1
                                            " A pencil ":
                                                l " Interesting! They sound pretty cool! "
                                                l " I have a feeling that this character called 'Shrimpy' would try to break their head off, though... "
                                                l " That's how he is! He's a bully! "
                                                scene black with dissolve
                                                " You spent the rest of your break designing OC's with Lana and Abbie... "
                                                " Maybe you should try out this game they were talking about later. "
                                                " It actually sounds quite interesting... What's it called? "
                                                " Andy's World? Maybe, that's what it was. "
                                                " You'll check it out later when you get home. "
                                                play sound "audio/bellring.mp3"
                                                " Whilst you were making oc's with Abbie and Lana, the bell rings. "
                                                " You all got up and went to the next class: Language. "
                                                pause 2.0
                                                jump languageclass1
                                            " I don't know ":
                                                l " Oooh, that's alright! "
                                                l " To me, I think you're...I don't know... "
                                                l " A dual-sided pendant, maybe? "
                                                l " Like, one side is ornate and polished - but the other one is rough and tarnished! "
                                                l " Oooh, and what if there's like a photo inside that changes depending on who opens it? "
                                                " ...Why did that somehow describe how you are. "
                                                scene black with dissolve
                                                " You spent the rest of your break designing OC's with Lana and Abbie... "
                                                " Maybe you should try out this game they were talking about later. "
                                                " It actually sounds quite interesting... What's it called? "
                                                " Andy's World? Maybe, that's what it was. "
                                                " You'll check it out later when you get home. "
                                                play sound "audio/bellring.mp3"
                                                " Whilst you were making ocs with Abbie and Lana, the bell rings. "
                                                " You all got up and went to the next class: Language. "
                                                pause 2.0
                                                jump languageclass1
                                    " I'll watch ":
                                        l " Alrighty! We're making ocs for this one game called 'Andy's world', by the way! "
                                        l " It's really cool, you should try it out sometime! "
                                        scene black with dissolve
                                        " You spent the rest of your break watching Abbie and Lana make ocs... "
                                        " Maybe you should try out this game they were talking about later. "
                                        " It actually sounds quite interesting... What's it called? "
                                        " Andy's World? Maybe, that's what it was. "
                                        " You'll check it out later when you get home. "
                                        play sound "audio/bellring.mp3"
                                        " Whilst you were watching Abbie and Lana make ocs, the bell rings. "
                                        " You all got up and went to the next class: Language. "
                                        pause 2.0
                                        jump languageclass1
                            " Nah, I'd rather not disturb them. ":
                                " You decided not to disturb them and you stayed where you are. "
                                " You spent your time watching the clouds pass by, sometimes even looking at your phone. "
                                " Nothing really interesting happened, but atleast you got some peace...and somewhat alone time. "
                                play sound "audio/bellring.mp3"
                                " After taking a few breathers, the bell eventually rang and you got up. "
                                " You dusted yourself off since you basically sat on the ground and then you went to your next class: Language. "
                                scene black with dissolve
                                pause 2.0
                                jump languageclass1
                    else:
                        " You spot a girl and a black haired boy. Seems like they're busy talking and making something... "
                        " Would you like to join them? "
                        menu:
                            " Move over to them ":
                                $ lanaknow = True
                                $ abbieknow = True
                                show lananeutral at left with easeinright
                                show abbieneutral at right with easeinright
                                " You move closer to them and they're drawing little characters based off of themselves. "
                                " How cute! "
                                " You tap the girl's shoulder to get hers and Abbie's attention. "
                                hide lananeutral at bottom
                                show lanahappy at left
                                x " Oh, hey there [name]! "
                                hide lanahappy at bottom
                                show lananeutral at left
                                x " Hi, [name]... "
                                x " I don't think I got to introduce myself before to you, so... "
                                l " I'm Lana! This is my friend, Abbie! "
                                l " We were just making some cool ocs for a game we really like! "
                                a " It's kinda cringe, I know... "
                                l " Nah, it isn't really cringe! People make ocs for a game they like all the time! "
                                l " It's normal! Sure, some people may find it weird but atleast it's not the whole world shaming you for it! "
                                l " Just... as long as your oc isn't too problematic then it's fine. "
                                l " Anywho! [name]! Would you like to make some ocs with us? It's okay if you just wanna watch! "
                                menu:
                                    " Make ocs with them ":
                                        l " Alrighty then! We're making ocs for this one game where you basically team up with other people, "
                                        l " And you basically have to avoid these things called 'twisteds' because they'll kill you! "
                                        l " There's like, a lot of characters in the game! "
                                        hide abbieneutral at bottom
                                        show abbiehappy at right
                                        a " ...My favorite is Aster... "
                                        hide lananeutral at bottom
                                        show lanahappy at left
                                        l " And I really like Shelly! "
                                        hide lanahappy at bottom
                                        show lananeutral at center
                                        l " My oc is gonna be based off of a sock puppet! "
                                        a " I don't really know for mine... Maybe an apple? "
                                        l " Sure, If you want it to be one! "
                                        a " What about yours, [name]? "
                                        menu:
                                            " A school book ":
                                                l " Ooh! I think they'd be great friends with Britney! "
                                                l " Britney's this really smart lamp that likes books! "
                                                scene black with dissolve
                                                " You spent the rest of your break designing OC's with Lana and Abbie... "
                                                " Maybe you should try out this game they were talking about later. "
                                                " It actually sounds quite interesting... What's it called? "
                                                " Andy's World? Maybe, that's what it was. "
                                                " You'll check it out later when you get home. "
                                                play sound "audio/bellring.mp3"
                                                " Whilst you were making oc's with Abbie and Lana, the bell rings. "
                                                " You all got up and went to the next class: Language. "
                                                pause 2.0
                                                jump languageclass1
                                            " A pencil ":
                                                l " Interesting! They sound pretty cool! "
                                                l " I have a feeling that this character called 'Shrimpy' would try to break their head off, though... "
                                                l " That's how he is! He's a bully! "
                                                scene black with dissolve
                                                " You spent the rest of your break designing OC's with Lana and Abbie... "
                                                " Maybe you should try out this game they were talking about later. "
                                                " It actually sounds quite interesting... What's it called? "
                                                " Andy's World? Maybe, that's what it was. "
                                                " You'll check it out later when you get home. "
                                                play sound "audio/bellring.mp3"
                                                " Whilst you were making oc's with Abbie and Lana, the bell rings. "
                                                " You all got up and went to the next class: Language. "
                                                pause 2.0
                                                jump languageclass1
                                            " I don't know ":
                                                l " Oooh, that's alright! "
                                                l " To me, I think you're...I don't know... "
                                                l " A dual-sided pendant, maybe? "
                                                l " Like, one side is ornate and polished - but the other one is rough and tarnished! "
                                                l " Oooh, and what if there's like a photo inside that changes depending on who opens it? "
                                                " ...Why did that somehow describe how you are. "
                                                scene black with dissolve
                                                " You spent the rest of your break designing OC's with Lana and Abbie... "
                                                " Maybe you should try out this game they were talking about later. "
                                                " It actually sounds quite interesting... What's it called? "
                                                " Andy's World? Maybe, that's what it was. "
                                                " You'll check it out later when you get home. "
                                                play sound "audio/bellring.mp3"
                                                " Whilst you were making ocs with Abbie and Lana, the bell rings. "
                                                " You all got up and went to the next class: Language. "
                                                pause 2.0
                                                jump languageclass1
                                    " I'll watch ":
                                        l " Alrighty! We're making ocs for this one game called 'Andy's world', by the way! "
                                        l " It's really cool, you should try it out sometime! "
                                        scene black with dissolve
                                        " You spent the rest of your break watching Abbie and Lana make ocs... "
                                        " Maybe you should try out this game they were talking about later. "
                                        " It actually sounds quite interesting... What's it called? "
                                        " Andy's World? Maybe, that's what it was. "
                                        " You'll check it out later when you get home. "
                                        play sound "audio/bellring.mp3"
                                        " Whilst you were watching Abbie and Lana make ocs, the bell rings. "
                                        " You all got up and went to the next class: Language. "
                                        pause 2.0
                                        jump languageclass1
                            " Nah, I'd rather not disturb them. ":
                                " You decided not to disturb them and you stayed where you are. "
                                " You spent your time watching the clouds pass by, sometimes even looking at your phone. "
                                " Nothing really interesting happened, but atleast you got some peace...and somewhat alone time. "
                                play sound "audio/bellring.mp3"
                                " After taking a few breathers, the bell eventually rang and you got up. "
                                " You dusted yourself off since you basically sat on the ground and then you went to your next class: Language. "
                                scene black with dissolve
                                pause 2.0
                                jump languageclass1
                label languageclass1:
                    scene classroom with dissolve
                    show msthravelneutral at center with dissolve
                    mst " Good morning, students! Let's get started with the lesson! "
                    hide msthravelneutral at left with easeoutleft
                    " The class is pretty boring. I mean, it's just language class. "
                    " What should you do to pass the time? "
                    menu:
                        " Draw something ":
                            " You grabbed a piece of paper from your bag, and you started to draw. "
                            " You didn't really know what you were drawing, you just knew that you were drawing {i}something{/i}. "
                            " You decided to draw yourself next to the little silly goober you just made. "
                            " ...Yeah, this looks horrible. Horrible in a good way. "
                            " Maybe you should make more silly goobers. "
                            " But you should probably stop before the teacher notices that you aren't paying attention. "
                            " You went back to taking your notes about the lesson. "
                            jump oliganglanguage
                        " Think about your life choices ":
                            " You decided to think about and regret your life choices whilst in class. "
                            " It honestly helped since it tuned out some of the teacher's yapping, but then you're gonna have to deal with the consequences if she does a quiz. "
                            " Why are you in here again? Just to suffer? Yes. "
                            " What was the purpose of trying to get friends in this school? Idk ask the creator about that "
                            " The only thing that's keeping you from backflipping off of the school's rooftop is the fact that the game won't even let you do that. "
                            " You're gonna have to endure this pain for a bit. "
                            " Whether you like it or not. "
                            jump oliganglanguage
                        " Actually pay attention to class ":
                            " Are you seriously gonna pay attention to class? "
                            " Alright, nerd. "
                            " It wasn't anything important, really. "
                            " There were a few times you've zoned out a bit in the middle of the teacher speaking, but only for a short bit. "
                            jump oliganglanguage
                    label oliganglanguage:
                        play sound "audio/bellring.mp3"
                        " The bell rang, and it was time for another break. "
                        " You were about to get up from your seat, but you felt something hit the back of your head. "
                        " You turned around and looked down to see that it was a paper aeroplane. "
                        " You picked it up and unraveled it and saw a message written on it. It read: "
                        if kind == True:
                            " 'lol u stink'- Edward "
                            " ...Was that really the best insult they could come up with? "
                            " You turned it into a paper ball and you threw it into the trash before you went out into the hallways. "
                        elif mean == True and clairebeatup == True:
                            " 'u suck for apologizing to claire lol' - Oliver "
                            " What. "
                            " You're not happy with this. "
                            " Once you find this Oliver guy, you'll go ahead and teach him a lesson. "
                            " ...If you can. "
                            " You then walk out into the hallways. "
                        elif mean == True and clairebeatup == False:
                            " 'ur such a wimp lmaoooo' - Oliver"
                            " What. "
                            " You're not happy with this. "
                            " Once you find this guy, you'll go ahead and teach him a lesson. "
                            " ...If you can. "
                            " You then walk out into the hallways. "
                        elif calm == True:
                            " 'if u continue to b so chill why dont i make you even chiller by shoving icecubes up ur butt ' - zip "
                            " ...Well that's interesting. "
                            " You didn't really let that message get to you, though. "
                            " You're just a chill guy, after all. "
                            " You decide to put the aeroplane in the trash before you went out to the hallways. "
                        scene black with dissolve
                        pause 2.0
                        jump abbiebully
label abbiebully:
    scene hallway with dissolve
    " When you walked out of the classroom, you saw three people surrounding someone... "
    " What's going on over there? "
    show zipneutral at left with easeinright
    show oliverbully at center with easeinright
    show edwardbully at right with easeinright
    x " Heh, aww, are you gonna cry? "
    " The taller out of the three was choking the poor boy, whilst the other two seemed to be holding the remains of the boy's notebook."
    if abbieknow == True:
        " Wait... "
        " That's {b}Abbie{/b} they're choking. "
        menu:
            " Step in ":
                " You decided to walk up behind them, you weren't just gonna stand there and do nothing. "
                " What should you do? "
                menu:
                    " Talk to them politely ":
                        " You clear your throat to get their attention. "
                        hide oliverbully at bottom
                        show oliverneutral at center
                        hide edwardbully at bottom
                        show edwardneutral at right
                        " They decided to let Abbie down for a bit as they put all their attention to you. "
                        " You then start giving them a lecture on how they shouldn't be doing stuff like this. "
                        " And how it's wrong to bully someone, but one of them just laughs right at your face. "
                        hide oliverneutral at bottom
                        show oliverhappy at center
                        x " You think some simple words are gonna change our minds? "
                        x " Please, you'd bully this little FREAK too if you know what he's been doing! "
                        if mean == True:
                            " ...You're seriously holding yourself back from punching this bitch right now. "
                            " Should you beat him up or not? "
                            menu:
                                " Beat him up. (At the cost of being sent to the principal.) ":
                                    $ abbiemeandefend = True
                                    $ abbielv += 5
                                    stop music fadeout 0.5
                                    " Alright. "
                                    hide zipneutral at bottom
                                    show zipconfused at left
                                    hide edwardneutral at bottom
                                    show edwardconfused at right
                                    " Time to teach this tough guy a lesson. "
                                    play sound "audio/worry.mp3" fadein 0.5
                                    hide zipconfused at left with easeoutleft
                                    hide edwardconfused at right with easeoutright
                                    " You warm up your arms for a bit before you start beating the absolute shit out of him. "
                                    hide oliverhappy at bottom
                                    show olivershit at center
                                    " You then grabbed his hand and threw him right at a locker. Hard. "
                                    o " OW, SHIT! " with vpunch
                                    " You slammed him down to the ground and proceeded to beat him up and punch him multiple times.  " with vpunch
                                    hide olivershit at bottom with easeoutbottom
                                    stop music
                                    play sound "audio/concern.mp3"
                                    o " FUCK, MY EYE! " with vpunch
                                    o " STOP! STOP IT! " with vpunch
                                    " Oh, look who's telling me to stop now. " with vpunch
                                    " You didn't stop when you were strangling Abbie, so why should I? " with vpunch
                                    " Messing with someone as {sc}fragile him is a low blow. You should've understood that.{/sc} " with vpunch
                                    " {sc}But no, you're too much of an idiot to understand that{/sc} because you thought it was fun. " with vpunch
                                    " {sc}You've been playing with someones life, you could've murdered them.{/sc} " with vpunch
                                    " {sc}All for your entertainment? How cruel of you.{/sc} " with vpunch
                                    " I should let you go ahead and rot in hell, like where the rest of your family belongs.{nw}" with vpunch
                                    stop music
                                    " WHAT IS GOING ON HERE?! " with vpunch
                                    " That was a teacher. You slowly get off of the now beaten up boy. "
                                    " A lot of students were looking at you. "
                                    " Atleast they know not to fuck with you now. "
                                    scene black with dissolve
                                    " You and Oliver were called to the principal's office. "
                                    pause 2.0
                                    jump principalsoffice
                                " Insult him ":
                                    $ abbielv += 5
                                    " You were about to insult him, but then a teacher came by and saw what happened. "
                                    hide edwardconfused at right with easeoutright
                                    hide oliverhappy at right with easeoutright
                                    hide zipconfused at right with easeoutright
                                    " Thankfully, any more drama that was gonna happen was cut off as the teacher brought the trio away and scolded them somewhere else. "
                                    show abbiesad at center with easeinbottom
                                    " You helped Abbie up from the ground and asked if he was alright. "
                                    a " *sniff*... I'm fine... "
                                    a " Thank you for...for coming in to help me, though.. "
                                    a " I appreciate it... "
                                    a " But, you didn't have to do all that for me... "
                                    scene black with dissolve
                                    " You spent the rest of the break with Abbie, making sure no one hurts him. "
                                    " You wouldn't want anything bad happening to him ever again. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rang soon enough, and you both went to class. "
                                    " Science class, to be specific. "
                                    pause 2.0
                                    jump scienceclass1
                        else:
                            " You were about to say something else, but then a teacher came by. "
                            hide edwardconfused at right with easeoutright
                            hide oliverhappy at right with easeoutright
                            hide zipconfused at right with easeoutright
                            " Thankfully, any more drama that was gonna happen was cut off as the teacher brought the trio away and scolded them somewhere else. "
                            show abbiesad at center with easeinbottom
                            " You helped Abbie up from the ground and asked if he was alright. "
                            a " *sniff*... I'm fine... "
                            a " Thank you for...for coming in to help me, though.. "
                            a " I appreciate it... "
                            a " But, you didn't have to do all that for me... "
                            scene black with dissolve
                            " You spent the rest of the break with Abbie, making sure no one hurts him. "
                            " You wouldn't want anything bad happening to him ever again. "
                            play sound "audio/bellring.mp3"
                            " The bell rang soon enough, and you both went to class. "
                            " Science class, to be specific. "
                            pause 2.0
                            jump scienceclass1
                    " Kick the taller one down ":
                        hide oliverbully at bottom
                        show olivershit at center
                        hide edwardbully at bottom
                        show edwardconfused at right
                        hide zipneutral at bottom
                        show zipconfused at left
                        " You decided to kick the taller guy in the center down. "
                        " When he didn't fall, you kicked him harder, causing him to fall down to the ground and letting go of Abbie. "
                        hide olivershit at bottom with easeoutbottom
                        " ...Causing Abbie to fall aswell. "
                        x " Hey, what the hell - ?! "
                        " You got Abbie's hand and you ran away from them, turning multiple corners until you were certain that they couldn't find you two. "
                        show abbiesad at center with appearright
                        a " *sniff*... "
                        " You sit Abbie down somewhere and ask if he's alright. "
                        a " I'm..I'm fine... "
                        a " Thank you for coming in to help, though... "
                        a " ... "
                        a " I feel...so weak... "
                        a " I can't even defend myself...from bullies... "
                        a " My grades are low... I'm so...pathetic... "
                        a " They were right...I-i'm just some...lame loser... "
                        a " I don't fit in here at all... "
                        menu:
                            " Comfort him. ":
                                $ abbielv += 5
                                hide abbiesad at bottom
                                show abbieneutral at center
                                " You comfort him until he felt better. "
                                a " ...Thanks again, [name]... "
                                a " You can go back to...doing what you wanted now... "
                                a " I don't want to be a bother to you... "
                                a " Byebye... "
                                hide abbieneutral at right with easeoutright
                                " You then get up after Abbie left, and decided to go somewhere since you still had some time before class starts. "
                                " Where do you go? "
                                menu:
                                    " {image=bubbleicon} Front of the school {image=bubbleicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump frontschool2
                                    " {image=skellicon} Back of the school {image=skellicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump backschool2
                                    " {image=popularicon} The gym {image=popularicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump gym2
                                    " The cafeteria ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump cafe2
                                    " {image=rubyicon} The rooftop {image=rubyicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump rooftop2
                                    " {image=claireicon} The library {image=claireicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump library2
                    " Get a teacher on them ":
                        " You quickly spot a nearby teacher and told them what was going on. "
                        " They come with you and they dragged the trio away, scolding them somewhere else. "
                        " Meanwhile, you help Abbie up from the ground due to the one that was choking him let go of him. "
                        show abbiesad at center with easeinbottom
                        a " *sniff*... "
                        " You sit Abbie down somewhere and ask if he's alright. "
                        a " I'm..I'm fine... "
                        a " Thank you for coming in to help, though... "
                        a " ... "
                        a " I feel...so weak... "
                        a " I can't even defend myself...from bullies... "
                        a " My grades are low... I'm so...pathetic... "
                        a " They were right...I-i'm just some...lame loser... "
                        a " I don't fit in here at all... "
                        menu:
                            " Comfort him. ":
                                $ abbielv += 5
                                hide abbiesad at bottom
                                show abbieneutral at center
                                " You comfort him until he felt better. "
                                a " ...Thanks again, [name]... "
                                a " You can go back to...doing what you wanted now... "
                                a " I don't want to be a bother to you... "
                                a " Byebye... "
                                hide abbieneutral at right with easeoutright
                                " You then get up after Abbie left, and decided to go somewhere since you still had some time before class starts. "
                                " Where do you go? "
                                menu:
                                    " {image=bubbleicon} Front of the school {image=bubbleicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump frontschool2
                                    " {image=skellicon} Back of the school {image=skellicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump backschool2
                                    " {image=popularicon} The gym {image=popularicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump gym2
                                    " The cafeteria ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump cafe2
                                    " {image=rubyicon} The rooftop {image=rubyicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump rooftop2
                                    " {image=claireicon} The library {image=claireicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump library2
            " Let someone else help ":
                hide edwardbully at right with easeoutright
                hide oliverbully at right with easeoutright
                hide zipneutral at right with easeoutright
                " You just stood there and eventually a teacher managed to stop everything from getting worse. "
                " You could've done something, but your body chose not to. "
                " You'll have to spend your time wandering around the school whilst worrying for Abbie and seeing if he's gonna be okay. "
                " To take the scene of what just happened off of your mind, where should you go? "
                menu:
                    " {image=bubbleicon} Front of the school {image=bubbleicon} ":
                        scene black with dissolve
                        pause 2.0
                        jump frontschool2
                    " {image=skellicon} Back of the school {image=skellicon} ":
                        scene black with dissolve
                        pause 2.0
                        jump backschool2
                    " {image=popularicon} The gym {image=popularicon} ":
                        scene black with dissolve
                        pause 2.0
                        jump gym2
                    " The cafeteria ":
                        scene black with dissolve
                        pause 2.0
                        jump cafe2
                    " {image=rubyicon} The rooftop {image=rubyicon} ":
                        scene black with dissolve
                        pause 2.0
                        jump rooftop2
                    " {image=claireicon} The library {image=claireicon} ":
                        scene black with dissolve
                        pause 2.0
                        jump library2
    else:
        " It seems as though they were choking a boy with black hair, and a leaf on his head... "
        menu:
            " Step in ":
                " You decided to walk up behind them, you weren't just gonna stand there and do nothing. "
                " What should you do? "
                menu:
                    " Talk to them politely ":
                        " You clear your throat to get their attention. "
                        hide oliverbully at bottom
                        show oliverneutral at center
                        hide edwardbully at bottom
                        show edwardneutral at right
                        " They decided to let the boy down for a bit as they put all their attention to you. "
                        " You then start giving them a lecture on how they shouldn't be doing stuff like this. "
                        " And how it's wrong to bully someone, but one of them just laughs right at your face. "
                        hide oliverneutral at bottom
                        show oliverhappy at center
                        x " You think some simple words are gonna change our minds? "
                        x " Please, you'd bully this little FREAK too if you know what he's been doing! "
                        if mean == True:
                            " ...You're seriously holding yourself back from punching this bitch right now. "
                            " Should you beat him up or not? "
                            menu:
                                " Beat him up. (At the cost of being sent to the principal.) ":
                                    $ abbiemeandefend = True
                                    $ abbielv += 5
                                    stop music
                                    " Alright. "
                                    hide zipneutral at bottom
                                    show zipconfused at left
                                    hide edwardneutral at bottom
                                    show edwardconfused at right
                                    " Time to teach this tough guy a lesson. "
                                    hide zipconfused at left with easeoutleft
                                    hide edwardconfused at right with easeoutright
                                    play music "audio/worry.mp3" fadein 0.5
                                    " You warm up your arms for a bit before you start beating the absolute shit out of him. "
                                    show olivershit at center
                                    " You then grabbed his hand and threw him right at a locker. "
                                    hide oliverhappy at bottom
                                    o " OW, SHIT! "
                                    " You slammed him down to the ground and proceeded to beat him up and punch him multiple times.  " with vpunch
                                    hide olivershit at bottom with easeoutbottom
                                    stop music
                                    play music "audio/concern.mp3"
                                    o " FUCK, MY EYE! " with vpunch
                                    o " STOP! STOP IT! " with vpunch
                                    " Oh, look who's telling me to stop now. " with vpunch
                                    " You didn't stop when you were strangling this poor boy, so why should I? " with vpunch
                                    " Messing with someone as {sc}fragile him is a low blow. You should've understood that.{/sc} " with vpunch
                                    " {sc}But no, you're too much of an idiot to understand that because you thought it was fun.{/sc} " with vpunch
                                    " {sc}You've been playing with someones life, you could've murdered them.{/sc} " with vpunch
                                    " {sc}All for your entertainment? How cruel of you.{/sc} " with vpunch
                                    " {sc}I should let you go ahead and rot in hell, like where the rest of your family belongs.{/sc}{nw}" with vpunch
                                    stop music
                                    " WHAT IS GOING ON HERE?! " with vpunch
                                    " That was a teacher. You slowly get off of the now beaten up boy. "
                                    " A lot of students were looking at you. "
                                    " Atleast they know not to fuck with you now. "
                                    scene black with dissolve
                                    " You and Oliver were called to the principal's office. "
                                    pause 2.0
                                    jump principalsoffice
                                " Insult him ":
                                    $ abbielv += 5
                                    " You were about to insult him, but then a teacher came by and saw what happened. "
                                    $ abbieknow = True
                                    " Thankfully, any more drama that was gonna happen was cut off as the teacher brought the trio away and scolded them somewhere else. "
                                    hide edwardconfused at right with easeoutright
                                    hide oliverhappy at right with easeoutright
                                    hide zipconfused at right with easeoutright
                                    show abbiesad at center with easeinbottom
                                    " You helped the boy up from the ground and asked if he was alright. "
                                    x " *sniff*... I'm fine... "
                                    x " Thank you for...for coming in to help me, though.. "
                                    x " I appreciate it... "
                                    x " But, you didn't have to do all that for me... "
                                    a " I'm Abbie, by the way... "
                                    a " It's, um... Nice to meet you... "
                                    scene black with dissolve
                                    " You spent the rest of the break with Abbie, making sure no one hurts him. "
                                    " You wouldn't want anything bad happening to him ever again. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rang soon enough, and you both went to class. "
                                    " Science class, to be specific. "
                                    pause 2.0
                                    jump scienceclass1
                        else:
                            $ abbieknow = True
                            " You were about to say something else, but then a teacher came by. "
                            " Thankfully, any more drama that was gonna happen was cut off as the teacher brought the trio away and scolded them somewhere else. "
                            hide edwardneutral at right with easeoutright
                            hide oliverhappy at right with easeoutright
                            hide zipneutral at right with easeoutright
                            show abbiesad at center with easeinbottom
                            " You helped the boy up from the ground and asked if he was alright. "
                            x " *sniff*... I'm fine... "
                            x " Thank you for...for coming in to help me, though.. "
                            x " I appreciate it... "
                            x " But, you didn't have to do all that for me... "
                            a " I'm Abbie, by the way... "
                            a " It's, um... Nice to meet you... "
                            scene black with dissolve
                            " You spent the rest of the break with Abbie, making sure no one hurts him. "
                            " You wouldn't want anything bad happening to him ever again. "
                            play sound "audio/bellring.mp3"
                            " The bell rang soon enough, and you both went to class. "
                            " Science class, to be specific. "
                            pause 2.0
                            jump scienceclass1
                    " Kick the taller one down ":
                        $ abbieknow = True
                        hide oliverbully at bottom
                        show olivershit at center
                        hide edwardbully at bottom
                        show edwardconfused at right
                        hide zipneutral at bottom
                        show zipconfused at left
                        " You decided to kick the taller guy in the center down. "
                        " When he didn't fall, you kicked him harder, causing him to fall down to the ground and letting go of Abbie. "
                        hide olivershit at bottom with easeoutbottom
                        " ...Causing the boy to fall aswell. "
                        x " Hey, what the hell - ?! "
                        " You got Abbie's hand and you ran away from them, turning multiple corners until you were certain that they couldn't find you two. "
                        show abbiesad at center with easeinleft
                        x " *sniff*... "
                        " You sit the boy down somewhere and ask if he's alright. "
                        x " I'm..I'm fine... "
                        x " Thank you for coming in to help, though... "
                        a " I'm...Abbie... "
                        a " ... "
                        a " I feel...so weak... "
                        a " I can't even defend myself...from bullies... "
                        a " My grades are low... I'm so...pathetic... "
                        a " They were right...I-i'm just some...lame loser... "
                        a " I don't fit in here at all... "
                        menu:
                            " Comfort him. ":
                                $ abbielv += 5
                                hide abbiesad at bottom
                                show abbieneutral at center
                                " You comfort him until he felt better. "
                                a " ...Thanks again, [name]... "
                                a " You can go back to...doing what you wanted now... "
                                a " I don't want to be a bother to you... "
                                a " Byebye... "
                                hide abbieneutral at right with easeoutright
                                " You then get up after Abbie left, and decided to go somewhere since you still had some time before class starts. "
                                " Where do you go? "
                                menu:
                                    " {image=bubbleicon} Front of the school {image=bubbleicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump frontschool2
                                    " {image=skellicon} Back of the school {image=skellicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump backschool2
                                    " {image=popularicon} The gym {image=popularicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump gym2
                                    " The cafeteria ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump cafe2
                                    " {image=rubyicon} The rooftop {image=rubyicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump rooftop2
                                    " {image=claireicon} The library {image=claireicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump library2
                    " Get a teacher on them ":
                        " You quickly spot a nearby teacher and told them what was going on. "
                        " They come with you and they dragged the trio away, scolding them somewhere else. "
                        " Meanwhile, you help Abbie up from the ground due to the one that was choking him let go of him. "
                        show abbiesad at center with easeinbottom
                        a " *sniff*... "
                        " You sit Abbie down somewhere and ask if he's alright. "
                        a " I'm..I'm fine... "
                        a " Thank you for coming in to help, though... "
                        a " ... "
                        a " I feel...so weak... "
                        a " I can't even defend myself...from bullies... "
                        a " My grades are low... I'm so...pathetic... "
                        a " They were right...I-i'm just some...lame loser... "
                        a " I don't fit in here at all... "
                        menu:
                            " Comfort him. ":
                                $ abbielv += 5
                                hide abbiesad at bottom
                                show abbieneutral at center
                                " You comfort him until he felt better. "
                                a " ...Thanks again, [name]... "
                                a " You can go back to...doing what you wanted now... "
                                a " I don't want to be a bother to you... "
                                a " Byebye... "
                                hide abbieneutral at right with easeoutright
                                " You then get up after Abbie left, and decided to go somewhere since you still had some time before class starts. "
                                " Where do you go? "
                                menu:
                                    " {image=bubbleicon} Front of the school {image=bubbleicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump frontschool2
                                    " {image=skellicon} Back of the school {image=skellicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump backschool2
                                    " {image=popularicon} The gym {image=popularicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump gym2
                                    " The cafeteria ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump cafe2
                                    " {image=rubyicon} The rooftop {image=rubyicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump rooftop2
                                    " {image=claireicon} The library {image=claireicon} ":
                                        scene black with dissolve
                                        pause 2.0
                                        jump library2
            " Let someone else help ":
                " You just stood there and eventually a teacher managed to stop everything from getting worse. "
                " You could've done something, but your body chose not to. "
                " You'll have to spend your time wandering around the school whilst worrying for Abbie and seeing if he's gonna be okay. "
                " To take the scene of what just happened off of your mind, where should you go? "
                menu:
                    " {image=bubbleicon} Front of the school {image=bubbleicon} ":
                        scene black with dissolve
                        pause 2.0
                        jump frontschool2
                    " {image=skellicon} Back of the school {image=skellicon} ":
                        scene black with dissolve
                        pause 2.0
                        jump backschool2
                    " {image=popularicon} The gym {image=popularicon} ":
                        scene black with dissolve
                        pause 2.0
                        jump gym2
                    " The cafeteria ":
                        scene black with dissolve
                        pause 2.0
                        jump cafe2
                    " {image=rubyicon} The rooftop {image=rubyicon} ":
                        scene black with dissolve
                        pause 2.0
                        jump rooftop2
                    " {image=claireicon} The library {image=claireicon} ":
                        scene black with dissolve
                        pause 2.0
                        jump library2
label principalsoffice:
    $ warning1 = True
    $ oligangknow = True
    scene principalsoffice with dissolve
    show oliverangry at right with easeinright
    " You sat next to the other boy, as much as you hated it. "
    " You had to wait for the principal to get there because she was dealing with something else at the moment. "
    " You could very much tell that the guy was still upset and glaring at you for what happened earlier. "
    " You only did it because he deserved it, right? "
    " He was the one that started it first. "
    show msgraceneutral at center with easeinleft
    " Finally, the principal arrives. "
    msg " Alright, so, would one of you like to enlighten me on what happened in the hallway? "
    x " [name] over here thought it was a great idea to start beating me up out of nowhere! "
    x " I wasn't even doing anything, [they] just started to punch me and beat me up and throw me everywhere! "
    msg " ...[name], is this true? "
    " You take a deep breath in. "
    " You then start explaining what REALLY happened to Miss Grace. "
    msg " ...Okay, so let me get this straight first. "
    msg " You're telling me right after your language class had ended, you spotted Oliver here strangling another student. "
    msg " That student being Abbie... "
    msg " Then you stepped in to attempt to stop him but he didn't. "
    msg " So, out of rage you started beating him up? "
    " Miss Grace sighed and seemed to be thinking about a few things. "
    " It took her quite a bit to think of something to say, but eventually she spoke up. "
    msg " [name], I'll leave you off with a warning for now. "
    msg " I know you were only trying to do the right thing, but violence is never the next thing to do if someone isn't listening to you. "
    msg " Though, if you get 5 warnings in total, I have no choice but to expel you from this school. "
    msg " I hope that doesn't happen, since you had just gotten here. And I hope that you won't cause trouble. "
    msg " As for you, Oliver... "
    msg " I'm gonna have to suspend you for 3 days. I hope that you won't do this again. "
    msg " And if you do, I have no hesitation on getting you expelled from this school. "
    msg " I better not be hearing any complaints from you. "
    msg " Oliver, you may go home. As for [name], then you may go to class. It's time for your science class right now. "
    o " ...Fuck... "
    hide oliverangry at right with easeoutright
    msg " Before you go to class, [name]. Could you ask if Abbie's feeling alright? "
    msg " It's much appreciated if you do. "
    " You nodded, before going outside and closing the door to the principal's office. "
    scene black with dissolve
    " You were glad that the situation was finally sorted out, and you could go to science class. "
    " Oliver, Zip, and Edward won't be interactable until Wednesday. "
    pause 2.0
    play music "audio/paperhigh.mp3" fadein 1.5
    jump scienceclass1

label frontschool2:
    scene paperschoolfront with dissolve
    " You step outside to feel that nice fresh air you felt earlier again. "
    " You take a seat on one of the nearby benches, and you didn't notice that someone was there next to you. "
    " That was until they talked to you. "
    if bubbleknow == True:
        show bubblehappy at center with easeinleft
        b " Hiya, [name]! "
        b " What're you doing here? "
        b " I'm just out here looking at the clouds to pass the time... "
        b " It's real relaxing! I used to do this a lot as a kid, you know! "
        hide bubblehappy at bottom
        show bubbleneutral at center
        b " Hmm... Since you probably don't have anything else to do... "
        b " Would ya like to spend some time with me and watch the clouds? "
        menu:
            " Sure! ":
                hide bubbleneutral at bottom
                show bubbleamazed at center
                b " Yay!! Alright, let's do this! "
                hide bubbleamazed at bottom
                show bubblehappy at center
                b " Okay, okay! Tell me what you see! "
                " You look up into the sky... "
                " You see multiple shapes the clouds have formed, but which one should you point out to Bubble? "
                menu:
                    " An open book ":
                        hide bubblehappy at bottom
                        show bubbleneutral at center
                        b " Oooh, an open book? that's pretty interesting! "
                        hide bubbleneutral at bottom
                        show bubblehappy at center
                        b " Maybe that symbolizes how much of a nerd you are? "
                        b " Only kidding, heh! "
                        hide bubblehappy at bottom
                        show bubbleneutral at center
                        b " Hmm... Lemme see what I can find... "
                        b " Hhhh...Oh! I see a little heart over there! "
                        " Bubble pointed up in the direction where the little heart-shaped cloud was. "
                        hide bubbleneutral at bottom
                        show bubblehappy at center
                        b " How cute! "
                        scene black with dissolve
                        " You spent the rest of your break looking at clouds with Bubble. "
                        " For a second you saw a cloud thats shaped like balls, but it quickly disappeared. "
                        play sound "audio/bellring.mp3"
                        " You continued to look at clouds and talk with Bubble until the bell rings. "
                        " You both got up and got to the next class, which was science. "
                        pause 2.0
                        jump scienceclass1
                    " A key ":
                        hide bubblehappy at bottom
                        show bubbleneutral at center
                        b " Ooh, a key? Interesting... "
                        b " Don't know what that means, but I think it's something like... "
                        b " You're the key to unlocking something, maybe? "
                        b " I'm not really sure, eheh... But then again, it couldn't really mean anything! "
                        b " Let's keep looking! "
                        scene black with dissolve
                        " You spent the rest of your break looking at clouds with Bubble. "
                        " For a second you saw a cloud thats shaped like balls, but it quickly disappeared. "
                        play sound "audio/bellring.mp3"
                        " You continued to look at clouds and talk with Bubble until the bell rings. "
                        " You both got up and got to the next class, which was science. "
                        pause 2.0
                        jump scienceclass1
                    " Hey are those ba- ":
                        hide bubblehappy at bottom
                        show bubbleconfuse at center
                        b " Huh...? Balls? "
                        b " I don't see it... "
                        b " Maybe you're just tweaking out, [name]. "
                        hide bubbleconfuse at bottom
                        show bubbleneutral at center
                        b " It would've been funny if we saw it though! "
                        b " Let's keep looking! "
                        scene black with dissolve
                        " You spent the rest of your break looking at clouds with Bubble. "
                        " For a second you saw a cloud thats shaped like balls, but it quickly disappeared. "
                        play sound "audio/bellring.mp3"
                        " You continued to look at clouds and talk with Bubble until the bell rings. "
                        " You both got up and got to the next class, which was science. "
                        pause 2.0
                        jump scienceclass1
            " Nah, I just wanna chill here for a bit. ":
                b " Alrighty then! "
                b " Ooooh, hmm... I see... "
                b " Theres a little heart up there!! How cute! Wait a moment... "
                b " ARE THOSE BALLS{nw} "
                scene black with dissolve
                " You spent the rest of your break chilling whilst Bubble looked at clouds in the sky. "
                " For a second you saw a cloud thats shaped like balls when you looked up, but it quickly disappeared. "
                play sound "audio/bellring.mp3"
                " You continued to look talk with Bubble until the bell rings. "
                " You both got up and got to the next class, which was science. "
                pause 2.0
                jump scienceclass1
    else:
        $ bubbleknow = True
        show bubblehappy at center with easeinleft
        x " Hiya, [name]! "
        x " I don't believe I've properly introduced myself before, but... "
        b " I'm Bubble! It's so great to meet you! "
        b " Anywho, what're you doing here? "
        b " I'm just out here looking at the clouds to pass the time... "
        b " It's real relaxing! I used to do this a lot as a kid, you know! "
        hide bubblehappy at bottom
        show bubbleneutral at center
        b " Hmm... Since you probably don't have anything else to do... "
        b " Would ya like to spend some time with me and watch the clouds? "
        menu:
            " Sure! ":
                hide bubbleneutral at bottom
                show bubbleamazed at center
                b " Yay!! Alright, let's do this! "
                hide bubbleamazed at bottom
                show bubblehappy at center
                b " Okay, okay! Tell me what you see! "
                " You look up into the sky... "
                " You see multiple shapes the clouds have formed, but which one should you point out to Bubble? "
                menu:
                    " An open book ":
                        hide bubblehappy at bottom
                        show bubbleneutral at center
                        b " Oooh, an open book? that's pretty interesting! "
                        hide bubbleneutral at bottom
                        show bubblehappy at center
                        b " Maybe that symbolizes how much of a nerd you are? "
                        b " Only kidding, heh! "
                        hide bubblehappy at bottom
                        show bubbleneutral at center
                        b " Hmm... Lemme see what I can find... "
                        b " Hhhh...Oh! I see a little heart over there! "
                        " Bubble pointed up in the direction where the little heart-shaped cloud was. "
                        hide bubbleneutral at bottom
                        show bubblehappy at center
                        b " How cute! "
                        scene black with dissolve
                        " You spent the rest of your break looking at clouds with Bubble. "
                        " For a second you saw a cloud thats shaped like balls, but it quickly disappeared. "
                        play sound "audio/bellring.mp3"
                        " You continued to look at clouds and talk with Bubble until the bell rings. "
                        " You both got up and got to the next class, which was science. "
                        pause 2.0
                        jump scienceclass1
                    " A key ":
                        hide bubblehappy at bottom
                        show bubbleneutral at center
                        b " Ooh, a key? Interesting... "
                        b " Don't know what that means, but I think it's something like... "
                        b " You're the key to unlocking something, maybe? "
                        b " I'm not really sure, eheh... But then again, it couldn't really mean anything! "
                        b " Let's keep looking! "
                        scene black with dissolve
                        " You spent the rest of your break looking at clouds with Bubble. "
                        " For a second you saw a cloud thats shaped like balls, but it quickly disappeared. "
                        play sound "audio/bellring.mp3"
                        " You continued to look at clouds and talk with Bubble until the bell rings. "
                        " You both got up and got to the next class, which was science. "
                        pause 2.0
                        jump scienceclass1
                    " Hey are those ba- ":
                        hide bubblehappy at bottom
                        show bubbleconfuse at center
                        b " Huh...? Balls? "
                        b " I don't see it... "
                        b " Maybe you're just tweaking out, [name]. "
                        hide bubbleconfuse at bottom
                        show bubbleneutral at center
                        b " It would've been funny if we saw it though! "
                        b " Let's keep looking! "
                        scene black with dissolve
                        " You spent the rest of your break looking at clouds with Bubble. "
                        " For a second you saw a cloud thats shaped like balls, but it quickly disappeared. "
                        play sound "audio/bellring.mp3"
                        " You continued to look at clouds and talk with Bubble until the bell rings. "
                        " You both got up and got to the next class, which was science. "
                        pause 2.0
                        jump scienceclass1
            " Nah, I just wanna chill here for a bit. ":
                b " Alrighty then! "
                b " Ooooh, hmm... I see... "
                b " Theres a little heart up there!! How cute! Wait a moment... "
                b " ARE THOSE BALLS{nw} "
                scene black with dissolve
                " You spent the rest of your break chilling whilst Bubble looked at clouds in the sky. "
                " For a second you saw a cloud thats shaped like balls when you looked up, but it quickly disappeared. "
                play sound "audio/bellring.mp3"
                " You continued to look talk with Bubble until the bell rings. "
                " You both got up and got to the next class, which was science. "
                pause 2.0
                jump scienceclass1

label backschool2:
    scene paperschoolback with dissolve
    " The back of the school was always so peaceful, since no one really goes here. "
    " Except for the fact that it sometimes smells like shit, it's all good. "
    if skellknow == True:
        " You look around for a bit more and find that Skell is here once again. "
        " He seems to be taking a little nap... "
        " Disturb him? "
        menu:
            " Hell yeah ":
                stop music fadeout 1.5
                scene skellcutscene with dissolve
                " You sat down next to him as he took a nap. "
                " Seems like he only had one earphone on, too. "
                " You can hear the faint noise of some vocaloid music he was listening to from his other earphone he wasn't wearing. "
                " Take a listen? "
                menu:
                    " Listen ":
                        " You slowly picked up one of the earbuds that he wasn't wearing so that you wouldn't accidentally wake him up... "
                        " And then you put it on. "
                        play music "audio/whatishatsunemikudoinghere.mp3" fadein 1.5 volume 0.5
                        " ...Well this song is interesting. "
                        " Now that you think about it, it's actually kind of catchy, in an odd way. "
                        " Maybe you should ask Skell what this song was so that you can add it to your Spotify playlist. "
                        " You just sat there and listened to the song for a bit. "
                        " (Feel free to stay here for a bit, and leave once you feel like it.) "
                        " ... "
                        scene paperschoolback with dissolve
                        show skellneutral at center with easeinbottom
                        " Eventually, Skell wakes up. He stretches for a bit and looks around as if he were processing where he was and what he was doing. "
                        hide skellneutral at bottom
                        show skellsurprised at center
                        " It didn't take long for him to figure out that you were listening to one of his songs on his very secret playlist. "
                        stop music fadeout 0.5
                        " Out of embarrassment, he immediately paused the song on his phone. "
                        sk " I, um... "
                        sk " I gotta go. Sorry. "
                        hide skellsurprised at left with easeoutleft
                        " He yanked his earphones and skedaddled his way back into the school. "
                        " ...Man you could've really asked for the songs name, but he was too fast. "
                        play sound "audio/bellring.mp3"
                        play music "audio/paperhigh.mp3" fadein 0.5
                        " ...Oh. The bell rang. "
                        " You're just gonna have to ask him later. "
                        scene black with dissolve
                        pause 2.0
                        jump scienceclass1
                    " Nah ":
                        scene paperschoolback with dissolve
                        " Well, you just missed your opportunity to listen to a banger Hatsune Miku song. "
                        " You honestly kinda just sat there and looked around, not knowing what to do. "
                        " Sure, you could've pranked him right now but you didn't really know what to prank him with. "
                        show skellneutral at center with easeinbottom
                        " Skell eventually wakes up and stretches and looks around, processing where he was and what he was doing. "
                        hide skellneutral at bottom
                        show skellsurprised at center
                        " Then there's that realization that you might've heard what he was listening to. "
                        " Out of embarrassment he paused the music on his phone and he got up. "
                        sk " ...I'm sorry, I have to uh...go. "
                        hide skellsurprised at left with easeoutleft
                        " ...Huh. "
                        " Well, you didn't even really listen to what he was listening to in the first place. "
                        play sound "audio/bellring.mp3"
                        play music "audio/paperhigh.mp3" fadein 0.5
                        " ...Oh. The bell rang. "
                        " Well, time to go to your next class, then. "
                        scene black with dissolve
                        pause 2.0
                        jump scienceclass1
            " Nah no thanks ":
                " Well, you just missed your opportunity to listen to a banger Hatsune Miku song. "
                " You honestly kinda just sat there and looked around, not knowing what to do. "
                " Sure, you could've pranked him right now but you didn't really know what to prank him with. "
                show skellneutral at center with easeinbottom
                " Skell eventually wakes up and stretches and looks around, processing where he was and what he was doing. "
                hide skellneutral at bottom
                show skellsurprised at center
                " Then there's that realization that you might've heard what he was listening to. "
                " Out of embarrassment he paused the music on his phone and he got up. "
                sk " ...I'm sorry, I have to uh...go. "
                hide skellsurprised at left with easeoutleft
                " ...Huh. "
                " Well, you didn't even really listen to what he was listening to in the first place. "
                play sound "audio/bellring.mp3"
                " ...Oh. The bell rang. "
                " Well, time to go to your next class, then. "
                scene black with dissolve
                pause 2.0
                jump scienceclass1
    else:
        " You look around for a bit more and find a little emo guy chilling. "
        " He seems to be taking a little nap... "
        " Disturb him? "
        menu:
            " Hell yeah ":
                stop music fadeout 1.5
                scene skellcutscene with dissolve
                " You sat down next to him as he took a nap. "
                " Seems like he only had one earphone on, too. "
                " You can hear the faint noise of some vocaloid music he was listening to from his other earphone he wasn't wearing. "
                " Take a listen? "
                menu:
                    " Listen ":
                        " You slowly picked up one of the earbuds that he wasn't wearing so that you wouldn't accidentally wake him up... "
                        " And then you put it on. "
                        play music "audio/whatishatsunemikudoinghere.mp3" fadein 1.5 volume 0.5
                        " ...Well this song is interesting. "
                        " Now that you think about it, it's actually kind of catchy, in an odd way. "
                        " Maybe you should ask him what this song was so that you can add it to your Spotify playlist. "
                        " You just sat there and listened to the song for a bit. "
                        " (Feel free to stay here for a bit, and leave once you feel like it.) "
                        " ... "
                        scene paperschoolback with dissolve
                        show skellneutral at center with easeinbottom
                        " Eventually, the other boy wakes up. He stretches for a bit and looks around as if he were processing where he was and what he was doing. "
                        hide skellneutral at bottom
                        show skellsurprised at center
                        " It didn't take long for him to figure out that you were listening to one of his songs on his very secret playlist. "
                        stop music fadeout 0.5
                        " Out of embarrassment, he immediately paused the song on his phone. "
                        x " I, um... "
                        x " I gotta go. Sorry. "
                        hide skellsurprised at left with easeoutleft
                        " He yanked his earphones and skedaddled his way back into the school. "
                        " ...Man you could've really asked for the songs name, but he was too fast. "
                        play sound "audio/bellring.mp3"
                        play music "audio/paperhigh.mp3" fadein 0.5
                        " ...Oh. The bell rang. "
                        " You're just gonna have to ask him later. "
                        scene black with dissolve
                        pause 2.0
                        jump scienceclass1
                    " Nah ":
                        scene paperschoolback with dissolve
                        " Well, you just missed your opportunity to listen to a banger Hatsune Miku song. "
                        " You honestly kinda just sat there and looked around, not knowing what to do. "
                        " Sure, you could've pranked him right now but you didn't really know what to prank him with. "
                        show skellneutral at center with easeinbottom
                        " The other boy eventually wakes up and stretches and looks around, processing where he was and what he was doing. "
                        hide skellneutral at bottom
                        show skellsurprised at center
                        " Then there's that realization that you might've heard what he was listening to. "
                        " Out of embarrassment he paused the music on his phone and he got up. "
                        x " ...I'm sorry, I have to uh...go. "
                        hide skellsurprised at left with easeoutleft
                        " ...Huh. "
                        " Well, you didn't even really listen to what he was listening to in the first place. "
                        play sound "audio/bellring.mp3"
                        play music "audio/paperhigh.mp3" fadein 0.5
                        " ...Oh. The bell rang. "
                        " Well, time to go to your next class, then. "
                        scene black with dissolve
                        pause 2.0
                        jump scienceclass1
            " Nah no thanks ":
                " Well, you just missed your opportunity to listen to a banger Hatsune Miku song. "
                " You honestly kinda just sat there and looked around, not knowing what to do. "
                " Sure, you could've pranked him right now but you didn't really know what to prank him with. "
                show skellneutral at center with easeinbottom
                " The other boy eventually wakes up and stretches and looks around, processing where he was and what he was doing. "
                hide skellneutral at bottom
                show skellsurprised at center
                " Then there's that realization that you might've heard what he was listening to. "
                " Out of embarrassment he paused the music on his phone and he got up. "
                x " ...I'm sorry, I have to uh...go. "
                hide skellsurprised at left with easeoutleft
                " ...Huh. "
                " Well, you didn't even really listen to what he was listening to in the first place. "
                play sound "audio/bellring.mp3"
                " ...Oh. The bell rang. "
                " Well, time to go to your next class, then. "
                scene black with dissolve
                pause 2.0
                jump scienceclass1

label gym2:
    scene poolroom with dissolve
    " Oh yes, the gym. "
    " You decided to sit on one of the bleachers, and you could hear a two girls gossiping about something. "
    if popularknow == True:
        " You looked around and you realize it was Petunia and Lizzy. "
        " Go up to them? "
        menu:
            " Sit closer to them and talk to them ":
                " You moved over to where they were and listened to what they were talking about. "
                show lizzyneutral at left with easeinright
                show petunianeutral at right with easeinright
                lz " Did you hear? Abbie was almost choked to death once language class ended. "
                hide petunianeutral at bottom
                show petuniasurprised at right
                p " FOR REAL?? WHY?? "
                lz " Don't know. Luckily a teacher came by and stopped it from getting worse. "
                p " Who started it though? "
                lz " Oliver and his little crew. "
                hide petuniasurprised at bottom
                show petuniaangry at right
                p " Ouuughh, those BITCHES! Why should I even be surprised at this point?! "
                p " It's always those hoes that start it, huh?! "
                p " {sc}AND WHAT MADE THEM THINK THAT IT WAS OKAY TO DO THAT, HUH?!{/sc} " with vpunch
                lz " 'tunia, calm down. Atleast Abbie's okay. "
                lz " And besides, Oliver's getting suspended for 3 days, from what I heard. "
                p " Well, that's good to hear... but we have to deal with the other two little shits. "
                p " Whew... Sometimes I wonder what's going on in Oliver's head. "
                hide petuniaangry at bottom
                show petunianeutral at right
                p " Oh, hey there, [name]... "
                p " Gonna move onto another topic here to lighten the mood, erm... "
                p " Uhh... Liz, what was the thing we were gonna do again? "
                lz " The thing. "
                p " Thing? which thi-{nw} "
                p " Oh!! Me and Liz are gonna do another tiktok tomorrow! "
                p " Wanna be in it? "
                menu:
                    " Sure! ":
                        $ popularlv += 10
                        $ populartiktok = True
                        hide petunianeutral at bottom
                        show petuniahappy at right
                        hide lizzyneutral at bottom
                        show lizzyhappy at left
                        p " Great! Maybe we'll let you join us on our channel if that video gets popular enough! "
                        lz " It'll be nice to have you on a video. "
                        hide petuniahappy at bottom
                        hide lizzyhappy at bottom
                        show petunianeutral at right
                        show lizzyneutral at left
                        p " Now, to pass the time... "
                        p " How about let's talk about some ideas for the video we're gonna do tomorrow? "
                        lz " ...How about we add a chill guy image somewhere? "
                        if calm == True:
                            p " Eh, we don't need that. "
                            p " We've already got one right here. "
                            " ... "
                            " You're just a chill guy!{nw} "
                            " I mean what huh "
                        else:
                            p " Eeeh, we don't really need that... "
                        lz " Or we could do another popular tiktok dance and hope that goes popular{nw} "
                        lz " Wait... I might have an idea. "
                        lz " We could do this QnA thing with [name] with a trending audio to boost chances of getting views. "
                        lz " It's not guaranteed to get popular, but we could try. "
                        p " Sounds a little weird, but...yeah, we could just try to do something new for once. "
                        p " [name] IS new, so this could get a chance for both us and the viewers to know [them] better! "
                        lz " ...We could've just asked [them] a few questions about [them]self, but okay. "
                        p " How about we do this... Uh, at the back of the school maybe when class is done? "
                        lz " Sure. "
                        hide petunianeutral at bottom
                        show petuniahappy at right
                        p " Alrighty! Let's do this, guys! "
                        scene black with dissolve
                        " You talked with Petunia and Lizzy about even more ideas for the video for the rest of the break. "
                        play sound "audio/bellring.mp3"
                        " Though, of course, the bell rings and cuts you off in the middle of you giving a really good idea. "
                        " You all get up and get to the next class: Science. "
                        pause 2.0
                        jump scienceclass1
                    " Nah, no thanks ":
                        $ popularlv += 5
                        $ populartiktok = False
                        p " Ah, alrighty then... "
                        p " We'll just be thinking of video ideas then! "
                        p " You could still help us with getting ideas, by the way. "
                        lz " Okay, so how about we... "
                        scene black with dissolve
                        " You listened to Lizzy and Petunia about their video ideas. "
                        " You also gave them some feedback and some ideas of your own to make them more popular. "
                        " Well, they weren't popular in the first place but that's what they believe. "
                        play sound "audio/bellring.mp3"
                        " Whilst you were helping them, the bell rang and it was time to go to your next class. "
                        " You all got up and went to Science class. "
                        pause 2.0
                        jump scienceclass1
    else:
        " You looked around and you saw that it was a bunny girl and a girl with a crown. "
        " They seem pretty busy... should you go ahead and talk to them? "
        menu:
            " Sit closer to them and talk to them ":
                " You moved over to where they were and listened to what they were talking about. "
                show lizzyneutral at left with easeinright
                show petunianeutral at right with easeinright
                x " Did you hear? Abbie was almost choked to death once language class ended. "
                hide petunianeutral at bottom
                show petuniasurprised at right
                x " FOR REAL?? WHY?? "
                x " Don't know. Luckily a teacher came by and stopped it from getting worse. "
                x " Who started it though? "
                x " Oliver and his little crew. "
                hide petuniasurprised at bottom
                show petuniaangry at right
                x " Ouuughh, those BITCHES! Why should I even be surprised at this point?! "
                x " It's always those hoes that start it, huh?! "
                x " {sc}AND WHAT MADE THEM THINK THAT IT WAS OKAY TO DO THAT, HUH?!{/sc} " with vpunch
                x " 'tunia, calm down. Atleast Abbie's okay. "
                x " And besides, Oliver's getting suspended for 3 days, from what I heard. "
                p " Well, that's good to hear... but we have to deal with the other two little shits. "
                p " Whew... Sometimes I wonder what's going on in Oliver's head. "
                hide petuniaangry at bottom
                show petunianeutral at right
                p " Oh, hey there, [name]... "
                p " Gonna move onto another topic here to lighten the mood, erm... "
                p " Oh, right! We never really properly have introduced ourselves before! "
                $ popularknow = True
                p " I'm Petunia, and this is my best friend, Lizzy! "
                lz " I'm sure you've heard of us before, we're kinda famous on TikTok. "
                hide petunianeutral at bottom
                show petuniahappy at right
                p " It's great to meet you! "
                hide petuniahappy at bottom
                show petunianeutral at right
                " Something tells you that they're not all that famous as they seem... "
                " They still look pretty cool though. "
                p " Oh, yeah... Liz, weren't we supposed to do something? "
                p " Uhh... what was the thing we were gonna do again? "
                lz " The thing. "
                p " Thing? which thi-{nw} "
                p " Oh!! Me and Liz are gonna do another tiktok tomorrow! "
                p " Wanna be in it? "
                menu:
                    " Sure! ":
                        $ popularlv += 10
                        $ populartiktok = True
                        hide petunianeutral at bottom
                        show petuniahappy at right
                        hide lizzyneutral at bottom
                        show lizzyhappy at left
                        p " Great! Maybe we'll let you join us on our channel if that video gets popular enough! "
                        lz " It'll be nice to have you on a video. "
                        hide petuniahappy at bottom
                        hide lizzyhappy at bottom
                        show petunianeutral at right
                        show lizzyneutral at left
                        p " Now, to pass the time... "
                        p " How about let's talk about some ideas for the video we're gonna do tomorrow? "
                        lz " ...How about we add a chill guy image somewhere? "
                        if calm == True:
                            p " Eh, we don't need that. "
                            p " We've already got one right here. "
                            " ... "
                            " You're just a chill guy!{nw} "
                            " I mean what huh "
                        else:
                            p " Eeeh, we don't really need that... "
                        lz " Or we could do another popular tiktok dance and hope that goes popular{nw} "
                        lz " Wait... I might have an idea. "
                        lz " We could do this QnA thing with [name] with a trending audio to boost chances of getting views. "
                        lz " It's not guaranteed to get popular, but we could try. "
                        p " Sounds a little weird, but...yeah, we could just try to do something new for once. "
                        p " [name] IS new, so this could get a chance for both us and the viewers to know [them] better! "
                        lz " ...We could've just asked [them] a few questions about [them]self, but okay. "
                        p " How about we do this... Uh, at he back of the school maybe when class is done? "
                        lz " Sure. "
                        hide petunianeutral at bottom
                        show petuniahappy at right
                        p " Alrighty! Let's do this, guys! "
                        scene black with dissolve
                        " You talked with Petunia and Lizzy about even more ideas for the video for the rest of the break. "
                        play sound "audio/bellring.mp3"
                        " Though, of course, the bell rings and cuts you off in the middle of you giving a really good idea. "
                        " You all get up and get to the next class: Science. "
                        pause 2.0
                        jump scienceclass1
                    " Nah, no thanks ":
                        $ popularlv += 5
                        $ populartiktok = False
                        p " Ah, alrighty then... "
                        p " We'll just be thinking of video ideas then! "
                        p " You could still help us with getting ideas, by the way. "
                        lz " Okay, so how about we... "
                        scene black with dissolve
                        " You listened to Lizzy and Petunia about their video ideas. "
                        " You also gave them some feedback and some ideas of your own to make them more popular. "
                        " Well, they weren't popular in the first place but that's what they believe. "
                        play sound "audio/bellring.mp3"
                        " Whilst you were helping them, the bell rang and it was time to go to your next class. "
                        " You all got up and went to Science class. "
                        pause 2.0
                        jump scienceclass1
label cafe2:
    scene cafeteria with dissolve
    " The cafeteria is loud as per usual. "
    " Who do you want to sit with? "
    if abbieknow, engelknow, robbyknow == True:
        menu:
            " {image=abbieicon} Sit next to Abbie {image=abbieicon} ":
                jump abbiesit
            " {image=engelicon} Sit next to Engel {image=engelicon} ":
                jump engelsit
            " {image=robbyicon} Sit next to Robby and a weird looking girl. {image=rileyicon} ":
                jump robbrileysit
    elif abbieknow, engelknow == True and robbyknow == False:
        menu:
            " {image=abbieicon} Sit next to Abbie {image=abbieicon} ":
                jump abbiesit
            " {image=engelicon} Sit next to Engel {image=engelicon} ":
                jump engelsit
            " {image=robbyicon} Sit next to a guy with a weird hat and a weird looking girl. {image=rileyicon} ":
                jump robbrileysit
    elif abbieknow, robbyknow == True and engelknow == False:
        menu:
            " {image=abbieicon} Sit next to Abbie {image=abbieicon} ":
                jump abbiesit
            " {image=engelicon} Sit next to a white haired boy with two feathers on his head {image=engelicon} ":
                jump engelsit
            " {image=robbyicon} Sit next to Robby and a weird looking girl. {image=rileyicon} ":
                jump robbrileysit
    elif robbyknow, engelknow == True and abbieknow == False:
        menu:
            " {image=abbieicon} Sit next to a lonely looking boy {image=abbieicon} ":
                jump abbiesit
            " {image=engelicon} Sit next to Engel {image=engelicon} ":
                jump engelsit
            " {image=robbyicon} Sit next to Robby and a weird looking girl. {image=rileyicon} ":
                jump robbrileysit
    elif abbieknow == True and robbyknow, engelknow == False:
        menu:
            " {image=abbieicon} Sit next to Abbie {image=abbieicon} ":
                jump abbiesit
            " {image=engelicon} Sit next to a white haired boy with two feathers on his head {image=engelicon} ":
                jump engelsit
            " {image=robbyicon} Sit next to a guy with a weird hat and a weird looking girl. {image=rileyicon} ":
                jump robbrileysit
    elif robbyknow == True and abbieknow, engelknow == False:
        menu:
            " {image=abbieicon} Sit next to a lonely looking boy {image=abbieicon} ":
                jump abbiesit
            " {image=engelicon} Sit next to a white haired boy with two feathers on his head {image=engelicon} ":
                jump engelsit
            " {image=robbyicon} Sit next to Robby and a weird looking girl. {image=rileyicon} ":
                jump robbrileysit
    elif engelknow == True and abbieknow, robbyknow == False:
        menu:
            " {image=abbieicon} Sit next to a lonely looking boy {image=abbieicon} ":
                jump abbiesit
            " {image=engelicon} Sit next to Engel {image=engelicon} ":
                jump engelsit
            " {image=robbyicon} Sit next to a guy with a weird hat and a weird looking girl. {image=rileyicon} ":
                jump robbrileysit
    else:
        menu:
            " {image=abbieicon} Sit next to a lonely looking boy {image=abbieicon} ":
                jump abbiesit
            " {image=engelicon} Sit next to a white haired boy with two feathers on his head {image=engelicon} ":
                jump engelsit
            " {image=robbyicon} Sit next to a guy with a weird hat and a weird looking girl. {image=rileyicon} ":
                jump robbrileysit
    label abbiesit:
        show abbieneutral at center with easeinleft
        if abbieknow == True:
            " You decided to sit next to Abbie, who seems to be in deep thought. "
            " He was looking at the ground and fiddling with his fingers whilst he thought about something... "
            " Wonder what's on his mind. "
            " Eventually, he takes notice that you're there and he looks up at you with his usual expression. "
            a " Hey there, [name]... "
            if abbiemeandefend == True:
                a " You know... I appreciate what you did for me, but... "
                a " You didn't have to do all of that for me... "
                a " But still, thank you... I know that no one else would've done something like that for me... "
                a " I could've died there...  "
                " You then remembered that Miss Grace asked you to check on Abbie. "
                " You asked if he was alright now. "
                " Upon closer inspection, seems like Oliver had beaten up Abbie a bit before he choked him. "
                " You saw a lot of scars and bruises...Big scars, little scars... "
                " That just made you a little more pissed than you originally were towards Oliver. "
                " Luckily, he's not gonna be here for a bit. "
                a " Oh, erm... I'm fine now. "
                a " Also, Miss Grace asked...? "
                a " ..mmm.. "
                menu:
                    " Find bandages for Abbie ":
                        $ abbielv += 10
                        a " You...you're gonna find bandages for...me...? "
                        hide abbieneutral at bottom
                        show abbiehappy at center
                        a " T-thank you... "
                        a " ...You're so nice... "
                        scene black with dissolve
                        " You went to go find some bandages for Abbie. "
                        " You had to push a few people out of the way, but atleast you got the bandages. "
                        " You then went back to Abbie once you got the bandages you needed. "
                        scene hallway with dissolve
                        show abbieneutral at center with dissolve
                        a " ...You...really didn't have to do this for me... "
                        a " I could've gotten some bandages myself... "
                        a " But, still... thanks... "
                        a " For, um... "
                        a " This is gonna sound a little weird, since we don't really know eachother that well, but... "
                        a " Thank you for being there for me...and doing all of this for me... "
                        a " I...I appreciate it... A whole lot. "
                        a " If you weren't so kind to me, you'd probably be laughing at my face for how weak I am, heh... "
                        a " ... "
                        a " Um, [name]... "
                        a " Why do you...choose to stay with me...? "
                        a " ...Is this just because you feel bad for me, or... "
                        menu:
                            " Because I see you as a friend and I care for you ":
                                $ abbielv += 10
                                hide abbieneutral at bottom
                                show abbiehappy at center
                                a " That's... "
                                a " ... "
                                a " You have to be the nicest person I've ever met here, [name]... "
                                a " ...I never thought that I would have a friend, other than Lana... "
                                " You continued to talk with Abbie, and you've also finished wrapping up the bandages on his arms. "
                                " It still makes you pissed that Oliver causes him this pain, but you remind yourself that Oliver's not gonna be here for now. "
                                " You calm yourself down before you accidentally go feral again. "
                                play sound "audio/bellring.mp3"
                                " The bell rings, but you could hear Abbie let out another quiet 'thank you' to you as you stood up. "
                                " You smiled and him and gave him a little pat on the head before you went to class. "
                                scene black with dissolve
                                pause 2.0
                                jump scienceclass1
                            " Say nothing ":
                                $ abbielv += 2
                                a " ... "
                                " Abbie says nothing as you continue to patch him up. "
                                " You continued to talk with Abbie, and you've also finished wrapping up the bandages on his arms. "
                                " It still makes you pissed that Oliver causes him this pain, but you remind yourself that Oliver's not gonna be here for now. "
                                " You calm yourself down before you accidentally go feral again. "
                                play sound "audio/bellring.mp3"
                                " The bell rings, but you could hear Abbie let out another quiet 'thank you' to you as you stood up. "
                                " You smiled and him and gave him a little pat on the head before you went to class. "
                                scene black with dissolve
                                pause 2.0
                                jump scienceclass1
                    " Hang out with Abbie for a bit ":
                        $ abbielv += 3
                        scene black with dissolve
                        " You talked with Abbie for the rest of the break. "
                        " He said it comforted him that someone actually wanted to talk to him... "
                        " That someone was you. How nice. "
                        play sound "audio/bellring.mp3"
                        " In the middle of talking with Abbie, the bell rings, signaling that it was time for the next class. "
                        " You both got up and went to your next class; Science. "
                        pause 2.0
                        jump scienceclass1
            else:
                " You waved to him as a 'hello', but then you noticed something... "
                " You noticed bruises and cuts (big and small) on Abbie's arms. You start to get concerned. "
                " You then asked Abbie about them. "
                a " Oh...these...? "
                hide abbieneutral at bottom
                show abbiesad at center
                a " Oliver gave me these before he started to choke me... "
                a " It...I-it still hurts... a lot... "
                a " I keep remembering what happened... "
                a " I'm so useless... "
                menu:
                    " Find bandages for Abbie ":
                        $ abbielv += 10
                        a " You...you're gonna find bandages for...me...? "
                        hide abbieneutral at bottom
                        show abbiehappy at center
                        a " T-thank you... "
                        a " ...You're so nice... "
                        scene black with dissolve
                        " You went to go find some bandages for Abbie. "
                        " You had to push a few people out of the way, but atleast you got the bandages. "
                        " You then went back to Abbie once you got the bandages you needed. "
                        scene hallway with dissolve
                        show abbieneutral at center with dissolve
                        a " ...You...really didn't have to do this for me... "
                        a " I could've gotten some bandages myself... "
                        a " But, still... thanks... "
                        a " For, um... "
                        a " This is gonna sound a little weird, since we don't really know eachother that well, but... "
                        a " Thank you for being there for me...and doing all of this for me... "
                        a " I...I appreciate it... A whole lot. "
                        a " If you weren't so kind to me, you'd probably be laughing at my face for how weak I am, heh... "
                        a " ... "
                        a " Um, [name]... "
                        a " Why do you...choose to stay with me...? "
                        a " ...Is this just because you feel bad for me, or... "
                        menu:
                            " Because I see you as a friend and I care for you ":
                                $ abbielv += 10
                                hide abbieneutral at bottom
                                show abbiehappy at center
                                a " That's... "
                                a " ... "
                                a " You have to be the nicestperson I've ever met here, [name]... "
                                a " ...I never thought that I would have a friend, other than Lana... "
                                " You continued to talk with Abbie, and you've also finished wrapping up the bandages on his arms. "
                                " It still makes you pissed that Oliver causes him this pain, but you remind yourself that Oliver's not gonna be here for now. "
                                " You calm yourself down before you accidentally go feral. "
                                play sound "audio/bellring.mp3"
                                " The bell rings, but you could hear Abbie let out another quiet 'thank you' to you as you stood up. "
                                " You smiled and him and gave him a little pat on the head before you went to class. "
                                scene black with dissolve
                                pause 2.0
                                jump scienceclass1
                            " Say nothing ":
                                $ abbielv += 2
                                a " ... "
                                " Abbie says nothing as you continue to patch him up. "
                                " You continued to talk with Abbie, and you've also finished wrapping up the bandages on his arms. "
                                " It still makes you pissed that Oliver causes him this pain, but you remind yourself that Oliver's not gonna be here for now. "
                                " You calm yourself down before you accidentally go feral again. "
                                play sound "audio/bellring.mp3"
                                " The bell rings, but you could hear Abbie let out another quiet 'thank you' to you as you stood up. "
                                " You smiled and him and gave him a little pat on the head before you went to class. "
                                scene black with dissolve
                                pause 2.0
                                jump scienceclass1
                    " Hang out with Abbie for a bit ":
                        $ abbielv += 3
                        scene black with dissolve
                        " You talked with Abbie for the rest of the break. "
                        " He said it comforted him that someone actually wanted to talk to him... "
                        " That someone was you. How nice. "
                        play sound "audio/bellring.mp3"
                        " In the middle of talking with Abbie, the bell rings, signaling that it was time for the next class. "
                        " You both got up and went to your next class; Science. "
                        pause 2.0
                        jump scienceclass1
        else:
            $ abbieknow = True
            " You decided to sit next to the lonely boy, who seems to be in deep thought. "
            " He was looking at the ground and fiddling with his fingers whilst he thought about something... "
            " Wonder what's on his mind. "
            " Eventually, he takes notice that you're there and he looks up at you. "
            x " Oh, u-um... Hey there... "
            x " I...I'm um... "
            a " ...I'm Abbie... Nice to meet you... "
            " You look closer and you saw that he has bruises and cuts on his arms. "
            " You immediately become concerned, and you asked him on who gave those wounds. "
            a " These...? oh.... "
            hide abbieneutral at bottom
            show abbiesad at center
            a " Oliver gave me these, earlier... "
            a " Luckily, a teacher came by and stopped him for choking me.. "
            a " ...I could've died there... "
            " Abbie whispers something to himself that wasn't audible enough for you to hear. "
            " But, you could guess that it was something very concerning. "
            " Something very concerning that you wouldn't wanna hear someone do. "
            " You started comforting Abbie just incase he's thinking of doing anything stupid. "
            a " ... "
            hide abbiesad at bottom
            show abbieneutral at center
            a " ...You...You're very nice, [name]... "
            scene black with dissolve
            " You continued to comfort Abbie and listened to all of his worries for the rest of the break. "
            " You didn't want him to actually...Uh, how do I word this as a narrator... "
            " You don't actually want him to reset character. "
            " That's the best I can do. "
            " Thankfully, he reassured you that he isn't doing anything stupid anytime soon. "
            " ...Hopefully, just hopefully that wasn't a lie. "
            play sound "audio/bellring.mp3"
            " In the middle of you comforting Abbie, the bell rings. "
            " You made sure Abbie was okay for one last time, and then you went to your next class: Science. "
            pause 2.0
            jump scienceclass1
    label engelsit:
        show engelneutral at center with easeinright
        if engelknow == True:
            " You walk up and sit next to Engel, who seems to be busy reading something... "
            " You look closer, and it seems like he's studying. Studying for science. "
            " Why? is there gonna be a quiz? "
            " Engel was so focused in studying, that he didn't even notice you for the first few minutes of you being there. "
            " Eventually though, he noticed you. "
            e " O-oh! Sorry [name], I got too focused on studying... "
            e " (That was quite rude of me...erm...) "
            e " W...well... We have a Science quiz today. "
            e " I may or may not have forgotten and just now got reminded of it... "
            e " Science is our next subject, so I'm rushing this a bit... "
            e " Would you like to study with me? "
            menu:
                " Sure ":
                    e " Alrighty, here we go... "
                    scene black with dissolve
                    " You studied with Engel for the science quiz today. "
                    " You've gained answers for the science quiz! In order: "
                    " Gravitational Force, NaCl, Mitochondria, Milkyway, Mantle. "
                    play sound "audio/bellring.mp3"
                    " The bell rings as you finished up studying with Engel. "
                    " You then get up and went to science class. "
                    pause 2.0
                    jump scienceclass1
                " Nah ":
                    e " Alright... "
                    scene black with dissolve
                    " You sort of just sat there whilst Engel studied. "
                    " He seemed to be so focused to the point that he didn't even respond to you. "
                    "  ...Huh. Well you did hear that he was somewhat of a top student.. "
                    play sound "audio/bellring.mp3"
                    " After a while of sitting there, the bell rings, signalling that it was time to go to the next class. "
                    " ...Which is science. "
                    " You get up and you went to your classroom. "
                    pause 2.0
                    jump scienceclass1
        else:
            $ engelknow = True
            " You walk up and sit next to the white haired boy, who seems to be busy reading something... "
            " You look closer, and it seems like he's studying. Studying for science. "
            " Why? is there gonna be a quiz? "
            " He was so focused in studying, that he didn't even notice you for the first few minutes of you being there. "
            " Eventually though, he noticed you. "
            x " O-oh! Sorry [name], I got too focused on studying... "
            x " (That was quite rude of me...erm...) "
            e " I'm Engel by the way...it's nice to meet you. "
            " You ask him what he's doing. "
            e " W...well... We have a Science quiz today. "
            e " I may or may not have forgotten and just now got reminded of it... "
            e " Science is our next subject, so I'm rushing this a bit... "
            e " Would you like to study with me? "
            menu:
                " Sure ":
                    e " Alrighty, here we go... "
                    scene black with dissolve
                    " You studied with Engel for the science quiz today. "
                    " You've gained answers for the science quiz! In order: "
                    " Gravitational Force, NaCl, Mitochondria, Milkyway, Mantle. "
                    play sound "audio/bellring.mp3"
                    " The bell rings as you finished up studying with Engel. "
                    " You then get up and went to science class. "
                    pause 2.0
                    jump scienceclass1
                " Nah ":
                    e " Alright... "
                    scene black with dissolve
                    " You sort of just sat there whilst Engel studied. "
                    " He seemed to be so focused to the point that he didn't even respond to you. "
                    "  ...Huh. Well you did hear that he was somewhat of a top student.. "
                    play sound "audio/bellring.mp3"
                    " After a while of sitting there, the bell rings, signalling that it was time to go to the next class. "
                    " ...Which is science. "
                    " You get up and you went to your classroom. "
                    pause 2.0
                    jump scienceclass1
    label robbrileysit:
        show robbyneutral at left with easeinright
        show rileyneutral at right with easeinright
        if robbyknow == True:
            $ rileyknow = True
            " You sat next Robby and this strange looking girl... "
            " She was rambling about something whilst Robby was busy fixing something that apparently the girl had broken. "
            " Though, the girl seemed not to care and continued to talk. "
            " You're honestly starting to get a little more curious the more she's words she's spitting out... "
            " Though she's talking somehow a bit too fast for you to understand some of her words. "
            " Try to listen into what the girl's saying? "
            menu:
                " Sure, might be some drama ":
                    " You attempt to listen to what the girls saying... "
                    x " andthenimworkingonthisfanficofmeandoliver{nw} "
                    x " whereimoliversgirlfriendandwifeandwekissandlivehappilyeverafter{nw} "
                    x " butthenalicetriestotakehimawayfromme{nw} "
                    x " soibecomethealphaandtakehimbackbecausehesmypookiebear{nw} "
                    x " andhesmineforeverandever{nw} "
                    x " andeverandeverandeverandeverand{nw} "
                    hide robbyneutral at bottom
                    show robbyangry at left
                    rb " OH MY GOD, RILEY! SHUT UP! "
                    rb " I'm trying to work here, I'm trying to fix one of Cubbie's toys that YOU broke! "
                    rb " Could you {i}PLEASE{/i} let me work in peace, "
                    rb " Instead of YAPPING and YAPPING about OLIVER out of all people?! "
                    hide rileyneutral at bottom
                    show rileyhappy at right
                    x " Sorry, can't hear youuuu~ "
                    x " so then like (even more annoying yapping) "
                    rb " Sigh... When will she ever stop... "
                    menu:
                        " Tell the girl to stop ":
                            " You kindly tell the girl to stop. "
                            " According to Robby's information, this girl REALLY likes Oliver. "
                            " What should you tell her? "
                            if kind == True:
                                menu:
                                    " hey so like you should probably be quiet otherwise oliver wont like you ":
                                        jump rileyok
                                    " heyy if you keep talking oliver wont like you ":
                                        jump rileyok
                                    " stop talking. ":
                                        jump rileyok
                            elif mean == True:
                                menu:
                                    " yk oliver would hate you cause you yap too much ":
                                        jump rileyok
                                    " js shut up you yappatron 6000 ffs ":
                                        jump rileyoh
                                    " (your response here was censored because it was too rude) ":
                                        jump rileyoh
                            elif calm == True:
                                menu:
                                    " yooo buddy you should probably stop cause olivers watching ":
                                        jump rileyok
                                    " dudeee you should prolly stop ":
                                        jump rileyok
                                    " can you stop bro ":
                                        jump rileyok
                            label rileyok:
                                hide rileyhappy at bottom
                                show rileyneutral at right
                                ri " ... "
                                ri " Fine... "
                                ri " Both of you are so boring! "
                                hide robbyangry at bottom
                                show robbyneutral at left
                                rb " I just want to work in peace, Riley. "
                                rb " You could go ahead and yap to someone else... "
                                rb " Like Ruby. Wonder where she's at, now... "
                                rb " Probably busy talking with Skell, or doing something else. "
                                rb " Or you could go ahead and try to find Oliver. "
                                rb " Heard he really wants to see you today. "
                                hide rileyneutral at bottom
                                show rileyhappy at right
                                ri " REALLY?! WHERE IS HE!!!!!! "
                                hide rileyhappy at left with easeoutleft
                                pause 0.5
                                hide robbyneutral at bottom
                                show robbyhappy at center with move
                                rb " ...That always seems to get her, heh. "
                                rb " Now I'll have no disturbances... "
                                menu:
                                    " Help Robby with what he's working on ":
                                        $ robbrileylv += 10
                                        hide robbyhappy at bottom
                                        show robbyneutral at center
                                        rb " Huh...? You wanna help out? "
                                        hide robbyneutral at bottom
                                        show robbyhappy at center
                                        rb " Well, if it means getting this done faster, then of course you can! "
                                        scene black with dissolve
                                        " You helped Robby with fixing Cubbie's toy. "
                                        " It took a bit, but eventually it looked as good as new! "
                                        " You've been so distracted by fixing it, you didn't notice that the bell had rang. "
                                        " Robby thanked you for your help, before you and him went to class together. "
                                        pause 2.0
                                        jump scienceclass1
                                    " Just chill with Robby for a bit " :
                                        $ robbrileylv += 5
                                        rb " Now, time to get back to work on this thing... "
                                        scene black with dissolve
                                        " You watched Robby fix one of Cubbie's toys, with you and him talking for a bit. "
                                        " You couldn't really help him fix what's been broken =, because you didn't know how to fix stuff like that. "
                                        " In your case, you'd probably make it look worse than it originally was. "
                                        " It took a bit for Robby to fix it, but eventually it looked as good as new!! "
                                        " The bell rang as soon as he finished making it, though. "
                                        " You got up and you headed off to your next class. "
                                        pause 2.0
                                        jump scienceclass1
                            label rileyoh:
                                hide rileyhappy at bottom
                                show rileysad at right
                                ri " ... "
                                ri " ...Oh! That's not... "
                                hide rileysad at left with easeoutright
                                ri " {b}{sc}WAAAAAAAAAAAAAAAAAAAHHHHH!!!!{/sc}{/b} "
                                " ...Riley skedaddled off because of what you said. "
                                " Come on, what you told her probably wasn't THAT bad...right??? "
                                " Well atleast Robby can work in peace now. "
                                hide robbyangry at bottom
                                show robbyneutral at right
                                " Robby looks a little flabbergasted at what you said. "
                                " He quickly regains his composure though, and gets back to working. "
                                show robbyneutral at center with move
                                rb " Well... atleast I don't have any disturbances now. "
                                rb " Not exactly what I was thinking in mind for you to get rid of her, but... "
                                rb " Thanks, I suppose? "
                                menu:
                                    " Help Robby with what he's working on ":
                                        $ robbrileylv += 10
                                        rb " Huh...? You wanna help out? "
                                        hide robbyneutral at bottom
                                        show robbyhappy at center
                                        rb " Well, if it means getting this done faster, then of course you can! "
                                        scene black with dissolve
                                        " You helped Robby with fixing Cubbie's toy. "
                                        " It took a bit, but eventually it looked as good as new! "
                                        " You've been so distracted by fixing it, you didn't notice that the bell had rang. "
                                        " Robby thanked you for your help, before you and him went to class together. "
                                        pause 2.0
                                        jump scienceclass1
                                    " Just chill with Robby for a bit " :
                                        $ robbrileylv += 5
                                        rb " Now, time to get back to work on this thing... "
                                        scene black with dissolve
                                        " You watched Robby fix one of Cubbie's toys, with you and him talking for a bit. "
                                        " You couldn't really help him fix what's been broken =, because you didn't know how to fix stuff like that. "
                                        " In your case, you'd probably make it look worse than it originally was. "
                                        " It took a bit for Robby to fix it, but eventually it looked as good as new!! "
                                        " The bell rang as soon as he finished making it, though. "
                                        " You got up and you headed off to your next class. "
                                        pause 2.0
                                        jump scienceclass1
                        " Let the girl continue ":
                            " You let the girl continue to yap and yap to Robby... "
                            " You could already feel bad for Robby's ears. Dealing with someone like this must be tiring... "
                            hide robbyangry at left with easeoutleft
                            " Eventually, Robby manages to sneak out whilst Riley was yapping and didn't notice him leaving. "
                            show rileyhappy at center with move
                            " Though, when she {i}did{/i} notice that he was gone, she started yapping to you instead. "
                            " You had to deal with this for the rest of the break. "
                            " You honestly weren't even listening and you were just looking around the cafeteria, looking for something that looked interesting. "
                            play sound "audio/bellring.mp3"
                            " Thankfully, the bell saves you from the yapping and you immediately skedaddled to your next class. "
                            " Not even saying bye to Riley, you just speedran out of the cafeteria and into your classroom. "
                            scene black with dissolve
                            pause 2.0
                            jump scienceclass1
                " Nah, probably not interesting. ":
                    " You still managed to hear what she was saying, due to how loud she was. "
                    " ...It was something about how she's someones girlfriend and wife forever. "
                    " That sounds familiar, doesn't it? "
                    " Wink wink nudge nudge to the sans, bendy, baldi fangirls back in the days. "
                    " It seemed to annoy Robby to the point of him yelling at her. "
                    " ...But, the girl just continued to yap and yap to him. "
                    " He very clearly looks annoyed that he can't get some peace....poor dude. "
                    " If I were that guy, I probably would've just left. "
                    " Too bad he has to deal with her for the rest of the break. "
                    play sound "audio/bellring.mp3"
                    " You sort of just chilled there until the bell rang. "
                    " Thankfully the guy can be left alone now... Probably. "
                    " You get up and you went to your next class. "
                    scene black with dissolve
                    pause 2.0
                    jump scienceclass1
        else:
            $ robbyknow = True
            $ rileyknow = True
            " You sat next to this odd looking boy and this strange looking girl... "
            " She was rambling about something whilst the boy was busy fixing something that apparently the girl had broken. "
            " Though, the girl seemed not to care and continued to talk. "
            " You're honestly starting to get a little more curious the more she's words she's spitting out... "
            " Though she's talking somehow a bit too fast for you to understand some of her words. "
            " Try to listen into what the girl's saying? "
            menu:
                " Sure, might be some drama ":
                    " You attempt to listen to what the girls saying... "
                    x " andthenimworkingonthisfanficofmeandoliver{nw} "
                    x " whereimoliversgirlfriendandwifeandwekissandlivehappilyeverafter{nw} "
                    x " butthenalicetriestotakehimawayfromme{nw} "
                    x " soibecomethealphaandtakehimbackbecausehesmypookiebear{nw} "
                    x " andhesmineforeverandever{nw} "
                    x " andeverandeverandeverandeverand{nw} "
                    hide robbyneutral at bottom
                    show robbyangry at left
                    x " OH MY GOD, RILEY! SHUT UP! "
                    x " I'm trying to work here, I'm trying to fix one of Cubbie's toys that YOU broke! "
                    x " Could you {i}PLEASE{/i} let me work in peace, "
                    x " Instead of YAPPING and YAPPING about OLIVER out of all people?! "
                    hide rileyneutral at bottom
                    show rileyhappy at right
                    ri " Sorry, can't hear youuuu~ "
                    ri " so then like (even more annoying yapping) "
                    x " Sigh... When will she ever stop... "
                    menu:
                        " Tell the girl to stop ":
                            " You kindly tell the girl to stop. "
                            " According to Robby's information, this girl REALLY likes Oliver. "
                            " What should you tell her? "
                            if kind == True:
                                menu:
                                    " hey so like you should probably be quiet otherwise oliver wont like you ":
                                        jump rileyok2
                                    " heyy if you keep talking oliver wont like you ":
                                        jump rileyok2
                                    " stop talking. ":
                                        jump rileyok2
                            elif mean == True:
                                menu:
                                    " yk oliver would hate you cause you yap too much ":
                                        jump rileyok2
                                    " js shut up you yappatron 6000 ffs ":
                                        jump rileyoh2
                                    " (your response here was censored because it was too rude) ":
                                        jump rileyoh2
                            elif calm == True:
                                menu:
                                    " yooo buddy you should probably stop cause olivers watching ":
                                        jump rileyok2
                                    " dudeee you should prolly stop ":
                                        jump rileyok2
                                    " can you stop bro ":
                                        jump rileyok2
                            label rileyok2:
                                hide rileyhappy at bottom
                                show rileyneutral at right
                                ri " ... "
                                ri " Fine... "
                                ri " Both of you are so boring! "
                                hide robbyangry at bottom
                                show robbyneutral at left
                                x " I just want to work in peace, Riley. "
                                x " You could go ahead and yap to someone else... "
                                x " Like Ruby. Wonder where she's at, now... "
                                x " Probably busy talking with Skell, or doing something else. "
                                x " Or you could go ahead and try to find Oliver. "
                                x " Heard he really wants to see you today. "
                                hide rileyneutral at bottom
                                show rileyhappy at right
                                ri " REALLY?! WHERE IS HE!!!!!! "
                                hide rileyhappy at left with easeoutleft
                                pause 0.5
                                hide robbyneutral at bottom
                                show robbyhappy at center with move
                                x " ...That always seems to get her, heh. "
                                x " Now I'll have no disturbances... "
                                menu:
                                    " Help Robby with what he's working on ":
                                        $ robbrileylv += 10
                                        hide robbyhappy at bottom
                                        show robbyneutral at center
                                        x " Huh...? You wanna help out? "
                                        hide robbyneutral at bottom
                                        show robbyhappy at center
                                        x " Well, if it means getting this done faster, then of course you can! "
                                        rb " The name's Robby, by the way. Glad to meet you. "
                                        rb " Let's get started! "
                                        scene black with dissolve
                                        " You helped Robby with fixing Cubbie's toy. "
                                        " It took a bit, but eventually it looked as good as new! "
                                        " You've been so distracted by fixing it, you didn't notice that the bell had rang. "
                                        " Robby thanked you for your help, before you and him went to class together. "
                                        pause 2.0
                                        jump scienceclass1
                                    " Just chill with Robby for a bit " :
                                        $ robbrileylv += 5
                                        x " Now, time to get back to work on this thing... "
                                        rb " Oh. [name]. Didn't really notice you there, uh... I'm Robby. "
                                        rb " Nice to meet you. "
                                        rb " If you need anything, I'll just be right here. "
                                        scene black with dissolve
                                        " You watched Robby fix one of Cubbie's toys, with you and him talking for a bit. "
                                        " You couldn't really help him fix what's been broken =, because you didn't know how to fix stuff like that. "
                                        " In your case, you'd probably make it look worse than it originally was. "
                                        " It took a bit for Robby to fix it, but eventually it looked as good as new!! "
                                        " The bell rang as soon as he finished making it, though. "
                                        " You got up and you headed off to your next class. "
                                        pause 2.0
                                        jump scienceclass1
                            label rileyoh2:
                                hide rileyhappy at bottom
                                show rileysad at right
                                ri " ... "
                                ri " ...Oh! That's not... "
                                hide rileysad at left with easeoutright
                                ri " {b}{sc}WAAAAAAAAAAAAAAAAAAAHHHHH!!!!{/sc}{/b} "
                                " ...Riley skedaddled off because of what you said. "
                                " Come on, what you told her probably wasn't THAT bad...right??? "
                                " Well atleast Robby can work in peace now. "
                                hide robbyangry at bottom
                                show robbyneutral at right
                                " the boy looks a little flabbergasted at what you said. "
                                " He quickly regains his composure though, and gets back to working. "
                                show robbyneutral at center with move
                                x " Well... atleast I don't have any disturbances now. "
                                x " Not exactly what I was thinking in mind for you to get rid of her, but... "
                                x " Thanks, I suppose? "
                                menu:
                                    " Help Robby with what he's working on ":
                                        $ robbrileylv += 10
                                        x " Huh...? You wanna help out? "
                                        hide robbyneutral at bottom
                                        show robbyhappy at center
                                        x " Well, if it means getting this done faster, then of course you can! "
                                        rb " The name's Robby, by the way. Glad to meet you. "
                                        rb " Let's get started! "
                                        scene black with dissolve
                                        " You helped Robby with fixing Cubbie's toy. "
                                        " It took a bit, but eventually it looked as good as new! "
                                        " You've been so distracted by fixing it, you didn't notice that the bell had rang. "
                                        " Robby thanked you for your help, before you and him went to class together. "
                                        pause 2.0
                                        jump scienceclass1
                                    " Just chill with Robby for a bit " :
                                        $ robbrileylv += 5
                                        rb " Now, time to get back to work on this thing... "
                                        rb " Oh. [name]. Didn't really notice you there, uh... I'm Robby. "
                                        rb " Nice to meet you. "
                                        rb " If you need anything, I'll just be right here. "
                                        scene black with dissolve
                                        " You watched Robby fix one of Cubbie's toys, with you and him talking for a bit. "
                                        " You couldn't really help him fix what's been broken =, because you didn't know how to fix stuff like that. "
                                        " In your case, you'd probably make it look worse than it originally was. "
                                        " It took a bit for Robby to fix it, but eventually it looked as good as new!! "
                                        " The bell rang as soon as he finished making it, though. "
                                        " You got up and you headed off to your next class. "
                                        pause 2.0
                                        jump scienceclass1
                        " Let the girl continue ":
                            " You let the girl continue to yap and yap to the boy... "
                            " You could already feel bad for Robby's ears. Dealing with someone like this must be tiring... "
                            hide robbyangry at left with easeoutleft
                            " Eventually, the boy manages to sneak out whilst Riley was yapping and didn't notice him leaving. "
                            show rileyhappy at center with move
                            " Though, when she {i}did{/i} notice that he was gone, she started yapping to you instead. "
                            " You had to deal with this for the rest of the break. "
                            " You honestly weren't even listening and you were just looking around the cafeteria, looking for something that looked interesting. "
                            play sound "audio/bellring.mp3"
                            " Thankfully, the bell saves you from the yapping and you immediately skedaddled to your next class. "
                            " Not even saying bye to Riley, you just speedran out of the cafeteria and into your classroom. "
                            scene black with dissolve
                            pause 2.0
                            jump scienceclass1
                " Nah, probably not interesting. ":
                    " You still managed to hear what she was saying, due to how loud she was. "
                    " ...It was something about how she's someones girlfriend and wife forever. "
                    " That sounds familiar, doesn't it? "
                    " Wink wink nudge nudge to the sans, bendy, baldi fangirls back in the days. "
                    " It seemed to annoy Robby to the point of him yelling at her. "
                    " ...But, the girl just continued to yap and yap to him. "
                    " He very clearly looks annoyed that he can't get some peace....poor dude. "
                    " If I were that guy, I probably would've just left. "
                    " Too bad he has to deal with her for the rest of the break. "
                    play sound "audio/bellring.mp3"
                    " You sort of just chilled there until the bell rang. "
                    " Thankfully the guy can be left alone now... Probably. "
                    " You get up and you went to your next class. "
                    scene black with dissolve
                    pause 2.0
                    jump scienceclass1
label rooftop2:
    scene rooftop with dissolve
    stop music fadeout 0.5
    " The rooftop... It's so quiet here. "
    " ...Though you could still hear the faint noises of students screaming and talking, "
    " No one really comes up here, so no one can bother you. "
    " And when there {i}are{/i} people up here, they'll justbe doing their own thing. "
    " It feels refreshing to have a short little break, doesn't it? "
    " You know, sometimes you should just take a breather just like what you're doing right now. "
    " And maybe even take a break from your device every once and awhile to get your thoughts sorted out. "
    " You don't have to pressure yourself into doing things you dont want to, either. "
    " Just have a breather and chillax, you know? "
    " Who knows, one day you might need it. "
    " You've been so lost in thought to the point that you didn't notice someone was standing next to you. "
    " They seem to be admiring the view, just like what you were doing moments ago. "
    " You turn your head around to get a better look at them... "
    show rubyneutral at center with dissolve
    if rubyknow == True:
        " It was Ruby. She was just looking at the sky, and everyone else who looked like they were having fun for the break. "
        " She then noticed that you were looking at her, and she spoke up. "
        ru " Oh, you've finally got out of your deep thinking! "
        ru " I've been standing and looking at you for a few minutes just trying to talk to you... "
        ru " I was gonna ask you about what you were thinking about... "
        ru " But, I decided not to. Since it's probably something personal. "
        hide rubyneutral at bottom
        show rubyhappy at center
        ru " That's why I just decided to chill with you for a bit! "
        hide rubyhappy at bottom
        show rubyneutral at center
        ru " ...{w=0.5} You know... "
        hide rubyneutral at bottom
        show rubyconfused at center
        ru " I wonder what it's like to be a human sometimes. "
        ru " Being some sort of robot thing is... I dunno how to explain it, really. "
        ru " Odd? I mean... Sure, there's a lot of people here that look weird, and I don't mean that in a bad way, but... "
        ru " It kinda just makes me feel a little out of place, you know? "
        ru " There's no other robot-like things around here except for...well, me. "
        ru " I just wanna feel how it's like to not get water splashed on your screen every few seconds. "
        ru " Do humans get that, too? "
        ru " ...I've seen it in movies, a few times. "
        ru " Humans are odd, but that's what make them more interesting, you get me? "
        hide rubyconfused at bottom
        show rubyneutral at center
        ru " ...{w=0.5} I'm sorry, I'm just going on one of my odd rambling sessions. "
        ru " I do that every now and then, when I have nothing else to talk about. "
        ru " Hope that I wasn't acting too weird... "
        menu:
            " Tell her that it's okay, and let her continue rambling. ":
                $ rubylv += 10
                hide rubyneutral at bottom
                show rubysurprised at center
                ru " ...? "
                ru " You'd really listen to my rambling? "
                ru " Are you certain? I can get a little... "
                hide rubysurprised at bottom
                show rubyneutral at center
                ru " ... Well, if you say that you're fine with it, then... "
                hide rubyneutral at bottom
                show rubyhappy at center
                ru " I'll be glad to start rambling all my thoughts and ideas to you! "
                scene black with dissolve
                " You spent the rest of the break talking to Ruby. "
                " You listened to all of her thoughts, of course, some of them were a bit... interesting, to say the least. "
                " But, most of them were good and happy thoughts. "
                play sound "audio/bellring.mp3"
                " Eventually, the bell rings whilst Ruby was in the middle of her yapping session. "
                " After a bit more yapping, you and Ruby walk together to the classroom for the next class. "
                pause 2.0
                jump scienceclass1
            " Tell her that it's okay. ":
                $ rubylv += 5
                ru " ...Anywho, we should probably get to class early. "
                ru " It's better to be early rather than late, you know! "
                hide rubyneutral at bottom
                show rubyhappy at center
                ru " I'll go ahead and I'll see you in class, [name]! "
                hide rubyhappy at right with easeoutright
                menu:
                    " Go to class early ":
                        scene black with dissolve
                        " You followed Ruby shortly after she had left to go to class early. "
                        " You don't know how the teacher would react if you got late to their class... "
                        " And you don't want to know, either. Judging from what you've heard about this school. "
                        pause 2.0
                        play music "audio/paperhigh.mp3" fadein 0.5
                        jump scienceclass1
                    " Stay here for a bit ":
                        scene black with dissolve
                        " You stayed on the rooftop for a bit longer. "
                        " You got a bit late to your class, but the teacher let it slide since it's your first day here. "
                        play music "audio/paperhigh.mp3" fadein 0.5
                        pause 2.0
                        jump scienceclass1
    else:
        " It was a girl with a TV for a head, and had some pretty colorful accessories on her. "
        " She was just looking at the sky, and everyone else who looked like they were having fun for the break. "
        " She then noticed that you were looking at her, and she spoke up. "
        x " Oh, you've finally got out of your deep thinking! "
        x " I've been standing and looking at you for a few minutes just trying to talk to you... "
        x " I was gonna ask you about what you were thinking about... "
        x " But, I decided not to. Since it's probably something personal. "
        hide rubyneutral at bottom
        show rubyhappy at center
        x " That's why I just decided to chill with you for a bit! "
        hide rubyhappy at bottom
        show rubyneutral at center
        x " Wait, hold on... "
        x " I haven't introduced myself yet, I must look like a creep, sorry... "
        hide rubyneutral at bottom
        show rubyhappy at center
        $ rubyknow = True
        ru " I'm Ruby! Glad to meet you! "
        ru " I've been wanting to be friends with you for a bit, ehe... "
        hide rubyhappy at bottom
        show rubyneutral at center
        " There was some awkward silence between you two. "
        " I mean, you can't really talk. The only times you do is when you pick the options in this game. "
        " No, I'm not adding an option for you to talk here. "
        " Why? you STINK "
        ru " ...I'm gonna try to think about something to talk about real quick... "
        ru " Hmmmm... "
        ru " ...{w=0.5} You know... "
        hide rubyneutral at bottom
        show rubyconfused at center
        ru " I wonder what it's like to be a human sometimes. "
        ru " Being some sort of robot thing is... I dunno how to explain it, really. "
        ru " Odd? I mean... Sure, there's a lot of people here that look weird, and I don't mean that in a bad way, but... "
        ru " It kinda just makes me feel a little out of place, you know? "
        ru " There's no other robot-like things around here except for...well, me. "
        ru " I just wanna feel how it's like to not get water splashed on your screen every few seconds. "
        ru " Do humans get that, too? "
        ru " ...I've seen it in movies, a few times. "
        ru " Humans are odd, but that's what make them more interesting, you get me? "
        hide rubyconfused at bottom
        show rubyneutral at center
        ru " ...{w=0.5} I'm sorry, I'm just going on one of my odd rambling sessions. "
        ru " I do that every now and then, when I have nothing else to talk about. "
        ru " Hope that I wasn't acting too weird... "
        menu:
            " Tell her that it's okay, and let her continue rambling. ":
                $ rubylv += 10
                hide rubyneutral at bottom
                show rubysurprised at center
                ru " ...? "
                ru " You'd really listen to my rambling? "
                ru " Are you certain? I can get a little... "
                hide rubysurprised at bottom
                show rubyneutral at center
                ru " ... Well, if you say that you're fine with it, then... "
                hide rubyneutral at bottom
                show rubyhappy at center
                ru " I'll be glad to start rambling all my thoughts and ideas to you! "
                scene black with dissolve
                " You spent the rest of the break talking to Ruby. "
                " You listened to all of her thoughts, of course, some of them were a bit... interesting, to say the least. "
                " But, most of them were good and happy thoughts. "
                play sound "audio/bellring.mp3"
                " Eventually, the bell rings whilst Ruby was in the middle of her yapping session. "
                " After a bit more yapping, you and Ruby walk together to the classroom for the next class. "
                pause 2.0
                play music "audio/paperhigh.mp3" fadein 0.5
                jump scienceclass1
            " Tell her that it's okay. ":
                $ rubylv += 5
                ru " ...Anywho, we should probably get to class early. "
                ru " It's better to be early rather than late, you know! "
                hide rubyneutral at bottom
                show rubyhappy at center
                ru " I'll go ahead and I'll see you in class, [name]! "
                hide rubyhappy at right with easeoutright
                menu:
                    " Go to class early ":
                        scene black with dissolve
                        " You followed Ruby shortly after she had left to go to class early. "
                        " You don't know how the teacher would react if you got late to their class... "
                        " And you don't want to know, either. Judging from what you've heard about this school. "
                        pause 2.0
                        play music "audio/paperhigh.mp3" fadein 0.5
                        jump scienceclass1
                    " Stay here for a bit ":
                        scene black with dissolve
                        " You stayed on the rooftop for a bit longer. "
                        " You got a bit late to your class, but the teacher let it slide since it's your first day here. "
                        pause 2.0
                        play music "audio/paperhigh.mp3" fadein 0.5
                        jump scienceclass1

label library2:
    scene library with dissolve
    " The library was as calm and quiet as per usual. "
    " No disturbances, no one yelling... "
    " You always thought it was nice whenever you visited libraries because they're all quiet. "
    " Or you never even visited a library before and are just imagining that you've went to one. "
    " You could see a few people reading their books, on the ground or on the tables. "
    " Only a few people ever go here, because some people think that reading books are for nerds. "
    " Well, not really. Not all people who like books are nerds. "
    if mean == True and clairebeatup == True:
        " You roam around for a bit, and you spot someone familiar reading a book... "
        show claireneutral at center with dissolve
        " It was Claire. Seems like she's focused on the book she's reading on... "
        " Would you like to sit next to her? "
        menu:
            " Sure! ":
                " You walked over to Claire and you sat next to her. "
                " Wondering what she's reading, you took a closer look on the books pages... "
                " Seems like she was reading a book about space. Interesting... "
                " It didn't take long for her to notice that you were there. "
                c " Oh! Hey there, [name]! "
                c " Just reading a book about space, is all. I know, a little boring... "
                hide claireneutral at bottom
                show clairehappy at center
                c " But I think space is pretty cool! "
                c " There's just so many things that we haven't explored or seen yet, "
                c " It all just makes me want to learn more and more! "
                hide clairehappy at bottom
                show claireneutral at center
                c " Oh, yeah, right! I've read about this thing called a 'GravaStar'! "
                c " I don't really see anyone talk about it, but it's basically like a black hole! "
                c " Of course, the both of them are way, way different, but I still think that they're cool! "
                c " There's also these cool little constellations, my only question is that why the pegasus one looks like a hand... "
                c " Oh well! "
                c " Anywho, would you like to read with me for the time being? "
                menu:
                    " Hang out with Claire ":
                        $ clairelv += 10
                        hide claireneutral at bottom
                        show clairehappy at center
                        c " Alrighty! "
                        hide clairehappy at bottom
                        show claireneutral at center
                        c " Though, fair warning... I might yap a bit too much. Is that alright? "
                        c " You can stop me from yapping anytime you want, if it's getting too much for you. "
                        " You tell Claire that it's alright and you start reading with her and listening to her yap and yap. "
                        scene black with dissolve
                        " You spent the rest of your break reading a book about space with Claire. "
                        " Claire was being sort of a yapfest, but you're cool with that. "
                        " After all, you probably become a yapfest yourself when someone mentions your fandom. "
                        " Probably. And you also probably have little ocs you made for that fandom that you like. "
                        " Don't worry, me too. "
                        play sound "audio/bellring.mp3"
                        " The bell rings in the middle of Claire yapping, and you both get up to go to the next class. "
                        " Claire returns the book, and off the both of you went to the classroom. "
                        pause 2.0
                        jump scienceclass1
                    " Nah I'll just chill with you ":
                        c " That's fine, then. "
                        hide claireneutral at bottom
                        show clairehappy at center
                        c " If you need anything, you can ask me for stuff! "
                        hide clairehappy at bottom
                        show claireneutral at center
                        c " Though, I might be too busy reading, ehe... "
                        scene black with dissolve
                        " You spent the rest of the day chilling around with Claire. "
                        " You could hear her being a yapfest to herself about some stuff in the book, but that's alright. "
                        " After all, you probably become a yapfest yourself when someone mentions your fandom. "
                        " Probably. And you also probably have little ocs you made for that fandom that you like. "
                        " Don't worry, me too. "
                        play sound "audio/bellring.mp3"
                        " The bell rings in the middle of Claire yapping, and you both get up to go to the next class. "
                        " Claire returns the book, and off the both of you went to the classroom. "
                        pause 2.0
                        jump scienceclass1
                        pause 2.0
                        jump scienceclass1
            " No thanks ":
                " You decided not to sit next to Claire, as to not disturb her reading. "
                " You just decided to roam around the library for a bit, looking at books here and there... "
                " There were some that caught your attention but you only read up to 5 or 10 pages before you put them back into their place. "
                " You didn't really find anything else interesting, though. "
                " You just sit in one of the corners and just...think for a bit. "
                play sound "audio/bellring.mp3"
                " The bell snaps you out of your thinking session before you could get too deep into your thinking, though. "
                " You get up from the ground, dusted yourself off and you get up to go to the next class. "
                scene black with dissolve
                pause 2.0
                jump scienceclass1
    elif mean == True and clairebeatup == False:
        " You roam around for a bit, and you spot someone familiar reading a book... "
        " It was Claire. I don't think that she'd be too happy to se you right now. Or at all. "
        " The moment she notices you that you're there, she just moves herself to another spot, far away from you. "
        " Damn... all that just for you beating her up? jeez. "
        " You could've honestly done worse than what you did earlier, so you didn't really understand why she was acting this way. "
        " But, oh well. Not like you could change how people react to how you treat them. "
        scene black with dissolve
        " You just leave her alone and decide to leave the library to do something else. "
        " You decided to take a walk around the school for a bit, since you were bored and had nothing else to do. "
        " You could feel a few students staring at you, but you didn't really care. "
        " You're the alpha, after all. "
        " ...im sorry that was so horrible{nw} "
        play sound "audio/bellring.mp3"
        " After a bit of walking down the hallways, the bell rings. "
        " You then start making your way back to your classroom for the next class. "
        pause 2.0
        jump scienceclass1
    else:
        " You roam around for a bit, and you spot someone familiar reading a book... "
        show claireneutral at center with dissolve
        " It was Claire. Seems like she's focused on the book she's reading on... "
        " Would you like to sit next to her? "
        menu:
            " Sure! ":
                " You walked over to Claire and you sat next to her. "
                " Wondering what she's reading, you took a closer look on the books pages... "
                " Seems like she was reading a book about space. Interesting... "
                " It didn't take long for her to notice that you were there. "
                c " Oh! Hey there, [name]! "
                c " Just reading a book about space, is all. I know, a little boring... "
                hide claireneutral at bottom
                show clairehappy at center
                c " But I think space is pretty cool! "
                c " There's just so many things that we haven't explored or seen yet, "
                c " It all just makes me want to learn more and more! "
                hide clairehappy at bottom
                show claireneutral at center
                c " Oh, yeah, right! I've read about this thing called a 'GravaStar'! "
                c " I don't really see anyone talk about it, but it's basically like a black hole! "
                c " Of course, the both of them are way, way different, but I still think that they're cool! "
                c " There's also these cool little constellations, my only question is that why the pegasus one looks like a hand... "
                c " Oh well! "
                c " Anywho, would you like to read with me for the time being? "
                menu:
                    " Hang out with Claire ":
                        $ clairelv += 10
                        hide claireneutral at bottom
                        show clairehappy at center
                        c " Alrighty! "
                        hide clairehappy at bottom
                        show claireneutral at center
                        c " Though, fair warning... I might yap a bit too much. Is that alright? "
                        c " You can stop me from yapping anytime you want, if it's getting too much for you. "
                        " You tell Claire that it's alright and you start reading with her and listening to her yap and yap. "
                        scene black with dissolve
                        " You spent the rest of your break reading a book about space with Claire. "
                        " Claire was being sort of a yapfest, but you're cool with that. "
                        " After all, you probably become a yapfest yourself when someone mentions your fandom. "
                        " Probably. And you also probably have little ocs you made for that fandom that you like. "
                        " Don't worry, me too. "
                        play sound "audio/bellring.mp3"
                        " The bell rings in the middle of Claire yapping, and you both get up to go to the next class. "
                        " Claire returns the book, and off the both of you went to the classroom. "
                        pause 2.0
                        jump scienceclass1
                    " Nah I'll just chill with you ":
                        c " That's fine, then. "
                        hide claireneutral at bottom
                        show clairehappy at center
                        c " If you need anything, you can ask me for stuff! "
                        hide clairehappy at bottom
                        show claireneutral at center
                        c " Though, I might be too busy reading, ehe... "
                        scene black with dissolve
                        " You spent the rest of the day chilling around with Claire. "
                        " You could hear her being a yapfest to herself about some stuff in the book, but that's alright. "
                        " After all, you probably become a yapfest yourself when someone mentions your fandom. "
                        " Probably. And you also probably have little ocs you made for that fandom that you like. "
                        " Don't worry, me too. "
                        play sound "audio/bellring.mp3"
                        " The bell rings in the middle of Claire yapping, and you both get up to go to the next class. "
                        " Claire returns the book, and off the both of you went to the classroom. "
                        pause 2.0
                        jump scienceclass1
                        pause 2.0
                        jump scienceclass1
            " No thanks ":
                " You decided not to sit next to Claire, as to not disturb her reading. "
                " You just decided to roam around the library for a bit, looking at books here and there... "
                " There were some that caught your attention but you only read up to 5 or 10 pages before you put them back into their place. "
                " You didn't really find anything else interesting, though. "
                " You just sit in one of the corners and just...think for a bit. "
                play sound "audio/bellring.mp3"
                " The bell snaps you out of your thinking session before you could get too deep into your thinking, though. "
                " You get up from the ground, dusted yourself off and you get up to go to the next class. "
                scene black with dissolve
                pause 2.0
                jump scienceclass1
label scienceclass1:
    scene classroom with dissolve
    show missbloomieneutral at center with easeinright
    msb " Alrighty, class. Today we'll be having a quiz. "
    msb " Don't worry, since I'm being 'nice' today, I'll be giving out an easier quiz for all of you. "
    hide missbloomieneutral at left with easeoutleft
    " Miss bloomie then proceeds to hand out papers to you and your classmates. "
    " Alright, time to get answering. "
    " What is the primary force that keeps planets in orbit around the Sun? "
    menu:
        " Electromagnetic Force ":
            " Alright, I think that's the answer... "
            jump ques2
        " Gravitational Force ":
            $ sciencetest += 1
            " Alright, I think that's the answer... "
            jump ques2
        " Nuclear Force ":
            " Alright, I think that's the answer... "
            jump ques2
    label ques2:
        " What is the chemical formula for table salt? "
        menu:
            " NaCl ":
                $ sciencetest += 1
                " Alright, I think that's the answer... "
                jump ques3
            " H2O ":
                " Alright, I think that's the answer... "
                jump ques3
            " CO2 ":
                " Alright, I think that's the answer... "
                jump ques3
        label ques3:
            " What is the powerhouse of the cell? "
            menu:
                " Mitochondria ":
                    $ sciencetest += 1
                    " Alright, I think that's the answer... "
                    jump ques4
                " Nucleus ":
                    " Alright, I think that's the answer... "
                    jump ques4
                " Ribosome ":
                    " Alright, I think that's the answer... "
                    jump ques4
            label ques4:
                " What galaxy do we live in? "
                menu:
                    " Whirlpool ":
                        " Alright, I think that's the answer... "
                        jump ques5
                    " Andromeda ":
                        " Alright, I think that's the answer... "
                        jump ques5
                    " Milkyway ":
                        $ sciencetest += 1
                        " Alright, I think that's the answer... "
                        jump ques5
                label ques5:
                    " Final question: What layer of the earth is responsible for tectonic plate movement? "
                    menu:
                        " Crust ":
                            " Alright, we're done. "
                            jump final
                        " Mantle ":
                            $ sciencetest += 1
                            " Alright, we're done. "
                            jump final
                        " Core ":
                            " Alright, we're done. "
                            jump final
label final:
    show missbloomieneutral at center with easeinleft
    msb " Time's up. I'll be getting all of your test papers, finished or unfinished. "
    hide missbloomieneutral at left with easeoutleft
    pause 5.5
    show missbloomieneutral at center with easeinleft
    msb " I've gotten and graded all of your papers. "
    if sciencetest == 5:
        msb " I'd like to congratulate [name] for getting the highest score for this quiz. "
        msb " Congratulations, you're not stupid. "
        msb " Class is dismissed. "
        scene black with dissolve
        " You then went outside the hallway so that you could explore the school once again. "
        pause 2.0
        jump break3
    elif sciencetest <= 5:
        msb " I'd like to congratulate Engel for getting the highest score on this quiz. "
        msb " You should all be more like him and start improving your grades. "
        msb " Class is dismissed. "
        scene black with dissolve
        " You then went outside the hallway so that you could explore the school once again. "
        pause 2.0
        jump break3
    elif sciencetest == 1:
        msb " I'd like to congratulate Engel for getting the highest score on this quiz. "
        msb " You should all be more like him and start improving your grades. "
        msb " Of course, there are some that have failed this test... somehow. "
        msb " I'll have to ask everyone but [name] to leave the class. "
        stop music fadeout 0.5
        " You watch everyone leave the class as you stay in your seat. "
        hide missbloomieneutral at bottom
        show missbloomieangry at center
        msb " ... "
        scene black with vpunch
        " ...She basically turned you from a one whole sheet of paper to a one half. "
        " Seriously, how could you get a score of {i}1{/i} on a simple test as that... "
        " You probably just wanted to see what would happen if you failed, didn't you. "
        " Well, since I'm nice enough, I'll give you the chance to retry. "
        menu:
            " Retry ":
                " Be serious this time. "
                jump testretry
            " Go back to menu ":
                return
    elif sciencetest == 0:
        msb " I'd like to congratulate Engel for getting the highest score on this quiz. "
        msb " You should all be more like him and start improving your grades. "
        msb " Of course, there are some that have failed this test... somehow. "
        msb " I'll have to ask everyone but [name] to leave the class. "
        stop music fadeout 0.5
        " You watch everyone leave the class as you stay in your seat. "
        hide missbloomieneutral at bottom
        show missbloomieangry at center
        msb " ... "
        scene black with vpunch
        " ...She basically turned you from a one whole sheet of paper to a one half. "
        " Seriously, how could you get a score of {i}0{/i} on a simple test as that... "
        " You probably just wanted to see what would happen if you failed, didn't you. "
        " Well, since I'm nice enough, I'll give you the chance to retry. "
        menu:
            " Retry ":
                " Be serious this time. "
                jump testretry
            " Go back to menu ":
                return
label testretry:
    play music "audio/paperhigh.mp3" fadein 0.5
    $ sciencetest = 0
    scene classroom with dissolve
    show missbloomieneutral at center with easeinright
    msb " Alrighty, class. Today we'll be having a quiz. "
    msb " Don't worry, since I'm being 'nice' today, I'll be giving out an easier quiz for all of you. "
    hide missbloomieneutral at left with easeoutleft
    " Miss bloomie then proceeds to hand out papers to you and your classmates. "
    " Alright, time to get answering. "
    " What is the primary force that keeps planets in orbit around the Sun? "
    menu:
        " Electromagnetic Force ":
            " Alright, I think that's the answer... "
            jump ques2ret
        " Gravitational Force ":
            $ sciencetest += 1
            " Alright, I think that's the answer... "
            jump ques2ret
        " Nuclear Force ":
            " Alright, I think that's the answer... "
            jump ques2ret
    label ques2ret:
        " What is the chemical formula for table salt? "
        menu:
            " NaCl ":
                $ sciencetest += 1
                " Alright, I think that's the answer... "
                jump ques3ret
            " H2O ":
                " Alright, I think that's the answer... "
                jump ques3ret
            " CO2 ":
                " Alright, I think that's the answer... "
                jump ques3ret
        label ques3ret:
            " What is the powerhouse of the cell? "
            menu:
                " Mitochondria ":
                    $ sciencetest += 1
                    " Alright, I think that's the answer... "
                    jump ques4ret
                " Nucleus ":
                    " Alright, I think that's the answer... "
                    jump ques4ret
                " Ribosome ":
                    " Alright, I think that's the answer... "
                    jump ques4ret
            label ques4ret:
                " What galaxy do we live in? "
                menu:
                    " Whirlpool ":
                        " Alright, I think that's the answer... "
                        jump ques5ret
                    " Andromeda ":
                        " Alright, I think that's the answer... "
                        jump ques5ret
                    " Milkyway ":
                        $ sciencetest += 1
                        " Alright, I think that's the answer... "
                        jump ques5ret
                label ques5ret:
                    " Final question: What layer of the earth is responsible for tectonic plate movement? "
                    menu:
                        " Crust ":
                            " Alright, we're done. "
                            jump finalret
                        " Mantle ":
                            $ sciencetest += 1
                            " Alright, we're done. "
                            jump finalret
                        " Core ":
                            " Alright, we're done. "
                            jump finalret
label finalret:
    show missbloomieneutral at center with easeinleft
    msb " Time's up. I'll be getting all of your test papers, finished or unfinished. "
    hide missbloomieneutral at left with easeoutleft
    pause 5.5
    show missbloomieneutral at center with easeinleft
    msb " I've gotten and graded all of your papers. "
    if sciencetest == 5:
        msb " I'd like to congratulate [name] for getting the highest score for this quiz. "
        msb " Congratulations, you're not stupid. "
        msb " Class is dismissed. "
        scene black with dissolve
        " You then went outside the hallway so that you could explore the school once again. "
        pause 2.0
        jump break3
    elif sciencetest <= 5:
        msb " I'd like to congratulate Engel for getting the highest score on this quiz. "
        msb " You should all be more like him and start improving your grades. "
        msb " Class is dismissed. "
        scene black with dissolve
        " You then went outside the hallway so that you could explore the school once again. "
        pause 2.0
        jump break3
    elif sciencetest == 1:
        msb " I'd like to congratulate Engel for getting the highest score on this quiz. "
        msb " You should all be more like him and start improving your grades. "
        msb " Of course, there are some that have failed this test... somehow. "
        msb " I'll have to ask everyone but [name] to leave the class. "
        stop music fadeout 0.5
        " You watch everyone leave the class as you stay in your seat. "
        hide missbloomieneutral at bottom
        show missbloomieangry at center
        msb " ... "
        scene black with vpunch
        " ...She basically turned you from a one whole sheet of paper to a one half. "
        " Dude, I gave you a second chance. How the hell did you fumble so badly? "
        " You could've even used google here... "
        " You probably just wanted to see what would happen if you failed again, didn't you. "
        " And since I'm NOT nice enough to give you a retry, I'm sending you straight to the menu. "
        " See you later buddy{nw} "
        return
    elif sciencetest == 0:
        msb " I'd like to congratulate Engel for getting the highest score on this quiz. "
        msb " You should all be more like him and start improving your grades. "
        msb " Of course, there are some that have failed this test... somehow. "
        msb " I'll have to ask everyone but [name] to leave the class. "
        stop music fadeout 0.5
        " You watch everyone leave the class as you stay in your seat. "
        hide missbloomieneutral at bottom
        show missbloomieangry at center
        msb " ... "
        scene black with vpunch
        " ...She basically turned you from a one whole sheet of paper to a one half. "
        " Dude, I gave you a second chance. How the hell did you fumble so badly? "
        " You could've even used google here... "
        " You probably just wanted to see what would happen if you failed again, didn't you. "
        " And since I'm NOT nice enough to give you a retry, I'm sending you straight to the menu. "
        " See you later buddy{nw} "
        return
label break3:
    scene hallway with dissolve
    " Where do you want to go this time? "
    menu:
        " {image=abbieicon} Front of the school {image=abbieicon} ":
            scene black with dissolve
            pause 2.0
            jump frontschool3
        " {image=skellicon} Back of the school {image=rubyicon} ":
            scene black with dissolve
            pause 2.0
            jump backschool3
        " {image=engelicon} The gym {image=bubbleicon} ":
            scene black with dissolve
            pause 2.0
            jump gym3
        " The cafeteria ":
            scene black with dissolve
            pause 2.0
            jump cafe3
        " {image=rileyicon} The rooftop {image=lanaicon} ":
            scene black with dissolve
            pause 2.0
            jump rooftop3
        " {image=kevinicon} The library {image=robbyicon} ":
            scene black with dissolve
            pause 2.0
            jump library3
    label frontschool3:
        scene paperschoolfront with dissolve
        stop music fadeout 0.5
        " A step outside, and you could already hear some arguing. "
        " Curious, you decide to eavesdrop a little on the conversation. "
        show zipangry at left with easeinleft
        show abbiesad at right with easeinright
        x " You little prick - You got Oliver suspended until wednesday! "
        if abbieknow == True:
            a " I'm...I'm sorry... "
            a " I didn't... mean to... "
            x " Bullshit! " with vpunch
            x " We weren't even doing anything wrong, it's not like we were trying to KILL you! "
            x " If he could, Oliver would've snapped your neck right then and there! "
            x " You're lucky I can't do shit right now, the teachers have their eyes on me and Edward for the day. "
            x " I would've LOVED to break your limbs right now. But too bad, I can't. "
            x " Not like you'll need them anyway, you can't even do anything useful. "
            x " You're nothing but a piece of garbage trying to fit in with society. "
            x " It would've been better if you killed yourself. No one would even notice that you were gone. "
            hide zipangry at bottom
            show zipneutral at left
            x " Don't worry, I'll go to your funeral! "
            x " ..To absolutely just trash your grave. You think I'd actually pay respects to you? "
            x " HAH! In your dreams! "
            x " Get out of the way, loser. "
            hide zipneutral at right with easeoutright
            show abbiesad at center with move
            a " ...*sniff*... "
            menu:
                " Go up to him ":
                    a " ...Why... "
                    a " ...Why do I...always have to be such a crybaby... "
                    a " I just wish...I could fight back someday...But I-I... "
                    a " I-I can't...I'm too...*sniff*...I'm too weak... "
                    a " I could hardly get a punch into Oliver's group... "
                    a " I can't even bring myself to hurt a fly... "
                    a " What's...what's wrong with me...? "
                    menu:
                        " Nothings wrong with you, you're perfectly fine the way you are ":
                            a " ...Really..? "
                            a " I don't...Don't think so... "
                            a " I can't fight back... "
                            a " How can I be fine when I'm just a walking punching bag for everyone else around me...? "
                            a " How can I be fine when even if I try to stand up for myself, I'll end up looking more of a fool...? "
                            a " I just... I-I just don't get it... "
                            a " It's all so...so...so unfair... "
                            hide abbiesad at left with easeoutleft
                            " ...Abbie ran away. "
                            " Poor kid... "
                            " If only you could do something to help him. "
                            " Something to give him more confidence in himself... "
                            if abbielv >= 10:
                                $ abbiehelp = True
                                " You have an idea. "
                                " You can help him tomorrow. "
                            elif abbielv == 10:
                                $ abbiehelp = True
                                " You have an idea. "
                                " You can help him tomorrow. "
                            else:
                                $ abbiehelp = False
                                " You did have an idea, but you quickly threw it out of your mind. "
                                " It wouldn't really work, anyway.. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, and you go to your next class. "
                            scene black with dissolve
                            pause 2.0
                            play music "audio/paperhigh.mp3" fadein 0.5
                            jump historyclass1
                        " It's all gonna be over in the end ":
                            a " But...But what if it isn't...? "
                            a " I don't think this will end, ever... "
                            a " I'm just gonna be a walking punching bag for everyone near me, for my entire life... "
                            a " There's no use in trying to change what's destined for me... "
                            a " I'll just be...as weak as I always am... "
                            a " Life is just...so..so..unfair... "
                            hide abbiesad at left with easeoutleft
                            " ...Abbie ran away. "
                            " Poor kid... "
                            " If only you could do something to help him. "
                            " Something to give him more confidence in himself... "
                            if abbielv >= 10:
                                " You have an idea. "
                                " You can help him tomorrow. "
                            elif abbielv == 10:
                                " You have an idea. "
                                " You can help him tomorrow. "
                            else:
                                " You did have an idea, but you quickly threw it out of your mind. "
                                " It wouldn't really work, anyway.. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, and you go to your next class. "
                            scene black with dissolve
                            pause 2.0
                            play music "audio/paperhigh.mp3" fadein 0.5
                            jump historyclass1
                " Act like nothing happened ":
                    " You left Abbie there to cry like a baby. "
                    " You would've done something, but you didn't have the balls to. "
                    " Or you just picked this option to see what would happen. "
                    " Anywho, Abbie's still sad, and you went back into the school to do your own stuff. "
                    scene black with dissolve
                    " You kinda just roamed around school... there wasn't anything to do, really. "
                    " You could see the same girl who talked shit about Abbie earlier bullying another student. "
                    " Oh, how you wanted to break every bone in her body... "
                    " But alas, you'd get your ass beaten by the teachers. Only if they caught you, that is. "
                    " That's still gonna be hard if you try to, since theres security cameras in this school. "
                    " ...Wait, hey... how does Oliver's group even get away with such things? "
                    " Man, you're starting to question how this school works. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, and you go to your next class. "
                    pause 2.0
                    jump historyclass1
        else:
            x " I'm...I'm sorry... "
            x " I didn't... mean to... "
            x " Bullshit! " with vpunch
            x " We weren't even doing anything wrong, it's not like we were trying to KILL you! "
            x " If he could, Oliver would've snapped your neck right then and there! "
            x " You're lucky I can't do shit right now, the teachers have their eyes on me and Edward for the day. "
            x " I would've LOVED to break your limbs right now. But too bad, I can't. "
            x " Not like you'll need them anyway, you can't even do anything useful. "
            x " You're nothing but a piece of garbage trying to fit in with society. "
            x " It would've been better if you killed yourself. No one would even notice that you were gone. "
            hide zipangry at bottom
            show zipneutral at left
            x " Don't worry, I'll go to your funeral! "
            x " ..To absolutely just trash your grave. You think I'd actually pay respects to you? "
            x " HAH! In your dreams! "
            x " Get out of the way, loser. "
            hide zipneutral at right with easeoutright
            show abbiesad at center with move
            x " ...*sniff*... "
            menu:
                " Go up to him ":
                    x " ...Why... "
                    x " ...Why do I...always have to be such a crybaby... "
                    x " I just wish...I could fight back someday...But I-I... "
                    x " I-I can't...I'm too...*sniff*...I'm too weak... "
                    x " I could hardly get a punch into Oliver's group... "
                    x " I can't even bring myself to hurt a fly... "
                    x " What's...what's wrong with me...? "
                    menu:
                        " Nothings wrong with you, you're perfectly fine the way you are ":
                            x " ...Really..? "
                            x " I don't...Don't think so... "
                            x " I can't fight back... "
                            x " How can I be fine when I'm just a walking punching bag for everyone else around me...? "
                            x " How can I be fine when even if I try to stand up for myself, I'll end up looking more of a fool...? "
                            x " I just... I-I just don't get it... "
                            x " It's all so...so...so unfair... "
                            hide abbiesad at left with easeoutleft
                            " ...He ran away. "
                            " Poor kid... "
                            " If only you could do something to help him. "
                            " Something to give him more confidence in himself... "
                            if abbielv >= 10:
                                " You have an idea. "
                                " You can help him tomorrow. "
                            elif abbielv == 10:
                                " You have an idea. "
                                " You can help him tomorrow. "
                            else:
                                " You did have an idea, but you quickly threw it out of your mind. "
                                " It wouldn't really work, anyway.. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, and you go to your next class. "
                            scene black with dissolve
                            pause 2.0
                            play music "audio/paperhigh.mp3" fadein 0.5
                            jump historyclass1
                        " It's all gonna be over in the end ":
                            x " But...But what if it isn't...? "
                            x " I don't think this will end, ever... "
                            x " I'm just gonna be a walking punching bag for everyone near me, for my entire life... "
                            x " There's no use in trying to change what's destined for me... "
                            x " I'll just be...as weak as I always am... "
                            x " Life is just...so..so..unfair... "
                            hide abbiesad at left with easeoutleft
                            " ...He ran away. "
                            " Poor kid... "
                            " If only you could do something to help him. "
                            " Something to give him more confidence in himself... "
                            if abbielv >= 10:
                                " You have an idea. "
                                " You can help him tomorrow. "
                            elif abbielv == 10:
                                " You have an idea. "
                                " You can help him tomorrow. "
                            else:
                                " You did have an idea, but you quickly threw it out of your mind. "
                                " It wouldn't really work, anyway.. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, and you go to your next class. "
                            scene black with dissolve
                            pause 2.0
                            play music "audio/paperhigh.mp3" fadein 0.5
                            jump historyclass1
                " Act like nothing happened ":
                    " You left the boy there to cry like a baby. "
                    " You would've done something, but you didn't have the balls to. "
                    " Or you just picked this option to see what would happen. "
                    " Anywho, the guy's still sad, and you went back into the school to do your own stuff. "
                    scene black with dissolve
                    " You kinda just roamed around school... there wasn't anything to do, really. "
                    " You could see the same girl who talked shit about Abbie earlier bullying another student. "
                    " Oh, how you wanted to break every bone in her body... "
                    " But alas, you'd get your ass beaten by the teachers. Only if they caught you, that is. "
                    " That's still gonna be hard if you try to, since theres security cameras in this school. "
                    " ...Wait, hey... how does Oliver's group even get away with such things? "
                    " Man, you're starting to question how this school works. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, and you go to your next class. "
                    pause 2.0
                    jump historyclass1
    label backschool3:
        scene paperschoolback with dissolve
        # skell and ruby
        if skellknow == True:
            " You went back to the back of the school, and you see Skell there again. "
            " This time, he seemed to be talking with a girl... "
            if rubyknow == True:
                " A girl you've seen before...Is that Ruby? "
                " You should go up to them and see what they're talking about. "
                show skellneutral at left with easeinright
                show rubyneutral at right with easeinright
                sk " So... you remembered anything about the history thing? "
                ru " Actually, Skelly, we didn't have anything to do in history, if that's what you're asking. "
                ru " Remember, last friday it was only a lecture! "
                sk " Ah, alright, then... thanks for reminding me. "
                " Skell was about to leave, but he notices you standing there. "
                sk " Oh, hey, [name]... "
                ru " You know [them] too? "
                sk " Yep. We met once while it was breaktime and we just sorta....relaxed. "
                hide rubyneutral at bottom
                show rubyhappy at right
                ru " Ouuhh!! That's nice, then! "
                ru " I'm glad that you're getting more friends, Skelly! You're doing so great! "
                sk " ... "
                hide rubyhappy at bottom
                show rubyneutral at right
                ru " Anyway...Zip and Edward seem to be a little more...angry today. "
                sk " Oh? and why is that? "
                ru " According to my research, Oliver got suspended until wednesday due to him almost choking Abbie to death. "
                sk " Deserved. Honestly, they should've expected for something like that to happen sometime soon. "
                sk " They can't just think that they can do whatever they want all the time... "
                sk " What a bunch of assholes. "
                hide rubyneutral at bottom
                show rubyangry at right
                ru " Skelly, language... "
                hide rubyangry at bottom
                show rubyneutral at right
                sk " ...Right. But still, Oliver deserved it."
                sk " He'd have to get a punishment one day, whether he likes it or not. "
                ru " I agree... "
                " You, Ruby, and Skell continued to talk for a bit. "
                " Why do I say this? the programmer had no ideas on what to put here. "
                " It's not easy being a writer, man. Sometimes you lose motivation in the middle of you writing something "
                " ...Like that. I just continued writing something 10 minutes after I wrote the last line. "
                play sound "audio/bellring.mp3"
                " The bell rings, you and Ruby both go but Skell decided to stay behind for a bit longer. "
                hide rubyneutral at right with easeoutright
                scene black with dissolve
                pause 2.0
                jump historyclass1
            else:
                " It was a girl with a TV for a head. You could recognize her since she's from your class, from what you remember... "
                " Maybe you should go up to them and see what they're talking about. "
                show skellneutral at left with easeinright
                show rubyneutral at right with easeinright
                sk " So... you remembered anything about the history thing? "
                x " Actually, Skelly, we didn't have anything to do in history, if that's what you're asking. "
                x " Remember, last friday it was only a lecture! "
                sk " Ah, alright, then... thanks for reminding me. "
                " Skell was about to leave, but he notices you standing there. "
                sk " Oh, hey, [name]... "
                x " Oh, oh!! Who's that? is that a new friend of yours? "
                sk " ...I guess you could say that, yeah. "
                sk " They sort of just... relaxed with me earlier. "
                x " It's good to know that you're getting more friends, Skelly! "
                x " I'd like to introduce myself to them! Ahem... "
                $ rubyknow = True
                hide rubyneutral at bottom
                show rubyhappy at right
                ru " I'm Ruby! I hope we can be great friends! "
                ru " It's oh so nice to meet you! "
                hide rubyhappy at bottom
                show rubyneutral at right
                ru " Anyway...Zip and Edward seem to be a little more...angry today. "
                sk " Oh? and why is that? "
                ru " According to my research, Oliver got suspended until wednesday due to him almost choking Abbie to death. "
                sk " Deserved. Honestly, they should've expected for something like that to happen sometime soon. "
                sk " They can't just think that they can do whatever they want all the time... "
                sk " What a bunch of assholes. "
                hide rubyneutral at bottom
                show rubyangry at right
                ru " Skelly, language... "
                hide rubyangry at bottom
                show rubyneutral at right
                sk " ...Right. But still, Oliver deserved it."
                sk " He'd have to get a punishment one day, whether he likes it or not. "
                ru " I agree... "
                " You, Ruby, and Skell continued to talk for a bit. "
                " Why do I say this? the programmer had no ideas on what to put here. "
                " It's not easy being a writer, man. Sometimes you lose motivation in the middle of you writing something "
                " ...Like that. I just continued writing something 10 minutes after I wrote the last line. "
                play sound "audio/bellring.mp3"
                " The bell rings, you and Ruby both go but Skell decided to stay behind for a bit longer. "
                hide rubyneutral at right with easeoutright
                scene black with dissolve
                pause 2.0
                jump historyclass1
        else:
            " You went back to the back of the school, and you see an emo...looking...cat thing? "
            " This time, he seemed to be talking with a girl... "
            if rubyknow == True:
                " A girl you've seen before...Is that Ruby? "
                " You should go up to them and see what they're talking about. "
                show skellneutral at left with easeinright
                show rubyneutral at right with easeinright
                x " So... you remembered anything about the history thing? "
                ru " Actually, Skelly, we didn't have anything to do in history, if that's what you're asking. "
                ru " Remember, last friday it was only a lecture! "
                x " Ah, alright, then... thanks for reminding me. "
                " The cat boy was about to leave, but he notices you standing there. "
                x " Oh, um... Hey there. "
                hide rubyneutral at bottom
                show rubyhappy at right
                ru " [name]! It's good to see you here! "
                x " You know this guy, Ruby? "
                hide rubyhappy at bottom
                show rubyneutral at right
                $ skellknow = True
                ru " Yepp! [they] [are] my friend! "
                ru " [name], meet Skelly! He's my friend! "
                ru " I hope you two can get along well! Skelly really does need more friends... "
                sk " ...Sup. "
                ru " Anyway...Zip and Edward seem to be a little more...angry today. "
                sk " Oh? and why is that? "
                ru " According to my research, Oliver got suspended until wednesday due to him almost choking Abbie to death. "
                sk " Deserved. Honestly, they should've expected for something like that to happen sometime soon. "
                sk " They can't just think that they can do whatever they want all the time... "
                sk " What a bunch of assholes. "
                hide rubyneutral at bottom
                show rubyangry at right
                ru " Skelly, language... "
                hide rubyangry at bottom
                show rubyneutral at right
                sk " ...Right. But still, Oliver deserved it."
                sk " He'd have to get a punishment one day, whether he likes it or not. "
                ru " I agree... "
                " You, Ruby, and Skell continued to talk for a bit. "
                " Why do I say this? the programmer had no ideas on what to put here. "
                " It's not easy being a writer, man. Sometimes you lose motivation in the middle of you writing something "
                " ...Like that. I just continued writing something 10 minutes after I wrote the last line. "
                play sound "audio/bellring.mp3"
                " The bell rings, you and Ruby both go but Skell decided to stay behind for a bit longer. "
                hide rubyneutral at right with easeoutright
                scene black with dissolve
                pause 2.0
                jump historyclass1
            else:
                " It was a girl with a TV for a head. You could recognize her since she's from your class, from what you remember... "
                " Maybe you should go up to them and see what they're talking about. "
                show skellneutral at left with easeinright
                show rubyneutral at right with easeinright
                x " So... you remembered anything about the history thing? "
                x " Actually, Skelly, we didn't have anything to do in history, if that's what you're asking. "
                x " Remember, last friday it was only a lecture! "
                x " Ah, alright, then... thanks for reminding me. "
                " The cat boy was about to leave, but he notices you standing there. "
                x "Oh. Um... hey there. "
                x " Oh, oh!! Who's that? is that a new friend of yours? "
                x " ...No, I haven't really met [them] before. "
                x " All I know is that [they] [are] in our class. "
                x " Well then! We should introduce ourselves to them! "
                x " Theres nothing wrong in making new friends, you know! "
                $ rubyknow = True
                $ skellknow = True
                hide rubyneutral at bottom
                show rubyhappy at right
                ru " I'm Ruby! I hope we can be great friends! "
                ru " It's oh so nice to meet you! "
                ru " This here is my friends, Skelly! "
                ru " I hope that you two can become really good friends as well, as he barely has any! "
                ru " Well... other than me, Robby, and Riley... "
                sk " ... Nice to meet you, I guess. "
                hide rubyhappy at bottom
                show rubyneutral at right
                ru " Anyway...Zip and Edward seem to be a little more...angry today. "
                sk " Oh? and why is that? "
                ru " According to my research, Oliver got suspended until wednesday due to him almost choking Abbie to death. "
                sk " Deserved. Honestly, they should've expected for something like that to happen sometime soon. "
                sk " They can't just think that they can do whatever they want all the time... "
                sk " What a bunch of assholes. "
                hide rubyneutral at bottom
                show rubyangry at right
                ru " Skelly, language... "
                hide rubyangry at bottom
                show rubyneutral at right
                sk " ...Right. But still, Oliver deserved it."
                sk " He'd have to get a punishment one day, whether he likes it or not. "
                ru " I agree... "
                " You, Ruby, and Skell continued to talk for a bit. "
                " Why do I say this? the programmer had no ideas on what to put here. "
                " It's not easy being a writer, man. Sometimes you lose motivation in the middle of you writing something "
                " ...Like that. I just continued writing something 10 minutes after I wrote the last line. "
                play sound "audio/bellring.mp3"
                " The bell rings, you and Ruby both go but Skell decided to stay behind for a bit longer. "
                hide rubyneutral at right with easeoutright
                scene black with dissolve
                pause 2.0
                jump historyclass1
    label gym3:
        scene gym with dissolve
        if bubbleknow == True and engelknow == True:
            " As you enter the gym, you spot Engel and Bubble sitting on the bleachers. "
            " The both of them were doing their own respective things, sitting away from eachother. "
            " You kind of feel like talking to one of them. Probably because you're bored. "
            " Who should you talk to? "
            menu:
                " Bubble ":
                    show bubbleneutral at center with easeinright
                    " Bubble seems to be busy doodling something on a piece of paper... "
                    " You take a closer look at what she's drawing, and it actually looks pretty good. "
                    " Her artstyle looks like one of those cool animes you've seen. "
                    " Once she notices you there, she seems a little bit embarrassed of her drawing and she hides it from you. "
                    b " OH!! uh... Hi there, [name]... "
                    b " What was I drawing...? Well, it's not really...done yet... "
                    b " I don't really want you to see it since it's not done. And plus, it probably looks super cringy! "
                    " You reassure her that it probably looks fine and tell her that you want to see it. "
                    b " W...well... If you say so, then... "
                    " Bubble grabs her piece of paper once again and she shows you the drawing that she was working on. "
                    " It was a nice drawing of that one flame dude from Angel Slayer... or was it Demon Slayer? "
                    " You can't really remember. Either way, it looks good. "
                    " And also, the way she drew it looked accurate to the actual artstyle from the anime. "
                    " You never knew she could be so talented... "
                    menu:
                        " Compliment her art and tell her the artstyle is accurate ":
                            $ bubblelv += 10
                            b " Really...? "
                            hide bubbleneutral at bottom
                            show bubbleamazed at center
                            b " Thank you so much! I worked so hard on replicating the artstyle! "
                            b " It was a little tricky, of course, but I managed to get it in the end! "
                            hide bubbleamazed at bottom
                            show bubblehappy at center
                            b " I'm glad that you like my art, [name]! "
                            hide bubblehappy at bottom
                            show bubbleneutral at center
                            b " Would you... would you like to draw with me? If you want to... "
                            menu:
                                " Draw with her ":
                                    hide bubbleneutral at bottom
                                    show bubblehappy at center
                                    b " Yayy!! Alrighty! "
                                    scene black with dissolve
                                    " You drew little characters with Bubble for the rest of the break. "
                                    " Your drawings were a little bad compared to Bubble's, but she didn't mind. "
                                    " She thought they were cute, after all. "
                                    " Someday you might want to learn how to draw like that, but then again it's gonna be a bit difficult to. "
                                    " You're just gonna have to think about it for awhile. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rings, and you take a picture of yours and Bubble's art. "
                                    " You then get up and went to the classroom with Bubble for your next class. "
                                    pause 2.0
                                    jump historyclass1
                                " Nah I'll just watch, I don't want to ruin the masterpiece ":
                                    b " That's nice that you don't wanna ruin my drawings, [name]... "
                                    b " But I think your drawings wouldn't be bad at all! No one's drawings are bad! "
                                    b " We all start at one point, and at that one point, all we knew how to draw was just shapes and stickmen! "
                                    b " I'll just continue to draw while we talk, alright? "
                                    scene black with dissolve
                                    " You talked with Bubble whilst she was drawing. "
                                    " Her art was so good, you didn't want to put your ugly drawings on the paper. "
                                    " But, she's right. No one's drawings are bad. "
                                    " Still, it was mesmerizing for you to see how she made her drawings. "
                                    " So detailed... "
                                    play sound "audio/bellring.mp3"
                                    " The bell eventually rang, and you n Bubble went back to the classroom for the next class. "
                                    pause 2.0
                                    jump historyclass1
                        " Compliment her art ":
                            $ bubblelv += 5
                            b " Really...? "
                            hide bubbleneutral at bottom
                            show bubblehappy at center
                            b " Thank you so much, [name]! "
                            b " You know... It took me a bit to replicate the artstyle from the anime, but... "
                            b " I managed to copy it in the end! "
                            b " I'll just continue to draw while we talk, alright? "
                            scene black with dissolve
                            " You talked with Bubble whilst she was drawing. "
                            " Her art was so good, you didn't want to put your ugly drawings on the paper. "
                            " But, then again, No one's drawings are bad. We all start at some point. "
                            " Still, it was mesmerizing for you to see how she made her drawings. "
                            " So detailed... "
                            play sound "audio/bellring.mp3"
                            " The bell eventually rang, and you n Bubble went back to the classroom for the next class. "
                            pause 2.0
                            jump historyclass1
                " Engel ":
                    " You sat next to Engel to see what he was reading. "
                    show engelneutral at center with easeinleft
                    " He was quiet, and all you could hear in the room was some faint breathing and some doodling noises from Bubble. "
                    " ...And the loudness of the hallways, but only just a little. "
                    " You decided to lean in more to see what he was reading, and you could see that he was reading a book about history this time. "
                    " You even decided to read a few of the lines from the book, until you heard him speak up. Looks like he finally noticed that you were there. "
                    e " Hello there, [name]... "
                    e " Apologies that I hadn't noticed you at first... I do tend to get absorbed in my reading too much. "
                    e " What brings you here? Did you want to read with me? "
                    menu:
                        " Read with him ":
                            hide engelneutral at bottom
                            show engelhappy at center
                            e " Alrighty, then... If that's what you wish. "
                            e " Now... "
                            " Engel talked to you about interesting history facts he's found. "
                            " Somehow, he made it feel as if he were a dad telling his kid a bedtime story. "
                            " You even leaned into his shoulder because you felt sleepy due to how soft his voice was... "
                            " Damn. He'd make a great dad in the future. "
                            " You already feel like you're his kid at this point. "
                            play sound "audio/bellring.mp3"
                            " You were about to fall asleep, but the bell prevented you from doing that. "
                            e " I can tell you wanted to sleep right there... "
                            e " Don't worry, [name], it's just a few more classes until the day ends. "
                            e " Then, you can get all the rest you want for tomorrow. "
                            e " I'll see you there in the classroom. "
                            scene black with dissolve
                            pause 2.0
                            jump historyclass1
                        " Just chill and talk ":
                            e " You wanted to talk? That's fine by me, then... "
                            e " Though, I'm gonna be probably busy reading, so... "
                            e " I hope you're fine with me sometimes not listening. "
                            e " I can't really help it... "
                            scene black with dissolve
                            " You talked with Engel about random school related topics. "
                            " Although he couldn't really respond some of the times due to how busy he was with reading, "
                            " You were fine with repeating your sentences until he responded. "
                            " ...One time you had to repeat 3 times before he responded. But that's okay. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, and you both get up from the bleachers and went to the classroom for the next class. "
                            pause 2.0
                            jump historyclass1
                " Nah I'll just chill ":
                    " You ended up not choosing at all and you just sat inbetween them. "
                    " You turned your head and you saw Engel reading somrthing. "
                    " You turned your head to the other side and you saw Bubble doodling... "
                    " You could be doing something right now. "
                    " Maybe look through your phone, or just chill for a bit. "
                    " You pull out your phone and just scroll through tiktok for a bit. "
                    " There wasn't really anything interesting, just a few videos of cute cats here and there... also some drama going on. "
                    play sound "audio/bellring.mp3"
                    " You continued to mindlessly scroll until you heard the bell ring. "
                    " You got up, and you walk down over to your classroom for your next class. "
                    scene black with dissolve
                    pause 2.0
                    jump historyclass1
        elif bubbleknow == True and engelknow == False:
            " As you enter the gym, you spot a guy reading something and Bubble sitting on the bleachers. "
            " The both of them were doing their own respective things, sitting away from eachother. "
            " You kind of feel like talking to one of them. Probably because you're bored. "
            " Who should you talk to? "
            menu:
                " Bubble ":
                    show bubbleneutral at center with easeinright
                    " Bubble seems to be busy doodling something on a piece of paper... "
                    " You take a closer look at what she's drawing, and it actually looks pretty good. "
                    " Her artstyle looks like one of those cool animes you've seen. "
                    " Once she notices you there, she seems a little bit embarrassed of her drawing and she hides it from you. "
                    b " OH!! uh... Hi there, [name]... "
                    b " What was I drawing...? Well, it's not really...done yet... "
                    b " I don't really want you to see it since it's not done. And plus, it probably looks super cringy! "
                    " You reassure her that it probably looks fine and tell her that you want to see it. "
                    b " W...well... If you say so, then... "
                    " Bubble grabs her piece of paper once again and she shows you the drawing that she was working on. "
                    " It was a nice drawing of that one flame dude from Angel Slayer... or was it Demon Slayer? "
                    " You can't really remember. Either way, it looks good. "
                    " And also, the way she drew it looked accurate to the actual artstyle from the anime. "
                    " You never knew she could be so talented... "
                    menu:
                        " Compliment her art and tell her the artstyle is accurate ":
                            $ bubblelv += 10
                            b " Really...? "
                            hide bubbleneutral at bottom
                            show bubbleamazed at center
                            b " Thank you so much! I worked so hard on replicating the artstyle! "
                            b " It was a little tricky, of course, but I managed to get it in the end! "
                            hide bubbleamazed at bottom
                            show bubblehappy at center
                            b " I'm glad that you like my art, [name]! "
                            hide bubblehappy at bottom
                            show bubbleneutral at center
                            b " Would you... would you like to draw with me? If you want to... "
                            menu:
                                " Draw with her ":
                                    hide bubbleneutral at bottom
                                    show bubblehappy at center
                                    b " Yayy!! Alrighty! "
                                    scene black with dissolve
                                    " You drew little characters with Bubble for the rest of the break. "
                                    " Your drawings were a little bad compared to Bubble's, but she didn't mind. "
                                    " She thought they were cute, after all. "
                                    " Someday you might want to learn how to draw like that, but then again it's gonna be a bit difficult to. "
                                    " You're just gonna have to think about it for awhile. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rings, and you take a picture of yours and Bubble's art. "
                                    " You then get up and went to the classroom with Bubble for your next class. "
                                    pause 2.0
                                    jump historyclass1
                                " Nah I'll just watch, I don't want to ruin the masterpiece ":
                                    b " That's nice that you don't wanna ruin my drawings, [name]... "
                                    b " But I think your drawings wouldn't be bad at all! No one's drawings are bad! "
                                    b " We all start at one point, and at that one point, all we knew how to draw was just shapes and stickmen! "
                                    b " I'll just continue to draw while we talk, alright? "
                                    scene black with dissolve
                                    " You talked with Bubble whilst she was drawing. "
                                    " Her art was so good, you didn't want to put your ugly drawings on the paper. "
                                    " But, she's right. No one's drawings are bad. "
                                    " Still, it was mesmerizing for you to see how she made her drawings. "
                                    " So detailed... "
                                    play sound "audio/bellring.mp3"
                                    " The bell eventually rang, and you n Bubble went back to the classroom for the next class. "
                                    pause 2.0
                                    jump historyclass1
                        " Compliment her art ":
                            $ bubblelv += 5
                            b " Really...? "
                            hide bubbleneutral at bottom
                            show bubblehappy at center
                            b " Thank you so much, [name]! "
                            b " You know... It took me a bit to replicate the artstyle from the anime, but... "
                            b " I managed to copy it in the end! "
                            b " I'll just continue to draw while we talk, alright? "
                            scene black with dissolve
                            " You talked with Bubble whilst she was drawing. "
                            " Her art was so good, you didn't want to put your ugly drawings on the paper. "
                            " But, then again, No one's drawings are bad. We all start at some point. "
                            " Still, it was mesmerizing for you to see how she made her drawings. "
                            " So detailed... "
                            play sound "audio/bellring.mp3"
                            " The bell eventually rang, and you n Bubble went back to the classroom for the next class. "
                            pause 2.0
                            jump historyclass1
                " The guy reading something ":
                    " You sat next to the boy to see what he was reading. "
                    show engelneutral at center with easeinleft
                    " He was quiet, and all you could hear in the room was some faint breathing and some doodling noises from Bubble. "
                    " ...And the loudness of the hallways, but only just a little. "
                    " You decided to lean in more to see what he was reading, and you could see that he was reading a book about history this time. "
                    " You even decided to read a few of the lines from the book, until you heard him speak up. Looks like he finally noticed that you were there. "
                    x " Hello there, [name]... "
                    x " Apologies that I hadn't noticed you at first... I do tend to get absorbed in my reading too much. "
                    x " And I'm afraid I haven't properly introduced myself before, as I never had the chance to... "
                    $ engelknow = True
                    e " I am Engel. I'm glad to meet you. I'm in your class, if you don't remember. "
                    e " Anywho, with that aside... "
                    e " What brings you here? Did you want to read with me? "
                    menu:
                        " Read with him ":
                            hide engelneutral at bottom
                            show engelhappy at center
                            e " Alrighty, then... If that's what you wish. "
                            e " Now... "
                            " Engel talked to you about interesting history facts he's found. "
                            " Somehow, he made it feel as if he were a dad telling his kid a bedtime story. "
                            " You even leaned into his shoulder because you felt sleepy due to how soft his voice was... "
                            " Damn. He'd make a great dad in the future. "
                            " You already feel like you're his kid at this point. "
                            play sound "audio/bellring.mp3"
                            " You were about to fall asleep, but the bell prevented you from doing that. "
                            e " I can tell you wanted to sleep right there... "
                            e " Don't worry, [name], it's just a few more classes until the day ends. "
                            e " Then, you can get all the rest you want for tomorrow. "
                            e " I'll see you there in the classroom. "
                            scene black with dissolve
                            pause 2.0
                            jump historyclass1
                        " Just chill and talk ":
                            e " You wanted to talk? That's fine by me, then... "
                            e " Though, I'm gonna be probably busy reading, so... "
                            e " I hope you're fine with me sometimes not listening. "
                            e " I can't really help it... "
                            scene black with dissolve
                            " You talked with Engel about random school related topics. "
                            " Although he couldn't really respond some of the times due to how busy he was with reading, "
                            " You were fine with repeating your sentences until he responded. "
                            " ...One time you had to repeat 3 times before he responded. But that's okay. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, and you both get up from the bleachers and went to the classroom for the next class. "
                            pause 2.0
                            jump historyclass1
                " Nah I'll just chill ":
                    " You ended up not choosing at all and you just sat inbetween them. "
                    " You turned your head and you saw the other boy reading something. "
                    " You turned your head to the other side and you saw Bubble doodling... "
                    " You could be doing something right now. "
                    " Maybe look through your phone, or just chill for a bit. "
                    " You pull out your phone and just scroll through tiktok for a bit. "
                    " There wasn't really anything interesting, just a few videos of cute cats here and there... also some drama going on. "
                    play sound "audio/bellring.mp3"
                    " You continued to mindlessly scroll until you heard the bell ring. "
                    " You got up, and you walk down over to your classroom for your next class. "
                    scene black with dissolve
                    pause 2.0
                    jump historyclass1
        elif bubbleknow == False and engelknow == True:
            " As you enter the gym, you spot Engel and a girl doodling sitting on the bleachers. "
            " The both of them were doing their own respective things, sitting away from eachother. "
            " You kind of feel like talking to one of them. Probably because you're bored. "
            " Who should you talk to? "
            menu:
                " The girl doodling ":
                    show bubbleneutral at center with easeinright
                    " She seems to be busy doodling something on a piece of paper... "
                    " You take a closer look at what she's drawing, and it actually looks pretty good. "
                    " Her artstyle looks like one of those cool animes you've seen. "
                    " Once she notices you there, she seems a little bit embarrassed of her drawing and she hides it from you. "
                    x " OH!! uh... Hi there... "
                    x " What was I drawing...? Well, it's not really...done yet... "
                    x " Um...um... I don't think we've met before! "
                    " ...I think that was a desperate attempt to change the topic. "
                    $ bubbleknow = True
                    b " I'm Bubble! Uh... great to meet you! "
                    " You introduce yourself to her, and you question her about the drawing she was working on. "
                    b " O..oh, uh... That drawing...? Well... "
                    b " I don't really want you to see it since it's not done. And plus, it probably looks super cringy! "
                    " You reassure her that it probably looks fine and tell her that you want to see it. "
                    b " W...well... If you say so, then... "
                    " Bubble grabs her piece of paper once again and she shows you the drawing that she was working on. "
                    " It was a nice drawing of that one flame dude from Angel Slayer... or was it Demon Slayer? "
                    " You can't really remember. Either way, it looks good. "
                    " And also, the way she drew it looked accurate to the actual artstyle from the anime. "
                    " You never knew she could be so talented... "
                    menu:
                        " Compliment her art and tell her the artstyle is accurate ":
                            $ bubblelv += 10
                            b " Really...? "
                            hide bubbleneutral at bottom
                            show bubbleamazed at center
                            b " Thank you so much! I worked so hard on replicating the artstyle! "
                            b " It was a little tricky, of course, but I managed to get it in the end! "
                            hide bubbleamazed at bottom
                            show bubblehappy at center
                            b " I'm glad that you like my art, [name]! "
                            hide bubblehappy at bottom
                            show bubbleneutral at center
                            b " Would you... would you like to draw with me? If you want to... "
                            menu:
                                " Draw with her ":
                                    hide bubbleneutral at bottom
                                    show bubblehappy at center
                                    b " Yayy!! Alrighty! "
                                    scene black with dissolve
                                    " You drew little characters with Bubble for the rest of the break. "
                                    " Your drawings were a little bad compared to Bubble's, but she didn't mind. "
                                    " She thought they were cute, after all. "
                                    " Someday you might want to learn how to draw like that, but then again it's gonna be a bit difficult to. "
                                    " You're just gonna have to think about it for awhile. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rings, and you take a picture of yours and Bubble's art. "
                                    " You then get up and went to the classroom with Bubble for your next class. "
                                    pause 2.0
                                    jump historyclass1
                                " Nah I'll just watch, I don't want to ruin the masterpiece ":
                                    b " That's nice that you don't wanna ruin my drawings, [name]... "
                                    b " But I think your drawings wouldn't be bad at all! No one's drawings are bad! "
                                    b " We all start at one point, and at that one point, all we knew how to draw was just shapes and stickmen! "
                                    b " I'll just continue to draw while we talk, alright? "
                                    scene black with dissolve
                                    " You talked with Bubble whilst she was drawing. "
                                    " Her art was so good, you didn't want to put your ugly drawings on the paper. "
                                    " But, she's right. No one's drawings are bad. "
                                    " Still, it was mesmerizing for you to see how she made her drawings. "
                                    " So detailed... "
                                    play sound "audio/bellring.mp3"
                                    " The bell eventually rang, and you n Bubble went back to the classroom for the next class. "
                                    pause 2.0
                                    jump historyclass1
                        " Compliment her art ":
                            $ bubblelv += 5
                            b " Really...? "
                            hide bubbleneutral at bottom
                            show bubblehappy at center
                            b " Thank you so much, [name]! "
                            b " You know... It took me a bit to replicate the artstyle from the anime, but... "
                            b " I managed to copy it in the end! "
                            b " I'll just continue to draw while we talk, alright? "
                            scene black with dissolve
                            " You talked with Bubble whilst she was drawing. "
                            " Her art was so good, you didn't want to put your ugly drawings on the paper. "
                            " But, then again, No one's drawings are bad. We all start at some point. "
                            " Still, it was mesmerizing for you to see how she made her drawings. "
                            " So detailed... "
                            play sound "audio/bellring.mp3"
                            " The bell eventually rang, and you n Bubble went back to the classroom for the next class. "
                            pause 2.0
                            jump historyclass1
                " Engel ":
                    " You sat next to Engel to see what he was reading. "
                    show engelneutral at center with easeinleft
                    " He was quiet, and all you could hear in the room was some faint breathing and some doodling noises from Bubble. "
                    " ...And the loudness of the hallways, but only just a little. "
                    " You decided to lean in more to see what he was reading, and you could see that he was reading a book about history this time. "
                    " You even decided to read a few of the lines from the book, until you heard him speak up. Looks like he finally noticed that you were there. "
                    e " Hello there, [name]... "
                    e " Apologies that I hadn't noticed you at first... I do tend to get absorbed in my reading too much. "
                    e " What brings you here? Did you want to read with me? "
                    menu:
                        " Read with him ":
                            hide engelneutral at bottom
                            show engelhappy at center
                            e " Alrighty, then... If that's what you wish. "
                            e " Now... "
                            " Engel talked to you about interesting history facts he's found. "
                            " Somehow, he made it feel as if he were a dad telling his kid a bedtime story. "
                            " You even leaned into his shoulder because you felt sleepy due to how soft his voice was... "
                            " Damn. He'd make a great dad in the future. "
                            " You already feel like you're his kid at this point. "
                            play sound "audio/bellring.mp3"
                            " You were about to fall asleep, but the bell prevented you from doing that. "
                            e " I can tell you wanted to sleep right there... "
                            e " Don't worry, [name], it's just a few more classes until the day ends. "
                            e " Then, you can get all the rest you want for tomorrow. "
                            e " I'll see you there in the classroom. "
                            scene black with dissolve
                            pause 2.0
                            jump historyclass1
                        " Just chill and talk ":
                            e " You wanted to talk? That's fine by me, then... "
                            e " Though, I'm gonna be probably busy reading, so... "
                            e " I hope you're fine with me sometimes not listening. "
                            e " I can't really help it... "
                            scene black with dissolve
                            " You talked with Engel about random school related topics. "
                            " Although he couldn't really respond some of the times due to how busy he was with reading, "
                            " You were fine with repeating your sentences until he responded. "
                            " ...One time you had to repeat 3 times before he responded. But that's okay. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, and you both get up from the bleachers and went to the classroom for the next class. "
                            pause 2.0
                            jump historyclass1
                " Nah I'll just chill ":
                    " You ended up not choosing at all and you just sat inbetween them. "
                    " You turned your head and you saw Engel reading something. "
                    " You turned your head to the other side and you saw the girl still doodling... "
                    " You could be doing something right now. "
                    " Maybe look through your phone, or just chill for a bit. "
                    " You pull out your phone and just scroll through tiktok for a bit. "
                    " There wasn't really anything interesting, just a few videos of cute cats here and there... also some drama going on. "
                    play sound "audio/bellring.mp3"
                    " You continued to mindlessly scroll until you heard the bell ring. "
                    " You got up, and you walk down over to your classroom for your next class. "
                    scene black with dissolve
                    pause 2.0
                    jump historyclass1
        else:
            " As you enter the gym, you spot a guy reading and a girl doodling sitting on the bleachers. "
            " The both of them were doing their own respective things, sitting away from eachother. "
            " You kind of feel like talking to one of them. Probably because you're bored. "
            " Who should you talk to? "
            menu:
                " The girl doodling ":
                    show bubbleneutral at center with easeinright
                    " She seems to be busy doodling something on a piece of paper... "
                    " You take a closer look at what she's drawing, and it actually looks pretty good. "
                    " Her artstyle looks like one of those cool animes you've seen. "
                    " Once she notices you there, she seems a little bit embarrassed of her drawing and she hides it from you. "
                    x " OH!! uh... Hi there... "
                    x " What was I drawing...? Well, it's not really...done yet... "
                    x " Um...um... I don't think we've met before! "
                    " ...I think that was a desperate attempt to change the topic. "
                    $ bubbleknow = True
                    b " I'm Bubble! Uh... great to meet you! "
                    " You introduce yourself to her, and you question her about the drawing she was working on. "
                    b " O..oh, uh... That drawing...? Well... "
                    b " I don't really want you to see it since it's not done. And plus, it probably looks super cringy! "
                    " You reassure her that it probably looks fine and tell her that you want to see it. "
                    b " W...well... If you say so, then... "
                    " Bubble grabs her piece of paper once again and she shows you the drawing that she was working on. "
                    " It was a nice drawing of that one flame dude from Angel Slayer... or was it Demon Slayer? "
                    " You can't really remember. Either way, it looks good. "
                    " And also, the way she drew it looked accurate to the actual artstyle from the anime. "
                    " You never knew she could be so talented... "
                    menu:
                        " Compliment her art and tell her the artstyle is accurate ":
                            $ bubblelv += 10
                            b " Really...? "
                            hide bubbleneutral at bottom
                            show bubbleamazed at center
                            b " Thank you so much! I worked so hard on replicating the artstyle! "
                            b " It was a little tricky, of course, but I managed to get it in the end! "
                            hide bubbleamazed at bottom
                            show bubblehappy at center
                            b " I'm glad that you like my art, [name]! "
                            hide bubblehappy at bottom
                            show bubbleneutral at center
                            b " Would you... would you like to draw with me? If you want to... "
                            menu:
                                " Draw with her ":
                                    hide bubbleneutral at bottom
                                    show bubblehappy at center
                                    b " Yayy!! Alrighty! "
                                    scene black with dissolve
                                    " You drew little characters with Bubble for the rest of the break. "
                                    " Your drawings were a little bad compared to Bubble's, but she didn't mind. "
                                    " She thought they were cute, after all. "
                                    " Someday you might want to learn how to draw like that, but then again it's gonna be a bit difficult to. "
                                    " You're just gonna have to think about it for awhile. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rings, and you take a picture of yours and Bubble's art. "
                                    " You then get up and went to the classroom with Bubble for your next class. "
                                    pause 2.0
                                    jump historyclass1
                                " Nah I'll just watch, I don't want to ruin the masterpiece ":
                                    b " That's nice that you don't wanna ruin my drawings, [name]... "
                                    b " But I think your drawings wouldn't be bad at all! No one's drawings are bad! "
                                    b " We all start at one point, and at that one point, all we knew how to draw was just shapes and stickmen! "
                                    b " I'll just continue to draw while we talk, alright? "
                                    scene black with dissolve
                                    " You talked with Bubble whilst she was drawing. "
                                    " Her art was so good, you didn't want to put your ugly drawings on the paper. "
                                    " But, she's right. No one's drawings are bad. "
                                    " Still, it was mesmerizing for you to see how she made her drawings. "
                                    " So detailed... "
                                    play sound "audio/bellring.mp3"
                                    " The bell eventually rang, and you n Bubble went back to the classroom for the next class. "
                                    pause 2.0
                                    jump historyclass1
                        " Compliment her art ":
                            $ bubblelv += 5
                            b " Really...? "
                            hide bubbleneutral at bottom
                            show bubblehappy at center
                            b " Thank you so much, [name]! "
                            b " You know... It took me a bit to replicate the artstyle from the anime, but... "
                            b " I managed to copy it in the end! "
                            b " I'll just continue to draw while we talk, alright? "
                            scene black with dissolve
                            " You talked with Bubble whilst she was drawing. "
                            " Her art was so good, you didn't want to put your ugly drawings on the paper. "
                            " But, then again, No one's drawings are bad. We all start at some point. "
                            " Still, it was mesmerizing for you to see how she made her drawings. "
                            " So detailed... "
                            play sound "audio/bellring.mp3"
                            " The bell eventually rang, and you n Bubble went back to the classroom for the next class. "
                            pause 2.0
                            jump historyclass1
                " The guy reading ":
                    " You sat next to the boy to see what he was reading. "
                    show engelneutral at center with easeinleft
                    " He was quiet, and all you could hear in the room was some faint breathing and some doodling noises from Bubble. "
                    " ...And the loudness of the hallways, but only just a little. "
                    " You decided to lean in more to see what he was reading, and you could see that he was reading a book about history this time. "
                    " You even decided to read a few of the lines from the book, until you heard him speak up. Looks like he finally noticed that you were there. "
                    x " Hello there, [name]... "
                    x " Apologies that I hadn't noticed you at first... I do tend to get absorbed in my reading too much. "
                    x " And I'm afraid I haven't properly introduced myself before, as I never had the chance to... "
                    $ engelknow = True
                    e " I am Engel. I'm glad to meet you. I'm in your class, if you don't remember. "
                    e " Anywho, with that aside... "
                    e " What brings you here? Did you want to read with me? "
                    menu:
                        " Read with him ":
                            hide engelneutral at bottom
                            show engelhappy at center
                            e " Alrighty, then... If that's what you wish. "
                            e " Now... "
                            " Engel talked to you about interesting history facts he's found. "
                            " Somehow, he made it feel as if he were a dad telling his kid a bedtime story. "
                            " You even leaned into his shoulder because you felt sleepy due to how soft his voice was... "
                            " Damn. He'd make a great dad in the future. "
                            " You already feel like you're his kid at this point. "
                            play sound "audio/bellring.mp3"
                            " You were about to fall asleep, but the bell prevented you from doing that. "
                            e " I can tell you wanted to sleep right there... "
                            e " Don't worry, [name], it's just a few more classes until the day ends. "
                            e " Then, you can get all the rest you want for tomorrow. "
                            e " I'll see you there in the classroom. "
                            scene black with dissolve
                            pause 2.0
                            jump historyclass1
                        " Just chill and talk ":
                            e " You wanted to talk? That's fine by me, then... "
                            e " Though, I'm gonna be probably busy reading, so... "
                            e " I hope you're fine with me sometimes not listening. "
                            e " I can't really help it... "
                            scene black with dissolve
                            " You talked with Engel about random school related topics. "
                            " Although he couldn't really respond some of the times due to how busy he was with reading, "
                            " You were fine with repeating your sentences until he responded. "
                            " ...One time you had to repeat 3 times before he responded. But that's okay. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, and you both get up from the bleachers and went to the classroom for the next class. "
                            pause 2.0
                            jump historyclass1
                " Nah I'll just chill ":
                    " You ended up not choosing at all and you just sat inbetween them. "
                    " You turned your head and you saw the boy reading something. "
                    " You turned your head to the other side and you saw the girl still doodling... "
                    " You could be doing something right now. "
                    " Maybe look through your phone, or just chill for a bit. "
                    " You pull out your phone and just scroll through tiktok for a bit. "
                    " There wasn't really anything interesting, just a few videos of cute cats here and there... also some drama going on. "
                    play sound "audio/bellring.mp3"
                    " You continued to mindlessly scroll until you heard the bell ring. "
                    " You got up, and you walk down over to your classroom for your next class. "
                    scene black with dissolve
                    pause 2.0
                    jump historyclass1
    label cafe3:
        scene cafeteria with dissolve
        " Who do you want to sit with today? "
        if claireknow == True and popularknow,cubbieknow == False:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    " You walk up to Claire who seems to be reading something. "
                    jump clairecafeint
                " {image=popularicon} Two girls who seem popular. {image=popularicon} ":
                    " Either you also wanna be popular, or you just wanna sit with them cause they're cool. "
                    " Hopefully this doesn't end up like Heathers the musical. "
                    " Theres only two of them, anyway. You're probably about to become the third. "
                    jump popularcafeint
                " {image=cubbieicon} A cute little cat! {image=cubbieicon} ":
                    " Who wouldn't wanna sit next to a cute looking cat? "
                    " Upon closer looks, they have a sharpener for a body. "
                    " Still absolutely adorable though! You made no hesitation on sitting right next to them. "
                    jump cubbiecafeint
        elif popularknow == True and claireknow,cubbieknow == False:
            menu:
                " {image=claireicon} A girl with short white hair and a bow on her {image=claireicon} ":
                    " She seems to be reading something... "
                    " Let's go disturb her. "
                    jump clairecafeint
                " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                    " Time to see what drama they've got for you for today. "
                    jump popularcafeint
                " {image=cubbieicon} A cute little cat! {image=cubbieicon} ":
                    " Who wouldn't wanna sit next to a cute looking cat? "
                    " Upon closer looks, they have a sharpener for a body. "
                    " Still absolutely adorable though! You made no hesitation on sitting right next to them. "
                    jump cubbiecafeint
        elif cubbieknow == True and claireknow,popularknow == False:
            menu:
                " {image=claireicon} A girl with short white hair and a bow on her {image=claireicon} ":
                    " She seems to be reading something... "
                    " Let's go disturb her. "
                    jump clairecafeint
                " {image=popularicon} Two girls who seem popular. {image=popularicon} ":
                    " Either you also wanna be popular, or you just wanna sit with them cause they're cool. "
                    " Hopefully this doesn't end up like Heathers the musical. "
                    " Theres only two of them, anyway. You're probably about to become the third. "
                    jump popularcafeint
                " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                    " He seems to be playing with a few cat toys out of boredom... "
                    " How cute! You walk up to him and sit next to him. "
                    jump cubbiecafeint
        elif claireknow,popularknow == True and cubbieknow == False:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    " You walk up to Claire who seems to be reading something. "
                    jump clairecafeint
                " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                    " Time to see what drama they've got for you for today. "
                    jump popularcafeint
                " {image=cubbieicon} A cute little cat! {image=cubbieicon} ":
                    " Who wouldn't wanna sit next to a cute looking cat? "
                    " Upon closer looks, they have a sharpener for a body. "
                    " Still absolutely adorable though! You made no hesitation on sitting right next to them. "
                    jump cubbiecafeint
        elif claireknow,cubbieknow == True and popularknow == False:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    " You walk up to Claire who seems to be reading something. "
                    jump clairecafeint
                " {image=popularicon} Two girls who seem popular. {image=popularicon} ":
                    " Either you also wanna be popular, or you just wanna sit with them cause they're cool. "
                    " Hopefully this doesn't end up like Heathers the musical. "
                    " Theres only two of them, anyway. You're probably about to become the third. "
                    jump popularcafeint
                " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                    " He seems to be playing with a few cat toys out of boredom... "
                    " How cute! You walk up to him and sit next to him. "
                    jump cubbiecafeint
        elif popularknow,cubbieknow == True and claireknow == False:
            menu:
                " {image=claireicon} A girl with short white hair and a bow on her {image=claireicon} ":
                    " She seems to be reading something... "
                    " Let's go disturb her. "
                    jump clairecafeint
                " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                    " Time to see what drama they've got for you for today. "
                    jump popularcafeint
                " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                    " He seems to be playing with a few cat toys out of boredom... "
                    " How cute! You walk up to him and sit next to him. "
                    jump cubbiecafeint
        elif claireknow,popularknow,cubbieknow == True:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    " You walk up to Claire who seems to be reading something. "
                    jump clairecafeint
                " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                    " Time to see what drama they've got for you for today. "
                    jump popularcafeint
                " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                    " He seems to be playing with a few cat toys out of boredom... "
                    " How cute! You walk up to him and sit next to him. "
                    jump cubbiecafeint
        else:
            menu:
                " {image=claireicon} A girl with short white hair and a bow on her {image=claireicon} ":
                    " She seems to be reading something... "
                    " Let's go disturb her. "
                    jump clairecafeint
                " {image=popularicon} Two girls who seem popular. {image=popularicon} ":
                    " Either you also wanna be popular, or you just wanna sit with them cause they're cool. "
                    " Hopefully this doesn't end up like Heathers the musical. "
                    " Theres only two of them, anyway. You're probably about to become the third. "
                    jump popularcafeint
                " {image=cubbieicon} A cute little cat! {image=cubbieicon} ":
                    " Who wouldn't wanna sit next to a cute looking cat? "
                    " Upon closer looks, they have a sharpener for a body. "
                    " Still absolutely adorable though! You made no hesitation on sitting right next to them. "
                    jump cubbiecafeint
        label clairecafeint:
            if mean == True and clairebeatup == True:
                " You walk up to Claire and sit next to her, curious on what she's reading. "
                show claireneutral at center with easeinright
                " Well, she seems quite focused... "
                " You leaned in a bit to see what she was reading, and saw it was a book about people playing minigames until theres one left. "
                " Each of them die everytime they fail a minigame. "
                " It's called... octupus game. What an odd name... "
                " You're sure that you won't live even for a second in there. Terrifying. "
                " Eventually, Claire notices that you're there and she decides to greet you. "
                hide claireneutral at bottom
                show clairehappy at center
                c " Hi there, [name]! "
                c " I'm just reading this cool new book that Bubble had recommended me, "
                c " It's very trending, according to her! "
                c " Basically, 69 people are all on an island and they get to go through minigames! "
                c " If you fail, you die.. "
                c " And the prize if you win is 69 million dollars! That's why everyone wants to win! "
                c " Sounds cool, right? "
                hide clairehappy at bottom
                show claireneutral at center
                c " Well, I mean... except about the dying part. They're pretty gruesome and they give a very detailed explanation on how they die... "
                c " You wanna read it with me? "
                menu:
                    " Sure ":
                        c " Alrighty! Should I start at the very beginning, or...? "
                        scene black with dissolve
                        " You read octupus game with Claire. "
                        " There were some points in the book that Claire didn't really agree with, like one of her favorite characters dying, "
                        " But it happens. It happens a lot in other shows to make someones favorite character to die. "
                        " Either the author wants to make other people cry about it, or they just wanted to do it for fun. "
                        " It was nicely written, though. You could go for another hour of reading this... "
                        play sound "audio/bellring.mp3"
                        " Unfortunately, the bell says no to that. You've still got classes to go to, [name]! "
                        " You and Claire both get up from the seats and walk to the next class of the day. "
                        pause 2.0
                        jump historyclass1
                    " Nah, I'd just chill with you. ":
                        c " Okay! But don't mind me whenever I rant about something in the book, alright? "
                        scene black with dissolve
                        " You sat with Claire as she read her book, often talking about school as she did. "
                        " She would sometimes just be a little bit mad over certain things that happen in the book, but that's normal. "
                        " I would've cried too if Shrek died. Wait... this isn't even about shrek. Am I high? Probably. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, and you n Claire both get up to go to your next class. "
                        pause 2.0
                        jump historyclass1
            elif mean == True and clairebeatup == False:
                " On second thought... "
                " Maybe approaching Claire isn't a good idea. "
                " After all, you did hurt her feelings. "
                " Instead of approaching her, you go ahead and sit alone on an empty table. "
                " ...It kinda sucks being alone like this, does it not? "
                " Setting the fact that you can have peace aside, being too lonely starts feeling weird. "
                " You try to shake off the unsettling feeling by scrolling on your phone for the rest of the break. "
                " ...Maybe you shouldn't have hit her like that. But it's too late to turn back now. "
                scene black with dissolve
                play sound "audio/bellring.mp3"
                " You stay in the cafeteria until the bell rings. "
                " You get up from your seat and you catch a glimpse of Claire enjoying her time with her friends. "
                " She looks happy... Maybe you've done something wrong. "
                " ... "
                stop music fadeout 0.5
                " This is weak. All too weak. Emotions are weak. "
                " What you did was right, you hit her and you didn't need her help, you could get up on your own. "
                play music "audio/concern.mp3" fadein 0.5
                " Why did she think that you needed her help? You don't need anyone's help. "
                " You could do everything all on your own. "
                " You could do better. "
                stop music
                play music "audio/worry.mp3"
                " {sc}BE{/sc} better. Be better than everyone else in this school. "
                " You don't need anyone. You don't need friends. "
                " There was no point in making friends in this school, you're only going to use them for your own selfish shit. "
                stop music fadeout 0.5
                " ...You take a moment to calm yourself. "
                " You should probably stop thinking this way. But you don't know how. "
                play music "audio/paperhigh.mp3" fadein 0.5
                " You're going to be late to class, so you skedaddle on over to your classroom. "
                scene black with dissolve
                pause 2.0
                jump historyclass1
            else:
                " You walk up to Claire and sit next to her, curious on what she's reading. "
                show claireneutral at center with easeinright
                " Well, she seems quite focused... "
                " You leaned in a bit to see what she was reading, and saw it was a book about people playing minigames until theres one left. "
                " Each of them die everytime they fail a minigame. "
                " It's called... octupus game. What an odd name... "
                " You're sure that you won't live even for a second in there. Terrifying. "
                " Eventually, Claire notices that you're there and she decides to greet you. "
                hide claireneutral at bottom
                show clairehappy at center
                c " Hi there, [name]! "
                c " I'm just reading this cool new book that Bubble had recommended me, "
                c " It's very trending, according to her! "
                c " Basically, 69 people are all on an island and they get to go through minigames! "
                c " If you fail, you die.. "
                c " And the prize if you win is 69 million dollars! That's why everyone wants to win! "
                c " Sounds cool, right? "
                hide clairehappy at bottom
                show claireneutral at center
                c " Well, I mean... except about the dying part. They're pretty gruesome and they give a very detailed explanation on how they die... "
                c " You wanna read it with me? "
                menu:
                    " Sure ":
                        c " Alrighty! Should I start at the very beginning, or...? "
                        scene black with dissolve
                        " You read octupus game with Claire. "
                        " There were some points in the book that Claire didn't really agree with, like one of her favorite characters dying, "
                        " But it happens. It happens a lot in other shows to make someones favorite character to die. "
                        " Either the author wants to make other people cry about it, or they just wanted to do it for fun. "
                        " It was nicely written, though. You could go for another hour of reading this... "
                        play sound "audio/bellring.mp3"
                        " Unfortunately, the bell says no to that. You've still got classes to go to, [name]! "
                        " You and Claire both get up from the seats and walk to the next class of the day. "
                        pause 2.0
                        jump historyclass1
                    " Nah, I'd just chill with you. ":
                        c " Okay! But don't mind me whenever I rant about something in the book, alright? "
                        scene black with dissolve
                        " You sat with Claire as she read her book, often talking about school as she did. "
                        " She would sometimes just be a little bit mad over certain things that happen in the book, but that's normal. "
                        " I would've cried too if Shrek died. Wait... this isn't even about shrek. Am I high? Probably. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, and you n Claire both get up to go to your next class. "
                        pause 2.0
                        jump historyclass1
        label popularcafeint:
            " You walk up and sit next to the two popular girls, wondering what srts of drama they've been talking about. "
            show lizzyneutral at left with easeinleft
            show petunianeutral at right with easeinleft
            if popularknow == True:
                p " Did you hear? Zip told Abbie death threats not too long ago. "
                lz " What? why? what did Abbie do? "
                p " Apparently, it was about Oliver being suspended until wednesday. "
                p " That's a stupid reason to give someone death threats, is it not? "
                lz " It is. Plus, it's just going to be until wednesday. It isn't a big deal. "
                p " It's a big deal to them. They always make everything a big deal, whenever something bad happens to them. "
                p " It's expected that they would act like this, at this point... "
                lz " Mm... "
                lz " Hey there, [name]. You heard about the stuff we just talked about? "
                hide petunianeutral at bottom
                show petuniasad at right
                p " It's really just some bullshit Oliver and his gang is throwing. Like, seriously... you should expect to get a punishment for almost choking a kid to death. "
                lz " Uh huh... Sometimes I question their sanity. "
                p " Can't forget to question how much braincells they have. "
                lz " They probably don't have any, judging by how they act. "
                hide petuniasad at bottom
                show petunianeutral at right
                p " Mhm. They don't seem to think when they're about to do something stupid. "
                lz " Do they even think at all? "
                p " Please, all they're thinking about is ways to absolutely wreck this school. "
                p " One day, the school might have a fire or the school's just gonna be all broken and turned into nothingness. "
                p " But they probably won't go that far. Probably. "
                scene black with dissolve
                " You talked with Petunia and Lizzy about the recent drama that's been going on in the school... "
                " Geez. This school is just filled with drama here and there... "
                " You've seen schools with drama, but not this much. "
                " This school is so chaotic... "
                " ...Just the way you like it. "
                play sound "audio/bellring.mp3"
                " The bell rings. You, including everyone else gets up from their seats and goes to the next class. "
                pause 2.0
                jump historyclass1
            else:
                x " Did you hear? Zip told Abbie death threats not too long ago. "
                x " What? why? what did Abbie do? "
                x " Apparently, it was about Oliver being suspended until wednesday. "
                x " That's a stupid reason to give someone death threats, is it not? "
                x " It is. Plus, it's just going to be until wednesday. It isn't a big deal. "
                x " It's a big deal to them. They always make everything a big deal, whenever something bad happens to them. "
                x " It's expected that they would act like this, at this point... "
                x " Mm... "
                x " Oh. Hey, you're that new kid. "
                x " How about we introduce ourselves? "
                $ popularknow = True
                lz " I'm Lizzy. This is my best friend, Petunia. "
                lz " We like to hang out a lot. We're inseparable. "
                hide petunianeutral at bottom
                show petuniahappy at right
                p " Yeah! We're always by eachother's side, no matter what! "
                hide petuniahappy at bottom
                show petunianeutral at right
                lz " Anyway, [name]... you heard about the stuff we just talked about? "
                hide petunianeutral at bottom
                show petuniasad at right
                p " It's really just some bullshit Oliver and his gang is throwing. Like, seriously... you should expect to get a punishment for almost choking a kid to death. "
                lz " Uh huh... Sometimes I question their sanity. "
                p " Can't forget to question how much braincells they have. "
                lz " They probably don't have any, judging by how they act. "
                hide petuniasad at bottom
                show petunianeutral at right
                p " Mhm. They don't seem to think when they're about to do something stupid. "
                lz " Do they even think at all? "
                p " Please, all they're thinking about is ways to absolutely wreck this school. "
                p " One day, the school might have a fire or the school's just gonna be all broken and turned into nothingness. "
                p " But they probably won't go that far. Probably. "
                scene black with dissolve
                " You talked with Petunia and Lizzy about the recent drama that's been going on in the school... "
                " Geez. This school is just filled with drama here and there... "
                " You've seen schools with drama, but not this much. "
                " This school is so chaotic... "
                " ...Just the way you like it. "
                play sound "audio/bellring.mp3"
                " The bell rings. You, including everyone else gets up from their seats and goes to the next class. "
                pause 2.0
                jump historyclass1
        label cubbiecafeint:
            " You walk up to the adorable looking cat, and sit next to him... What a cutie! "
            " You've heard that he's mute though, so you gotta find a way to communicate with him. "
            show cubbieneutral at center
            if cubbieknow == True:
                " Cubbie plays around with his mouse toy on the table, since he was bored and had nothing to do. "
                " Eventually, he stares at you with his big wide orbs...{w=1}GAHHH HE'S SO ADORABKLE{nw} "
                hide cubbieneutral at bottom
                show cubbiehappy at center
                cb " !! "
                " He seems happy to see you. "
                hide cubbiehappy at bottom
                show cubbieneutral at center
                " You thought about others statements and then you thought about that one time you heard Cubbie talk... "
                " You question him if he's selectively mute, or he just prefers not to speak. "
                cb " ... "
                cb " ...I can speak, I just prefer not to... "
                cb " I think my voice sounds a little weird, so I usually just write to express myself... "
                " ...Well, that's understandable. "
                " I mean, the guy you're playing right not doesn't even speak unless I say that you did or you make an option. "
                " Maybe you two would become good friends. "
                cb " ... "
                " Cubbie seems to be asking you if you could play around with him. He has this little extra mouse with him... "
                " It seems as though he wanted a break from studying all the time. "
                " Play around with him? "
                menu:
                    " Yeah ":
                        $ cubbielv += 10
                        hide cubbieneutral at bottom
                        show cubbieamazed at center
                        cb " ...!! "
                        " Seems like Cubbie got really happy at that. "
                        scene black with dissolve
                        " You played around with the mouses that Cubbie gave, and you were honestly starting to enjoy it. "
                        " It's like you're a kid again, playing with the little toys you had... "
                        " ...How you miss being a kid. You're probably all grown up now and you've grown out of playing with toys. "
                        " Everything was so simple back then, but now you probably have to deal with assignments or schoolwork out in the real world. "
                        " Everything was brighter when you were a kid, where's all of that now? "
                        " Even so, you can always enjoy life as best as you can whilst you're still alive and breathing. "
                        " Take breaks every now and then, take a breather, spend time with your friends and family... "
                        " There's no time machine to go back to how it was backthen. And so, you must continue to live the best out of your life. "
                        play sound "audio/bellring.mp3"
                        " ...Well that's enough of the inspiring messages! "
                        " Back to the game, you get up from your seat and walk to your next class. "
                        " But really, please take care of yourself. "
                        pause 2.0
                        jump historyclass1
                    " Nah ":
                        " Cubbie seems to respect your decision, and he continues playing with his mouse. "
                        " He's so adorable...I mean, he IS a cat. All cats are cute. "
                        " Yes trisha, even the bald ones. "
                        scene black with dissolve
                        " You continued to hang around with Cubbie for a bit, watching him goof around. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, as per usual, and you get up to go to your next class. "
                        pause 2.0
                        jump historyclass1
            else:
                " The cat plays around with his mouse toy on the table, since he was bored and had nothing to do. "
                " Eventually, he stares at you with his big wide orbs...{w=1}GAHHH HE'S SO ADORABKLE{nw} "
                " You've heard that this kid's name is Cubbie. What an adorable name for a adorable little guy! "
                $ cubbieknow = True
                hide cubbieneutral at bottom
                show cubbiehappy at center
                cb " !! "
                " He seems happy to see you. "
                hide cubbiehappy at bottom
                show cubbieneutral at center
                " You thought about others statements and then you thought about that one time you heard Cubbie talk... "
                " You question him if he's selectively mute, or he just prefers not to speak. "
                cb " ... "
                cb " ...I can speak, I just prefer not to... "
                cb " I think my voice sounds a little weird, so I usually just write to express myself... "
                " ...Well, that's understandable. "
                " I mean, the guy you're playing right not doesn't even speak unless I say that you did or you make an option. "
                " Maybe you two would become good friends. "
                cb " ... "
                " Cubbie seems to be asking you if you could play around with him. He has this little extra mouse with him... "
                " It seems as though he wanted a break from studying all the time. "
                " Play around with him? "
                menu:
                    " Yeah ":
                        $ cubbielv += 10
                        hide cubbieneutral at bottom
                        show cubbieamazed at center
                        cb " ...!! "
                        " Seems like Cubbie got really happy at that. "
                        scene black with dissolve
                        " You played around with the mouses that Cubbie gave, and you were honestly starting to enjoy it. "
                        " It's like you're a kid again, playing with the little toys you had... "
                        " ...How you miss being a kid. You're probably all grown up now and you've grown out of playing with toys. "
                        " Everything was so simple back then, but now you probably have to deal with assignments or schoolwork out in the real world. "
                        " Everything was brighter when you were a kid, where's all of that now? "
                        " Even so, you can always enjoy life as best as you can whilst you're still alive and breathing. "
                        " Take breaks every now and then, take a breather, spend time with your friends and family... "
                        " There's no time machine to go back to how it was backthen. And so, you must continue to live the best out of your life. "
                        play sound "audio/bellring.mp3"
                        " ...Well that's enough of the inspiring messages! "
                        " Back to the game, you get up from your seat and walk to your next class. "
                        " But really, please take care of yourself. "
                        pause 2.0
                        jump historyclass1
                    " Nah ":
                        " Cubbie seems to respect your decision, and he continues playing with his mouse. "
                        " He's so adorable...I mean, he IS a cat. All cats are cute. "
                        " Yes trisha, even the bald ones. "
                        scene black with dissolve
                        " You continued to hang around with Cubbie for a bit, watching him goof around. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, as per usual, and you get up to go to your next class. "
                        pause 2.0
                        jump historyclass1
    label rooftop3:
        scene rooftop with dissolve
        # Riley + Lana
        " Ah yes, you could finally get some fresh air-{nw} "
        x " OLIVER IS SO HOT!!! " with vpunch
        " ...Oh boy. And you thought you were gonna get some peace and quiet up here... "
        " You decide to walk over to where the noise was, curiously. "
        show lananeutral at left with easeinright
        show rileyhappy at right with easeinright
        if lanaknow == True and rileyknow == True:
            ri " Ouuuhh, I just wonder when I'll become his one and only girlfriend! He's just so perfect! "
            l " Erh, that's nice, Riley, but doesn't Oliver already have a girlfriend?-{nw} "
            ri " EEEEEEE!! I LOVE HIM SO MUCHH!! " with vpunch
            l " ...Yeah... I know you do, Riley. I know you do. "
            " You could tell Lana was cringing internally because of Riley. "
            " You could feel yourself cringing as well, but you should probably get used to it if Riley's gonna always act like this. "
            " Whilst Riley was continuing her yapping about Oliver in the background, Lana whispered to you. "
            l " [name]... she's just gonna keep yapping and yapping, isn't she...? "
            l " I honestly don't know how to feel about this, is this what Ruby and Skell have to deal with everyday...? "
            l " I just wanted to talk about this new game I found with her, but when I mentioned that there was a character named Oliver, she suddenly went batshit crazy! "
            l " And now, I've been standing here putting a smile on my face and nodding and pretending that I'm listening to her... "
            l " Was it a bad idea to show her this game...? "
            l " ...You know what, I'm gonna leave. She's distracted anyway... "
            l " She's not gonna notice, don't worry! If you wanna leave too, you can leave with me, no worries! "
            hide lananeutral at left with easeoutleft
            menu:
                " Leave with Lana ":
                    " Yeah, you're not gonna listen to all of this. "
                    " Time to skedaddle on outta here! "
                    scene black with dissolve
                    pause 2.0
                    scene hallway with dissolve
                    show lananeutral at center with easeinleft
                    l " Alrighty, we're away... "
                    l " Though... what should we do now? "
                    l " We can't just stand here for the rest of the break. "
                    " ... "
                    mc " did you know i paid 50k for a video of sans undertale buff{nw} "
                    l " YOU CAN TALK???{nw} "
                    scene black
                    pause 2.0
                    jump historyclass1
                " Stay with Riley ":
                    " You chose to stick around with Riley for a bit longer. "
                    " The question is... "
                    " ...How are you going to endure all of this yapping. "
                    " You don't know. I don't know either. I guess you're just that good of a listener. "
                    " All she yaps about it Oliver and nothing else, so this should be easy to go through. "
                    " Whilst there are some questionable comments about Oliver, it's kinda normal for a girl like Riley to be acting like this. "
                    " I mean... It's Riley. It should be expected that she'd go batshit insane over Oliver. "
                    play sound "audio/bellring.mp3"
                    " She doesn't even stop when the bell rings... "
                    scene black with dissolve
                    " She talks to you about Oliver all the way until you reach the classroom for the next class. "
                    pause 2.0
                    jump historyclass1
        elif lanaknow == True and rileyknow == False:
            x " Ouuuhh, I just wonder when I'll become his one and only girlfriend! He's just so perfect! "
            l " Erh, that's nice, Riley, but doesn't Oliver already have a girlfriend?-{nw} "
            x " EEEEEEE!! I LOVE HIM SO MUCHH!! " with vpunch
            l " ...Yeah... I know you do, Riley. I know you do. "
            " You could tell Lana was cringing internally because of Riley. "
            " You could feel yourself cringing as well, but you should probably get used to it if this girl's gonna always act like this. "
            " Whilst the girl was continuing her yapping about Oliver in the background, Lana whispered to you. "
            l " [name]... she's just gonna keep yapping and yapping, isn't she...? "
            l " I honestly don't know how to feel about this, is this what Ruby and Skell have to deal with everyday...? "
            l " I just wanted to talk about this new game I found with her, but when I mentioned that there was a character named Oliver, she suddenly went batshit crazy! "
            l " And now, I've been standing here putting a smile on my face and nodding and pretending that I'm listening to her... "
            l " Was it a bad idea to show her this game...? "
            l " ...You know what, I'm gonna leave. She's distracted anyway... "
            l " She's not gonna notice, don't worry! If you wanna leave too, you can leave with me, no worries! "
            hide lananeutral at left with easeoutleft
            menu:
                " Leave with Lana ":
                    " Yeah, you're not gonna listen to all of this. "
                    " Time to skedaddle on outta here! "
                    scene black with dissolve
                    pause 2.0
                    scene hallway with dissolve
                    show lananeutral at center with easeinleft
                    l " Alrighty, we're away... "
                    l " Though... what should we do now? "
                    l " We can't just stand here for the rest of the break. "
                    " ... "
                    mc " did you know i paid 50k for a video of sans undertale buff{nw} "
                    l " YOU CAN TALK???{nw} "
                    scene black
                    pause 2.0
                    jump historyclass1
                " Stay with Riley ":
                    " You chose to stick around with Riley for a bit longer. "
                    " The question is... "
                    " ...How are you going to endure all of this yapping. "
                    " You don't know. I don't know either. I guess you're just that good of a listener. "
                    " All she yaps about it Oliver and nothing else, so this should be easy to go through. "
                    " Whilst there are some questionable comments about Oliver, it's kinda normal for a girl like Riley to be acting like this. "
                    " I mean... It's Riley. It should be expected that she'd go batshit insane over Oliver. "
                    play sound "audio/bellring.mp3"
                    " She doesn't even stop when the bell rings... "
                    scene black with dissolve
                    " She talks to you about Oliver all the way until you reach the classroom for the next class. "
                    pause 2.0
                    jump historyclass1
        elif lanaknow == False and rileyknow == True:
            ri " Ouuuhh, I just wonder when I'll become his one and only girlfriend! He's just so perfect! "
            x " Erh, that's nice, Riley, but doesn't Oliver already have a girlfriend?-{nw} "
            ri " EEEEEEE!! I LOVE HIM SO MUCHH!! " with vpunch
            x " ...Yeah... I know you do, Riley. I know you do. "
            " You could tell the other girl was cringing internally because of Riley. "
            " You could feel yourself cringing as well, but you should probably get used to it if Riley's gonna always act like this. "
            " Whilst Riley was continuing her yapping about Oliver in the background, the opther girl next to you whispered to you. "
            x " [name]... she's just gonna keep yapping and yapping, isn't she...? "
            x " I honestly don't know how to feel about this, is this what Ruby and Skell have to deal with everyday...? "
            x " I just wanted to talk about this new game I found with her, but when I mentioned that there was a character named Oliver, she suddenly went batshit crazy! "
            x " And now, I've been standing here putting a smile on my face and nodding and pretending that I'm listening to her... "
            x " Was it a bad idea to show her this game...? "
            x " ...You know what, I'm gonna leave. She's distracted anyway... "
            x " She's not gonna notice, don't worry! If you wanna leave too, you can leave with me, no worries! "
            hide lananeutral at left with easeoutleft
            menu:
                " Leave with Lana ":
                    " Yeah, you're not gonna listen to all of this. "
                    " Time to skedaddle on outta here! "
                    scene black with dissolve
                    pause 2.0
                    scene hallway with dissolve
                    show lananeutral at center with easeinleft
                    x " Alrighty, we're away... "
                    x " Though... what should we do now? "
                    x " We can't just stand here for the rest of the break. "
                    x " Oh right! I haven't introduced myself properly! "
                    l " I'm Lana! Good to meet you! The girl from earlier is called Riley. "
                    l " She always acts like that, so yes, it's normal... "
                    $ lanaknow = True
                    $ rileyknow = True
                    l " Now... what else do we talk about...? "
                    " ... "
                    mc " did you know i paid 50k for a video of sans undertale buff{nw} "
                    l " YOU CAN TALK???{nw} "
                    scene black
                    pause 2.0
                    jump historyclass1
                " Stay with Riley ":
                    " You chose to stick around with Riley for a bit longer. "
                    " The question is... "
                    " ...How are you going to endure all of this yapping. "
                    " You don't know. I don't know either. I guess you're just that good of a listener. "
                    " All she yaps about it Oliver and nothing else, so this should be easy to go through. "
                    " Whilst there are some questionable comments about Oliver, it's kinda normal for a girl like Riley to be acting like this. "
                    " I mean... It's Riley. It should be expected that she'd go batshit insane over Oliver. "
                    play sound "audio/bellring.mp3"
                    " She doesn't even stop when the bell rings... "
                    scene black with dissolve
                    " She talks to you about Oliver all the way until you reach the classroom for the next class. "
                    pause 2.0
                    jump historyclass1
        else:
            x " Ouuuhh, I just wonder when I'll become his one and only girlfriend! He's just so perfect! "
            x " Erh, that's nice, Riley, but doesn't Oliver already have a girlfriend?-{nw} "
            x " EEEEEEE!! I LOVE HIM SO MUCHH!! " with vpunch
            x " ...Yeah... I know you do, Riley. I know you do. "
            " You could tell the other girl was cringing internally because of Riley. "
            " You could feel yourself cringing as well, but you should probably get used to it if Riley's gonna always act like this. "
            " Whilst Riley was continuing her yapping about Oliver in the background, the opther girl next to you whispered to you. "
            x " [name]... she's just gonna keep yapping and yapping, isn't she...? "
            x " I honestly don't know how to feel about this, is this what Ruby and Skell have to deal with everyday...? "
            x " I just wanted to talk about this new game I found with her, but when I mentioned that there was a character named Oliver, she suddenly went batshit crazy! "
            x " And now, I've been standing here putting a smile on my face and nodding and pretending that I'm listening to her... "
            x " Was it a bad idea to show her this game...? "
            x " ...You know what, I'm gonna leave. She's distracted anyway... "
            x " She's not gonna notice, don't worry! If you wanna leave too, you can leave with me, no worries! "
            hide lananeutral at left with easeoutleft
            menu:
                " Leave with Lana ":
                    " Yeah, you're not gonna listen to all of this. "
                    " Time to skedaddle on outta here! "
                    scene black with dissolve
                    pause 2.0
                    scene hallway with dissolve
                    show lananeutral at center with easeinleft
                    x " Alrighty, we're away... "
                    x " Though... what should we do now? "
                    x " We can't just stand here for the rest of the break. "
                    x " Oh right! I haven't introduced myself properly! "
                    l " I'm Lana! Good to meet you! The girl from earlier is called Riley. "
                    l " She always acts like that, so yes, it's normal... "
                    $ lanaknow = True
                    $ rileyknow = True
                    l " Now... what else do we talk about...? "
                    " ... "
                    mc " did you know i paid 50k for a video of sans undertale buff{nw} "
                    l " YOU CAN TALK???{nw} "
                    scene black
                    pause 2.0
                    jump historyclass1
                " Stay with Riley ":
                    $ rileyknow = True
                    " You chose to stick around with Riley for a bit longer. "
                    " The question is... "
                    " ...How are you going to endure all of this yapping. "
                    " You don't know. I don't know either. I guess you're just that good of a listener. "
                    " All she yaps about it Oliver and nothing else, so this should be easy to go through. "
                    " Whilst there are some questionable comments about Oliver, it's kinda normal for a girl like Riley to be acting like this. "
                    " I mean... It's Riley. It should be expected that she'd go batshit insane over Oliver. "
                    play sound "audio/bellring.mp3"
                    " She doesn't even stop when the bell rings... "
                    scene black with dissolve
                    " She talks to you about Oliver all the way until you reach the classroom for the next class. "
                    pause 2.0
                    jump historyclass1
    label library3:
        scene library with dissolve
        # Kevin + Robby
        " The library, quiet as ever... "
        " You walked around for a bit, seeing other people read their own books. "
        " Most of the other people were weird looking monster things, like a tiny little giraffe. "
        " Other people were actual humans... they were still cute, though. Animals and humans are cute. "
        " Though, out of all of the people in the library, two people have managed to catch your interest. "
        " Two nerds... How did they catch your attention? You don't know. They look like your average stereotypical school nerds, "
        " But something makes them more interesting, somehow. "
        show kevinneutral at left with easeinright
        show robbyneutral at right with easeinright
        if kevinknow == True and robbyknow == True:
            " Turns out it was Kevin and Robby that had caught your attention. "
            " Seriously, how did these two get your attention instead of anyone else? "
            " I don't know myself, I'm gonna go ask the programmer. "
            " ... "
            " He said that it was for plot reasons. Or something. "
            " What? He {i}had{/i} to make a interaction with these two. For game reasons. "
            " Anyway, they seem to be talking about something. Let's listen in. "
            kv " So turns out, 10 + 10 is NOT 1010... "
            rb " Really? You just noticed now? "
            kv " Yeeeaaah, no wonder why I've been sort of fumbling simple questions in math... "
            rb " So, you just looked at a calculator and figured out that 10 + 10 is 20. "
            hide kevinneutral at bottom
            show kevinsad at left
            kv " ...Yeah. "
            rb " Hey dude, it's fine. Mistakes like that happen. "
            rb " (but seriously, how'd you think 10 + 10 is 1010 for your entire life...) "
            rb " Atleast you didn't fumble too big. Now you know that it's 20. "
            hide kevinsad at bottom
            show kevinneutral at left
            kv " Mhm. "
            kv " Hello there, [name]. "
            rb " Oh. Hey there, [name]. We're just chilling. "
            rb " I had to fix Cubbie's toy earlier because Riley broke it. "
            kv " Uh? why did she break it? "
            rb " She was rambling about Oliver and she got too feral, holding onto it and accidentally splitting it into two. "
            kv " Geez...why's she so interested in Oliver anyway? If I had a crush, I wouldn't act like that. "
            rb " Don't know. Wait, isn't Oliver from a different school? What's he doing in here anyway? "
            kv " Don't know either. It's gonna be hard to ask him because he's mostly off bullying people. "
            kv " ...And it's also going to be dangerous, because there's a chance he'll just beat me up. "
            rb " Yeah, that sounds like him, alright... "
            rb " Some questions are better left unanswered, is what they would say. "
            scene black with dissolve
            " You hung out with Robby and Kevin for the rest of the break. "
            " They mostly talked about school, and only a little bit talked about something else. "
            " Wow, you really chose to hang out with a couple of nerds for an entire break. "
            " Not like you had an option to leave, anyway. "
            " Unless if you clicked the back button. Then you could've just chose something else. "
            " Or you jsut wanted to see what would happen. "
            " ...I've probably said that previous line too much in this game. "
            " Probably. "
            play sound "audio/bellring.mp3"
            " The bell rings. You, Kevin, and Robby get up and going to the next class. "
            pause 2.0
            jump historyclass1
        elif kevinknow == True and robbyknow == False:
            " Turns out it was Kevin and another nerd that you don't know that had caught your attention. "
            " Seriously, how did these two get your attention instead of anyone else? "
            " I don't know myself, I'm gonna go ask the programmer. "
            " ... "
            " He said that it was for plot reasons. Or something. "
            " What? He {i}had{/i} to make a interaction with these two. For game reasons. "
            " Anyway, they seem to be talking about something. Let's listen in. "
            kv " So turns out, 10 + 10 is NOT 1010... "
            x " Really? You just noticed now? "
            kv " Yeeeaaah, no wonder why I've been sort of fumbling simple questions in math... "
            x " So, you just looked at a calculator and figured out that 10 + 10 is 20. "
            hide kevinneutral at bottom
            show kevinsad at left
            kv " ...Yeah. "
            x " Hey dude, it's fine. Mistakes like that happen. "
            x " (but seriously, how'd you think 10 + 10 is 1010 for your entire life...) "
            x " Atleast you didn't fumble too big. Now you know that it's 20. "
            hide kevinsad at bottom
            show kevinneutral at left
            kv " Mhm. "
            kv " Hello there, [name]. "
            x " Oh. Hey there, [name]. We're just chilling. "
            x " And, uh, I don't think I got to introduce myself to you. So... "
            $ robbyknow = True
            rb " I'm Robby. I like to fix stuff. And speaking of fixing stuff... "
            rb " I had to fix Cubbie's toy earlier because Riley broke it. "
            kv " Uh? why did she break it? "
            rb " She was rambling about Oliver and she got too feral, holding onto it and accidentally splitting it into two. "
            kv " Geez...why's she so interested in Oliver anyway? If I had a crush, I wouldn't act like that. "
            rb " Don't know. Wait, isn't Oliver from a different school? What's he doing in here anyway? "
            kv " Don't know either. It's gonna be hard to ask him because he's mostly off bullying people. "
            kv " ...And it's also going to be dangerous, because there's a chance he'll just beat me up. "
            rb " Yeah, that sounds like him, alright... "
            rb " Some questions are better left unanswered, is what they would say. "
            scene black with dissolve
            " You hung out with Robby and Kevin for the rest of the break. "
            " They mostly talked about school, and only a little bit talked about something else. "
            " Wow, you really chose to hang out with a couple of nerds for an entire break. "
            " Not like you had an option to leave, anyway. "
            " Unless if you clicked the back button. Then you could've just chose something else. "
            " Or you jsut wanted to see what would happen. "
            " ...I've probably said that previous line too much in this game. "
            " Probably. "
            play sound "audio/bellring.mp3"
            " The bell rings. You, Kevin, and Robby get up and going to the next class. "
            pause 2.0
            jump historyclass1
        elif kevinknow == False and robbyknow == True:
            " Turns out it was a nerd you didn't recognize and Robby that had caught your attention. "
            " Seriously, how did these two get your attention instead of anyone else? "
            " I don't know myself, I'm gonna go ask the programmer. "
            " ... "
            " He said that it was for plot reasons. Or something. "
            " What? He {i}had{/i} to make a interaction with these two. For game reasons. "
            " Anyway, they seem to be talking about something. Let's listen in. "
            x " So turns out, 10 + 10 is NOT 1010... "
            rb " Really? You just noticed now? "
            x " Yeeeaaah, no wonder why I've been sort of fumbling simple questions in math... "
            rb " So, you just looked at a calculator and figured out that 10 + 10 is 20. "
            hide kevinneutral at bottom
            show kevinsad at left
            x " ...Yeah. "
            rb " Hey dude, it's fine. Mistakes like that happen. "
            rb " (but seriously, how'd you think 10 + 10 is 1010 for your entire life...) "
            rb " Atleast you didn't fumble too big. Now you know that it's 20. "
            hide kevinsad at bottom
            show kevinneutral at left
            x " Mhm. "
            x " Hello there, [name]. "
            rb " Oh. Hey there, [name]. We're just chilling. "
            rb " I had to fix Cubbie's toy earlier because Riley broke it. "
            x " Wait - I just realized I haven't introduced myself to [name] yet. "
            $ kevinknow = True
            kv " I'm Kevin. It's a pleasure to meet you, [name]. "
            kv " Anywho... "
            kv " Robby, why did Riley break Cubbie's toy? "
            rb " She was rambling about Oliver and she got too feral, holding onto it and accidentally splitting it into two. "
            kv " Geez...why's she so interested in Oliver anyway? If I had a crush, I wouldn't act like that. "
            rb " Don't know. Wait, isn't Oliver from a different school? What's he doing in here anyway? "
            kv " Don't know either. It's gonna be hard to ask him because he's mostly off bullying people. "
            kv " ...And it's also going to be dangerous, because there's a chance he'll just beat me up. "
            rb " Yeah, that sounds like him, alright... "
            rb " Some questions are better left unanswered, is what they would say. "
            scene black with dissolve
            " You hung out with Robby and Kevin for the rest of the break. "
            " They mostly talked about school, and only a little bit talked about something else. "
            " Wow, you really chose to hang out with a couple of nerds for an entire break. "
            " Not like you had an option to leave, anyway. "
            " Unless if you clicked the back button. Then you could've just chose something else. "
            " Or you jsut wanted to see what would happen. "
            " ...I've probably said that previous line too much in this game. "
            " Probably. "
            play sound "audio/bellring.mp3"
            " The bell rings. You, Kevin, and Robby get up and going to the next class. "
            pause 2.0
            jump historyclass1
        else:
            " Turns out it was Kevin and Robby that had caught your attention. "
            " Seriously, how did these two get your attention instead of anyone else? "
            " I don't know myself, I'm gonna go ask the programmer. "
            " ... "
            " He said that it was for plot reasons. Or something. "
            " What? He {i}had{/i} to make a interaction with these two. For game reasons. "
            " Anyway, they seem to be talking about something. Let's listen in. "
            x " So turns out, 10 + 10 is NOT 1010... "
            x " Really? You just noticed now? "
            x " Yeeeaaah, no wonder why I've been sort of fumbling simple questions in math... "
            x " So, you just looked at a calculator and figured out that 10 + 10 is 20. "
            hide kevinneutral at bottom
            show kevinsad at left
            x " ...Yeah. "
            x " Hey dude, it's fine. Mistakes like that happen. "
            x " (but seriously, how'd you think 10 + 10 is 1010 for your entire life...) "
            x " Atleast you didn't fumble too big. Now you know that it's 20. "
            hide kevinsad at bottom
            show kevinneutral at left
            x " Mhm. "
            x " Hello there, [name]. "
            x " Oh. Hey there, [name]. We're just chilling. "
            x " We should probably introduce ourselves to [name] first before we do anything... "
            $ robbyknow = True
            $ kevinknow = True
            rb " Uh huh. I'm Robby. I like to fix stuff. "
            kv " And I'm Kevin. It's a pleasure to meet you, [name]. "
            rb " Gonna go and talk about the thing I wanted to say... "
            rb " I had to fix Cubbie's toy earlier because Riley broke it. "
            kv " Uh? why did she break it? "
            rb " She was rambling about Oliver and she got too feral, holding onto it and accidentally splitting it into two. "
            kv " Geez...why's she so interested in Oliver anyway? If I had a crush, I wouldn't act like that. "
            rb " Don't know. Wait, isn't Oliver from a different school? What's he doing in here anyway? "
            kv " Don't know either. It's gonna be hard to ask him because he's mostly off bullying people. "
            kv " ...And it's also going to be dangerous, because there's a chance he'll just beat me up. "
            rb " Yeah, that sounds like him, alright... "
            rb " Some questions are better left unanswered, is what they would say. "
            scene black with dissolve
            " You hung out with Robby and Kevin for the rest of the break. "
            " They mostly talked about school, and only a little bit talked about something else. "
            " Wow, you really chose to hang out with a couple of nerds for an entire break. "
            " Not like you had an option to leave, anyway. "
            " Unless if you clicked the back button. Then you could've just chose something else. "
            " Or you jsut wanted to see what would happen. "
            " ...I've probably said that previous line too much in this game. "
            " Probably. "
            play sound "audio/bellring.mp3"
            " The bell rings. You, Kevin, and Robby get up and going to the next class. "
            pause 2.0
            jump historyclass1
    label historyclass1:
        scene classroom with dissolve
        " The teacher isn't here yet, it's been 10 minutes... "
        " Where are they? It's supposed to be history class right now, from what you've heard. "
        " After 3 more minutes, you hear the door open, and the teacher steps in. "
        show msemilyshock at center with easeinleft
        mse " Whew, I'm so sorry for being a liiiittle bit too late, class. "
        mse " I had to deal with a little... problem in the hallways, that's why I was late. "
        hide msemilyshock at bottom
        show msemilyangry at center
        mse " Apparently, a kid had poured water all over the floor for a 'prank'! "
        mse " I managed to find them, and I sent them to detention. "
        hide msemilyangry at bottom
        show msemilyhappy at center
        mse " Not to worry, all of the mess has been cleaned up by our janitor! "
        mse " Without any more disruptances, let us begin our class for today! "
        scene black with dissolve
        " You sat around in history class, listening to whatever the teacher was talking about. "
        " About the thing the teacher said earlier, who thought it was a good idea to do that? "
        " In your opinion, it wasn't really that good of a prank at all. "
        " Sounds like something a little kid would do if they had a tantrum because they didn't get what they wanted. "
        " Hmm...{w=0.5} It would've been better if they flooded the whole school... "
        " No, how would they even be able to do that? "
        " You'd need like, a bunch of water for that to happen. "
        " Ms. Emily notices that you're zoning out and probably thinking of flooding the school, so she kindly makes you pay attention to the class... "
        " By whacking your head with her ruler. "
        " Yeowch. It certainly worked though. "
        play sound "audio/bellring.mp3"
        " The bell rings, and you leave the classroom to go onto the hallways. "
        pause 2.0
        jump break4
    label break4:
        scene hallway with dissolve
        " Where do you want to go now? "
        menu:
            " {image=engelicon} Front of the school {image=abbieicon} ":
                scene black with dissolve
                pause 2.0
                jump frontschool4
            " {image=skellicon} Back of the school {image=rileyicon} ":
                scene black with dissolve
                pause 2.0
                jump backschool4
            " {image=lanaicon} Gym {image=rubyicon} ":
                scene black with dissolve
                pause 2.0
                jump gym4
            " Cafeteria ":
                scene black with dissolve
                pause 2.0
                jump cafe4
            " {image=claireicon} The Rooftop {image=popularicon} ":
                scene black with dissolve
                pause 2.0
                jump rooftop4
            " {image=bubbleicon} The library {image=cubbieicon} ":
                scene black with dissolve
                pause 2.0
                jump library4
    label frontschool4:
        scene paperschoolfront with dissolve
        # engel, abbie
        " You take in the fresh air as you stepped out of the school. "
        " You walked around for a bit, admiring the trees near you as well as the plants. "
        " You then heard two people talking, near one of the bushes... "
        " You walked over, your footsteps quiet. You spotted two people talking behind the bushes... "
        show engelsad at left with easeinright
        show abbiesad at right with easeinright
        if abbieknow == True and engelknow == True:
            a " I don't know, Engel... do you really think I can stand up for myself...? "
            e " Abbie... I know you can; all you've gotta do is be strong, alright? "
            a " But everytime they do, they always knock me back down... I can't... "
            e " Abbie... "
            e " No matter how many times you fall down, you should always get back up. "
            hide engelsad at bottom
            show engelhappy at left
            e " Show no weakness, and show them that you can handle it all. "
            e " Keep getting right back up, and eventually... hit them. Hit them back as hard as you can. "
            e " Even if they make you feel horrible, don't let their words get to you. "
            e " They're only trying to bring you down, and you crying and being afraid is only getting them what they want out of you; "
            e " A reaction. "
            e " It's time to be brave, Abbie. Even if you think that it's going to be impossible. "
            e " I know you can do it. I believe in you. "
            a " ...*sniff*.. "
            hide abbiesad at bottom
            show abbiehappy at right
            a " Thanks, Engel... I appreciate it... "
            a " I'll... I'll try to be strong... "
            hide engelhappy at bottom
            show engelcontent at left
            e " You're welcome! "
            e " If you need anything else, I'll always be here to listen to you. "
            hide engelcontent at bottom
            show engelhappy at left
            e " Oooh, who's that? [name]! Hello there! "
            e " I was just comforting Abbie about... you know... what happened in the hallways. "
            a " ...Hi [name]... "
            e " I don't get why they would go ahead and attack this poor bean... "
            a " Hey, I'm not a bean... "
            e " They're just so, so mean! hurting a cute little thing... "
            a " Heeeeeyy... "
            " Engel drags you down, making you sit next to him. "
            " He then whispers to you, so that Abbie can't hear what he's planning. "
            e " (Pssst, [name]!) "
            e " (Play along with me, and shower Abbie with compliments!) "
            e " (Abbie likes being complimented, and if we can do that enough...) "
            e " (It'll get his mind off of whatever happened earlier!) "
            e " (You with me?{w=1} I'll take that silence as a yes!) "
            scene black with dissolve
            " You and Engel showered Abbie with compliments to give Abbie more positive thoughts. "
            " Well, for now. You're sure something bad is probably gonna happen later or tomorrow. "
            " You should just enjoy the moment though. Seeing Abbie being happy is nice... "
            play sound "audio/bellring.mp3"
            " You continue to do this until the bell rings. "
            " You, Engel and Abbie get up and get to the next class of the day. "
            pause 2.0
            jump musicclass1
        elif abbieknow == True and engelknow == False:
            a " I don't know, Engel... do you really think I can stand up for myself...? "
            x " Abbie... I know you can; all you've gotta do is be strong, alright? "
            a " But everytime they do, they always knock me back down... I can't... "
            x " Abbie... "
            x " No matter how many times you fall down, you should always get back up. "
            hide engelsad at bottom
            show engelhappy at left
            x " Show no weakness, and show them that you can handle it all. "
            x " Keep getting right back up, and eventually... hit them. Hit them back as hard as you can. "
            x " Even if they make you feel horrible, don't let their words get to you. "
            x " They're only trying to bring you down, and you crying and being afraid is only getting them what they want out of you; "
            x " A reaction. "
            x " It's time to be brave, Abbie. Even if you think that it's going to be impossible. "
            x " I know you can do it. I believe in you. "
            a " ...*sniff*.. "
            hide abbiesad at bottom
            show abbiehappy at right
            a " Thanks, Engel... I appreciate it... "
            a " I'll... I'll try to be strong... "
            hide engelhappy at bottom
            show engelcontent at left
            x " You're welcome! "
            x " If you need anything else, I'll always be here to listen to you. "
            hide engelcontent at bottom
            show engelhappy at left
            x " Oooh, who's that? [name]! Hello there! "
            x " I was just comforting Abbie about... you know... what happened in the hallways. "
            a " ...Hi [name]... "
            x " Abbie, is this your little friend? "
            a " Yes, [they] [are]... "
            x " Well, I'd like to introduce myself to them then! "
            $ engelknow = True
            e " I'm Engel, it's great to meet you, [name]! "
            e " Anywho... "
            e " I don't get why they would go ahead and attack this poor bean... "
            a " Hey, I'm not a bean... "
            e " They're just so, so mean! hurting a cute little thing... "
            a " Heeeeeyy... "
            " Engel drags you down, making you sit next to him. "
            " He then whispers to you, so that Abbie can't hear what he's planning. "
            e " (Pssst, [name]!) "
            e " (Play along with me, and shower Abbie with compliments!) "
            e " (Abbie likes being complimented, and if we can do that enough...) "
            e " (It'll get his mind off of whatever happened earlier!) "
            e " (You with me?{w=1} I'll take that silence as a yes!) "
            scene black with dissolve
            " You and Engel showered Abbie with compliments to give Abbie more positive thoughts. "
            " Well, for now. You're sure something bad is probably gonna happen later or tomorrow. "
            " You should just enjoy the moment though. Seeing Abbie being happy is nice... "
            play sound "audio/bellring.mp3"
            " You continue to do this until the bell rings. "
            " You, Engel and Abbie get up and get to the next class of the day. "
            pause 2.0
            jump musicclass1
        elif abbieknow == False and engelknow == True:
            x " I don't know, Engel... do you really think I can stand up for myself...? "
            e " Abbie... I know you can; all you've gotta do is be strong, alright? "
            x " But everytime they do, they always knock me back down... I can't... "
            e " Abbie... "
            e " No matter how many times you fall down, you should always get back up. "
            hide engelsad at bottom
            show engelhappy at left
            e " Show no weakness, and show them that you can handle it all. "
            e " Keep getting right back up, and eventually... hit them. Hit them back as hard as you can. "
            e " Even if they make you feel horrible, don't let their words get to you. "
            e " They're only trying to bring you down, and you crying and being afraid is only getting them what they want out of you; "
            e " A reaction. "
            e " It's time to be brave, Abbie. Even if you think that it's going to be impossible. "
            e " I know you can do it. I believe in you. "
            x " ...*sniff*.. "
            hide abbiesad at bottom
            show abbiehappy at right
            x " Thanks, Engel... I appreciate it... "
            x " I'll... I'll try to be strong... "
            hide engelhappy at bottom
            show engelcontent at left
            e " You're welcome! "
            e " If you need anything else, I'll always be here to listen to you. "
            hide engelcontent at bottom
            show engelhappy at left
            e " Oooh, who's that? [name]! Hello there! "
            e " I was just comforting Abbie about... you know... what happened in the hallways. "
            x " ...Hi [name]... "
            e " Come to think of it... Abbie, have you met [name] before? "
            hide abbiehappy at bottom
            show abbieneutral at right
            x " N-no... I didn't get to introduce myself to [them] yet... "
            e " Well then! Go ahead, Introduce yourself! "
            x " Oh, um... "
            e " Don't be shy, [they] [arent] rude or anything! Not like they'll hurt you or anything... "
            x " Okay... "
            $ abbieknow = True
            a " I'm Abbie...Nice to meet you... "
            e " There you go!! That wasn't so hard now, was it? "
            e " I don't get why they would go ahead and attack this poor bean... "
            hide abbieneutral at bottom
            show abbiehappy at right
            a " Hey, I'm not a bean... "
            e " They're just so, so mean! hurting a cute little thing... "
            a " Heeeeeyy... "
            " Engel drags you down, making you sit next to him. "
            " He then whispers to you, so that Abbie can't hear what he's planning. "
            e " (Pssst, [name]!) "
            e " (Play along with me, and shower Abbie with compliments!) "
            e " (Abbie likes being complimented, and if we can do that enough...) "
            e " (It'll get his mind off of whatever happened earlier!) "
            e " (You with me?{w=1} I'll take that silence as a yes!) "
            scene black with dissolve
            " You and Engel showered Abbie with compliments to give Abbie more positive thoughts. "
            " Well, for now. You're sure something bad is probably gonna happen later or tomorrow. "
            " You should just enjoy the moment though. Seeing Abbie being happy is nice... "
            play sound "audio/bellring.mp3"
            " You continue to do this until the bell rings. "
            " You, Engel and Abbie get up and get to the next class of the day. "
            pause 2.0
            jump musicclass1
        else:
            x " I don't know, Engel... do you really think I can stand up for myself...? "
            x " Abbie... I know you can; all you've gotta do is be strong, alright? "
            x " But everytime they do, they always knock me back down... I can't... "
            x " Abbie... "
            x " No matter how many times you fall down, you should always get back up. "
            hide engelsad at bottom
            show engelhappy at left
            x " Show no weakness, and show them that you can handle it all. "
            x " Keep getting right back up, and eventually... hit them. Hit them back as hard as you can. "
            x " Even if they make you feel horrible, don't let their words get to you. "
            x " They're only trying to bring you down, and you crying and being afraid is only getting them what they want out of you; "
            x " A reaction. "
            x " It's time to be brave, Abbie. Even if you think that it's going to be impossible. "
            x " I know you can do it. I believe in you. "
            x " ...*sniff*.. "
            hide abbiesad at bottom
            show abbiehappy at right
            x " Thanks, Engel... I appreciate it... "
            x " I'll... I'll try to be strong... "
            hide engelhappy at bottom
            show engelcontent at left
            x " You're welcome! "
            x " If you need anything else, I'll always be here to listen to you. "
            hide engelcontent at bottom
            show engelhappy at left
            x " Oooh, who's that? [name]! Hello there! "
            x " I was just comforting Abbie about... you know... what happened in the hallways. "
            x " ...Hi [name]... "
            x " Now, come to think of it... I didn't really get to introduce myself to you, [name]! "
            x " Me neither... "
            x " Well then! How about we both introduce ourselves to [name]? "
            hide abbiehappy at bottom
            show abbieneutral at right
            x " Oh, um... "
            x " Come on now, don't be shy! It's not like [they] [are] gonna hurt you, or anything... "
            x " Okay... "
            $ abbieknow = True
            $ engelknow = True
            e " I'll go first! I'm Engel! "
            a " And I'm Abbie... "
            a " It's, um... great to meet you... "
            e " See? That wasn't so bad now, was it? "
            a " Mhm... "
            e " Anywho, about the incident that happened earlier in the hallways... "
            e " I don't get why they would go ahead and attack this poor bean... "
            hide abbieneutral at bottom
            show abbiehappy at right
            a " Hey, I'm not a bean... "
            e " They're just so, so mean! hurting a cute little thing... "
            a " Heeeeeyy... "
            " Engel drags you down, making you sit next to him. "
            " He then whispers to you, so that Abbie can't hear what he's planning. "
            e " (Pssst, [name]!) "
            e " (Play along with me, and shower Abbie with compliments!) "
            e " (Abbie likes being complimented, and if we can do that enough...) "
            e " (It'll get his mind off of whatever happened earlier!) "
            e " (You with me?{w=1} I'll take that silence as a yes!) "
            scene black with dissolve
            " You and Engel showered Abbie with compliments to give Abbie more positive thoughts. "
            " Well, for now. You're sure something bad is probably gonna happen later or tomorrow. "
            " You should just enjoy the moment though. Seeing Abbie being happy is nice... "
            play sound "audio/bellring.mp3"
            " You continue to do this until the bell rings. "
            " You, Engel and Abbie get up and get to the next class of the day. "
            pause 2.0
            jump musicclass1
    label backschool4:
        scene paperschoolback with dissolve
        # skell, riley
        " You walk to the back of the school, going to chill there... "
        " Well, that was until you heard two people talking to eachother. "
        " You, being the curious and chaotic little bean you are, were planning to eavesdrop on the conversation. "
        " You saw that it was a cool emo looking cat, and a pretty insane looking girl... "
        " You listened to their conversation. "
        show rileyneutral at left with easeinright
        show skellangry at right with easeinright
        if skellknow == True and rileyknow == True:
            sk " Riley, I told you to leave me alone for the day... "
            ri " But Skeeeeeeell, how could I leave you alone when I have so much to talk about to you? "
            sk " The only things you ever talk about is Oliver, and that's it. "
            sk " You talking about something else would be a miracle. And you leaving would be a blessing. "
            ri " Well, too bad! I'm not gonna leave until I'm done talking to you about my sweet Oliver! "
            " ...And there Riley goes again. Talking about Oliver. "
            " You're starting to question this girls sanity, and your own sanity as well. "
            " More importantly, you feel bad for Skell having to deal with this. "
            " What should you do to stop this? "
            menu:
                " Jump in and tell Riley that Oliver invited her to his house ":
                    $ skelllv += 10
                    " You got out of your hiding spot and you told Riley that she was invited to go to Oliver's house. "
                    hide skellangry at bottom
                    show skellneutral at right
                    hide rileyneutral at bottom
                    show rileyhappy at left
                    ri " REALLY?? HE DID?? "
                    ri " Well, I don't really know where his house is... Could you tell me where? "
                    " You thought she'd know where Oliver lives, due to how obsessed she was, but no... "
                    " You took this as an opportunity and you pointed in a random direction, telling her that his house was that way. "
                    " When really, you're probably just leading her to an abandoned house. Or a stranger's house. Or nowhere. "
                    ri " Eeeek! Okay! I'll get going! "
                    hide rileyhappy at right with easeoutright
                    show skellneutral at center with move
                    sk " ...She's so easy to fool. "
                    sk " Oliver's house is far away, I know that because Oliver threw a party once and everyone went to it. "
                    sk " Including me, since Ruby dragged me to it. "
                    sk " And luckily enough, Riley was sick that day so she couldn't join. "
                    sk " Her parents wouldn't let her outside and they even locked all of the exits. "
                    sk " Plus, Oliver never really said where the party was going to be held. He just said that he'll pick up everyone from school. "
                    sk " And that's why Riley doesn't know where Oliver's house was. "
                    sk " ...Well, since I have nothing to do now... "
                    sk " You want to just...chill with me? "
                    " You nod your head as a yes. "
                    sk " Great. "
                    scene black with dissolve
                    " You listened to Skell's music and talked with him throughout the break. "
                    " You were just vibing with him and talking about random topics that popped up in your head. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, Skell takes back his earphones and you both get up to get to the next class. "
                    pause 2.0
                    jump musicclass1
                " Do absolutely nothing and watch Skell suffer ":
                    " You just watched Skell suffer for the entire break. "
                    " You could tell that Skell was cringing internally, and at one point, he even put his earphones on to block out Riley's yapping. "
                    " Riley didn't even notice that he had music on, she just continued to talk and talk endlessly. "
                    " Your ears couldn't handle her rambling, so you get up and go back into the school. "
                    scene black with dissolve
                    " You wandered the school, your ears finally at peace because you don't have to listen to that girl's yapping anymore. "
                    " You continued to wander and wander, and eventually, you hear the sound that not everybody likes. "
                    " Do you have a guess on what it is? "
                    play sound "audio/bellring.mp3"
                    " Yeeaaahhh!! It's the bell ringing!! "
                    " Well, time to get skedaddling over to your next class! "
                    pause 2.0
                    jump musicclass1
        elif skellknow == True and rileyknow == False:
            sk " Riley, I told you to leave me alone for the day... "
            x " But Skeeeeeeell, how could I leave you alone when I have so much to talk about to you? "
            sk " The only things you ever talk about is Oliver, and that's it. "
            sk " You talking about something else would be a miracle. And you leaving would be a blessing. "
            x " Well, too bad! I'm not gonna leave until I'm done talking to you about my sweet Oliver! "
            " ...And there she goes. Talking about Oliver. "
            " You're starting to question this girls sanity, and your own sanity as well. "
            " More importantly, you feel bad for Skell having to deal with this. "
            " What should you do to stop this? "
            menu:
                " Jump in and tell the girl that Oliver invited her to his house ":
                    $ skelllv += 10
                    " You got out of your hiding spot and you told Riley that she was invited to go to Oliver's house. "
                    hide skellangry at bottom
                    show skellneutral at right
                    hide rileyneutral at bottom
                    show rileyhappy at left
                    x " REALLY?? HE DID?? "
                    x " Well, I don't really know where his house is... Could you tell me where? "
                    " You thought she'd know where Oliver lives, due to how obsessed she was, but no... "
                    " You took this as an opportunity and you pointed in a random direction, telling her that his house was that way. "
                    " When really, you're probably just leading her to an abandoned house. Or a stranger's house. Or nowhere. "
                    x " Eeeek! Okay! I'll get going! "
                    hide rileyhappy at right with easeoutright
                    show skellneutral at center with move
                    sk " ...She's so easy to fool. "
                    sk " Oliver's house is far away, I know that because Oliver threw a party once and everyone went to it. "
                    sk " Including me, since Ruby dragged me to it. "
                    sk " And luckily enough, Riley was sick that day so she couldn't join. "
                    sk " Her parents wouldn't let her outside and they even locked all of the exits. "
                    sk " Plus, Oliver never really said where the party was going to be held. He just said that he'll pick up everyone from school. "
                    sk " And that's why Riley doesn't know where Oliver's house was. "
                    sk " ...Well, since I have nothing to do now... "
                    sk " You want to just...chill with me? "
                    " You nod your head as a yes. "
                    sk " Great. "
                    scene black with dissolve
                    " You listened to Skell's music and talked with him throughout the break. "
                    " You were just vibing with him and talking about random topics that popped up in your head. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, Skell takes back his earphones and you both get up to get to the next class. "
                    pause 2.0
                    jump musicclass1
                " Do absolutely nothing and watch Skell suffer ":
                    " You just watched Skell suffer for the entire break. "
                    " You could tell that Skell was cringing internally, and at one point, he even put his earphones on to block out the girl's yapping. "
                    " the girl didn't even notice that he had music on, she just continued to talk and talk endlessly. "
                    " Your ears couldn't handle her rambling, so you get up and go back into the school. "
                    scene black with dissolve
                    " You wandered the school, your ears finally at peace because you don't have to listen to that girl's yapping anymore. "
                    " You continued to wander and wander, and eventually, you hear the sound that not everybody likes. "
                    " Do you have a guess on what it is? "
                    play sound "audio/bellring.mp3"
                    " Yeeaaahhh!! It's the bell ringing!! "
                    " Well, time to get skedaddling over to your next class! "
                    pause 2.0
                    jump musicclass1
        elif skellknow == False and rileyknow == True:
            x " Riley, I told you to leave me alone for the day... "
            ri " But Skeeeeeeell, how could I leave you alone when I have so much to talk about to you? "
            x " The only things you ever talk about is Oliver, and that's it. "
            x " You talking about something else would be a miracle. And you leaving would be a blessing. "
            ri " Well, too bad! I'm not gonna leave until I'm done talking to you about my sweet Oliver! "
            " ...And there Riley goes again. Talking about Oliver. "
            " You're starting to question this girls sanity, and your own sanity as well. "
            " More importantly, you feel bad for this guy having to deal with this. "
            " What should you do to stop this? "
            menu:
                " Jump in and tell Riley that Oliver invited her to his house ":
                    $ skelllv += 10
                    " You got out of your hiding spot and you told Riley that she was invited to go to Oliver's house. "
                    hide skellangry at bottom
                    show skellneutral at right
                    hide rileyneutral at bottom
                    show rileyhappy at left
                    ri " REALLY?? HE DID?? "
                    ri " Well, I don't really know where his house is... Could you tell me where? "
                    " You thought she'd know where Oliver lives, due to how obsessed she was, but no... "
                    " You took this as an opportunity and you pointed in a random direction, telling her that his house was that way. "
                    " When really, you're probably just leading her to an abandoned house. Or a stranger's house. Or nowhere. "
                    ri " Eeeek! Okay! I'll get going! "
                    hide rileyhappy at right with easeoutright
                    show skellneutral at center with move
                    x " ...She's so easy to fool. "
                    x " Oliver's house is far away, I know that because Oliver threw a party once and everyone went to it. "
                    x " Including me, since Ruby dragged me to it. "
                    x " And luckily enough, Riley was sick that day so she couldn't join. "
                    x " Her parents wouldn't let her outside and they even locked all of the exits. "
                    x " Plus, Oliver never really said where the party was going to be held. He just said that he'll pick up everyone from school. "
                    x " And that's why Riley doesn't know where Oliver's house was. "
                    x " ...Well, since I have nothing to do now... "
                    x " I guess I could introduce myself, since I haven't yet. "
                    $ skellknow = True
                    sk " I'm Skell. I usually chill around here. "
                    sk " Uh...so... "
                    sk " You want to just...chill with me and listen to some music? "
                    " You nod your head as a yes. "
                    sk " Great. "
                    scene black with dissolve
                    " You listened to Skell's music and talked with him throughout the break. "
                    " You were just vibing with him and talking about random topics that popped up in your head. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, Skell takes back his earphones and you both get up to get to the next class. "
                    pause 2.0
                    jump musicclass1
                " Do absolutely nothing and watch the cat guy suffer ":
                    " You just watched the guy suffer for the entire break. "
                    " You could tell that the other guy was cringing internally, and at one point, he even put his earphones on to block out Riley's yapping. "
                    " Riley didn't even notice that he had music on, she just continued to talk and talk endlessly. "
                    " Your ears couldn't handle her rambling, so you get up and go back into the school. "
                    scene black with dissolve
                    " You wandered the school, your ears finally at peace because you don't have to listen to that girl's yapping anymore. "
                    " You continued to wander and wander, and eventually, you hear the sound that not everybody likes. "
                    " Do you have a guess on what it is? "
                    play sound "audio/bellring.mp3"
                    " Yeeaaahhh!! It's the bell ringing!! "
                    " Well, time to get skedaddling over to your next class! "
                    pause 2.0
                    jump musicclass1
        else:
            x " Riley, I told you to leave me alone for the day... "
            x " But Skeeeeeeell, how could I leave you alone when I have so much to talk about to you? "
            x " The only things you ever talk about is Oliver, and that's it. "
            x " You talking about something else would be a miracle. And you leaving would be a blessing. "
            x " Well, too bad! I'm not gonna leave until I'm done talking to you about my sweet Oliver! "
            " ...And there she goes. Talking about Oliver. "
            " You're starting to question this girls sanity, and your own sanity as well. "
            " More importantly, you feel bad for this guy having to deal with this. "
            " What should you do to stop this? "
            menu:
                " Jump in and tell the girl that Oliver invited her to his house ":
                    $ skelllv += 10
                    " You got out of your hiding spot and you told Riley that she was invited to go to Oliver's house. "
                    hide skellangry at bottom
                    show skellneutral at right
                    hide rileyneutral at bottom
                    show rileyhappy at left
                    x " REALLY?? HE DID?? "
                    x " Well, I don't really know where his house is... Could you tell me where? "
                    " You thought she'd know where Oliver lives, due to how obsessed she was, but no... "
                    " You took this as an opportunity and you pointed in a random direction, telling her that his house was that way. "
                    " When really, you're probably just leading her to an abandoned house. Or a stranger's house. Or nowhere. "
                    x " Eeeek! Okay! I'll get going! "
                    hide rileyhappy at right with easeoutright
                    show skellneutral at center with move
                    x " ...She's so easy to fool. "
                    x " Oliver's house is far away, I know that because Oliver threw a party once and everyone went to it. "
                    x " Including me, since Ruby dragged me to it. "
                    x " And luckily enough, Riley was sick that day so she couldn't join. "
                    x " Her parents wouldn't let her outside and they even locked all of the exits. "
                    x " Plus, Oliver never really said where the party was going to be held. He just said that he'll pick up everyone from school. "
                    x " And that's why Riley doesn't know where Oliver's house was. "
                    x " ...Well, since I have nothing to do now... "
                    x " I guess I could introduce myself, since I haven't yet. "
                    $ skellknow = True
                    sk " I'm Skell. I usually chill around here. "
                    sk " That girl from earlier... Her name's Riley. "
                    $ rileyknow = True
                    sk " She always acts like that. Always talks about Oliver. "
                    sk " It's actually rare for her to talk about anyone else. "
                    sk " Uh...so... "
                    sk " You want to just...chill with me and listen to some music? "
                    " You nod your head as a yes. "
                    sk " Great. "
                    scene black with dissolve
                    " You listened to Skell's music and talked with him throughout the break. "
                    " You were just vibing with him and talking about random topics that popped up in your head. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, Skell takes back his earphones and you both get up to get to the next class. "
                    pause 2.0
                    jump musicclass1
                " Do absolutely nothing and watch the cat guy suffer ":
                    " You just watched the guy suffer for the entire break. "
                    " You could tell that the other guy was cringing internally, and at one point, he even put his earphones on to block out Riley's yapping. "
                    " Riley didn't even notice that he had music on, she just continued to talk and talk endlessly. "
                    " Your ears couldn't handle her rambling, so you get up and go back into the school. "
                    scene black with dissolve
                    " You wandered the school, your ears finally at peace because you don't have to listen to that girl's yapping anymore. "
                    " You continued to wander and wander, and eventually, you hear the sound that not everybody likes. "
                    " Do you have a guess on what it is? "
                    play sound "audio/bellring.mp3"
                    " Yeeaaahhh!! It's the bell ringing!! "
                    " Well, time to get skedaddling over to your next class! "
                    pause 2.0
                    jump musicclass1
    label gym4:
        scene gym with dissolve
        # Lana, Ruby
        " You walk into the gym, and sat on one of the bleachers. "
        " You look at your sides, and you see two other people sitting near you. "
        if lanaknow == True and rubyknow == True:
            " On one side, Lana was sitting a few seats up right from you. "
            " And on another side, Ruby was sitting a few seats left and down from you. "
            " Who do you want to talk with? "
            menu:
                " {image=lanaicon} Talk with Lana {image=lanaicon} ":
                    show lananeutral at center with easeinright
                    " You went up and sat next to Lana, looking at what she was doing... "
                    " It looks like she was making little sock puppets! How cute! "
                    " It took her a tad bit to notice you, since she was so focused. "
                    l " Hey there, [name]! "
                    l " I'm working on some new sock puppets. Their names are gonna be Bob and Gerson! "
                    l " They say 'hi' to you, [name]! "
                    " You say 'hi' back to the two sock puppets. "
                    " They look quite adorable...adorably stupid with how Lana made them. "
                    " It's cause of the googly eyes they have of them. You find googly eyes pretty funny. "
                    l " Actually... do you want me to teach you how to make these sock puppets? "
                    menu:
                        " Sure! ":
                            $ lanalv += 10
                            hide lananeutral at bottom
                            show lanahappy at center
                            l " Yipeee!! "
                            l " Let's get to working, then! "
                            scene lanapuppets with dissolve
                            " Lana taught you how to make sock puppets. "
                            " It was a pretty simple process... "
                            " You thought as you make a slightly wonky looking puppet. "
                            " Lana said that it was okay since it was your first one. "
                            " She says that there were other people making more interesting hand puppets. "
                            " Like literally making cats or dragons out of paper. "
                            " You've heard about it before, it's called paper dragon making. "
                            " You honestly have some mad respect for people who make paper dragons, cause some of them look like they took hours to make. "
                            " You'd probably just end up making a cat and that's it. "
                            " Lana thinks they're cool as well, and has tried to make a paper dragon before. "
                            " It wasn't the best, but she said that she wanted to try making them again. "
                            " She just got a few instructions wrong, probably. "
                            play sound "audio/bellring.mp3"
                            scene gym with dissolve
                            show lananeutral at center with dissolve
                            l " And that's how you make sock puppets! - oh, look! and we finished right when the bell rang! "
                            l " This was really fun, [name]! I hope we can spend more time like this in the future! "
                            l " I'll get going now, see you later! "
                            hide lananeutral at left with easeoutleft
                            " You shortly follow Lana to go to the next class of the day. "
                            scene black with dissolve
                            pause 2.0
                            jump musicclass1
                        " Naw ":
                            $ lanalv += 5
                            " You polietely declined Lana's offer, and just told her that you wanted to chill. "
                            l " Ah, that's alright... "
                            l " Well - I'll just be making sock puppets while I talk to you then! "
                            l " Have you heard of this show called Ghost stories? It's in japanese, but honestly I prefer the english dub better! "
                            l " Trust me, you should watch it! Its pretty funny! "
                            " Lana continues to talk about this anime that she likes. "
                            " It sounds pretty... "
                            " Wait, you've heard of this before. "
                            " Is this that one anime that has this guy saying: 'THINK OF A BIG BLACK MAN CHASING YOU!!' "
                            " Lana you're nice but like why that anime "
                            " I would never expect that Lana would like that anime but like "
                            " Then again, it's kind of popular on the web, so... "
                            play sound "audio/bellring.mp3"
                            " As you talked, the bell rang - Signalling it was time for class. "
                            " You get up with Lana, and you two went to the next class. "
                            scene black with dissolve
                            pause 2.0
                            jump musicclass1
                " {image=rubyicon} Talk with Ruby {image=rubyicon} ":
                    " You moved down to your left so that you could see what Ruby was doing. "
                    show rubyneutral at center with easeinleft
                    ru " ... "
                    " She seemed to be processing something, as she was sitting completely still. "
                    " The only time she'd move, is when she'd blink. She would move her arms slightly. "
                    " She stayed like this for 15 minutes. until she suddenly spoke up. "
                    ru " Oh, hey... "
                    ru " I'm sorry for not noticing you there. "
                    ru " I was just in deep thought, is all. "
                    ru " You wanna know a fun fact about me? "
                    ru " I can actually play games in my head. Like cards, that one bartender game... "
                    ru " Just not anything like roblox or minecraft. I think they'd cause me to overheat if I tried. "
                    " You pointed out to her that she seems more tired than usual. "
                    ru " That's because... "
                    ru " I need to update. And in order to update, I need to stay asleep. "
                    ru " And an update takes about 2 hours. "
                    ru " I can't really fall asleep in school because I'd get myself killed by the teachers.. "
                    ru " So I'm making myself stay up until I reach home. "
                    ru " Once I get home, I'm immediately going to charge myself and update. "
                    ru " Just hoping that I don't really forget to do any assignments... "
                    ru " We didn't really have any assignments from what I remember, they were all just doing discussions... "
                    scene black with dissolve
                    " You talked with Ruby for the rest of the break. "
                    " You were starting to wonder how people like Ruby really worked, but you decided not to ask. "
                    " There were many times that Ruby almost fell asleep in the middle of your conversation... "
                    " This would be your honest reaction after not sleeping for an entire day. "
                    " You helped Ruby stay up for the break, making sure she doesn't fall asleep. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, and that manages to wake up Ruby more. "
                    " You and Ruby both get up from your seats and you two went to the next class. "
                    pause 2.0
                    jump musicclass1
                " Just chill there I guess ":
                    " You decided not to talk to either of them, and you just sat there. "
                    " Wondering what you could do, you pulled out your phone to waste your time. "
                    " Instead of scrolling through tiktok, you decided to go on youtube to watch some random funny videos. "
                    " You decided to watch a funfacts video of a game you liked; TaleUnder. "
                    " Some of the facts in the video, you didn't even know. Which was cool. "
                    play sound "audio/bellring.mp3"
                    " You continued to watch the video until you heard the bell ring. "
                    " You put your phone back in your pocket, get up and went to your classroom for the next class. "
                    scene black with dissolve
                    pause 2.0
                    jump musicclass1
        elif lanaknow == True and rubyknow == False:
            " On one side, Lana was sitting a few seats up right from you. "
            " And on another side, a girl with a TV for a head was a few seats left and down from you. "
            " Who do you want to talk with? "
            menu:
                " {image=lanaicon} Talk with Lana {image=lanaicon} ":
                    show lananeutral at center with easeinright
                    " You went up and sat next to Lana, looking at what she was doing... "
                    " It looks like she was making little sock puppets! How cute! "
                    " It took her a tad bit to notice you, since she was so focused. "
                    l " Hey there, [name]! "
                    l " I'm working on some new sock puppets. Their names are gonna be Bob and Gerson! "
                    l " They say 'hi' to you, [name]! "
                    " You say 'hi' back to the two sock puppets. "
                    " They look quite adorable...adorably stupid with how Lana made them. "
                    " It's cause of the googly eyes they have of them. You find googly eyes pretty funny. "
                    l " Actually... do you want me to teach you how to make these sock puppets? "
                    menu:
                        " Sure! ":
                            $ lanalv += 10
                            hide lananeutral at bottom
                            show lanahappy at center
                            l " Yipeee!! "
                            l " Let's get to working, then! "
                            scene lanapuppets with dissolve
                            " Lana taught you how to make sock puppets. "
                            " It was a pretty simple process... "
                            " You thought as you make a slightly wonky looking puppet. "
                            " Lana said that it was okay since it was your first one. "
                            " She says that there were other people making more interesting hand puppets. "
                            " Like literally making cats or dragons out of paper. "
                            " You've heard about it before, it's called paper dragon making. "
                            " You honestly have some mad respect for people who make paper dragons, cause some of them look like they took hours to make. "
                            " You'd probably just end up making a cat and that's it. "
                            " Lana thinks they're cool as well, and has tried to make a paper dragon before. "
                            " It wasn't the best, but she said that she wanted to try making them again. "
                            " She just got a few instructions wrong, probably. "
                            play sound "audio/bellring.mp3"
                            scene gym with dissolve
                            show lananeutral at center with dissolve
                            l " And that's how you make sock puppets! - oh, look! and we finished right when the bell rang! "
                            l " This was really fun, [name]! I hope we can spend more time like this in the future! "
                            l " I'll get going now, see you later! "
                            hide lananeutral at left with easeoutleft
                            " You shortly follow Lana to go to the next class of the day. "
                            scene black with dissolve
                            pause 2.0
                            jump musicclass1
                        " Naw ":
                            $ lanalv += 5
                            " You polietely declined Lana's offer, and just told her that you wanted to chill. "
                            l " Ah, that's alright... "
                            l " Well - I'll just be making sock puppets while I talk to you then! "
                            l " Have you heard of this show called Ghost stories? It's in japanese, but honestly I prefer the english dub better! "
                            l " Trust me, you should watch it! Its pretty funny! "
                            " Lana continues to talk about this anime that she likes. "
                            " It sounds pretty... "
                            " Wait, you've heard of this before. "
                            " Is this that one anime that has this guy saying: 'THINK OF A BIG BLACK MAN CHASING YOU!!' "
                            " Lana you're nice but like why that anime "
                            " I would never expect that Lana would like that anime but like "
                            " Then again, it's kind of popular on the web, so... "
                            play sound "audio/bellring.mp3"
                            " As you talked, the bell rang - Signalling it was time for class. "
                            " You get up with Lana, and you two went to the next class. "
                            scene black with dissolve
                            pause 2.0
                            jump musicclass1
                " {image=rubyicon} The girl with the TV head {image=rubyicon} ":
                    " You moved down to your left so that you could see what this girl was doing. "
                    show rubyneutral at center with easeinleft
                    x " ... "
                    " She seemed to be processing something, as she was sitting completely still. "
                    " The only time she'd move, is when she'd blink. She would move her arms slightly. "
                    " She stayed like this for 15 minutes. until she suddenly spoke up. "
                    x " Oh, hey... "
                    x " I'm sorry for not noticing you there. "
                    x " I was just in deep thought, is all. "
                    $ rubyknow = True
                    ru " I'm Ruby... Nice to meet you... "
                    ru " You wanna know a fun fact about me? "
                    ru " I can actually play games in my head. Like cards, that one bartender game... "
                    ru " Just not anything like roblox or minecraft. I think they'd cause me to overheat if I tried. "
                    " You pointed out to her that she seems more tired than usual. "
                    ru " That's because... "
                    ru " I need to update. And in order to update, I need to stay asleep. "
                    ru " And an update takes about 2 hours. "
                    ru " I can't really fall asleep in school because I'd get myself killed by the teachers.. "
                    ru " So I'm making myself stay up until I reach home. "
                    ru " Once I get home, I'm immediately going to charge myself and update. "
                    ru " Just hoping that I don't really forget to do any assignments... "
                    ru " We didn't really have any assignments from what I remember, they were all just doing discussions... "
                    scene black with dissolve
                    " You talked with Ruby for the rest of the break. "
                    " You were starting to wonder how people like Ruby really worked, but you decided not to ask. "
                    " There were many times that Ruby almost fell asleep in the middle of your conversation... "
                    " This would be your honest reaction after not sleeping for an entire day. "
                    " You helped Ruby stay up for the break, making sure she doesn't fall asleep. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, and that manages to wake up Ruby more. "
                    " You and Ruby both get up from your seats and you two went to the next class. "
                    pause 2.0
                    jump musicclass1
                " Just chill there I guess ":
                    " You decided not to talk to either of them, and you just sat there. "
                    " Wondering what you could do, you pulled out your phone to waste your time. "
                    " Instead of scrolling through tiktok, you decided to go on youtube to watch some random funny videos. "
                    " You decided to watch a funfacts video of a game you liked; TaleUnder. "
                    " Some of the facts in the video, you didn't even know. Which was cool. "
                    play sound "audio/bellring.mp3"
                    " You continued to watch the video until you heard the bell ring. "
                    " You put your phone back in your pocket, get up and went to your classroom for the next class. "
                    scene black with dissolve
                    pause 2.0
                    jump musicclass1
        elif lanaknow == False and rubyknow == True:
            " On one side, A girl making sock puppets was sitting a few seats up right from you. "
            " And on another side, Ruby was sitting a few seats left and down from you. "
            " Who do you want to talk with? "
            menu:
                " {image=lanaicon} Talk with the girl making sock puppets {image=lanaicon} ":
                    show lananeutral at center with easeinright
                    " You went up and sat next to this girl, looking at what she was doing... "
                    " It looks like she was making little sock puppets! How cute! "
                    " It took her a tad bit to notice you, since she was so focused. "
                    x " Hey there, [name]! "
                    x " I'm working on some new sock puppets. Their names are gonna be Bob and Gerson! "
                    x " They say 'hi' to you, [name]! "
                    " You say 'hi' back to the two sock puppets. "
                    " They look quite adorable...adorably stupid with how Lana made them. "
                    " It's cause of the googly eyes they have of them. You find googly eyes pretty funny. "
                    x " Wait, I'm sorry... I forgot to introduce myself... "
                    $ lanaknow = True
                    l " I'm Lana! We go to the same class. "
                    l " It's nice to meet you! "
                    l " Actually... I just had an idea. Do you want me to teach you how to make these sock puppets? "
                    menu:
                        " Sure! ":
                            $ lanalv += 10
                            hide lananeutral at bottom
                            show lanahappy at center
                            l " Yipeee!! "
                            l " Let's get to working, then! "
                            scene lanapuppets with dissolve
                            " Lana taught you how to make sock puppets. "
                            " It was a pretty simple process... "
                            " You thought as you make a slightly wonky looking puppet. "
                            " Lana said that it was okay since it was your first one. "
                            " She says that there were other people making more interesting hand puppets. "
                            " Like literally making cats or dragons out of paper. "
                            " You've heard about it before, it's called paper dragon making. "
                            " You honestly have some mad respect for people who make paper dragons, cause some of them look like they took hours to make. "
                            " You'd probably just end up making a cat and that's it. "
                            " Lana thinks they're cool as well, and has tried to make a paper dragon before. "
                            " It wasn't the best, but she said that she wanted to try making them again. "
                            " She just got a few instructions wrong, probably. "
                            play sound "audio/bellring.mp3"
                            scene gym with dissolve
                            show lananeutral at center with dissolve
                            l " And that's how you make sock puppets! - oh, look! and we finished right when the bell rang! "
                            l " This was really fun, [name]! I hope we can spend more time like this in the future! "
                            l " I'll get going now, see you later! "
                            hide lananeutral at left with easeoutleft
                            " You shortly follow Lana to go to the next class of the day. "
                            scene black with dissolve
                            pause 2.0
                            jump musicclass1
                        " Naw ":
                            $ lanalv += 5
                            " You polietely declined Lana's offer, and just told her that you wanted to chill. "
                            l " Ah, that's alright... "
                            l " Well - I'll just be making sock puppets while I talk to you then! "
                            l " Have you heard of this show called Ghost stories? It's in japanese, but honestly I prefer the english dub better! "
                            l " Trust me, you should watch it! Its pretty funny! "
                            " Lana continues to talk about this anime that she likes. "
                            " It sounds pretty... "
                            " Wait, you've heard of this before. "
                            " Is this that one anime that has this guy saying: 'THINK OF A BIG BLACK MAN CHASING YOU!!' "
                            " Lana you're nice but like why that anime "
                            " I would never expect that Lana would like that anime but like "
                            " Then again, it's kind of popular on the web, so... "
                            play sound "audio/bellring.mp3"
                            " As you talked, the bell rang - Signalling it was time for class. "
                            " You get up with Lana, and you two went to the next class. "
                            scene black with dissolve
                            pause 2.0
                            jump musicclass1
                " {image=rubyicon} Talk with Ruby {image=rubyicon} ":
                    " You moved down to your left so that you could see what Ruby was doing. "
                    show rubyneutral at center with easeinleft
                    ru " ... "
                    " She seemed to be processing something, as she was sitting completely still. "
                    " The only time she'd move, is when she'd blink. She would move her arms slightly. "
                    " She stayed like this for 15 minutes. until she suddenly spoke up. "
                    ru " Oh, hey... "
                    ru " I'm sorry for not noticing you there. "
                    ru " I was just in deep thought, is all. "
                    ru " You wanna know a fun fact about me? "
                    ru " I can actually play games in my head. Like cards, that one bartender game... "
                    ru " Just not anything like roblox or minecraft. I think they'd cause me to overheat if I tried. "
                    " You pointed out to her that she seems more tired than usual. "
                    ru " That's because... "
                    ru " I need to update. And in order to update, I need to stay asleep. "
                    ru " And an update takes about 2 hours. "
                    ru " I can't really fall asleep in school because I'd get myself killed by the teachers.. "
                    ru " So I'm making myself stay up until I reach home. "
                    ru " Once I get home, I'm immediately going to charge myself and update. "
                    ru " Just hoping that I don't really forget to do any assignments... "
                    ru " We didn't really have any assignments from what I remember, they were all just doing discussions... "
                    scene black with dissolve
                    " You talked with Ruby for the rest of the break. "
                    " You were starting to wonder how people like Ruby really worked, but you decided not to ask. "
                    " There were many times that Ruby almost fell asleep in the middle of your conversation... "
                    " This would be your honest reaction after not sleeping for an entire day. "
                    " You helped Ruby stay up for the break, making sure she doesn't fall asleep. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, and that manages to wake up Ruby more. "
                    " You and Ruby both get up from your seats and you two went to the next class. "
                    pause 2.0
                    jump musicclass1
                " Just chill there I guess ":
                    " You decided not to talk to either of them, and you just sat there. "
                    " Wondering what you could do, you pulled out your phone to waste your time. "
                    " Instead of scrolling through tiktok, you decided to go on youtube to watch some random funny videos. "
                    " You decided to watch a funfacts video of a game you liked; TaleUnder. "
                    " Some of the facts in the video, you didn't even know. Which was cool. "
                    play sound "audio/bellring.mp3"
                    " You continued to watch the video until you heard the bell ring. "
                    " Yu put your phone back in your pocket, get up and went to your classroom for the next class. "
                    scene black with dissolve
                    pause 2.0
                    jump musicclass1
        else:
            " On one side, Lana was sitting a few seats up right from you. "
            " And on another side, Ruby was sitting a few seats left and down from you. "
            " Who do you want to talk with? "
            menu:
                " {image=lanaicon} Talk with the girl making sock puppets {image=lanaicon} ":
                    show lananeutral at center with easeinright
                    " You went up and sat next to this girl, looking at what she was doing... "
                    " It looks like she was making little sock puppets! How cute! "
                    " It took her a tad bit to notice you, since she was so focused. "
                    x " Hey there, [name]! "
                    x " I'm working on some new sock puppets. Their names are gonna be Bob and Gerson! "
                    x " They say 'hi' to you, [name]! "
                    " You say 'hi' back to the two sock puppets. "
                    " They look quite adorable...adorably stupid with how Lana made them. "
                    " It's cause of the googly eyes they have of them. You find googly eyes pretty funny. "
                    x " Wait, I'm sorry... I forgot to introduce myself... "
                    $ lanaknow = True
                    l " I'm Lana! We go to the same class. "
                    l " It's nice to meet you! "
                    l " Actually... I just had an idea. Do you want me to teach you how to make these sock puppets? "
                    menu:
                        " Sure! ":
                            $ lanalv += 10
                            hide lananeutral at bottom
                            show lanahappy at center
                            l " Yipeee!! "
                            l " Let's get to working, then! "
                            scene lanapuppets with dissolve
                            " Lana taught you how to make sock puppets. "
                            " It was a pretty simple process... "
                            " You thought as you make a slightly wonky looking puppet. "
                            " Lana said that it was okay since it was your first one. "
                            " She says that there were other people making more interesting hand puppets. "
                            " Like literally making cats or dragons out of paper. "
                            " You've heard about it before, it's called paper dragon making. "
                            " You honestly have some mad respect for people who make paper dragons, cause some of them look like they took hours to make. "
                            " You'd probably just end up making a cat and that's it. "
                            " Lana thinks they're cool as well, and has tried to make a paper dragon before. "
                            " It wasn't the best, but she said that she wanted to try making them again. "
                            " She just got a few instructions wrong, probably. "
                            play sound "audio/bellring.mp3"
                            scene gym with dissolve
                            show lananeutral at center with dissolve
                            l " And that's how you make sock puppets! - oh, look! and we finished right when the bell rang! "
                            l " This was really fun, [name]! I hope we can spend more time like this in the future! "
                            l " I'll get going now, see you later! "
                            hide lananeutral at left with easeoutleft
                            " You shortly follow Lana to go to the next class of the day. "
                            scene black with dissolve
                            pause 2.0
                            jump musicclass1
                        " Naw ":
                            $ lanalv += 5
                            " You polietely declined Lana's offer, and just told her that you wanted to chill. "
                            l " Ah, that's alright... "
                            l " Well - I'll just be making sock puppets while I talk to you then! "
                            l " Have you heard of this show called Ghost stories? It's in japanese, but honestly I prefer the english dub better! "
                            l " Trust me, you should watch it! Its pretty funny! "
                            " Lana continues to talk about this anime that she likes. "
                            " It sounds pretty... "
                            " Wait, you've heard of this before. "
                            " Is this that one anime that has this guy saying: 'THINK OF A BIG BLACK MAN CHASING YOU!!' "
                            " Lana you're nice but like why that anime "
                            " I would never expect that Lana would like that anime but like "
                            " Then again, it's kind of popular on the web, so... "
                            play sound "audio/bellring.mp3"
                            " As you talked, the bell rang - Signalling it was time for class. "
                            " You get up with Lana, and you two went to the next class. "
                            scene black with dissolve
                            pause 2.0
                            jump musicclass1
                " {image=rubyicon} The girl with the TV head {image=rubyicon} ":
                    " You moved down to your left so that you could see what this girl was doing. "
                    show rubyneutral at center with easeinleft
                    x " ... "
                    " She seemed to be processing something, as she was sitting completely still. "
                    " The only time she'd move, is when she'd blink. She would move her arms slightly. "
                    " She stayed like this for 15 minutes. until she suddenly spoke up. "
                    x " Oh, hey... "
                    x " I'm sorry for not noticing you there. "
                    x " I was just in deep thought, is all. "
                    $ rubyknow = True
                    ru " I'm Ruby... Nice to meet you... "
                    ru " You wanna know a fun fact about me? "
                    ru " I can actually play games in my head. Like cards, that one bartender game... "
                    ru " Just not anything like roblox or minecraft. I think they'd cause me to overheat if I tried. "
                    " You pointed out to her that she seems more tired than usual. "
                    ru " That's because... "
                    ru " I need to update. And in order to update, I need to stay asleep. "
                    ru " And an update takes about 2 hours. "
                    ru " I can't really fall asleep in school because I'd get myself killed by the teachers.. "
                    ru " So I'm making myself stay up until I reach home. "
                    ru " Once I get home, I'm immediately going to charge myself and update. "
                    ru " Just hoping that I don't really forget to do any assignments... "
                    ru " We didn't really have any assignments from what I remember, they were all just doing discussions... "
                    scene black with dissolve
                    " You talked with Ruby for the rest of the break. "
                    " You were starting to wonder how people like Ruby really worked, but you decided not to ask. "
                    " There were many times that Ruby almost fell asleep in the middle of your conversation... "
                    " This would be your honest reaction after not sleeping for an entire day. "
                    " You helped Ruby stay up for the break, making sure she doesn't fall asleep. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, and that manages to wake up Ruby more. "
                    " You and Ruby both get up from your seats and you two went to the next class. "
                    pause 2.0
                    jump musicclass1
                " Just chill there I guess ":
                    " You decided not to talk to either of them, and you just sat there. "
                    " Wondering what you could do, you pulled out your phone to waste your time. "
                    " Instead of scrolling through tiktok, you decided to go on youtube to watch some random funny videos. "
                    " You decided to watch a funfacts video of a game you liked; TaleUnder. "
                    " Some of the facts in the video, you didn't even know. Which was cool. "
                    play sound "audio/bellring.mp3"
                    " You continued to watch the video until you heard the bell ring. "
                    " Yu put your phone back in your pocket, get up and went to your classroom for the next class. "
                    scene black with dissolve
                    pause 2.0
                    jump musicclass1
    label cafe4:
        scene cafeteria with dissolve
        # Kevin, Robby
        " You looked around the cafeteria to find a place to sit. "
        " You spot two people that you sort of recognize from your class, and you thought it would be good to talk to one of them. "
        " Who do you sit next to? "
        if kevinknow == True and robbyknow == True:
            menu:
                " {image=kevinicon} Kevin {image=kevinicon} ":
                    jump kevincafeint69
                " {image=robbyicon} Robby {image=robbyicon} ":
                    jump robbycafeint69
        elif kevinknow == True and robbyknow == False:
            menu:
                " {image=kevinicon} Kevin {image=kevinicon} ":
                    jump kevincafeint69
                " {image=robbyicon} A weird looking guy with a weird hat. {image=robbyicon} ":
                    jump robbycafeint69
        elif kevinknow == False and robbyknow == True:
            menu:
                " {image=kevinicon} A nerd {image=kevinicon} ":
                    jump kevincafeint69
                " {image=robbyicon} Robby {image=robbyicon} ":
                    jump robbycafeint69
        else:
            menu:
                " {image=kevinicon} A nerd {image=kevinicon} ":
                    jump kevincafeint69
                " {image=robbyicon} A weird looking guy with a weird hat. {image=robbyicon} ":
                    jump robbycafeint69
        label kevincafeint69:
            " You walk up to the nerd and sit next to him. "
            show kevinneutral at center with easeinleft
            if kevinknow == True:
                " He was just eating a sandwich that he had. "
                " Now that you thought about it, you haven't really eaten at all. "
                " The only thing you ate was the thing you ate earlier, before you went to school. "
                " And then your hunger kicks in. Oh boy. "
                " Kevin seems to ntice that you're a bit hungry, so he gets down to get something from his backpack... "
                " ...And he pulls out a extra sandwich that he had and gives it to you. "
                kv " I noticed that you looked a bit hungry. "
                kv " Thankfully, I had an extra in my bag. "
                " You took the extra sandwich, and you start to eat... "
                " ...it actually tastes pretty good. "
                kv " No one here would be willing enough to give someone their food in here. "
                kv " Well, theres some people. But the others? nope. No chance. "
                kv " Take Oliver as an example. He'd probably trick you that he has food for you and then he would just smush it all over your face. "
                " You ask if Kevin himself made this sandwich. "
                kv " Well, yes. I make them just like how my mom used to make them for me. "
                kv " She always had sandwiches that just hit different, they still taste so good, up until now. "
                kv " You think i'd get tired of the taste, but you're wrong. "
                kv " You won't see me getting tired of this. "
                " Wow, Kevin's mom really has some good sandwich making skills. "
                " You don't really know if that's a bad thing to say, considering that men usually ask women to make the sandwiches for them. "
                " Eugh, I hate those kind of men. "
                " Those men can make a sandwich themselves, there isn't really a point in asking a woman to make it for you. "
                " Why're you asking them to make something for you? Can't make something yourselves? Can't cook? "
                " Cooking is a basic skill, everyone including men know how to do that, John. It's not just for women. "
                " ...How did this turn into getting a sandwich into me just yapping. "
                " Am I wrong though? "
                play sound "audio/bellring.mp3"
                " The bell rings, and you finish up the sandwich that Kevin gave you. "
                " You thank him for the food before you got up from your seat and went to your next class. "
                scene black with dissolve
                pause 2.0
                jump musicclass1
            else:
                " He was just eating a sandwich that he had. "
                " Now that you thought about it, you haven't really eaten at all. "
                " The only thing you ate was the thing you ate earlier, before you went to school. "
                " And then your hunger kicks in. Oh boy. "
                " Kevin seems to ntice that you're a bit hungry, so he gets down to get something from his backpack... "
                " ...And he pulls out a extra sandwich that he had and gives it to you. "
                x " I noticed that you looked a bit hungry. "
                x " Thankfully, I had an extra in my bag. "
                " You took the extra sandwich, and you start to eat... "
                " ...it actually tastes pretty good. "
                $ kevinknow = True
                kv " I'm Kevin, by the way. We're classmates. "
                kv " No one here would be willing enough to give someone their food in here. "
                kv " Well, theres some people. But the others? nope. No chance. "
                kv " Take Oliver as an example. He'd probably trick you that he has food for you and then he would just smush it all over your face. "
                " You ask if Kevin himself made this sandwich. "
                kv " Well, yes. I make them just like how my mom used to make them for me. "
                kv " She always had sandwiches that just hit different, they still taste so good, up until now. "
                kv " You think i'd get tired of the taste, but you're wrong. "
                kv " You won't see me getting tired of this. "
                " Wow, Kevin's mom really has some good sandwich making skills. "
                " You don't really know if that's a bad thing to say, considering that men usually ask women to make the sandwiches for them. "
                " Eugh, I hate those kind of men. "
                " Those men can make a sandwich themselves, there isn't really a point in asking a woman to make it for you. "
                " Why're you asking them to make something for you? Can't make something yourselves? Can't cook? "
                " Cooking is a basic skill, everyone including men know how to do that, John. It's not just for women. "
                " ...How did this turn into getting a sandwich into me just yapping. "
                " Am I wrong though? "
                play sound "audio/bellring.mp3"
                " The bell rings, and you finish up the sandwich that Kevin gave you. "
                " You thank him for the food before you got up from your seat and went to your next class. "
                scene black with dissolve
                pause 2.0
                jump musicclass1
        label robbycafeint69:
            " You walk up to the goofy looking guy and sit next to him. "
            show robbyneutral at center with easeinright
            if robbyknow == True:
                " Seems like he was in deep thought about something. He was staring down at a piece of paper. "
                " He looks...rather shocked. Or disgusted. "
                " You take a look at what he saw... "
                " 'hey so like can u fix my 5000 toys'....it was a note from Oliver that was apparently sent by Edward. "
                " Those toys werent any normal toys, they were the FREAKY kind. "
                rb " I have...{w=1}no words. "
                " Me too, Robby. Me too. "
                hide robbyneutral at bottom
                show robbyangry at center
                rb " Stupid Oliver... "
                " Robby proceeded to turn the paper into a ball and he threw it into the nearby trash can. "
                hide robbyangry at bottom
                show robbyneutral at center
                rb " He's so...god damn annoying. "
                " You tell Robby that it's gonna be okay since Oliver's not gonna be here for a bit. "
                rb " But he'll come back. "
                rb " And besides, he still has his two goons in this school. "
                rb " It's not like they'll just suddenly stop bullying people just because Oliver's not here. "
                rb " ...But, I guess I'll just enjoy the time of not having Oliver in this school. "
                " You continued to talk with Robby for the rest of the break. "
                " He seemed to be really pissed because of the note Oliver wrote to him, but he managed to calm down the more you talked to him. "
                play sound "audio/bellring.mp3"
                " The bell rings. Yes, the programmer got lazy at writing this part. "
                " You and Robby both get up to go to the next class. "
                scene black with dissolve
                pause 2.0
                jump musicclass1
            else:
                " Seems like he was in deep thought about something. He was staring down at a piece of paper. "
                " He looks...rather shocked. Or disgusted. "
                " You take a look at what he saw... "
                " 'hey so like can u fix my 5000 toys'....it was a note from Oliver that was apparently sent by Edward. "
                " Those toys werent any normal toys, they were the FREAKY kind. "
                x " I have...{w=1}no words. "
                " Me too, Robby. Me too. "
                hide robbyneutral at bottom
                show robbyangry at center
                x " Stupid Oliver... "
                " The boy proceeded to turn the paper into a ball and he threw it into the nearby trash can. "
                hide robbyangry at bottom
                show robbyneutral at center
                x " He's so...god damn annoying. "
                " You tell the guy that it's gonna be okay since Oliver's not gonna be here for a bit. "
                x " But he'll come back. "
                x " And besides, he still has his two goons in this school. "
                x " It's not like they'll just suddenly stop bullying people just because Oliver's not here. "
                x " ...But, I guess I'll just enjoy the time of not having Oliver in this school. "
                " You continued to talk with the other guy for the rest of the break. "
                " He seemed to be really pissed because of the note Oliver wrote to him, but he managed to calm down the more you talked to him. "
                play sound "audio/bellring.mp3"
                " The bell rings. Yes, the programmer got lazy at writing this part. "
                " You and the other guy both get up to go to the next class. "
                scene black with dissolve
                pause 2.0
                jump musicclass1
    label rooftop4:
        scene rooftop with dissolve
        # claire, petunia and lizzy
        " You get up onto the rooftop, and you spot three people that you recognize. "
        " Who do you talk to? "
        if claireknow == True and popularknow == True:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    jump clairerooftopint
                " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                    jump popularrooftopint
                " Just chill around ":
                    jump chillrooftop
        elif claireknow == True and popularknow == False:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    jump clairerooftopint
                " {image=popularicon} Those two popular looking girls. {image=popularicon} ":
                    jump popularrooftopint
                " Just chill around ":
                    jump chillrooftop
        elif claireknow == False and popularknow == True:
            menu:
                " {image=claireicon} A girl with a white bow and short hair. {image=claireicon} ":
                    jump clairerooftopint
                " {image=popularicon} Petunia and Lizzy {image=popularicon} ":
                    jump popularrooftopint
                " Just chill around ":
                    jump chillrooftop
        else:
            menu:
                " {image=claireicon} A girl with a white bow and short hair. {image=claireicon} ":
                    jump clairerooftopint
                " {image=popularicon} Those two popular looking girls. {image=popularicon} ":
                    jump popularrooftopint
                " Just chill around ":
                    jump chillrooftop
        label clairerooftopint:
            " You walk over and sit next to the girl, who seems to be just relaxing and looking at the clouds. "
            show claireneutral at center with easeinright
            if claireknow == True:
                if mean == True and clairebeatup == False:
                    stop music fadeout 0.5
                    " And then you froze again, whilst you were in the middle of walking up to her. "
                    " What's wrong with you? What's making you so afraid of approaching her? "
                    " It's not like she'll do a powerful move and kill you off. That's impossible. "
                    " You take a few steps back, backing up into a wall as you hide away from her. "
                    " What's wrong? "
                    " You don't know what's wrong with you. "
                    " You're supposed to be STRONG. You aren't supposed to be afraid of some girl who's harmless. "
                    " Are you this sensitive to someone hating you? "
                    " Too bad. This was your choice, and now you have to face your consequences. "
                    " There's no turning back from this point. You've lost your second chance. "
                    " Are you this afraid of someone disliking you? "
                    " Did you want everyone to like you? "
                    " It's unfortunate that you got too caught up in yourself trying to make yourself look more dominant, "
                    " Leading to this ending. You feel weak for feeling this way. "
                    " All because you didn't apologize to her? How pathetic. "
                    " Even though she hates you, you still have to stay strong. Not like...this. "
                    " You're weak. You're slowing down because of her. "
                    " You have to keep.{w=0.5} being.{w=0.5} STRONG.{w=0.5} Do you not understand that? "
                    " What a dumb child you are. "
                    " From now on, Claire interactions are disabled. "
                    play sound "audio/bellring.mp3"
                    " ... "
                    " You're starting to think that you should maybe go to a therapist. "
                    " It's not okay to think like this. "
                    " You've been thinking about negative thoughts for the entire break, that's no good at all.. "
                    " You get up from where you were sitting, and you went to go to your classroom for your next class. "
                    scene black with dissolve
                    pause 2.0
                    play music "audio/paperhigh.mp3" fadein 0.5
                    jump musicclass1
                else:
                    c " Hi there, [name]! "
                    c " Sometimes I come up here to take a short break and just look at the clouds. "
                    c " Looking at the sky and nature and other things can really help you calm down, if you're feeling stressed over something! "
                    c " Well, atleast that's my expirience. "
                    c " Stuff is different for everyone. "
                    c " Maybe you like to listen to music to calm you down... Or do other things to distract yourself... "
                    hide claireneutral at bottom
                    show clairehappy at center
                    c " As long as it makes you feel better, then it's okay! "
                    hide clairehappy at bottom
                    show claireneutral at center
                    c " You know... I gotta practice a little something for language class. "
                    c " We have to make a inspirational quote! You don't get to do it though, since you're very new and Ms. Thavel is being nice. "
                    c " I hope you don't mind me practicing for a bit... "
                    " Claire takes a deep breath, before she goes on to practice. "
                    c " Sometimes it's hard for people to calm down, especially if they're going through something serious. "
                    c " But just know that you're suffering now so that you can relax later! "
                    c " Days may seem bad, but you're gonna have better days in the future! "
                    c " Keep going, and if things don't go well... "
                    c " Keep picking yourself back up and go through the storm, you'll find peace eventually! "
                    hide claireneutral at bottom
                    show clairehappy at center
                    c " And that's my totally inspiring words for you! "
                    hide clairehappy at bottom
                    show claireneutral at center
                    c " So... how'd I do? "
                    menu:
                        " You did good ":
                            " You tell her that she did good. "
                            hide claireneutral at bottom
                            show clairehappy at center
                            c " Really? thanks! "
                            scene black with dissolve
                            " You talked a lot with Claire after she practiced a little. "
                            " Mostly just talking about random things because the programmer cant think of anything else to write. "
                            " What? we all have our lazy days. Like you when you're doing homework, you get lazy. "
                            " I probably just called out some people when they do their assignments. "
                            play sound "audio/bellring.mp3"
                            " The bell rings. You walk down the stairs so that you could go to your next class. "
                            pause 2.0
                            jump musicclass1
                        " Needs a lil improvement ":
                            hide claireneutral at bottom
                            show claireconfused at center
                            c " Really? "
                            c " Could you tell me where it needs improvement, and what I should say, then? "
                            " You nod your head before you tried to help Claire with her little assignment. "
                            scene black with dissolve
                            " You spent the rest of the break helping Claire. "
                            " It wasn't too hard, just some little grammarly-like and chatgpt-like ideas... "
                            " They totally won't catch her cheating with this one... "
                            " Totally... "
                            " Wait, it's supposed to be an inspirational message. "
                            " Why are we using grammarly and chat gpt again? "
                            " No clue, just follow the script, I guess. "
                            play sound "audio/bellring.mp3"
                            " The bell rings. You walk down the stairs so that you could go to your next class. "
                            pause 2.0
                            jump musicclass1
            else:
                if mean == True and clairebeatup == False:
                    stop music fadeout 0.5
                    " And then you froze again, whilst you were in the middle of walking up to her. "
                    " What's wrong with you? What's making you so afraid of approaching her? "
                    " It's not like she'll do a powerful move and kill you off. That's impossible. "
                    " You take a few steps back, backing up into a wall as you hide away from her. "
                    " What's wrong? "
                    " You don't know what's wrong with you. "
                    " You're supposed to be STRONG. You aren't supposed to be afraid of some girl who's harmless. "
                    " Are you this sensitive to someone hating you? "
                    " Too bad. This was your choice, and now you have to face your consequences. "
                    " There's no turning back from this point. You've lost your second chance. "
                    " Are you this afraid of someone disliking you? "
                    " Did you want everyone to like you? "
                    " It's unfortunate that you got too caught up in yourself trying to make yourself look more dominant, "
                    " Leading to this ending. You feel weak for feeling this way. "
                    " All because you didn't apologize to her? How pathetic. "
                    " Even though she hates you, you still have to stay strong. Not like...this. "
                    " You're weak. You're slowing down because of her. "
                    " You have to keep.{w=0.5} being.{w=0.5} STRONG.{w=0.5} Do you not understand that? "
                    " What a dumb child you are. "
                    " From now on, Claire interactions are disabled. "
                    play sound "audio/bellring.mp3"
                    " ... "
                    " You're starting to think that you should maybe go to a therapist. "
                    " It's not okay to think like this. "
                    " You've been thinking about negative thoughts for the entire break, that's no good at all.. "
                    " You get up from where you were sitting, and you went to go to your classroom for your next class. "
                    scene black with dissolve
                    pause 2.0
                    play music "audio/paperhigh.mp3" fadein 0.5
                    jump musicclass1
                else:
                    x " Hi there, [name]! "
                    x " I think I haven't introduced myself yet to you, so I might as well do that now! "
                    $ claireknow = True
                    c " Sometimes I come up here to take a short break and just look at the clouds. "
                    c " Looking at the sky and nature and other things can really help you calm down, if you're feeling stressed over something! "
                    c " Well, atleast that's my expirience. "
                    c " Stuff is different for everyone. "
                    c " Maybe you like to listen to music to calm you down... Or do other things to distract yourself... "
                    hide claireneutral at bottom
                    show clairehappy at center
                    c " As long as it makes you feel better, then it's okay! "
                    hide clairehappy at bottom
                    show claireneutral at center
                    c " You know... I gotta practice a little something for language class. "
                    c " We have to make a inspirational quote! You don't get to do it though, since you're very new and Ms. Thavel is being nice. "
                    c " I hope you don't mind me practicing for a bit... "
                    " Claire takes a deep breath, before she goes on to practice. "
                    c " Sometimes it's hard for people to calm down, especially if they're going through something serious. "
                    c " But just know that you're suffering now so that you can relax later! "
                    c " Days may seem bad, but you're gonna have better days in the future! "
                    c " Keep going, and if things don't go well... "
                    c " Keep picking yourself back up and go through the storm, you'll find peace eventually! "
                    hide claireneutral at bottom
                    show clairehappy at center
                    c " And that's my totally inspiring words for you! "
                    hide clairehappy at bottom
                    show claireneutral at center
                    c " So... how'd I do? "
                    menu:
                        " You did good ":
                            " You tell her that she did good. "
                            hide claireneutral at bottom
                            show clairehappy at center
                            c " Really? thanks! "
                            scene black with dissolve
                            " You talked a lot with Claire after she practiced a little. "
                            " Mostly just talking about random things because the programmer cant think of anything else to write. "
                            " What? we all have our lazy days. Like you when you're doing homework, you get lazy. "
                            " I probably just called out some people when they do their assignments. "
                            play sound "audio/bellring.mp3"
                            " The bell rings. You walk down the stairs so that you could go to your next class. "
                            pause 2.0
                            jump musicclass1
                        " Needs a lil improvement ":
                            hide claireneutral at bottom
                            show claireconfused at center
                            c " Really? "
                            c " Could you tell me where it needs improvement, and what I should say, then? "
                            " You nod your head before you tried to help Claire with her little assignment. "
                            scene black with dissolve
                            " You spent the rest of the break helping Claire. "
                            " It wasn't too hard, just some little grammarly-like and chatgpt-like ideas... "
                            " They totally won't catch her cheating with this one... "
                            " Totally... "
                            " Wait, it's supposed to be an inspirational message. "
                            " Why are we using grammarly and chat gpt again? "
                            " No clue, just follow the script, I guess. "
                            play sound "audio/bellring.mp3"
                            " The bell rings. You walk down the stairs so that you could go to your next class. "
                            pause 2.0
                            jump musicclass1
        label popularrooftopint:
            " Let's go and talk to the popular girls, then. "
            show petunianeutral at left with easeinright
            show lizzyneutral at right with easeinright
            if popularknow == True:
                p " Heya there, [name]! "
                lz " Hi there. "
                p " I'm so bored, there's no drama for me to spill! "
                lz " Really? Thought you had atleast a little bit more with you. "
                p " Well, I - OH YEAH! "
                p " You know that Riley girl, yeah? "
                lz " The one that's madly in love with Oliver, yes. "
                lz " It's hard not to know her, she talks about him more than the teachers talk about exams. "
                p " Heh! Well then, I've heard that she got invited to Oliver's house. "
                hide lizzyneutral at bottom
                show lizzyconfused at right
                lz " Woah, now hold on there. Really? "
                hide lizzyconfused at bottom
                show lizzyneutral at right
                lz " There's no way he actually invited her. "
                p " That's the thing! He didn't. "
                p " Turns out, Riley was bothering Skell too much and told her that she just got invited to his house. "
                p " And when she got there, it lead to an abandoned house! "
                p " God, she's so easily to fool whenever it's about Oliver! "
                lz " She's really gotta learn to not believe in things so easily... "
                p " Right? At this rate, she's gonna believe me if I say that Oliver likes her! "
                lz " Most definitely, yeah. She's gonna believe that for years until Oliver has to straight up break it to her that he doesn't like her that way. "
                lz " On the topic of Riley... Seems like she likes it whenever Oliver chooses to bully her. "
                p " Mhm. I remember at the very first day of school, when Oliver called her weird, she started blushing like MAD. "
                lz " And that's the reason why Oliver chooses not to bully her as much. "
                lz " He thinks that she's too weird for her own good, and plus, imagine if you've got someone on your tail 24/7. Yikes. "
                p " Yup! It's really uncomfortable if you're dealing with someone like that, you won't feel safe anywhere! "
                lz " Like in hallways, your own house, hell, even bathrooms. It feels like you really can't escape them. "
                lz " The more you deal with it, the more frustating it gets. "
                lz " And if that continues even more, then you're gonna have to confront them. "
                p " Or file a restraining order on them! "
                lz " Eeeeyeah. Just don't go around bothering and harrassing people, it's really weird. "
                lz " You're gonna look like an absolute creep. "
                p " Uh huh... Honestly, I wouldn't even think of stalking someone just because I like them! "
                p " You gotta take in the fact that they probably don't like you, and stalking them would only lower your chances of getting with them. "
                p " Not everything in books and fanfictions are real, guys! "
                lz " People really gotta start learning that nowadays... "
                play sound "audio/bellring.mp3"
                p " Oh, hey! Looks like the bell rang. "
                lz " We'll see you in class, [name]. "
                p " Buh-bye! "
                scene black with dissolve
                pause 2.0
                jump musicclass1
            else:
                x " Heya there, [name]! "
                x " Hi there. "
                hide petunianeutral at bottom
                show petuniasurprised at left
                x " Wait, Liz, liz! We haven't introduced ourselves to them yet! I just realized! "
                x " Oh, really? I thought that they knew us already... "
                hide petuniasurprised at bottom
                show petunianeutral at left
                x " Well, not yet! You gotta know that there's just some people that don't know us! "
                x " We're not exactly world famous or anything, I mean, we're just popular! "
                x " We only have 190 followers, after all! "
                " ...Wow, no wonder why you haven't heard of them before. "
                $ popularknow = True
                p " I'm Petunia, and this is my best friend, Lizzy! "
                lz " We're inseparable. We're always seen together, we're pretty much an iconic duo around here. "
                p " It's hard to see us without eachother! "
                p " Anywho... "
                p " I'm so bored, there's no drama for me to spill! "
                lz " Really? Thought you had atleast a little bit more with you. "
                p " Well, I - OH YEAH! "
                p " You know that Riley girl, yeah? "
                lz " The one that's madly in love with Oliver, yes. "
                lz " It's hard not to know her, she talks about him more than the teachers talk about exams. "
                p " Heh! Well then, I've heard that she got invited to Oliver's house. "
                hide lizzyneutral at bottom
                show lizzyconfused at right
                lz " Woah, now hold on there. Really? "
                hide lizzyconfused at bottom
                show lizzyneutral at right
                lz " There's no way he actually invited her. "
                p " That's the thing! He didn't. "
                p " Turns out, Riley was bothering Skell too much and told her that she just got invited to his house. "
                p " And when she got there, it lead to an abandoned house! "
                p " God, she's so easily to fool whenever it's about Oliver! "
                lz " She's really gotta learn to not believe in things so easily... "
                p " Right? At this rate, she's gonna believe me if I say that Oliver likes her! "
                lz " Most definitely, yeah. She's gonna believe that for years until Oliver has to straight up break it to her that he doesn't like her that way. "
                lz " On the topic of Riley... Seems like she likes it whenever Oliver chooses to bully her. "
                p " Mhm. I remember at the very first day of school, when Oliver called her weird, she started blushing like MAD. "
                lz " And that's the reason why Oliver chooses not to bully her as much. "
                lz " He thinks that she's too weird for her own good, and plus, imagine if you've got someone on your tail 24/7. Yikes. "
                p " Yup! It's really uncomfortable if you're dealing with someone like that, you won't feel safe anywhere! "
                lz " Like in hallways, your own house, hell, even bathrooms. It feels like you really can't escape them. "
                lz " The more you deal with it, the more frustating it gets. "
                lz " And if that continues even more, then you're gonna have to confront them. "
                p " Or file a restraining order on them! "
                lz " Eeeeyeah. Just don't go around bothering and harrassing people, it's really weird. "
                lz " You're gonna look like an absolute creep. "
                p " Uh huh... Honestly, I wouldn't even think of stalking someone just because I like them! "
                p " You gotta take in the fact that they probably don't like you, and stalking them would only lower your chances of getting with them. "
                p " Not everything in books and fanfictions are real, guys! "
                lz " People really gotta start learning that nowadays... "
                play sound "audio/bellring.mp3"
                p " Oh, hey! Looks like the bell rang. "
                lz " We'll see you in class, [name]. "
                p " Buh-bye! "
                scene black with dissolve
                pause 2.0
                jump musicclass1
        label chillrooftop:
            " You decided not to talk to anyone at all, and you just chillaxed there. "
            " You sat on the ground against a wall and looked up at the sky, looking at the clouds. "
            " You get this rare feeling of peace wash over your body as you look up. "
            " No one's there to bother you. It's just you on this part of the rooftop. "
            " You could just chillax without the loud noises. "
            " You could still faintly hear the sounds of students talking and walking, but you didn't really care. "
            " You just focused on resting for now, as you looked up at the blue sky. "
            " Feel free to take a break here, go get water, or do something. Stay here if needed and continue when ready. "
            play sound "audio/bellring.mp3"
            " After some chilling, you hear the bell ring. "
            " You get up, and you walk back down to go to your next class. "
            scene black with dissolve
            pause 2.0
            jump musicclass1
    label library4:
        scene library with dissolve
        # bubble, cubbie
        " You enter the library, and you see two people that you recognize in your class. "
        " Do you want to approach one of them? If so, which one? "
        if bubbleknow == True and cubbieknow == True:
            menu:
                " {image=bubbleicon} Bubble {image=bubbleicon} ":
                    jump bubblelibraryint
                " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                    jump cubbielibraryint
                " Just hang around in the library ":
                    jump chilllibrary
        elif bubbleknow == True and cubbieknow == False:
            menu:
                " {image=bubbleicon} Bubble {image=bubbleicon} ":
                    jump bubblelibraryint
                " {image=cubbieicon} A cute cat! {image=cubbieicon} ":
                    jump cubbielibraryint
                " Just hang around in the library ":
                    jump chilllibrary
        elif bubbleknow == False and cubbieknow == True:
            menu:
                " {image=bubbleicon} A very 'bubbly' looking girl {image=bubbleicon} ":
                    jump bubblelibraryint
                " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                    jump cubbielibraryint
                " Just hang around in the library ":
                    jump chilllibrary
        else:
            menu:
                " {image=bubbleicon} A very 'bubbly' looking girl {image=bubbleicon} ":
                    jump bubblelibraryint
                " {image=cubbieicon} A cute cat! {image=cubbieicon} ":
                    jump cubbielibraryint
                " Just hang around in the library ":
                    jump chilllibrary
        label bubblelibraryint:
            if bubbleknow == True:
                " You decide to hang out with Bubble for the break. "
                " You walked over to her and sat next to her. "
            else:
                " You decide to hang out with the girl for the break. "
                " You walked over to her and sat next to her. "
            show bubbleneutral at center with easeinright
            if bubbleknow == True:
                b " Hmmmm... "
                " You looked in a little bit closer, and it seems that she's reading a book about ducks. "
                " Seconds later, she starts quietly singing a small tune... "
                b " ...bum bum bum... ba dum ba dum... "
                b " ...A duck walked by to a lemonade stand, and he said to he man, running the stand... "
                b " hey, bum bum bum... got any grapes... "
                " What a familiar tune... too bad you can't put a finger on what song she's singing out though. "
                " It didn't take too long for her to notice you sitting next to her though. "
                b " Hi there, [name]! "
                b " I'm just reading a book about ducks, you see? "
                b " I just think that ducks are the cutest things in the world.. "
                b " That's why I got myself a rubber duck! See that on my head? His name is goobert! "
                b " My family actually gave me this rubber duck, cause they can't afford a real one... "
                b " That doesn't stop my duck obsession, though! "
                b " You've got no idea how much my room is filled with ducks, actually! "
                b " It sounds childish, I know... but I just really like ducks! "
                b " Infact, I know a truckload of facts about ducks! "
                b " Would you like to know some of them? "
                menu:
                    " Give into the duck addiction. Theres no other choice. ":
                        " You nod your head, basically telling her: 'yes i do wanna know about ducks tell me all about them i love ducks too'. "
                        hide bubbleneutral at bottom
                        show bubblehappy at center
                        " She then gets all excited and she looks as if she just fangirled internally. "
                        b " Yayy!! Alrighty, first duck fun fact! Did you know... "
                        scene black with dissolve
                        " You spent the entire break talking about duck facts. You had no other choice anyway... "
                        " Embrace your inner duck, [name]. Theres no escaping it. "
                        " You simply just can't refuse it. You know that ducks are cute. "
                        play sound "audio/bellring.mp3"
                        " Unfortunately, the bell rang and cut you off from knowing any more duck facts. "
                        " You reluctantly get up from your seat and headed off to your classroom. "
                        pause 2.0
                        jump musicclass1
            else:
                x " Hmmmm... "
                " You looked in a little bit closer, and it seems that she's reading a book about ducks. "
                " Seconds later, she starts quietly singing a small tune... "
                x " ...bum bum bum... ba dum ba dum... "
                x " ...A duck walked by to a lemonade stand, and he said to he man, running the stand... "
                x " hey, bum bum bum... got any grapes... "
                " What a familiar tune... too bad you can't put a finger on what song she's singing out though. "
                " It didn't take too long for her to notice you sitting next to her though. "
                x " Hi there, [name]! "
                x " I'm afraid I haven't introduced myself before, so... "
                $ bubbleknow = True
                b " I'm Bubble! We go to the same class. As for what I'm doing? "
                b " I'm just reading a book about ducks, you see? "
                b " I just think that ducks are the cutest things in the world.. "
                b " That's why I got myself a rubber duck! See that on my head? His name is goobert! "
                b " My family actually gave me this rubber duck, cause they can't afford a real one... "
                b " That doesn't stop my duck obsession, though! "
                b " You've got no idea how much my room is filled with ducks, actually! "
                b " It sounds childish, I know... but I just really like ducks! "
                b " Infact, I know a truckload of facts about ducks! "
                b " Would you like to know some of them? "
                menu:
                    " Give into the duck addiction. Theres no other choice. ":
                        " You nod your head, basically telling her: 'yes i do wanna know about ducks tell me all about them i love ducks too'. "
                        hide bubbleneutral at bottom
                        show bubblehappy at center
                        " She then gets all excited and she looks as if she just fangirled internally. "
                        b " Yayy!! Alrighty, first duck fun fact! Did you know... "
                        scene black with dissolve
                        " You spent the entire break talking about duck facts. You had no other choice anyway... "
                        " Embrace your inner duck, [name]. Theres no escaping it. "
                        " You simply just can't refuse it. You know that ducks are cute. "
                        play sound "audio/bellring.mp3"
                        " Unfortunately, the bell rang and cut you off from knowing any more duck facts. "
                        " You reluctantly get up from your seat and headed off to your classroom. "
                        pause 2.0
                        jump musicclass1
        label cubbielibraryint:
            " You decided to go up and sit next to the cute little kitty. "
            show cubbieneutral at center with easeinleft
            if cubbieknow == True:
                cb " ... "
                " Cubbie seems to be reading something. You wonder what it might be... "
                " You lean in a bit closer and it seems he was reading a book about cats. "
                " Seems like he wanted to know a little more about himself. "
                " And it also looks like he noticed that you were there, as well. "
                hide cubbieneutral at bottom
                show cubbiehappy at center
                cb " ...! "
                " Cubbie is happy to see you. He looks at you with a certain look, as if he was silently saying hello to you. "
                hide cubbiehappy at bottom
                show cubbieneutral at center
                cb " ... "
                " Cubbie is pointing at the book, as if he was telling you what he was reading. "
                " Cubbie then pointed at you, then back at the book, then to himself. "
                " Seems like he's asking if you want to read with him. "
                " Would you like to read with him? "
                menu:
                    " Read with the cute little car. There's no other choice. ":
                        hide cubbieneutral at bottom
                        show cubbieamazed at center
                        cb " !!! "
                        " Cubbie seems happy with this decision. "
                        scene black with dissolve
                        " You read a book about cats with Cubbie for the entire break. "
                        " At one point, Cubbie must've felt a bit sleepy. "
                        " He was resting his head on your shoulder as he read, maybe he just needed a little rest... "
                        play sound "audio/bellring.mp3"
                        " Though, the bell ringing a few minutes later seemed to have woken him up. "
                        " He thanked you for your time silently and you both got up to  go to the next class. "
                        pause 2.0
                        jump musicclass1
            else:
                x " ... "
                $ cubbieknow = True
                " From what you've heard, this little guy's name was Cubbie. "
                " He doesn't really speak a lot. Not like he's mute or anything, he just prefers not to speak at all. "
                " It's considered a little rare whenever he does, though. "
                " The little cat seems to be reading something. You wonder what it might be... "
                " You lean in a bit closer and it seems he was reading a book about cats. "
                " Seems like he wanted to know a little more about himself. "
                " And it also looks like he noticed that you were there, as well. "
                hide cubbieneutral at bottom
                show cubbiehappy at center
                cb " ...! "
                " Cubbie is happy to see you. He looks at you with a certain look, as if he was silently saying hello to you. "
                hide cubbiehappy at bottom
                show cubbieneutral at center
                cb " ... "
                " Cubbie is pointing at the book, as if he was telling you what he was reading. "
                " Cubbie then pointed at you, then back at the book, then to himself. "
                " Seems like he's asking if you want to read with him. "
                " Would you like to read with him? "
                menu:
                    " Read with the cute little car. There's no other choice. ":
                        hide cubbieneutral at bottom
                        show cubbieamazed at center
                        cb " !!! "
                        " Cubbie seems happy with this decision. "
                        scene black with dissolve
                        " You read a book about cats with Cubbie for the entire break. "
                        " At one point, Cubbie must've felt a bit sleepy. "
                        " He was resting his head on your shoulder as he read, maybe he just needed a little rest... "
                        play sound "audio/bellring.mp3"
                        " Though, the bell ringing a few minutes later seemed to have woken him up. "
                        " He thanked you for your time silently and you both got up to  go to the next class. "
                        pause 2.0
                        jump musicclass1
        label chilllibrary:
            " You decided not to interact with them at all, and just chillaxed at a random empty table. "
            " With this time, you took a short nap there. "
            " You needed a little rest, after all. You were feeling just a little bit tired. "
            scene black with dissolve
            pause 2.0
            play sound "audio/bellring.mp3"
            " It only took about a few mintues until the bell rang and woke you up. "
            " It felt like you've only been asleep for a second, but yuo've been asleep for about 30 minutes. "
            " You tiredly get out of your chair and went to your classroom for the next class. "
            pause 2.0
            jump musicclass1
    label musicclass1:
        scene classroom with dissolve
        " You sit down on your chair, and you see the music teacher glide into the room, as if he was rushing to not get late. "
        show mrdemineutral at center with easeinright
        msd " *intense breathing from how much he was trying to get into the classroom*... "
        msd " U-uhm... Sorry class, I was just dealing with an...issue in the cafeteria. "
        msd " (God, that was so embarrassing...) "
        msd " (I'll just have to make sure that doesn't happen again...) "
        msd " ...A-anyway, let's get started with the class! "
        scene black with dissolve
        " While Mister Demi was teaching, you couldn't help but wonder what had happened at the cafeteria. "
        " That thought lingered in your mind for the rest of the lesson. "
        pause 1.0
        play sound "audio/bellring.mp3"
        " The bell rang, indicating that it was the end of the class. "
        " You then get up to go onto the hallways to find somewhere you can chill at. "
        pause 2.0
        jump break5
    label break5:
        scene hallway with dissolve
        " It's the last break for the day. "
        " Where do you go? "
        menu:
            " {image=robbyicon} The front of the school {image=rileyicon} ":
                scene black with dissolve
                pause 2.0
                jump frontschool5
            " {image=skellicon} The back of the school {image=skellicon} ":
                scene black with dissolve
                pause 2.0
                jump backschool5
            " {image=claireicon} The gym {image=kevinicon} ":
                scene black with dissolve
                pause 2.0
                jump gym5
            " {image=bubbleicon} The cafeteria {image=lanaicon} ":
                scene black with dissolve
                pause 2.0
                jump cafe5
            " The rooftop ":
                scene black with dissolve
                pause 2.0
                jump rooftop5
            " {image=popularicon} The library {image=popularicon} ":
                scene black with dissolve
                pause 2.0
                jump library5
    label frontschool5:
        scene paperschoolfront with dissolve
        # Robby, Riley
        " You step out into the fron of the school, and you could hear an argument going on. "
        " You decided to listen onto what was going on... "
        show robbyneutral at right with easeinleft
        show rileyangry at left with easeinleft
        if robbyknow == True and rileyknow == True:
            ri " CAN YOU BELIEVE IT?! I GOT SCAMMED! " with vpunch
            rb " Come on, Riley. You know that Oliver would never invite you to his house. "
            ri " SKELL IS SUCH A DIRTY LIAR FOR SAYING THAT HE LIKES ME! "
            rb " Technically Skell said that Oliver wanted you to come over to his house, but okay. "
            rb " And also, you were bothering him so he had to use something to get you away from him. "
            ri " NOT TO MENTION, HE'S SUCH A MEANIE! HE DIDN'T WANT TO LISTEN TO MY RAMBLINGS ABOUT MY SWEET, BELOVED OLIVER! "
            rb " Look, Riley... Not everyone wants to listen to you. "
            rb " Either they're pretending that they're actually listening, or they already ran away before you even noticed. "
            rb " Plus, you're gonna hurt people's ears if you keep on screaming and screaming to them about how much you like Oliver. "
            rb " One day you're gonna get someone to a hospital if you keep shouting so loudly. "
            ri " ... "
            hide rileyangry at bottom
            show rileysad at left
            ri " {sc}WAAAAAAAAAAAAAAAAAH!!{/sc} YOU'RE SUCH A MEANIE!!! " with vpunch
            hide robbyneutral at bottom
            show robbyangry at right
            " Wow, and he was only saying the truth to her... "
            " How exactly was he the meanie here? Is she just that persistent on wanting people to hear her ramblings about this 'Oliver' guy...? "
            rb " Jeez, please stop screaming and crying...! My ears are hurting! "
            ri " YOU'RE SO MEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANN!! " with vpunch
            rb " Hey, I only said the truth! You really gotta tone down sometimes...! "
            " Your ears are starting to hurt aswell... "
            " You should probably do something to stop her from screaming so much. "
            " What should you do? "
            menu:
                " Lie to her ":
                    " You slowly go up to her and you put a hand on her shouder, grabbing her attention. "
                    hide robbyangry at bottom
                    show robbyneutral at right
                    " You told Riley that Oliver is gonna come back soon, and that she could talk to him a lot. "
                    ri " Really? You promise? "
                    " You promise, even though you know that it's just a lie to shut her up. "
                    ri " ... "
                    hide rileysad at bottom
                    show rileyhappy at left
                    ri " Okay! "
                    " Geez, fooling her really {i}is{/i} easy... "
                    " Atleast you got her to shut up now. "
                    hide rileyhappy at right with easeoutright
                    show robbyneutral at center with move
                    " Riley skips away, beaming with joy about the lie that you just told her. "
                    " Oh, Riley... you really gotta tell when someone's lying to you or not. "
                    " You can't just believe everything someone says, especially if it's about Oliver. "
                    rb " ...Whew... my ears are saved. "
                    rb " Thanks for uh... distracting her. "
                    rb " She's a little annoying... but I can't just say that straight to her face. "
                    rb " She'd actually make an attempt to make my ears stop working. "
                    rb " Thanks again, [name]. "
                    play sound "audio/bellring.mp3"
                    rb " Seems like it's time for class... "
                    rb " I'll see you there, [name]. "
                    scene black with dissolve
                    pause 2.0
                    jump artclass1
                " Leave ":
                    " Nope. You're not dealing with this. "
                    " Guess Robby's gonna have to deal with this alone. "
                    scene black with dissolve
                    " You enter the school, and even when you're in the hallways, you could still hear Riley screaming. "
                    " It got so bad that it got the other students in the hallway to talk about it... "
                    " Geez, how long does this have to go for? "
                    play sound "audio/bellring.mp3"
                    " Thankfully, the screaming stops when the bell rings moments later. "
                    " Now you can go to your classroom in peace, without the sound of screaming in your ears. "
                    pause 2.0
                    jump artclass1
        elif robbyknow == True and rileyknow == False:
            x " CAN YOU BELIEVE IT?! I GOT SCAMMED! " with vpunch
            rb " Come on, Riley. You know that Oliver would never invite you to his house. "
            x " SKELL IS SUCH A DIRTY LIAR FOR SAYING THAT HE LIKES ME! "
            rb " Technically Skell said that Oliver wanted you to come over to his house, but okay. "
            rb " And also, you were bothering him so he had to use something to get you away from him. "
            x " NOT TO MENTION, HE'S SUCH A MEANIE! HE DIDN'T WANT TO LISTEN TO MY RAMBLINGS ABOUT MY SWEET, BELOVED OLIVER! "
            rb " Look, Riley... Not everyone wants to listen to you. "
            rb " Either they're pretending that they're actually listening, or they already ran away before you even noticed. "
            rb " Plus, you're gonna hurt people's ears if you keep on screaming and screaming to them about how much you like Oliver. "
            rb " One day you're gonna get someone to a hospital if you keep shouting so loudly. "
            x " ... "
            hide rileyangry at bottom
            show rileysad at left
            x " {sc}WAAAAAAAAAAAAAAAAAH!!{/sc} YOU'RE SUCH A MEANIE!!! " with vpunch
            hide robbyneutral at bottom
            show robbyangry at right
            " Wow, and he was only saying the truth to her... "
            " How exactly was he the meanie here? Is she just that persistent on wanting people to hear her ramblings about this 'Oliver' guy...? "
            rb " Jeez, please stop screaming and crying...! My ears are hurting! "
            x " YOU'RE SO MEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANN!! " with vpunch
            rb " Hey, I only said the truth! You really gotta tone down sometimes...! "
            " Your ears are starting to hurt aswell... "
            " You should probably do something to stop her from screaming so much. "
            " What should you do? "
            menu:
                " Lie to her ":
                    " You slowly go up to her and you put a hand on her shouder, grabbing her attention. "
                    hide robbyangry at bottom
                    show robbyneutral at right
                    " You told the girl that Oliver is gonna come back soon, and that she could talk to him a lot. "
                    x " Really? You promise? "
                    " You promise, even though you know that it's just a lie to shut her up. "
                    x " ... "
                    hide rileysad at bottom
                    show rileyhappy at left
                    x " Okay! "
                    " Geez, fooling her really {i}is{/i} easy... "
                    " Atleast you got her to shut up now. "
                    hide rileyhappy at right with easeoutright
                    show robbyneutral at center with move
                    " The girl skips away, beaming with joy about the lie that you just told her. "
                    " Oh boy... that girl really has to learn how to tell when someone's lying to you or not. "
                    " You can't just believe everything someone says, especially if it's about Oliver. "
                    rb " ...Whew... my ears are saved. "
                    $ rileyknow = True
                    rb " That girl just now... her name is Riley. She's like that all the time. "
                    rb " Thanks for uh... distracting her. "
                    rb " She's a little annoying... but I can't just say that straight to her face. "
                    rb " She'd actually make an attempt to make my ears stop working. "
                    rb " Thanks again, [name]. "
                    play sound "audio/bellring.mp3"
                    rb " Seems like it's time for class... "
                    rb " I'll see you there, [name]. "
                    scene black with dissolve
                    pause 2.0
                    jump artclass1
                " Leave ":
                    " Nope. You're not dealing with this. "
                    " Guess Robby's gonna have to deal with this alone. "
                    scene black with dissolve
                    " You enter the school, and even when you're in the hallways, you could still hear the girl screaming. "
                    " It got so bad that it got the other students in the hallway to talk about it... "
                    " Geez, how long does this have to go for? "
                    play sound "audio/bellring.mp3"
                    " Thankfully, the screaming stops when the bell rings moments later. "
                    " Now you can go to your classroom in peace, without the sound of screaming in your ears. "
                    pause 2.0
                    jump artclass1
        elif robbyknow == False and rileyknow == True:
            ri " CAN YOU BELIEVE IT?! I GOT SCAMMED! " with vpunch
            x " Come on, Riley. You know that Oliver would never invite you to his house. "
            ri " SKELL IS SUCH A DIRTY LIAR FOR SAYING THAT HE LIKES ME! "
            x " Technically Skell said that Oliver wanted you to come over to his house, but okay. "
            x " And also, you were bothering him so he had to use something to get you away from him. "
            ri " NOT TO MENTION, HE'S SUCH A MEANIE! HE DIDN'T WANT TO LISTEN TO MY RAMBLINGS ABOUT MY SWEET, BELOVED OLIVER! "
            x " Look, Riley... Not everyone wants to listen to you. "
            x " Either they're pretending that they're actually listening, or they already ran away before you even noticed. "
            x " Plus, you're gonna hurt people's ears if you keep on screaming and screaming to them about how much you like Oliver. "
            x " One day you're gonna get someone to a hospital if you keep shouting so loudly. "
            ri " ... "
            hide rileyangry at bottom
            show rileysad at left
            ri " {sc}WAAAAAAAAAAAAAAAAAH!!{/sc} YOU'RE SUCH A MEANIE!!! " with vpunch
            hide robbyneutral at bottom
            show robbyangry at right
            " Wow, and he was only saying the truth to her... "
            " How exactly was he the meanie here? Is she just that persistent on wanting people to hear her ramblings about this 'Oliver' guy...? "
            x " Jeez, please stop screaming and crying...! My ears are hurting! "
            ri " YOU'RE SO MEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANN!! " with vpunch
            x " Hey, I only said the truth! You really gotta tone down sometimes...! "
            " Your ears are starting to hurt aswell... "
            " You should probably do something to stop her from screaming so much. "
            " What should you do? "
            menu:
                " Lie to her ":
                    " You slowly go up to her and you put a hand on her shouder, grabbing her attention. "
                    hide robbyangry at bottom
                    show robbyneutral at right
                    " You told Riley that Oliver is gonna come back soon, and that she could talk to him a lot. "
                    ri " Really? You promise? "
                    " You promise, even though you know that it's just a lie to shut her up. "
                    ri " ... "
                    hide rileysad at bottom
                    show rileyhappy at left
                    ri " Okay! "
                    " Geez, fooling her really {i}is{/i} easy... "
                    " Atleast you got her to shut up now. "
                    hide rileyhappy at right with easeoutright
                    show robbyneutral at center with move
                    " Riley skips away, beaming with joy about the lie that you just told her. "
                    " Oh, Riley... you really gotta tell when someone's lying to you or not. "
                    " You can't just believe everything someone says, especially if it's about Oliver. "
                    x " ...Whew... my ears are saved. "
                    x " Thanks for uh... distracting her. "
                    $ robbyknow = True
                    rb " I'm Robby. We go to the same class. As for that girl... "
                    rb " She's a little annoying... but I can't just say that straight to her face. "
                    rb " She'd actually make an attempt to make my ears stop working. "
                    rb " Thanks again, [name]. "
                    play sound "audio/bellring.mp3"
                    rb " Seems like it's time for class... "
                    rb " I'll see you there, [name]. "
                    scene black with dissolve
                    pause 2.0
                    jump artclass1
                " Leave ":
                    " Nope. You're not dealing with this. "
                    " Guess that boy is just gonna have to deal with this alone. "
                    scene black with dissolve
                    " You enter the school, and even when you're in the hallways, you could still hear Riley screaming. "
                    " It got so bad that it got the other students in the hallway to talk about it... "
                    " Geez, how long does this have to go for? "
                    play sound "audio/bellring.mp3"
                    " Thankfully, the screaming stops when the bell rings moments later. "
                    " Now you can go to your classroom in peace, without the sound of screaming in your ears. "
                    pause 2.0
                    jump artclass1
        else:
            x " CAN YOU BELIEVE IT?! I GOT SCAMMED! " with vpunch
            x " Come on, Riley. You know that Oliver would never invite you to his house. "
            x " SKELL IS SUCH A DIRTY LIAR FOR SAYING THAT HE LIKES ME! "
            x " Technically Skell said that Oliver wanted you to come over to his house, but okay. "
            x " And also, you were bothering him so he had to use something to get you away from him. "
            x " NOT TO MENTION, HE'S SUCH A MEANIE! HE DIDN'T WANT TO LISTEN TO MY RAMBLINGS ABOUT MY SWEET, BELOVED OLIVER! "
            x " Look, Riley... Not everyone wants to listen to you. "
            x " Either they're pretending that they're actually listening, or they already ran away before you even noticed. "
            x " Plus, you're gonna hurt people's ears if you keep on screaming and screaming to them about how much you like Oliver. "
            x " One day you're gonna get someone to a hospital if you keep shouting so loudly. "
            x " ... "
            hide rileyangry at bottom
            show rileysad at left
            x " {sc}WAAAAAAAAAAAAAAAAAH!!{/sc} YOU'RE SUCH A MEANIE!!! " with vpunch
            hide robbyneutral at bottom
            show robbyangry at right
            " Wow, and he was only saying the truth to her... "
            " How exactly was he the meanie here? Is she just that persistent on wanting people to hear her ramblings about this 'Oliver' guy...? "
            x " Jeez, please stop screaming and crying...! My ears are hurting! "
            x " YOU'RE SO MEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANN!! " with vpunch
            x " Hey, I only said the truth! You really gotta tone down sometimes...! "
            " Your ears are starting to hurt aswell... "
            " You should probably do something to stop her from screaming so much. "
            " What should you do? "
            menu:
                " Lie to her ":
                    " You slowly go up to her and you put a hand on her shouder, grabbing her attention. "
                    hide robbyangry at bottom
                    show robbyneutral at right
                    " You told the girl that Oliver is gonna come back soon, and that she could talk to him a lot. "
                    x " Really? You promise? "
                    " You promise, even though you know that it's just a lie to shut her up. "
                    x " ... "
                    hide rileysad at bottom
                    show rileyhappy at left
                    x " Okay! "
                    " Geez, fooling her really {i}is{/i} easy... "
                    " Atleast you got her to shut up now. "
                    hide rileyhappy at right with easeoutright
                    show robbyneutral at center with move
                    " The girl skips away, beaming with joy about the lie that you just told her. "
                    " Oh boy... that girl really has to learn how to tell when someone's lying to you or not. "
                    " You can't just believe everything someone says, especially if it's about Oliver. "
                    x " ...Whew... my ears are saved. "
                    $ rileyknow = True
                    x " That girl just now... her name is Riley. She's like that all the time. "
                    x " Thanks for uh... distracting her. "
                    x " I almost for got to introduce myself, my apologies... "
                    $ robbyknow = True
                    rb " I'm Robby. We're in the same class. As for that girl... "
                    rb " She's a little annoying... but I can't just say that straight to her face. "
                    rb " She'd actually make an attempt to make my ears stop working. "
                    rb " Thanks again, [name]. "
                    play sound "audio/bellring.mp3"
                    rb " Seems like it's time for class... "
                    rb " I'll see you there, [name]. "
                    scene black with dissolve
                    pause 2.0
                    jump artclass1
                " Leave ":
                    " Nope. You're not dealing with this. "
                    " Guess that guy's just gonna have to deal with this alone. "
                    scene black with dissolve
                    " You enter the school, and even when you're in the hallways, you could still hear the girl screaming. "
                    " It got so bad that it got the other students in the hallway to talk about it... "
                    " Geez, how long does this have to go for? "
                    play sound "audio/bellring.mp3"
                    " Thankfully, the screaming stops when the bell rings moments later. "
                    " Now you can go to your classroom in peace, without the sound of screaming in your ears. "
                    pause 2.0
                    jump artclass1
    label backschool5:
        scene paperschoolback with dissolve
        # skell
        " You walk to the back of the school, and you could hear some faint singing. "
        " You look around a corner, to see a familiar emo black cat with wings singing a song... "
        show skellhappy at center with easeinright
        if skellknow == True:
            sk " ...(insert lyrics to the song rabbit hole except its the english cover from will stetson)... "
            " Woah, Skell! those are some FREAKY lyrics! "
            " You didn't know that Skell was like that... "
            " You're starting to think of Skell in the outfit of the character in that music video... "
            " wait stop that thought is "
            " IS THE MC GAY?!?!?!? "
            " wait naw technically if the mc chose the girl option it would be straight but like "
            " to the homies that chose the guy option oh boy! "
            " Skell, after finishing his little concert, seems to have notice you... "
            hide skellhappy at bottom
            show skellsurprised at center
            " ...And is very visibly embarrassed. You did just listen to him sing a song about... you know. "
            sk " ... "
            sk " Listen, I can explain myself... "
            " Yeah Skell are you sure you can get yourself out of this "
            hide skellsurprised at bottom
            show skellneutral at center
            sk " ...I just really like the song, alright? It's a banger, I don't actually relate to the songs lyrics or anything like that. "
            sk " I'm still a kid, you know. It's gonna be weird if I already thought of actually doing THAT at this young age. "
            sk " I prefer doing stuff like that when I'm older... "
            hide skellneutral at bottom
            show skellsurprised at center
            sk " Wait, that just proves that I want that stuff to happen to me but only if I'm older... "
            sk " Shit, how do I get myself out of this... "
            scene black with dissolve
            " You listened to Skell trying to explain himself to you. "
            " Honestly, he was just stuttering all the time and it was hard for you to understand what he was saying. "
            play sound "audio/bellring.mp3"
            " He gave up when the bell rang. "
            " You just helped him up and you both went to the last class of the day. "
            pause 2.0
            jump artclass1
        else:
            x " ...(insert lyrics to the song rabbit hole except its the english cover from will stetson)... "
            " Woah, buddy! those are some FREAKY lyrics! "
            " You didn't know that Skell was like that... "
            " You're starting to think of Skell in the outfit of the character in that music video... "
            " wait stop that thought is "
            " IS THE MC GAY?!?!?!? "
            " wait naw technically if the mc chose the girl option it would be straight but like "
            " to the homies that chose the guy option oh boy! "
            " The emo cat guy, after finishing his little concert, seems to have notice you... "
            hide skellhappy at bottom
            show skellsurprised at center
            " ...And is very visibly embarrassed. You did just listen to him sing a song about... you know. "
            x " ... "
            x " Listen, I can explain myself... "
            " Yeah dude are you sure you can get yourself out of this "
            hide skellsurprised at bottom
            show skellneutral at center
            x " ...I just really like the song, alright? It's a banger, I don't actually relate to the songs lyrics or anything like that. "
            x " I'm still a kid, you know. It's gonna be weird if I already thought of actually doing THAT at this young age. "
            x " I prefer doing stuff like that when I'm older... "
            hide skellneutral at bottom
            show skellsurprised at center
            x " Wait, that just proves that I want that stuff to happen to me but only if I'm older... "
            x " Shit, how do I get myself out of this... "
            scene black with dissolve
            " You listened to the guy trying to explain himself to you. "
            " Honestly, he was just stuttering all the time and it was hard for you to understand what he was saying. "
            play sound "audio/bellring.mp3"
            " He gave up when the bell rang. "
            " You just helped him up and you both went to the last class of the day. "
            pause 2.0
            jump artclass1
    label gym5:
        scene gym with dissolve
        # Claire, Kevin
        " You walked into the gym, and you spot two people you recognize from your class... "
        " Do you sit next to one of them, or do you just sit alone? "
        if claireknow == True and kevinknow == True:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    jump clairechillaxer
                " {image=kevinicon} Kevin {image=kevinicon} ":
                    jump kevinchillaxer
                " Nah, I'd chill. ":
                    jump gymchillaxer
        elif claireknow == True and kevinknow == False:
            menu:
                " {image=claireicon} Claire {image=claireicon} ":
                    jump clairechillaxer
                " {image=kevinicon} A nerd {image=kevinicon} ":
                    jump kevinchillaxer
                " Nah, I'd chill. ":
                    jump gymchillaxer
        elif claireknow == False and kevinknow == True:
            menu:
                " {image=claireicon} A girl with a bow on her {image=claireicon} ":
                    jump clairechillaxer
                " {image=kevinicon} Kevin {image=kevinicon} ":
                    jump kevinchillaxer
                " Nah, I'd chill. ":
                    jump gymchillaxer
        else:
            menu:
                " {image=claireicon} A girl with a bow on her {image=claireicon} ":
                    jump clairechillaxer
                " {image=kevinicon} A nerd {image=kevinicon} ":
                    jump kevinchillaxer
                " Nah, I'd chill. ":
                    jump gymchillaxer
        label clairechillaxer:
            if clairebeatup == True and clairesorry == False:
                " No. "
                scene black
                pause 2.0
                jump gymchillaxer
            elif clairebeatup == True and clairesorry == True:
                " You walk up to Claire, curious as to what she was doing. "
                show claireneutral at center with easeinleft
                " She seemed to be watching a k-drama on her phone... "
                " You can't exactly tell what was going on due to the fact that she was wearing earphones, "
                " But it looks like a married couple is fighting at the moment. "
                " How'd you know that they were married? You don't really know. There was just this feeling. "
                " Claire notices you after a moment, and paused her little watching session. "
                c " Hey there, [name]! "
                c " I'm watching this new k-drama Petunia recommended to me! "
                c " It's pretty interesting...and emotional, too! I like how they wrote the characters! "
                c " Petunia really chose a good one for me, since I just started out watching K-dramas... "
                c " This is actually my first one that I've ever watched! "
                c " Do you perhaps want to watch with me? It's okay if not! "
                c " You can just chill around me if that's what you wanted. "
                menu:
                    " Watch with Claire ":
                        c " Okay! Here we go! "
                        " Claire lends you one of her earphones for you to hear what was going on. "
                        " You put it on and began to watch the k-drama with her. "
                        scene black with dissolve
                        " You spent the entire break watching a k-drama with Claire. "
                        " You honestly got a bit mad and emotional at some parts, cause of what the characters were doing. "
                        " You never knew K-dramas were this good... "
                        " You should probably look at some other k-dramas. Though you gotta be careful not to form an addiction. "
                        " You don't want to be those weird and creepy k drama people you keep seeing in youtube documentaries or something. "
                        " It would've been bad if you became one of them, eeyikes... "
                        play sound "audio/bellring.mp3"
                        " The bell rings, you and Claire pause the video and get up. "
                        " Claire promises that she might continue watching with you if you want to. "
                        " You then went to your classroom for the final class of the day. "
                        pause 2.0
                        jump artclass1
                    " Just chill ":
                        c " Alrighty! Just tap my shoulder if you need me for anything! "
                        scene black with dissolve
                        " You spent the break hanging out with Claire, who was watching a K-drama. "
                        " You two didn't really talk much since she was busy watching, but you were just vibing. "
                        " You were scrolling through your tiktok fyp anyway, so atleast you had some entertainment. "
                        play sound "audio/bellring.mp3"
                        " Wow, time sure does go faster when you're focused on a gadget... "
                        " You tapped Claire's shoulder and told her that it was time to go to class. "
                        " Afterwards, the both of you get up your seats and head down to the last class for the day. "
                        pause 2.0
                        jump artlcass1
            elif claireknow == True and clairebeatup == False:
                " You walk up to Claire, curious as to what she was doing. "
                show claireneutral at center with easeinleft
                " She seemed to be watching a k-drama on her phone... "
                " You can't exactly tell what was going on due to the fact that she was wearing earphones, "
                " But it looks like a married couple is fighting at the moment. "
                " How'd you know that they were married? You don't really know. There was just this feeling. "
                " Claire notices you after a moment, and paused her little watching session. "
                c " Hey there, [name]! "
                c " I'm watching this new k-drama Petunia recommended to me! "
                c " It's pretty interesting...and emotional, too! I like how they wrote the characters! "
                c " Petunia really chose a good one for me, since I just started out watching K-dramas... "
                c " This is actually my first one that I've ever watched! "
                c " Do you perhaps want to watch with me? It's okay if not! "
                c " You can just chill around me if that's what you wanted. "
                menu:
                    " Watch with Claire ":
                        c " Okay! Here we go! "
                        " Claire lends you one of her earphones for you to hear what was going on. "
                        " You put it on and began to watch the k-drama with her. "
                        scene black with dissolve
                        " You spent the entire break watching a k-drama with Claire. "
                        " You honestly got a bit mad and emotional at some parts, cause of what the characters were doing. "
                        " You never knew K-dramas were this good... "
                        " You should probably look at some other k-dramas. Though you gotta be careful not to form an addiction. "
                        " You don't want to be those weird and creepy k drama people you keep seeing in youtube documentaries or something. "
                        " It would've been bad if you became one of them, eeyikes... "
                        play sound "audio/bellring.mp3"
                        " The bell rings, you and Claire pause the video and get up. "
                        " Claire promises that she might continue watching with you if you want to. "
                        " You then went to your classroom for the final class of the day. "
                        pause 2.0
                        jump artclass1
                    " Just chill ":
                        c " Alrighty! Just tap my shoulder if you need me for anything! "
                        scene black with dissolve
                        " You spent the break hanging out with Claire, who was watching a K-drama. "
                        " You two didn't really talk much since she was busy watching, but you were just vibing. "
                        " You were scrolling through your tiktok fyp anyway, so atleast you had some entertainment. "
                        play sound "audio/bellring.mp3"
                        " Wow, time sure does go faster when you're focused on a gadget... "
                        " You tapped Claire's shoulder and told her that it was time to go to class. "
                        " Afterwards, the both of you get up your seats and head down to the last class for the day. "
                        pause 2.0
                        jump artlcass1
            elif claireknow == False and clairebeatup == False:
                " You walk up to the girl, curious as to what she was doing. "
                show claireneutral at center with easeinleft
                " She seemed to be watching a k-drama on her phone... "
                " You can't exactly tell what was going on due to the fact that she was wearing earphones, "
                " But it looks like a married couple is fighting at the moment. "
                " How'd you know that they were married? You don't really know. There was just this feeling. "
                " She notices you after a moment, and paused her little watching session. "
                x " Hey there, [name]! "
                x " Don't think I got to introduce myself to you before, so... "
                $ claireknow = True
                hide claireneutral at bottom
                show clairehappy at center
                c " I'm Claire! Nice to meet you! We also go to the same class! As for what I'm doing... "
                hide clairehappy at bottom
                show claireneutral at center
                c " I'm watching this new k-drama Petunia recommended to me! "
                c " It's pretty interesting...and emotional, too! I like how they wrote the characters! "
                c " Petunia really chose a good one for me, since I just started out watching K-dramas... "
                c " This is actually my first one that I've ever watched! "
                c " Do you perhaps want to watch with me? It's okay if not! "
                c " You can just chill around me if that's what you wanted. "
                menu:
                    " Watch with Claire ":
                        c " Okay! Here we go! "
                        " Claire lends you one of her earphones for you to hear what was going on. "
                        " You put it on and began to watch the k-drama with her. "
                        scene black with dissolve
                        " You spent the entire break watching a k-drama with Claire. "
                        " You honestly got a bit mad and emotional at some parts, cause of what the characters were doing. "
                        " You never knew K-dramas were this good... "
                        " You should probably look at some other k-dramas. Though you gotta be careful not to form an addiction. "
                        " You don't want to be those weird and creepy k drama people you keep seeing in youtube documentaries or something. "
                        " It would've been bad if you became one of them, eeyikes... "
                        play sound "audio/bellring.mp3"
                        " The bell rings, you and Claire pause the video and get up. "
                        " Claire promises that she might continue watching with you if you want to. "
                        " You then went to your classroom for the final class of the day. "
                        pause 2.0
                        jump artclass1
                    " Just chill ":
                        c " Alrighty! Just tap my shoulder if you need me for anything! "
                        scene black with dissolve
                        " You spent the break hanging out with Claire, who was watching a K-drama. "
                        " You two didn't really talk much since she was busy watching, but you were just vibing. "
                        " You were scrolling through your tiktok fyp anyway, so atleast you had some entertainment. "
                        play sound "audio/bellring.mp3"
                        " Wow, time sure does go faster when you're focused on a gadget... "
                        " You tapped Claire's shoulder and told her that it was time to go to class. "
                        " Afterwards, the both of you get up your seats and head down to the last class for the day. "
                        pause 2.0
                        jump artlcass1
            else:
                " You walk up to the girl, curious as to what she was doing. "
                show claireneutral at center with easeinleft
                " She seemed to be watching a k-drama on her phone... "
                " You can't exactly tell what was going on due to the fact that she was wearing earphones, "
                " But it looks like a married couple is fighting at the moment. "
                " How'd you know that they were married? You don't really know. There was just this feeling. "
                " She notices you after a moment, and paused her little watching session. "
                x " Hey there, [name]! "
                x " Don't think I got to introduce myself to you before, so... "
                $ claireknow = True
                hide claireneutral at bottom
                show clairehappy at center
                c " I'm Claire! Nice to meet you! We also go to the same class! As for what I'm doing... "
                hide clairehappy at bottom
                show claireneutral at center
                c " I'm watching this new k-drama Petunia recommended to me! "
                c " It's pretty interesting...and emotional, too! I like how they wrote the characters! "
                c " Petunia really chose a good one for me, since I just started out watching K-dramas... "
                c " This is actually my first one that I've ever watched! "
                c " Do you perhaps want to watch with me? It's okay if not! "
                c " You can just chill around me if that's what you wanted. "
                menu:
                    " Watch with Claire ":
                        c " Okay! Here we go! "
                        " Claire lends you one of her earphones for you to hear what was going on. "
                        " You put it on and began to watch the k-drama with her. "
                        scene black with dissolve
                        " You spent the entire break watching a k-drama with Claire. "
                        " You honestly got a bit mad and emotional at some parts, cause of what the characters were doing. "
                        " You never knew K-dramas were this good... "
                        " You should probably look at some other k-dramas. Though you gotta be careful not to form an addiction. "
                        " You don't want to be those weird and creepy k drama people you keep seeing in youtube documentaries or something. "
                        " It would've been bad if you became one of them, eeyikes... "
                        play sound "audio/bellring.mp3"
                        " The bell rings, you and Claire pause the video and get up. "
                        " Claire promises that she might continue watching with you if you want to. "
                        " You then went to your classroom for the final class of the day. "
                        pause 2.0
                        jump artclass1
                    " Just chill ":
                        c " Alrighty! Just tap my shoulder if you need me for anything! "
                        scene black with dissolve
                        " You spent the break hanging out with Claire, who was watching a K-drama. "
                        " You two didn't really talk much since she was busy watching, but you were just vibing. "
                        " You were scrolling through your tiktok fyp anyway, so atleast you had some entertainment. "
                        play sound "audio/bellring.mp3"
                        " Wow, time sure does go faster when you're focused on a gadget... "
                        " You tapped Claire's shoulder and told her that it was time to go to class. "
                        " Afterwards, the both of you get up your seats and head down to the last class for the day. "
                        pause 2.0
                        jump artlcass1
        label kevinchillaxer:
            " You decide to sit next to the nerd, wondering what he was doing. "
            show kevinneutral at center with easeinright
            if kevinknow == True:
                " Kevin seemed to be watching a little show of his... "
                " From what you could see, he was watching something about magical girls. "
                hide kevinneutral at bottom
                show kevinsurprised at center
                " Though, he quickly notices that you were there and he immediately hides his phone away from you due to embarrassment. "
                hide kevinsurprised at bottom
                show kevinsad at center
                kv " ...You were not supposed to see me watching that. "
                kv " From my calculations, you probably think that I'm more of a nerd now... Watching a show about magical girls... "
                kv " You probably think I'm weird. "
                menu:
                    " You aren't weird ":
                        hide kevinsad at bottom
                        show kevinsurprised at center
                        " Kevin seems to be surprised by what you had just said. "
                        " I mean, liking magical girl stuff is okay as long as you aren't acting weird about the characters. "
                        kv " Really? you don't think that I'm weird? "
                        kv " Lots of people have said that I'm weird for liking Madoka Magica, actually. "
                        " YOU KNOW MADOKA MAGICA?? "
                        hide kevinsurprised at bottom
                        show kevinamazed at center
                        kv " You know madoka magica too?! "
                        scene black with dissolve
                        " You spent the entire day talking about madoka magica with Kevin. "
                        " The both of you were kinda just gushing about how good the anime is, "
                        " And how peak madohomu (madoka x homura) yuri is. "
                        " Madoka magica is peak and you should go watch it, actually. "
                        " No its not the meowbahh anime shut up "
                        play sound "audio/bellring.mp3"
                        " The bell rings, stopping the both of you from yapping about madoka magica for now. "
                        " You and Kevin get up from your seats, and go to the last class of the day. "
                        pause 2.0
                        jump artclass1
                    " You are weird " :
                        kv " Yeah, I knew you would say that... "
                        hide kevinsad at right with easeoutright
                        " Kevin gets up from his seat and he leaves. Poor guy, you made him sad. "
                        " Atleast you got some peace now and you can do your own thing. "
                        " ...Like looking at your phone. Or taking a nap. "
                        " Yeah, let's go ahead and take a quick nap. "
                        scene black with dissolve
                        " You take a short nap in the gym. "
                        pause 2.0
                        play sound "audio/bellring.mp3"
                        " The bell rings eventually, waking you up from your slumber. Rise and shine, sleeping beauty. "
                        " You get up so that you could go to your next class. "
                        pause 2.0
                        jump artclass1
            else:
                " The guy seemed to be watching a little show of his... "
                " From what you could see, he was watching something about magical girls. "
                hide kevinneutral at bottom
                show kevinsurprised at center
                " Though, he quickly notices that you were there and he immediately hides his phone away from you due to embarrassment. "
                hide kevinsurprised at bottom
                show kevinsad at center
                x " ...You were not supposed to see me watching that. "
                x " From my calculations, you probably think that I'm more of a nerd now... Watching a show about magical girls... "
                x " You probably think I'm weird. "
                menu:
                    " You aren't weird ":
                        hide kevinsad at bottom
                        show kevinsurprised at center
                        " The boy seems to be surprised by what you had just said. "
                        " I mean, liking magical girl stuff is okay as long as you aren't acting weird about the characters. "
                        x " Really? you don't think that I'm weird? "
                        x " Lots of people have said that I'm weird for liking Madoka Magica, actually. "
                        " YOU KNOW MADOKA MAGICA?? "
                        hide kevinsurprised at bottom
                        show kevinamazed at center
                        x " You know madoka magica too?! "
                        scene black with dissolve
                        " You spent the entire day talking about madoka magica with the guy. "
                        " The both of you were kinda just gushing about how good the anime is, "
                        " And how peak madohomu (madoka x homura) yuri is. "
                        $ kevinknow = True
                        " Also you learnt that the guys name is Kevin. "
                        " I mean, pretty stereotypical name for a nerd but sure. "
                        " Madoka magica is peak and you should go watch it, actually. "
                        " No its not the meowbahh anime shut up "
                        play sound "audio/bellring.mp3"
                        " The bell rings, stopping the both of you from yapping about madoka magica for now. "
                        " You and Kevin get up from your seats, and go to the last class of the day. "
                        pause 2.0
                        jump artclass1
                    " You are weird " :
                        x " Yeah, I knew you would say that... "
                        hide kevinsad at right with easeoutright
                        " The other guy gets up from his seat and he leaves. Poor guy, you made him sad. "
                        " Atleast you got some peace now and you can do your own thing. "
                        " ...Like looking at your phone. Or taking a nap. "
                        " Yeah, let's go ahead and take a quick nap. "
                        scene black with dissolve
                        " You take a short nap in the gym. "
                        pause 2.0
                        play sound "audio/bellring.mp3"
                        " The bell rings eventually, waking you up from your slumber. Rise and shine, sleeping beauty. "
                        " You get up so that you could go to your next class. "
                        pause 2.0
                        jump artclass1
        label gymchillaxer:
            " You decided not to hang out with anyone at all, and you just chillaxed there on a random seat. "
            " Then again, you do feel a little sleepy. Maybe you should take a quick nap... "
            " A little nap won't hurt. Plus, you need some of that energy to go through the last class. "
            " You curl yourself into a comfortable ball, and you fall asleep. "
            scene black with dissolve
            " Wonder what you're dreaming about... "
            pause 2.0
            play sound "audio/bellring.mp3"
            " You were awakened from your deep slumber by the bell ringing loudly in your ears. "
            " You tiredly stand up, still trying to get yourself to process what's going on. "
            " Once you're all awake and you've got everything processed, you walk down so that you could go to the final class of the day. "
            pause 2.0
            jump artclass1
    label cafe5:
        scene cafeteria with dissolve
        " You walk into the cafeteria and find two people that you recognize from your class. "
        " Should you talk with them, or should you just sit alone? "
        if bubbleknow == True and lanaknow == True:
            menu:
                " {image=bubbleicon} Bubble {image=bubbleicon} ":
                    jump bubblecafe
                " {image=lanaicon} Lana {image=lanaicon} ":
                    jump lanacafeuh
                " Nah, I'd be alone. ":
                    jump cafechillaxer
        elif bubbleknow == True and lanaknow == False:
            menu:
                " {image=bubbleicon} Bubble {image=bubbleicon} ":
                    jump bubblecafe
                " {image=lanaicon} A girl with sock puppets for hands {image=lanaicon} ":
                    jump lanacafeuh
                " Nah, I'd be alone. ":
                    jump cafechillaxer
        elif bubbleknow == False and lanaknow == True:
            menu:
                " {image=bubbleicon} A very 'bubbly' looking girl {image=bubbleicon} ":
                    jump bubblecafe
                " {image=lanaicon} Lana {image=lanaicon} ":
                    jump lanacafeuh
                " Nah, I'd be alone. ":
                    jump cafechillaxer
        else:
            menu:
                " {image=bubbleicon} A very 'bubbly' looking girl {image=bubbleicon} ":
                    jump bubblecafe
                " {image=lanaicon} A girl with sock puppets for hands {image=lanaicon} ":
                    jump lanacafeuh
                " Nah, I'd be alone. ":
                    jump cafechillaxer
        label bubblecafe:
            " Let's go and talk with her, then. "
            show bubbleneutral at center with easeinright
            if bubbleknow == True:
                " You sat next to Bubble, wondering what she's gonna be doing for the last break of the day. "
                " You look closer and you see that she was making a little paper star... wow. "
                " You've heard that they were pretty difficult to make, so you were wondering how Bubble was doing that. "
                " Bubble was quick to notice that you were looking at her, though. "
                b " Hey there, [name]! "
                b " Just making a few paper stars here and there... They're so fun to make! "
                b " I could teach you how to make them, if you want me to! "
                b " They're not really that hard... Well, it may seem like that at the start but once you make these a lot of times they get easier and easier! "
                b " Would you like to make some with me? "
                " Make paper stars with Bubble? "
                menu:
                    " Make paper stars with her ":
                        hide bubbleneutral at bottom
                        show bubblehappy at center
                        " Bubble seems to be happy with this decision. "
                        b " Yipee! Alright, I'll teach you have to make them! "
                        b " Don't rush, and just follow along to what I say! "
                        scene black with dissolve
                        " You spent the entire time learning how to make paper stars with Bubble. "
                        " It was a little hard for you to understand at first, but you eventually got it! "
                        " You've made 5 paper stars in total, each being a different color and size. "
                        " Bubble said that you were pretty good, for a beginner! "
                        " Maybe you should start making more paper stars... "
                        play sound "audio/bellring.mp3"
                        " The bell rings and interrupts Bubble from making another paper star. "
                        " She said she'll just make more in the middle of class. "
                        " You both get up to go to the last class of the day. "
                        pause 2.0
                        jump artclass1
                    " Nah ":
                        b " Alright, if you say so... "
                        b " If you need anything, just tell me, okay? "
                        " Bubble then gets to work on her paper stars. "
                        scene black with dissolve
                        " You sort of just hung out with Bubble for a bit, and watched her make paper stars. "
                        " You know, now that you think about it... it looks pretty easy when she does it. "
                        " But in reality, it might not be as easy as you thought it would be. "
                        " She probably needed some time to learn how to make those paper stars... "
                        " The best you could make out of paper is just paper butterflies. "
                        " Hold on... isn't this world about paper? "
                        " What if you try making one ofthe guys into a paper butterfly... "
                        " ...Nah, you'd get in trouble for that. "
                        play sound "audio/bellring.mp3"
                        " The bell rings and interrupts Bubble from making another paper star. "
                        " She said she'll just make more in the middle of class. "
                        " You both get up to go to the last class of the day. "
                        pause 2.0
                        jump artclass1
            else:
                " You sat next to the bubble girl, wondering what she's gonna be doing for the last break of the day. "
                " You look closer and you see that she was making a little paper star... wow. "
                " You've heard that they were pretty difficult to make, so you were wondering how she was doing that. "
                " The girl was quick to notice that you were looking at her, though. "
                x " Hey there, [name]! "
                x " Actually, I don't think I've ever gotten to introduce myself before...  Have I? "
                x " Hmmm... well I don't remember anything about telling you who I am... "
                $ bubbleknow = True
                hide bubbleneutral at bottom
                show bubblehappy at center
                b " I'm Bubble! We go to the same class! I hope we become good friends! "
                b " And was for what I'm doing... "
                hide bubblehappy at bottom
                show bubbleneutral at center
                b " Just making a few paper stars here and there... They're so fun to make! "
                b " I could teach you how to make them, if you want me to! "
                b " They're not really that hard... Well, it may seem like that at the start but once you make these a lot of times they get easier and easier! "
                b " Would you like to make some with me? "
                " Make paper stars with Bubble? "
                menu:
                    " Make paper stars with her ":
                        hide bubbleneutral at bottom
                        show bubblehappy at center
                        " Bubble seems to be happy with this decision. "
                        b " Yipee! Alright, I'll teach you have to make them! "
                        b " Don't rush, and just follow along to what I say! "
                        scene black with dissolve
                        " You spent the entire time learning how to make paper stars with Bubble. "
                        " It was a little hard for you to understand at first, but you eventually got it! "
                        " You've made 5 paper stars in total, each being a different color and size. "
                        " Bubble said that you were pretty good, for a beginner! "
                        " Maybe you should start making more paper stars... "
                        play sound "audio/bellring.mp3"
                        " The bell rings and interrupts Bubble from making another paper star. "
                        " She said she'll just make more in the middle of class. "
                        " You both get up to go to the last class of the day. "
                        pause 2.0
                        jump artclass1
                    " Nah ":
                        b " Alright, if you say so... "
                        b " If you need anything, just tell me, okay? "
                        " Bubble then gets to work on her paper stars. "
                        scene black with dissolve
                        " You sort of just hung out with Bubble for a bit, and watched her make paper stars. "
                        " You know, now that you think about it... it looks pretty easy when she does it. "
                        " But in reality, it might not be as easy as you thought it would be. "
                        " She probably needed some time to learn how to make those paper stars... "
                        " The best you could make out of paper is just paper butterflies. "
                        " Hold on... isn't this world about paper? "
                        " What if you try making one ofthe guys into a paper butterfly... "
                        " ...Nah, you'd get in trouble for that. "
                        play sound "audio/bellring.mp3"
                        " The bell rings and interrupts Bubble from making another paper star. "
                        " She said she'll just make more in the middle of class. "
                        " You both get up to go to the last class of the day. "
                        pause 2.0
                        jump artclass1
        label lanacafeuh:
            " Alright. Let's talk to her... "
            show lananeutral at center with easeinleft
            if lanaknow == True:
                " You wonder what Lana is doing, so you take a peek at her paper for a bit. "
                " Looks like she's making another character of hers, but she seems to be struggling a bit. "
                l " Hm... What lore should I give you...? "
                l " Oh, Hi [name]! "
                l " I'm trying to make some lore for my new oc... "
                l " Her name is Katie! I'm trying to think of some cool ideas right now, but honestly, I don't have anything... "
                l " Maybe you could help me? Do you have any ideas that I could try? "
                menu:
                    " Give Katie emo lore ":
                        " You tell Lana how you want Katie's backstory to be. "
                        " You tell her to make her parents die in a car crash and make her depressed... "
                        " ...Then give her someone to care about. "
                        " Only for that someone to die aswell, giving her more trauma. "
                        " And that person died right infront of her. More trauma! "
                        " A little more trauma won't hurt, right? "
                        " You also decided to add that Lana should give her a pet. "
                        " A cute fluffy cat! "
                        " Only for that cat to be burned by one of Katie's enemies. "
                        " And voila, there's her lore! "
                        l " Oh, wow... You're pretty good at making lore, [name]! "
                        l " I didn't expect you to be good at this kind of stuff! "
                        hide lananeutral at bottom
                        show lanahappy at center
                        l " Thanks! I'll be sure to add all of that to her lore! "
                        hide lanahappy at bottom
                        show lananeutral at center
                        l " She's going to be such a cool oc, heheh... "
                        l " Actually! I wanna talk to you about my ocs, is that alright? "
                        " You nod your head, wanting to know about Lana's ocs. "
                        " You're getting yourself prepared to hear the ultimate yapping session of the century. "
                        l " Okay, so, Katie is like.... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Lana about her oc's. "
                        " Honestly, all of her ocs sound badass. You like the ideas she has. "
                        " You're starting to become a huge fan of them, actually... "
                        play sound "audio/bellring.mp3"
                        " The bell rings, stopping Lana from yapping anymore. "
                        " You honestly wanted to hear more of her ocs, so that's unfortunate. "
                        " You both get up to go to the last class of the day. "
                        pause 2.0
                        jump artclass1
                    " Don't give Katie trauma ":
                        " You tell Lana how you want Katie's backstory to be. "
                        " Just let Katie have some nice parents and nothing else. "
                        " And let Katie adopt a cat. How cute! "
                        l " That actually sounds pretty nice, [name]! "
                        l " Plus, it's good to have a break from giving characters a truckload of trauma! "
                        l " Not all characters need trauma to make them interesting, ehe... "
                        l " You're actually pretty good at writing this type of stuff!"
                        l " Thanks! I'll be sure to add all of that to her lore! "
                        l " She's going to be such a cool oc, heheh... "
                        l " Actually! I wanna talk to you about my ocs, is that alright? "
                        " You nod your head, wanting to know about Lana's ocs. "
                        " You're getting yourself prepared to hear the ultimate yapping session of the century. "
                        l " Okay, so, Katie is like.... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Lana about her oc's. "
                        " Honestly, all of her ocs sound badass. You like the ideas she has. "
                        " You're starting to become a huge fan of them, actually... "
                        play sound "audio/bellring.mp3"
                        " The bell rings, stopping Lana from yapping anymore. "
                        " You honestly wanted to hear more of her ocs, so that's unfortunate. "
                        " You both get up to go to the last class of the day. "
                        pause 2.0
                        jump artclass1
            else:
                " You wonder what Lana is doing, so you take a peek at her paper for a bit. "
                " Looks like she's making another character of hers, but she seems to be struggling a bit. "
                x " Hm... What lore should I give you...? "
                x " Oh, Hi [name]! "
                x " Wait, I haven't introduced myself to you before! How rude of me... "
                $ lanaknow = True
                l " I'm Lana! We go to the same class... Nice to meet you! Hope we can be good friends! "
                l " Actually, I may or may not need some help right now... "
                l " I'm trying to make some lore for my new oc... "
                l " Her name is Katie! I'm trying to think of some cool ideas right now, but honestly, I don't have anything... "
                l " Maybe you could help me? Do you have any ideas that I could try? "
                menu:
                    " Give Katie emo lore ":
                        " You tell Lana how you want Katie's backstory to be. "
                        " You tell her to make her parents die in a car crash and make her depressed... "
                        " ...Then give her someone to care about. "
                        " Only for that someone to die aswell, giving her more trauma. "
                        " And that person died right infront of her. More trauma! "
                        " A little more trauma won't hurt, right? "
                        " You also decided to add that Lana should give her a pet. "
                        " A cute fluffy cat! "
                        " Only for that cat to be burned by one of Katie's enemies. "
                        " And voila, there's her lore! "
                        l " Oh, wow... You're pretty good at making lore, [name]! "
                        l " I didn't expect you to be good at this kind of stuff! "
                        hide lananeutral at bottom
                        show lanahappy at center
                        l " Thanks! I'll be sure to add all of that to her lore! "
                        hide lanahappy at bottom
                        show lananeutral at center
                        l " She's going to be such a cool oc, heheh... "
                        l " Actually! I wanna talk to you about my ocs, is that alright? "
                        " You nod your head, wanting to know about Lana's ocs. "
                        " You're getting yourself prepared to hear the ultimate yapping session of the century. "
                        l " Okay, so, Katie is like.... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Lana about her oc's. "
                        " Honestly, all of her ocs sound badass. You like the ideas she has. "
                        " You're starting to become a huge fan of them, actually... "
                        play sound "audio/bellring.mp3"
                        " The bell rings, stopping Lana from yapping anymore. "
                        " You honestly wanted to hear more of her ocs, so that's unfortunate. "
                        " You both get up to go to the last class of the day. "
                        pause 2.0
                        jump artclass1
                    " Don't give Katie trauma ":
                        " You tell Lana how you want Katie's backstory to be. "
                        " Just let Katie have some nice parents and nothing else. "
                        " And let Katie adopt a cat. How cute! "
                        l " That actually sounds pretty nice, [name]! "
                        l " Plus, it's good to have a break from giving characters a truckload of trauma! "
                        l " Not all characters need trauma to make them interesting, ehe... "
                        l " You're actually pretty good at writing this type of stuff!"
                        l " Thanks! I'll be sure to add all of that to her lore! "
                        l " She's going to be such a cool oc, heheh... "
                        l " Actually! I wanna talk to you about my ocs, is that alright? "
                        " You nod your head, wanting to know about Lana's ocs. "
                        " You're getting yourself prepared to hear the ultimate yapping session of the century. "
                        l " Okay, so, Katie is like.... "
                        scene black with dissolve
                        " You spent the rest of the break talking with Lana about her oc's. "
                        " Honestly, all of her ocs sound badass. You like the ideas she has. "
                        " You're starting to become a huge fan of them, actually... "
                        play sound "audio/bellring.mp3"
                        " The bell rings, stopping Lana from yapping anymore. "
                        " You honestly wanted to hear more of her ocs, so that's unfortunate. "
                        " You both get up to go to the last class of the day. "
                        pause 2.0
                        jump artclass1
        label cafechillaxer:
            " Instead of choosing someone to talk with, you just decided to chill. "
            " You sat down in an empty table and pulled out some earphones from your pocket that you didn't even know that you had. "
            " Either way, you put them on and you decided to listen to your playlist... "
            if kind == True:
                " ...playlist of metal music. "
                " What? You didn't expect that? Well, kind people can still listen to music too, you know. "
                " It's not exactly everyone's thing but you think metal music is a banger. "
                " People are gonna be surprised when you say you like this stuff... "
                " ...Especially since they think that you're so kind and innocent with that look of yours. "
            elif mean == True:
                " ...Playlist of princess themed music. "
                " What? You didn't expect that? Well, this is some of the most manliest songs you could ever hear. "
                " They make you feel strong... and make you feel like a pretty princess. "
                " If you disagree with this kind of music I will bite your ankles. "
            elif calm == True:
                " ...Playlist of chill frutiger aero music. "
                " Frutiger aero themed things are pretty underrated, in your opinion. "
                " Especially the music thats inspired off of it. "
                " They're really calming in some situations, if you're going through stress or you just need background noise. "
                " Frutiger aero themed songs need more appreciation. Including other underrated music genres. "
            pause 1.0
            play sound "audio/bellring.mp3"
            " The bell rings after a few minutes of chillaxing, and you take out your earphones and put them back in your pocket. "
            " You then get up to go to the last class of the day. "
            scene black with dissolve
            pause 2.0
            jump artclass1
    label rooftop5:
        scene rooftop with dissolve
        # cubbie, engel, ruby
        " You walk up into the rooftop, and you see some classmates of yours hanging out. "
        " Who do you hang out with? "
        if cubbieknow, engelknow, rubyknow == True:
            menu:
                " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                    jump cubbierooftop
                " {image=engelicon} Engel {image=engelicon} ":
                    jump engelrooftop
                " {image=rubyicon} Ruby {image=rubyicon} ":
                    jump rubyrooftop
        elif cubbieknow == True and engelknow, rubyknow == False:
            menu:
                " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                    jump cubbierooftop
                " {image=engelicon} A guy with two feathers on his head {image=engelicon} ":
                    jump engelrooftop
                " {image=rubyicon} A girl with a tv for a head {image=rubyicon} ":
                    jump rubyrooftop
        elif engelknow == True and cubbieknow, rubyknow == False:
            menu:
                " {image=cubbieicon} A cute cat!! {image=cubbieicon} ":
                    jump cubbierooftop
                " {image=engelicon} Engel {image=engelicon} ":
                    jump engelrooftop
                " {image=rubyicon} A girl with a tv for a head {image=rubyicon} ":
                    jump rubyrooftop
        elif rubyknow == True and cubbieknow, engelknow == False:
            menu:
                " {image=cubbieicon} A cute cat!! {image=cubbieicon} ":
                    jump cubbierooftop
                " {image=engelicon} A guy with two feathers on his head {image=engelicon} ":
                    jump engelrooftop
                " {image=rubyicon} Ruby {image=rubyicon} ":
                    jump rubyrooftop
        elif cubbieknow, engelknow == True and rubyknow == False:
            menu:
                " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                    jump cubbierooftop
                " {image=engelicon} Engel {image=engelicon} ":
                    jump engelrooftop
                " {image=rubyicon} A girl with a tv for a head {image=rubyicon} ":
                    jump rubyrooftop
        elif cubbieknow, rubyknow == True and engelknow == False:
            menu:
                " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                    jump cubbierooftop
                " {image=engelicon} A guy with two feathers on his head {image=engelicon} ":
                    jump engelrooftop
                " {image=rubyicon} Ruby {image=rubyicon} ":
                    jump rubyrooftop
        elif engelknow, rubyknow == True and cubbieknow == False:
            menu:
                " {image=cubbieicon} A cute cat!! {image=cubbieicon} ":
                    jump cubbierooftop
                " {image=engelicon} Engel {image=engelicon} ":
                    jump engelrooftop
                " {image=rubyicon} Ruby {image=rubyicon} ":
                    jump rubyrooftop
        else:
            menu:
                " {image=cubbieicon} A cute cat!! {image=cubbieicon} ":
                    jump cubbierooftop
                " {image=engelicon} A guy with two feathers on his head {image=engelicon} ":
                    jump engelrooftop
                " {image=rubyicon} A girl with a tv for a head {image=rubyicon} ":
                    jump rubyrooftop
        label cubbierooftop:
            " You go and talk to the cute little kitty, wondering what he's doing. "
            show cubbieneutral at center with easeinleft
            if cubbieknow == True:
                " Cubbie was sitting on the ground, looking up at the clouds. "
                " Cubbie seems to notice you, and pats the spot next to him. "
                cb " .... "
                " Seems like he wants you to sit next to him. "
                " Sit with Cubbie? "
                menu:
                    " Sit next to him. ":
                        " You sat down next to Cubbie. "
                        " You look up at the sky, like what Cubbie is doing. "
                        " Slowly, you could see a cat shaped cloud forming. "
                        " You point that out to Cubbie... "
                        hide cubbieneutral at bottom
                        show cubbiehappy at center
                        cb " ...!! "
                        " Cubbie seems happy that the cloud looks like him. "
                        " He looks so cute whenever he's happy, you just wanna squish him. "
                        " All cats are adorable, including Cubbie. "
                        " If you think otherwise I will give you rabies. "
                        hide cubbiehappy at bottom
                        show cubbieamazed at center
                        " Cubbie points you a you-shaped cloud in the sky. "
                        " He seems to be amazed by it. Well, you're amazed too. "
                        " Now theres a you shaped cloud and a Cubbie shaped cloud in the sky. "
                        " And they're next to eachother...adorable. "
                        " You took a photo of it with your phone. "
                        scene black with dissolve
                        " You spent the rest of the break watching the clouds with Cubbie. "
                        " It was pretty relaxing, a nice little break. "
                        " You enjoyed your time with Cubbie, and he enjoyed his time with you. "
                        pause 1.0
                        play sound "audio/bellring.mp3"
                        " The bell rings, and you both get up to go to the last class of the day. "
                        pause 2.0
                        jump artclass1
                    " I prefer standing. ":
                        " You made a gesture to Cubbie that you just prefer standing. "
                        " Cubbie seems to understand your decision. "
                        " You look up at the sky, like what Cubbie is doing. "
                        " Slowly, you could see a cat shaped cloud forming. "
                        " You point that out to Cubbie... "
                        hide cubbieneutral at bottom
                        show cubbiehappy at center
                        cb " ...!! "
                        " Cubbie seems happy that the cloud looks like him. "
                        " He looks so cute whenever he's happy, you just wanna squish him. "
                        " All cats are adorable, including Cubbie. "
                        " If you think otherwise I will give you rabies. "
                        hide cubbiehappy at bottom
                        show cubbieamazed at center
                        " Cubbie points you a you-shaped cloud in the sky. "
                        " He seems to be amazed by it. Well, you're amazed too. "
                        " Now theres a you shaped cloud and a Cubbie shaped cloud in the sky. "
                        " And they're next to eachother...adorable. "
                        " You took a photo of it with your phone. "
                        scene black with dissolve
                        " You spent the rest of the break watching the clouds with Cubbie. "
                        " It was pretty relaxing, a nice little break. "
                        " You enjoyed your time with Cubbie, and he enjoyed his time with you. "
                        pause 1.0
                        play sound "audio/bellring.mp3"
                        " The bell rings, and you help Cubbie get up from the ground. "
                        " You both then get down to go to the last class of the day. "
                        pause 2.0
                        jump artclass1
            else:
                " The little cat was sitting on the ground, looking up at the clouds. "
                $ cubbieknow = True
                " From what you've heard, this little guys name was Cubbie. "
                " He doesn't really like to talk. I mean, he prefers not to. He can, but he doesn't want to. "
                " He seems to notice you after a few minutes and pats the spot next to him. "
                cb " ... "
                " Seems like he wants you to sit next to him. "
                " Sit with Cubbie? "
                menu:
                    " Sit next to him. ":
                        " You sat down next to Cubbie. "
                        " You look up at the sky, like what Cubbie is doing. "
                        " Slowly, you could see a cat shaped cloud forming. "
                        " You point that out to Cubbie... "
                        hide cubbieneutral at bottom
                        show cubbiehappy at center
                        cb " ...!! "
                        " Cubbie seems happy that the cloud looks like him. "
                        " He looks so cute whenever he's happy, you just wanna squish him. "
                        " All cats are adorable, including Cubbie. "
                        " If you think otherwise I will give you rabies. "
                        hide cubbiehappy at bottom
                        show cubbieamazed at center
                        " Cubbie points you a you-shaped cloud in the sky. "
                        " He seems to be amazed by it. Well, you're amazed too. "
                        " Now theres a you shaped cloud and a Cubbie shaped cloud in the sky. "
                        " And they're next to eachother...adorable. "
                        " You took a photo of it with your phone. "
                        scene black with dissolve
                        " You spent the rest of the break watching the clouds with Cubbie. "
                        " It was pretty relaxing, a nice little break. "
                        " You enjoyed your time with Cubbie, and he enjoyed his time with you. "
                        pause 1.0
                        play sound "audio/bellring.mp3"
                        " The bell rings, and you both get up to go to the last class of the day. "
                        pause 2.0
                        jump artclass1
                    " I prefer standing. ":
                        " You made a gesture to Cubbie that you just prefer standing. "
                        " Cubbie seems to understand your decision. "
                        " You look up at the sky, like what Cubbie is doing. "
                        " Slowly, you could see a cat shaped cloud forming. "
                        " You point that out to Cubbie... "
                        hide cubbieneutral at bottom
                        show cubbiehappy at center
                        cb " ...!! "
                        " Cubbie seems happy that the cloud looks like him. "
                        " He looks so cute whenever he's happy, you just wanna squish him. "
                        " All cats are adorable, including Cubbie. "
                        " If you think otherwise I will give you rabies. "
                        hide cubbiehappy at bottom
                        show cubbieamazed at center
                        " Cubbie points you a you-shaped cloud in the sky. "
                        " He seems to be amazed by it. Well, you're amazed too. "
                        " Now theres a you shaped cloud and a Cubbie shaped cloud in the sky. "
                        " And they're next to eachother...adorable. "
                        " You took a photo of it with your phone. "
                        scene black with dissolve
                        " You spent the rest of the break watching the clouds with Cubbie. "
                        " It was pretty relaxing, a nice little break. "
                        " You enjoyed your time with Cubbie, and he enjoyed his time with you. "
                        pause 1.0
                        play sound "audio/bellring.mp3"
                        " The bell rings, and you help Cubbie get up from the ground. "
                        " You both then get down to go to the last class of the day. "
                        pause 2.0
                        jump artclass1
        label engelrooftop:
            " Let's go and talk with the guy, then... "
            show engelneutral at center with easeinright
            if engelknow == True:
                " Engel seems to be chilling on a bench, drawing something... "
                " Sit next to him? "
                menu:
                    " Sit next to Engel ":
                        " You sat next to him, looking at what he was drawing... "
                        if claireknow == True:
                            " You saw that he was drawing a picture of Claire. "
                            " It looked really detailed and nice, you didn't know that he was such a good artist... "
                            " He then noticed you after a bit. "
                        else:
                            " You saw that he was drawing a picture of a girl you don't recognize. "
                            " It looked really detailed and nice, you didn't know that he was such a good artist... "
                            " He then noticed you after a bit. "
                        e " Hello, [name]... "
                        e " I'm just practicing for art class that we're having later. "
                        e " Do you think it looks alright...? "
                        " You nod, silently saying that it looks good. "
                        e " I'm glad... "
                        e " You know... Miss Sasha's pretty nice. "
                        e " Our art teacher, I mean. "
                        e " One time I came to her class late on accident and yet she still forgave me and gave me time to make a painting of my own... "
                        e " And by that time, class was already over. When I got there. "
                        hide engelneutral at bottom
                        show engelhappy at center
                        e " I got made fun of by Oliver and his little crew when I finished, but she protected me from them. "
                        e " She's sort of like... a mother figure, you know? "
                        e " Well, she {i}does{/i} teach the kindergarten students here, too, so I guess that's why she's like that. "
                        e " ...{w=0.5} Would you like to draw with me, [name]? Just for now. "
                        " You nod once more, silently saying that you want to draw with him. "
                        e " Fantastic. Here's a piece of paper for you to draw on... "
                        scene black with dissolve
                        " You spent the entire break drawing with Engel. "
                        " You drew Engel, and he drew you. "
                        " In comparison, yours looked a tad bit worse than his. "
                        " Engel said that yours looked good though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, soon enough, and you n Engel get up to go to the final class of the day. "
                        pause 2.0
                        jump artclass1
                    " Nah, I don't want to bother him. ":
                        " You decided not to bother Engel. "
                        " Besides, he looks pretty concentrated. "
                        hide engelneutral at left with easeoutleft
                        " You just decided to hang around on another part of the rooftop. "
                        " You took that time to listen to some music you had on your phone. "
                        " How relaxing...Feeling the wind and looking at nature whilst listening to your nice pretty princess music... "
                        " Though you knew this moment wouldn't last forever so that you can relax, but you just decided to enjoy the moment. "
                        scene black with dissolve
                        " You stayed like this for a few minutes. "
                        pause 1.0
                        play sound "audio/bellring.mp3"
                        " The bell rings after a few moments, and you take out your earphones and put them back in your pocket. "
                        " You then went to go to your last class of the day. "
                        pause 2.0
                        jump artclass1
            else:
                " The boy seems to be chilling on a bench, drawing something... "
                " Sit next to him? "
                menu:
                    " Sit next to him ":
                        " You sat next to him, looking at what he was drawing... "
                        if claireknow == True:
                            " You saw that he was drawing a picture of Claire. "
                            " It looked really detailed and nice, you didn't know that he was such a good artist... "
                            " He then noticed you after a bit. "
                        else:
                            " You saw that he was drawing a picture of a girl you don't recognize. "
                            " It looked really detailed and nice, you didn't know that he was such a good artist... "
                            " He then noticed you after a bit. "
                        x " Hello there... "
                        x " I believe we haven't met before, so I'd like to introduce myself. "
                        $ engelknow = True
                        e " I'm Engel. I think we go to the same class... "
                        e " It's nice to meet you, [name]. "
                        " You ask him what he's doing. "
                        e " I'm just practicing for art class that we're having later. "
                        e " Do you think it looks alright...? "
                        " You nod, silently saying that it looks good. "
                        e " I'm glad... "
                        e " You know... Miss Sasha's pretty nice. "
                        e " Our art teacher, I mean. "
                        e " One time I came to her class late on accident and yet she still forgave me and gave me time to make a painting of my own... "
                        e " And by that time, class was already over. When I got there. "
                        hide engelneutral at bottom
                        show engelhappy at center
                        e " I got made fun of by Oliver and his little crew when I finished, but she protected me from them. "
                        e " She's sort of like... a mother figure, you know? "
                        e " Well, she {i}does{/i} teach the kindergarten students here, too, so I guess that's why she's like that. "
                        e " ...{w=0.5} Would you like to draw with me, [name]? Just for now. "
                        " You nod once more, silently saying that you want to draw with him. "
                        e " Fantastic. Here's a piece of paper for you to draw on... "
                        scene black with dissolve
                        " You spent the entire break drawing with Engel. "
                        " You drew Engel, and he drew you. "
                        " In comparison, yours looked a tad bit worse than his. "
                        " Engel said that yours looked good though. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, soon enough, and you n Engel get up to go to the final class of the day. "
                        pause 2.0
                        jump artclass1
                    " Nah, I don't want to bother him. ":
                        " You decided not to bother the boy. "
                        " Besides, he looks pretty concentrated. "
                        hide engelneutral at left with easeoutleft
                        " You just decided to hang around on another part of the rooftop. "
                        " You took that time to listen to some music you had on your phone. "
                        " How relaxing...Feeling the wind and looking at nature whilst listening to your nice pretty princess music... "
                        " Though you knew this moment wouldn't last forever so that you can relax, but you just decided to enjoy the moment. "
                        scene black with dissolve
                        " You stayed like this for a few minutes. "
                        pause 1.0
                        play sound "audio/bellring.mp3"
                        " The bell rings after a few moments, and you take out your earphones and put them back in your pocket. "
                        " You then went to go to your last class of the day. "
                        pause 2.0
                        jump artclass1
        label rubyrooftop:
            " Let's go talk to her then. "
            show rubyneutral at center with easeinright
            if rubyknow == True:
                " You saw Ruby looking over at clouds, curiously. "
                " You stand next to her and tap her shoulder to get her attention on you. "
                ru " Hi, [name]! "
                ru " Aren't clouds so interesting...? "
                ru " They can form all sorts of shapes, and they look so soft and nice to lay down on... "
                ru " ...Even if you can't really do that if you actually tried, haha. "
                ru " ...You ever see those cloud pictures? Where they look a little...funny? "
                ru " Like some clouds forming a long window of sorts... I don't know how to describe it. "
                ru " It looks impossible, but at the same time my mind tells me it is! "
                ru " Ah, how interesting life can be... "
                ru " Theres so much we don't know, so much we can discover if we explore and expiriment a lot! "
                ru " We have so much to learn... "
                ru " ...Would you like to gaze at the sky with me? "
                ru " It sounds boring, I know, but it's what I do whenever it's break time. "
                ru " Well, whenever I don't have anyone to talk to, of course. "
                ru " You don't have to stay with me, if you don't want to. "
                ru " I'll be just fine over here. "
                " Stay with Ruby? "
                menu:
                    " Stay and watch the clouds with her ":
                        " You decided to watch the clouds with Ruby. "
                        scene black with dissolve
                        " You stayed with Ruby for the rest of the break. "
                        " At one point, you swore that you saw a you-shaped cloud in the sky... "
                        " ...It quickly faded away though, before you could point it out to Ruby. "
                        " It's honestly nice and calming, looking at clouds with a friend... "
                        " Reminds you of the good old days... "
                        play sound "audio/bellring.mp3"
                        " The bell rings, interrupting you and Ruby from watching the clouds. "
                        " You both get up to go to the final class of the day. "
                        pause 2.0
                        jump artclass1
                    " Nah, I have places to be ":
                        " You tell Ruby that you wanna go somewhere else. "
                        ru " Alright! I'll be here if you need anything, okay? "
                        ru " I'll see you later! "
                        scene black with dissolve
                        " You went down from the rooftop, and started roaming around the school. "
                        " Everything was the same in the hallways, people laughing, people on their phones... "
                        " People gossiping, people just walking around, all the same. "
                        " Hopefully you don't get picked on while on your walk. "
                        " And you didn't actually. Today was oddly peaceful, no one was getting bullied at all.. "
                        " The reason might've been from earlier where Oliver got suspended. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, interrupting your little walk. "
                        " Luckily, you were right near your classroom. So, you walked in, going into your final class of the day. "
                        pause 2.0
                        jump artclass1
            else:
                " You saw the girl looking over at clouds, curiously. "
                " You stand next to her and tap her shoulder to get her attention on you. "
                x " Oh, hello there... "
                x " I don't think we've met before! Or have we...? "
                x " I can't exactly remember... aren't we in the same class? "
                x " Either way, I think I should introduce myself to you! It'd be kind of rude if I didn't... "
                $ rubyknow = True
                ru " I'm Ruby! I hope we get to be great friends! "
                ru " What's your name? "
                " You tell her your name. "
                ru " [name]... You've got a pretty nice name there! "
                ru " Anywho! I've got a question for you, [name]! "
                ru " Aren't clouds so interesting...? "
                ru " They can form all sorts of shapes, and they look so soft and nice to lay down on... "
                ru " ...Even if you can't really do that if you actually tried, haha. "
                ru " ...You ever see those cloud pictures? Where they look a little...funny? "
                ru " Like some clouds forming a long window of sorts... I don't know how to describe it. "
                ru " It looks impossible, but at the same time my mind tells me it is! "
                ru " Ah, how interesting life can be... "
                ru " Theres so much we don't know, so much we can discover if we explore and expiriment a lot! "
                ru " We have so much to learn... "
                ru " ...Would you like to gaze at the sky with me? "
                ru " It sounds boring, I know, but it's what I do whenever it's break time. "
                ru " Well, whenever I don't have anyone to talk to, of course. "
                ru " You don't have to stay with me, if you don't want to. "
                ru " I'll be just fine over here. "
                " Stay with Ruby? "
                menu:
                    " Stay and watch the clouds with her ":
                        " You decided to watch the clouds with Ruby. "
                        scene black with dissolve
                        " You stayed with Ruby for the rest of the break. "
                        " At one point, you swore that you saw a you-shaped cloud in the sky... "
                        " ...It quickly faded away though, before you could point it out to Ruby. "
                        " It's honestly nice and calming, looking at clouds with a friend... "
                        " Reminds you of the good old days... "
                        play sound "audio/bellring.mp3"
                        " The bell rings, interrupting you and Ruby from watching the clouds. "
                        " You both get up to go to the final class of the day. "
                        pause 2.0
                        jump artclass1
                    " Nah, I have places to be ":
                        " You tell Ruby that you wanna go somewhere else. "
                        ru " Alright! I'll be here if you need anything, okay? "
                        ru " I'll see you later! "
                        scene black with dissolve
                        " You went down from the rooftop, and started roaming around the school. "
                        " Everything was the same in the hallways, people laughing, people on their phones... "
                        " People gossiping, people just walking around, all the same. "
                        " Hopefully you don't get picked on while on your walk. "
                        " And you didn't actually. Today was oddly peaceful, no one was getting bullied at all.. "
                        " The reason might've been from earlier where Oliver got suspended. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, interrupting your little walk. "
                        " Luckily, you were right near your classroom. So, you walked in, going into your final class of the day. "
                        pause 2.0
                        jump artclass1
    label library5:
        scene library with dissolve
        # petunia and lizzy
        " You walk into the library, and you spot the popular girls, probably gossiping about something. "
        " Curious, you decided to go up to them and see what they're talking about. "
        show petunianeutral at right with easeinleft
        show lizzyneutral at left with easeinleft
        if popularknow == True:
            p " Hiya there, [name]! "
            lz " Hey. "
            p " We're just looking some books here and there... shocker, right? "
            lz " We actually wanted to look at books. Heard that it would make us cool. "
            p " Mhm! Come, join us! "
            " You joined in on looking at interesting books with Petunia and Lizzy. "
            " That's when Petunia actually found something interesting. "
            p " Hey, hey! "
            lz " Hm... yes, Petunia? What is it? "
            lz " You've gotta be quiet, by the way. We're in a library. "
            p " I know, I know... just that I found an interesting book! "
            p " Looks like someone left their BL book in here! "
            lz " Oh my heavens. For real? "
            p " Yeah! Let's see what good stuff they have... "
            " Petunia opens it and looks at a few pages, quickly flipping through them... "
            hide petunianeutral at bottom
            show petuniasurprised at right
            " ...Though, she stops at one page and she seems quite...flabbergasted when she got to a specific page. "
            hide lizzyneutral at bottom
            show lizzyconfused at left
            " She kept staring at it in shock for a few minutes until Lizzy got a little concerned. "
            lz " ...Uh, Petunia? You've been staring at that page for a bit now. "
            show lizzyconfused at center with move
            lz " Let me see, I'm sure it can't be that bad-{nw} "
            hide lizzyconfused at bottom
            show lizzysad at center
            lz " Holy shit. "
            " You got curious as well, and you eventually decided to look. "
            " ...Let's just say that the scene Lizzy and Petunia wasn't really family friendly. "
            " You think you just got traumatized just by looking at that. "
            hide petuniasurprised at bottom
            show petuniasad at right
            p " ...Yeah, no. Let's just leave it here for the owner to find again... "
            show lizzysad at left with move
            lz " Yeah. Jeez, wonder what kind of freaky stuff people are actually reading in this school... "
            p " The thing is, who would even bring this stuff to school? "
            p " Also, I'm not even into this kind of stuff. I prefer yuri. "
            hide lizzysad at bottom
            show lizzyneutral at left
            lz " So, you're saying that it would've been better if it was yuri? "
            hide petuniasad at bottom
            show petunianeutral at right
            p " Well, it still would've looked gross, but yuri makes it better. "
            play sound "audio/bellring.mp3"
            " The bell rings, signalling that it was time for the last class of the day to start. "
            p " Oh, hey. Looks like class is about to start. "
            lz " We'll see you in the classroom, [name]. "
            p " Yeah! See ya! "
            scene black with dissolve
            " Petunia and Lizzy left the library to go to class. "
            " You followed them shortly after. "
            " The question still lingered in your mind, who could've bought that book to school? "
            " Well, we'll never know. "
            " You eventually reached your classroom and you went to sit on your seat. "
            pause 2.0
            jump artclass1
        else:
            x " Hiya there! "
            x " Hey. "
            x " You're that new kid, right? "
            x " It's cool to meet you. "
            x " Liizzz!! We should introduce ourselves to make us more popular! "
            x " Aren't we popular enough for [them] to know us? "
            x " Well, not everyone knows us! You gotta remember that! "
            x " Alright, fine... "
            $ popularknow = True
            lz " I'm Lizzy. This is my best friend, Petunia. "
            p " We're always together, no matter what! "
            lz " We're inseparable, basically. "
            p " Anywho... "
            p " We're just looking some books here and there... shocker, right? "
            lz " We actually wanted to look at books. Heard that it would make us cool. "
            p " Mhm! Come, join us! "
            " You joined in on looking at interesting books with Petunia and Lizzy. "
            " That's when Petunia actually found something interesting. "
            p " Hey, hey! "
            lz " Hm... yes, Petunia? What is it? "
            lz " You've gotta be quiet, by the way. We're in a library. "
            p " I know, I know... just that I found an interesting book! "
            p " Looks like someone left their BL book in here! "
            lz " Oh my heavens. For real? "
            p " Yeah! Let's see what good stuff they have... "
            " Petunia opens it and looks at a few pages, quickly flipping through them... "
            hide petunianeutral at bottom
            show petuniasurprised at right
            " ...Though, she stops at one page and she seems quite...flabbergasted when she got to a specific page. "
            hide lizzyneutral at bottom
            show lizzyconfused at left
            " She kept staring at it in shock for a few minutes until Lizzy got a little concerned. "
            lz " ...Uh, Petunia? You've been staring at that page for a bit now. "
            show lizzyconfused at center with move
            lz " Let me see, I'm sure it can't be that bad-{nw} "
            hide lizzyconfused at bottom
            show lizzysad at center
            lz " Holy shit. "
            " You got curious as well, and you eventually decided to look. "
            " ...Let's just say that the scene Lizzy and Petunia wasn't really family friendly. "
            " You think you just got traumatized just by looking at that. "
            hide petuniasurprised at bottom
            show petuniasad at right
            p " ...Yeah, no. Let's just leave it here for the owner to find again... "
            show lizzysad at left with move
            lz " Yeah. Jeez, wonder what kind of freaky stuff people are actually reading in this school... "
            p " The thing is, who would even bring this stuff to school? "
            p " Also, I'm not even into this kind of stuff. I prefer yuri. "
            hide lizzysad at bottom
            show lizzyneutral at left
            lz " So, you're saying that it would've been better if it was yuri? "
            hide petuniasad at bottom
            show petunianeutral at right
            p " Well, it still would've looked gross, but yuri makes it better. "
            play sound "audio/bellring.mp3"
            " The bell rings, signalling that it was time for the last class of the day to start. "
            p " Oh, hey. Looks like class is about to start. "
            lz " We'll see you in the classroom, [name]. "
            p " Yeah! See ya! "
            scene black with dissolve
            " Petunia and Lizzy left the library to go to class. "
            " You followed them shortly after. "
            " The question still lingered in your mind, who could've bought that book to school? "
            " Well, we'll never know. "
            " You eventually reached your classroom and you went to sit on your seat. "
            pause 2.0
            jump artclass1
    label artclass1:
        scene classroom with dissolve
        " You were just on your seat, waiting for the art teacher to come by. "
        " You hear the door opening, and saw the teacher walk in. "
        show sashaneutral at center with easeinright
        mss " Good day, class! "
        hide sashaneutral at bottom
        show sashahappy at center
        mss " Today, I'll have an activity for us! "
        mss " Now, I wanted to give an activity because we have a new classmate! "
        hide sashahappy at bottom
        show sashaneutral at center
        mss " What's your name, little [person]? "
        " You tell the teacher your name. Boy, she seems like a fun teacher... "
        mss " [name]! What a pretty and unique name you've got! "
        mss " How about we say hello to [name], and give [them] a warm welcome? "
        hide sashaneutral at bottom
        show sashahappy at center
        mss " On the count of three! "
        mss " One... "
        mss " Two... "
        mss " Three! "
        " You hear everyone from your class say hello to you. "
        " This has to be one of the most fun class you've ever had in your life. "
        " And also this had to be the one teacher that has actually acknowledged that you were a new student in the entirety of the game. "
        " The others just quickly went to starting the class, not even getting to know who you are. "
        " Really do feels like you're appreciated here. "
        hide sashahappy at bottom
        show sashaneutral at center
        mss " Good job, everyone! "
        mss " Now, for this activity this'll be for 50 points! "
        mss " I'll have you all paint on canvases to paint what ever you'd like! "
        mss " Don't worry, since I have a whole load of extra paints in my home, I've got you all painting materials! "
        mss " Now, drawing anything crude won't get you any points for the day. "
        mss " I don't tolerate that behavior in my class! "
        mss " I'll start giving out your canvases and painting materials, now! "
        hide sashaneutral at left with easeoutleft
        " Miss Sasha started giving out painting materials to everyone including you. "
        " What should you paint? "
        menu:
            " A portrait of Miss Sasha (for extra points) ":
                " You wanted to paint Miss Sasha, since she was being so nice. "
                " You started to paint her, looking at her every now and then to make sure you've got every detail correct. "
                if claengbub == True:
                    if clairelv == 10 or clairelv >= 10:
                        if clairebeatup == True:
                            scene black
                            jump endday1
                        else:
                            show claireamazed at center with easeinleft
                            " You also saw that Claire was looking at your canvas in awe. "
                            c " Wooahhh... You're pretty good at painting, [name]! "
                            c " So detailed and so pretty... Mine's not as good as yours! "
                            hide claireamazed at bottom
                            show clairehappy at center
                            c " I'm sure Miss Sasha will like your drawing! "
                            c " I think she's gonna be very, very happy about it, actually! "
                            c " I'll get back to work on mine, heh... "
                            c " It's just a simple tree, though! "
                            hide clairehappy at left with easeoutleft
                            " Feeling proud due to Claire's compliments, you decided to continue painting and made it look even better with all sorts of details. "
                    elif engellv == 10 or engellv >= 10:
                        show engelhappy at center with easeinright
                        " You also saw that Engel was looking at your canvas, seemingly proud of what you're working on. "
                        e " My, I didn't know that you were such a talented artist, [name]... "
                        e " You're pretty good at this, I'll give you that. "
                        e " Mine's just a little duck on a lilypad. It's nowhere as impressive as yours, though. "
                        e " However, I won't disturb you for longer. I'll get back to work so that you can focus. "
                        hide engelhappy at right with easeoutright
                        " Feeling happy due to Engel's compliments, you decided to continue painting and made it look even better with all sorts of details. "
                    elif bubblelv == 10 or bubblelv >= 10:
                        show bubbleamazed at center with easeinleft
                        " You also saw that Bubble was looking at your canvas, looking in awe of what you're painting. "
                        b " Woah... You're like, such a cool artist, [name]! "
                        b " I can only paint or draw in a anime-ish artstyle... I actually wanna learn how you do this stuff! "
                        hide bubbleamazed at bottom
                        show bubblehappy at center
                        b " Miss Sasha's gonna love this, surely! "
                        b " I'll get back to work so that I won't have to bother you, okay? "
                        b " And if you're gonna ask what I'm painting... It's my favorite anime character! "
                        b " Not telling you who it is though, and no peeking! Not until I'm done! "
                        hide bubblehappy at left with easeoutleft
                        " Feeling happy due to Bubble's compliments and curiousity because you wanna see who Bubble's favorite character is, you continued to paint, giving little details almost everywhere. "
                    else:
                        " You continued to paint and paint, being very focused and not letting anything distract you. "
                elif abblana == True:
                    if abbielv == 10 or abbielv >= 10:
                        show abbiehappy at center with easeinright
                        " You also saw Abbie looking at your canvas, being amazed at what you're painting. "
                        a " Wow... is that a painting of Miss Sasha...? "
                        a " It looks so nice and detailed... "
                        a " I really do wish I can draw as great as you, [name]... "
                        a " I'm sure Miss Sasha will like what you've made... "
                        a " I'm just drawing a little teddy bear right now... And um... "
                        a " I don't want to disturb you further, so... "
                        a " I'll get back to work... "
                        hide abbiehappy at right with easeoutright
                        " Feeling happy due to Abbie's compliments, you decided to continue painting and made it look even better with all sorts of details. "
                    elif lanalv == 10 or lanalv >= 10:
                        show lananeutral at center with easeinleft
                        " You also saw Lana looking at your canvas, looking quite amazed at what you're painting. "
                        l " Woah! You've got some good painting skills there, [name]! "
                        l " A painting of Miss Sasha... She's gonna like that a lot! "
                        l " I wish I could paint as good as you, sigh... "
                        l " I won't bother you anymore though! I'll get back to working on my painting! "
                        hide lananeutral at left with easeoutleft
                        " Feeling happy due to Lana's compliments, you decided to continue painting and made it look even better with all sorts of details. "
                    else:
                        " You continued painting and painting, adding little details here and there to make it look even more beautiful. "
                elif alone == True:
                    " You continued painting and painting, adding little details here and there to make it look even more beautiful. "
                else:
                    return
                " Eventually, it was time for you to let the drawing be seen by the teacher. "
                mss " Alright class! Time is up! "
                mss " I'll be going around to see what you've all drawn, okay? "
                mss " Stop painting and put down your paintbrushes! "
                " You set down your paintbrush, and you waited for Miss Sasha to come by. "
                show sashaneutral at center with easeinleft
                " Miss sasha eventually came by to your seat, and you waited for her reaction. "
                hide sashaneutral at bottom
                show sashaconfused at center
                mss " Oh? This is... "
                hide sashaconfused at bottom
                show sashahappy at center
                mss " Awhhh!! You drew me!! "
                mss " And it's so nicely painted too, with all of the details and such... "
                mss " You're gonna be such a great artist in the future! "
                mss " For this, I'll give you a score of 60 for today! "
                mss " Good job on your first day, [name]! "
                " Told you it would get you extra points. "
                hide sashahappy at bottom
                show sashaneutral at center
                mss " Actually, do you mind if I took this with me? I wanna put this somewhere in my house... "
                " You told that you didn't mind, and you were glad that she enjoyed your painting. "
                mss " Yahhoo!! Thanks, [name]! "
                hide sashaneutral at right with easeoutright
                " Miss Sasha took the painting from you and placed it somewhere near her table, then she went on to check the other paintings. "
                play sound "audio/bellring.mp3"
                " She continued this until all paintings were graded. And until the bell rang. "
                " Class was dismissed, and you get to go home. Finally... "
                scene black with dissolve
                pause 2.0
                jump endday1
            " Something nature related ":
                " You decided to draw something nature related. Like a tree. "
                " You also decided to make it extra detailed, since you were feeling nice. "
                if claengbub == True:
                    if clairelv == 10 or clairelv >= 10:
                        " Claire takes a look at your drawing and gives you a sweet smile. "
                        " She looked back at what she was painting and continued to do her thing. "
                        " She must've liked what you've painted, judging by her look... "
                        " That just made you even more motivated to make this even more detailed. "
                        " And so, you kept painting. "
                    elif engellv == 10 or engellv >= 10:
                        " Engel takes a look at your painting and he seems impressed. "
                        " He gives you a thumbs up before he went back to painting his own thing. "
                        " He must've liked what you painted, judging by his look... "
                        " That just made you even more motivated to make this even more detailed. "
                        " And so, you kept painting. "
                    elif bubblelv == 10 or bubblelv >= 10:
                        " Bubble takes a look at your painting, and she seems to like it. "
                        " She gives a thumbs up to you before going back to what she was painting. "
                        " She must've liked what you've painted, judging by her look... "
                        " That just made you even more motivated to make this even more detailed. "
                        " And so, you kept painting. "
                    else:
                        " You just kept painting, occasionally adding little details here and there to make it 'pop' more. "
                elif abblana == True:
                    if abbielv == 10 or abbielv >= 10:
                        " Abbie takes a look at your painting, and seems amazed at what you're painting. "
                        " Though, the moment he sees that you've noticed him, he got embarrassed and continued to paint his own thing. "
                        " Abbie seems to really like what you've painted... "
                        " That just made you even more motivated to make this even more detailed. "
                        " And so, you kept painting. "
                    elif lanalv == 10 or lanalv >= 10:
                        " Lana takes a look at your painting, and she looks like she likes it. "
                        " Lana gives you a smile before she continued painting what she was painting. "
                        " Lana seems to really like what you've painted... "
                        " That just made you even more motivated to make this even more detailed. "
                        " And so, you kept painting. "
                    else:
                        " You just kept painting, occasionally adding little details here and there to make it 'pop' more. "
                elif alone:
                    " You just kept painting, occasionally adding little details here and there to make it 'pop' more. "
                else:
                    return
                " Eventually, it was time for you to let the drawing be seen by the teacher. "
                mss " Alright class! Time is up! "
                mss " I'll be going around to see what you've all drawn, okay? "
                mss " Stop painting and put down your paintbrushes! "
                " You set down your paintbrush, and you waited for Miss Sasha to come by. "
                show sashaneutral at center with easeinleft
                " Miss sasha eventually came by to your seat, and you waited for her reaction. "
                hide sashaneutral at bottom
                show sashaconfused at center
                mss " Oh? This is... "
                hide sashaconfused at bottom
                show sashaneutral at center
                mss " This is pretty nice, [name]! "
                mss " You're quite a good artist, actually! I love how you added little details! "
                mss " But, always remember to not focus yourself on the tiny little details too much. "
                mss " Adding more details can sidetrack you from the actual thing; "
                mss " Since you're trying to make the painting look better! "
                mss " I'll give you a 40/50 for today, good work! "
                hide sashaneutral at right with easeoutright
                " Miss Sasha then went on to check the other paintings. "
                play sound "audio/bellring.mp3"
                " She continued this until all paintings were graded. And until the bell rang. "
                " Class was dismissed, and you get to go home. Finally... "
                scene black with dissolve
                pause 2.0
                jump endday1
            " A weird little creature ":
                " You had no other ideas in mind, so you decided to paint a weird little creature. "
                " You're gonna name this little guy Bob when you're done. "
                if claengbub == True or abblana == True:
                    " Your classmates seemed a little perplexed when they saw what you were painting "
                    " But they quickly went back to focus on what they were drawing instead of looking at yours. "
                elif alone:
                    " This was gonna be your best painting yet. "
                    " You thought, as you painted and painted. "
                else:
                    return
                " Eventually, it was time for you to let the drawing be seen by the teacher. "
                mss " Alright class! Time is up! "
                mss " I'll be going around to see what you've all drawn, okay? "
                mss " Stop painting and put down your paintbrushes! "
                " You set down your paintbrush, and you waited for Miss Sasha to come by. "
                show sashaneutral at center with easeinleft
                " Miss sasha eventually came by to your seat, and you waited for her reaction. "
                hide sashaneutral at bottom
                show sashaconfused at center
                mss " Oh? This is... "
                " Now that you look at it, this looks like a half-assed drawing of Miss Sasha. Oh well. "
                hide sashaconfused at bottom
                show sashasad at center
                mss " ...Is this me? "
                " You had the womp womp face on you when she said that. "
                mss " No- No! It's nice! "
                mss " It's so nice...Oh... "
                mss " I've never looked better! "
                " Miss Sasha then picks up the canvas and she looks at it closely. "
                hide sashasad at bottom
                show sashaneutral at center
                mss " Oooh, where were you... Where were you when it was time for senior photos? "
                " You tell her that you don't think it looks good. "
                hide sashaneutral at bottom
                show sashahappy at center
                mss " It is FANTASTIC! " with vpunch
                mss " Oooh, my goood!! "
                mss " What's that? "
                " She says as she points at a little detail you made. "
                hide sashahappy at bottom
                show sashaneutral at center
                mss " Is that hyperpigmentation? "
                mss " Ehehhe... I'll give you a 30/50. "
                mss " You did great, [name]! I'm proud of you! "
                hide sashaneutral at right with easeoutright
                " Miss Sasha then went on to check the other paintings. "
                play sound "audio/bellring.mp3"
                " She continued this until all paintings were graded. And until the bell rang. "
                " Class was dismissed, and you get to go home. Finally... "
                scene black with dissolve
                pause 2.0
                jump endday1
    label endday1:
        scene paperschoolfront with dissolve
        " It's finally the end of the day. "
        " You see your classmates all go out the school, talking to their friends or just walking alone. "
        " It's time for you to go home as well. "
        " You quietly walk to your house, saying bye to a few classmates who were saying goodbye to you. "
        scene black with dissolve
        stop music fadeout 0.5
        pause 2.0
        play music "audio/home.mp3" fadein 0.5
        scene mcroom with dissolve
        " You plop onto your bed, exhausted due to the day you had in school. "
        " You've gone through a lot for this day, but you'll be going through more tomorrow. "
        " That's why you should sleep, to get energy to conquer tomorrow and other days! "
        " You quickly check your schools group chat to see if theres any assignments before you crash out and fall asleep. "
        scene black with dissolve
        stop music fadeout 0.5
        " Good night, [name]... "
        pause 2.0
        jump tuesday
